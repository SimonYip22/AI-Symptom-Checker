import httpx

# Replace this with your live Render/Railway/Heroku URL
API_URL = "https://ai-symptom-checker-5rfb.onrender.com"

def test_health_endpoint():
    response = httpx.get(f"{API_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_endpoint_valid():
    payload = {"symptoms": ["fever", "cough"]}
    response = httpx.post(f"{API_URL}/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "user_symptoms" in data
    assert "top_conditions" in data
    assert len(data["top_conditions"]) == 3
    assert any("Influenza" in c["condition"] for c in data["top_conditions"])

def test_predict_endpoint_invalid():
    payload = {"symptoms": ["notasymptom"]}
    response = httpx.post(f"{API_URL}/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Expect empty or zero scores
    assert data["user_symptoms"] == [] or data["user_symptoms"] == ["notasymptom"]
    assert all(c["score"] == "0.0%" for c in data["top_conditions"])