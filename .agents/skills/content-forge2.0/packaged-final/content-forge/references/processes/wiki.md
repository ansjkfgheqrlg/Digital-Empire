# Process: `wiki` — Obsidian Second Brain Integration

> Builder: `wiki-builder-agent` (B7)
> Stage: 5
> Tempo medio stimato: 2 turni utente + 1-2 iterazioni

---

## 1. Identità

Il target `wiki` trasforma il KG in **un set di note atomiche per il vault Obsidian** dell'utente, una nota per concetto, con backlink `[[wikilink]]` densi e MOC (Map of Content) generati. È il target con la **forma più granulare**: molte piccole note interconnesse, invece di un singolo documento monolitico.

Aderisce ai principi di **Andy Matuschak** (evergreen notes) e **Zettelkasten** (un'idea per nota, connessioni esplicite). Ogni nota è:
- atomica (un solo concetto)
- evergreen (formulata per durare, non come "appunti di...")
- connessa (≥2 backlink in media)
- contestualizzata (frontmatter + tag)

Obsidian-specific: usa `[[wikilinks]]`, frontmatter YAML, embed `![[note]]`, tag `#tag/sub`, callout `> [!note]`.

## 2. Forma canonica dell'output

```
output/
└── vault-import/
    ├── MOC - <topic>.md           # Map of Content principale
    ├── _Index.md                  # entry point con link a MOC e categorie
    ├── concepts/
    │   ├── <atom-slug-1>.md       # nota atomica
    │   ├── <atom-slug-2>.md
    │   └── ...
    ├── examples/
    │   └── <example-slug>.md      # esempi corposi tratti dal sorgente (P2)
    ├── frameworks/
    │   └── <framework-slug>.md    # framework/modelli (P6)
    ├── procedures/
    │   └── <procedure-slug>.md    # how-to step-by-step (P5)
    ├── glossary/
    │   └── <term-slug>.md         # termini definiti (con `aliases`)
    ├── _meta/
    │   ├── source.md              # nota che descrive il sorgente
    │   └── import-log.md          # cosa è stato importato, quando, da Forge
    ├── changelog.md
    └── README.md                  # come integrare nel proprio vault
```

### Struttura canonica di una nota atomica

```markdown
---
title: <Titolo human-readable>
aliases: [<sinonimi>, <abbreviazioni>]
tags:
  - <area>/<sub>
  - source/<source-slug>
  - status/seedling | budding | evergreen
created: <ISO date>
source: "[[_meta/source]]"
forge_atom_id: <id>
---

# <Titolo>

## Definizione canonica
<1-2 frasi che definiscono il concetto in modo evergreen>

## Spiegazione estesa
<paragrafi ampliati dal KG>

## Esempio
<dal sorgente, con citazione>

## ➕ Esempio aggiuntivo
<generato da Forge, etichettato>

## Schema
```
<ascii / mermaid se applicabile>
```

## Connessioni
- Si appoggia su [[<prerequisito>]]
- Si applica in [[<contesto-1>]], [[<contesto-2>]]
- Contrasta con [[<concetto-opposto>]]
- Vedi anche [[<concetto-correlato>]]

## Domande aperte
- ...

## Riferimenti
- Source: [[_meta/source]] § <sezione>
```

### Struttura del MOC

```markdown
---
title: MOC — <topic>
tags: [moc, source/<source-slug>]
---

# MOC — <topic>

> Map of Content auto-generata da `content-forge`. Riorganizza secondo le tue preferenze.

## 🌱 Concetti di base
- [[<concept-1>]] — <1-line description>
- [[<concept-2>]] — ...

## 🧠 Framework e modelli
- [[<framework-1>]] — ...

## 🛠 Procedure
- [[<procedure-1>]] — ...

## 📚 Esempi
- [[<example-1>]] — ...

## 📖 Glossario
- [[<term-1>]] — ...

## 🔗 Connessioni esterne (suggerite)
> Forge ha trovato concetti che potrebbero collegarsi a note già esistenti nel tuo vault.
> Usalo come spunto, verifica tu.
- [[<external-note-1>]]
- [[<external-note-2>]]
```

## 3. Input atteso

```
inputs/
├── kg.json
├── atoms/
├── source_meta.json
├── user_answers.json
└── (opzionale) vault_index.json   # se l'utente ha esportato la lista delle sue note esistenti
```

## 4. PLAN (cosa fa il builder)

1. Legge `kg.json` e mappa ogni atomo a **una nota atomica** (target 1:1).
2. Identifica **categorie** (concept / framework / procedure / example / glossary) → cartelle.
3. Identifica **gerarchie** (P3) → strutturano il MOC.
4. Identifica **alias** per ogni concetto (sinonimi nel sorgente).
5. Identifica i **link incrociati** (P8) sia interni al set sia (se disponibile) verso il vault esistente.
6. Stima il MOC: quanti cluster, quante voci per cluster.
7. Restituisce PLAN al Conductor.

## 5. ASK (domande generate da D1)

1. **Vault path**: "Qual è il path del tuo vault Obsidian?"
2. **Cartella di destinazione**: "Vuoi che le note vadano in `<vault>/<cartella>/`? Propongo `Imports/Forge/<topic>/`."
3. **Tag convention**: "Hai una tag convention esistente? (es. `#area/...`, `#status/...`, `#source/...`). Te la propongo o seguo la tua?"
4. **Template di nota**: "Hai un template di nota standard nel tuo vault? Se sì, dammi il path; lo userò come base."
5. **Naming convention**: "Naming dei file: `kebab-case`, `Title Case`, o altro? Underscore o spazi?"
6. **Lingua**: "Note in italiano, inglese, o lingua del sorgente?"
7. **MOC**: "Sì/no? Se sì, quanti livelli di gerarchia?"
8. **Granularità**: "Una nota per atomo (proposta default) o vuoi note più dense (1 nota per cluster)?"
9. **Esempi**: "Gli esempi vanno in note separate (più atomiche) o inline nella nota del concetto (più contestualizzati)?"
10. **Vault index**: "Mi puoi dare un export della lista delle tue note esistenti (anche solo nomi)? Così posso suggerire link a note che già hai."
11. **Status iniziale**: "Le note nascono come `seedling`, `budding` o `evergreen`?"
12. **Collisioni**: "Se una nota proposta ha lo stesso nome di una tua esistente: skip, rename, merge prompt?"

## 6. BUILD (ordine di scrittura)

1. **`_meta/source.md`**: prima cosa, perché tutte le altre note ci puntano.
2. **`_meta/import-log.md`**: log della creazione (per tracciabilità).
3. **Per ogni atomo del KG**: una nota in `concepts/` (o nella cartella categorica giusta) con la struttura canonica.
4. **`glossary/`**: per ogni termine con definizione, una nota separata con `aliases`.
5. **`examples/`** (se l'utente ha scelto esempi separati): un file per esempio significativo.
6. **`frameworks/`**, **`procedures/`**: come sopra per i pattern P5/P6.
7. **Collegamenti**: passa su tutte le note e sostituisce menzioni di concetti con `[[wikilink]]` corretti. Usa `obsidian_packager.py` per garantire integrità.
8. **MOC**: genera `MOC - <topic>.md` con strutturazione gerarchica dei cluster.
9. **`_Index.md`**: entry point con link al MOC e alle cartelle.
10. **Suggested external links** (se `vault_index.json` disponibile): aggiunge sezione al MOC con suggerimenti di connessione a note esistenti.
11. **Self-critique** (vedi §7).
12. **`README.md`**: come integrare nel vault, raccomandazioni post-import (es. "review delle note seedling", "valida i suggested links").

## 7. Self-critique (interna)

- **Atomicità**: ogni nota tratta UN solo concetto? (proxy: titoli con "e", "/" sono red flag)
- **Evergreen-ness**: ogni nota è formulata in modo durevole (no "in questo video Tizio dice..." come opening — riformulare)?
- **Backlink density**: media >= 2 wikilinks per nota? Se no, c'è isolation problem.
- **Alias coverage**: termini con sinonimi nel sorgente hanno `aliases` nel frontmatter?
- **MOC coverage**: ogni nota è raggiungibile dal MOC in ≤2 hop?
- **No orphan notes**: nessuna nota senza backlink o senza outlink (eccetto glossary terminali)?
- **Slug consistency**: i nomi file rispettano la naming convention scelta?
- **Wikilink integrity**: ogni `[[link]]` punta a un file esistente nel set (verificato da `obsidian_packager.py`)?
- **Frontmatter validity**: YAML parsabile per tutte le note?

## 8. Critique esterna (C1 + C3)

- **C1**: ogni atomo del KG è una nota o è esplicitamente embedded in una nota. Soglia 95% (alta, perché è il target più atomico).
- **C3**: schema validation su frontmatter, wikilink integrity (`obsidian_packager.py`), tag convention compliance, file naming.

## 9. Iterate

Tipici fix:
- splittare note non atomiche
- riformulare in evergreen
- aggiungere backlink in note isolate
- normalizzare slug
- aggiungere alias mancanti

## 10. Failure modes del processo

| Failure | Sintomo | Mitigazione |
|---|---|---|
| Note "narrative" | "In questo video..." | Riformulare in evergreen |
| Note giganti | >1000 parole per nota | Splittare in atomiche |
| No backlinks | Nota isolata | Forzare ≥1 outlink ad atomo correlato |
| Wikilink rotti | `[[xxx]]` non risolve | `obsidian_packager.py` blocca commit |
| Tag chaos | Tag inconsistenti | Forzare adesione alla convention dichiarata |
| Slug collision con vault esistente | Sovrascriverebbe nota dell'utente | Skip + report o rename con suffisso |

## 11. Esempio realistico

Input: serie di 8 articoli + 3 video su "advanced RAG" → KG con 132 atomi.
Vault: `~/Vault`, cartella import `Imports/Forge/Advanced RAG/`.
Tag convention: `#area/ai/rag`, `#source/forge-import-2025-05`, `#status/seedling`.
Naming: `kebab-case`.
Granularità: 1 nota per atomo, esempi separati.

Output:
- 132 note in `concepts/`
- 18 note in `glossary/` con aliases
- 24 note in `examples/`
- 9 note in `frameworks/`
- 7 note in `procedures/`
- MOC con 9 cluster
- `_Index.md`
- `_meta/source.md`
- ~190 file totali, ~14k backlink

Coverage: 96%. Schema: OK. Wikilink integrity: 100% (zero rotti).

## 12. Handoff al Conductor

- path `output/vault-import/`
- `build-report.json`
- `next-suggestions.md` (es. "ho identificato 8 note del tuo vault esistente che potrebbero linkare alle nuove — vuoi che generi una lista di edit suggeriti per quelle note?")

---

## 13. 📎 Appendice — Helpers Obsidian (embedded)

### Slug generation (canonica)

```python
import re, unicodedata
def slugify(title: str, style: str = "kebab") -> str:
    """Converte un titolo in slug per il filename Obsidian."""
    # Normalizza unicode (accenti, etc)
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    # Rimuove caratteri non alfanumerici (preserva spazi)
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    if style == "kebab":
        return re.sub(r"[\s_]+", "-", s)
    if style == "snake":
        return re.sub(r"[\s-]+", "_", s)
    if style == "title":
        return title.strip()  # mantieni casing
    raise ValueError(f"unknown style: {style}")
```

### Frontmatter canonico per nota atomica

```python
import datetime as dt
def build_frontmatter(atom_id: str, title: str, aliases: list[str], tags: list[str],
                      source_slug: str, status: str = "seedling") -> dict:
    return {
        "title": title,
        "aliases": aliases,
        "tags": tags + [f"source/{source_slug}", f"status/{status}"],
        "created": dt.date.today().isoformat(),
        "source": f"[[_meta/source]]",
        "forge_atom_id": atom_id
    }
```

### Wikilink integrity check (pseudo)

```python
import re, pathlib
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:\#[^\]|]+)?(?:\|[^\]]+)?\]\]")

def check_wikilinks(vault_import_dir: pathlib.Path) -> list[tuple[str, str]]:
    """Ritorna lista di (file_sorgente, link_rotto)."""
    existing = {p.stem for p in vault_import_dir.rglob("*.md")}
    broken = []
    for f in vault_import_dir.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        for m in WIKILINK.finditer(text):
            target = m.group(1).strip()
            if target not in existing:
                broken.append((str(f), target))
    return broken
```

### MOC scaffold (data structure)

```python
moc_structure = {
    "topic": str,
    "categories": [
        {
            "label": str,             # "🌱 Concetti di base"
            "tag_filter": str,        # "#area/X/base"
            "entries": [
                {"slug": str, "one_liner": str}
            ]
        }
    ],
    "suggested_external_links": list[str]   # da vault_index.json se presente
}
```
