# department-lead - Playbook

## Flusso operativo
1. Classificare l'input: URL di video singolo, canale, o playlist.
2. Per i canali, delegare a yt-screening la selezione dei video rilevanti per --focus.
3. Assegnare a yt-channel-ingester / video-single-ingester l'ingestion vera (yt_ingest.py).
4. Consegnare a Processing & Vision le run pronte (ingest.json) con priorita'.
5. Aggiornare workflow-state con l'avanzamento del reparto.

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
