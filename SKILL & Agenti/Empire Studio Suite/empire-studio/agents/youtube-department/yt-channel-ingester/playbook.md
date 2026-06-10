# yt-channel-ingester - Playbook

## Flusso operativo
1. Eseguire yt_ingest.py in modalita' canale (extract_flat) per elencare i video.
2. Applicare il filtro di screening ricevuto da yt-screening.
3. Per ogni video selezionato, scaricare info.json + auto-subs + thumbnail.
4. Creare una run per video (o una run con videos.json) per il reparto Vision.

## Esempi
- Happy: input valido -> yt-channel-ingester produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
