# ctr-seqrec-avazu

Leakage-safe CTR/RecSys project with time-based evaluation, label-shuffle sanity checks, and reproducible metrics.

## TL;DR

This repo demonstrates a **leakage-safe CTR / sequential recommendation pipeline** on the **Avazu** dataset.

It is designed to answer three recruiter-facing questions quickly:

1. **What problem is being solved?**  
   Predict whether a user will click an ad.

2. **Why is this hard?**  
   CTR pipelines are vulnerable to **data leakage**, unrealistic splits, and inflated metrics.

3. **How was it validated?**  
   With **time-based evaluation**, **label-shuffle sanity checks**, and saved metrics in `reports/metrics.json`.

## Key result

- **Test AUC:** 0.72659
- **Test LogLoss:** 0.40009

## Why this repo matters

- **Leakage-safe evaluation** with time-based split
- **Sanity checks** to detect suspicious performance
- **Reproducible outputs** saved to `reports/metrics.json`
- **Clear benchmark framing** for CTR / RecSys portfolio use

## Quickstart

```bash
pip install -r requirements.txt
python src/train.py
type reports\metrics.json

