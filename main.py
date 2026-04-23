from fastapi import FastAPI, HTTPException # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from pydantic import BaseModel # type: ignore
import anthropic # type: ignore
import json
import re
 
app = FastAPI(title="AI Code Review Bot", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
 
client = anthropic.Anthropic()

REVIEW_SYSTEM_PROMPT = """You are an expert code reviewer with deep knowledge of software engineering best practices, design patterns, security vulnerabilities, performance optimization, and clean code principles.
 
Analyze the provided code and return a JSON response ONLY (no markdown, no extra text) with this exact structure:
{
  "summary": "2-3 sentence overall assessment",
  "score": <integer 1-10>,
  "language": "<detected language>",
  "issues": [
    {
      "severity": "critical|high|medium|low|info",
      "category": "security|performance|style|logic|maintainability|bug",
      "line": <line number or null>,
      "title": "short title",
      "description": "detailed explanation",
      "suggestion": "how to fix it"
    }
  ],
  "strengths": ["list", "of", "good", "things"],
  "refactored_snippet": "optional improved version of the most critical section (or null)"
}
 
Be thorough, actionable, and specific. Focus on real issues, not nitpicks."""

class ReviewRequest(BaseModel):
    code: str
    context: str = ""
    language: str = ""

class ReviewResponse(BaseModel):
    summary: str
    score: int
    language: str
    issues: list
    strengths: list
    refactored_snippet: str | None


 
@app.get("/")
def root():
    return {"status": "ok", "service": "AI Code Review Bot"}

@app.post("/review", response_model=ReviewResponse)
def review_code(req: ReviewRequest):
    if not req.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    if len(req.code) > 50_000:
        raise HTTPException(status_code=400, detail="Code too long (max 50,000 chars)")
 
    user_prompt = f"""Review this code{f' ({req.language})' if req.language else ''}:

```
{req.code}
```
{f'Additional context: {req.context}' if req.context else ''}"""

    try:
        message = client.message.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            system=REVIEW_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        raw = message.content[0].text.strip()
        
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)
 
        data = json.loads(raw)
        return ReviewResponse(**data)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse AI response: {e}")
    except anthropic.APIError as e:
        raise HTTPException(status_code=502, detail=f"Anthropic API error: {e}")
 
 
@app.get("/health")
def health():
    return {"status": "healthy"}