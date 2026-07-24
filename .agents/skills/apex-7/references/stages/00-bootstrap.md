# Stage 0: Bootstrap

## Obiettivo
Inizializzare la sessione APEX-7 e preparare il sistema all'esecuzione.

## Agente Responsabile
**ORCHESTRATOR** (nessun subagente spawnato)

## Input
- Goal utente (testo libero)

## Processo

1. Generare `session_id = "sess-{uuid}"`
2. Inizializzare Working Memory con:
   - `session_id`
   - `started_at` (ISO-8601)
   - `user_goal` (testuale)
   - `current_level: 1`
   - `current_cycle: 0`
   - `agent_states: tutti IDLE`
3. Eseguire `Memory.RECALL` per contesto passato rilevante
4. Emettere evento `task.created`
5. Mostrare banner APEX-7 all'utente

## Output
- `trace.jsonl`: prima entry con session_id e timestamp
- `state.json`: stato iniziale del sistema
- Banner visibile all'utente

## Criteri di Completamento
- [x] Session ID generato
- [x] Working Memory inizializzata
- [x] Memory.RECALL eseguita
- [x] Banner mostrato
- [x] Evento `task.created` emesso

## Next Stage
→ Stage 1: Planning
