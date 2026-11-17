import uuid
from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)

    payment_type = Column(String(50), nullable=False)
    card_4digits = Column(String(4), nullable=True)
    transaction_status = Column(String(50), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)

    order = relationship("Order", back_populates="payments")
