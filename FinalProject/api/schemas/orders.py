from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_name: str
    customer_phone: str
    customer_address: Optional[str] = None
    order_type: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_address: Optional[str] = None
    order_type: Optional[str] = None
    status: Optional[str] = None


class Order(OrderBase):
    id: int
    tracking_number: str
    status: str
    order_date: Optional[datetime] = None
    total_price: Optional[Decimal] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
