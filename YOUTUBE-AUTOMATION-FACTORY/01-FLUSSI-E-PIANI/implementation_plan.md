# Refactoring YouTube Automation into APEX-7

Refactoring the YouTube Automation codebase from `.claude/skills/youtube-automation-factory` into the new workspace `YOUTUBE-AUTOMATION-FACTORY` following the **APEX-7** framework structure. 

The APEX-7 framework introduces a structured, event-driven, memory-connected, quality-gated multi-agent architecture.

---

## 🔎 STATO REALE (audit 2026-07-27, Claude, su richiesta Gael)

**Scaffolding: ✅ costruito e testato.** Tutti e 7 i Plan hanno codice + test dedicato in
`test_youtube_apex7.py` (**11/11 test verdi**), più un E2E reale eseguito (`memory/runs/run_yt-run-20260725-085030.json`,
decisioni loggate per tutti e 6 i gate L1→L7).

**⚠️ Ma il contenuto è simulato in OGNI fase.** Verificato leggendo `apex7_orchestrator.py` riga per
riga: non solo le Fasi 5-6 (già segnalato in CP-20260724-008), **tutte le 6 fasi** scrivono dati
hardcoded invece di usare l'output reale della fase precedente:
- **F1 Scouting**: canale mock "Legami d'amore" con 2 video finti, indice cash-cow 76.5 fisso, verdetto PASS fisso — non legge `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/` (dati REALI di Gemini, pronti da settimane, mai collegati).
- **F2 Selezione**: 2 candidati hardcoded con SEO score finti (45.0 / 85.0).
- **F3 Script**: stesso testo statico ("Vuoi installare l'agente IA più veloce?") indipendentemente dal video scelto in F2.
- **F4 Produzione**: spec Fliki con 1 sola scena fissa.
- **F5 Pubblicazione**: stesso titolo/metadati "Claude Code" ogni volta.
- **F6 Audit**: metriche di performance finte (`views_per_hour: 35.5` fisso) scritte in `performance_logs.json` — il self-improver impara quindi sempre sugli stessi dati falsi.
- **`execute_critic` (il "Critic" che valuta ogni fase)**: ritorna SEMPRE lo stesso punteggio fisso (8.5/8.0/7.5/8.0/9.0) — non valuta realmente nulla.
- **Dashboard** (`run_youtube_apex7.py` → `06-DASHBOARD-E-METRICHE/YOUTUBE-PERFORMANCE-DASHBOARD.md`): scrive sempre la stessa tabella "🟢 PASS" per tutte le 6 fasi, a prescindere dall'esito reale della run.

**I motori di calcolo sotto le fasi sembrano reali** (`seo_score.py`, `cashcow_check.py`,
`thumbnail_analyzer.py`, `validate_schemas.py`, `meta_agent.py`, `self_improve.py` — 85-200 righe
ciascuno, output JSON verificato a runtime nel test suite): il problema non è che calcolano male,
è che **nessuno gli passa mai dati veri**.

**Conclusione:** la fabbrica è un simulatore end-to-end perfettamente funzionante, non ha mai
prodotto un video reale né mai processato una nicchia reale. Stesso pattern identificato in
[[CP-20260724-007]] (7 piani ristrutturazione): "il problema non era la capacità, era l'esecuzione".

### Task aperti, in ordine di priorità (via libera di Gael il 2026-07-27, si parte da F1)
1. ✅ **F1 → dati reali (FATTO 2026-07-27)**: `apex7_orchestrator.py::run_phase_1` ora legge i 20
   canali reali da `WORKFLOW-ESTATE/04-SKILLS-E-REFERENCE/youtube-niche-scout-analysis/01_MAPPA_CANALI.md`
   (nuovo metodo `load_real_niche_channels()`), seleziona il canale con priorità di tier
   "Altissima/Media-Alta opportunità per il Manuale" (dall'analisi di clusterizzazione reale del
   documento) e a parità di tier per viste medie più alte. Il Cash Cow Index si calcola su una
   stima aggregata onestamente dichiarata (view medie low/high del canale reale + età stimata
   dalla frequenza di upload reale — 01_MAPPA_CANALI.md non ha dati singolo-video da Video IQ).
   `scheda-nicchia.md` e il decision log ora riportano il **verdetto reale** (può essere FAIL:
   verificato con un run manuale, canale scelto "Alberto Olla", indice 44.0, sotto soglia 60 →
   niche-gate FAIL — la vecchia versione scriveva sempre "PASS" per costruzione, questa no).
   11/11 test invariati verdi.
   **Aggiornamento 2026-07-27 (stesso giorno, via libera Gael "includilo"): niche-gate ora reale
   e bloccante.** `run_phase_1` prova i candidati in ordine di priorità finché uno non supera
   davvero la soglia 60 (retry automatico, come farebbe un niche-scout umano — non si accontenta
   del primo canale "in target" se le sue viste reali sono troppo basse). Verificato: Alberto Olla
   (44.0), Martes AI (19.7), Piero Savastano (17.3), SOS Automazioni (20.2) scartati in sequenza,
   **Andrea Ciraolo selezionato con indice reale 78.4 (PASS)**. Se TUTTI e 20 i canali reali
   falliscono il gate, `run_phase_1` ora ritorna `False` per davvero (`sys.exit(1)`, "Riprendi con
   --resume") invece di forzare comunque un PASS.
2. ✅ **F2 → dati reali (FATTO 2026-07-27)**: `run_phase_2` ora scarica i video REALI del canale
   scelto in F1 direttamente dalla pagina pubblica `youtube.com/<handle>/videos` (nessuna API key:
   dati già visibili a chiunque la visiti — nuove funzioni `_fetch_channel_videos_live()`,
   `_extract_videos_from_yt_data()` con supporto sia allo schema legacy `videoRenderer` sia al
   nuovo `lockupViewModel`, migrato da YouTube nel 2025-2026 e scoperto empiricamente durante
   l'implementazione). Risultato in cache (`memory/channel_videos/<handle>.json`, TTL 7gg) per
   non dipendere dalla rete a ogni run/test — se il fetch live fallisce ma la cache esiste (anche
   scaduta), la usa con un avviso; se non esiste nessuna cache, la fase fallisce onestamente.
   Video troppo giovani (<24h) scartati dal ranking (velocity views/ora troppo rumorosa). SEO
   score reale calcolato solo sul titolo (unico dato reale disponibile per video di canali terzi:
   niente descrizione/tag inventati) via `seo_score.py`. A-upside = massima velocity reale;
   B-sicurezza = prossimo per velocity con SEO pari/superiore. Verificato su Andrea Ciraolo (26
   video reali): candidati e punteggi cambiano ad ogni fetch perché i dati sono vivi, non fissi.
   11/11 test invariati verdi (usano la cache committata, zero chiamate di rete nei test).
3. **F3 → script reale**: invocare l'agente `operatori/script-writer.md` sul video/nicchia reale, non scrivere sempre lo stesso testo.
4. **F4 → produzione reale**: generare la spec Fliki dallo script reale di F3 (scene multiple, non 1 fissa).
5. **F5 → metadati/SEO reali**: titolo/tag/keyword dal video reale scelto, non sempre "claude code".
6. **F6 → performance reali**: il log di performance deve venire da un video REALMENTE pubblicato, non da metriche inventate — altrimenti il self-improver ottimizza su rumore.
7. **`execute_critic` → punteggio reale**: derivare le 5 dimensioni da controlli veri sul contenuto (lunghezza, presenza HOOK/CTA, keyword density), non da un dict fisso.
8. **Dashboard → stato reale**: riflettere l'esito vero di ogni gate della run corrente, non una tabella statica sempre verde.

---

## The 7-Step Architectural Evolution (Plan 1 to Plan 7)

### 📈 Plan 1: L1 - Le Fondamenta (Foundations) — ✅ costruito e testato (scaffolding)
- **Goal**: Set up the physical directory structure and import the core YouTube knowledge files (the Master Knowledge Document `MKD.md`, `ARCHITECTURE.md`, `SKILL.md`) into `YOUTUBE-AUTOMATION-FACTORY`. Create skeleton implementations for the APEX-7 components:
  - `memory.py` (Memory Query Interface)
  - `event_bus.py` (Publish-Subscribe Bus)
  - `quality_gate.py` (Quality Gate Definitions & Engine)
  - `gate_agent.py` (Quality Check Agent)
- **Pass Gate**: All files exist, compile, and simple unit tests verify component existence.

---

### 🔗 Plan 2: L2 - Struttura Connessa (Connected Structure)
- **Goal**: Wire the YouTube Conductor and operators (Niche Scout, Video Hunter, Script Writer, Video Producer, Metadata Optimizer, SEO Analyst) to the Event Bus and Memory.
- **Key Changes**:
  - The Conductor publishes a `task.created` event when it starts.
  - Operators communicate exclusively by publishing events (e.g., `niche.scouted`, `script.written`) instead of calling each other directly.
  - The `GateAgent` (`GATE-1`) listens to event requests and evaluates outputs against specific criteria for each phase.
- **Pass Gate**: End-to-end event chain works. Event log shows messages flowing from one agent to another via the Event Bus.

---

### 🔄 Plan 3: L3 - Loop Adattivi (Adaptive Loops)
- **Goal**: Implement feedback and error recovery loops.
- **Key Changes**:
  - If the `GateAgent` fails a step (e.g., the script written is too long or does not fit the target video), a `gate.failed` event is published.
  - A remediation flow triggers: the script writer receives the feedback, queries the Memory Decision Log, adapts its strategy, and retries.
  - If it fails 3 times, the Escalation Protocol freezes the flow and logs the anti-pattern.
- **Pass Gate**: Successfully demonstrates automatic retry and strategy change on simulated failures (e.g. forced low SEO score -> regeneration).

---

### ⚡ Plan 4: L4 - Parallelismo & Integrazione RuFLO (Concurrency & RuFLO)
- **Goal**: Introduce concurrent execution of tasks and interface with the RuFLO codebase.
- **Key Changes**:
  - Allow running multiple niche scouting tasks or script iterations in parallel.
  - Handle race conditions when writing to the central Memory DB using the Write-Lock (100ms timeout).
  - Map and integrate RuFLO API points for automation tasks.
- **Pass Gate**: Multiple concurrent agent execution runs successfully without database corruption or deadlock.

---

### 🧠 Plan 5: L5 - Intelligenza (Intelligence & Meta-Agent)
- **Goal**: Implement a supervisor agent (Meta-Agent) that has complete visibility over the swarm.
- **Key Changes**:
  - The Meta-Agent analyzes the overall workflow, detects failure patterns, and calculates dynamic quality scores.
  - It adjusts the instructions or inputs of operators based on past run history.
- **Pass Gate**: Meta-Agent successfully detects a repeating bottleneck in logs and corrects the prompt parameters.

---

### ♻️ Plan 6: L6 - Auto-Evoluzione (Self-Evolution)
- **Goal**: Allow the system to optimize its own operations within safe boundaries.
- **Key Changes**:
  - Implement memory compression (archiving low-relevance or old logs to prevent token bloat).
  - Let the system update its own rules file (`learned_rules.json`) based on performance audit results.
  - Establish strict spawning limits for agents and enforce human-override requirements for safety-critical steps.
- **Pass Gate**: System compresses its memory size and adds a new rule to its blacklist without human manual editing.

---

### 🏆 Plan 7: L7 - APEX Integration (Full Swarm & E2E Validation)
- **Goal**: Run the complete, coordinated swarm from beginning to end with self-healing capabilities.
- **Key Changes**:
  - Coordinated multi-swarm handling.
  - End-to-end execution of a real/mock YouTube video generation task (Scout -> Selection -> Script -> Video Spec -> SEO optimized title/desc -> mock upload).
  - Generation of a Consolidated Performance Dashboard.
- **Pass Gate**: 100% test coverage of all quality gates, self-healing demonstrated on multiple failure scenarios, and a clean run outputting all files.

---

## Brainstorming & Open Questions

To kick off the brainstorming session, Gael, here are a few simple questions:

1. **Il Canale e la Nicchia**: Abbiamo già delle nicchie pre-selezionate o dei canali di riferimento da usare come test iniziale per la fabbrica YouTube, oppure preferisci che il sistema inizi a cercarli da zero?
2. **Il Ruolo di Fliki**: Nella produzione dei video, useremo Fliki (tramite le sue istruzioni/spec) come strumento principale di creazione. Vuoi che la fabbrica generi solo le specifiche testuali pronte per essere incollate in Fliki, o prevedi un'integrazione più automatizzata?
3. **Controllo Umano (Gate)**: In quale fase preferisci avere il controllo manuale (es. approvare lo script prima di fare il video, o controllare il video finale prima di pubblicarlo)?
4. **Obiettivo Finale del Video**: I video avranno lo scopo di vendere i nostri info-prodotti (funnel) o punteranno a fare visualizzazioni di massa (Cash Cow classica)?

---

## Verification Plan

### Automated Tests
- Create `test_youtube_apex7.py` to test the event bus routing, memory lock timeouts, quality gate checks, and Conductor state machine.
- Run the test suite: `python -m unittest 02-AUTOMAZIONI-E-SCRIPTS/test_youtube_apex7.py`

### Manual Verification
- Execute a dry-run of the Conductor pipeline from Phase 1 to Phase 5 in headed/dry-run mode, producing final script files and metadata check reports.
