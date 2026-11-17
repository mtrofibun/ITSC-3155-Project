from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    payment_type: str
    card_4digits: Optional[str] = None
    transaction_status: str
    amount: Decimal


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None
    card_4digits: Optional[str] = None
    transaction_status: Optional[str] = None
    amount: Optional[Decimal] = None


class Payment(PaymentBase):
    payment_id: int

    model_config = {"from_attributes": True}