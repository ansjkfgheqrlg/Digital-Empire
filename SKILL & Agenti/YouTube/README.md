# 🎬 YouTube Ecosystem — Digital Empire

> **Owner:** Gael
> **Status:** 🟡 Setup iniziale
> **Comando Trigger:** `iniziamo con Youtube`

---

## 🎯 Obiettivo

Costruire l'intero ecosistema YouTube per Digital Empire: automazione completa dalla ricerca competitor alla pubblicazione, con memoria integrata e collegamento al modello di business.

---

## 📚 Documentazione

### Punto di Partenza
1. **Leggi:** `company/Memory/SISTEMA-TASK-GAEL.md` (sezione YouTube)
2. **Leggi:** `memory/youtube/MEMORY-INDEX.md`
3. **Leggi:** `company/Memory/checkpoints/CP-20260719-004.md`

### Comando per Iniziare
```
iniziamo con Youtube
```

Questo comando avvia il piano operativo completo per YouTube.

---

## 🏗️ Architettura

### Livelli Ecosistema

```
YouTube Ecosystem
├── 🎯 Orchestrator (3 agenti)
│   ├── youtube-conductor
│   ├── youtube-planner
│   └── youtube-qa-supervisor
│
├── 📊 Research & Analysis (4 agenti)
│   ├── yt-competitor-scout
│   ├── yt-trend-analyzer
│   ├── yt-keyword-researcher
│   └── yt-audience-analyst
│
├── 🎥 Content Production (7 agenti)
│   ├── yt-script-writer
│   ├── yt-script-optimizer
│   ├── yt-video-generator
│   ├── yt-thumbnail-creator
│   ├── yt-seo-optimizer
│   ├── yt-title-generator
│   └── yt-description-writer
│
├── 📤 Publishing & Distribution (3 agenti)
│   ├── yt-publisher
│   ├── yt-playlist-manager
│   └── yt-community-poster
│
├── 📈 Analytics & Optimization (3 agenti)
│   ├── yt-analytics-tracker
│   ├── yt-ab-tester
│   └── yt-revenue-optimizer
│
└── 🧠 Memory & Integration (3 agenti)
    ├── yt-memory-manager
    ├── yt-business-integrator
    └── yt-funnel-connector
```

**Totale:** 23 agenti × 7 file canonici = 161 file

---

## 🔄 Workflow

### WF-YT-RESEARCH (3 workflow)
1. Competitor Analysis
2. Trend Detection
3. Content Gap Analysis

### WF-YT-PRODUCTION (4 workflow)
4. Script Generation
5. Video Creation (Fliki API)
6. SEO Optimization
7. Quality Assurance

### WF-YT-PUBLISHING (3 workflow)
8. YouTube Upload
9. Playlist Management
10. Community Post

### WF-YT-OPTIMIZATION (3 workflow)
11. Performance Analysis
12. A/B Testing
13. Revenue Optimization

### WF-YT-MEMORY (4 workflow)
14. Checkpoint Creation
15. Decision Recording
16. Session Handoff
17. Knowledge Graph Update

**Totale:** 17 workflow

---

## 📅 Piano Implementazione

### Fase 1: Fondamenta (G2-G3)
**Obiettivo:** Setup infrastruttura + primo video test

- [ ] Setup API (Fliki, YouTube)
- [ ] Creazione agenti research (4)
- [ ] Primo video test end-to-end
- [ ] Memoria YouTube operativa

**Tempo:** 2 giorni

### Fase 2: Pipeline Completa (G4-G5)
**Obiettivo:** Pipeline produzione completa operativa

- [ ] Creazione agenti production (7)
- [ ] Workflow completi (script, video, SEO, QA)
- [ ] Test pipeline 5 video

**Tempo:** 2 giorni

### Fase 3: Publishing & Analytics (G6-G7)
**Obiettivo:** Pubblicazione automatica + analytics

- [ ] Creazione agenti publishing (3)
- [ ] Creazione agenti optimization (3)
- [ ] Automazione upload + tracking
- [ ] A/B testing thumbnail/titoli

**Tempo:** 2 giorni

### Fase 4: Business Integration (G8-G10)
**Obiettivo:** Integrazione con modello di business

- [ ] Creazione agenti memory (3)
- [ ] Collegamento funnel Claude Code
- [ ] Lead generation dai video
- [ ] Cross-platform sync

**Tempo:** 3 giorni

### Fase 5: Scaling & Optimization (G11-G14)
**Obiettivo:** Scalare a produzione

- [ ] Content calendar mensile
- [ ] Batch production 10 video
- [ ] Ottimizzazione basata su dati
- [ ] Revenue tracking

**Tempo:** 4 giorni

**Tempo totale:** 13 giorni (2.5 settimane)

---

## 🚀 Task Operativi Iniziali

### STEP 1: Setup Infrastruttura (2 ore)

1. **Setup Memory System** ✅ (già fatto)
   - Struttura `memory/youtube/` creata
   - MEMORY-INDEX.md inizializzato
   - State file creato

2. **Setup Fliki API**
   - Verificare chiave API Fliki (in `.env`)
   - Test chiamata API (1 video test)
   - Documentare limiti/rate limits
   - CP: CP-001-fliki-setup.md

3. **Setup YouTube API**
   - Verificare OAuth setup
   - Test upload video (1 video test)
   - Documentare scopes necessari
   - CP: CP-002-youtube-setup.md

4. **Setup Workspace** ✅ (già fatto)
   - Struttura `SKILL & Agenti/YouTube/` creata
   - Directory agents/, workflows/, scripts/, tests/

5. **Checkpoint**
   - CP-001-setup-infrastruttura.md
   - Aggiornare MEMORY-INDEX.md
   - Push GitHub

### STEP 2: Creazione Agenti Research (3 ore)

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
    - CP-002-agenti-research.md
    - Test agenti (1 ricerca completa)
    - Aggiornare MEMORY-INDEX.md
    - Push GitHub

### STEP 3: Primo Video Test (3 ore)

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
    - CP-003-primo-video-test.md
    - Documentare processo completo
    - Identificare gap/automazioni necessarie
    - Aggiornare MEMORY-INDEX.md
    - Push GitHub

### STEP 4: Analisi & Planning (1 ora)

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
    - CP-004-analisi-planning.md
    - Creare PLAN-v2-youtube-pipeline.md
    - Aggiornare MEMORY-INDEX.md
    - Push GitHub

**Tempo totale STEP 1-4:** 9 ore (1 giornata intensa)

---

## 📊 Metriche Successo

| Metrica | Target Fase 1 | Target Fase 2 | Target Fase 3 |
|---|---|---|---|
| **Video prodotti** | 1 test | 10 | 30 |
| **Tempo produzione** | 4 ore | 2 ore | 1 ora |
| **Automazione %** | 20% | 60% | 90% |
| **Views per video** | — | 100+ | 500+ |
| **Watch time** | — | 40%+ | 50%+ |
| **Lead gen** | — | 5 | 20 |

---

## 🔗 Connessioni Business

```
YouTube → Lead Generation → Funnel Claude Code → Vendita Corso/Libro
YouTube → Brand Awareness → Instagram Cross-promo → Community
YouTube → Content Repurpose → Instagram Caroselli → Engagement
```

---

## ⚠️ Regole Operative

1. **Memory-first:** OGNI azione crea CP/DEC/SES
2. **Test-driven:** OGNI agente testato prima di produzione
3. **Incrementale:** Costruire un pezzo alla volta, testare, poi prossimo
4. **Documentare:** OGNI workflow documentato con input/output/process
5. **Collegare:** OGNI video collegato a funnel business
6. **Ottimizzare:** Basare decisioni su dati, non opinioni
7. **Scalare:** Automatizzare solo dopo aver validato manualmente
8. **Monitorare:** Tracking metriche OGNI settimana

---

## 📁 Struttura Directory

```
SKILL & Agenti/YouTube/
├── agents/
│   ├── orchestrator/
│   ├── research/
│   ├── production/
│   ├── publishing/
│   ├── analytics/
│   └── memory/
├── workflows/
│   ├── research/
│   ├── production/
│   ├── publishing/
│   ├── optimization/
│   └── memory/
├── scripts/
├── tests/
└── README.md (questo file)

memory/youtube/
├── checkpoints/
├── decisions/
├── sessions/
├── plans/
├── architectures/
├── knowledge/
│   ├── competitors/
│   ├── trends/
│   ├── best-practices/
│   └── analytics/
├── state/
│   └── youtube-state.json
└── MEMORY-INDEX.md
```

---

## 🎯 Prossimo Step

**Comando:** `iniziamo con Youtube`

**Cosa farà Gael:**
1. Setup infrastruttura (API Fliki + YouTube)
2. Creazione agenti research (4 agenti × 7 file)
3. Primo video test end-to-end
4. Analisi & planning pipeline completa
5. Continuazione con fasi 2-5

**Output atteso:** Ecosistema YouTube completo, operativo, integrato con modello di business.

---

## 📝 Note

- **Principio guida:** Memory-first (P10), test-driven, incrementale
- **Checkpoint:** OGNI step completato → CP + push
- **Memoria:** memory/youtube/ è la fonte di verità
- **Connessioni:** YouTube → Instagram → Lancio (cross-promo)

---

*Creato: 2026-07-19*
*Owner: Gael*
*Supervisione: Max*
*Versione: 1.0*
