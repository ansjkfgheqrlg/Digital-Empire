# FAQ

> Generata da steel-manning (P4) delle claim non banali del workshop. Ogni Q&A formula la **migliore obiezione possibile** alla claim originale, seguita da una risposta che concede ciò che va concesso e riprecisa la claim.

## Q1. Few-shot non è sempre meglio di zero-shot, vero?

Vero. Few-shot ha un costo (token + complexity prompt) e non sempre vale la pena.

**Casi in cui zero-shot batte few-shot**:
- Modelli istruiti su task molto comuni (es. classificazione sentiment generica)
- Quando il formato output è ovvio dal task descrittivo
- Quando hai vincoli stretti di context window

**Regola operativa**: prova zero-shot prima, passa a few-shot solo se accuracy < target. Misura.

## Q2. CoT è sempre meglio di risposta diretta?

No. CoT su task semplici può **peggiorare**: la verbosità introduce errori intermedi che si propagano, e il modello istruito ha spesso la risposta corretta in zero-shot.

**CoT vince quando**:
- Task multi-step (matematica, planning, logica)
- Quando la risposta intermedia è verificabile

**CoT perde quando**:
- Pattern matching diretto
- Risposte molto brevi
- Cost-sensitive (CoT costa 3-10x in token)

## Q3. Self-consistency vale il costo (N×)?

Dipende dalla **posta in gioco** del task.

- **Sì** per task con risposta univoca corretta + alto valore (math reasoning, code generation critico)
- **No** per task generativi liberi (creative writing, brainstorming) — non c'è "risposta corretta"
- **No** per task ad alta latency tolerance (dove un singolo run è già lento)

## Q4. JSON mode/function calling rendono inutili i prompt strutturati?

No, sono **complementari**.

JSON mode forza la sintassi (output sempre valido JSON), ma **non la semantica** (campi giusti, valori sensati). Per quello servono:
- schema esplicito nel prompt
- 1-2 esempi di output ben formato
- istruzioni chiare sui vincoli per campo

JSON mode senza il resto = JSON sintatticamente valido ma semanticamente sbagliato.

## Q5. "Be creative" è davvero così male?

Sì, in generale. Ma ci sono eccezioni narrow.

**Quando "be creative" funziona malgrado tutto**: task molto convenzionalmente "creativi" (poesia, brainstorming aperto) dove la varianza è il *valore*, non un bug.

**Quando NON funziona** (caso comune): task dove "creative" è proxy per qualcosa di specifico (es. "creative product names" → meglio "product names that combine technical accuracy with playful tone, like these 3 examples: [...]").

## Q6. Versioning di prompt come codice — è overkill per progetti piccoli?

Per side project esplorativi, sì.

Per **qualsiasi prompt che gira in produzione (anche solo internamente)**, no — è il minimo. La regressione silenziosa di un prompt cambiato "a senso" è tra i bug più subdoli e costosi da debuggare *dopo*.

**Soglia operativa**: se il prompt è usato >100 volte al mese o è in un flow critico, versionalo. Altrimenti annota almeno l'ultimo cambio in cima al file.
