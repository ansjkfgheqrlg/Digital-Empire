# 👤 IDENTITY-HR — Registro unico degli agenti

> Fonte: PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md sez. 1.4
> **Backbone component.** La fonte di verità su "chi lavora qui": ogni agente anagrafato
> con ruolo, costo, performance. La FORGE assume (registra alla creazione) e ritira.
> Collegato a: [[GRUPPO.md]] · [[company/Backbone/README.md]]

---

## File principale

`Identity-HR/registro-agenti.yaml` — ✅ PRESENTE (19 agenti censiti F2)
Vista generata (NON modificare a mano): registro-agenti.md (da generare F2)
Persistenza runtime: `company/runtime/identity/agents.jsonl`
Namespace AgentDB: `identity/`

---

## Schema record (YAML tipato)

```yaml
- id: AGY-ACQ-email-writer-01        # <ECO>-<REPARTO>-<ruolo>-<seq>
  ecosistema: AGENCY
  reparto: Acquisizione
  team: WF-OUTREACH-EMAIL
  ruolo: worker                       # coordinator | worker | sentinel | guild-lead
  tier_modello: 2                     # 0=WASM 1=Haiku 2=Sonnet 3=Opus (policy §2.3 dossier 07)
  costo:
    stimato_run: 0.04                 # USD per singola invocazione
    cumulativo_30g: 1.20              # USD ultimi 30 giorni
  performance:
    task_done: 87
    pass_rate_gate: 0.94              # % handoff approvati al primo tentativo
    reject_rate: 0.03                 # % handoff rejected dal destinatario
  stato: active                       # active | idle | retired
  assunto: 2026-06-15
  da: FORGE
```

---

## Ciclo di vita degli agenti

```
FORGE agent_spawn
    → record creato in registro-agenti.yaml (stato: active)
    → namespace AgentDB identity/ aggiornato
         ↓
Observability aggiorna costo/performance ad ogni run
         ↓
Pass_rate < soglia (< 85%) o idle > 14 giorni
    → Cost-Sentinel / Quality-Sentinel segnalano
         ↓
FORGE agent_terminate
    → stato: retired (mai cancellato: storia = apprendimento)
    → record in history/ per ReasoningBank
```

**Invariante:** nessun agente viene cancellato; solo `stato: retired`. I retired alimentano il ReasoningBank con i pattern di fallimento.

---

## Agenti censiti (F2 — 19 agenti)

### Board / C-Suite (L0 — 7 agenti)

| ID | Nome | Tier | KPI primario |
|---|---|---|---|
| `empire-conductor` | CEO / Empire-Conductor | Opus | decisioni cross-ecosistema risolte/sessione |
| `empire-coo` | COO | Sonnet | uptime sistema + blocchi risolti in < 2h |
| `empire-cto` | CTO | Sonnet/Opus | verify.sh verde + ADR per decisioni arch. |
| `empire-cmo` | CMO | Sonnet | score APSOC medio ≥ 80 + brand gate pass > 70% |
| `empire-cro` | CRO | Sonnet | lead/settimana + tasso chiusura preventivo |
| `empire-cfo` | CFO | Haiku/Sonnet | budget overrun 0 + dry-run compliance 100% |
| `empire-chief-forge` | Chief Forge | Opus | skill con eval gate superato 100% |

### Backbone (2 agenti)

| ID | Nome | Tier | KPI primario |
|---|---|---|---|
| `backbone-bus-coordinator` | Bus Coordinator | Haiku | backlog pending > 24h = 0 |
| `backbone-brain-syncer` | Brain Syncer (wiki-syncer) | Haiku | lag wiki/AgentDB < 24h |

### Guild Masters (5 agenti)

| ID | Nome | Guild | Tier |
|---|---|---|---|
| `guild-master-prompt` | Prompt Guild Master | Prompt | Sonnet |
| `guild-master-copy` | Copy/APSOC Guild Master | Copy-APSOC | Sonnet |
| `guild-master-quality` | Quality Guild Master | Quality | Sonnet |
| `guild-master-cost` | Cost Guild Master | Cost | Haiku |
| `guild-master-design` | Design Guild Master | Design | Haiku |

### Sentinels (5 agenti)

| ID | Nome | Tier | Supervisore |
|---|---|---|---|
| `sentinel-cost` | Cost Sentinel | Haiku | CFO |
| `sentinel-quality` | Quality Sentinel | Sonnet | CMO |
| `sentinel-drift` | Drift Sentinel | Sonnet | CTO |
| `sentinel-security` | Security Sentinel | Haiku | CTO |
| `sentinel-brandvoice` | BrandVoice Sentinel | Haiku/Sonnet | CMO |

---

## Agenti da censire (F3 — migrazione asset)

L1-L5 agents (coordinatori ed executor per ecosistema):
- AGENCY: A1-Researcher, A2-Outreach, A3-Preventivi, A4-Delivery, A5-Copy, A6-Marketing + workers
- MARKETING: A1-A8 (Copy-Workflow team), S1-S3 (style agents)
- CONTENT-FACTORY: team Strategia, Video, Testuale, Visual
- Totale stimato: ~180+ agenti su tutti i livelli L2-L5

Query operative (dopo init): `agent_list --stato active`, `agent_list --eco AGENCY`, `grep "tier_modello: 3" registro-agenti.yaml`

---

## Differenza vs CF Exponium

CF usa registro md + jsonl senza tier modello né performance strutturata; DE impone YAML tipato con `tier_modello`, `pass_rate_gate` e costo cumulativo — necessari perché i 10 ecosistemi condividono budget e il routing 3-tier è policy.

---

## Stato

- `registro-agenti.yaml` — ✅ PRESENTE (19 agenti: 7 Board + 2 Backbone + 5 Guild + 5 Sentinel)
- Schema YAML tipato — ✅ definito
- L1-L5 agents — ⏳ da censire in F3 (migrazione asset)
- Vista registro-agenti.md — ⏳ da generare (F2, task 2.6)
- Ciclo hire/retire automatico FORGE — ⏳ da costruire (F8)
