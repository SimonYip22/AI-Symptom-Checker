# test_ai_symptom_checker.py
import pytest
from v2_api.ai_symptom_checker_v2 import score_conditions, normalise_choice_input

# -----------------------
# Core Functionality Tests
# -----------------------

def test_single_symptom_match():
    user_symptoms = ["fever"]
    scores = score_conditions(user_symptoms)
    assert scores["Influenza (flu)"] > 0
    assert scores["Migraine"] == 0

def test_multiple_symptoms_match():
    user_symptoms = ["fever", "cough"]
    scores = score_conditions(user_symptoms)
    assert scores["Influenza (flu)"] > scores["Pneumonia (chest infection)"]

def test_invalid_symptom():
    user_symptoms = ["notasymptom"]
    scores = score_conditions(user_symptoms)
    assert all(val == 0 for val in scores.values())

def test_empty_input():
    scores = score_conditions([])
    assert all(val == 0 for val in scores.values())

# -----------------------
# Alias & Normalisation
# -----------------------

@pytest.mark.parametrize("alias,expected", [
    ("high temperature", "fever"),
    ("painful pee", "painful urination"),
    ("can't hold pee!", "urinary urgency"),
    ("night-time pee", "night time urination"),
])
def test_alias_normalisation(alias, expected):
    assert normalise_choice_input(alias) == expected

def test_duplicate_symptoms():
    scores = score_conditions(["fever", "fever"])
    scores_once = score_conditions(["fever"])
    assert scores["Influenza (flu)"] == scores_once["Influenza (flu)"]

# -----------------------
# Top-3 Ranking
# -----------------------

def test_top_three_ranking():
    scores = score_conditions(["fever", "cough"])
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_conditions = [cond for cond, _ in sorted_scores[:3]]
    assert "Influenza (flu)" in top_conditions
    assert sorted_scores[0][1] >= sorted_scores[1][1] >= sorted_scores[2][1]

# -----------------------
# Future-Proofing: API v2 Placeholder
# -----------------------

from fastapi.testclient import TestClient
from v2_api.app import app   

client = TestClient(app)

def test_api_health_check():
    """Health check endpoint should return status OK."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_api_predict_valid():
    """Valid symptoms should return a structured prediction JSON."""
    payload = {"symptoms": ["fever", "cough"]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()

    # keys exist
    assert "user_symptoms" in data
    assert "top_conditions" in data
    assert "likely_diagnosis" in data
    assert "advice" in data

    # at least one condition matches flu
    conditions = [c["condition"] for c in data["top_conditions"]]
    assert any("Influenza" in cond for cond in conditions)

def test_api_predict_invalid_input():
    """Invalid symptoms should still return JSON with empty or zero scores, not crash."""
    payload = {"symptoms": ["notasymptom"]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()

    # invalid symptoms should give empty/low scores
    assert data["user_symptoms"] == ["notasymptom"] or data["user_symptoms"] == []
    assert all(cond["score"] == "0.0%" for cond in data["top_conditions"])