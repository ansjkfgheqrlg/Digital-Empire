import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.AI_Team import ai_client

REVIEWER_PROMPT = """
Sei un Senior Editor e CRO Specialist esperto. Il tuo compito è revisionare il copy scritto da un tuo collega.
Devi essere severo e pignolo. Assicurati che il copy rispetti questi criteri:

1. PROPORZIONE: È davvero 90% valore/formazione e solo 10% vendita?
2. HOOK: La prima frase è magnetica? Ferma lo scroll?
3. CTA: La Call to Action finale è chiara e spinge a prenotare la "Briefing Call" (o seguire la pagina)?
4. LINGUAGGIO: È umano, emozionante e privo di "AI-isms" (parole troppo robotiche o pompose)?
5. STRUTTURA: È facile da leggere (frasi brevi, paragrafi puliti)?

Rispondi in questo formato:
STATUS: [APPROVATO o RIFIUTATO]
FEEDBACK: [Se rifiutato, elenca i punti da migliorare. Se approvato, lascia vuoto.]
"""

def review_copy(topic, copy_draft):
    """
    Revisiona il copy e restituisce lo stato e il feedback.
    """
    print(f"[Reviewer Agent] Audit del copy in corso...")
    
    messages = [
        {"role": "system", "content": REVIEWER_PROMPT},
        {"role": "user", "content": f"Argomento: {topic}\n\nCopy da revisionare:\n{copy_draft}"}
    ]
    
    response = ai_client.generate_completion(messages, temperature=0.3)
    
    approved = "STATUS: APPROVATO" in response.upper()
    feedback = ""
    if "FEEDBACK:" in response:
        feedback = response.split("FEEDBACK:")[1].strip()
        
    return approved, feedback
