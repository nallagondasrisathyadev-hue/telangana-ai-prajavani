from week_2.day_1.app.text_normalizer import normalize_text


def test_normalizes_tanglish_power_outage():
    result = normalize_text("Current poindi 4 hours nundi")
    assert result["language"] == "tanglish"
    assert "power outage" in result["normalized_text"]


def test_normalizes_telugu_script_gloss():
    result = normalize_text("రోడ్లో పెద్ద గుంత ఉంది")
    assert result["language"] == "te"
    assert "pothole" in result["normalized_text"]


def test_preserves_raw_text_untouched():
    raw = "  Current poindi   "
    result = normalize_text(raw)
    assert result["raw_text"] == raw


def test_rejects_none_input():
    import pytest
    with pytest.raises(ValueError):
        normalize_text(None)