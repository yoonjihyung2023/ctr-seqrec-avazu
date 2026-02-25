# ctr-seqrec-avazu
**Leakage-safe CTR/RecSys with sequential modeling on Avazu — reproducible `reports/metrics.json` + FastAPI serving demo (via `ctr-api`)**

## One-line
Leakage-safe CTR/RecSys — time-based split (no future) + label-shuffle sanity + reproducible outputs (`reports/metrics.json`) + CI green.

## Proof (Kaggle full run)
Avazu (2M rows, Tesla T4): **Test AUC 0.72659 / LogLoss 0.40009**  
Kaggle Notebook: https://www.kaggle.com/code/yoonjihyung/notebook260213

## Leakage-safe eval (3 lines)
- **Time-based split**: train/val/test split by time (**no future leakage**)
- **No future leakage**: features/sequences are built using **past events only**
- **Label-shuffle sanity**: shuffle **train labels only** ⇒ AUC near **0.5** (random-like)

## Run in 3 lines (creates `reports/metrics.json`)
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```

- Local run is a smoke test (pipeline + sanity check). Full numbers are from Kaggle.

## Results

Final model (1-line): DIN-style feature interaction + Transformer-based sequence encoder (SASRec-inspired) for leakage-safe CTR prediction.
최종 모델(한 줄): DIN 기반 feature interaction + Transformer 기반 시퀀스 인코더로 leakage-safe CTR 예측

Metric	Main Model (Kaggle full run)	Label-Shuffle Sanity (shuffle train labels only)
Test AUC	0.72659	0.53265
Test LogLoss	0.40009	0.45085
Meaning	Strong predictive signal	Near-random (sanity check)

Reproducible: Results obtained from an end-to-end Kaggle run (2M rows, Tesla T4).
Leakage verification: Shuffling train labels only collapses performance toward near-random (AUC ~0.5).
(Small deviations like ~0.53 can occur due to sampling/training noise and early stopping.)

## Evidence: reports/metrics.json snapshot (Kaggle full run)
{
  "main": {
    "test_auc": 0.72659,
    "test_logloss": 0.40009,
    "best_val_logloss": 0.40076
  },
  "label_shuffle": {
    "test_auc": 0.53265,
    "test_logloss": 0.45085,
    "best_val_logloss": 0.46177
  },
  "data": {
    "rows_used": 2000000,
    "total_samples": 1693522,
    "click_rate_raw": 0.1616
  },
  "split": {
    "train": 1393474,
    "val": 174464,
    "test": 125584
  },
  "env": {
    "platform": "Kaggle",
    "gpu": "Tesla T4",
    "cuda": true
  }
}

## Quickstart
Kaggle Notebook (Recommended for full results)

Create a Kaggle Notebook

Attach dataset: avazu-ctr-prediction

Run the cells

Confirm output in console and reports/metrics.json

Kaggle Notebook: https://www.kaggle.com/code/yoonjihyung/notebook260213

Local (Smoke test only)

This local run is NOT the full Avazu training result.
It is a smoke test to prove the pipeline runs + leakage checks. AUC may be ~0.50.

Mac/Linux

pip install -r requirements.txt
python -m src.run
cat reports/metrics.json

Windows PowerShell (one-liner)

py -m pip install -r requirements.txt; py -m src.run; type .\reports\metrics.json

Expected output (local smoke test)

{"test_auc": 0.5, "test_logloss": 0.9339, "label_shuffle_auc": 0.5}
What This Does

Predicts click-through rate (CTR) using sequential user behavior modeling.

Why sequential? Clicks follow patterns:

Just viewed sports articles → more likely to click sports ads

Just browsed shopping → more likely to click shopping ads

Pipeline (high level)

Tokenize events (18 features per event, vocab: 9,664)

Build user sequences by device_id (~163K users)

Time-based split (train uses only past data)

Train hybrid DIN + Transformer (SASRec-inspired)

Verify with label-shuffle sanity check

Dataset: Avazu CTR (2M rows, ~1.69M samples, ~16.8% positive ratio)

Leakage Prevention
Time-based Split

Train (past) → Val → Test (future)

Split by target timestamp → no future data in training.

Label-shuffle Sanity Check

Shuffle train labels only (corrupt the signal)

Train the model on corrupted labels

Expected: AUC near 0.50 (random-like)

Observed (Kaggle): AUC 0.53265 (near-random)

If leakage existed, the model could still perform well despite shuffled labels.

Interview-ready Evidence

Leakage checklist: docs/leakage_checklist.md

Interview Q&A: docs/interview_qa.md

Serving demo: docs/serving_demo.md

FastAPI repo: ctr-api

Repro outputs: reports/metrics.json
 + reports/run_meta.json

Citation
@misc{ctr-seqrec-avazu,
  title={Leakage-safe CTR Prediction with Sequential Modeling},
  author={Jihyung Yoon},
  year={2026},
  publisher={GitHub},
  url={https://github.com/yoonjihyung2023/ctr-seqrec-avazu}
}
License

MIT License
