"""i18n.py
Centralized translation dictionary for English and Japanese.
"""

translations = {
    # Page title and headers
    "title": {
        "en": "Production KPI Dashboard — Python Migration",
        "jp": "生産KPIダッシュボード — Python移行版"
    },
    "page_title": {
        "en": "Production KPI Dashboard",
        "jp": "生産KPIダッシュボード"
    },
    "data_filters": {
        "en": "Data & Filters",
        "jp": "データ・フィルター"
    },
    
    # File upload
    "upload_data": {
        "en": "Upload production .xlsx file",
        "jp": "生産 .xlsx ファイルをアップロード"
    },
    "use_sample": {
        "en": "Use sample data",
        "jp": "サンプルデータを使用"
    },
    
    # Error messages
    "error_load_file": {
        "en": "Failed to load uploaded file: {}",
        "jp": "アップロードされたファイルの読み込みに失敗しました: {}"
    },
    "error_sample_data": {
        "en": "Sample data not found. Run `python data/generate_sample_data.py` to create it.",
        "jp": "サンプルデータが見つかりません。`python data/generate_sample_data.py` を実行して作成してください。"
    },
    "error_no_data": {
        "en": "Please upload a valid .xlsx or create sample data.",
        "jp": "有効な .xlsx をアップロードするか、サンプルデータを作成してください。"
    },
    
    # Filter labels
    "date_range": {
        "en": "Date range",
        "jp": "日付範囲"
    },
    "machine": {
        "en": "Machine",
        "jp": "機械"
    },
    "shift": {
        "en": "Shift",
        "jp": "シフト"
    },
    "all_option": {
        "en": "All",
        "jp": "すべて"
    },
    
    # KPI Card labels
    "total_output": {
        "en": "Total Output",
        "jp": "総生産量"
    },
    "avg_defect_rate": {
        "en": "Avg Defect Rate",
        "jp": "平均不良率"
    },
    "machine_utilization": {
        "en": "Machine Utilization",
        "jp": "設備稼働率"
    },
    "efficiency_score": {
        "en": "Efficiency Score",
        "jp": "効率スコア"
    },
    
    # Charts section
    "charts": {
        "en": "Charts",
        "jp": "グラフ"
    },
    "daily_output_trend": {
        "en": "Daily Output Trend",
        "jp": "日別生産量トレンド"
    },
    "output_by_machine": {
        "en": "Output by Machine",
        "jp": "機械別生産量"
    },
    "defects_trend": {
        "en": "Defects Trend",
        "jp": "不良トレンド"
    },
    
    # Chart axis labels
    "date": {
        "en": "Date",
        "jp": "日付"
    },
    "machine": {
        "en": "Machine",
        "jp": "機械"
    },
    "output": {
        "en": "Output",
        "jp": "生産量"
    },
    "total_output": {
        "en": "Total Output",
        "jp": "総生産量"
    },
    "defects": {
        "en": "Defects",
        "jp": "不良"
    },
    
    # Data table and export
    "filtered_data": {
        "en": "Filtered Data",
        "jp": "フィルター済みデータ"
    },
    "download_filtered": {
        "en": "Download filtered data as Excel",
        "jp": "フィルター済みデータをExcelでダウンロード"
    },
    "download_excel": {
        "en": "Download Excel",
        "jp": "Excelをダウンロード"
    },
    "filtered_file": {
        "en": "filtered_production_data.xlsx",
        "jp": "filtered_production_data.xlsx"
    },
    
    # KPI summary export
    "export_kpi_summary": {
        "en": "Export KPI Summary",
        "jp": "KPIサマリーをエクスポート"
    },
    "export_button": {
        "en": "Export KPI to Excel",
        "jp": "KPIをExcelにエクスポート"
    },
    "download_summary": {
        "en": "Download KPI Summary",
        "jp": "KPIサマリーをダウンロード"
    },
    "summary_file": {
        "en": "kpi_summary.xlsx",
        "jp": "kpi_summary.xlsx"
    },
    
    # Footer
    "notes": {
        "en": "**Notes:** This app accepts .xlsx uploads and can use the generator to build a sample dataset.",
        "jp": "**注:** このアプリケーションは .xlsx ファイルをアップロード可能で、ジェネレータを使用してサンプルデータセットを構築できます。"
    },
    
    # Language selector
    "language": {
        "en": "Language",
        "jp": "言語"
    },
}


def t(key: str, lang: str) -> str:
    """Translate a key to the specified language.
    
    Args:
        key: The translation key (e.g., "title", "machine")
        lang: The language code ("en" for English, "jp" for Japanese)
    
    Returns:
        The translated string or the key itself if not found.
    """
    if key not in translations:
        return key
    lang_code = "jp" if lang == "日本語" else "en"
    return translations[key].get(lang_code, key)
