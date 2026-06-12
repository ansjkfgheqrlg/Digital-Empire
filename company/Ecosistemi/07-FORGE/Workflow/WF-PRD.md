> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 07 L2 WORKFLOW-WORKS · L3 WF-PRD

# WF-PRD — Workflow L3: Product Requirements Document (prd-architect-os)

**Ecosistema:** 07-FORGE · **Reparto:** WORKFLOW-WORKS (L2.3) · **Stato:** DEFINED

Collega: [[07-FORGE/ECOSISTEMA.md]] · [[07-FORGE/BACKBONE.md]]

---

## Missione

Produrre **PRD di qualità verificata** (score 0-100) per qualsiasi prodotto o feature di
EMPIRE OS, usando `prd-architect-os` come motore. La generazione è bloccata se il context
score è inferiore a 60. Il PRD è il deliverable delle fasi S-P di SPARC e alimenta
PLATFORM (WF-SAAS-BUILD) e INFO-BUSINESS (lanci di prodotto).

---

## I 5 tipi di PRD (A–E)

| Tipo | Nome | Quando | Lunghezza |
|---|---|---|---|
| A | Enterprise | prodotto complesso, team grande, roadmap multi-fase | 10-30 pagine |
| B | MVP Lean | validazione rapida idea con risorse minime | 3-5 pagine |
| C | Feature Spec | singola feature su prodotto esistente | 2-4 pagine |
| D | Vibecoding AI-Ready | spec per build AI-assisted (Claude, Cursor) | 4-8 pagine + prompt |
| E | PR/FAQ Amazon-style | focus su outcome utente, lavora a ritroso | 3-6 pagine |

---

## Fasi del workflow

| Fase | Attore | Output | Gate |
|---|---|---|---|
| **Intake** | `frg-prd-architect` | raccolta: tipo prodotto, audience, vincoli, obiettivi, budget | intake form completo |
| **Context Enrichment** | `frg-prd-architect` + INTELLIGENCE | ricerca esistente (wiki, AgentDB, competitor) | context score ≥ 60 o blocco |
| **Generation** | `frg-prd-architect` (prd-architect-os) | PRD bozza nel tipo A-E scelto | struttura tipo rispettata |
| **Validation** | `frg-prd-architect` + `frg-eval-runner` | quality score 0-100 con breakdown per sezione | ≥ 75/100 o iterazione |
| **Approvazione** | `frg-chief` | PRD approvato per la build | sign-off registrato in handoff |
| **Consegna** | `frg-prd-architect` | PRD a PLATFORM/INFO-BUSINESS + archiviazione `forge/prds/` | handoff con acceptance_criteria |

---

## I 4 engine di prd-architect-os

1. **Intake Engine** — estrae e struttura i requisiti grezzi dall'input dell'ecosistema richiedente
2. **Context Enrichment Engine** — interroga wiki (INTELLIGENCE), AgentDB, ricerche competitor; calcola context score
3. **Generation Engine** — genera il PRD nel tipo scelto, con sezioni obbligatorie per tipo
4. **Validation Engine** — verifica completezza, misurabilità degli obiettivi, assenza di ambiguità, coerenza col Mandato Empire; produce quality score

---

## Blocco context score < 60

Se il context score è inferiore a 60 dopo l'enrichment:
- Generazione bloccata (non si procede alla creazione del documento)
- `frg-prd-architect` apre richiesta a INTELLIGENCE: quali dati mancano?
- Si torna all'Intake con lista di informazioni da raccogliere
- Nessuna eccezione: un PRD con contesto insufficiente produce un prodotto sbagliato

---

## Integrazione con PLATFORM e INFO-BUSINESS

- **PLATFORM WF-SAAS-BUILD**: riceve PRD tipo B/D come spec di costruzione
- **INFO-BUSINESS lanci**: riceve PRD tipo A/E come piano di lancio
- **FORGE ECOSYSTEM-WORKS**: PRD tipo A è il dossier iniziale di ogni nuovo ecosistema

---

## KPI

| Metrica | Target |
|---|---|
| PRD con quality score ≥ 75/100 al primo ciclo | ≥ 70% |
| PRD bloccati per context score < 60 (con debriefing) | tracciati tutti |
| PRD consegnati senza archiviazione in forge/prds/ | 0 |
| Tempo intake → PRD approvato (tipo B) | ≤ 1 giorno |
