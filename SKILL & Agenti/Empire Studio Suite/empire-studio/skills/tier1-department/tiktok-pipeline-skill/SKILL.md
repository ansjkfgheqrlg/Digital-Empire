---
name: tiktok-pipeline-skill
tier: tier1-department
description: "Skill di reparto che orchestra la pipeline TikTok (video brevi, frame densi): coordina le skill tier2 funzionali del reparto e applica il Strategy Manifest."
uses_scripts:
  - ../tier2-functional/yt-ingest-skill
  - ../tier2-functional/frame-extractor-skill
controls:
  - skill tier2 del reparto
---

# tiktok-pipeline-skill (tier1-department)

> La catena del reparto TikTok (video brevi).

## Cosa fa
- Coordina tiktok-ingest + frame-extractor (densi) + video-vision.
- Applica la strategia TikTok (frame ogni pochi secondi, quick-reference).
- Consegna le run analizzate al Forge.

## Come si usa
```
(invocata dal department-lead; coordina le skill tier2 del reparto)
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `tiktok-department/department-lead`

## Trace
orchestra il reparto TikTok.
