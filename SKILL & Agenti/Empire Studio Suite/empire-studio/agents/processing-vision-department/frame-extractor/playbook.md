# frame-extractor - Playbook

## Flusso operativo
1. Scaricare il video a bassa risoluzione (yt-dlp) per non pesare.
2. Decidere i timestamp dei frame (capitoli da ingest.json o intervalli/%).
3. Estrarre i frame con ffmpeg e scrivere frames/manifest.json (frame->timestamp).
4. Verificare che i PNG non siano vuoti/neri prima di passarli alla visione.

## Esempi
- Happy: input valido -> frame-extractor produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
