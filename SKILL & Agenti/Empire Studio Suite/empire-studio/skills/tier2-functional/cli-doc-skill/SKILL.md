---
name: cli-doc-skill
tier: tier2-functional
description: "Genera report leggibili (stile cli-printing-press) da una run: cosa e' stato ingerito, dove e' finito, con le trace principali. Per il deliverable finale all'utente."
uses_scripts:
  - scripts/make_report.py
---

# cli-doc-skill (tier2-functional)

> Il report finale leggibile della run (cosa/dove/trace).

## Cosa fa
- Legge gli artefatti della run (ingest, frame, analisi, note wiki, proposte).
- Assembla runs/<run-id>/REPORT.md strutturato e leggibile.
- Elenca le trace principali fonte->frame->nota.

## Come si usa
```
python skills/tier2-functional/cli-doc-skill/scripts/make_report.py --run myrun
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `forge-wiki-department/knowledge-packager`

## Script
`scripts/make_report.py` assembla il report dai file della run.

## Trace
usa cli-printing-press per output professionale, come da repo fornita.
