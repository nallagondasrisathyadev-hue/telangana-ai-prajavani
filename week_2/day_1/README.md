# Sri Sathyadev — Telugu & Dialect NLP Pipeline

This module owns speech-to-text, language detection, and text
normalization for the Telangana AI-PrajaVani grievance intake system.

## What it does
Raw citizen input (Telugu script, Tanglish, English, or voice) goes in;
a standardized record comes out:

```python
{
    "raw_text": "<original input>",
    "language": "te" | "tanglish" | "en",
    "normalized_text": "<standardized English-leaning text>",
}
```

## Files
- `app/language_detector.py` — rule-based Telugu/Tanglish/English detector.
- `app/text_normalizer.py` — normalizes raw text using a Telugu-script
  gloss table and a Tanglish/administrative-vocabulary map.
- `app/audio_processor.py` — Whisper-based STT wrapper; feeds transcripts
  straight into the normalizer. Falls back to a labeled offline mock
  when no `OPENAI_API_KEY` is set.

## How another intern calls this module
```python
from week_2.day_1.app.audio_processor import AudioGrievanceProcessor

processor = AudioGrievanceProcessor()
record = processor.transcribe_grievance("citizen_complaint.wav")
```

## Tests 
All 9 tests passing.

## Known limitations
- The Tanglish vocabulary map is a small seed set; needs to grow from
  real complaint samples.
- Live Whisper transcription is untested against real audio in this
  environment — only the offline mock path has been exercised.
- Telugu-script normalization uses a small word-gloss table, not a full
  translation model.