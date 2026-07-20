# `assets/examples/` — Esempi end-to-end per ogni target

> Esempi realistici di cosa producono i builder (B1-B8) partendo da un sorgente comune.
> Usati come **reference visiva** per i builder ("ecco com'è fatto un buon output") e per debugging.

## Struttura

```
examples/
├── _shared/                          # input comune a tutti gli esempi
│   ├── source.md                     # transcript finto "Prompt Engineering Avanzato"
│   ├── kg.json                       # KG simulato (12 atomi, 3 cluster)
│   └── master.md                     # MKD simulato (output di Stage 4)
├── doc/                              # output di B1 doc-builder
├── agent/                            # output di B2 agent-builder
├── team/                             # output di B3 team-builder
├── skill/                            # output di B4 skill-builder (meta!)
├── workflow/                         # output di B5 workflow-builder
├── orchestration/                    # output di B6 orchestration-builder
├── wiki/                             # output di B7 wiki-builder (Obsidian)
└── custom/                           # output di B8 custom-builder (system prompt injection)
```

## Come leggerli

Ogni cartella `<target>/` ha:
- `README.md` — descrive input ASK, output prodotto, scelte di design, stats
- File canonici del target (variano)

Apri prima il `README.md` per il contesto, poi i file specifici per vedere la "forma".

## Source comune

Tutti gli esempi partono dallo **stesso sorgente** (`_shared/source.md` ~720 parole) per:
- Confronto diretto: cosa cambia tra un `doc` e una `wiki` dello stesso contenuto?
- Ridotta complessità di lettura: una volta che hai il modello mentale del contenuto, vedi solo le differenze di forma
- Coverage controllabile: 12 atomi nel KG → tracciabili attraverso ogni target

## Per i builder agents

Quando spawnati, i builder leggono questi esempi come **reference** prima di costruire l'output reale. Il pattern di esempio non è da copiare ciecamente — è da capire come modello di "forma canonica" e adattare al sorgente reale.

## Note di onestà

Questi esempi sono **simulati** (non frutto di un run reale di Forge end-to-end). Servono come reference architetturale. In Phase 7 (test end-to-end reali) verrà fatto un run su sorgente reale e si confronterà l'output con questi esempi.
