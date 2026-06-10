---
name: youtube-pipeline-skill
tier: tier1-department
description: "Skill di reparto che orchestra la pipeline YouTube (ingest -> frame -> visione): coordina le skill tier2 funzionali del reparto e applica il Strategy Manifest."
uses_scripts:
  - ../tier2-functional/yt-ingest-skill
  - ../tier2-functional/frame-extractor-skill
controls:
  - skill tier2 del reparto
---

# youtube-pipeline-skill (tier1-department)

> La catena completa del reparto YouTube.

## Cosa fa
- Coordina yt-ingest + frame-extractor + video-vision per i video YouTube.
- Applica la strategia YouTube (frame per capitolo, visione densa per long-form).
- Consegna le run analizzate al reparto Forge & Wiki.

## Come si usa
```
(invocata dal department-lead; coordina le skill tier2 del reparto)
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `youtube-department/department-lead`

## Trace
orchestra il reparto YouTube.
