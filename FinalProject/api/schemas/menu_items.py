from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    calories: Optional[int] = None
    category: Optional[str] = None


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    calories: Optional[int] = None
    category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int

    class ConfigDict:
        from_attributes = True