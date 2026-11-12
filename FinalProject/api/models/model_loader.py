from . import orders, order_details, menu_items, ingredients

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    ingredients.Base.metadata.create_all(engine)
