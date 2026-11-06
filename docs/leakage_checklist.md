# Leakage Checklist

- Time-based split: train < valid < test (future 금지)
- Sequence도 예측 시점 이후 이벤트 포함 금지
- 금지: random split, test/valid를 섞은 global 통계(CTR/target encoding)

Sanity:
- Label-shuffle AUC가 0.50 근처인지 보조 점검한다. 이 결과만으로 누수가 없다고 증명할 수 없다.

Evidence:
- 원본 노트북의 실행 출력과 코드, 분할 설정을 함께 확인
- reports/metrics.json은 요약 기록이며 원본 실행 출력의 독립적인 증거는 아님
