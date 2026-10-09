# evaluation/

Reads finished tracker CSVs plus a reference and reports. Never runs the tracker, never opens a
video. Dependencies: numpy, scipy, TrackEval (pinned commit `12c8791b303e0a0b50f753af204249e622d0281a`,
installed with `.venv/bin/python -m pip install "git+https://github.com/JonathonLuiten/TrackEval@12c8791b303e0a0b50f753af204249e622d0281a"`).

Built to be portable to the repo's `edge/evaluation`: `contracts.py` keeps the names and
meaning of `spoorpredictioneval.contracts` (`Detection`, `TrackUpdate`, `Track`, `Provenance`,
`RunResult`); fields this kit adds are marked `# added` and have defaults.

| module | role |
|---|---|
| `contracts.py` | the vocabulary: observation, track update, track, provenance, run |
| `provenance.py` | mandatory `extra` keys: predictor, claim, dataset, video_id, inputs with sha256, notes |
| `hashing.py` | sha256 of files, of the `tracker/` source tree, of JSON payloads |
| `store.py` | JSONL store with content-addressed ids and `"<dataset>|<video_id>|<dimension>"` references |
| `adapters/` | one adapter per producer: ground truth, cloud export, detector CSV, tracker CSV (6 or 10 columns), MOTChallenge exporter |
| `views.py` | per-frame views (`observations` = matched rows, `updates` = all rows), ignore regions, frame restriction |
| `similarity.py` | `s = max(0, 1 - d/T)`, `T = match_px / (1 - threshold)` (8 px -> T = 16 at threshold 0.5); IoU for validation |
| `trackeval_bridge.py` | feeds views to TrackEval's HOTA, CLEAR and Identity classes directly; numpy alias shim for `np.float` / `np.int` |
| `diagnostics.py` | identity-switch list, ids per object, orphan ids, gaps and durations (Hungarian with CLEAR's tie-break, so switches explain CLEAR's IDSW) |
| `evaluate.py` | one candidate against one reference: metrics table, sensitivity, both views, with/without region, diagnostics; markdown and JSON rendering |
| `cli.py` | report one run from explicit paths |
| `batch_report.py` | evaluate every run under `outputs/runs` and write `outputs/reports/SUMMARY.md` |
| `quick_metrics.py` | standalone script: HOTA/MOTA/IDF1 straight from CSVs, no store or report |

Coasting convention (from the repo's finished surface): a matched row is an observation and a
track update with confidence 1.0; a coasting row is only a track update with confidence 0.0 and
its `missed_frame_count`. The 6-column baseline cannot tell them apart, so its adapter marks
`coasting_known = False` and the matched-rows-only view is refused for it.

Claims: a report names what a comparison asserts from the reference's provenance: `accuracy`
(ground truth), `parity` (cloud export), `regression` (a frozen tracker run).

```
.venv/bin/python evaluation/cli.py --tracks outputs/runs/flock/real_default/tracks.csv \
  --reference ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv --reference-kind gt \
  --video-id 20251012_164031_1DAC --out outputs/reports/my_report
.venv/bin/python evaluation/batch_report.py --jobs 4
.venv/bin/python evaluation/quick_metrics.py --gt ground_truth/..._reference_tracks_corrected.csv --tracks results/flock/baseline_tracks.csv --px 8
.venv/bin/python -m pytest -q
```
