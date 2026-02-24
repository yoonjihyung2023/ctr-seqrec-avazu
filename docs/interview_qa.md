# Interview Q&A (10)

1) 왜 time-split? → CTR 로그는 시간 데이터라 random split은 미래 누수.
2) 왜 label-shuffle? → 누수 없으면 신호가 사라져 AUC≈0.50이 정상.
3) 왜 AUC+LogLoss? → AUC=랭킹 품질, LogLoss=확률 품질.
4) 왜 sequential? → 유저의 최근 행동이 intent를 반영.
5) 누수 위험 3개? → random split / 미래 이벤트 포함 / 기간 섞인 통계.
6) offline-online 갭? → shift, position bias, delayed feedback.
7) 재현성 보장? → metrics.json + run_meta.json(환경/seed/커밋).
8) 다음 개선 3개? → calibration / HPO / bias-feature(포지션 등).
9) 실서빙은? → versioned artifact + 모니터링 + 롤백.
10) 왜 너? → 누수방지+재현+서빙데모까지 “검증 가능한 증거”가 있음.
