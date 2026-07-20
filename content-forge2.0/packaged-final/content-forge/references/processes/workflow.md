# Process: `workflow` — Complete Workflow

> Builder: `workflow-builder-agent` (B5)
> Stage: 5
> Tempo medio stimato: 3-5 turni utente + 2-3 iterazioni

---

## 1. Identità

Il target `workflow` trasforma il KG in **un workflow operativo end-to-end** che combina **agenti, skill, script e step manuali** lungo un DAG (Directed Acyclic Graph) di passi, con stato esplicito, trigger, gestione errori e osservabilità.

Differenza chiave vs `team`: il `team` è un *insieme di agenti che collaborano* su un task aperto. Il `workflow` è una *macchina a stati* con passi ben definiti, condizioni di transizione, e composizione di **risorse eterogenee** (alcuni passi sono agenti, altri sono skill invocate, altri sono script, altri sono umani).

Il workflow è pensato per essere **eseguito ripetutamente** in produzione, con SLA, retry, alert. Non è "una conversazione". È un sistema operativo del processo.

## 2. Forma canonica dell'output

```
output/
└── <workflow-slug>/
    ├── flow.md                    # DAG human-readable, passo per passo
    ├── flow.mermaid               # diagramma del DAG
    ├── state.md                   # schema dello stato + transizioni
    ├── triggers.md                # cosa fa partire il workflow
    ├── steps/
    │   ├── step-01-<name>.md      # spec di ogni step
    │   ├── step-02-<name>.md
    │   └── ...
    ├── agents/                    # se qualche step usa agenti dedicati
    ├── skills/                    # se qualche step invoca skill esistenti (riferimenti)
    ├── scripts/                   # se qualche step è deterministico
    ├── error_handling.md          # retry, fallback, alert, halt policy
    ├── observability.md           # log, metriche, tracing
    ├── runbook.md                 # come operarlo in produzione (cosa fare se X)
    ├── eval_scenarios.json        # scenari end-to-end (happy + edge + failure)
    ├── changelog.md
    └── README.md
```

### Esempio `flow.md` (forma canonica)

```markdown
# Workflow: <name>

## Trigger
<vedi triggers.md>

## State
<vedi state.md>

## Steps

### Step 01 — <name>
- **Type**: agent | skill | script | manual | branch | merge
- **Input**: <campo dello state letto>
- **Output**: <campo dello state scritto>
- **Implementation**: <pointer a steps/step-01-*.md>
- **On success**: → Step 02
- **On failure**: <vedi error_handling.md::<failure-id>>

### Step 02 — ...
...

## DAG (testo)
01 → 02 → (03 || 04) → 05 → END
```

### Tipi di step supportati

| Type | Cosa significa | File |
|---|---|---|
| `agent` | Esegue un agente | `agents/<name>.md` |
| `skill` | Invoca una skill esistente | `skills/<name>.md` (puntatore + invocation example) |
| `script` | Esegue uno script Python | `scripts/<name>.py` |
| `manual` | Step umano (gate di approvazione, input richiesto) | descritto in `steps/` |
| `branch` | Decisione condizionale | espressione + ramo per esito |
| `merge` | Sincronizzazione di rami paralleli | regola di merge |
| `parallel` | Esecuzione concorrente di N step | descritto in `steps/` |

## 3. Input atteso

```
inputs/
├── kg.json
├── atoms/
├── source_meta.json
└── user_answers.json
```

## 4. PLAN (cosa fa il builder)

1. Analizza il KG cercando **sequenze procedurali** (P5 è il pattern dominante qui).
2. Costruisce un DAG candidato:
   - nodi = step
   - archi = transizioni con condizioni
   - identifica branch (decisioni nel sorgente)
   - identifica parallel (step indipendenti)
3. Per ogni step, classifica il **tipo** (agent / skill / script / manual / branch / merge).
4. Identifica lo **stato condiviso** che attraversa il workflow.
5. Identifica i punti **failure-likely** (chiamate esterne, parsing, decisioni ambigue).
6. Propone la **granularità**: troppo fine (1 prompt per step) è ingestibile; troppo grosso (1 step monstre) è non osservabile.
7. Restituisce PLAN al Conductor.

## 5. ASK (domande generate da D1)

1. **Trigger**: "Come parte il workflow? (cron, webhook, manuale, evento upstream, file drop, altro)"
2. **Granularità**: "Propongo <N> step. Ti sembra granuloso giusto? Vuoi accorpare/splittare alcuni?"
3. **Tipo per step ambigui**: "Lo step `<X>` può essere un agente o uno script. Hai preferenza? (regola: agente se richiede ragionamento non strutturato, script se è puramente determistico)"
4. **Stato**: "Dove vive lo stato del workflow? (filesystem JSON, db, queue, in-memory, distributed)"
5. **Idempotenza**: "Ogni step deve essere idempotente (rieseguibile senza side-effect)? Quali no per natura?"
6. **Parallelo**: "Questi step sono indipendenti: <lista>. Vuoi eseguirli in parallelo o sequenziali per semplicità?"
7. **Errori**: "Per ogni tipo di errore: retry, fallback, alert, halt? Proponi policy globale + override per step critici."
8. **Skill esistenti**: "Quali skill già installate dovrebbe usare il workflow? Dammi nome + descrizione + parametri tipici."
9. **Step manuali**: "Ci sono step umani? (approvazioni, input, decisioni). Per ciascuno: chi lo fa, come viene notificato, timeout."
10. **Osservabilità**: "Stack di log/metriche/tracing? (es. stdout, file, datadog, OpenTelemetry, custom)"
11. **SLA**: "Tempo totale max accettabile? Per step?"
12. **Eval scenarios**: "Dammi 2-3 scenari end-to-end (happy / edge / failure)."

## 6. BUILD (ordine di scrittura)

1. **`state.md`**: schema dello stato condiviso. Senza, gli step non si possono scrivere.
2. **`triggers.md`**: chi/cosa fa partire il workflow + payload iniziale dello state.
3. **`flow.md` + `flow.mermaid`**: DAG completo con tutti gli step (descrizione alta).
4. **Per ogni step**: file `steps/step-NN-<name>.md` con:
   - tipo
   - input/output sullo state
   - implementazione (pointer ad agent/skill/script/manuale)
   - precondition / postcondition
   - timeout
   - errori possibili (puntatore a `error_handling.md`)
5. **`agents/`**, **`skills/`**, **`scripts/`**: contenuti reali per ogni step che li usa.
6. **`error_handling.md`**: tabella `failure-id | dove avviene | retry | fallback | alert | halt-cond`.
7. **`observability.md`**: cosa loggare per ogni step, metriche da emettere, span di tracing.
8. **`runbook.md`**: scenario di operatività (cosa fare se X fallisce in produzione).
9. **`eval_scenarios.json`**: scenari end-to-end con stato iniziale, traiettoria attesa, stato finale.
10. **Self-critique** (vedi §7).
11. **`README.md`**.

## 7. Self-critique (interna)

- **DAG ben formato**: nessun ciclo, nessun nodo orfano, nessun nodo unreachable.
- **State consistency**: ogni step legge/scrive solo campi dichiarati nello state schema.
- **Error coverage**: ogni step può fallire — è coperto in `error_handling`?
- **Idempotenza dichiarata**: per ogni step è chiaro se è idempotente o no? Se no, c'è dedupe?
- **Granularità sensata**: nessun step >2h, nessun step <30s (se troppo piccolo, mergiare).
- **No god-step**: nessuno step fa 5 cose diverse.
- **Manual steps documentati**: per ogni step manuale: chi lo fa, come, in che tempo.
- **Eval discriminanti**: gli eval scenarios falliscono se il workflow è rotto?
- **Runbook actionable**: il runbook ha azioni concrete, non solo "investigare"?

## 8. Critique esterna (C1 + C3)

- **C1**: ogni atomo del KG → step / agente / skill / script / runbook entry. Soglia 90%.
- **C3**: validazione DAG (no cicli, no orfani), validazione state schema, validazione integrità referenziale (ogni puntatore esiste).

## 9. Iterate

Tipici fix:
- splittare god-step
- aggiungere error path mancanti
- normalizzare granularità
- riscrivere runbook in stile actionable

## 10. Failure modes del processo

| Failure | Sintomo | Mitigazione |
|---|---|---|
| DAG con ciclo | C3 fail | Identificare e rompere il ciclo con stato |
| State implicito | Step accede a campi non dichiarati | Forzare schema strict |
| Error handling generico | Tutti gli step "retry 3x" | Personalizzare per step critici |
| Step manuali senza owner | Workflow si blocca in attesa | Dichiarare owner + timeout + escalation |
| Osservabilità a posteriori | Niente log nei punti chiave | Forzare log su input/output di ogni step |

## 11. Esempio realistico

Input: tutorial completo su "lead enrichment + outbound + nurture" → KG con 110 atomi.
Steps proposti: 14 (trigger CSV upload → parse → enrich via API → dedup → score → branch (hot/cold) → personalizza email → manuale approval → send → log → 3-day wait → check reply → branch → nurture sequence).
State: filesystem JSON per ogni lead.
Skills riusate: `email-personalizer`, `reply-classifier`.
Scripts: `csv_parser.py`, `dedup.py`, `lead_scorer.py`.

Output:
- `flow.md` + `flow.mermaid`
- 14 file in `steps/`
- 3 scripts con test
- 2 skill references
- `error_handling.md` con 18 failure mode
- `runbook.md` con 12 scenari operativi
- `eval_scenarios.json` con 4 scenari

Coverage: 88% (alcuni atomi puramente narrativi non mappati a step). Schema: OK.

## 12. Handoff al Conductor

- path `output/<workflow-slug>/`
- `build-report.json`
- `next-suggestions.md` (es. "questo workflow potrebbe stare sotto un `orchestration` layer se ne hai altri simili, vuoi pianificarlo?")

---

## 13. 📎 Appendice — Algoritmi e shape (embedded)

### DAG validation (cycle detection con Kahn)

```python
# Pseudocodice eseguibile che il builder DEVE generare come parte di scripts/validate_dag.py
from collections import defaultdict, deque

def has_cycle(edges: list[tuple[str, str]], nodes: list[str]) -> bool:
    """Ritorna True se il DAG contiene un ciclo (Kahn's topological sort)."""
    indeg = defaultdict(int)
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        indeg[b] += 1
    q = deque([n for n in nodes if indeg[n] == 0])
    seen = 0
    while q:
        n = q.popleft()
        seen += 1
        for m in adj[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)
    return seen != len(nodes)

def find_orphans(edges: list[tuple[str, str]], nodes: list[str], start_nodes: list[str]) -> list[str]:
    """Nodi unreachable dai trigger."""
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
    visited = set()
    q = deque(start_nodes)
    while q:
        n = q.popleft()
        if n in visited:
            continue
        visited.add(n)
        q.extend(adj[n])
    return [n for n in nodes if n not in visited]
```

### State schema canonical shape

```python
state_schema = {
    "version": str,                   # semver
    "fields": [
        {
            "name": str,
            "type": str,              # "string" | "int" | "float" | "bool" | "json" | "ref:<state-name>"
            "required": bool,
            "default": object | None,
            "writable_by_steps": list[str],
            "readable_by_steps": list[str],
            "description": str
        }
    ]
}
```

### Step definition shape

```python
step_spec = {
    "id": str,                         # "step-01"
    "name": str,
    "type": str,                       # agent|skill|script|manual|branch|merge|parallel
    "implementation": str,             # path al file (agent.md / skill ref / script.py)
    "reads": list[str],                # campi dello state
    "writes": list[str],
    "preconditions": list[str],        # espressioni booleane su state
    "postconditions": list[str],
    "timeout_seconds": int | None,
    "idempotent": bool,
    "on_success": str,                 # next step id o "END"
    "on_failure": str                  # failure-id in error_handling.md
}
```
