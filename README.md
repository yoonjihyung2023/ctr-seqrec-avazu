# ctr-seqrec-avazu

Leakage-safe CTR benchmark on Avazu with sequential modeling  
Proof: Kaggle 2M rows (Tesla T4) — **Test AUC 0.72659 / LogLoss 0.40009**  
Trustworthy + reproducible: time-based split + label-shuffle sanity + `reports/metrics.json`

## One-line
A reproducible CTR prediction pipeline for trustworthy offline evaluation without future leakage.

## Summary
- **Dataset:** Avazu CTR
- **Split logic:** time-based train / val / test split
- **Models:** CTR baseline + sequential modeling pipeline
- **Metrics:** AUC, LogLoss
- **Sanity checks:** label-shuffle sanity, reproducible metrics artifact

## Why this repo matters
- Prevents common offline evaluation mistakes with **time-based split**
- Checks false learning signals with **label-shuffle sanity**
- Produces reproducible outputs in **`reports/metrics.json`**
- Provides interview-ready benchmark proof from a full Kaggle run

## Quickstart
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
Windows PowerShell
py -m pip install -r requirements.txt
py -m src.run
type reports\metrics.json
Proof

Dataset: Avazu CTR

Run setting: Kaggle, 2M rows, Tesla T4

Test AUC: 0.72659

Test LogLoss: 0.40009

Leakage-safe evaluation

Time-based split: train / val / test are separated by time

No future leakage: features and sequences are built from past information only

Label-shuffle sanity: shuffled labels should collapse performance toward random-like behavior

Output

reports/metrics.json

Why recruiters/interviewers can trust this

Clear offline evaluation logic

Explicit leakage prevention mindset

Reproducible metric artifact

Benchmark result tied to a concrete run setting
