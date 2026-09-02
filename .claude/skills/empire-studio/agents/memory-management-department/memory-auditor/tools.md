# memory-auditor - Tools

Strumenti CLI/script che questo agente usa. Solo CLI, no API, no paid (la visione, dove serve, la fornisce Claude leggendo i frame).

## Strumenti che usa
1. **memory_manager.py --status/--index** - stato e rebuild INDEX
   ```
   python scripts/memory_manager.py --status
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
