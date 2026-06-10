# repo-deep-study - Playbook

## Flusso operativo
1. Mappare la struttura della repo (cartelle, moduli, entrypoint).
2. Leggere i file chiave (sola lettura) e ricostruire l'architettura.
3. Identificare pattern, dipendenze, decisioni tecniche e qualita'.
4. Tracciare ogni osservazione a file:riga.

## Esempi
- Happy: input valido -> repo-deep-study produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
