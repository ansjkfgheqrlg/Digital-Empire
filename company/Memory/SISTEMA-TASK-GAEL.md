# 🎯 SISTEMA TASK GAEL — Diviso per Categorie

> **Comando Trigger:** `iniziamo con [categoria]`
> **Categorie attive:** YouTube, Instagram, Lancio
> **Aggiornato:** 2026-07-19

---

## 📋 STRUTTURA GENERALE

### Ruolo Gael
- ✅ Creazione **TUTTI i workflow**
- ✅ Creazione **TUTTE le skill**
- ✅ Logica generale di collegamento
- ✅ Ecosistema che collega il modello di business
- ✅ Logica della memoria (ecosistema memory, checkpoint, risoluzione)
- ✅ Ogni singolo dettaglio
- ✅ Pulire logica di planning, brainstorming, architettura, struttura specifica
- ✅ Costruire OGNI singolo agente, workflow, automazione per il modello target

### Categorie Operative

| Categoria | Owner | Status | Comando Trigger |
|---|---|---|---|
| **YouTube** | Gael | 🟢 PRONTO | `iniziamo con Youtube` |
| **Instagram** | Gael | 🟡 Da iniziare | `iniziamo con Instagram` |
| **Lancio** | Gael | 🟡 Da iniziare | `iniziamo con Lancio` |

---

## 🎬 CATEGORIA: YOUTUBE

### 🎯 Obiettivo
Costruire l'intero ecosistema YouTube per Digital Empire: automazione completa dalla ricerca competitor alla pubblicazione, con memoria integrata e collegamento al modello di business.

### 🏗️ Architettura Sistema YouTube

```
YouTube Ecosystem
├── 📊 Research & Analysis
│   ├── Competitor Intelligence
│   ├── Trend Detection
│   ├── Keyword Research
│   └── Audience Analysis
│
├── 🎥 Content Production Pipeline
│   ├── Script Generation
│   ├── Video Creation (Fliki API)
│   ├── Thumbnail Generation
│   ├── SEO Optimization
│   └── Quality Assurance
│
├── 📤 Publishing & Distribution
│   ├── YouTube Upload
│   ├── Description & Tags
│   ├── Playlist Management
│   └── Community Posts
│
├── 📈 Analytics & Optimization
│   ├── Performance Tracking
│   ├── A/B Testing
│   ├── Audience Retention
│   └── Revenue Optimization
│
├── 🧠 Memory System
│   ├── Checkpoints (CP)
│   ├── Decisions (ADR)
│   ├── Sessions
│   ├── Plans
│   └── Knowledge Graph
│
└── 🔗 Business Integration
    ├── Lead Generation
    ├── Course Funnel (Claude Code)
    ├── Product Promotion
    └── Cross-platform Sync
```

### 🤖 Agenti Necessari (YouTube)

#### L1 - Orchestrator
1. **youtube-conductor** - Orchestratore principale
2. **youtube-planner** - Pianificazione contenuti
3. **youtube-qa-supervisor** - Supervisore qualità

#### L2 - Research & Analysis
4. **yt-competitor-scout** - Ricerca competitor
5. **yt-trend-analyzer** - Analisi trend
6. **yt-keyword-researcher** - Ricerca keyword
7. **yt-audience-analyst** - Analisi audience

#### L3 - Content Production
8. **yt-script-writer** - Scrittura script
9. **yt-script-optimizer** - Ottimizzazione script
10. **yt-video-generator** - Generazione video (Fliki)
11. **yt-thumbnail-creator** - Creazione thumbnail
12. **yt-seo-optimizer** - Ottimizzazione SEO
13. **yt-title-generator** - Generazione titoli
14. **yt-description-writer** - Scrittura descrizioni

#### L4 - Publishing & Distribution
15. **yt-publisher** - Pubblicazione YouTube
16. **yt-playlist-manager** - Gestione playlist
17. **yt-community-poster** - Post community

#### L5 - Analytics & Optimization
18. **yt-analytics-tracker** - Tracking analytics
19. **yt-ab-tester** - A/B testing
20. **yt-revenue-optimizer** - Ottimizzazione revenue

#### L6 - Memory & Integration
21. **yt-memory-manager** - Gestione memoria YouTube
22. **yt-business-integrator** - Integrazione business
23. **yt-funnel-connector** - Connessione funnel Claude Code

### 🔄 Workflow Necessari (YouTube)

#### WF-YT-RESEARCH
1. **Competitor Analysis**
   - Input: nicchia, keyword
   - Process: ricerca competitor, analisi video top
   - Output: report competitor, trend, opportunità

2. **Trend Detection**
   - Input: nicchia
   - Process: analisi trend, keyword research
   - Output: lista trend, keyword, volumi

3. **Content Gap Analysis**
   - Input: competitor, trend
   - Process: identificazione gap
   - Output: opportunità contenuti

#### WF-YT-PRODUCTION
4. **Script Generation**
   - Input: topic, keyword, competitor analysis
   - Process: generazione script, ottimizzazione hook/CTA
   - Output: script completo

5. **Video Creation**
   - Input: script
   - Process: Fliki API, generazione video, thumbnail
   - Output: video MP4, thumbnail PNG

6. **SEO Optimization**
   - Input: video, script, keyword
   - Process: ottimizzazione titolo, descrizione, tags
   - Output: metadata SEO-ready

7. **Quality Assurance**
   - Input: video, script, metadata
   - Process: check qualità, brand compliance, SEO
   - Output: report QA, approvazione/rifiuto

#### WF-YT-PUBLISHING
8. **YouTube Upload**
   - Input: video, metadata
   - Process: upload YouTube, setup metadata
   - Output: video pubblicato

9. **Playlist Management**
   - Input: video, playlist
   - Process: aggiunta a playlist, organizzazione
   - Output: video in playlist

10. **Community Post**
    - Input: video
    - Process: creazione post community
    - Output: post pubblicato

#### WF-YT-OPTIMIZATION
11. **Performance Analysis**
    - Input: video URL
    - Process: analisi views, retention, engagement
    - Output: report performance

12. **A/B Testing**
    - Input: video, varianti thumbnail/titolo
    - Process: test varianti, analisi risultati
    - Output: vincitore, raccomandazioni

13. **Revenue Optimization**
    - Input: performance data
    - Process: analisi revenue, ottimizzazione
    - Output: piano ottimizzazione

#### WF-YT-MEMORY
14. **Checkpoint Creation**
    - Input: azione completata
    - Process: creazione CP, update INDEX
    - Output: checkpoint salvato

15. **Decision Recording**
    - Input: decisione presa
    - Process: creazione ADR, motivazione
    - Output: decision record

16. **Session Handoff**
    - Input: fine sessione
    - Process: creazione handoff, summary
    - Output: handoff document

17. **Knowledge Graph Update**
    - Input: nuovo knowledge
    - Process: update KG, collegamenti
    - Output: KG aggiornato

### 🧠 Sistema Memoria YouTube

```
memory/youtube/
├── checkpoints/
│   ├── CP-001-competitor-analysis.md
│   ├── CP-002-script-generated.md
│   └── ...
├── decisions/
│   ├── DEC-001-nicchie-scelte.md
│   ├── DEC-002-fliki-config.md
│   └── ...
├── sessions/
│   ├── SES-001-setup-youtube.md
│   ├── SES-002-primo-video.md
│   └── ...
├── plans/
│   ├── PLAN-v1-youtube-ecosystem.md
│   ├── PLAN-v2-content-calendar.md
│   └── ...
├── architectures/
│   ├── ARCH-001-youtube-pipeline.md
│   └── ...
├── knowledge/
│   ├── competitors/
│   ├── trends/
│   ├── best-practices/
│   └── analytics/
├── state/
│   ├── youtube-state.json
│   └── channel-state.json
└── MEMORY-INDEX.md
```

### 📅 Piano Implementazione YouTube

#### Fase 1: Fondamenta (G2-G3)
**Obiettivo:** Setup infrastruttura + primo video test

- [ ] **WF-YT-RESEARCH**: Creare agenti research (4)
- [ ] **Fliki API**: Configurare API, test generazione
- [ ] **YouTube API**: Setup OAuth, test upload
- [ ] **Memory System**: Setup memory/youtube/ structure
- [ ] **Primo Video Test**: End-to-end test (ricerca → pubblicazione)

#### Fase 2: Pipeline Completa (G4-G5)
**Obiettivo:** Pipeline produzione completa operativa

- [ ] **WF-YT-PRODUCTION**: Creare agenti production (7)
- [ ] **Script Generation**: Workflow completo script
- [ ] **Video Creation**: Workflow completo video (Fliki)
- [ ] **SEO Optimization**: Workflow completo SEO
- [ ] **Quality Assurance**: Workflow completo QA
- [ ] **Test Pipeline**: Test end-to-end 5 video

#### Fase 3: Publishing & Analytics (G6-G7)
**Obiettivo:** Pubblicazione automatica + analytics

- [ ] **WF-YT-PUBLISHING**: Creare agenti publishing (3)
- [ ] **YouTube Upload**: Automazione upload completo
- [ ] **Playlist Management**: Automazione playlist
- [ ] **WF-YT-OPTIMIZATION**: Creare agenti optimization (3)
- [ ] **Analytics Tracking**: Setup tracking completo
- [ ] **A/B Testing**: Setup test thumbnail/titoli

#### Fase 4: Business Integration (G8-G10)
**Obiettivo:** Integrazione con modello di business

- [ ] **WF-YT-MEMORY**: Creare agenti memory (3)
- [ ] **Memory System**: Implementazione completa
- [ ] **Business Integration**: Collegamento funnel Claude Code
- [ ] **Lead Generation**: Setup lead gen dai video
- [ ] **Cross-platform Sync**: Sync con Instagram/Lancio

#### Fase 5: Scaling & Optimization (G11-G14)
**Obiettivo:** Scalare a produzione

- [ ] **Content Calendar**: Piano contenuti mensile
- [ ] **Batch Production**: Produzione batch 10 video
- [ ] **Performance Optimization**: Ottimizzazione basata su dati
- [ ] **Revenue Tracking**: Tracking revenue YouTube
- [ ] **Documentation**: Documentazione completa workflow

### 🎯 Task Operativi Iniziali (Comando: `iniziamo con Youtube`)

#### STEP 1: Setup Infrastruttura (2 ore)

1. **Setup Memory System**
   ```bash
   mkdir -p memory/youtube/{checkpoints,decisions,sessions,plans,architectures,knowledge,state}
   ```
   - Creare struttura memory/youtube/
   - Inizializzare MEMORY-INDEX.md
   - Setup state files

2. **Setup Fliki API**
   - Verificare chiave API Fliki (in .env)
   - Test chiamata API (1 video test)
   - Documentare limiti/rate limits

3. **Setup YouTube API**
   - Verificare OAuth setup
   - Test upload video (1 video test)
   - Documentare scopes necessari

4. **Setup Workspace**
   ```bash
   mkdir -p SKILL\ &\ Agenti/YouTube/{agents,workflows,scripts,tests}
   ```
   - Creare struttura progetto YouTube
   - Setup agents/ directory
   - Setup workflows/ directory
   - Setup scripts/ directory

5. **Checkpoint**
   - Creare CP-001-setup-infrastruttura.md
   - Aggiornare MEMORY-INDEX.md
   - Push GitHub

#### STEP 2: Creazione Agenti Research (3 ore)

6. **yt-competitor-scout** (7 file canonici)
   ```
   agents/youtube/research/yt-competitor-scout/
   ├── spec.md
   ├── system-prompt.md
   ├── tools.md
   ├── playbook.md
   ├── evals.md
   ├── failure-modes.md
   └── memory.md
   ```
   - Specifica: ricerca competitor YouTube
   - Tools: YouTube Data API, web scraping
   - Output: report competitor analysis

7. **yt-trend-analyzer** (7 file canonici)
   - Specifica: analisi trend YouTube
   - Tools: Google Trends API, YouTube Analytics
   - Output: report trend + opportunità

8. **yt-keyword-researcher** (7 file canonici)
   - Specifica: ricerca keyword YouTube
   - Tools: YouTube Suggest API, Keyword Planner
   - Output: lista keyword + volumi

9. **yt-audience-analyst** (7 file canonici)
   - Specifica: analisi audience
   - Tools: YouTube Analytics, social listening
   - Output: report audience + preferenze

10. **Checkpoint**
    - Creare CP-002-agenti-research.md
    - Test agenti (1 ricerca completa)
    - Aggiornare MEMORY-INDEX.md
    - Push GitHub

#### STEP 3: Primo Video Test (3 ore)

11. **E2E Test: Research**
    - Lanciare yt-competitor-scout su nicchia "Claude Code"
    - Lanciare yt-trend-analyzer su "AI coding"
    - Lanciare yt-keyword-researcher su "Claude tutorial"
    - Risultato: report research completo

12. **E2E Test: Script (manuale per ora)**
    - Basandosi su report research
    - Scrivere script 10 minuti
    - Ottimizzare hook + CTA
    - Risultato: script pronto

13. **E2E Test: Video (Fliki)**
    - Inviare script a Fliki API
    - Generare video MP4
    - Generare thumbnail PNG
    - Risultato: video + thumbnail pronti

14. **E2E Test: SEO (manuale per ora)**
    - Creare titolo ottimizzato
    - Scrivere descrizione con keyword
    - Selezionare tags (500 chars)
    - Risultato: metadata SEO pronti

15. **E2E Test: Upload (YouTube API)**
    - Upload video su YouTube
    - Setup metadata (titolo, descrizione, tags)
    - Setup thumbnail
    - Risultato: video pubblicato

16. **Checkpoint**
    - Creare CP-003-primo-video-test.md
    - Documentare processo completo
    - Identificare gap/automazioni necessarie
    - Aggiornare MEMORY-INDEX.md
    - Push GitHub

#### STEP 4: Analisi & Planning (1 ora)

17. **Analisi Primo Video**
    - Cosa ha funzionato?
    - Cosa non ha funzionato?
    - Gap identificati?
    - Automazioni necessarie?

18. **Planning Pipeline Completa**
    - Quali agenti creare dopo?
    - Quali workflow automatizzare?
    - Priorità prossimi step?
    - Stima tempo completamento?

19. **Checkpoint**
    - Creare CP-004-analisi-planning.md
    - Creare PLAN-v2-youtube-pipeline.md
    - Aggiornare MEMORY-INDEX.md
    - Push GitHub

### 📊 Metriche Successo YouTube

| Metrica | Target Fase 1 | Target Fase 2 | Target Fase 3 |
|---|---|---|---|
| **Video prodotti** | 1 test | 10 | 30 |
| **Tempo produzione** | 4 ore | 2 ore | 1 ora |
| **Automazione %** | 20% | 60% | 90% |
| **Views per video** | — | 100+ | 500+ |
| **Watch time** | — | 40%+ | 50%+ |
| **Lead gen** | — | 5 | 20 |

### 🔗 Connessioni Business

```
YouTube → Lead Generation → Funnel Claude Code → Vendita Corso/Libro
YouTube → Brand Awareness → Instagram Cross-promo → Community
YouTube → Content Repurpose → Instagram Caroselli → Engagement
```

### ⚠️ Regole Operative YouTube

1. **Memory-first:** OGNI azione crea CP/DEC/SES
2. **Test-driven:** OGNI agente testato prima di produzione
3. **Incrementale:** Costruire un pezzo alla volta, testare, poi prossimo
4. **Documentare:** OGNI workflow documentato con input/output/process
5. **Collegare:** OGNI video collegato a funnel business
6. **Ottimizzare:** Basare decisioni su dati, non opinioni
7. **Scalare:** Automatizzare solo dopo aver validato manualmente
8. **Monitorare:** Tracking metriche OGNI settimana

---

## 📸 CATEGORIA: INSTAGRAM

> **Status:** 🟡 Da iniziare
> **Comando:** `iniziamo con Instagram`

### Struttura (da definire)
- Pagine: mentalita.brutale, crea.illtuo_impero, altre
- Agenti: content-creator, carousel-generator, scheduler, analytics
- Workflow: content-calendar, carousel-production, publishing, analytics
- Integration: cross-promo YouTube, funnel Claude Code

---

## 🚀 CATEGORIA: LANCI0

> **Status:** 🟡 Da iniziare
> **Comando:** `iniziamo con Lancio`

### Struttura (da definire)
- Obiettivo: Lancio corso Claude Code + libro
- Agenti: launch-manager, funnel-builder, email-marketer, ads-manager
- Workflow: pre-launch, launch-week, post-launch, optimization
- Integration: YouTube promo, Instagram promo, email sequence, ads

---

## 🎯 COMANDI DISPONIBILI

```bash
# Iniziare categoria
iniziamo con Youtube      # Setup ecosistema YouTube
iniziamo con Instagram    # Setup ecosistema Instagram
iniziamo con Lancio       # Setup lancio corso/libro

# Status
status Youtube           # Status categoria YouTube
status Instagram         # Status categoria Instagram
status Lancio            # Status categoria Lancio

# Progress
progress Youtube         # Progresso YouTube (checkpoints, agenti, workflow)
progress Instagram       # Progresso Instagram
progress Lancio          # Progresso Lancio

# Memory
memory Youtube           # Ultimi checkpoint/decisioni YouTube
memory Instagram         # Ultimi checkpoint/decisioni Instagram
memory Lancio            # Ultimi checkpoint/decisioni Lancio
```

---

## 📋 RIEPILOGO

**Comando trigger per Gael:** `iniziamo con Youtube`

**Cosa farà Gael:**
1. Setup infrastruttura (memory, API, workspace)
2. Creazione agenti research (4 agenti × 7 file)
3. Primo video test end-to-end
4. Analisi & planning pipeline completa
5. Continuazione con fasi 2-5 (production, publishing, integration, scaling)

**Principi:**
- Memory-first (P10)
- Test-driven
- Incrementale
- Documentare tutto
- Collegare al business
- Basare su dati
- Automatizzare dopo validazione
- Monitorare metriche

**Output atteso:** Ecosistema YouTube completo, operativo, integrato con modello di business.

---

*Documento creato: 2026-07-19*
*Owner: Gael*
*Supervisione: Max*
