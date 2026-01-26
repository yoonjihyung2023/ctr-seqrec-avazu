# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Stacking)

한 줄: Avazu CTR(클릭) 예측에서 **사용자 행동의 순서(Sequence)** 를 쓰는 모델(SASRec/BERT4Rec)을 학습하고,  
**누수(Leakage) 없이 재현 가능한 실험 파이프라인**을 만들었습니다. (석사 논문 기반)

## 결과 (Leakage 확인 포함)
- Test AUC: 0.xx / LogLoss: 0.xx
- Label Shuffle AUC: 0.50 근처 ✅ (정상: 누수 없음)
- Label Shuffle은 **y만 섞고**(feature/sequence는 그대로), **같은 평가 코드로** 다시 측정합니다.

예시(`reports/metrics.json`)
```json
{
  "test_auc": 0.78,
  "test_logloss": 0.41,
  "label_shuffle_auc": 0.50
}
```

## 바로 실행
- 시간 기준 Split 사용(미래 정보 금지).

```bash
pip install -r requirements.txt
python run_all.py
cat reports/metrics.json
```
