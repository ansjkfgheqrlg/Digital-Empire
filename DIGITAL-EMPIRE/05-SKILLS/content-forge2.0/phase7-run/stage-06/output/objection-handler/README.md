# objection-handler — Skill ufficiale

> Skill specializzata nella gestione delle obiezioni del prospect in copy persuasivo.
> Basata sul Manuale 4 della strategia APSOC.

## Installazione

Copia questa cartella in `~/.claude/skills/` (o equivalente per il tuo ambiente).

```bash
cp -r objection-handler ~/.claude/skills/
```

## Come usarla

Triggera naturalmente quando scrivi o rivedi copy persuasivo. Esempi:

- "Ho questa sales page, perché non converte?"
- "Come gestisco l'obiezione 'il prezzo è troppo alto'?"
- "Voglio strutturare la sezione obiezioni di una landing"
- "Audit del mio copy per obiezioni mancanti"

Oppure invoca esplicitamente con `/obj` (se hai configurato l'alias).

## Cosa fa

1. Identifica le **11 categorie** di obiezioni nel tuo copy / contesto
2. Le priorizza dalla più forte alla più debole
3. Applica il **framework CPB** (Claim-Proof-Benefit)
4. Sceglie le prove giuste dal **catalogo di 8 tecniche** (prima&dopo, bandwagon, processi logici, showoff, garanzie, menzioni media, recensioni, studi)
5. Marca le tecniche **borderline etiche** in modo trasparente

## Struttura della skill

```
objection-handler/
├── SKILL.md                                  # kernel
├── references/
│   ├── categorie-obiezioni.md               # tassonomia 11 categorie
│   ├── catalogo-prove.md                    # 8 tecniche + combinazioni
│   ├── processes/
│   │   └── cpb-workflow.md                  # workflow 4 step + esempio end-to-end
│   ├── patterns/
│   │   └── showoff-templates.md             # 7 template riusabili
│   └── conventions/
│       └── etica-prove.md                   # quando una prova è borderline
├── evals/
│   └── evals.json                           # 6 test cases
└── README.md
```

## Generata da

`content-forge` (Phase 7 reale, 24 maggio 2026) dal Manuale 4 della strategia APSOC.

Coverage atomi sorgente: 17/18 (94%) — vedi `coverage-report.json` allegato nel deliverable Forge.

## Gap noti

- Le altre lettere di APSOC (A, P, S, C) non sono incluse — questa skill copre solo "O".
- Manuale 8 (direct response) citato nei processi logici non è incluso.
