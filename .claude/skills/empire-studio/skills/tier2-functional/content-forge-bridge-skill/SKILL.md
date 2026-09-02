---
name: content-forge-bridge-skill
tier: tier2-functional
description: "Ponte verso content-forge: assembla forge-input/ (analisi+atomi+transcript+trace) da una run e prepara il comando /forge --target=wiki. Garantisce MKD e tracciabilita'."
uses_scripts:
  - scripts/prepare_forge_input.py
controls:
  - content-forge (skill esterna /forge)
---

# content-forge-bridge-skill (tier2-functional)

> Prepara il materiale e lo passa a content-forge per le note wiki.

## Cosa fa
- Raccoglie in forge-input/ tutti i materiali della run (analisi, atomi, transcript).
- Scrive un INDEX con le fonti e il comando /forge suggerito.
- Lascia all'agente content-forge-invoker l'invocazione di /forge --target=wiki.

## Come si usa
```
python skills/tier2-functional/content-forge-bridge-skill/scripts/prepare_forge_input.py --run myrun
/forge runs/myrun/forge-input/ --target=wiki --name myrun
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `forge-wiki-department/content-forge-invoker`

## Script
`scripts/prepare_forge_input.py` assembla l'input; il forging vero lo fa la skill content-forge.

## Trace
risponde a 'tutto va portato in content-forge'.
