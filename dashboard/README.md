# dashboard/

One Streamlit file that answers three questions for one video and one detection source:
which tracker performs best, how the trackers compare, and what their results look like.

```
.venv/bin/streamlit run dashboard/dashboard.py        # from the repo root
```

## What it reads (it computes nothing)

| input | written by |
|---|---|
| `benchmark/outputs/reports/birdeval/metrics_per_video.csv` | `benchmark/evaluation/run_birdeval.py`, which runs the team's evaluator (`evaluationScripts/birdeval`): one row per experiment, input, variant, similarity and video, with every metric (about 50 columns) |
| `benchmark/outputs/reports/birdeval/runs_index.csv` | the same script: maps each (experiment, input, video) to our run folder, tracker, parameters and degradation |
| `benchmark/clips.json` | by hand: the clip registry (titles, paths, notes) |
| `benchmark/outputs/runs/<clip>/<tracker>/<run>/tracks.png` and `tracked.mp4` | `benchmark/experiments/render_all.py` |
| `benchmark/outputs/videos/<clip>/<a>__vs__<b>.mp4` | the dashboard itself, on demand (side-by-side button) |

So after new runs: `run_birdeval.py`, then `render_all.py`, then reload the page. A tracker
appears as soon as it has an evaluated `real_default` or `gt_default` run.

## Sections

1. **Which tracker performs best**: the comparison table. Left of the line, the seven main
   metrics (HOTA, AssA, MOTA, MOTP, IDF1, IDSW, Frag) with the best value in indigo; right of
   the line, the detection/association breakdown (DetA, DetRe, DetPr, AssRe, AssPr), the counts
   (ids, birds, ids / birds) and the evaluator's own `id changes`. MOTP is the mean similarity of
   matched pairs (1 = centers coincide), as birdeval defines it.
2. **How they compare**: HOTA, IDF1 and MOTA as horizontal bars, trackers ordered by HOTA, the
   Spoor tracker in indigo and the others in grey; a DetA versus AssA breakdown in an expander.
3. **What the results look like**: every tracker's complete tracks drawn on the clip's last
   frame (grid), then one tracker's video, then two trackers side by side.
4. **SimpleSORT parameter and robustness studies** (collapsed): the E5 heatmap and the E4 curves.

Controls: video, detections given to the trackers (detector output or ground-truth boxes,
never mixed in one table), and under "Evaluation settings" the variant (which rows are scored)
and the similarity (DotD with the bird's size as scale, DotD with 9 px, or IoU).

## Deploying it (Streamlit Community Cloud)

A plain Streamlit app deploys straight from GitHub: at share.streamlit.io, "Create app", pick
the repository and branch, main file path `dashboard/dashboard.py`. `dashboard/requirements.txt`
(streamlit, plotly, pandas, numpy, pyyaml) sits next to the entrypoint, so Community Cloud uses it
instead of the heavier root `requirements.txt`; the theme is read from `.streamlit/config.toml`
at the repo root. The deployed page shows tables, charts and the complete-track images (the
birdeval CSVs, `clips.json` and `tracks.png` are committed); the videos are not in the repo, so
that section shows a note instead.

## Design

Spoor light theme in `.streamlit/config.toml` at the repo root (tokens converted from OKLCH: page `#FBF7F4`,
cards white, indigo `#31149C`, lavender `#C9BCFF`), EB Garamond for headings and Geist for
text, loaded from Google Fonts in the CSS block at the top of `dashboard.py`. The Streamlit
toolbar (Deploy, menu) is hidden by `toolbarMode = "minimal"`.
