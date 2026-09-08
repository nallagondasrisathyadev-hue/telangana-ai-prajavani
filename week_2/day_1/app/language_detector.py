"""
Language / script detector for Telugu-Tanglish-English grievance text.

Owner: Sri Sathyadev (Telugu & Dialect NLP Pipeline)
"""

import re

_TELUGU_SCRIPT_RE = re.compile(r"[\u0C00-\u0C7F]")

_TANGLISH_MARKERS = {
    "undi", "ledu", "kada", "bagundi", "gunta", "poindi", "vachindi",
    "cheppandi", "chudandi", "meeru", "nenu", "mee", "vundi", "raledu",
    "kaani", "enti", "ela", "ekkada", "eppudu", "current", "neellu",
}


def detect_language(text: str) -> str:
    if not text or not text.strip():
        return "en"

    if _TELUGU_SCRIPT_RE.search(text):
        return "te"

    tokens = re.findall(r"[a-zA-Z']+", text.lower())
    tanglish_hits = sum(1 for t in tokens if t in _TANGLISH_MARKERS)

    if tanglish_hits > 0:
        return "tanglish"

    return "en"


if __name__ == "__main__":
    samples = [
        "రోడ్లో పెద్ద గుంత ఉంది",
        "Current poindi 4 hours nundi",
        "There is a large pothole on the road",
    ]
    for s in samples:
        print(f"{s!r} -> {detect_language(s)}")