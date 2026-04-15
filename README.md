# ctr-seqrec-avazu

Leakage-safe CTR/RecSys benchmark on Avazu with sequential modeling.

**Proof:** Kaggle Avazu 2M rows (Tesla T4) — **Test AUC 0.72659 / LogLoss 0.40009**

## Why this repo matters

- **Leakage-safe evaluation**: time-based split to avoid future information leakage
- **Sanity check included**: label-shuffle test should collapse performance toward random
- **Reproducible output**: run the pipeline and save metrics to `reports/metrics.json`
- **Recruiter-friendly proof**: one repo showing data split, training, evaluation, and metrics

## What is implemented

- CTR prediction pipeline for Avazu-style tabular data
- Sequential/recommender-style modeling workflow
- Time-based train/validation/test split
- Offline evaluation with AUC and LogLoss
- Reproducible report artifact in `reports/metrics.json`

## Main result

| Run | Dataset / Setup | Metric |
|---|---|---|
| Full run | Avazu 2M rows, Tesla T4 | **AUC 0.72659 / LogLoss 0.40009** |

## Trustworthiness

This repository is designed to make the result easier to trust.

1. **Time-based split**
   - Train on the past, evaluate on the future.
   - Prevents unrealistic leakage from random shuffling across time.

2. **Label-shuffle sanity check**
   - If labels are shuffled, performance should drop toward random.
   - This helps verify the pipeline is not accidentally leaking target information.

3. **Reproducible metrics file**
   - Final outputs are written to `reports/metrics.json`.
   - This makes reruns and verification easier.

## Quickstart

```bash
py -m src.run
type reports\metrics.json

Or:

python -m src.run
cat reports/metrics.json
Expected output

The exact value depends on environment and run mode, but the pipeline should produce a metrics file like:

{
  "auc": 0.72659,
  "logloss": 0.40009
}
Repository structure
src/                # training / evaluation pipeline
reports/            # output metrics.json
README.md
Who this is for

This repo is intended as portfolio evidence for roles such as:

ML Engineer
Applied ML Engineer
Ads / CTR Prediction Engineer
Recommender Systems Engineer
Related project
ctr-api
: FastAPI + Docker serving demo for model inference