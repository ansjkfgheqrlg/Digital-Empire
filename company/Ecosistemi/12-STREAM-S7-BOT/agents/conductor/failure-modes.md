# CHIEF FORGE - FAILURE MODES

| Failure Mode | Sintomo | Prevenzione | Rilevamento | Recupero |
|---|---|---|---|---|
| FM-CF-001: Context Stuffing | Rallentamento risposta sciame | Usare HandoffPacket con puntatori di memoria | Log > 500ms | Svuotamento buffer conversational |
| FM-CF-002: Unaligned Trade | Trade inviato senza OK del Risk | Hard check programmatico in `swarm_orchestrator.py` | Exception nel Risk Manager | Attivazione automatica Kill-Switch |
