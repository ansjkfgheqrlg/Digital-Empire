---
name: frame-extractor-skill
tier: tier2-functional
description: "Estrazione di frame VERI da video con ffmpeg ai timestamp dei capitoli o a intervalli. Scarica il video a bassa risoluzione (yt-dlp) e produce PNG + manifest. I frame li guardera' Claude."
uses_scripts:
  - scripts/extract.py (wrapper) -> ../../scripts/frame_extractor.py (ffmpeg)
---

# frame-extractor-skill (tier2-functional)

> Frame reali (non screenshot ripetuti) che il video-watcher guardera' davvero.

## Cosa fa
- Scarica il video a bassa risoluzione (leggero, no audio).
- Estrae frame con ffmpeg ai capitoli o a intervalli/%.
- Scrive frames/frame-NNN.png + frames/manifest.json (frame->timestamp->capitolo).

## Come si usa
```
python skills/tier2-functional/frame-extractor-skill/scripts/extract.py --run myrun --kind youtube
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `processing-vision-department/frame-extractor`
- `processing-vision-department/video-watcher`

## Script
`scripts/extract.py` imposta la densita' di frame per tipo e delega a `scripts/frame_extractor.py`.

## Trace
fornisce i frame REALI: corregge il watcher finto del primo tentativo.
