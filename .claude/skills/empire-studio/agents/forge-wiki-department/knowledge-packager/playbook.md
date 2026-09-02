# knowledge-packager - Playbook

## Flusso operativo
1. Raccogliere i percorsi delle note wiki, l'MKD, le update proposals.
2. Produrre runs/<run-id>/REPORT.md leggibile per l'utente (via cli-printing-press style).
3. Elencare le trace principali (fonte->frame->atomo->nota wiki).
4. Consegnare il report al Conductor per la comunicazione all'utente.

## Esempi
- Happy: input valido -> knowledge-packager produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
