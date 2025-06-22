#  ______________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from .models.models import Item, ItemResponse
#  ______________________


app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "world"}


@app.post(path="/items/", response_model=ItemResponse)
# Original
# def create_item(item: Item) -> Item:
# return item
# Better
def create_item(item: Item) -> ItemResponse:
    response_data: ItemResponse = ItemResponse(name="Elle", is_offer=False, price=101)
    return response_data  # <-- Return the instance of ItemResponse


# def main() -> None:
#     print("Hello from fa-tut-pr!")


# if __name__ == "__main__":
#     main()


#  ______________________
#  Import LIBRARIES
#  Import FILES
#  ______________________
