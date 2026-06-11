# ctr-seqrec-avazu

End-to-end CTR system:
training ??serving ??logging ??retraining

Simulates real production workflow (no data leakage, time-based split)

Ready for integration into online ad/recommendation systems

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

```
powershell
pip install -r requirements.txt
python -m src.run
type reports\metrics.json
```

For macOS/Linux:

```
bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```
## Portfolio Proof

This repo demonstrates the **training / offline evaluation** part of my Ads/RecSys portfolio.

- Dataset: Avazu CTR prediction
- Result: AUC 0.72659 / LogLoss 0.40009
- Validation: leakage-safe time split
- Sanity check: label-shuffle test
- Reproducibility: `reports/metrics.json`

## Suggested Screenshot

Add a screenshot showing `reports/metrics.json` or terminal output after running:

- `python -m src.run`
- `cat reports/metrics.json`

Recommended path:

- `docs/metrics-proof.png`

Then include it in this README later:

- `![Metrics proof](docs/metrics-proof.png)`nn## Quickstart

### macOS / Linux

```bash
pip install -r requirements.txt
python -m src.run
cat metrics_kaggle_avazu_2m.json
Windows PowerShell
pip install -r requirements.txt
py -m src.run
type metrics_kaggle_avazu_2m.jsonnn
Model Comparison
Model    Main Idea    Strengths    Limitations    Role in This Project
SASRec / SAS4CTR    Unidirectional self-attention for sequential user behavior    Fast, simple, effective for recent behavior patterns    Weaker at capturing bidirectional context    Main sequential CTR baseline
BERT4Rec / BERT4CTR    Bidirectional Transformer with masked item modeling    Stronger long-term representation and context modeling    Heavier training cost and higher compute demand    Main comparison model
DIN    Attention over user behavior history for CTR prediction    Strong personalization and interpretable user-interest weighting    Less focused on sequence order than Transformer models    CTR-oriented reference baseline
DeepFM    Combines factorization machines and deep neural networks    Strong general CTR baseline for sparse features    Does not explicitly model behavior sequence    Non-sequential CTR baseline

This project focuses on comparing sequential recommendation models for CTR prediction, especially the trade-off between accuracy, personalization, and computational efficiency.nn## Quickstart

### macOS / Linux

```bash
pip install -r requirements.txt
python -m src.run
cat metrics_kaggle_avazu_2m.json
Windows PowerShell
pip install -r requirements.txt
py -m src.run
type metrics_kaggle_avazu_2m.jsonnn
Model Comparison
Model    Main Idea    Strengths    Limitations    Role in This Project
SASRec / SAS4CTR    Unidirectional self-attention for sequential user behavior    Fast, simple, effective for recent behavior patterns    Weaker at capturing bidirectional context    Main sequential CTR baseline
BERT4Rec / BERT4CTR    Bidirectional Transformer with masked item modeling    Stronger long-term representation and context modeling    Heavier training cost and higher compute demand    Main comparison model
DIN    Attention over user behavior history for CTR prediction    Strong personalization and interpretable user-interest weighting    Less focused on sequence order than Transformer models    CTR-oriented reference baseline
DeepFM    Combines factorization machines and deep neural networks    Strong general CTR baseline for sparse features    Does not explicitly model behavior sequence    Non-sequential CTR baseline

This project focuses on comparing sequential recommendation models for CTR prediction, especially the trade-off between accuracy, personalization, and computational efficiency.

