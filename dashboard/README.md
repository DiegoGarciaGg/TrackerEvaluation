# dashboard/

One Streamlit file that answers three questions for one video and one detection source:
which tracker performs best, how the trackers compare, and what their results look like.

```
.venv/bin/streamlit run dashboard/dashboard.py        # from the repo root
```

## What it reads (it computes nothing)

| input | written by |
|---|---|
| `benchmark/outputs/reports/summary_rows.json` | `benchmark/evaluation/batch_report.py` (one entry per evaluated run: clip, tracker, run, detection source, metrics at every distance and view) |
| `benchmark/clips.json` | by hand: the clip registry (titles, paths, notes) |
| `benchmark/outputs/runs/<clip>/<tracker>/<run>/tracks.png` and `tracked.mp4` | `benchmark/experiments/render_all.py` |
| `benchmark/outputs/videos/<clip>/<a>__vs__<b>.mp4` | the dashboard itself, on demand (side-by-side button) |

So after new runs: `batch_report.py`, then `render_all.py`, then reload the page. A tracker
appears as soon as it has an evaluated `real_default` or `gt_default` run.

## Sections

1. **Which tracker performs best**: the comparison table. Left of the line, the seven main
   metrics (HOTA, AssA, MOTA, MOTP px, IDF1, IDSW, Frag) with the best value in indigo; right of
   the line, the detection/association breakdown (DetA, DetRe, DetPr, AssRe, AssPr) and the
   counts (ids, birds, ids / birds).
2. **How they compare**: HOTA, IDF1 and MOTA as horizontal bars, trackers ordered by HOTA, the
   Spoor tracker in indigo and the others in grey; a DetA versus AssA breakdown in an expander.
3. **What the results look like**: every tracker's complete tracks drawn on the clip's last
   frame (grid), then one tracker's video, then two trackers side by side.
4. **SimpleSORT parameter and robustness studies** (collapsed): the E5 heatmap and the E4 curves.

Controls: video, detections given to the trackers (detector output or ground-truth boxes,
never mixed in one table), and under "Evaluation settings" the reference, the rows scored and
the match distance.

## Deploying it (Streamlit Community Cloud)

The dashboard is a plain Streamlit app, so it deploys straight from GitHub:

1. Push the repo (the branch you want to show).
2. Go to share.streamlit.io, sign in with GitHub, click "Create app", pick the repository and
   branch, and set the main file path to `dashboard/dashboard.py`.
3. Dependencies: `dashboard/requirements.txt` (streamlit, plotly, pandas, numpy) is next to the
   entrypoint, so Community Cloud uses it instead of the heavier root `requirements.txt`.
   The theme is read from `.streamlit/config.toml` at the repo root (Cloud runs from the root).

What the deployed page shows: the tables, the charts and the complete-track images, because
`summary_rows.json`, `clips.json` and the `tracks.png` files are committed. The videos are not
(they are gitignored, hundreds of megabytes), so the video section shows a note instead; to
publish videos, store them with Git LFS or on external hosting and point `st.video` at the URL.

## Design

Spoor light theme in `.streamlit/config.toml` at the repo root (tokens converted from OKLCH: page `#FBF7F4`,
cards white, indigo `#31149C`, lavender `#C9BCFF`), EB Garamond for headings and Geist for
text, loaded from Google Fonts in the CSS block at the top of `dashboard.py`. The Streamlit
toolbar (Deploy, menu) is hidden by `toolbarMode = "minimal"`.
