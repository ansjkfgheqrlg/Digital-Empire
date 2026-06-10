# department-lead - Tools

Strumenti CLI/script che questo agente usa. Solo CLI, no API, no paid (la visione, dove serve, la fornisce Claude leggendo i frame).

## Strumenti che usa
1. **content-forge (skill /forge)** - forging materiale -> note wiki atomiche
   ```
   /forge runs/<run-id>/forge-input/ --target=wiki --name <slug>
   ```
2. **wiki_writer.py** - deposita le note nella wiki + log
   ```
   python scripts/wiki_writer.py --note runs/<run-id>/wiki-notes/ --topic <t> --source <url>
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
