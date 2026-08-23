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

for _d in (SESSIONS_DIR, LIBRI_PRONTI_DIR, LIBRI_PUBBLICATI_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------------- #
# Amazon — l'unico sito che il codice apre ancora (2026-08-15). Serve a MISURARE
# le nicchie con dati veri, non a generare contenuto: nessun modello dietro.
# Le costanti di LM Arena, Brave e Google Docs sono state tolte da qui quando
# l'automazione della scrittura e' stata archiviata in
# `_archivio_automazione_modelli/` — vivono ancora la' dentro, per chi dovesse
# rileggere quel codice.
# --------------------------------------------------------------------------- #
AMAZON_BASE_URL = "https://www.amazon.com"
AMAZON_SEARCH_URL_TEMPLATE = AMAZON_BASE_URL + "/s?k={keyword}"

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

# Misurato su due libri veri impaginati con `kdp_formatter` (6x9in, margini specchio):
#   The Quiet Hours  37.279 parole -> 115 pagine reali = 324 p/pag
#   The Ninth Winter 36.756 parole -> 115 pagine reali = 320 p/pag
# A 300 la stima NON era conservativa: sbagliava per ECCESSO di pagine (~+6%), cioe' nella
# direzione pericolosa. The Ninth Winter e' passato dal controllo parole a 34.897 ("116,3
# pagine") ed e' arrivato al PDF con 111 pagine reali, sotto il minimo. 320 e' il piu' basso
# dei due rapporti misurati: prudente sul minimo parole, senza inventare margine.
# AGGIORNAMENTO 2026-08-20, dopo il terzo libro: il rapporto NON e' costante fra stili.
#   The Quiet Hours           37.168 / 115 = 323 p/pag   (scarto stima 1,2 pagine)
#   The Ninth Winter          36.871 / 116 = 318 p/pag   (scarto stima 0,8 pagine)
#   The Second-Hand Spellbook 38.110 / 115 = 331 p/pag   (scarto stima 4,3 pagine)
# Un libro con molti dialoghi brevi e molte interruzioni di scena impagina diversamente da
# uno di prosa continua. Percio' 320 resta il valore prudente per PIANIFICARE, ma la stima
# non sostituisce il PDF: su The Second-Hand Spellbook diceva 117,3 pagine e le pagine vere
# erano 113, cioe' sotto il minimo. Il PDF va generato almeno una volta PRIMA della consegna
# finale, per tarare il rapporto vero di quel libro.
WORDS_PER_PAGE_ESTIMATE = 320
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
