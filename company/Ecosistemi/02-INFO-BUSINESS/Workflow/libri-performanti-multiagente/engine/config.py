"""
Config centralizzato del motore reale (PIANO-KDP-67, CP0).
Tutti i path sono relativi a questo file (pathlib + __file__) — MAI hardcoded
tipo /home/user/... (bug trovato in ogni variante finta consegnata finora,
vedi CP-20260805-001 §Audit punto 2 e 5).
"""
from pathlib import Path

# --------------------------------------------------------------------------- #
# Path (tutti relativi, portabili)
# --------------------------------------------------------------------------- #
ENGINE_DIR = Path(__file__).resolve().parent
WORKFLOW_DIR = ENGINE_DIR.parent  # .../libri-performanti-multiagente/
SESSIONS_DIR = WORKFLOW_DIR / "sessions"  # gitignored (**/sessions/ in .gitignore root)
LIBRI_DIR = WORKFLOW_DIR / "LIBRI"
LIBRI_PRONTI_DIR = LIBRI_DIR / "libri_pronti"
LIBRI_PUBBLICATI_DIR = LIBRI_DIR / "libri_pubblicati"

AMAZON_SESSION_PATH = SESSIONS_DIR / "amazon_state.json"
LMARENA_SESSION_PATH = SESSIONS_DIR / "lmarena_state.json"

# --------------------------------------------------------------------------- #
# Chrome profile reale (per CP1, dopo che Google ha bloccato il login OAuth
# dentro un browser automatizzato — bloccato sia con Chromium bundlato sia con
# channel="chrome", verificato con 2 tentativi reali il 2026-08-05). Si riusa
# un profilo Chrome GIÀ autenticato invece di fare un login nuovo dentro
# l'automazione. Scelto da Gael: Profile 8 (max.infoproducer@gmail.com).
# Copiato in sessions/ (esclusa cache) — IL PROFILO ORIGINALE NON VIENE MAI
# SCRITTO, solo letto per la copia iniziale.
# --------------------------------------------------------------------------- #
import os as _os

CHROME_USER_DATA_ROOT = Path(_os.environ.get("LOCALAPPDATA", "")) / "Google" / "Chrome" / "User Data"
CHROME_SOURCE_PROFILE_NAME = "Profile 8"  # max.infoproducer@gmail.com — scelto da Gael 2026-08-05
CHROME_PROFILE_COPY_DIR = SESSIONS_DIR / "chrome_profile_copy"
CHROME_COPY_EXCLUDE_DIRS = {
    "Cache", "Cache_Data", "Code Cache", "GPUCache", "DawnCache",
    "DawnGraphiteCache", "GrShaderCache", "ShaderCache", "Service Worker",
    "blob_storage", "Crashpad", "component_crx_cache", "Extensions",
    "Extension State", "File System", "IndexedDB",
}

# --------------------------------------------------------------------------- #
# Brave profile reale (SOLO per LM Arena — il login Google su LM Arena resta
# bloccato anche dentro Chrome/profilo reale, 2026-08-05, secondo tentativo di
# Gael dopo CP1. Soluzione proposta da Gael: usare Brave invece di Chrome per
# quel sito). Stesso principio del profilo Chrome sopra: si riusa un profilo
# Brave GIÀ autenticato, mai un login nuovo dentro l'automazione, originale
# solo letto mai scritto. Scelto da Gael: Profile 9 (etichetta "gd" in Local
# State) — 7 profili Brave trovati senza email visibile, NON presunto, chiesto
# esplicitamente. Amazon resta su Chrome (CP1 già verificato funzionante lì,
# non toccato).
# --------------------------------------------------------------------------- #
BRAVE_EXECUTABLE_PATH = Path(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
BRAVE_USER_DATA_ROOT = Path(_os.environ.get("LOCALAPPDATA", "")) / "BraveSoftware" / "Brave-Browser" / "User Data"
BRAVE_SOURCE_PROFILE_NAME = "Profile 9"  # etichetta "gd" — scelto da Gael 2026-08-05
BRAVE_PROFILE_COPY_DIR = SESSIONS_DIR / "brave_profile_copy"

# --------------------------------------------------------------------------- #
# Profilo PERSISTENTE dedicato per LM Arena (2026-08-07). Motivo, verificato:
# arena.ai mostra una sfida captcha "Security Verification" quando il browser
# si presenta come contesto NUOVO ad ogni avvio (`browser.new_context(
# storage_state=...)`), perche' non riconosce nessuna storia precedente. Il
# workflow gia' in produzione sullo stesso sito
# (YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/arena_thumbnail.py,
# `chrome-profile-arena`) gira headless SENZA MAI incontrare captcha perche'
# usa `launch_persistent_context` su un profilo dedicato che persiste fra i
# run — segnalato da Gael: "in molti altri workflow questo problema non
# c'era". Qui si replica quel pattern invece di reinventarlo.
#
# NB: e' un profilo VUOTO creato da Playwright, non la copia da 381MB del
# profilo Brave reale (quella causava timeout al lancio, vedi CP4 2026-08-06):
# leggero, dedicato, e non tocca nessun profilo personale.
# --------------------------------------------------------------------------- #
LMARENA_PROFILE_DIR = SESSIONS_DIR / "chrome-profile-arena"

for _d in (SESSIONS_DIR, LIBRI_PRONTI_DIR, LIBRI_PUBBLICATI_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------- #
# Amazon
# --------------------------------------------------------------------------- #
AMAZON_BASE_URL = "https://www.amazon.com"
AMAZON_SEARCH_URL_TEMPLATE = AMAZON_BASE_URL + "/s?k={keyword}"

# --------------------------------------------------------------------------- #
# LM Arena — URL confermato reale (lmarena.ai). Il MODELLO specifico (testo e
# immagine) NON è ancora deciso: Gael non ha risposto alla domanda in
# PIANO-KDP-67.md §3 punto 1. Da scegliere al primo login reale in CP1/CP4
# guardando l'interfaccia effettiva — non indovinato qui alla cieca.
# --------------------------------------------------------------------------- #
LMARENA_BASE_URL = "https://lmarena.ai/"
LMARENA_TEXT_MODEL = None  # TODO CP4: confermare guardando la UI reale
LMARENA_IMAGE_MODEL = None  # TODO CP4: confermare guardando la UI reale

# --------------------------------------------------------------------------- #
# KDP formatting (da REPORT_KDP_FORMATTING.md consegnato — regole KDP reali,
# fonti ufficiali kdp.amazon.com citate nello zip analizzato, non inventate)
# --------------------------------------------------------------------------- #
TRIM_SIZE_INCHES = (6.0, 9.0)  # width, height — più comune per Books category
MARGIN_INSIDE_INCHES = 0.5
MARGIN_OUTSIDE_INCHES = 0.5
MARGIN_TOP_INCHES = 0.75
MARGIN_BOTTOM_INCHES = 0.75
BODY_FONT_NAME = "Garamond"
BODY_FONT_SIZE_PT = 11
HEADING_FONT_NAME = "Lucida Grande"  # fallback: verificare disponibilità reale in CP6
HEADING_FONT_SIZE_PT = 24
COVER_BLEED_INCHES = 0.125
COVER_SIZE_WITH_BLEED_INCHES = (
    TRIM_SIZE_INCHES[0] + COVER_BLEED_INCHES,
    TRIM_SIZE_INCHES[1] + 2 * COVER_BLEED_INCHES,
)

WORDS_PER_PAGE_ESTIMATE = 300  # stima conservativa usata per validare il target
TARGET_PAGE_COUNT = 120
TARGET_PAGE_COUNT_TOLERANCE = 5  # accettato: 115-125 pagine
TARGET_WORD_COUNT_MIN = (TARGET_PAGE_COUNT - TARGET_PAGE_COUNT_TOLERANCE) * WORDS_PER_PAGE_ESTIMATE
TARGET_WORD_COUNT_MAX = (TARGET_PAGE_COUNT + TARGET_PAGE_COUNT_TOLERANCE) * WORDS_PER_PAGE_ESTIMATE

# --------------------------------------------------------------------------- #
# Story Validator (CP3) — niche story SI, diario/questionario NO. Liste reali
# usate per un controllo deterministico a keyword, nessuna chiamata LLM.
# --------------------------------------------------------------------------- #
FORBIDDEN_NICHE_KEYWORDS = [
    "diary", "diario", "questionnaire", "questionario", "journal", "guided journal",
    "low-content journal", "tracker", "workbook", "gratitude journal",
    "productivity journal", "self-care journal", "mood tracker",
    "habit tracker", "planner", "organizer", "30-day challenge",
    "prompt journal", "log book", "logbook",
]
# Generi narrativi riconosciuti. La lista va tenuta LARGA: una keyword mancante non
# produce un "non lo so", produce un NO-GO che butta via una nicchia buona — successo
# davvero il 2026-08-12 con "cozy paranormal mystery witch", scartata (punteggio forzato a
# 0) solo perche' "paranormal" e "witch" non erano in elenco, pur essendo uno dei generi
# piu' venduti su KDP. Il compito di questa lista e' distinguere una STORIA da un
# diario/planner, non giudicare se il genere piace.
REQUIRED_NICHE_KEYWORDS = [
    # gia' presenti
    "cozy mystery", "small town romance", "psychological thriller",
    "family secret", "cozy bakery mystery", "small-town rural fiction",
    "memoir", "true crime", "novella", "detective", "suspense",
    # mystery e crime
    "mystery", "whodunit", "murder", "crime", "noir", "investigation",
    "amateur sleuth", "police procedural", "heist",
    # thriller
    "thriller", "domestic suspense", "spy", "espionage", "conspiracy",
    # romance (uno dei generi piu' venduti su KDP)
    "romance", "romantic", "love story", "amish", "regency", "historical romance",
    "second chance", "enemies to lovers", "billionaire", "cowboy",
    # paranormale, fantasy, horror
    "paranormal", "witch", "vampire", "werewolf", "shifter", "ghost", "haunted",
    "fantasy", "magic", "urban fantasy", "horror", "supernatural", "occult",
    # fantascienza e distopia
    "science fiction", "sci-fi", "dystopian", "post-apocalyptic", "space opera",
    "time travel", "cyberpunk",
    # altri narrativi
    "western", "adventure", "saga", "coming of age", "literary fiction",
    "historical fiction", "war", "survival", "young adult",
]

# --------------------------------------------------------------------------- #
# Retry / rate limiting (Playwright verso siti esterni reali)
# --------------------------------------------------------------------------- #
MAX_RETRIES = 3
DEFAULT_TIMEOUT_MS = 30000
