"""
Multi-agent orchestrator (Week 2, Day 4-6).

NOTE: RAG (vector_store) and metadata/routing classification modules
are owned by teammates and are not yet wired in here. This orchestrator
currently only exercises the NLP pipeline (audio -> normalized text).
Full integration happens in Week 3-4.
"""

from week_2.day_1.app.audio_processor import AudioGrievanceProcessor


class PrajaVaniOrchestrator:
    def __init__(self):
        self.audio_engine = AudioGrievanceProcessor()

    def process_voice_grievance(self, raw_audio_path: str, baseline_meta: dict) -> dict:
        """Runs the NLP portion of the pipeline: Audio -> Transcribe -> Normalize."""
        # 1. Speech-to-Text + normalization
        transcription_data = self.audio_engine.transcribe_grievance(raw_audio_path)
        raw_text = transcription_data["normalized_text"]

        return {
            "transcription": raw_text,
            "language": transcription_data["language"],
            "metadata": baseline_meta,
            "matched_schemes": [],  # TODO: wire in RAG engine once available
        }


if __name__ == "__main__":
    engine = PrajaVaniOrchestrator()
    print("NLP-only orchestrator operational (RAG/routing pending Week 3-4 integration).")