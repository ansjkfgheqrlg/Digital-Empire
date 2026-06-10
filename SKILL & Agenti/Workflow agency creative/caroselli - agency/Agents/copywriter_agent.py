import json
import re
from Agents.ai_client import call_ai

def extract_json(text):
    """Estrae un blocco JSON dal testo dell'IA."""
    match = re.search(r'```(?:json)?(.*?)```', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

def generate_carousel_copy(topic=None):
    """
    Usa l'IA (Nemotron/Llama3) per generare il copy di un carosello.
    Simula la competenza della skill 'CRO Copy Architect'.
    Restituisce un dizionario contenente la lista delle slide e la descrizione del post.
    """
    
    prompt = f"""
    Sei il CRO Copy Architect di Digital Empire.
    Devi scrivere il copy per un carosello Instagram composto da ESATTAMENTE 3 slide per l'Agency, e anche la descrizione del post (caption per Instagram).
    Il carosello non deve avere muri di testo: frasi estremamente compatte, potenti, orientate alla conversione e corte.
    
    Argomento (se 'None', inventane uno nuovo inedito e potente sul marketing/conversioni per agenzie): {topic}
    
    Regole di Output:
    - Restituisci ESCLUSIVAMENTE un oggetto JSON valido contenente le chiavi "slides" (array di 3 oggetti) e "descrizione" (stringa), senza altro testo prima o dopo.
    - Ogni oggetto nell'array "slides" rappresenta una slide e DEVE avere queste chiavi:
        "slide_numero": intero (1, 2, o 3)
        "titolo_nascosto": (stringa, lo scopo della slide es. "Headline", "Spiegazione", "CTA")
        "testo_esatto": stringa (il testo breve, max 12 parole, che andrà FISICAMENTE stampato sulla slide grafica).
    - La chiave "descrizione" deve contenere la descrizione per il post Instagram, scritta in modo accattivante, con emoji e hashtag rilevanti.
        
    Specifiche delle 3 slide:
    - Slide 1 (Headline / Attenzione): Deve introdurre l'argomento in modo dirompente.
    - Slide 2 (Spiegazione / Struttura): Fornisce la spiegazione o la struttura strategica (ad es. un funnel, una regola, o un framework).
    - Slide 3 (CTA): Il testo_esatto DEVE avere questo formato fisso:
        "scrivimi '[PAROLA]' in Dm per una call gratuita 90% formazione e valore concreto 10% vendita."
        (Sostituisci '[PAROLA]' con una singola parola rilevante legata all'argomento, ad esempio: "Funnel", "Clienti", "Crescita").
        
    ESEMPIO DI OUTPUT ATTESO:
    {{
      "slides": [
        {{
          "slide_numero": 1,
          "titolo_nascosto": "Headline",
          "testo_esatto": "non basta una semplice landing page serve un funnel legato ad essa"
        }},
        {{
          "slide_numero": 2,
          "titolo_nascosto": "Spiegazione",
          "testo_esatto": "un lead magnet forte attrae contatti mentre la landing converte con struttura apsoc"
        }},
        {{
          "slide_numero": 3,
          "titolo_nascosto": "CTA",
          "testo_esatto": "scrivimi 'Funnel' in Dm per una call gratuita 90% formazione e valore concreto 10% vendita."
        }}
      ],
      "descrizione": "Perché le tue landing page non convertono? 🛑 Non basta mandare traffico su una pagina statica. Serve un funnel integrato con un lead magnet potente per educare il pubblico ed eliminare le obiezioni con la struttura APSOC.\\n\\nVuoi sbloccare le deine conversioni? Scrivimi 'Funnel' in DM per prenotare una call gratuita di 30 minuti (90% valore, 10% vendita).\\n\\n#marketing #funnel #cro #agency #digitalempire"
    }}
    """
    
    messages = [
        {"role": "system", "content": "Sei un agente che produce solo e rigorosamente JSON valido come richiesto."},
        {"role": "user", "content": prompt}
    ]
    
    response = call_ai(messages, label="Copywriter")
    
    if not response:
        return None
        
    try:
        clean_json_str = extract_json(response)
        data = json.loads(clean_json_str)
        return data
    except Exception as e:
        print(f"[Copywriter] Errore nel parsing del JSON restituito: {e}")
        print(f"Risposta raw:\n{response}")
        return None
