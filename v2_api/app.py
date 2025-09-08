# app.py

# FastAPI imports
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Import your CLI functions and dictionaries **as modules in the same folder**
from .ai_symptom_checker_v2 import score_conditions, normalise_choice_input, advice, conditions

# Initialize FastAPI app
app = FastAPI(title="Clinically-Informed AI Symptom Checker v2 API")

# Pydantic model for input
class Symptoms(BaseModel):
    symptoms: List[str]

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Main predict endpoint
@app.post("/predict")
def predict(symptoms_input: Symptoms):
    # Normalise input
    normalised = [normalise_choice_input(s) for s in symptoms_input.symptoms]
    normalised = [s for s in normalised if s is not None]

    # Compute scores
    scores = score_conditions(normalised)

    # Top 3 conditions
    sorted_conditions = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

    top_conditions = []
    for cond, score in sorted_conditions:
        matched = [s for s in normalised if s in conditions[cond]]
        top_conditions.append({
            "condition": cond,
            "score": f"{round(score*100, 1)}%",
            "matched_symptoms": matched
        })

    likely_diagnosis = sorted_conditions[0][0] if sorted_conditions else None

    return {
        "user_symptoms": normalised,
        "top_conditions": top_conditions,
        "likely_diagnosis": likely_diagnosis,
        "advice": advice.get(likely_diagnosis, "No advice available")
    }