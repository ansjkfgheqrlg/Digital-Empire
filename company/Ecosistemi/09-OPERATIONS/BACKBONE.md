# BACKBONE — 🔧 09-OPERATIONS

> Come OPERATIONS si collega al Corporate Backbone di EMPIRE OS.
> Organigramma completo: `company/GRUPPO.md` · Dettagli tecnici: `company/Backbone/`
> Dossier: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §09 + `07-BACKBONE-RUFLO-SKILLS.md`

## COORDINATION (Ruflo) — Topologia: **MESH**

OPERATIONS gira in **mesh**: ogni suo agente può parlare direttamente con ogni
ecosistema, senza passare per una radice. Motivo: è l'ecosistema di servizio che
**osserva e serve tutti contemporaneamente** —

- `ops-cost-sentinel` deve poter bloccare una spesa di QUALSIASI ecosistema in tempo reale;
- `ops-watchdog` deve poter interrogare lo stato di QUALSIASI run senza coda;
- `ops-scheduler` lancia run per conto di tutti, su trigger temporali indipendenti.

Una gerarchia introdurrebbe latenza proprio dove serve reattività (blocco pre-sforo,
alert). Il coordinamento interno resta sotto `ops-director`, ma il piano dati (eventi
costo, health, alert) è mesh.

```
ruflo swarm init --topology mesh --namespace operations
```

**Eccezione:** WF-SWARM-RUN spawna sotto-swarm **hierarchical** temporanei
(`ops-swarm-marshal` come coordinator dei worker) — la mesh è la rete stabile,
i sotto-swarm sono usa-e-getta per batch.

**Fallback senza daemon (rischio #5, daemon Windows):** pattern ibrido ADR-005 di CF —
script bash/ps1 + file jsonl in `company/runtime/` ; il watchdog rileva il daemon giù
e attiva il fallback auto-riparante.

## BUS (Message bus)

**Inbound (riceve):**
- richiesta run ← qualsiasi ecosistema: `{workflow, parametri, budget_max, schedule, brand_kit}`
- registrazione cost model ← FORGE (nuovo agente/team: tier + costo stimato/run)

**Outbound (manda):**
- run result → richiedente: `{esito, costo, durata, output_paths}`
- alert → ecosistema interessato + CFO: budget 80%, run fallita, drift costo, zombie
- report costi settimanale → Board (L0)
- eventi run chiuse → 10-MEMORY (HC-ME-POST, il CP include i costi)

Handoff contract standard (pattern #2 — `acceptance_criteria` obbligatori, senza = INVALIDO):
```json
{
  "id": "H-YYYYMMDD-NNNN",
  "from": "<ECOSISTEMA>/<reparto>/<workflow>",
  "to": "OPERATIONS/SCHEDULING/WF-CRON",
  "type": "directive|handoff|result|escalation",
  "payload": { "workflow": "...", "budget_max": 0, "schedule": "cron-expr", "brand_kit": "DE|<cliente>" },
  "acceptance_criteria": ["evento costo emesso", "report esito entro SLA", "0 sforamenti"],
  "status": "pending|accepted|in_progress|done|rejected|escalated"
}
```

## BRAIN (Memoria)

**Namespace AgentDB dichiarati:**

| Namespace | Contenuto | Chi scrive |
|---|---|---|
| `operations/cost` | eventi costo per run/agente/commessa | ops-cost-accountant |
| `operations/ledger` | aggregati settimanali per ecosistema | ops-cost-accountant |
| `operations/schedule` | calendario run, esiti cron | ops-scheduler |
| `operations/swarm-state` | stato swarm attivi, code, retry | ops-swarm-marshal |
| `operations/assets` | indice asset: naming, dedup hash, retention | ops-asset-keeper |
| `operations/health` | health check, token in scadenza, incidenti | ops-watchdog |

Fonte di verità umana: `second-brain-vault/wiki/` (post-mortem run → `concepts/`/`synthesis/`
via INTELLIGENCE). Pattern di fallimento run → ReasoningBank (`patterns/`).

## GOVERNANCE (Gate qualità)

- `G-DRYRUN` — ogni workflow nuovo gira prima in dry-run con stima costi (pattern #3)
- `G-BUDGET` — budget dichiarato e approvato prima della run reale (pattern #9)
- `G-ATTRIBUTION` — run senza evento costo = run non valida
- `G-RUNBOOK` — ogni workflow schedulato ha runbook + rollback
- Verifica struttura: `scripts/verify-empire.sh` (da creare in F2) — categoria check OPERATIONS:
  ledger coerente, 0 run orfane, 0 schedule senza runbook

## IDENTITY-HR (Registro agenti)

I 10 agenti `ops-*` (schede in `Agenti/`) vanno censiti in
`company/Backbone/Identity-HR/registro-agenti.yaml` con tier e costo stimato/run.
Assunzioni/ritiri: solo tramite 07-FORGE → Chief-Forge → registro. OPERATIONS ha un
ruolo speciale: **valida il cost model** di OGNI nuovo agente della holding prima
che la FORGE lo deployi (handoff FORGE → OPERATIONS).

## OBSERVABILITY

OPERATIONS è l'OPERATORE del componente Observability del Backbone: metrics,
cost-attribution e dashboard sono i suoi deliverable (WF-DASHBOARD, WF-ATTRIBUTION).
Le altre business unit consumano; OPERATIONS produce.

*Aggiornato: 2026-06-11 · Fonte: dossier 06 §09 + dossier 07*
