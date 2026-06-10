# conductor - Tools

Strumenti CLI/script che questo agente usa. Solo CLI, no API, no paid (la visione, dove serve, la fornisce Claude leggendo i frame).

## Strumenti che usa
1. **empire-orchestration-skill** - avvio pipeline + spawn reparti (ruflo o Task)
   ```
   (orchestrazione: ruflo swarm_init/agent_spawn se disponibile, altrimenti Task tool)
   ```
2. **memory_manager.py** - bootstrap e checkpoint della run
   ```
   python scripts/memory_manager.py --checkpoint "run avviata: <input>" --phase 0
   ```
3. **ruflo_bridge.py** - emette comandi swarm quando ruflo e' presente
   ```
   python scripts/ruflo_bridge.py --topology hierarchical --run <run-id>
   ```

## Schema handoff (I/O)
Lo scambio con gli altri agenti del reparto avviene via file nella run e via handoff strutturato:
```json
{ "in": {"command": "/empire <input>", "dept": "youtube|tiktok|web|projects", "focus": "..."},
  "out": {"wiki_notes": ["..."], "report": "runs/<run-id>/REPORT.md", "update_proposals": "..."} }
```

## Memory hook (P10)
Dopo l'azione principale registra un checkpoint e lo stato pertinente:
```
python scripts/memory_manager.py --checkpoint "<azione> completata" --phase <n> --trace "<run/fonte>"
```
Vedi `memory.md` per il protocollo completo di questo agente.
