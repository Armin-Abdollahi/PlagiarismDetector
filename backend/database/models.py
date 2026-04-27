from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    reference: str
    suspect: str


class ScoreModel(BaseModel):
    lexical: float
    semantic: float
    structure: float


class AnalysisResponse(BaseModel):
    scores: ScoreModel
    highlight_ref: str
    highlight_sus: str
