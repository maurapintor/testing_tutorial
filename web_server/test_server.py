from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_item_valid():
    response = client.post("/items/", json={"name": "Book", "price": 5})
    assert response.status_code == 200


def test_create_item_invalid():
    response = client.post("/items/", json={"name": "A", "price": -5})
    assert response.status_code == 422
