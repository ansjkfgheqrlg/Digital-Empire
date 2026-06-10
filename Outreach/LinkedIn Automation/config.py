"""
LinkedIn Automation — Configurazione centrale
Basato su tecniche di: Oleg Melnikov, Ben AI, Zubair Trabzada (NotebookLM)
"""

# ─── ACCOUNT LINKEDIN ────────────────────────────────────────────────────────
LINKEDIN_EMAIL    = "max.infoproducer@gmail.com"   
LINKEDIN_PASSWORD = "Max.23.09"    

# File di sessione salvata (evita di fare login ogni volta)
SESSION_FILE = "linkedin_session.json"

# ─── LIMITI GIORNALIERI (sicurezza account) ───────────────────────────────────
# Oleg: 20-25 connection requests/day MAX su account nuovo
DAILY_CONNECT_LIMIT  = 20   # connection requests/giorno (richiesta utente, safe)
DAILY_MESSAGE_LIMIT  = 20   # DM post-accettazione/giorno
DAILY_COMMENT_LIMIT  = 30   # commenti warming su post target/giorno
DELAY_MIN_SECONDS    = 8    # delay minimo tra azioni (simula umano)
DELAY_MAX_SECONDS    = 20   # delay massimo tra azioni

# ─── TARGET NICCHIE ──────────────────────────────────────────────────────────
# PIVOT: vendiamo IMPLEMENTAZIONI AI (Outreach Factory, Content Factory, Second Brain)
# Target: agenzie marketing, info business, marketing pros freelance, ecommerce.
# NIENTE professionisti locali (dentisti, avvocati, ristoranti, artigiani, salute).
TARGET_SEARCHES = [
    # Agenzie marketing / digital agency
    'agenzia marketing digitale',
    'digital agency Italia',
    'titolare agenzia marketing',
    'founder agenzia comunicazione',
    # Info product / formatori / corsi online
    'formatore corsi online Italia',
    'info product creator',
    'creator corsi online',
    'vendita corsi online',
    # Coach / business mentor
    'business coach Italia',
    'business mentor',
    'consulente strategico business',
    # Social media manager freelance
    'social media manager freelance',
    'social media strategist',
    # Copywriter freelance
    'copywriter freelance',
    'copywriter a risposta diretta',
    # Ads specialist (facebook / meta / google)
    'facebook ads specialist',
    'meta ads manager freelance',
    'google ads specialist',
    # Growth / funnel
    'growth marketer',
    'funnel specialist',
    'growth hacker Italia',
    # E-commerce / shopify / dropshipping
    'ecommerce manager Italia',
    'shopify store owner',
    'dropshipping ecommerce',
    'brand ecommerce founder',
]

# ─── CLAUDE API per personalizzazione ────────────────────────────────────────
# Usa la stessa API key che usi per Claude Code
# Metti in variabile d'ambiente: set ANTHROPIC_API_KEY=sk-ant-...
import os
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# ─── DATABASE LEAD ────────────────────────────────────────────────────────────
LEADS_FILE     = "linkedin_leads.json"
SENT_FILE      = "linkedin_sent.json"
FOLLOWUP_FILE  = "linkedin_followup.json"

# ─── LINK / OFFERTA ──────────────────────────────────────────────────────────
AGENCY_URL       = "https://agency-empire-landing.vercel.app"
PRESENTATION_URL = "https://presentazione-empire.vercel.app/"
LAUNCH_OFFER     = "sconto early-adopter per i primi clienti che partono questo mese"
