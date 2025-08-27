# AI Symptom Checker 🩺
**Python | Rule-based AI | CLI Tool**

![Python](https://img.shields.io/badge/python-3.13-blue)
![Build Status](https://img.shields.io/github/actions/workflow/status/SimonYip22/ai-symptom-checker/python-tests.yml?branch=main)
![License](https://img.shields.io/badge/license-MIT-green)
![Release](https://img.shields.io/github/v/release/SimonYip22/ai-symptom-checker)
![Issues](https://img.shields.io/github/issues/SimonYip22/ai-symptom-checker)
![Forks](https://img.shields.io/github/forks/SimonYip22/ai-symptom-checker)
![Stars](https://img.shields.io/github/stars/SimonYip22/ai-symptom-checker)
![Contributors](https://img.shields.io/github/contributors/SimonYip22/ai-symptom-checker)

A simple **Python-based rule-based AI symptom checker**, that allows users to enter symptoms via a **command-line interface** and returns the most likely conditions along with advice for management of the most likely condition. Designed for educational purposes and future AI/ML expansion.

---


## TL;DR

- Enter symptoms one by one.
- Program returns **top 3 likely conditions** ranked by percentage likelihood, with matched symptoms.
- Displays the **most likely condition** with matched symptoms and management advice.
- Modular design for easy extension, integration of AI/ML, and data persistence.

---


## Features

- **Covers 6 common primary-care conditions**: Urinary Tract Infection, Influenza, Gastroenteritis, Otitis Media, Migraine, Pneumonia  
- Input normalisation & alias mapping, so handles **lay-term symptom input** (e.g., "high temperature" → "fever")  
- **Rule-based weighted scoring**:
  - Each symptom has a weight per condition.
  - Top 3 conditions ranked based on normalized and adjusted scores.
- Modular CLI interface for quick testing and future integration.
- Advice dictionary provides condition-specific management guidance.
- Fully extendable to incorporate AI/ML models or probabilistic reasoning.

---


## Technical Highlights

- **Rule-based inference engine**: Weighted scoring allows quick adaptation for new conditions.
-	**Normalization and alias mapping**: Handles human input variability.
-	**Modular function design**: Each step (input, scoring, display) is separated, enabling future AI integration.
-	**Scoring normalization**: Adjusts scores based on max number of symptoms per condition.
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
3.	**Input Normalization (normalise_choice_input)**
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


## Quick Start

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


## Example session

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
├── .github/
    └── workflows/
        └── python-tests.yml
├── 01_Miscellaneous
├── ai_symptom_checker.py
├── notes.md
├── README.md
├── reflection.md
├── sample_run.txt
└── test_ai_symptom_checker.py
```

**Explanations**:
- **.github/workflows/python-tests.yml** — GitHub Actions workflow for running tests
- **01_Miscellaneous** — Miscellaneous folders and files
- **ai_symptom_checker.py** — Main program
- **notes.md** — Daily notes and reflections
- **README.md** — Project documentation
- **reflection.md** — Final project reflection
- **sample_run.txt** — Example runs
- **test_ai_symptom_checker.py** — Automated tests

---


## Disclaimer

- Educational use only. 
- Not a substitute for professional medical advice.
- For severe, sudden, or life-threatening symptoms, contact 999/A&E immediately.
- For non-emergency concerns, contact NHS 111.
