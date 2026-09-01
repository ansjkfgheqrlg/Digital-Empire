# P5 — Procedural Decomposition

> Trasforma "how-to" narrativi in **sequenze di step esplicite**, con decision points, precondizioni, postcondizioni, failure modes.

## Cosa fa

Quando il sorgente descrive *come si fa* qualcosa, P5 lo riformula come **procedura eseguibile**: passi numerati, ogni passo con input/output chiari, branch (decisioni), error path (cosa va male e come si recupera).

Output: una struttura simile a uno step di workflow, ma generica e riusabile.

## Chi lo applica

- **A2 `analyst-agent`** annota `category: procedure` e produce un'estrazione preliminare.
- **B2 `agent-builder`** — diventa la sezione "How to act" del system prompt.
- **B3 `team-builder`** — distribuisce gli step tra i ruoli del team (RACI).
- **B5 `workflow-builder`** — diventa il DAG vero e proprio (uno step per passo).
- **B7 `wiki-builder`** — diventa una nota nella cartella `procedures/`.

## Quando applicarlo

- Sempre per atomi `category: procedure`.
- Spesso per `category: concept` quando il concetto include "come si fa".
- Talvolta per `claim` se la claim è "X funziona — ecco come implementarlo".

## Quando NON applicarlo

- Per contenuto puramente descrittivo / definizionale.
- Per opinion / framework cognitivi (lì serve P6, mental model surfacing).

## Cuore del pattern

```python
# Procedure canonical shape
procedure = {
    "name": str,
    "goal": str,                          # cosa otterrai dopo
    "preconditions": list[str],           # cosa serve PRIMA
    "inputs": list[dict],                 # parametri richiesti
    "steps": [
        {
            "id": str,                    # "step-01"
            "name": str,
            "instruction": str,           # azione concreta
            "decision_point": dict | None,  # se branch: {"condition": str, "if_true": "step-X", "if_false": "step-Y"}
            "tools_used": list[str],
            "common_errors": list[str],
            "recovery": str | None,
        }
    ],
    "postconditions": list[str],          # cosa è vero dopo
    "outputs": list[dict],
    "failure_modes": list[dict],          # cosa può andare male a livello procedura
    "estimated_time": str,
}
```

## Algoritmo di decomposizione (pseudo)

```python
def decompose_procedure(narrative: str, kg_context: dict) -> dict:
    """Trasforma narrativa how-to in struttura procedurale."""
    # 1. Identifica verbi d'azione → candidati step
    actions = extract_action_verbs(narrative)
    # 2. Raggruppa azioni atomiche in step (granularità: ogni step ha un risultato osservabile)
    steps = group_to_steps(actions)
    # 3. Identifica decision points (parole tipo "se", "quando", "altrimenti", "depending on")
    for step in steps:
        if has_conditional_language(step):
            step["decision_point"] = extract_branch(step)
    # 4. Identifica precondizioni (parole tipo "assicurati che", "prima di iniziare")
    preconds = extract_preconditions(narrative)
    # 5. Identifica failure mode (parole tipo "se fallisce", "in caso di errore", "se non funziona")
    failures = extract_failure_handling(narrative)
    # 6. Identifica tools (oggetti manipolati: file, API, comandi)
    for step in steps:
        step["tools_used"] = extract_tools(step["instruction"])
    return assemble_procedure(steps, preconds, failures, ...)
```

## Esempio (input narrativo → output procedurale)

**Input** (estratto sorgente):
> "Per fare cold outreach efficace su LinkedIn, prima identifichi il prospect ideale (ICP), poi cerchi 20 contatti che matchano, leggi il loro profilo per personalizzare, e mandi un messaggio breve. Se non rispondono in 3 giorni, fai un follow-up. Se la connessione viene rifiutata, NON insistere — passa al prossimo."

**Output procedurale**:

```yaml
name: "Cold outreach LinkedIn"
goal: "Ottenere risposta da prospect qualificato"
preconditions:
  - "ICP definito (industria, ruolo, dimensione azienda)"
  - "Account LinkedIn con Sales Navigator (o equivalente)"
inputs:
  - {name: "icp_profile", type: "dict"}
  - {name: "batch_size", type: "int", default: 20}
steps:
  - id: "step-01"
    name: "Search prospects"
    instruction: "Cerca <batch_size> contatti che matchano ICP usando filtri LinkedIn"
    tools_used: ["linkedin_search"]
  - id: "step-02"
    name: "Profile review for personalization"
    instruction: "Per ogni prospect, leggi profilo (azienda, ruolo recente, post recenti) e identifica 1 hook personale"
    tools_used: ["linkedin_profile_read"]
  - id: "step-03"
    name: "Send connection + first message"
    instruction: "Invia connection request con messaggio personalizzato breve (≤300 char)"
    tools_used: ["linkedin_send_message"]
  - id: "step-04"
    name: "Wait & track"
    instruction: "Attendi 3 giorni, monitora replies"
  - id: "step-05"
    name: "Decision: reply received?"
    decision_point:
      condition: "prospect_replied OR connection_accepted_with_reply"
      if_true: "step-07 (move to conversation)"
      if_false: "step-06 (follow-up)"
  - id: "step-06"
    name: "Follow-up"
    instruction: "Invia messaggio follow-up (diverso dal primo, valore aggiunto, no pressure)"
    common_errors: ["follow-up identico al primo (basso reply rate)"]
  - id: "step-07"
    name: "Move to conversation"
    instruction: "Trasferisci a CRM, classifica come 'engaged'"
postconditions:
  - "Ogni prospect è in uno stato: 'no_reply', 'engaged', 'rejected'"
failure_modes:
  - failure: "Connection rejected"
    recovery: "Non insistere, marca come 'rejected', passa al prossimo"
  - failure: "LinkedIn rate limit"
    recovery: "Pausa 24h, riprendi"
estimated_time: "30 min per batch di 20"
```

Questo output è la base per:
- Un agente (B2): la sezione "How to act" del SP
- Un workflow (B5): 7 step nel DAG
- Una nota wiki (B7): in `procedures/cold-outreach-linkedin.md`

## Anti-pattern

- **Step troppo grossi** (1 step = "fare cold outreach"): inutile, non decomposto. Splittare.
- **Step troppo fini** (1 step = "cliccare bottone X"): rumore. Aggregare.
- **Decision point impliciti** (testo "se X allora Y" non estratto come branch): perdi struttura. Esplicitare.
- **Failure modes ignorati** ("se va male riprovi"): non è recovery. Specificare COSA si fa.

## Riferimenti

- BPMN (Business Process Model and Notation)
- Runbook engineering (Google SRE Book)
