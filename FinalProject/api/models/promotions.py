import uuid
from sqlalchemy import Column, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotions(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(100), unique=True, nullable=False)
    discount_percent = Column(float, nullable=False, server_default='0.0')
    expiration_date = Column(datetime,nullable=False)

    orders = relationship("Order", back_populates="promotion")
