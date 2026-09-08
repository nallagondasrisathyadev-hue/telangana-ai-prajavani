from week_2.day_1.app.audio_processor import AudioGrievanceProcessor


def test_offline_mock_returns_normalized_record():
    processor = AudioGrievanceProcessor()
    result = processor.transcribe_grievance("sample.wav")

    assert result["status"] == "offline_mock"
    assert result["language"] == "te"
    assert "pothole" in result["normalized_text"]
    assert result["source_path"] == "sample.wav"