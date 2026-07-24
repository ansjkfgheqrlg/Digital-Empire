# Process: `custom` — Custom Injection (escape hatch)

> Builder: `custom-builder-agent` (B8)
> Stage: 5
> Tempo medio stimato: variabile (1-4 turni utente)

---

## 1. Identità

Il target `custom` è l'**escape hatch**: l'utente sa cosa gli serve, ma non è uno dei 7 target canonici. Tipici casi d'uso:

- "Voglio iniettare il valore di questo contenuto come **system prompt** in un mio workflow esistente."
- "Voglio un **config block** YAML per il mio agente in CrewAI / LangGraph / n8n."
- "Voglio un **knowledge pack** in formato per RAG (chunks + metadata)."
- "Voglio un **prompt template** parametrizzato per un'API specifica."
- "Voglio un **playbook PDF-ready** in markdown con un layout particolare."
- "Voglio un **brief** per un nuovo collaboratore umano."
- "Voglio un **deck outline** per una presentazione."

Differenza chiave vs gli altri target: il `custom` builder **non ha forma canonica predefinita**. Costruisce la forma su misura, ma applica comunque gli stessi pattern P1-P9 e gli stessi anti-pattern (no riassunto, expansion over compression).

## 2. Forma canonica dell'output

Non c'è una forma canonica fissa. Tuttavia, **ogni run `custom` produce sempre** questi tre file fissi:

```
output/
└── <custom-slug>/
    ├── artifact/                  # qui dentro va l'artefatto richiesto (forma libera)
    │   └── (file specifici alla richiesta)
    ├── spec.md                    # cosa è stato chiesto, perché ha quella forma, vincoli applicati
    ├── coverage_map.md            # mappa atomo→dove-finisce-nell-artefatto
    └── README.md                  # come usare l'artefatto, dove iniettarlo
```

`spec.md` è cruciale: documenta la **decisione di forma**, così l'utente sa esattamente cosa ha ottenuto e perché.

## 3. Input atteso

```
inputs/
├── kg.json
├── atoms/
├── source_meta.json
└── user_answers.json
    └── (più ricco del solito: include context_description, desired_form, constraints)
```

## 4. PLAN (cosa fa il builder)

Il PLAN è **dinamico**: dipende quasi interamente da cosa dirà l'utente in ASK.

Step iniziale:
1. Legge il KG per capire il **contenuto disponibile**.
2. Prepara una **proposta di intent** (cosa l'utente potrebbe voler fare con questo contenuto, oltre ai 7 target canonici).
3. Restituisce PLAN al Conductor che lo presenta come "ipotesi", non come PLAN definitivo.

Il PLAN diventa definitivo solo dopo la ASK phase, dove emerge la **forma target**.

## 5. ASK (domande generate da D1, più aperte del solito)

D1 in modalità `custom` adotta un approccio **funnel**: parte largo, restringe.

**Funnel apertura — "Cosa devo produrre?"**

1. "Descrivimi a parole tue cosa vuoi ottenere. Non serve un nome tecnico — descrivimelo come lo spiegheresti a un collega."
2. "Dove andrà a finire l'artefatto? (un file, un campo di un'app, una pagina web, un prompt, un tool config, un brief per persone, ...)"
3. "Chi/cosa lo userà? (un altro AI, un developer, un utente non-tech, un esecutore umano, un parser strutturato)"

**Funnel forma — "Che forma deve avere?"**

4. "Formato del file (markdown, YAML, JSON, plain text, codice, altro)?"
5. "Vincoli di lunghezza (max parole/righe/token)?"
6. "Vincoli di struttura (es. deve avere certe sezioni, certi campi, certi placeholder)?"
7. "Ci sono variabili/placeholder da preservare (es. `{user_name}`, `${input}`)?"
8. "C'è un esempio di qualcosa di simile che già esiste e a cui devo conformarmi? (incollalo o dammi il path)"
9. "Lingua?"

**Funnel iniezione — "Come si integra?"**

10. "Dove esattamente va iniettato l'artefatto? (es. 'system prompt del mio workflow X in n8n nodo Y', 'campo description del mio agente CrewAI', 'config.yaml chiave Z')"
11. "Ci sono regole di formattazione del contesto di destinazione che devo rispettare? (es. escaping di certi caratteri, no triple backtick, max 4000 char)"
12. "L'artefatto sostituisce qualcosa di esistente o si aggiunge? Se sostituisce: passami la versione corrente, così mantengo coerenza."

**Funnel chiusura — "Verifica"**

13. "Riassumendo (per disambiguazione, non per compressione): produrre `<forma>` in `<formato>` di `<lunghezza>` per `<scopo>` da iniettare in `<destinazione>`. Confermi?"

> ⚠️ Nota: questa è l'unica situazione in cui il termine "riassumendo" è ammesso, perché è meta-comunicazione di disambiguazione, non l'output. Comunque il builder usa "ricapitolando" per evitare l'associazione.

## 6. BUILD (ordine di scrittura)

1. **`spec.md`**: prima cosa. Documenta: cosa l'utente ha chiesto, quale forma è stata scelta, quali vincoli sono attivi, quali atomi del KG sono in scope. Senza `spec.md` esplicito, il rischio di drift è alto.
2. **`artifact/`**: contenuto vero. La struttura interna dipende dal caso:
   - **System prompt injection**: `artifact/system_prompt.md` (pronto per copy-paste o template)
   - **Config block**: `artifact/config.<ext>` (yaml/json) con commenti se applicabile
   - **Knowledge pack RAG**: `artifact/chunks.jsonl` + `artifact/metadata.json` + `artifact/embeddings_plan.md`
   - **Prompt template**: `artifact/template.md` con segnaposto chiari
   - **Brief umano**: `artifact/brief.md` strutturato per lettore umano
   - **Deck outline**: `artifact/outline.md` con slide-by-slide
   - **Altro**: forma negoziata con l'utente
3. **`coverage_map.md`**: tabella `atom_id → dove finisce nell'artifact`. Per ogni atomo: o c'è una riga con location, o c'è una riga con "out-of-scope" e razionale.
4. **Self-critique** (vedi §7).
5. **`README.md`**: istruzioni di iniezione passo-passo, con esempi se la destinazione è nota.

## 7. Self-critique (interna)

Il custom builder ha self-critique più stringente perché manca uno schema canonico:

- **Spec aderente**: l'artifact rispetta ogni vincolo dichiarato in `spec.md`?
- **Coverage**: ogni atomo del KG è in `coverage_map.md`?
- **No drift**: l'artifact non include atomi out-of-scope?
- **No riassunto**: nessuna parola-bandiera ("in sintesi", "riassumendo")?
- **Forma compilabile** (se config/code): parsing pulito?
- **Variabili preservate**: placeholder/variabili dichiarati sono presenti e formattati correttamente?
- **Lunghezza**: rispetta i vincoli dichiarati?
- **Iniettabilità**: se la destinazione è nota, l'artifact ci entra senza modifiche?
- **`spec.md` parlante**: un altro essere umano (o LLM) può capire cosa è stato fatto leggendo solo `spec.md` + `artifact/`?

## 8. Critique esterna (C1 + C3)

- **C1 `coverage-verifier`**: usa `coverage_map.md` come ground truth dichiarato. Verifica che la mappatura sia onesta (gli atomi marcati come "presenti in artifact" sono davvero presenti).
- **C3 `target-schema-validator`**: ha logica speciale per `custom` → non valida contro uno schema fisso, ma valida che:
  - i 3 file fissi (`spec.md`, `coverage_map.md`, `README.md`) esistano
  - `spec.md` abbia certe sezioni minime
  - se l'utente ha dichiarato un format machine-readable (yaml/json), che sia parsabile
  - se l'utente ha dichiarato vincoli di lunghezza, che siano rispettati

## 9. Iterate

Tipici fix:
- aggiustare `artifact/` per matchare meglio l'esempio fornito dall'utente
- snellire o ampliare per vincoli di lunghezza
- normalizzare placeholder/variabili
- arricchire `spec.md` se è troppo magro

## 10. Failure modes del processo

| Failure | Sintomo | Mitigazione |
|---|---|---|
| ASK sotto-specificato | L'utente non ha risposto a domande chiave → drift | Bloccare BUILD se ASK non è completa, riproporre |
| Spec implicita | `spec.md` mancante o vago | Forzare `spec.md` PRIMA di `artifact/` |
| Artifact "fa il riassunto" | Vince la tentazione di compressione | Self-critique rigorosa + coverage map onesta |
| Iniettabilità non testata | L'utente prova a iniettare e non entra | Se la destinazione è nota, simulare iniezione (es. parsare il config nel parser target) |
| Atomi orfani | Atomi del KG né dentro né dichiarati out-of-scope | C1 fail, richiedere coverage_map completa |

## 11. Esempi realistici

### Esempio A — System prompt injection

Input: 3 articoli su "customer success best practices" → KG 48 atomi.
Richiesta utente: "Voglio iniettare questo come system prompt del mio agente CS in n8n. Max 3000 caratteri, deve mantenere `{customer_tier}` come variabile."

Output:
- `artifact/system_prompt.md`: 2870 caratteri, variabile preservata, struttura instruction-heavy
- `spec.md`: documenta i vincoli e le scelte (es. "trade-off: ho dovuto comprimere il cluster X in 2 righe per rispettare il limite — vedi `coverage_map.md` per dettagli")
- `coverage_map.md`: 48 atomi → 42 "in artifact", 6 "out-of-scope per vincolo di lunghezza" (con razionale per ognuno)
- `README.md`: istruzioni per incollare in n8n con screenshot-style

### Esempio B — RAG knowledge pack

Input: 6 documenti tecnici → KG 180 atomi.
Richiesta: "Voglio chunks pronti per essere indicizzati in Pinecone, con metadata per filtering."

Output:
- `artifact/chunks.jsonl`: 180+ chunks (alcuni atomi splittati in più chunk per dimensione)
- `artifact/metadata.json`: schema dei metadata applicato
- `artifact/embeddings_plan.md`: raccomandazioni di chunking + modello embedding suggerito
- `spec.md`, `coverage_map.md`, `README.md`

## 12. Handoff al Conductor

- path `output/<custom-slug>/`
- `build-report.json`
- `next-suggestions.md` (es. "questa forma è inusuale, vuoi che generi una nota in `wiki` per ricordarti come l'hai fatto?", "vuoi che pacchetti questa configurazione `custom` come template riusabile?")

---

## 13. 📎 Appendice — Shape (embedded)

### `coverage_map.md` — formato canonico (tabella)

Il custom builder DEVE produrre `coverage_map.md` con questa struttura tabellare:

```markdown
# Coverage Map

| atom_id | atom_title | status | location_in_artifact | rationale |
|---------|-----------|--------|----------------------|-----------|
| a-001 | Definizione del lead | included | artifact/system_prompt.md §"What is a lead" | core concept |
| a-002 | Distinzione MQL/SQL | included | artifact/system_prompt.md §"Lead grades" | needed for tier policy |
| a-003 | Storia del cold calling | out_of_scope | — | not relevant to SP for n8n agent |
| ... | | | | |
```

Equivalente Python (machine-readable):

```python
coverage_map_schema = {
    "atoms": [
        {
            "atom_id": str,
            "atom_title": str,
            "status": str,                  # "included" | "out_of_scope"
            "location_in_artifact": str | None,
            "rationale": str
        }
    ],
    "stats": {
        "total": int,
        "included": int,
        "out_of_scope": int,
        "inclusion_rate": float
    }
}
```

### Spec.md — sezioni minime obbligatorie

```python
spec_required_sections = [
    "Original Request",          # cosa l'utente ha chiesto (verbatim, da user_answers.json)
    "Chosen Form",               # forma decisa per l'artifact
    "Constraints Applied",       # vincoli (lunghezza, formato, variabili da preservare)
    "Injection Target",          # dove va iniettato
    "Trade-offs",                # cosa è stato sacrificato e perché
    "How to Verify"              # come l'utente può verificare che funzioni
]
```
