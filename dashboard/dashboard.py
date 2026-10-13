"""Tracker comparison dashboard. One file, Streamlit + Plotly.

    .venv/bin/streamlit run dashboard/dashboard.py

Answers three questions for one video and one detection source at a time: which tracker
performs best, how the trackers compare on the main metrics, and what their results look like.
Reads benchmark/outputs/reports/summary_rows.json (written by benchmark/evaluation/batch_report.py)
and shows the tracks.png and tracked.mp4 next to each run (written by benchmark/experiments/render_all.py). Nothing here computes
metrics. A new tracker appears automatically once its run is evaluated.

Design: Spoor light theme (.streamlit/config.toml at the repo root, where Streamlit looks for it), EB Garamond headings, Geist text. Charts use
one hue; the Spoor tracker is emphasised in indigo and the others sit in stone grey.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

ROOT = Path(__file__).resolve().parent.parent  # repository root
sys.path.insert(0, str(ROOT / "benchmark"))
from paths import OUTPUTS, RUNS  # noqa: E402  (puts benchmark/ and tracker_kit/ on sys.path)
from evaluation.clips import load_clips  # noqa: E402

CLIPS = load_clips(ROOT)
SUMMARY = OUTPUTS / "reports" / "summary_rows.json"
VIDEOS = OUTPUTS / "videos"
METRICS = ["HOTA", "AssA", "MOTA", "MOTP_px", "IDF1", "IDSW", "Frag"]
EXTRA = ["DetA", "DetRe", "DetPr", "AssRe", "AssPr", "num_tracker_ids", "num_gt_ids"]  # shown to the right of the table
LABELS = {"HOTA": "HOTA", "AssA": "AssA", "MOTA": "MOTA", "MOTP_px": "MOTP (px)", "IDF1": "IDF1", "IDSW": "IDSW", "Frag": "Frag",
          "DetA": "DetA", "DetRe": "DetRe", "DetPr": "DetPr", "AssRe": "AssRe", "AssPr": "AssPr", "num_tracker_ids": "ids", "num_gt_ids": "birds", "id_ratio": "ids / birds"}
LOWER_IS_BETTER = {"MOTP_px", "IDSW", "Frag"}
TRACKER_NAMES = {"simplesort": "SimpleSORT (Spoor)", "sort": "SORT", "bytetrack": "ByteTrack", "ocsort": "OC-SORT", "botsort": "BoT-SORT", "cbiou": "C-BIoU"}
SOURCE_NAMES = {"real": "Detector output", "gt": "Ground-truth boxes as detections"}
CLIP_NAMES = {name: clip["title"] for name, clip in CLIPS.items()}

INDIGO, INDIGO_LIGHT, STONE, BORDER, INK = "#31149C", "#C9BCFF", "#B8AEA8", "#ECE1DA", "#27160C"
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400&family=Geist:wght@400;500&display=swap');
html, body, [class*="css"], .stMarkdown, .stSelectbox, .stRadio, .stExpander, p, label, div[data-baseweb] { font-family: 'Geist', sans-serif; font-size: 18px; }
h1, h2, h3 { font-family: 'EB Garamond', serif !important; font-weight: 400 !important; }
h1 { font-size: 56px !important; } h2 { font-size: 36px !important; margin-top: 1.2em !important; } h3 { font-size: 26px !important; }
.eyebrow { font-size: 15px; letter-spacing: 0.02em; text-transform: uppercase; color: #7C706A; }
.caption { font-size: 16px; color: #7C706A; line-height: 1.5; }
header [data-testid="stToolbar"], [data-testid="stStatusWidget"], #MainMenu { display: none; }
table.metrics { border-collapse: collapse; width: 100%; font-size: 18px; font-variant-numeric: tabular-nums; }
table.metrics th { text-align: right; font-weight: 500; color: #7C706A; padding: 10px 12px; border-bottom: 1px solid #ECE1DA; }
table.metrics td { text-align: right; padding: 10px 12px; border-bottom: 1px solid #ECE1DA; }
table.metrics th:first-child, table.metrics td:first-child { text-align: left; }
table.metrics .sep { border-left: 2px solid #ECE1DA; }
table.metrics .best { font-weight: 600; color: #31149C; }
</style>
"""


# ----------------------------------------------------------------------------- data


@st.cache_data
def load_rows(path: str) -> pd.DataFrame:
    """One row per (run, reference, view, px, region) with the metrics and the run's metadata."""
    records = []
    for item in json.loads(Path(path).read_text()):
        params = item.get("params") or {}
        degradation = item.get("degradation") or {}
        for row in item["rows"]:
            records.append(
                {
                    "clip": item["clip"], "run": item["name"], "reference": item["reference"],
                    "tracker": item.get("tracker", "simplesort"), "library": item.get("library", ""),
                    "source": item.get("detection_source", "unknown"),
                    "is_default": item["name"] in ("real_default", "gt_default"),
                    "view": "matched rows" if row["view"] == "observations" else "all rows",
                    "px": row["match_px"], "region": "ignored" if row["ignore_region"] else "none",
                    "max_age": params.get("max_age"), "tentative_threshold": params.get("tentative_threshold"),
                    "drop_rate": degradation.get("drop_rate"), "center_noise_px": degradation.get("center_noise_px"),
                    "false_positives_per_frame": degradation.get("false_positives_per_frame"),
                    **{m: row["metrics"][m] for m in METRICS + EXTRA},
                }
            )
    return pd.DataFrame(records)


def slice_rows(df: pd.DataFrame, clip: str, reference: str, view: str, px: float) -> pd.DataFrame:
    picked = df[(df["clip"] == clip) & (df.reference == reference) & (df.view == view) & (df.px == px)]
    region = "ignored" if (picked.region == "ignored").any() else "none"
    return picked[picked.region == region]


def tracker_label(tracker: str) -> str:
    return TRACKER_NAMES.get(tracker, tracker)


def metrics_table_html(rows: pd.DataFrame) -> str:
    """The comparison table as HTML: main metrics, a separator, then the detection/association breakdown and counts."""
    extra = ["DetA", "DetRe", "DetPr", "AssRe", "AssPr", "num_tracker_ids", "num_gt_ids", "id_ratio"]
    rows = rows.assign(id_ratio=rows.num_tracker_ids / rows.num_gt_ids.clip(lower=1))
    best = {m: (rows[m].min() if m in LOWER_IS_BETTER else rows[m].max()) for m in METRICS}

    def cell(metric, value):
        if metric in ("MOTP_px", "id_ratio"):
            text = f"{value:.2f}"
        elif metric in ("IDSW", "Frag", "num_tracker_ids", "num_gt_ids"):
            text = f"{value:.0f}"
        else:
            text = f"{value:.3f}"
        classes = ("best " if metric in best and value == best[metric] else "") + ("sep" if metric == extra[0] else "")
        return "<td class=\"" + classes.strip() + "\">" + text + "</td>"

    head = "<tr><th>Tracker</th>" + "".join(f"<th>{LABELS[m]}</th>" for m in METRICS) + "".join(
        "<th class=\"sep\">" + LABELS[m] + "</th>" if m == extra[0] else f"<th>{LABELS[m]}</th>" for m in extra) + "</tr>"
    body = "".join(f"<tr><td>{r.Tracker}</td>" + "".join(cell(m, getattr(r, m)) for m in METRICS + extra) + "</tr>" for r in rows.itertuples())
    return "<table class=\"metrics\">" + head + body + "</table>"


def bar_panels(table: pd.DataFrame, metrics: list[str]) -> go.Figure:
    """Small multiples: one horizontal bar panel per metric, trackers ordered by HOTA, Spoor emphasised."""
    order = table.sort_values("HOTA")["Tracker"].tolist()
    sub = table.set_index("Tracker").loc[order]
    colors = [INDIGO if name.startswith("SimpleSORT") else STONE for name in order]
    fig = make_subplots(rows=1, cols=len(metrics), subplot_titles=[LABELS[m] for m in metrics], shared_yaxes=True, horizontal_spacing=0.04)
    for i, metric in enumerate(metrics, start=1):
        fig.add_trace(go.Bar(x=sub[metric], y=order, orientation="h", marker_color=colors, text=[f"{v:.2f}" for v in sub[metric]],
                             textposition="outside", textfont_color=INK, hovertemplate="%{y}: %{x:.3f}<extra></extra>", showlegend=False), row=1, col=i)
        fig.update_xaxes(showgrid=True, gridcolor=BORDER, zeroline=True, zerolinecolor=BORDER, row=1, col=i)
    fig.update_layout(height=80 + 42 * len(order), margin=dict(l=10, r=30, t=40, b=10), plot_bgcolor="white", paper_bgcolor="white",
                      font_family="Geist", bargap=0.35)
    return fig


def breakdown(table: pd.DataFrame) -> go.Figure:
    """DetA and AssA per tracker in two shades of one hue; HOTA is their geometric mean."""
    order = table.sort_values("HOTA")["Tracker"].tolist()
    sub = table.set_index("Tracker").loc[order]
    fig = go.Figure()
    fig.add_trace(go.Bar(name="DetA (detection)", x=sub["DetA"], y=order, orientation="h", marker_color=INDIGO_LIGHT, hovertemplate="DetA %{x:.3f}<extra>%{y}</extra>"))
    fig.add_trace(go.Bar(name="AssA (association)", x=sub["AssA"], y=order, orientation="h", marker_color=INDIGO, hovertemplate="AssA %{x:.3f}<extra>%{y}</extra>"))
    fig.update_layout(barmode="group", height=80 + 48 * len(order), margin=dict(l=10, r=20, t=10, b=10), plot_bgcolor="white", paper_bgcolor="white",
                      font_family="Geist", legend=dict(orientation="h", y=1.08, x=0), xaxis=dict(range=[0, 1.05], showgrid=True, gridcolor=BORDER))
    return fig


# ----------------------------------------------------------------------------- page

st.set_page_config(page_title="Tracker comparison", page_icon="◍", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)
if not SUMMARY.exists():
    st.error(f"{SUMMARY} not found. Run `.venv/bin/python benchmark/evaluation/batch_report.py` first.")
    st.stop()
df = load_rows(str(SUMMARY))

st.markdown('<div class="eyebrow">Spoor · tracker evaluation</div>', unsafe_allow_html=True)
st.title("Tracker comparison")

c1, c2, c3 = st.columns([2, 2, 3])
clip = c1.selectbox("Video", [c for c in CLIPS if c in set(df["clip"])], format_func=lambda c: CLIP_NAMES.get(c, c))
sources = [s for s in ("real", "gt") if ((df["clip"] == clip) & (df.source == s)).any()]
source = c2.selectbox("Detections given to the trackers", sources, format_func=lambda s: SOURCE_NAMES[s],
                      help="Every tracker receives exactly the same boxes. Ground-truth boxes remove detector errors and show association quality alone. "
                           "A clip without detector output offers only the ground-truth option.")
with c3.expander("Evaluation settings"):
    references = ["gt"] + (["cloud"] if ((df["clip"] == clip) & (df.reference == "cloud")).any() else [])
    reference = st.radio("Reference", references, horizontal=True, format_func=lambda r: "ground truth (accuracy)" if r == "gt" else "cloud export (parity)")
    view = st.radio("Rows scored", ["matched rows", "all rows"], horizontal=True, help="SimpleSORT also writes coasting rows; 'all rows' includes them. Library trackers only emit matched rows.")
    px_value = st.select_slider("Match distance (px)", options=sorted(df.px.unique()), value=8.0)
    st.markdown(f'<div class="caption">Metrics by TrackEval (HOTA, CLEAR, Identity) on center-distance matching. This clip: {CLIPS[clip]["note"]}.</div>', unsafe_allow_html=True)

shown = slice_rows(df, clip, reference, view, px_value)
defaults = shown[(shown.source == source) & shown.is_default].sort_values("HOTA", ascending=False)
if defaults.empty:
    st.warning("No evaluated run for these settings.")
    st.stop()

# --- 1. comparison table
st.header("Which tracker performs best")
st.markdown(f'<div class="caption">{CLIP_NAMES.get(clip, clip)} · {SOURCE_NAMES[source]} · default parameters of each tracker · best value of the main metrics in indigo. '
            "Higher is better except MOTP, IDSW and Frag.</div>", unsafe_allow_html=True)
chart_table = defaults.assign(Tracker=defaults.tracker.map(tracker_label))
st.markdown(metrics_table_html(chart_table), unsafe_allow_html=True)
st.markdown('<div class="caption">Right of the line: DetA = detection accuracy (DetRe recall, DetPr precision); AssRe low = a bird split over several ids, AssPr low = an id jumping between birds; '
            "ids = track ids the tracker produced, birds = labelled birds, ids / birds = 1 is ideal.</div>", unsafe_allow_html=True)

# --- 2. charts
st.header("How they compare")
st.plotly_chart(bar_panels(chart_table, ["HOTA", "IDF1", "MOTA"]), width="stretch")
with st.expander("Metric breakdown: detection versus association (HOTA = sqrt(DetA x AssA))"):
    st.plotly_chart(breakdown(chart_table), width="stretch")

# --- 3. complete tracks at a glance, then videos
st.header("What the results look like")
runs = {tracker_label(r.tracker): r for r in defaults.itertuples()}
st.subheader("Complete tracks on the last frame")
st.markdown('<div class="caption">Each run drawn as trajectories in the track\'s colour with its id at the end; ground truth in green. '
            "A colour change along one path is an identity switch, a coloured line on nothing is a false track, a green line without company is a missed bird.</div>", unsafe_allow_html=True)
images = [(name, RUNS / clip / r.tracker / r.run / "tracks.png") for name, r in runs.items()]
images = [(name, path) for name, path in images if path.exists()]
if images:
    for start in range(0, len(images), 3):
        cols = st.columns(3)
        for col, (name, path) in zip(cols, images[start:start + 3]):
            col.image(str(path), caption=name, width="stretch")
else:
    st.info("No track images yet. Run `.venv/bin/python benchmark/experiments/render_all.py --images-only`.")

st.subheader("Videos")
st.markdown('<div class="caption">Tracker boxes in the track\'s colour with its id (thin = coasting row); ground truth as thin green outlines. '
            "Rendered at half resolution by experiments/render_video.py.</div>", unsafe_allow_html=True)
v1, v2 = st.columns(2)
with v1:
    one = st.selectbox("One tracker", list(runs), key="one")
    video = RUNS / clip / runs[one].tracker / runs[one].run / "tracked.mp4"
    if video.exists():
        st.video(str(video))
    else:
        st.info(f"No video yet for this run. Run `.venv/bin/python benchmark/experiments/render_all.py` (or render_video.py for runs/{clip}/{runs[one].tracker}/{runs[one].run}).")
with v2:
    left = st.selectbox("Side by side: left", list(runs), key="left")
    right = st.selectbox("Side by side: right", list(runs), index=min(1, len(runs) - 1), key="right")
    a, b = runs[left], runs[right]
    composite = VIDEOS / clip / f"{a.tracker}_{a.run}__vs__{b.tracker}_{b.run}.mp4"
    if composite.exists():
        st.video(str(composite))
    elif (a.tracker, a.run) == (b.tracker, b.run):
        st.info("Pick two different trackers.")
    elif not CLIPS[clip]["video"].exists():
        st.info("The clip itself is not available here (videos are not in the repository), so this pair cannot be rendered. Render it locally and commit or upload the result.")
    elif st.button("Render side-by-side video (about a minute)"):
        from experiments.render_video import render

        with st.spinner("Rendering..."):
            render(CLIPS[clip]["video"], [RUNS / clip / a.tracker / a.run / "tracks.csv", RUNS / clip / b.tracker / b.run / "tracks.csv"],
                   [left, right], composite, CLIPS[clip]["gt_tracks"], 0.5)
        st.rerun()

# --- 4. SimpleSORT studies (kept from the earlier experiments, collapsed)
studies = shown[(shown.tracker == "simplesort") & ~shown.is_default]
if not studies.empty:
    with st.expander("SimpleSORT parameter and robustness studies (E4, E5)"):
        metric = st.selectbox("Metric", METRICS, format_func=lambda m: LABELS[m], key="studies")
        e5 = shown[(shown.tracker == "simplesort") & (shown.source == "real") & shown.max_age.notna()]
        if len(e5) > 1:
            grid = e5.pivot_table(index="max_age", columns="tentative_threshold", values=metric)
            fig = go.Figure(go.Heatmap(z=grid.values, x=[str(c) for c in grid.columns], y=[str(i) for i in grid.index],
                                       colorscale=[[0, "#FFFFFF"], [1, INDIGO]], reversescale=metric in LOWER_IS_BETTER,
                                       text=grid.values, texttemplate="%{text:.3f}" if metric not in ("IDSW", "Frag") else "%{text:.0f}", colorbar_title=LABELS[metric]))
            fig.update_layout(title="E5: max_age x tentative_threshold, real detections", xaxis_title="tentative_threshold", yaxis_title="max_age",
                              height=360, plot_bgcolor="white", paper_bgcolor="white", font_family="Geist")
            st.plotly_chart(fig, width="stretch")
        e4 = shown[shown.drop_rate.notna()]
        if not e4.empty:
            curves = e4.groupby(["drop_rate", "center_noise_px", "false_positives_per_frame"], as_index=False)[metric].mean()
            shades = ["#31149C", "#6B55C8", "#9D8CE0", "#C9BCFF", "#7C706A", "#B8AEA8"]
            fig = go.Figure()
            for i, ((noise, fp), part) in enumerate(curves.groupby(["center_noise_px", "false_positives_per_frame"])):
                fig.add_trace(go.Scatter(x=part.drop_rate, y=part[metric], mode="lines+markers", name=f"noise {noise:g} px, FP {fp:g}/frame",
                                         line=dict(color=shades[i % len(shades)], width=2), marker=dict(size=8)))
            fig.update_layout(title="E4: ground-truth boxes degraded (mean over seeds)", xaxis_title="fraction of detections dropped", yaxis_title=LABELS[metric],
                              height=400, plot_bgcolor="white", paper_bgcolor="white", font_family="Geist", legend=dict(orientation="h", y=-0.25))
            fig.update_xaxes(showgrid=True, gridcolor=BORDER)
            fig.update_yaxes(showgrid=True, gridcolor=BORDER)
            st.plotly_chart(fig, width="stretch")

st.markdown('<div class="caption">Source: benchmark/outputs/reports/summary_rows.json and benchmark/clips.json. After new runs: benchmark/evaluation/batch_report.py, then benchmark/experiments/render_all.py for images and videos.</div>', unsafe_allow_html=True)
