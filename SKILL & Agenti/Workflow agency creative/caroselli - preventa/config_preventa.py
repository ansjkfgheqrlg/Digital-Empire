# config_preventa.py
# Riusa le credenziali/chiavi del progetto Agency (stesso account Arena, stesse
# API key Groq/OpenRouter) - non duplicate qui apposta, per non avere due copie
# delle stesse credenziali in due file diversi (una sola fonte da ruotare se
# Max decide di rigenerarle - vedi CP-20260803-006 nota sicurezza).
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENCY_DIR = os.path.join(os.path.dirname(PROJECT_DIR), "caroselli - agency")
if AGENCY_DIR not in sys.path:
    sys.path.append(AGENCY_DIR)

import config as agency_config  # noqa: E402 - riuso chiavi/credenziali esistenti

GROQ_API_KEY = agency_config.GROQ_API_KEY
OPENROUTER_API_KEY = agency_config.OPENROUTER_API_KEY
ARENA_EMAIL = agency_config.ARENA_EMAIL
ARENA_PASSWORD = agency_config.ARENA_PASSWORD

# Verificato leggendo arena_generator.py: generate_carousel_visuals() apre SEMPRE
# https://arena.ai/ da capo per ogni slide (nessuna chat persistente riusata) - la
# continuita' stilistica viene dal ricaricare l'immagine della slide precedente come
# allegato, non da un chat URL. ARENA_CHAT_URL esiste in config.py solo per
# read_arena_chat.py (studio one-shot di una chat passata) - non serve per generare.
# Non duplicato qui: non necessario per il flusso di generazione Preventa.

# Allegati di contesto per la slide 1 (stile di riferimento) - dedicati a Preventa,
# SEPARATI da quelli Agency per non mischiare i due stili visivi. Vuoto al primo
# run: senza reference lo stile viene dal prompt testuale (colori/regole in
# REGOLE.md) - la slide 1 generata diventa poi reference per i run successivi.
ALLEGATI_DIR = os.path.join(PROJECT_DIR, "allegati di contesto (slide)")

LOCAL_DOWNLOAD_DIR = os.path.join(PROJECT_DIR, "output_preventa")

DRIVE_ROOT_FOLDER = "Digital Empire"
DRIVE_IG_FOLDER = "IG page"
DRIVE_PREVENTA_FOLDER = "Preventa"
DRIVE_CAROUSELLI_FOLDER = "caroselli"
