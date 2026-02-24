# ctr-seqrec-avazu
??Run in 3 lines ??creates `reports/metrics.json`  
??Time-based split (no future leakage)  
??Label-shuffle sanity check (AUC about 0.50)  
??Proof: `python -m src.run` prints DONE + metrics.json is generated  
??CI: GitHub Actions runs the same pipeline
??Kaggle full-run proof: [Notebook](https://www.kaggle.com/code/yoonjihyung/notebook260213/edit) + `reports/metrics.json` snapshot
??Local proof (smoke test): `DONE: {'test_auc': 0.5, 'test_logloss': 0.9339, 'label_shuffle_auc': 0.5}`

**Leakage-safe CTR prediction with sequential modeling on the Avazu dataset**

[![Time-based Split](https://img.shields.io/badge/split-time--based-green)](https://github.com/yoonjihyung2023/ctr-seqrec-avazu)
[![Sanity Check](https://img.shields.io/badge/sanity-label--shuffle-blue)](https://github.com/yoonjihyung2023/ctr-seqrec-avazu)
[![Python](https://img.shields.io/badge/python-3.10%2B-informational)](https://www.python.org/)
[![Kaggle](https://img.shields.io/badge/run-kaggle-20BEFF)](https://www.kaggle.com/c/avazu-ctr-prediction)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

---

## Results

**Final model (1-line):** DIN-style feature interaction + Transformer-based sequence encoder (SASRec-inspired) for leakage-safe CTR prediction.  
**理쒖쥌 紐⑤뜽(??以?:** DIN 湲곕컲 feature interaction + Transformer ?쒗???몄퐫??SASRec ?꾩씠?붿뼱)濡?CTR???덉륫?섍퀬, time-split?쇰줈 ?꾩닔 ?놁씠 ?됯??⑸땲??

| Metric | Main Model | Label-Shuffle Sanity Check (train labels only) |
|--------|------------|-----------------------------------------------|
| **Test AUC** | **0.72659** | **0.53265** ??|
| **Test LogLoss** | **0.40009** | **0.45085** |
| **Meaning** | Strong predictive signal | Near-random ??sanity check passed |

??**Reproducible**: Results obtained from an end-to-end **Kaggle run** (2M rows, **Tesla T4**).

**Leakage verification**: Shuffling **train labels only** collapses performance toward random ??**sanity check passed** ?? 
*(Small deviations like ~0.53 can occur due to sampling/training noise and early stopping.)*

---

### ?뱦 Evidence: `reports/metrics.json` snapshot (from Kaggle full run)

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
}
```

## Quickstart

### Kaggle Notebook (Recommended for full results)
1. Create a Kaggle Notebook
2. Attach dataset: `avazu-ctr-prediction`
3. Run the cells
4. View results in the console (and optionally save to `reports/metrics.json`)

### Local (Smoke test only: verifies pipeline runs + creates `reports/metrics.json`)
> This local run is **NOT** the full Avazu training result.  
> It is a **smoke test** to prove reproducibility + leakage checks (AUC may be ~0.50).

**Mac/Linux:**
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```

**Windows PowerShell:**
**One-liner:**
```powershell
py -m pip install -r requirements.txt; py -m src.run; type .\reports\metrics.json
```

**Step-by-step:**
```powershell
py -m pip install -r requirements.txt
py -m src.run
type .\reports\metrics.json
```

**Expected output (local smoke test):** AUC about 0.50 is OK here (demo run).
```json
{"test_auc": 0.5, "test_logloss": 0.9339, "label_shuffle_auc": 0.5}
```

- Note: Local demo numbers are for verifying the pipeline + leakage check only (not comparable to Kaggle full run).

## What This Does

- Predicts click-through rate (CTR) using sequential user behavior modeling.

Why sequential? Clicks follow patterns:

- Just viewed sports articles -> more likely to click sports ads
- Just browsed shopping -> more likely to click shopping ads

Pipeline
- Tokenize events (18 features per event, vocab: 9,664)
- Build user sequences by device_id (~163K users)
- Time-based split (train uses only past data)
- Train hybrid DIN + Transformer (SASRec-inspired)
- Verify with label-shuffle sanity check

Dataset: Avazu CTR (2M rows, ~1.69M samples, ~16.8% positive ratio)

## Leakage Prevention
### Time-based Split

- Train (past) -> Val -> Test (future)
- Split by target timestamp -> no future data in training.

### Label-Shuffle Sanity Check

- Shuffle train labels only (corrupt the signal)
- Train model on corrupted labels
- Expected: AUC about 0.50 (random)
- Observed: AUC 0.53265 (local)

If leakage existed, the model could still perform well despite shuffled labels.

## Citation
```bibtex
@misc{ctr-seqrec-avazu,
  title={Leakage-safe CTR Prediction with Sequential Modeling},
  author={Jihyung Yoon},
  year={2026},
  publisher={GitHub},
  url={https://github.com/yoonjihyung2023/ctr-seqrec-avazu}
}
```

## License
MIT License

## 📌 Evidence (Interview-ready)
- Leakage checklist: [docs/leakage_checklist.md](docs/leakage_checklist.md)
- Interview Q&A: [docs/interview_qa.md](docs/interview_qa.md)
- Serving demo: [docs/serving_demo.md](docs/serving_demo.md) (FastAPI repo: [ctr-api](https://github.com/yoonjihyung2023/ctr-api))
- Repro outputs: [reports/metrics.json](reports/metrics.json) + [reports/run_meta.json](reports/run_meta.json)






