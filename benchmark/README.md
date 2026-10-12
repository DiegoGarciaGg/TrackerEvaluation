# benchmark/

Everything that measures the trackers: the hand-labelled ground truth, the clip registry, the
code that runs trackers and the code that scores them, the tests, and every generated result.
The tracker under test lives in `../tracker_kit/` and is never modified from here.

```
benchmark/
  clips.json         the clip registry: one entry per video (paths, labelled frame range, ignore region, note)
  paths.py           where things are (repo root, tracker_kit, outputs); every script imports it first
  ground_truth/      hand labels per clip + the semrev clip itself, sha256 in SHA256SUMS
  experiments/       RUN trackers: Spoor's SimpleSORT and Roboflow Trackers, degraded detections, sweeps, rendering
  evaluation/        SCORE runs: contracts, adapters, TrackEval metrics, diagnostics, reports
  tests/             44 pytest tests + validation scripts (TrackEval parity, reference cross-check)
  outputs/           generated: runs/, reports/, detections/, store/, docs/
```

## The pipeline, in four commands

```
# 1. run a tracker -> outputs/runs/<clip>/<tracker>/<run>/tracks.csv + tracks.csv.manifest.json
.venv/bin/python benchmark/experiments/run_experiment.py --tracker cbiou \
    --video tracker_kit/data/20251012_164031_1DAC.mp4 \
    --detections tracker_kit/data/20251012_164031_1DAC_detections.csv --detection-source real \
    --out benchmark/outputs/runs/flock/cbiou/real_default/tracks.csv
#    (or many at once: benchmark/experiments/sweep.py --spec benchmark/experiments/specs/<spec>.json --jobs 4)

# 2. score every run against the ground truth -> outputs/reports/runs/, SUMMARY.md, summary_rows.json
.venv/bin/python benchmark/evaluation/batch_report.py --jobs 4

# 3. render what the runs look like -> tracks.png and tracked.mp4 next to each tracks.csv
.venv/bin/python benchmark/experiments/render_all.py

# 4. look at it
.venv/bin/streamlit run dashboard/dashboard.py
```

Run folders are named by what they received and how: `real_default` (detector output, default
parameters), `gt_default` (ground-truth boxes as detections), `real_maxage15_tent3` (parameter
sweep), `gtdeg_drop0.10_noise1.0_fp0.5_seed1` (degraded ground truth). A new tracker is a new
folder under the clip; the batch report and the dashboard discover it.

## outputs/

| folder | content | regenerable? |
|---|---|---|
| `runs/<clip>/<tracker>/<run>/` | `tracks.csv` (10 columns), `tracks.csv.manifest.json` (provenance: input hashes, parameters, library, timing), `tracks.png`, `tracked.mp4` | the CSV is the evidence (hours of compute for the flock); images and videos by `render_all.py` |
| `reports/runs/<clip>/<tracker>__<run>__vs_<ref>.md|.json` | one report per run and reference: metrics at 4/6/8/12 px, both views, with/without region, identity-switch list, per-track table | yes, `batch_report.py` |
| `reports/SUMMARY.md`, `reports/summary_rows.json` | all experiment tables; the JSON feeds the dashboard | yes |
| `detections/` | degraded ground-truth detection files + manifests (deterministic from seed) | yes |
| `store/` | JSONL result store with content-addressed ids and `dataset|video|dimension` references | yes |
| `docs/` | the phase reports written during the work (phase0..phase6) and the plain-language report `INFORME_GENERAL.md` | no, history |

## Ground truth and references

Three references, three claims; every report names the one it makes in its first line:
ground truth = **accuracy**, cloud export = **parity**, a frozen tracker run = **regression**.

| clip | labels | detector output | notes |
|---|---|---|---|
| flock | 25 birds, 10,142 boxes, all 1009 frames; first flock only, a second flock is unlabelled | yes | 9x7 px birds; the burnt-in timestamp (top-left) is ignored by default |
| turbine | 1 bird over frames 53..293 of 671 | yes | accuracy scored on 53..293 only |
| semrev | 2 birds over frames 32..457 of 500, landscape 3840x2160 | no | only ground-truth boxes can be fed to the trackers |

Metrics: TrackEval (pinned commit) HOTA, CLEAR and Identity on center-distance similarity
`s = max(0, 1 - d/T)`, `T = 2 * px`; 8 px by default. Details in `evaluation/README.md`.

## Tests

```
.venv/bin/python -m pytest -q          # from the repo root; pytest.ini points here
```
