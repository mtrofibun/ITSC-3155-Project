from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False, default=0)
    unit = Column(String(20), nullable=False)