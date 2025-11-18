# Bilingual Implementation Guide

## Overview
The Production KPI Dashboard application has been successfully converted to support both **English** and **Japanese (日本語)** languages with instant switching capability.

## Files Modified

### 1. **i18n.py** (NEW FILE)
A centralized translation module containing:
- Complete translation dictionary with 40+ UI text entries
- Support for English ("en") and Japanese ("jp")
- Helper function `t(key, lang)` to retrieve translations

**Usage:**
```python
from i18n import t
label = t("total_output", "English")  # Returns "Total Output"
label = t("total_output", "日本語")    # Returns "総生産量"
```

### 2. **app.py** (REFACTORED)
Updates include:
- Language selector using `st.sidebar.radio()` at the top of sidebar
- Language stored in `st.session_state["lang"]`
- All UI text wrapped with `t(key, lang)` function
- Instant language switching (no page reload needed)
- Default language: English

**Key Changes:**
- Line 26-39: Language selector initialization and radio button
- Line 42: `lang = st.session_state["lang"]` for convenient access
- All hardcoded strings replaced with translation calls

### 3. **charts.py** (REFACTORED)
Updates include:
- Chart functions now accept `lang` parameter
- Chart titles, axis labels, and legends translated
- Bilingual support for:
  - Daily Output Trend Chart
  - Output by Machine Bar Chart
  - Defects Trend Chart

**Function Signatures:**
```python
def daily_trend_chart(df, value_col="Output", lang="English") -> BytesIO
def machine_output_bar_chart(df, lang="English") -> BytesIO
def defect_trend_chart(df, lang="English") -> BytesIO
```

## Translation Coverage

### Translated Elements
✅ Page title and main headers
✅ Sidebar labels and filters
✅ File upload text
✅ Error messages
✅ Filter options (date, machine, shift)
✅ KPI card labels (Total Output, Defect Rate, etc.)
✅ Chart titles and axis labels
✅ Table headers and export buttons
✅ Footer notes

### Translation Dictionary (i18n.py)
40+ keys organized by category:
- **Page Elements**: title, headers, sidebar
- **File Operations**: upload, sample data, errors
- **Filters**: date_range, machine, shift
- **KPIs**: total_output, defect_rate, utilization, efficiency_score
- **Charts**: titles and axis labels
- **Export**: buttons, file names, summaries
- **Footer**: notes and tips

## How It Works

### Language Switching Flow
1. User selects language from `st.sidebar.radio()`
2. Selection stored in `st.session_state["lang"]`
3. Current language retrieved: `lang = st.session_state["lang"]`
4. All UI text uses: `t(key, lang)`
5. Streamlit automatically re-renders with new language

### Example: Adding New Translations
To add a new translatable element:

```python
# In i18n.py, add to translations dict:
"my_new_key": {
    "en": "English text",
    "jp": "日本語テキスト"
}

# In app.py or charts.py, use:
st.header(t("my_new_key", lang))
```

## Testing the Bilingual App

### Prerequisites
```bash
pip install pandas streamlit matplotlib openpyxl
```

### Run the App
```bash
cd python_app
streamlit run app.py
```

### Test Language Switching
1. Open the app in browser
2. Look for language selector in top of sidebar
3. Click "English" or "日本語" radio button
4. Observe UI text changes instantly:
   - Headers
   - Sidebar labels
   - KPI card labels
   - Chart titles and axis labels
   - Button text
   - Error messages

### Language Test Checklist
- [ ] Title changes (Production KPI Dashboard ↔ 生産KPIダッシュボード)
- [ ] Sidebar filters show correct language
- [ ] KPI cards display translated labels
- [ ] Chart titles are in correct language
- [ ] Axis labels (Date, Machine, Output, etc.) are translated
- [ ] Error messages appear in selected language
- [ ] Export buttons and file names work
- [ ] Language persists across interactions

## Architecture

### Module Dependencies
```
app.py
├── i18n.py (translation dictionary)
├── charts.py (depends on i18n.py)
├── compute_kpis.py
└── data_loader.py
```

### Data Flow
```
User selects language
    ↓
st.session_state["lang"] updated
    ↓
Page re-renders with lang variable
    ↓
All t(key, lang) calls return translated text
    ↓
Charts created with language-specific labels
    ↓
UI displays in selected language
```

## Languages Supported
- **English** (en) - Default language
- **日本語** (Japanese) - jp

## Future Enhancements
- Add more languages (French, German, Chinese, etc.)
- Persist language preference to local storage
- Language-specific number formatting (thousands separator, decimals)
- Timezone support for date/time display
- RTL language support (Arabic, Hebrew)

## Notes for Developers
1. Always use `t()` function for user-visible text
2. Keep translations in `i18n.py` organized by category
3. Test both languages when adding new features
4. Use clear, concise translation keys
5. Avoid putting translated text directly in comments or docstrings (for code clarity)

---
**Last Updated:** November 14, 2025
**Version:** 1.0 (Bilingual Implementation)
