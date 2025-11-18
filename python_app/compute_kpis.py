"""compute_kpis.py
KPI calculation functions used by the Streamlit app.
"""
import pandas as pd


def calculate_kpis(df: pd.DataFrame) -> dict:
    """Calculate KPIs for a filtered DataFrame.

    Returns a dict with Total Output, Avg Defect Rate, Machine Utilization (%), Efficiency Score.
    """
    if df.empty:
        return {
            "total_output": 0,
            "avg_defect_rate": 0.0,
            "machine_utilization": 0.0,
            "efficiency_score": 0.0,
        }

    total_output = df["Output"].sum()
    total_defects = df["Defects"].sum()
    total_downtime = df["DowntimeMinutes"].sum()

    # Defect rate: defects / output (handle zero)
    avg_defect_rate = (total_defects / total_output) if total_output > 0 else 0.0

    # Machine utilization: 100 - (Downtime / (shift_minutes * shifts)) * 100
    # We approximate shifts as number of rows (assuming each row is a shift record)
    shift_minutes = 480
    shifts = max(1, len(df))
    utilization = 100.0 - ((total_downtime / (shift_minutes * shifts)) * 100.0)
    utilization = max(0.0, min(100.0, utilization))

    # Efficiency score: Output / (Output + Defects)
    efficiency_score = (total_output / (total_output + total_defects)) if (total_output + total_defects) > 0 else 0.0

    return {
        "total_output": int(total_output),
        "avg_defect_rate": float(avg_defect_rate),
        "machine_utilization": float(utilization) / 100.0,  # store as fraction
        "efficiency_score": float(efficiency_score),
    }
