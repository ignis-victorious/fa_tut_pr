#  ______________________
#  Import LIBRARIES
from pydantic import BaseModel
#  Import FILES
#  ______________________


class ItemResponse(BaseModel):
    name: str
    price: int
    is_offer: bool = False


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False
    password: str = "Don't show this"
