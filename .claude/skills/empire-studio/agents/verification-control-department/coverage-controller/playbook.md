# coverage-controller - Playbook

## Flusso operativo
1. Contare gli atomi vs quelli presenti nelle note forgiate.
2. Verificare che ogni atomo abbia una trace valida (P12).
3. Segnalare gap di coverage sotto soglia.
4. Richiedere ri-forge mirato se la coverage e' bassa.

## Esempi
- Happy: input valido -> coverage-controller produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
