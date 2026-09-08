"""
Telugu / Tanglish text normalizer.

Owner: Sri Sathyadev (Telugu & Dialect NLP Pipeline)
"""

import re
from week_2.day_1.app.language_detector import detect_language

_VOCAB_MAP = {
    "gunta": "pothole",
    "guntalu": "potholes",
    "current poindi": "power outage",
    "current ledu": "no power supply",
    "neellu ledu": "no water supply",
    "neellu raavatledu": "no water supply",
    "road lo": "on the road",
    "bagundi": "is fine",
    "raledu": "has not arrived",
    "vachindi": "has arrived",
    "cheppandi": "please inform",
}

_TELUGU_GLOSS_MAP = {
    "గుంత": "pothole",
    "రోడ్లో": "on the road",
    "ఉంది": "is there",
    "కరెంట్": "power",
    "నీళ్ళు": "water",
}


def _clean_whitespace_and_case(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def _apply_vocab_map(text: str) -> str:
    lowered = text.lower()
    for phrase, replacement in sorted(_VOCAB_MAP.items(), key=lambda kv: -len(kv[0])):
        lowered = lowered.replace(phrase, replacement)
    return lowered


def _gloss_telugu_script(text: str) -> str:
    for word, gloss in _TELUGU_GLOSS_MAP.items():
        text = text.replace(word, gloss)
    return text


def normalize_text(raw_text: str) -> dict:
    if raw_text is None:
        raise ValueError("raw_text must not be None")

    language = detect_language(raw_text)
    text = _clean_whitespace_and_case(raw_text)

    if language == "te":
        text = _gloss_telugu_script(text)
    else:
        text = _apply_vocab_map(text)

    normalized_text = _clean_whitespace_and_case(text)

    return {
        "raw_text": raw_text,
        "language": language,
        "normalized_text": normalized_text,
    }


if __name__ == "__main__":
    samples = [
        "రోడ్లో పెద్ద గుంత ఉంది",
        "Current poindi 4 hours nundi",
        "There is a large pothole on the road",
    ]
    for s in samples:
        print(normalize_text(s))