"""
Speech-to-text wrapper for citizen voice grievances.

Owner: Sri Sathyadev (Telugu & Dialect NLP Pipeline)
"""

import os
from week_2.day_1.app.text_normalizer import normalize_text

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class AudioGrievanceProcessor:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key) if (OpenAI and self.api_key) else None

    def transcribe_grievance(self, audio_path: str) -> dict:
        if self.client is None:
            return self._mock_transcription(audio_path)

        try:
            with open(audio_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                )
            raw_text = transcript.text
            record = normalize_text(raw_text)
            record["status"] = "transcribed"
            record["source_path"] = audio_path
            return record
        except FileNotFoundError:
            return self._mock_transcription(audio_path, status="error_file_not_found")
        except Exception as exc:
            return self._mock_transcription(audio_path, status=f"error_api_failure: {exc}")

    def _mock_transcription(self, audio_path: str, status: str = "offline_mock") -> dict:
        raw_text = "రోడ్లో పెద్ద గుంత ఉంది"
        record = normalize_text(raw_text)
        record["status"] = status
        record["source_path"] = audio_path
        return record


if __name__ == "__main__":
    processor = AudioGrievanceProcessor()
    print(processor.transcribe_grievance("sample.wav"))