---
name: forge-wiki-skill
tier: tier1-department
description: "Skill di reparto che orchestra la pipeline Forge & Wiki (forge -> wiki -> update proposals): coordina le skill tier2 funzionali del reparto e applica il Strategy Manifest."
uses_scripts:
  - ../tier2-functional/content-forge-bridge-skill
  - ../tier2-functional/wiki-writer-skill
  - ../tier2-functional/cli-doc-skill
  - ../tier2-functional/update-proposer-skill
controls:
  - skill tier2 del reparto
---

# forge-wiki-skill (tier1-department)

> La catena finale verso la wiki.

## Cosa fa
- Coordina content-forge-bridge + content-forge (/forge) + wiki-writer + cli-doc.
- Applica lo stile wiki del Strategy Manifest.
- Produce note wiki + REPORT + update proposals.

## Come si usa
```
(invocata dal department-lead; coordina le skill tier2 del reparto)
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `forge-wiki-department/department-lead`

## Trace
orchestra il reparto Forge & Wiki.
