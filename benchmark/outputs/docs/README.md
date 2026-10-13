# benchmark/outputs/docs/

Write-ups of the work, in the order it happened. They were written with the earlier in-house
evaluator (fixed 8 px matching, ignore regions), later replaced by the team's
`evaluationScripts`; their numbers are within a few hundredths of the current ones.

| file | what |
|---|---|
| `phase0/` | data exploration: ground truth inventory, coordinate checks, coasting semantics of the kit, the timestamp-overlay detections (with frames) |
| `phase1/` | contracts, adapters and store of the in-house evaluator |
| `phase2/` | the experiment runner and the byte-for-byte baseline check |
| `phase3/` | metrics and diagnostics |
| `phase4/` | validation: TrackEval parity, exact distance test, cross-check against the company's evaluator |
| `phase5/` | experiments E1..E5 and their reading |
| `phase6/` | dashboard redesign, Roboflow trackers, videos, the semrev clip |
| `INFORME_GENERAL.md` | the whole story in plain language (Spanish) |
