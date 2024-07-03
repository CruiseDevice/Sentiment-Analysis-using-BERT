from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    
    sentiment: str
    confidence: float
    probabilities: Dict[str, float]


@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    return SentimentResponse(
        sentiment="positive",
        confidence=0.98,
        probabilities=dict(negative=0.005, neutral=0.015, positive=0.98)
    )