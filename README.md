# ctr-seqrec-avazu
Reproducible CTR prediction & sequential recommendation experiments (Avazu-style)

> Goal: Build an end-to-end, **reproducible** CTR pipeline (data → split → train → evaluate → report)
> with **leakage-safe** preprocessing and sequence-aware models.

## What’s inside (in plain words)
- **Problem**: predict click-through rate (CTR) from user behavior logs
- **Focus**: show how **sequential signals** (user’s recent actions) can improve prediction
- **Key point**: results must be **trustworthy** (no data leakage, correct split, repeatable runs)

## Models
- Baselines:
  - Logistic Regression / LightGBM (optional)
  - Simple MLP (optional)
- Deep CTR / RecSys:
  - DIN (attention over user behavior)
  - SASRec (Transformer-based sequential model)
  - BERT4Rec-style (masked sequence modeling, adapted for CTR)

> Note: I intentionally prioritize **reproducibility and correct evaluation** over “too-perfect” scores.

## Metrics
- AUC-ROC
- Log Loss

## Quickstart
### 1) Setup
```bash
git clone https://github.com/yoonjihyung2023/ctr-seqrec-avazu.git
cd ctr-seqrec-avazu
python -m venv .venv
source .venv/bin/activate  # (Windows) .venv\Scripts\activate
pip install -r requirements.txt
