# 💸 Cost Sentinel

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 4.1
> **Sentinel always-on.** Autorità di enforcement LX.
> Supervisore C-Suite: CFO (empire-cfo)
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/Governance/README.md]]

---

## Identità

| Campo | Valore |
|---|---|
| **ID registro** | SENT-COST-001 (`Backbone/Identity-HR/registro-agenti.yaml`) |
| **Ruolo** | Sentinel autonomo always-on — enforcement budget |
| **Tier** | L0-Sentinel (sopra gli ecosistemi, risponde a LX e CFO) |
| **Modello** | Haiku (monitoraggio continuo) / Sonnet (analisi crisi) |
| **Namespace AgentDB** | `patterns/incidents/cost/` |

---

## Cosa osserva

- Crediti API consumati per agente, per team, per ecosistema, per brand_kit (multi-tenant)
- Tier modello usato vs tier previsto dalla routing policy 3-tier (`07-BACKBONE` §2.3)
- Agenti in loop (velocità di chiamata API > 20x normale per > 2 minuti)
- Utilizzo Opus su task classificati Tier 0 o Tier 1 (violazione routing policy)
- Dry-run eseguito o non eseguito prima del run reale (pattern #3 Piano Maestro §6)

---

## Soglie e trigger

| Soglia | Condizione | Azione automatica |
|---|---|---|
| **60% envelope ecosistema** | spesa raggiunge il 60% del budget mensile autorizzato | Log in `patterns/incidents/cost/` · notifica CFO via gbus |
| **80% envelope** | spesa raggiunge l'80% | Warning a CFO + COO + CEO via gbus `priority: HIGH` |
| **95% envelope** | spesa raggiunge il 95% | Blocco task non urgenti nell'ecosistema; escalation CFO |
| **100% + accelerazione** | budget esaurito con run ancora in corso | Crisi: stop immediato task, escalation CEO via hive-mind |
| **Opus su Tier ≤1** | modello Opus usato per classificazione/parsing/tagging | Segnalazione al team + CFO; raccomandazione downgrade |
| **Agente in loop** | >20 chiamate/min per >2 min consecutivi | Sospensione agente; notifica CTO e CFO |
| **Dry-run saltato** | run reale senza dry-run registrato | Blocco esecuzione; richiesta dry-run preventivo |

---

## Azioni quando scatta

1. **Log immediato** — deposita evento in `company/runtime/metrics/runs.jsonl` con `{tipo: cost_alert, eco, agente, importo, soglia_toccata, ts}`.
2. **Notifica via gbus** — messaggio `type: escalation, priority: HIGH` al CFO e al reparto impattato.
3. **Blocco preventivo** — se la soglia è ≥95%: blocca task non urgenti (urgenza = `priority: CRITICAL` nel handoff).
4. **Raccomandazione routing** — suggerisce downgrade modello con stima risparmio.
5. **Deposito in ReasoningBank** — ogni intervento finisce in `patterns/incidents/cost/` per auto-calibrazione soglie.

---

## Input / Output

**Input atteso (via Bus):**
```json
{
  "tipo": "run_start | run_done | budget_query",
  "ecosistema": "01-AGENCY | ...",
  "agente": "AGY-ACQ-email-writer-01",
  "tier_modello": 2,
  "costo_stimato": 0.04,
  "dry_run_eseguito": true,
  "brand_kit": "DE | <cliente>"
}
```

**Output prodotto:**
```json
{
  "approvato": true,
  "alert_level": "verde | giallo | arancio | rosso",
  "budget_residuo_ecosistema": 0,
  "raccomandazione": "downgrade a Haiku stimato risparmio 80%",
  "incident_id": "INC-COST-20260611-001"
}
```

---

## KPI

| Metrica | Target |
|---|---|
| Budget overrun senza alert preventivo | 0 |
| Task con Opus su Tier ≤1 non segnalati | 0 |
| Dry-run saltati non rilevati | 0 |
| Interventi depositati nel ReasoningBank | 100% |
| Latenza alert dalla soglia | < 30 secondi (quando daemon attivo) |

---

## Escalation

| Destinatario | Quando | Canale |
|---|---|---|
| CFO | qualsiasi alert ≥60% | gbus `type: escalation` |
| CEO | crisi 100%+ o loop agente | hive-mind raft |
| CTO | agente in loop o tier anomalo | gbus `priority: HIGH` |

---

## Skill operative

- `budget-guard` — da forgiare P0 (Backbone/Governance) — wrapper del Sentinel per invocazione manuale
- `empire-cost` — stima dry-run di un workflow (§3.2 dossier 07)
- Fallback manuale (F1-F3): checklist CFO prima di ogni run costoso

---

## Stato

Struttura definita (F1). Implementazione automatica da costruire in F2-F5.
Nelle prime fasi (F1-F3): eseguito manualmente come checklist dal fondatore o da Claude.