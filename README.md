# ctr-seqrec-avazu
**Reproducible CTR prediction & sequential RecSys experiments (Avazu CTR)**  
End-to-end pipeline: **data → split → train → evaluate → report**  
✅ Focus: **reproducibility + leakage/overfitting checks** (trustworthy evaluation over “too-perfect” scores)

---

## 이 레포는 뭐 하는 곳이야? (아주 쉽게)
CTR(클릭률) 예측은 “이 광고/아이템을 사용자가 클릭할까?”를 맞추는 일이에요.  
근데 더 중요한 건 **점수가 좋아 보이는 것**이 아니라,  
**점수가 진짜 믿을 수 있게(누수 없이) 나온 것**이에요.

그래서 이 레포는 Avazu CTR 데이터로:
- 데이터를 준비하고
- 누수 없이 나누고(split)
- 모델을 학습하고(train)
- 평가하고(evaluate)
- 결과를 정리(report)
까지 **끝까지** 재현 가능하게 만드는 프로젝트입니다.

---

## 포함 내용 (What’s inside)
### 문제(Task)
- 대규모 범주형 로그에서 CTR 예측
- 사용자 최근 행동(시퀀스)을 활용한 예측 성능 향상 실험

### 모델(Models)
**Baselines**
- Logistic Regression / LightGBM *(optional)*
- Simple MLP *(optional)*

**Deep CTR / Sequential**
- DIN (attention over user behavior)
- SASRec (Transformer-based sequential model)
- BERT4Rec-style (masked sequence modeling adapted for CTR)

### 평가(Metrics)
- **AUC-ROC**
- **LogLoss**

---

## 데이터(Dataset)
- Dataset: **Avazu CTR** (Kaggle)
- 라이선스 때문에 데이터는 레포에 포함하지 않습니다.

**Expected file**
- `data/raw/train.csv`

---

## 빠른 실행(Quickstart)
> 아래 구조가 아직 없으면, 먼저 폴더를 만들어 주세요. (WIP)

### 1) 설치(Setup)
```bash
git clone https://github.com/yoonjihyung2023/ctr-seqrec-avazu.git
cd ctr-seqrec-avazu
python -m venv .venv
source .venv/bin/activate  # (Windows) .venv\Scripts\activate
pip install -r requirements.txt
