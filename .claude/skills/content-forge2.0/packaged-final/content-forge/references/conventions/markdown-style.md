# Markdown Style Guide

> Convenzioni di formattazione applicate da TUTTI i builder.

## Heading

- Un solo `# H1` per file (è il titolo).
- Gerarchia stretta: `##` sotto `#`, `###` sotto `##`. Mai saltare livelli.
- Heading senza emoji a meno che non sia un MOC o file di navigazione.

## Liste

- `-` per unordered (mai `*`)
- `1.` per ordered (mai `1)`)
- Indentazione: 2 spazi per livello

## Blocchi codice

- Sempre con language hint: ` ```python `, ` ```json `, ` ```bash `
- Mai bare ` ``` ` senza linguaggio

## Tabelle

- Allineamento esplicito quando aumenta leggibilità (`|:---|---:|`)
- Header sempre presente
- Max 7 colonne (oltre → ristrutturare)

## Link

- Inline: `[testo](url)` per esterni
- Wiki: `[[slug]]` solo per target `wiki` (Obsidian)
- Reference: `[label]: url` in coda quando si ripete molto

## Frontmatter YAML

- Sempre tra `---` ... `---` a inizio file
- Chiavi `snake_case`
- Liste con `-`, mai inline `[]` salvo per array corti

## Callout (Obsidian-style, opzionale)

- `> [!note]`, `> [!warning]`, `> [!example]` per evidenziare

## Etichetta ➕

- Tutto il contenuto auto-generato da Forge (esempi, schemi, controesempi) prefissato con `➕` o introdotto da "➕ Esempio aggiuntivo:" / "➕ Schema:"
