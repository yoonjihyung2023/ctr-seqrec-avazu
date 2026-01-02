ctr-seqrec-avazu

Reproducible CTR prediction & Sequential RecSys experiments (Avazu CTR)
End-to-end pipeline: data → split → train → evaluate → report
✅ Focus: 재현성 + 누수/과적합 점검 (점수 “잘 나옴”보다 믿을 수 있는 평가)

이 레포는 뭐 하는 곳이야? (아주 쉽게)

CTR(클릭률) 예측은 **“이 광고/아이템을 사용자가 클릭할까?”**를 맞히는 문제입니다.
하지만 이 분야에서 더 중요한 건 점수가 높아 보이는 것이 아니라, 그 점수가 진짜 믿을 수 있게 나온 결과인지입니다.

CTR 로그/시퀀스 데이터는 데이터가 크고 복잡해서,
split 실수·전처리 순서·시퀀스 구성 실수만으로도 AUC가 비정상적으로 높아지는 “누수(leakage)”가 쉽게 생깁니다.

그래서 이 레포는 Avazu CTR 데이터를 사용해:

데이터를 준비하고

누수 없이 분리하고(split)

모델을 학습하고(train)

성능을 평가하고(evaluate)

실험 결과를 정리(report)
까지 끝까지 재현 가능하게 만드는 것을 목표로 합니다.

포함 내용 (What’s inside)
1) 문제(Task)

대규모 범주형 로그에서 CTR 예측

사용자 최근 행동(시퀀스)을 활용해 예측 성능을 높이는 실험

2) 모델(Models)

Baselines

Logistic Regression / LightGBM (optional)

Simple MLP (optional)

Deep CTR / Sequential

DIN: 사용자 과거 행동에 attention을 적용해 “관심사(interest)”를 반영

SASRec: Transformer 기반의 순차 추천 모델로 행동 문맥을 학습

BERT4Rec-style: 마스크드 시퀀스 학습을 CTR 설정에 맞게 응용

3) 평가(Metrics)

AUC-ROC

LogLoss

데이터(Dataset)

Dataset: Avazu CTR (Kaggle)

라이선스 때문에 데이터는 레포에 포함하지 않습니다.

Expected file

data/raw/train.csv

왜 “누수 체크”가 핵심인가?

CTR 실험에서는 결과가 너무 완벽하면 오히려 위험 신호일 때가 많습니다.

AUC ≈ 0.5 / LogLoss ≈ 8.18
→ 모델이 거의 구분을 못하고 랜덤에 가까운 상태일 수 있음

AUC = 1.0 / LogLoss = 0.0
→ 대부분의 경우 데이터 누수/평가 실수/타깃이 입력에 섞인 경우를 강하게 의심해야 함

이 레포는 그래서 “높은 점수 만들기”보다
누수 없이 정직하게 측정되는 실험 파이프라인을 우선합니다.

빠른 실행(Quickstart) (예시)

목표는 “누가 봐도 쉽게 실행”입니다. 실제 코드 구조에 맞춰 train/eval 진입점을 연결하면 됩니다.

# 1) 설치
pip install -r requirements.txt

# 2) 데이터 준비
python -m src.data.prepare --config configs/base.yaml

# 3) 학습
python -m src.train --config configs/bert4rec.yaml
python -m src.train --config configs/sasrec.yaml
python -m src.train --config configs/din.yaml

# 4) 평가
python -m src.eval --config configs/base.yaml

# 5) 앙상블(스태킹/블렌딩)
python -m src.ensemble.stack --config configs/ensemble.yaml
