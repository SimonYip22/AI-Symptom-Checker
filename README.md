# 𝐁𝐮𝐢𝐥𝐝𝐢𝐧𝐠 𝐚 𝐑𝐮𝐥𝐞-𝐁𝐚𝐬𝐞𝐝 𝐏𝐲𝐭𝐡𝐨𝐧 𝐀𝐈 𝐒𝐲𝐦𝐩𝐭𝐨𝐦 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 🧠🤖
**Python | Rule-based AI | CLI Tool | FastAPI | Pydantic | JSON Output | Clinically-Informed Logic**

<!-- Tech Stack -->
![Python](https://img.shields.io/badge/python-3.13-blue) 
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-green) 
![Pydantic](https://img.shields.io/badge/Pydantic-2.11.7-orange) 
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.35.0-lightgrey)

<!-- Project Status & Quality -->
![Build Status](https://img.shields.io/github/actions/workflow/status/SimonYip22/ai-symptom-checker/python-tests.yml?branch=main)
![Tests](https://github.com/SimonYip22/ai-symptom-checker/actions/workflows/python-tests.yml/badge.svg?branch=main)
![Release](https://img.shields.io/github/v/release/SimonYip22/ai-symptom-checker)

<!-- Repository Info -->
![License](https://img.shields.io/badge/license-MIT-green)
![Issues](https://img.shields.io/github/issues/SimonYip22/ai-symptom-checker)
![Forks](https://img.shields.io/github/forks/SimonYip22/ai-symptom-checker)
![Stars](https://img.shields.io/github/stars/SimonYip22/ai-symptom-checker)
![Contributors](https://img.shields.io/github/contributors/SimonYip22/ai-symptom-checker)

A **Python-based, rule-driven AI symptom checker** that leverages **clinical reasoning** to interpret patient-reported symptoms and rank potential conditions. Users can interact via a **command-line interface (CLI)** **or** a **FastAPI-based JSON API (v2)**, making the tool both scriptable and deployable for web integration.

The **v2 upgrade adds a deployable API**, allowing the system to serve JSON responses for top conditions, matched symptoms, and management advice—demonstrating production-ready backend capabilities alongside the original CLI.

The system outputs the **top 3 likely conditions**, including **matched symptoms** and **management advice** for the most probable diagnosis.

This project demonstrates a **clinically-informed workflow**, where condition-symptom mappings and formula-weighted scoring reflect real-world clinical prioritisation. The outputs are interpretable, relevant, and grounded in clinical reasoning—skills that only a clinician could encode accurately. Modular code supports **future AI/ML integration**. 

A **deployable backend** with API endpoints highlights production-readiness and makes the project recruiter-ready, showcasing both CLI and web-accessible functionality.


---

## System Workflow

![Symptom Checker Flowchart](symptom-checker-flowchart.png)
*Figure 1: Flowchart overview of symptom input, scoring, and output display workflow.*


---


## Clinical & Technical Highlights

- **Rule-based weighted scoring**: Each symptom has a weight per condition. Weighted scores simulate clinical prioritisation of symptoms per condition.  
- **Input normalisation & alias mapping**: Accepts lay terms (e.g., “high temperature” → “fever”) for realistic user input handling.  
- **Top 3 condition ranking**: Provides probabilistic-style output using a formula-based scoring system.  
- **Educational disclaimer**: Emphasizes safe usage and clinical context.  
- **Advice dictionary**: provides condition-specific management guidance.
- **Modular CLI architecture**: Each step (input collection, normalization, scoring, display) is separated for maintainability and future expansion.  
- **Future AI/ML potential**: Easily extendable for machine learning classifiers, NLP symptom extraction, or Bayesian reasoning.

---

## How It Works

1. **User Input**  
   - Collects symptoms one at a time until “done” is entered.  
   - Normalizes input using aliases and canonical symptom mapping.  

2. **Scoring Engine**  
   - Iterates over conditions and computes weighted scores for matched symptoms.  
   - Adjusts scores relative to total possible symptoms per condition as well as total possible score.  
   - Returns top 3 conditions ranked by normalized score.  

3. **Result Display**  
   - Prints matched symptoms and percentage likelihood for top conditions.  
   - Provides management advice for the most likely condition.  
   - CLI output includes clear formatting and disclaimers.


---


## CLI Technical Highlights

- **Rule-based inference engine**: Weighted scoring allows quick adaptation for new conditions. 
-	**Normalization and alias mapping**: Handles human input variability.
-	**Modular function design**: Each step (input, scoring, display) is separated, enabling future AI integration.
-	**Scoring normalisation**: Developed a scoring algorithm that accounts for total symptom scores and relative condition length: 
`adjusted_score = (total_score / total_possible) * (num_symptoms / max_symptoms)`
-	**CLI-based UX**: Lightweight, fast, and easy to extend.

---


## Architecture & Implementation

**Key Components**
1.	**Conditions Dictionary**
	- Maps each condition to its symptoms and weighted scores.
	- **Example**: "Urinary Tract Infection": {"urinary frequency": 3, "blood in urine": 2, ...}
2.	**Symptom Aliases**
	-	Handles layman terms for symptoms.
	-	**Example**: "wee a lot" → "urinary frequency"
3.	**Input Normalisation (normalise_choice_input)**
	-	Cleans text inputs (lowercase, remove punctuation).
	-	Maps aliases to canonical symptom names.
	-	Returns None for unrecognised symptoms.
4.	**User Input Collection (user_symptoms_list)**
	-	Prompts the user to enter symptoms until "done".
	-	Normalizes input using normalise_choice_input.
	-	Returns validated symptom list.
5.	**Scoring Function (score_conditions)**
	-	Iterates through all conditions.
	-	Computes weighted scores for matched symptoms.
	-	Adjusts scores for condition length vs max symptoms.
	-	Returns a dictionary of normalized condition scores.
6.	**Display Results (display_results)**
	-	Sorts conditions by score.
	-	Displays top 3 conditions with percentage scores and matched symptoms.
	-	Prints likely diagnosis with advice.
	-	Includes educational disclaimer.
7.	**Main CLI Loop (__main__)**
	-	Continuously prompts user for input or "exit".
	-	Runs display_results() for each session.

---


## Future Improvements

- **AI/ML Integration**:
  - Train classifiers on clinical datasets for probabilistic condition ranking.
  - NLP for symptom extraction from free text.
  -	Bayesian inference for probabilistic reasoning.
-	**UI/UX Enhancements**:
  -	Web or GUI front-end.
  -	Real-time suggestions and auto-completion.
-	**External Data Integration**:
  -	Pull real-time disease prevalence data.
  -	Connect with EHRs for personalized risk assessment.

---


## CLI Quick Start

**Clone repo and run**:

```bash
git clone https://github.com/SimonYip22/ai-symptom-checker.git
cd ai-symptom-checker
python ai_symptom_checker.py 
```

- Press Enter to start
- Enter symptoms one at a time
- Type "done" when finished
- Type "exit" to quit

---


## CLI Example session

```text
Press Enter to start symptom checker, or type 'exit' to quit: 

Enter a symptom: diarrhoea
Enter a symptom: vomiting
Enter a symptom: stomach pain
Enter a symptom: done
You have entered these symptoms:  ['diarrhoea', 'vomiting', 'abdominal pain']

Top 3 possible conditions:
Gastroenteritis (stomach bug): 32.3% | Matched symptoms: ['diarrhoea', 'vomiting', 'abdominal pain']
Influenza (flu): 9.1% | Matched symptoms: ['vomiting']
Migraine: 7.3% | Matched symptoms: ['vomiting']

Likely diagnosis is:  Gastroenteritis (stomach bug)
Advice: Stay at home and get plenty of rest, drink plenty of water to stay hydrated (small sips if you feel sick),
 Try and eat when you feel able to, paracetamol +/- ibuprofen if in pain.
Important: This tool is for educational purposes only and does not replace medical advice. If you are worried about your symptoms, please contact NHS 111.
 Call 999 or go to A&E immediately if your symptoms are severe, sudden, or life-threatening.
Press Enter to start symptom checker, or type 'exit' to quit: 
```

---

## v2 — API Deployment with FastAPI

**Python | FastAPI | Pydantic | JSON Output**

## Overview
- CLI logic wrapped into a deployable API
- JSON output includes:
	- user_symptoms (normalised)
	- top_conditions (top 3, percentage, matched symptoms)
	- likely_diagnosis
	- advice
- Keeps CLI and API modularly separate for maintainability and scalability

## Endpoints
- /health → GET → API health check
- /predict → POST → Input: list of symptoms; Output: top conditions JSON

## Screenshots

![Swagger UI Home](v2_api/swagger_home.png)  
*Figure 2: FastAPI Swagger UI home page showing available endpoints.*

![Swagger Health Check](v2_api/swagger_health_check.png)  
*Figure 3: /health endpoint response confirming API is running.*

![Swagger /predict Example](v2_api/swagger_predict_example.png)  
*Figure 4: /predict endpoint example request and JSON response.*

## Example POST.predict request

```json
{
  "symptoms": ["fever", "cough"]
}
```

## Example JSON response

```json
{
  "user_symptoms": [
    "fever",
    "cough"
  ],
  "top_conditions": [
    {
      "condition": "Influenza (flu)",
      "score": "27.3%",
      "matched_symptoms": [
        "fever",
        "cough"
      ]
    },
    {
      "condition": "Pneumonia (chest infection)",
      "score": "15.6%",
      "matched_symptoms": [
        "fever",
        "cough"
      ]
    },
    {
      "condition": "Otitis Media (inner ear infection)",
      "score": "9.1%",
      "matched_symptoms": [
        "fever"
      ]
    }
  ],
  "likely_diagnosis": "Influenza (flu)",
  "advice": "Rest and sleep, keep warm, paracetamol +/- ibuprofen for fever and pain,\n Drink plenty of water to stay hydrated, stay at home and avoid contact with others to prevent spreading,\n Cover mouth and nose with tissue when cough or sneezing, dispose of immediately,\n Wash hands regularly with soap and water."
}
```

## How to run locally

```bash
cd v2_api
uvicorn app:app --reload
```

- Visit http://127.0.0.1:8000/docs for interactive Swagger UI
- Test endpoints in-browser
- View JSON responses for example inputs


## Notes / Future Work
- Demonstrates production-ready backend for a clinician-technologist portfolio
- JSON outputs are easy to integrate into a frontend later if desired
- Future improvements:
	- Expand conditions & specialties
	- Integrate ML/NLP for symptom extraction
	- Deploy live on Render / Railway / Heroku
	- Add persistent logging/analytics
- No frontend required; API + CLI + deployment is enough for portfolio.


---

## Running Tests

**Test the scoring logic and alias handling**:

```bash
pytest -v
```
**Tests include:**
- Weighted scoring correctness
- Symptom alias normalization
- Handling unrecognized inputs
- Top-3 ranking validation


---


## Project Structure

```text
ai-symptom-checker/
├── v2_api/
│   ├── ai_symptom_checker_v2.py
│   ├── app.py
│   ├── requirements.txt
│   ├── swagger_health_check.png
│   ├── swagger_home.png
│   └── swagger_predict_example.png
├── ai_symptom_checker.py
├── notes.md
├── README.md
├── reflection.md
├── sample_run.txt
├── symptom-checker-flowchart.png
└── test_ai_symptom_checker.py
```

**Explanations**:
- **v2_api/** — Contains the FastAPI version of the symptom checker
	- **ai_symptom_checker_v2.py** — Core logic for scoring, normalisation, and advice, adapted for API usage
	- **app.py** — FastAPI app wrapping the core logic into /predict and /health endpoints
	- **requirements.txt** — Python dependencies for v2 API (FastAPI, Pydantic, Uvicorn)
	- **swagger_health_check.png** — Screenshot showing /health endpoint response
	- **swagger_home.png** — Screenshot of the Swagger UI home page
	- **swagger_predict_example.png** — Screenshot showing /predict example request and JSON response
- **ai_symptom_checker.py** — Original CLI program
- **notes.md** — Daily notes and reflections
- **README.md** — Project documentation
- **reflection.md** — Final project reflection
- **sample_run.txt** — Example runs
- **symptom-checker-flowchart.png** - Flowchart explaining logic
- **test_ai_symptom_checker.py** — Automated tests


---


## Disclaimer

- Educational use only. 
- Not a substitute for professional medical advice.
- For severe, sudden, or life-threatening symptoms, contact 999/A&E immediately.
- For non-emergency concerns, contact NHS 111.
