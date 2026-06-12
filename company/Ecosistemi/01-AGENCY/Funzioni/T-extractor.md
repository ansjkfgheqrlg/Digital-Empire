> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A1 + sez. 5 (extractor.py)

# T-EXTRACTOR — Estrattore Contatti e Dati

> Funzione L4 di A1-RICERCA · Worker · Agente: `AG-A1-EXTRACT-W` (haiku)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1

## Cosa fa

Normalizza il batch raw di T-SCRAPER in contatti strutturati pronti per T-QUALIFIER.
Estrae email, nome, settore, sito e altri campi rilevanti dal raw eterogeneo delle 4 fonti.

## Script

`Outreach/Outreach Workflow/extractor.py` — usato-così (ADR-003, azione F3).

## Output schema

```json
{
  "email": "contatto@azienda.it",
  "nome_azienda": "Azienda Srl",
  "settore": "ecommerce",
  "sito_web": "https://azienda.it",
  "citta": "Milano",
  "fonte": "google_maps",
  "timestamp_estrazione": "2026-06-11T10:00:00Z",
  "nicchia": "ecommerce-moda",
  "raw_ref": "batch_20260611_001"
}
```

## Comportamento

- Dedup: se lo stesso record appare da più fonti → merge, mantiene tutte le fonti
- Campi obbligatori: `email` e `nome_azienda` — record senza entrambi viene scartato con log
- Normalizzazione settore: mappa le categorie raw ai settori ICP (usa regola `06_ricerca_ai_prospects.md`)
- **NON fa qualifica** — solo normalizzazione strutturale; la qualifica è T-QUALIFIER

## Failure

| Evento | Risposta |
|---|---|
| Record senza email | scartato + log motivo "no_email" in agency/leads |
| Encoding non standard | pulizia caratteri; se irrecuperabile → scartato + log |
| Formato raw non riconosciuto | alert a AG-A1-COORD; batch sospeso per quella fonte |

## Connessioni

- [`./T-scraper.md`](./T-scraper.md) (fornitore raw) · [`./T-qualifier.md`](./T-qualifier.md) (cliente output)
- [`../Workflow/WF-LEAD-SOURCING.md`](../Workflow/WF-LEAD-SOURCING.md)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
