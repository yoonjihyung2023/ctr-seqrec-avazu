"""Chronological Avazu CTR benchmark. No click labels are used as features."""
import argparse
import hashlib
import json
import platform
import random
import time
from importlib.metadata import version
from pathlib import Path

import joblib
import lightgbm as lgb
import numpy as np
import pandas as pd
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.preprocessing import OneHotEncoder
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

HISTORY_FIELDS = ("site_id", "app_id", "device_model")


def split_hours(hours):
    unique = np.unique(hours)
    if len(unique) < 3:
        raise ValueError("At least three distinct event hours are required.")
    # Approximate 70/15/15 by event count, never splitting an hour.
    counts = np.searchsorted(hours, unique, side="right")
    a = int(np.clip(np.searchsorted(counts, len(hours)*.70), 0, len(unique)-3))
    b = int(np.clip(np.searchsorted(counts, len(hours)*.85), a+1, len(unique)-2))
    return int(counts[a]), int(counts[b])


def encode(frame, train_end, max_vocab):
    arrays, vocab = [], {}
    for name in frame:
        values = frame[name].astype("string").fillna("__MISSING__")
        frequent = values.iloc[:train_end].value_counts()
        keys = frequent[frequent >= 2].index[:max_vocab]
        mapping = {str(key): i+1 for i, key in enumerate(keys)}
        arrays.append(values.map(mapping).fillna(0).to_numpy(dtype=np.int32))
        vocab[name] = mapping
    return np.column_stack(arrays), vocab


def previous_indices(devices, hours, length):
    """Return row IDs of strictly earlier-hour events, -1 for padding."""
    codes, _ = pd.factorize(devices, sort=False)
    row = np.arange(len(hours), dtype=np.int32)
    order = np.lexsort((row, hours, codes))
    d, h = codes[order], hours[order]
    new_device = np.r_[True, d[1:] != d[:-1]]
    new_hour = new_device | np.r_[True, h[1:] != h[:-1]]
    device_start = np.maximum.accumulate(np.where(new_device, row, 0))
    hour_start = np.maximum.accumulate(np.where(new_hour, row, 0))
    start = np.maximum(device_start, hour_start-length)
    result = np.full((len(row), length), -1, dtype=np.int32)
    for j in range(length):
        positions = start+j
        valid = (positions < hour_start) & (d != -1)
        result[order[valid], j] = order[positions[valid]]
    return result


class SeqCTR(nn.Module):
    def __init__(self, sizes, hist_cols, length, dim=32):
        super().__init__()
        self.register_buffer("offsets", torch.tensor(np.cumsum([0]+sizes[:-1])))
        self.register_buffer("hist_cols", torch.tensor(hist_cols))
        self.embedding = nn.Embedding(sum(sizes), dim)
        self.position = nn.Embedding(length, dim)
        self.current = nn.Sequential(nn.Linear(len(sizes)*dim, dim*2), nn.ReLU(),
                                     nn.Linear(dim*2, dim))
        layer = nn.TransformerEncoderLayer(dim, 4, dim*2, dropout=.1, batch_first=True)
        self.encoder = nn.TransformerEncoder(layer, 1, enable_nested_tensor=False)
        self.attention = nn.Sequential(nn.Linear(dim*4, dim), nn.ReLU(), nn.Linear(dim, 1))
        self.head = nn.Sequential(nn.Linear(dim*3, dim*2), nn.ReLU(),
                                  nn.Dropout(.1), nn.Linear(dim*2, 1))

    def forward(self, x, hist, valid):
        q = self.current(self.embedding(x+self.offsets).flatten(1))
        seq = self.embedding(hist+self.offsets[self.hist_cols]).mean(dim=2)
        seq = seq + self.position(torch.arange(seq.shape[1], device=x.device))
        seq = seq.masked_fill(~valid.unsqueeze(-1), 0)
        safe = valid.clone()
        safe[:, 0] = True
        causal = torch.ones(seq.shape[1], seq.shape[1], device=x.device,
                            dtype=torch.bool).triu(1)
        seq = self.encoder(seq, mask=causal, src_key_padding_mask=~safe)
        seq = seq.masked_fill(~valid.unsqueeze(-1), 0)
        expanded = q.unsqueeze(1).expand_as(seq)
        score = self.attention(torch.cat((expanded, seq, expanded-seq, expanded*seq), -1))
        weights = score.squeeze(-1).masked_fill(~safe, -1e9).softmax(1)
        pooled = (seq*weights.unsqueeze(-1)).sum(1)
        idx = (valid.sum(1)-1).clamp_min(0)
        last = seq[torch.arange(len(x), device=x.device), idx]
        return self.head(torch.cat((q, pooled, last), 1)).squeeze(-1)


def metrics(labels, scores):
    if np.unique(labels).size != 2:
        raise ValueError("Each evaluation split must contain both classes.")
    if not np.isfinite(scores).all():
        raise ValueError("Non-finite prediction.")
    return {"auc": float(roc_auc_score(labels, scores)),
            "logloss": float(log_loss(labels, scores, labels=[0, 1]))}


def batches(x, y, history, start, end, batch_size, shuffle, seed):
    ids = torch.arange(start, end)
    return DataLoader(TensorDataset(ids), batch_size=batch_size, shuffle=shuffle,
                      generator=torch.Generator().manual_seed(seed))


def pack(ids, x, y, history, hist_cols, device):
    i = ids.numpy()
    idx = history[i]
    valid = idx >= 0
    h = x[np.maximum(idx, 0)[:, :, None], np.array(hist_cols)[None, None, :]]
    h[~valid] = 0
    return (torch.as_tensor(x[i], dtype=torch.long, device=device),
            torch.as_tensor(h, dtype=torch.long, device=device),
            torch.as_tensor(valid, device=device),
            torch.as_tensor(y[i], dtype=torch.float32, device=device))


def predict(model, x, y, history, hist_cols, start, end, args, device):
    model.eval()
    out = []
    with torch.inference_mode():
        for (ids,) in batches(x, y, history, start, end, args.batch_size, False, args.seed):
            a,b,c,_ = pack(ids, x, y, history, hist_cols, device)
            out.append(model(a,b,c).sigmoid().cpu().numpy())
    return np.concatenate(out)


def train_seq(x,y,history,hist_cols,sizes,a,b,args,device,out):
    model = SeqCTR(sizes,hist_cols,args.history_length).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=.001)
    criterion = nn.BCEWithLogitsLoss()
    best_loss, best_state, epochs = float("inf"), None, []
    for epoch in range(args.epochs):
        model.train()
        for (ids,) in batches(x,y,history,0,a,args.batch_size,True,args.seed+epoch):
            c,h,mask,target = pack(ids,x,y,history,hist_cols,device)
            optimizer.zero_grad(set_to_none=True)
            loss = criterion(model(c,h,mask),target)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
        validation = metrics(y[a:b],predict(model,x,y,history,hist_cols,a,b,args,device))
        epochs.append({"epoch":epoch+1, **validation})
        print("sequence validation", epochs[-1], flush=True)
        if validation["logloss"] < best_loss:
            best_loss = validation["logloss"]
            best_state = {k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
    model.load_state_dict(best_state)
    torch.save({"state_dict":best_state,"sizes":sizes,"hist_cols":hist_cols,
                "history_length":args.history_length},out/"sequence.pt")
    return predict(model,x,y,history,hist_cols,b,len(y),args,device), epochs


def main(args):
    if min(args.rows,args.epochs,args.batch_size,args.history_length,args.max_vocab,args.threads) < 1:
        raise ValueError("Numeric arguments must be positive.")
    random.seed(args.seed); np.random.seed(args.seed); torch.manual_seed(args.seed)
    torch.set_num_threads(args.threads)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    out = Path(args.output)
    # Never overwrite previous experimental evidence.
    out.mkdir(parents=True,exist_ok=False)
    started = time.time()
    source = pd.read_csv(args.data, nrows=args.rows, dtype=str)
    required = {"id","click","hour","device_id",*HISTORY_FIELDS}
    if not required.issubset(source):
        raise ValueError(f"Missing columns: {required-set(source)}")
    if source["hour"].isna().any():
        raise ValueError("Event hours must be nonmissing.")
    if source["id"].isna().any() or source["id"].duplicated().any():
        raise ValueError("Event IDs must be nonmissing and unique.")
    if not source["click"].isin(["0","1"]).all():
        raise ValueError("Click labels must be 0/1.")
    source["hour"] = pd.to_datetime(source["hour"],format="%y%m%d%H",errors="raise")
    source = source.sort_values("hour",kind="stable").reset_index(drop=True)
    hours = source["hour"].to_numpy(dtype="datetime64[ns]").astype(np.int64)
    a,b = split_hours(hours)
    y = source["click"].astype(np.int8).to_numpy()
    for part in (y[:a],y[a:b],y[b:]):
        if np.unique(part).size != 2:
            raise ValueError("Each split must contain both classes.")
    devices = source["device_id"].copy()
    history = previous_indices(devices,hours,args.history_length)
    assert hours[a-1] < hours[a] and hours[b-1] < hours[b]
    for j in range(args.history_length):
        valid = history[:,j]>=0
        assert np.all(hours[history[valid,j]] < hours[valid])
    frame = source.drop(columns=["id","click","hour"])
    frame["event_hour"] = source["hour"].dt.hour.astype(str)
    frame["weekday"] = source["hour"].dt.dayofweek.astype(str)
    frame["history_count"] = (history>=0).sum(1).astype(str)
    x,vocab = encode(frame,a,args.max_vocab)
    columns = list(frame.columns)
    hist_cols = [columns.index(c) for c in HISTORY_FIELDS]
    sizes = [len(vocab[c])+1 for c in columns]
    (out/"vocab.json").write_text(json.dumps(vocab),encoding="utf-8")
    fingerprint = hashlib.sha256(pd.util.hash_pandas_object(source,index=False).values.tobytes()).hexdigest()
    test_ids = source["id"].iloc[b:].to_numpy()
    del source,frame,devices
    results = []
    def record(name,pred,seconds):
        result = {"model":name, **metrics(y[b:],pred),"seconds":round(seconds,2)}
        results.append(result)
        print(result,flush=True)
    pred_table = {"id":test_ids,"click":y[b:]}
    t = time.time()
    encoder = OneHotEncoder(handle_unknown="ignore",dtype=np.float32)
    train = encoder.fit_transform(x[:a])
    lr = LogisticRegression(solver="saga",max_iter=150,random_state=args.seed)
    lr.fit(train,y[:a])
    del train
    pred = lr.predict_proba(encoder.transform(x[b:]))[:,1]
    record("Logistic Regression",pred,time.time()-t)
    results[-1]["iterations"] = int(lr.n_iter_.max())
    results[-1]["converged_before_limit"] = bool(lr.n_iter_.max() < lr.max_iter)
    pred_table["lr"] = pred
    joblib.dump((encoder,lr),out/"lr.joblib")
    del lr,encoder
    t = time.time()
    tree = lgb.LGBMClassifier(n_estimators=300,learning_rate=.05,num_leaves=31,
                              random_state=args.seed,n_jobs=args.threads,verbosity=-1,
                              deterministic=True,force_col_wise=True)
    tree.fit(x[:a],y[:a],categorical_feature=list(range(x.shape[1])),
             eval_set=[(x[a:b],y[a:b])],eval_metric="binary_logloss",
             callbacks=[lgb.early_stopping(20,verbose=False)])
    pred = tree.booster_.predict(x[b:])
    record("LightGBM",pred,time.time()-t)
    pred_table["lightgbm"] = pred
    tree.booster_.save_model(str(out/"lightgbm.txt"))
    t = time.time()
    pred,epochs = train_seq(x,y,history,hist_cols,sizes,a,b,args,device,out)
    record("SASRec-DIN-inspired",pred,time.time()-t)
    pred_table["sequence"] = pred
    pd.DataFrame(pred_table).to_csv(out/"test_predictions.csv.gz",index=False)
    report = {"dataset_rows":len(y),"sample_hash":fingerprint,
              "splits":{"train":a,"validation":b-a,"test":len(y)-b,
                        "validation_start":str(pd.Timestamp(hours[a])),
                        "test_start":str(pd.Timestamp(hours[b]))},
              "seed":args.seed,"device":str(device),"columns":columns,
              "unknown_rates_test":dict(zip(columns,(x[b:]==0).mean(0).tolist())),
              "arguments":vars(args),"versions":{n:version(n) for n in
                  ["numpy","pandas","scikit-learn","lightgbm","torch"]},
              "python":platform.python_version(),"sequence_validation":epochs,
              "results":results,"total_seconds":round(time.time()-started,2)}
    (out/"benchmark.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    lines=["# CTR chronological benchmark","",
           f"Rows: {len(y):,}; train/validation/test: {a:,}/{b-a:,}/{len(y)-b:,}.",
           f"Seed: {args.seed}; validation starts {report['splits']['validation_start']}; test starts {report['splits']['test_start']}.",
           "", "| Model | ROC AUC | LogLoss | Fit + evaluation (s) |",
           "|---|---:|---:|---:|"]
    lines += [f"| {r['model']} | {r['auc']:.6f} | {r['logloss']:.6f} | {r['seconds']:.2f} |" for r in results]
    lines += ["","Train-only categorical mapping; unknown/rare values use index 0.",
              "Histories use strictly earlier hours; within older hours, file order is a deterministic proxy.",
              "All events are scored, including cold-start events. Device ID is a proxy, not verified user identity.",
              "Baselines use current features and past event count; sequential model also uses past event categories.",
              "Validation selects tree iteration and sequence checkpoint; test is for final evaluation.",
              "Single seed; not a direct reproduction of the legacy notebook."]
    (out/"benchmark.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(out/"benchmark.md")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data",required=True)
    parser.add_argument("--output",required=True)
    parser.add_argument("--rows",type=int,default=2_000_000)
    parser.add_argument("--epochs",type=int,default=3)
    parser.add_argument("--batch-size",type=int,default=512)
    parser.add_argument("--history-length",type=int,default=20)
    parser.add_argument("--max-vocab",type=int,default=50_000)
    parser.add_argument("--seed",type=int,default=42)
    parser.add_argument("--threads",type=int,default=4)
    main(parser.parse_args())
