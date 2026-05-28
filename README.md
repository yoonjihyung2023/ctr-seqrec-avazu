# ctr-seqrec-avazu

## Trust / Reproducibility Check

This repo separates the main Kaggle Avazu result from local smoke/synthetic checks to avoid metric confusion.

- **Main Kaggle Avazu 2M run:** `reports/metrics_kaggle_avazu_2m.json`
  - AUC: **0.72659**
  - LogLoss: **0.40009**
  - Split: leakage-safe time-based split
- **Local smoke/synthetic check:** `reports/metrics_local_synthetic.json`
- **Compatibility pointer:** `reports/metrics.json`

The Kaggle full-run metric and local smoke metric are intentionally stored separately.


Ads / RecSys CTR prediction benchmark on the Avazu dataset.

**Key result:** AUC **0.72659** / LogLoss **0.40009** on Avazu 2M rows.

This project focuses on evaluation correctness and reproducibility:

- Leakage-safe time-based split
- Label-shuffle sanity check
- Reproducible run command
- Main Kaggle metrics saved to `reports/metrics_kaggle_avazu_2m.json`; local smoke metrics kept in `reports/metrics.json`

## Quickstart

```
bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics_kaggle_avazu_2m.json
```

For Windows PowerShell:

```
powershell
pip install -r requirements.txt
py -m src.run
type reports\metrics_kaggle_avazu_2m.json
```

## Result

| Dataset | Rows | AUC | LogLoss | Validation |
|---|---:|---:|---:|---|
| Avazu | 2M | 0.72659 | 0.40009 | Leakage-safe time split |

## Portfolio Proof

This repository demonstrates practical ML engineering skills for CTR / recommendation systems:

- Built an end-to-end CTR prediction pipeline
- Used time-based validation to avoid future leakage
- Ran a label-shuffle sanity check to verify the evaluation setup
- Saved reproducible metrics in `reports/metrics.json`
- Packaged the project so it can be rerun with a single module command

## Why this matters

CTR prediction and recommendation problems are sensitive to data leakage.
A random split can make offline metrics look better than real-world performance.

This project uses a time-based split and sanity checks so the reported result is more trustworthy.

## Tech Stack

- Python
- PyTorch
- pandas / scikit-learn
- Reproducible CLI pipeline

## Related Project

Serving demo:

- [ctr-api](https://github.com/yoonjihyung2023/ctr-api) — FastAPI + Docker inference API



