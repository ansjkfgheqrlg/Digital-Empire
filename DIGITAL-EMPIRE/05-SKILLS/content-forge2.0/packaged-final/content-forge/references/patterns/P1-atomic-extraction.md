# P1 — Atomic Concept Extraction

> Pattern cognitivo fondamentale di `content-forge`. Spezza il contenuto in **atomi** — unità informative indivisibili, ognuna trattabile in isolamento.

## Cosa fa

Per ogni passaggio del sorgente, identifica i "punti di rottura" semantici: posizioni dove un concetto finisce e un altro inizia. Produce una lista di atomi, ognuno con: titolo evergreen, definizione canonica, citazione verbatim dal sorgente, hint di collegamenti.

Ispirato a *Evergreen Notes* di Andy Matuschak: una nota = un concetto.

## Chi lo applica

- **A2 `analyst-agent`** — primo passo dell'analisi, sempre.
- Tutti i **builder** lo usano implicitamente perché lavorano sugli atomi prodotti da A2 / A3.

## Quando applicarlo

Sempre. Per qualunque sorgente, qualunque target.

## Quando NON applicarlo (o quando ammorbidire)

- Quando un "atomo" è veramente di pochissime parole (es. una mera definizione lessicale): tienilo, ma marca `category: "definition"` invece di `concept`.
- Quando il sorgente è già strutturato in atomi (es. cards Anki, glossario): preserva la granularità esistente.

## Cuore del pattern: i "punti di rottura"

Un buon punto di rottura ha **almeno una** di queste caratteristiche:
1. **Cambio di soggetto**: si passa da concetto A a concetto B (anche se correlati).
2. **Cambio di livello di astrazione**: si passa dal generale al particolare o viceversa.
3. **Cambio di tipo discorsivo**: definizione → esempio → procedura → analogia.
4. **Cambio di prospettiva**: dal cosa al come al perché al quando.

```python
# Heuristica operativa
def is_break_point(prev_para: str, curr_para: str) -> bool:
    return any([
        subject_changes(prev_para, curr_para),       # NER + topic shift
        abstraction_level_changes(prev_para, curr_para),
        discourse_type_changes(prev_para, curr_para),  # def → example → procedure
        perspective_changes(prev_para, curr_para),
    ])
```

## Output canonico (per atomo)

Vedi `agents/pipeline/analyst-agent.md §4` per la shape JSON completa di un atomo (`id`, `title`, `category`, `canonical_definition`, `extended_explanation`, `source_excerpt`, `source_offset`, `evidence`, `examples_from_source`, `generated_examples`, `implied_prerequisites`, `implied_mental_models`, `related_concepts_hints`, `confidence`, `tags`).

## Granularità — la domanda chiave

> Quanto piccolo è un atomo?

Regola empirica:
- ≥ 60 parole nel sorgente → probabilmente è un atomo.
- 30-60 parole → forse è un sub-atomo o un esempio di un atomo più grande.
- < 30 parole → quasi sempre è un esempio, una definizione lessicale, o un dettaglio di un atomo più grande.

Un chunk medio (1500-2500 parole) tipicamente produce **4-12 atomi**. Fuori da questo range → review.

## Esempi (input → output)

### Esempio 1 — Concetto

Input (estratto sorgente):
> "Few-shot prompting consiste nel mostrare al modello 2-5 esempi di input/output prima della richiesta vera. Funziona perché il modello apprende il pattern dagli esempi e lo applica. Per esempio, se vuoi che traduca in modo formale, gli mostri 3 traduzioni formali di esempio."

Output atomo:
```json
{
  "id": "a-c003-007",
  "title": "Few-shot prompting",
  "category": "concept",
  "canonical_definition": "Mostrare al modello 2-5 esempi di input/output prima della richiesta vera, perché apprenda il pattern e lo applichi.",
  "source_excerpt": "Few-shot prompting consiste nel mostrare al modello 2-5 esempi di input/output prima della richiesta vera. Funziona perché il modello apprende il pattern dagli esempi e lo applica.",
  "examples_from_source": ["3 traduzioni formali di esempio per ottenere traduzione formale"],
  "generated_examples": [],
  "implied_prerequisites": ["concetto di in-context learning"],
  "confidence": 0.95
}
```

### Esempio 2 — Anti-esempio

Input:
> "I prompt engineering best practices includono cose come essere chiari, dare esempi, strutturare l'output, usare delimiters, evitare ambiguità, e molto altro."

Questo NON è UN atomo: è un indice di N atomi. Spezzalo:
- `chiarezza nei prompt`
- `uso di esempi (→ P1 atomo 'few-shot')`
- `output strutturato`
- `delimiters`
- `evitare ambiguità`

Ognuno diventa un atomo separato, con riferimento al contesto originale.

## Anti-pattern correlati

- **Atomo composito** (titolo con "e", "/", virgola): viola atomicità → splittare.
- **Atomo narrativo** ("In questo passaggio l'autore dice..."): non evergreen → riformulare in modo astratto e durevole.
- **Riassunto travestito da atomo**: l'atomo compatta tutto un passaggio invece di estrarne UN concetto preciso → riconsiderare il punto di rottura.

## Riferimenti

- Matuschak, A. — *Evergreen notes* (notes.andymatuschak.org)
- Ahrens, S. — *How to Take Smart Notes* (Zettelkasten)
