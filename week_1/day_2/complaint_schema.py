from pydantic import BaseModel
from typing import Optional, List

class ComplaintContract(BaseModel):
    complaint_id: str          # e.g., APV-2026-000123
    source_channel: str        # web / telegram / whatsapp / voice
    language: str              # te / en / tanglish
    raw_text: str
    normalized_text: str
    category: str
    department: str
    urgency_score: int         # 1 to 5
    duplicate_score: Optional[float] = 0.0
    scheme_matches: Optional[List[str]] = []
    confidence: Optional[float] = 0.0
