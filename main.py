from typing import Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos


class Item(BaseModel):
    name: str
    price: float
    stock: int


# Almacenamiento en memoria (diccionario)
items_db: Dict[int, Item] = {}
next_id = 1


@app.post("/items/")
def create_item(item: Item):
    global next_id
    items_db[next_id] = item
    response = {"id": next_id, **item.dict()}
    next_id += 1
    return response


@app.get("/items/")
def list_items():
    return [{"id": item_id, **item.dict()} for item_id, item in items_db.items()]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return {"id": item_id, **items_db[item_id].dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    items_db[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    del items_db[item_id]
    return {"message": "Elemento eliminado satisfactoriamente"}
