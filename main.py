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

# Crear un nuevo registro


@app.post("/items/")
def create_item(item: Item):
    global next_id
    items_db[next_id] = item
    response = {"id": next_id, **item.dict()}
    next_id += 1
    return response

# Listar todos los registros


@app.get("/items/")
def list_items():
    return [{"id": item_id, **item.dict()} for item_id, item in items_db.items()]

# Obtener un registro por ID


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id].dict()}

# Actualizar un registro


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"id": item_id, **item.dict()}

# Eliminar un registro


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}

# Documentación automática disponible en:
# http://127.0.0.1:8000/docs (Swagger UI)
# http://127.0.0.1:8000/redoc (Redoc)
