---
Type: WORKFLOW
Status: Active
Tags: #workflow #partnership #onboarding #referral #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-PARTNER-ONBOARDING

> Reparto: **A9 — Partnership & Referral** (01-AGENCY, L2) · Standard CF-grade (ADR-007)
> Scopo: portare un candidato partner da "interessante" a **`attivo`**, cioè abilitato a inviare
> referral. Un partner non attivo **non esiste** per la pipeline DE.
> Skill: `partner-onboarder` (P2) · wrap di `co-marketing`, `referrals`, `icp-radar` (ADR-003).

---

## Trigger

| Trigger | Sorgente | Payload |
|---|---|---|
| Candidato dal triage non-ICP | `AG-A9-QUALIFY` (WF-NONICP-ROUTING → esito `PARTNER_POTENZIALE`) | `lead_ref`, azienda, motivo complementarità |
| Candidato da ricerca proattiva | `AG-A9-COORD` (coordinata con A1-Ricerca) | azienda, tipo, motivo |
| Candidato inbound | `AG-A9-COORD` | azienda, tipo, canale |

Apre un `run_id` in `agency/a9/runs/{run_id}.json` con `workflow = WF-PARTNER-ONBOARDING`.

---

## Input

```json
{
  "partner_id": "PT-0001",
  "tipo": "agenzia-no-ai | consulente-hr | commercialista | studio | altro",
  "azienda": "string",
  "motivo_complementarita": "string",
  "fonte_candidato": "nonicp-triage | ricerca-proattiva | inbound"
}
```

Vincolo: nessuna PII nel payload (R4) — azienda e ruolo sì, persona no.

---

## Step

### S1 — Valutazione complementarità · `AG-A9-COORD`

Verifica che il candidato sia **complementare** e **non concorrente** sui 3 prodotti DE (P4).
Skill: `co-marketing`.

- Complementare ⇒ crea `agency/a9/partners/{partner_id}.json` con `stato = candidato`.
- Concorrente o ambiguo ⇒ **STOP**: nessun contatto. Motivo scritto nel run.

### S2 — Contatto e proposta · `AG-A9-OUTREACH`

Contatta il candidato. Presenta il programma referral (skill `referrals`) e la **commissione da
catalogo** (fonte: A3-Preventivi).

- Il partner chiede una commissione **fuori catalogo** ⇒ **STOP** + escalation `AG-A9-COORD` → `AG-DIR`.
  Mai accettazione sul posto (R6, P5).
- Log contatti in `agency/a9/partners/{partner_id}/contatti` (canale, data, esito — no PII).

### S3 — Accordo scritto · `AG-A9-OUTREACH` → `AG-A9-MGMT`

Accordo referral **scritto e firmato**. Nessuna intesa verbale (P3). L'accordo contiene la
clausola vincolante: *ogni lead inviato deve avere profilo ICP compilato e **consenso verificato**
del lead* (flag + data + fonte) — è ciò che rende applicabile il Consent Gate (R3).

`AG-A9-MGMT` scrive `accordo = {firmato: true, data_firma}` e `commissione_catalogo_id`.

### S4 — Registrazione · `AG-A9-MGMT`

Anagrafica completa in `agency/a9/partners/{partner_id}.json`. `stato` resta **`candidato`**:
la registrazione non attiva il partner.

### S5 — Briefing ICP · `AG-A9-MGMT`

Briefing sul prodotto DE e sull'ICP (skill `icp-radar`): **quale** lead vogliamo, **cosa** deve
allegare il partner (profilo ICP completo + consenso documentato), **cosa** viene respinto.
Scrive `data_briefing`. Senza briefing datato, il gate fallisce.

### S6 — Partner Gate · `AG-A9-QA` — **BLOCCANTE**

Verifica le tre precondizioni. PASS ⇒ `stato = attivo` (unico punto del sistema dove si attiva un
partner). FAIL ⇒ `stato` resta `candidato` e **nessun suo lead entra in A9** (R2).

### S7 — Registrazione KPI · `AG-A9-INTEL`

Incrementa `partner attivi`; apre la `partner-scorecard/{partner_id}`.

---

## Gate

| Gate | Owner | Condizione PASS | FAIL ⇒ |
|---|---|---|---|
| Complementarità (S1) | `AG-A9-COORD` | Non concorrente sui 3 prodotti DE | Nessun contatto; candidato scartato con motivo |
| Catalogo (S2) | `AG-A9-OUTREACH` | Commissione = catalogo A3 | Escalation `AG-DIR`; mai accettazione sul posto (R6) |
| **Partner Gate (S6)** | `AG-A9-QA` | `accordo.firmato=true` **AND** `commissione_catalogo_id` valida **AND** `data_briefing` popolata | `stato = candidato`; **zero lead accettati** dal partner (R2) |

Nessun gate è bypassabile, nemmeno da `AG-A9-COORD`.

---

## Output

```json
{
  "partner_id": "PT-0001",
  "stato": "attivo | candidato",
  "accordo": { "firmato": true, "data_firma": "YYYY-MM-DD" },
  "commissione_catalogo_id": "CAT-REF-XX",
  "data_briefing": "YYYY-MM-DD",
  "gate_status": "PASS | FAIL",
  "motivo_fail": "string | null"
}
```

Scritto in `agency/a9/partners/{partner_id}.json` · run chiuso in `agency/a9/runs/{run_id}.json`.

---

## Handoff

| Direzione | Controparte | Cosa transita |
|---|---|---|
| ← in | `AG-A9-QUALIFY` (WF-NONICP-ROUTING) | Candidato `PARTNER_POTENZIALE` |
| ← in | A1-Ricerca (via `AG-A9-COORD`) | Candidati da ricerca proattiva |
| ↔ | A3-Preventivi | Lettura catalogo commissioni (fonte di verità) |
| → out | WF-REFERRAL-PIPELINE | Partner `attivo` ⇒ abilitato a inviare lead (`HC-PT-AG-01`) |
| → out | `AG-DIR` | Escalation: commissione fuori catalogo |
| → out | `AG-A9-INTEL` | Nuovo partner attivo (KPI) |

---

## DONE-WHEN

Il workflow è **chiuso** quando **tutte** queste condizioni sono vere:

- [ ] `agency/a9/partners/{partner_id}.json` esiste e ha `stato` ∈ {`attivo`, `candidato`} con motivo scritto.
- [ ] Se `attivo`: accordo **firmato** presente, `commissione_catalogo_id` verificata a catalogo,
      `data_briefing` popolata, `gate_status = PASS` di `AG-A9-QA`.
- [ ] Se `candidato`: `motivo_fail` scritto e comunicato; nessun lead del partner in `agency/a9/referrals`.
- [ ] Clausola ICP + **consenso verificato** presente nell'accordo (precondizione di R3).
- [ ] Nessuna PII in nessun record scritto (R4).
- [ ] `agency/a9/runs/{run_id}.json` chiuso con `gate_status` e `next_action` popolati.
- [ ] `AG-A9-INTEL` ha aggiornato il conteggio partner attivi (baseline **[DM]**).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` §5.1 — flusso di onboarding
- [[WF-REFERRAL-PIPELINE]] · `workflow/WF-REFERRAL-PIPELINE.md` — consuma i partner attivi
- [[SKILLS]] · `skills/SKILLS.md` — skill `partner-onboarder` (P2)
- [[REGOLE]] · `regole/REGOLE.md` — R2, R3, R6
