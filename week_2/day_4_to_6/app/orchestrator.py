from week_2.day_1.app.audio_processor import AudioGrievanceProcessor
from week_2.day_2.app.vector_store import GovSchemeVectorStore
from week_2.day_3.app.metadata_augmenter import MetadataAugmenter

class PrajaVaniOrchestrator:
    def __init__(self):
        self.audio_engine = AudioGrievanceProcessor()
        self.vector_db = GovSchemeVectorStore()
        self.augmenter = MetadataAugmenter()

    def process_voice_grievance(self, raw_audio_path: str, baseline_meta: dict) -> dict:
        """Runs the sequential AI pipeline: Audio Transcribe -> Augment Meta -> Fetch matching RAG rules."""
        # 1. Speech-to-Text Pipeline execution phase
        transcription_data = self.audio_engine.transcribe_grievance(raw_audio_path)
        raw_text = transcription_data["text"]

        # 2. Metadata Enrichment structural calculations phase
        enriched_meta = self.augmenter.augment_complaint_metadata(raw_text, baseline_meta)

        # 3. Vector database context retrieval verification phase
        rag_context = self.vector_db.query_matching_schemes(raw_text, n_results=1)

        return {
            "transcription": raw_text,
            "metadata": enriched_meta,
            "matched_schemes": rag_context.get("documents", [[]])[0]
        }

if __name__ == "__main__":
    engine = PrajaVaniOrchestrator()
    print("Multi-Agent core routing orchestrator dashboard operational.")
