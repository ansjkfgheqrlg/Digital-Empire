---
Type: WORKFLOW
Status: Active
Tags: #workflow #referral #pipeline #consenso #gate #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-REFERRAL-PIPELINE

> Reparto: **A9 — Partnership & Referral** (01-AGENCY, L2) · Standard CF-grade (ADR-007)
> Scopo: portare ogni lead in arrivo da un partner (`HC-PT-AG-01`) o da un segnale referral di
> A7-Account-Management dal **ricevimento** all'**handoff** verso A8-Closing o A2-Acquisizione,
> con **profilo ICP compilato** e **consenso verificato**.
> Skill: `referral-router` (P3) · wrap di `icp-radar`, `referrals` (ADR-003).

---

## Trigger

| Trigger | Sorgente | Handoff |
|---|---|---|
| Lead da partner attivo | Partner esterno → `AG-A9-MGMT` | `HC-PT-AG-01` |
| Segnale referral da cliente attivo | A7-Account-Management | `cliente_id` + contatto indicato |
| Risveglio lead nurture consenziente | `AG-A9-QUALIFY` (`agency/a9/nurture`) | data risveglio raggiunta |

Apre `agency/a9/runs/{run_id}.json` con `workflow = WF-REFERRAL-PIPELINE`.

---

## Input

```json
{
  "referral_id": "RF-0001",
  "origine": "partner | a7-cliente | nurture-wakeup",
  "partner_id": "PT-0001",
  "lead_ref": "LD-XXXX",
  "icp_profile": { "settore": "…", "dimensione": "…", "problema": "…", "budget_segnale": "…" },
  "consent": { "flag": true, "data": "YYYY-MM-DD", "fonte": "…" },
  "temperatura": "caldo | tiepido"
}
```

Nessuna PII (R4): il lead viaggia come `lead_ref`.

---

## Step

### S1 — Intake · `AG-A9-MGMT`

Registra il referral in `agency/a9/referrals/{referral_id}.json` con `origine` e `partner_id`.

**Non pre-seleziona e non "aggiusta"** un ICP incompleto o un consenso mancante: registra
**così com'è** e passa al gate. Manipolare l'input per farlo passare è una violazione (R3).

Se il partner è in stato `candidato` o `sospeso` ⇒ **STOP immediato**: lead respinto, non registrato
in pipeline (R2).

### S2 — Gate ICP + Consenso · `AG-A9-QA` — **BLOCCANTE**

Verifica in quest'ordine, fermandosi al primo FAIL:

1. **Partner attivo?** (accordo firmato + commissione catalogo + briefing datato).
2. **ICP completo?** ogni campo obbligatorio di `icp_profile` valorizzato (skill `icp-radar`).
   Un ICP "quasi completo" è FAIL.
3. **Consenso VERIFICATO?** `consent = {flag: true, data, fonte}`. Un consenso *dichiarato ma non
   documentato* è FAIL. A9 **non lo raccoglie al posto del partner** e **non lo presume** (R3).
4. **Ownership libera?** lead assente da `agency/a2/pipeline` e da `agency/clients` (R8).

- **PASS** ⇒ `gate_status = PASS` (immutabile) → S3.
- **FAIL** ⇒ `gate_status = FAIL` + `motivo_fail`; lead **respinto al partner** con motivo scritto;
  `AG-A9-MGMT` richiama il partner al briefing; `fail_count++`.
  Il lead **non viene passato ad A2/A8 in nessun caso**.

### S3 — Routing · `AG-A9-COORD`

Post-PASS, decide la destinazione (skill `referral-router`):

- **CALDO** (il lead ha già chiesto di parlare con DE) ⇒ **A8-Closing**, fast-track chiusura.
- **TIEPIDO** (va scaldato) ⇒ **A2-Acquisizione**, outreach su lead **consenziente**.
- **HOLD** (conflitto ownership non risolto) ⇒ escalation `AG-A9-COORD` + coordinatore A2 → `AG-DIR`.

Scrive `routing` in `agency/a9/referrals/{referral_id}.json`.

### S4 — Handoff · `AG-A9-COORD`

Consegna il dossier al reparto ricevente: `referral_id`, `lead_ref`, `icp_profile`, `consent`,
`partner_id`, `temperatura`. Il ricevente **non deve ricostruire nulla** (P6).

### S5 — Tracciamento esito · `AG-A9-INTEL`

Monitora `agency/a8/deals`. A deal chiuso: `esito = chiuso-vinto | chiuso-perso`.

### S6 — Commissione · `AG-A9-MGMT` + `AG-A9-QA`

A `chiuso-vinto`: commissione `maturata` **solo se** `contratto_firmato = true` **e** deal
confermato da A8. Altrimenti `hold` + escalation `AG-DIR` (R6). Importo **da catalogo**, mai negoziato.

---

## Gate

| Gate | Owner | Condizione PASS | FAIL ⇒ |
|---|---|---|---|
| Partner attivo (S2.1) | `AG-A9-QA` | `stato = attivo` | Lead respinto; non entra in pipeline (R2) |
| **ICP (S2.2)** | `AG-A9-QA` | Tutti i campi obbligatori valorizzati | Lead respinto al partner + richiamo briefing |
| **Consenso (S2.3)** | `AG-A9-QA` | `flag=true` + `data` + `fonte` documentata | **Lead respinto. Mai ad A2/A8.** `fail_count++` (R3) |
| Ownership (S2.4) | `AG-A9-QA` | Lead assente da A2/clients | `HOLD` + escalation coordinatore A2 → AG-DIR (R8) |
| Commissione (S6) | `AG-A9-MGMT` + `AG-A9-QA` | Contratto firmato + deal confermato | `hold`; nessun pagamento; escalation AG-DIR (R6) |

Nessun gate bypassabile. `gate_status` scritto è **immutabile**: un nuovo tentativo apre un nuovo `run_id`.

---

## Output

```json
{
  "referral_id": "RF-0001",
  "gate_status": "PASS | FAIL",
  "motivo_fail": "icp_incompleto | consenso_mancante | ownership_conflict | partner_non_attivo | null",
  "routing": "A8-fast-track | A2-outreach | respinto | hold",
  "esito": "aperto | chiuso-vinto | chiuso-perso",
  "commissione": { "stato": "hold | maturata | pagata", "importo_catalogo": "…" }
}
```

---

## Handoff

| Direzione | Controparte | Cosa transita |
|---|---|---|
| ← in | Partner attivo | Lead + ICP + consenso (`HC-PT-AG-01`) |
| ← in | A7-Account-Management | Segnale referral da cliente attivo |
| ← in | `AG-A9-QUALIFY` | Risveglio lead nurture consenziente |
| → out | **A8-Closing** | Lead CALDO post-PASS (fast-track) |
| → out | **A2-Acquisizione** | Lead TIEPIDO post-PASS (outreach) |
| → out | Partner | FAIL con motivo scritto + richiamo al briefing |
| → out | `AG-DIR` | Commissioni maturate; escalation ownership/contratto |

---

## DONE-WHEN

- [ ] `agency/a9/referrals/{referral_id}.json` esiste con `gate_status` ∈ {PASS, FAIL}.
- [ ] Se **PASS**: `icp_profile` completo, `consent = {flag:true, data, fonte}`, ownership libera,
      partner `attivo`, `routing` scritto (A8 o A2), handoff consegnato.
- [ ] Se **FAIL**: `motivo_fail` scritto, lead **respinto** (non presente in A2/A8), partner
      richiamato al briefing, `fail_count` incrementato.
- [ ] Nessuna PII in nessun record (R4); `consent` registrato solo come flag/data/fonte.
- [ ] Esito tracciato da `AG-A9-INTEL` (`aperto` finché A8 non conferma).
- [ ] Commissione `maturata` **solo** con contratto firmato + deal confermato; altrimenti `hold`.
- [ ] `agency/a9/runs/{run_id}.json` chiuso con `step_corrente` e `next_action` coerenti.
- [ ] Partner con `fail_count ≥ 2` su consenso ⇒ proposta di sospensione inviata a `AG-A9-COORD` (R8).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` §5.2 — flusso referral
- [[ag-a9-qa]] · `agenti/ag-a9-qa.md` — owner del gate bloccante
- [[REGOLE]] · `regole/REGOLE.md` — R1, R3, R6, R8
- [[state/README]] · `state/README.md` — schema `agency/a9/referrals`
