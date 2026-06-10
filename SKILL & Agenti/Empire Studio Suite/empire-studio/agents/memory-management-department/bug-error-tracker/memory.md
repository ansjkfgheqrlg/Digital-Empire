# bug-error-tracker - Memory (P10)

L'agente aggiorna l'ecosistema di memoria dopo OGNI azione significativa.

## Cosa registra e dove
- **bugs/**: i bug
- **errors/**: gli errori
- **workflow-state/**: impatti

## Quando aggiorna
Prima di iniziare legge lo stato rilevante della run (per non rifare lavoro gia' fatto); dopo ogni azione significativa crea un checkpoint; a fine handoff aggiorna agent-state con le metriche della propria esecuzione.

## Two-layer (P10)
Short-term: lo stato operativo della run corrente vive nei file di `runs/<run-id>/` (artefatti, manifest). Long-term: i checkpoint, le decisioni e gli stati persistenti vivono in `memory/` e sono indicizzati in `MEMORY-INDEX.md`, riutilizzabili in run future (es. stesso canale/argomento).

## Comando tipico
```
python scripts/memory_manager.py --checkpoint "<azione> completata" --phase <n> --trace "<run/fonte>"
```

## Trace (P12)
risponde a 'ogni bug, ogni errore, ogni problema deve essere aggiornato'.
