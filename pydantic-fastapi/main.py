from typing import List

from fastapi import FastAPI, HTTPException

from config import settings
from models import Review, ReviewResponse

# === Fake storage ===
reviews_db: List[Review] = []


app = FastAPI(title=settings.app_name, debug=settings.debug)


# === Routes ===
@app.post("/reviews", response_model=ReviewResponse)
def create_review(review: Review):
    if len(reviews_db) >= settings.max_reviews:
        raise HTTPException(status_code=400, detail="Maximum number of reviews reached")
    reviews_db.append(review)
    return ReviewResponse(
        message="Review received", data=review, summary=review.summary
    )


@app.get("/reviews", response_model=List[Review])
def get_reviews():
    return reviews_db


@app.get("/config")
def get_config():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "max_reviews": settings.max_reviews,
    }
