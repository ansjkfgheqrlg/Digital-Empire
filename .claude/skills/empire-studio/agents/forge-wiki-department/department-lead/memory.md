# department-lead - Memory (P10)

L'agente aggiorna l'ecosistema di memoria dopo OGNI azione significativa.

## Cosa registra e dove
- **checkpoints/**: forge+wiki completati per run X
- **updates/**: note scritte e proposte generate
- **workflow-state/**: wiki aggiornata

## Quando aggiorna
Prima di iniziare legge lo stato rilevante della run (per non rifare lavoro gia' fatto); dopo ogni azione significativa crea un checkpoint; a fine handoff aggiorna agent-state con le metriche della propria esecuzione.

## Two-layer (P10)
Short-term: lo stato operativo della run corrente vive nei file di `runs/<run-id>/` (artefatti, manifest). Long-term: i checkpoint, le decisioni e gli stati persistenti vivono in `memory/` e sono indicizzati in `MEMORY-INDEX.md`, riutilizzabili in run future (es. stesso canale/argomento).

## Comando tipico
```
python scripts/memory_manager.py --checkpoint "<azione> completata" --phase <n> --trace "<run/fonte>"
```

## Trace (P12)
risponde a 'tutto va portato in content-forge... inserito nella wiki... la wiki e' connessa a Claude Code'.
