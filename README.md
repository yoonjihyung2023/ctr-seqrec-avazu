
ctr-seqrec-avazu

Leakage-safe CTR/RecSys benchmark on Avazu with sequential modeling.

Proof

Kaggle 2M rows (Tesla T4)
Test AUC: 0.72659
LogLoss: 0.40009

Why this repo matters
Leakage-safe evaluation: time-based split to avoid future information leakage
Trustworthy sanity check: label-shuffle test should push AUC close to 0.5
Reproducible output: run the pipeline and save metrics to reports/metrics.json
Recruiter-friendly proof: one repo shows data pipeline, training, evaluation, and result reporting
Method

This project is designed as a trustworthy CTR prediction benchmark rather than a leaderboard-only experiment.

Split data by time order
Build features and sequences using past information only
Train and evaluate sequential/recommendation-style CTR models
Verify the pipeline with a label-shuffle sanity check
Quickstart
py -m src.run
type reports\metrics.json

Expected output is a metrics file at:

reports/metrics.json
Evaluation principles
1) Time-based split

Training/validation/test are separated by time so the model does not learn from the future.

2) Label-shuffle sanity check

If training labels are shuffled, performance should collapse toward random guessing.
That is a useful check that the pipeline is not benefitting from leakage.

3) Reproducibility

The goal is not just a single score, but a pipeline that can be rerun and verified.

Example result snapshot
Avazu 2M rows
Tesla T4
Test AUC: 0.72659
LogLoss: 0.40009
Repo structure
src/                # training / evaluation pipeline
reports/            # metrics output
README.md
Who this is for

This repository is useful evidence for roles such as:

ML Engineer
Applied ML Engineer
Recommender Systems / Ranking Engineer
Ads ML / CTR Prediction Engineer
Key takeaway

This is not just “I trained a model.”
It shows evaluation discipline, leakage awareness, reproducibility, and measurable CTR benchmark results.

Related project

Also see ctr-api for a lightweight FastAPI + Docker serving demo that complements this training/evaluation project.
