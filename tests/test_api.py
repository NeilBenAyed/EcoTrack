from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur EcoTrack API"}

def test_create_user():
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    assert response.json()["email"] == "alice@example.com"

def test_create_activity():
    # Crée un utilisateur pour l'activité
    user_resp = client.post("/users/", json={"name": "Bob", "email": "bob@example.com"})
    user_id = user_resp.json()["id"]
    response = client.post("/activities/", json={"user_id": user_id, "type": "transport", "value": 10.5, "date": "2025-11-21"})
    assert response.status_code == 200
    assert response.json()["type"] == "transport"
    assert response.json()["value"] == 10.5

def test_calculate_carbon_footprint():
    # Crée un utilisateur et une activité
    user_resp = client.post("/users/", json={"name": "Charlie", "email": "charlie@example.com"})
    user_id = user_resp.json()["id"]
    client.post("/activities/", json={"user_id": user_id, "type": "food", "value": 5.0, "date": "2025-11-21"})
    client.post("/activities/", json={"user_id": user_id, "type": "transport", "value": 7.0, "date": "2025-11-21"})
    response = client.get(f"/carbon_footprint/{user_id}")
    assert response.status_code == 200
    assert response.json()["total"] == 12.0
