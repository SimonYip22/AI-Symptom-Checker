import os
import pytest
import httpx
from fastapi.testclient import TestClient
from v2_api.app import app

# Local FastAPI test client
client = TestClient(app)

# Live API URL (Render/Heroku/Railway)
API_URL = "https://ai-symptom-checker-5rfb.onrender.com"

# -----------------------------------------------------------------------------
# Local tests (always run on CI/CD)
# -----------------------------------------------------------------------------

def test_root_local():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_endpoint_valid_local():
    payload = {"symptoms": ["fever", "cough"]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "user_symptoms" in data
    assert "top_conditions" in data
    assert len(data["top_conditions"]) == 3

# -----------------------------------------------------------------------------
# Live API tests (only run if explicitly enabled, e.g. schedule/dispatch)
# -----------------------------------------------------------------------------

RUN_LIVE = os.getenv("RUN_LIVE", "false").lower() == "true"

@pytest.mark.skipif(not RUN_LIVE, reason="Skipping live API tests in default CI")
def test_health_endpoint_live():
    response = httpx.get(f"{API_URL}/health", timeout=15.0)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.skipif(not RUN_LIVE, reason="Skipping live API tests in default CI")
def test_predict_endpoint_valid_live():
    payload = {"symptoms": ["fever", "cough"]}
    response = httpx.post(f"{API_URL}/predict", json=payload, timeout=15.0)
    assert response.status_code == 200
    data = response.json()
    assert "user_symptoms" in data
    assert "top_conditions" in data
    assert len(data["top_conditions"]) == 3
    assert any("Influenza" in c["condition"] for c in data["top_conditions"])

@pytest.mark.skipif(not RUN_LIVE, reason="Skipping live API tests in default CI")
def test_predict_endpoint_invalid_live():
    payload = {"symptoms": ["notasymptom"]}
    response = httpx.post(f"{API_URL}/predict", json=payload, timeout=15.0)
    assert response.status_code == 200
    data = response.json()
    assert "user_symptoms" in data
    assert all(c["score"] == "0.0%" for c in data["top_conditions"])