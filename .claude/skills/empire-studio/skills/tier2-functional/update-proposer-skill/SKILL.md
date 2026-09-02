---
name: update-proposer-skill
tier: tier2-functional
description: "Confronta gli atomi di una run con i workflow esistenti e produce uno scheletro di update-proposals.md (match atomo->workflow). Solo proposte, mai modifica."
uses_scripts:
  - scripts/update_proposer.py
---

# update-proposer-skill (tier2-functional)

> Dai nuovi atomi a proposte concrete per migliorare i workflow esistenti.

## Cosa fa
- Carica atoms.json della run e i workflow noti (workflow-state + lista).
- Trova candidati match atomo->workflow per parole chiave.
- Scrive update-proposals.md che l'agente raffina con proposte e trace.

## Come si usa
```
python skills/tier2-functional/update-proposer-skill/scripts/update_proposer.py --run myrun
```

## Invarianti
- Solo PROPOSTE: nessun workflow modificato.
- Trace alla fonte ispiratrice.

## Agenti che la impugnano
- `forge-wiki-department/update-proposer`
- `projects-repos-workloads-department/workload-comparator`

## Script
`scripts/update_proposer.py` produce lo scheletro dei candidati.

## Trace
risponde a 'la wiki interroga su come aggiornare i flussi esistenti'.
