# ctr-seqrec-avazu
Avazu CTR 데이터로 CTR(클릭) 예측 + 순차(Sequential) 추천 모델을 실험한 레포입니다.  
포인트: **누수 방지 + 재현성(같은 결과 다시 만들기)**

## 🚀 Quickstart (3줄)
```bash
pip install -r requirements.txt
python -m src.run --config configs/sasrec.yaml
cat reports/metrics.json
```

## ✅ Results (논문 숫자)
- 1차: BERT4Rec/SASRec → AUC 0.5, LogLoss 8.18
- 2차: (앙상블) → AUC 1.0, LogLoss 0.0

> Note: AUC=1.0은 과적합일 수도 있어 추가 검증이 필요합니다.
