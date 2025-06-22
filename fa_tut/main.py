#  ______________________
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ______________________


app: FastAPI = FastAPI()


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "world"}


# def main() -> None:
#     print("Hello from fa-tut-pr!")


# if __name__ == "__main__":
#     main()
