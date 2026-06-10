---
name: video-vision-skill
tier: tier2-functional
description: "Skill funzionale che realizza il 'video va visto' di Empire Studio. Combina estrazione di frame reali (ffmpeg) con la visione nativa di Claude: produce uno scheletro di analisi (script assemble_analysis.py) e lo fa riempire all'agente video-watcher che LEGGE i PNG. Niente vision API, niente descrizioni inventate. Output: video-analysis.md reale con visual timeline, key visual passages e atomi tracciati."
uses_scripts:
  - scripts/assemble_analysis.py
depends_on_engine:
  - ../../scripts/frame_extractor.py
  - ../../scripts/yt_ingest.py
---

# video-vision-skill (Tier-2 funzionale)

> Il cuore del requisito #1: **il video va visto**. Risolve l'errore del primo
> tentativo (uno script che inventava le descrizioni) facendo guardare i frame
> a Claude.

## Cosa fa
1. Prerequisiti (da altre skill): `yt_ingest.py` ha gia' ingerito il video e
   `frame_extractor.py` ha gia' estratto i frame reali in `runs/<run>/frames/`.
2. `assemble_analysis.py` crea lo **scheletro** `video-analysis.SKELETON.md`:
   una voce per ogni frame (timestamp + capitolo + trace) con un segnaposto
   `[VISIONE: ...]`. Questo e' lavoro deterministico, niente invenzione.
3. L'agente **video-watcher** (Claude) apre ogni `frame-NNN.png` con Read e
   riempie i segnaposto con descrizioni REALI -> `video-analysis.md`.

## Come si usa
```
# 1) frame reali (skill frame-extractor)
python ../../scripts/frame_extractor.py --run <run-id> --max-frames 12
# 2) scheletro
python scripts/assemble_analysis.py --run <run-id>
# 3) l'agente video-watcher legge i PNG e completa video-analysis.md
```

## Invarianti
- **NO-FINTO:** lo script non descrive nulla. La descrizione la fa Claude vedendo.
- **Trace (P12):** ogni voce porta `<id>#<ts> + frame-NNN.png`.
- **CLI-only, no paid:** ffmpeg + yt-dlp + Claude vision (inclusa, gratis).

## File
- `scripts/assemble_analysis.py` - generatore di scheletro (reale, compila).
- Reference protocollo: `references/ARCHITECTURE.md` §6.

## Agente che la impugna
`agents/processing-vision-department/video-watcher/` (7 file).

## Test eseguito (reale)
Smoke test su "Me at the zoo" (jNQXAC9IVRw): 6 frame estratti, Claude li ha
guardati, `video-analysis.md` reale prodotto. Vedi `runs/test-youtube-001/`.
