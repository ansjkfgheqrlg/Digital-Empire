# BACKBONE: STREAM S7 BOT

Questo documento definisce l'architettura portante dell'ecosistema STREAM-S7-BOT.

## Infrastruttura Tecnica
- **Esecuzione:** Basato su delegazione Gemini in ambiente isolato. Nessuna deviazione manuale permessa.
- **Dati:** RPC pubblica vs nodo dedicato (latenza monitorata).
- **Controllo Rischio:** Hard cap di capitale inserito in logica. Se il bilancio scende sotto la soglia X, l'esecuzione viene terminata (Circuit Breaker).
