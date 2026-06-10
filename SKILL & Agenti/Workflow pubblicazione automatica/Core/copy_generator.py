import os
import sys

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Nota: richiede l'installazione di openai `pip install openai`
# import openai

# Legge il prompt dal config di Instagram (usato come base per tutto il flusso Agency)
from Core.AI_Team import orchestrator_ai
from Instagram import config as ig_config

def generate_caption(topic_name, brand_config=None):
    """
    Genera la caption usando il Team di Agenti AI (Nemotron/Groq).
    """
    print(f"[Copywriter AI] Avvio Team di Agenti per l'argomento: '{topic_name}'")
    
    # Se non viene passato un config specifico, usa quello di default (Agency)
    config = brand_config if brand_config else ig_config
    
    system_prompt = getattr(config, "COPYWRITER_SYSTEM_PROMPT", "")
    
    try:
        # Il processo ora coinvolge Writer e Reviewer
        final_copy = orchestrator_ai.generate_perfect_copy(topic_name, system_prompt)
        
        # Se la generazione restituisce un errore o è vuota, forziamo il fallback
        if "ERRORE" in final_copy or len(final_copy.strip()) < 50:
            raise ValueError("Generazione AI non valida o vuota.")
            
        return final_copy
        
    except Exception as e:
        print(f"[Copywriter AI] Attivo il copy di fallback premium a causa dell'errore: {e}")
        
        # Splendido copy di fallback specifico per il tema di Mentalità Brutale
        fallback_copy = (
            "Realizzi che il 90% dei tuoi problemi sono causati da una versione di te che non vuole lavorare? 🔥\n\n"
            "La verità è cruda: non sono le circostanze, non è l'economia, non è la sfortuna. È quella parte di te che sceglie la comodità invece della disciplina. \n\n"
            "Ogni volta che rimandi, ogni volta che cedi alla pigrizia, stai nutrendo la versione di te che ti tiene bloccato. \n\n"
            "Se vuoi cambiare la tua vita, devi sconfiggere quel nemico interiore. Smetti di cercare scuse. Inizia a lavorare su te stesso con costanza e dedizione totale. La disciplina è l'unica via per la vera libertà. 🐺🚀\n\n"
            "Salva questo Reel e segui la pagina per non perdere i prossimi video di pura mentalità.\n\n"
            "#mentalitavincente #disciplina #successo #businessitalia #mentalitadesistente #crescitapersonale"
        )
        return fallback_copy

