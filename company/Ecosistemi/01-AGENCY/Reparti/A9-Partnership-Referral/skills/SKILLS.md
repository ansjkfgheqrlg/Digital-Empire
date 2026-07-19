---
Type: SKILLS
Status: Active
Tags: #skills #partnership #referral #icp #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# SKILLS — A9 Partnership & Referral

> **ADR-003 — wrap, non riscrittura.** A9 **avvolge** le skill esistenti (`referrals`,
> `co-marketing`, `icp-radar`) con contratti I/O e gate di reparto. Non le duplica,
> non le riscrive, non le forka.

---

## 1. Skill esistenti mappate (wrap)

| Skill | Agente principale | Uso in A9 |
|---|---|---|
| `referrals` | `AG-A9-MGMT` | Motore del programma referral: tier partner, regole di invio, struttura commissioni, report |
| `co-marketing` | `AG-A9-OUTREACH` | Proposta di partnership, valutazione complementarità, iniziative congiunte |
| `icp-radar` | `AG-A9-QUALIFY`, `AG-A9-QA` | Triage non-ICP e verifica del profilo ICP allegato dal partner (gate) |

Il **gate** non è nella skill: è in `AG-A9-QA`. Le skill producono giudizio; il reparto decide se
è sufficiente a lasciar passare un lead.

---

## 2. Skill nuove del reparto

### `partner-onboarder` — P2

Owner: `AG-A9-OUTREACH` + `AG-A9-MGMT`. Porta un candidato da "interessante" a "attivo".

**Input**
```json
{
  "partner_id": "PT-0001",
  "tipo": "agenzia-no-ai | consulente-hr | commercialista | studio | altro",
  "azienda": "string",
  "motivo_complementarita": "string",
  "fonte_candidato": "nonicp-triage | ricerca-proattiva | inbound",
  "commissione_catalogo_id": "CAT-REF-XX"
}
```

**Output**
```json
{
  "partner_id": "PT-0001",
  "stato": "candidato | attivo | sospeso",
  "accordo": { "firmato": true, "data_firma": "YYYY-MM-DD" },
  "commissione_catalogo_id": "CAT-REF-XX",
  "data_briefing": "YYYY-MM-DD",
  "gate_status": "PASS | FAIL",
  "motivo_fail": "string | null"
}
```

**Gate:** `accordo.firmato = true` **AND** `commissione_catalogo_id` presente in catalogo
**AND** `data_briefing` non vuota. Altrimenti `stato` resta `candidato` (R2, R6).

---

### `referral-router` — P3

Owner: `AG-A9-QA` (verifica) + `AG-A9-COORD` (routing). Decide dove va un lead da partner.

**Input**
```json
{
  "referral_id": "RF-0001",
  "partner_id": "PT-0001",
  "lead_ref": "LD-XXXX",
  "icp_profile": { "settore": "string", "dimensione": "string", "problema": "string", "budget_segnale": "string" },
  "consent": { "flag": true, "data": "YYYY-MM-DD", "fonte": "string" },
  "temperatura": "caldo | tiepido"
}
```

**Output**
```json
{
  "referral_id": "RF-0001",
  "gate_status": "PASS | FAIL",
  "motivo_fail": "icp_incompleto | consenso_mancante | ownership_conflict | partner_non_attivo | null",
  "routing": "A8-fast-track | A2-outreach | respinto | hold",
  "handoff": "HC-PT-AG-01"
}
```

**Gate:** tutti i campi di `icp_profile` valorizzati **AND** `consent.flag = true` con `data` e
`fonte` **AND** partner `attivo` **AND** nessun conflitto ownership. Un solo FAIL ⇒ `respinto` (R1, R3, R8).

---

## 3. Regole comuni alle skill A9

- **Nessuna PII** in input/output: solo `lead_ref`, `partner_id`, azienda, ruolo (R4).
- **Nessuna skill contatta** direttamente lead o partner: producono artefatti, non messaggi inviati.
- Output sempre serializzabile in `agency/a9/*` senza trasformazioni manuali.

---

## Connessioni

- [[ag-a9-qa]] · `agenti/ag-a9-qa.md` — enforcement dei gate delle skill
- [[WF-PARTNER-ONBOARDING]] · `workflow/WF-PARTNER-ONBOARDING.md` — consuma `partner-onboarder`
- [[WF-REFERRAL-PIPELINE]] · `workflow/WF-REFERRAL-PIPELINE.md` — consuma `referral-router`
