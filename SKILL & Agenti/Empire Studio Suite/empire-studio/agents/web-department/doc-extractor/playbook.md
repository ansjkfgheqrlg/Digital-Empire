# doc-extractor - Playbook

## Flusso operativo
1. Estrarre il main content (no nav/footer/ads) dalle pagine raccolte.
2. Preservare code block, tabelle, heading (struttura semantica).
3. Allegare la trace all'URL (e allo screenshot se la sezione e' visiva).
4. Produrre materiale testuale pulito per knowledge-extractor.

## Esempi
- Happy: input valido -> doc-extractor produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
