> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 · Reparto L2 LEARNING · WF-REASONINGBANK / WF-NEURAL

# T-REASONINGBANK — Pattern Learning e Memoria Vettoriale Agenti

> Funzione L4 · Reparto: L2 LEARNING · Ecosistema: 08-INTELLIGENCE
> Riferimento ecosistema: `company/Ecosistemi/08-INTELLIGENCE/ECOSISTEMA.md`

---

## Scopo

Raccogliere i fallimenti e le lezioni di tutti i workflow della holding, distillarli in
**pattern riusabili** e renderli disponibili via recall semantico (AgentDB HNSW) prima
di ogni nuovo task. Implementa il pattern #5 (ReasoningBank) del Piano Maestro.
Il motore è Ruflo: `memory_store/search`, `neural_train`, `autopilot`.

---

## Input — Evento fallimento/lezione

```json
{
  "task_id": "CP-YYYYMMDD-NNN",
  "ecosistema": "01-AGENCY | 03-CF | ...",
  "workflow": "WF-OUTREACH | WF-SITE-FULL | ...",
  "esito": "fallito | parziale | warning",
  "causa_radice": "descrizione breve",
  "lezione": "cosa fare diversamente",
  "contesto": "parametri che erano attivi"
}
```

## Output — Pattern distillato

```json
{
  "pattern_id": "pat-NNN",
  "titolo": "Mai avviare WF-X senza Y",
  "condizione": "se {workflow} + {contesto}",
  "azione": "esegui Z prima",
  "fonte_cp": "CP-20260611-004",
  "namespace": "patterns/08-intelligence"
}
```

---

## Processo step-by-step

1. **Ricezione evento** — ogni CP post-task include campo `lezioni`; ME-A09 (ecosistema 10-MEMORY)
   propaga gli eventi rilevanti verso INTELLIGENCE/LEARNING.
2. **Analisi causa radice** — `int-pattern-distiller` categorizza: errore di input, errore
   di sequenza, dipendenza mancante, budget superato, tool failure.
3. **Distillazione pattern** — IF-THEN format: condizione + azione preventiva + contesto.
4. **Store AgentDB** — `memory_store(namespace="patterns/<ecosistema>", pattern_obj)` con
   embedding per recall semantico futuro.
5. **Neural training** — `neural_train` periodico (mensile) su set di pattern accumulati per
   aumentare la prediction accuracy di `autopilot`.
6. **Recall pre-task** — ogni agente prima di agire: `memory_search("patterns/<ecosistema>", task_keywords)`;
   se pattern rilevante trovato → applicato automaticamente.

---

## Regole critiche

- Pattern distillato solo da eventi REALI (CP esistenti), mai sintetizzati a priori.
- Namespace separati per ecosistema: `patterns/01-agency`, `patterns/03-cf`, ecc.
- KPI: pattern_search hit nei workflow → trend crescente mese/mese (indicatore di apprendimento).
- `neural_train` non tocca skill attive — opera solo su AgentDB (gate G-SAFE-ENRICH).

---

## Connessioni

- Agente gestore: `int-pattern-distiller`
- Motore Ruflo: `memory_store` · `memory_search` · `neural_train` · `autopilot`
- Alimentato da: ecosistema 10-MEMORY (ME-A09 sync-agent propaga CP con lezioni)
- Cross-link: [[T-WIKI-CONTEXT]] · [[T-INGEST-VIDEO]] · [[08-INTELLIGENCE/ECOSISTEMA.md]]
