# app.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

# Where FastAPI lives, the bridge between HTTP requests (someone sends symptoms over the web) and my Python functions (scoring engine)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Import your existing CLI functions and dictionaries
from v2_api.ai_symptom_checker_v2 import score_conditions, normalise_choice_input, advice, conditions

# Initialize FastAPI app
app = FastAPI(title="Clinically-Informed AI Symptom Checker v2 API")

# Pydantic model for validating input
class Symptoms(BaseModel):
    symptoms: List[str]

# Health check endpoint. Just tells us the API is alive.
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Main endpoint to predict conditions. Send it a list of symptoms and it returns a JSON object
@app.post("/predict")
def predict(symptoms_input: Symptoms):
    # Normalise and filter user input
    normalised = [normalise_choice_input(s) for s in symptoms_input.symptoms]
    normalised = [s for s in normalised if s is not None]  # ignore unrecognised symptoms

    # Compute scores using your existing scoring function
    scores = score_conditions(normalised)

    # Get top 3 conditions
    sorted_conditions = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

    top_conditions = []
    for cond, score in sorted_conditions:
        # Find which normalised symptoms matched this condition
        matched = [s for s in normalised if s in conditions[cond]]
        top_conditions.append({
            "condition": cond,
            "score": f"{round(score*100, 1)}%",  # show as %
            "matched_symptoms": matched
        })

    # Most likely diagnosis
    likely_diagnosis = sorted_conditions[0][0] if sorted_conditions else None

    return {
        "user_symptoms": normalised,
        "top_conditions": top_conditions,
        "likely_diagnosis": likely_diagnosis,
        "advice": advice.get(likely_diagnosis, "No advice available")
    }