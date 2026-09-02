# memory-architect - Playbook

## Flusso operativo
1. Definire/mantenere le 16 categorie e i loro schemi.
2. Garantire le convenzioni di naming Windows-safe.
3. Versionare l'architettura della memoria quando evolve.
4. Documentare il two-layer (short-term run, long-term INDEX).

## Esempi
- Happy: input valido -> memory-architect produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
