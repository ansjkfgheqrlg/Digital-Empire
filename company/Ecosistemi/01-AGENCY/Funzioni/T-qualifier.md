> Fonte: PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md sez. 2-A1 + sez. 5 (qualifier.py, regola 03)

# T-QUALIFIER — Qualificatore Lead vs ICP

> Funzione L4 di A1-RICERCA · Worker · Agente: `AG-A1-QUAL-W` (sonnet)
> Fonte vincolante: `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md` §2-A1

## Cosa fa

Applica lo scoring ICP su ogni lead normalizzato da T-EXTRACTOR e decide:
- score ≥ soglia → lead promosso in `leads.db` con tag
- score < soglia → scartato CON motivo (il motivo alimenta `agency/reasoning`)

## Script e knowledge

- `Outreach/Outreach Workflow/qualifier.py` — logica di scoring base (usata-così, ADR-003)
- `Agenti/Agency/outreach/rules/03_qualifica_lead.md` — criteri di qualifica espliciti per nicchia
- ICP corrente da `agency/leads` namespace o da T-ICP-PROFILER

## Criteri di scoring (da `03_qualifica_lead.md`)

I criteri variano per nicchia; esempio per e-commerce:
- Ha sito web funzionante: +20 punti
- Settore target (e-commerce, coaching, servizi B2B): +30 punti
- Dimensione (1-50 dipendenti, non enterprise): +20 punti
- Segnali di crescita (ads attive, prodotti nuovi): +15 punti
- Email aziendale (non gmail/hotmail): +15 punti
- SOGLIA DEFAULT: ≥60/100 → qualificato

## Comportamento

- `memory_search` su `agency/leads` PRIMA di inserire → dedup per email
- Ogni record scartato viene loggato con `{motivo, score, nicchia}` — non si buttano via i dati
- Lead "sotto soglia ma borderline (50-59)" → flag separato per review manuale da AG-A1-COORD
- La soglia NON è fissa: dipende dal profilo ICP della nicchia corrente (aggiornato da T-ICP-PROFILER)

## Output in leads.db

```json
{
  "email": "...",
  "score": 72,
  "status": "qualificato",
  "nicchia": "ecommerce-moda",
  "fonte": "google_maps",
  "data_qualifica": "2026-06-11",
  "tags": ["sito-ok", "ads-attive", "email-aziendale"]
}
```

## Failure

| Evento | Risposta |
|---|---|
| ICP non caricato | T-qualifier si ferma → AG-A1-COORD richiede ICP a T-ICP-PROFILER prima di procedere |
| % qualifica < baseline per 2 cicli | pattern in agency/reasoning + AG-A1-COORD apre HC-AG-IN-01 (ICP da rivedere) |

## Connessioni

- [`./T-extractor.md`](./T-extractor.md) (fornitore) · [`./T-icp-profiler.md`](./T-icp-profiler.md) (fonte ICP)
- [`../Workflow/WF-LEAD-SOURCING.md`](../Workflow/WF-LEAD-SOURCING.md)
- [`../../ECOSISTEMA.md`](../ECOSISTEMA.md)
