# decision-codifier - Playbook

## Flusso operativo
1. Riconoscere quando una scelta e' una decisione architetturale.
2. Scrivere un ADR completo (contesto/alternative/razionale/conseguenze).
3. Collegare la decisione ai CP e agli stati rilevanti.
4. Garantire la tracciabilita' della decisione.

## Esempi
- Happy: input valido -> decision-codifier produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
