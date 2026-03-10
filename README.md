# ctr-seqrec-avazu

[![CI](https://github.com/yoonjihyung2023/ctr-seqrec-avazu/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/yoonjihyung2023/ctr-seqrec-avazu/actions/workflows/ci.yml)

**Leakage-safe CTR benchmark on Avazu with sequential modeling**  
**Proof:** Kaggle 2M rows (Tesla T4) — **Test AUC 0.72659 / LogLoss 0.40009**  
**Trustworthy & reproducible:** time-based split + label-shuffle sanity + `reports/metrics.json`

## One-line
A reproducible CTR prediction pipeline for trustworthy offline evaluation without future leakage.

## Why this repo matters
- **Time-based split** for leakage-safe offline evaluation
- **Label-shuffle sanity** to check false learning signals
- **Reproducible output** saved to **`reports/metrics.json`**
- **Interview-ready proof** from a full Kaggle run

## Proof
- Dataset: **Avazu CTR**
- Run setting: **Kaggle, 2M rows, Tesla T4**
- **Test AUC:** `0.72659`
- **Test LogLoss:** `0.40009`

## Quickstart
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```

## Leakage-safe evaluation
- **Time-based split:** train / validation / test are split by time
- **Past-only features:** no future information is used to build inputs
- **Label-shuffle sanity:** shuffled-train-label run should drop toward random-like performance

## Outputs
- Main artifact: **`reports/metrics.json`**

## Project goal
This repo is built to show trustworthy CTR/RecSys evaluation with sequential user modeling, focusing on leakage prevention, reproducibility, and clear proof of results.

