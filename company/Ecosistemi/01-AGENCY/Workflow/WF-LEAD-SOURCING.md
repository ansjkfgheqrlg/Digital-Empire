> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A1 + sez. 4 (step 1) + sez. 5

# WF-LEAD-SOURCING — Sourcing & Qualifica Lead

> Workflow L3 di A1-RICERCA · Topologia: `star` (fan-out su fonti → qualifier in serie)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1

## Cosa è

Pipeline di approvvigionamento lead: scraping multi-fonte → estrazione contatti → arricchimento →
qualifica vs ICP → caricamento in `leads.db`. Output diretto: lead qualificati pronti per A2.

**Azione F3:** Questo workflow **wrappa** la pipeline esistente in `Outreach/Outreach Workflow/`
(scraper, extractor, qualifier) — il codice è INVARIATO, questa interfaccia aggiunge
handoff contract, log in `agency/leads` e dry-run. Vedere ADR-003.

## Flusso

```
[T-scraper] fan-out star su fonti:
  Maps → maps_browser_scraper.py
  Apify → apify_scraper.py
  Outscraper → outscraper_scraper.py
  Google → google_scraper.py
          ↓ raw batch
[T-extractor] extractor.py → contatti normalizzati (email, nome, settore, sito)
          ↓ contatti normalizzati
[T-qualifier] qualifier.py vs ICP corrente (regola 03_qualifica_lead.md)
          ↓ lead con score
GATE: score ≥ soglia → lead in leads.db con tag {nicchia, fonte, score}
      score < soglia → scartato con motivo (→ agency/reasoning)
```

## I/O

| | Dettaglio |
|---|---|
| **Input** | ICP corrente (da T-icp-profiler o da `agency/leads`), config fonti (nicchia target, regole per nicchia es. `01_ricerca_no_sito.md`) |
| **Output** | lead qualificati in `leads.db` con `{email, nome, settore, score, fonte, nicchia, data}`; evento `lead_generated` in `company/metrics/runs.jsonl` |

## Gate di uscita

- Qualifier score ≥ soglia ICP (la soglia è definita nel profilo ICP, non fissa)
- `memory_search` su `agency/leads` per dedup prima di ogni inserimento
- Dry-run disponibile: stima volumi per fonte senza inserimento reale (pattern #3)

## Comportamento su errore

| Evento | Risposta |
|---|---|
| Fonte scraper down / bloccata | retry con backoff esponenziale (3 tentativi), poi switch fonte alternativa, poi alert a 09 OPS |
| % qualifica < baseline 2 cicli | AG-A1-COORD apre HC-AG-IN-01 (ICP da rivedere) o HC-AG-FG-01 (skill mancante) |
| Dati stantii (freschezza KPI fuori soglia) | re-run prioritario sulla nicchia interessata prima del prossimo ciclo outreach |
| leads.db corrotto / inaccessibile | alert a 09 OPS (backup schedulato via HC-AG-OP-01); run sospesa |

## Schedule

Run giornaliera schedulata da 09 OPERATIONS via `HC-AG-OP-01`. Puà anche essere avviata
on-demand da AG-A2-COORD quando il buffer lead scende sotto soglia.

## Connessioni

- [`../Reparti/A1-Ricerca/`](../Reparti/A1-Ricerca/) — reparto owner
- [`./WF-MARKET-INTEL.md`](./WF-MARKET-INTEL.md) — flusso gemello (intelligence di nicchia)
- [`../Funzioni/T-scraper/`](../Funzioni/T-scraper/) · [`T-extractor/`](../Funzioni/T-extractor/) · [`T-qualifier/`](../Funzioni/T-qualifier/)
- `Outreach/Outreach Workflow/` — codice sorgente (INVARIATO, ADR-003)
- [`../../BACKBONE.md`](../BACKBONE.md) · [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
