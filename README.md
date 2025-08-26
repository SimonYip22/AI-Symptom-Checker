# AI Symptom Checker 🩺

![Python](https://img.shields.io/badge/python-3.13-blue)
![Build Status](https://img.shields.io/github/actions/workflow/status/SimonYip22/ai-symptom-checker/python-tests.yml?branch=main)
![License](https://img.shields.io/badge/license-MIT-green)
![Release](https://img.shields.io/github/v/release/SimonYip22/ai-symptom-checker)
![Issues](https://img.shields.io/github/issues/SimonYip22/ai-symptom-checker)
![Forks](https://img.shields.io/github/forks/SimonYip22/ai-symptom-checker)
![Stars](https://img.shields.io/github/stars/SimonYip22/ai-symptom-checker)
![Contributors](https://img.shields.io/github/contributors/SimonYip22/ai-symptom-checker)

A simple **Python-based rule-based AI symptom checker**, a command-line tool that ranks possible medical conditions based on user-entered symptoms. Designed for educational purposes and future AI/ML expansion.

---

## TL;DR

Enter symptoms one by one, and the program returns the **top 3 likely conditions** ranked with % likelihood, and with matched symptoms, returns **most likely condition** and advice for management.

---

## Features

- Covers 6 common primary-care conditions:
  - Urinary Tract Infection, Influenza, Gastroenteritis, Otitis Media, Migraine, Pneumonia  
- Input normalisation & alias mapping, so handles **lay-term symptom input** (e.g., "high temperature" → "fever")  
- Rule-based inference with formula-weighted scoring to rank conditions by likelihood  
- Top 3 conditions as well as most likely condition, displayed with advice  
- Modular design for easy extension  
- Structured clinical reasoning in a command-line interface (CLI)

---


## Quick Start

Clone repo and run:

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

Test the scoring logic and alias handling:

```bash
pytest -v
```

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

Explanations:
- .github/workflows/python-tests.yml — GitHub Actions workflow for running tests
- 01_Miscellaneous — Miscellaneous folders and files
- ai_symptom_checker.py — Main program
- notes.md — Daily notes and reflections
- README.md — Project documentation
- reflection.md — Final project reflection
- sample_run.txt — Example runs
- test_ai_symptom_checker.py — Automated tests

---


## Reflections

- Learned input normalization, lay-term mapping, weighted scoring, and modular function design
- Balanced clinical accuracy with usability
- Future improvements (more advanced AI techniques for MSc final project):
  - Machine learning classifiers for automated condition ranking
  - NLP for symptom entity recognition
  - Bayesian inference & probabilistic reasoning
  - Front-end UI & integration with external datasets/APIs

---

## Disclaimer

Educational use only. Not a substitute for professional medical advice.
Call 999 or go to A&E in emergencies.
