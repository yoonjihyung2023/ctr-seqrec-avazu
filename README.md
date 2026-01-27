# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Leakage-safe Pipeline)

한 줄: Avazu CTR 예측에서 **사용자 행동 순서(Sequence)** 를 쓰는 모델(SASRec/BERT4Rec)을 학습하고,  
**시간 기준 분리(time split) + 누수 점검(label shuffle) + 재현 가능한 실행 파이프라인**을 만들었습니다. (석사 논문 기반)

## What I built (제가 만든 것)
- 미래 정보가 섞이지 않게 **time split** 적용
- 같은 평가 코드로 **label shuffle sanity check** 실행
- 실험 결과를 `reports/metrics.json`으로 저장 (재현/비교 쉬움)

## Results (Leakage sanity check 포함)
| Metric | Value |
|---|---|
| Test AUC | TBD |
| Test LogLoss | TBD |
| Label Shuffle AUC (should be ~0.50) | TBD |

- Label Shuffle: **y만 섞고**, **같은 평가 코드로** 다시 측정합니다.
- AUC≈0.50이면 **누수 의심이 낮습니다**(sanity check).

샘플 형식 (`reports/metrics.json`)
```json
{
  "test_auc": "TBD",
  "test_logloss": "TBD",
  "label_shuffle_auc": "TBD"
}
```
## Environment
Python 3.x (CPU로도 실행 가능, GPU optional)

## Next
Stacking 등 확장 실험은 검증 완료 후 순차적으로 공개 예정

## 바로 실행
시간 기준 Split 사용(미래 정보 금지).

Step 1) 설치
```bash
pip install -r requirements.txt
```

Step 2) 실행
```bash
python run_all.py
cat reports/metrics.json
```
