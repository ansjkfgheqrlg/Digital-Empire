---
title: Few-shot prompting
aliases:
  - few-shot
  - few shot
  - n-shot prompting
tags:
  - area/ai/prompting
  - source/forge-import-2026-05
  - status/seedling
created: 2026-05-23
source: "[[_meta/source]]"
forge_atom_id: a-002
---

# Few-shot prompting

## Definizione canonica

Dare al modello 2-5 esempi di input/output prima della richiesta vera, per fargli apprendere il pattern da replicare.

## Spiegazione estesa

Few-shot sfrutta l'[[in-context-learning]]: il modello fa pattern recognition sugli esempi del prompt e replica il pattern sul nuovo input. Non è apprendimento permanente — solo runtime.

Funziona meglio quando gli esempi sono **rappresentativi e diversi tra loro**, non tutti uguali. L'omogeneità degli esempi causa overfitting all'esempio; la diversità forza generalizzazione.

## Esempio (sorgente)

> Commit message in formato Conventional Commits con 3 esempi tipo "Added user login" → "feat(auth): implement user login".

## ➕ Esempio aggiuntivo

Classificazione del sentiment con 4 esempi mixati (positive/negative/neutral/sarcastico) prima del testo da classificare. La diversità fa generalizzare; tutti positivi farebbero il modello biased a vedere positivo ovunque.

## Schema

```
[Esempio 1: input → output]
[Esempio 2: input → output]
[Esempio 3: input → output]
[Vero input] → ?
```

## Connessioni

- Prerequisito: [[in-context-learning]] (meccanismo che lo fa funzionare)
- Sibling: [[chain-of-thought-cot]] (altra tecnica core)
- Anti-pattern collegato: [[istruzioni-vaghe]] (few-shot è l'alternativa alle istruzioni vaghe)
- Applicato in: [[structured-output]] (esempi sono fondamentali per output JSON)

## Domande aperte

- Quanti esempi è "troppi"? (limit pratico: lost-in-the-middle a >10 esempi)
- Come scegliere ESEMPI rappresentativi vs. random sample del dataset?
- Few-shot vince ancora con modelli istruiti (es. claude-sonnet-4) o è obsoleto?

## Riferimenti

- Source: [[_meta/source]] § Tecniche core (00:01:15)
