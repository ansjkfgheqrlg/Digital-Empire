# P8 — Cross-Reference Weaving

> Crea **link semantici** tra gli atomi del KG (interni all'output) e suggerisce link verso il vault Obsidian dell'utente (esterni). Trasforma una collezione piatta di atomi in un grafo navigabile.

## Cosa fa

1. **Edge inference** durante la costruzione del KG (A3 + P3).
2. **Weaving** durante la generazione dell'output: ogni menzione di un concetto trattato altrove diventa un link.
3. **Suggested external links**: se l'utente ha condiviso `vault_index.json`, suggerisce collegamenti a sue note esistenti.

## Chi lo applica

- **A3 `knowledge-graph-agent`** — costruisce gli edge nel KG.
- **B1 `doc-builder`** — link interni `[testo](#anchor)` nel documento finale.
- **B7 `wiki-builder`** — `[[wikilink]]` Obsidian + suggested external links nel MOC.
- **B4 `skill-builder`** — pointer tra `SKILL.md` e `references/`.

## Quando applicarlo

Sempre nel KG (P3 + P8 sono congiunti).
Quasi sempre nei target output (qualunque output strutturato beneficia di cross-ref).

## Quando ammorbidire

- Output molto brevi (1 atomo singolo) → non c'è nulla da tessere.
- Target `custom` con vincoli di formato che non ammettono link.

## Cuore del pattern

```python
# Tipi di link prodotti da P8
link_types = {
    "internal_anchor": "[testo](#sezione)",        # nel doc
    "internal_wikilink": "[[slug]]",               # nella wiki Obsidian
    "internal_anchor_wikilink": "[[slug#header]]", # nella wiki con sub-anchor
    "external_suggested": "[[<existing-vault-note>]]",  # suggerimento
    "alias_link": "[[slug|testo visualizzato]]",   # con label custom
    "embed": "![[slug]]",                          # solo Obsidian, embed di una nota dentro un'altra
}
```

## Quando un atomo "merita" un link

Heuristica:
1. **Definizione altrove**: se l'atomo A è definito in una sezione/nota e l'atomo B menziona A nel suo testo → link.
2. **Prerequisite** (P3 edge): la sezione di B inizia con "richiede [[A]]".
3. **Contrast** (P4 controesempio): "contrasta con [[A]]".
4. **Applies-in / example-of**: nei doc esempi possono linkare back al concetto principale.
5. **See-also**: in coda alla sezione, lista di link a atomi correlati ma non strettamente collegati.

## Algoritmo (pseudo)

```python
import re

def weave_internal_links(text: str, atoms: list[dict], style: str = "wikilink") -> str:
    """Sostituisce menzioni di atomi con link."""
    # Build alias map: ogni atomo → tutti i suoi nomi (title + aliases)
    alias_map = {}
    for atom in atoms:
        all_aliases = [atom["title"]] + atom.get("aliases", [])
        for alias in all_aliases:
            alias_map[alias.lower()] = atom

    # Match in ordine di lunghezza decrescente (per evitare match parziali)
    sorted_aliases = sorted(alias_map.keys(), key=len, reverse=True)

    for alias in sorted_aliases:
        atom = alias_map[alias]
        slug = atom.get("slug", atom["id"])
        # Sostituisci solo PRIMA occorrenza per sezione (evita rumore)
        if style == "wikilink":
            replacement = f"[[{slug}|{alias}]]"
        elif style == "anchor":
            replacement = f"[{alias}](#{slug})"
        else:
            continue
        # Regex word-boundary, case-insensitive, only first match
        pattern = re.compile(rf"\b{re.escape(alias)}\b", re.I)
        text = pattern.sub(replacement, text, count=1)

    return text

def suggest_external_links(atoms: list[dict], vault_index: list[dict]) -> list[dict]:
    """Per ogni atomo, suggerisce note del vault esistente che sono semanticamente vicine."""
    suggestions = []
    for atom in atoms:
        scored = []
        for vault_note in vault_index:
            score = semantic_similarity(atom["title"] + " " + atom["canonical_definition"],
                                        vault_note["title"] + " " + vault_note.get("excerpt", ""))
            if score >= 0.7:
                scored.append((score, vault_note))
        if scored:
            top3 = sorted(scored, reverse=True)[:3]
            suggestions.append({"atom_id": atom["id"],
                                "suggested": [n for _, n in top3]})
    return suggestions
```

## Esempio: weaving nel doc-builder

Prima (output grezzo):
> "Per implementare RAG efficacemente, parti da un buon chunking. Il chunking semplice è naive ma funziona; opzioni più sofisticate includono sliding window e semantic chunking."

Dopo (con P8 applicato):
> "Per implementare [[rag|RAG]] efficacemente, parti da un buon [[chunking-strategy|chunking]]. Il [[chunking-naive|chunking semplice]] è naive ma funziona; opzioni più sofisticate includono [[sliding-window-chunking|sliding window]] e [[semantic-chunking]]."

## Esempio: suggested external links nel MOC della wiki

Se `vault_index.json` contiene una nota dell'utente `[[information-retrieval-basics]]`, il MOC includerà:

```markdown
## 🔗 Connessioni esterne (suggerite)
> Forge ha identificato note del tuo vault esistente che potrebbero collegarsi alle nuove.
> Verifica e accetta/scarta a tua discrezione.

- [[information-retrieval-basics]] — connesso a [[rag]], [[semantic-chunking]]
- [[vector-database-comparison]] — connesso a [[embedding-models]]
```

## Densità target

- **Doc** (`doc-builder`): in media 2-4 link interni per capitolo (non sovraccaricare).
- **Wiki** (`wiki-builder`): media ≥2 outlink per nota (Andy Matuschak suggerisce 3-5 in media per evergreen notes mature).
- **Skill** (`skill-builder`): SKILL.md → references → reference cross-link (gerarchia, no flat web).

## Anti-pattern

- **Over-linking**: linkare ogni menzione di ogni alias → l'output diventa una lista di wikilink. Limita per sezione.
- **Link rotti**: `[[slug]]` che non risolve a nessuna nota. `obsidian_packager.py` deve fallire.
- **Link circolari semantici**: A → B → C → A senza che ci sia vera dipendenza concettuale. Filtra.
- **Suggested external "auto-accettati"**: i suggerimenti esterni sono *suggerimenti*; il MOC li elenca esplicitamente come tali, non li integra direttamente nelle note.

## Riferimenti

- Andy Matuschak — *Evergreen notes should be densely linked*
- Bush, V. — *As We May Think* (concetto storico di hypertext)
