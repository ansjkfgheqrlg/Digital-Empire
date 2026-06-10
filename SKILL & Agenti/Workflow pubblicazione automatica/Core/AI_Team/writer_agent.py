import sys
import os

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from Core.AI_Team import ai_client

def generate_initial_draft(topic, system_prompt):
    """
    Genera la prima bozza del copy basata sul topic e sulle istruzioni del brand.
    """
    print(f"[Writer Agent] Generazione bozza per: {topic}")
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"L'argomento del contenuto è: '{topic}'. Scrivi un copy impeccabile seguendo i framework CRO e la struttura 90% valore / 10% vendita."}
    ]
    
    return ai_client.generate_completion(messages)

def refine_draft(topic, original_draft, feedback, system_prompt):
    """
    Raffina la bozza basandosi sul feedback del Reviewer.
    """
    print(f"[Writer Agent] Raffinamento bozza basato sul feedback...")
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Argomento: {topic}\n\nEcco la tua bozza precedente:\n{original_draft}\n\nIl Reviewer ha dato questo feedback:\n{feedback}\n\nPer favore, riscrivi il copy correggendo questi punti e rendendolo perfetto."},
    ]
    
    return ai_client.generate_completion(messages)
