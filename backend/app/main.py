from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Member 3 imports (AI logic)
from app.ai_core import get_gemini_analysis

# Member 4 imports (validators)
from app.validator import check_domain_age, verify_recruiter_exists

app = FastAPI(title="Credibility Shield API")


# ---------- Request / Response Models ----------

class AnalyzeRequest(BaseModel):
    text: str
    url: Optional[str] = None
    domain: Optional[str] = None
    recruiter_name: Optional[str] = None


class AnalyzeResponse(BaseModel):
    score: int
    verdict: str
    reasons: list[str]


# ---------- Routes ----------

@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest):
    total_score = 0
    reasons = []

    # --- AI ANALYSIS (Member 3) ---
    ai_result = get_gemini_analysis(payload.text)
    total_score += ai_result.get("score", 0)
    reasons.extend(ai_result.get("reasons", []))

    # --- DOMAIN AGE CHECK (Member 4) ---
    if payload.domain:
        domain_result = check_domain_age(payload.domain)
        if domain_result["is_new"]:
            total_score += domain_result["score"]
            reasons.append(domain_result["reason"])

    # --- RECRUITER VERIFICATION (Member 4) ---
    if payload.recruiter_name:
        recruiter_valid = verify_recruiter_exists(payload.recruiter_name)
        if not recruiter_valid:
            total_score += 15
            reasons.append("Recruiter has weak or no online presence")

    # --- FINAL VERDICT ---
    if total_score >= 70:
        verdict = "Likely Scam"
    elif total_score >= 40:
        verdict = "Suspicious"
    else:
        verdict = "Likely Safe"

    return AnalyzeResponse(
        score=min(total_score, 100),
        verdict=verdict,
        reasons=reasons
    )
