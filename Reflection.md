# Final Reflection

---

## Project Overview

This project implements a **rule-based AI symptom checker** for six primary-care conditions. Users enter symptoms via a **CLI**, and the program outputs **ranked conditions** based on weighted symptom scoring. Canonical medical terminology is paired with **alias mapping** to support layperson inputs while maintaining clinical precision.

Key technical achievements include **weighted scoring normalization, modular function design, and transparent symptom-condition mapping**, which collectively allow future integration with AI/ML models.

---

## Technical Learning Outcomes

Throughout the project, I built both technical and conceptual skills:

- **Python Programming**:
    - Leveraged dictionaries for symptom-condition mapping with weights.
    - Implemented modular functions (normalise_choice_input, user_symptoms_list, score_conditions, display_results) to separate concerns and maintain readability.
    - Used loops, list comprehensions, and sorting with lambda functions to rank conditions efficiently.
- **Rule-based Logic Design**:
    - Developed a scoring algorithm that adjusts for the number of symptoms per condition relative to the maximum, producing normalized likelihood scores.
    - Maintained explainability by displaying which symptoms contributed to each condition score.
- **Data Normalization & Input Handling**:
    - Mapped user-entered lay terms to canonical symptoms.
    - Implemented error handling for invalid inputs.
- **Testing & Debugging**:
    - Wrote automated tests for alias mapping, scoring accuracy, and top-3 ranking.
    - Resolved flow issues such as infinite loops, Enter key restarts, and proper symptom accumulation.

---

## Design Choices

- **Condition Scope**: Limited to six clinically common conditions for clarity and demonstration purposes.
- **Weighted Symptoms**: Allowed finer granularity of likelihood by scoring symptom importance differently per condition.
- **CLI vs GUI**: Chose command-line interface for simplicity and rapid iteration, enabling a professional foundation before UI development.
- **Modularity & Extensibility**: Functions are self-contained to facilitate future ML integration, data logging, and web interface deployment.

---

## Challenges & Solutions

- **Ambiguous Inputs**: Users could enter multiple phrasings; solved via symptom_aliases dictionary.
- **Score Normalisation**: Adjusted scores by condition length relative to maximum symptoms to avoid bias toward conditions with more symptoms.
- **Program Flow**: Ensured repeated sessions via infinite loop with __main__, handling user exit gracefully.
- **Initial Over-engineering**: Considered JSON storage initially; realized Python dictionaries sufficed, simplifying development.

---

## Future Improvements

Reflecting on this build, several areas for enhancement are evident:

- **Input Handling**: Expand alias mapping, integrate typo correction, and explore NLP entity recognition.
- **Clinical Breadth**: Add more conditions, grouped by system (respiratory, neurological, gastrointestinal, etc.) and specialty (paediatrics, psychiatry, infectious disease).  
- **AI/ML Integration**: Incorporate probabilistic or machine learning models for condition ranking using real-world datasets.
- **Explainability & Advice**: Provide not just conditions and scores, but tailored advice for next steps, red flags, and disclaimers.  
- **UX/UI Upgrade**: Transition to a web or Streamlit interface with clickable symptoms, real-time validation, and graphical output.
- **Data Logging & Analytics**: Persist user inputs and outputs to CSV/JSON for trend analysis, evaluation, and model training.

---

## Key Takeaways
1.	**Rule-based foundations** provide a transparent and extendable starting point for ML pipelines.
2.	**Incremental testing and modular design** are critical for maintainable and scalable CLI applications.
3.	**Balancing clinical precision with usability** ensures the tool is both accurate and approachable.
4.	**Demonstrates technical and clinical skill convergence**, bridging Python programming, clinical reasoning, and AI readiness.