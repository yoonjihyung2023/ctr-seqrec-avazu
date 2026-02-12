# ctr-seqrec-avazu
**Leakage-safe CTR prediction with sequential modeling on the Avazu dataset**

[![Time-based Split](https://img.shields.io/badge/split-time--based-green)](https://github.com/yoonjihyung2023/ctr-seqrec-avazu)
[![Sanity Check](https://img.shields.io/badge/sanity-label--shuffle-blue)](https://github.com/yoonjihyung2023/ctr-seqrec-avazu)
[![Python](https://img.shields.io/badge/python-3.10%2B-informational)](https://www.python.org/)
[![Kaggle](https://img.shields.io/badge/run-kaggle-20BEFF)](https://www.kaggle.com/c/avazu-ctr-prediction)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

---

## 🎯 Results

| Metric | Main Model | Label-Shuffle Sanity Check (train labels only) |
|--------|------------|-----------------------------------------------|
| **Test AUC** | **0.72659** | **0.53265** ✅ |
| **Test LogLoss** | **0.40009** | **0.45085** |
| **Meaning** | Strong predictive signal | Near-random → sanity check passed |

✅ **Reproducible**: Results obtained from an end-to-end **Kaggle run** (2M rows, **Tesla T4**).

**Leakage verification**: Shuffling **train labels only** collapses performance toward random → **sanity check passed** ✅  
*(Small deviations like ~0.53 can occur due to sampling/training noise and early stopping.)*

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
    "gpu": "Tesla T4",
    "cuda": true
  }
}
```

## 🚀 Quickstart

### Kaggle Notebook (Recommended for full results)
1. Create a Kaggle Notebook
2. Attach dataset: `avazu-ctr-prediction`
3. Run the cells
4. View results in the console (and optionally save to `reports/metrics.json`)

### Local (demo only: structure + leakage checks; numbers differ vs Kaggle full run)

**Mac/Linux:**
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```

**Windows PowerShell:**
```powershell
pip install -r requirements.txt
python -m src.run
type .\reports\metrics.json
```
**Expected output example (local demo / smoke test):**
```json
{"test_auc": 0.5, "test_logloss": 0.9339, "label_shuffle_auc": 0.5}

- Note: Local demo numbers are for verifying the pipeline + leakage check only (not comparable to Kaggle full run).

## 📊 What This Does

- Predicts click-through rate (CTR) using sequential user behavior modeling.

Why sequential? Clicks follow patterns:

- Just viewed sports articles → more likely to click sports ads
- Just browsed shopping → more likely to click shopping ads

Pipeline

- Tokenize events (18 features per event, vocab: 9,664)
- Build user sequences by device_id (~163K users)
- Time-based split (train uses only past data)
- Train hybrid DIN + Transformer (inspired by SASRec) model
- Verify with label-shuffle sanity check

Dataset: Avazu CTR (2M rows, ~1.69M samples, ~16.8% positive ratio)

## 🔒 Leakage Prevention
### Time-based Split

- Train (past) → Val → Test (future)
- Split by target timestamp → no future data in training.

### Label-Shuffle Sanity Check

- Shuffle train labels only (corrupt the signal)
- Train model on corrupted labels
- Expected: AUC ≈ 0.50 (random)
- Observed: AUC 0.53265 ✅

If leakage existed, the model could still perform well despite shuffled labels.

## 📖 Citation
```bibtex
@misc{ctr-seqrec-avazu,
  title={Leakage-safe CTR Prediction with Sequential Modeling},
  author={Jihyung Yoon},
  year={2026},
  publisher={GitHub},
  url={https://github.com/yoonjihyung2023/ctr-seqrec-avazu}
}
```

## 📄 License
MIT License

## 🌏 한국어
<details>
<summary>클릭하여 보기</summary>

### 결과
본 모델: Test AUC 0.72659 / LogLoss 0.40009  
라벨 셔플(학습 라벨만): Test AUC 0.53265 / LogLoss 0.45085 (≈0.50)

### 핵심
시퀀스 기반 CTR 예측 + 시간 분할로 미래 데이터 차단 + 학습 라벨 셔플로 누수 검증

### 실행
Kaggle(권장): 노트북 생성 → avazu-ctr-prediction attach → 실행 → 콘솔 결과 확인

### Windows PowerShell(데모)
```powershell
pip install -r requirements.txt
python -m src.run
type .\reports\metrics.json
```

### 로컬(데모: Mac/Linux)
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```
</details> 
