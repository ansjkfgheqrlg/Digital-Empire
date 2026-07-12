---
Type: WORKFLOW
Status: Active
Tags: #workflow #non-icp #triage #zero-loss #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-NONICP-ROUTING

> Reparto: **A9 — Partnership & Referral** (01-AGENCY, L2) · Standard CF-grade (ADR-007)
> Scopo: dare **una casa a ogni lead che A1-Ricerca scarta**. Ogni lead non-ICP riceve **uno e un
> solo** esito tracciato: `PARTNER_POTENZIALE` · `NURTURE` · `ARCHIVIO`.
> Nel v1 questi lead sparivano. In v2 **nessun lead muore senza decisione** (P1, R5).
> Skill: wrap di `icp-radar`, `co-marketing` (ADR-003).

---

## Trigger

| Trigger | Sorgente | Payload |
|---|---|---|
| Batch lead non-ICP | A1-Ricerca — `AG-A1-QUAL` verdetto "scarta" / "nurture" | lista `lead_ref` + motivo scarto |
| Risveglio nurture programmato | `agency/a9/nurture` (data risveglio raggiunta) | `lead_ref` + motivo parcheggio |

Apre `agency/a9/runs/{run_id}.json` con `workflow = WF-NONICP-ROUTING`, `batch.lead_totali = N`,
`batch.lead_con_esito = 0`.

---

## Input

```json
{
  "batch_id": "B-YYYYMMDD-NN",
  "fonte": "a1-qual",
  "leads": [
    { "lead_ref": "LD-XXXX", "verdetto_a1": "scarta | nurture", "motivo_a1": "…", "settore": "…", "dimensione": "…" }
  ]
}
```

Nessuna PII (R4): solo `lead_ref`, azienda/settore, mai persone.

---

## Step

### S1 — Apertura batch · `AG-A9-COORD`

Conta `lead_totali`, apre il run. Il batch è `OPEN` finché `lead_con_esito < lead_totali` (R5).

### S2 — Triage · `AG-A9-QUALIFY`

Per **ogni** lead, skill `icp-radar` (distanza dall'ICP dei 3 prodotti DE) + `co-marketing`
(complementarità del mestiere). Tre esiti possibili, mutuamente esclusivi:

| Esito | Criterio | Destinazione |
|---|---|---|
| `PARTNER_POTENZIALE` | Mestiere **complementare** a DE (agenzia no-AI, consulente HR, commercialista, studio): può inviare referral | Coda **WF-PARTNER-ONBOARDING** → `AG-A9-OUTREACH` |
| `NURTURE` | Fuori ICP **oggi**, plausibile domani (troppo piccolo, timing, prodotto non pronto) | `agency/a9/nurture/{lead_ref}` + `data_risveglio` |
| `ARCHIVIO` | Mai ICP e mai partner (settore incompatibile, dato sporco, azienda inesistente) | `agency/a9/archive/{lead_ref}` + motivo (append-only) |

Ogni esito è scritto in `agency/a9/nonicp/{lead_ref}.json` con **motivo**.

**`AG-A9-QUALIFY` non contatta mai il lead**: il triage è **documentale**. Nessun contatto senza
consenso verificato (R3).

### S3 — Escalation ambigui · `AG-A9-QUALIFY` → `AG-A9-COORD`

Un lead che **potrebbe rientrare in un prodotto DE futuro** è ambiguo: **non si archivia in
autonomia**. Esito `ambiguo` + escalation a `AG-A9-COORD`, che decide (e la decisione diventa
l'esito definitivo). Un ambiguo pendente tiene il batch `OPEN`.

### S4 — Promozione candidati partner · `AG-A9-QUALIFY` → `AG-A9-OUTREACH`

I `PARTNER_POTENZIALE` diventano `agency/a9/partners/{partner_id}.json` con `stato = candidato`.
**Candidato ≠ partner**: l'attivazione richiede il Partner Gate di `AG-A9-QA` (WF-PARTNER-ONBOARDING, R2).

### S5 — Programmazione risvegli · `AG-A9-QUALIFY`

Ogni `NURTURE` riceve una `data_risveglio`. Al risveglio, il lead può rientrare in
WF-REFERRAL-PIPELINE **solo se** ha consenso verificato; altrimenti resta in nurture (R3).

### S6 — Zero-Loss Gate · `AG-A9-QUALIFY` — **BLOCCANTE**

`lead_con_esito == lead_totali`?

- **Sì** ⇒ batch `CLOSED`; `AG-A9-INTEL` pubblica il KPI del periodo.
- **No** ⇒ batch resta `OPEN`; `AG-A9-INTEL` **non pubblica** i KPI del periodo (R5).

### S7 — Metriche · `AG-A9-INTEL`

Copertura esiti (target **100%**), distribuzione per esito, candidati partner generati. Baseline **[DM]**.

---

## Gate

| Gate | Owner | Condizione PASS | FAIL ⇒ |
|---|---|---|---|
| **Zero-Loss (S6)** | `AG-A9-QUALIFY` | `lead_con_esito == lead_totali` | Batch `OPEN`; KPI del periodo **non pubblicabili** (R5) |
| Ambiguo (S3) | `AG-A9-COORD` | Nessun lead `ambiguo` pendente | Batch `OPEN` finché il coordinatore non decide |
| No-contatto (S2) | `AG-A9-QA` | Zero contatti al lead durante il triage | Violazione R3 (consenso) ⇒ rework + incident |
| No-PII (S2) | `AG-A9-QA` | Solo `lead_ref` / azienda nei record | Record da bonificare prima di avanzare (R4) |
| Candidato ≠ partner (S4) | `AG-A9-QA` | `stato = candidato` alla creazione | Attivazione irregolare ⇒ rollback (R2) |

---

## Output

```json
{
  "batch_id": "B-YYYYMMDD-NN",
  "lead_totali": 0,
  "lead_con_esito": 0,
  "esiti": { "PARTNER_POTENZIALE": 0, "NURTURE": 0, "ARCHIVIO": 0, "ambiguo": 0 },
  "batch_status": "OPEN | CLOSED",
  "candidati_partner": ["PT-0001"]
}
```

Per lead: `agency/a9/nonicp/{lead_ref}.json` = `{esito, motivo, verdetto_a1, timestamp}`.

---

## Handoff

| Direzione | Controparte | Cosa transita |
|---|---|---|
| ← in | A1-Ricerca (`AG-A1-QUAL`) | Batch lead non-ICP ("scarta"/"nurture") + motivo |
| → out | WF-PARTNER-ONBOARDING (`AG-A9-OUTREACH`) | Candidati `PARTNER_POTENZIALE` |
| → out | `agency/a9/nurture` | Lead parcheggiati + data risveglio |
| → out | WF-REFERRAL-PIPELINE | Risveglio nurture **con consenso verificato** |
| → out | `AG-A9-COORD` | Lead ambigui (decisione) |
| → out | `AG-A9-INTEL` | Copertura esiti (Zero-Loss) |

---

## DONE-WHEN

- [ ] **Ogni** lead del batch ha un record `agency/a9/nonicp/{lead_ref}.json` con `esito` + `motivo`.
- [ ] `lead_con_esito == lead_totali` ⇒ `batch_status = CLOSED` (Zero-Loss, R5).
- [ ] Zero lead `ambiguo` pendenti: ognuno ha ricevuto una decisione da `AG-A9-COORD`.
- [ ] Ogni `PARTNER_POTENZIALE` esiste in `agency/a9/partners` con `stato = candidato` (mai `attivo`).
- [ ] Ogni `NURTURE` ha `data_risveglio` programmata.
- [ ] Ogni `ARCHIVIO` ha motivo scritto in `agency/a9/archive` (append-only).
- [ ] **Nessun lead è stato contattato** durante il triage (R3).
- [ ] Nessuna PII in nessun record scritto (R4).
- [ ] `AG-A9-INTEL` ha registrato la copertura esiti (baseline **[DM]**).
- [ ] `agency/a9/runs/{run_id}.json` chiuso con `batch` e `next_action` coerenti.

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` §5.3 — flusso di triage non-ICP
- [[ag-a9-qualify]] · `agenti/ag-a9-qualify.md` — owner del workflow
- [[WF-PARTNER-ONBOARDING]] · `workflow/WF-PARTNER-ONBOARDING.md` — destinazione dei candidati
- [[REGOLE]] · `regole/REGOLE.md` — R3 (consenso), R4 (no PII), R5 (Zero-Loss)
