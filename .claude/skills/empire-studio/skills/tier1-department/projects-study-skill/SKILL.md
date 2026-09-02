---
name: projects-study-skill
tier: tier1-department
description: "Skill di reparto che orchestra la pipeline Projects/Repos (deep study read-only): coordina le skill tier2 funzionali del reparto e applica il Strategy Manifest."
uses_scripts:
  - ../tier2-functional/repo-study-skill
  - ../tier2-functional/update-proposer-skill
controls:
  - skill tier2 del reparto
---

# projects-study-skill (tier1-department)

> La catena del deep study di progetti/repo.

## Cosa fa
- Coordina repo-study (scan read-only) + deep analysis + estrazione atomi.
- Garantisce la regola di sola lettura (mai modifica l'originale).
- Consegna deep-analysis + atomi tracciati al Forge.

## Come si usa
```
(invocata dal department-lead; coordina le skill tier2 del reparto)
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `projects-repos-workloads-department/department-lead`

## Trace
orchestra il 4o reparto (deep study).
