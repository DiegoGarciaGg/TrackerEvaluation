# Tracker evaluation

Measures how well bird trackers turn per-frame detections into stable identities, on Spoor's
clips with hand-labelled ground truth. The tracker under test is Spoor's SimpleSORT; five
open-source trackers (Roboflow Trackers) run on the same inputs for comparison. One folder per
responsibility:

```
tracker-kit-Eval/
  tracker_kit/        the Spoor tracker kit as delivered: tracker/, run_tracker.py, data/, results/ (its own README inside). Not modified.
  evaluationScripts/  the team's evaluator (birdeval): TrackEval with DotD similarity, variants, all metrics. The metric engine.
  benchmark/          ground truth, clip registry, experiments (run trackers), the bridge to the evaluator, tests, outputs
  dashboard/          the Streamlit dashboard that shows benchmark/outputs/reports/birdeval
  README.md           this file
  requirements.txt, pytest.ini, .gitignore, .streamlit/ (dashboard theme)
```

## Quick start

```
.venv/bin/python -m pip install -r requirements.txt            # plus TrackEval, see benchmark/evaluation/README.md
.venv/bin/python -m pytest -q                                  # benchmark tests (14); evaluationScripts has its own: pytest evaluationScripts/tests
.venv/bin/streamlit run dashboard/dashboard.py                 # the results, already generated
```

To add a run, score it and see it: `benchmark/README.md` has the four commands.

## How the pieces fit

```
tracker_kit/data/*_detections.csv  ─┐
benchmark/ground_truth/*_detections_corrected.csv (GT boxes as detections) ─┤
                                                                           ▼
                 benchmark/experiments/run_experiment.py  (Spoor SimpleSORT or a Roboflow tracker)
                                                                           ▼
                 benchmark/outputs/runs/<clip>/<tracker>/<run>/tracks.csv + manifest
                                                                           ▼
                 benchmark/evaluation/run_birdeval.py  (exports the runs, calls evaluationScripts/birdeval)
                                                                           ▼
                 benchmark/outputs/reports/birdeval/metrics_per_video.csv (all metrics) + runs_index.csv
                 benchmark/experiments/render_all.py -> tracks.png, tracked.mp4 next to each run
                                                                           ▼
                 dashboard/dashboard.py
```

## What the numbers mean

Metrics come from the team's evaluator in `evaluationScripts/` (TrackEval HOTA, Identity and
CLEAR, plus counts and its own diagnostics; `evaluationScripts/METRICS.md` explains every
column). Boxes are matched by DotD, `exp(-distance between centers / s)` with `s` the bird's
size, because the birds are about nine pixels; IoU and a fixed 9 px scale are computed too.
Every frame of every clip is scored, with no ignore regions. The CSV holds every metric for every
run, variant and similarity; the dashboard shows seven of them plus a breakdown. "Detector
output" and "ground-truth boxes as detections" are separate configurations and never mixed in
one table: the second removes detector errors and shows association quality alone.

`benchmark/evaluation/` holds only the bridge to that evaluator (`run_birdeval.py`), the clip
registry and the hashing helpers. The earlier in-house evaluator was removed once the team's
scripts replaced it; its reports and the phase-by-phase notes remain in `benchmark/outputs/docs/`.

## Headline results (HOTA, birdeval, DotD per_track, matched rows)

| clip | detections | best | Spoor SimpleSORT |
|---|---|---|---|
| flock | detector output | C-BIoU 0.265, ByteTrack 0.264 | 0.262 |
| flock | ground-truth boxes | C-BIoU 0.989 | 0.960 |
| turbine | detector output | see dashboard (every frame scored, unlabelled frames count as false positives) | |
| semrev | ground-truth boxes | SimpleSORT | |

With detector output on the flock the top three are within 0.003: the detector finds only 17 % of
the labelled birds, so it is the ceiling. With perfect boxes the Spoor tracker associates well
(one id per bird); its weak point, measured on degraded ground truth, is identity hand-off
between neighbours while a bird is coasting: 10 % of detections dropped multiplies its identity
switches by eight. The full table is
`benchmark/outputs/reports/birdeval/metrics_per_video.csv` (`evaluationScripts/scripts/show_metrics.py`
prints it); the plain-language account is in `benchmark/outputs/docs/INFORME_GENERAL.md` and the
phase-by-phase technical notes in `benchmark/outputs/docs/phase0..phase6` (written with the earlier
evaluator, numbers within a few hundredths of birdeval's).

## Decisions worth knowing

- Flock ground truth covers the first flock only (25 birds); a second flock in the same clip is
  unlabelled and inflates false positives. The `--reference-proximity-px` option of the CLI
  discounts tracker output far from every labelled bird.
- The flock's burnt-in timestamp attracts 471 detector boxes; the team evaluator scores every
  frame without ignore regions, so they count as false positives (the earlier evaluator ignored them).
- Turbine labels cover one bird over frames 53..293; the team evaluator scores all 671 frames.
- Roboflow trackers receive no confidence (our detections have none), BoT-SORT's camera motion
  compensation is off, parameters are library defaults.
- TrackEval's `np.float` / `np.int` are restored as aliases before import; its sources are not patched.
- The venv's `pip` has a stale path: use `.venv/bin/python -m pip`.
