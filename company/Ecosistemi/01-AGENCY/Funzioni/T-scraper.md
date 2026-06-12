> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A1 + sez. 5 (asset scraper)

# T-SCRAPER — Runner Scraper Multi-Fonte

> Funzione L4 di A1-RICERCA · Worker · Agente: `AG-A1-SCRAPE-W` (haiku)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1 + §5

## Cosa fa

Esegue gli scraper su 4 fonti in parallelo e restituisce il batch raw a T-EXTRACTOR.
Implementa i cap e i retry. Il codice scraper è **usato-così** (ADR-003, azione F3).

## Fonti e script esistenti

| Fonte | Script | Output raw |
|---|---|---|
| Google Maps | `Outreach/Outreach Workflow/maps_browser_scraper.py` | nome azienda, indirizzo, categoria, rating, sito web |
| Apify | `Outreach/Outreach Workflow/apify_scraper.py` | lead da dataset Apify configurato |
| Outscraper | `Outreach/Outreach Workflow/outscraper_scraper.py` | lead con email da Google Maps arricchito |
| Google Search | `Outreach/Outreach Workflow/google_scraper.py` | aziende da query settore/area |

## Comportamento

- **Fan-out**: T-scraper può eseguire le 4 fonti in parallelo (topologia `star` di A1)
- **Dry-run**: con `--dry-run` stima il volume per fonte senza scaricare dati reali (pattern #3)
- **Cap impliciti**: rispetta i rate limit delle API; mai volume anomalo senza dry-run approvato
- **Output**: batch raw in formato standard `{raw_record, fonte, timestamp, nicchia}` → T-EXTRACTOR

## Failure handling

| Evento | Risposta |
|---|---|
| API fonte non raggiungibile | retry 3×(backoff esponenziale), poi skip fonte + log in agency/leads |
| Credenziale scaduta | alert a 09 OPS (HC-AG-OP-01); la fonte viene saltata per quel ciclo |
| Volume anomalo (10× rispetto alla media) | alert e stop: richiede conferma da AG-A1-COORD |

## Connessioni

- [`../Reparti/A1-Ricerca/`](../Reparti/A1-Ricerca/) · [`../Workflow/WF-LEAD-SOURCING.md`](../Workflow/WF-LEAD-SOURCING.md)
- [`./T-extractor.md`](./T-extractor.md) (cliente diretto dell'output)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
