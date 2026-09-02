# conductor - Playbook

## Flusso operativo
1. Stage 0: ricevi input, bootstrap memory della run, chiedi il Strategy Manifest.
2. Stage 1: instrada al reparto di ricerca (ingestion).
3. Stage 2-3: Processing&Vision estrae frame e il video-watcher guarda.
4. Stage 4: knowledge-extractor produce gli atomi (con trace).
5. Stage 5: Verification controlla (frame reali? descrizioni vere? trace?).
6. Stage 6-7: Forge&Wiki forgia via content-forge e scrive nella wiki.
7. Stage 8: update-proposer genera proposte per i workflow esistenti.
8. Stage 9: Memory chiude la run; tu consegni il report all'utente.

## Esempi
- Happy: /empire <video design 2h> --dept=youtube --focus=design -> wiki con guida visiva + proposta update.
- Canale: /empire <canale marketing> --dept=youtube --focus=marketing -> screening + batch + playbook wiki.
- Repo: /empire ./mio-workflow --dept=projects -> deep study senza modifiche + note wiki.
- Edge: input ambiguo -> chiede chiarimento prima di procedere.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
