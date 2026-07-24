# P6 — Mental Model Surfacing

> Estrae i **modelli mentali impliciti** dell'autore del sorgente: metafore ricorrenti, frame interpretativi, analogie, ontologie. Li rende espliciti per essere usati dal target (es. "How to think" del system prompt di un agente).

## Cosa fa

Distingue tra **contenuto esplicito** (cosa l'autore dice) e **modello mentale implicito** (come l'autore *vede* il mondo per dire quelle cose). Il modello mentale è spesso più potente del contenuto: replicarlo permette di generalizzare ai casi che il sorgente non copre.

## Chi lo applica

- **A2 `analyst-agent`** annota `implied_mental_models` come hint.
- **B2 `agent-builder`** — diventa la sezione "How to think" del SP (la sezione più "pesante" dell'agente: gli dà la lente con cui leggere il mondo).
- **B3 `team-builder`** — modello mentale del coordinator + di ogni ruolo.
- **B1 `doc-builder`** — diventa una sezione "Modelli mentali" o "Frame interpretativi" del doc.
- **B7 `wiki-builder`** — note in `frameworks/`.

## Quando applicarlo

Sempre. Anche il sorgente più tecnico ha modelli mentali impliciti (es. un tutorial su RAG implica un certo modo di pensare "memoria" e "retrieval").

## Quando ammorbidire

- Sorgenti molto eterogenei (multi-autore con visioni diverse): identifica modelli mentali per cluster, non per l'intero KG.

## Cuore del pattern

I modelli mentali si manifestano come:

| Tipo | Esempio nel sorgente | Cosa estrarre |
|---|---|---|
| **Metafora** | "il prompt è come una conversazione con un collega smart" | frame: "modello = collega cooperativo" |
| **Analogia operativa** | "RAG funziona come Google interno alla risposta" | frame: "LLM + retrieval = motore di ricerca cognitivo" |
| **Ontologia** | "ci sono 3 livelli di prompt: zero/few/CoT" | tassonomia: levels of explicit reasoning |
| **Heuristic** | "se non funziona, dai più esempi" | rule of thumb: "underperformance → more demonstrations" |
| **Anti-frame** | "non pensare al modello come a un database" | cosa NON è (definisce per contrasto) |
| **Value loaded** | "i prompt brevi sono migliori" | giudizio implicito: brevity = quality |

## Algoritmo (pseudo)

```python
def surface_mental_models(text: str, kg: dict) -> list[dict]:
    """Estrae modelli mentali impliciti dal sorgente."""
    mms = []
    # 1. Cerca metafore e analogie ("è come", "come se fosse", "pensa a X come Y")
    for m in find_metaphors(text):
        mms.append({"type": "metaphor", "source": m, "frame": extract_frame(m)})
    # 2. Cerca tassonomie esplicite ("ci sono N tipi", "i livelli sono", "le categorie")
    for t in find_taxonomies(text):
        mms.append({"type": "ontology", "source": t, "frame": extract_taxonomy(t)})
    # 3. Cerca heuristics ("regola generale", "se X allora Y", "tipicamente")
    for h in find_heuristics(text):
        mms.append({"type": "heuristic", "source": h, "frame": extract_rule(h)})
    # 4. Cerca anti-frame ("non è un X", "non pensare in termini di Y")
    for af in find_antiframes(text):
        mms.append({"type": "anti_frame", "source": af, "frame": extract_negation(af)})
    return mms
```

## Output canonico (per atomo o per cluster)

```python
mental_model = {
    "id": str,
    "type": str,                      # "metaphor" | "analogy" | "ontology" | "heuristic" | "anti_frame" | "value"
    "concise_name": str,              # nome breve evergreen ("Modello = collega cooperativo")
    "explanation": str,               # 2-4 frasi
    "source_evidence": list[str],     # citazioni dal sorgente che lo manifestano
    "implications": list[str],        # cosa cambia se adotti questo modello (vs alternativa)
    "alternatives": list[str],        # modelli mentali alternativi sullo stesso dominio
    "applies_to": list[str],          # atom_ids del KG
}
```

## Esempio (sorgente → modello mentale)

**Sorgente** (estratti):
> "Quando scrivi un prompt, immagina di parlare con un collega molto sveglio ma che è appena arrivato. Sa tutto in astratto, ma del TUO contesto specifico non sa nulla."
>
> "Non dare per scontato che il modello capisca cosa intendi. Se a un collega umano serviva un esempio, al modello serve un esempio."
>
> "L'errore tipico è trattare il modello come un motore di ricerca: dare una query e aspettarsi una risposta. Trattalo come un collega: dagli contesto, esempi, vincoli."

**Modello mentale estratto** (➕):

```yaml
id: mm-001
type: metaphor
concise_name: "Modello come collega cooperativo nuovo del progetto"
explanation: |
  Il modello è competente in astratto ma ignaro del contesto specifico.
  Va trattato come un collega umano al primo giorno: gli dai contesto,
  esempi, vincoli, ti aspetti che ragioni — NON come un motore di ricerca.
source_evidence:
  - "immagina di parlare con un collega molto sveglio ma che è appena arrivato"
  - "Trattalo come un collega: dagli contesto, esempi, vincoli"
implications:
  - "Spendi token su contesto, non economizzarli"
  - "Dai esempi quando un umano ne avrebbe bisogno"
  - "Aspettati ragionamento, non solo lookup"
alternatives:
  - "Modello come motore di ricerca (esplicitamente rifiutato dal sorgente)"
  - "Modello come oracolo (non considerato)"
  - "Modello come stocastico parrot (visione cinica, non adottata)"
applies_to: ["a-c001-002", "a-c003-005", "a-c007-001"]
```

Questa cosa, messa nella sezione "How to think" di un system prompt, dà al modello downstream un'enorme **leva**: capisce *perché* il prompt è scritto in un certo modo, può generalizzare ai casi nuovi.

## Anti-pattern

- **Mental model = riassunto**: spacciare un sommario tematico per "modello mentale". No: un modello mentale è una **lente**, non un riassunto.
- **Modello mentale inventato**: attribuire all'autore un frame che non emerge dal sorgente. → sempre `source_evidence` non vuoto.
- **Trascurare anti-frame**: ignorare i "non è X" → si perdono i confini.

## Riferimenti

- Lakoff & Johnson — *Metaphors We Live By*
- Charlie Munger — *Mental models* (Poor Charlie's Almanack)
- Cognitive frames (sociologia, Goffman)
