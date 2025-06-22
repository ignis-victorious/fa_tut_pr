#  ______________________
#  Import LIBRARIES
from pydantic import BaseModel
#  Import FILES
#  ______________________


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False
