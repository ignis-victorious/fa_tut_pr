#  ______________________
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from .models.models import Item
#  ______________________


app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "world"}


@app.post(path="/items/")
def create_item(item: Item) -> dict[str, str | Item]:
    return {"message": "Item created", "Item": item}


# def main() -> None:
#     print("Hello from fa-tut-pr!")


# if __name__ == "__main__":
#     main()


#  ______________________
#  Import LIBRARIES
#  Import FILES
#  ______________________
