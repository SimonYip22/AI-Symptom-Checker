Reflection / Learnings:
	•	How rules could evolve into ML
	•	Potential improvements: UI, web app, ML integration

I chose to focus on 6 common primary-care conditions to keep the symptom checker clinically relevant and understandable. 
I also wanted to differentiate the project by using medically precise terms and mapping lay input to clinical terminology. I also wanted to keep it simple by letting the user type symptoms, cons are that users may use different words or phrasing, so I needed to map lay terms into canonical symptoms. I considered using more technical terms (dysuria, polyuria, etc.) to show awareness but ultimately decided not to.

In future iterations, I will handle typos, I plan to expand the rule logic to an ML-based system, include more conditions, use grouping by system (respiratory, neurological, gastrointestinal, etc.) and specialty (paediatrics, infectious disease, psychiatry, etc.), and potentially implement a simple CLI or Streamlit interface.”

In future, I could implement clickable options for easier UX, so present a list of possible symptoms and let the user select (e.g., type a number, or check in GUI/Streamlit later), no guessing needed and less error-prone. Easier in Streamlit or other GUI later