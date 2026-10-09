# Tracker evaluation (tracker-kit-Eval)

What this folder is: a research copy of Spoor's tracker kit (`SimpleSORTTracker` from
bird-watcher, standalone, CSV in and CSV out) plus an evaluation framework built around it to
measure the **tracker alone**, not the detector. The kit itself (`tracker/`, `run_tracker.py`,
`data/`, `results/`, the original `README.md`) is untouched; everything new lives in
`evaluation/`, `experiments/`, `tests/`, `ground_truth/` and `outputs/`.

## Goal

Answer, with numbers that can be defended later: how well does the tracker turn per-frame
bird detections into stable identities, where does it fail, and how much of the failure is
the tracker's and how much the detector's.

## Data

| what | where | notes |
|---|---|---|
| flock clip | `data/20251012_164031_1DAC.mp4` | frames 4001..5009 of the original, 1009 frames, 2160x3840 portrait, 25 fps |
| turbine clip | `data/20250920_063942_6C42.mp4` | frames 2000..2670 of the original, 671 frames |
| real detections | `data/*_detections.csv` | birdwatcher rgb_yolo output, no confidence column |
| cloud export | `data/*_cloud_reference_tracks.csv` | another tracker's output: parity reference, not truth |
| frozen baseline | `results/*/baseline_tracks.csv` | the kit's own output on 2026-09-22, default parameters |
| ground truth | `ground_truth/` | hand labels copied from `tracker-kit-Changing/GT`, sha256 in `SHA256SUMS` |

Ground truth facts (verified in Phase 0): the flock labels cover the **first flock only**
(25 birds, 10,142 boxes, boxes about 9x7 px, two thirds with a neighbour closer than 20 px); a
second flock in the same clip is not labelled. The turbine labels cover **one bird** over
frames 53..293. The detector fires 471 times on the burnt-in timestamp at the top-left corner.

## The three references and what a comparison claims

- against ground truth: **accuracy**;
- against the cloud export: **parity** (agreement with another system, not correctness);
- against the frozen baseline: **regression** (did anything change).

Every report prints its claim in the first line.

## Layout

```
dashboard.py    Streamlit dashboard of the metrics (see Dashboard below)
evaluation/     reads finished CSVs + a reference, reports; never runs the tracker (see evaluation/README.md)
experiments/    runs the tracker (unchanged) with provenance; detection sources; sweeps (see experiments/README.md)
tests/          35 pytest tests; tests/validation/ has the TrackEval and reference cross-checks
ground_truth/   the labels + SHA256SUMS
outputs/
  runs/         98 tracker runs, each with tracks.csv + tracks.csv.manifest.json
  detections/   degraded ground-truth detection files + manifests
  store/        JSONL result store, references like flock|20251012_164031_1DAC|gt
  reports/      SUMMARY.md (all experiment tables) + runs/<clip>/<run>__vs_<ref>.md|.json
  phase0..5/    technical summary of each phase; INFORME_GENERAL.md is the plain-language report
```

## How it works, briefly

1. **Contracts** (`evaluation/contracts.py`): `Detection`, `TrackUpdate`, `Track`,
   `Provenance`, `RunResult`, same names and meaning as `spoorpredictioneval.contracts` in
   the company repo, so this can be ported to `edge/evaluation`. A tracker row matched to a
   detection is an observation and a track update; a coasting row (the kit repeats the last
   box for up to 29 frames after losing a bird) is only a track update and never an
   observation. The 6-column baseline cannot tell the two apart; the 10-column format written
   by `experiments/run_experiment.py` can.
2. **Metrics**: TrackEval (pinned commit `12c8791b`) HOTA, CLEAR and Identity, fed directly
   with our similarity `s = max(0, 1 - d/T)` on center distance, `T = 2 * px` (8 px by
   default; 4, 6, 8, 12 reported). IoU is useless for 9-pixel birds. Validated: identical to
   TrackEval's own pipeline with IoU, exact at the configured distance, cross-checked against
   the company's `evaluate_track_quality`.
3. **Diagnostics**: list of every identity switch (frame, bird, ids, position), tracker ids
   per bird, orphan ids, gaps and durations. Hungarian matching with CLEAR's tie-break, so the
   list explains CLEAR's IDSW exactly.
4. **Views and regions**: every 10-column run is scored twice (matched rows only, and every
   row as written) and with and without an ignore region (the timestamp overlay for the
   flock). An optional proximity filter drops tracker output far from every labelled bird, for
   partially labelled clips.

## Commands

```
.venv/bin/python -m pytest -q                                   # 35 tests, ~15 s
.venv/bin/python experiments/run_experiment.py --video data/20251012_164031_1DAC.mp4 \
    --detections data/20251012_164031_1DAC_detections.csv --detection-source real \
    --out outputs/runs/flock/real_default/tracks.csv --check-baseline results/flock/baseline_tracks.csv
.venv/bin/python experiments/sweep.py --spec experiments/specs/e5_params.json --jobs 4
.venv/bin/python evaluation/cli.py --tracks outputs/runs/flock/real_default/tracks.csv \
    --reference ground_truth/20251012_164031_1DAC_reference_tracks_corrected.csv --reference-kind gt \
    --video-id 20251012_164031_1DAC --out outputs/reports/my_report [--reference-proximity-px 50]
.venv/bin/python evaluation/batch_report.py --jobs 4           # rebuild outputs/reports/SUMMARY.md
.venv/bin/python evaluation/quick_metrics.py --gt ground_truth/..._reference_tracks_corrected.csv \
    --tracks results/flock/baseline_tracks.csv --px 8          # standalone, no pipeline
.venv/bin/streamlit run dashboard.py                           # dashboard (reads outputs/reports/summary_rows.json)
```

## Dashboard

`dashboard.py` is a single Streamlit file (theme in `.streamlit/config.toml`, Spoor light
tokens). It shows the seven metrics (HOTA, AssA, MOTA, MOTP px, IDF1, IDSW, Frag) for every
run: an at-a-glance row (default run against its ground-truth ceiling), a filterable table, a
bar chart to compare runs, the E4 robustness curves, the E5 parameter heatmap and the
sensitivity to the match distance. Settings in the sidebar: clip, reference, rows scored, match
distance, timestamp region. It computes nothing: regenerate the JSON with `batch_report.py`
after new runs. Adding a new tracker later means running it through `experiments/` and
re-running the batch report; it then appears in the table and charts.

A flock run of the tracker takes 5 to 11 minutes; the turbine clip takes seconds. The venv's
`pip` has a stale path; use `.venv/bin/python -m pip`.

## Experiments and headline results (8 px, matched rows, overlay ignored)

| experiment | result |
|---|---|
| E1 accuracy, baseline vs GT | flock HOTA 0.273, IDF1 0.180, 156 switches, 35 ids for 25 birds; turbine HOTA 0.68, 0 switches |
| E2 parity, baseline vs cloud | flock IDF1 0.50: the cloud covers 15 % of the labelled birds, not a truth |
| E3 ceiling, GT as detections | flock HOTA 0.962, 25 ids for 25 birds, 17 switches (new-bird entries, one crossing); turbine 0.992 |
| E4 robustness, degraded GT | missed detections dominate: 10 % dropped -> switches x8, 20 % -> HOTA 0.51; 1 px noise harmless; FPs amplify |
| E5 parameters, real detections | HOTA 0.271..0.275 for all 12 settings; tentative_threshold 5 removes noise ids (35 -> 25); max_age 60 = 30 |

Reading: the tracker associates well on good input; with real detections it is limited by a
detector that covers 17 % of the labelled birds, and its own weak point is identity hand-off
between neighbours while a bird is coasting. The unlabelled second flock inflates false
positives (FP 2180 -> 492 with the proximity filter) but changes no conclusion.

## Decisions taken along the way

- Ground truth = first flock only (25 ids); duplicate box at frame 517 and small label gaps kept as is.
- Default ignore region for the flock: rectangle (0,0)-(721,400), the timestamp overlay.
- Turbine accuracy scored on frames 53..293 only.
- TrackEval's `np.float` / `np.int` restored as aliases before import; its sources are not patched.
- Runs on ground-truth-derived detections use `--allow-partial-coverage` (the kit's alignment check refuses a CSV with no box on frame 0 or the last frame).
- `tracker-kit-Changing/bird-mot-eval` ignored, as agreed.

## Open items

- Curves for E4 exist as tables only (no plotting dependency agreed).
- The turbine labels are partial; only recall-side metrics are accuracy there.
- Labelling the second flock would remove the need for the proximity filter.
- Nothing is committed: the folder is not a git repository.
