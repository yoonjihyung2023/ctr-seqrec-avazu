# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Leakage-safe Pipeline)

한 줄: Avazu CTR 예측에서 **사용자 행동 순서(Sequence)** 를 쓰는 모델(SASRec/BERT4Rec) 실험을 목표로,  
**재현 가능한 실행 흐름 + 결과 저장 형식(reports/metrics.json)** 을 먼저 정리했습니다. (석사 논문 기반)

## What I built (제가 만든 것)
- 실행 스크립트: `run_all.py`
- 결과 저장 형식: `reports/metrics.json` (나중에 실험 비교가 쉬움)
- README에 “실험을 어떻게 재현하는지”를 10초 만에 보이게 구성

## Results
현재 공개 버전은 **결과 파일 형식(metrics.json)과 실행 뼈대**를 제공합니다.  
실제 학습/평가 코드 정리 후 **Test AUC/LogLoss, Label-shuffle sanity check** 수치를 업데이트합니다.

샘플 형식 (`reports/metrics.json`)
```json
{
  "test_auc": "TBD",
  "test_logloss": "TBD",
  "label_shuffle_auc": "TBD"
}
```
## Environment
Python 3.x

## Next
Stacking 등 확장 실험은 검증 완료 후 순차적으로 공개 예정

## 바로 실행
시간 기준 Split 사용(미래 정보 금지).

## Run
```bash
pip install -r requirements.txt
python run_all.py
```

## 실행 확

## Next
configs/학습/평가 모듈 정리 후 공개
time split + label shuffle sanity check 자동화
stacking 등 확장 실험 추가
