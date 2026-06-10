# STRATEGY-REGISTRY.md — Libreria di Strategie Multiple (Non una sola strategia generica)

**Filosofia**: Non esiste "la" strategia. Esistono **molte strategie** specializzate, attivate in base a contesto, dipartimento, tipo di contenuto, tipo di output sulla wiki, ecc. Questo registro elenca, descrive e versiona tutte le strategie.

Ogni strategia deve essere:
- Specifica (non generica)
- Architettata (con fasi, decision tree, regole, handoff)
- Performante (ottimizzata per velocità/qualità/coverage)
- Versionata e tracciata in memory/strategy-versions/
- Applicata, controllata e migliorata da agenti dedicati del Strategy Department

## 1. Strategie per Dipartimento (Environment / Reparto)

### 1.1 YouTube Department Strategy
- **Trigger**: Input è link canale o video YouTube.
- **Focus primario**: Video lunghi (spesso 30min-3h), capitoli chiari, demo visive forti, tutorial strutturati.
- **Fasi specifiche**:
  1. Screening avanzato (titolo + description + tags + views + capitoli).
  2. Ingestion con yt-dlp esteso (auto-subs multi-lingua, info.json completa).
  3. "Guardare" obbligatorio con frame densi su capitoli + mid-points.
  4. Estrazione forte di "passaggi mostrati" (UI, click, risultati visivi).
  5. Wiki implementation: Note atomiche + MOC per "YouTube Knowledge Pack" + trace forte a timestamp + frame.
- **Wiki Implementation Style**: "Tutorial Deep Dive" — sezioni dettagliate per fase, esempi visivi referenziati, practical steps numerati.
- **Performance rules**: Max 20 video per run se non filtrati; parallelizzazione su video indipendenti.
- **Version**: v1.0 (2026-06-07)

### 1.2 TikTok Department Strategy
- **Trigger**: Input TikTok.
- **Focus primario**: Video brevi, demo rapide, hook visivi forti, trend/pratici.
- **Fasi specifiche**:
  1. Ingestion yt-dlp (TikTok support).
  2. "Guardare" con frame molto densi (ogni 5-10 secondi o key moments).
  3. Estrazione di "micro-passaggi" e hook visivi.
  4. Wiki: Note molto atomiche e "quick-win" + link a video brevi.
- **Wiki Implementation Style**: "Micro-Tutorial / Quick Reference" — bullet point pesanti, GIF-like description, "fai questo in 30 secondi".
- **Version**: v1.0

### 1.3 Web Department Strategy
- **Trigger**: Siti web, ricerche avanzate, articoli, documentazione.
- **Focus**: Testo denso, meno visual, ma possibile scraping di screenshot di UI.
- **Fasi specifiche**:
  1. Playwright per crawl avanzato (no API).
  2. Estrazione strutturata + screenshot di sezioni chiave.
  3. Meno enfasi su "frame temporali", più su "sezioni/pagine".
- **Wiki Implementation Style**: "Reference / Knowledge Base" — gerarchia MOC + pagine atomiche con trace a URL + screenshot.
- **Version**: v1.0

## 2. Strategie per Tipo di Contenuto

### 2.1 Marketing Content Strategy
- Focus: Funnel, copy, ads, positioning, case studies.
- Wiki style: "Playbook Marketing" con sezioni "Framework", "Esempi", "Metriche da misurare".
- Applicazione: Forte emphasis su "come replicare" + esempi visivi da video.

### 2.2 Design System / Tool Creation Strategy (es. video 2h design system)
- Focus: Passaggi visivi di creazione UI, export, tokens, components.
- "Guardare" obbligatorio con frame su ogni passaggio di tool (Figma, ecc.).
- Wiki style: "Step-by-Step Visual Guide" + "Token Export Process" + "Component Library Structure".
- Output speciale: Proposta di update per workflow di creazione skills/design.

### 2.3 Tutorial Pratici / Skills & Automazioni Strategy
- Focus: Tool usage, creazione di skills, automazioni, CLI, integrazioni.
- Wiki style: "How-to + Gotchas" + comandi esatti + screenshot di output.
- Forte link a "come aggiornare flussi esistenti".

### 2.4 Theoretical / Framework Strategy
- Focus: Concetti, principi, modelli mentali.
- Wiki style: "Concept Map" + "Principle → Application" + riferimenti incrociati.

## 3. Strategie di Implementazione sulla Wiki

### 3.1 Atomic Notes + MOC (default per la maggior parte)
- Ogni atomo di conoscenza = nota separata.
- MOC (Map of Content) per collegare.

### 3.2 Playbook Style
- Per contenuti operativi (marketing, automazioni): struttura "When to use / How to / Examples / Pitfalls".

### 3.3 Visual-Heavy Reference
- Per design system, tool demo: molte reference a frame/PNG + descrizioni visive.

### 3.4 Update-Proposal Integrated
- Ogni ingest rilevante genera automaticamente sezione "Suggested Updates to Existing Workflows" nella wiki.

## 4. Strategie Esterne / Indipendenti
- Strategia per "Update di flussi esistenti" (cross-ecosystem improvement).
- Strategia di Self-Improvement dell'ecosistema stesso (meta).
- Strategia di "Knowledge Propagation" (come la nuova conoscenza si diffonde in memory e in altri reparti).

## 5. Come si Seleziona e Applica una Strategia

**Decision Tree (gestito dal Strategy Coordinator Agent)**:
1. Analizza input type (YouTube / TikTok / Web / Mixed).
2. Analizza focus dichiarato o dedotto (marketing, design, automation, general).
3. Seleziona combinazione: Dipartimento Strategy + Content-Type Strategy + Wiki-Implementation Strategy.
4. Crea "Strategy Manifest" per il run corrente (salvato in memory/strategy-applications/).
5. Passa il manifest ai team L2/L3.
6. Strategy Controller verifica che venga seguita.
7. Strategy Improver analizza post-run (via memory) e propone miglioramenti alla strategia usata.

Ogni applicazione di strategia viene loggata in memory/strategy-applications/ con:
- Quale combinazione di strategie è stata scelta
- Perché
- Come è stata applicata
- Risultato (coverage, qualità visuale, update generati)
- Feedback dal Verification Team

## 6. Versioning e Miglioramento

- Tutte le strategie sono versionate (v1.0, v1.1...).
- Le versioni vivono in /home/user/content-ingest-ecosystem/strategies/ + memory/strategy-versions/.
- Il Meta-Strategy Manager + Strategy Improver sono responsabili di proporre nuove versioni basate su run reali e memory.

**Trace (P12)**: Questo registro è stato creato per rispondere alla tua critica che la strategia era "troppo generica" e alla richiesta di "tante strategie per ogni singolo tipo di funzionalità, per l'ambiente (reparto Youtube, TikTok, web), per diversi tipi di contenuti, diversi tipi di implementazione sulla wiki".

La strategia ora è multipla, specifica, architettata e gestita da un team di agenti dedicato.
