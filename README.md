# ctr-seqrec-avazu

Leakage-safe CTR/RecSys project with time-based evaluation, label-shuffle sanity checks, and reproducible metrics.

Built on the Avazu CTR dataset to demonstrate trustworthy offline validation for click-through rate prediction.

**Test AUC:** 0.72659 | **LogLoss:** 0.40009  
**Validation:** time-based split, no future leakage, label-shuffle sanity check  
**Reproducibility:** results saved to `reports/metrics.json`

## Quickstart
```bash
pip install -r requirements.txt
python src/train.py
type reports\metrics.json
```

## TL;DR
Leakage-safe CTR/RecSys on Avazu with trustworthy offline evaluation and reproducible results.
