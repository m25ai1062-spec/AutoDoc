
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float = 0.0

@app.get('/hello', summary='Hello endpoint', tags=['misc'])
def hello():
    return {'msg': 'Hello World'}

@app.get('/items/{item_id}', summary='Get item', tags=['items'])
def get_item(item_id: int = Path(..., description='ID of the item')):
    return {'id': item_id, 'name': 'Sample', 'price': 9.99}

@app.post('/items', summary='Create item', tags=['items'])
def create_item(item: Item = Body(...)):
    return {'created': True, 'item': item}
