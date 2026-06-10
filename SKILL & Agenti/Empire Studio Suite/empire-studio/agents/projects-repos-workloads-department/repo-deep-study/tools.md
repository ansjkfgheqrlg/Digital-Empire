# repo-deep-study - Tools

Strumenti CLI/script che questo agente usa. Solo CLI, no API, no paid (la visione, dove serve, la fornisce Claude leggendo i frame).

## Strumenti che usa
1. **scan_repo.py** - scanner struttura repo (read-only)
   ```
   python skills/tier2-functional/repo-study-skill/scripts/scan_repo.py --path <path> --run <run-id>
   ```

## Schema handoff (I/O)
Lo scambio con gli altri agenti del reparto avviene via file nella run e via handoff strutturato:
```json
{ "in": {"run_id": "...", "from": "<lead>"},
  "out": {"artifacts": ["..."], "summary_for_lead": "...", "trace": "..."} }
```

## Memory hook (P10)
Dopo l'azione principale registra un checkpoint e lo stato pertinente:
```
python scripts/memory_manager.py --checkpoint "<azione> completata" --phase <n> --trace "<run/fonte>"
```
Vedi `memory.md` per il protocollo completo di questo agente.
