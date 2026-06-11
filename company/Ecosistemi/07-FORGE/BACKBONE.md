# BACKBONE — 🔨 07-FORGE

> Come FORGE si collega al Corporate Backbone di EMPIRE OS.
> Organigramma completo: `company/GRUPPO.md` · Dettagli tecnici: `company/Backbone/`
> Fonte topologie e namespace: `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md`

---

## Topologia swarm: STAR (hub = i motori della forgia)

```
                    WF-SKILL-AUDIT          WF-PRD
                          │                   │
   WF-SKILL-IMPROVE ──┐   │   ┌── WF-AGENT-NEW
                      ▼   ▼   ▼
              ┌─────────────────────────┐
              │   HUB DELLA FORGIA      │
              │  skill-creator +        │
              │  content-forge (MKD)    │
              │  [+ omega-create per    │
              │   progetti Browser]     │
              └─────────────────────────┘
                      ▲   ▲   ▲
    WF-TEAM-NEW ──────┘   │   └────── WF-ECOSYSTEM-NEW
                          │
                  WF-FORGE-PIPELINE
```

**Perché star:** ogni nuovo asset organizzativo nasce dal centro e viene validato lì.
I raggi (workflow L3) non si parlano tra loro direttamente: tutto passa per il hub,
dove vivono i due motori reali (skill-creator, content-forge) e i gate
(G-MKD, G-EVAL, G-CONTRADICTION). Questo impedisce che due workflow producano
artefatti divergenti dallo stesso ordine. `frg-chief` siede al centro della stella.

Init: `ruflo swarm_init --topology star --namespace forge` (parallelismo consentito
sui raggi: più skill forgiabili in parallelo, validazione sempre centralizzata).

## BUS (Message bus)

**Inbound (riceve da TUTTI):** la FORGE è il fornitore universale di capability.

| Da | Payload |
|---|---|
| QUALSIASI ecosistema | `{capability_mancante, contesto, KPI_attesi, budget}` — ordine di build |
| INTELLIGENCE | materiale raw ingerito (Empire Studio) + pattern ReasoningBank — materia prima |
| LX / Board | mandato per nuovi ecosistemi interi (es. F9+: E-commerce) |

**Outbound (consegna):**

| A | Payload |
|---|---|
| Ecosistema richiedente | **asset installato** (skill in `.claude/skills/`, agente/team nel reparto target) + eval report |
| INTELLIGENCE | ogni artefatto creato → pagina wiki `tools/` + log; enrichment skill esistenti passa per Memory Empire |
| OPERATIONS | ogni nuovo agente dichiara tier modello + costo stimato → budget guard pre-approvazione |
| Backbone Identity-HR | assunzione/ritiro agenti: `registro-agenti.yaml` aggiornato a ogni forgiatura |

Handoff contract standard (ogni ordine e ogni consegna):
```json
{
  "from": "<ecosistema_richiedente> | FORGE",
  "to": "FORGE | <ecosistema_destinazione>",
  "payload": {
    "tipo": "skill | agente | team | workflow | ecosistema",
    "capability_mancante": "",
    "contesto": "",
    "kpi_attesi": [],
    "budget": ""
  },
  "acceptance_criteria": [
    "G-SPEC, G-MKD/PRD, G-EVAL, G-CONTRADICTION, G-REGISTRY superati",
    "artefatto installato e funzionante presso il richiedente",
    "eval report allegato"
  ],
  "status": "pending | fulfilled | rejected"
}
```

## BRAIN (Memoria)

**Namespace AgentDB:** `forge/builds` (ordini e build in corso) · `forge/evals`
(risultati eval e benchmark) · `forge/registry` (specchio operativo di Identity-HR) ·
`forge/templates` (template agenti/skill — vedi dossier 07 §namespace).

Ogni agente frg-* legge/scrive SOLO in questi namespace. Pattern dai fallimenti di
forgiatura → ReasoningBank (`reasoningbank-*` via Ruflo).
Fonte di verità umana: `second-brain-vault/wiki/tools/` (ogni artefatto forgiato ha pagina wiki).
Memoria operativa (checkpoint, ADR): ecosistema 10 MEMORY (`company/Memory/`) — memory-first #13.

## GOVERNANCE (Gate qualità)

Catena gate FORGE: **G-SPEC → G-MKD/PRD → G-EVAL → G-CONTRADICTION → G-REGISTRY**
(dettaglio in `ECOSISTEMA.md` §6). In più: pattern #7 progressive disclosure
(kernel ≤500 righe) e pattern #1 schema team canonico verificati a ogni audit.
Verifica struttura: `scripts/verify-empire.ps1` (creato in F2, PASS 59/59).

## IDENTITY-HR (Registro agenti)

La FORGE è l'**operatore** di Identity-HR per tutta la holding: è l'unico ecosistema
che assume e ritira. Registro: `company/Backbone/Identity-HR/registro-agenti.yaml`.
Ciclo di vita: `agent_spawn` → record creato → Observability aggiorna costo/performance →
pass_rate < soglia o idle > 14g → segnalazione → FORGE ritira (`agent_terminate`).
Agenti propri della FORGE (frg-*): censiti nello stesso registro, owner = Chief-Forge.

## OBSERVABILITY

Ogni forgiatura emette evento `{ordine, artefatto, durata, eval_score, costo}` verso
OPERATIONS (cost attribution). Report trimestrale `forge-metrics` (skill da creare, BASSA).

## COORDINATION (Ruflo)

- Topologia: **star** (hub skill-creator/content-forge) — vedi sopra.
- Namespace memoria: `ruflo memory init --namespace forge`
- Decisioni che cambiano l'organigramma (nuovo ecosistema, ritiro team): proposta
  al Board via hive-mind consensus (raft) — la FORGE propone, il Board approva.

*Fonte: `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md` §07 + `07-BACKBONE-RUFLO-SKILLS.md` · Aggiornato: 2026-06-11*
