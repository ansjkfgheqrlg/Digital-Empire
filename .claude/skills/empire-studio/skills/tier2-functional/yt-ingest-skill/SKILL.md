---
name: yt-ingest-skill
tier: tier2-functional
description: "Ingestione YouTube/TikTok via yt-dlp: video singolo o canale con screening per focus. Estrae metadata, sottotitoli, capitoli, thumbnail. CLI-only, no API."
uses_scripts:
  - scripts/ingest.py (wrapper) -> ../../scripts/yt_ingest.py (motore yt-dlp)
---

# yt-ingest-skill (tier2-functional)

> Da link/canale a materiale grezzo strutturato pronto per la visione.

## Cosa fa
- Ingerisce un video singolo (info+subs+thumbnail, no download del video).
- Fa screening di un canale/playlist filtrando per --focus.
- Produce runs/<run-id>/ingest.json con id, durata, capitoli, subs.

## Come si usa
```
python skills/tier2-functional/yt-ingest-skill/scripts/ingest.py <url> --focus design --run myrun
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `youtube-department/yt-channel-ingester`
- `youtube-department/video-single-ingester`
- `tiktok-department/tiktok-ingester`

## Script
`scripts/ingest.py` valida l'URL e delega al motore condiviso `scripts/yt_ingest.py`.

## Trace
risponde a 'parti da un link o da un canale e fai screening dei video'.
