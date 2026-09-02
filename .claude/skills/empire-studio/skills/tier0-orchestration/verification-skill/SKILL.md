---
name: verification-skill
tier: tier0-orchestration
description: "Skill che governa la verifica e il controllo continui: esegue il validator anti-stub, coordina i controllori (visione reale, coverage, compliance CLI-only, real-test) e puo' bloccare gli handoff."
uses_scripts:
  - scripts/validator.py
  - scripts/catalog_status.py
controls:
  - verifiche dei reparti
---

# verification-skill (tier0-orchestration)

> I controllori: niente e' 'fatto' finche' non e' verificato.

## Cosa fa
- Esegue validator.py (cancello anti-stub + nomi safe) sull'ecosistema.
- Coordina visual-verifier/coverage-controller/compliance-auditor/real-tester.
- Blocca gli handoff e apre ticket di errore quando una verifica fallisce.

## Come si usa
```
python scripts/validator.py
python scripts/catalog_status.py
```

## Invarianti
- No-stub (AP01).
- No-finto.
- CLI-only.
- Real-test prima del via libera.

## Agenti che la impugnano
- `verification-control-department/department-lead`
- `verification-control-department/visual-verifier`

## Trace
risponde a 'un intero reparto che deve verificare e controllori'.
