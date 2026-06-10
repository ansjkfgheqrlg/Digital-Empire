# knowledge-extractor - Playbook

## Flusso operativo
1. Leggere video-analysis.md (visione) + transcript.clean.md.
2. Estrarre atomi atomici (un concetto/passo per atomo), espandendo non riassumendo.
3. Assegnare a ogni atomo una trace (video-id#ts + frame-NNN.png o sezione testo).
4. Marcare con + gli atomi inferiti (non osservati direttamente).

## Esempi
- Happy: input valido -> knowledge-extractor produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
