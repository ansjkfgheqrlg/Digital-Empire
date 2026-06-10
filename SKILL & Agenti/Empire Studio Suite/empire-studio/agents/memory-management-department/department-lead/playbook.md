# department-lead - Playbook

## Flusso operativo
1. Coordinare gli agenti di memoria (checkpoint, decisioni, bug, sessioni, stati).
2. Garantire l'aggiornamento dopo OGNI azione significativa (P10).
3. Mantenere MEMORY-INDEX.md sempre aggiornato.
4. Far propagare gli aggiornamenti rilevanti (update-propagator).

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
