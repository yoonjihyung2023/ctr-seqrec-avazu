# ctr-seqrec-avazu
**Leakage-safe CTR/RecSys with sequential modeling on Avazu — outputs reports/metrics.json**  
**Proof (Kaggle, 2M rows, Tesla T4):** Test AUC **0.72659** / LogLoss **0.40009**  
**Leakage-safe:** time-based split (no future) + label-shuffle sanity (shuffle train labels only => AUC ~= 0.5) + CI green  
**FastAPI serving demo:** https://github.com/yoonjihyung2023/ctr-api

## TL;DR (One-line)
Leakage-safe CTR/RecSys — time-based split + label-shuffle sanity + CI green.  
Reproducible output: reports/metrics.json

## Results
| Metric | Main Model (Kaggle full run) | Label-Shuffle Sanity (shuffle train labels only) | Meaning |
|---|---:|---:|---|
| Test AUC | **0.72659** | 0.53265 | predictive signal vs near-random |
| Test LogLoss | **0.40009** | 0.45085 | lower is better |

> Note: Small deviations like ~0.53 can occur due to sampling/training noise and early stopping.

## Model (1-line)
DIN-style feature interaction + Transformer-based sequence encoder (SASRec-inspired) for leakage-safe CTR prediction.  
최종 모델(한 줄): DIN 기반 feature interaction + Transformer 기반 시퀀스 인코더로 leakage-safe CTR 예측

## Run (Local smoke test; generates reports/metrics.json)
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```

Local run is a **smoke test** (pipeline + leakage checks). **Full metrics are from Kaggle**.

### Windows PowerShell (one-liner)
```powershell
py -m pip install -r requirements.txt; py -m src.run; type .\reports\metrics.json
```

### Expected output (local smoke test)
Local smoke test may be near-random (AUC ~0.50) because it runs on a small subset / short training.  
Example:
```json
{"test_auc": 0.50, "test_logloss": 0.93, "label_shuffle_auc": 0.50}
```
## Kaggle full run (Recommended)
Kaggle Notebook: https://www.kaggle.com/code/yoonjihyung/notebook260213

## What this does
Predicts click-through rate (CTR) using sequential user behavior modeling.

Why sequential? Clicks follow patterns:
- Just viewed sports articles -> more likely to click sports ads
- Just browsed shopping -> more likely to click shopping ads

## Pipeline (high level)
- Tokenize events (18 features per event, vocab: 9,664)
- Build user sequences by device_id (~163K users)
- Time-based split (train uses only past data)
- Train hybrid DIN + Transformer (SASRec-inspired)
- Verify with label-shuffle sanity check
- Dataset: Avazu CTR (2M rows, ~1.69M samples, ~16.8% positive ratio)

## Leakage prevention
### Time-based split
Train (past) -> Val -> Test (future)  
Split by target timestamp -> no future data in training.

### Label-shuffle sanity check
Shuffle **train labels only** (corrupt the signal) -> model should collapse to near-random.  
Observed (Kaggle): AUC **0.53265** (near-random).  
If leakage existed, the model could still perform well despite shuffled labels.

## Evidence: reports/metrics.json snapshot (Kaggle full run)
```json
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
```
}

## Interview-ready evidence
- Leakage checklist: docs/leakage_checklist.md
- Interview QnA: docs/interview_qa.md
- Serving demo: docs/serving_demo.md
- FastAPI repo: https://github.com/yoonjihyung2023/ctr-api
- Repro outputs: reports/metrics.json + reports/run_meta.json

## Citation
bibtex
@misc{ctr-seqrec-avazu,
  title={Leakage-safe CTR Prediction with Sequential Modeling},
  author={Jihyung Yoon},
  year={2026},
  publisher={GitHub},
  url={https://github.com/yoonjihyung2023/ctr-seqrec-avazu}
}

## License
MIT License


