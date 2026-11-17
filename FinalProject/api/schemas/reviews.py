from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    review_item_id: int
    customer_name: str
    score: int
    review_text: str
    review_date: datetime


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    customer_name: Optional[str] = None
    score: Optional[int] = None
    review_text: Optional[str] = None


class Review(ReviewBase):
    review_id: int

    model_config = {"from_attributes": True}