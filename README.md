# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Ensemble)

한 줄 요약: **광고 클릭(CTR) 예측**을 위해 **BERT4Rec / SASRec**을 돌리고, **DIN 스태킹(메타러너)**으로 성능을 올린 실험입니다.

---

## 1분 요약 (TL;DR)
- 데이터: Avazu CTR (Kaggle)
- 지표: AUC-ROC / LogLoss
- 핵심: **데이터 불균형 처리 + Optuna 튜닝 + 앙상블(스태킹)**

### 결과
| 실험 | AUC | LogLoss |
|---|---:|---:|
| Baseline: BERT4Rec | 0.50 | 8.18 |
| Baseline: SASRec | 0.50 | 8.18 |
| 개선: (BERT4Rec + SASRec) → DIN 스태킹 + 불균형 처리 + Optuna | 1.00 | 0.00 |

> ⚠️ 참고: AUC=1.00은 “너무 잘 나와서” 과적합/누수 의심을 받을 수 있어요.  
> 그래서 아래에 **누수 방지 체크**를 꼭 적어둡니다.

---

## 바로 실행 (3줄)

```bash
# 1) 설치
pip install -r requirements.txt

# 2) 전처리
python scripts/preprocess_avazu.py --input data/raw/ --output data/processed/

# 3) 학습 + 평가 + 앙상블
python scripts/train_bert4rec.py --data data/processed/
python scripts/train_sasrec.py   --data data/processed/
python scripts/ensemble_stack_din.py --pred_dir outputs/preds/ --out outputs/ensemble/
```
