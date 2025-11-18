# Production KPI Dashboard – VBA to Python Migration

Overview

This repository demonstrates a migration from an Excel VBA-based KPI reporting tool to a modern Python web application using Streamlit. It simulates a manufacturing company's internal dashboard for production management, quality control, and operations reporting.

**NEW: Full bilingual support (English + 日本語)!**

Features

- Legacy Excel VBA automation for KPI reporting (VBA modules included)
- Streamlit-based Python application with modular structure
- ✨ **Bilingual UI: English + Japanese (日本語)** with instant language switching
- File upload (.xlsx) and sample data generator
- Filter options (date range, machine, shift)
- KPI cards, charts (matplotlib), data table, and export options
- Language selector in sidebar for easy switching

Screenshots

- screenshot_kpi_cards.png (placeholder)
- screenshot_charts.png (placeholder)
- screenshot_table.png (placeholder)

How to run the VBA version

1. Open the Excel workbook containing the `production_data` sheet and import the VBA modules:
   - `ProductionKPITool.bas`
   - `Helpers.bas`
   - Import the `UserForm.frm` into the VBA editor (or recreate form controls).
2. Ensure the workbook has sheets named `production_data` and `kpi_dashboard`.
3. Run the `RunProductionKPI` macro (or assign to a button).

How to run the Python version

Prerequisites

- Python 3.9+ (3.10 recommended)
- Create and activate virtual environment

Install dependencies:

```powershell
python -m venv .venv; .venv\Scripts\Activate.ps1; pip install -U pip
pip install pandas streamlit matplotlib openpyxl
```

Generate sample data (optional but recommended):

```powershell
python python_app/data/generate_sample_data.py
```

Run the Streamlit app:

```powershell
cd python_app
streamlit run app.py
```

**Bilingual Support:** Once the app launches, use the language selector in the sidebar to switch between English and 日本語 (Japanese).

Project structure

```
/project-root
    README.md
    BILINGUAL_GUIDE.md
    /vba
        ProductionKPITool.bas
        UserForm.frm
        Helpers.bas
    /python_app
        app.py
        i18n.py                    (NEW: Translation module)
        compute_kpis.py
        charts.py
        data_loader.py
        styles.css
        test_i18n.py              (NEW: Translation test script)
        /data
            generate_sample_data.py
            sample_production_data.xlsx (generated via script)
```

Bilingual Features (English + 日本語)

**New in Version 1.0:**
- Language selector in sidebar (top) using `st.sidebar.radio()`
- Instant language switching with automatic UI re-render
- 40+ translation keys covering all UI elements
- Bilingual support in:
  - Page headers and titles
  - Sidebar labels and filters
  - KPI card labels
  - Chart titles and axis labels
  - Error messages
  - Export buttons and file names

**Translation Module (`i18n.py`):**
- Centralized translation dictionary
- Simple `t(key, lang)` function for retrieving translations
- Easy to extend with new languages

**How to test bilingual features:**
```powershell
cd python_app
python test_i18n.py       # Verify translations
streamlit run app.py      # Launch app and switch language in sidebar
```

**For detailed bilingual implementation guide, see: `BILINGUAL_GUIDE.md`**

KPI formulas explanation

- Total Output: Sum of `Output` over filtered records.
- Defect Rate: Total Defects / Total Output (shown as percentage).
- Machine Utilization: 100 - (Total DowntimeMinutes / (shift_minutes * shifts)) * 100.
  - `shift_minutes` is assumed to be 480 (8-hour shift) by default.
  - `shifts` approximated by number of rows in the filtered data.
- Efficiency Score: Output / (Output + Defects)

Use-case scenario

This dashboard is intended for production managers and quality engineers to:

- Monitor daily production output across machines and shifts
- Track defect trends and identify problem machines
- Estimate utilization (time lost due to downtime)
- Export KPI summaries for reporting and accounting

Setup & Development notes

- The Python app is modular: `data_loader.py`, `compute_kpis.py`, and `charts.py`.
- Styles are in `python_app/styles.css` and injected into Streamlit at runtime.
- The sample data generator `python_app/data/generate_sample_data.py` creates a realistic dataset.

Future improvements

- Add user authentication and role-based access
- Persist data to a database and add historical comparisons
- More advanced utilization calculation using shift schedules
- Add interactive charting (Plotly) and drill-downs
- Add unit tests for KPI calculations


