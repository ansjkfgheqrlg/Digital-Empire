---
Type: README
Status: Active
Tags: #state #namespace #agentdb #no-pii #partnership #agency #A9
Created: 2026-07-11
Last updated: 2026-07-11
---

# state/ — A9 Partnership & Referral

> Namespace di memoria: **`agency/a9`**.
> Regola sovrana: **zero PII** (R4). In state si scrivono **riferimenti**, mai persone.

---

## 1. Namespace

| Chiave | Contenuto | Owner scrittura | Lettura |
|---|---|---|---|
| `agency/a9/partners/{partner_id}` | Anagrafica e stato del partner | `AG-A9-MGMT`, `AG-A9-OUTREACH` (campo `outreach`), `AG-A9-QA` (campo `gate_status`) | tutto A9, AG-DIR |
| `agency/a9/referrals/{referral_id}` | Referral ricevuto: origine, ICP, consenso, gate, routing, esito | `AG-A9-MGMT` (intake), `AG-A9-QA` (gate), `AG-A9-COORD` (routing) | tutto A9, A2, A8 |
| `agency/a9/nonicp/{lead_ref}` | Esito del triage non-ICP | `AG-A9-QUALIFY` | tutto A9 |
| `agency/a9/nurture/{lead_ref}` | Lead parcheggiato + data risveglio | `AG-A9-QUALIFY` | tutto A9 |
| `agency/a9/archive/{lead_ref}` | Lead archiviato + motivo (append-only) | `AG-A9-QUALIFY` | tutto A9 |
| `agency/a9/commissions/{deal_id}` | Commissione: importo da catalogo, stato, contratto | `AG-A9-MGMT`, `AG-A9-QA` (gate) | AG-DIR |
| `agency/a9/intel/*` | KPI e partner scorecard | `AG-A9-INTEL` | AG-DIR |
| `agency/a9/runs/{run_id}` | Stato di esecuzione di un workflow | agente che esegue lo step | tutto A9 |

---

## 2. Schema FS

```
agency/a9/
├── partners/
│   └── {partner_id}.json          # PT-0001, PT-0002, ...
├── referrals/
│   └── {referral_id}.json         # RF-0001, ...
├── nonicp/
│   └── {lead_ref}.json            # LD-XXXX (esito triage)
├── nurture/
│   └── {lead_ref}.json            # LD-XXXX (+ data_risveglio)
├── archive/
│   └── {lead_ref}.json            # append-only
├── commissions/
│   └── {deal_id}.json             # DL-XXXX
├── intel/
│   ├── kpi.json
│   └── partner-scorecard/{partner_id}.json
└── runs/
    └── {run_id}.json              # state.json di workflow
```

### `partners/{partner_id}.json`
```json
{
  "partner_id": "PT-0001",
  "tipo": "agenzia-no-ai",
  "azienda": "string",
  "stato": "candidato | attivo | sospeso",
  "accordo": { "firmato": false, "data_firma": null },
  "commissione_catalogo_id": "CAT-REF-XX",
  "data_briefing": null,
  "gate_status": "pending | PASS | FAIL",
  "fail_count": 0,
  "last_updated": "YYYY-MM-DDThh:mm:ssZ"
}
```

### `referrals/{referral_id}.json`
```json
{
  "referral_id": "RF-0001",
  "origine": "partner | a7-cliente",
  "partner_id": "PT-0001",
  "lead_ref": "LD-XXXX",
  "icp_status": "completo | incompleto",
  "consent": { "flag": false, "data": null, "fonte": null },
  "gate_status": "pending | PASS | FAIL",
  "motivo_fail": null,
  "routing": "A8-fast-track | A2-outreach | respinto | hold",
  "esito": "aperto | chiuso-vinto | chiuso-perso",
  "last_updated": "YYYY-MM-DDThh:mm:ssZ"
}
```

### `runs/{run_id}.json`
```json
{
  "run_id": "A9-YYYYMMDD-NNN",
  "workflow": "WF-PARTNER-ONBOARDING | WF-REFERRAL-PIPELINE | WF-NONICP-ROUTING",
  "step_corrente": "string",
  "gate_status": "pending | PASS | FAIL",
  "motivo": null,
  "batch": { "lead_totali": 0, "lead_con_esito": 0 },
  "next_action": "string",
  "last_updated": "YYYY-MM-DDThh:mm:ssZ"
}
```

---

## 3. Lifecycle

| Entità | Stati |
|---|---|
| **Partner** | `candidato` → (accordo firmato + commissione catalogo + briefing) → **`attivo`** → (≥2 FAIL consenso) → `sospeso` → (nuovo briefing + revoca scritta) → `attivo` |
| **Referral** | `ricevuto` → `gate:pending` → **`PASS`** → `routing:A8/A2` → `esito` · oppure **`FAIL`** → `respinto` (motivo al partner) |
| **Lead non-ICP** | `in-triage` → `PARTNER_POTENZIALE` (→ onboarding) · `NURTURE` (→ risveglio) · `ARCHIVIO` (append-only) · `ambiguo` → escalation COORD |
| **Commissione** | `hold` → (contratto firmato **+** deal confermato da A8) → **`maturata`** → `pagata` |
| **Run** | `open` → `gate:pending` → `PASS`/`FAIL` → `closed` (mai `closed` con Zero-Loss < 100%) |

**Ripartibilità a freddo:** `runs/{run_id}.json` contiene `step_corrente` + `next_action`.
Un agente rientra dal punto esatto di interruzione senza riestrarre il contesto (test amnesia V2).

---

## 4. Accessi

| Namespace esterno | Accesso A9 |
|---|---|
| `agency/a1/leads` | **Read-only** — batch non-ICP |
| `agency/a2/pipeline` | **Read-only** — check ownership + confronto conversione |
| `agency/a8/deals` | **Read-only** — conferma deal chiusi (commissioni) |
| `agency/clients` | **Read-only** — anti-duplicato referral |
| Catalogo commissioni (A3) | **Read-only** — fonte di verità pricing |
| `agency/kpi` | **Write** — solo `AG-A9-INTEL`, sezione A9 |

---

## 5. Divieti (bloccanti)

1. **Nessuna PII** in nessun file di `agency/a9/*`: vietati nome/cognome persona, email, telefono,
   indirizzo, link a profili personali. Ammessi: `lead_ref`, `partner_id`, azienda, ruolo, settore (R4).
2. Il consenso si scrive **solo** come `{flag, data, fonte}` — mai come copia del dato personale (R3).
3. `gate_status` è **immutabile** una volta scritto da `AG-A9-QA`: un nuovo tentativo apre un nuovo
   `run_id`, non sovrascrive il verdetto precedente.
4. `archive/` è **append-only**: un lead archiviato non si cancella, si risveglia con un nuovo record.
5. Nessuna scrittura A9 fuori da `agency/a9/*` (eccetto la sezione A9 di `agency/kpi`).

---

## Connessioni

- [[ARCHITETTURA]] · `ARCHITETTURA.md` §8 — mappa namespace
- [[REGOLE]] · `regole/REGOLE.md` — R3 (consenso), R4 (zero PII), R5 (Zero-Loss)
- [[scripts/README]] · `scripts/README.md` — automazioni che leggono/scrivono questi schemi
