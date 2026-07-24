---
title: MOC — Prompt Engineering Avanzato
tags:
  - moc
  - area/ai/prompting
  - source/forge-import-2026-05
---

# MOC — Prompt Engineering Avanzato

> Map of Content generata da `content-forge` dal workshop omonimo.
> 12 note atomiche totali, 4 categorie.
>
> **Nota** (questo è un esempio illustrativo): solo la nota `[[few-shot-prompting]]` è materializzata
> come file in questo esempio. Le altre sono elencate come placeholder (nomi delle note che
> sarebbero generate). In un run reale di Forge tutte le 12 note esistono fisicamente con frontmatter,
> body, backlink e wikilink integrity 100%.

## 🌱 Concetti

- **prompt-come-interfaccia** — il prompt è un'interfaccia con regole, pattern, anti-pattern *(placeholder)*
- [[few-shot-prompting]] — dare 2-5 esempi prima della richiesta ✅ *(nota completa in concepts/)*
- **in-context-learning** — pattern recognition runtime che fa funzionare few-shot *(placeholder)*
- **chain-of-thought-cot** — ragionare step by step esplicitando il ragionamento *(placeholder)*
- **self-consistency** — N CoT + majority voting *(placeholder)*
- **structured-output** — JSON/XML reliable via schema + esempi + JSON mode *(placeholder)*
- **delimiters** — marker per separare sezioni del prompt *(placeholder)*

## 🧠 Framework e mental model

- **modello-come-collega-cooperativo** — il mental model centrale *(placeholder)*
- **istruzioni-vaghe** — anti-pattern: "be creative" è vuoto *(placeholder)*
- **prompt-giganti-lost-in-the-middle** — anti-pattern: prompt >4000 parole *(placeholder)*

## 🛠 Procedure

- **prompt-come-codice-versionare-testare** — git, A/B test, CI/CD *(placeholder)*

## 📌 Claims (con caveat)

- **quando-cot-non-aiuta** — CoT su task triviali può peggiorare *(placeholder)*

## 🗺 Mappa concettuale (gerarchia)

In un run reale, questa sezione conterrebbe la gerarchia con wikilink:

```
modello-come-collega-cooperativo (mental model di base)
       ↓
prompt-come-interfaccia (framing)
       ↓
prompt-come-codice-versionare-testare (operatività)
       ├─→ [[few-shot-prompting]] ← in-context-learning
       ├─→ chain-of-thought-cot → self-consistency
       │            ↓ caveat
       │     quando-cot-non-aiuta
       ├─→ structured-output ← delimiters
       └─→ AVOID:
            istruzioni-vaghe
            prompt-giganti-lost-in-the-middle
```

## 📖 Source

- [[_meta/source]] — info sul workshop originale *(placeholder)*
- [[_meta/import-log]] — log di questo import generato da Forge *(placeholder)*
