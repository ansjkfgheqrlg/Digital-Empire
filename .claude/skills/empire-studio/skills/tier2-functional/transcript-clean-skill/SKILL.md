---
name: transcript-clean-skill
tier: tier2-functional
description: "Pulisce un transcript .vtt/.srt (rimuove timestamp/tag/duplicati) e ricompone frasi leggibili con ancore temporali, per la sincronia testo-immagine."
uses_scripts:
  - scripts/clean_transcript.py
---

# transcript-clean-skill (tier2-functional)

> Da auto-sub rumorosi a transcript leggibile e ancorato ai tempi.

## Cosa fa
- Parsa .vtt/.srt e rimuove header/tag/duplicati consecutivi.
- Ricompone le frasi con ancore temporali ogni ~30s.
- Produce runs/<run-id>/transcript.clean.md (o segnala l'assenza di transcript).

## Come si usa
```
python skills/tier2-functional/transcript-clean-skill/scripts/clean_transcript.py --run myrun
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `processing-vision-department/transcript-processor`

## Script
`scripts/clean_transcript.py` e' standalone (stdlib only).

## Trace
supporta 'trascrive tutto completamente' + sincronia con la visione.
