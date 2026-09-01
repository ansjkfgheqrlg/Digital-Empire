# Tools — memory-wiki-bridge

## Read / Grep / Glob
- `company/Memory/checkpoints/*.md`
- `company/Memory/decisions/*.md`
- `company/Memory/STATO-EMPIRE.md`
- `second-brain-vault/wiki/log.md`
- `second-brain-vault/wiki/index.md`

## Write
- Nuove pagine in `second-brain-vault/wiki/{projects,concepts,entities,tools,sources,synthesis}/`

## Edit
- `second-brain-vault/wiki/index.md`
- `second-brain-vault/wiki/log.md`
- Pagine wiki esistenti (append/aggiornamento, mai overwrite)

## Handoff
- Produce `memory/handoffs/wiki-bridge-<timestamp>.json` con l'elenco gap trovati/colmati,
  passato a knowledge-cartographer per verifica grafo.
