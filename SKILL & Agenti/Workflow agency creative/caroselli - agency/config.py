# config.py
import os

# Credenziali API per Team Agenti (Nemotron / Groq / OpenRouter)
GROQ_API_KEY = "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"
OPENROUTER_API_KEY = "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"

# Arena.ai configurazione
ARENA_EMAIL = "max.infoproducer@gmail.com"
ARENA_PASSWORD = "Max.23.09"
ARENA_CHAT_URL = "https://arena.ai/c/019e0848-07c0-7e49-b8a1-b4c2a8af388e"

# Path locale per il download dei file e gli allegati di contesto
LOCAL_DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_caroselli")

# Path della directory del progetto (calcolato automaticamente)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ALLEGATI_DIR = os.path.join(PROJECT_DIR, "allegati di contesto (slide)")

# Path su Google Drive
DRIVE_ROOT_FOLDER = "Digital Empire"
DRIVE_IG_FOLDER = "IG page"
DRIVE_AGENCY_FOLDER = "Agency"
DRIVE_CAROUSELLI_FOLDER = "caroselli"
