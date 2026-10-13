# benchmark/evaluation/

The scoring side. The metrics themselves are computed by the team's evaluator in
`../../evaluationScripts/` (birdeval: TrackEval HOTA, Identity and CLEAR with DotD and IoU
similarity, several row variants, counts and diagnostics; `evaluationScripts/METRICS.md`
explains every column). This folder only holds the glue:

| file | role |
|---|---|
| `run_birdeval.py` | exports every `outputs/runs/<clip>/<tracker>/<run>/tracks.csv` into birdeval's labelled layout, writes its config, runs it, and leaves `outputs/reports/birdeval/metrics_per_video.csv` (every metric per run, variant, similarity and video), `metrics_pooled.csv`, `run_info.json` and `runs_index.csv` (which run folder, tracker and parameters each row belongs to) |
| `clips.py` | loads `benchmark/clips.json`, the clip registry (paths relative to the repo root, notes) |
| `hashing.py` | sha256 of files, of a source tree and of JSON payloads, used by the run manifests |

How our runs map to birdeval's vocabulary (done by `run_birdeval.py`):

- `input`: `yolo` for detector output, `gt` for ground-truth boxes as detections.
- `experiment`: `<tracker>__<configuration>`, e.g. `simplesort__default`, `cbiou__default`,
  `simplesort__maxage15_tent3`, `simplesort__gtdeg_drop0.10_noise1.0_fp0.5_seed1`.
- rows: our matched rows become `row_type = matched`; SimpleSORT's coasting rows (the last
  matched box repeated) become `row_type = predicted`, so birdeval's `predicted` and `frozen`
  variants coincide for us. Our runner never writes pre-confirmation rows, so `matched_final`
  (the default variant) equals `matched_online`. Every track in our CSVs is confirmed.
- the cloud exports in `tracker_kit/data` are the external reference (`input = cloud`).

```
.venv/bin/python benchmark/evaluation/run_birdeval.py                 # all runs, about 15 minutes
.venv/bin/python benchmark/evaluation/run_birdeval.py --only-defaults  # the default runs only, 2 minutes
.venv/bin/python evaluationScripts/scripts/show_metrics.py benchmark/outputs/reports/birdeval/metrics_per_video.csv
```

Scoring rules inherited from the team evaluator: every frame of every clip is scored, with no
ignore regions and no labelled frame range (the flock's burnt-in timestamp detections and the
turbine's unlabelled frames count as false positives); boxes are matched by DotD
`exp(-d / s)` with `s` the bird's size (primary), a fixed 9 px scale, or IoU.
