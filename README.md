# ctr-seqrec-avazu — Avazu CTR 예측 (SeqRec + Leakage-safe)

## Quickstart (Windows PowerShell)
```powershell
pip install -r requirements.txt
python run_all.py
type reports\metrics.json
```

## 한 줄
3줄만 실행하면 `reports/metrics.json`이 생성되는 **재현 가능한** CTR/SeqRec 평가 파이프라인입니다.  
“사람이 클릭할지”를 예측하고, **시간 기준 split(미래 금지)** 으로 **데이터 누수 없이** 평가합니다.

## 10초 핵심
- ✅ **미래 데이터 금지**: `time-based split`
- ✅ **치팅 방지 확인**: `label shuffle` 하면 AUC ≈ 0.50 (정상)
- ✅ **재현 가능**: 실행하면 `reports/metrics.json` 파일이 자동으로 생김

## 현재 확실히 공개 가능한 결과
- ✅ `label_shuffle_auc = 0.50` (라벨을 섞으면 동전 수준이 나와야 정상)
- ✅ `test_auc = 0.50`, `test_logloss = 0.9339` (데모 실행 결과)

> 성능 숫자(AUC/LogLoss)는 “검증된 값”만 올립니다.  
> 너무 완벽한 값(AUC 1.0 / LogLoss 0.0)은 누수/버그로 오해받기 쉬워서  
> **검증 완료 전에는 메인에 올리지 않습니다.**

## 설치 + 실행 (3줄)
- ✅ 3줄 실행만으로 재현 가능(결과가 `reports/metrics.json`에 저장됨)
- ✅ 권장: Python 3.10+ (예: `python --version` 으로 확인)

### Mac / Linux / 일반
```bash
pip install -r requirements.txt
python -m src.run
cat reports/metrics.json
```

### Windows
```powershell
pip install -r requirements.txt
py -m src.run
type .\reports\metrics.json
```

✅ 중요: 이 실행은 “누수 방지 검사(`label shuffle`)”도 같이 돌도록 되어 있으며, `label_shuffle_auc ≈ 0.50`이 같이 나오면 “치팅 없이 평가했다”는 최소 신뢰가 생깁니다.

## 데이터
Avazu Click-Through Rate Prediction (Kaggle)

## 결과 파일
- `reports/metrics.json`
  - `test_auc`
  - `test_logloss`
  - `label_shuffle_auc`

```json
{
  "test_auc": 0.5,
  "test_logloss": 0.9339,
  "label_shuffle_auc": 0.5
}
```

## 내가 만든 것
- 시간 기준 split 파이프라인 (미래 금지)
- label shuffle sanity check (치팅 방지)
- 실험 결과 저장 구조 (`metrics.json`)

## 다음 작업 (짧게)
- metric 계산/저장 검증 완료 후 `test_auc`, `test_logloss` 업데이트

## One-line summary
Demo pipeline for CTR/SeqRec evaluation with leakage sanity-check (label shuffle).

## 왜 “순서(시퀀스)”를 보냐?

CTR은 보통 “한 번 노출 = 한 번 예측”처럼 보지만, 실제로는 사람이 방금 뭐 했는지가 중요합니다.

예를 들어:
- 방금 스포츠 기사를 많이 봤으면 → 스포츠 광고를 더 누를 수 있음
- 방금 쇼핑을 많이 봤으면 → 쇼핑 광고를 더 누를 수 있음

그래서 이 프로젝트는:
- 사람의 최근 행동을 순서대로 모아서
- 그 다음 클릭을 예측합니다.

그리고 제일 중요한 건:
- 미래 데이터를 절대 쓰지 않고(`time-based split`)
- 라벨을 섞는 테스트(`label shuffle`)로 치팅이 없는지 확인한다는 점입니다.
