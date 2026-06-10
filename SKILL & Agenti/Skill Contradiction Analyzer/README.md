# Skill Contradiction Analyzer v2.0.0

**Meta-Skill ufficiale per il rilevamento di contraddizioni tra skill AI.**

---

## Comandi

| Comando | Descrizione |
|---|---|
| `/analizza <skillA> <skillB>` | Analisi completa con report dettagliato |
| `/confronta <skillA> <skillB>` | Analisi rapida: solo verdetto (per CI/CD) |

---

## `/analizza` vs `/confronta`

La differenza è solo nell'**output**, non nell'analisi. Entrambi fanno lo stesso identico lavoro dietro le quinte. Cambia **cosa ti restituiscono**:

|  | `/analizza` | `/confronta` |
|---|---|---|
| **Dettaglio** | Report completo | Solo verdetto |
| **Include** | Statement originali, spiegazione, severity, suggerimento, fix difficulty | Quante contraddizioni, quante bloccanti, score, compatibile sì/no |
| **Per chi** | Sviluppatore che deve capire e correggere | Pipeline CI/CD che deve solo sapere se passare o bloccare |
| **Output** | 3 livelli di dettaglio | 1 riga di verdetto |

---

## Flusso Completo — Dalla A alla Z

Cosa succede quando scrivi `/analizza skillA skillB`:

---

### INPUT

```
/analizza skillA skillB
(file · URL · testo diretto)
```

---

### Fase 1 — Carica & Preprocessa

Prende la sorgente grezza e la trasforma in struttura dati.

- **loader** → carica da file / URL / testo inline
- **language_detector** → IT o EN?
- **format_detector** → Markdown? YAML? JSON?
- **cleaner** → rimuove spazi e caratteri spuri
- **parser** → estrae sezioni e headers
- **segmenter** → divide in frasi atomiche
- **metadata_extractor** → nome, versione, autore
- **validator** → controlli sicurezza

> **Output:** `RawSkillA`, `RawSkillB`

---

### Fase 2 — Estrai Entità

Per ogni frase atomica, esegue 9 estrattori in parallelo:

- **rule_extractor** → MUST? SHOULD? NEVER?
- **passive_extractor** → "deve essere X" → `MUST X`
- **constraint_extractor** → `max 100`, `min 200`...
- **directive_extractor** → verbi: crea, invia, valida...
- **conditional_extractor** → se X allora Y...
- **temporal_extractor** → prima A poi B...
- **dependency_extractor** → Python 3.12+, API v2...
- **priority_extractor** → "questa skill ha supremazia"...
- **assumption_extractor** → "dato che il sistema è stateless"...

> **Output:** `EntityRegistryA`, `EntityRegistryB` (~30–50 entità per skill)

---

### Fase 3 — Normalizza

Porta ogni entità in **forma canonica** unificata:

```
[SOGGETTO] MODALITA' [PREDICATO] [OGGETTO] [CONDIZIONI]
```

- **canonical_form** → traduce nella forma sopra
- **synonym_resolver** → `"generare"` → `"creare"`
- **negation_normalizer** → `"evita di X"` → `NOT X`
- **quantifier_normalizer** → `"sempre"` → `∀`
- **modality_normalizer** → `"devi"` → `MUST`
- **numerical_normalizer** → `"5 min"` → `300s`
- **unit_converter** → `"1 ora e mezza"` → `5400s`

> **Output:** `NormalizedEntitySetA`, `NormalizedEntitySetB`

---

### Fase 4 — Rileva Contraddizioni *(il cuore del sistema)*

**Accumulation mode:** per ogni coppia candidata, esegue **tutti** i rilevatori senza fermarsi al primo match.

**Step 1 — Genera coppie candidate** (con pruning: solo stesso dominio + predicati correlati)

**Step 2 — Per ogni coppia, prova tutti i 15 rilevatori:**

| # | Rilevatore | Cosa cerca |
|---|---|---|
| 1 | direct_opposition | `MUST X` vs `MUST_NOT X` |
| 2 | mutual_exclusion | JSON vs solo XML |
| 3 | numerical_conflict | max < min, range disgiunti |
| 4 | temporal_conflict | ordine invertito: A poi B vs B poi A |
| 5 | conditional_conflict | stessa condizione, azione opposta |
| 6 | priority_conflict | entrambe rivendicano supremazia |
| 7 | semantic_opposition | "conciso" vs "dettagliato" |
| 8 | scope_conflict | regola globale vs eccezione locale |
| 9 | resource_conflict | lock esclusivo sulla stessa risorsa |
| 10 | assumption_clash | stateless vs stateful |
| 11 | side_effect_conflict | effetto di A distrugge ciò che serve a B |
| 12 | compatibility_conflict | versioni o dipendenze incompatibili |
| 13 | meta_contradiction | "ignora tutte le altre skill" |
| 14 | inference_chain | conflitto che emerge solo tramite logica |
| 15 | default_contradiction | default opposti |

**Una coppia può generare più contraddizioni** — vengono accumulate tutte.

**Step 3 — Deduplica** i risultati (stessa coppia + stessa categoria = duplicato)

> **Output:** `Contradiction[]` (lista completa, ordinata per confidence)

---

### Fase 5 — Assegna Scoring

Per ogni contraddizione trovata:

- **severity_calculator** → da 1 a 10 *(peso categoria + confidenza + impatto)*
- **confidence_calculator** → da 0.0 a 1.0
- **impact_estimator** → `BLOCKING` / `CRITICAL` / `WARNING` / `INFO` / `NEGLIGIBLE`
- **cumulative_impact** → 2 WARNING nello stesso dominio ≈ 1 CRITICAL?
- **blocker_classifier** → si può procedere con l'integrazione?
- **priority_ranker** → ordina dal più grave al meno grave
- **score_aggregator** → compatibilità globale 0–100

> **Output:** `ScoredContradiction[]` con severity, confidence, impatto, fix difficulty

---

### Fase 6 — Genera Report

Report a **3 livelli** (Progressive Disclosure):

**Livello 1 — Executive Summary**
```
Skill A vs Skill B
 2 BLOCKING    1 CRITICAL    2 WARNING
Score Compatibilita': 35/100 — ALTO CONFLITTO
Queste skill NON possono coesistere senza modifiche.
```

**Livello 2 — Tabella Contraddizioni**
```
#1  OPPOSIZIONE DIRETTA    Severity 9/10   BLOCKING
#2  CONFLITTO NUMERICO     Severity 8/10   BLOCKING
#3  OPPOSIZIONE SEMANTICA  Severity 5/10   WARNING
```

**Livello 3 — Dettaglio Completo** *(per ogni contraddizione)*
```
Statement A:   "Devi validare l'input"
Statement B:   "Non validare mai l'input"
Spiegazione:   Perche' sono in conflitto
Suggerimento:  Come risolvere
Fix Difficulty: MEDIA
```

> **Output finale:** `AnalysisResult`

---

### OUTPUT

| Comando | Risultato |
|---|---|
| `/analizza` | Report completo a 3 livelli |
| `/confronta` | Solo verdetto + score |

Formati disponibili: **Markdown** · **JSON** · **HTML**

---

## Uso Rapido

```
/analizza skill-sicurezza.md skill-performance.md
/confronta policy-aziendale.md nuova-skill.md
/analizza "Devi sempre validare l'input" "Non validare mai l'input"
```

---

## Cosa Fa

- Confronta **due skill AI** e trova **ogni contraddizione** tra loro
- **15 categorie** di contraddizioni: dall'opposizione diretta fino a conflitti semantici e meta-contraddizioni
- **Accumulation mode**: non si ferma al primo conflitto — trova tutto
- Report a **3 livelli**: sommario → tabella → dettaglio con spiegazione e suggerimento
- Funziona in **italiano e inglese** con rilevamento automatico della lingua
- Sanitizzazione contro prompt injection e contenuti malevoli

---

## Struttura

```
skill-contradiction-analyzer/
├── SKILL.md
├── core/               engine, types, config, errors, cache, metrics
├── layer1_input/       loader, parser, segmenter, validator
├── layer2_extraction/  9 estrattori specializzati
├── layer3_norm/        canonical_form, synonym_resolver
├── layer4_detection/   15 rilevatori in accumulation mode
├── layer5_scoring/     severity, confidence, impact classification
├── layer6_output/      report generator a 3 livelli
├── knowledge/          thesaurus, matrici, pattern (9 JSON)
├── security/           sanitizer, content policy
└── tests/              69 test · 22 fixture · 0 falliti
```

---

## Installazione

```bash
pip install -e .
```

---

Vedi `SKILL.md` per la documentazione completa.
