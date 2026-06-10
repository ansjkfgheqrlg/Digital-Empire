from Agents.copywriter_agent import generate_carousel_copy

def get_final_carousel_plan(topic=None):
    """
    In una versione più avanzata, questo orchestratore avvierebbe anche il ReviewerAgent
    per controllare il copy e iterare.
    Per la versione attuale (che alimenta Arena.ai), ci basta la generazione CRO perfetta 
    dal Copywriter.
    """
    print("[Orchestrator AI] Avvio team per generazione Copy...")
    
    res = generate_carousel_copy(topic)
    
    if res and "slides" in res:
        slides = res["slides"]
        descrizione = res.get("descrizione", "")
        print(f"[Orchestrator AI] Generato carosello di {len(slides)} slide con successo.")
        
        # Determina un nome argomento dalla prima slide o uno standard (rimuovendo caratteri non validi in Windows)
        import re
        try:
            # Sostituisce spazi con underscore e rimuove caratteri non validi in Windows (es. due punti, asterischi, ecc.)
            text_clean = slides[0]['testo_esatto'].replace(" ", "_")
            topic_name = re.sub(r'[^a-zA-Z0-9_]', '', text_clean).strip()
            # Tronca se troppo lungo
            topic_name = topic_name[:30]
            if not topic_name:
                topic_name = "Carosello_Marketing"
        except:
            topic_name = "Carosello_Marketing"
            
        return slides, descrizione, topic_name
        
    else:
        print("[Orchestrator AI] Fallimento critico nella generazione del testo.")
        return None, None, None
