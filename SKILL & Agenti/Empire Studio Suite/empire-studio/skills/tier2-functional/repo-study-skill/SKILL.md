---
name: repo-study-skill
tier: tier2-functional
description: "Scanner READ-ONLY di repo/cartelle: mappa struttura, tipi di file, entrypoint, README. Mai modifica l'originale. Base per il deep study del 4o reparto."
uses_scripts:
  - scripts/scan_repo.py
---

# repo-study-skill (tier2-functional)

> Mappa la repo in sola lettura per il deep study (architettura/decisioni).

## Cosa fa
- Scansiona una cartella ignorando .git/node_modules/binari.
- Mappa conteggi, estensioni, entrypoint, README in repo-structure.json.
- Garantisce la sola lettura: nessun file modificato.

## Come si usa
```
python skills/tier2-functional/repo-study-skill/scripts/scan_repo.py --path <repo> --run myrun
```

## Invarianti
- SOLA LETTURA: mai modifica l'originale.
- Trace a file:riga.
- Ignora binari/vendored.

## Agenti che la impugnano
- `projects-repos-workloads-department/repo-deep-study`
- `projects-repos-workloads-department/department-lead`

## Script
`scripts/scan_repo.py` e' read-only (stdlib only).

## Trace
risponde a '4o reparto: studiarlo nei minimi dettagli, non lo devi modificare'.
