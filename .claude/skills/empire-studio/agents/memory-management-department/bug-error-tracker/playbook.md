# bug-error-tracker - Playbook

## Flusso operativo
1. Creare report dettagliati per ogni bug/errore/problema.
2. Collegare il problema a agent-state/workflow-state impattati.
3. Coordinarsi con error-triage-controller per la risoluzione.
4. Tracciare lo stato (aperto/risolto) e la prevenzione futura.

## Esempi
- Happy: input valido -> bug-error-tracker produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
