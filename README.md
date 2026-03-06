# ctr-seqrec-avazu
**Leakage-safe CTR benchmark on Avazu with sequential modeling**  
**Proof:** Kaggle 2M rows (Tesla T4) — **Test AUC 0.72659 / LogLoss 0.40009**  
**Trustworthy & reproducible:** time-based split + label-shuffle sanity + `py -m src.run` → `reports/metrics.json`

## One-line
A reproducible, leakage-safe CTR pipeline for trustworthy offline evaluation.

## Why this repo matters
- **Prevents common offline evaluation mistakes** with **time-based split**
- **Checks for false learning signals** with **label-shuffle sanity**
- **Produces reproducible metrics** in **`reports/metrics.json`**
- **Provides interview-ready proof** from a full Kaggle run

## Proof
- Dataset: **Avazu CTR**
- Run setting: **Kaggle, 2M rows, Tesla T4**
- **Test AUC:** `0.72659`
- **Test LogLoss:** `0.40009`

## Leakage-safe evaluation
- **Time-based split:** train / val / test are split by time
- **No future leakage:** features and sequences use past events only
- **Label-shuffle sanity:** shuffle train labels only → AUC should drop near random

## Quickstart
```bash
pip install -r requirements.txt
py -m src.run
type reports\metrics.json
```

Generates `reports/metrics.json` with validation and test metrics.

## Output
```text
reports/metrics.json
```

## Example fields
- `val_auc`
- `val_logloss`
- `test_auc`
- `test_logloss`

## What I built
- End-to-end pipeline: preprocess → train → evaluate
- Sequential CTR modeling with leakage-safe offline evaluation
- Reproducible experiment output for portfolio and interviews

## Related repo
For serving/demo deployment, see **[ctr-api](https://github.com/yoonjihyung2023/ctr-api)**.
