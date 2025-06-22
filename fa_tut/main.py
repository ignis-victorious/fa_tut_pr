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
# def read_item(item_id: int) -> dict[str, int]:
def read_item(item_id: int, q: str) -> dict[str, int | str]:
    return {"item_id": item_id, "query": q}


# def main() -> None:
#     print("Hello from fa-tut-pr!")


# if __name__ == "__main__":
#     main()
