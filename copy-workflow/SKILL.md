# Copy-Workflow — Orchestration Layer Completo
> Sistema multi-agente per la produzione di copy persuasivo professionale basato sul framework APSOC

---

## Invocazione

```
/copywriting [modalità] [opzioni]
```

### Modalità disponibili

| Comando | Cosa fa |
|---|---|
| `/copywriting full` | Pipeline completo: briefing → ricerca → APSOC → QA → copy finale |
| `/copywriting ad` | Ad copy rapida (Facebook/Instagram/TikTok/Google) — 3 varianti |
| `/copywriting sales-page` | Sales page completa (1000–5000 parole) — score ≥85 |
| `/copywriting email` | Sequenza email marketing (welcome, nurture, launch) |
| `/copywriting vsl` | Script VSL 8-20 min — hook + APSOC + stack valore + CTA |
| `/copywriting social` | 5 post social (IG/FB/LinkedIn) in sequenza strategica |
| `/copywriting headline` | Genera 10+ headline con formule APSOC |
| `/copywriting objections` | Gestisci obiezioni con CPB (Claim, Proof, Benefit) |
| `/copywriting avatar` | Crea buyer persona / avatar completo |
| `/copywriting funnel` | Progetta funnel strategico |
| `/copywriting review` | Revisione copy esistente con checklist APSOC |

Invocazione naturale: descrivi cosa vuoi scrivere e il sistema sceglie la modalità.

---

## Il Team (8 Agenti Specializzati)

```
ORCHESTRATORE MASTER
        │
        ├── FASE 1: STRATEGIA
        │   ├── A1 — Briefing Analyst        (analisi briefing + obiettivi)
        │   └── A2 — Target Analyst          (ricerca + avatar buyer persona)
        │
        ├── FASE 2: SCRITTURA APSOC (sequenziale)
        │   ├── A3 — Attention Writer        (headline + hook + apertura)
        │   ├── A4 — Problem Writer          (pain point + conseguenze)
        │   ├── A5 — Solution Writer         (USP + vantaggi + post-acquisto)
        │   ├── A6 — Objections Handler      (CPB: Claim + Proof + Benefit)
        │   └── A7 — CTA Writer              (call to action profonde)
        │
        └── FASE 3: QA
            └── A8 — Copy Reviewer           (APSOC validator + checklist)
```

---

## Framework APSOC (Il DNA del Sistema)

Ogni output di questo sistema segue la struttura APSOC:

| Step | Funzione | Regola |
|---|---|---|
| **A** — Attenzione | Cattura l'attenzione, vendi la lettura | Prima di tutto il resto |
| **P** — Problema | Descrivi il pain point meglio del target | SEMPRE prima della soluzione |
| **S** — Soluzione | Presenta il prodotto + USP | Solo DOPO il problema |
| **O** — Obiezioni | CPB: gestisci dubbi e resistenze | In ordine di importanza |
| **C** — CTA | Chiama all'azione in modo chiaro | Profondo > superficiale |

**Regola aurea**: Prima il problema, poi la soluzione. Sempre.

---

## Come Risponde il Sistema

### Trigger naturali

Il sistema si attiva quando senti queste frasi:
- "devo scrivere un'ad per..."
- "ho bisogno di una sales page..."
- "scrivi un'email di lancio per..."
- "migliora il mio copy..."
- "non so come gestire l'obiezione del prezzo..."
- "crea il profilo del mio cliente ideale..."
- "come struttura il funnel per..."
- "genera headline per..."

### Decision tree iniziale

```
Hai un prodotto/servizio specifico?
├── Sì → Hai già un briefing?
│         ├── Sì → Vai a Fase 2 (skip A1)
│         └── No → Spawna A1 (Briefing Analyst)
└── No → Chiedi: "Descrivi il prodotto che vuoi vendere"

Hai definito il target?
├── Sì → Hai già l'avatar?
│         ├── Sì → Vai a Fase 2 (skip A2)
│         └── No → Spawna A2 (Target Analyst)
└── No → Spawna A2 (Target Analyst)
```

---

## Struttura File del Sistema

```
copy-workflow/
├── SKILL.md                          ← questo file (entry point)
├── orchestrators/
│   └── copy-master.md                ← orchestratore principale
├── agents/
│   ├── research/
│   │   ├── briefing-analyst.md       ← A1
│   │   └── target-analyst.md         ← A2
│   ├── apsoc/
│   │   ├── attention-writer.md       ← A3
│   │   ├── problem-writer.md         ← A4
│   │   ├── solution-writer.md        ← A5
│   │   ├── objections-handler.md     ← A6
│   │   └── cta-writer.md             ← A7
│   └── qa/
│       └── copy-reviewer.md          ← A8
├── skills/
│   ├── apsoc-builder/SKILL.md        ← Full APSOC generation
│   ├── target-avatar/SKILL.md        ← Buyer persona builder
│   ├── headline-forge/SKILL.md       ← Headline formulas
│   ├── objections-forge/SKILL.md     ← CPB objections
│   ├── funnel-designer/SKILL.md      ← Funnel strategy
│   └── copy-review/SKILL.md          ← QA checklist
├── workflows/
│   ├── full-copy-workflow.md         ← Pipeline completo
│   ├── quick-ad-workflow.md          ← Ad copy rapida
│   ├── sales-page-workflow.md        ← Sales page
│   ├── email-sequence-workflow.md    ← Email sequence
│   ├── vsl-workflow.md               ← Script VSL 8-20 min
│   └── social-post-workflow.md       ← 5 post social in sequenza
├── templates/
│   ├── briefing-template.md          ← Standard briefing
│   ├── avatar-template.md            ← Buyer persona
│   ├── copy-checklist.md             ← APSOC QA checklist
│   └── cpb-template.md               ← CPB objections template
├── references/
│   ├── concepts/
│   │   ├── copy-psychology.md        ← Trigger emotivi e bias cognitivi
│   │   └── apsoc-advanced.md         ← Pattern avanzati, varianti, eccezioni
│   ├── conventions/
│   │   └── anti-patterns.md          ← 15 errori che distruggono il copy
│   └── patterns/
│       └── industry-specific.md      ← Adattamenti per settore (B2B, info-product, e-commerce...)
├── assets/
│   └── examples/
│       └── corso-online.md           ← Esempio end-to-end annotato
└── evals/
    └── evals.json                    ← 8 scenari di test realistici
```

---

## Routing Rapido alle Reference

| Se hai bisogno di... | File |
|---|---|
| Capire perché le persone comprano (trigger emotivi) | `references/concepts/copy-psychology.md` |
| Pattern avanzati APSOC, varianti, eccezioni strategiche | `references/concepts/apsoc-advanced.md` |
| Lista errori da evitare (usabile in A3-A8) | `references/conventions/anti-patterns.md` |
| Adattare il copy per B2B / info-product / e-commerce / coaching | `references/patterns/industry-specific.md` |
| Vedere un esempio completo end-to-end | `assets/examples/corso-online.md` |
| Testare il sistema con scenari realistici | `evals/evals.json` |

---

## Principi Non Negoziabili

1. **Le persone comprano con le emozioni e giustificano con la logica.** Ogni copy deve avere una componente emotiva.
2. **Prima il problema, poi la soluzione.** Sempre. Senza eccezioni (salvo strategiche documentate).
3. **Show, don't tell.** Non dire "questo ti farà sentire X", mostralo con una storia.
4. **Il target non sei tu.** Dimentica le tue preferenze. Parla come parla il target.
5. **Ogni parola ha uno scopo.** Se non puoi giustificare strategicamente una parola, eliminala.
6. **Gestisci le obiezioni che generi.** Se scrivi qualcosa che potrebbe generare un dubbio, gestiscilo.

---

## Istruzione per il Conductor

Leggi `orchestrators/copy-master.md` prima di procedere.
Spawna gli agenti secondo la fase corrente del run.
Parla all'utente in italiano (o nella lingua dell'utente).
