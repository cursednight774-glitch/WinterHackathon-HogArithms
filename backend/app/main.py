from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_core import get_gemini_analysis
from app.validator import check_domain_age

app = FastAPI(title="Credibility Shield API")

class AnalyzeRequest(BaseModel):
    text: str
    url: str | None = None

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    ai_result = get_gemini_analysis(req.text)

    domain_result = None
    if req.url:
        domain_result = check_domain_age(req.url)

    return {
        "ai_result": ai_result,
        "domain_result": domain_result
    }
