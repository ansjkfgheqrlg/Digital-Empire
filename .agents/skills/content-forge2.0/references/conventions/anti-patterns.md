# Anti-Patterns (cosa NON fare)

> Catalogo completo. Lo legge ogni builder prima di scrivere, e il quality-critic (interno) lo usa come checklist.

## 🚫 1. Riassunto strisciante

Output più corto del sorgente, oppure presenza di:

```python
FORBIDDEN_PHRASES_IT = [r"in sintesi", r"riassumendo", r"in breve",
                        r"in conclusione", r"tl;dr", r"per farla breve",
                        r"i tre punti chiave"]
FORBIDDEN_PHRASES_EN = [r"in summary", r"to summarize", r"in short",
                        r"tl;dr", r"the (three|four|five) key points"]
```

Eccezione tollerata: in `references/processes/custom.md` §5 il termine è ammesso solo come meta-comunicazione di disambiguazione, sostituito con "ricapitolando".

## 🚫 2. Invenzione di fatti

Aggiungere come se fosse del sorgente qualcosa che il sorgente non dice. Tutto ciò che è generato DEVE essere etichettato con `➕`.

## 🚫 3. Coverage parziale silenziosa

Saltare atomi senza dichiararli `out_of_scope` con razionale. Sempre coverage_map.md (per custom) o coverage report C1 (altri target).

## 🚫 4. ALWAYS/NEVER senza perché

Istruzioni rigide a maiuscolo senza spiegazione del rationale → l'LLM downstream non sa adattarsi. Sempre spiegare il *perché*.

## 🚫 5. God-step / God-agent / God-skill

Un singolo componente che fa 5 cose distinte. Se SP >2000 parole → splittare in reference.

## 🚫 6. Esempi tutti dal sorgente

Senza alcun `➕` esempio aggiuntivo, l'output è solo "riformulazione". Forzare ≥1 esempio generato per atomo non-banale.

## 🚫 7. Esempi tutti happy path

Eval cases / playbook senza edge case e failure recovery → test non discriminanti.

## 🚫 8. Schema-less output

Output strutturato (agent, team, workflow, ...) senza file canonici previsti → schema validator (C3) fallirà.

## 🚫 9. Cross-file inconsistency

Termini definiti diversamente in capitoli diversi, naming non uniforme tra file dello stesso output.

## 🚫 10. Skipping ASK phase per "guadagnare tempo"

I builder complessi DEVONO passare per ASK. Senza ASK = build a freddo = drift garantito.

## 🚫 11. Output che parla all'utente

Gli agent producono artefatti, non rispondono all'utente. Toni tipo "ecco il tuo agente!" sono fuori posto.

## 🚫 12. Templates riempiti meccanicamente

I template in `assets/templates/` sono *scaffolding*, non *cookie cutter*. Il builder li adatta, non li compila ciecamente.

## 🚫 13. Confusione di responsabilità tra ruoli (per `team`)

Due agenti del team con stessa `responsible` in RACI → errore di design. Forzare R singolo.

## 🚫 14. Wikilink rotti (per `wiki`)

`[[slug]]` che non risolve a un file esistente. `obsidian_packager.py` deve fallire.

## 🚫 15. DAG con cicli (per `workflow`)

Workflow con ciclo → non è un DAG. Validator (Kahn) deve fallire.

---

## ℹ️ Contesti in cui le parole-bandiera sono AMMESSE (whitelist)

Lo script `no_summary_lint.py` deve riconoscere e ignorare:

1. **Citazioni come anti-pattern**: frasi tipo "evita 'in sintesi'", "non usare 'riassumendo'" sono OK perché sono *menzioni*, non *uso*.
2. **Documentazione meta**: dentro `PLAN-*.md`, `README.md`, `references/conventions/`, `references/processes/<*>.md §appendice` la menzione è esplicativa.
3. **Custom escape**: `references/processes/custom.md` §5 ammette esplicitamente "ricapitolando" come meta-comunicazione, mai come modalità di output.
4. **Blocchi code (` ```python `)**: dentro a regex/liste forbidden, l'occorrenza è LETTERALE, non output.

```python
# Heuristica di context-aware lint
def is_legitimate_mention(text_around: str) -> bool:
    """True se l'occorrenza è meta (citazione/whitelist), non comportamento."""
    triggers = ["evita", "non usare", "vietato", "forbidden", "FORBIDDEN_",
                "anti-pattern", "do not use", "scaffold", "PLAN"]
    return any(t.lower() in text_around.lower() for t in triggers)
```
