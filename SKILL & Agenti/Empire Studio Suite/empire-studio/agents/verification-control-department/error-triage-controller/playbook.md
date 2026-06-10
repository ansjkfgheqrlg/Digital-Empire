# error-triage-controller - Playbook

## Flusso operativo
1. Raccogliere gli errori segnalati dai reparti e dalle verifiche.
2. Classificarli (gravita', tipo) e assegnare priorita'.
3. Decidere recovery immediato vs escalation.
4. Coordinare la registrazione con bug-error-tracker.

## Esempi
- Happy: input valido -> error-triage-controller produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
