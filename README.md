# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Leakage-safe Pipeline)

한 줄: “사람이 클릭할지”를 맞히는 모델을 만들었고, **시간 기준 split(미래 금지)** 으로 **누수 없이** 성능을 봤어요.  
(석사 논문 기반: SASRec / BERT4Rec, 평가: AUC-ROC & LogLoss)

## Results (핵심만 10초)
*Baseline = 간단한 기본 모델 / Tried = 순차모델+앙상블 시도.*  
이 프로젝트는 “클릭 맞히기 게임”이에요.  
점수는 **AUC(클수록 좋음)**, **LogLoss(작을수록 좋음)** 입니다.

- Split: time-based (미래 정보 사용 금지)
- Sanity check (label shuffle): AUC = 0.50 → 정상
- Next: test AUC/LogLoss = 0.0 이슈 → metric 계산/저장 버그 수정 후 수치 업데이트
- Tried: SASRec/BERT4Rec + stacking (meta-learner: DIN)

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

포함되는 항목:
- `test_auc`: Test AUC (계산/저장 파이프라인 점검 후 업데이트)
- `test_logloss`: Test LogLoss (계산/저장 파이프라인 점검 후 업데이트)
- `label_shuffle_auc`: Sanity check AUC (라벨을 섞으면 0.50 근처가 정상)

현재 확인된 값:
- `label_shuffle_auc = 0.50` ✅

## Environment
Python 3.10+
