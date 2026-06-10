# P12 — Traceability Source-to-Output

> **Definizione canonica**: Ogni atomo informativo del sorgente è tracciabile fino all'output finale attraverso una catena esplicita: **Source → Atoms → KG → MKD → Target output**. Misurabile via coverage check + formula validator. **Niente perdite silenziose**: se un atomo non finisce nell'output, deve essere dichiarato `out_of_scope` con razionale.

## Perché funziona

### 1. Le perdite silenziose sono il peggior tipo di bug
Quando produci una skill da un sorgente di 30k parole e silenziosamente perdi 20% del contenuto, l'utente:
- Non lo sa
- Non può controllare
- Quando si accorge (settimane dopo, magari mai), non sa cosa ha perso

Tracciabilità formale rende impossibile la perdita silenziosa. Se manca qualcosa, è **dichiarato** in `gaps.md` o `coverage_map.md`.

### 2. La tracciabilità è la base del trust
Quando l'utente vede che ogni atomo del sorgente è mappato a una sezione dell'output (o esplicitamente dichiarato out-of-scope con razionale), si fida del sistema. Senza tracciabilità, deve fidarsi a fede.

In contesti professionali (consulting, legal, technical writing) la tracciabilità non è opzionale.

### 3. Permette validazione automatica
Coverage check è uno script. Confronta atomi nel KG con presenze nell'output. Numero deterministico, riproducibile. Senza P12, "questa skill copre il sorgente?" è una domanda di giudizio. Con P12, è una metrica.

## Come applicarlo (operativo)

### La catena di tracciabilità (5 stage)

```
SORGENTE (cleaned.md)
     │  ranges in cleaned.md → source_offsets
     ▼
ATOMS (atoms-*.json)
     │  per ogni atomo: source_excerpts + source_offsets
     ▼
KG (kg.json)
     │  atomi consolidati + cluster + edges
     ▼
MKD (master.md)
     │  ogni sezione H3 ha {atom_id} anchor
     ▼
TARGET OUTPUT (skill/agent/wiki/...)
     │  ogni componente cita atom_ids di provenienza
     ▼
COVERAGE CHECK (scripts/coverage_check.py)
     │  Verifica: ogni atom_id appare in qualche file dell'output
     ▼
PASS (90%+ coverage) o FAIL (con missing_ids esplicitati)
```

### Le 4 metriche di P12

#### 1. Atom coverage
% atomi del KG presenti nell'output finale.

Calcolato da `scripts/coverage_check.py`: per ogni atomo, cerca lexical + semantic match nei file output. Soglie:
- MKD: 100% (mandatory)
- doc/wiki: 95%
- skill/agent/team/workflow: 90%
- orchestration: 85%
- custom: 85% (con coverage_map.md esplicito)

#### 2. Source quote ratio
% paragrafi dell'output che includono almeno una citazione verbatim dal sorgente.

Bassa = output troppo paraphrased (rischio drift semantico). Alta (>80%) = output ancorato al sorgente.

#### 3. Formula completeness
Per ogni formula identificata nel sorgente (es. CPB, APSOC, AIDA), tutti i componenti sono applicati nell'output?

Validato da `O5 formula-validator-agent`. Esempio: se sorgente cita "CPB" e output ha solo Claim + Proof (manca Benefit) → FAIL.

#### 4. Out-of-scope declaration
Per ogni atomo NON nell'output, esiste razionale esplicito?

Per `custom` target: obbligatorio `coverage_map.md` con tabella "atom_id | status (included|out_of_scope) | rationale".

### Implementazione: i campi di tracciabilità

```python
# Atom (in atoms-*.json e kg.json)
{
  "id": "a-007",
  "title": "Few-shot prompting",
  "source_excerpts": ["Few-shot vuol dire dare 2-5 esempi..."],
  "source_offsets": [[460, 690]],  # range in cleaned.md
  "source_file_id": "src-001",     # in multi-source
  "examples_from_source": [...],
  "generated_examples": ["➕ Esempio: ..."],  # marcati ➕
}

# MKD section (in master.md)
### Few-shot prompting {#a-007}
**Definizione**: ...
**Esempio (sorgente)**:
> "Few-shot vuol dire dare 2-5 esempi..."  # citazione verbatim
**➕ Esempio aggiuntivo**: ...  # etichettato

# Output skill (es. reference)
## Few-shot
> Definizione canonica: dal MKD §Few-shot prompting (atom a-007).
[contenuto adattato]
```

### Multi-source extension

Quando l'input è una cartella o lista di file:

```python
# sources.json (output di Stage 1)
{
  "sources": [
    {"id": "src-001", "path": "video1.md", "range_in_cleaned": [0, 8543]},
    {"id": "src-002", "path": "video2.md", "range_in_cleaned": [8543, 15672]},
    ...
  ]
}

# Cleaned.md ha marker invisibili
<!-- FORGE_SOURCE_BOUNDARY id="src-001" file="video1.md" -->
... contenuto pulito ...
<!-- FORGE_SOURCE_BOUNDARY id="src-002" file="video2.md" -->
... contenuto pulito ...
```

Ogni atomo, MKD section, output component sa da quale source proviene. Output può citare: "Come spiegato in [video 1]: ..."

### Failure modes di tracciabilità

| Failure | Detection | Fix |
|---|---|---|
| Atomo nell'output ma senza source_offset | Coverage check find missing | A2 deve sempre annotare offset |
| Atomo perso silenziosamente | Coverage check rate <soglia | Builder ITERATE su gap specifici |
| Esempio fake-attribuito al sorgente | Manual review (raro) | Regola hardcoded: ogni esempio etichettato `(sorgente)` o `➕` |
| Multi-source mescolato senza citazione | O5 formula validator + manual | Force `*(da <file>)*` se sources>1 |

## Esempi

### Esempio 1 — content-forge Phase 7 (test reale)

Sorgente: Manuale APSOC, 3041 parole.
Estratti 18 atomi nel KG.
MKD: 5743 parole con 18 sezioni H3 (1:1 con atomi), ogni sezione con `{#a-NNN}` anchor.
Coverage check: 100% (18/18 atomi nel MKD).
Output skill (`objection-handler`): coverage 94.4% (16 covered + 2 partial / 18) = PASS.

Tracciabilità completa: dato un atom_id, posso trovare:
- La sua sezione nel MKD (`#a-NNN`)
- Le sue citazioni nei reference della skill
- L'esempio originale dal sorgente

Nessuna perdita silenziosa.

### Esempio 2 — coverage_map.md per target=custom

Esempio Test #1 ipotetico:
```markdown
# Coverage Map

| atom_id | atom_title | status | location | rationale |
|---|---|---|---|---|
| a-001 | Prompt come interfaccia | included | system_prompt.md §"How to think" | core mental model |
| a-005 | Quando CoT NON aiuta | included | system_prompt.md §"Avoid" | critica per uso |
| a-008 | Delimiters | included | examples sezione | shown via examples |
| a-006 | Self-consistency | out_of_scope | — | costoso da spiegare in 3000 char; raro per use case freelancer |
| a-011 | Prompt come codice | out_of_scope | — | off-topic per system prompt runtime |
```

Tracciabilità onesta: include 3/5, out_of_scope 2/5 con razionale. Utente sa esattamente cosa ha ottenuto.

### Esempio 3 — ➕ Pattern in altri domini

**Requirements traceability matrix** (engineering): ogni requirement ha ID, ogni componente system ha back-reference al requirement. Pattern identico per software/hardware.

**Bibliography in academic writing**: ogni claim ha citation. Tracciabilità a fonte primaria.

**Audit trail in finance/medical records**: ogni decisione/azione ha provenance documentata. Compliance requirement.

**Knowledge Graph databases** (Neo4j, RDF): tracciabilità di entità a fonte è feature core.

## Anti-pattern correlato

**AP09 — Premature Optimization** (in P12 context): comprimere/riassumere atomi simili pensando di "essere efficienti", perdendo tracciabilità. Sintomo: 18 atomi diventano 12 nel KG senza dichiarare merging. **Fix**: A3 knowledge-graph-agent deve dichiarare ogni merge in `duplicate_groups_merged` stat + log.

**Anti-pattern duale**: **Trace overload** — citazioni verbatim per ogni riga, output diventa illeggibile. **Fix**: citazioni solo per atomi non-banali, sezioni narrative possono esserci senza quote verbatim continui.

## Decision tree: "il mio output è tracciabile?"

```
Ogni atomo del KG ha source_offsets?
├─ NO → A2 non sta annotando, fix builder
└─ SÌ → continua
   ├─ MKD ha {#anchor} per ogni sezione = atom_id?
   │  ├─ NO → A5 deve aggiungere anchor
   │  └─ SÌ → continua
   ├─ Output finale ha citazioni verbatim ≥1 per atomo non-banale?
   │  ├─ NO → builder deve aggiungere
   │  └─ SÌ → continua
   ├─ Coverage check ≥ soglia per target?
   │  ├─ NO → ITERATE, fix gap
   │  └─ SÌ → continua
   ├─ Per atomi mancanti: declared out_of_scope con razionale?
   │  ├─ NO → silent loss, P12 violato
   │  └─ SÌ → tracciabilità completa ✅
   │
   └─ Multi-source: ogni esempio cita la fonte?
      ├─ NO (se sources>1) → force citation
      └─ SÌ → fully traceable ✅
```

## Quando NON applicare full P12

- **Output puramente creativo/generativo**: tracciabilità non è value (esempio: skill che genera nomi di brand)
- **Trasformazioni 1:1 dirette**: input = output, tracciabilità banale
- **Prototipi early-stage**: prima fai funzionare, poi aggiungi tracciabilità
- **Privacy constraints**: in alcuni contesti (sensitive data) la tracciabilità a fonte può essere problema. Vincoli specifici.

## Riferimenti esterni

- **Requirements Traceability Matrix** (engineering best practice).
- **Provenance in databases / knowledge graphs** (W3C PROV).
- **Audit trail in compliance** (HIPAA, SOX, GDPR).
- **Anthropic Constitutional AI** — Concetto analogo di "principle traceability" nelle risposte.
- **Andy Matuschak**, *Evergreen Notes* — backlinks come tracciabilità lateral.

## Connessioni con altri principi

- Necessario per: P01 (Iterative Planning) — senza traceability tra versioni di output, non sai cosa è cambiato
- Combina con: P03 (No-Summary, Always Expansion) — espandere senza perdere = traceability
- Combina con: P06 (Shapes) — shape canonica include source_offsets, source_excerpts
- Validato da: scripts/coverage_check.py + agente C1 + agente O5
