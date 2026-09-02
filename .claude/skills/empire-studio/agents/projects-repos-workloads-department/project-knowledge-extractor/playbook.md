# project-knowledge-extractor - Playbook

## Flusso operativo
1. Leggere deep-analysis.md / repo-analysis.md.
2. Estrarre atomi (pattern, decisione, principio, anti-pattern) uno per concetto.
3. Assegnare a ogni atomo la trace a file:riga/sezione del progetto.
4. Marcare con + le inferenze (giudizi non esplicitamente scritti nella fonte).

## Esempi
- Happy: input valido -> project-knowledge-extractor produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
