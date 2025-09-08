# Final Reflection — Clinically-Informed AI Symptom Checker

## Project Overview

In clinical practice, patients often describe symptoms in lay terms that don’t map neatly onto medical terminology. This project bridges that gap by building a **Python-based, rule-driven AI symptom checker** that translates layperson input into clinically weighted diagnoses, for an initial set of **clinically-relevant conditions**. Users enter symptoms via a **CLI**, and the program outputs **ranked conditions** using a formula-weighted scoring system. Canonical medical terminology is paired with **alias mapping** to support layperson inputs while maintaining clinical precision.

With the addition of **v2 FastAPI deployment (live on Render: [https://ai-symptom-checker-5rfb.onrender.com/docs](https://ai-symptom-checker-5rfb.onrender.com/docs))**, users can also interact via a **JSON API**, making the tool scriptable, web-accessible, and recruiter-ready. Continuous integration via **GitHub Actions** ensures the live endpoints function reliably, providing production-grade validation of `/health`, `/`, and `/predict` endpoints.

The condition-symptom mappings and scoring were **designed using clinical reasoning**, ensuring that the outputs are not just algorithmically correct but **reflect real-world medical prioritisation** of symptoms and likelihood of conditions. This makes the tool **clinically interpretable and relevant**, something a generic AI or CS student could not achieve without domain expertise.

Key technical achievements include **weighted scoring normalisation, modular function design, transparent symptom-condition mapping**, and **API integration with live deployment**, which collectively allow future integration with AI/ML models and clinician-informed decision support.

The workflow diagram, CLI examples, and API endpoints (see README) illustrate transparency, explainability, and production-readiness, key requirements for clinical adoption.

This project laid the foundation for my MSc final project — a fully deployed **Clinical Decision Support Tool (CDST)** integrating machine learning, NLP, and real-world datasets into the same clinically-informed framework.

---

## Design Choices
- **Clinician–Technologist Insight**: Encodes reasoning that usually stays tacit in a doctor’s mind, creating outputs that are interpretable and clinically meaningful, not just algorithmically correct.
- **Condition Scope**: Limited to initial clinically-relevant conditions for clarity and demonstration.
- **Weighted Symptoms**: Each symptom is weighted per condition to reflect **true clinical prioritisation**, a feature only possible with domain knowledge.
- **CLI vs API**: Chose a command-line interface for simplicity and rapid iteration, and added a **FastAPI v2 API (live on Render)** for web deployment and professional portfolio demonstration.
- **Modularity & Extensibility**: Functions are self-contained to facilitate future ML integration, FastAPI deployment, data logging, and UI upgrades.
- **CI/CD & Testing**: Automated GitHub Actions workflow validates endpoint functionality on push and on a weekly schedule, ensuring live deployment reliability.

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
- **FastAPI Integration & Deployment**:
    - Wrapped CLI logic into API endpoints (`/predict` and `/health`) with structured JSON output.
    - Hosted live on **Render**: [https://ai-symptom-checker-5rfb.onrender.com/docs](https://ai-symptom-checker-5rfb.onrender.com/docs)
    - Documented endpoints via Swagger UI for professional usability.
- **Testing & Debugging**:
    - Wrote automated tests for alias mapping, scoring accuracy, top-3 ranking, and API responses.
    - Implemented GitHub Actions workflow to validate live API endpoints on push and weekly schedules.
    - Resolved flow issues such as infinite loops, Enter key restarts, and proper symptom accumulation.

---

## Challenges & Solutions

- **Ambiguous Inputs**: Handled multiple phrasings via a symptom alias dictionary.
- **Score Normalisation**: Implemented the weighted formula `(total_score / total_possible) * (num_symptoms / max_symptoms)` to avoid bias from conditions with many or few symptoms.
- **Program Flow**: Maintained repeated sessions via `__main__` loop with graceful exit handling for CLI and API testing.
- **Clinical Relevance Framing**: Ensured symptom-condition mappings reflect true clinical reasoning, making outputs interpretable and meaningful—something a generic CS-focused AI tool cannot replicate.
- **API Deployment & CI/CD**: Separated CLI and API logic for modularity; validated live endpoints continuously to ensure production-readiness.

---

## Future Improvements  

- **FastAPI Deployment Enhancements**: Expand live deployment with persistent logging, analytics, and monitoring.
- **AI/ML Integration**: Train machine learning classifiers on real-world datasets, integrate Bayesian reasoning, and apply NLP for automated symptom extraction.
- **UX/UI Upgrade**: Transition from CLI to a web or Streamlit interface with clickable symptoms, real-time validation, and graphical outputs for improved accessibility.
- **Clinical Breadth**: Expand to additional conditions grouped by system (respiratory, neurological, gastrointestinal, etc.) and specialty (paediatrics, psychiatry, infectious disease).
- **Explainability & Advice**: Provide not only ranked conditions, but also next-step guidance, red flag warnings, and safety disclaimers.
- **Input Handling**: Broaden alias mapping, add typo-tolerant matching, and explore NLP entity recognition for free-text input.
- **Data Logging & Analytics**: Persist inputs/outputs to CSV/JSON for auditing, longitudinal tracking, and model training.

---

## Key Takeaways

1. **Clinically-informed design** ensures the symptom-to-condition logic reflects real-world medical reasoning, making outputs interpretable and relevant—distinct from generic AI approaches.
2. **Rule-based foundations** provide a transparent and extendable starting point for ML pipelines.
3. **Incremental testing and modular design** are critical for maintainable and scalable CLI and API applications.
4. **Balancing clinical precision with usability** ensures the tool is accurate yet approachable.
5. **Demonstrates technical and clinical skill convergence**, bridging Python programming, clinical reasoning, API deployment, CI/CD, and AI readiness for healthcare applications.
6. **Recruiter-ready impact**: The v2 FastAPI endpoints demonstrate a production-ready, web-accessible backend, with automated endpoint validation enhancing professional credibility.

This project demonstrates the unique value of combining medical expertise with technical rigour—skills that position me as an irreplaceable clinician–technologist in healthcare AI.

---