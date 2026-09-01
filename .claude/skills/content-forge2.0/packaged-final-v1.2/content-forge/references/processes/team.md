# Process: `team` — Multi-Agent Team

> Builder: `team-builder-agent` (B3)
> Stage: 5
> Tempo medio stimato: 3-4 turni utente + 2-3 iterazioni

---

## 1. Identità

Il target `team` trasforma il KG in **un team di agenti coordinati** che collaborano per portare a termine un compito complesso che un singolo agente non gestirebbe bene (perché richiede ruoli diversi, expertise distinte, o scala parallela).

Output: pacchetto completo con topologia, coordinator (se serve), N agenti specializzati, protocollo di handoff, regole di failure recovery, scenari di valutazione end-to-end.

Differenza chiave vs `agent`: qui si ragiona di **divisione del lavoro**. Il builder *parte* dal sorgente e *decompone* in ruoli non sovrapposti, ognuno con la sua specializzazione.

## 2. Forma canonica dell'output

```
output/
└── <team-slug>/
    ├── topology.md                # diagramma + razionale della topologia scelta
    ├── coordinator.md             # SP del coordinator (se topologia supervisor/hub-spoke)
    ├── agents/
    │   ├── <role-1>.md            # spec completa dell'agente (mini-version del target `agent`)
    │   ├── <role-1>.system_prompt.md
    │   ├── <role-2>.md
    │   ├── <role-2>.system_prompt.md
    │   └── ...
    ├── communication_protocol.md  # formato dei messaggi/file di handoff
    ├── handoff_rules.md           # chi passa cosa a chi, quando, in che condizioni
    ├── failure_handling.md        # cosa fa il team se un agente fallisce
    ├── shared_state.md            # schema dello stato condiviso (se presente)
    ├── team_eval_cases.json       # scenari end-to-end
    ├── changelog.md
    └── README.md                  # come istanziare il team, come lanciarlo
```

### Topologie supportate (file `topology.md`)

| Topologia | Quando si usa | Pro | Contro |
|---|---|---|---|
| **Supervisor** (coordinator + workers) | Compito che richiede pianificazione + esecuzione delegata | Controllo centrale, debug facile | Bottleneck sul coordinator |
| **Pipeline** (A → B → C) | Compito sequenziale con trasformazioni successive | Semplice, deterministico | Inflessibile, no parallelo |
| **Peer-to-peer** (tutti parlano con tutti) | Compito collaborativo, brainstorming, dibattito | Emergenza, creatività | Caotico, costoso |
| **Hub-spoke** (router + specialisti) | Triage / dispatching su input eterogeneo | Scalabile, costo controllato | Solo se i task sono indipendenti |
| **Hybrid** (mix) | Casi reali complessi | Adattivo | Più difficile da debuggare |

## 3. Input atteso

```
inputs/
├── kg.json
├── atoms/
├── source_meta.json
└── user_answers.json
```

## 4. PLAN (cosa fa il builder)

1. Analizza il KG per identificare **assi di specializzazione**:
   - per fase del processo (pipeline)
   - per dominio/competenza (hub-spoke)
   - per livello di astrazione (supervisor + worker)
   - per ruoli sociali nel sorgente (es. "il venditore parla col tecnico parla col CFO")
2. Propone **2-3 topologie candidate** con razionale.
3. Per ciascuna topologia: propone gli agenti con nome, ruolo, responsabilità, NON-responsabilità.
4. Identifica i punti di handoff (dove cambia di mano il lavoro).
5. Identifica i candidati per **stato condiviso** (cosa serve a tutti).
6. Restituisce PLAN al Conductor.

## 5. ASK (domande generate da D1)

1. **Topologia**: "Propongo: <opzione preferita> perché <razionale>. Le alternative sono <opzione B>, <opzione C>. Quale scegli?"
2. **Numero di agenti**: "Per la topologia scelta propongo N=<n> agenti: <lista nomi+ruolo>. Vuoi mergiare, splittare, rinominare?"
3. **Coordinator**: "Serve un coordinator separato o uno degli agenti lo fa anche? (es. il PM fa anche da coordinator)"
4. **Modello per ruolo**: "Per ogni agente, quale modello? (proposta: Opus per planner, Sonnet per worker, Haiku per task semplici)"
5. **Storage condiviso**: "Dove vive lo stato condiviso del team? (filesystem, db, in-memory, none)"
6. **Protocollo handoff**: "File-based (un agente scrive un file che il prossimo legge), message-based (passing diretto via task tool), o entrambi?"
7. **Trigger**: "Il team parte manualmente, su evento, o gira continuamente?"
8. **Concorrenza**: "Più team in parallelo o single-instance?"
9. **Failure**: "Se un agente fallisce, il team: (a) si ferma, (b) skippa, (c) ritenta con backoff, (d) usa un fallback?"
10. **Eval end-to-end**: "Hai scenari completi che vuoi che il team gestisca? Dammene 2-3."

## 6. BUILD (ordine di scrittura)

1. **`topology.md`**: prima di tutto, ufficializza la topologia con diagramma (mermaid) e razionale.
2. **`shared_state.md`**: prima degli agenti, perché tutti devono sapere com'è fatto lo stato condiviso.
3. **`communication_protocol.md`**: formato standard dei messaggi/file di handoff. Esempi reali.
4. **Per ogni agente** (in parallelo logico, sequenziale fisico):
   a. `<role>.md` (mini-process `agent`, ma con scope limitato a ciò che ricade nel ruolo)
   b. `<role>.system_prompt.md`
5. **`handoff_rules.md`**: matrice "from → to: cosa, quando, in che formato, validazione". Tabella.
6. **`coordinator.md`** (se topologia lo richiede): SP del coordinator con awareness di tutti gli altri ruoli, regole di delega, regole di re-routing.
7. **`failure_handling.md`**: per ogni agente e per ogni handoff, cosa va male e come si recupera. Tabella per riga.
8. **`team_eval_cases.json`**: 5-10 scenari end-to-end, ognuno con input al team, traiettoria attesa (chi fa cosa in che ordine), output atteso.
9. **Self-critique** (vedi §7).
10. **README.md**: come istanziare, come lanciare, esempi di invocazione.

## 7. Self-critique (interna)

Il builder verifica:

- **Disgiunzione dei ruoli**: ogni responsabilità è ALLOCATA a UN SOLO agente? Verifica via tabella ruolo×responsabilità (RACI semplificata).
- **No orfani**: c'è qualche responsabilità del KG che non è allocata a nessuno?
- **No deadlock**: c'è un handoff che richiede qualcosa che nessuno produce?
- **Coerenza del protocollo**: tutti gli agenti producono e consumano nello stesso formato?
- **Coordinator coherence**: il coordinator conosce davvero tutti gli agenti e i loro confini?
- **Failure coverage**: ogni handoff ha una failure handling?
- **Sovraccarico cognitivo**: c'è un agente con SP >1500 parole? → potrebbe servire splittarlo.
- **Sotto-specializzazione**: c'è un agente che fa una sola micro-cosa? → potrebbe essere uno script o tool, non un agente.

## 8. Critique esterna (C1 + C3)

- **C1**: ogni atomo del KG è riflesso in qualche agente, o nel coordinator, o nel protocollo. Soglia 90%.
- **C3**: schema validation di tutti i file canonici + integrità referenziale (es. ogni `handoff_rules` riferisce ruoli esistenti, ogni eval case usa nomi di agenti esistenti).

## 9. Iterate

Fix tipici:
- riallocazione di responsabilità tra agenti
- aggiunta di un nuovo agente o merge di due
- riscrittura del protocollo per uniformare i formati
- aggiunta di failure case mancanti

## 10. Failure modes del processo

| Failure | Sintomo | Mitigazione |
|---|---|---|
| Responsabilità sovrapposte | Due agenti competono per lo stesso task | RACI strict, un solo R per task |
| Coordinator onnisciente | SP coordinator >2500 parole | Spostare conoscenza nei singoli agenti |
| Protocollo ad-hoc | Ogni handoff ha un suo formato | Standardizzare in `communication_protocol.md` |
| No state machine | Lo stato del team non è chiaro | Aggiungere diagramma di stati in `shared_state.md` |
| Eval cases solo happy path | Test scoprono solo bug ovvi | Forzare ≥1 case di failure recovery |

## 11. Esempio realistico

Input: trascript di un workshop di 3h su "due-diligence M&A per startup tech" → KG con 84 atomi.
Topologia scelta: **Supervisor + 4 workers**.
Agenti: `dd-supervisor`, `legal-analyst`, `financial-analyst`, `tech-analyst`, `market-analyst`.
Storage: filesystem con cartella per ogni acquisition target.
Handoff: file-based JSON.
Eval: 3 scenari (small SaaS, deep-tech con IP, distressed asset).

Output:
- `topology.md` con mermaid
- `coordinator.md` 900 parole
- 4 agenti, ognuno con `.md` (~500 parole) + `.system_prompt.md` (~800 parole)
- `communication_protocol.md`: formato JSON standard con esempi
- `handoff_rules.md`: matrice 4×4 + supervisor
- `failure_handling.md`: 12 failure mode
- `team_eval_cases.json`: 3 scenari end-to-end
- `README.md`

Coverage: 91%. Schema: OK.

## 12. Handoff al Conductor

- path `output/<team-slug>/`
- `build-report.json`
- `next-suggestions.md` (es. "questo team beneficerebbe di un `workflow` esterno che lo invochi su trigger CRM, vuoi che lo pianifichi?")

---

## 13. 📎 Appendice — Strutture (embedded)

### RACI matrix (canonical)

```python
# Per garantire disgiunzione dei ruoli, il team-builder produce e valida una RACI
raci_schema = {
    "responsibilities": [
        {
            "id": str,                  # responsibility-NN
            "description": str,
            "responsible": str,         # UN SOLO agente — enforce con validator
            "accountable": str,
            "consulted": list[str],
            "informed": list[str]
        }
    ]
}

def validate_raci(raci: dict) -> list[str]:
    """Verifica disgiunzione (un solo R per responsabilità)."""
    issues = []
    for r in raci["responsibilities"]:
        if not isinstance(r["responsible"], str):
            issues.append(f"{r['id']}: responsible deve essere singolo agente")
        if r["responsible"] in r.get("consulted", []):
            issues.append(f"{r['id']}: responsible non può essere anche consulted")
    return issues
```

### Handoff envelope (canonico tra agenti)

```python
handoff_envelope = {
    "from_agent": str,
    "to_agent": str,
    "task_id": str,
    "timestamp": str,
    "payload": dict,                    # contenuto specifico
    "context_refs": list[str],          # path a file di stato condiviso
    "expectation": str,                 # cosa deve restituire il destinatario
    "deadline": str | None,
    "trace_id": str                     # per observability
}
```

### Topology validation

```python
def validate_topology(topo: str, agents: list[str], handoffs: list[dict]) -> list[str]:
    issues = []
    if topo == "supervisor":
        coord = [a for a in agents if a.endswith("supervisor") or a.endswith("coordinator")]
        if len(coord) != 1:
            issues.append("supervisor topology richiede esattamente 1 coordinator")
    elif topo == "pipeline":
        # ogni agente compare al più una volta come 'from' e una come 'to'
        froms = [h["from_agent"] for h in handoffs]
        tos   = [h["to_agent"]   for h in handoffs]
        if len(set(froms)) != len(froms) or len(set(tos)) != len(tos):
            issues.append("pipeline non lineare")
    return issues
```
