---
name: wiki-writer-skill
tier: tier2-functional
description: "Scrive le note forgiate nella wiki di Digital Empire (sottocartella per tipo) e aggiorna log.md. Auto-rileva second-brain-vault/wiki. Evita sovrascritture."
uses_scripts:
  - scripts/write.py (wrapper) -> ../../scripts/wiki_writer.py (motore)
---

# wiki-writer-skill (tier2-functional)

> Deposita le note nella wiki di Digital Empire + aggiorna il log.

## Cosa fa
- Sceglie la sottocartella wiki per tipo (sources/concepts/tools/synthesis).
- Scrive le note con front-matter (fonte/data/topic) e aggiorna wiki/log.md.
- Auto-rileva il percorso della wiki risalendo le cartelle.

## Come si usa
```
python skills/tier2-functional/wiki-writer-skill/scripts/write.py --note runs/myrun/wiki-notes/ --kind external --source <url>
```

## Invarianti
- CLI-only, no API, no paid.
- Tracciabilita' P12 sugli output.
- Memory-first: aggiorna memory dopo l'azione.

## Agenti che la impugnano
- `forge-wiki-department/wiki-writer`

## Script
`scripts/write.py` mappa il tipo a sottocartella e delega a `scripts/wiki_writer.py`.

## Trace
realizza 'aggiungere contenuto alla wiki connessa a Claude Code'.
