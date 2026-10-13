"""Tracker comparison dashboard. One file, Streamlit + Plotly.

    .venv/bin/streamlit run dashboard/dashboard.py        # from the repo root

Answers three questions for one video and one detection source at a time: which tracker
performs best, how the trackers compare on the main metrics, and what their results look like.

Data: the team's evaluator (evaluationScripts/birdeval, run through
benchmark/evaluation/run_birdeval.py) writes benchmark/outputs/reports/birdeval/metrics_per_video.csv
with EVERY metric for every run, variant and similarity; runs_index.csv maps each row back to our
run folder (tracker, parameters). This page joins the two and shows a handful of columns. The
images and videos come from benchmark/experiments/render_all.py. Nothing here computes metrics.

Design: Spoor light theme (.streamlit/config.toml at the repo root), EB Garamond headings,
Geist text; one hue in the charts, the Spoor tracker emphasised in indigo.
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
REPORT = OUTPUTS / "reports" / "birdeval"
VIDEOS = OUTPUTS / "videos"

MAIN = ["HOTA", "AssA", "MOTA", "MOTP", "IDF1", "IDSW", "Frag"]
EXTRA = ["DetA", "DetRe", "DetPr", "AssRe", "AssPr", "n_pred_ids", "n_gt_ids", "id_ratio", "diag_id_changes"]
LABELS = {"HOTA": "HOTA", "AssA": "AssA", "MOTA": "MOTA", "MOTP": "MOTP", "IDF1": "IDF1", "IDSW": "IDSW", "Frag": "Frag",
          "DetA": "DetA", "DetRe": "DetRe", "DetPr": "DetPr", "AssRe": "AssRe", "AssPr": "AssPr",
          "n_pred_ids": "ids", "n_gt_ids": "birds", "id_ratio": "ids / birds", "diag_id_changes": "id changes"}
LOWER_IS_BETTER = {"IDSW", "Frag", "diag_id_changes"}
INTEGER = {"IDSW", "Frag", "n_pred_ids", "n_gt_ids", "diag_id_changes"}
TRACKER_NAMES = {"simplesort": "SimpleSORT (Spoor)", "sort": "SORT", "bytetrack": "ByteTrack", "ocsort": "OC-SORT", "botsort": "BoT-SORT", "cbiou": "C-BIoU"}
SOURCE_NAMES = {"yolo": "Detector output", "gt": "Ground-truth boxes as detections"}
SIMILARITY_NAMES = {("dotd", "per_track"): "DotD, scale = bird size (primary)", ("dotd", "fixed"): "DotD, scale = 9 px", ("dotd", "per_box"): "DotD, scale = box size", ("iou", "none"): "IoU"}
CLIP_BY_VIDEO = {clip["video_id"]: name for name, clip in CLIPS.items()}

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
def load_metrics(metrics_path: str, index_path: str) -> pd.DataFrame:
    """birdeval's per-video metrics joined with our run index (tracker, run, parameters)."""
    metrics = pd.read_csv(metrics_path)
    index = pd.read_csv(index_path)
    index["params"] = index["params"].apply(lambda s: json.loads(s) if isinstance(s, str) else {})
    index["degradation"] = index["degradation"].apply(lambda s: json.loads(s) if isinstance(s, str) else {})
    df = metrics.merge(index, on=["experiment", "input", "video"], how="inner")
    df["clip"] = df["video"].map(CLIP_BY_VIDEO)
    df["is_default"] = df["run"].isin(["real_default", "gt_default"])
    df["max_age"] = df["params"].apply(lambda p: p.get("max_age"))
    df["tentative_threshold"] = df["params"].apply(lambda p: p.get("tentative_threshold"))
    for key in ("drop_rate", "center_noise_px", "false_positives_per_frame"):
        df[key] = df["degradation"].apply(lambda d: d.get(key))
    return df


def tracker_label(tracker: str) -> str:
    return TRACKER_NAMES.get(tracker, tracker)


def metrics_table_html(rows: pd.DataFrame) -> str:
    """Main metrics, a separator, then the detection/association breakdown and counts."""
    best = {m: (rows[m].min() if m in LOWER_IS_BETTER else rows[m].max()) for m in MAIN}

    def fmt(metric, value):
        if pd.isna(value):
            return "-"
        return f"{value:.0f}" if metric in INTEGER else (f"{value:.2f}" if metric == "id_ratio" else f"{value:.3f}")

    def cell(metric, value):
        classes = ("best " if metric in best and value == best[metric] else "") + ("sep" if metric == EXTRA[0] else "")
        return '<td class="' + classes.strip() + '">' + fmt(metric, value) + "</td>"

    head = "<tr><th>Tracker</th>" + "".join(f"<th>{LABELS[m]}</th>" for m in MAIN)
    head += "".join(('<th class="sep">' if m == EXTRA[0] else "<th>") + LABELS[m] + "</th>" for m in EXTRA) + "</tr>"
    body = "".join(f"<tr><td>{r.Tracker}</td>" + "".join(cell(m, getattr(r, m)) for m in MAIN + EXTRA) + "</tr>" for r in rows.itertuples())
    return '<table class="metrics">' + head + body + "</table>"


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
if not (REPORT / "metrics_per_video.csv").exists():
    st.error(f"{REPORT / 'metrics_per_video.csv'} not found. Run `.venv/bin/python benchmark/evaluation/run_birdeval.py` first.")
    st.stop()
df = load_metrics(str(REPORT / "metrics_per_video.csv"), str(REPORT / "runs_index.csv"))

st.markdown('<div class="eyebrow">Spoor · tracker evaluation</div>', unsafe_allow_html=True)
st.title("Tracker comparison")

c1, c2, c3 = st.columns([2, 2, 3])
clip = c1.selectbox("Video", [c for c in CLIPS if c in set(df["clip"])], format_func=lambda c: CLIPS[c]["title"])
sources = [s for s in ("yolo", "gt") if ((df["clip"] == clip) & (df["input"] == s)).any()]
source = c2.selectbox("Detections given to the trackers", sources, format_func=lambda s: SOURCE_NAMES[s])
with c3.expander("Evaluation settings"):
    variant = "matched_final"  # only rows with a detection are scored, for every tracker
    sims = [s for s in SIMILARITY_NAMES if s in set(zip(df["similarity"], df["s_scheme"]))]
    similarity = st.selectbox("Box matching (similarity)", sims, format_func=lambda s: SIMILARITY_NAMES[s],
                              help="DotD = exp(-distance between centers / scale). IoU is harsh on nine-pixel birds.")
    st.markdown(f'<div class="caption">Only rows with a detection are scored (birdeval variant matched_final). Every frame counts, no ignore regions. '
                f'This clip: {CLIPS[clip]["note"]}.</div>', unsafe_allow_html=True)

shown = df[(df["clip"] == clip) & (df["variant"] == variant) & (df["similarity"] == similarity[0]) & (df["s_scheme"] == similarity[1])]
defaults = shown[(shown["input"] == source) & shown["is_default"]].sort_values("HOTA", ascending=False)
if defaults.empty:
    st.warning("No evaluated run for these settings.")
    st.stop()

# --- 1. comparison table
st.header("Which tracker performs best")
st.markdown(f'<div class="caption">{CLIPS[clip]["title"]} · {SOURCE_NAMES[source]} · default parameters of each tracker · best value of the main metrics in indigo. '
            "Higher is better except IDSW, Frag and id changes; MOTP here is the mean similarity of matched pairs (1 = centers coincide).</div>", unsafe_allow_html=True)
chart_table = defaults.assign(Tracker=defaults["tracker"].map(tracker_label))
st.markdown(metrics_table_html(chart_table), unsafe_allow_html=True)

# --- 2. charts
st.header("How they compare")
st.plotly_chart(bar_panels(chart_table, ["HOTA", "IDF1", "MOTA"]), width="stretch")
with st.expander("Metric breakdown: detection versus association (HOTA = sqrt(DetA x AssA))"):
    st.plotly_chart(breakdown(chart_table), width="stretch")

# --- 3. complete tracks at a glance, then videos
st.header("What the results look like")
# plain strings, not pandas scalars: {display name: (tracker folder, run folder)}
runs: dict[str, tuple[str, str]] = {tracker_label(str(t)): (str(t), str(r)) for t, r in zip(defaults["tracker"], defaults["run"])}
st.subheader("Complete tracks on the last frame")
st.markdown('<div class="caption">Each run drawn as trajectories in the track\'s colour with its id at the end; ground truth in green. '
            "A colour change along one path is an identity switch, a coloured line on nothing is a false track, a green line without company is a missed bird.</div>", unsafe_allow_html=True)
images = [(name, RUNS / clip / tracker / run / "tracks.png") for name, (tracker, run) in runs.items()]
images = [(name, path) for name, path in images if path.exists()]
if images:
    for start in range(0, len(images), 3):
        cols = st.columns(3)
        for col, (name, path) in zip(cols, images[start:start + 3]):
            col.image(str(path), caption=name, width="stretch")
else:
    st.info("No track images yet. Run `.venv/bin/python benchmark/experiments/render_all.py --images-only`.")

st.subheader("Videos")
st.markdown('<div class="caption">Tracker boxes and trails in the track\'s colour with its id (thin box = coasting row); ground truth as thin green outlines. '
            "Rendered at half resolution by benchmark/experiments/render_video.py.</div>", unsafe_allow_html=True)
v1, v2 = st.columns(2)
with v1:
    one = st.selectbox("One tracker", list(runs), key="one")
    video = RUNS / clip / runs[one][0] / runs[one][1] / "tracked.mp4"
    if video.exists():
        st.video(str(video))
    else:
        st.info("No video yet for this run. Run `.venv/bin/python benchmark/experiments/render_all.py`.")
with v2:
    left = st.selectbox("Side by side: left", list(runs), key="left")
    right = st.selectbox("Side by side: right", list(runs), index=min(1, len(runs) - 1), key="right")
    (a_tracker, a_run), (b_tracker, b_run) = runs[left], runs[right]
    composite = VIDEOS / clip / f"{a_tracker}_{a_run}__vs__{b_tracker}_{b_run}.mp4"
    if composite.exists():
        st.video(str(composite))
    elif (a_tracker, a_run) == (b_tracker, b_run):
        st.info("Pick two different trackers.")
    elif not CLIPS[clip]["video"].exists():
        st.info("The clip itself is not available here, so this pair cannot be rendered.")
    elif st.button("Render side-by-side video (about a minute)"):
        from experiments.render_video import render

        with st.spinner("Rendering..."):
            render(CLIPS[clip]["video"], [RUNS / clip / a_tracker / a_run / "tracks.csv", RUNS / clip / b_tracker / b_run / "tracks.csv"],
                   [left, right], composite, CLIPS[clip]["gt_tracks"], 0.5)
        st.rerun()

# --- 4. SimpleSORT studies (collapsed)
studies = shown[(shown["tracker"] == "simplesort") & ~shown["is_default"]]
if not studies.empty:
    with st.expander("SimpleSORT parameter and robustness studies (E4, E5)"):
        metric = st.selectbox("Metric", MAIN, format_func=lambda m: LABELS[m], key="studies")
        e5 = shown[(shown["tracker"] == "simplesort") & (shown["input"] == "yolo") & shown["max_age"].notna()]
        if len(e5) > 1:
            grid = e5.pivot_table(index="max_age", columns="tentative_threshold", values=metric)
            fig = go.Figure(go.Heatmap(z=grid.values, x=[str(c) for c in grid.columns], y=[str(i) for i in grid.index],
                                       colorscale=[[0, "#FFFFFF"], [1, INDIGO]], reversescale=metric in LOWER_IS_BETTER,
                                       text=grid.values, texttemplate="%{text:.3f}" if metric not in INTEGER else "%{text:.0f}", colorbar_title=LABELS[metric]))
            fig.update_layout(title="E5: max_age x tentative_threshold, detector output", xaxis_title="tentative_threshold", yaxis_title="max_age",
                              height=360, plot_bgcolor="white", paper_bgcolor="white", font_family="Geist")
            st.plotly_chart(fig, width="stretch")
        e4 = shown[shown["drop_rate"].notna()]
        if not e4.empty:
            curves = e4.groupby(["drop_rate", "center_noise_px", "false_positives_per_frame"], as_index=False)[metric].mean()
            shades = ["#31149C", "#6B55C8", "#9D8CE0", "#C9BCFF", "#7C706A", "#B8AEA8"]
            fig = go.Figure()
            for i, ((noise, fp), part) in enumerate(curves.groupby(["center_noise_px", "false_positives_per_frame"])):
                fig.add_trace(go.Scatter(x=part["drop_rate"], y=part[metric], mode="lines+markers", name=f"noise {noise:g} px, FP {fp:g}/frame",
                                         line=dict(color=shades[i % len(shades)], width=2), marker=dict(size=8)))
            fig.update_layout(title="E4: ground-truth boxes degraded (mean over seeds)", xaxis_title="fraction of detections dropped", yaxis_title=LABELS[metric],
                              height=400, plot_bgcolor="white", paper_bgcolor="white", font_family="Geist", legend=dict(orientation="h", y=-0.25))
            fig.update_xaxes(showgrid=True, gridcolor=BORDER)
            fig.update_yaxes(showgrid=True, gridcolor=BORDER)
            st.plotly_chart(fig, width="stretch")

st.markdown('<div class="caption">Source: benchmark/outputs/reports/birdeval/metrics_per_video.csv (all metrics) joined with runs_index.csv. '
            "After new runs: benchmark/evaluation/run_birdeval.py, then benchmark/experiments/render_all.py for images and videos.</div>", unsafe_allow_html=True)
