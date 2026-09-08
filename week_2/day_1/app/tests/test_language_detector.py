from week_2.day_1.app.language_detector import detect_language


def test_detects_telugu_script():
    assert detect_language("రోడ్లో పెద్ద గుంత ఉంది") == "te"


def test_detects_tanglish():
    assert detect_language("Current poindi 4 hours nundi") == "tanglish"


def test_detects_english():
    assert detect_language("There is a large pothole on the road") == "en"


def test_empty_string_defaults_to_english():
    assert detect_language("") == "en"