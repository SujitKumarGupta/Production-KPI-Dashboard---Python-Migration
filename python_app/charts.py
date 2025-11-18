"""charts.py
Chart generation functions using matplotlib.
Each function returns a BytesIO PNG image.
Supports bilingual labels (English and Japanese).
"""
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
from i18n import t


def daily_trend_chart(df: pd.DataFrame, value_col: str = "Output", lang: str = "English") -> BytesIO:
    """Generate daily trend line chart.
    
    Args:
        df: DataFrame with Date and value_col columns
        value_col: Column to plot (e.g., "Output")
        lang: Language code ("English" or "日本語")
    """
    fig, ax = plt.subplots(figsize=(8, 3.5))
    daily = df.groupby("Date")[value_col].sum().reset_index()
    ax.plot(daily["Date"], daily[value_col], marker="o", linewidth=1.5)
    
    # Translate title and axis labels
    title_key = "daily_output_trend" if value_col == "Output" else "defects_trend"
    ax.set_title(t(title_key, lang))
    ax.set_xlabel(t("date", lang))
    ax.set_ylabel(t(value_col.lower() if value_col.lower() in ["output", "defects"] else "output", lang))
    
    fig.autofmt_xdate()
    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf


def machine_output_bar_chart(df: pd.DataFrame, lang: str = "English") -> BytesIO:
    """Generate machine output bar chart.
    
    Args:
        df: DataFrame with Machine and Output columns
        lang: Language code ("English" or "日本語")
    """
    fig, ax = plt.subplots(figsize=(8, 3.5))
    machine = df.groupby("Machine")["Output"].sum().sort_values(ascending=False)
    ax.bar(machine.index, machine.values, color="#5B9BD5")
    ax.set_title(t("output_by_machine", lang))
    ax.set_xlabel(t("machine", lang))
    ax.set_ylabel(t("total_output", lang))
    plt.xticks(rotation=45, ha="right")
    fig.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf


def defect_trend_chart(df: pd.DataFrame, lang: str = "English") -> BytesIO:
    """Generate daily defects trend line chart.
    
    Args:
        df: DataFrame with Date and Defects columns
        lang: Language code ("English" or "日本語")
    """
    fig, ax = plt.subplots(figsize=(8, 3.5))
    daily = df.groupby("Date")["Defects"].sum().reset_index()
    ax.plot(daily["Date"], daily["Defects"], marker="o", color="#F44336")
    ax.set_title(t("defects_trend", lang))
    ax.set_xlabel(t("date", lang))
    ax.set_ylabel(t("defects", lang))
    fig.autofmt_xdate()
    fig.tight_layout()
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)
    return buf
