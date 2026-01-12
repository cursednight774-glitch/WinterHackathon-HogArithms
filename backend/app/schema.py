from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    risk_score: float
    verdict: str