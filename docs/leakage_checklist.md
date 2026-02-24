# Leakage Checklist

- Time-based split: train < valid < test (future 금지)
- Sequence도 예측 시점 이후 이벤트 포함 금지
- 금지: random split, test/valid를 섞은 global 통계(CTR/target encoding)

Sanity:
- Label-shuffle AUC ≈ 0.50 이면 정상(누수 없음)

Evidence:
- reports/metrics.json
- reports/run_meta.json
