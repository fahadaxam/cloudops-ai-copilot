
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_analyze_endpoint():
    incident = {
        "service": "Amazon EC2",
        "symptom": "High CPU utilisation"
    }

    response = client.post("/analyze", json=incident)

    assert response.status_code == 200

    data = response.json()

    assert data["service"] == "Amazon EC2"
    assert len(data["recommendations"]) == 3
    assert data["ai_enabled"] is False


def test_invalid_incident():
    incident = {
        "service": "A",
        "symptom": "CPU"
    }

    response = client.post("/analyze", json=incident)

    assert response.status_code == 422
