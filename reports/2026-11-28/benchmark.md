# CTR chronological benchmark

Rows: 2,000,000; train/validation/test: 1,435,205/416,555/148,240.
Seed: 42; validation starts 2014-10-21 07:00:00; test starts 2014-10-21 09:00:00.

| Model | ROC AUC | LogLoss | Fit + evaluation (s) |
|---|---:|---:|---:|
| Logistic Regression | 0.740531 | 0.396285 | 87.87 |
| LightGBM | 0.720676 | 0.402776 | 48.32 |
| SASRec-DIN-inspired | 0.742281 | 0.392768 | 99.67 |

Train-only categorical mapping; unknown/rare values use index 0.
Histories use strictly earlier hours; within older hours, file order is a deterministic proxy.
All events are scored, including cold-start events. Device ID is a proxy, not verified user identity.
Baselines use current features and past event count; sequential model also uses past event categories.
Validation selects tree iteration and sequence checkpoint; test is for final evaluation.
Single seed; not a direct reproduction of the legacy notebook.
