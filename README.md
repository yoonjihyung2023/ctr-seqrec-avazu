# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Leakage-safe Pipeline)

한 줄: “사람이 클릭할지”를 맞히는 모델을 만들었고, **시간 기준 split(미래 금지)** 으로 **누수 없이** 성능을 봤어요.  
(석사 논문 기반: SASRec / BERT4Rec, 평가: AUC-ROC & LogLoss)

## Results (핵심만 10초)
*Baseline = 간단한 기본 모델 / Improved = 순차모델+앙상블.*  
이 프로젝트는 “클릭 맞히기 게임”이에요.  
점수는 **AUC(클수록 좋음)**, **LogLoss(작을수록 좋음)** 입니다.

- Baseline(처음, 거의 랜덤): **AUC 0.50 / LogLoss 8.18**
- Improved(더 잘하려고 한 것): **SASRec/BERT4Rec 실험 + Stacking(메타러너: DIN)로 개선**
- Safety check(속임수 방지): **Label Shuffle AUC ≈ 0.50 이면 정상** (수치 업데이트 예정)

⚠️ 참고: AUC가 너무 높게 나오면(예: 1.0) **누수/과적합**일 수도 있어요.

## What I built (제가 만든 것)
- 한 번에 돌리는 스크립트: `run_all.py`
- 결과 저장: `reports/metrics.json` (실험 비교 쉽게)
- 시간 기준 Split(미래 정보 금지) + Label-shuffle sanity check 구조

## Run (바로 실행)
```bash
pip install -r requirements.txt
python run_all.py
```

## Output (결과 파일)
`reports/metrics.json`에 저장됩니다.

예시:
```json
{
  "test_auc": 0.50,
  "test_logloss": 8.18,
  "label_shuffle_auc": null
}
```
- `label_shuffle_auc`는 정상이라면 0.50 근처입니다. (추후 업데이트)

## Environment
Python 3.10+
