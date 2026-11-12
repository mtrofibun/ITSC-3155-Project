from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(300))
    price = Column(DECIMAL(6, 2), nullable=False)
    calories = Column(Integer)
    category = Column(String(50))

    order_details = relationship("OrderDetail", back_populates="menu_item")