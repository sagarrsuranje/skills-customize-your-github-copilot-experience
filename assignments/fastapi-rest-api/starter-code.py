# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = ""

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Add CRUD endpoints below

# Example:
# @app.post("/items/")
# def create_item(item: Item):
#     items.append(item)
#     return item
