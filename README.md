# ctr-seqrec-avazu

Reproducible **CTR (Click-Through Rate) prediction** pipeline on the **Avazu dataset**.  
Focus: **no data leakage**, **fair evaluation**, and **clear reproducibility**.

---

## 🚀 Quickstart (3 lines)
```bash
pip install -r requirements.txt
python scripts/preprocess.py
python scripts/train.py

# ctr-seqrec-avazu
CTR(클릭) 예측 + 순차 추천 실험을 Avazu 데이터로 **누수 없이** 재현하는 레포입니다.  
목표는 점수 자랑이 아니라 **믿을 수 있는 실험 파이프라인**입니다.

## 한 줄로 말하면
“이 사람이 광고를 클릭할까?”를 맞히는 모델을 만들고, **AUC/LogLoss**로 평가합니다.

## 들어있는 것
- 데이터 준비 (Avazu)
- train/val/test 분할(누수 방지)
- 모델: DIN / SASRec / BERT4Rec-style
- 평가: AUC-ROC, LogLoss
- 리포트 생성: `reports/summary.md`

## 결과(요약)
- Round 1: AUC 0.50 / LogLoss 8.18
- Round 2: AUC 1.00 / LogLoss 0.00  
  → 이런 점수는 먼저 **누수/과적합을 의심하고 검증**합니다.

## Quickstart (그대로 복붙해서 실행)
```bash
# install
pip install -r requirements.txt

# data
python -m src.data.prepare --config configs/base.yaml

# train
python -m src.train --config configs/din.yaml
python -m src.train --config configs/sasrec.yaml
python -m src.train --config configs/bert4rec.yaml

# eval & report
python -m src.eval --config configs/base.yaml
python -m scripts.make_report --out reports/summary.md
