from fastapi import APIRouter
from app.services import analyze_sentiment
from app.models import SentimentRequest, SentimentResponse

router = APIRouter()

@router.post("/sentiment", response_model=SentimentResponse)
def sentiment_endpoint(request: SentimentRequest):
    return analyze_sentiment(request.text)
