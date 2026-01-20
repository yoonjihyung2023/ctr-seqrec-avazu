# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Ensemble)

광고 클릭(CTR)을 예측하는 모델을 만들었습니다.
Avazu 데이터로, 사용자 행동 “순서”를 보는 모델(SASRec/BERT4Rec)을 학습했습니다. 
AUC-ROC / LogLoss로 성능을 확인했고, 스태킹(DIN 기반)으로 성능을 개선했습니다. 

Built a CTR prediction model for online ads.
Trained sequence-based user models (SASRec/BERT4Rec) on the Avazu dataset. 
Evaluated with AUC-ROC / LogLoss and improved performance via stacking (DIN-based). 

한 줄 요약: Avazu CTR 예측(SeqRec) 파이프라인을 재현했고, 시간(Time) split 최종 점수 공개 예정입니다.

## 핵심
- 무엇: Avazu CTR(클릭) 예측 실험 (BERT4Rec / SASRec + 스태킹 후보)
- 어떻게: Stratified split + (중요) 샘플링/튜닝은 Train에만 적용
- 현재 상태: 스태킹/SMOTE에서 비정상 점수 발생 → 누수/버그 점검 후 시간 split로 다시 공개

---

## 1분 요약 (TL;DR)
- 데이터: Avazu CTR (Kaggle)
- 지표: AUC-ROC / LogLoss
- 핵심: **데이터 불균형 처리 + Optuna 튜닝 + 앙상블(스태킹)**

### 결과(요약)
- Baseline(BERT4Rec/SASRec): 현재 재현 완료 (AUC≈0.50 수준)
- Next update: 시간(Time) 기준 Split로 재검증 후, 최종 숫자(AUC/LogLoss) 공개

> NOTE: 스태킹/SMOTE/Optuna 실험에서 AUC가 비정상적으로 높게 나와
> **누수/버그 가능성 점검 후** “시간 split 결과”로 다시 공개 예정입니다.

---

## 누수 체크(3줄, 가장 중요)
- 라벨 섞기 테스트: y(클릭)를 랜덤으로 섞어 학습 → AUC가 0.5 근처면 정상, 높으면 누수/버그 의심
- 파이프라인 순서 확인: split 먼저, 그 다음에 인코딩/샘플링/튜닝 (Valid/Test는 절대 fit 금지)
- 중복/ID 확인: Train과 Test에 같은 행(또는 같은 ID)이 같이 들어가면 누수

---

## 바로 실행 (3줄)
```bash
pip install -r requirements.txt
python run_all.py
cat reports/metrics.json
```

> run_all.py는 **Train/Valid/Test를 먼저 나눈 뒤**, 샘플링/튜닝은 **Train에만** 적용하고, 결과를 `reports/metrics.json`에 저장합니다.

결과 파일: [reports/metrics.json](reports/metrics.json)
