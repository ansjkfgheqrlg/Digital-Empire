# CENSIMENTO 04 — I MOTORI REALI (tutto cio' che gira fuori da `company/`)

> **Stato:** IN COSTRUZIONE (blocco 1/4 — Outreach chiuso).
> **Metodo:** ogni riga viene da un file aperto o da un comando lanciato. Nessuna deduzione dal nome della cartella.
> **Esclusi dai conteggi:** `node_modules/`, `.git/`, `__pycache__/`, `venv/`, `.venv/`, `.next/`.
> **Nessuno script e' stato eseguito.** Solo lettura e ispezione (nessun invio, nessuna spesa, nessun account toccato).
> **Soglia VIVO:** ha prodotto un output datato negli ultimi 60 giorni (cioe' dal 2026-07-08 in poi).

---

## 1. FAMIGLIA OUTREACH — `Outreach/`

Radice: `c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach`
Totale famiglia: **7.022 file**, **312 file .py**, **101.713 righe di Python**, ultima modifica 2026-08-31.

### 1.1 preventa-maps-scraper (Outreach Preventa concessionari)
- **Percorso:** `Outreach/preventa-maps-scraper/`
- **A cosa serve:** scraping concessionari da Google Maps, qualifica import-focus, invio WhatsApp reale ai numeri trovati. Da `outreach_giornaliero.py` e dai log: eligibili -> bibbia -> invio -> esito per singolo numero.
- **Dimensione:** 27 file .py, ultima modifica 2026-08-31.
- **Punto d'ingresso:** `outreach_giornaliero.py` (piu' `scraper.py`, `contact_leads.py`, `invia_email.py`); skill `/avvia-outreach-preventa`.
- **GIRA ANCORA? VIVO.** Prova: `Outreach/preventa-maps-scraper/logs/outreach_2026-08-22.log` registra invii WhatsApp reali il 2026-08-22 ("Trailer Import: inviato", "Importcars.it | Maxet: inviato"). Serie di log continua dal 2026-08-05 al 2026-08-22.
- **Dipendenze esterne:** profilo Chromium persistente `Outreach/WhatsApp Automation/whatsapp-profile/` (ultima scrittura 2026-08-22), `requirements.txt` presente, CRM Areus.
- **Chi lo possiede:** `01-AGENCY / A2-Acquisizione` — censito in `company/REGISTRO-IMPRESA.md` §3 come **preventa-maps-scraper**. NON orfano.
- **Come si avvolge:** manca un `--json` che stampi l'esito della run (eligibili/inviati/falliti) su stdout: oggi l'esito e' solo dentro il file di log.

### 1.2 Outreach Workflow (motore email)
- **Percorso:** `Outreach/Outreach Workflow/`
- **A cosa serve:** pipeline email completa (scraping lead -> qualifier -> writer -> gate "Bibbia" -> invio Gmail). Da `SISTEMA_OUTREACH_COMPLETO.md`: 300+ email/giorno, poi ridotte a 25-30/giorno per deliverability.
- **Dimensione:** 238 file .py; ultima modifica del codice 2026-08-31.
- **Punto d'ingresso:** `run.py` / `agents/orchestrator.py`; batch `2_AVVIA.bat`; skill `/avvia-email`.
- **GIRA ANCORA? DORMIENTE.** Il codice e' stato toccato di recente, ma l'ultimo output di produzione e' `Outreach Workflow/output/2026-06-03_invio_log.csv` — **95 giorni fa**. Nessun log di invio dopo il 3 giugno 2026.
- **Dipendenze esterne:** credenziali Gmail, `leads.db` (SQLite, 1,5 MB, fermo al 2026-06-03), `requirements.txt` presente.
- **Chi lo possiede:** `01-AGENCY / A2-Acquisizione` — **Outreach Runtime** in `company/REGISTRO-IMPRESA.md` §3. NON orfano.
- **Come si avvolge:** esiste gia' la skill `/avvia-email`; serve solo un codice di uscita e un riepilogo macchina-leggibile a fine run.

### 1.3 LinkedIn Automation
- **Percorso:** `Outreach/LinkedIn Automation/`
- **A cosa serve:** warming a commenti, richieste di connessione con nota, messaggi e follow-up su LinkedIn (`01_scrape_leads.py` -> `05_send_followups.py`).
- **Dimensione:** 30 file .py, ultima modifica 2026-08-23.
- **Punto d'ingresso:** i cinque script numerati `01_..05_`, orchestrati da `Outreach/run_parallel.py`; skill `/avvia-linkedin`.
- **GIRA ANCORA? ROTTO.** Guasto esatto, da `LinkedIn Automation/comments_log.txt`, ultima riga del 2026-08-12 10:08:51: `[ERRORE] Sessione LinkedIn scaduta. Esegui: python refresh_session.py`. Lo stesso errore compare gia' il 2026-08-07. In piu' `run_today_log.txt` registra un `PermissionError: [Errno 13]` sul proprio file di log.
- **Dipendenze esterne:** `linkedin_session.json` — **scaduto** (file fermo al 2026-05-18).
- **Chi lo possiede:** `01-AGENCY / A2-Acquisizione` (dentro Outreach Runtime). NON orfano.
- **Come si avvolge:** serve che `refresh_session.py` sia richiamabile e che l'uscita dichiari "sessione scaduta" invece di morire nel log.

### 1.4 Instagram Automation
- **Percorso:** `Outreach/Instagram Automation/`
- **A cosa serve:** scout hashtag -> qualifica profili -> DM personalizzati (Barnum/Rainbow) -> F1/F2 -> lettura risposte.
- **Dimensione:** 10 file .py, ultima modifica 2026-07-20.
- **Punto d'ingresso:** `run_today.py` (DM Orchestrator), `_avvia_ig.bat`; skill `/avvia-ig`.
- **GIRA ANCORA? ROTTO.** Guasto esatto, da `Instagram Automation/run_today_log.txt` del 2026-07-19: ogni profilo fallisce con `Page.goto: Target page, context or browser has been closed` — il browser Playwright si chiude a meta' run. Decine di screenshot `debug_err_*.png` e `debug_no_btn_*.png` a testimonianza.
- **Dipendenze esterne:** `instagram_session.json` fermo al 2026-06-04, Playwright/Chromium.
- **Chi lo possiede:** `01-AGENCY / A2-Acquisizione` (dentro Outreach Runtime). NON orfano.
- **Come si avvolge:** stabilizzare il contesto browser e restituire un contatore (candidati/qualificati/DM inviati) a fine run.

### 1.5 WhatsApp Automation
- **Percorso:** `Outreach/WhatsApp Automation/`
- **A cosa serve:** invio reale su WhatsApp Web tramite profilo Chromium persistente; e' il braccio esecutivo di preventa-maps-scraper.
- **Dimensione:** 2 file .py + profilo browser completo; ultima scrittura del profilo 2026-08-22.
- **Punto d'ingresso:** invocato da `preventa-maps-scraper/outreach_giornaliero.py`, non ha un lancio proprio dichiarato.
- **GIRA ANCORA? VIVO** (2026-08-22, invii riusciti registrati).
- **Dipendenze esterne:** sessione WhatsApp Web dentro `whatsapp-profile/` — vive finche' non viene sloggata.
- **Chi lo possiede:** `01-AGENCY / A2-Acquisizione`. NON orfano (parte del pacchetto Preventa).
- **Come si avvolge:** gia' avvolto: e' una libreria chiamata dal giornaliero.

### 1.6 Orchestratore parallelo
- **Percorso:** `Outreach/run_parallel.py` (+ `run_all.bat`, `run_ig_email.py`, `run_linkedin_only.py`, `rerun_partial.py`)
- **A cosa serve:** dall'intestazione del file, avvia tre catene indipendenti in parallelo (LinkedIn commenti/connessioni/follow-up, Email genera+invia, Instagram DM+risposte) con log separati.
- **Punto d'ingresso:** `python run_parallel.py`, oppure doppio clic su `run_all.bat`; skill `/avvia-parallel`.
- **GIRA ANCORA? ROTTO in due catene su tre** (LinkedIn sessione scaduta, Instagram browser che si chiude); la catena email e' dormiente.
- **Chi lo possiede:** `01-AGENCY / A2-Acquisizione`. NON orfano.

### 1.7 Satelliti Outreach
- `Outreach/preventa-outreach-pack/` — script freddo APSOC concessionari, 0 file .py (materiale testuale), fermo al 2026-07-29. Censito in REGISTRO §3.
- `Outreach/outreach-dashboard-premium/` — dashboard web, 0 .py, ferma al 2026-06-05; lanciata da `AVVIA-DASHBOARD.bat`/`start-dashboard.bat`.
- `Outreach/agents/`, `Outreach/knowledge/`, `Outreach/forge-run-2026-07-30T-outreach-bible/` — definizioni agenti e Bibbia dei Messaggi, ultima modifica 2026-08-03/23.
- `Outreach/Formazione/` — materiale, fermo al 2026-06-05.

---

*(sezioni 2-N e sintesi A/B/C/D in costruzione)*
