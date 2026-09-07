from pydantic import BaseModel
from typing import Optional, List

class ComplaintContract(BaseModel):
    complaint_id: str
    source_channel: str
    language: str
    raw_text: str
    normalized_text: str
    category: str
    department: str
    urgency_score: int
    duplicate_score: Optional[float] = 0.0
    scheme_matches: Optional[List[str]] = []
    confidence: Optional[float] = 0.0
