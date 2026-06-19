---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #copywriting #apsoc #pipeline #namespace #gate #L2.1
Created: 2026-06-18
Last updated: 2026-06-18
---

# ARCHITETTURA — L2.1 Copywriting

> **Ecosistema:** 04-MARKETING · **Standard:** CF-grade · **ADR-003:** il motore esiste, non si riscrive.

---

## 1. Gerarchia del reparto

```
L1 04-MARKETING (MKT-Conductor)
  └── L2.1 COPYWRITING (COPY-MASTER — coordinator, router decisionale)
        ├── Ricerca
        │   ├── A1 Briefing Analyst (sonnet)
        │   └── A2 Target Analyst (sonnet)
        ├── Scrittura APSOC
        │   ├── A3 Attention Writer (opus)   ← headline + hook, 9 strategie
        │   ├── A4 Problem Writer (opus)     ← dolore amplificato, NO prodotto
        │   ├── A5 Solution Writer (opus)    ← USP + benefit + visione; P PRIMA di S
        │   ├── A6 Objections Handler (sonnet) ← CPB per 10 tipi canonici
        │   └── A7 CTA Writer (opus)         ← CTA profondo, no scarcity falsa
        └── QA / Gate
            ├── A8 Copy Reviewer (opus, verifier)     ← score 100pt, GATE G1
            └── COPY-QA-LEAD (opus, verifier) [NUOVO] ← supervisore gate, decisore iterazioni
```

Agenti strategici prestati a altri reparti (definiti nel motore, registrati qui):
- `S1` Funnel Strategist (sonnet) → presta a L2.6
- `S2` Positioning Strategist (sonnet) → presta a L2.5
- `S3` Campaign Strategist (sonnet) → presta a L2.2

---

## 2. Pipeline operativa — A1 → A8

```
Contratto in ingresso
  │
  ▼
COPY-MASTER (router)
  ├── ha icp? ─── NO → spawna A2 prima ──────┐
  │                                          │
  ├── ha awareness_level? ─── NO → deduce ───┤
  │                                          ▼
  └── sceglie workflow ────────────────> A1 Briefing
                                          │
                                          ▼
                                         A2 Target (se necessario)
                                          │
                                          ▼
                                         A3 Attention (headline + hook)
                                          │
                                          ▼
                                         A4 Problem (dolore amplificato)
                                          │
                                      [P PRIMA di S — Art.4.2 — INVIOLABILE]
                                          │
                                          ▼
                                         A5 Solution (USP + benefit)
                                          │
                                          ▼
                                         A6 Objections (CPB per obiezione)
                                          │
                                          ▼
                                         A7 CTA (chiusura + urgenza reale)
                                          │
                                          ▼
                                         A8 Copy Reviewer (score 100pt)
                                          │
                               ┌──────────┴──────────┐
                               ▼                     ▼
                          score ≥80/85           score < soglia
                          GATE PASS              GATE BLOCCA
                               │                     │
                               │              COPY-QA-LEAD decide:
                               │              fix mirato vs rifacimento
                               ▼
                         Output gated al committente
```

**Regola P prima di S (Art.4.2 Mandato):** se la soluzione compare prima del problema, il
score A8 perde automaticamente -15 punti. Questa regola non è soggetta a discrezione.

---

## 3. Gate G1 — Schema di scoring A8

| Score | Verdetto | Azione |
|---|---|---|
| ≥ 90 | Eccellente | Rilascia senza modifiche |
| 80-89 | Buono | Ritocchi minori; COPY-QA-LEAD decide se passare |
| 70-79 | Accettabile | Rivedi 1-2 sezioni; non si rilascia |
| 60-69 | Insufficiente | Revisione sostanziale; COPY-QA-LEAD valuta rifacimento |
| < 60 | Bocciato | Rifacimento da capo |

**Gate standard: ≥80. Sales page: ≥85. Entrambi BLOCCANTI — non bypassabili.**

Violazione automatica -15pt: S appare prima di P.
Violazione automatica: scarcity falsa in CTA (Art.2.3 Mandato).

---

## 4. Wrapper di handoff — contratto I/O del reparto

**Input (dal committente a COPY-MASTER):**
```json
{
  "committente": "01-AGENCY",
  "formato": "landing",
  "awareness_level": "problem-aware",
  "icp": "marketing/avatars/consulente-finanziario-nord-italia",
  "obiettivo": "opt-in per demo gratuita",
  "deadline": "2026-06-25",
  "brand_kit": "DE",
  "materiali": "path/al/briefing.md",
  "vincoli": "max 400 parole, no testimonials clienti reali senza consenso"
}
```

**Output (da A8 / COPY-QA-LEAD al committente):**
```json
{
  "copy_finale": "path/al/copy-finale.md",
  "score_APSOC": 84,
  "qa_report": "path/al/qa-report.md",
  "brand_gate": "PASS",
  "gate_g1": "PASS",
  "pattern_usati": ["barnum-nicchia", "cta-micro-commitment"],
  "workflow_eseguito": "WF-COPY-FULL",
  "iterazioni": 1,
  "note_copy_qa_lead": "prima iterazione sufficiente; 2 punti recuperati su P-amplification"
}
```

---

## 5. Namespace memoria — marketing/copy/...

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `marketing/copy/patterns/{icp}` | Pattern copy ad alto score per ICP | A8 + AN4 (L2.4) |
| `marketing/copy/antipatterns/{icp}` | Pattern che abbassano il score per ICP | A8 + COPY-QA-LEAD |
| `marketing/copy/scores/{formato}` | Storico score per formato | A8 |
| `marketing/avatars/{icp}` | Avatar + pain map + language map | A2 |

Nota: lo stato runtime del motore (sessioni copy in corso) resta nel motore esistente in
`SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/`. Il layer memoria del reparto qui
sopra è il layer di registrazione e learning — non duplica il motore.

---

## 6. Routing APSOC per awareness_level (T-AWARENESS-ROUTER)

| Awareness level | Dosaggio APSOC consigliato |
|---|---|
| `unaware` | A pesante (lunga attenzione), P amplissimo (educazione al dolore), S breve, O media, C morbida |
| `problem-aware` | A media, P forte, S media con proof, O robusta, C chiara |
| `solution-aware` | A breve, P accennato, S molto dettagliata con differenziatori, O completa, C urgente |
| `product-aware` | A quasi assente, P minimo, S con dettagli tecnici + garanzie, O risolutiva, C diretta |
| `most-aware` | Offerta diretta + proof + CTA aggressiva — A/P minimali |

Il routing è deterministico: COPY-MASTER applica questa tabella e dichiara il dosaggio
nel briefing prima che A3 cominci. Il dosaggio non è opinione — è parte del contratto.

---

## 7. Namespace script e invocazione del motore

Il motore si invoca tramite le skill esistenti:
- `/copywriting full` → WF-COPY-FULL (A1→A8, 60-120 min)
- `/copywriting ad` → WF-COPY-AD (15-20 min, 3 varianti)
- `/copywriting sales-page` → WF-COPY-SALES-PAGE (90-120 min, gate ≥85)
- `/copywriting email` → WF-COPY-EMAIL (sequenza email)
- `/copywriting review` → T-REVIEW (score su copy esistente)
- `/copywriting avatar` → T-AVATAR (buyer persona → namespace memoria)

I wrapper di invocazione dei workflow di reparto v2 vivono in `scripts/README.md`.

---

## Connessioni

- [[Tool_Copy_Workflow_Orchestration]] · `second-brain-vault/wiki/tools/Tool_Copy_Workflow_Orchestration.md`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.1`
- [[ADR-003]] · `company/Memory/decisions/ADR-003-migrazione-wrap-non-riscrittura.md`
