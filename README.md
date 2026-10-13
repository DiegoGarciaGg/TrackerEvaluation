# Tracker evaluation

Measures how well bird trackers turn per-frame detections into stable identities, on Spoor's
clips with hand-labelled ground truth, and shows the comparison in a dashboard. Every folder has
its own README saying what is inside and why.

```
tracker-kit-Eval/
  tracker_kit/        Spoor's tracker kit as delivered (the tracker under test). Not modified.
  evaluationScripts/  the team's evaluator (birdeval): computes every metric. Its README and METRICS.md explain the columns.
  benchmark/          ground truth, clip registry, scripts that run trackers, the bridge to the evaluator, tests, outputs
  dashboard/          the Streamlit page that shows the results
  .streamlit/         dashboard theme (Streamlit reads it from the folder you run from, so it stays here)
  requirements.txt    Python dependencies (TrackEval and Roboflow Trackers: see benchmark/evaluation/README.md)
  pytest.ini          where the tests are; pyrightconfig.json tells the editor where imports resolve
```

## Quick start

```
.venv/bin/python -m pytest -q                              # tests
.venv/bin/streamlit run dashboard/dashboard.py             # the results, already generated
```

To run a tracker, score it and see it: the four commands in `benchmark/README.md`.

## Where the numbers come from

`benchmark/outputs/runs/<clip>/<tracker>/<run>/tracks.csv` (tracker output with provenance) ->
`benchmark/evaluation/run_birdeval.py` (the team evaluator) ->
`benchmark/outputs/reports/birdeval/metrics_per_video.csv` (all metrics) -> `dashboard/dashboard.py`.
The plain-language report is `benchmark/outputs/docs/INFORME_GENERAL.md`.
