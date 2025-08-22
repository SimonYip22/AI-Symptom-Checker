# Final Reflection

## Project Overview
This project was a rule-based **symptom checker** designed to score and rank a small set of common primary care conditions. The aim was to build a transparent, modular program where users could enter symptoms, receive ranked conditions, and see which symptoms matched each condition. The scope was intentionally limited to six clinically relevant conditions to keep it understandable and medically grounded.

A key differentiator was my decision to use medically precise terminology while also mapping layperson inputs to canonical symptoms. This helped maintain clinical accuracy while making the tool usable for non-medical users.


## What I have learnt
Throughout the project, I built both technical and conceptual skills:

- **Python Fundamentals**: Strengthened understanding of dictionaries, loops, conditional logic, sorting, modular functions, and pipelines (connecting `score_conditions` to `display_results`).  
- **Explainability in AI/logic systems**: Learned to provide transparency by showing which symptoms matched each condition.  
- **Debugging & Iteration**: Faced challenges with indentation, loops, and program flow (e.g., ensuring the Enter key restarted the loop correctly).  
- **False Starts**: Initially thought JSON was needed for storing conditions, but later realised dictionaries sufficed. Reinforced the importance of clarity and simplicity over premature optimisation.  
- **Prompt Design & Usability**: Learned that precise wording matters; for example, “Press Enter to continue” vs. “Enter new symptoms or type exit” affected user flow.

---

## Design Choices
- Limited to **six primary care conditions** for clinical focus.  
- Balanced **clinical precision** (canonical terms like “polyuria, dysuria”) with usability, opting for simpler input terms but demonstrating awareness of technical vocabulary.  
- Chose **typed symptom input** for simplicity, despite its limitations (variations in phrasing, typos).

---

## Future Improvements
Reflecting on this build, several areas for enhancement are evident:

- **Input Handling**: Expand synonym mapping, handle typos, and eventually allow structured clickable symptom options to reduce user error.  
- **Clinical Breadth**: Add more conditions, grouped by system (respiratory, neurological, gastrointestinal, etc.) and specialty (paediatrics, psychiatry, infectious disease).  
- **User Interface**: Transition from CLI to a Streamlit or web-based app with checkboxes or dropdowns for easier UX.  
- **Explainability & Advice**: Provide not just conditions and scores, but tailored advice for next steps, red flags, and disclaimers.  
- **Scalability**: Evolve from simple rule-based logic into a machine learning–based system, potentially using a dataset to train and validate models.

---

## Key Takeaways
1. Start simple: dictionaries and lists were sufficient; JSON or other data formats can be added later as the project scales.  
2. Usability matters: clear instructions and prompts improve the intuitiveness of the program.  
3. Incremental development with daily testing and reflection made the project more manageable.  
4. This project demonstrates how **rule-based systems can form the foundation for ML approaches**, bridging from handcrafted logic to data-driven intelligence.