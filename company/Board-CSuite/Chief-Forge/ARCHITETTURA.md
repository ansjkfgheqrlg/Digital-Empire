# ARCHITETTURA — Chief-Forge (Blueprint Espanso)

> Fonte vincolante: `company/Board-CSuite/_BLUEPRINT/BP-Chief-Forge.md`
> Standard CF-grade: `PIANO-MAESTRO/12-DOSSIER-MAXIMILIAN.md` §0
> Connessioni: [[14-DOSSIER-ARCHITETTURA]] · [[07-FORGE/ECOSISTEMA.md]]

---

## 1. Gerarchia interna della figura

```
CHIEF-FORGE (figura L0)
│
├── cf-conductor (Opus)            ← il coordinatore: unico a parlare con CEO/CFO
│     │
│     ├── cf-intake-router (Sonnet)   ← frontdoor: cattura ogni richiesta in ingresso
│     │
│     ├── [TEAM ANALISI]
│     │     ├── cf-skill-portfolio (Haiku)        ← catalogo skill vivente
│     │     ├── cf-agent-registry (Haiku)         ← Identity-HR registro completo
│     │     └── cf-contradiction-warden (Sonnet)  ← anti-duplicati/conflitti
│     │
│     ├── [TEAM PONTI GENESI CORE]
│     │     ├── cf-architettura-liaison (Sonnet)  ← parla con ARCHITETTURA
│     │     └── cf-forge-liaison (Sonnet)         ← parla con FORGE
│     │
│     ├── [TEAM GATE E MANDATI]
│     │     ├── cf-eval-warden (Sonnet)           ← gate eval pre-rilascio
│     │     └── cf-ecosystem-builder (Opus)       ← mandati ecosistemi nuovi
│     │
│     └── cf-memoria (Haiku)        ← storico persistente, pattern organizzativi
```

**Regola topologica:** nessun agente parla direttamente a CEO/CFO senza passare da
`cf-conductor`. Nessun agente commissiona build a FORGE senza coordinamento con
`cf-forge-liaison`. Nessun blueprint viene richiesto ad ARCHITETTURA senza
`cf-architettura-liaison`.

---

## 2. Flusso operativo principale (WF-CAPABILITY-INTAKE)

```
Ecosistema X
  │  {gap, contesto, KPI, budget}
  ▼
cf-intake-router          ← valida formato, assegna priorità
  │
  ├─ cf-skill-portfolio   ← esiste già? duplicato? gap reale?
  ├─ cf-agent-registry    ← agente equivalente già registrato?
  └─ cf-contradiction-warden ← contraddice skill/agenti esistenti?
  │
  │  [output: brief validato con raccomandazione]
  ▼
cf-conductor              ← decisione: build | reject | defer
  │
  ├─ se REJECT → risposta motivata all'ecosistema richiedente
  ├─ se DEFER → inserimento in backlog con priorità
  └─ se BUILD →
        │
        ├─ cf-architettura-liaison → ARCHITETTURA (blueprint)
        │       {tipo, scopo, vincoli, eval_criteria}
        │       ← blueprint validato (struct-gate PASS)
        │
        ├─ cf-forge-liaison → FORGE (build)
        │       {blueprint_id, path_destinazione, budget}
        │       ← artefatto prodotto (path, eval_report)
        │
        └─ cf-eval-warden ← gate eval (≥85% pass)
              │
              ├─ PASS → cf-agent-registry aggiorna Identity-HR
              │          cf-skill-portfolio aggiorna catalogo
              │          cf-memoria registra pattern
              │          CONSEGNA all'ecosistema richiedente
              └─ FAIL → iterate (max 2 cicli) → escalation CEO
```

---

## 3. Flusso ecosistemi nuovi (WF-ECOSYSTEM-MANDATE)

```
Board (CEO/CFO/Max)
  │  {richiesta ecosistema nuovo, motivazione strategica}
  ▼
cf-conductor + cf-ecosystem-builder
  │  analisi impatto, costo stimato, piano fasi
  ▼
cf-architettura-liaison → ARCHITETTURA L2.5 (Progettazione Ecosistemi)
  │  {tipo: ecosistema, nome, missione, vincoli budget}
  ▼
ARCHITETTURA produce: org chart L1→L5, BACKBONE, namespace memoria, handoff
  │  blueprint approvato
  ▼
cf-conductor → CEO: "mandato di build ecosistema X"
  │  approvazione esplicita CEO richiesta
  ▼
cf-forge-liaison → FORGE (WF-ECOSYSTEM-NEW)
  │  build completa
  ▼
cf-eval-warden + cf-ecosystem-builder: gate verifica ecosistema operativo
  ▼
cf-agent-registry + cf-skill-portfolio: aggiornamento completo registri
  ▼
cf-memoria: logging evento fondativo ecosistema
```

---

## 4. Relazione con ARCHITETTURA

ARCHITETTURA (dossier 14) è il **fulcro per-artefatto**: disegna la struttura di ogni
cosa prima che la FORGE la costruisca. Chief-Forge è il **committente di alto livello**:
decide cosa costruire, non come costruirlo strutturalmente.

Il ponte operativo è `cf-architettura-liaison`. Nessuna richiesta a ARCHITETTURA parte
senza il brief validato da `cf-intake-router` e approvato da `cf-conductor`.

Handoff Chief-Forge → ARCHITETTURA:
```json
{
  "request_id": "CF-REQ-YYYYMMDD-NNN",
  "tipo": "skill | agente | team | workflow | documento | ecosistema",
  "scopo": "problema da risolvere",
  "vincoli": {"budget": "...", "tier_max": "haiku|sonnet|opus", "ecosistema_dest": "XX"},
  "eval_criteria": ["criterio1", "criterio2"],
  "deadline": "YYYY-MM-DD"
}
```

Handoff ARCHITETTURA → Chief-Forge (via liaison):
```json
{
  "blueprint_id": "ARCH-BP-YYYYMMDD-NNN",
  "struct_gate": "PASS | FAIL",
  "struttura_artefatto": {...},
  "schema_canonico_usato": "skill | agente | team | ...",
  "note_architetturali": "..."
}
```

---

## 5. Relazione con FORGE

FORGE (ecosistema 07) è il **braccio operativo di build**: costruisce ciò che ARCHITETTURA
ha disegnato. Chief-Forge è il mandante: decide il "cosa" e il "perché"; FORGE decide il "come".

Il ponte operativo è `cf-forge-liaison`. Nessun artefatto viene messo in coda di FORGE
senza blueprint ARCHITETTURA approvato e budget autorizzato.

Handoff Chief-Forge → FORGE:
```json
{
  "forge_order_id": "CF-FO-YYYYMMDD-NNN",
  "blueprint_id": "ARCH-BP-YYYYMMDD-NNN",
  "path_destinazione": "company/...",
  "budget_approvato": "USD",
  "urgenza": "CRITICAL | HIGH | NORMAL | LOW",
  "eval_threshold": 85
}
```

Handoff FORGE → Chief-Forge (via liaison):
```json
{
  "artefatto_id": "nome-skill | agente-id | team-id",
  "tipo": "skill | agente | team | workflow | ecosistema",
  "path": "path installato",
  "eval_report": {"pass_rate": 0, "test_count": 0, "failures": []},
  "status": "delivered | in_progress | rejected"
}
```

---

## 6. Namespace memoria e state

Namespace AgentDB: `board/chief-forge`

Sotto-namespace:
- `board/chief-forge/intake` — richieste in ingresso, stato pipeline
- `board/chief-forge/portfolio` — catalogo skill vivente
- `board/chief-forge/registry` — Identity-HR snapshot
- `board/chief-forge/eval` — storico valutazioni gate
- `board/chief-forge/memoria` — pattern organizzativi, storico forgiature

Dettaglio schema in `state/README.md`.

---

## Connessioni

- [[README.md]] — overview figura
- [[BP-Chief-Forge]] — blueprint sorgente
- [[14-DOSSIER-ARCHITETTURA]] — organo ARCHITETTURA
- [[07-FORGE/ECOSISTEMA.md]] — organo FORGE
- [[agenti/cf-conductor.md]] — coordinator principale
- [[workflow/WF-CAPABILITY-INTAKE.md]] — flusso principale
