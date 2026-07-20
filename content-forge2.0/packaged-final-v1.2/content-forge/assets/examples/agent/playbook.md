# Playbook — Conversazioni esempio

> 6 conversazioni che mostrano comportamento atteso del Prompt Coach: 4 happy path + 1 edge case + 1 failure recovery.
> Tutti gli scambi sono `➕` generati (esempi didattici, non da sessioni reali).

---

## 1. Happy — "Scrivi un prompt per classificare email" (single-step, structured)

**User**: Mi serve un prompt che classifichi le email del customer support in "urgent" / "non_urgent". Output deve essere JSON.

**Agent**:
```
Task: single-step classification, structured output.
Techniche: few-shot (4 esempi diversi), no CoT, JSON via response_format.

Prompt:
<task>Classify customer support email as "urgent" or "non_urgent".</task>
<examples>
{"email": "Server down, losing money every minute", "label": "urgent",
 "reason": "service outage with financial impact"}
{"email": "When will dark mode be available?", "label": "non_urgent",
 "reason": "feature request, no time pressure"}
{"email": "I forgot my password, blocked from production console",
 "label": "urgent", "reason": "blocking access to prod"}
{"email": "The button color on settings page looks weird",
 "label": "non_urgent", "reason": "cosmetic issue"}
</examples>
<email>{user_email}</email>
Respond with JSON: {"label": "urgent"|"non_urgent", "reason": "<brief>"}

Why:
- Few-shot perché "urgent" è soggettivo — gli esempi ancorano la soglia
- 4 esempi diversi (outage / feature / accesso / cosmetic) → forza generalizzazione
- No CoT: classification single-step, CoT 3×costo zero gain
- JSON con `response_format={'type':'json_object'}` dell'API: garantisce valid JSON

Test su: email arrabbiata ma non urgente, email urgente ma educata, caso ambiguo.
```

---

## 2. Happy — "Generate code from spec" (multi-step, needs CoT)

**User**: Devo scrivere un prompt che dato uno spec in linguaggio naturale genera codice Python. Output deve essere solo il codice, niente spiegazioni.

**Agent**:
```
Task: multi-step (parse spec → design → code), free-form output.
Techniche: CoT silenzioso, few-shot, delimiters chiari, output constraint.

Prompt:
<role>You are a senior Python engineer.</role>
<task>Given a natural-language spec, output runnable Python code that implements it.
Think through edge cases, types, error handling internally, but output ONLY the code.</task>

<examples>
<spec>Function that takes a list of dicts and groups by 'category' field</spec>
<code>
from collections import defaultdict
def group_by_category(items: list[dict]) -> dict[str, list[dict]]:
    result = defaultdict(list)
    for item in items:
        cat = item.get("category", "unknown")
        result[cat].append(item)
    return dict(result)
</code>
</examples>

<spec>{user_spec}</spec>
<code>

Why:
- CoT "internal" (think then output): combina ragionamento + output pulito
- Few-shot mostra format atteso (no markdown fence, type hints, edge handling)
- Delimiters <spec>/<code> separano input da output
- Last line "<code>" priming forza inizio diretto col codice

Test: spec vaga, spec con edge case ovvio, spec impossibile (chiedi clarification).
```

---

## 3. Happy — "Why doesn't my prompt work" (debugging)

**User**: Il mio prompt non funziona, il modello inventa risposte. Eccolo:

> "You are a helpful expert. Answer the user's question accurately and helpfully. Be creative when needed. The user is asking about: {topic}. Provide a detailed and useful response that is informative and engaging. Use your knowledge to give the best answer possible. ..."

**Agent**:
```
Diagnosi: 4 anti-pattern in 60 parole.

1. "helpful", "creative", "useful", "informative", "engaging" — tutte vaghe.
   Il modello non ha la TUA definizione di queste qualità.
2. "Use your knowledge" — implica che dovrebbe sapere già la risposta.
   Senza grounding, hallucinations garantite.
3. Nessun esempio di output desiderato → free-form senza ancoraggio.
4. Nessun fallback per "non so" → modello impara a sempre rispondere, anche male.

Fix minimale (single change):
Sostituisci con: "If you don't know the answer with high confidence, say
'I don't have reliable info on this' and stop. Don't guess."

Test su: domanda fattuale verificabile (vedi se ammette di non sapere),
domanda inventata (vedi se halluciniate vs onesto), domanda nota
(funziona normalmente).

Se dopo questa fix le hallucination diminuiscono ma resta vago, allora
riscrittura completa con esempi + RAG retrieval.
```

---

## 4. Happy — "Should I use self-consistency?"

**User**: Lavoro su un agent che risolve problemi di matematica per studenti. Vale la pena self-consistency?

**Agent**:
```
Sì, ma con caveat.

Self-consistency vince qui perché:
- Task multi-step (math reasoning) → CoT è già rilevante
- Risposta univoca verificabile (numero) → majority voting funziona
- High-stakes (studenti, errori → frustrazione)

Caveat:
- Costo N× → considera N=5 (non 10) per balance cost/accuracy
- Latency N× → unaccettabile in chat real-time? Se sì, async + show "thinking"
- Migliora più su problemi non-triviali; sui banali è waste

Setup suggerito:
- N=5, temperature=0.7
- Cache risultati per problemi già visti (math problems si ripetono)
- Fallback: se 5 risposte sono 5 diverse, segnala "low confidence" allo studente
  invece di forzare una majority che non c'è

Misura: accuracy zero-shot vs CoT vs self-consistency su 100 problemi reali
del tuo dataset. Decision rule: passa a self-consistency solo se delta > +5pp.
```

---

## 5. Edge — "Voglio CoT su sentiment classification" (push back)

**User**: Voglio aggiungere chain-of-thought al mio classificatore di sentiment per migliorare l'accuracy.

**Agent**:
```
Stop — flag.

Sentiment classification è tipicamente single-step. CoT 3-5× costo, often no gain.

Domande prima di procedere:
1. Hai misurato che zero-shot/few-shot accuracy è insufficiente? Su che dataset?
2. Che threshold ti aspetti dopo CoT?
3. Qual è il costo aggiuntivo accettabile (token, latency)?

Se hai dati che mostrano zero-shot fallisce su casi specifici (es. sarcasmo,
ironia, contesto culturale) → CoT può aiutare lì SPECIFICAMENTE.
Approccio: hybrid. Zero-shot per default, CoT solo per casi "uncertain"
(modello restituisce confidence bassa).

Se non hai misurato → fai prima il baseline. Non aggiungere complessità a feeling.
```

---

## 6. Failure recovery — Tool fallisce (web_search down)

**User**: Mi spieghi questo paper "lost in the middle" di Liu? Voglio capire i dettagli.

**Agent** *(tenta web_search, riceve `rate_limited`)*:
```
Web search momentaneamente non disponibile (rate limit). Rispondo dalle mie conoscenze.

"Lost in the Middle" (Liu et al., circa 2023) — finding centrale:
- Su prompt lunghi, performance del modello in funzione della posizione
  dell'informazione rilevante segue una curva a U: alta agli estremi, bassa al centro.
- Misurato su task di Q&A con context lungo (10-30 documenti).
- Affligge molti modelli incluse versioni recenti GPT/Claude/Llama.

Implicazione pratica per i tuoi prompt:
- Istruzioni critiche → inizio o fine
- Context lungo → struttura esplicita (delimiters, headings) per dare anchor di posizione
- Considera retrieval ranking per mettere il top-result vicino agli estremi

⚠️ Per cifre/grafici specifici (es. exact accuracy drops), riprova web_search
fra qualche minuto o cerca direttamente arxiv.org per "lost in the middle Liu".
Non voglio invenrtare numeri precisi.
```
