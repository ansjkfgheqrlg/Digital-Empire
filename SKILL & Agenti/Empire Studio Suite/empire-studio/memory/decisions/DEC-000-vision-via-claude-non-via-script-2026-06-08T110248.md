# Vision via Claude, non via script

- **Category:** decisions
- **Timestamp:** 2026-06-08 11:02:48
- **Trace:** cronologia chat: 'il video va visto... passaggi che si mostrano'
## Contesto
il video va visto senza API/paid; uno script Python non puo' descrivere i frame

## Alternative
vision API a pagamento (rifiutata: viola no-paid); OCR tesseract (insufficiente: legge testo, non capisce UI)

## Decisione & Razionale
Claude Code E' un modello con visione: estraggo frame con yt-dlp+ffmpeg (CLI gratis) e Claude legge i PNG. Fix dell'AP01 scaffold-as-deliverable e del watcher finto.
