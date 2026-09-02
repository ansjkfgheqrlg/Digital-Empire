---
name: processing-pipeline-skill
tier: tier1-department
description: "Skill di reparto che orchestra la pipeline Processing & Vision (frame + visione + atomi): coordina le skill tier2 funzionali del reparto e applica il Strategy Manifest."
uses_scripts:
  - ../tier2-functional/video-vision-skill
  - ../tier2-functional/frame-extractor-skill
  - ../tier2-functional/transcript-clean-skill
controls:
  - skill tier2 del reparto
---

# processing-pipeline-skill (tier1-department)

> La catena della visione e dell'analisi.

## Cosa fa
- Coordina frame-extractor + video-vision + transcript-clean + knowledge-extractor.
- Mette la visione reale di Claude al centro dell'analisi.
- Consegna analysis + atoms.json (tracciati) al Forge.

## Come si usa
```
(invocata dal department-lead; coordina le skill tier2 del reparto)
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `processing-vision-department/department-lead`
- `processing-vision-department/video-watcher`

## Trace
orchestra il reparto Processing & Vision.
