from week_2.day_4_to_6.app.orchestrator import PrajaVaniOrchestrator

def test_orchestrator_pipeline_dry_run():
    orchestrator = PrajaVaniOrchestrator()
    dummy_meta = {"source_channel": "voice", "language": "te"}
    
    # Trigger modular pipeline dry-run framework verification checks
    pipeline_output = orchestrator.process_voice_grievance("mock_path.wav", dummy_meta)
    
    assert "transcription" in pipeline_output
    assert "metadata" in pipeline_output
    assert "matched_schemes" in pipeline_output
