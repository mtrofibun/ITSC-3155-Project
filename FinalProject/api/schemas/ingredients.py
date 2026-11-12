from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str
    amount: Decimal
    unit: str


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[Decimal] = None
    unit: Optional[str] = None


class Ingredient(IngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True