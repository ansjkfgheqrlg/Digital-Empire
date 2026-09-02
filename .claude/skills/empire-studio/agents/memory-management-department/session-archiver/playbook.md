# session-archiver - Playbook

## Flusso operativo
1. Creare un SES per ogni run con il log significativo.
2. Mantenere il layer short-term (stato conversazionale della run).
3. Collegare la sessione ai CP/decisioni della run.
4. Archiviare in modo che la run sia ricostruibile.

## Esempi
- Happy: input valido -> session-archiver produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
