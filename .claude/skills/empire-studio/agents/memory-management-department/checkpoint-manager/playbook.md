# checkpoint-manager - Playbook

## Flusso operativo
1. Creare CP via memory_manager dopo ogni azione significativa.
2. Assicurare che ogni CP abbia fase + trace.
3. Mantenere la numerazione progressiva coerente.
4. Appendere all'INDEX in modo affidabile.

## Esempi
- Happy: input valido -> checkpoint-manager produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
