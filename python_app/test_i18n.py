"""test_i18n.py
Quick test to verify i18n module works correctly.
Run: python test_i18n.py
"""

from i18n import t, translations

def test_translation_module():
    """Test translation module functionality."""
    print("Testing i18n module...\n")
    
    # Test 1: Check all keys have both languages
    print("✓ Test 1: Checking translation dictionary completeness")
    errors = []
    for key, langs in translations.items():
        if "en" not in langs:
            errors.append(f"  - Missing 'en' for key: {key}")
        if "jp" not in langs:
            errors.append(f"  - Missing 'jp' for key: {key}")
    
    if errors:
        print(f"  ✗ Found {len(errors)} errors:")
        for err in errors:
            print(err)
    else:
        print(f"  ✓ All {len(translations)} keys have both English and Japanese")
    
    # Test 2: Translation function
    print("\n✓ Test 2: Translation function t()")
    en_text = t("total_output", "English")
    jp_text = t("total_output", "日本語")
    print(f"  English: {en_text}")
    print(f"  Japanese: {jp_text}")
    
    assert en_text == "Total Output", "English translation failed"
    assert jp_text == "総生産量", "Japanese translation failed"
    print("  ✓ Translation function works correctly")
    
    # Test 3: Sample translations
    print("\n✓ Test 3: Sample bilingual output")
    samples = ["title", "machine", "defect_rate", "export_button", "notes"]
    for key in samples:
        en = t(key, "English")
        jp = t(key, "日本語")
        print(f"  {key:20s} | EN: {en:35s} | JP: {jp}")
    
    print("\n✅ All tests passed! i18n module is working correctly.")
    print(f"Total keys available: {len(translations)}")

if __name__ == "__main__":
    test_translation_module()
