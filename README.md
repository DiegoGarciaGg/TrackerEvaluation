# Tracker evaluation

Measures how well bird trackers turn per-frame detections into stable identities, on Spoor's
clips with hand-labelled ground truth. The tracker under test is Spoor's SimpleSORT; five
open-source trackers (Roboflow Trackers) run on the same inputs for comparison. One folder per
responsibility:

```
tracker-kit-Eval/
  tracker_kit/   the Spoor tracker kit as delivered: tracker/, run_tracker.py, data/, results/ (its own README inside). Not modified.
  benchmark/     everything that measures: ground truth, clip registry, experiments (run trackers), evaluation (score runs), tests, outputs
  dashboard/     the Streamlit dashboard that shows benchmark/outputs
  README.md      this file
  requirements.txt, pytest.ini, .gitignore
```

## Quick start

```
.venv/bin/python -m pip install -r requirements.txt            # plus TrackEval, see benchmark/evaluation/README.md
.venv/bin/python -m pytest -q                                  # 44 tests
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
                 benchmark/evaluation/batch_report.py  (TrackEval vs benchmark/ground_truth)
                                                                           ▼
                 benchmark/outputs/reports/summary_rows.json  +  render_all.py -> tracks.png, tracked.mp4
                                                                           ▼
                 dashboard/dashboard.py
```

## What the numbers mean

Every comparison names its claim: against ground truth it is **accuracy**, against the cloud
export **parity**, against a frozen run **regression**. Metrics are TrackEval's (pinned commit)
HOTA, AssA, MOTA, MOTP, IDF1, IDSW and Frag, computed on center-distance matching because the
birds are about nine pixels (8 px by default; 4, 6 and 12 also reported). "Detector output" and
"ground-truth boxes as detections" are separate configurations and never mixed in one table:
the second removes detector errors and shows association quality alone.

## Headline results (HOTA at 8 px, matched rows)

| clip | detections | best | Spoor SimpleSORT |
|---|---|---|---|
| flock | detector output | C-BIoU 0.276, ByteTrack 0.276 | 0.273 |
| flock | ground-truth boxes | C-BIoU 0.990 | 0.962 |
| turbine | detector output | SimpleSORT 0.682 | 0.682 |
| turbine | ground-truth boxes | ByteTrack / C-BIoU 0.996 | 0.992 |
| semrev | ground-truth boxes | SimpleSORT 0.992 | 0.992 |

With detector output on the flock the top three are within 0.003: the detector finds only 17 % of
the labelled birds, so it is the ceiling. With perfect boxes the Spoor tracker associates well
(one id per bird); its weak point, measured on degraded ground truth, is identity hand-off
between neighbours while a bird is coasting: 10 % of detections dropped multiplies its identity
switches by eight. Full tables in `benchmark/outputs/reports/SUMMARY.md`, the plain-language
account in `benchmark/outputs/docs/INFORME_GENERAL.md`, and the phase-by-phase technical notes in
`benchmark/outputs/docs/phase0..phase6`.

## Decisions worth knowing

- Flock ground truth covers the first flock only (25 birds); a second flock in the same clip is
  unlabelled and inflates false positives. The `--reference-proximity-px` option of the CLI
  discounts tracker output far from every labelled bird.
- The flock's burnt-in timestamp is ignored by default (471 detector boxes sit on its digits).
- Turbine labels cover one bird over frames 53..293; accuracy is scored there only.
- Roboflow trackers receive no confidence (our detections have none), BoT-SORT's camera motion
  compensation is off, parameters are library defaults.
- TrackEval's `np.float` / `np.int` are restored as aliases before import; its sources are not patched.
- The venv's `pip` has a stale path: use `.venv/bin/python -m pip`.
