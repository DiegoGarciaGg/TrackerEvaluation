# benchmark/outputs/

Everything generated. Nothing here is edited by hand.

| folder | what | made by | in git? |
|---|---|---|---|
| `runs/<clip>/<tracker>/<run>/` | `tracks.csv` (the tracker's output, 10 columns), `tracks.csv.manifest.json` (provenance: input hashes, parameters, library, timing), `tracks.png` (whole run drawn on the last frame), `tracked.mp4` (video with boxes and trails) | `experiments/run_experiment.py`, `render_all.py` | yes, except the mp4 |
| `reports/birdeval/` | `metrics_per_video.csv` (every metric for every run, variant, similarity and video), `metrics_pooled.csv`, `runs_index.csv` (which run folder each row is), `run_info.json`, `config_used.yaml` | `evaluation/run_birdeval.py` | yes |
| `birdeval/` | the runs re-exported in the team evaluator's layout, links to the videos, its metadata cache; working copies only | `evaluation/run_birdeval.py` | no |
| `detections/` | degraded ground-truth detection files with their manifests (seed and parameters); regenerable | `experiments/detection_sources.py` | manifests only |
| `videos/` | side-by-side videos rendered from the dashboard | `dashboard` | no |
| `docs/` | the write-ups of each phase of the work (phase0..phase6) and `INFORME_GENERAL.md`, the plain-language report; history, not regenerated | by hand | yes |

Run names: `real_default` (detector output, default parameters), `gt_default` (ground-truth
boxes as detections), `real_maxage<N>_tent<M>` (parameter sweep), `gtdeg_<...>_seed<s>` (degraded
ground truth).
