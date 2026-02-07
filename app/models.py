from pydantic import BaseModel, Field
from uuid import uuid4

#... is a must required field
class ItemBase(BaseModel):
    name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., ge=0)


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: str


    @staticmethod
    def generate_id()->str:
        return str(uuid4())