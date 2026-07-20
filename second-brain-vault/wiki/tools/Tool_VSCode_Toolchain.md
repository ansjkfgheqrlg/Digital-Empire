---
Type: TOOL
Status: Active
Tags: #vscode #toolchain #editor #governance #adr-008
Created: 2026-07-20
Last updated: 2026-07-20
---

# Toolchain VS Code (editor ufficiale dell'impero)

## Overview
Scansione completa dei plugin VS Code (14 categorie del Marketplace, censimento reale dello stack
7.6k md / 867 py / 181 yaml) → decisione a 3 fasce per tutti i workflow W1-W10. Dossier canonico:
`PIANO-MAESTRO/19-TOOLCHAIN-VSCODE.md`. Config condivisa committata in `.vscode/` (extensions +
settings): VS Code propone l'installazione automatica a chiunque apra la repo.

## Decisioni chiave
- **Agente AI = solo Claude Code** (`anthropic.claude-code`). Copilot/Cody/Cline/Continue = duplicati
  → esclusi (Cody Free morto 2025-07, Dendron deprecato).
- **Mai format-on-save globale**: 7.625 md + vendor ADR-003 intoccabili.
- **Pesi reali del repo** guidano la scelta: Markdown (7.6k), Python (867), YAML (181), TSX (596).
- Tier 1 (10): Claude Code, GitLens, GitHub PR, Python, Pylance, Ruff, Markdown All in One,
  Markdown Memo (wikilink vault), YAML Red Hat, Spell Checker IT+EN.

## Usi attuali
- `.vscode/extensions.json` = recommendations ufficiali (Tier 1+2) + 2 unwanted (Dendron, Cody).
- `.vscode/settings.json` = format-on-save OFF, telemetry OFF, spellcheck it+en, wrap md.

## Related
- [[Tool_Forge_Agent_Skill_Reparto]] (W8, principale fruitore YAML+md della toolchain)
- [[Project_YouTube_Lead_Machine]] (W7, area md-heavy)
- Dossier: `PIANO-MAESTRO/19-TOOLCHAIN-VSCODE.md` · `PIANO-MAESTRO/18-ARCHITETTURA-IMPERO-REVISIONE.md` (mappa W1-W10)
