---
Type: CONCEPT
Status: Active
Tags: #workflow #cfo #spend-approval #dry-run #mandato #cf-grade
Created: 2026-06-17
Last updated: 2026-06-17
---

# WF-SPEND-APPROVAL — Workflow Approvazione Spesa API

> **Tipo:** CF-grade · **Figura:** CFO
> **Blueprint:** `company/Board-CSuite/_BLUEPRINT/BP-CFO.md`
> **Connessioni:** [[WF-BUDGET]] · [[cfo-spend-approver]] · [[cfo-tier-router]] · [[cfo-budget-guard]]

---

## Scopo

Gestire il percorso obbligatorio di ogni spesa API reale dalla stima all'approvazione esplicita.
Il Mandato Art.4.3 lo impone senza eccezioni: prima si stima (dry-run), poi si approva (ok esplicito),
poi si esegue. Non esiste inversione di questo ordine. Il workflow garantisce che l'approval_id
esista sempre prima dell'esecuzione e che il sistema di stima sia calibrato nel tempo.

---

## Trigger

- Ecosistema richiede di eseguire un run che supera la soglia di approvazione autonoma.
- `cfo-budget-guard` riceve un check pre-run e necessita del dry-run prima di autorizzare.
- Richiesta di override esplicito su un run bloccato.
- Audit retroattivo su run eseguiti senza approval_id (rilevato da `cfo-cost-accountant`).

---

## Agenti coinvolti

| Agente | Fase | Ruolo nel workflow |
|---|---|---|
| `cfo-tier-router` | 1 | Valida il tier prima del dry-run |
| `cfo-spend-approver` | 2, 3, 4 | Valida il dry-run, emette / rifiuta approval_id |
| `cfo-budget-guard` | 2 | Conferma disponibilità budget per il costo stimato |
| `cfo-conductor` | 3, 5 | Decide su escalation; firma override se necessario |
| `cfo-cost-accountant` | 5 | Riceve l'approval_id e lo registra nel ledger post-run |

---

## Flusso passo-passo

```
STEP 0 — RICEZIONE RICHIESTA
├─ Input: { run_id, ecosistema, task_descrizione, tier_pianificato,
            costo_stimato, metodo_stima }
├─ cfo-spend-approver: verifica completezza dei campi
│   Campo mancante → richiede completamento prima di procedere
└─ Output: richiesta validata (campi completi) o rifiuto per dati incompleti

STEP 1 — VALIDAZIONE TIER (prima del dry-run)
├─ cfo-tier-router: il tier pianificato è corretto per il task?
│   Anomalia → declassa il tier; aggiorna la richiesta
│   Ok → procede
└─ Output: tier confermato / corretto

STEP 2 — DRY-RUN CHECK
├─ cfo-spend-approver valuta il metodo di stima:
│   "token_count" → accettato (metodo diretto)
│   "analogia_run_precedente" → accettato se run_id di riferimento esiste nel ledger
│   "stima_manuale" → accettato solo se fornita spiegazione del ragionamento
│   Metodo non documentato → RIFIUTO: richiede dry-run con metodo valido
├─ cfo-budget-guard: costo_stimato ≤ budget_residuo?
│   Sì → budget check pass
│   No → BLOCCO: segnala al conductor per decisione
└─ Output: dry_run_valid: boolean + budget_check: "pass | block"

STEP 3 — DECISIONE APPROVAZIONE
├─ Sotto soglia autonoma E dry_run_valid E budget_check pass →
│   cfo-spend-approver emette approval_id (autonomo)
│
├─ Sopra soglia autonoma →
│   cfo-spend-approver prepara dossier: { run_id, costo, tier, giustificazione }
│   Scala al conductor con RACCOMANDAZIONE: "approvo / non approvo perché..."
│   Conductor decide; traccia la decisione
│
└─ Override richiesto (run bloccato da budget) →
    Conductor valuta: giustificazione valida? Sì → firma override + motivo.
    Override senza giustificazione esplicita: VIETATO.

STEP 4 — EMISSIONE APPROVAL_ID
├─ Se approvato: cfo-spend-approver genera APPR-YYYYMMDD-NNN
├─ Scrive in: board/cfo/approvals-pending → rimuove da pending
├─ Scrive in: state/approvals/APPR-YYYYMMDD-NNN.json (record permanente)
└─ Output: { approval_id, costo_approvato, tier_approvato, validita }

STEP 5 — POST-ESECUZIONE
├─ Dopo il run: cfo-cost-accountant riceve { run_id, costo_effettivo, approval_id }
├─ Verifica: approval_id presente nel record state/approvals/? Sì → ok.
├─ Discrepanza costo_stimato vs. costo_effettivo > soglia [DM]?
│   Sì → notifica cfo-forecast-finance per ricalibrazione
└─ Output: entry ledger con approval_id registrato

STEP 6 — CHIUSURA
├─ cfo-spend-approver: aggiorna stato approval a "eseguito_verificato"
├─ cfo-conductor: log workflow chiuso
└─ Se audit retroattivo: identifica run senza approval_id → anomalia da risolvere
```

---

## Gate del workflow

| Gate | Posizione | Tipo | Condizione per passare |
|---|---|---|---|
| Campi completi | Step 0 | Bloccante | Tutti i campi obbligatori presenti |
| Tier corretto | Step 1 | Bloccante | Tier validato da `cfo-tier-router` |
| Dry-run con metodo | Step 2 | Bloccante (Art.4.3) | Metodo stima documentato e valido |
| Budget disponibile | Step 2 | Bloccante | Budget check pass da `cfo-budget-guard` |
| Soglia / escalation | Step 3 | Governance | Sopra soglia → sempre al conductor |
| Approval retroattiva | Step 6 | Bloccante | Mai: se richiesta a posteriori → rifiuto + tracciamento violazione |

---

## Casi speciali

**Override su run bloccato:**
Se un ecosistema richiede di sbloccare un run bloccato da `cfo-budget-guard` per budget
insufficiente: il conductor può emettere un override esplicito SOLO con:
- Giustificazione scritta (perché questo run vale la deroga).
- Dichiarazione esplicita della fonte alternativa (da dove verrà coperto il costo extra).
- Tracciamento nel log della sessione come "override budget autorizzato".

**Approvazione retroattiva — VIETATA:**
Se `cfo-cost-accountant` rileva un run eseguito senza approval_id → segnala come violazione
Art.4.3. Il conductor documenta la violazione. Non si rilascia un approval_id retroattivo:
la violazione è tracciata e il sistema non viene "ripulito" eliminando la traccia.

---

## Input del workflow

```json
{
  "tipo": "approval_request | override_request | audit_retroattivo",
  "run_id": "RUN-YYYYMMDD-NNN",
  "ecosistema": "01-AGENCY | ...",
  "task_descrizione": "testo sintetico",
  "tier_pianificato": "haiku | sonnet | opus | wasm",
  "costo_stimato": "number",
  "metodo_stima": "token_count | analogia_run_precedente | stima_manuale",
  "giustificazione_override": "testo | null"
}
```

## Output del workflow

```json
{
  "workflow_id": "WF-SPEND-YYYYMMDD-NNN",
  "esito": "approval_emessa | rifiuto | escalato_conductor | override_firmato | violazione_retroattiva",
  "approval_id": "APPR-YYYYMMDD-NNN | null",
  "motivo_rifiuto": "testo | null",
  "costo_approvato": "number | null",
  "tier_approvato": "haiku | sonnet | opus | wasm | null",
  "override": "boolean",
  "giustificazione_override": "testo | null"
}
```

---

## State

- Approvazioni pendenti: `board/cfo/approvals-pending`.
- Approvazioni emesse (record permanenti): `state/approvals/APPR-YYYYMMDD-NNN.json`.
- Log violazioni: `state/violations/violation_YYYYMMDD.json`.

---

## Connessioni

- [[cfo-spend-approver]] · `agenti/cfo-spend-approver.md`
- [[cfo-tier-router]] · `agenti/cfo-tier-router.md`
- [[cfo-budget-guard]] · `agenti/cfo-budget-guard.md`
- [[cfo-conductor]] · `agenti/cfo-conductor.md`
- [[cfo-cost-accountant]] · `agenti/cfo-cost-accountant.md`
- [[WF-BUDGET]] · `workflow/WF-BUDGET.md`
- [[REGOLE]] · `regole/REGOLE.md`
- [[13-DOSSIER-MANDATO-ECOSISTEMA]] · `PIANO-MAESTRO/13-DOSSIER-MANDATO-ECOSISTEMA.md`
