# Stage 5 — Target Selection

> Stage **opzionale**: si attiva solo se l'utente non ha già specificato un target. Produce raccomandazioni con razionale.

## Obiettivo

Analizzare il KG e proporre 1-3 target sensati tra gli 8 disponibili, con razionale per ognuno. Lascia decidere all'utente.

## Agente principale

**A4 `target-advisor-agent`** — vedi `agents/pipeline/target-advisor-agent.md`.

## Input attesi

```
<workspace>/forge-run-<ts>/stage-03/kg.json
<workspace>/forge-run-<ts>/stage-03/kg.md
<workspace>/forge-run-<ts>/stage-04/master.md       # MKD per esempi nelle proposte
<workspace>/forge-run-<ts>/stage-04/mkd-report.json
```

## Output canonici

```
<workspace>/forge-run-<ts>/stage-05/recommendation.md
```

Struttura `recommendation.md`:
- Top 1 con score (0-100) + razionale + domande per confermare
- Top 2 + Top 3 analoghi
- Domande critiche per decidere
- Combinazioni possibili (es. `doc` + `wiki` da stesso KG)

## Quando questo stage si attiva

**Solo se** `state.json["target"]` è `None` o `"unknown"` dopo Stage 3.

```python
if state["target"] in (None, "unknown"):
    spawn_a4()
else:
    skip_to_stage_05()
```

## Quando si conclude

L'utente (tramite Conductor) ha selezionato un target tra i proposti, o ne ha indicato uno diverso non proposto. `state.json["target"]` viene aggiornato.

## Failure modes specifici

| Failure | Mitigazione |
|---|---|
| Nessun target con score >50 | KG povero o ambiguo; mostra all'utente i top 3 anche se bassi + chiedi conferma esplicita |
| 3+ target tutti con score >75 | Contenuto multi-uso; suggerisci all'utente di scegliere uno per ora + propone run successivi per gli altri |
| L'utente indica un target diverso dai proposti | OK: salva la scelta, A4 era solo consulente. Stage 5 procede col target dell'utente |

## Contratto con Stage 5

Stage 5 spawna il builder corrispondente al target finale (`state.json["target"]`). Riceve `kg.json` + `recommendation.md` (per contesto).

## Nota su target=doc dopo l'introduzione del MKD

Dato che il MKD è già il "documento perfetto" (Stage 4), il target `doc` (Stage 6) è
diventato leggero: in pratica è un **MKD adapter** che riformatta il MKD secondo le
preferenze utente (audience, registro, lingua se diversa). Questo lo rende un target
"facile da consigliare" — perché la base è già pronta.

## Heuristics (riassunto, dettagli in `agents/pipeline/target-advisor-agent.md §3`)

```python
target_signals = {
    "doc": "KG denso di concetti, audience didattica implicita",
    "agent": "KG ricco di procedure + ruolo chiaro nel sorgente + tool menzionati",
    "team": "Multipli ruoli distinti, handoff impliciti",
    "skill": "How-to ripetibile + trigger pattern + output canonico",
    "workflow": "Sequenza temporale + decisioni branch + stato",
    "orchestration": "Multipli sistemi + routing + policies",
    "wiki": "Molti concetti atomici interconnessi + intent di studio",
    "custom": "L'utente ha già descritto forma non canonica",
}
```
