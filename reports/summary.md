# Experiment Summary

## Best snapshot
| Model | AUC | LogLoss | Split | Seed |
|------|-----|---------|------|------|
| DIN | 0.50 | 8.18 | stratified | 42 |
| SASRec | TBD | TBD | TBD | TBD |
| BERT4Rec | TBD | TBD | TBD | TBD |

## Leakage / Overfit checks (quick)
- Label shuffle sanity check: TBD (expected AUC ~0.5)
- Train-only fit (encoding/scaling): OK
- Resampling only on train: OK
- Split policy documented: README
