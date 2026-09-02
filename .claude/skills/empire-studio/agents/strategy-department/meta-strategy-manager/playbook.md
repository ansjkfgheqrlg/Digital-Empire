# meta-strategy-manager - Playbook

## Flusso operativo
1. Mantenere il STRATEGY-REGISTRY coerente e aggiornato.
2. Versionare le strategie e integrare le proposte dello strategy-improver.
3. Garantire che non ci siano strategie duplicate o contraddittorie.
4. Creare nuove strategie quando emerge un tipo/reparto non coperto.

## Esempi
- Happy: input valido -> meta-strategy-manager produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
