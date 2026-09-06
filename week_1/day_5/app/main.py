from fastapi import FastAPI
from week_1.day_2.complaint_schema import ComplaintContract

app = FastAPI(title="Telangana AI-PrajaVani API Baseline")

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

@app.post("/complaints/validate")
def validate_complaint(complaint: ComplaintContract):
    return {"message": "Data adheres to system contract explicitly", "data": complaint}
