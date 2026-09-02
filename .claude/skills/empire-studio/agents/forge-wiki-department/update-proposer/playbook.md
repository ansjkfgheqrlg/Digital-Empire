# update-proposer - Playbook

## Flusso operativo
1. Leggere knowledge-state e workflow-state (cosa l'ecosistema gia' fa/sa).
2. Confrontare con i nuovi atomi: cosa migliorerebbe un workflow esistente?
3. Produrre update-proposals.md con proposta + razionale + trace al video/frame.
4. Non modificare nulla: solo proporre (la decisione e' dell'utente).

## Esempi
- Happy: input valido -> update-proposer produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
