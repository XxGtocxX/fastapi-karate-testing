from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI + Karate DSL Project"}

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product():
    data = {"name": "Keyboard", "price": 1200.0}
    response = client.post("/products", json=data)
    assert response.status_code == 200
    product = response.json()
    assert product["name"] == "Keyboard"
    assert product["price"] == 1200.0

def test_update_product():
    # First create a product
    create_response = client.post("/products", json={"name": "Mouse", "price": 600.0})
    product_id = create_response.json()["id"]

    # Update the product
    update_data = {"name": "Gaming Mouse", "price": 999.0}
    response = client.put(f"/products/{product_id}", json=update_data)
    assert response.status_code == 200
    updated = response.json()
    assert updated["name"] == "Gaming Mouse"
    assert updated["price"] == 999.0

def test_delete_product():
    # Create product to delete
    create_response = client.post("/products", json={"name": "Monitor", "price": 12000.0})
    product_id = create_response.json()["id"]

    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Product deleted"}
