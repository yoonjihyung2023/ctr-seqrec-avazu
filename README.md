# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Ensemble)

한 줄 요약: Avazu CTR(클릭) 예측을 위해 BERT4Rec/SASRec을 실험했고, 스태킹은 누수 점검 후 시간 split로 재검증 예정입니다.

## 핵심
- 무엇: Avazu CTR(클릭) 예측 실험 (BERT4Rec / SASRec + 스태킹 후보)
- 어떻게: Stratified split + (중요) 샘플링/튜닝은 Train에만 적용
- 현재 상태: 스태킹/SMOTE에서 비정상 점수 발생 → 누수/버그 점검 후 시간 split로 다시 공개

---

## 1분 요약 (TL;DR)
- 데이터: Avazu CTR (Kaggle)
- 지표: AUC-ROC / LogLoss
- 핵심: **데이터 불균형 처리 + Optuna 튜닝 + 앙상블(스태킹)**

### 결과(현재)
| 실험 | Split | AUC | LogLoss |
|---|---|---:|---:|
| Baseline: BERT4Rec | Stratified | 0.50 | 8.18 |
| Baseline: SASRec | Stratified | 0.50 | 8.18 |

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
