# P4 — Steel-manning & Counter-examples

> Per ogni tesi non banale, generare **la migliore obiezione possibile** e una **risposta forte**. Per ogni concetto, generare almeno un **controesempio** che chiarisca i confini.

## Cosa fa

Forza il sistema a confrontarsi con le obiezioni più valide alle proprie tesi (non quelle deboli — "straw-manning"). Produce contenuto **più robusto e più utile**: l'utente impara non solo cosa funziona, ma anche **quando NON funziona** e perché.

## Chi lo applica

- **B1 `doc-builder`** — sezione FAQ (steel-manning → Q&A).
- **B4 `skill-builder`** — sezione "Quando NON usare questa skill" + edge cases negli evals.
- **B7 `wiki-builder`** — sezione "Contrasta con [[<concetto-opposto>]]" e "Limiti" in ogni nota.
- Tutti i builder possono attingere per failure_modes / anti-patterns / edge case eval.

## Quando applicarlo

- Sempre per tesi forti del sorgente (claims con conseguenze pratiche).
- Sempre per concetti che si distinguono da concetti vicini (es. "few-shot" vs "fine-tuning").
- Talvolta per definizioni (controesempio = cosa NON è coperto dalla definizione).

## Quando NON applicarlo

- Per pure definizioni lessicali (non hanno opposizione sensata).
- Quando il sorgente è già una "voce sola" e l'utente vuole quella prospettiva (es. opinion piece).

## Cuore del pattern

```python
# Steel-man triple
steelman = {
    "claim": str,                      # la tesi originale
    "best_objection": str,             # la migliore obiezione, formulata in modo convincente
    "objection_strength": str,         # perché l'obiezione è forte (non straw)
    "strong_response": str,            # come rispondere mantenendo la tesi (se possibile)
    "concession_if_any": str,          # cosa la tesi deve cedere all'obiezione (ammissione onesta)
}

# Counter-example triple
counter_example = {
    "concept": str,
    "near_case_that_isnt": str,        # caso che SEMBRA il concetto ma non lo è
    "why_not": str,                    # cosa lo distingue
}
```

## Come si fa uno steel-man fatto bene

1. **Identifica chi obietterebbe**: un esperto del campo, un utente con caso d'uso particolare, una scuola di pensiero alternativa.
2. **Formula l'obiezione nella sua versione più forte**: cita dati, ragioni concettuali, casi reali — non versioni deboli.
3. **Rispondi senza minimizzare**: se l'obiezione è valida, ammettilo. Distingui dove la tesi vale e dove no.
4. **Riformula la tesi più precisamente** se l'obiezione l'ha ammorbidita.

## Esempio (claim → steel-man)

**Claim** (dal sorgente): "Chain-of-thought (CoT) prompting migliora sempre l'accuracy del modello su task di ragionamento."

**Steel-man (auto-generato, ➕)**:

> **Obiezione forte**: CoT può *peggiorare* la performance su task semplici o su task in cui il modello già aveva l'intuizione corretta. La verbosità introduce errori intermedi che si propagano. Su MMLU senza ragionamento esplicito richiesto, modelli istruiti spesso fanno meglio in zero-shot diretto che in CoT lungo. (Ref: alcune ablation in papers post-CoT originale.)
>
> **Risposta forte**: La claim originale è vera per task **multi-step** e **non triviali**. Su single-step / pattern-matching, CoT è overhead non necessario. Riformulazione precisa: "CoT migliora l'accuracy *quando il task richiede ragionamento intermedio esplicito*; non è una panacea universale."
>
> **Concessione**: la versione assoluta della claim è eccessiva.

Questa coppia diventa, nel doc finale, una entry FAQ. Nella wiki, una nota separata `[[Quando CoT NON aiuta]]`.

## Esempio (controesempio)

**Concetto**: "Few-shot prompting".

**Near-case che non lo è (➕)**: dare al modello **una sola** dimostrazione (n=1) tipicamente si chiama "one-shot", non few-shot. Anche se è "pochi", la dinamica è diversa: con n=1 il modello non può inferire pattern, solo seguire un esempio (più rischio di overfitting all'esempio).

**Why**: il valore di few-shot sta nell'**aggregato** di esempi che fanno emergere un pattern; n=1 perde questa proprietà.

## Algoritmo (pseudo)

```python
def generate_steelman(claim: str, kg: dict, domain: str) -> dict:
    """Genera obiezione + risposta + concessione opzionale."""
    # 1. Identifica scuole di pensiero alternative nel KG / dominio
    # 2. Per ogni alternativa, genera l'obiezione più forte alla claim
    # 3. Valuta la forza dell'obiezione (peso 0-1)
    # 4. Scegli l'obiezione più forte (>0.6)
    # 5. Costruisci risposta che CONCEDA la parte valida e riprecisi la claim
    return {"claim": claim, "best_objection": ..., "strong_response": ...}

def generate_counter_example(concept: str, kg: dict) -> dict:
    """Genera un near-case che NON è il concetto, per chiarire i confini."""
    # 1. Trova concetti adiacenti nel KG (via edge sibling_of / see_also)
    # 2. Tra quelli, scegli quello più facilmente confuso col concept
    # 3. Articola perché NON è il concept
    return {"concept": concept, "near_case_that_isnt": ..., "why_not": ...}
```

## Anti-pattern

- **Straw-manning**: formulare un'obiezione debole solo per "smontarla" facilmente. È peggio che niente — segnala disonestà intellettuale.
- **Concessione passiva-aggressiva** ("alcuni sostengono ma sbagliano"): non è uno steel-man.
- **Controesempio irrilevante**: prendere qualcosa di completamente diverso ("X è caldo, ma il numero 5 non è caldo") → non aiuta a chiarire i confini.

## Riferimenti

- Daniel Dennett — *Intuition Pumps*, regole del "rapport disagreement"
- Rationalist community — steelmanning / Ideological Turing Test
