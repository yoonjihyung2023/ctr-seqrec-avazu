# CTR experiment notes: Avazu and local synthetic checks

This repository collects CTR experiment notes and a small synthetic smoke test.
The Kaggle experiment and the local script use different data and serve different purposes.

## Avazu Kaggle experiment

A saved Kaggle notebook loads the first 2,000,000 rows of the Avazu training file,
uses `device_id` as a history key, and constructs samples from the preceding 20 events.
The PyTorch model combines a causal Transformer inspired by SASRec with
current-event-to-history attention inspired by DIN. Target events are split by hour.
The recorded execution output reports a Tesla T4 GPU.

The notebook output currently available is a **training-label shuffle sanity check**:

| Run | Test AUC | Test LogLoss | Status |
| --- | ---: | ---: | --- |
| Training labels shuffled | 0.53265 | 0.45085 | Observed in saved notebook output; diagnostic run, not normal-training performance |
| Normal training, previously reported | 0.72659 | 0.40009 | Original execution output has not been located; not independently verified |

The previously reported normal-run numbers remain in
[`reports/metrics_kaggle_avazu_2m.json`](reports/metrics_kaggle_avazu_2m.json)
as a record, not proof of a reproduced result. The saved Kaggle notebook is not
currently included in this repository, so the Kaggle results cannot be
reproduced from this repository alone.

A time split and a label-shuffle check are useful safeguards, but neither proves
the absence of leakage. `device_id` is a proxy for a user and may be shared;
the available hour field also does not establish event order within an hour.

## Local synthetic smoke test

`python -m src.run` generates synthetic data and computes simple diagnostic
metrics. It does not load Avazu, train the Kaggle model, or reproduce the Kaggle
scores. It writes to `reports/metrics_local_synthetic.json`, leaving the
separate Kaggle result record untouched.

The JSON field names `test_auc` and `test_logloss` are legacy labels in this
synthetic script: it does not create an independent train/test split. The results
are for checking the local experiment workflow, not a held-out benchmark.

### Run locally

```bash
python -m pip install -r requirements.txt
python -m src.run
```

Inspect the synthetic output:

```bash
# macOS / Linux
cat reports/metrics_local_synthetic.json

# Windows PowerShell
Get-Content reports/metrics_local_synthetic.json
```

The synthetic sequence-length notes are in
[`experiments/2026-02-15-seq-len.md`](experiments/2026-02-15-seq-len.md).

## Next verification step

Locate the original normal-training notebook output or rerun the Kaggle
experiment with label shuffling disabled, preserving the code, split settings,
and final test output together. Do not treat the existing JSON summary alone as
independent evidence of the normal-run result.
