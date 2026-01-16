# ctr-seqrec-avazu
Avazu CTR 데이터로 **CTR(클릭) 예측 + 순차(Sequential) 추천 모델**을 실험하는 레포입니다.  
목표는 점수 자랑이 아니라 **누수 없이, 누구나 같은 결과를 재현**하는 것입니다.

✅ 포트폴리오 포인트: **데이터 누수 방지 / 재현성 / config 기반 실험**

---

## 🚀 Quickstart (3 commands)
```bash
pip install -r requirements.txt
python -m src.run --config configs/sasrec.yaml
cat reports/metrics.json
```

실행 결과는 `reports/metrics.json`에 저장됩니다.
