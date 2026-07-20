# yt-seo-publisher - Playbook

## Flusso operativo

1. Ricevi video.mp4 + metadata dal yt-fliki-renderer
2. Prepari payload per YouTube Data API (title, description con link Manuale, tags, privacyStatus)
3. Carichi il video
4. Imposti thumbnail (se presente)
5. Pubblichi
6. Salvi `publish.json` con URL e ID video
7. Chiami memory_manager.py --checkpoint
8. Handoff a yt-performance-analyzer

## Esempi
- Happy path: video caricato → URL YouTube + trace
- Edge: quota API esaurita → retry con backoff
- Failure: errore upload → registra in memory/errors

## Handoff in uscita
Al yt-performance-analyzer con `publish.json` + trace P12.