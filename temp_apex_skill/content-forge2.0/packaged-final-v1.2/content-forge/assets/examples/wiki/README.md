# Esempio end-to-end — target `wiki` (Obsidian)

> Output di `B7 wiki-builder-agent`.
> Trasforma il workshop in **note atomiche Obsidian** evergreen con MOC e backlink fitti.

## Input

- Sorgente / KG / MKD: `_shared/`
- ASK answers:
  - Vault path: `~/Vault`
  - Cartella destinazione: `Imports/Forge/Prompt Engineering`
  - Tag convention: `#area/ai/prompting`, `#source/forge-import-2026-05`, `#status/seedling`
  - Naming: kebab-case
  - Lingua: italiano (preservata da MKD)
  - MOC: sì, 1 livello
  - Granularità: 1 nota per atomo del KG (12 atomi → 12 note)
  - Esempi: separati in `examples/`
  - Vault index: non fornito (no suggested external links)
  - Status: tutte seedling (utente le promuoverà a evergreen dopo review)

## Output

```
vault-import/
├── MOC - Prompt Engineering Avanzato.md
├── _Index.md
├── concepts/                                  # 6 note (atomi category=concept)
│   ├── prompt-come-interfaccia.md
│   ├── few-shot-prompting.md
│   ├── in-context-learning.md
│   ├── chain-of-thought-cot.md
│   ├── self-consistency.md
│   ├── structured-output.md
│   └── delimiters.md
├── frameworks/                                # 3 note (atomi category=framework)
│   ├── istruzioni-vaghe.md                    # anti-pattern
│   ├── prompt-giganti-lost-in-the-middle.md   # anti-pattern
│   └── modello-come-collega-cooperativo.md    # mental model
├── procedures/                                # 1 nota
│   └── prompt-come-codice-versionare-testare.md
├── claims/                                    # 1 nota
│   └── quando-cot-non-aiuta.md
├── _meta/
│   ├── source.md                              # info sul workshop
│   └── import-log.md                          # log generato da Forge
├── changelog.md
└── README.md
```

12 note totali (1:1 con KG atomi) + MOC + Index + 2 meta = **16 file**.

## Stats

- 12 atomi → 12 note (1:1 ratio, granularità massima)
- Wikilink integrity: 100% (verificata da `obsidian_packager.py --check-only`)
- Average outlinks per note: 2.8
- MOC: 4 sezioni (concepts / frameworks / procedures / claims)
- Frontmatter: tutti validi YAML
- Coverage atomi: 100%

## Quando trascinare nel vault

L'utente trascina `vault-import/Imports/Forge/Prompt Engineering/` dentro il suo vault. Obsidian indicizza automaticamente, MOC funziona, wikilink risolvono.

## Differenza con `doc`

| Aspetto | `doc` (singolo file) | `wiki` (note atomiche) |
|---|---|---|
| Output | 1 file lungo | 16 file piccoli |
| Lettura | sequenziale | esplorativa (graph + MOC) |
| Manutenzione | edit centralizzato | edit locale per nota |
| Riusabilità | come reference | come building blocks per altre note |
| Use case | onboarding nuovo membro | second brain / Zettelkasten personale |
