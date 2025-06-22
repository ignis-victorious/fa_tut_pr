#  ______________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ______________________


app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "world"}


@app.get(path="/items/{item_id}")
#  Use /items/12345678
# def read_item(item_id: int) -> dict[str, int]:
#  Use /items/12345678?q=erre
def read_item(item_id: int, q: str) -> dict[str, int | str]:
    return {"item_id": item_id, "query": q}


#  use ? / & to change the values: /products/?skip=9 - /products/?skip=11&limit=9
@app.get(path="/products/")
def list_products(skip: int = 0, limit: int = 10) -> dict[str, int]:
    return {"skip": skip, "limit": limit}


# def main() -> None:
#     print("Hello from fa-tut-pr!")


# if __name__ == "__main__":
#     main()
