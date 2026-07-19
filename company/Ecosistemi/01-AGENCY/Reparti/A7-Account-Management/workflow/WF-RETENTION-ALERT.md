---
Type: PROJECT
Status: Active
Tags: #workflow #account-management #churn #retention #alert #A7
Created: 2026-07-11
Last updated: 2026-07-11
---

# WF-RETENTION-ALERT — Intercettare il churn prima della perdita

> **Reparto:** A7 Account Management & Customer Success · **Standard:** CF-grade (ADR-007)
> **Scopo:** intercettare i rischi di churn **prima** che diventino perdita del cliente. Gira in
> parallelo a WF-CUSTOMER-LIFECYCLE per tutta la durata del ciclo, senza interromperlo.

---

## Trigger

**Segnale di ingresso:** AG-A7-HEALTH rileva uno o più segnali oltre soglia durante il monitoraggio
settimanale (`scripts/health_scan.py`, return code `2`) o su evento (variazione in `agency/a4/sla`).

```json
{
  "trigger": "segnale_churn",
  "fonte": "AG-A7-HEALTH",
  "client_id": "identificativo univoco",
  "segnali_attivi": [
    {"segnale": "ticket_multipli_aperti", "valore": 3, "soglia": 2},
    {"segnale": "risposta_cliente_lenta", "valore": "7gg", "soglia": "5gg"},
    {"segnale": "nps_intermedio_basso", "valore": 6, "soglia": 6},
    {"segnale": "milestone_in_ritardo", "valore": "4gg", "soglia": "0gg"}
  ],
  "health_score": "giallo | rosso",
  "timestamp_segnale": "ISO-8601"
}
```

**Trigger anticipato:** anche un solo segnale `rosso` (es. NPS intermedio ≤6) attiva il workflow
immediatamente, senza attendere la scansione settimanale.

---

## Input

| Input | Fonte | Note |
|---|---|---|
| Segnali attivi + soglie | `agency/a7/health/{client_id}` (AG-A7-HEALTH) | Obbligatorio |
| SLA ticket | `agency/a4/sla/{client_id}` (A4-Delivery) | **Sola lettura** — A7 non produce questo dato |
| Milestone e fase ciclo | `agency/a7/clients/{client_id}` | Obbligatorio |
| Clima dai touchpoint | `agency/a7/touchpoints/{client_id}` | Contesto qualitativo |
| Storico alert | `agency/a7/alerts/*` | Un alert ricorrente pesa di più di un alert isolato |

---

## Step

### Step 1 — Rilevazione `[AG-A7-HEALTH]`

`churn-prevention` valuta i segnali contro le soglie. Se il rischio è `medio` o `alto`, genera
`ALRT-{client_id}-NNN` con `timestamp_segnale` in ISO-8601.

> **Nessuno score inventato:** se i segnali di input mancano (es. A4 non ha prodotto l'SLA),
> `health_score: [DM]` e il fatto viene **segnalato ad AG-A7-QA** come gate cieco (P5).

### Step 2 — Alert entro 24h `[AG-A7-HEALTH → AG-A7-COORD]`

L'alert viene notificato ad **AG-A7-COORD** — destinatario unico — **entro 24h** dal
`timestamp_segnale`, e registrato in `agency/a7/alerts/{alert_id}` con `stato: aperto`.

> **GATE BLOCCANTE (R2):** superate le 24h senza alert alzato → escalation automatica ad **AG-DIR**.
> Non è discrezionale: lo esegue `scripts/alert_watchdog.py`.

### Step 3 — Scelta dell'azione correttiva `[AG-A7-COORD]`

Con `churn-prevention` e il playbook `support-90`, sceglie **una** azione:

| Azione | Quando | Chi esegue |
|---|---|---|
| **Check call** | Attrito relazionale, silenzio prolungato, aspettative disallineate | AG-A7-COMM drafta · Max invia |
| **Escalation A4** | Il problema è di **esecuzione**: ticket fermi, SLA sforato, milestone in ritardo | A4-Delivery |
| **Coinvolgimento Max** | Serve una **leva commerciale** (sconto, rimborso, estensione) | **Max** — mai l'agente (R6) |
| **Mediazione scope** | Conflitto su cosa era stato venduto | AG-A7-MID |

> **GATE BLOCCANTE (R6):** nessun agente concede sconti, rimborsi o lavoro extra. Se l'azione
> richiede una leva commerciale, il workflow **si ferma** e passa a Max. Un agente sotto pressione
> relazionale che regala margine è il fallimento più costoso e più silenzioso del reparto.

### Step 4 — Registrazione dell'azione `[AG-A7-COORD]`

L'azione scelta viene scritta in `agency/a7/alerts/{alert_id}` con timestamp e responsabile.
`stato: aperto → in_lavorazione`.

> **GATE BLOCCANTE (R2):** azione **registrata entro 24h** dall'alert. Un'azione decisa ma non
> scritta **non conta**: dal punto di vista dello state, il rischio è ancora non gestito (P3).

### Step 5 — Esecuzione `[AG-A7-COMM | A4-Delivery | AG-A7-MID | Max]`

- **Check call** → AG-A7-COMM drafta sulla voce di Max. Riconosce il problema **esplicitamente**,
  cita i fatti con fonte, **non maschera** il ritardo (P4) e **non promette** date non confermate
  da A4 (R4). L'invio è **umano**.
- **Escalation A4** → richiesta formale ad A4-Delivery sui ticket fermi. A7 **non lavora il ticket**.
- **Leva commerciale** → decisione di Max, poi comunicata da AG-A7-COMM.

> **GATE BLOCCANTE (R4):** draft con claim scoperti (date non confermate, risultati non misurati,
> concessioni non autorizzate) → **non inviabile**. Rework.

### Step 6 — Log del touchpoint `[AG-A7-COMM]`

Ogni contatto generato dall'alert è loggato in `agency/a7/touchpoints/{client_id}`.
AG-A7-HEALTH registra il contatto: il segnale "risposta cliente lenta" si azzera.

> **GATE BLOCCANTE (R3):** un touchpoint non loggato **non è avvenuto**.

### Step 7 — Verifica di rientro `[AG-A7-QA]`

> **GATE BLOCCANTE — chiusura dell'alert:**
> - L'azione correttiva è **registrata** in `agency/a7/alerts`? (non solo decisa)
> - L'azione è stata **eseguita** (touchpoint loggato / escalation emessa)?
> - Il **segnale è rientrato**? (ticket rientrati sotto soglia, cliente tornato reattivo, milestone recuperata)
>
> **PASS** → `stato: chiuso` con esito. AG-A7-HEALTH aggiorna score e trend.
> **FAIL** → l'alert **resta aperto** ed escala ad **AG-DIR**.

**Un alert non si autochiude e non si chiude per decorrenza dei termini.** Lo chiude solo AG-A7-QA,
solo dopo aver verificato che il segnale è **realmente** rientrato.

---

## Output

```json
{
  "alert_id": "ALRT-{client_id}-NNN",
  "client_id": "...",
  "segnali_attivi": [{"segnale": "...", "valore": 3, "soglia": 2}],
  "timestamp_segnale": "ISO-8601",
  "timestamp_alert": "ISO-8601",
  "azione_correttiva": "check_call | escalation_A4 | coinvolgimento_Max | mediazione_scope",
  "timestamp_azione": "ISO-8601",
  "esito": "segnale_rientrato | segnale_persistente | cliente_perso",
  "stato": "aperto | in_lavorazione | chiuso | scaduto",
  "escalation": "nessuna | AG-DIR | Max",
  "namespace_state": "agency/a7/alerts/{alert_id}"
}
```

---

## Handoff

| Direzione | Destinatario | Cosa transita |
|---|---|---|
| ← riceve | **AG-A7-HEALTH** | Segnale oltre soglia, score, timestamp |
| ← riceve | **A4-Delivery** | SLA ticket (read-only) — la fonte principale del segnale |
| → interno | **AG-A7-COORD** | Alert da lavorare entro 24h (destinatario unico) |
| → interno | **AG-A7-COMM** | Draft della check call (invio umano) |
| → interno | **AG-A7-MID** | Mediazione su conflitto di scope |
| → esterno | **A4-Delivery** | Escalation tecnica su ticket fermi / SLA sforato |
| ↕ escalation | **AG-DIR** | Alert scaduto (>24h) · segnale non rientrato · FAIL ripetuto |
| ↕ escalation | **Max** | Qualsiasi leva commerciale (R6) — **sempre**, mai l'agente |
| → uscita | **AG-A7-CLOSE** | Storico alert: contesto per la lettura dell'NPS a G+90 |

---

## DONE-WHEN

L'alert è chiuso quando **tutte** queste condizioni sono vere:

- [ ] L'alert è stato alzato **entro 24h** dal `timestamp_segnale` (R2)
- [ ] Un'azione correttiva è **registrata** in `agency/a7/alerts/{alert_id}` entro 24h dall'alert (R2)
- [ ] L'azione è stata **eseguita** e il touchpoint (se previsto) è **loggato** (R3)
- [ ] Nessun claim scoperto è uscito verso il cliente (R4) e nessuna leva commerciale è stata
      concessa da un agente (R6)
- [ ] Il **segnale è rientrato**, verificato da AG-A7-QA sui dati, non sull'impressione
- [ ] **AG-A7-QA ha emesso PASS** → `stato: chiuso` con esito registrato
- [ ] AG-A7-HEALTH ha aggiornato score e trend in `agency/a7/health/{client_id}`

**Se il segnale non rientra:** l'alert **resta aperto** ed escala ad AG-DIR. Un alert aperto oltre
la finestra non è un fallimento del cliente — è un fallimento del processo, e va trattato come tale.

---

## Connessioni

- [[ag-a7-health]] · `agenti/ag-a7-health.md` — rilevatore del segnale, owner della dashboard
- [[ag-a7-coord]] · `agenti/ag-a7-coord.md` — destinatario unico dell'alert, sceglie l'azione
- [[ag-a7-qa]] · `agenti/ag-a7-qa.md` — unico agente che può chiudere un alert
- [[WF-CUSTOMER-LIFECYCLE]] · `workflow/WF-CUSTOMER-LIFECYCLE.md` — gira in parallelo
- [[A4-Delivery]] · `../A4-Delivery/` — produttore dell'SLA ticket e destinatario dell'escalation tecnica
