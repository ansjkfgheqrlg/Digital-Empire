---
name: strategy-manifest-skill
tier: tier0-orchestration
description: "Skill che governa la selezione e l'applicazione delle strategie: produce il Strategy Manifest (reparto + tipo contenuto + stile wiki) e lo impone ai reparti. Coordina il reparto Strategy."
uses_scripts:
  - scripts/generate_strategy_manifest.py
controls:
  - strategie tier1 di reparto
---

# strategy-manifest-skill (tier0-orchestration)

> Sceglie e impone la strategia giusta per ogni run (non una generica).

## Cosa fa
- Genera il Strategy Manifest via generate_strategy_manifest.py.
- Lo salva in memory/strategy-applications/ e lo distribuisce ai reparti.
- Coordina coordinator/applicator/controller/improver del reparto Strategy.

## Come si usa
```
python scripts/generate_strategy_manifest.py --input-type <t> --focus <f> --run <run-id>
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `strategy-department/strategy-coordinator`
- `strategy-department/strategy-applicator`

## Trace
risponde a 'tante strategie specifiche gestite da un team di agenti'.
