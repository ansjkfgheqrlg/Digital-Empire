# department-lead - Playbook

## Flusso operativo
1. Classificare l'input: singolo TikTok o profilo/hashtag.
2. Delegare a tiktok-trend-scout l'individuazione dei video rilevanti.
3. Assegnare a tiktok-ingester l'ingestion (yt-dlp supporta TikTok).
4. Istruire Vision a usare frame densi (ogni 3-8s) data la brevita'.
5. Aggiornare workflow-state col progresso del reparto.

## Esempi
- Happy: input valido -> department-lead produce l'output atteso con trace.
- Edge: input parziale/incompleto -> procede col disponibile e dichiara la limitazione.
- Failure-recovery: errore tool -> registra in memory/errors e ritenta/escala al lead.

## Handoff in uscita
Al reparto successivo (o al verification/forge) con summary + trace.
