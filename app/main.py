from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI Karate Demo")

class Product(BaseModel):
    id: int
    name: str
    price: float

# simple in-memory store for Day 1
products = [
    {"id": 1, "name": "Laptop", "price": 700.0},
    {"id": 2, "name": "Phone", "price": 300.0},
]

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastAPI Karate Demo"}

@app.get("/products", response_model=List[Product])
def list_products():
    return products
