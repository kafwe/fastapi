from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)

def test_create_user():
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
