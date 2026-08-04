# BLUEPRINT WORKFLOW MULTI-AGENTE - LIBRI PERFORMANTI E RIPRODUCIBILI

**Versione:** 1.0 - Architettura Finale
**Data:** 2026-08-03
**Vincolo Fondamentale:** Solo elementi in ALLOWED_ELEMENTS

---

## 1. OBIETTIVO E LOGICA GENERALE

### 1.1 Obiettivo di Business Primario
Guadagnare attraverso la **quantità di libri performanti**. Non massimizzare un singolo bestseller, ma massimizzare il throughput di opportunità sostenibili.

**Equazione di valore del workflow:**
```
Valore = (Numero di libri) x (Performance su Amazon) x (Probabilità di riproducibilità)
         ---------------------------------------------------------------
              Costo di produzione (tempo + complessità)
```

### 1.2 Filtri Decisionali Invarianti
Ogni decisione in ogni fase deve superare 5 gate obbligatori:

1.  **Performante?** Esistono segnali su Amazon e sui siti che analizzano le review di Amazon che indicano domanda/traccia?
2.  **Riproducibile?** Possiamo replicare struttura e valore senza elementi inaccessibili?
3.  **Sostenibile?** Il carico di produzione è compatibile con logica di quantità?
4.  **Non Assurdo?** Assenza di elementi assurdi, irrealistici, incoerenti con produzione rapida.
5.  **Non Troppo Lento?** Il tempo stimato di produzione è sotto la soglia di sostenibilità.

Se un gate fallisce → `no-go` motivato + log in memoria.

### 1.3 Logica di Flusso
Pipeline sequenziale a 5 fasi con checkpoint obbligatori, memoria always-on, self-healing trasversale, auto-improvement a ciclo chiuso. Playwright è l'unico strumento di automazione consentito ed è usato esclusivamente per:
- navigazione e raccolta dati da Amazon via keyword search
- navigazione e raccolta da siti che analizzano/calcolano Amazon reviews
- salvataggio di risultati, fonti, URL, note, materiale utile
- supporto attività visual team dove richiesto

**Principio di non-invenzione:** Nessuna metrica, API, fonte dati, canale esterno viene introdotto se non direttamente derivabile da `keyword search on Amazon` o `sites that analyze or calculate Amazon reviews`.

---

## 2. MAPPA DEL WORKFLOW

### 2.1 Diagramma Logico

```
[ORCHESTRATORE + MEMORY ECOSYSTEM (always_active)]
                |
                | init hierarchies, checkpoint_0
                v
FASE 1: RESEARCH TEAM --Playwright--> [books_found + review_sites_found + raw_data]
                | checkpoint CP1 + memory_write
                | structured_output
                v
FASE 2: QUALIFICATION TEAM --BookNicheDecisionSkill-->
        [qualification_plan + decision GO/NO-GO + risk_flags]
                | checkpoint CP2 + memory_write (decisions, plans, risk)
                | if GO
                v
FASE 3: PLANNING TEAM (Secondo Livello)
        [second_level_plan {video_structure REQUIRED + chapters + details + production_start_signal}]
                | checkpoint CP3 + memory_write
                | if production_start_signal = TRUE
                v
FASE 4: PRODUCTION TEAM --read memory--> [complete_book + production_log]
                | checkpoint CP4 + memory_write
                v
FASE 5: VISUAL TEAM --Playwright (support)--> [graphics + graphic_prompts + cover]
                | checkpoint CP5 (FINALE) + memory_write
                v
[OUTPUT FINALE PRONTO PER AMAZON]

LOOP TRASVERSALI PARALLELI:
- SelfHealingEngine monitora tutte le fasi su 8 trigger
- AutoImprovementEngine raccoglie 6 feedback signals e migliora 5 target
- MemoryWriter/Reader/Validator/CheckpointManager sempre attivi
```

### 2.2 Dipendenze Esplicite
- F2 dipende al 100% da F1 `structured_output`
- F3 dipende da F2 solo se `decision=GO`
- F4 dipende da F3 solo se `production_start_signal=TRUE` e `plan_validity=TRUE`
- F5 dipende da F4 + F3 (legge piani e decisioni da memoria)
- Tutte le fasi dipendono da MemoryEcosystem per read/write

### 2.3 Modularità
Ogni Team è un modulo isolato con input/output validati. Nessun team accede direttamente ai tool interni di un altro team. Comunicazione solo tramite output strutturato + memoria.

---

## 3. FASI OPERATIVE DETTAGLIATE

### FASE 1 — RICERCA LIBRI

- **Nome fase:** F1_RESEARCH
- **Scopo:** Trovare libri e opportunità rilevanti tramite keyword su Amazon e tramite siti che analizzano le review di Amazon. Raccogliere, organizzare e salvare tutto tramite Playwright.
- **Agenti coinvolti:** Research Team (3 sub-agenti)
  - `KeywordSearchAgent`: esegue keyword search on Amazon via Playwright
  - `ReviewSiteDiscoveryAgent`: trova sites that analyze or calculate Amazon reviews via Playwright
  - `CollectorAgent`: raccoglie, organizza, salva risultati, fonti, URL, note via Playwright
  - Skill attiva: `BookNicheDecisionSkill` per pre-ranking iniziale

- **Input:**
  - Lista seed di keyword iniziali (da memoria `important_notes` se presenti, altrimenti da config orchestrator)
  - Checkpoints precedenti di ricerca (per evitare duplicati)
  - Hierarchies da memoria

- **Attività dettagliate:**
  1.  `KeywordSearchAgent`: Naviga Amazon con Playwright, esegue keyword search, raccoglie metadata libro (titolo, URL, note visibili senza inventare metriche). Salva raw HTML/screenshot se utile via Playwright.
  2.  `ReviewSiteDiscoveryAgent`: Naviga su siti che analizzano o calcolano Amazon reviews (trovati tramite ricerca), raccoglie dati di analisi disponibili su quei siti. Salva URL, fonte, note, raw_data via Playwright.
  3.  `CollectorAgent`: Normalizza tutto in `structured_output` pronto per qualifica. Organizza per opportunità. Ogni record ha: source_url, collection_timestamp, keyword_origine, note, raw_data_ref.
  4.  Validazione interna: verifica che `books_found` non sia vuoto, che ci siano URL, che raw_data sia salvato via Playwright.
  5.  `BookNicheDecisionSkill` pre-score: ranking preliminare opportunità basato su segnali disponibili (senza inventare metriche esterne).

- **Output (formato obbligatorio):**
```json
{
  "books_found": [{"title": "", "amazon_url": "", "keyword_match": "", "observed_signals": "", "notes": ""}],
  "review_sites_found": [{"site_url": "", "analysis_type": "", "data_collected": "", "notes": ""}],
  "raw_data": "riferimento a materiale salvato via Playwright (path/log)",
  "structured_output": "dataset normalizzato pronto per F2"
}
```

- **Checkpoint:** CP1_RESEARCH_END
  - Stato: lista libri + siti + raw_data refs
  - Salvato da: CheckpointManagerAgent
  - Letto da: SelfHealingEngine in caso di failure, QualificationTeam

- **Criteri di validazione:**
  - `books_found.length > 0` OR `review_sites_found.length > 0`
  - Ogni item ha `amazon_url` o `site_url` valido e salvato via Playwright
  - `raw_data` non vuoto
  - `structured_output` parsabile da F2

- **Criteri di passaggio a F2:**
  - Validazione superata + checkpoint CP1 creato + memory_write completato
  - Sufficiente per avanzare = TRUE

- **Principali rischi/fallimenti:**
  - empty result from research
  - Playwright failure (timeout, block)
  - memory write failure
  - incoherent output (URL non Amazon, dati non pertinenti)

- **Comportamento self-healing associato:**
  - empty result → retry con adjusted parameters (nuove keyword da memoria `important_notes`) → se fallisce 2 volte → skip_and_log + escalate
  - Playwright failure → retry → rollback a checkpoint precedente → log in important_notes
  - memory write failure → retry → escalate

---

### FASE 2 — QUALIFICA

- **Nome fase:** F2_QUALIFICATION
- **Scopo:** Ricevere output ricerca e produrre piano di qualifica dettagliato che determini se un libro è riproducibile, sostenibile e coerente con obiettivo business quantità+performance.
- **Agenti coinvolti:** Qualification Team (4 sub-agenti)
  - `ReproducibilityEvaluator`: valuta can this be reproduced efficiently?
  - `AbsurdityAndSpeedEvaluator`: valuta absurd elements + too slow?
  - `PlanValidityEvaluator`: valuta is the reproduction plan itself valid?
  - `DecisionSynthesizer`: produce decisione finale GO/NO-GO motivata
  - Skill attiva: `BookNicheDecisionSkill` (core), `SelfHealingSkill` (monitor)

- **Input:**
  - `structured_output` da F1
  - `books_found`, `review_sites_found`, `raw_data` (da memoria via MemoryReaderAgent)
  - `decisions` storiche, `risk_flags` storici, `important_notes` (per apprendere cosa è stato scartato prima)

- **Attività dettagliate:**
  1.  Lettura memoria: `decisions`, `plans`, `important_notes` precedenti.
  2.  Per ogni book opportunity: creazione `qualification_plan` con 5 criteri espliciti:
      - `reproducibility`: can this book be reproduced efficiently?
      - `absurdity_check`: are there absurd or unrealistic elements?
      - `production_speed`: is this book too slow to produce?
      - `plan_validity`: is the reproduction plan itself valid?
      - `business_alignment`: does this align with quantity + performance goal?
  3.  Ogni criterio = score descrittivo + evidenze + flag rischio. Nessuna metrica inventata: solo valutazione qualitativa basata su dati disponibili.
  4.  `BookNicheDecisionSkill` applicata: ranked list con motivazione.
  5.  Sintesi decisione GO/NO-GO con motivazione tracciabile.
  6.  Produzione risk_flags.

- **Output:**
```json
{
  "qualification_plan": {
    "book_id": "",
    "criteria_evaluation": {
      "reproducibility": {"verdict": "", "evidence": "", "risk": ""},
      "absurdity_check": {"verdict": "", "evidence": "", "risk": ""},
      "production_speed": {"verdict": "", "evidence": "", "risk": ""},
      "plan_validity": {"verdict": "", "evidence": ""},
      "business_alignment": {"verdict": "", "evidence": ""}
    },
    "overall_score_notes": ""
  },
  "decision": {"value": "GO | NO-GO", "motivation": "", "trace": ""},
  "risk_flags": ["flag1", "flag2"],
  "memory_write": ["decision", "qualification_plan", "risk_flags"]
}
```

- **Checkpoint:** CP2_QUALIFICATION_END per ogni libro processato + CP2_BATCH per lotto

- **Criteri di validazione:**
  - Tutti e 5 i criteri valutati esplicitamente
  - Decision non vuota e motivata
  - Plan validity valutata (self-check)
  - Memory write eseguito su decisions, plans

- **Criteri di passaggio a F3:**
  - `decision=GO` + `plan_validity=TRUE` + `absurdity_check=FALSE` (non absurdo) + `production_speed != too_slow`
  - Se NO-GO → ramo chiuso, checkpoint salvato, auto-improvement signal generato, non passa a F3 ma torna a F1 per prossima opportunità

- **Rischi/fallimenti:**
  - no-go decision without alternative path (tutti NO-GO)
  - qualification plan incoerente
  - memory write failure
  - missing output

- **Self-healing:**
  - no-go senza alternative → `requalify` con anomaly flag + `retry` con parametri diversi + log in memory + `skip_and_log` se batch intero fallito
  - incoherent output → `rollback` a CP1 + `retry`
  - failed validation → `escalate` + richiesta review manuale tracciata in important_notes

---

### FASE 3 — SECONDO LIVELLO DEL PIANO

- **Nome fase:** F3_PLANNING_SECOND_LEVEL
- **Scopo:** Creare piano operativo di secondo livello, più vicino alla produzione, che includa struttura del video, capitoli e ogni dettaglio necessario. Mark actual start of production flow.
- **Agenti coinvolti:** Planning Team (3 sub-agenti)
  - `StructureArchitect`: definisce video_structure (REQUIRED), chapters
  - `DetailExpander`: definisce every relevant detail
  - `ProductionGateKeeper`: definisce production_start_signal esplicito

- **Input:**
  - Qualification output GO con motivation
  - `qualification_plan`, `risk_flags`
  - Memoria: `decisions`, `plans`, `checkpoints`, `hierarchies`

- **Attività dettagliate:**
  1.  Read da memoria: decisioni, piani di qualifica, risk flags.
  2.  Creazione `second_level_plan`:
      - `video_structure`: campo OBBLIGATORIO, preservato esattamente come da requisiti originali, non reinterpretato. Gestione ambiguità → vedi Sez.10.
      - `chapters`: lista capitoli con descrizioni
      - `details`: ogni dettaglio rilevante per produzione sostenibile
      - `production_start_signal`: booleano esplicito + timestamp
  3.  Validazione che piano non introduca elementi assurdi / troppo lenti / non riproducibili.
  4.  Allineamento con obiettivo quantità+performance.
  5.  Scrittura in memoria + checkpoint.

- **Output:**
```json
{
  "second_level_plan": {
    "video_structure": "REQUIRED — as per original requirements — preserved verbatim + explicit control point",
    "chapters": [{"title": "", "description": "", "estimated_effort": "fast/sustainable vs slow"}],
    "details": {"production_constraints": "", "style_notes": "", "business_alignment_notes": ""},
    "production_start_signal": {"value": true, "timestamp": "", "validated_by": ""}
  },
  "memory_write": ["second_level_plan", "production_start_signal"]
}
```

- **Checkpoint:** CP3_PLANNING_END — critico, segna inizio produzione

- **Criteri validazione:**
  - `video_structure` presente, non vuoto, non reinterpretato
  - `chapters` definito
  - `details` non generico, concreto
  - `production_start_signal` esplicito TRUE
  - Coerenza con decisione GO e con risk_flags gestiti

- **Criteri passaggio a F4:**
  - CP3 salvato + `production_start_signal=TRUE` + validazione superata + memory_write OK

- **Rischi:**
  - video_structure mancante (violazione requisito originale) → failure critico
  - plan incoerente con qualifica
  - memory write failure

- **Self-healing:**
  - missing output (video_structure) → `retry` con read forzata da requisiti originali + `rollback` a CP2 + `escalate` se persiste
  - incoherent output → `requalify` (rimanda a F2 con anomaly flag)
  - memory write failure → retry + escalate

---

### FASE 4 — PRODUZIONE

- **Nome fase:** F4_PRODUCTION
- **Scopo:** Ricevere piano approvato e scrivere intero libro in coerenza con decisioni e vincoli emersi nelle fasi precedenti.
- **Agenti coinvolti:** Production Team (2 sub-agenti)
  - `BookWriterAgent`: write entire book
  - `ConsistencyGuardianAgent`: maintain consistency with all previous decisions and constraints, read from memory
  - Skill: `SelfHealingSkill`

- **Input:**
  - `second_level_plan` approvato
  - Memoria completa: `decisions`, `plans`, `checkpoints`, `hierarchies`, `important_notes`, `risk_flags`
  - `production_start_signal=TRUE`

- **Attività:**
  1.  MemoryReaderAgent recupera: second_level_plan, decisions, qualification_plan, important_notes.
  2.  `BookWriterAgent` scrive libro completo seguendo chapters + details + video_structure.
  3.  `ConsistencyGuardianAgent` verifica durante scrittura che non compaiano elementi assurdi / troppo lenti / incoerenti con GO decision.
  4.  Log di decisioni prese durante scrittura.
  5.  Scrittura in memoria di complete_book + production_log + checkpoint.

- **Output:**
```json
{
  "complete_book": "full written book content reference",
  "production_log": {"decisions_made": [], "consistency_checks": [], "deviations": []},
  "memory_write": ["complete_book", "production_log"]
}
```

- **Checkpoint:** CP4_PRODUCTION_END dopo ogni capitolo + finale

- **Criteri validazione:**
  - Libro completo, non parziale
  - Coerenza con second_level_plan (chapters rispettati, video_structure considerato)
  - Nessuna introduzione di elementi flaggati come assurdi in F2
  - Log presente

- **Criteri passaggio a F5:**
  - complete_book validato + production_log salvato + CP4 finale

- **Rischi:**
  - blocked process (scrittura bloccata)
  - incoherent output (libro incoerente con piano)
  - memory write failure

- **Self-healing:**
  - blocked → retry con lettura memoria per riconnessione contesto → rollback a ultimo CP4 capitolo
  - incoherent → requalify parziale: flag in important_notes + retry capitolo
  - memory write failure → retry

---

### FASE 5 — GRAFICHE E COPERTINA

- **Nome fase:** F5_VISUAL
- **Scopo:** Creare grafiche, prompt per le grafiche e copertina del libro, collegandosi a Playwright dove necessario.
- **Agenti coinvolti:** Visual Team (3 sub-agenti)
  - `GraphicsCreatorAgent`: create graphics
  - `PromptEngineerAgent`: create prompts for graphics generation
  - `CoverDesignerAgent`: create book cover
  - Playwright usage: support visual creation and saving processes

- **Input:**
  - `complete_book` + `second_level_plan` + `chapters` + memoria `plans`, `decisions`
  - `production_log`

- **Attività:**
  1.  Read memoria: second_level_plan, complete_book reference, important_notes, style constraints.
  2.  `PromptEngineerAgent` crea graphic_prompts coerenti con contenuto libro e vincolo non-assurdo.
  3.  `GraphicsCreatorAgent` crea grafiche (riferimenti salvati via Playwright se necessario).
  4.  `CoverDesignerAgent` crea cover finale (coerente con nicchia performante).
  5.  Tutto salvato via Playwright dove richiesto (saving processes).
  6.  Memory write + checkpoint finale.

- **Output:**
```json
{
  "graphics": ["ref_grafica_1", "ref_grafica_2"],
  "graphic_prompts": [{"prompt": "", "purpose": "", "chapter_ref": ""}],
  "cover": "final_book_cover_ref",
  "memory_write": ["graphics", "graphic_prompts", "cover"]
}
```

- **Checkpoint:** CP5_VISUAL_END + CP_FINAL (fine workflow intera pipeline)

- **Criteri validazione:**
  - graphics non vuota se richiesta da details (altrimenti esplicito skip_and_log)
  - graphic_prompts presenti e tracciati
  - cover presente, finale
  - Coerenza con libro + piano

- **Criteri passaggio a chiusura:**
  - Validazione superata + memory_write + CP_FINAL → workflow completo → signal per AutoImprovementEngine

- **Rischi:**
  - Playwright failure su saving
  - missing output (cover mancante)
  - memory write failure

- **Self-healing:**
  - Playwright failure → retry → skip_and_log del singolo asset se non bloccante
  - missing cover → retry → escalate (cover è critico)
  - memory write failure → retry

---

## 4. TEAM DI AGENTI

### Research Team
- **Nome:** Research Team
- **Responsabilità:** find books via keyword search on Amazon; find sites that analyze or calculate Amazon reviews; collect all relevant information; save results, sources, URLs, notes via Playwright
- **Rapporto con altri team:** Upstream di tutti. Fornisce structured_output a Qualification Team. Non ha dipendenze downstream dirette ma legge hierarchies da orchestrator. In caso di empty result, trigger self-healing che può richiedere nuove keyword da memory (important_notes).
- **Tipo output:** list of book opportunities with metadata + list of sites with analysis data + raw_data salvato via Playwright + structured_output
- **Dati che legge da memoria:** hierarchies, checkpoints (per deduplicazione), important_notes (keyword storiche, pattern di successo/fallimento)
- **Dati che scrive in memoria:** checkpoints (CP1), raw_data refs, books_found (via MemoryWriterAgent), important_notes su strategie di ricerca

### Qualification Team
- **Nome:** Qualification Team
- **Responsabilità:** receive research output; create detailed qualification plan; evaluate if a book can be reproduced; evaluate if there are absurd or unrealistic elements; evaluate if book is too slow to produce; evaluate if qualification plan itself is valid; produce clear decision on book potential
- **Rapporto:** Riceve da Research Team, invia solo GO a Planning Team. In caso di NO-GO massivo, segnala a orchestrator e ad AutoImprovementEngine, torna a Research. Usa BookNicheDecisionSkill centralmente.
- **Tipo output:** qualification_plan dettagliato, decision GO/NO-GO motivata, risk_flags, memory_write
- **Legge da memoria:** structured_output, books_found, decisions storiche, risk_flags storici, important_notes, plans precedenti, checkpoints CP1
- **Scrive in memoria:** decisions (GO/NO-GO), plans (qualification_plan), important_notes (risk_flags), checkpoints CP2

### Planning Team
- **Nome:** Planning Team
- **Responsabilità:** receive qualification output; create second-level operational plan; define video structure; define chapters; define every relevant detail; mark actual start of production flow
- **Rapporto:** Riceve da Qualification Team solo GO, fornisce second_level_plan a Production Team e Visual Team. Gate critico per business alignment.
- **Tipo output:** second_level_plan completo {video_structure REQUIRED, chapters, details, production_start_signal}
- **Legge da memoria:** decisions, qualification_plan, risk_flags, checkpoints CP2, hierarchies, important_notes
- **Scrive in memoria:** plans (second_level_plan), decisions (production_start_signal), checkpoints CP3, important_notes su vincoli

### Production Team
- **Nome:** Production Team
- **Responsabilità:** receive approved second-level plan; write entire book; maintain consistency with all previous decisions and constraints; read from memory to maintain context continuity
- **Rapporto:** Riceve da Planning Team, fornisce complete_book a Visual Team. Usa MemoryReaderAgent intensivamente per coerenza.
- **Tipo output:** complete_book full written, production_log, memory_write
- **Legge da memoria:** second_level_plan, decisions, plans, checkpoints, hierarchies, important_notes, risk_flags, qualification_plan
- **Scrive in memoria:** complete_book, production_log, checkpoints CP4, important_notes su deviazioni/coerenza

### Visual Team
- **Nome:** Visual Team
- **Responsabilità:** create graphics; create prompts for graphics generation; create the book cover; connect to Playwright where needed
- **Rapporto:** Downstream finale. Riceve da Production Team e Planning Team. Chiude la pipeline.
- **Tipo output:** graphics, graphic_prompts, cover, memory_write
- **Legge da memoria:** second_level_plan, complete_book, production_log, plans, decisions, important_notes
- **Scrive in memoria:** graphics, graphic_prompts, cover, checkpoints CP5/CP_FINAL, important_notes su prompt efficaci

### Memory Ecosystem Agents (trasversali, always_active)
- **MemoryWriterAgent:** scrive structured data da tutti i team
- **MemoryReaderAgent:** recupera relevant memory on request
- **MemoryValidatorAgent:** verifica memory consistency e flag corruzione/gap
- **CheckpointManagerAgent:** gestisce checkpoint creation, storage, restoration
- **Rapporto:** Servono tutti i team. Non producono output di business ma output di sistema.

---

## 5. SKILL

### SKILL 1 — BookNicheDecisionSkill
- **Nome:** BookNicheDecisionSkill
- **Funzione:** decide which books and niches to target
- **Fasi in cui viene usata:** research, qualification (obbligatorio), può informare planning per business_alignment
- **Motivo per cui deve esistere come skill separata:** central to every cycle, reused across phases, directly tied to business objective (quantità di libri performanti). Evita duplicazione logica di decisione nicchia in ogni team.
- **Input:** market signals, keyword data, review data (tutti derivati esclusivamente da Amazon keyword search + sites that analyze Amazon reviews, senza inventare altre fonti)
- **Output:** ranked list of book opportunities with scores (score descrittivo, non metrica inventata, con motivazione trace: performante, riproducibile, sostenibile, non absurdo, non lento)
- **Condizioni di attivazione:** 
  - In F1: dopo collection, per pre-ranking
  - In F2: obbligatoria per ogni qualification_plan, per decisione GO/NO-GO
  - Trigger: ogni volta che `books_found` o `structured_output` disponibile

### SKILL 2 — SelfHealingSkill
- **Nome:** SelfHealingSkill
- **Funzione:** detect, handle and recover from failures in any phase
- **Fasi in cui viene usata:** all (trasversale)
- **Motivo per cui deve esistere come skill separata:** transversal, reused by every team, requires dedicated logic and memory access. Non può essere replicata in ogni team altrimenti incoerenza nella gestione failure.
- **Input:** error signals, phase status, checkpoints (da MemoryEcosystem)
- **Output:** recovery action (retry/rollback/escalate/skip_and_log/requalify), updated checkpoint, anomaly log (in important_notes)
- **Condizioni di attivazione:** 
  - Su qualsiasi detection trigger: missing output, incoherent output, blocked process, failed validation, empty result from research, no-go decision without alternative path, memory write failure, Playwright failure
  - Monitoraggio continuo da SelfHealingEngine

**Nota conformità:** Nessuna altra skill introdotta perché non derivabile direttamente dai requisiti. Proposte di skill tipo CoverPromptSkill o WritingSkill sarebbero invenzioni non consentite: le responsabilità di scrittura e visual rimangono dentro i team.

---

## 6. ECOSISTEMA DI MEMORIA

### Struttura Piccolo Ecosistema di Memoria — Always Active, Integrato

**Stato:** always_active
**Integrazione:** all phases and all teams
**Principio:** Ogni fase lascia tracce leggibili, ogni output è direttamente usabile dalla fase successiva, ogni checkpoint è ripristinabile da SelfHealingEngine.

### Categorie di Memoria

#### A) checkpoints
- **Descrizione:** state snapshots at critical points
- **Cosa viene salvato:** CP0_INIT (hierarchies), CP1_RESEARCH_END, CP2_QUALIFICATION_END (per libro + batch), CP3_PLANNING_END, CP4_PRODUCTION_END (per capitolo + finale), CP5_VISUAL_END, CP_FINAL
- **Quando:** at the end of each phase and at critical decision points (GO/NO-GO, production_start_signal)
- **Chi scrive:** all teams via CheckpointManagerAgent + MemoryWriterAgent
- **Chi legge:** self-healing engine, all teams on recovery, orchestrator
- **Gestione:** CheckpointManagerAgent crea, versiona, valida, restaura. Ogni checkpoint ha {phase, timestamp, data_ref, valid=TRUE/FALSE, parent_checkpoint_id}. Su rollback, SelfHealingSkill ripristina parent valido.

#### B) decisions
- **Descrizione:** all go/no-go and qualification decisions
- **Cosa salvato:** decision value (GO/NO-GO), motivation, trace, qualification_plan ref, risk_flags, business_alignment notes
- **Quando:** at every decision point (F2 per ogni libro, F3 per production_start_signal)
- **Chi scrive:** qualification team, planning team
- **Chi legge:** production team, visual team, auto-improvement engine, future qualification cycles
- **Registrazione:** Ogni decisione è immutabile, con append-only log + motivazione. NO-GO ha alternative_path flag.

#### C) plans
- **Descrizione:** qualification plans and second-level plans
- **Cosa salvato:** qualification_plan completo (5 criteri), second_level_plan (video_structure, chapters, details, production_start_signal)
- **Quando:** when a plan is approved and validated (F2 valid, F3 valid)
- **Chi scrive:** qualification team, planning team
- **Chi legge:** production team, visual team, auto-improvement engine (per plan validity scores)
- **Conservazione:** Versionato, non sovrascritto. Ogni plan ha validity_score descrittivo, linked a decision.

#### D) hierarchies
- **Descrizione:** agent hierarchies and team responsibilities
- **Cosa salvato:** struttura team, responsabilità, input/output contratti, skill mapping, Playwright usage policy
- **Quando:** at workflow initialization and on update (se orchestrator modifica)
- **Chi scrive:** orchestrator (unica fonte)
- **Chi legge:** all teams (per sapere cosa devono fare e cosa leggere/scrivere)
- **Mantenimento:** MemoryValidatorAgent verifica che hierarchies non siano corrotte; se gap → SelfHealingSkill escalates.

#### E) important_notes (important notes to remember)
- **Descrizione:** critical notions, risk flags, anomaly logs
- **Cosa salvato:** risk_flags, anomaly logs, Playwright failure notes, keyword patterns efficaci/inefficaci, segnali di libri assurdi/lenti, improvement suggestions, validation uncertainties
- **Quando:** whenever a relevant signal is detected (in qualsiasi fase, da qualsiasi agente + da SelfHealingEngine + da AutoImprovementEngine)
- **Chi scrive:** all teams, self-healing engine, auto-improvement engine
- **Chi legge:** all teams, auto-improvement engine, future research cycles
- **Mantenimento:** MemoryValidatorAgent flagga corruzione/gap. Deduplicazione periodica ma senza perdita di trace decisionali.

### Flusso Read/Write Standardizzato
```
Team → MemoryWriterAgent.write(category, data, writer) → checkpoint_created=TRUE → MemoryValidatorAgent verifica

Team → MemoryReaderAgent.read(category, requester) → relevant data + timestamp

CheckpointManagerAgent → create/restore → SelfHealingEngine può invocare restore su failure
```

### Gestione Checkpoint Dettagliata
- Creazione: fine fase + decisione critica
- Storage: reference in memoria con timestamp e parent
- Restoration: solo via SelfHealingSkill con log in important_notes: {restored_from, reason, phase, action_taken}
- Validazione: MemoryValidatorAgent verifica consistenza tra checkpoint e memory categories (es. decisione scritta ma checkpoint non creato → flag)

---

## 7. SELF-HEALING

### SelfHealingEngine — Scope: all phases, all teams, all processes — Always Active

#### Detection Triggers (8 obbligatori)
1.  missing output
2.  incoherent output
3.  blocked process
4.  failed validation
5.  empty result from research
6.  no-go decision without alternative path
7.  memory write failure
8.  Playwright failure

#### Response Actions (5)
- **retry:** retry the failed operation with adjusted parameters (es. nuova keyword, rilettura memoria, nuovo tentativo Playwright)
- **rollback:** return to last valid checkpoint (via CheckpointManagerAgent)
- **escalate:** flag the anomaly and pause that branch (scrive in important_notes, non blocca intero workflow, segnala orchestrator)
- **skip_and_log:** skip the broken step, log it, continue where possible (solo per asset non critici, es. singola grafica, non cover)
- **requalify:** send the item back to qualification with anomaly flag (quando incoerenza rilevata in F3/F4)

#### Schema handle_failure per fase

**F1 - Research:**
- empty result → retry con adjusted keyword da important_notes → se 2 fail → skip_and_log batch + escalate + genera improvement signal per future research quality
- Playwright failure → retry 2x → rollback a CP0 → log + escalate
- memory write failure → retry → escalate

**F2 - Qualification:**
- missing output → retry → rollback a CP1
- incoherent output → rollback a CP1 + re-execute BookNicheDecisionSkill
- no-go without alternative → requalify con flag "all no-go" → richiedi a F1 nuovo batch con keyword diverse (via memory) + log
- failed validation → escalate + create validation checkpoint (vedi Sez 10)

**F3 - Planning:**
- missing video_structure → CRITICAL → retry + read forzato requisito originale + se fallisce → rollback a CP2 + escalate (blocco produzione)
- incoherent plan → requalify → rimanda a F2 con anomaly flag
- failed validation → rollback a CP2

**F4 - Production:**
- blocked process → retry con read memoria per riconnessione → rollback a ultimo CP4 capitolo
- incoherent output → skip capitolo? NO, critical → retry capitolo + requalify parziale + log
- memory write failure → retry

**F5 - Visual:**
- Playwright failure su saving → retry → skip_and_log se grafica singola, escalate se cover
- missing output cover → retry → escalate (cover è finale, non skippabile)
- incoherent graphics vs book → retry con read memoria + log

#### Memory Updated su ogni handling
Ogni handle_failure scrive in `important_notes`: {phase, error_type, checkpoint_restored, action_taken, memory_updated=TRUE, flow_continued, timestamp}

---

## 8. AUTO-MIGLIORAMENTO

### AutoImprovementEngine — Scope: all phases — Alimentato da esiti reali

#### Feedback Signals (6 obbligatori)
1.  **qualification outcomes:** GO vs NO-GO ratio, motivazioni ricorrenti
2.  **production speed metrics:** tempo effettivo per fase, per capitolo, flag too slow reali vs stimati (senza inventare metriche esterne: solo misurazione tempo interno)
3.  **book performance signals:** segnali di performance osservati in ricerca (da Amazon e review analysis sites) dei libri simili a quelli prodotti → loop feedback qualitativo
4.  **self-healing activation frequency:** quante volte scatta, dove, perché → indica fragilità
5.  **plan validity scores:** quante volte un plan è stato giudicato invalido in F2/F3
6.  **memory retrieval patterns:** cosa viene letto di più, cosa mai, gap di memoria

#### Improvement Targets (5)
1.  future research quality
2.  future qualification decisions
3.  future plan accuracy
4.  production flow speed
5.  risk detection sensitivity

#### Schema generate_improvement_signal
```json
{
  "source_phase": "F2_QUALIFICATION",
  "outcome_summary": {"GO_rate": "...", "main_NO-GO_reason": "..."},
  "improvement_suggestion": "es. evitare keyword X perché porta a libri too slow, rafforzare controllo absurd",
  "target": "next cycle F1 research + F2 qualification",
  "memory_write": true,
  "written_to": "important_notes + checkpoints improvement log"
}
```

#### Ciclo di Miglioramento Continuo
1.  Ogni fase alla chiusura genera `improvement_signal`
2.  MemoryWriterAgent scrive signal in `important_notes` + `checkpoints`
3.  Prima di ogni nuovo ciclo, Research Team e Qualification Team leggono `important_notes` per adattare keyword e criteri
4.  BookNicheDecisionSkill aggiorna ranking in base a lessons learned (senza introdurre nuovi dati, solo pesi qualitativi su evidenze esistenti)
5.  SelfHealingEngine riduce frequenza su pattern risolti

**Esempio concreto:**
- Se F2 scarta 80% per `too slow to produce` su nicchia X → AutoImprovement segnala a F1: deprioritizza keyword di X → future research quality migliorata → risk detection sensitivity aumentata per speed.
- Se F3 ha molti rollback per video_structure mancante → improvement target: future plan accuracy → aggiunta checklist validazione F3.

---

## 9. HANDOFF TRA FASI

### Regola: Ogni handoff è esplicito, strutturato, tracciato in memoria, validato.

#### H1: F1 → F2
- **Da:** Research Team
- **A:** Qualification Team
- **Payload:** structured_output + books_found + review_sites_found + raw_data ref + CP1 ID
- **Canale:** output file salvato via Playwright + scrittura memoria (checkpoints, important_notes)
- **Validazione handoff:** MemoryValidatorAgent verifica che structured_output non vuoto e URLs salvati, che CP1 esista
- **Traccia memoria:** CheckpointManagerAgent logga handoff ID, MemoryWriterAgent scrive handoff event in important_notes
- **Failure path:** Se payload empty → SelfHealingEngine trigger empty result → non avanza

#### H2: F2 → F3
- **Da:** Qualification Team
- **A:** Planning Team
- **Payload:** Solo opportunità con decision=GO + qualification_plan + risk_flags + CP2 ID
- **Canale:** memoria decisions + plans + checkpoint
- **Validazione:** decision==GO AND plan_validity==TRUE AND absurdity_check==FALSE AND production_speed!=too_slow
- **Traccia:** decisions immutabili, CP2
- **Failure path:** NO-GO → ramo chiuso, non handoff, log + auto-improvement + ritorno a F1

#### H3: F3 → F4
- **Da:** Planning Team
- **A:** Production Team
- **Payload:** second_level_plan completo (video_structure REQUIRED + chapters + details + production_start_signal TRUE) + CP3 ID
- **Canale:** memoria plans + decisions
- **Validazione:** video_structure presente verbatim + production_start_signal TRUE + chapters non vuoto + CP3 valid
- **Traccia:** CP3 = inizio produzione ufficiale
- **Failure path:** Se video_structure mancante → critical self-healing → rollback a CP2, no advance

#### H4: F4 → F5
- **Da:** Production Team
- **A:** Visual Team
- **Payload:** complete_book ref + production_log + second_level_plan + CP4 finale
- **Canale:** memoria checkpoints + plans + complete_book
- **Validazione:** complete_book non vuoto, production_log presente, coerenza con plan
- **Traccia:** CP4 finale, important_notes coerenza
- **Failure path:** blocked/incoherent → self-healing rollback a CP4 capitolo

#### H5: F5 → CHIUSURA
- **Da:** Visual Team
- **A:** Orchestrator / Output Finale
- **Payload:** graphics + graphic_prompts + cover + complete_book + CP5 + CP_FINAL
- **Canale:** memoria finale + file salvati via Playwright
- **Validazione:** cover presente, graphic_prompts tracciati, graphics salvate via Playwright, memory_write completo
- **Traccia:** CP_FINAL + memory_write finale + improvement_signal per ciclo

**Principio handoff:** Ogni team non chiama direttamente il prossimo. Orchestrator + MemoryEcosystem fanno da broker. Ogni handoff ha checkpoint, così rollback sempre possibile.

---

## 10. AMBIGUITÀ E PUNTI DI CONTROLLO

### Metodo handle_ambiguity applicato sistematicamente

```python
def handle_ambiguity(requirement):
    return {
        "original_requirement": requirement,
        "ambiguity_detected": True,
        "action": "preserve_and_encapsulate",
        "resolution_method": "create_validation_checkpoint",
        "forbidden_action": "fill_with_assumptions",
        "output": "explicit_control_point_in_workflow"
    }
```

#### Lista Ambiguità Rilevate e Gestione

**A1 - AMBIGUITÀ CRITICA: "struttura del video" / "video structure"**
- **Requisito originale:** `video_structure` REQUIRED as per original requirements in Planning Team
- **Ambiguità:** Cosa significa video in workflow di libri? Tipo di video? Durata? Formato? Non definito.
- **Azione:** preserve_and_encapsulate
- **Risoluzione:** Creato CONTROL POINT CP-VIDEO-01 in F3
  - Campo `video_structure` mantenuto verbatim, non riscritto, non reinterpretato
  - Struttura: {"original_requirement": "video structure", "preserved_as_is": true, "validation_required": "human_or_orchestrator must confirm interpretation before F4", "placeholder_for_detail": "every relevant detail must specify how video_structure integrates with book chapters"}
  - Self-healing: se manca → failure critico, non inventare → escalate
  - Memory: scritto in plans + important_notes con flag `ambiguity_preserved`

**A2 - "libri performanti"**
- **Ambiguità:** Cosa è performante? Quale metrica? BSR, review count, rank? Non specificato in requirements, vietato inventare metriche.
- **Azione:** preserve_and_encapsulate
- **Risoluzione:** CONTROL POINT CP-PERF-01 in F1 e F2
  - Definizione: performance = segnali osservabili tramite keyword search on Amazon + sites that analyze or calculate Amazon reviews, senza introdurre metrica esterna inventata
  - BookNicheDecisionSkill output: ranked list con motivazione descrittiva basata su segnali disponibili, non su metriche inventate
  - Validation checkpoint: Qualification Team deve esplicitare quale segnale osservato motiva "performante" per ogni libro

**A3 - "troppo lenti da realizzare" / "assurdi"**
- **Ambiguità:** Soglia tempo? Cosa è assurdo? Soggettivo.
- **Azione:** preserve_and_encapsulate
- **Risoluzione:** CONTROL POINT CP-SPEED-ABSURD-01 in F2
  - Criteri lasciati qualitativi: too slow = produzione non compatibile con obiettivo quantità (valutazione da team)
  - absurd = elementi irrealistici, non sostenibili, incoerenti con produzione (valutazione da team)
  - Ogni valutazione deve avere evidence in qualification_plan + risk_flag
  - Auto-improvement raccoglie pattern per affinare sensibilità nel tempo

**A4 - "siti che analizzano o calcolano Amazon reviews"**
- **Ambiguità:** Quali siti? Non listati. Non possiamo inventare nomi.
- **Azione:** preserve_and_encapsulate
- **Risoluzione:** CONTROL POINT CP-SITES-01 in F1
  - Task di ReviewSiteDiscoveryAgent: trovare tali siti tramite Playwright senza assumere lista predefinita
  - Output: lista di siti trovati con URL, tipo di analisi, data collected
  - Validation: MemoryValidatorAgent verifica che siti siano pertinenti ad Amazon reviews, non generici
  - Se nessun sito trovato: trigger empty result ma non fallimento totale se books_found esiste

**A5 - "grafiche, prompt grafici e copertina"**
- **Ambiguità:** Quante grafiche? Stile? Tool generazione? Non specificato, vietato inventare API grafiche.
- **Azione:** preserve_and_encapsulate
- **Risoluzione:** CONTROL POINT CP-VISUAL-01 in F3 e F5
  - F3 `details` deve specificare quante grafiche necessarie e dove
  - F5 crea graphic_prompts coerenti, senza assumere tool esterno: prompt sono output testuali, graphics sono refs salvate via Playwright (support visual creation and saving processes)
  - Nessuna API immagini inventata

**A6 - "piccolo ecosistema di memoria"**
- **Ambiguità:** Piccolo quanto? Tecnologia? Dimensione?
- **Risoluzione:** Implementato come definito in requisiti: 5 categorie (checkpoints, decisions, plans, hierarchies, important notes), 4 agenti, always_active, integration all phases. Non introdotta tecnologia storage esterna: solo logica di agenti + read/write astratta.

**Politica Generale:** Mai riempire gap con supposizioni. Ogni ambiguità = checkpoint di validazione esplicito + log in important_notes + traccia decisionale.

---

## 11. ORDINE DI IMPLEMENTAZIONE CONSIGLIATO

### Priorità rispettando DESIGN_PRIORITIES: operational_clarity > flow_feasibility > selection_quality > production_sustainability > modularity > traceability > resilience > improvement

**STEP 0 - Fondamenta (Settimana 1)**
1.  Implementare `MemoryEcosystem` + 4 agenti memoria + strutture categorie + read/write API astratta
2.  Implementare `CheckpointManagerAgent` e logica checkpoint creation/restoration
3.  Implementare `hierarchies` init da orchestrator, salvataggio in memoria
4.  Validare con MemoryValidatorAgent

**STEP 1 - Resilienza Trasversale (Settimana 1-2)**
5.  Implementare `SelfHealingSkill` e `SelfHealingEngine` con 8 trigger e 5 azioni
6.  Integrare self-healing hooks in ogni fase (stub)
7.  Testare handle_failure con scenari: missing output, Playwright failure, memory write failure

**STEP 2 - Skill Centrali (Settimana 2)**
8.  Implementare `BookNicheDecisionSkill`: input market signals (solo da Amazon + review sites), output ranked list con scores descrittivi + motivazione
9.  Collegare skill a memoria (legge important_notes storiche)
10. Testare skill su dati fittizi ma conformi (solo URL Amazon + review sites)

**STEP 3 - F1 Research (Settimana 2-3)**
11. Implementare Research Team + Playwright wrapper per Amazon keyword search e review sites discovery
12. Implementare CollectorAgent + structured_output normalizer
13. Implementare CP1 + memory_write
14. Integrare BookNicheDecisionSkill in pre-ranking
15. Test E2E F1 con self-healing empty result e Playwright failure

**STEP 4 - F2 Qualification (Settimana 3-4)**
16. Implementare Qualification Team con 5 criteri espliciti
17. Implementare decision policy (halt_branch se insufficient info)
18. Implementare CP2 + memory_write decisions/plans/risk_flags
19. Integrare BookNicheDecisionSkill (core) + self-healing no-go without alternative path
20. Test con batch F1 reale simulato: pochi GO, molti NO-GO → verifica loop

**STEP 5 - F3 Planning Second Level (Settimana 4)**
21. Implementare Planning Team
22. Implementare CONTROL POINT critico video_structure: preservazione verbatim + validation checkpoint
23. Implementare second_level_plan con production_start_signal esplicito
24. CP3 = produzione start gate
25. Test ambiguità handling

**STEP 6 - F4 Production (Settimana 5)**
26. Implementare Production Team con MemoryReader intensivo per coerenza
27. Implementare production_log e consistency checks
28. CP4 per capitolo + finale
29. Test coerenza con decisioni precedenti, test blocked process healing

**STEP 7 - F5 Visual (Settimana 5-6)**
30. Implementare Visual Team: graphics, graphic_prompts, cover
31. Playwright usage limitato a support visual creation and saving processes (non navigazione inventata)
32. CP5 + CP_FINAL
33. Test cover mancante → escalate

**STEP 8 - Auto-Miglioramento Chiusura Loop (Settimana 6)**
34. Implementare AutoImprovementEngine con 6 feedback signals e 5 target
35. Integrare generazione improvement_signal in ogni fase end
36. Implementare lettura important_notes all'inizio di ogni nuovo ciclo per adattare ricerca/qualifica
37. Test ciclo completo 2 iterazioni: verifica che second cycle sia migliore su research quality

**STEP 9 - Orchestrazione End-to-End e Hardening (Settimana 7)**
38. Collegare tutti gli handoff H1-H5 via MemoryEcosystem broker (non chiamate dirette)
39. Implementare orchestrator che verifica decision_policy (sufficient_for_advance)
40. Stress test: empty results, incoherent outputs, Playwright failures su ogni fase
41. Validare che ogni fase lasci tracce leggibili e che output sia direttamente usabile dalla successiva

**STEP 10 - Validazione Business (Settimana 7-8)**
42. Eseguire workflow completo su 2-3 nicchie diverse (solo tramite keyword Amazon + review sites)
43. Misurare: GO rate, tempo produzione, attivazioni self-healing, qualità memory retrieval
44. Verificare obiettivo: quantità di libri performanti riproducibili sostenibili non absurdi non troppo lenti → valutazione qualitativa da orchestrator
45. Freeze blueprint, documentare lessons learned in important_notes

### Deliverable Finale di Implementazione
- Codice orchestrator + 5 team + 4 memory agents + 2 skill + 2 engine trasversali
- Playwright scripts conformi a PLAYWRIGHT_USAGE_POLICY (solo usi consentiti)
- Storage memoria (qualsiasi tech, ma categorie come da requisiti)
- Log completo checkpoints, decisions, plans, hierarchies, important_notes
- Dashboard (opzionale, non inventando tool esterni: può essere vista di memoria) per decision_traceability

---

## APPENDICE - CONFORMITÀ REGOLA PRINCIPALE

**Verifica ALLOWED_ELEMENTS:**
- platforms: solo Amazon usato → OK
- research_methods: solo keyword search on Amazon → OK
- external_sources: solo sites that analyze or calculate Amazon reviews → OK, non nominati siti specifici inventati
- automation_tools: solo Playwright → OK
- system_components: agent teams, skills, self-healing, auto-improvement, memory ecosystem → OK
- memory_contents: checkpoints, decisions, plans, hierarchies, important notes → OK

**Nessuna API inventata, nessuna metrica inventata (BSR, conversion rate, ecc non introdotti), nessun canale (social, email) introdotto, nessuna automazione oltre Playwright.**

**Gestione ambiguità:** Tutti i punti ambigui trasformati in validation checkpoint espliciti, non riempiti con assunzioni.

---

**FINE BLUEPRINT**
