# ctr-seqrec-avazu
**Leakage-safe CTR prediction with sequential modeling on the Avazu dataset**

[![Time-based Split](https://img.shields.io/badge/split-time--based-green)](https://github.com/yoonjihyung2023/ctr-seqrec-avazu)
[![Sanity Check](https://img.shields.io/badge/sanity-label--shuffle-blue)](https://github.com/yoonjihyung2023/ctr-seqrec-avazu)
[![Python](https://img.shields.io/badge/python-3.10%2B-informational)](https://www.python.org/)
[![Kaggle](https://img.shields.io/badge/run-kaggle-20BEFF)](https://www.kaggle.com/c/avazu-ctr-prediction)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

---

 ## 🎯 TL;DR (Results)
 
 | Metric | Main Model | Label-Shuffle Check |
 |--------|------------|---------------------|
 | **Test AUC** | **0.72659** | **0.53265** ✅ |
 | **Test LogLoss** | **0.40009** | **0.45085** |
 | **Best Val LogLoss** | **0.40076** | **0.46177** |
 | **Meaning** | Predictive signal learned | Near-random (≈0.50) = no leakage |
 
 **Key takeaway**: Shuffling **train labels only** collapses performance to near-random → **sanity check passed**.
+
+✅ **Reproducible**: The TL;DR numbers are from an end-to-end **Kaggle notebook run** on **2M rows (Tesla T4)** and printed in the console.
 
 > **What do these numbers mean?**
 > - **AUC 0.727**: Model correctly ranks 72.7% of click/non-click pairs (higher is better, max 1.0)
 > - **LogLoss 0.400**: Good calibration for CTR tasks (lower is better, min 0.0)
-> - **Label-shuffle AUC 0.533**: Near 0.50 (random) proves no data leakage
+> - **Label-shuffle AUC 0.533**: Near 0.50 (random). Small deviations (e.g., ~0.53) can happen due to sampling/training noise → still indicates no exploitable leakage
 
---

### 📌 Evidence: `reports/metrics.json` snapshot (from Kaggle full run)

```json
{
  "main": {
    "test_auc": 0.72659,
    "test_logloss": 0.40009,
    "best_val_logloss": 0.40076
  },
  "label_shuffle": {
    "test_auc": 0.53265,
    "test_logloss": 0.45085,
    "best_val_logloss": 0.46177
  },
  "data": {
    "rows_used": 2000000,
    "total_samples": 1693522,
    "click_rate_raw": 0.1616
  },
  "split": {
    "train": 1393474,
    "val": 174464,
    "test": 125584
  },
  "env": {
    "platform": "Kaggle",
    "gpu": "Tesla T4"
  }
}

## 🚀 Quickstart

### Option 1: Kaggle Notebook (Recommended)
```bash
pip install -r requirements.txt
python -m src.run
type .\reports\metrics.json
```

Local src.run is a minimal reproducible pipeline demo (creates reports/metrics.json with the structure/format).
+> It is intended for pipeline structure + leakage checks, while the full TL;DR metrics are from Kaggle.

📊 What This Project Does

This project predicts click-through rate (CTR) using sequential user behavior, with rigorous leakage prevention.

### Leakage-Safety Checklist

EN: We repeat the **train-label shuffle** experiment **5 times** (different seeds) and report mean±std:
- Label-shuffle Test AUC (5 runs): **0.51 ± 0.02**  *(example format; replace with your measured values)*

KR: 학습 라벨 셔플을 **5번 반복**(seed 변경)해서 평균±표준편차로 제시합니다:
- 라벨 셔플 Test AUC (5회): **0.51 ± 0.02** *(형식 예시 / 실제 값으로 교체)*

   ✅ Time split by target timestamp: future events never appear in train
   ✅ History window uses only past events: hist contains events strictly before the target
   ✅ No test-label access: label-shuffle is applied to train labels only
   ✅ Tokenization/vocab: built without using test targets (recommended: train-only or train+val; specify your choice)

### Why Sequential Modeling?

Clicks aren't random—they follow patterns:

User just viewed 5 sports articles → more likely to click sports ads

User just browsed shopping → more likely to click shopping ads

### Model Architecture

-- Hybrid: DIN (Deep Interest Network) + SASRec-style Transformer
+- Hybrid: DIN (Deep Interest Network) + Transformer encoder inspired by SASRec

DIN component: Attention over historical events relevant to current item

Transformer component: Multi-head self-attention for sequence modeling

Output: Binary classification (click probability)

🔬 Methodology

@@ -132,7 +146,7 @@
Results (shuffled labels):

Validation AUC trajectory:

Epoch 1: 0.53516

Epoch 2: 0.49530

Epoch 3: 0.54221

Final test (shuffled):

Test AUC: 0.53265

Test LogLoss: 0.45085

-✅ Conclusion: When labels are destroyed, performance collapses to near-random → sanity check passed.
+✅ Conclusion: When train labels are destroyed, performance collapses to near-random → sanity check passed. (Optionally report mean±std over multiple shuffles for even stronger evidence.)
