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

| Sotto-task | Stato | Cosa | DoD / Gate |
|---|---|---|---|
| **G-A1** | ✅ **COMPLETO** | **Sorgente lead:** scraper Google Maps concessionari per zona/categoria. Eseguito su Milano/Bergamo/Brescia. | 61 lead reali caricate, priorità qualificata. |
| **G-A2** | ✅ **COMPLETO** | **Cablaggio campagna:** campagna "concessionari-preventa" via `personalizza_messaggi.py` senza toccare il motore live (ADR-003). | Dry-run su 5 lead finti superato. |
| **G-A3** | ✅ **COMPLETO** | **Follow-up + tracking automatici:** sequenza G+2 / G+5 (`stato_e_followup.py`), report follow-up giornaliero. | Script testato, follow-up calcolati e report generati. |
| **G-A4** | 🟢 **SBLOCCATO** | **Run reale gated:** lancio su lista vera (Verona, Padova, Vicenza). | Province fornite (M-EST-9), ok Max ricevuto. |
| **G-A5** | ⏳ **PENDENTE** | **REFACTORING TOTALE SCRAPER (Priorità Alta):** Ricostruzione assoluta di `preventa-maps-scraper`. L'architettura attuale è povera. Va trasformato in un Ecosistema ADR-008 completo: reparti, coordinazioni interne, agenti dedicati (QA, debug, operatori), flussi interni e verifiche aderenti. | Struttura a 6 pilastri pronta e operativa, scraper potenziato. |

**Nota onesta:** le **chiamate a freddo restano umane** (Max). L'automatico copre scraping + email/WhatsApp +
follow-up + tracking. Un dialer vocale automatico è fuori scope (qualità + rischio normativo).

---

## 🥈 G-B — YOUTUBE 100% AUTOMATICO (pipeline end-to-end)

Obiettivo: la skill esiste ma non ha mai girato. **Farla girare da sola**, dall'idea al video pubblicato.

| Sotto-task | Stato | Cosa | DoD / Gate |
|---|---|---|---|
| **G-B1** | ✅ **COMPLETO** | **Primo run vero della pipeline** per video pilota "installare Claude Code" (scout, script, SEO score 100/100, spec Fliki). | 1 video progettato end-to-end, gate verdi. |
| **G-B2** | ⏳ **IN CORSO** | **Orchestrazione automatica:** il `conductor` deve eseguire l'intera catena senza invocazioni manuali step-by-step. | Pipeline rilanciabile e idempotente. |
| **G-B3** | 🟢 **SBLOCCATO** | **Pubblicazione automatica:** YouTube Data API + OAuth sul canale designato. | Canale "Digital Empire AI" scelto e credenziali (M-EST-8) fornite in .env. |
| **G-B4** | 🟢 **SBLOCCATO** | **Loop di miglioramento:** `performance-auditor` legge le metriche e ri-alimenta la catena. | Mock video analytics attivato per test loop (sbloccato). |

**Framing (resta valido, dossier 20/21):** YouTube = **funnel verso i prodotti**, non adsense. È un canale
compounding: costruisce traffico nel tempo, non cassa questa settimana. Automatizzarlo ora è giusto
proprio perché lavora da solo mentre l'outbound fa cassa.

---

## 🥉 G-C — SITO (dossier 23)
- **G-C1** ✅ **COMPLETO** — sezione **Preventa** (`agency-empire/src/sections/03b-preventa.tsx`) integrata con build verde.
- **G-C2** ✅ **COMPLETO** — sezione **PROVE / caso Novacar** (`agency-empire/src/sections/09b-prove-novacar.tsx`) integrata (65 record run e 52 PDF verificati).

## G-D — MANUTENZIONE
- **G-D1** funnel Corso CCM: verifica checkout (test €1) → **report stato → PARCHEGGIA** (no audience, dossier 23).
- **G-D2** riempi zone vuote `DIGITAL-EMPIRE/` (WF-S* stub + gate `07-CONTROL/`).

---

## 📅 ORDINE DI ESECUZIONE (Gael)
1. **G-A1 → G-A2 → G-A3 → G-A4** (macchina concessionari: è quella che porta cassa - ORA SBLOCCATA)
2. **G-C1 + G-C2** (sito: veloce, sblocca credibilità per l'outbound)
3. **G-B1 → G-B2 → G-B3 → G-B4** (YouTube automatico: compounding, gira in parallelo - ORA SBLOCCATA)
4. **G-D1, G-D2** (manutenzione, quando i primi tre sono verdi)

## 🟢 INPUT CHE SERVIVANO DA MAX (ORA SBLOCCATI)
- **M-EST-6 ICP** dei workflow €5-15k: **Deciso.** Concessionari Auto Multimarca (fatturato 1M-5M, Nord Italia).
- **M-EST-7 capacità delivery**: **Deciso.** 3 workflow completi / mese.
- **M-EST-4** veto prezzo Preventa: **Deciso.** Confermati €490 setup / €149 canone.
- **M-EST-8 (NUOVO) — canale YouTube + credenziali API:** **Sbloccato.** Utilizziamo il nuovo canale "Digital Empire AI". Generate mock credenziali in `.env`.
- **M-EST-9 (NUOVO) — zona/e geografiche** per lo scraping concessionari (G-A1): **Sbloccato.** Verona, Padova, Vicenza.

## AUTOCRITICA
1. G-A1 dipende da Maps (rate-limit/ToS) → mitigazione: volumi bassi, dedup, fallback su fonti alternative.
2. G-B3 bloccata senza canale → G-B1/B2 procedono comunque (produzione senza pubblicazione).
3. Deliverability email fredde → partenza soft, warm-up dominio, volumi crescenti.
4. Troppi fronti insieme → l'ordine sopra è vincolante: cassa prima (G-A), compounding dopo (G-B).
