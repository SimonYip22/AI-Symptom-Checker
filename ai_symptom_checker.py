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
    "foul-smelling urine": ["smelly urine", "bad smell in pee"],

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

    max_symptoms = max(len(symptoms_dict) for symptoms_dict in conditions.values())

    scores = {} #stores the total score for each condition as a dictionary
    
    for condition, symptoms_dict in conditions.items(): #loop through each condition

        num_symptoms = len(symptoms_dict) #total number of symptoms for this condition
    
        total_possible = 0
        for symptom, value in symptoms_dict.items(): 
            total_possible = total_possible + value #total possible score for this condition 

        total_score = 0 #start score at 0
        for symptom in user_symptoms: #loop through every symptom the user entered in the list
            if symptom in symptoms_dict: #check if symptom exists for this condition
                total_score = total_score + symptoms_dict[symptom] #add the weighted score
    
        adjusted_score = (total_score/total_possible) * (num_symptoms/max_symptoms) #gives you the value for each condition
        scores[condition] = adjusted_score #scores dictionary now has key = condition, value = adjusted_score
   
    return scores #returns score dictionary containing every condition since it is outside the loop


if __name__ == "__main__": #when you run Python from terminal __name__ is set to __main__
    while True: #create infinite loop
        user_input = user_symptoms_list() #asks the user for symptoms and stores them as user_input
        scores = score_conditions(user_input) #calculates scores for each condition based on those symptoms and stores them

        print("\nCondition scores:")
        for condition, score in scores.items(): #for loop will print each output on a different line
            print(f"{condition}: {score:.3f}") #prints the number to 3 decimal places

        print("\nEnter a new set of symptoms to score again.\n")


def display_results():
    user_input = user_symptoms_list()
    scores = score_conditions(user_input)

    sorted_conditions = sorted(scores.items(), key = lambda x: x[1], reverse=True) #turn the dictionary iterables into tuples, sort by highest value. 
                                                                                   #lambda x is a small function that takes x as the input (x is the tuple)
                                                                                   # x[1] is second element of the tuple (the value)
                                                                                   #reverse=True sorts from high to low. If ommited or reverse=False then defaults to low to high

    print("\nCondition scores:")
    for condition, score in sorted_conditions:
            matched = [s for s in user_input if s in conditions[condition]]
            print(f"{condition}: {score:.3f} | Matched symptoms: {matched}")