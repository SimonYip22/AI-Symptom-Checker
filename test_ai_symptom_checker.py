# test_ai_symptom_checker.py
from ai_symptom_checker import score_conditions, normalise_choice_input

def test_single_symptom_match():
    user_symptoms = ["fever"]
    scores = score_conditions(user_symptoms)
    # Influenza and other fever conditions should have non-zero scores
    assert scores["Influenza (flu)"] > 0
    assert scores["Migraine"] == 0

def test_multiple_symptoms_match():
    user_symptoms = ["fever", "cough"]
    scores = score_conditions(user_symptoms)
    # Influenza should score higher than Pneumonia for this example
    assert scores["Influenza (flu)"] > scores["Pneumonia (chest infection)"]

def test_symptom_alias():
    # Using an alias should normalize correctly
    user_symptoms = [normalise_choice_input("high temperature")]
    scores = score_conditions(user_symptoms)
    assert scores["Influenza (flu)"] > 0
    assert scores["Migraine"] == 0

def test_invalid_symptom():
    user_symptoms = ["notasymptom"]
    scores = score_conditions(user_symptoms)
    # No condition should get a score
    for val in scores.values():
        assert val == 0

def test_empty_input():
    user_symptoms = []
    scores = score_conditions(user_symptoms)
    # All conditions should have score 0
    for val in scores.values():
        assert val == 0