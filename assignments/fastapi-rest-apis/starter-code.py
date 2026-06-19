from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items = [
    # Example item:
    # Item(id=1, name='Example', description='A sample item', price=9.99)
]

@app.get('/')
def read_root():
    return {'message': 'Welcome to the FastAPI REST API'}


@app.get('/items/{item_id}')
def read_item(item_id: int):
    # TODO: Find and return the item for the given ID
    raise HTTPException(status_code=404, detail='Item not found')


@app.post('/items')
def create_item(item: Item):
    # TODO: Add validation, save the item, and return the created item
    return item


@app.get('/search')
def search_items(name: Optional[str] = None, max_price: Optional[float] = None):
    # TODO: Filter items by query parameters and return results
    return []
