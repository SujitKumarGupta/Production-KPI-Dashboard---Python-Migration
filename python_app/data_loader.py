"""data_loader.py
Functions to load uploaded Excel file or sample dataset.
"""
from io import BytesIO
import pandas as pd
from datetime import datetime


def load_excel(uploaded_file=None, path=None):
    """Load Excel file from an uploaded Streamlit file or a path.

    Returns a pandas DataFrame with expected columns.
    """
    try:
        if uploaded_file is not None:
            # uploaded_file is a BytesIO or UploadedFile (has read())
            bytes_data = uploaded_file.read()
            df = pd.read_excel(BytesIO(bytes_data))
        elif path is not None:
            df = pd.read_excel(path)
        else:
            raise ValueError("No source provided for data load")

        # Normalize columns
        expected = ["Date", "Shift", "Machine", "Output", "Defects", "DowntimeMinutes"]
        missing = [c for c in expected if c not in df.columns]
        if missing:
            raise ValueError(f"Missing columns in data: {missing}")

        df = df[expected].copy()
        # Ensure types
        df["Date"] = pd.to_datetime(df["Date"]).dt.date
        df["Shift"] = df["Shift"].astype(str)
        df["Machine"] = df["Machine"].astype(str)
        df["Output"] = pd.to_numeric(df["Output"], errors="coerce").fillna(0).astype(int)
        df["Defects"] = pd.to_numeric(df["Defects"], errors="coerce").fillna(0).astype(int)
        df["DowntimeMinutes"] = pd.to_numeric(df["DowntimeMinutes"], errors="coerce").fillna(0).astype(int)

        return df
    except Exception:
        raise
