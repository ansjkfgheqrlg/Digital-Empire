"""
Instagram Automation — Configurazione centrale
Digital Empire — PIVOT: vendiamo IMPLEMENTAZIONI AI (workflow installati sui server
del cliente, codice incluso, zero canoni, setup 7 giorni, automazione 100%).
3 prodotti: Outreach Factory, Content Factory, Second Brain.
"""

import os

# ─── CREDENZIALI (da variabile d'ambiente o .env) ─────────────────────────────
_ENV = os.path.join(os.path.dirname(__file__), '..', 'Outreach Workflow', '.env')
if os.path.exists(_ENV):
    with open(_ENV) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith('#') and '=' in _line:
                _k, _v = _line.split('=', 1)
                os.environ.setdefault(_k.strip(), _v.strip())

INSTAGRAM_USERNAME = "digitalempireagency.e"
INSTAGRAM_PASSWORD = "Max.23.09"

# ─── FILE SESSIONE E LEADS ────────────────────────────────────────────────────
SESSION_FILE = "instagram_session.json"
LEADS_FILE   = "instagram_leads.json"

# ─── LIMITI GIORNALIERI (Instagram è più sensibile di LinkedIn) ───────────────
DAILY_DM_LIMIT      = 30   # DM primo contatto al giorno (richiesta utente)
DAILY_FOLLOWUP_LIMIT = 20  # Follow-up al giorno
DAILY_FOLLOW_LIMIT   = 20  # Follow (opzionale, warm-up account)
DELAY_MIN_SECONDS    = 15  # delay minimo tra azioni
DELAY_MAX_SECONDS    = 45  # delay massimo tra azioni

# ─── LINK ─────────────────────────────────────────────────────────────────────
AGENCY_URL = "https://agency-empire-landing.vercel.app"
PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
LAUNCH_OFFER = "sconto early-adopter per i primi clienti che partono questo mese"

# ─── HASHTAG TARGET (agenzie, info business, marketing pro, ecommerce, imprenditori digitali) ───
TARGET_HASHTAGS = [
    # Info product / corsi online
    "corsionline",
    "formatoreonline",
    "infoprodotto",
    "lanciocorso",
    "vendereonline",
    "corsidigitali",
    # Coach / mentor
    "businesscoach",
    "coachingonline",
    "mentoritaliano",
    "coachingbusiness",
    "businessmentor",
    "mindsetcoach",
    # Marketing freelance / pro
    "socialmediaconsulente",
    "socialmediamanager",
    "copywritingita",
    "consulentedigitale",
    "facebookadsita",
    "marketingdigitale",
    "freelancemarketing",
    "adsspecialist",
    "growthhacking",
    "personalbranding",
    # Agenzie
    "agenziamarketing",
    "agenziacomunicazione",
    "webagencyitalia",
    # E-commerce
    "ecommerceitaliano",
    "shopifyitalia",
    "dropshippingitalia",
    "venditaonline",
    # Imprenditori / business online
    "imprenditoreitaliano",
    "imprenditoredigitale",
    "businessonline",
    "startupitaliana",
    "imprenditoridigitali",
    "guadagnareonline",
    "automazionebusiness",
    "intelligenzaartificiale",
]

# ─── KEYWORD RICERCA (alternativa agli hashtag) ───────────────────────────────
TARGET_SEARCHES = [
    "agenzia marketing Italia",
    "business coach Italia",
    "formatore corsi online",
    "social media manager freelance",
    "copywriter freelance Italia",
    "facebook ads specialist Italia",
    "consulente marketing digitale",
    "e-commerce Italia",
    "imprenditore digitale Italia",
]

# ─── PAROLE CHIAVE BIO (filtro — target del pivot AI) ─────────────────────────
TARGET_KEYWORDS = [
    # Info product
    "corso", "corsi", "formatore", "formatrice", "formazione", "infoprodotto",
    "info product", "ebook", "membership", "lancio", "programma online", "insegno",
    "accademia", "academy", "masterclass", "workshop", "webinar",
    # Coach / mentor
    "coach", "coaching", "mentor", "mentoring", "mindset", "mentore",
    # Marketing / digital
    "social media manager", "smm", "copywriter", "copywriting", "facebook ads",
    "meta ads", "google ads", "ads specialist", "media buyer", "marketing",
    "consulente", "consulente digitale", "digital", "strategist", "growth",
    "funnel", "content creator", "ugc", "personal brand", "personal branding",
    # Freelance / professionisti digitali
    "freelance", "freelancer", "libero professionista", "libera professionista",
    # E-commerce
    "ecommerce", "e-commerce", "shopify", "dropshipping", "dropshipper",
    "amazon", "negozio online", "store", "seller", "brand",
    # Business / imprenditore / agency
    "imprenditore", "imprenditrice", "business", "agenzia", "agency", "web agency",
    "venditore", "vendo", "reddito online", "entrepreneur", "digital nomad",
    "automazione", "ai", "intelligenza artificiale",
]
