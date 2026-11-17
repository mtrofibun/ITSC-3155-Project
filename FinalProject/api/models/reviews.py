from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_item_id = Column(Integer, ForeignKey("items.id"), nullable=False)

    customer_name = Column(String(100), nullable=False)
    score = Column(Integer, nullable=False)
    review_text = Column(String(1000), nullable=False)
    review_date = Column(DateTime, nullable=False, default=datetime.now)