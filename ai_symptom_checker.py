conditions = {

    "Urinary Tract Infection (urine infection)": ["urinary frequency", "urinary urgency",
                                                  "painful urination", "night time urination", 
                                                  "blood in urine", "suprapubic pain", "fever",
                                                  "discharge", "foul smelling urine"], 

    "Influenza (flu)": ["cough", "coryza", "fever", "rigors", "fatigue",
                        "anorexia", "headache", "myalgia", "nausea", "vomiting"],

    "Gastroenteritis": ["diarrhoea", "nausea", "vomiting", "anorexia", "malaise",
                        "fever", "bloody diarrhoea", "abdominal pain"],
    "Otitis Media": ["ear pain", "fever", "ear discharge", "hearing loss"],

    "Migraine": ["nausea", "vomiting", "headache", "flashing lights", "visual defect",
                 "photophobia", "phonophobia", "neck pain"],

    "Pneumonia": ["chest pain", "shortness of breath", "cough",
                  "purulent sputum", "blood-stained sputum", "fever"]
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
    "fatigue": ["tired", "exhausted"],
    "anorexia": ["loss of appetite", "not hungry", "cant eat"],
    "headache": ["head pain"],
    "myalgia": ["muscle aches", "body aches"],
    "nausea": ["feel sick", "feeling sick"],
    "vomiting": ["throwing up", "sick"],

    "diarrhoea": ["loose stools", "runny stools", "runny poo"],
    "malaise": ["tired", "fatigue"],
    "bloody diarrhoea": ["blood in stool", "blood in poo", "bloody stool"],
    "abdominal pain": ["stomach pain", "tummy pain"],

    "ear pain": ["ear ache", "ear hurts"],
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
def normalize_choice_input(input_text):
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
    return cleaned

#usage
user_input = input("What symptom do you have? ")
normalized = normalize_choice_input(user_input)
print("You typed:", user_input)
print("Canonical symptom detected:", normalized)
