"""Streamlit app for Production KPI Dashboard
Run: `streamlit run app.py` from the `python_app` folder.
Bilingual support: English and Japanese.
"""
import streamlit as st
import pandas as pd
from datetime import date
import io
from pathlib import Path

from data_loader import load_excel
from compute_kpis import calculate_kpis
from charts import daily_trend_chart, machine_output_bar_chart, defect_trend_chart
from i18n import t

# UI Setup
st.set_page_config(page_title="Production KPI Dashboard", layout="wide")

# Inject CSS
css_path = Path(__file__).parent / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize language in session state
if "lang" not in st.session_state:
    st.session_state["lang"] = "English"

# Language selector in sidebar (top)
st.sidebar.markdown("---")
st.sidebar.subheader(t("language", st.session_state["lang"]))
lang_choice = st.sidebar.radio(
    "Select language / 言語を選択",
    options=["English", "日本語"],
    key="lang_selector"
)
st.session_state["lang"] = lang_choice
st.sidebar.markdown("---")

# Get current language for easier access
lang = st.session_state["lang"]

st.title(t("title", lang))

# Sidebar
st.sidebar.header(t("data_filters", lang))
uploaded = st.sidebar.file_uploader(t("upload_data", lang), type=["xlsx"])
use_sample = st.sidebar.checkbox(t("use_sample", lang), value=True)

# Load data
df = None
if uploaded is not None:
    try:
        df = load_excel(uploaded_file=uploaded)
    except Exception as e:
        st.sidebar.error(t("error_load_file", lang).format(str(e)))

if df is None and use_sample:
    sample_path = Path(__file__).parent / "data" / "sample_production_data.xlsx"
    if sample_path.exists():
        df = load_excel(path=sample_path)
    else:
        st.sidebar.info(t("error_sample_data", lang))

if df is None:
    st.info(t("error_no_data", lang))
    st.stop()

# Filters
min_date = df["Date"].min()
max_date = df["Date"].max()
start, end = st.sidebar.date_input(t("date_range", lang), value=(min_date, max_date))

machines = [t("all_option", lang)] + sorted(df["Machine"].unique().tolist())
selected_machine = st.sidebar.selectbox(t("machine", lang), machines)

shifts = [t("all_option", lang)] + sorted(df["Shift"].unique().tolist())
selected_shift = st.sidebar.selectbox(t("shift", lang), shifts)

# Apply filters
fdf = df.copy()
if isinstance(start, tuple) or isinstance(start, list):
    start_date = start[0]
    end_date = start[1]
else:
    start_date = start
    end_date = end

all_label = t("all_option", lang)
fdf = fdf[(fdf["Date"] >= start_date) & (fdf["Date"] <= end_date)]
if selected_machine != all_label:
    fdf = fdf[fdf["Machine"] == selected_machine]
if selected_shift != all_label:
    fdf = fdf[fdf["Shift"] == selected_shift]

# KPIs
kpis = calculate_kpis(fdf)

col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    st.markdown("<div class='kpi-card'><div class='kpi-label'>" + t("total_output", lang) + "</div><div class='kpi-value'>" + f"{kpis['total_output']:,}" + "</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='kpi-card'><div class='kpi-label'>" + t("avg_defect_rate", lang) + "</div><div class='kpi-value'>" + f"{kpis['avg_defect_rate']:.2%}" + "</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='kpi-card'><div class='kpi-label'>" + t("machine_utilization", lang) + "</div><div class='kpi-value'>" + f"{kpis['machine_utilization']:.2%}" + "</div></div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='kpi-card'><div class='kpi-label'>" + t("efficiency_score", lang) + "</div><div class='kpi-value'>" + f"{kpis['efficiency_score']:.2%}" + "</div></div>", unsafe_allow_html=True)

st.markdown("---")

# Charts section
st.header(t("charts", lang))
chart1_col, chart2_col = st.columns([2,1])
with chart1_col:
    st.subheader(t("daily_output_trend", lang))
    buf = daily_trend_chart(fdf, value_col="Output", lang=lang)
    st.image(buf)

with chart2_col:
    st.subheader(t("output_by_machine", lang))
    buf2 = machine_output_bar_chart(fdf, lang=lang)
    st.image(buf2)

st.subheader(t("defects_trend", lang))
buf3 = defect_trend_chart(fdf, lang=lang)
st.image(buf3)

# Data table and export
with st.expander(t("filtered_data", lang)):
    st.dataframe(fdf.reset_index(drop=True))
    to_download = st.button(t("download_filtered", lang))
    if to_download:
        towrite = io.BytesIO()
        fdf.to_excel(towrite, index=False)
        towrite.seek(0)
        st.download_button(label=t("download_excel", lang), data=towrite, file_name=t("filtered_file", lang), mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

st.header(t("export_kpi_summary", lang))
if st.button(t("export_button", lang)):
    out = io.BytesIO()
    summary = pd.DataFrame([{
        'StartDate': start_date,
        'EndDate': end_date,
        'Machine': selected_machine,
        'TotalOutput': kpis['total_output'],
        'AvgDefectRate': kpis['avg_defect_rate'],
        'MachineUtilization': kpis['machine_utilization'],
        'EfficiencyScore': kpis['efficiency_score']
    }])
    summary.to_excel(out, index=False)
    out.seek(0)
    st.download_button(t("download_summary", lang), data=out, file_name=t("summary_file", lang), mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

st.write('')

st.markdown(t("notes", lang))
