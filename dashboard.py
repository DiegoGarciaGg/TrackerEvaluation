"""Tracker evaluation dashboard. One file, Streamlit + Plotly.

    .venv/bin/streamlit run dashboard.py

Reads outputs/reports/summary_rows.json, which evaluation/batch_report.py writes (run it first
if the file is missing or stale). Nothing here computes metrics: it only shows what the
reports contain. Sections: a table of runs, a comparison chart between runs, the robustness
curves (E4), the parameter grid (E5) and the sensitivity to the match distance.

Design: Spoor light theme (see .streamlit/config.toml), EB Garamond for headings, Geist for
text, deep indigo for the main series and lavender for the secondary one.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

SUMMARY = Path(__file__).parent / "outputs" / "reports" / "summary_rows.json"
METRICS = ["HOTA", "AssA", "MOTA", "MOTP_px", "IDF1", "IDSW", "Frag"]
LABELS = {"HOTA": "HOTA", "AssA": "AssA", "MOTA": "MOTA", "MOTP_px": "MOTP (px)", "IDF1": "IDF1", "IDSW": "IDSW", "Frag": "Frag"}
HIGHER_IS_BETTER = {"HOTA": True, "AssA": True, "MOTA": True, "MOTP_px": False, "IDF1": True, "IDSW": False, "Frag": False}

# Spoor light tokens (hex from OKLCH)
INDIGO = "#31149C"     # accent-foreground: main series
LAVENDER = "#C9BCFF"   # primary
PEACH = "#FFCEA3"      # primary-alt
STONE = "#7C706A"      # muted-foreground
BORDER = "#ECE1DA"
PALETTE = [INDIGO, LAVENDER, PEACH, STONE, "#BAABF8", "#EBE3DC"]

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;1,400&family=Geist:wght@400;500&display=swap');
html, body, [class*="css"], .stMarkdown, .stDataFrame { font-family: 'Geist', sans-serif; }
h1, h2, h3 { font-family: 'EB Garamond', serif !important; font-weight: 400 !important; letter-spacing: -0.01em; }
h1 { font-size: 48px !important; } h2 { font-size: 32px !important; } h3 { font-size: 24px !important; }
.eyebrow { font-size: 13px; letter-spacing: 0.02em; text-transform: uppercase; color: #7C706A; }
.caption { font-size: 13px; color: #7C706A; }
.card { background: #FFFFFF; border: 1px solid #ECE1DA; border-radius: 12px; padding: 16px 20px; }
.stat { font-family: 'EB Garamond', serif; font-size: 40px; font-variant-numeric: tabular-nums; color: #27160C; line-height: 1.1; }
</style>
"""


# ----------------------------------------------------------------------------- data


@st.cache_data
def load_rows(path: str) -> pd.DataFrame:
    """One row per (run, reference, view, px, region) with the seven metrics and the run's parameters."""
    records = []
    for item in json.loads(Path(path).read_text()):
        params = item.get("params") or {}
        degradation = item.get("degradation") or {}
        for row in item["rows"]:
            records.append(
                {
                    "clip": item["clip"],
                    "run": item["name"],
                    "group": group_of(item["name"]),
                    "reference": item["reference"],
                    "view": "matched rows" if row["view"] == "observations" else "all rows",
                    "px": row["match_px"],
                    "region": "ignored" if row["ignore_region"] else "none",
                    "max_age": params.get("max_age"),
                    "tentative_threshold": params.get("tentative_threshold"),
                    "drop_rate": degradation.get("drop_rate"),
                    "center_noise_px": degradation.get("center_noise_px"),
                    "false_positives_per_frame": degradation.get("false_positives_per_frame"),
                    "seed": degradation.get("seed"),
                    **{metric: row["metrics"][metric] for metric in METRICS},
                }
            )
    return pd.DataFrame(records)


def group_of(name: str) -> str:
    if name == "frozen_baseline":
        return "E1 frozen baseline"
    if name == "gt_default":
        return "E3 ground truth as detections"
    if name.startswith("gtdeg_"):
        return "E4 degraded ground truth"
    if name.startswith("real_maxage"):
        return "E5 parameter sweep"
    if name == "real_default":
        return "E1/E5 real detections, default parameters"
    return "other"


def select(df: pd.DataFrame, clip: str, reference: str, view: str, px: float, region: str) -> pd.DataFrame:
    """The slice shown everywhere: one row per run under the chosen settings."""
    picked = df[(df["clip"] == clip) & (df.reference == reference) & (df.view == view) & (df.px == px)]
    if (picked.region == region).any():
        picked = picked[picked.region == region]
    return picked.sort_values(["group", "run"]).reset_index(drop=True)


# ----------------------------------------------------------------------------- page

st.set_page_config(page_title="Tracker evaluation", page_icon="◍", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

if not SUMMARY.exists():
    st.error(f"{SUMMARY} not found. Run `.venv/bin/python evaluation/batch_report.py` first.")
    st.stop()
df = load_rows(str(SUMMARY))

st.markdown('<div class="eyebrow">Spoor · tracker-kit-Eval</div>', unsafe_allow_html=True)
st.title("Tracker evaluation")
st.markdown(
    '<div class="caption">Metrics computed with TrackEval (HOTA, CLEAR, Identity) on center-distance matching. '
    "A run is one execution of the tracker; the reference is the hand-labelled ground truth (accuracy) or the cloud export (parity).</div>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Settings")
    clip = st.radio("Clip", sorted(df["clip"].unique()), index=0)
    reference = st.radio("Reference", ["gt", "cloud"], format_func=lambda r: "ground truth (accuracy)" if r == "gt" else "cloud export (parity)")
    view = st.radio("Rows scored", ["matched rows", "all rows"], help="matched rows = only rows with a detection; all rows = coasting rows included")
    px_value = st.select_slider("Match distance (px)", options=sorted(df.px.unique()), value=8.0)
    region = st.radio("Timestamp overlay region", ["ignored", "none"], help="Only the flock clip has one") if clip == "flock" else "none"
    st.markdown('<div class="caption">Higher is better for HOTA, AssA, MOTA and IDF1; lower is better for MOTP, IDSW and Frag.</div>', unsafe_allow_html=True)

shown = select(df, clip, reference, view, px_value, region)
if shown.empty:
    st.warning("No run matches these settings (the 6-column baseline has no matched-rows view).")
    st.stop()

# --- headline: default run vs ground-truth-as-detections
st.header("At a glance")
cols = st.columns(len(METRICS))
default_run = shown[shown.run == "real_default"]
ceiling_run = shown[shown.run == "gt_default"]
for col, metric in zip(cols, METRICS):
    with col:
        value = default_run[metric].iloc[0] if not default_run.empty else float("nan")
        ceiling = ceiling_run[metric].iloc[0] if not ceiling_run.empty else None
        fmt = "{:.0f}" if metric in ("IDSW", "Frag") else "{:.2f}"
        extra = f"ceiling {fmt.format(ceiling)}" if ceiling is not None else ""
        st.markdown(f'<div class="card"><div class="eyebrow">{LABELS[metric]}</div><div class="stat">{fmt.format(value)}</div><div class="caption">{extra}</div></div>', unsafe_allow_html=True)
st.markdown('<div class="caption">Real detections with default parameters; "ceiling" is the same tracker fed the ground-truth boxes as detections.</div>', unsafe_allow_html=True)

# --- table of runs
st.header("Runs")
groups = st.multiselect("Experiment groups", sorted(shown.group.unique()), default=[g for g in sorted(shown.group.unique()) if not g.startswith("E4")])
table = shown[shown.group.isin(groups)]
st.dataframe(
    table[["group", "run", "max_age", "tentative_threshold", "drop_rate", "center_noise_px", "false_positives_per_frame", "seed"] + METRICS]
    .rename(columns=LABELS),
    width="stretch",
    hide_index=True,
)

# --- compare runs on one metric
st.header("Compare runs")
left, right = st.columns([1, 3])
with left:
    metric = st.selectbox("Metric", METRICS, format_func=lambda m: LABELS[m])
    candidates = sorted(table.run.unique())
    chosen = st.multiselect("Runs", candidates, default=[r for r in candidates if r in ("frozen_baseline", "real_default", "gt_default")] or candidates[:3])
with right:
    subset = table[table.run.isin(chosen)]
    fig = px.bar(subset, x="run", y=metric, color="group", color_discrete_sequence=PALETTE, text_auto=".3f" if metric not in ("IDSW", "Frag") else True)
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", yaxis_title=LABELS[metric], xaxis_title="", legend_title="", font_family="Geist")
    st.plotly_chart(fig, width="stretch")

# --- E4 robustness curves
e4 = shown[shown.group == "E4 degraded ground truth"]
if not e4.empty:
    st.header("Robustness to degraded detections (E4)")
    st.markdown('<div class="caption">Ground-truth boxes with a fraction dropped, centers shifted by Gaussian noise, and spurious boxes added. Mean over seeds.</div>', unsafe_allow_html=True)
    metric_e4 = st.selectbox("Metric ", METRICS, format_func=lambda m: LABELS[m], key="e4")
    curves = e4.groupby(["drop_rate", "center_noise_px", "false_positives_per_frame"], as_index=False)[metric_e4].mean()
    curves["setting"] = curves.apply(lambda r: f"noise {r.center_noise_px:g} px, FP {r.false_positives_per_frame:g}/frame", axis=1)
    fig = px.line(curves, x="drop_rate", y=metric_e4, color="setting", markers=True, color_discrete_sequence=PALETTE)
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", xaxis_title="fraction of detections dropped", yaxis_title=LABELS[metric_e4], legend_title="", font_family="Geist")
    fig.update_xaxes(showgrid=True, gridcolor=BORDER)
    fig.update_yaxes(showgrid=True, gridcolor=BORDER)
    st.plotly_chart(fig, width="stretch")

# --- E5 parameter grid
e5 = shown[shown.group.isin(["E5 parameter sweep", "E1/E5 real detections, default parameters"])]
if len(e5) > 1:
    st.header("Parameter sweep (E5)")
    metric_e5 = st.selectbox("Metric  ", METRICS, format_func=lambda m: LABELS[m], key="e5")
    grid = e5.pivot_table(index="max_age", columns="tentative_threshold", values=metric_e5)
    fig = go.Figure(
        go.Heatmap(
            z=grid.values, x=[str(c) for c in grid.columns], y=[str(i) for i in grid.index],
            colorscale=[[0, "#FFFFFF"], [1, INDIGO]], reversescale=not HIGHER_IS_BETTER[metric_e5],
            text=grid.values, texttemplate="%{text:.3f}" if metric_e5 not in ("IDSW", "Frag") else "%{text:.0f}",
            colorbar_title=LABELS[metric_e5],
        )
    )
    fig.update_layout(xaxis_title="tentative_threshold", yaxis_title="max_age", plot_bgcolor="white", paper_bgcolor="white", font_family="Geist")
    st.plotly_chart(fig, width="stretch")

# --- sensitivity to the match distance
st.header("Sensitivity to the match distance")
sens = df[(df["clip"] == clip) & (df.reference == reference) & (df.view == view) & (df.run.isin(chosen))]
if (sens.region == region).any():
    sens = sens[sens.region == region]
metric_px = st.selectbox("Metric   ", METRICS, format_func=lambda m: LABELS[m], key="px")
fig = px.line(sens.sort_values("px"), x="px", y=metric_px, color="run", markers=True, color_discrete_sequence=PALETTE)
fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", xaxis_title="match distance (px)", yaxis_title=LABELS[metric_px], legend_title="", font_family="Geist")
fig.update_xaxes(showgrid=True, gridcolor=BORDER)
fig.update_yaxes(showgrid=True, gridcolor=BORDER)
st.plotly_chart(fig, width="stretch")

st.markdown('<div class="caption">Source: outputs/reports/summary_rows.json. Regenerate with evaluation/batch_report.py after new runs.</div>', unsafe_allow_html=True)
