# ctr-seqrec-avazu
Reproducible CTR prediction & sequential RecSys experiments on Avazu CTR  
데이터→분할→학습→평가→리포트까지 “누수 없이” 다시 돌릴 수 있게 만드는 레포

## 이 레포는 뭐 하는 곳이야? (아주 쉽게)
CTR 예측은 “이 사람이 이 광고를 클릭할까?”를 맞히는 일이야.  
근데 CTR 실험은 **조금만 실수해도 점수가 비정상적으로 좋아질 수 있어**(데이터 누수).

그래서 이 레포는 **점수 자랑**이 아니라,
✅ **정직하게 측정되는 실험 파이프라인**을 만드는 게 목표야.

## 무엇을 할 수 있어?
- Avazu CTR 데이터 준비
- 누수 없이 train/val/test 분리
- 모델 학습: DIN / SASRec / BERT4Rec-style
- 평가: AUC-ROC, LogLoss
- 결과 리포트 생성(표/그래프/로그)

## 논문 기반 결과(요약)
- Round 1: AUC 0.5 / LogLoss 8.18 (거의 랜덤 수준)
- Round 2: AUC 1.0 / LogLoss 0.0 (누수/과적합 가능성도 함께 점검 필요)

> 이 레포는 Round 2 같은 “완벽한 점수”가 나오면  
> 오히려 **Split/전처리/평가 파이프라인을 먼저 의심하고 검증**합니다.

## 누수 방지 체크리스트 ✅ (이게 핵심!)
- [ ] SMOTE/언더샘플링은 TRAIN에만 적용
- [ ] 타깃 인코딩/스케일링은 TRAIN에만 fit, val/test는 transform만
- [ ] 분할 규칙 문서화(계층화/시간 분할 비교)
- [ ] seed 여러 개로 평균/표준편차 기록
- [ ] 라벨 셔플하면 AUC가 0.5 근처로 떨어지는지 확인

## Quickstart
```bash
# 1) install
pip install -r requirements.txt

# 2) data
python -m src.data.prepare --config configs/base.yaml

# 3) train
python -m src.train --config configs/din.yaml
python -m src.train --config configs/sasrec.yaml
python -m src.train --config configs/bert4rec.yaml

# 4) eval & report
python -m src.eval --config configs/base.yaml
python -m scripts.make_report --out reports/summary.md


---

## 2) (복붙) README 최종형 — EN (짧고 믿음 가게)

```md
# ctr-seqrec-avazu
Reproducible CTR prediction & sequential RecSys experiments on Avazu CTR  
End-to-end pipeline: data → split → train → evaluate → report (with leakage checks)

## What is this repo? (super simple)
CTR prediction means: “Will a user click this ad/item?”  
But CTR experiments can look *artificially great* if you make small mistakes (data leakage).

So the goal here is NOT “flashy scores”, but:
✅ a reproducible, honest evaluation pipeline.

## What’s inside
- Data prep for Avazu CTR
- Train/val/test splits (documented)
- Models: DIN / SASRec / BERT4Rec-style
- Metrics: AUC-ROC, LogLoss
- Reports: tables/plots/logs as portfolio artifacts

## Thesis-based results (brief)
- Round 1: AUC 0.5 / LogLoss 8.18 (near-random)
- Round 2: AUC 1.0 / LogLoss 0.0 (requires strong leakage/overfit validation)

> If we ever see “AUC=1.0”, we treat it as a red flag first,
> and verify split rules + preprocessing order + evaluation code.

## Leakage Checklist ✅ (the most important part)
- [ ] Resampling (SMOTE/undersampling) on TRAIN only
- [ ] Encoding/scaling fit on TRAIN only, transform on val/test
- [ ] Split policy documented (stratified / optional time-based)
- [ ] Multi-seed mean/std
- [ ] Label-shuffle sanity check → AUC should drop ~0.5

## Quickstart
```bash
pip install -r requirements.txt
python -m src.data.prepare --config configs/base.yaml
python -m src.train --config configs/din.yaml
python -m src.train --config configs/sasrec.yaml
python -m src.train --config configs/bert4rec.yaml
python -m src.eval --config configs/base.yaml
python -m scripts.make_report --out reports/summary.md


---

## 3) 너 초안에서 “딱 6개”만 고치면 더 합격처럼 보이는 이유 (5살 버전)

### ① 설명을 “짧게”
사람은 길면 안 읽어.  
그래서 “이 레포 뭐야?”를 **3줄**로 만들었어.

### ② “우리는 점수 자랑 안 해요”를 “우리는 믿음 보여줘요”로
“점수 잘 나옴보다 믿을 수 있는 평가” → **완전 좋은 메시지**야.  
근데 더 강하게 보이게 하려면 **체크리스트**가 필수야.  
(말만 하면 못 믿고, 체크하면 믿어.)

### ③ AUC 1.0을 “자랑”으로 쓰지 말기
AUC 1.0을 “좋다”라고 쓰면 어른들이 의심해.  
그래서 “레드 플래그 먼저 확인” 문장을 넣었어.

### ④ Quickstart는 “한 덩어리”로
명령어가 여기저기 있으면 안 따라 해.  
그래서 “설치→데이터→학습→평가→리포트” 순서로 붙여줬어.

### ⑤ “reports”를 꼭 언급하기
취업 포트폴리오는 **코드**보다 **증거(리포트)**가 더 강해.  
그래서 `reports/summary.md`를 만들게 유도했어.

### ⑥ “What’s inside”는 5줄로 끝
너무 많으면 산만해.  
그래서 면접관이 좋아하는 5개(데이터/분할/모델/평가/리포트)만 남겼어.

---

## 4) (진짜 중요) README에 꼭 추가하면 합격확률 올라가는 3개 파일
이건 README 말고 **파일로 존재**해야 “진짜”가 돼.

1) `reports/summary.md`  
- 결과표 1개 + 그래프 1개 + 실험 설정(시드/분할)

2) `docs/split_policy.md`  
- stratified split인지, time split인지, 유저 단위인지(있으면) 명확히

3) `docs/leakage_checks.md`  
- “SMOTE는 train에만”, “target encoding fit은 train에만” 같은 규칙을 글로 적기
