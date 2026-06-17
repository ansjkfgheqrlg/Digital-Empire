---
Type: CONCEPT
Status: Active
Tags: #cmo #scripts #automation #gate #pattern
Created: 2026-06-17
Last updated: 2026-06-17
---

# SCRIPTS — CMO (Chief Marketing Officer)

> Script operativi del team CMO. Supportano i workflow e le skill nella fase di esecuzione.
> Stato build: da implementare nella fase di build successiva (script → FORGE o CTO/Platform).
> Nessuno script va in produzione senza dry-run documentato (Mandato Art.4.3, pattern #3).

---

## Script 1 — `apsoc-scorer.py`

**Scopo:** Calcola il punteggio APSOC di un testo con output JSON strutturato.
Implementa il kernel della skill `empire-brand-gate` (parte deterministica).

**Input:** `{ "testo": "...", "formato": "cold_email|sales_page|...", "brand_kit": "DE", "icp": "..." }`
**Output:** `{ "score": 82, "sezioni": {"A": 13, "P": 18, "S": 18, "O": 14, "C": 19}, "penalita": 0, "flag_cpb": [] }`

**Logica:** regex + heuristic su pattern APSOC (Barnum, agitazione, social proof, obiezione, CTA micro-commitment).
La parte di giudizio "AI-slop" rimane LLM; la parte di scoring è deterministica.

**Dry-run:** sì — produce il report senza bloccare nulla. Il blocco è implementato nello skill `empire-brand-gate`.
**Status:** da implementare.

---

## Script 2 — `campaign-brief-generator.py`

**Scopo:** Genera un brief campagna strutturato (JSON + markdown) da un obiettivo di business
e un ICP, chiamando `icp-pattern-library` per arricchire con pattern storici.

**Input:** `{ "obiettivo": "lead", "icp_id": "ICP-PMI-MANI-001", "canali": [...], "deadline": "YYYY-MM-DD" }`
**Output:** brief campagna completo per `cmo-marketing-liaison` e `cmo-content-liaison`.

**Dipendenze:** `icp-pattern-library` (skill 3), AgentDB namespace `board/cmo/icp-patterns/`.
**Dry-run:** sì — genera il brief senza trasmettere a liaison. Conductor lo valida prima del handoff.
**Status:** da implementare.

---

## Script 3 — `brand-gate-log-aggregator.py`

**Scopo:** Aggrega i log di `board/cmo/brand-gate-log/` e produce statistiche per il report KPI:
first-pass rate, score medio, sezioni più fallite, trend nel tempo.

**Input:** range temporale + opzionale filtro per formato o campagna.
**Output:** `aggregate-stats.json` + report markdown per il conductor.

**Frequenza:** su richiesta (per report periodici) o su trigger di nuove entries nel log.
**Dry-run:** non applicabile (read-only).
**Status:** da implementare.

---

## Script 4 — `icp-pattern-refresh.py`

**Scopo:** Segnala i pattern in `board/cmo/icp-patterns/` non aggiornati da >90 giorni
e li marca con flag `validato_recentemente: false`. Supporta la pulizia temporale di `cmo-memoria`.

**Input:** namespace AgentDB `board/cmo/icp-patterns/`
**Output:** lista pattern aggiornati + log operazione.
**Frequenza:** schedulato ogni 90 giorni.
**Dry-run:** sì (in modalità `--dry-run` non scrive i flag, produce solo la lista di pattern da aggiornare).
**Status:** da implementare.

---

## Note di build

1. Tutti gli script devono avere una modalità `--dry-run` che produce l'output senza modificare
   nulla. Solo dopo revisione umana (o trigger esplicito) si eseguono in modalità "live".
2. Nessun secret (API key, token) nei file script: vivono in `.env` locale (Mandato Art.7.1).
3. Output sempre in JSON strutturato + log human-readable in markdown.
4. Ogni script con costo API/crediti: stima il costo in `--dry-run` e lo stampa prima di eseguire.

---

## Connessioni

- [[skills/SKILLS.md]] — le skill che questi script implementano
- [[WF-BRAND-GATE]] · `workflow/WF-BRAND-GATE.md`
- [[cmo-brand-voice-warden]] · `agenti/cmo-brand-voice-warden.md`
- [[cmo-memoria]] · `agenti/cmo-memoria.md`
- [[MANDATO-EMPIRE]] Art.4.3 (dry-run) + Art.7.1 (zero segreti nel repo)
