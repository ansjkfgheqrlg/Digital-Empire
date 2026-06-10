---
name: web-pipeline-skill
tier: tier1-department
description: "Skill di reparto che orchestra la pipeline Web (ricerca + crawl + estrazione): coordina le skill tier2 funzionali del reparto e applica il Strategy Manifest."
uses_scripts:
  - ../tier2-functional/web-research-skill
controls:
  - skill tier2 del reparto
---

# web-pipeline-skill (tier1-department)

> La catena del reparto Web (ricerca e crawl).

## Cosa fa
- Coordina web-research (Playwright) + estrazione contenuto + screenshot.
- Applica la strategia Web (stile reference/MOC, screenshot sezioni chiave).
- Consegna il materiale testuale + screenshot al Forge.

## Come si usa
```
(invocata dal department-lead; coordina le skill tier2 del reparto)
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `web-department/department-lead`

## Trace
orchestra il reparto Web.
