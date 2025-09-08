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


---


# Day 2 — Scoring System  

## Goals  
- Implement a weighted scoring function (score_conditions) to rank medical conditions based on user-entered symptoms.
- Test the function with example symptom combinations to ensure correctness and logical ranking.
- Introduce an “adjusted score” formula to account for conditions with differing numbers of symptoms.



## Goal Explanation  
- The scoring function is the core reasoning engine of the symptom checker.
- It transforms raw user symptom inputs into condition likelihoods by weighting symptom importance and normalizing across conditions.
- This step moves the project from simple input handling to a tool that approximates clinical prioritization logic.
- Adjusted scoring prevents bias toward conditions with either very few or very many symptoms.



## Plan / Thoughts  
1.	Standardize user input:
    - Use normalise_choice_input to map user-entered symptoms to canonical symptom names.
    - Ignore or provide feedback for unrecognized symptoms.
2.	Define condition weights:
    - Each condition is a dictionary: keys = canonical symptom names, values = symptom importance scores.
3.	Score calculation:
    - Calculate max_symptoms.
    - Loop through each condition.
    - For each condition:
        - Calculate num_symptoms (total symptoms listed for that condition).
        - Sum total_possible (sum of all symptom weights for that condition).
        - Loop through user symptoms and add corresponding weights to total_score for matches.
    - Calculate adjusted_score for each condition:

    adjusted score for each condition = (input score/total possible score) * (number of symptoms in condition/max number of symptoms amoung all conditions)

    - This normalizes scores so no single minor symptom dominates a condition with few symptoms, and conditions with more symptoms aren’t unfairly penalized.
    - where they go:
        1.	Before the outer loop, calculate max_symptoms.
        2.	Inside the outer loop, calculate total_possible and num_symptoms for that condition.
        3.	After summing total_score (your existing logic), calculate adjusted_score.
        4.	Store adjusted_score instead of total_score in your scores dictionary.
4.	Store results:
	- scores[condition] = adjusted_score → dictionary maps each condition to its final score.
5.	Testing:
	- Manual tests with single and multiple symptom inputs.
	- Confirm that:
        - Conditions with matching symptoms score higher.
        - Adjusted scoring behaves as intended.
        - Invalid symptoms are ignored or reported without crashing.



## Reflections  
- Nested loops and dictionary handling: Iterating over multiple lists/dictionaries and accumulating values reinforced Python looping concepts.
- Input validation and normalization: Learned the importance of preprocessing user input before scoring.
- Adjusted scoring formula:
    - Helps balance conditions with different numbers of symptoms.
    - Prevents single minor symptoms from disproportionately influencing scores.
- Function modularity:Scoring is separated from input handling and later from output display. This makes the code easier to test and extend.
- Testing strategy:
	- Writing test_matcher.py reinforced automated testing for edge cases (single symptom, multiple matches, invalid input, empty input).
	- Automated tests confirmed that the scoring logic matched expectations without manually entering data every time.
- Debugging insights:
	- Understanding .items(), .append(), and dictionary assignments was critical for correct implementation.
	- Learned to distinguish between accumulating a score vs storing matched items in a dictionary for reference.


---


# Day 3: Presentation

## Goals
- Implement a function `display_results` to rank conditions based on the scores from Day 2.
- Show which symptoms matched each condition to provide transparency.
- Test the ranking and display with example symptom lists.
- Implement a simple user interface to repeatedly run the symptom checker or exit gracefully.


## Goal Explanation / Plan
- Take the dictionary of scores returned by score_conditions(user_symptoms).
- Sort the conditions in descending order by score (e.g., using sorted(scores.items(), key=lambda x: x[1], reverse=True)) so the most likely conditions appear first.
- For each condition, display:
	- Condition name
	- Percentage score (scaled from weighted symptom values)
	- Matched symptoms from user input
- Show only the top 3 conditions for clarity.
- Identify the most likely diagnosis based on the highest score.
- Display specific advice for the most likely diagnosis using the advice dictionary.
- Finish with a safety disclaimer reminding users this is educational only.
- Keep the function modular to allow reuse or extension in future improvements.
- Wrap the entire interaction in a while loop so users can press Enter to start again or type “exit” to quit:

                while True:
                    command = input("Press Enter to start symptom checker, or type 'exit' to quit: ")
                    if command.lower() == "exit":
                        break
                    display_results()

## Reflections
- Sorting the results clearly shows the most likely conditions first, improving usability.
- Displaying matched symptoms adds explainability to the AI logic, making it easier to justify why a condition was ranked higher.
- Reinforced understanding of Python concepts: dictionaries, loops, sorting, string formatting, and modular function design.
- Learned how to connect outputs from one function (score_conditions) to another (display_results) in a pipeline.
- Learned user interface design considerations:
    - Using input() to start or exit the program
    - Understanding that pressing Enter returns an empty string "" that can trigger the function
    - Avoiding confusing prompts like “Enter a new set of symptoms to score again” — pressing Enter alone suffices to restart.
- Clarified edge cases:
    - Empty symptom list
    - No matched symptoms for a condition
    - Tie scores between conditions
- Learned to clean and normalize input with a dedicated function (normalise_choice_input) to handle aliases and user typos.
- Practiced debugging and understanding function flow, including:
    - Why display_results() runs after pressing Enter
    - How to structure a repeating loop for continuous user interaction
    - How to avoid overwriting Python keywords (continue cannot be used as a variable)
- Clarified several confusions during implementation:
  - Initially struggled with `sorted_conditions[0][0]`; learned this is tuple unpacking to access just the condition name.
  - Unsure why `advice[likely_diagnosis]` worked; now understand this retrieves the advice string using the condition name as a dictionary key.
  - Got stuck on input loop logic and prompt wording (pressing Enter vs. typing `exit`); rewrote it so the flow is intuitive for users.
- Overall, reinforced modular design and readability, making future modifications (like adding new conditions or advice) simple.


---


# v2 — FastAPI / API

## Goals
- Wrap CLI symptom checker as deployable API
- Provide JSON output for top conditions, matched symptoms, likely diagnosis, and advice
- Keep CLI code modular and separate

## Implementation
- app.py endpoints:
    - GET /health → API health check
    - POST /predict → input: list of symptoms, output: JSON
- Pydantic Symptoms model validates input
- JSON output includes:
    - user_symptoms (normalised)
    - top_conditions (top 3, percentage, matched symptoms)
    - likely_diagnosis
    - advice

## Reflections
- API-ready JSON output makes project portfolio-ready
- Screenshots captured:
	1.	Swagger UI home page
	2.	Health check response
	3.	/predict input/output JSON
- Demonstrates clinical + technical skill:
    - Domain expertise encoded in weights
	- Structured outputs for automated consumption
	- CLI/API separation ensures modularity

## Testing
- Automated tests via pytest + httpx for endpoint validation
- Ensures outputs consistent with v1 CLI


---