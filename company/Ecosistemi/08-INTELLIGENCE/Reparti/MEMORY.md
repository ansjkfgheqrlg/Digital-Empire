> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 L2 MEMORY

# Reparto L2.2 — MEMORY (= Memory Empire v3)

**Ecosistema:** 08-INTELLIGENCE · **Livello:** L2 · **Owner:** `int-memory-router`
**Vincolo cardinale:** Memory Empire v3 si ingloba **COSÌ COM'È** — router + archivio + enrichment già attivi.
Non è l'ecosistema 10 MEMORY (memoria operativa); è il motore di *knowledge routing e enrichment*.

Collega: [[08-INTELLIGENCE/ECOSISTEMA.md]] · [[08-INTELLIGENCE/BACKBONE.md]]

---

## Cosa fa

MEMORY è il **router universale e arricchitore della conoscenza DE**: ogni richiesta di
qualsiasi ecosistema passa da Memory Empire v3, che la instrada al workflow corretto
(INGESTION, SECOND-BRAIN, RESEARCH, LEARNING) e gestisce l'archivio integrale in `knowledge/`.

**Tre linee di lavoro:**
1. **WF-ROUTE** — router: ogni richiesta DE → workflow giusto, attivazione di sicurezza (rete)
2. **WF-ARCHIVE** — archivio integrale: knowledge/ + wiki (mai riassunto)
3. **WF-ENRICH** — enrichment pipeline: nuova conoscenza → skill/workflow esistenti (con backup + diff)

**Confine con ecosistema 10 MEMORY**: MEMORY (qui) custodisce la *conoscenza* (esterna ingerita,
wiki, pattern appresi). Ecosistema 10 custodisce la *memoria operativa* (checkpoint CP, ADR,
piani, stato, sessioni). Non sovrapposti per design.

---

## Come si collega

| Con | Relazione |
|---|---|
| INGESTION | WF-ROUTE instrada le richieste di ingestione a Empire Studio |
| SECOND-BRAIN | WF-ARCHIVE alimenta la wiki; WF-ROUTE usa wiki-context come context pack |
| LEARNING | WF-ENRICH riceve pattern dal ReasoningBank e li applica (safe) |
| FORGE / SKILL-WORKS | enrichment skill richiede approvazione FORGE per modificare skill attive |
| Ecosistema 10 MEMORY | confine chiaro: questo MEMORY = conoscenza; 10 MEMORY = operatività |

---

## Asset (WRAPPA — non riscrivere)

| Asset | Azione |
|---|---|
| `~/.claude/skills/memory-empire/` v3 (agents, departments, knowledge, scripts, routing-map.md) | **USA COSÌ COM'È** |
| skill `memory-management` | **USA** |
| `~/.claude/projects/.../memory/MEMORY.md` (auto-memory) | **WRAPPA** — sync periodico verso wiki |

---

## Regola G-SAFE-ENRICH (non negoziabile)

Prima di qualsiasi enrichment su skill/workflow attivi:
1. Backup della versione corrente
2. Diff proposto approvato da FORGE (frg-chief)
3. Eval prima/dopo
4. Rollback automatico se score post < baseline

---

## KPI

| Metrica | Target |
|---|---|
| Richieste DE instradate correttamente da router | ≥ 98% |
| Enrichment con regressione (score post < baseline) | 0 (rollback immediato) |
| Contenuto archiviato integrale (mai riassunto) | 100% |
| Routing-map aggiornata dopo ogni nuovo workflow | 100% |
