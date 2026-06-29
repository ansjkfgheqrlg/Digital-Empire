---
Type: ARCHITETTURA
Status: Active
Tags: #architettura #agency #delivery #handover #autonomia #A4
Created: 2026-06-23
Last updated: 2026-06-23
---

# ARCHITETTURA — A4 Delivery & Implementazione

> Documento di architettura interna del reparto. Descrive gerarchia, flussi, confini e namespace.
> Standard: CF-grade (ADR-007). Motori esistenti → wrap, mai rewrite (ADR-003).

---

## 1. Gerarchia interna

```
01-AGENCY (L1) — AG-DIR
   └── A4 Delivery & Implementazione
         │
         AG-A4-COORD (coordinator, opus)
         ├── AG-A4-ENV    (worker, sonnet)  → verifica ambiente cliente; install; secrets
         ├── AG-A4-TENANT (worker, sonnet)  → iniezione brand_kit + icp (pattern 11)
         ├── AG-A4-UAT    (worker, sonnet)  → run accettazione; checklist UAT firmabile
         ├── AG-A4-TRAIN  (worker, sonnet)  → training kit; skill delivery-playbook
         ├── AG-A4-HAND   (worker, sonnet)  → handover pack; skill client-handover
         ├── AG-A4-SUPP   (worker, haiku)   → triage ticket 90gg; SLA; skill support-90
         ├── AG-A4-LEARN  (worker, sonnet)  → distilla pattern delivery → agency/reasoning
         └── AG-A4-QA     (verifier, sonnet)→ Gate Delivery: autonomia cliente, zero dipendenza
```

**Principio di coordinamento:** AG-A4-COORD (opus) riceve l'handoff da A3 (contratto firmato +
scope congelato + prerequisiti ambiente), pianifica la delivery in giorni G+0→G+7, orchestra
i worker e decide il **rollback** se il giorno-1 ambiente fallisce. AG-A4-QA è **bloccante**
su ogni delivery: nessun handover si chiude senza Gate Delivery verde. Il countdown 7gg parte
SOLO ad ambiente conforme (protezione commerciale esplicita nel contratto).

---

## 2. Flussi principali (delivery attiva + supporto 90gg)

### 2.1 Delivery di un prodotto (≤7 giorni, sul server del cliente)

```
[A3 Preventivi: contratto firmato + scope congelato + prerequisiti raccolti in call]
         │
         ▼
AG-A4-COORD — valida handoff; pianifica G+0→G+7; apre state delivery
         │
         ▼
G+0  AG-A4-ENV — verifica prerequisiti ambiente cliente (OS, Python, permessi, rete)
  → ambiente conforme? SÌ → countdown parte · NO → rollback day-1: countdown NON parte,
    runbook requisiti al cliente, alert a Max (la promise 7gg è protetta dal contratto)
         │
         ▼
G+1  AG-A4-ENV — setup repo + secrets sul server del cliente (mai in locale DE)
         │
         ▼
G+2  AG-A4-TENANT — iniezione brand_kit + icp del cliente in ogni workflow (pattern 11)
         │
         ▼
G+3-4  Test run su campione piccolo sullo stack parametrizzato (debug in dry-run, pattern 3)
         │
         ▼
G+5  AG-A4-TRAIN — training kit (video walkthrough, runbook operativo, FAQ) + sessione
         │
         ▼
G+6  AG-A4-UAT — run UAT con il cliente; checklist firmabile; il cliente esegue 1 run da solo
         │
         ▼
G+7  AG-A4-HAND — handover pack (codice, README, credenziali, licenza d'uso)
         │
         ▼
AG-A4-QA — Gate Delivery (bloccante): vedi §3
  → PASS: delivery chiusa; segnale a A6 (case study) · FAIL: rework mirato → re-gate
         │
         ▼
AG-A4-LEARN — distilla pattern (ambienti critici, errori ricorrenti) → agency/reasoning
```

### 2.2 Supporto 90gg (ticket decrescenti, cliente sempre più autonomo)

```
[Ticket in ingresso durante i 90gg]   oppure   [Check proattivo settimanale da 09 OPERATIONS]
         │
         ▼
AG-A4-SUPP — triage: bug | domanda | fuori scope
  → bug → fix (SLA ≤24h) · domanda → risposta (SLA ≤48h) · fuori scope → proposta upsell A6
         │
         ▼
Log ticket + SLA in agency/a4/support · check proattivo settimanale
         │
         ▼
A 90gg → review con A7 Account Mgmt · proposta upsell da A6 · nessun ticket chiuso senza conferma cliente
```

---

## 3. Gate Delivery — il confine "agenzia da licenziare"

| Check | Condizione PASS | Owner |
|---|---|---|
| Gira sul server del cliente | Workflow funzionante sul server cliente, NON in locale/staging DE | AG-A4-QA |
| Run reale passata | Almeno 1 run reale completata sullo stack parametrizzato | AG-A4-QA |
| Training erogato | Materiale consegnato + sessione fatta | AG-A4-TRAIN |
| UAT firmata | Checklist UAT firmata dal cliente | AG-A4-UAT |
| Autonomia verificata | Il cliente ha eseguito **1 run da solo** in UAT | AG-A4-QA |
| Zero dipendenza residua | Nessuna credenziale DE, nessun nodo DE nel runtime cliente | AG-A4-QA |

**Regola d'oro (identità DE):** "l'agenzia progettata per essere licenziata". Il Gate Delivery
non passa finché il cliente non è **autonomo**: se per girare serve ancora DE, la delivery
non è chiusa. Zero dipendenza residua è una condizione di PASS, non un nice-to-have.

---

## 4. Namespace memoria — `agency/a4/...`

| Namespace | Contenuto | Owner scrittura |
|---|---|---|
| `agency/a4/delivery` | Delivery attive/chiuse: piano G+0→G+7, stato per step, esito Gate | AG-A4-COORD |
| `agency/a4/uat` | Checklist UAT firmabili/firmate per delivery; esito run autonoma cliente | AG-A4-UAT |
| `agency/a4/environments` | Profili ambiente cliente: OS, Python, permessi, rete, esito conformità | AG-A4-ENV |
| `agency/a4/support` | Ticket 90gg: classe, SLA, stato, conferma cliente, check settimanali | AG-A4-SUPP |
| `agency/a4/reasoning` | Pattern delivery distillati: ambienti critici, errori ricorrenti | AG-A4-LEARN |

**Regola di integrità:** nessuna delivery in `agency/a4/delivery` può essere in stato
`handover_completo` senza `gate_delivery: "PASS"`. Nessun PII/segreto cliente nello state
(solo riferimenti; i secrets vivono sul server del cliente, mai nel namespace DE).

---

## 5. Confine con i fornitori di motore (03-CF, 08-INTELLIGENCE, Outreach DE)

| Aspetto | A4 Delivery | Fornitore motore |
|---|---|---|
| Motore Outreach | Clona + parametrizza sul server cliente | Pipeline outreach DE (esistente — wrap) |
| Motore Content Factory | Riceve via `HC-AG-CF-01`, setup, training | 03-CONTENT-FACTORY |
| Template Second Brain | Riceve via `HC-IN-AG-01`, configura vault | 08-INTELLIGENCE |
| Parametrizzazione | Inietta brand_kit + icp del cliente (pattern 11) | — |
| Autonomia cliente | Verifica e firma (Gate Delivery) | — |

**Regola ADR-003 (wrap-not-rewrite):** A4 non riscrive i motori esistenti. Li clona,
li parametrizza multi-tenant e li installa sul server del cliente. Se un motore richiede
modifiche strutturali, A4 apre handoff al reparto proprietario, non patcha in locale.

---

## 6. State e ripartibilità

Ogni delivery produce un `state.json` in `agency/a4/delivery/{delivery_id}/` con i campi:
- `delivery_id` · `cliente` (riferimento, non PII) · `prodotto`
- `ambiente_conforme` (bool) + `countdown_start` (data o null)
- `step_corrente` (G+0…G+7) · `tenant_injected` (bool)
- `uat_firmata` (bool) + `run_autonoma_cliente` (bool)
- `gate_delivery` (pending | PASS | FAIL) + `gate_fail_motivo`
- `last_updated` (timestamp)

Questo permette la **ripartibilità a freddo**: un agente rientra nella delivery dal punto
esatto di interruzione (test amnesia §6 V2) senza riestrarre tutto il contesto.

---

## Connessioni

- [[README]] · `README.md` — missione, roster, KPI del reparto
- [[01-ECOSISTEMA-AGENCY-V2]] · `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY-V2.md §A4`
- [[A3-Preventivi]] · fornitore contratto + scope congelato + prerequisiti ambiente
- [[A6-Marketing-Interno]] · riceve segnale "delivery chiusa" per case study
- [[WF-DELIVERY-OUTREACH-FACTORY]] · `workflow/WF-DELIVERY-OUTREACH-FACTORY.md`
- [[WF-SUPPORTO-90GG]] · `workflow/WF-SUPPORTO-90GG.md`
