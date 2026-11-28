## Latest Benchmark (2026-11-28)

Avazu CTR prediction benchmark using 2 million impressions.

| Model | ROC AUC | LogLoss |
|---|---:|---:|
| Logistic Regression | 0.740531 | 0.396285 |
| LightGBM | 0.720676 | 0.402776 |
| **SASRec-DIN-inspired** | **0.742281** | **0.392768** |

- 0.89% lower LogLoss than Logistic Regression.
- 2.48% lower LogLoss than LightGBM.
- Chronological split, train-only vocabulary and strictly earlier-hour histories.

[Benchmark code and results (ZIP)](github_ctr_update.zip)

Limitations: Single seed, short test window, additional historical features in the sequential model, and unverified statistical significance. This is a separate experiment from the earlier benchmark.

---

# CTR experiment notes: Avazu and local synthetic checks

This repository collects CTR experiment notes and a small synthetic smoke test.
The Kaggle experiment and the local script use different data and serve different purposes.

## Avazu Kaggle experiment

The notebook loads the first 2,000,000 rows of the Avazu competition's `train.gz`,
uses `device_id` as a history key, and constructs each sample from the preceding
20 events. The PyTorch model combines a causal Transformer inspired by SASRec
with current-event-to-history attention inspired by DIN.

**Representative run (2026-11-21).** Normal training on a Tesla T4 yielded
**Test AUC 0.72656** and **Test LogLoss 0.40010** on **125,584 events** in the
internal test split. The target event hour determined the chronological split.
The [execution notebook with saved output](notebooks/avazu-ctr-2m-din-sasrec.ipynb) contains
the code and the epoch-by-epoch and final test results.

| Run | Test AUC | Test LogLoss | Evidence |
| --- | ---: | ---: | --- |
| Normal training, 2026-11-21 | **0.72656** | **0.40010** | Code and saved output in the linked notebook |
| Training labels shuffled | 0.53265 | 0.45085 | Saved output from the earlier diagnostic run |
| Normal training, previously reported | 0.72659 | 0.40009 | [Historical record](reports/metrics_kaggle_avazu_2m.json) with the original output unverified |

The notebook builds the categorical vocabulary before splitting. A `device_id`
is a proxy for a user and may be shared. Events logged in the same hour can
appear in the history window, so their precise order is unavailable.

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
