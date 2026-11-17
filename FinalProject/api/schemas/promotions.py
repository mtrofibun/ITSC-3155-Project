from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    code: str
    discount_percent: float
    expiration_date: datetime


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    discount_percent: Optional[float] = None
    expiration_date: Optional[datetime] = None


class Promotion(PromotionBase):
    id: int

    model_config = {"from_attributes": True}