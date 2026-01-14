# ctr-seqrec-avazu

Avazu CTR 데이터로 **CTR(클릭) 예측 + 순차 추천 모델**을 실험하는 레포입니다.  
목표는 점수 자랑이 아니라 **누수 없이, 누구나 같은 결과를 재현**하는 것입니다.

✅ 포트폴리오 포인트: **데이터 누수 방지 / 재현성 / 실험 관리(config 기반)**

---

## 한 줄로 말하면
“이 사람이 광고를 클릭할까?”를 예측하고 **AUC / LogLoss**로 평가합니다.

---

## 왜 믿을 수 있어요? (누수 방지 3가지)
- **Split 규칙 고정**: (예: 시간 기준 / 유저 기준)으로 train/val/test를 나눕니다.
- **전처리 규칙**: 전처리는 train에만 `fit`, val/test는 `transform`만 합니다.
- **검사 코드**: 누수 의심 신호를 자동으로 검사합니다. (예: AUC=1.0 같은 비정상 결과)

👉 자세한 체크리스트: `docs/leakage_checklist.md`

---

## 🚀 Quickstart (끝까지 4줄)
```bash
pip install -r requirements.txt
python -m src.data.prepare --config configs/base.yaml
python -m src.train        --config configs/din.yaml
python -m src.eval         --config configs/din.yaml
