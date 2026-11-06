# Interview Q&A (10)

1) 왜 time-split? → 미래 구간에 대한 예측을 평가하고 미래 정보가 학습에 반영될 위험을 줄이기 위해.
2) 왜 label-shuffle? → 정답을 섞었을 때 성능을 살펴보는 보조 점검. 이것만으로 누수 부재를 증명할 수는 없다.
3) 왜 AUC+LogLoss? → AUC=랭킹 품질, LogLoss=확률 품질.
4) 왜 sequential? → 유저의 최근 행동이 intent를 반영.
5) 누수 위험 3개? → random split / 미래 이벤트 포함 / 기간 섞인 통계.
6) offline-online 갭? → shift, position bias, delayed feedback.
7) 재현성은? → 원본 코드, 데이터 분할, 환경과 실행 출력을 함께 보존해야 한다. 일반 학습 결과의 원본 출력은 아직 확인되지 않았다.
8) 다음 개선 3개? → calibration / HPO / bias-feature(포지션 등).
9) 실서빙은? → versioned artifact + 모니터링 + 롤백.
10) 왜 너? → CTR 실험, 평가 유틸리티와 규칙 기반 API 데모를 통해 모델 평가와 서비스 구조를 학습했다.
