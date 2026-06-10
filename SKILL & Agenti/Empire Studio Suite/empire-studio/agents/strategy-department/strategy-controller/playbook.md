# strategy-controller - Playbook

## Flusso operativo
1. Caricare il Manifest e le sue regole specifiche.
2. Auditare l'output dei reparti contro quelle regole (es. frame per capitolo presenti?).
3. Loggare l'esito in verification-logs.
4. Escalare a improver/coordinator in caso di violazione grave.

## Esempi
- Happy: input valido -> strategy-controller produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
