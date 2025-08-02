from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field, model_validator


# === Pydantic models ===
class Reviewer(BaseModel):
    name: str = Field(..., min_length=1)
    email: Optional[EmailStr] = None
    verified: bool = False


class Review(BaseModel):
    book_title: str = Field(..., min_length=1)
    reviewer: Reviewer
    rating: int = Field(..., ge=1, le=5)
    review: str

    @property
    def summary(self) -> str:
        return f"{self.book_title} by {self.reviewer} - {self.rating} stars"

    @model_validator(mode="after")
    def check_verified_for_five_star(self):
        if self.rating == 5 and not self.reviewer.verified:
            raise ValueError("Five-star reviews must be from verified reviewers")
        return self


class ReviewResponse(BaseModel):
    message: str
    data: Review
    summary: str
