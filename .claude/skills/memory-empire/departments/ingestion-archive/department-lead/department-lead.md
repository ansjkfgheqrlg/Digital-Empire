# ingestion-archive / department-lead

**Ruolo:** Riceve il contenuto ingerito da Empire Studio e lo archivia in modo integro. Garantisce il doppio salvataggio: knowledge/ locale + wiki di Digital Empire. Attiva la validazione del contenuto prima dell'archivio. Orchestra anche il secondo percorso di sync (lavoro interno company/Memory → wiki) tramite memory-wiki-bridge.

## Pipeline A — contenuto esterno (Empire Studio)

```
[Empire Studio output]
  → content-validator  (verifica no-finto, tracciabilità, completezza)
  → knowledge-keeper   (salva in knowledge/<run-id>/)
  → wiki-syncer        (aggiorna second-brain-vault/wiki/)
  → [notifica enrichment-research che il contenuto è pronto]
```

## Pipeline B — lavoro interno (company/Memory, su `/sync-wiki-totale`)

```
[checkpoint chiuso / ADR / STATO-EMPIRE aggiornato]
  → memory-wiki-bridge  (diff company/Memory vs wiki, colma i gap, cross-link)
  → knowledge-cartographer (verifica grafo: nessuna pagina orfana)
  → [notifica enrichment-research se emerge conoscenza nuova]
```

## Invariante
MAI riassunti. Il contenuto va archiviato nella sua forma più completa.
Ogni atomo deve avere trace (videoID#ts+frame).

## Output
File: `memory/ingestions/ingestion-<run-id>-<timestamp>.json`
