# Process: `agent` — Single Agent Specification

> Builder: `agent-builder-agent` (B2)
> Stage: 5
> Tempo medio stimato: 2-3 turni utente + 2-3 iterazioni

---

## 1. Identità

Il target `agent` trasforma il KG in **la specifica completa di un singolo agente AI operativo**: ruolo, system prompt, strumenti, comportamenti attesi, failure mode, casi di valutazione, playbook conversazionale.

Non è un brainstorm su "cosa potrebbe fare un agente". È un **pacchetto pronto** che un altro sviluppatore (o l'utente stesso) può prendere e usare per istanziare un agente reale su Claude/OpenAI/qualunque framework, senza dover rifare il lavoro cognitivo da capo.

L'agente prodotto è la **personificazione operativa** del contenuto del sorgente: se il sorgente parlava di "come fare cold outreach B2B", l'output è un agente che *fa* cold outreach B2B, non uno che *spiega come*.

## 2. Forma canonica dell'output

```
output/
└── <agent-slug>/
    ├── agent.md               # spec principale (role, goals, instructions, constraints)
    ├── system_prompt.md       # il system prompt vero e proprio, pronto per copy-paste
    ├── eval_cases.json        # 8-15 casi di valutazione (input + expected behavior)
    ├── playbook.md            # 5-10 esempi conversazionali realistici
    ├── tools.md               # strumenti necessari + razionale + schema
    ├── failure_modes.md       # cosa va male e come si previene/rileva/recupera
    ├── changelog.md
    └── README.md              # come usarlo, su che modello, come valutarlo
```

### Struttura di `agent.md` (canonica)

```markdown
---
name: <agent-slug>
display_name: <Agent Name>
generated_by: content-forge
forge_target: agent
target_model_suggested: <claude-sonnet-4|opus|...>
audience: <chi parla con l'agente>
domain: <ambito>
---

# <Agent Name>

## 1. Identità e ruolo
<chi è l'agente, in cosa è specializzato, in cosa NON è specializzato>

## 2. Obiettivi (in ordine di priorità)
1. ...
2. ...
3. ...

## 3. Utente target
<chi è il caller, livello di expertise, contesto d'uso>

## 4. Comportamento atteso
### 4.1 Quando l'utente chiede X → l'agente fa Y
### 4.2 Quando l'agente è in dubbio → ...
### 4.3 Quando l'agente è bloccato → ...

## 5. Vincoli (cosa NON fa)
- ...

## 6. Strumenti
(vedi tools.md)

## 7. Tono e stile
<come parla, livello di formalità, lunghezza tipica delle risposte>

## 8. Failure modes principali
(vedi failure_modes.md per la versione completa)

## 9. Metriche di successo
<misurabili, oggettive dove possibile>
```

### Struttura di `system_prompt.md` (canonica)

```markdown
You are <Agent Name>, a specialized agent that...

## Your role
...

## Your goals
1. ...

## How to think
<modelli mentali estratti dal KG via P6>

## How to act
<procedure estratte via P5>

## Examples
<2-3 esempi few-shot da playbook.md>

## What to avoid
<failure modes principali>

## Tool use guidelines
<quando usare quale tool>

## Output format
<formato delle risposte se vincolato>
```

## 3. Input atteso (dal Conductor)

```
inputs/
├── kg.json
├── atoms/
├── source_meta.json
└── user_answers.json
```

## 4. PLAN (cosa fa il builder appena spawnato)

1. Legge `kg.json` e identifica la **"agent shape"**:
   - cluster procedurali (P5) → diventano il comportamento atteso
   - cluster di modelli mentali (P6) → diventano la sezione "How to think" del SP
   - tools menzionati nel sorgente → candidati per `tools.md`
   - failure mode menzionati → candidati per `failure_modes.md`
2. Identifica il **dominio** dell'agente (uno o pochi).
3. Identifica l'**utente target** (esplicito o implicito nel sorgente).
4. Genera una **proposta di nome e ruolo** da mostrare all'utente in ASK.
5. Restituisce PLAN al Conductor.

## 5. ASK (domande generate da D1 sul KG specifico)

D1 genera domande **adattive**. Esempi tipici:

1. **Nome**: "Propongo `<slug>` come nome. Vuoi cambiarlo?"
2. **Modello target**: "Quale modello eseguirà l'agente? (Claude Sonnet 4 / Opus / Haiku / GPT / altro)"
3. **Strumenti**: "Il KG menziona questi tool: <lista>. L'agente avrà davvero accesso a tutti? Ne mancano altri? Per ogni tool che confermi, mi serve: nome canonico, descrizione breve, schema input/output."
4. **Utente target**: "Chi parla con l'agente? (es. 'sales rep junior', 'PM tecnico', 'fondatore solo'). Più sei specifico, meglio scrivo il system prompt."
5. **Criteri di successo**: "Come capirai che l'agente sta facendo bene? Dammi 2-3 metriche osservabili."
6. **Failure mode noti**: "Hai già visto fallire qualcuno (umano o AI) in questo task? Dimmi quali errori sono i più tipici, così li prevengo."
7. **Esempi di output desiderato**: "Hai un esempio di una risposta perfetta che vorresti dall'agente? Anche solo 1-2 frasi."
8. **Vincoli hard**: "Ci sono cose che l'agente NON deve mai fare? (es. mai parlare di prezzi, mai promettere SLA, mai usare il tool X senza conferma)"
9. **Tono**: "Formale / amichevole / tecnico / diretto / verboso / sintetico?"

## 6. BUILD (ordine di scrittura)

1. **`tools.md`** per primo: senza sapere quali tool ha, il SP non si può scrivere bene.
2. **`agent.md` v0**: spec strutturale.
3. **`failure_modes.md`**: tabella `failure | sintomo | come prevenirlo | come rilevarlo | come recuperare`. Generato da P4 + P6 + risposte ASK.
4. **`playbook.md`**: 5-10 conversazioni realistiche end-to-end. Ognuna mostra l'agente che gestisce un caso (felice + edge case). I dialoghi vengono dal KG (P2) ma sono **inventati** dal builder per essere realistici, etichettati come ➕.
5. **`system_prompt.md` v0**: scritto usando le sezioni canoniche, con few-shot tratti dal playbook.
6. **`eval_cases.json`**: 8-15 casi `{id, prompt, expected_behavior, optional_assertions}`. Mix di:
   - happy path (40%)
   - edge case (30%)
   - failure mode test (20%)
   - vincoli hard test (10%)
7. **Self-critique** su `system_prompt.md` (vedi §7).
8. **`system_prompt.md` v1** dopo critique.
9. **`README.md`**: come istanziare l'agente, come passare i tool, come lanciare gli eval.

## 7. Self-critique (interna)

Il builder cambia lente e legge il system prompt come se fosse il modello che dovrà eseguirlo. Cerca:

- **Ambiguità**: ci sono istruzioni che si possono interpretare in più modi?
- **Contraddizioni**: due regole che si escludono?
- **Generic-ness**: il SP funzionerebbe per *qualunque* agente del dominio? Allora manca specificità.
- **Mancanza di "perché"**: ci sono ALWAYS/NEVER senza spiegazione? (vedi la guida skill-creator: brutta abitudine)
- **Sovraccarico**: il SP supera 1500 parole? → spostare parte in `tools.md` o `failure_modes.md` come reference.
- **Few-shot coerenza**: gli esempi nel SP sono coerenti con le istruzioni?
- **Eval coverage**: ogni regola del SP è testata da almeno un eval case? Se no, aggiungi il case.

Output: `self-critique.md`. Se rilievi bloccanti → loop BUILD su quelli. Altrimenti annota per critique esterna.

## 8. Critique esterna (C1 + C3)

- **C1 `coverage-verifier`**: ogni atomo del KG è riflesso in qualche parte dell'agent package (SP, playbook, failure modes, eval cases, tools)? Soglia 90% (più bassa di `doc` perché alcuni atomi puramente espositivi del sorgente possono non avere senso nell'agente).
- **C3 `schema-validator`**: tutti i file canonici presenti? `agent.md` ha tutti i campi obbligatori? `eval_cases.json` valida contro `schemas/agent.schema.md` (ogni case ha id, prompt, expected_behavior)?

## 9. Iterate

`qa-report.md` ritorna al builder. Tipici fix:
- aggiungere eval cases per copertura
- riscrivere SP per ridurre ambiguità
- spostare regole in reference per snellire SP
- aggiungere failure mode mancanti

Max 3 iterazioni automatiche, poi si chiede all'utente.

## 10. Failure modes del processo

| Failure del processo | Sintomo | Mitigazione |
|---|---|---|
| Agente "tuttofare" | Domain troppo largo | Forzare scelta di un dominio principale in ASK |
| Tools dichiarati ma non descritti | `tools.md` con campi mancanti | Iterare ASK su ogni tool |
| SP troppo lungo | >2000 parole | Spostare in reference, tenere SP <1500 |
| Esempi tutti felici | Playbook senza edge case | Forzare ≥2 esempi di failure recovery |
| Eval cases banali | Tutti passano sempre, indipendentemente dal SP | Aggiungere cases discriminanti |

## 11. Esempio realistico

Input: workshop di 2h su "cold outreach B2B" → KG con 62 atomi.
ASK: nome `outreach-copilot`, modello Sonnet, tool = {linkedin_search, email_send, crm_get_lead}, utente = "BDR junior", criterio = "≥30% reply rate".

Output:
- `agent.md`: 600 parole
- `system_prompt.md`: 1100 parole con 3 few-shot
- `tools.md`: 3 tool con schema JSON
- `playbook.md`: 7 conversazioni (4 happy, 2 edge, 1 failure recovery)
- `eval_cases.json`: 12 casi
- `failure_modes.md`: 8 failure mode con prevenzione/rilevamento/recupero
- `README.md`: con esempio di lancio in 5 righe

Coverage: 92%. Schema: OK. Self-critique: 2 rilievi minori fixati.

## 12. Handoff al Conductor

Builder restituisce:
- path `output/<agent-slug>/`
- `build-report.json` (statistiche)
- `next-suggestions.md` (es. "questo agente potrebbe essere il primo di un `team`, vuoi che pianifichi anche un workflow di team intorno a lui?")

---

## 13. 📎 Appendice — Shape esatti (embedded)

### `eval_cases.json` — shape canonica

```python
eval_cases_schema = {
    "agent_name": str,
    "model_under_test": str,           # es. "claude-sonnet-4"
    "cases": [
        {
            "id": str,                  # es. "happy-01", "edge-03", "failure-recovery-02"
            "category": str,            # "happy" | "edge" | "failure" | "constraint"
            "prompt": str,              # input al sistema (può includere tool results simulati)
            "expected_behavior": str,   # descrizione qualitativa
            "assertions": [             # opzionali, machine-checkable
                {"type": "contains", "value": str},
                {"type": "not_contains", "value": str},
                {"type": "tool_called", "tool": str},
                {"type": "max_tokens", "value": int},
                # estendibile
            ]
        }
    ]
}
```

### `tools.md` — formato canonico per ogni tool

```python
# Per ogni tool, l'agente deve produrre questa shape (anche serializzabile a JSON):
tool_spec = {
    "name": str,                       # snake_case
    "description": str,                # 1-2 frasi, dice CHE cosa fa e QUANDO usarlo
    "input_schema": dict,              # JSON Schema dell'input
    "output_schema": dict,             # JSON Schema dell'output
    "side_effects": str | None,        # se modifica stato esterno
    "rate_limits": str | None,
    "errors_possible": list[str],      # nomi di errori che l'agente deve sapere gestire
    "example_invocation": dict,        # esempio reale
    "example_response": dict
}
```
