
conditions = {

    "Urinary Tract Infection (urine infection)": {"urinary frequency": 3, "urinary urgency": 3,
                                                  "painful urination": 3, "night time urination": 2, 
                                                  "blood in urine": 2, "suprapubic pain": 1, "fever": 1,
                                                  "discharge": 1, "foul smelling urine": 3}, 

    "Influenza (flu)": {"cough": 3, "coryza": 1, "fever": 3, "rigors": 2, "fatigue": 3,
                        "anorexia": 1, "headache": 1, "myalgia": 2, "nausea": 2, "vomiting": 2, "sore throat": 2},

    "Gastroenteritis (stomach bug)": {"diarrhoea": 3, "nausea": 3, "vomiting": 3, "anorexia": 3, "malaise": 1,
                                      "fever": 1, "bloody diarrhoea": 2, "abdominal pain": 2},

    "Otitis Media (inner ear infection)": {"ear pain": 3, "fever": 2, "ear discharge": 1, "hearing loss": 2},

    "Migraine": {"nausea": 2, "vomiting": 2, "headache": 3, "flashing lights": 3, "visual defect": 3,
                 "photophobia": 3, "phonophobia":3, "neck pain": 1},

    "Pneumonia (chest infection)": {"chest pain": 3, "shortness of breath": 3, "cough": 3,
                                    "purulent sputum": 2, "blood stained sputum": 2, "fever": 1}
}


symptom_aliases = {
    "urinary frequency": ["wee a lot", "weeing a lot", "going to toilet often"],
    "urinary urgency": ["need to pee urgently", "cant hold pee", "cant hold in pee"],
    "painful urination": ["painful pee", "burning pee", "stinging pee"],
    "night time urination": ["night time pee", "peeing at night"],
    "blood in urine": ["blood in pee", "red urine"],
    "suprapubic pain": ["lower tummy pain", "pain above pubic bone"],
    "fever": ["temperature", "high temperature"],
    "discharge": ["fluid from penis", "fluid from vagina"],
    "foul smelling urine": ["smelly urine", "bad smell in pee"],

    "cough": ["coughing", "hacking cough"],
    "coryza": ["runny nose", "stuffy nose", "blocked nose"],
    "rigors": ["shivering", "shivers"],
    "fatigue": ["tired", "exhausted", "weakness"],
    "anorexia": ["loss of appetite", "not hungry", "cant eat"],
    "headache": ["head pain"],
    "myalgia": ["muscle aches", "body aches"],
    "nausea": ["feel sick", "feeling sick"],
    "vomiting": ["throwing up", "sick"],
    "sore throat": ["painful throat", "throat hurts", "scratchy throat"],

    "diarrhoea": ["loose stools", "runny stools", "runny poo"],
    "malaise": ["tired", "fatigue"],
    "bloody diarrhoea": ["blood in stool", "blood in poo", "bloody stool"],
    "abdominal pain": ["stomach pain", "tummy pain"],

    "ear pain": ["ear ache", "ear hurts", "earache"],
    "ear discharge": ["fluid from ear", "ear fluid"],
    "hearing loss": ["trouble hearing", "difficulty hearing", "blocked hearing"],

    "flashing lights": ["seeing flashing lights", "seeing flashes", "seeing sparkles"],
    "visual defect": ["blurred vision"],
    "photophobia": ["sensitive to light"],
    "phonophobia": ["sensitive to sound"],
    "neck pain": ["neck stiffness", "stiff neck", "neck hurts"],

    "chest pain": ["chest ache", "chest hurts"],
    "shortness of breath": ["difficulty breathing", "short of breath"],
    "purulent sputum": ["green phlegm", "yellow phlegm"],
    "blood stained sputum": ["coughing blood", "coughing up blood", "blood in phlegm"]
}

advice = {
    
          "Urinary Tract Infection (urine infection)": "Paracetamol +/- ibuprofen for pain relief,\n Pharmacist or GP may prescribe a short course of antibiotics.",
          
          "Influenza (flu)": "Rest and sleep, keep warm, paracetamol +/- ibuprofen for fever and pain,\n Drink plenty of water to stay hydrated, stay at home and avoid contact with others to prevent spreading,\n Cover mouth and nose with tissue when cough or sneezing, dispose of immediately,\n Wash hands regularly with soap and water.",

          "Gastroenteritis (stomach bug)": "Stay at home and get plenty of rest, drink plenty of water to stay hydrated (small sips if you feel sick),\n Try and eat when you feel able to, paracetamol +/- ibuprofen if in pain.",

          "Otitis Media (inner ear infection)": "Paracetamol +/- ibuprofen for pain relief, remove any discharge by wiping ear with cotton wool,\n Do not put anything inside your ear, do not let water into ear, do not go swimming while you have an ear infection.\n Pharmacist or GP may prescribe antibiotic ear drops",

          "Migraine": "Paracetamol +/- ibuprofen for pain reflief, try sleeping or laying down in a dark room during migraine,\n Pharmacist or GP may prescribe Triptans (e.g. Sumatriptan) +/- anti-sickness medication.\n Prevention: Stay hydrated and limit caffeine and alcohol intake, eat regular meals,\n avoid known triggers, get regular exercise, get plenty of sleep, manage stress.",

          "Pneumonia (chest infection)": "Pharmacist or GP will prescribe antibiotics.\n Rest and drink plenty of fluids, paracetamol +/- ibuprofen for fever and pain,\n cover mouth and nose with tissue when cough or sneezing, dispose of immediately,\n Wash hands regularly with soap and water."
}

#function for cleaning the text the user inputs
def normalise_choice_input(input_text):
    cleaned = input_text.strip().lower()
    cleaned = cleaned.replace("'", "")
    cleaned = cleaned.replace("-", " ")
    cleaned = cleaned.replace("!", "")
    cleaned = cleaned.replace(".", "")

    for canonical, aliases in symptom_aliases.items():
        if cleaned == canonical: #if user input is same as the canonical symptom
            return canonical
        if cleaned in aliases: #if user input matches a lay term 
            return canonical
    return None



def user_symptoms_list():
    user_symptoms = []
    print("Enter symptoms one by one. Type 'done' when finished.\n")

    while True: #loop continues indefinitely until user types "done"
        symptom = input("Enter a symptom: ")
        if symptom.lower() == "done": #if done is entered then the while loop breaks
            break 

        normalised = normalise_choice_input(symptom) #each user input is cleaned by the function

        if normalised is None: #if the user input flagged as invalid in the cleaning function
            print(f"'{symptom}' not recognised as a valid symptom. Please try again. ")
            continue #go back to start of loop, invalid inputs are ignored and not added to the list

        user_symptoms.append(normalised) #adds each valid cleaned symptom into the list
    
    print("You have entered these symptoms: ", user_symptoms)
    return user_symptoms



def score_conditions(user_symptoms):
    """
    Compute normalized, adjusted scores for each condition based on user_symptoms.
    Duplicate symptoms in the input list are ignored (counted once).
    """
    # Keep order but remove duplicates (so duplicates don't inflate scores)
    unique_symptoms = list(dict.fromkeys(user_symptoms))

    # Find the condition with the most symptoms (used for length adjustment)
    max_symptoms = max(len(symptoms_dict) for symptoms_dict in conditions.values())

    scores = {}

    for condition, symptoms_dict in conditions.items():
        num_symptoms = len(symptoms_dict)
        total_possible = sum(symptoms_dict.values())

        # Sum weights only for matched unique symptoms
        total_score = sum(
            symptoms_dict[s] for s in unique_symptoms if s in symptoms_dict
        )

        # Safeguard: avoid division by zero
        if total_possible > 0:
            adjusted_score = (total_score / total_possible) * (num_symptoms / max_symptoms)
        else:
            adjusted_score = 0.0

        scores[condition] = adjusted_score

    return scores


def display_results():
    user_symptoms = user_symptoms_list() #name the list output of the function a new variable which is outside the scope of the function
    scores = score_conditions(user_symptoms) #input the list into the function, name the dictionary output a new variable name score

    sorted_conditions = sorted(scores.items(), key = lambda x: x[1], reverse=True) #turn the dictionary iterables into tuples, sort by highest value. 
                                                                                   #lambda x is a small function that takes x as the input (x is the tuple)
                                                                                   # x[1] is second element of the tuple (the value)
                                                                                   #reverse=True sorts from high to low. If ommited or reverse=False then defaults to low to high
        

    print("\nTop 3 possible conditions:")
    for condition, score in sorted_conditions[0:3]: #loop for each condition, we only want the top 3 though
        matched = [s for s in user_symptoms if s in conditions[condition]] #list comprehension, take each item in the user_input list and call it s, only add s into the list comprehension if it matches a key of the symptoms dictionary
                                                                        #'in' iterates through the keys of the symptoms dictionary for that condition
                                                                        #Take each symptom s from the user input, but only keep it if it exists in the current condition’s symptom list.
        
        percentage_score = score * 100 #convert the number into a percentage
        
        print(f"{condition}: {percentage_score:.1f}% | Matched symptoms: {matched}") #print the percentage score to 1 dp, and also the matched symptoms list to the condition
    
    likely_diagnosis = sorted_conditions[0][0] #the most likely diagnosis is the condiiton with the highest score, pick the first tuple [0], then pick the first element in the first tuple [0][0]

    if likely_diagnosis in advice: #if the condition is in the dictionary, print the corresponding value to the key condition that matches the likely_diagnosis
        print("\nLikely diagnosis is: ", likely_diagnosis)
        print("Advice:", advice[likely_diagnosis]) #we are calling the dictionary value by its key advice[likely_diagnosis]

    print("Important: This tool is for educational purposes only and does not replace medical advice. If you are worried about your symptoms, please contact NHS 111.\n Call 999 or go to A&E immediately if your symptoms are severe, sudden, or life-threatening.") 


if __name__ == "__main__": #when you run Python from terminal __name__ is set to __main__
    while True: #create infinite loop
        command = input("Press Enter to start symptom checker, or type 'exit' to quit: ")
        if command.lower() == "exit":
            print("Goodbye!")
            break #while loop only breaks if exit is input, otherwise, display_results will run

        display_results() 