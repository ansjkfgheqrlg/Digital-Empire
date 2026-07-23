# 25 — GAEL TASK BOARD OPERATIVO (autorevole — sostituisce le righe Gael del dossier 24)

> Creato 2026-07-23, Claude (Opus). Ordine Max: "aggiorna veramente tutte le task di Gael, dobbiamo partire
> con outreach automatico concessionari + YouTube che deve andare COMPLETAMENTE in automatico, tutto con
> workflow/automazioni". Path verificati su disco, non a memoria. Regola ADR-003: **wrappa, non riscrivere.**

## ⚡ ASSET GIÀ ESISTENTI (verificati — NON ricostruirli)
- `Outreach/preventa-outreach-pack/` → **gli script APSOC concessionari ci sono già**: `01_SCRIPT_CHIAMATA_FREDDA_APSOC.md`,
  `02_SCRIPT_WHATSAPP_EMAIL_3MSG.md`, `03_ARGOMENTARIO_OBIEZIONI_ESTESO.md`, `04_5_VARIANTI_GANCIO_AB.md`, `05_FOLLOW_UP_G2_G5.md`.
- `Outreach/Outreach Workflow/` → **motore outreach LIVE**: `empire_auto_v3.py`, `agents/`, `1_SETUP.bat`/`2_AVVIA.bat`/`3_TEST_EMAIL.bat`, `emails_*_ready.json`, `ARCHITETTURA_COMPLETA.md`.
- `.claude/skills/youtube-automation-factory/` → **skill YT completa**: `conductor.md` + operatori (niche-scout,
  video-hunter, script-writer, seo-analyst, thumbnail-designer, metadata-optimizer) + controllo (niche-gate,
  seo-gate, qa-audio-video, performance-auditor) + `workflows/`, `scripts/`, `memory/`. **MAI ESEGUITA.**

**Quindi il lavoro NON è costruire: è CABLARE questi pezzi in due macchine che girano da sole.**

---

## 🥇 G-A — OUTREACH CONCESSIONARI 100% AUTOMATICO (Preventa) — priorità assoluta

Obiettivo: una macchina che trova concessionari, li contatta con gli script APSOC già scritti, fa follow-up
e riporta i risultati — **senza intervento umano** (tranne il gate di approvazione iniziale e le chiamate vocali).

| Sotto-task | Cosa | DoD / Gate |
|---|---|---|
| **G-A1** | **Sorgente lead (il pezzo mancante):** scraper Google Maps concessionari per zona/categoria → CSV `nome, indirizzo, telefono, sito, n_recensioni, media, ha_sito`. Colonna `priorita_lead`: ALTA se NO sito o sito scarso. Rate-limiting rispettoso, dedup. Se arriva lo zip Arena (dossier 19 PROMPT 2) → integra quello invece di riscriverlo. | CSV con ≥50 concessionari reali, 0 duplicati |
| **G-A2** | **Cablaggio campagna:** wrappa il motore `Outreach Workflow/` con una campagna "concessionari-preventa" che usa gli script di `preventa-outreach-pack/` (email + WhatsApp 3 msg). **NON modificare `empire_auto_v3.py`**: aggiungi config/campagna a fianco (ADR-003). Personalizzazione per lead (nome attività, città, gancio da `04_5_VARIANTI_GANCIO_AB.md`). | dry-run su **5 lead finti** end-to-end, 0 invii reali |
| **G-A3** | **Follow-up + tracking automatici:** sequenza G+2 / G+5 da `05_FOLLOW_UP_G2_G5.md`, stato per lead (contattato/risposto/interessato/no), report giornaliero. | follow-up parte da solo, report generato |
| **G-A4** | **Run reale gated:** lancio su lista vera SOLO dopo ok Max (ICP + volume giornaliero). Partenza soft (volumi bassi, deliverability). | prima run reale tracciata |

**Nota onesta:** le **chiamate a freddo restano umane** (Max). L'automatico copre scraping + email/WhatsApp +
follow-up + tracking. Un dialer vocale automatico è fuori scope (qualità + rischio normativo).

---

## 🥈 G-B — YOUTUBE 100% AUTOMATICO (pipeline end-to-end)

Obiettivo: la skill esiste ma non ha mai girato. **Farla girare da sola**, dall'idea al video pubblicato.

| Sotto-task | Cosa | DoD / Gate |
|---|---|---|
| **G-B1** | **Primo run vero della pipeline** (`youtube-automation-factory`): `niche-scout` → **niche-gate** → `video-hunter` → `script-writer` → produzione video (Fliki, chiave in `.env` locale) → `thumbnail-designer` → `seo-analyst`+`metadata-optimizer` → **seo-gate** + **qa-audio-video** → pubblicazione → `performance-auditor`. Nicchia: **AI/Claude in italiano** (DEC-EST-004). | **1 video completo end-to-end**, gate verdi |
| **G-B2** | **Orchestrazione automatica:** il `conductor` deve eseguire l'intera catena senza invocazioni manuali step-by-step. Pipeline schedulabile (es. N video/settimana) con stato persistente e ripresa dopo errore. | pipeline rilanciabile, idempotente |
| **G-B3** | **Pubblicazione automatica:** YouTube Data API + OAuth sul canale designato (upload, titolo, descrizione, tag, thumbnail, pianificazione). ⚠️ **Dipendenza bloccante: serve un canale che controlliamo + credenziali API** (vedi input Max sotto). | upload automatico riuscito |
| **G-B4** | **Loop di miglioramento:** `performance-auditor` legge le metriche del pubblicato e ri-alimenta `niche-scout`/`script-writer` (feedback loop già previsto dai workflow WF1-WF5). | 2° ciclo usa i dati del 1° |

**Framing (resta valido, dossier 20/21):** YouTube = **funnel verso i prodotti**, non adsense. È un canale
**compounding**: costruisce traffico nel tempo, non cassa questa settimana. Automatizzarlo ora è giusto
proprio perché lavora da solo mentre l'outbound fa cassa.

---

## 🥉 G-C — SITO (dossier 23)
- **G-C1** sezione **Preventa** separata: `agency-empire/src/sections/03b-preventa.tsx` + import in `page.tsx`
  (tier SaaS verticale concessionari, NON nella grid dei workflow €5-15k). Gate: `npm run build` verde.
- **G-C2** sezione **PROVE / case study Novacar** — è il gap CRO n.1: un ticket €5-15k non si chiude a freddo
  senza prove. Anche una sola prova reale cambia il tasso di chiusura.

## G-D — MANUTENZIONE
- **G-D1** funnel Corso CCM: verifica checkout (test €1) → **report stato → PARCHEGGIA** (no audience, dossier 23).
- **G-D2** riempi zone vuote `DIGITAL-EMPIRE/` (WF-S* stub + gate `07-CONTROL/`).

---

## 📅 ORDINE DI ESECUZIONE (Gael)
1. **G-A1 → G-A2 → G-A3** (macchina concessionari: è quella che porta cassa)
2. **G-C1 + G-C2** (sito: veloce, sblocca credibilità per l'outbound)
3. **G-B1 → G-B2 → G-B3 → G-B4** (YouTube automatico: compounding, gira in parallelo)
4. **G-D1, G-D2** (manutenzione, quando i primi tre sono verdi)

## 🔵 INPUT CHE SERVONO DA MAX (senza questi Gael si ferma)
- **M-EST-6 ICP** dei workflow €5-15k (settore/dimensione/dove) — punta la lista A.
- **M-EST-7 capacità delivery** (quanti workflow consegnabili in estate).
- **M-EST-4** veto prezzo Preventa (€490 setup / €149 canone).
- **M-EST-8 (NUOVO) — canale YouTube + credenziali API:** quale canale usiamo? (`Legami d'amore` ha proprietà
  non chiarita, 471 video, vedi dossier 20 → serve login) oppure ne creiamo uno nuovo per la nicchia AI/Claude?
  **G-B3 è bloccata finché non lo decidi.**
- **M-EST-9 (NUOVO) — zona/e geografiche** per lo scraping concessionari (G-A1): quali province partiamo?

## AUTOCRITICA
1. G-A1 dipende da Maps (rate-limit/ToS) → mitigazione: volumi bassi, dedup, fallback su fonti alternative.
2. G-B3 bloccata senza canale → G-B1/B2 procedono comunque (produzione senza pubblicazione).
3. Deliverability email fredde → partenza soft, warm-up dominio, volumi crescenti.
4. Troppi fronti insieme → l'ordine sopra è vincolante: cassa prima (G-A), compounding dopo (G-B).
