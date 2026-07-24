# Process: `orchestration` — Orchestration Layer

> Builder: `orchestration-builder-agent` (B6)
> Stage: 5
> Tempo medio stimato: 3-4 turni utente + 2 iterazioni
> **Prerequisito implicito**: l'utente ha già (o sta pianificando) più componenti — workflow, agenti, skill — da orchestrare. Se non ne ha, probabilmente vuole `workflow` o `team`.

---

## 1. Identità

Il target `orchestration` produce **il livello sopra i workflow**: un *supervisor / router / planner* che riceve richieste eterogenee e decide dinamicamente quale workflow / agente / skill invocare, con quale priorità, sotto quali policy.

Pensa a un'orchestration layer come al **sistema operativo del tuo asset cognitivo**:
- ha un **registry** dei componenti disponibili (cosa esiste e cosa fa)
- ha **routing rules** (chi gestisce cosa)
- ha **policies** (budget, quota, priorità, security)
- ha **observability** (sa cosa sta succedendo)
- ha **failure modes** (cosa fare se un componente cade o si comporta male)

Differenza chiave vs `workflow`: il workflow è UNA macchina a stati. L'orchestration sceglie quale macchina (o quale agente) invocare in base alla richiesta.

## 2. Forma canonica dell'output

```
output/
└── <orchestration-slug>/
    ├── supervisor.md              # SP del supervisor (se LLM-based)
    ├── routing.md                 # regole di routing (rule-based o LLM-based)
    ├── registry.md                # catalogo dei componenti orchestrati
    ├── registry.json              # versione machine-readable
    ├── policies.md                # budget, quota, priorità, security
    ├── observability.md           # log, metriche, tracing, alert
    ├── failure_modes.md           # cosa va male e come si gestisce
    ├── escalation.md              # quando coinvolgere un umano
    ├── eval_scenarios.json        # input → componente atteso (router test)
    ├── changelog.md
    └── README.md
```

### Struttura di `routing.md`

```markdown
# Routing

## Strategy
- Type: rule-based | LLM-based | hybrid
- Default: <componente di fallback>

## Routing rules (rule-based o hybrid)

| # | Condition | Route to | Reason |
|---|-----------|----------|--------|
| 1 | input.type == "lead_csv" AND size < 100 | wf:lead-enrichment-small | dedicated for small batches |
| 2 | input.type == "lead_csv" AND size >= 100 | wf:lead-enrichment-bulk | parallel processing |
| 3 | input.intent == "due_diligence" | team:dd-team | requires multi-expert analysis |
| 4 | ... | ... | ... |

## LLM-based routing prompt (se applicabile)
<prompt che usa supervisor.md>
```

### Struttura di `registry.md`

Catalogo dei componenti. Per ognuno:

```markdown
## <componente-slug>
- **Type**: workflow | agent | skill | team
- **Path**: <repo path o registry URI>
- **Owner**: <human or team responsible>
- **Description**: <what it does, in 1-3 lines>
- **Input schema**: <riferimento o inline>
- **Output schema**: <riferimento o inline>
- **Cost class**: low | medium | high
- **Latency class**: fast | normal | slow
- **Dependencies**: <altri componenti, API esterne>
- **SLA**: <se applicabile>
- **Status**: stable | beta | deprecated
```

## 3. Input atteso

```
inputs/
├── kg.json
├── atoms/
├── source_meta.json
├── user_answers.json
└── existing_components.json   # ← UNICO target che richiede questo input extra
```

`existing_components.json` è la lista dei componenti che l'utente vuole orchestrare. Senza, non si può costruire un'orchestration sensata.

## 4. PLAN (cosa fa il builder)

1. Verifica presenza di `existing_components.json`. Se manca → blocca e chiede al Conductor di raccoglierlo dall'utente prima di procedere.
2. Analizza il KG per estrarre:
   - **principi di routing** (regole di decisione menzionate)
   - **policies** menzionate (es. "non spendere più di X", "priorità a clienti enterprise")
   - **failure modes** menzionati
3. Cross-reference: per ogni componente in `existing_components.json`, c'è un cluster nel KG che lo riguarda? Se no, segnala.
4. Identifica se serve un **supervisor LLM-based** (compito complesso, routing soft) o **rule-based** è sufficiente.
5. Identifica i **gap**: componenti menzionati nel KG ma non presenti nel registry → suggerimenti per il futuro.
6. Restituisce PLAN al Conductor.

## 5. ASK (domande generate da D1)

1. **Componenti esistenti**: "Mi serve la lista dei componenti che vuoi orchestrare. Per ognuno: tipo, descrizione, input atteso, costo/latency. Hai un file? Te lo scrivo io basandomi su quello che mi dici? Quanti sono?"
2. **Strategia di routing**: "Rule-based (deterministico, debug facile, scala male se le regole crescono) o LLM-based (flessibile, semantic understanding, più costoso)? Hybrid è possibile."
3. **Default fallback**: "Se nessun componente matcha, cosa fa l'orchestration? (errore, default component, escalation umana)"
4. **Policies**: "Budget mensile / chiamata? Quote per utente? Priorità per tier? Whitelist/blacklist?"
5. **SLA**: "C'è un tempo max per la decisione di routing? Per l'esecuzione end-to-end?"
6. **Osservabilità**: "Cosa serve loggare? Quale stack? Chi guarda i log?"
7. **Escalation umana**: "Quando coinvolgere un umano? (low confidence, alta posta in gioco, errori consecutivi, richiesta esplicita)"
8. **Security**: "Componenti con accesso a dati sensibili? Policy di sandboxing?"
9. **Versioning**: "Come gestiamo nuovi componenti / deprecation di vecchi?"
10. **Eval scenarios**: "Dammi 5-10 input di esempio che vorresti vedere routare correttamente. Per ognuno: input + componente atteso (o set di componenti accettabili)."

## 6. BUILD (ordine di scrittura)

1. **`registry.md` + `registry.json`**: catalogo, perché tutto il resto ci si appoggia.
2. **`policies.md`**: budget/quota/priority/security.
3. **`routing.md`**: regole + (se LLM-based) prompt del supervisor.
4. **`supervisor.md`** (se LLM-based): SP completo del supervisor con esempi di routing, casi limite, formato output (es. JSON con `route_to`, `confidence`, `reason`).
5. **`failure_modes.md`**: per componente e per il supervisor stesso. Tabella.
6. **`escalation.md`**: trigger di escalation umana, format della notifica, owner.
7. **`observability.md`**: log per evento (input, decisione, latenza, costo, esito), metriche aggregate, tracing per chiamata.
8. **`eval_scenarios.json`**: input + expected component + (opzionale) expected response.
9. **Self-critique** (vedi §7).
10. **`README.md`**.

## 7. Self-critique (interna)

- **Routing completeness**: ogni tipo di input dichiarato in eval scenarios matcha almeno una regola?
- **No ambiguità**: due regole non possono matchare lo stesso input con esiti diversi (a meno che ci sia priorità esplicita)?
- **Default fallback presente**: c'è sempre una via d'uscita?
- **Policy enforcement**: ogni policy ha un punto di enforcement chiaro nel flusso?
- **Cost awareness**: per componenti high-cost, ci sono guardrail?
- **Observability completeness**: ogni decisione di routing è loggata con razionale?
- **Supervisor SP coerente** (se LLM-based): conosce il registry, sa formattare output, ha esempi few-shot per ogni cluster di routing?
- **Escalation actionable**: l'escalation è concreta (chi, come, in che tempo)?

## 8. Critique esterna (C1 + C3)

- **C1**: ogni atomo del KG → registry entry / policy / failure mode / observability metric / escalation. Soglia 85% (più bassa perché parte degli atomi parlano di componenti specifici già coperti nel loro `agent.md` etc).
- **C3**: validazione schema registry, validazione routing (no overlap senza priority), validazione integrità referenziale (ogni `route_to` punta a componente esistente nel registry).

## 9. Iterate

Tipici fix:
- regole di routing duplicate/ambigue
- componenti nel registry senza owner
- policy senza enforcement
- escalation troppo vaga

## 10. Failure modes del processo

| Failure | Sintomo | Mitigazione |
|---|---|---|
| Registry stale | Componenti nel registry non esistono più | Forzare owner per componente + check di staleness |
| Routing ambiguo | Stesso input → componente diverso a ogni run | Esplicitare priority |
| Supervisor confuso | LLM-based router con basso accuracy | Aggiungere few-shot, ridurre numero di componenti, splittare in più layer |
| Budget overflow | Costi fuori controllo | Hard cap + alert |
| Black box | Decisioni non spiegabili | Forzare campo `reason` in ogni decisione loggata |

## 11. Esempio realistico

Input: serie di articoli + brief interno su "sales ops orchestration" → KG con 75 atomi. Componenti esistenti dichiarati dall'utente: 4 workflow + 3 agenti + 2 skill (9 totali).

Strategia: hybrid (regole per casi ovvi, supervisor LLM per casi ambigui).
Policies: budget mensile $500, priorità a tier enterprise, sandboxing per componenti con accesso CRM.

Output:
- `registry.md` con 9 entry complete + `registry.json`
- `routing.md` con 14 regole + supervisor prompt fallback
- `supervisor.md` (Sonnet, 1200 parole)
- `policies.md` 5 sezioni
- `failure_modes.md` 16 failure
- `escalation.md` 4 trigger
- `observability.md` con stack proposto (stdout + jsonl + opzionale OTel)
- `eval_scenarios.json` 12 scenari

Coverage: 86%. Schema: OK.

## 12. Handoff al Conductor

- path `output/<orchestration-slug>/`
- `build-report.json`
- `next-suggestions.md` (es. "il registry segnala 3 componenti non ancora costruiti, vuoi generarli con `agent` / `workflow`?")

---

## 13. 📎 Appendice — Shape registry (embedded)

### `registry.json` — shape canonica

```python
registry_schema = {
    "version": str,                     # semver del registry
    "generated_at": str,                # ISO timestamp
    "components": [
        {
            "slug": str,                # univoco
            "type": str,                # "workflow" | "agent" | "skill" | "team"
            "path": str,                # repo path o URI
            "owner": str,
            "description": str,         # 1-3 righe
            "input_schema_ref": str,    # path a JSON Schema
            "output_schema_ref": str,
            "cost_class": str,          # "low" | "medium" | "high"
            "latency_class": str,       # "fast" | "normal" | "slow"
            "dependencies": list[str],
            "sla": dict | None,
            "status": str,              # "stable" | "beta" | "deprecated"
            "version": str
        }
    ]
}
```

### Routing rule eval (pseudo)

```python
def route(input_payload: dict, rules: list[dict], default: str) -> dict:
    """Ritorna la decisione di routing con razionale."""
    for r in sorted(rules, key=lambda x: x.get("priority", 100)):
        if eval_condition(r["condition"], input_payload):  # safe eval, no exec
            return {
                "route_to": r["route_to"],
                "confidence": 1.0,
                "reason": r["reason"],
                "rule_id": r["id"]
            }
    return {"route_to": default, "confidence": 0.5, "reason": "default fallback", "rule_id": None}
```

### Supervisor LLM output schema (se LLM-based)

```python
supervisor_output_schema = {
    "route_to": str,                    # slug del componente
    "confidence": float,                # 0.0-1.0
    "reason": str,                      # spiegazione human-readable
    "alternatives": list[str],          # altri candidati con confidence inferiore
    "needs_escalation": bool,
    "estimated_cost_class": str
}
```
