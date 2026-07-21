# Naming Conventions

> Regole di naming per file, slug, ID atomi, ID agenti. Caricato da builder e validator.

## Slug per file e cartelle

- `kebab-case` per default
- ASCII only (no accenti)
- Max 60 char
- Niente date in head (`2025-05-23-...`) salvo casi specifici (es. import-log)

```python
import re, unicodedata
def slugify_kebab(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)[:60]
```

## ID atomi

- Pattern: `a-<NNN>` globale (es. `a-001`, `a-127`)
- Durante stage-02 (per chunk): `a-c<chunk>-<NNN>` (es. `a-c007-003`)
- A3 li riallinea a globali in `kg.json`

## ID cluster

- Pattern: `c-<NNN>`

## ID agente runtime

- L'agent_id resta `A1`..`D1` per riferimento al sistema
- Il nome file include `-agent.md` per chiarezza

## Nome dei target output

- `<target-slug>` deve essere kebab-case
- Se l'utente non lo specifica, builder propone `<intent>-<short>` (es. `prompt-engineering`)

## Naming Obsidian

- Vedi `references/processes/wiki.md` §6 e Appendice §13.
