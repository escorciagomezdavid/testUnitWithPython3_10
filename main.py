# --- Libreria para pruebas PyTest
# --- docs.pytest.org
import json
import uvicorn
from fastapi import FastAPI, Request
from typing import Optional
from services import (read, search, create, update, delete)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/persons")
def read_persons():
    person = read()
    return person


@app.get("/persons/{id}")
def search_person(id: str):
    person = search(id)
    return {
        "status": 200,
        "data": person
    }


@app.post("/persons")
async def create_person(request: Request):
    payload = json.loads(await request.body())
    person = payload["person"]

    create(person)

    return {
        "status": 201,
        "data": "La Persona ha sido Creada"
    }


@app.put("/persons/{id}")
async def update_person(id: str, request: Request):
    payload = json.loads(await request.body())
    person = payload["person"]
    update(id, person)

    return {
        "status": 200,
        "data": "La Persona ha sido Actualizada"
    }


@app.delete("/persons/{id}")
async def delete_person(id: str):
    delete(id)

    return {
        "status": 200,
        "data": "La Persona ha sido Eliminado"
    }


# ---                                    Esto lo uso para debugear
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
