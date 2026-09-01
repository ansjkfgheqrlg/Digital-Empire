# PT04 — Question Designer Pattern (Dynamic ASK Phase)

> **Shape canonica**: La fase ASK (raccolta input da utente) **non è una checklist statica**. È gestita da un agente dedicato (`question-designer`) che legge il Knowledge Graph specifico del run, decide quali domande sono necessarie (omette quelle che il KG già risponde), propone default pre-compilati dove può, ordina per criticità, raggruppa in batch.

## Quando applicarlo

✅ **Applica se**:
- Skill ha fase ASK con >5 domande possibili
- Domande dipendono dal sorgente specifico
- Vuoi UX efficiente (utente risponde solo a domande non deducibili)

❌ **NON applicare se**:
- Solo 1-3 domande sempre necessarie (overhead non vale)
- Skill non-interactive (batch processing)
- Domande non dipendono dal contesto

## Perché funziona

### 1. Le checklist statiche frustrano l'utente
Se la skill chiede 15 domande di cui 10 sono già nel sorgente (es. "in che lingua?" quando il KG ha lingua=it), l'utente diventa frustrato. Sente che il sistema non "ascolta".

Dynamic ASK omette domande deducibili → utente risponde a 3-5 domande reali invece di 15.

### 2. Default pre-compilati riducono friction
Invece di "Quale modello?" → "Propongo Claude Sonnet 4. Confermi?". 1-click acceptance vs typing risposta.

### 3. Ordering per criticità = best signal first
Domande "blocking" prima, "preferred" dopo, "optional" in fondo. L'utente che si stanca a metà ha comunque dato le info critiche.

## Esempio dal nostro percorso

`D1 question-designer-agent` in content-forge:

```python
ask_set_shape = {
    "target": str,
    "total_questions": int,
    "presentation_batches": [
        {
            "batch_id": int,
            "questions": [
                {
                    "id": str,
                    "question": str,
                    "type": "confirm" | "choose_one" | "choose_multi" | "free_text" | "file_path",
                    "options": list[str] | None,
                    "default_proposal": str | None,
                    "rationale": str,  # mostrato all'utente: perché chiediamo
                    "criticality": "blocking" | "preferred" | "optional",
                    "depends_on": list[str] | None
                }
            ]
        }
    ]
}
```

Per ogni target, D1 ha un template di domande possibili. Per ogni domanda chiede: "il KG già risponde?" → omit. "Posso proporre default?" → pre-fill.

## Esempi di adattività concreta

### Template generico
"In che lingua deve essere l'output?"

### Adattato dal KG
"Il KG indica lingua=it (sorgente italiano). Confermi italiano per output, o vuoi traduzione in en?"
**Type**: confirm. **Default**: "it"

→ Utente fa OK in 1 click invece di scrivere "italiano".

### Template generico
"Quali strumenti userà l'agente?"

### Adattato dal KG
"Il KG menziona questi tool: `linkedin_search`, `crm_get_lead`, `email_send`. Confermi tutti? Mancano altri? Per ognuno mi serve schema input/output."
**Type**: free_text. **Default**: lista pre-compilata.

## Batching strategy

Max 6 domande per batch. Se >6, dividi in batch successivi (B2 solo dopo che B1 ha risposte):

```
Batch 1 (5 critiche):    blocking + preferred prioritarie
   ↓ utente risponde
Batch 2 (3-4 opzionali): refinements
   ↓
(eventuali batch 3+ per casi complessi tipo workflow)
```

Senza batching: lista 15 domande → utente abbandona.
Con batching: utente percepisce "5 domande, manageable", scopre dopo che ce ne sono altre se necessario.

## ➕ Esempio in altri domini

**TurboTax**: domande tax adattate alla situazione. Sapere già che hai casa → no domanda "hai casa?", invece "hai casa singola o multipla?". Same pattern.

**Smart forms** in healthcare: domande EHR-conditional (se paziente femmina + età X → domanda gravidanza appare). Same pattern.

**Conversational onboarding** (Stripe, Notion): non form lungo, ma 3-5 domande adattate al "use case" scelto in step 1.

## Anti-pattern correlato

**Static checklist**: 15 domande fisse sempre uguali, ignora context. Utente compila roba ridondante.

**Anti-pattern duale**: **Over-inferential** — assume troppo dal KG, non chiede info critiche pensando di averle dedotte. Risultato: output sbagliato basato su assunzioni. Fix: domande "blocking" sempre chieste, anche se sembrano deducibili.

## Trade-off

| Pro | Contro |
|---|---|
| UX boost (meno domande) | 1 agente in più da mantenere (D1) |
| Default pre-compilati = velocità | Logic di adattività complessa |
| Ordering = best signal first | Domande dinamiche più difficili da testare |
| Batching = no overwhelm | KG must be accurate per omitting |

## Decision tree

```
La tua skill ha fase ASK con >5 domande possibili?
├─ NO → ask inline nel builder, no pattern dedicato
└─ SÌ → continua
   ├─ Le domande variano per sorgente/contesto?
   │  ├─ NO → static checklist OK
   │  └─ SÌ → continua
   ├─ Puoi dedurre alcune risposte da KG?
   │  ├─ NO → ask tutte, no omitting
   │  └─ SÌ → dynamic ASK pattern (D1 agent)
   │
   └─ Implementa:
      1. Agente D1 (question-designer-agent) dedicato
      2. Per ogni target/builder, template domande possibili
      3. Logic: "questa domanda è risposta dal KG?" → omit
      4. Default proposal dove possibile
      5. Ordering: blocking → preferred → optional
      6. Batching: max 6 per batch
```

## Connessioni

- Combina con: PT01 (Conductor with Subagents) — D1 è agente specializzato
- Combina con: P04 (Interactive Scaffolding) — D1 è il "A" di PLAN→ASK→BUILD
- Vedi anche: P15 (Trigger Design) — analogo: precision over recall

## Riferimenti

- Progressive disclosure in UX (Nielsen)
- TurboTax adaptive interview pattern
- Conversational forms (Typeform, ManyChat)
