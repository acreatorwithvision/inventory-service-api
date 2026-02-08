from fastapi import FastAPI, HTTPException
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

@app.get("/items/{item_id}",response_model=Item)
def get_item(item_id:str):
    item=inventory_db.get(item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item

@app.put("/items/{item_id}",response_model=Item)
def update_item(item_id:str , updated: ItemCreate):
    existing=inventory_db.get(item_id)

    if not existing:
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated_item=Item(id=item_id, **updated.model_dump())
    inventory_db[item_id]=updated_item

    return updated_item

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in inventory_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del inventory_db[item_id]

    return {"message":"Item deleted Successfully"}