# 🚀 ADVANCED_OPERATIONS — Usi Sofisticati della Wiki

Questa sezione è per quando capisci bene il sistema base e vuoi sfruttarlo al massimo.

---

## 🤖 Operazioni Avanzate (Le Usiamo Dopo il Primo Mese)

### 1. AUTO-TAGGING & CATEGORIZZAZIONE
```
Quando aggiungi file in raw/, io:
- Scansiono il testo
- Estraggo i tag automaticamente
- Categoria il file nella wiki corretta
- Aggiorno l'indice

Esempio:
raw/articolo_funnel.txt
→ Io noto: "Questo è su funnel e conversion"
→ Creo/aggiorno [[Concept: Funnel Sales]]
→ Assegno tag #sales #conversion
```

### 2. CROSS-LINKING AUTOMATICO
```
Quando creo una nuova pagina, io:
- Trovo 5-10 pagine correlate
- Aggiungo link bidirezionali
- Creo "Vedi anche" sections
- Aggiorno graph view

Così non devi linkare manualmente.
```

### 3. GRAPH VISUALIZATION & INSIGHTS
```
Usando Obsidian's graph view:
- Vedi il grafo completo della wiki
- Identifica nodi centrali (concetti importanti)
- Nota cluster (domini interconnessi)
- Scopri nodi isolati (opportunità di connessione)

/generate-graph-report
→ Io creo un report visuale della struttura
```

### 4. SEMANTIC SIMILARITY SEARCH
```
/search-semantic [query]
→ Io non cerco parole esatte, ma SENSO
→ Trovo pagine correlate anche se non contengono le parole che cerchi

Es: "Come attiro clienti nuovi?"
→ Trovo [[Concept: Funnel]], [[Metric: CAC]], [[Project: Lancio...]],
         [[Synthesis: Growth strategies]]
```

### 5. CONTRADICTION DETECTION
```
/find-contradictions
→ Io scansiono la wiki cercando affermazioni contraddittorie

Es: "Pagina A dice che l'email marketing converte al 5%"
    "Pagina B dice che l'email marketing converte al 3%"
    
→ Io le segnalo per reconciliation
```

### 6. PATTERN MINING & DISCOVERY
```
/mine-patterns [dominio]
→ Io esamino tutti i progetti in un dominio
→ Estraggo pattern ricorrenti
→ Creo nuove pagine di synthesis

Es: /mine-patterns "Info Products"
→ Io noto: tutti i corsi di successo seguono questo funnel
→ Creo [[Synthesis: Winning pattern for course launches]]
```

---

## 🔧 Integrazioni & Automazioni (V1.5+)

### Setup: Obsidian Web Clipper
```
1. Installa Obsidian Web Clipper (browser extension)
2. Configura per salvare in raw/
3. Quando leggi online, clicca il clipper
4. Automaticamente aggiunge a raw/

Io periodicamente:
/process-webclipper-inbox
→ Processiamo tutto quello che hai clippato
```

### Setup: Git + Versioning
```
cd second-brain-vault
git init
git add .
git commit -m "Initial wiki"
git push origin main

Così:
- La wiki è versionata
- Puoi collaborare con il team
- Hai backup su GitHub
```

### Setup: Scheduled Lint & Synthesis
```
Ogni lunedì mattina:
- /lint-wiki automaticamente
- Genero un report
- Ti mando i problemi rilevati

Ogni due settimane:
- /synthesize-domains automaticamente
- Creo nuove pagine di connessione cross-domain
```

---

## 📊 Reporting & Analytics

### Weekly Report
```
/generate-weekly-report
→ Io genero un report che contiene:
  - Pagine aggiunte questa settimana
  - Link creati
  - Pattern emersi
  - Azioni proposte
  - Health check della wiki
```

### Monthly Deep Dive
```
/generate-monthly-analysis
→ Io faccio un'analisi profonda:
  - Evoluzioni nella conoscenza
  - Gap rilevati
  - Tendenze nei progetti
  - Raccomandazioni strategiche
  - Mappa del knowledge growth
```

### Domain-Specific Report
```
/report-domain [dominio]
→ Io genero un report su UN dominio
  (es: Agenzia, Info Products, SaaS)
  
Contiene:
  - Tutte le pagine rilevanti
  - KPI del dominio
  - Progetti in corso
  - Bottleneck identificati
```

---

## 🧠 Advanced Queries

### Semantic Comparison
```
/compare-semantically [concetto A] vs [concetto B]
→ Io non faccio solo lista di differenze
→ Analizzo la relazione profonda tra i due
→ Suggerisco quando scegliere uno vs l'altro
```

### Future Forecasting
```
/forecast [metric] next-quarter
→ Io analizo la trend storica
→ Propongo proiezioni
→ Evidenzio fattori che potrebbero cambiarla
```

### Hypothetical Analysis
```
/if-scenario "Supponi che il CAC salga del 50%. Cosa cambia?"
→ Io traccia tutte le implicazioni
→ Mostro quale concetti, progetti, metriche sarebbero impattati
→ Suggerisco strategie alternative
```

---

## 🔄 Batch Operations

### Bulk Ingest
```
Metti 20 file in raw/
/ingest-batch --deep --cross-link
→ Io proceso tutto in parallelo
→ Creo pagine
→ Collego aggressivamente al resto della wiki
→ Aggiorno index e log
→ Generate un report di output
```

### Bulk Update
```
/update-all-mentions [old_concept] → [new_concept]
→ Io trovo tutte le menzioni di "old_concept"
→ Le rimpiazzo con "new_concept"
→ Aggiorno i link
```

### Archival & Cleanup
```
/archive-domain [dominio] before [date]
→ Io sposto tutte le pagine non aggiornate prima di quella data
→ Le metto in archive/
→ Mantengo le connessioni ma le "freezo"
```

---

## 🚨 Advanced Lint Operations

### Deep Lint
```
/lint-wiki --deep
→ Non solo link rotti
→ Cerca:
  - Pagine con <3 outbound links
  - Cluster isolati nel grafo
  - Concetti usati in molti posti ma non ben documentati
  - Hint per refactoring architetturale
```

### Consistency Check
```
/check-consistency
→ Verifica:
  - Nomi consistenti (es: "Email Marketing" vs "Email marketing" vs "email-marketing")
  - Metadata completi su tutte le pagine
  - Timestamps logici (non creata nel futuro, ecc)
  - Links che puntano a pagine archiviate
```

### Orphan Recovery
```
/find-orphans --suggest-links
→ Trovo pagine con 0 inbound links
→ Per ognuna, suggerisco 3-5 pagine che dovrebbero linkarle
→ Tu approvi o modifchi i suggerimenti
```

---

## 🎨 Customization & Configuration

### Change Metadata Format
```
Nel CLAUDE.md, puoi cambiare:
- Campi obbligatori per ogni tipo di pagina
- Ordine sezioni
- Tag categories
- Icons/emoji da usare

Io aderirò ai nuovi standard per tutte le pagine future.
```

### Custom Categories
```
Se decidi di aggiungere una nuova categoria (es: "Legal", "Partnerships"):
1. Crea una cartella in wiki/
2. Aggiorna wiki/index.md con la categoria
3. Mi comunichi il schema per quella categoria
4. Io comincia a creare pagine in quel formato
```

### Custom Slash Commands
```
Puoi definire shortcut personalizzati.

Es:
/launch-checklist [project]
→ Io creo una checklist basata su pattern da lanci precedenti
→ La linko ai progetti correlati
→ La metto in output/ come documento scaricabile
```

---

## 🔗 Team Collaboration

### Shared Wiki with Git
```
Se vuoi che il team collabori:
1. Push il vault su un repo GitHub privato
2. Ogni membro clona il repo
3. Apre in Obsidian localmente
4. Fa i commit dei cambiamenti
5. Io rimango aggiornato delle modifiche

Non c'è sincronizzazione real-time (Obsidian è local-first),
ma puoi settare:
/sync-team-changes
→ Io raccolgo i cambiamenti, li ricompilo, risolvo conflitti
```

### Comment Threads
```
In ogni pagina, puoi aggiungere commenti di discussione:
"Sono d'accordo che questo è il pattern vincente?"

Io raccolgo i commenti e aggiungo nella pagina:
"**Team Discussion**: [cosa dicono]"
```

### Change Log
```
/generate-changelog [data-inizio] to [data-fine]
→ Io creo un report di tutto ciò che è cambiato nel periodo
→ Chi ha fatto cosa (se c'è Git)
→ Impact assessment di ogni cambiamento
```

---

## 📤 Export & Sharing

### Export Specific Domain
```
/export-domain [dominio] as [format]
→ Formati: PDF, HTML, Markdown, Notion

Es: /export-domain "Agenzia" as PDF
→ Mi genera un PDF belle con tutte le pagine dell'agenzia
→ Puoi condividere con il team o con clienti
```

### Generate Presentation
```
/generate-presentation [topic]
→ Creo una presentazione Obsidian (o esporta HTML)
→ Basata su tutte le pagine rilevanti
→ Pronta per raccontare la storia

Es: /generate-presentation "Growth Strategy 2026"
→ Automaticamente compone slide da fonti rilevanti
```

### Create Summary Document
```
/create-summary [topic] length=[short/medium/long]
→ Io creo un documento riassuntivo su UN topic
→ Riassume tutto quello che sappiamo senza essere una pagina wiki

Es: /create-summary "Info Products Strategy" length=medium
→ Documento scaricabile, shareable, perfetto per onboarding nuovo team member
```

---

## 🤝 Integration with Claude Code Workflow

### Context Injection
```
Tutte le mie risposte in questa conversazione caricheranno automaticamente
il contesto dalla wiki.

Quando parli di un progetto, io:
1. Carico il progetto dalla wiki
2. Carico i concetti correlati
3. Carico i learnings precedenti
4. Carico le metriche

Così le mie risposte sono sempre consapevoli di Digital Empire.
```

### Decision Documentation
```
Quando facciamo una decision importante in chat:

Tu: "Abbiamo deciso di lanciare il corso sul AI Copywriting"

Io:
1. Creo [[Project: AI Copywriting Course]]
2. Aggiorna [[Project: Lancio Strategico 2026]]
3. Creo [[Decision: Why AI Copywriting (not X)]]
4. Collego a [[Concept: Funnel info products]]

Così ogni decision rimane tracciata e interconnessa.
```

### Auto-Research Integration
```
Quando mi chiedi di fare ricerca:

Tu: "Rierca i trend attuali in AI for Marketing"

Io:
1. Faccio /research-topic "AI for Marketing trends"
2. Aggiungo fonti a [[Source: ...]]
3. Compilo insights in [[Concept: ...]]
4. Creo [[Synthesis: ...]] che connette a quello che già sappiamo
5. Ti segnalo "Ho aggiunto XXX pagine, guarda qui"
```

---

## ⚙️ Performance & Optimization

### For Large Wikis (500+ pages)
```
Se la wiki diventa enorme:
- Puoi splittare in "sub-vaults" per dominio
- Puoi archiviare pagine vecchie
- Puoi usare "Vault Switcher" in Obsidian

Io rimango consapevole di tutta la struttura
anche se è splittata.
```

### Caching & Search Optimization
```
Obsidian cache locale le ricerche.
Ma se vuoi ultra-velocità:
- Usiamo qmd (ripgrep-based search)
- O Khoj per semantic search su tutta la wiki
```

---

## 🧬 Evolutionary Patterns

### Quarterly Architecture Review
```
Ogni trimestre, facciamo:
/review-architecture
→ Io analizzo la struttura della wiki
→ Identifica se servono nuove categorie
→ Suggerisce refactoring
→ Mappa la densità del grafo

Poi decidi se fare cambiamenti strutturali.
```

### Concept Evolution
```
Quando un concetto che hai imparato evolve:
Tu: "So che il funnel sales che avevamo è vecchio, aggiornalo"

Io:
1. Creo una versione 2.0 del concetto
2. Archivio la vecchia
3. Aggiorno tutte le pagine che la referenziavano
4. Creo [[Synthesis: Evolution of Funnel Sales concept]]

La wiki rimane viva.
```

---

## 🎓 Teaching & Onboarding

### Generate Onboarding Document
```
/generate-onboarding [persona]
→ Creo un documento per una nuova persona nel team

Es: /generate-onboarding "New Developer"
→ Documenti su: Come funziona DE, Tech stack, Projects attivi
→ Estratto dalla wiki, personalizzato per il loro ruolo
```

### Create Learning Path
```
/create-learning-path [topic]
→ Io creo un percorso didattico lineare su un argomento
→ Parte dai concetti base
→ Scala verso argomenti avanzati
→ Collega alle applicazioni in DE

Es: /create-learning-path "Info Product Strategy"
→ Leggi [[Concept: Funnel]], poi [[Project: SkillBeast]], 
   poi [[Synthesis: Comparing all our courses]]
```

---

## 🔮 Future: AI-Native Operations (v2.0+)

Cose che aggiungeremo quando la wiki sarà stabile:

- **Predictive Analysis**: Predire quale progetto avrà successo basandosi sui pattern
- **Recommendation Engine**: Suggerire azioni basate su dati storici
- **Autonomous Synthesis**: Io genero synthesis senza che tu le chieda
- **Competitor Intelligence Loop**: Automazione per tracciare competitor e aggiornare wiki
- **Custom LLM Fine-tuning**: Fine-tune un modello specificamente su Digital Empire

---

## 📍 Quando Usare Cosa

| Operazione | Quando | Frequenza |
|---|---|---|
| `/lint-wiki` | Pulire la wiki | Settimanale |
| `/synthesize-domains` | Trovare pattern | Bi-settimanale |
| `/research-topic` | Approfondire | Al bisogno |
| `/generate-weekly-report` | Update | Settimanale |
| `/review-architecture` | Rivedere struttura | Trimestrale |
| `/find-contradictions` | Verificare coerenza | Mensile |
| `/mine-patterns` | Scoprire ricorrenze | Mensile |

---

**Versione**: 1.0 (Draft)  
**Maturità**: Pronto per uso dopo primo mese di wiki  
**Aggiornamento**: Via via che lo usiamo, aggiorniamo questa lista
