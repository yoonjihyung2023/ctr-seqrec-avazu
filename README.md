# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Ensemble)

한 줄 요약: **광고 클릭(CTR) 예측**을 위해 **BERT4Rec / SASRec**을 학습하고, **DIN 스태킹(메타러너)**으로 성능을 올린 실험입니다.

---

## 1분 요약 (TL;DR)
- 데이터: Avazu CTR (Kaggle)
- 지표: AUC-ROC / LogLoss
- 핵심: **데이터 불균형 처리 + Optuna 튜닝 + 앙상블(스태킹)**

### 결과
| 실험 | Split | AUC | LogLoss |
|---|---|---:|---:|
| Baseline: BERT4Rec | Stratified | 0.50 | 8.18 |
| Baseline: SASRec | Stratified | 0.50 | 8.18 |
| 개선: Stack(DIN) + SMOTE + Optuna | Stratified | 1.00 | 0.00 |

> ⚠️ 참고: AUC=1.00은 “너무 잘 나와서” 과적합/누수 의심을 받을 수 있어요.  
> 그래서 아래에 **누수 방지 체크**를 적었습니다.

---

## 누수 방지(중요)
- Train/Test 분리 후, **SMOTE/언더샘플링은 Train에만 적용** (Test는 절대 건드리지 않음)
- **계층 분할(Stratified split)**로 클래스 비율 유지
- (추가 예정) **시간 기준 분할 / 사용자 기준 분할**로 재검증

---

## 바로 실행 (3줄)
```bash
pip install -r requirements.txt
python run_all.py
cat reports/metrics.json
```
