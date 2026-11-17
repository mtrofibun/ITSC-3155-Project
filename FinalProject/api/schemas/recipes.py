from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich


class RecipeBase(BaseModel):
    menu_item_id: int
    ingredient_id: int
    quantity_need: int


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    ingredient_id: Optional[int] = None
    quantity_need: Optional[int] = None


class Recipe(RecipeBase):
    id: int

    model_config = {"from_attributes": True}