# ctr-seqrec-avazu
**Leakage-safe CTR/RecSys benchmark with sequential modeling on Avazu**  
**Proof (Kaggle, 2M rows, Tesla T4): Test AUC 0.72659 / LogLoss 0.40009**  
**Leakage-safe:** time-based split (no future leakage) + label-shuffle sanity  
**Reproducible:** `py -m src.run` → `reports/metrics.json`

## One-line
A leakage-safe CTR prediction pipeline with sequential user modeling, built for reproducible offline evaluation and interview-ready proof.

## Why this repo matters
- **Trustworthy evaluation** with **time-based split**
- **Sanity-checked learning** with **label-shuffle AUC ≈ 0.5**
- **Reproducible results** saved to **`reports/metrics.json`**
- **Portfolio-ready proof** from a full Kaggle run

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

## Output
This repo generates:

```text
reports/metrics.json
```

Example fields:
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
