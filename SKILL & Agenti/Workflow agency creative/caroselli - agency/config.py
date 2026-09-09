# config.py
"""Configurazione del workflow caroselli.

CREDENZIALI FUORI DAL CODICE (B-021, 2026-09-09). Fino a oggi questo file portava
in chiaro la password di Arena e due API key, ed e' tracciato su un repository
PUBBLICO in due copie. Adesso i segreti si leggono dall'ambiente o da un `.env`
accanto a questo file, che `.gitignore` non traccia.

ATTENZIONE, e togliere i valori da qui NON basta: erano leggibili da chiunque
nella storia git pubblica, quindi vanno considerati **bruciati** e vanno
**revocati sul servizio**. Toglierli dal codice chiude la falla per il futuro,
non per il passato.

Come si configura, una volta sola:

    cp .env.example .env      # accanto a questo file
    # poi si incollano nel .env i valori NUOVI, dopo la revoca

Se una variabile manca, il programma si ferma con un messaggio che dice quale:
meglio fermarsi che partire con una credenziale vuota e fallire piu' avanti in
un punto che non c'entra niente.
"""
import os

_QUI = os.path.dirname(os.path.abspath(__file__))


def _carica_env():
    """Legge il .env accanto a questo file, senza dipendenze esterne.

    Non sovrascrive una variabile gia' presente nell'ambiente: chi lancia con
    `GROQ_API_KEY=... python ...` vince sul file, che e' il comportamento che
    ci si aspetta ovunque.
    """
    percorso = os.path.join(_QUI, ".env")
    if not os.path.exists(percorso):
        return
    with open(percorso, encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if not riga or riga.startswith("#") or "=" not in riga:
                continue
            nome, _, valore = riga.partition("=")
            os.environ.setdefault(nome.strip(), valore.strip().strip('"').strip("'"))


_carica_env()


def _obbligatoria(nome):
    """Un segreto mancante e' un errore subito, non un None che gira per il programma."""
    valore = os.environ.get(nome, "")
    if not valore:
        raise RuntimeError(
            ("Manca la credenziale %s." % nome) + \
            "  Copia .env.example in .env accanto a config.py e mettici il valore." + \
            "  I valori vecchi sono bruciati (B-021): erano su un repo pubblico.")
    return valore


# Credenziali API per Team Agenti (Nemotron / Groq / OpenRouter)
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

# Arena.ai configurazione
ARENA_EMAIL = os.environ.get("ARENA_EMAIL", "")
ARENA_PASSWORD = os.environ.get("ARENA_PASSWORD", "")
ARENA_CHAT_URL = os.environ.get(
    "ARENA_CHAT_URL",
    "https://arena.ai/c/019e0848-07c0-7e49-b8a1-b4c2a8af388e")

# Path locale per il download dei file e gli allegati di contesto
LOCAL_DOWNLOAD_DIR = os.path.join(_QUI, "output_caroselli")

# Path della directory del progetto (calcolato automaticamente)
PROJECT_DIR = _QUI
ALLEGATI_DIR = os.path.join(PROJECT_DIR, "allegati di contesto (slide)")

# Path su Google Drive
DRIVE_ROOT_FOLDER = "Digital Empire"
DRIVE_IG_FOLDER = "IG page"
DRIVE_AGENCY_FOLDER = "Agency"
DRIVE_CAROUSELLI_FOLDER = "caroselli"
