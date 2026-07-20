# AUDIT ASSET — Pagine & Presidi Digitali (2026-07-20)

> Task: P0.2 — dossier 16 §1 (Piano Estate Revenue)  
> Owner: Gael  
> Fonte: censimento file-system + config + wiki  

---

## 🔍 SINTESI

| # | Pagina / Canale | Tipo | Stato | Prossima azione |
|---|---|---|---|---|
| 1 | **Agency Empire** (landing) | Next.js / Vercel | 🔴 Live ma da rivedere | Ricollegare funnel S2 (Manuale) + riattivare caroselli |
| 2 | **CCM Premium** (ccm-premium) | Next.js / Netlify | 🟡 Mai lanciato | Decidere se riattivare o archiviare |
| 3 | **CCM Sale Page** (ccm-sale-page-empire) | Next.js | 🟡 Potenziale | Popolate con funnel S2 se riattivate |
| 4 | **Mentalità Brutale** (@mentalita.brutale) | IG + caroselli | 🟡 Attivo ma fermo | Riattivare batch caroselli + funnel in bio |
| 5 | **Crea il tuo impero** (Lancio corso) | Landing / contenuto | 🟡 In pausa | Dipende da decisione Max su CCM |
| 6 | **Mentalità Business** (Lancio corso) | Landing / contenuto | 🟡 In pausa | Dipende da decisione Max |
| 7 | **LinkedIn** (@digitalempireagency) | Outreach automation | 🟢 Attivo | Monitorare, migliorare copy |
| 8 | **Email outreach** (300/gg) | Automazione email | 🟢 Attivo | Ottimizzare tasso risposta |

---

## DETTAGLIO PAGINE

### 1 — Agency Empire (landing principale)

**URL live:** `https://agency-empire-landing.vercel.app`  
**Repo:** `Agency page - Copia/` (Next.js 14, React, TypeScript)  
**Ultimo aggiornamento:** 2026-05-06 (stima da file .md)  
**Instagram collegato:** `@digitalempireagency.e`  
**Presentazione:** `https://presentazione-empire.vercel.app/`

**Contenuto:**
- Hero + automazioni (Agency, CRO Funnel, AI Implementation)
- Pricing / Objections (CPB)
- Testimonial / Trust badges
- Newsletter / CTA

**Stato follower/social:** ❓ **NON VERIFICABILE** da qui (richiede accesso account social reali)

**Prossima azione:**
- Ricollegare funnel S2 (Manuale Claude Code) alla landing
- Aggiungere CTA per PreventivoForge / S6

**Note:** La landing è ancora focalizzata su "agenzia marketing AI generica" — il POSITIONING potrebbe essere troppo ampio dato il pivot verso tool/prodotti (PreventivoForge, Manuale, Mentalità Brutale).

---

### 2 — CCM Premium (Corso Claude Mastery — Lancio Corso Skill Beast)

**URL:** non verificato (file Netlify/Next.js in `second-brain-vault/raw/Lancio corso skill beast/Leanding Page CCM/ccm-premium/`)  
**Stack:** Next.js (stesso pattern Agency Page)  
**Contesto:** `second-brain-vault/wiki/00 - Inbox/Lancio corso skill beast.md`  
**Struttura nota:**
- VSL sales page
- QA (accessibility, HTML, mobile, performance)
- Installazione guidata
- Pagine course (platform/next)

**Contenuto:** Corso su Claude Code / skill di prompting  
**Stato:** ❓ Mai pubblicato o pubblicato e fermo? — **Max deve confermare**

**Prossima azione:** Chiedere a Max se questa pagina è ancora strategica o da archiviare.

---

### 3 — CCM Sale Page (empire)

**URL:** non verificato  
**Stack:** Next.js  
**Varianti presenti:**
- `ccm-elite-ultimate`
- `ccm-full-empire`
- `formazione-empire`
- `ccm-sale-page-empire`

**Stato:** ❓ — probabilmente varianti mai pubblicate o test A/B

**Prossima azione:** Inventory delle varianti → decidere quale (se nessuna) tenere per S2/S3.

---

### 4 — Mentalità Brutale (@mentalita.brutale)

**Instagram:** `@mentalita.brutale`  
**Repo caroselli:** `Workfolw crea caroselli à/carousel-factory/brands/mentalita-brutale/`  
**Config brand:** ✅ Completa e aggiornata
- Font: Anton-Regular (hero) + Inter (body)
- Palette: nero `#0A0A0A` + rosso scuro `#8B0000` + argento `#C0C0C0`
- Effetti: grain, glow, vignette
- Logo: presente, bottom-right
- Canvas: 1080×1080

**Assets locali:**
- `Page IG - Mentalità Brutale/LOGO.png`
- `Page IG - Mentalità Brutale/Leanding page/` (screenshot landing page)
- `Page IG - Mentalità Brutale/POST/` (post generati, 8+ foto/caroselli)
- `Page IG - Mentalità Brutale/storie da rifare/` (storie IG)

**Contenuto IG:** Profilo Instagram per audience imprenditori/mindset  
**Automazione caroselli:** ✅ Carousel-factory configurato  
**Automazione IG:** `Outreach/Instagram Automation/` → `run_today.py` (DM + reply)

**Stato IG:** ❓ followers/post — richiede accesso account reale

**Prossime azioni:**
- S3: Riattivare batch caroselli (7 post con funnel in bio)
- S4: Pipeline 100% auto: caroselli → gate QA → scheduler pubblicazione → report
- Bio: `linktr.ee` o landing page con funnel verso Manuale / PreventivoForge

---

### 5 — Crea il tuo impero (Lancio Corso Skill Beast)

**Repo:** `Lancio corso skill beast/Page/Page Crea il tuo impero/`  
**Contenuto:**
- Video presentazione
- Caroselli generati (5+ versioni)
- Screenshot landing page
- Brand/logo Empire

**Stato:** ❓ — probabilmente materiale promozionale per un lancio corso

**Prossima azione:** Max decide se il corso Skill Beast è ancora in pipeline o archiviato.

---

### 6 — Mentalità Business (Lancio Corso Skill Beast)

**Repo:** `Lancio corso skill beast/Page/Mentalità Business/`  
**Contenuto:** Simile a "Crea il tuo impero"  
**Stato:** ❓ — materiale promozionale pausa

---

### 7 — LinkedIn (@digitalempireagency)

**Account:** `@digitalempireagency`  
**Automazione:** `Outreach/LinkedIn Automation/` (script Python + Chrome prompt)  
**Script:** `chrome_prompt_autonomo.md`, `chrome_prompt_v2.md`, `daily_checklist.md`  
**Target:** Imprenditori, agenzie, social media manager, freelance

**Canale:** LinkedIn outreach  
**Stato:** 🟢 Automazione presente — ❓ utilizzo effettivo recente

---

### 8 — Email Outreach (300/gg, $0/giorno)

**Automazione:** `Outreach/Outreach Workflow/` (pipeline completa NVIDIA Nemotron)  
**Stack:**
- Facebook Ad Library (ricerca lead, gratuito)
- BeautifulSoup + lxml (estrazione email)
- NVIDIA Nemotron via OpenRouter (AI copy, $0)
- Gmail SMTP (invio)
- SQLite (deduplicazione)

**Script:**
- `AVVIA-EMAIL-LIVE.bat` — lancio produzione
- 6 agenti in sequenza: scraper → extractor → qualifier → strategist → writer → humanizer → sender

**Target hashtags:** 40+ (corsionline, business coach, social media manager, copywriting, ecommerce, imprenditore digitale, ai)

**Link nelle email:**
- `https://agency-empire-landing.vercel.app` (Agency Empire)
- `https://presentazione-empire.vercel.app/` (Presentazione)

**Stato:** 🟢 Automazione presente — ❓ utilizzo effettivo recente  
**Config:** `Outreach Workflow/.env` (gitignorato, contiene API keys)

---

## 🗂️ ASSET SECOND-BRAIN (per audit second-brain)

| Cartella | Contenuto | Stato |
|---|---|---|
| `second-brain-vault/raw/Lancio corso skill beast/` | Tutte le landing CCM | Da rivedere/ decidere |
| `second-brain-vault/raw/Workfolw crea caroselli à/` | Carousel-factory + 4 brand | Mentalità-Brutale operativo |
| `second-brain-vault/raw/Outreach/` | Email + LinkedIn + IG automation | Email + IG operativi |
| `second-brain-vault/raw/Agency page - Copia/` | Sito agency | Live, da ricollegare a S2 |
| `second-brain-vault/wiki/projects/Lancio corso skill beast.md` | MOC del corso | Obsoleto o attivo? |

---

## 🎯 AZIONI PRIORITARIE (dal board dossier 16)

| Priorità | Azione | Stream | Da chi |
|---|---|---|---|
| 🔴 ALTA | Riattivare caroselli Mentalità Brutale (7 post + funnel in bio) | S3 | Gael |
| 🔴 ALTA | Ricollegare Agency Empire al funnel S2 (Manuale) | S2 | Gael |
| 🟡 MEDIA | Decisione Max: CCM corso — riattivare o archiviare? | S2/S3 | Max |
| 🟡 MEDIA | Pipeline auto S4: caroselli → QA → scheduler → report | S4 | Gael |
| 🟡 MEDIA | LinkedIn outreach — test copy + tasso risposta | S1/S2 | Max/Gael |
| 🟢 BASSA | Inventory CCM varianti (4+ landing page) | tutti | Gael |

---

## ❓ DOMANDE APERTE (da chiedere a Max)

1. CCM Corso Skill Beast è ancora strategico o da archiviare?
2. Agency Empire: il posizionamento "agenzia marketing AI" è ancora corretto o va ripensato (visto il pivot verso tool/prodotti)?
3. Qual è il link in bio di @mentalita.brutale attualmente?
4. LinkedIn outreach: quanto è attivo negli ultimi 30 giorni?
5. Email outreach: la pipeline Nemotron è ancora funzionante?

---

## 📁 File sorgente per questa audit

```
company/Ecosistemi/05-MULTI-BUSINESS/AUDIT-PAGINE-20260720.md  ← questo file
```

**Fonti verificate:**
- `Outreach/Instagram Automation/config.py` — credenziali IG, hashtag target, link
- `Outreach/Outreach Workflow/ARCHITETTURA_COMPLETA.md` — stack email outreach
- `Workfolw crea caroselli à/carousel-factory/brands/mentalita-brutale/config.json` — brand config
- `Agency page - Copia/package.json` — name=digital-empire-website
- `second-brain-vault/wiki/index.md` — panoramica second-brain
- `second-brain-vault/raw/Lancio corso skill beast/` — tutte le landing CCM
- `second-brain-vault/wiki/00 - Inbox/Lancio corso skill beast.md` — MOC corso
