from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


class Item(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)


@app.post("/items")
def post_item(item: Item):
    return {"item received": item}
