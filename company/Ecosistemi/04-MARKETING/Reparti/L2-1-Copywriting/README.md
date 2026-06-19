---
Type: REPARTO
Status: Active
Tags: #reparto #marketing #copywriting #apsoc #copy-workflow #L2.1 #priorita-assoluta
Created: 2026-06-18
Last updated: 2026-06-18
---

# L2.1 — Copywriting

> **Ecosistema:** 04-MARKETING · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.1`
> **Standard:** CF-grade (ADR-007) · **PRIORITÀ ASSOLUTA** dell'ecosistema Marketing e della holding intera.

---

## Missione

Produrre ogni copy di conversione di EMPIRE OS via framework **APSOC + CPB**, con QA a 100 punti
e gate bloccante. Ogni parola che esce da questo reparto con obiettivo di generare un'azione
misurabile deve superare lo score A8 ≥80 (≥85 sales page) e il brand gate G2. Senza gate,
l'output non viene rilasciato — questa regola non ha eccezioni (Mandato Art.4).

**Confine netto:**
- L2.1 NON produce contenuti editoriali (→ 03-CONTENT-FACTORY).
- L2.1 NON gestisce il cold outreach operativo (il writer.py vive in 01-AGENCY; L2.1 fa QA/evoluzione dei template cold via T-REVIEW).
- L2.1 NON implementa landing page (→ 06-PLATFORM).
- L2.1 NON disegna architetture funnel (→ L2.6 Conversion Architecture).

---

## Motore esistente — ADR-003 (wrap, non riscrittura)

Questo reparto **ingloba come motore operativo il Copy Workflow Orchestration Layer esistente**
in `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/`. Quel sistema — COPY-MASTER, A1-A8,
S1-S3, 6 workflow, template, sub-skill — è **ATTIVO e non si tocca** (ADR-003: wrap, mai riscrittura).

Il reparto L2.1-Copywriting è il **wrapper di registrazione v2**: registra il motore
nell'organigramma V2, ne definisce i contratti di handoff verso il resto della holding, e aggiunge
il livello di supervisione CF-grade (COPY-QA-LEAD, namespace, KPI, state). Il motore esegue;
il reparto governa e contabilizza.

**Dove vivono i file del motore:**
```
SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/
├── SKILL.md                          ← entry point, invoca con /copywriting [mode]
├── orchestrators/copy-master.md      ← COPY-MASTER (coordinator)
├── agents/research/                  ← A1, A2
├── agents/apsoc/                     ← A3, A4, A5, A6, A7
├── agents/qa/                        ← A8
├── skills/                           ← 6 sub-skill
├── workflows/                        ← 4 workflow core
└── templates/                        ← briefing, avatar, checklist, cpb
```

**Dove vive la struttura di reparto v2 (questo wrapper):**
```
company/Ecosistemi/04-MARKETING/Reparti/L2-1-Copywriting/
├── README.md              ← questo file
├── ARCHITETTURA.md        ← gerarchia, pipeline, namespace, gate
├── agenti/                ← 10 schede wrapper CF-grade + 1 nuovo (COPY-QA-LEAD)
├── workflow/              ← 6 workflow CF-grade
├── principi/              ← principi operativi
├── regole/                ← regole non negoziabili
├── skills/                ← mapping skill
├── scripts/               ← wrapper invocazione + script deterministici
├── kpi/                   ← KPI del reparto
└── state/                 ← namespace e schema memoria
```

---

## Roster del reparto (10 agenti)

| ID | Agente | File | Tipo | Tier | Motore |
|---|---|---|---|---|---|
| `COPY-MASTER` | Copy Master | `agenti/copy-master.md` | coordinator | opus | **Esistente** — wrapper v2 |
| `A1` | Briefing Analyst | `agenti/a1-briefing-analyst.md` | worker | sonnet | **Esistente** — wrapper v2 |
| `A2` | Target Analyst | `agenti/a2-target-analyst.md` | worker | sonnet | **Esistente** — wrapper v2 |
| `A3` | Attention Writer | `agenti/a3-attention-writer.md` | worker | opus | **Esistente** — wrapper v2 |
| `A4` | Problem Writer | `agenti/a4-problem-writer.md` | worker | opus | **Esistente** — wrapper v2 |
| `A5` | Solution Writer | `agenti/a5-solution-writer.md` | worker | opus | **Esistente** — wrapper v2 |
| `A6` | Objections Handler | `agenti/a6-objections-handler.md` | worker | sonnet | **Esistente** — wrapper v2 |
| `A7` | CTA Writer | `agenti/a7-cta-writer.md` | worker | opus | **Esistente** — wrapper v2 |
| `A8` | Copy Reviewer | `agenti/a8-copy-reviewer.md` | verifier | opus | **Esistente** — wrapper v2 |
| `COPY-QA-LEAD` | Copy QA Lead | `agenti/copy-qa-lead.md` | verifier | opus | **NUOVO v2** |

---

## Workflow del reparto (6 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-COPY-FULL** | `workflow/WF-COPY-FULL.md` | Pipeline A1→A8 per copy complesso | A8 ≥80 + G2 brand gate + G4 contract |
| **WF-COPY-AD** | `workflow/WF-COPY-AD.md` | 3+ varianti APSOC per ads (15-20 min) | A8 ≥80 ogni variante + G3 compliance |
| **WF-COPY-SALES-PAGE** | `workflow/WF-COPY-SALES-PAGE.md` | Sales page completa con sezioni APSOC | A8 ≥85 + P prima di S + G2 + G4 |
| **WF-COPY-EMAIL** | `workflow/WF-COPY-EMAIL.md` | Sequenze email APSOC (coord L2.3) | A8 ≥80 + deliverability check E2 |
| **WF-COPY-VSL** | `workflow/WF-COPY-VSL.md` | Script VSL 8-20 min strutturato | A8 ≥80 + timing check + G2 |
| **WF-COPY-SOCIAL** | `workflow/WF-COPY-SOCIAL.md` | 5 post in sequenza strategica | A8 ≥80 + brand gate + pattern library |

---

## Contratto di richiesta copy (handoff standard)

Ogni committente apre una richiesta con questo schema (da `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §1.2`):

```json
{
  "committente": "01-AGENCY | 02-INFO | 03-CF | 05-MB | 04-MKT",
  "formato": "ad | sales-page | email-seq | cold-email | landing | vsl | social | headline | listing | proposta | review",
  "awareness_level": "unaware | problem-aware | solution-aware | product-aware | most-aware",
  "icp": "riferimento ICP/avatar (id namespace o brief inline)",
  "obiettivo": "azione misurabile attesa",
  "deadline": "YYYY-MM-DD"
}
```

Risposta standard: `{copy_finale, score_APSOC, qa_report, brand_gate, pattern_usati, workflow_eseguito}`.

Regola: nessun ecosistema scrive copy di conversione in autonomia — il gate APSOC vive qui.

---

## KPI del reparto

| KPI | Owner | Definizione |
|---|---|---|
| First-pass rate G1 | COPY-QA-LEAD | % copy che superano A8 al primo tentativo (per formato) |
| Time-to-copy | COPY-MASTER | Minuti dal contratto in ingresso al copy gated in uscita |
| Score APSOC medio | A8 | Media score per formato nel periodo; [DM] baseline al primo ciclo |
| Pattern ad alto score | A8 + COPY-QA-LEAD | Pattern ICP per ICP in `marketing/copy/patterns/{icp}` |

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | 01-AGENCY | Brief proposta/cold-email/landing offerta |
| ← riceve da | 02-INFO-BUSINESS | Brief lancio: sales page, VSL, email lancio |
| ← riceve da | 03-CONTENT-FACTORY | Brief hook, headline, CTA conversione |
| ← riceve da | 05-MULTI-BUSINESS | Brief titoli YT, listing KDP |
| → consegna a | L2.2 Advertising | Copy ads gated per WF-ADS-CAMPAIGN |
| → consegna a | L2.3 Email & Lifecycle | Copy email gated per sequenze lifecycle |
| → consegna a | L2.6 Conversion Architecture | Copy per stage funnel |
| → consegna a | L2.5 Brand & Creative Strategy | Check brand_kit su richiesta BR-QA |

---

## Escalation

- Copy che fallisce A8 ≥2 iterazioni → COPY-QA-LEAD decide: fix mirato vs rifacimento totale.
- Richiesta senza `icp` → COPY-MASTER spawna A2 Target Analyst prima di qualsiasi scrittura.
- Richiesta senza `awareness_level` → COPY-MASTER la deduce e la dichiara nel payload (mai implicita).
- Score A8 sistematicamente basso su un ICP → COPY-QA-LEAD segnala a MKT-Conductor: pattern a rischio.
- Qualsiasi pressione a bypassare il gate → COPY-QA-LEAD rifiuta; documenta la pressione.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.1`
- [[Tool_Copy_Workflow_Orchestration]] · `second-brain-vault/wiki/tools/Tool_Copy_Workflow_Orchestration.md`
- [[Framework_Cold_Outreach_APSOC]] · `second-brain-vault/wiki/concepts/Framework_Cold_Outreach_APSOC.md`
- [[L2-6-Conversion-Architecture]] · cliente interno principale per copy per stage funnel
- [[L2-2-Advertising]] · riceve copy ads gated
- [[L2-3-Email-Lifecycle]] · riceve copy email gated
