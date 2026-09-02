# transcript-processor - Playbook

## Flusso operativo
1. Parsare i file .vtt/.srt scaricati da yt_ingest.
2. Rimuovere ridondanze, tag, righe duplicate; ricostruire frasi leggibili.
3. Allineare i segmenti di testo ai timestamp dei frame (per il video-watcher).
4. Segnalare le parti dove il transcript e' assente/povero (servira' la visione).

## Esempi
- Happy: input valido -> transcript-processor produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
