import os
from openai import OpenAI
from pydub import AudioSegment

class AudioGrievanceProcessor:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "mock-key-for-now"))

    def preprocess_audio(self, input_path: str, target_path: str) -> str:
        """Converts incoming multi-channel citizen complaints to optimized 16kHz mono audio channels."""
        try:
            audio = AudioSegment.from_file(input_path)
            audio = audio.set_frame_rate(16000).set_channels(1)
            audio.export(target_path, format="wav")
            return target_path
        except Exception as e:
            return f"Preprocessing checkpoint error payload: {str(e)}"

    def transcribe_grievance(self, audio_path: str) -> dict:
        """Sends the processed audio channel matrix to Whisper API targeting mixed code translation strings."""
        if os.getenv("OPENAI_API_KEY") is None:
            return {
                "text": "రోడ్లో పెద్ద గుంత ఉంది (Fallback Mock Text)",
                "language": "te",
                "status": "offline_mock"
            }
        
        with open(audio_path, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file,
                prompt="Deals with Telangana public grievances in Telugu script or Tanglish expressions like current poindi."
            )
            return {"text": transcript.text, "status": "processed"}

if __name__ == "__main__":
    processor = AudioGrievanceProcessor()
    print("Speech-to-Text extraction pipeline successfully initialized.")
