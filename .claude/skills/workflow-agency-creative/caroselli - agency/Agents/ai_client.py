import os
import sys
import time

try:
    from openai import OpenAI
except ImportError:
    print("Manca il modulo openai. Esegui: pip install openai")
    sys.exit(1)

root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.append(root_dir)

import config

def build_rotation():
    """Costruisce la lista di rotazione dei modelli API (Groq -> OpenRouter)"""
    groq_key = config.GROQ_API_KEY.strip()
    openrouter_key = config.OPENROUTER_API_KEY.strip()
    
    rotation = []
    
    if groq_key:
        groq = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=groq_key, timeout=45)
        # Llama 3.3 è eccellente, lo usiamo come primo su Groq (veloce e gratuito)
        rotation.append((groq, "llama-3.3-70b-versatile"))
        
    if openrouter_key:
        or_client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=openrouter_key, timeout=60)
        # Google Gemini 2.5 Flash tramite OpenRouter (estremamente economico, ultra-affidabile e potente)
        rotation.append((or_client, "google/gemini-2.5-flash"))
        # Meta Llama 3.3 70B (versione standard a pagamento su OpenRouter, senza limiti di token giornalieri dei modelli free)
        rotation.append((or_client, "meta-llama/llama-3.3-70b-instruct"))
        # Nemotron 70B (versione standard su OpenRouter)
        rotation.append((or_client, "nvidia/nemotron-4-340b-instruct"))
        
    return rotation

def call_ai(messages, max_tokens=2000, temperature=0.7, label="AI"):
    rotation = build_rotation()
    if not rotation:
        print(f"[{label}] Errore: Nessuna API Key configurata per Groq o OpenRouter.")
        return None

    for attempt, (client, model) in enumerate(rotation):
        try:
            print(f"[{label}] Chiamata a {model}...")
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            provider = "Groq" if "groq" in str(client.base_url) else "OpenRouter"
            print(f"[{label}] Errore {provider}/{model}: {e}")
            if attempt < len(rotation) - 1:
                print(f"[{label}] Ritento con il prossimo modello...")
                time.sleep(2)
            else:
                print(f"[{label}] Tutte le API hanno fallito.")
                
    return None
