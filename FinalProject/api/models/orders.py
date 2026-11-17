import uuid
from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tracking_number = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    customer_name = Column(String(100), nullable=False)
    customer_phone = Column(String(20), nullable=False)
    customer_address = Column(String(200))
    order_type = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False, default="Pending")
    order_date = Column(DATETIME, nullable=False, default=datetime.now)
    total_price = Column(DECIMAL(10, 2), nullable=False, default=0)

    order_details = relationship("OrderDetail", back_populates="order")
    promotions = relationship("Promotions", back_populates="order")
    payments = relationship("Payment", back_populates="order")