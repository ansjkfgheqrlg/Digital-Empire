# Memory Query Interface

La Memory Query Interface (MQI) rappresenta il sistema di gestione dello stato persistente e contestuale per gli agenti. Non viene considerata un database piatto, ma un'interfaccia a grafo gerarchico che fornisce contesto in base a rilevanza, recency e confidence.

## Principi Fondamentali

- **P1: READ-ANYWHERE**: Le operazioni di lettura sono sempre libere e non acquisiscono lock (no-blocking in lettura).
- **P2: WRITE-LOCK**: La scrittura richiede l'acquisizione di un lock esclusivo con un timeout rigoroso di 100ms. In caso di timeout, la scrittura abortisce o pianifica un retry.
- **P3: PROVENANCE AUTHOR**: Ogni informazione registrata deve dichiarare espressamente l'autore (agente o script sorgente) come metadato.
- **P4: CONTEXTUALITY**: Gli agenti leggono solo informazioni pertinenti al task corrente tramite un algoritmo di scoring, evitando dump completi di memoria.
- **P5: CONFIDENCE DECAY**: Le informazioni invecchiano. Viene applicato un moltiplicatore di obsolescenza (recency) che riduce l'importanza delle informazioni vecchie a meno che non siano costantemente ri-accedute.

---

## Tipi di Query Supportati

### 1. Contextual Recall
Recupera le informazioni rilevanti estraendo keyword dal task dell'agente.
- **Input**: `{current_task, current_agent, max_results}`
- **Processo**: Estrazione keyword, calcolo score combinato `relevance * recency * confidence` e filtro su confidence > 0.60.

### 2. Decision Lookup
Cerca decisioni affini o identiche prese in passato per evitare collisioni o duplicati.
- **Input**: `{decision_description, similarity_threshold}`
- **Processo**: Similarity match semantico/keyword nel Decision Log. Ritorna l'esito della decisione passata (SUCCESS/FAIL) e se riutilizzarla.

### 3. Strategy Fetch
Trova la strategia ottimale per risolvere un problema ricorrente.
- **Input**: `{problem_type, constraints}`
- **Processo**: Filtra lo Strategy Store in base ai vincoli e ordina per tasso di successo storico (`success_rate` discendente).

### 4. Write
Scrive una informazione in modo sicuro.
- **Processo**: Acquisisce il lock esclusivo, valida lo schema JSON del layer, deduplica e scrive aggiungendo metadati automatici (`id`, `timestamp`, `session_id`, `access_count`, `version`, `status`).

### 5. Forget (Strategic Forgetting)
Nessuna informazione viene eliminata fisicamente per ragioni di audit. Viene impostato lo stato `ARCHIVED` con motivazione e flag `superseded_by` che punta al record sostitutivo.
- **Trigger**: Strategie con tassi di successo bassi (< 30%), record antecedenti a 90 giorni con 0 accessi, o ordini diretti del Meta-Agent.
