---
Type: REPARTO
Status: Active
Tags: #reparto #agency #delivery #handover #autonomia #supporto90gg #A4
Created: 2026-07-11
Last updated: 2026-07-11
---

# A4 — Delivery & Implementazione

> **Ecosistema:** 01-AGENCY · **Livello:** L2 Reparto · **Dossier:** `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4`
> **Standard:** CF-grade (ADR-007) · **Topologia:** `hierarchical` (delivery attiva) + `star` (ticket 90gg)

---

## Missione

Consegnare i prodotti in **≤7 giorni** sul **server del cliente** — discovery tecnica → setup →
parametrizzazione multi-tenant → training → handover del codice — e poi presidiare **90 giorni
di supporto** con ticket decrescenti.

**Il cliente deve poterci licenziare.** È l'identità di Digital Empire tradotta in gate: se per
far girare il sistema serve ancora DE, la delivery **non è chiusa**. Zero dipendenza residua è
una condizione di PASS, non un nice-to-have.

A4 possiede l'**ESECUZIONE** dello sprint. A7-Account-Management possiede la **RELAZIONE**
post-firma. A4 non riscrive i motori esistenti: li clona, li parametrizza e li installa
(ADR-003 WRAP-not-rewrite).

---

## Roster del reparto (9 agenti)

| ID | Agente | File | Tipo | Tier | Ruolo |
|---|---|---|---|---|---|
| `AG-A4-COORD` | Coordinatore Delivery | `agenti/ag-a4-coord.md` | coordinator | opus | Valida l'handoff, pianifica G+0→G+7, decide il rollback day-1 |
| `AG-A4-ENV` | Environment Setup | `agenti/ag-a4-env.md` | worker | sonnet | Verifica ambiente cliente (OS, Python, permessi, rete); install; secrets |
| `AG-A4-TENANT` | Config Multi-Tenant | `agenti/ag-a4-tenant.md` | worker | sonnet | Inietta `brand_kit` + `icp` del cliente in ogni workflow (pattern 11) |
| `AG-A4-UAT` | UAT Runner | `agenti/ag-a4-uat.md` | worker | sonnet | Run di accettazione; checklist UAT firmabile; run autonoma del cliente |
| `AG-A4-TRAIN` | Training Kit | `agenti/ag-a4-train.md` | worker | sonnet | Video walkthrough, runbook operativo, FAQ + sessione (skill `delivery-playbook`) |
| `AG-A4-HAND` | Handover Pack | `agenti/ag-a4-hand.md` | worker | sonnet | Codice, README, credenziali, licenza d'uso (skill `client-handover`) |
| `AG-A4-SUPP` | Supporto 90gg | `agenti/ag-a4-supp.md` | worker | haiku | Triage ticket, SLA, check proattivo settimanale (skill `support-90`) |
| `AG-A4-LEARN` | Pattern Learner | `agenti/ag-a4-learn.md` | worker | sonnet | Distilla ambienti critici ed errori ricorrenti → `agency/reasoning` |
| `AG-A4-QA` | Gate Delivery | `agenti/ag-a4-qa.md` | verifier | sonnet | **Bloccante**: autonomia cliente, zero dipendenza residua |

---

## Workflow del reparto (4 workflow CF-grade)

| ID | File | Scopo | Gate di uscita |
|---|---|---|---|
| **WF-DELIVERY-OUTREACH-FACTORY** | `workflow/WF-DELIVERY-OUTREACH-FACTORY.md` | Clona la pipeline outreach DE, la parametrizza multi-tenant, la installa sul server cliente | AG-A4-QA: Gate Delivery PASS (autonomia verificata) |
| **WF-DELIVERY-CONTENT-FACTORY** | `workflow/WF-DELIVERY-CONTENT-FACTORY.md` | Richiede il motore CF parametrizzato (`HC-AG-CF-01`), setup, training, handover | AG-A4-QA: Gate Delivery PASS |
| **WF-DELIVERY-SECOND-BRAIN** | `workflow/WF-DELIVERY-SECOND-BRAIN.md` | Richiede il template second-brain (`HC-IN-AG-01`), configura vault + skill sul sistema cliente | AG-A4-QA: Gate Delivery PASS |
| **WF-SUPPORTO-90GG** | `workflow/WF-SUPPORTO-90GG.md` | Intake ticket → triage (bug / domanda / fuori scope) → fix → log; check settimanale | AG-A4-QA: nessun ticket chiuso senza conferma del cliente |

---

## Gate del reparto — Gate Delivery

**Presidio: AG-A4-QA. Bloccante — nessun handover si chiude senza gate verde.**
Sopra di esso agisce **A10-QA-Cliente**, gate indipendente che riporta ad AG-DIR (`HC-AG-QC-01`).

| Check | Condizione PASS |
|---|---|
| Gira sul server del cliente | Workflow funzionante sul server cliente, **non** in locale/staging DE |
| Run reale passata | Almeno 1 run reale completata sullo stack parametrizzato |
| Training erogato | Materiale consegnato + sessione fatta |
| UAT firmata | Checklist UAT firmata dal cliente |
| Autonomia verificata | Il cliente ha eseguito **1 run da solo** in UAT |
| Zero dipendenza residua | Nessuna credenziale DE, nessun nodo DE nel runtime cliente |

**Countdown 7gg:** parte **SOLO ad ambiente conforme**. Ambiente non conforme a G+0 → rollback
day-1: il countdown non parte, runbook requisiti al cliente, alert a Max (la promessa dei 7gg
è protetta contrattualmente).

---

## KPI del reparto

| KPI | Owner | Definizione | Baseline |
|---|---|---|---|
| Giorni delivery | AG-A4-COORD | Giorni da ambiente conforme a handover chiuso | Target ≤7 |
| UAT pass al primo giro | AG-A4-UAT | Delivery con UAT firmata senza rework / tot | [DM] |
| Ticket risolti in SLA | AG-A4-SUPP | Ticket entro SLA contrattuale / tot (bug ≤24h · domanda ≤48h) | [DM] |
| Run autonoma del cliente | AG-A4-QA | Delivery con run autonoma eseguita in UAT / tot | Target 100% |
| Gate bypass rate | AG-A4-QA | Handover chiusi senza Gate Delivery PASS / tot | Target 0 |

Dettaglio completo → `kpi/KPI.md`.

---

## Handoff e connessioni inter-reparto

| Direzione | Reparto/Ecosistema | Cosa transita |
|---|---|---|
| ← riceve da | A3-Preventivi | Scope congelato + prerequisiti d'ambiente raccolti in call |
| ← riceve da | A8-Closing (WIN) | Contratto firmato + scope per l'onboarding |
| ← riceve da | 09-OPERATIONS | Scheduling dei check settimanali 90gg, backup ambienti |
| ← riceve da | A10-QA-Cliente | `HC-QC-AG-01` — verdetto PASS/FAIL indipendente + lista difetti |
| → consegna a | A10-QA-Cliente | `HC-AG-QC-01` — richiesta review indipendente della delivery a G+7 |
| → consegna a | A7-Account-Management | Cliente live + SLA ticket + artefatti milestone |
| → consegna a | A6-Marketing-Interno | Segnale "delivery chiusa" → testimonianza + case study |
| → consegna a | 03-CONTENT-FACTORY | `HC-AG-CF-01` — richiesta motore CF parametrizzato per il cliente |
| → consegna a | 08-INTELLIGENCE | `HC-IN-AG-01` — richiesta template second-brain per il cliente |

---

## Namespace AgentDB

**Chiave canonica: `agency/a4`** — fonte di verità: `../../NAMESPACE.md`.

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a4/delivery` | Delivery attive/chiuse: piano G+0→G+7, stato per step, esito Gate | AG-A4-COORD |
| `agency/a4/uat` | Checklist UAT firmabili/firmate; esito run autonoma del cliente | AG-A4-UAT |
| `agency/a4/environments` | Profili ambiente cliente: OS, Python, permessi, rete, conformità | AG-A4-ENV |
| `agency/a4/support` | Ticket 90gg: classe, SLA, stato, conferma cliente, check settimanali | AG-A4-SUPP |
| `agency/a4/reasoning` | Pattern delivery distillati: ambienti critici, errori ricorrenti | AG-A4-LEARN |

**Regola di integrità:** nessuna delivery può essere in stato `handover_completo` senza
`gate_delivery: "PASS"`. **Nessun segreto cliente nello state**: i secrets vivono sul server
del cliente, mai nel namespace DE.

---

## Principi e regole

- Principi operativi → `principi/PRINCIPI.md`
- Regole non negoziabili → `regole/REGOLE.md`
- Stato e ripartibilità a freddo → `state/README.md`

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` — gerarchia, flussi G+0→G+7, Gate Delivery, namespace
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4`
- [[ag-a4-qa]] · `agenti/ag-a4-qa.md` — presidio del Gate Delivery
- [[WF-DELIVERY-OUTREACH-FACTORY]] · `workflow/WF-DELIVERY-OUTREACH-FACTORY.md`
- [[WF-SUPPORTO-90GG]] · `workflow/WF-SUPPORTO-90GG.md`
- [[A10-QA-Cliente]] · gate indipendente sopra il Gate Delivery
- [[A7-Account-Management]] · possiede la relazione post-firma
