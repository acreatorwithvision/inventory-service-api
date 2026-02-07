from fastapi import FastAPI
from typing import List

from app.models import Item, ItemCreate

app = FastAPI(title="Inventory Service API")


#Im-memory DB
inventory_db: dict[str, Item]={}


@app.get("/")
def root():
    return {"message": "Inventory API is running"}


@app.post("/items", response_model=Item)
def create_item(item: ItemCreate):
    item_id=Item.generate_id()
    new_item=Item(id=item_id, **item.model_dump())


    inventory_db[item_id]=new_item
    return new_item

@app.get("/items",response_model=List[Item])
def list_items():
    return list(inventory_db.values())