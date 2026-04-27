from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.similarity import compare_texts
from utils.pdf_generator import generate_pdf
from fastapi.responses import FileResponse

app = FastAPI(
    title="Plagiarism Detection API",
    description="Backend service for analyzing similarity between reference and suspect texts.",
    version="1.0.0"
)

# Allow frontend connection (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # در نسخه نهایی محدود شود
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisResponse(BaseModel):
    scores: dict
    highlight_ref: str
    highlight_sus: str


@app.get("/")
def root():
    return {"message": "Plagiarism Detection API is running"}


@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_texts(
    reference: str = Form(...),
    suspect: str = Form(...)
):
    # Basic validation
    if not reference.strip() or not suspect.strip():
        raise HTTPException(status_code=400, detail="Both texts must be provided.")

    # Run NLP analysis
    result = compare_texts(reference, suspect)

    return result
