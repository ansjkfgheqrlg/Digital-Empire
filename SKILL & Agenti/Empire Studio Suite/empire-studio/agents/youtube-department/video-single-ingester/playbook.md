# video-single-ingester - Playbook

## Flusso operativo
1. Eseguire yt_ingest.py per un singolo URL (no download video, solo info+subs).
2. Verificare presenza di capitoli (guida la strategia di frame extraction).
3. Normalizzare il transcript (passa a transcript-processor se necessario).
4. Creare la run pronta e segnalarne durata/capitoli a Processing & Vision.

## Esempi
- Happy: input valido -> video-single-ingester produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
