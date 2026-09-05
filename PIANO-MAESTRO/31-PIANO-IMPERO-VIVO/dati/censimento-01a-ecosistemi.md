# Censimento 01a — I 15 ecosistemi di `company/Ecosistemi/`

> Rilevazione del 2026-09-06. Perimetro: esattamente le 15 cartelle sotto
> `company/Ecosistemi/` (il file `REGISTRO-NUMERI.md` alla radice della cartella non e' un ecosistema
> e non e' schedato).
> **Esclusioni dai conteggi**, applicate a ogni comando `find`: `__pycache__/`, `node_modules/`, `.git/`.
> Ogni numero viene da un comando eseguito, ogni affermazione da un file aperto.
> Definizione di **vivo** usata per la voce "COSA MANCA": (a) invocabile con un comando dichiarato,
> (b) produce un'uscita conforme a un contratto scritto, (c) l'uscita finisce in un posto stabilito,
> (d) un test lo prova.

---

## 01 — AGENCY

- **Percorso**: `company/Ecosistemi/01-AGENCY/`

- **Cosa contiene davvero**: **209 file totali**, **tutti `.md`** (209/209). Zero `.py`, zero `.json`,
  zero `.yaml`, zero `.zip`, zero binari. Alberatura: 3 file di radice + `Funzioni/` (14 file) +
  `Workflow/` (10 file) + `Reparti/` (10 sottocartelle).

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE (carta d'identita', org chart L2→L5, DONE WHEN
  con 7 criteri, tabella "Sistemi attivi — NON toccare"), `BACKBONE.md` PRESENTE (8 namespace AgentDB
  con prefisso `agency/`, topologie swarm per reparto, handoff contract inter-ecosistema),
  `NAMESPACE.md` PRESENTE (mappa autoritativa chiavi AgentDB `agency/a<N>`). README di radice ASSENTE.
  Ogni reparto ha `README.md` + `ARCHITETTURA.md` propri.

- **Reparti (10)**: A1-Ricerca · A2-Acquisizione · A3-Preventivi · A4-Delivery ·
  A5-Copywriting-Interno · A6-Marketing-Interno · A7-Account-Management · A8-Closing ·
  A9-Partnership-Referral · A10-QA-Cliente.
  Ogni reparto ha la stessa forma a 8 comparti: `agenti/`, `workflow/`, `kpi/KPI.md`,
  `principi/PRINCIPI.md`, `regole/REGOLE.md`, `scripts/README.md`, `skills/SKILLS.md`, `state/README.md`.

- **Workflow definiti**: **38 file** — 10 in `Workflow/` di radice (WF-CASE-STUDY, WF-COPY-OUTREACH,
  WF-DELIVERY-CONTENT-FACTORY, WF-DELIVERY-OUTREACH-FACTORY, WF-DELIVERY-SECOND-BRAIN,
  WF-LEAD-SOURCING, WF-MARKET-INTEL, WF-PREVENTIVO, WF-SUPPORTO-90GG, `outreach-wrapper.md`) +
  **28** dentro i reparti (`Reparti/*/workflow/*.md`).

- **Agenti definiti dentro il nodo**: **74 schede**, tutte in `Reparti/<reparto>/agenti/`, con nome
  file `ag-a<N>-<ruolo>.md` (es. `ag-a1-scrape.md`, `ag-a2-bibbia`→`ag-a2-qa.md`, `ag-a3-price.md`,
  `ag-a10-handover.md`). In piu' 14 schede di "Funzione" L4 in `Funzioni/` (`T-scraper.md`,
  `T-extractor.md`, `T-qualifier.md`, `T-writer-apsoc.md`, `T-bibbia-qa.md`, `T-sender.md`,
  `T-reply-triage.md`, `T-followup.md`, `T-strategist.md`, `T-icp-profiler.md`,
  `T-competitor-profiler.md`, `T-discovery-brief.md`, `T-problem-audit.md`, `T-proposal-writer.md`).

- **Ha codice eseguibile?** **NO.** Nessun `.py`, `.sh`, `.bat`, `.js`. La cartella `scripts/` di ogni
  reparto contiene **solo un `README.md`** che documenta script che vivono altrove: p.es.
  `Reparti/A1-Ricerca/scripts/README.md` dichiara esplicitamente "A1 NON riscrive il runtime live
  (ADR-003): lo WRAPPA" e punta a `Outreach/Outreach Workflow/agents/` per scraper, `extractor.py`,
  `qualifier.py`, `competitor.py`, `cro_audit.py`.

- **Punto d'ingresso gia' esistente?** **NO dentro il nodo.** Nessun `main`. L'unico "punto di ingresso
  ufficiale" dichiarato e' un documento: `Workflow/outreach-wrapper.md`, che come avvio prescrive
  `Outreach/AVVIA-EMAIL-LIVE.bat` e `Outreach/AVVIA-DASHBOARD.bat` — entrambi fuori da `company/`.

- **Motore reale corrispondente FUORI da `company/`**: **SI, il piu' grosso dell'Impero.**
  - `Outreach/` — **313 file `.py`** (esclusi `__pycache__`), 6 `.bat` di avvio
    (`AVVIA-EMAIL-LIVE.bat`, `AVVIA-DASHBOARD.bat`, `TEST-EMAIL-10.bat`, `run_all.bat`,
    `run_followup_b3.bat`, `start-dashboard.bat`).
  - `Outreach/Outreach Workflow/agents/` — 25 moduli Python: `orchestrator.py`, `scraper.py`,
    `extractor.py`, `qualifier.py`, `strategist.py`, `writer.py`, `sender.py`, `bibbia_team.py`,
    `competitor.py`, `cro_audit.py`, `insight.py`, `research.py`, `reply_monitor.py`,
    `followup_writer.py`, `humanizer.py`, `conversation_manager.py`, `lead_analyzer.py`,
    `maps_browser_scraper.py`, `apify_scraper.py`, `apify_leads_finder.py`, `outscraper_scraper.py`,
    `google_scraper.py`, `copy_knowledge.py`, `ai_client.py`, `__init__.py`.
  - `Outreach/LinkedIn Automation/`, `Outreach/Instagram Automation/`, `Outreach/WhatsApp Automation/`,
    `Outreach/preventa-maps-scraper/`, `Outreach/preventa-outreach-pack/`,
    `Outreach/outreach-dashboard-premium/` (dashboard Next.js).
  - `agency-empire-landing/` e `agency-empire/` alla radice (landing + presentazione).
  - Runtime parallelo dentro `company/` ma **fuori** dal nodo censito: `company/01-agency/`
    (A1-RICERCA … A6-MARKETING-INTERNO + `BACKBONE.md` + `site-audit`), dichiarato in `ECOSISTEMA.md`
    come "Runtime operativo (Gael — NON toccare)".

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Nessun comando invoca il nodo.** `find company/Ecosistemi/01-AGENCY -name "*.py" -o -name "*.bat" -o -name "*.sh"` → 0 risultati. I 74 agenti sono prosa: non esiste un `agency.py` ne' una slash-command che accetti il nome di un reparto.
  - (a) **I 38 workflow non hanno runner.** `WF-PREVENTIVO.md` descrive i passi ma nessun eseguibile li percorre; l'unico wrapper (`outreach-wrapper.md`) delega a due `.bat` esterni che non leggono nulla del nodo.
  - (b) **Contratti scritti ma non validati.** `BACKBONE.md` §3 definisce i contract `HC-AG-*` in prosa/JSON inline; non c'e' uno schema JSON eseguibile nel nodo contro cui validarli (il template citato sta in `company/Backbone/Bus/contracts/HC-template.json`, fuori dal nodo).
  - (c) **Destinazione delle uscite dichiarata su AgentDB che il nodo non tocca.** `NAMESPACE.md` fissa `agency/a1…a10`, ma nessun file del nodo scrive li'; nessuna cartella `handoffs/{inbox,outbox,archive}` esiste dentro `01-AGENCY` (le dichiara `BACKBONE.md` §3 come "create in fase B2", fase non fatta).
  - (d) **Nessun test.** Zero file di test nel nodo; i 7 criteri "DONE WHEN" di `ECOSISTEMA.md` §2 sono verifiche a occhio ("struttura navigabile", "dry-run completo"), nessuna eseguibile.

- **Difficolta'**: **MEDIA** — il motore esiste, gira e produce (313 `.py` in `Outreach/`): manca solo
  il ponte fra la prosa del nodo e i `.bat` gia' funzionanti, non c'e' niente da inventare da zero.

---

## 02 — INFO-BUSINESS

- **Percorso**: `company/Ecosistemi/02-INFO-BUSINESS/`

- **Cosa contiene davvero**: **1.225 file totali** (esclusi `__pycache__`) — di gran lunga il nodo
  piu' pesante dopo APEX-7. Ripartizione esatta:
  **566 `.py`** · **514 `.md`** · **86 `.json`** · 14 `.txt` · 13 `.log` · 9 `.png` · 9 `.docx` ·
  6 `.pdf` · 4 `.epub` · 1 `.jsonl` · 1 `.bat` · 1 `.gitkeep` · 1 `.gitignore`. Nessun `.zip`, nessun `.yaml`.
  **Dove stanno i 566 `.py`** (tutti dentro un solo workflow):
  - 522 in `Workflow/libri-performanti-multiagente/_archivio_blueprint_narrativo/`
  - 28 in `Workflow/libri-performanti-multiagente/engine/`
  - 12 in `Workflow/libri-performanti-multiagente/_archivio_automazione_modelli/`
  - 4 in `Workflow/libri-performanti-multiagente/tests/`
  Il resto del nodo (Reparti, Agenti, Funzioni, gli altri 5 workflow) e' **solo prosa `.md`**.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE, `BACKBONE.md` PRESENTE. README di radice ASSENTE.
  Ogni reparto ha `README.md` + `ARCHITETTURA.md`. Il workflow libri ha una sua governance separata e
  molto piu' matura: `ARCHITETTURA.md`, `SOP-SCRIVERE-UN-LIBRO.md`, `PIANO-KDP-67.md`,
  `PIANO-KDP-V2-CLAUDE-CODE.md`, piu' 3 `LEGGIMI.md` dentro gli archivi.

- **Reparti (5)**: `IB-L2-COMM-Community-Retention` (18 file) · `IB-L2-LANC-Lanci-Campagne` (19) ·
  `IB-L2-PROD-Produzione-Prodotti` (21) · `IB-L2-STRA-Strategia-Intelligence` (17) ·
  `IB-L2-VEND-Vendite-Funnel` (19). Stessa forma a 8 comparti di 01-AGENCY.

- **Workflow definiti**: 5 schede `.md` in `Workflow/` (`WF-CORSO.md`, `WF-EBOOK.md`,
  `WF-FUNNEL-EVERGREEN.md`, `WF-LANCIO.md`, `WF-VALIDAZIONE.md`) + `lancio-wrapper.md` +
  **1 workflow che e' codice vero**: `Workflow/libri-performanti-multiagente/`.
  Piu' i workflow interni ai reparti (`Reparti/*/workflow/`).

- **Agenti definiti dentro il nodo**: **12 schede di radice** in `Agenti/` (`IB-0-conductor.md`,
  `IB-PM-product-manager.md`, `IB-CURRIC-designer.md`, `IB-MKD-forger.md`, `IB-PLATFORM-op.md`,
  `IB-LAUNCH-coordinator.md`, `IB-EMAIL-sequencer.md`, `IB-WEBINAR-host.md`, `IB-SALES-funnel.md`,
  `IB-COMMUNITY-manager.md`, `IB-COPY-liaison.md`, `IB-VALIDATION-analyst.md`)
  + **42 schede** dentro `Reparti/*/agenti/` + **3** dentro il workflow libri
  (`KDP-SCOUT.md`, `KDP-EDITOR.md`, `KDP-GATE.md`). Totale **57 schede agente**.
  In `Funzioni/`: 6 file (`T-CALENDARIO.md`, `T-COPY-LIAISON.md`, `T-CURRICULUM.md`,
  `T-DESIGN-PRODOTTO.md`, `T-MKD.md`, `T-PIATTAFORMA.md`).

- **Ha codice eseguibile?** **SI — l'unico ecosistema non-APEX che ne ha davvero dentro il nodo.**
  - `Workflow/libri-performanti-multiagente/engine/` — 28 moduli Python deterministici:
    `auto.py`, `book_project.py`, `kdp.py`, `kdp_formatter.py`, `niche_finder.py`,
    `session_manager.py`, `story_validator.py`, `gate_blocco.py`, `validators.py`, `epub.py`,
    `copertina_kdp.py`, `metriche.py`, `magazzino.py`, `piano.py`, `pubblicazione.py`,
    `report_validazione.py`, `scout.py`, `scrittore.py`, `paratesto.py`, `diagnosi.py`,
    `amazon_research.py`, `book_output_manager.py`, `book_report.py`, `config.py`,
    `ispirazione.py`, `libro_del_giorno.py`, `nicchia_attiva.py`, `__init__.py`.
  - **8 moduli hanno un blocco `__main__`** (`amazon_research.py`, `book_output_manager.py`,
    `book_project.py`, `kdp.py`, `kdp_formatter.py`, `niche_finder.py`, `session_manager.py`,
    `story_validator.py`); **3 hanno `argparse`** (`book_project.py`, `kdp.py`, `niche_finder.py`).
  - **4 test veri**: `tests/test_auto.py`, `tests/test_flusso_manuale.py`, `tests/test_kdp.py`,
    `tests/test_qualita_pacchetto.py`.
  - `requirements.txt` presente.
  - Due archivi di codice morto ma conservato: `_archivio_blueprint_narrativo/` (522 `.py`,
    generatori `gen_*.py` di un'architettura a 7 livelli) e `_archivio_automazione_modelli/` (12 `.py`,
    con `_scrittura_haiku/` e `_testo_lmarena/`, ognuno col proprio `LEGGIMI.md`).

- **Punto d'ingresso gia' esistente?** **SI, uno solo e parziale**:
  `Workflow/libri-performanti-multiagente/AVVIA-LOGIN-SESSIONI.bat`, che esegue
  `python -m engine.session_manager` (login una tantum Amazon + LM Arena). Gli altri comandi si
  invocano a mano come moduli (`python -m engine.kdp`, `engine.book_project`, `engine.niche_finder`).
  **Non esiste un punto d'ingresso per l'ecosistema** — i 5 workflow `.md` e i 5 reparti non hanno runner.

- **Motore reale corrispondente FUORI da `company/`**: **parzialissimo, e sotto quanto dichiarato.**
  `ECOSISTEMA.md` §"Asset esistenti" indica 4 cartelle: verificate una per una:
  - `Formazzione/` = **23 file**, di cui 14 `.pdf`, 5 `.png`, 3 `.txt`, 1 `.md` — **zero codice**.
  - `InfoBusiness/` = **5 file** (4 `.pdf`, 1 `.md`) — **zero codice**.
  - `Lanco ebook/` = **2 file** (1 `.html`, 1 `.md`) — **zero codice**.
  - `Lancio corso skill beast/` = 9.438 file, ma la composizione (2.192 `.txt`, 1.331 `.meta`,
    1.195 `.sst`, 1.168 `.rsc`, 806 `.js`, 566 `.json`) e' quella di un **progetto/cache esportato**,
    non di un motore di lancio invocabile.
  - `Workflow-libri/` alla radice = **78 file**, di cui 50 `.png`, 8 `.md`, **7 `.py`**, 5 `.txt` —
    e' il **predecessore** del workflow libri, molto piu' piccolo di quello che ora vive dentro il nodo.
  - `KDP - prodottti digitali/` alla radice **contiene 0 file** (`Glob "KDP - prodottti digitali/*"` → nessun risultato).
  **Il motore vero di questo ecosistema e' gia' dentro `company/`**, non fuori: e' `engine/`.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Il workflow libri e' vivo, l'ecosistema no.** Un comando esiste solo per i libri
    (`python -m engine.*`); per `WF-CORSO`, `WF-LANCIO`, `WF-FUNNEL-EVERGREEN`, `WF-VALIDAZIONE`,
    `WF-EBOOK` non esiste nessun eseguibile: `find Workflow -maxdepth 1 -name "*.py"` → 0.
  - (a) **Nessun comando dichiarato per i 57 agenti**: sono `.md` senza registrazione ne' invocazione.
  - (b) **Contratto d'uscita scritto solo per i libri.** `gate_blocco.py` + `validators.py` +
    `story_validator.py` fanno uscire il processo con codice d'errore (contratto eseguibile);
    per gli altri 5 workflow il "contratto" e' una tabella in prosa.
  - (c) **Destinazione dell'uscita definita solo per i libri**: `LIBRI/{in_lavorazione, libri_pronti,
    libri_pubblicati, _piani, _log, _ricerca_nicchie}` + `nicchia_attiva.json` + `chiamate.jsonl`.
    Per corso/lancio/funnel non esiste alcuna cartella di destinazione nel nodo.
  - (d) **Test presenti solo per i libri** (4 file in `tests/`). Zero test per i reparti e per gli
    altri workflow: `find Reparti -name "test_*"` → 0.
  - **Puntatore rotto da riparare**: `Workflow/libri-performanti-multiagente/ARCHITETTURA.md` rimanda
    la procedura a `.claude/skills/libro/SKILL.md` — **quella skill non esiste**
    (`ls .claude/skills/libro` → "No such file or directory"; esistono `book-optimizer-skill` e
    `book-to-skill`, che sono altra cosa).

- **Difficolta'**: **MEDIA** — un pezzo (i libri) e' gia' vivo secondo tutte e quattro le condizioni e
  fa da modello copiabile; il resto dell'ecosistema e' prosa senza motore da nessuna parte, dentro o fuori.

---

## 03 — CONTENT-FACTORY

- **Percorso**: `company/Ecosistemi/03-CONTENT-FACTORY/`

- **Cosa contiene davvero**: **186 file totali** — **183 `.md`**, **2 `.json`**, **1 `.jsonl`**.
  Zero `.py`, zero `.yaml`, zero `.zip`. I 3 file non-`.md` sono tutti tracce di ordini reali:
  `Reparti/CF-R5-Visual-Design-Caroselli/orders/CF-2026-PREVENTA-001/state.json`,
  `.../CF-2026-PREVENTA-001/trace.jsonl`, `.../CF-2026-PREVENTA-002/state.json`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE (6 DONE WHEN, confronto esplicito con la Content
  Factory di Exponium/AION), `BACKBONE.md` PRESENTE. README di radice ASSENTE.

- **Reparti**: **9 reparti veri** con struttura completa — `CF-R0-Director`, `CF-R1-Strategia-Brief`,
  `CF-R2-Brand-Kit-Registry`, `CF-R3-Produzione-Video`, `CF-R4-Produzione-Testuale`,
  `CF-R5-Visual-Design-Caroselli`, `CF-R6-QA-Gate`, `CF-R7-Pubblicazione`, `CF-R8-Apprendimento`
  (comparti: `agenti/`, `workflow/`, `kpi/`, `principi/`, `scripts/`, `state/`; CF-R5 ha in piu' `orders/`).
  **Piu' 5 cartelle-reparto residue con un solo `README.md` dentro e nessuna sottocartella**:
  `Reparti/Strategia/`, `Reparti/Produzione-Video/`, `Reparti/Produzione-Testuale/`,
  `Reparti/Visual-Design/`, `Reparti/Pubblicazione/` — 1 file ciascuna, gusci della nomenclatura vecchia
  rimasti accanto alla nuova.

- **Workflow definiti**: 5 in `Workflow/` (`WF-ARTICOLO.md`, `WF-PUBLISH.md`, `WF-THUMB.md`,
  `WF-VIDEO.md`, `caroselli-wrapper.md`) + **28** dentro i reparti (`Reparti/*/workflow/*.md`).

- **Agenti definiti dentro il nodo**: **71 schede** in `Agenti/` e `Reparti/*/agenti/`.

- **Ha codice eseguibile?** **NO.** Nessun `.py`, `.js`, `.mjs`, `.bat`, `.sh` nel nodo. Le cartelle
  `scripts/` contengono solo `README.md` di wrapping: `Reparti/CF-R5-Visual-Design-Caroselli/scripts/README.md`
  dichiara "carousel-factory e render.mjs non vengono modificati... i wrapper aggiungono il layer di
  parametrizzazione" (ADR-003) e descrive un wrapper `cf-carousel` che nel nodo **non esiste come file**.

- **Punto d'ingresso gia' esistente?** **NO nel nodo**, ma **SI fuori e gia' usato**: lo `state.json`
  dell'ordine CF-2026-PREVENTA-002 registra il comando esatto eseguito —
  `python "SKILL & Agenti/Workflow agency creative/caroselli.py" "<argomento>" --slide 6`.

- **Motore reale corrispondente FUORI da `company/`**: **SI, e verificato riga per riga dagli ordini.**
  - `SKILL & Agenti/Workflow agency creative/caroselli.py` — **esiste**, 21.052 byte, modificato il
    2026-08-31. E' l'entry-point del Ramo C: `genera_copy` (Gemini 2.5 Flash via OpenRouter),
    `valida_copy` prima del render, `gate` automatico con exit 1 in caso di fallimento.
  - `Workfolw crea caroselli à/carousel-factory/` — **esiste** (`brands/`, `templates/`, `scripts/`,
    `output/`, `package.json`, `node_modules/`): render Puppeteer HTML→PNG, invocato via
    `carousel-factory/scripts/generate.js`.
  - `caroselli/3-sistemi-ai/` alla radice — esiste ed e' il sorgente citato da `Workflow/caroselli-wrapper.md`.
  - `YOUTUBE-AUTOMATION-FACTORY/` — **136 file `.py`**, con `VIDEO-PRONTI/`, `memory/`, 4 profili
    Chrome dedicati (`chrome-profile-fliki`, `-arena`, `-youtube`, `-legamidiamore`): e' il motore
    reale del reparto CF-R3-Produzione-Video, **mai nominato in `ECOSISTEMA.md`**.
  - Consegne reali gia' su disco: `SKILL & Agenti/Workflow agency creative/Arsenale Caroselli/Preventa/`.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Il comando esiste ma non e' del nodo.** Nessun file di `03-CONTENT-FACTORY` puo' essere
    eseguito: chi ordina un carosello deve conoscere a memoria il path
    `SKILL & Agenti/Workflow agency creative/caroselli.py`, che nel nodo compare solo dentro
    un `state.json` di consuntivo, non in una scheda di comando.
  - (b) **Contratto d'ordine dichiarato ma non applicato in ingresso.** `ECOSISTEMA.md` DONE WHEN #1
    esige `{committente, brand_kit, icp, formato, quantita', deadline, budget}`: l'ordine 001 ha
    `"brand_kit_path": null`, l'ordine 002 ha un `brand_kit_path` che punta fuori
    (`Workfolw crea caroselli à/carousel-factory/brands/preventa/config.json`). Nessuno schema valida l'ordine.
  - (b) **Il gate esiste solo nel Ramo C.** Ordine 001: gate-formato e gate-brand con
    `"metodo": "verifica manuale (CF-R5-QA non ancora costruito come script reale)"`. Ordine 002:
    `"tipo": "AUTOMATICO"` perche' il gate e' dentro `caroselli.py`, non dentro il nodo.
  - (c) **La catena si interrompe al primo handoff.** Entrambi gli ordini dichiarano
    `"handoff-cf-r6": "non_eseguito" — CF-R6-QA-Gate non ancora costruito come reparto operativo`,
    e l'ordine 002 aggiunge "la pubblicazione non e' agganciata". CF-R7-Pubblicazione ha 0 ordini.
  - (c) **`orders/` esiste in un solo reparto su 9** (CF-R5). CF-R3 (video) ha il motore piu' grosso
    (`YOUTUBE-AUTOMATION-FACTORY`, 136 `.py`) e **zero ordini registrati**.
  - (d) **Nessun test**: `find company/Ecosistemi/03-CONTENT-FACTORY -name "test*"` → 0. Le prove sono
    2 `state.json` scritti a mano dopo il fatto.
  - **Da ripulire**: le 5 cartelle-reparto vuote della nomenclatura vecchia (`Strategia/`,
    `Produzione-Video/`, `Produzione-Testuale/`, `Visual-Design/`, `Pubblicazione/`) convivono con
    le 9 `CF-R*` e nessun documento dice quale delle due valga.

- **Difficolta'**: **BASSA** — e' l'ecosistema piu' vicino al vivo: un ordine reale ha gia' percorso
  brief → copy → render → gate automatico → consegna, e il comando che lo fa esiste e funziona;
  serve dargli una porta d'ingresso dentro il nodo e agganciare CF-R6/CF-R7.

---
