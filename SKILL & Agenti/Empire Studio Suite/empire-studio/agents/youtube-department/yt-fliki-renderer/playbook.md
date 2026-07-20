# yt-fliki-renderer - Playbook

## Flusso operativo

1. Ricevi script + voiceId + run-id dal lead
2. Prepari payload per `POST /v1/generate/video`
3. Invia richiesta e ottieni job_id
4. Polling `GET /generate/status` ogni 10 secondi (max 5 minuti)
5. Quando status = "completed" → scarica MP4
6. Salva `render.json` con metadata
7. Chiama `memory_manager.py --checkpoint "Fliki render completato"`
8. Handoff al yt-seo-publisher

## Esempi
- Happy path: script valido → video generato + trace
- Edge: API limit → attesa + retry con backoff
- Failure: errore API → registra in memory/errors e scala al lead

## Handoff in uscita
Al yt-seo-publisher con `render.json` + trace.