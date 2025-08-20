# Day 1 - Input

## Goals
- Define symptom checklist (6 conditions, 3–5 symptoms each)
- Implement `normalize_choice_input` function
- Test parsing user input
- Include lay-friendly aliases for symptoms

## Day 1 Goal Explanation
- Define the first helper function: `normalize_choice_input()`
- This function will clean up user input so my symptom checker can understand it.
- Use sample_run.txt logging for documentation

## Step 1 — Plan the function
1. Problem: Users may type symptoms differently:
   - Extra spaces: `" headache "`
   - Mixed case: `"Fever"` or `"fever"`
   - Lay phrases: "wee a lot" instead of "frequent urination"
   - Typos: we’ll ignore for now, just normalize spacing and case
2. Goal of `normalize_choice_input()`:
   - Take user input string
   - Strip spaces from start/end
   - Convert to lowercase
   - Map common lay terms to canonical symptoms using symptom_aliases

## Step 2 — Symptom checklist planning
**Goal:** Define 6 conditions, each with 5-10 symptoms. Use clinically accurate terms for backend, but map lay terms for user input. 

Urinary Tract Infection (urine infection):
- urinary frequency 
- urinary urgency 
- painful urination
- night-time urination
- blood in urine
- suprapubic pain
- fever
- discharge
- foul-smelling urine
Lay-term mapping examples:
"wee a lot": "urinary frequency"
"need to pee urgently": "urinary urgency"
"painful pee": "painful urination"
"night time pee": "night time urination"
"blood in pee": "blood in urine"
"lower tummy pain": "suprapubic pain"
"temperature": "fever"
"fluid from penis": "discharge"
"fluid from vagina": "discharge"
"smelly urine": "foul smelling urine"

Influenza (flu):
- cough
- coryza
- fever
- rigors
- fatigue
- anorexia
- headache
- myalgia
- nausea
- vomiting
Lay-term mapping examples:
"coughing" : "cough"
"runny nose" : "coryza"
"temperature" : "fever"
"shivering": "rigors"
"tired": "fatigue"
"loss of appetite" : "anorexia"
"head pain": "headache"
"muscle aches": "myalgia"
"feel sick": "nausea"
"throwing up": "vomiting"
"sick": "vomiting"

Gastroenteritis (stomach bug)
- diarrhoea
- nausea
- vomiting
- anorexia
- malaise
- fever
- bloody diarrhoea
- abdominal pain
Lay-term mapping examples:
"loose stools": "diarrhoea"
"runny stools": "diarrhoea"
"feel sick": "nausea"
"throwing up": "vomiting"
"sick": "vomiting"
"not hungry": "anorexia"
"loss of appetite" : "anorexia"
"tired" : "malaise"
"temperature" : "fever"
"blood in stool": "bloody diarrhoea"
"blood in poo": "bloody diarrhoea"
"stomach pain": "abdominal pain"
"tummy pain": "abdominal pain"

Otitis Media (inner ear infection)
- ear pain
- fever
- discharge
- hearing loss
Lay-term mapping examples:
"ear ache": "ear pain"
"temperature": "fever"
"fluid from ear": "ear discharge"
"trouble hearing": "hearing loss"
"difficulty hearing": "hearing loss"
"blocked hearing": "hearing loss"

Migraine
- nausea
- vomiting
- headache
- flashing lights
- visual defect
- photophobia (sensitivity to light)
- phonophobia (sensitivity to sound)
- neck pain
Lay-term mapping examples:
"feel sick": "nausea"
"throwing up": "vomiting"
"sick": "vomiting"
"head pain": "headache"
"seeing flashing lights": "flashing lights"
"blurred vision": "visual defect"
"sensitive to light": "photophobia"
"sensitive to sound": "phonophobia"
"neck stiffness": "neck pain"

Pneumonia
- chest pain
- shortness of breath
- cough
- purulent sputum
- blood stained sputum
- fever
Lay-term mapping examples:
"chest ache": "chest pain"
"chest hurts": "chest pain"
"difficulty breathing": "shortness of breath"
"coughing": "cough"
"green phlegm": "purulent sputum"
"yellow phlegm": "purulent sputum"
"coughing blood": "blood stained sputum"
"coughing up blood": "blood stained sputum"
"temperature": "fever"

**Thoughts:**  
- Store as a Python dictionary in `ai_symptom_checker.py`
- Keys = condition names, Values = list of symptoms
- Will use later for matching user input
- Backend dictionary uses formal clinical terms → demonstrates professional medical knowledge
- Lay-term mapping ensures users can input common symptom language → improves usability
- store dictionary in json file

## Step 3 - Notes for Implementation
- Store conditions and symptom_aliases in ai_symptom_checker.py
- Use normalize_choice_input() to:
	1.	Strip spaces
	2.	Convert to lowercase
	3.	Map lay terms → clinical terms using symptom_aliases
- Test with sample user inputs, logging results in sample_run.txt

## Step 4 - Reflections
- Description: 
    - Today focused on planning the first helper function and building a clinically relevant symptom checklist
    - Considered balancing formal medical terms with user-friendly input
    - Structuring a backend dictionary, mapping lay terms, basic function planning.
    - Conditions dictionary: keys = formal terms, values = list of symptoms
    - Symptom_aliases dictionary: keys = canonical terms, values = list of lay terms
    - mapped aliases to canonical terms using for loop
- What I learnt today:
	- Importance of normalizing user input for reliability
	- Mapping lay terms to clinical terms allows professional rigor without sacrificing usability
    - Used str.replace() to remove ' - ! . characters
	- Designing a foundational structure makes future ML/NLP integration easier
- Challenges & errors: 
	- Deciding between using lay terms vs clinical terms
    - Deciding on what specific conditions to include since I am very limited by 6 and so will need them to be broad and relevant.
	- Planning a mapping system that will scale as more conditions/symptoms are added
    - Deciding to include symptoms and only obvious signs a lay person can notice or measure easily 
    - Thinking about user input variability
    - Considered clickable options as can potentially be an issue if users may use different words or phrasing for a term
- Help used/references:
	- Clinical knowledge from MBBS training
	- Python basics (LinkedIn Learning)
	- Notion and GitHub for documentation/logging