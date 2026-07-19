---
Type: PROJECT
Status: Active
Tags: #workflow #account-management #customer-success #lifecycle #nps #upsell #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-CUSTOMER-LIFECYCLE — Dalla firma al G+90

> **Reparto:** A7 Account Management & Customer Success · **Standard:** CF-grade (ADR-007)
> **Scopo:** presidiare ogni cliente dalla firma del contratto al termine dei 90gg di supporto con
> touchpoint strutturati, e trasformare il ciclo chiuso in upsell, referral o cross-sell.

---

## Trigger

**Segnale di ingresso:** A4-Delivery emette `cliente_live` — contratto firmato, sprint avviato.

```json
{
  "trigger": "cliente_live",
  "fonte": "A4-Delivery",
  "client_id": "identificativo univoco",
  "contratto": {"data_firma": "YYYY-MM-DD", "tipo": "sprint | retainer", "durata_supporto_gg": 90},
  "milestone_previste": ["milestone dichiarate da A4-Delivery"],
  "contatto_cliente": {"nome": "...", "ruolo": "..."}
}
```

Il workflow **non parte** se `client_id` o `contratto.data_firma` mancano: senza contratto non c'è
relazione da presidiare.

---

## Input

| Input | Fonte | Obbligatorio |
|---|---|---|
| `client_id`, contratto, data firma | A4-Delivery | Sì |
| Milestone previste | A4-Delivery | Sì |
| Scope venduto | `agency/a3/contratti/{client_id}` (A3-Preventivi, read-only) | Sì |
| SLA ticket (continuo) | `agency/a4/sla/{client_id}` (A4-Delivery, read-only) | Sì, dal G+7 |
| Nome e ruolo contatto | A4-Delivery | Sì (nessun recapito — R7) |

---

## Step

### Step 1 — Assegnazione KAM `[AG-A7-COORD]`

Apre `agency/a7/clients/{client_id}/state.json` con `kam` popolato e `fase_ciclo: onboarding`.
Recall dello storico pre-firma via `memory_search("agency/a3/contratti")`.

> **GATE BLOCCANTE (R1):** nessun cliente esiste senza `kam`. Se il campo è vuoto, **nessun step
> successivo parte**. Non è un warning: è un arresto.

### Step 2 — Kickoff G+0 `[AG-A7-ONBOARD]`

Introduce il processo, presenta le milestone (**solo** quelle con date confermate da A4 — R4),
fissa la cadenza dei touchpoint, conferma per iscritto chi è il KAM. Registra le aspettative del
cliente **in parole sue** e i rischi early visibili già al G+0.
Il messaggio lo drafta **AG-A7-COMM**; l'invio è **umano** (Max).

### Step 3 — Gate onboarding `[AG-A7-QA]`

> **GATE BLOCCANTE:** `kam` popolato? milestone in stato `comunicata`? kickoff loggato in
> `agency/a7/touchpoints/{client_id}`? nessuna data non confermata comunicata?
> **PASS** → `fase_ciclo: delivery`. **FAIL** → AG-A7-ONBOARD ripristina il dato e ripresenta.

### Step 4 — Baseline salute `[AG-A7-HEALTH]`

Costruisce la dashboard iniziale in `agency/a7/health/{client_id}`. Da qui parte il monitoraggio
settimanale: milestone, ticket aperti (da `agency/a4/sla`), reattività del cliente.
Se i segnali di input mancano → `health_score: [DM]`, **mai uno score inventato** (P5).

### Step 5 — Monitoraggio continuo `[AG-A7-HEALTH]` (settimanale, G+7 → G+90)

Scansione settimanale (`scripts/health_scan.py`). Ogni segnale oltre soglia genera un alert e
attiva **WF-RETENTION-ALERT** in parallelo, senza interrompere il lifecycle.

### Step 6 — Mid-point review G+3-4 `[AG-A7-MID]`

Legge il clima del cliente, verifica che le milestone **percepite** coincidano con quelle **reali**,
intercetta i disallineamenti di scope. Ogni `delta_scope` rilevato riceve una **destinazione**:
A3-Preventivi (upsell) o rifiuto motivato. Mai un delta senza destinazione.

> **GATE BLOCCANTE:** mid-review loggata? ogni delta di scope instradato? rischio medio/alto con
> alert corrispondente aperto? nessun lavoro extra promesso senza copertura (R4, R6)?

### Step 7 — Gate Delivery G+7 `[A10-QA · 09-OPERATIONS]`

Gate esterno di ecosistema: verifica che le milestone siano loggate. A7 fornisce l'evidenza dallo
state; non produce il gate.

### Step 8 — Supporto 90gg `[AG-A7-COORD]` (settimane 2-12)

I ticket li lavora **A4-Delivery**. AG-A7-COORD **supervisiona l'SLA** leggendo `agency/a4/sla` e
agisce sul rischio (P2). A7 non tocca un ticket tecnico: se l'SLA scivola, escala.
Touchpoint secondo la cadenza fissata al kickoff — ognuno loggato (R3).

### Step 9 — Closure G+90 `[AG-A7-CLOSE]`

Raccoglie l'**NPS** (`scripts/nps_collect.py`) e il feedback qualitativo. Massimo **2 follow-up**:
oltre, si smette — la pressione danneggia il rapporto.
Con NPS raccolto, invoca `upsell-mapper` sui delta di scope registrati durante il ciclo.

### Step 10 — Handoff di uscita `[AG-A7-CLOSE → AG-A7-COORD]`

| Condizione | Destinazione |
|---|---|
| Opportunità di nuovo sprint / retainer | **A3-Preventivi** |
| NPS ≥8 **e** `consenso_case_study: confermato` | **A6-Marketing-Interno** (referral + case study) |
| Bisogno formativo rilevato | **02-INFO-BUSINESS** (cross-sell corso) |
| NPS ≤6 (detrattore) | **Nessun referral.** Alert win-back + AG-DIR |

### Step 11 — Gate finale closure `[AG-A7-QA]`

> **GATE BLOCCANTE — il più stringente del reparto:**
> - `nps` raccolto e ≠ `[DM]`? → altrimenti **FAIL** (R5)
> - Milestone tutte `completata` (o rinunciate con motivazione)?
> - `kam` **continuo** per tutti i 90gg?
> - Referral proposto solo con NPS ≥8 e consenso confermato? (R8)
>
> **PASS** → `esito_ciclo: chiuso_con_upsell | chiuso_pulito`; handoff sbloccati.
> **FAIL** → closure **bloccata**; gli handoff verso A3/A6/02-INFO **non partono**.

---

## Output

```json
{
  "client_id": "...",
  "esito_ciclo": "chiuso_con_upsell | chiuso_pulito | chiuso_con_riserva",
  "nps": "0-10 | [DM]",
  "milestone": [{"nome": "...", "stato": "completata"}],
  "upsell_referral": {"a3": "emesso | none", "a6": "emesso | none", "info": "emesso | none"},
  "alert_ciclo": [{"alert_id": "...", "esito": "rientrato | escalato"}],
  "gate_finale": "PASS | FAIL",
  "namespace_state": "agency/a7/clients/{client_id}"
}
```

---

## Handoff

| Direzione | Reparto | Cosa transita |
|---|---|---|
| ← riceve | **A4-Delivery** | Cliente live, milestone, SLA ticket (continuo, read-only) |
| ← riceve | **A3-Preventivi** | Scope venduto (read-only) |
| ← riceve | **09-OPERATIONS (A10-QA)** | Gate Delivery G+7 |
| → consegna | **A3-Preventivi** | Upsell mappato (nuovo sprint / retainer) |
| → consegna | **A6-Marketing-Interno** | Referral + case study (solo NPS ≥8 + consenso) |
| → consegna | **02-INFO-BUSINESS** | Cross-sell corso / info-product |
| → consegna | **08-INTELLIGENCE** | NPS e churn aggregati (read-only, senza nominativi) |
| ↕ escalation | **AG-DIR · Max** | Rischio non rientrato · leva commerciale (R6) · NPS `[DM]` |

---

## DONE-WHEN

Il workflow è concluso quando **tutte** queste condizioni sono vere:

- [ ] `agency/a7/clients/{client_id}` esiste con `kam` popolato per l'intero ciclo (R1)
- [ ] Kickoff, mid-review e closure sono **loggati** in `agency/a7/touchpoints/{client_id}` (R3)
- [ ] Tutte le milestone sono `completata` o rinunciate con motivazione registrata
- [ ] `nps` è raccolto e **≠ `[DM]`** (R5) — oppure il ciclo è `chiuso_con_riserva` con escalation AG-DIR
- [ ] Ogni alert alzato nel ciclo è **rientrato** o **escalato**, nessuno pendente
- [ ] `upsell_referral` è popolato: handoff emesso **o** motivo dell'assenza registrato
- [ ] **AG-A7-QA ha emesso PASS** sul gate finale — senza PASS il ciclo **non è chiuso**
- [ ] `esito_ciclo` scritto in state; snapshot in `agency/a7/gates/{client_id}`

**Un ciclo senza PASS di AG-A7-QA non è chiuso, indipendentemente da quanti giorni sono passati.**

---

## Connessioni

- [[ag-a7-coord]] · `agenti/ag-a7-coord.md` — orchestratore del workflow
- [[ag-a7-qa]] · `agenti/ag-a7-qa.md` — gate bloccante su ogni fase
- [[WF-RETENTION-ALERT]] · `workflow/WF-RETENTION-ALERT.md` — gira in parallelo dal G+7
- [[A4-Delivery]] · `../A4-Delivery/` — fornitore del cliente live
- [[A3-Preventivi]] · `../A3-Preventivi/` — destinatario dell'upsell
