import os
from dotenv import load_dotenv
from openai import OpenAI

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Inizializza i client
or_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

groq_client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

def generate_completion(messages, temperature=0.7):
    """
    Genera la risposta usando NVIDIA Nemotron (via OpenRouter).
    Se fallisce, passa al fallback su Groq (Llama-3-70b).
    """
    try:
        # PRIMA SCELTA: Google Gemma 2 9B (Free & Ultra-Stabile su OpenRouter)
        response = or_client.chat.completions.create(
            model="google/gemma-2-9b-it:free",
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"[AI Client] OpenRouter fallito ({e}). Passaggio al fallback GROQ...")
        
        try:
            # FALLBACK: Groq Llama 3.3 70B
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e_groq:
            print(f"[AI Client] Anche GROQ ha fallito: {e_groq}")
            return "ERRORE: Generazione AI fallita."
