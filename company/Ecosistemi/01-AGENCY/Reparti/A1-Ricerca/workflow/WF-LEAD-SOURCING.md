---
Type: WORKFLOW
Status: Active
Tags: #workflow #ricerca #lead #sourcing #scraping #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# WF-LEAD-SOURCING — Sourcing Lead Multi-Fonte [WRAPPA-ESISTENTE]

> **ID:** WF-A1-001 · **Owner:** `ag-a1-coord` · **Reparto:** A1 Ricerca & Market Intelligence
> **Trigger:** run schedulata da 09-OPERATIONS | richiesta lead da A2-Acquisizione

---

## Scopo

Trasformare una nicchia (con ICP definito) in lead qualificati pronti per l'outreach:
scraping multi-fonte → estrazione strutturata → qualifica vs ICP → gate QA → store in
`leads.db` + `agency/leads`. Wrappa il runtime esistente (`scraper/*.py`, `extractor.py`,
`qualifier.py`) senza riscriverlo (ADR-003 / R1).

---

## Attori

| Step | Agente A1 | Asset / Reparto esterno |
|---|---|---|
| Validazione ICP | `ag-a1-coord` | `ag-a1-icp` (se nicchia nuova) |
| Scraping | `ag-a1-scrape` | `scraper/*.py` (Maps/Apify/Outscraper/Google) |
| Estrazione | `ag-a1-extract` | `extractor.py` |
| Qualifica | `ag-a1-qual` | `qualifier.py` |
| Gate | `ag-a1-qa` | — |
| Store + handoff | `ag-a1-coord` | `leads.db` + A2-Acquisizione |

---

## Flusso passo-passo

```
[TRIGGER]
Run schedulata (09-OPS) | richiesta lead (A2) → AG-A1-COORD
  {nicchia, n_lead_target, deadline}
         │
         ▼
[STEP 1] AG-A1-COORD — validazione ICP (GATE-ICP / R2)
  → la nicchia ha un ICP in agency/a1/icp?
  → NO → assegna AG-A1-ICP (icp-radar) PRIMA di procedere; non si scrappa senza ICP
  → SÌ → riusa l'ICP; valuta se aggiornarlo
         │
         ▼
[STEP 2] AG-A1-SCRAPE — scraping multi-fonte (parallelo)
  → invoca scraper/*.py su Maps · Apify · Outscraper · Google in parallelo
  → log per fonte in agency/a1/sourcing (n_raw, errori, stato)
  → fonte down → retry backoff → switch fonte → alert se persiste
         │
         ▼
[STEP 3] AG-A1-EXTRACT — estrazione strutturata
  → invoca extractor.py sul raw per fonte
  → schede lead (nome, email, telefono, sito, settore) + normalizzazione
  → calcola completezza per scheda + marca candidati dedup
  → scrive schede in agency/leads (stato da_qualificare)
         │
         ▼
[STEP 4] AG-A1-QUAL — qualifica vs ICP
  → invoca qualifier.py con l'ICP corrente; score per scheda
  → triage: qualificato / nurture / scarta CON motivo (R7 → agency/reasoning)
  → pattern di scarto → feedback ad AG-A1-ICP
         │
         ▼
[STEP 5] AG-A1-QA — GATE sourcing (G-SOURCING)
  → completezza dati ≥80%?
  → dedup eseguito (no duplicati in agency/leads)?
  → GDPR-light rispettato (solo dati business pubblici)?
  → PASS → prosegui; FAIL → lead incompleto bloccato con motivo → rework EXTRACT/QUAL
         │
         ▼
[STEP 6] AG-A1-COORD — store + handoff
  → lead qualificati → leads.db + agency/leads (stato qualificato, tag nicchia/fonte)
  → evento lead_generated in metrics
  → handoff ad A2-Acquisizione (lead pronti per outreach)
  → aggiorna agency/a1/sourcing/{run_id}/state.json (stato store_completo)
```

---

## Gate bloccanti

| Gate | Condizione PASS | Owner | Blocca |
|---|---|---|---|
| G-ICP | Profilo ICP con fonti esiste prima dello scraping di nicchia nuova | AG-A1-QA / AG-A1-COORD | Avvio scraping (R2) |
| G-SOURCING | Completezza ≥80%, no duplicati, GDPR-light | AG-A1-QA | Store in leads.db (R3/R5) |

---

## Input / Output del workflow

**Input trigger:**
```json
{
  "nicchia": "ristorazione-roma",
  "n_lead_target": 200,
  "richiedente": "A2 | 09-OPERATIONS",
  "deadline": "2026-06-30"
}
```

**Output finale:**
```json
{
  "run_id": "RUN-001",
  "nicchia": "ristorazione-roma",
  "n_raw": 0,
  "n_estratti": 0,
  "n_qualificati": 0,
  "n_scartati": 0,
  "gate_qa": "PASS",
  "store": "leads.db + agency/leads",
  "handoff": "A2-Acquisizione",
  "stato": "store_completo"
}
```

---

## State

File: `agency/a1/sourcing/{run_id}/state.json`
- Aggiornato ad ogni fonte e ad ogni step.
- Ripartibilità a freddo: una run interrotta riprende dall'ultima fonte completata senza
  riscrappare tutto (test amnesia §6 V2).
- Archiviato dopo `store_completo`; mai eliminato.

---

## Failure & escalation

- Fonte down dopo retry+switch → alert ad AG-A1-COORD → 09-OPERATIONS.
- % qualifica < baseline per 2 cicli → AG-A1-COORD apre revisione ICP (AG-A1-ICP) o segnala a FORGE skill mancante.
- Dedup fallito (duplicati in store) → anomalia AG-A1-QA → AG-DIR.
- Ogni failure distillato in `agency/reasoning`.

---

## Connessioni

- [[ag-a1-coord]] · `agenti/ag-a1-coord.md`
- [[ag-a1-scrape]] · `agenti/ag-a1-scrape.md`
- [[ag-a1-qual]] · `agenti/ag-a1-qual.md`
- [[ag-a1-qa]] · `agenti/ag-a1-qa.md`
- [[scripts/README]] · `scripts/README.md` — runtime wrappato (ADR-003)
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A1`
