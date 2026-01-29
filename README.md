# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Leakage-safe)

## 한 줄
“사람이 클릭할지” 예측합니다. **시간 기준 split(미래 금지)** 으로 **데이터 누수 없이** 평가합니다.

## 10초 핵심 (면접관이 제일 보고 싶은 것)
- ✅ 미래 데이터 금지: time-based split
- ✅ 치팅 방지 확인: label shuffle 하면 AUC ≈ 0.50 (정상)
- ✅ 재현 가능: `run_all.py` 한 방 실행 + `reports/metrics.json` 결과 저장
- ✅ Reproduce: `python run_all.py` → `reports/metrics.json`

## 현재 확실히 공개 가능한 결과
- ✅ `label_shuffle_auc = 0.50`  (라벨을 섞으면 동전 수준이 나와야 정상)

> 성능 숫자(AUC/LogLoss)는 “확실한 값”만 올립니다.  
> 너무 완벽한 값(AUC 1.0 / LogLoss 0.0)은 누수/버그로 오해받기 쉬워서  
> 검증 완료 전에는 메인에 두지 않습니다.

## 실행 (2줄)
```bash
pip install -r requirements.txt
python run_all.py
```

## 데이터
Avazu Click-Through Rate Prediction (Kaggle)

## 결과 파일
- `reports/metrics.json`
  - `test_auc`
  - `test_logloss`
  - `label_shuffle_auc`

```json
{
  "label_shuffle_auc": 0.50,
  "test_auc": null,
  "test_logloss": null
}
```

## 내가 만든 것
- 시간 기준 split 파이프라인 (미래 금지)
- label shuffle sanity check (치팅 방지)
- 실험 결과 저장 구조 (`metrics.json`)

## 다음 작업 (짧게)
- metric 계산/저장 검증 완료 후 `test_auc`, `test_logloss` 업데이트
