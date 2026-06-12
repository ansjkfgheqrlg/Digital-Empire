> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 08 · Reparto L2 SECOND-BRAIN · WF-WIKI-CONTEXT

# T-WIKI-CONTEXT — Context Pack Pre-Task

> Funzione L4 · Reparto: L2 SECOND-BRAIN · Ecosistema: 08-INTELLIGENCE
> Riferimento ecosistema: `company/Ecosistemi/08-INTELLIGENCE/ECOSISTEMA.md`

---

## Scopo

Produrre il **context-pack** pre-task: un pacchetto strutturato di pagine wiki rilevanti,
memorie AgentDB, pattern ReasoningBank e fonti — consegnato a qualsiasi ecosistema PRIMA
che il task parta. Implementa il pattern #12 (wiki-first) e il pattern #13 (memory-first).
Gate G-CONTEXT: copertura ≥95% dei task non banali.

---

## Input

```json
{
  "task_id": "string",
  "ecosistema": "01-AGENCY | 03-CF | ...",
  "keywords": ["ICP", "competitor", "brand X"],
  "tipo_task": "build | research | delivery | decision"
}
```

## Output — Context Pack

```json
{
  "wiki_pages": ["wiki/projects/Clienti/X.md", "wiki/concepts/Y.md"],
  "memorie": [{"id": "mem-001", "contenuto": "...", "score": 0.92}],
  "pattern": [{"id": "pat-007", "lezione": "...", "fonte": "CP-20260610-003"}],
  "stato_memory": "STATO-EMPIRE.md snapshot rilevante",
  "contraddizioni_segnalate": []
}
```

---

## Processo step-by-step

1. **Parsing keywords** — estrae termini chiave dall'input (ecosistema + tipo task + keywords esplicite).
2. **Ricerca wiki** — scansiona `second-brain-vault/wiki/` per pagine rilevanti (index.md come mappa).
3. **memory_search AgentDB** — namespace `intelligence/` + `memory/` con threshold 0.75.
4. **Carico STATO-EMPIRE** — snippet del STATO-EMPIRE.md relativo all'ecosistema chiamante.
5. **Scoring e taglio** — ordina per rilevanza; max 10 item (pattern *relevance-scorer*); rimuove duplicati.
6. **Contradiction check** — verifica che il task non contraddica ADR attivi; se sì → segnala subito.
7. **Restituzione context-pack** — JSON strutturato + indicazione se il pack è completo o parziale.

---

## Regole critiche

- Tempo massimo di produzione: ≤ 30 secondi (KPI MEMORY).
- Se wiki_pages = 0 → segnalare lacuna; `int-librarian` crea bozza pagina after-task.
- Senza context-pack il task NON può partire (gate bloccante WF-PRETASK di MEMORY).
- Usa skill `wiki-context` come motore primario.

---

## Connessioni

- Agente gestore: `int-context-packer`
- Skill primaria: `wiki-context`
- Integra con: WF-PRETASK di `company/Ecosistemi/10-MEMORY/Workflow/WF-PRETASK.md`
- Cross-link: [[T-REASONINGBANK]] · [[T-RESEARCH]] · [[08-INTELLIGENCE/ECOSISTEMA.md]]
