# tiktok-ingester - Playbook

## Flusso operativo
1. Eseguire yt_ingest.py su URL TikTok.
2. Recuperare metadata (autore, descrizione, hashtag) utili al focus.
3. Segnalare la durata per la pianificazione frame densi.
4. Gestire i casi senza subs (frequenti su TikTok).

## Esempi
- Happy: input valido -> tiktok-ingester produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
