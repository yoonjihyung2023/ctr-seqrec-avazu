# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Stacking)

한 줄: Avazu CTR(클릭) 예측에서 **사용자 행동의 순서(Sequence)** 를 쓰는 모델(SASRec/BERT4Rec)을 학습하고,  
**누수(Leakage) 없이 재현 가능한 실험 파이프라인**을 만들었습니다. (석사 논문 기반)

## 지금 당장 되는 것 (3개)
- ✅ Split 먼저 → 그 다음 학습 (Valid/Test는 절대 fit 금지)
- ✅ **Label Shuffle(라벨 섞기)** 로 누수 여부를 확인 (정상이면 AUC ≈ 0.5)
- ✅ 실행하면 `reports/metrics.json` 파일이 생김

---

## 바로 실행 (3줄)
```bash
pip install -r requirements.txt
python run_all.py
cat reports/metrics.json
```

## Leakage 체크(예정)
Label Shuffle 테스트를 추가 중이며, 결과(`label_shuffle_auc`)는 `reports/metrics.json`에 저장됩니다.
