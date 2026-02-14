import json
import os
import time
import numpy as np

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def auc_roc(y_true, y_score):
    # Fast AUC using rank statistics (no sklearn dependency)
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    order = np.argsort(y_score)
    y_true_sorted = y_true[order]
    n_pos = int(y_true_sorted.sum())
    n_neg = len(y_true_sorted) - n_pos
    if n_pos == 0 or n_neg == 0:
        return 0.5
    ranks = np.arange(1, len(y_true_sorted) + 1)
    sum_ranks_pos = ranks[y_true_sorted == 1].sum()
    auc = (sum_ranks_pos - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)
    return float(auc)

def logloss(y_true, y_prob, eps=1e-12):
    y_true = np.asarray(y_true)
    y_prob = np.clip(np.asarray(y_prob), eps, 1 - eps)
    return float(-(y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob)).mean())

def main():
    os.makedirs("reports", exist_ok=True)

    # Experiment knob
    SEQ_LEN = int(os.getenv("SEQ_LEN", "20"))
    SEED = int(os.getenv("SEED", "42"))

    rng = np.random.default_rng(SEED)

    # Synthetic sequential CTR-like data:
    # - each sample has a "sequence signal" (recent history length matters)
    # - longer seq_len captures more signal -> slightly better AUC/logloss (usually)
    n = 50000
    d = 60  # max history length in generator

    # latent user intent sequence
    hist = rng.normal(0, 1, size=(n, d))
    # true weights emphasize more recent events
    w = np.exp(-np.arange(d) / 12.0)[::-1]
    w = w / w.sum()

    # model only sees last SEQ_LEN events
    x = hist[:, -SEQ_LEN:]
    w_seen = w[-SEQ_LEN:]
    w_seen = w_seen / w_seen.sum()

    # true label uses full history (harder if SEQ_LEN small)
    logit_true = (hist * w).sum(axis=1) + rng.normal(0, 0.3, size=n)
    p_true = sigmoid(logit_true)
    y = (rng.random(n) < p_true).astype(int)

    # simple predictor: mean of seen weighted history -> probability
    logit_pred = (x * w_seen).sum(axis=1)
    p_pred = sigmoid(logit_pred)

    # label-shuffle sanity
    y_shuf = rng.permutation(y)
    auc_shuf = auc_roc(y_shuf, p_pred)

    t0 = time.time()
    auc = auc_roc(y, p_pred)
    ll = logloss(y, p_pred)
    runtime_sec = float(time.time() - t0)

    metrics = {
        "seq_len": SEQ_LEN,
        "test_auc": round(auc, 6),
        "test_logloss": round(ll, 6),
        "label_shuffle_auc": round(auc_shuf, 6),
        "runtime_sec": round(runtime_sec, 4),
        "note": "synthetic quick experiment to validate weekly loop; extend to Avazu/Kaggle later"
    }

    with open("reports/metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    print("DONE:", metrics)

if __name__ == "__main__":
    main()
