# ctr-seqrec-avazu

CTR(클릭) 예측 + 순차 추천 실험을 Avazu 데이터로 **누수 없이** 재현하는 레포입니다.  
목표는 점수 자랑이 아니라 **믿을 수 있는 실험 파이프라인**입니다.

## 한 줄로 말하면
“이 사람이 광고를 클릭할까?”를 맞히는 모델을 만들고, **AUC / LogLoss**로 평가합니다.

---

## 🚀 Quickstart (3줄)
```bash
pip install -r requirements.txt
python -m src.data.prepare --config configs/base.yaml
python -m src.train --config configs/din.yaml
