# Final Reflection — Clinically-Informed AI Symptom Checker

## Project Overview

This project implements a **Python-based, rule-driven AI symptom checker** for six primary-care conditions. Users enter symptoms via a **CLI**, and the program outputs **ranked conditions** using a formula-weighted scoring system. Canonical medical terminology is paired with **alias mapping** to support layperson inputs while maintaining clinical precision.

The condition-symptom mappings and scoring were **designed using clinical reasoning**, ensuring that the outputs are not just algorithmically correct but **reflect real-world medical prioritisation** of symptoms and likelihood of conditions. This makes the tool **clinically interpretable and relevant**, something a generic AI or CS student could not achieve without domain expertise.

Key technical achievements include **weighted scoring normalisation, modular function design, and transparent symptom-condition mapping**, which collectively allow future integration with AI/ML models and clinician-informed decision support.

---

## Design Choices

- **Condition Scope**: Limited to six clinically common conditions for clarity and demonstration.
- **Weighted Symptoms**: Each symptom is weighted per condition to reflect **true clinical prioritisation**, a feature only possible with domain knowledge.
- **CLI vs GUI**: Chose a command-line interface for simplicity and rapid iteration, enabling a solid technical foundation before UI development.
- **Modularity & Extensibility**: Functions are self-contained to facilitate future ML integration, FastAPI deployment, data logging, and UI upgrades.

---


## Technical Learning Outcomes

Throughout this project, I built both technical and conceptual skills:

- **Python Programming**:
    - Leveraged dictionaries for symptom-condition mapping with weights.
    - Implemented modular functions (`normalise_choice_input`, `user_symptoms_list`, `score_conditions`, `display_results`) to separate concerns and maintain readability.
    - Used loops, list comprehensions, and sorting with lambda functions to rank conditions efficiently.
- **Rule-based Logic Design**:
    - Developed a scoring algorithm that accounts for total symptom scores and relative condition length:
      `adjusted_score = (total_score / total_possible) * (num_symptoms / max_symptoms)`
      This prevents bias toward conditions with more symptoms and ensures each symptom carries appropriate clinical weight.
    - Maintained **explainability**, showing which symptoms contributed to each condition’s score.
- **Data Normalisation & Input Handling**:
    - Mapped user-entered lay terms to canonical symptoms to emulate realistic patient communication.
    - Implemented error handling for invalid or unrecognised inputs.
- **Testing & Debugging**:
    - Wrote automated tests for alias mapping, scoring accuracy, and top-3 ranking.
    - Resolved flow issues such as infinite loops, Enter key restarts, and proper symptom accumulation.


---

## Challenges & Solutions

- **Ambiguous Inputs**: Handled multiple phrasings via a symptom alias dictionary.
- **Score Normalisation**: Implemented the weighted formula `(total_score / total_possible) * (num_symptoms / max_symptoms)` to avoid bias from conditions with many or few symptoms.
- **Program Flow**: Maintained repeated sessions via `__main__` loop with graceful exit handling.
- **Clinical Relevance Framing**: Ensured symptom-condition mappings reflect true clinical reasoning, making outputs interpretable and meaningful—something a generic CS-focused AI tool cannot replicate.

---

## Future Improvements

- **Input Handling**: Expand alias mapping, integrate typo correction, and explore NLP entity recognition.
- **Clinical Breadth**: Add more conditions grouped by system (respiratory, neurological, gastrointestinal, etc.) and specialty (paediatrics, psychiatry, infectious disease).  
- **AI/ML Integration**: Incorporate probabilistic or machine learning models for condition ranking using real-world datasets.
- **Explainability & Advice**: Provide not just conditions and scores, but tailored advice for next steps, red flags, and disclaimers.  
- **UX/UI Upgrade**: Transition to a web or Streamlit interface with clickable symptoms, real-time validation, and graphical output.
- **Data Logging & Analytics**: Persist user inputs and outputs to CSV/JSON for trend analysis, evaluation, and model training.
- **FastAPI Deployment**: Wrap CLI logic as an API for broader integration into healthcare workflows.

---

## Key Takeaways

1. **Clinically-informed design** ensures the symptom-to-condition logic reflects real-world medical reasoning, making outputs interpretable and relevant—distinct from generic AI approaches.
2. **Rule-based foundations** provide a transparent and extendable starting point for ML pipelines.
3. **Incremental testing and modular design** are critical for maintainable and scalable CLI applications.
4. **Balancing clinical precision with usability** ensures the tool is accurate yet approachable.
5. **Demonstrates technical and clinical skill convergence**, bridging Python programming, clinical reasoning, and AI readiness for healthcare applications.