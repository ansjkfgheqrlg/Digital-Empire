import os
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

# ==========================================
# APEX-7 | YOUTUBE AUTOMATION CONDUCTOR
# Orchestratore Idempotente
# ==========================================

# Risoluzione percorsi relativi alla directory base della Skill
BASE_DIR = Path(__file__).resolve().parent.parent
AGENTS_DIR = BASE_DIR / "03-AGENTI-E-RUOLI" / "operatori"
DASHBOARD_DIR = BASE_DIR / "06-DASHBOARD-E-METRICHE"
STATE_FILE = DASHBOARD_DIR / "state.json"

# Carica API keys dal root dell'ecosistema o dalla directory locale
load_dotenv(BASE_DIR.parent / ".env")
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

def log(msg, color="white"):
    """Logger colorato stile APEX"""
    colors = {
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "cyan": "\033[96m",
        "purple": "\033[95m",
        "white": "\033[0m"
    }
    print(f"{colors.get(color, colors['white'])}{msg}\033[0m")

def call_llm(prompt: str, context: str = "") -> str:
    """Chiama Gemini (o Anthropic) per eseguire il prompt dell'agente."""
    full_prompt = f"{prompt}\n\n--- CONTESTO DELLE FASI PRECEDENTI ---\n{context}" if context else prompt
    
    if GEMINI_API_KEY:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": full_prompt}]}]}
        
        log("[*] Invocazione Gemini API (gemini-2.5-flash)...", "purple")
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code != 200:
            raise Exception(f"API Gemini Error: {response.text}")
            
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        
    elif ANTHROPIC_API_KEY:
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        data = {
            "model": "claude-3-5-sonnet-20240620",
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": full_prompt}]
        }
        log("[*] Invocazione Anthropic API (Claude 3.5)...", "purple")
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code != 200:
            raise Exception(f"API Anthropic Error: {response.text}")
            
        return response.json()["content"][0]["text"]
    else:
        raise ValueError("Nessuna API Key trovata nel file .env (GEMINI_API_KEY o ANTHROPIC_API_KEY)")

def read_agent_prompt(agent_filename: str) -> str:
    """Legge il file markdown contenente il prompt dell'agente."""
    path = AGENTS_DIR / agent_filename
    if not path.exists():
        raise FileNotFoundError(f"File agente non trovato: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_state():
    """Carica lo stato dell'esecuzione (Idempotenza)."""
    if STATE_FILE.exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"current_phase": 1, "context": {}}

def save_state(state):
    """Salva lo stato corrente per permettere la ripresa automatica."""
    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)

def run_pipeline():
    log("\n==========================================", "cyan")
    log(" ⚡ ANTIGRAVITY ENGINE: YOUTUBE FACTORY ⚡ ", "cyan")
    log("==========================================\n", "cyan")
    
    state = load_state()
    phase = state.get("current_phase", 1)
    context_data = state.get("context", {})
    
    # Definizione lineare del workflow
    phases = [
        {"id": 1, "name": "Niche Scout", "agent": "niche-scout.md", "key": "niche_idea"},
        {"id": 2, "name": "Video Hunter", "agent": "video-hunter.md", "key": "video_research"},
        {"id": 3, "name": "SEO Analyst", "agent": "seo-analyst.md", "key": "seo_strategy"},
        {"id": 4, "name": "Script Writer", "agent": "script-writer.md", "key": "video_script"},
        {"id": 5, "name": "Metadata Optimizer", "agent": "metadata-optimizer.md", "key": "metadata"},
    ]
    
    for p in phases:
        if phase > p["id"]:
            log(f"⏩ FASE {p['id']} [{p['name']}] già completata. Salto.", "yellow")
            continue
            
        log(f"▶ ESECUZIONE FASE {p['id']}: {p['name']}", "cyan")
        
        try:
            # Carica il ruolo
            agent_prompt = read_agent_prompt(p["agent"])
            
            # Passa tutto il contesto accumulato (es: idea -> research -> script)
            context_string = json.dumps(context_data, indent=2, ensure_ascii=False) if context_data else ""
            
            # Esecuzione
            output = call_llm(agent_prompt, context_string)
            
            # Salvataggio Output
            context_data[p["key"]] = output
            state["current_phase"] = p["id"] + 1
            state["context"] = context_data
            save_state(state)
            
            log(f"✅ FASE {p['id']} COMPLETATA! Stato aggiornato in state.json\n", "green")
            
            # Rate limiting leggero
            time.sleep(2)
            
        except FileNotFoundError as e:
            log(f"⚠️ {e} - Assicurati che il file esista in 03-AGENTI-E-RUOLI/operatori", "red")
            break
        except Exception as e:
            log(f"❌ ERRORE DURANTE LA FASE {p['id']}: {e}", "red")
            break
            
    if state.get("current_phase", 1) > len(phases):
        log("\n🎉 TUTTE LE FASI DELLA YOUTUBE FACTORY COMPLETATE CON SUCCESSO! 🎉", "green")
        log(f"Verifica l'output completo in: {STATE_FILE}", "cyan")

if __name__ == "__main__":
    run_pipeline()
