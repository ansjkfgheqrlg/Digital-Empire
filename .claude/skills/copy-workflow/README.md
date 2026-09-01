# Copy-Workflow — Sistema Multi-Agente di Copywriting Persuasivo

Sistema completo per la produzione di copy professionale basato sul framework **APSOC** (Attenzione → Problema → Soluzione → Obiezioni → CTA).

## Come si attiva

Invocazione esplicita:
```
/copywriting [modalità]
```

Invocazione naturale — il sistema si attiva quando senti:
- "devo scrivere un'ad per..."
- "ho bisogno di una sales page per..."
- "scrivi la sequenza email per il lancio di..."
- "migliora questo copy..."
- "non so come gestire l'obiezione del prezzo"
- "genera headline per..."
- "crea il profilo del mio cliente ideale"

---

## Modalità Disponibili

| Comando | Output | Agenti | Durata |
|---|---|---|---|
| `/copywriting full` | Copy completo + QA report | A1-A8 | 60-120 min |
| `/copywriting ad` | 3 varianti ad (FB/IG/TikTok/Google) | A1 lite, A2 lite, A3, A4, A7 | 15-20 min |
| `/copywriting sales-page` | Sales page 1000-5000 parole | A1-A8, score ≥85 | 90-120 min |
| `/copywriting email` | Sequenza email completa | A1-A8 | 45-90 min |
| `/copywriting vsl` | Script VSL 8-20 min | A1-A8 + struttura video | 60-90 min |
| `/copywriting social` | 5 post social (IG/FB/LinkedIn) | A1 lite, A2 lite, A3, A4, A7 | 20-30 min |
| `/copywriting headline` | 10+ headline con formule | headline-forge skill | 10 min |
| `/copywriting objections` | CPB per obiezioni specifiche | objections-forge skill | 10-15 min |
| `/copywriting avatar` | Buyer persona completo | target-avatar skill | 15-20 min |
| `/copywriting funnel` | Piano funnel strategico | funnel-designer skill | 20-30 min |
| `/copywriting review` | Revisione copy esistente + score | copy-review skill | 10-20 min |

---

## Il Framework APSOC

Il DNA del sistema. Ogni copy segue questa struttura:

```
A → Attenzione   Cattura. Vendi la lettura, non il prodotto.
P → Problema     Prima il problema. Sempre. Nessuna eccezione.
S → Soluzione    Il prodotto come risposta naturale al problema.
O → Obiezioni    Anticipa i dubbi. Gestiscili con CPB.
C → CTA          Chiama all'azione. Profondo > superficiale.
```

**Regola assoluta**: P sempre prima di S. Violarla è l'errore più costoso del copy.

---

## Struttura File

```
copy-workflow/
├── SKILL.md                          ← Entry point + routing
├── README.md                         ← Questo file
├── note-strategiche.md               ← Decisioni architetturali
├── orchestrators/
│   └── copy-master.md                ← Orchestratore + state management
├── agents/
│   ├── research/
│   │   ├── briefing-analyst.md       ← A1 — Dati critici + USP + funnel
│   │   └── target-analyst.md         ← A2 — Avatar + pain points + language map
│   ├── apsoc/
│   │   ├── attention-writer.md       ← A3 — Headline + hook (9 strategie)
│   │   ├── problem-writer.md         ← A4 — Pain point amplificato (6 strategie)
│   │   ├── solution-writer.md        ← A5 — USP + benefits + post-acquisto
│   │   ├── objections-handler.md     ← A6 — CPB (Claim + Proof + Benefit)
│   │   └── cta-writer.md             ← A7 — CTA profondo + urgenza
│   └── qa/
│       └── copy-reviewer.md          ← A8 — Assemblaggio + score /100
├── skills/
│   ├── apsoc-builder/SKILL.md        ← Full APSOC interattivo
│   ├── target-avatar/SKILL.md        ← Buyer persona
│   ├── headline-forge/SKILL.md       ← 10+ headline con formule
│   ├── objections-forge/SKILL.md     ← CPB per obiezioni specifiche
│   ├── funnel-designer/SKILL.md      ← Piano funnel strategico
│   └── copy-review/SKILL.md          ← Revisione copy esistente
├── workflows/
│   ├── full-copy-workflow.md         ← Pipeline completo (A1-A8)
│   ├── quick-ad-workflow.md          ← Ad copy rapida
│   ├── sales-page-workflow.md        ← Sales page completa
│   ├── email-sequence-workflow.md    ← Sequenze email
│   ├── vsl-workflow.md               ← Script VSL
│   └── social-post-workflow.md       ← Post social media
├── references/
│   ├── concepts/
│   │   ├── copy-psychology.md        ← Trigger emotivi, bias cognitivi nel copy
│   │   └── apsoc-advanced.md         ← APSOC avanzato: pattern, varianti, eccezioni
│   ├── conventions/
│   │   └── anti-patterns.md          ← 15 errori che distruggono il copy
│   └── patterns/
│       └── industry-specific.md      ← Adattamenti per settore (B2B, info-product, ecc.)
├── assets/
│   ├── templates/
│   │   ├── briefing-template.md      ← Da compilare prima del pipeline
│   │   ├── avatar-template.md        ← Buyer persona template
│   │   ├── copy-checklist.md         ← APSOC QA checklist /100
│   │   └── cpb-template.md           ← Template gestione obiezioni
│   └── examples/
│       └── corso-online.md           ← Esempio end-to-end annotato
└── evals/
    └── evals.json                    ← 8 scenari di test realistici
```

---

## Principi Non Negoziabili

1. **Prima il problema, poi la soluzione.** Sempre. Nessuna eccezione strategica valida.
2. **Parla il linguaggio del target.** Non del marketer. La language map è sacra.
3. **Show, don't tell.** Non "ha un problema", ma "sono le 23 e il cursore lampeggia su uno schermo bianco."
4. **Il CTA è profondo.** Non "compra ora", ma "smetti di [pain point] — inizia [risultato specifico]."
5. **Le obiezioni si anticipano.** Non si aspetta che il target le pensi in silenzio.
6. **Ogni parola ha uno scopo.** Se non sai perché c'è, toglila.

---

## Quando NON usare questo sistema

- Copy puramente SEO-tecnico (meta description, alt text): usa strumenti dedicati
- Traduzioni di copy esistenti: traduzione diretta, no pipeline
- Copy ultra-breve (tagline da 3 parole): risposta diretta senza pipeline
- Descrizioni di prodotto puramente informative senza obiettivo di vendita

---

## Origine

Costruito con `content-forge` da **Il Manuale del Copywriting v1.1** (115 pagine, ~22.700 parole).
KG: 73 atomi in 9 cluster — APSOC, CPB, amplificazione dolore, headline, CTA, funnel, email, avatar, anti-pattern.
Build: 2026-05-26.



## Il pipeline completo — step per step


Tu scrivi: "/copywriting full — corso online €297 per freelance"
                              │
                    Copy-Master si attiva
                              │
            ┌─────────────────┴──────────────────┐
            │           FASE 1 — STRATEGIA       │
            │                                    │
            │  A1 Briefing Analyst               │
            │  → estrae prodotto, prezzo,        │
            │    obiettivo, tipo copy            │
            │  → produce: briefing-completo.md   │
            │                                    │
            │  A2 Target Analyst  (in parallelo) │
            │  → costruisce avatar, pain points, │
            │    language map (le parole esatte  │
            │    del target)                     │
            └─────────────────┬──────────────────┘
                              │
            ┌─────────────────┴──────────────────┐
            │         FASE 2 — SCRITTURA         │
            │         (sequenziale — ognuno      │
            │          riceve l'output del       │
            │          precedente come input)    │
            │                                    │
            │  A3 → scrive Attenzione + headline │
            │  A4 → scrive Problema (riceve A3)  │
            │  A5 → scrive Soluzione (riceve A4) │
            │  A6 → scrive Obiezioni (riceve A5) │
            │  A7 → scrive CTA (riceve tutto)    │
            └─────────────────┬──────────────────┘
                              │
            ┌─────────────────┴──────────────────┐
            │           FASE 3 — QA              │
            │                                    │
            │  A8 Copy Reviewer                  │
            │  → assembla tutte le sezioni       │
            │  → score su 100 (APSOC checklist)  │
            │  → se score < 80: rilancia         │
            │    l'agente problematico           │
            │  → se score ≥ 80: consegna         │
            └─────────────────┬──────────────────┘
                              │
                    Tu ricevi:
                    copy-finale.md + qa-report.md
