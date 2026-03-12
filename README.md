# ctr-seqrec-avazu

Leakage-safe CTR benchmark on Avazu with sequential modeling  
Proof: Kaggle 2M rows (Tesla T4) — AUC 0.72659 / LogLoss 0.40009  
Time-split + label-shuffle sanity + reproducible `reports/metrics.json`

## One-line
A reproducible CTR prediction pipeline for trustworthy offline evaluation without future leakage.

## Why this repo matters
- **Prevents common offline evaluation mistakes** with **time-based split**
- **Checks for false learning signals** with **label-shuffle sanity**
- **Produces reproducible metrics** in **`reports/metrics.json`**
- **Provides interview-ready proof** from a full Kaggle run

## Summary

| Item | Value |
|---|---|
| Dataset | Avazu CTR |
| Split logic | Time-based split |
| Modeling | Sequential user modeling |
| Run setting | Kaggle, 2M rows, Tesla T4 |
| Test AUC | 0.72659 |
| Test LogLoss | 0.40009 |
| Sanity check | Label-shuffle |
| Output artifact | `reports/metrics.json` |

## Leakage-safe evaluation
- **Time-based split:** train / val / test are split by time
- **No future leakage:** features and sequences are built from past information only
- **Label-shuffle sanity:** shuffled train labels should produce near-random performance

## Reproducible run
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
Main outputs

trained model artifact

evaluation metrics

reproducible reports/metrics.json

Why it is useful for hiring

This repository is built to show trustworthy CTR / RecSys experimentation:

not just model training

but also evaluation correctness

reproducibility

and proof that the result is not driven by leakage
