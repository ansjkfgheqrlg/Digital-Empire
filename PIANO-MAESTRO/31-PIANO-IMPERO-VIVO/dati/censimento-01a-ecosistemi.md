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
  - `KDP - prodottti digitali/` alla radice = **803 file**, due sole sottocartelle: `CAROSELLI/`
    (immagini `ChatGPT Image *.png` divise per titolo di libro) e `GPT - KDP Carousel Factory/` —
    e' un **archivio di immagini**, non un motore.
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

## 04 — MARKETING

- **Percorso**: `company/Ecosistemi/04-MARKETING/`

- **Cosa contiene davvero**: **159 file totali**, **tutti `.md`** (159/159). Zero `.py`, `.json`,
  `.yaml`, `.zip`, zero binari. Struttura: 2 file di radice (`ECOSISTEMA.md`, `BACKBONE.md`) +
  `Agenti/` (24) + `Funzioni/` (3) + `Workflow/` (8) + `Reparti/` (6 sottocartelle).

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE (missione, 4 gate di qualita' con soglie
  numeriche: APSOC ≥80, sales page ≥85, brand gate binario, "−15 automatico se P prima di S violata"),
  `BACKBONE.md` PRESENTE. README di radice ASSENTE.

- **Reparti (6)**: `L2-1-Copywriting` · `L2-2-Advertising` · `L2-3-Email-Lifecycle` ·
  `L2-4-Analytics` · `L2-5-Brand-Creative-Strategy` · `L2-6-Conversion-Architecture`.
  Ogni reparto ha gli 8 comparti (`agenti/`, `workflow/`, `kpi/`, `principi/`, `regole/`, `scripts/`,
  `skills/`, `state/`).

- **Workflow definiti**: 8 in `Workflow/` (`WF-ADS-CAMPAIGN.md`, `WF-COPY-AD.md`, `WF-COPY-EMAIL.md`,
  `WF-COPY-FULL.md`, `WF-COPY-SALES-PAGE.md`, `WF-EMAIL-LAUNCH.md`, `WF-OPTIMIZATION-LOOP.md`,
  `copy-workflow-wrapper.md`) + **22** dentro i reparti.

- **Agenti definiti dentro il nodo**: **68 schede** — **24 in `Agenti/`** di radice, nominate per ruolo
  APSOC (`A1-briefing-analyst.md` … `A8-copy-reviewer.md`, `S1-funnel-strategist.md`,
  `S2-positioning-strategist.md`, `S3-campaign-strategist.md`, `AD1-audience-analyst.md` …
  `AD4-compliance-checker.md`, `AN1-tracking-engineer.md` … `AN4-insight-distiller.md`,
  `E1-lifecycle-architect.md`, `E2-deliverability-guard.md`, `E3-segmentation-analyst.md`,
  `MKT-0-conductor.md`, `SEN-BV-brand-voice-sentinel.md`) + **44 in `Reparti/*/agenti/`**.
  In `Funzioni/`: 3 file (`T-AVATAR.md`, `T-HEADLINE.md`, `T-OBJECTIONS.md`).

- **Ha codice eseguibile?** **NO.** Zero file eseguibili. `Reparti/L2-1-Copywriting/scripts/README.md`
  lo dichiara: "gli script REALI che eseguono il copy vivono nel motore esistente ... e NON si
  riscrivono. Questa cartella contiene solo il layer di invocazione (wrapper)" — wrapper che pero'
  **non esiste come file**: `scripts/` contiene solo quel `README.md`.

- **Punto d'ingresso gia' esistente?** **SI, ma e' una skill Claude Code, non uno script**:
  `.claude/skills/copy-workflow/` esiste ed e' registrata, quindi il motore si invoca
  conversazionalmente. Nessun `main`, nessun `.bat`, nessuna CLI.

- **Motore reale corrispondente FUORI da `company/`**: **SI, ma e' un motore di prosa, non di codice.**
  - `SKILL & Agenti/Copy-Workflow-manuale/copy-workflow/` — **189 file**, di cui **56 `.md`**,
    14 `.sample`, 2 `.json`, 1 `.txt`, 1 `.pdf` e un repo git di backup (`bak/`).
    **Zero `.py`**: `find "SKILL & Agenti/Copy-Workflow-manuale" -name "*.py" | wc -l` → **0**.
    Contiene `SKILL.md`, `agents/`, `orchestrators/`, `workflows/`, `skills/`, `evals/`, `templates/`,
    `references/`.
  - Skill correlate registrate: `.claude/skills/copy-workflow/`, piu' `cro-copy-architect`,
    `market-copy`, `copywriting`, `ad-creative`, `emails`, `cold-email` nel catalogo skill.
  - `Marketing & Ai/` alla radice contiene una sola sottocartella omonima.
  - **Puntatore sbagliato**: `Workflow/copy-workflow-wrapper.md` cita il manuale come
    `SKILL & Agenti/Copy-Workflow-manuale/Il+manuale+del+copywriting+V1.1.pdf`; il file su disco si
    chiama `Il+manuale+del+copywriting+V1.1+Defo (1).pdf` — il path citato non esiste.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Invocabile solo da un umano in chat.** La skill `copy-workflow` parte se qualcuno la
    nomina; nessun altro ecosistema puo' chiamare MARKETING via comando: i contract `HC-*` in
    `BACKBONE.md` non hanno un ricevitore eseguibile.
  - (b) **I gate numerici non sono calcolati da niente.** `ECOSISTEMA.md` fissa APSOC ≥80 / ≥85 e
    "−15 se P prima di S": nel nodo e nei 189 file del motore non esiste una funzione che assegni
    quel punteggio — e' un giudizio che l'agente A8 esprime a mano, senza registro.
  - (c) **Nessun posto stabilito dove finisce il copy.** Nessuna cartella `orders/`, `output/` o
    `state/` popolata: `Reparti/*/state/` contiene solo prosa. A differenza di 03-CONTENT-FACTORY,
    qui non esiste **nemmeno un** ordine tracciato.
  - (d) **Nessun test.** `evals/` esiste nel motore esterno ma non e' agganciata a niente nel nodo;
    zero file di test dentro `04-MARKETING`.

- **Difficolta'**: **MEDIA** — la conoscenza e la struttura sono complete e la skill si invoca gia',
  ma tutto cio' che rende il lavoro verificabile (punteggio APSOC calcolato, ordine tracciato, output
  in un posto fisso) va costruito da zero: non c'e' una riga di codice da riusare.

---

## 05 — MULTI-BUSINESS

- **Percorso**: `company/Ecosistemi/05-MULTI-BUSINESS/`

- **Cosa contiene davvero**: **40 file totali**, **tutti `.md`** (40/40). Zero `.py`, `.json`, `.yaml`,
  `.zip`. Alberatura piatta: `Agenti/` (10), `Funzioni/` (2), `Reparti/` (11 **file**, non cartelle),
  `Workflow/` (15), + `ECOSISTEMA.md` e `BACKBONE.md`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE (7 DONE WHEN, e un "vincolo di onesta'"
  esplicito: i canali `@Legamidiamore` e `@dosementale` "NON sono ancora stati analizzati... Nessun
  dato su quei canali in questa documentazione e' inventato"), `BACKBONE.md` PRESENTE. README ASSENTE.

- **Reparti (11, ognuno un singolo file `.md`, non una cartella)**: `YT-Strategia.md`,
  `YT-Produzione.md`, `YT-Pubblicazione.md`, `YT-Ottimizzazione.md`, `PUB-Ricerca.md`,
  `PUB-Produzione.md`, `PUB-Packaging.md`, `PUB-Pubblicazione.md`, `ECOM-Ricerca.md`,
  `ECOM-Store.md`, `ECOM-Crescita.md`. **Differenza strutturale rispetto a 01/02/03/04**: qui non
  c'e' nessuno degli 8 comparti (`agenti/`, `kpi/`, `regole/`, `scripts/`, `state/`...): il reparto
  e' una pagina.

- **Workflow definiti (15)**: YouTube — `WF-YT-NICHE`, `WF-YT-CALENDAR`, `WF-YT-VIDEO-ORDER`,
  `WF-YT-PUBLISH`, `WF-YT-OPT`, `WF-YT-ANALYTICS`, `WF-YT-CHANNEL-LAUNCH`;
  Publishing — `WF-PUB-NICHE`, `WF-PUB-BOOK-ORDER`, `WF-PUB-COVER`, `WF-PUB-LISTING`,
  `WF-PUB-PUBLISH`, `WF-PUB-MONITOR`; E-commerce — `WF-ECOM-PRODUCT`; piu' `libri-wrapper.md`.

- **Agenti definiti dentro il nodo**: **10 schede** in `Agenti/` — `MB-A00-conductor.md` e
  `MB-YT-A01-strategy-coord.md` … `MB-YT-A09-opt-coord.md`. **Tutte e 9 le schede di reparto sono
  YouTube**: zero agenti per Publishing, zero per E-commerce, benche' entrambi abbiano reparti e
  workflow. In `Funzioni/`: `T-niche-scout.md`, `T-competitor-map.md`.

- **Ha codice eseguibile?** **NO.** Zero file eseguibili di qualunque tipo.

- **Punto d'ingresso gia' esistente?** **NO.** Nessun `main`, nessuno script, nessuna skill dedicata
  registrata col nome dell'ecosistema.

- **Motore reale corrispondente FUORI da `company/`**: **SI per due rami su tre, e non e' quello che il nodo dichiara.**
  - **Publishing** — `Workflow-libri/` alla radice: **78 file**, **7 `.py`** in `scripts/`
    (`orchestrator.py`, `build_book.py`, `build_book_reportlab.py`, `parse_manuscript.py`,
    `prepare_manuscript.py`, `generate_images.py`, `qa_checker.py`), piu' `agents/` (3),
    `templates/` (2), `input/` (2), `output/` (8), `config/`, `assets/images/`, `.claude/`.
    La struttura descritta in `Workflow/libri-wrapper.md` (`agents/`, `scripts/`, `templates/`,
    `input/`, `output/`) **corrisponde esattamente** al disco: e' l'unico wrapper del censimento il
    cui path dichiarato regge la verifica in ogni voce.
    **Ma**: il motore libri piu' avanzato dell'Impero non e' questo — e' `engine/` (28 moduli + 4 test)
    dentro `company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/`.
    Due ecosistemi rivendicano i libri KDP con due motori diversi e nessuno dei due lo dice.
  - **YouTube** — `YOUTUBE-AUTOMATION-FACTORY/` alla radice: **136 `.py`**, con `01-FLUSSI-E-PIANI/`,
    `02-AUTOMAZIONI-E-SCRIPTS/`, `03-AGENTI-E-RUOLI/`, `VIDEO-PRONTI/`, `memory/`, `transcripts/`,
    4 profili Chrome dedicati. **Il nodo `05-MULTI-BUSINESS` non lo nomina mai**: `grep -r
    "YOUTUBE-AUTOMATION-FACTORY" company/Ecosistemi/05-MULTI-BUSINESS/` → **0 occorrenze**.
    Gli unici path esterni citati dai 40 file sono `Workflow-libri/` (8 volte) e
    `KDP - prodottti digitali/` (15 volte, di cui 12 verso `.../LIBRO`).
  - **E-commerce** — **nessun motore, da nessuna parte.** Non esiste una cartella e-commerce
    alla radice; lo stesso `ECOSISTEMA.md` lo mette OUT OF SCOPE ("e-commerce operativo — solo scheletro").

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Nessun comando, per nessuno dei 15 workflow.** Il nodo e' 40 pagine di prosa: nessun
    eseguibile, nessuna skill che si chiami come l'ecosistema.
  - (a) **Il motore YouTube esiste (136 `.py`) ma il nodo non sa che esiste**: i 9 agenti `MB-YT-*`
    descrivono a parole cio' che `YOUTUBE-AUTOMATION-FACTORY/` gia' fa in codice, senza citarlo.
  - (b) **I 4 QA gate bloccanti (script, audio, visual, SEO) di `ECOSISTEMA.md` §3.1 non esistono
    come controllo**: nessun file del nodo li implementa ne' li registra.
  - (c) **Nessuna destinazione d'uscita nel nodo**: zero `orders/`, zero `state/`, zero `output/`.
    Le uscite reali (video pronti, libri) finiscono in cartelle esterne che il nodo non nomina.
  - (d) **Nessun test**, e i DONE WHEN #3 e #4 ("≥1 video che ha superato tutti e 4 i gate",
    "pipeline libro eseguita una volta end-to-end") non hanno alcun registro che li possa provare.
  - **Conflitto di competenza da sciogliere prima di costruire**: i libri KDP sono rivendicati sia
    qui (`Reparti/PUB-*`, `WF-PUB-*`, `libri-wrapper.md`) sia da 02-INFO-BUSINESS
    (`libri-performanti-multiagente/`, che e' quello con codice e test).

- **Difficolta'**: **MEDIA** — per YouTube e libri il codice esiste gia' altrove e va solo dichiarato
  e agganciato; per l'e-commerce non esiste niente e non e' nemmeno in scope, quindi l'ecosistema non
  potra' mai essere "vivo" al 100% finche' quel terzo ramo resta sulla carta.

---

## 06 — PLATFORM

- **Percorso**: `company/Ecosistemi/06-PLATFORM/`

- **Cosa contiene davvero**: **27 file totali**, **tutti `.md`** (27/27). Zero `.py`, `.json`, `.yaml`,
  `.zip`, zero binari. Alberatura piatta: `Agenti/` (11), `Funzioni/` (3), `Reparti/` (5 **file**),
  `Workflow/` (6), + `ECOSISTEMA.md` e `BACKBONE.md`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE (missione, tabella "Siti attivi" con 4 URL,
  elenco "Asset esistenti da migrare in F3"), `BACKBONE.md` PRESENTE. README di radice ASSENTE.
  **Nessun DONE WHEN misurabile**, a differenza di 01/02/03/05.

- **Reparti (5, ognuno un singolo file `.md`)**: `Web-Engineering.md`, `Tooling-Automation.md`,
  `Security-Quality.md`, `Deploy-CICD.md`, `Product-Engineering.md`.

- **Workflow definiti (6)**: `WF-SITE-FULL.md`, `WF-LANDING-RAPIDA.md`, `WF-EMPIRE-RESTYLE.md`,
  `WF-DEPLOY.md`, `WF-SEC-SCAN.md`, `crea-siti-wrapper.md`.

- **Agenti definiti dentro il nodo**: **11 schede** in `Agenti/` — `plt-director.md`,
  `plt-site-architect.md`, `plt-site-builder.md`, `plt-site-copy-merger.md`, `plt-motion-eng.md`,
  `plt-seo-tech.md`, `plt-qa-runner.md`, `plt-deploy-op.md`, `plt-sec-sentinel.md`,
  `plt-custodian.md`, `plt-cc-master.md`. In `Funzioni/`: `T-site-brief.md`,
  `T-site-architecture.md`, `T-site-design.md`.

- **Ha codice eseguibile?** **NO.** Zero file eseguibili nel nodo.

- **Punto d'ingresso gia' esistente?** **NO nel nodo.** Ma l'Impero ha gia' gli eseguibili che questo
  ecosistema dovrebbe governare: `scripts/verify-empire.ps1`, `scripts/verify-agents.py`,
  `scripts/verify-skills.py`, `scripts/empire-sync.ps1`, `scripts/gen-empire.py` — **tutti alla radice
  del repo, nessuno citato dal nodo**. In piu' esistono le skill registrate `site-build`, `site-deploy`,
  `site-qa`, `web-builder`, `website-creator`, `empire-premium-style`, `vercel:deploy`.

- **Motore reale corrispondente FUORI da `company/`**: **SI, molto frammentato.**
  - `Crea siti/` — **399 file** (esclusi `node_modules/` e `.git/`), con `agents/`, `skills/`,
    `system/`, `Siti CCM/`, `Preventa/`, `Skill-qui/`, `OPUS-CONTEXT.md`, `README.md`.
    E' il sorgente dichiarato da `Workflow/crea-siti-wrapper.md`.
  - `agency-empire/`, `agency-empire-landing/`, `Landing Page/`, `Agency page/`,
    `Skill empire-premium-style/`, `App/`, `EmpireDesk/` alla radice.
  - `scripts/` alla radice: **19 voci** fra `.py` e `.ps1`, incluso il `verify-empire.ps1` che
    `ECOSISTEMA.md` nomina nella missione del reparto CI/CD ma non collega mai a un path.
  - **Puntatore incompleto**: `ECOSISTEMA.md` elenca fra gli asset `empire-style/` e
    `presentazione-empire/` come cartelle di radice; sul disco esistono invece
    `Skill empire-premium-style/` e la presentazione solo come URL Vercel.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Nessun comando nel nodo**, e i comandi che esistono (i 19 script di `scripts/`) non sono
    dichiarati da nessuna delle 27 pagine: la parola "verify-empire" compare nella prosa del reparto
    CI/CD, mai come path eseguibile.
  - (b) **Nessun contratto d'uscita.** I 4 "siti attivi" sono elencati per URL: non c'e' un formato
    di consegna, un manifest di build, ne' una regola su cosa debba contenere un sito finito.
  - (c) **Nessun posto stabilito**: zero `state/`, zero `orders/`, zero log di deploy dentro il nodo.
    Il namespace `platform/*` e' dichiarato in `BACKBONE.md` e non scritto da niente.
  - (d) **Nessun test**, benche' esistano gia' `scripts/verify-*.py|ps1` che potrebbero diventarne
    la base immediata.
  - **Reparti fantasma nei path**: `ECOSISTEMA.md` indica `Reparti/Web-Engineering/`, `Reparti/Tooling/`,
    `Reparti/Security/`, `Reparti/CI-CD/` — **nessuna di queste cartelle esiste**; sul disco ci sono
    5 file `.md` con nomi in parte diversi (`Tooling-Automation.md`, `Security-Quality.md`, `Deploy-CICD.md`).

- **Difficolta'**: **BASSA** — l'ecosistema piu' facile da rendere vivo: 19 script eseguibili
  esistono gia' alla radice e fanno esattamente il suo mestiere (verify, sync, gen, deploy);
  basta dichiararli qui e dargli un posto dove scrivere l'esito.

---

## 07 — FORGE

- **Percorso**: `company/Ecosistemi/07-FORGE/`

- **Cosa contiene davvero**: **34 file totali**, **tutti `.md`** (34/34). Zero `.py`, `.json`, `.yaml`,
  `.zip`. Struttura: `Agenti/` (10), `Funzioni/` (7), `Reparti/` (5 cartelle con **un solo
  `README.md` dentro ciascuna**), `Workflow/` (10), + `ECOSISTEMA.md` e `BACKBONE.md`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE, `BACKBONE.md` PRESENTE. README di radice ASSENTE.
  Ogni reparto ha solo `README.md` (nessun `ARCHITETTURA.md`, nessun `agenti/`, nessun `kpi/`).

- **Reparti (5, cartelle con 1 file ciascuna)**: `AGENT-WORKS/`, `SKILL-WORKS/`, `WORKFLOW-WORKS/`,
  `ECOSYSTEM-WORKS/`, `METHOD-GUARD/`.

- **Workflow definiti (10)**: `WF-AGENT-NEW.md`, `WF-SKILL-NEW.md`, `WF-SKILL-AUDIT.md`,
  `WF-SKILL-IMPROVE.md`, `WF-TEAM-NEW.md`, `WF-ECOSYSTEM-NEW.md`, `WF-PRD.md`,
  `WF-FORGE-PIPELINE.md`, `WF-SPARC-ENFORCE.md`, `skill-creator-wrapper.md`.

- **Agenti definiti dentro il nodo**: **10 schede** in `Agenti/` — `frg-chief.md`, `frg-skill-smith.md`,
  `frg-org-designer.md`, `frg-spec-writer.md`, `frg-prd-architect.md`, `frg-mkd-forger.md`,
  `frg-eval-runner.md`, `frg-contradiction-gate.md`, `frg-sparc-warden.md`, `frg-hr-registrar.md`.
  In `Funzioni/` 7 file: `T-spec.md`, `T-draft.md`, `T-eval-runner.md`, `T-org-design.md`,
  `T-handoff-contracts.md`, `T-shared-state-schema.md`, `T-description-optimizer.md`.

- **Ha codice eseguibile?** **NO.** Zero file eseguibili nel nodo.

- **Punto d'ingresso gia' esistente?** **NO nel nodo**, ma il mestiere della FORGE e' gia' svolto da
  skill registrate e funzionanti: `.claude/skills/skill-creator/`, `agent-factory`, `skill-builder`,
  `agent-architecture`, `agent-specification`, `prd-architect-os`, `sparc-methodology`,
  `skill-contradiction-analyzer`. `Workflow/skill-creator-wrapper.md` e' il wrapper di una di queste.

- **Motore reale corrispondente FUORI da `company/`**: **SI, ed e' il piu' usato di tutti — ma non e'
  codice: sono le skill stesse.** Il catalogo skill del repo (`.claude/skills/`) contiene i motori
  che FORGE descrive: `skill-creator`, `agent-factory`, `skill-builder`, `master-build-architecture`,
  `content-forge` / `content-forge2.0`, `book-to-skill`, `prompt-engegniring-skill`,
  `system-promot-creator-project`, `swarm-advanced`, `sparc-methodology`. Piu' le cartelle di radice
  `master-build-architecture/`, `content-forge2.0/`, `master-app-builder-skill/`,
  `System OMEGA - Creazione proggetti e skill per Claude/`, `SKILL & Agenti/`.
  Fuori dal nodo esistono anche i verificatori: `scripts/verify-skills.py`, `scripts/verify-agents.py`,
  `scripts/peso_skill.py` — **nessuno dei tre e' citato dai 34 file di 07-FORGE**.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Il comando esiste (le skill) ma non passa da qui.** Quando si forgia una skill si invoca
    `skill-creator` direttamente: nessun passaggio tocca `07-FORGE`, che quindi non registra nulla.
  - (b) **`frg-contradiction-gate` e `frg-eval-runner` sono gate senza esecutore.** Esistono come
    schede; il controllo reale (`scripts/verify-skills.py`, `scripts/peso_skill.py`) vive altrove e
    non e' agganciato al gate.
  - (c) **Nessun registro delle forgiature.** `frg-hr-registrar.md` descrive un registro anagrafico
    degli agenti creati: quel registro **non esiste come file** nel nodo. Zero `state/`, zero `orders/`.
  - (d) **Nessun test** e nessuna eval agganciata, benche' `T-eval-runner.md` e `WF-SKILL-AUDIT.md`
    la presuppongano.
  - **Reparti vuoti**: 5 cartelle con un solo `README.md`, nessun agente e nessun workflow dentro —
    i 10 agenti e i 10 workflow stanno tutti nella radice del nodo, quindi i reparti non contengono
    il lavoro che dovrebbero organizzare.

- **Difficolta'**: **BASSA** — non serve costruire un motore: i motori (le skill) girano gia' ogni
  giorno; serve far passare la forgiatura da un registro e agganciare i tre verificatori esistenti.

---

## 08 — INTELLIGENCE

- **Percorso**: `company/Ecosistemi/08-INTELLIGENCE/`
  (⚠️ numero 08 **collide** con `08-STREAM-S7-BOT`: la collisione e' registrata e non risolta in
  `company/Ecosistemi/REGISTRO-NUMERI.md`, "duplicato vecchio, mai corretto")

- **Cosa contiene davvero**: **16 file totali**, **tutti `.md`** (16/16) — il secondo nodo piu' piccolo
  del perimetro dopo `14-TESORERIA` e `08-STREAM-S7-BOT`. Zero `.py`, `.json`, `.yaml`, `.zip`.
  Struttura: `Agenti/` (4), `Funzioni/` (5), `Reparti/` (4 **file**), `Workflow/` (1),
  + `ECOSISTEMA.md` e `BACKBONE.md`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE (missione, tabella "Asset attivi" con 6 voci e
  relativi path, avviso in grassetto sulle ingestioni YouTube pendenti), `BACKBONE.md` PRESENTE.
  README di radice ASSENTE.

- **Reparti (4, ognuno un singolo file `.md`)**: `INGESTION.md`, `MEMORY.md`, `RESEARCH.md`,
  `SECOND-BRAIN.md`. **`ECOSISTEMA.md` ne dichiara 5** (L2.1 Ingestione, L2.2 Wiki & Knowledge,
  L2.3 Memory Empire, L2.4 Research & Trend, L2.5 Cognitive Control/NERVE-SOLVE) **con path diversi
  da quelli reali** (`Reparti/Ingestione/`, `Reparti/Wiki/`, `Reparti/Memory-Empire/`,
  `Reparti/Research/`): nessuno di quei quattro path esiste.

- **Workflow definiti**: **uno solo** — `Workflow/wiki-wrapper.md`.

- **Agenti definiti dentro il nodo**: **4 schede** — `INT-A00-int-director.md`,
  `INT-A01-int-studio-conductor.md`, `INT-A02-int-memory-router.md`, `INT-A03-int-librarian.md`.
  In `Funzioni/` 5 file: `T-INGEST-VIDEO.md`, `T-INGEST-WEB.md`, `T-RESEARCH.md`,
  `T-WIKI-CONTEXT.md`, `T-REASONINGBANK.md`.

- **Ha codice eseguibile?** **NO.** Zero file eseguibili nel nodo.

- **Punto d'ingresso gia' esistente?** **SI, fuori dal nodo e realmente in uso**: le skill registrate
  `memory-empire` (presente sia in `.claude/skills/memory-empire/` sia in
  `~/.claude/skills/memory-empire/`), `wiki-context`, `sync-wiki-totale`, `empire-studio`,
  `nerve-solve` (`.claude/skills/nerve-solve/` — verificata presente, come dichiara `ECOSISTEMA.md`).

- **Motore reale corrispondente FUORI da `company/`**: **SI, ed e' vivo e pieno di dati.**
  - `second-brain-vault/wiki/` — **1.872 file**, organizzata in `00 - Inbox`, `01 - Projects`,
    `02 - Areas`, `03 - Frameworks`, `03 - Resources`, `04 - Notes`, `05 - Daily Notes`,
    `06 - People`, `07 - Meetings`, `08 - Templates`. E' la fonte di verita' dichiarata dal
    `CLAUDE.md` di progetto.
  - `SKILL & Agenti/Empire Studio Suite/` — pipeline di ingestione video (`empire-studio/runs/…`,
    con run reali `max18-v01…v09` visibili anche nello stato git).
  - Skill: `memory-empire`, `wiki-context`, `sync-wiki-totale`, `empire-studio`, `nerve-solve`,
    `conoscenza-empire` (agente), `graphify` + `graphify-out/`.
  - `company/Memory/` (ecosistema 10) e' il partner interno: vedi scheda 10.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Il nodo non e' mai il punto d'ingresso**: si invocano direttamente `memory-empire` o
    `wiki-context`; le 4 schede agente non sono registrate da nessuna parte come invocabili.
  - (b) **Il contratto d'uscita esiste ma e' altrove**: lo standard "ogni operazione logga in
    `second-brain-vault/wiki/log.md`" e' un obbligo scritto nel `CLAUDE.md` di progetto, non un
    controllo del nodo; nessun file di `08-INTELLIGENCE` verifica che sia stato rispettato.
  - (c) **La destinazione e' fuori** (`second-brain-vault/wiki/`), e il nodo non ha alcun `state/`.
  - (d) **Nessun test.** Nessun controllo automatico di integrita' della wiki (link morti, pagine
    orfane) esiste nel nodo, benche' `wiki-wrapper.md` dichiari l'operazione "LINT".
  - **Debito dichiarato nel documento stesso**: `ECOSISTEMA.md` marca `@Legamidiamore` e
    `@dosementale` come "NON ancora ingeriti — Task 7.0/F-MB1", e lo stesso vincolo blocca i
    parametri di 05-MULTI-BUSINESS.
  - **Il numero 08 va sanato** prima di qualunque automazione che indirizzi gli ecosistemi per numero.

- **Difficolta'**: **BASSA** — motore vivo (1.872 file di wiki), skill gia' invocabili, ingestioni che
  girano davvero: manca solo far passare le operazioni da un registro e mettere un lint automatico.

---

## 08 — STREAM-S7-BOT (secondo occupante del numero 08)

- **Percorso**: `company/Ecosistemi/08-STREAM-S7-BOT/`

- **Cosa contiene davvero**: **1 file** con i filtri standard — `S7_NFT_BOT.zip` (21.884 byte,
  23 luglio 2026) — **piu' una cartella `__pycache__/` con 4 file di bytecode compilato**
  (`analysis_engine.cpython-311.pyc`, `data_manager.cpython-311.pyc`,
  `execution_engine.cpython-311.pyc`, `risk_manager.cpython-311.pyc`), esclusi dal conteggio come da
  regola ma **non ignorabili**: sono la prova che questo codice **e' stato eseguito su questa macchina**
  con Python 3.11, il 23 luglio 2026 alle 08:47-08:48.
  **Un audit precedente aveva dichiarato questa cartella "vuota": e' falso.**

  **Contenuto dello `.zip` — aperto e letto, 14 voci, 40.731 byte decompressi:**
  | File | Byte | Cos'e' |
  |---|---|---|
  | `main.py` | 2.035 | entry-point `asyncio.run(main())`, lega i 4 layer |
  | `data_manager.py` | 3.882 | Layer A — ascolto WebSocket mempool Solana |
  | `analysis_engine.py` | 3.611 | Layer B — genera il segnale di BUY |
  | `execution_engine.py` | 3.205 | Layer C — esecuzione (con `_simulate_transaction`) |
  | `risk_manager.py` | 2.093 | Layer D — sizing + `activate_kill_switch()` |
  | `requirements.txt` | 97 | `solana==0.33.0`, `solders==0.21.0`, `websockets==12.0`, `pandas==2.2.0`, `numpy==1.26.4`, `python-dotenv==1.0.1` |
  | `.env.example` | 822 | `SOLANA_WSS_URL`, `TRADE_MODE`, `BASE_BANKROLL_SOL`, `MAX_POSITION_PCT`, `WALLET_*` |
  | `LEGGIMI.md` | 1.755 | istruzioni d'uso + procedura di passaggio a LIVE + kill-switch |
  | `report-studio.md` | 3.149 | **il verdetto**: l'edge del retail non esiste |
  | `paper_trade_log.csv` | 651 | **6 trade simulati reali**, tutti BUY, 0.5 SOL, esito SUCCESS, del 2026-07-23 |
  | 4 × `__pycache__/*.pyc` | 19.431 | bytecode, uguale a quello fuori dallo zip |

- **Documenti di governo**: `ECOSISTEMA.md` **ASSENTE**. `BACKBONE.md` **ASSENTE**. README di radice
  **ASSENTE** — l'unico documento e' `LEGGIMI.md`, **dentro** lo zip. E' l'unico dei 15 nodi senza
  alcun documento di governo leggibile senza decomprimere.

- **Reparti**: nessuno. **Workflow**: nessuno.

- **Agenti definiti dentro il nodo**: **zero schede.** Gli unici "agenti" sono i 4 layer software.

- **Ha codice eseguibile?** **SI, ma compresso**: 5 moduli Python dentro `S7_NFT_BOT.zip`
  (`main.py`, `data_manager.py`, `analysis_engine.py`, `execution_engine.py`, `risk_manager.py`).
  Fuori dallo zip non c'e' nessun `.py` estratto: resta solo il bytecode nel `__pycache__`.

- **Punto d'ingresso gia' esistente?** **SI, documentato con precisione dentro `LEGGIMI.md`**:
  `cd company/Ecosistemi/08-STREAM-S7-BOT` → `pip install -r requirements.txt` → `python main.py`.
  **Il comando cosi' com'e' oggi fallisce**: i file citati non esistono sul disco, sono dentro lo zip;
  serve un `unzip` che il LEGGIMI non menziona.

- **Motore reale corrispondente FUORI da `company/`**: **NO — e nemmeno serve: il motore e' questo.**
  Non esiste nessuna cartella di radice dedicata al trading/NFT. Esiste pero' un **gemello dentro
  `company/`**: `company/Ecosistemi/12-STREAM-S7-BOT/` (81 file, 31 `.py`, 31 `.md`), che porta lo
  stesso nome e lo stesso numero di stream — vedi scheda 12.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Il comando dichiarato non funziona da fermo**: `python main.py` in quella cartella non trova
    `main.py` (e' compresso). Basta estrarre lo zip perche' (a) sia soddisfatta.
  - (b) **Il contratto d'uscita esiste gia' ed e' il piu' rigoroso del censimento**: `LEGGIMI.md`
    impone che `report-studio.md` dimostri "un'expectancy positiva su almeno 30 giorni di simulazione"
    prima di passare a `TRADE_MODE=LIVE`. Il `paper_trade_log.csv` contiene pero' **6 righe di un
    solo minuto** (2026-07-23, 08:47-08:48) e **nessuna riga di chiusura** (solo BUY, mai SELL):
    l'expectancy non e' calcolabile, il gate non e' superato.
  - (c) **La destinazione e' stabilita** (`paper_trade_log.csv` accanto al codice) ma il file vive
    dentro lo zip: ogni nuova run scriverebbe in una cartella estratta non tracciata.
  - (d) **Nessun test**: nessun `test_*.py`, e il kill-switch (`activate_kill_switch()` in
    `risk_manager.py`) non ha una prova che si attivi davvero.
  - **Domanda che il piano deve porsi prima di spendere lavoro qui**: `report-studio.md` — scritto
    dallo studio stesso — conclude che il retail non ha edge ("un bot in Python su un VPS standard
    che usa una RPC pubblica riceve il dato dal mempool con 300-800 ms di ritardo... quando il nostro
    `analysis_engine.py` invia il segnale di BUY, l'NFT/token e' gia' stato comprato"). **Rendere
    "vivo" questo nodo puo' voler dire archiviarlo con onore, non collegarlo.**

- **Difficolta'**: **BASSA** in senso tecnico (un `unzip` e il codice riparte), **ALTA** in senso
  decisionale: il documento interno dice che la strategia non ha vantaggio statistico, quindi la
  scelta non e' tecnica ma di Max.

---

## 09 — OPERATIONS

- **Percorso**: `company/Ecosistemi/09-OPERATIONS/`

- **Cosa contiene davvero**: **32 file totali**, **tutti `.md`** (32/32). Zero `.py`, `.json`, `.yaml`,
  `.zip`. Struttura: `Agenti/` (10), `Funzioni/` (4), `Reparti/` (5 cartelle con un solo `README.md`
  ciascuna), `Workflow/` (11), + `ECOSISTEMA.md` e `BACKBONE.md`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE, con **4 DONE WHEN misurabili** e una tabella di
  handoff che nomina 7 controparti. `BACKBONE.md` PRESENTE. README di radice ASSENTE.
  Lo stato dichiarato in testa e' gia' onesto: "parziale (ruflo installato, swarm non inizializzato,
  run outreach attive ma lanciate a mano)".

- **Reparti (5, cartelle con 1 `README.md`)**: `RUNTIME/`, `SCHEDULING/`, `COST-GUARD/`,
  `STORAGE-ASSETS/`, `MONITORING-DASHBOARD/`.

- **Workflow definiti (11)**: `WF-SWARM-RUN.md`, `WF-QUEUE.md`, `WF-LOOP.md`, `WF-CRON.md`,
  `WF-WATCH.md`, `WF-BUDGET.md`, `WF-ATTRIBUTION.md`, `WF-TIER-ROUTING.md`, `WF-DASHBOARD.md`,
  `WF-BACKUP.md`, `WF-ASSET-MGMT.md`.

- **Agenti definiti dentro il nodo**: **10 schede** in `Agenti/` — `ops-director.md`,
  `ops-swarm-marshal.md`, `ops-scheduler.md`, `ops-watchdog.md`, `ops-cost-sentinel.md`,
  `ops-cost-accountant.md`, `ops-tier-router.md`, `ops-dashboard-builder.md`, `ops-backup-op.md`,
  `ops-asset-keeper.md`. In `Funzioni/` 4 file: `T-fanout.md`, `T-worker-pool.md`,
  `T-merge-results.md`, `T-retry-failed.md`.

- **Ha codice eseguibile?** **NO.** Zero file eseguibili nel nodo.

- **Punto d'ingresso gia' esistente?** **NO nel nodo**, ma esistono fuori i comandi che questo
  ecosistema dovrebbe schedulare e misurare: le skill registrate `avvia-email`, `avvia-ig`,
  `avvia-parallel`, `avvia-scraper`, `avvia-linkedin`, `avvia-outreach-preventa`, `avvia-estate-wk`
  (verificate presenti in `.claude/skills/`), piu' `scripts/empire-sync.ps1`, `scripts/agency-trace.ps1`,
  `scripts/gate_battito_hook.py`, `scripts/verifica_recap.py`.

- **Motore reale corrispondente FUORI da `company/`**: **parziale, e una gamba dichiarata e' vuota.**
  - **Esistono**: i 7 comandi `avvia-*` come skill, e i `.bat` che lanciano (`Outreach/*.bat`);
    `scripts/` alla radice con hook e verificatori.
  - **NON esiste il runtime dichiarato**: `ECOSISTEMA.md` dice "ruflo installato", e il `CLAUDE.md`
    globale rimanda a `ruflo` come MCP con `swarm_init`, `agent_spawn`, `memory_store`.
    Sul disco **`ruflo/` alla radice contiene 0 file** (`find ruflo -type f | wc -l` → **0**:
    cartella esistente e completamente vuota). Il server MCP `claude-flow` risulta inoltre non
    raggiungibile in questa sessione (timeout di connessione).
  - **Non esiste il ledger**: `find . -maxdepth 4 -iname "*ledger*"` → **0 risultati** in tutto il repo,
    benche' il DONE WHEN #1 lo esiga ("raccolto in un ledger unico").

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Nessun comando del nodo**, e i comandi reali (`avvia-*`) non passano da OPERATIONS: chi
    lancia una run non registra nulla qui.
  - (b) **L'evento standard `{ecosistema, workflow, costo, durata, esito}` del DONE WHEN #1 non
    esiste come formato in nessun file**: nessuno schema, nessun esempio compilato.
  - (c) **Nessun posto dove finiscono le misure**: zero `state/`, zero `ledger`, zero dashboard.
    Il DONE WHEN #4 ("dashboard unica leggibile in 30 secondi") non ha alcun artefatto.
  - (c) **Il budget guard (DONE WHEN #2) non puo' bloccare niente**: `ops-cost-sentinel.md` e
    `WF-BUDGET.md` descrivono il blocco, ma non c'e' codice che intercetti una spesa.
  - (d) **Nessun test.** In compenso esistono gia' fuori dal nodo due hook eseguibili e attivi
    (`scripts/gate_battito_hook.py`, `scripts/verifica_recap.py`): sono la prova che in questo repo
    un gate bloccante si sa scrivere — semplicemente non e' stato scritto per OPERATIONS.
  - **Da verificare prima di progettare lo swarm**: la dipendenza da `ruflo`, oggi cartella vuota.

- **Difficolta'**: **ALTA** — e' l'unico ecosistema trasversale il cui motore dichiarato (ruflo/swarm)
  **non esiste sul disco**: qui non si collega, si costruisce da zero (ledger, eventi, budget guard,
  dashboard), e ogni altro ecosistema dipende da lui per essere misurato.

---

## 10 — MEMORY

- **Percorso**: `company/Ecosistemi/10-MEMORY/`

- **Cosa contiene davvero**: **28 file totali**, **tutti `.md`** (28/28). Zero `.py`, `.json`, `.yaml`,
  `.zip`. Struttura: `Agenti/` (12), `Funzioni/` (5), `Reparti/` (5 **file**), `Workflow/` (4),
  + `ECOSISTEMA.md` e `BACKBONE.md`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE (dichiara stato "OPERATIVO (ME-0/ME-1)" e una
  tabella "Componenti operativi (gia' costruiti)" con 10 voci e i loro path), `BACKBONE.md` PRESENTE.
  README di radice ASSENTE. ADR fondativo citato: `company/Memory/decisions/ADR-002-memory-first.md`.

- **Reparti (5, ognuno un singolo file `.md`)**: `M1-RECALL-PRETASK.md`, `M2-CHECKPOINT-SESSIONI.md`,
  `M3-ADR.md`, `M4-PIANI-STATO.md`, `M5-SYNC.md`. **`ECOSISTEMA.md` ne dichiara altri 4 con path
  diversi** (`Reparti/Checkpoint/`, `Reparti/ADR/`, `Reparti/State/`, `Reparti/Audit/`, marcati
  "da costruire in fasi successive"): nessuna di quelle cartelle esiste.

- **Workflow definiti (4)**: `WF-PRE-TASK-GATE.md`, `WF-POST-TASK-COMMIT.md`, `WF-ADR-REGISTER.md`,
  `WF-AMNESIA-TEST.md`.

- **Agenti definiti dentro il nodo**: **12 schede** in `Agenti/` — `ME-A00-conductor.md` **e**
  `ME-A00-memory-conductor.md` (**due schede con lo stesso codice A00**), poi
  `ME-A01-context-loader.md`, `ME-A02-relevance-scorer.md`, `ME-A03-checkpoint-writer.md`,
  `ME-A04-session-logger.md`, `ME-A05-adr-registrar.md`, `ME-A06-contradiction-checker.md`,
  `ME-A07-plan-keeper.md`, `ME-A08-state-tracker.md`, `ME-A09-wiki-syncer.md`,
  `ME-A10-memory-sentinel.md`. In `Funzioni/` 5 file `T-M1…T-M5`.

- **Ha codice eseguibile?** **NO** dentro il nodo.

- **Punto d'ingresso gia' esistente?** **SI, fuori dal nodo, ed e' obbligatorio per legge interna**:
  `python scripts/checkpoint.py cp --titolo "..."` — file verificato: `scripts/checkpoint.py`,
  12.995 byte, modificato il 2026-09-05. Il `CLAUDE.md` di progetto lo impone: "il codice si conia con
  `python scripts/checkpoint.py cp`, **mai a mano e mai progressivo**".

- **Motore reale corrispondente FUORI da `company/`**: **SI — ed e' l'ecosistema piu' vivo dei 15.**
  - `company/Memory/` — **425 file**, con `INDEX.md`, `STATO-EMPIRE.md`, `BACKLOG.md`, `ROUTINES.md`,
    `PESO-SKILL.md`, `TESORERIA.md`, `ULTIMO-METRO.md`, piu' le cartelle `checkpoints/`,
    `decisions/`, `plans/`, `sessions/`, `session/`, `state/`, `studi/`, `riprese/`, `tasks/`,
    `templates/`, `audit/`, `tesoreria/`, `maximilian-corpus/`.
  - **Prova di attivita' reale, non dichiarata: 299 checkpoint** in `company/Memory/checkpoints/`,
    l'ultimo `CP-20260906-001.md` (oggi), e **25 ADR** in `company/Memory/decisions/`.
  - `scripts/checkpoint.py` (conio del codice CP), `scripts/emperator_hook.py`,
    `scripts/gate_battito_hook.py`, `scripts/verifica_recap.py` — hook attivi.
  - Skill correlate: `memory-empire`, `memory-management`, `sync-wiki-totale`.
  - Da notare: **il motore sta dentro `company/`, ma fuori dal nodo censito** — `company/Memory/`
    (425 file, vivo) contro `company/Ecosistemi/10-MEMORY/` (28 file, prosa).

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) **Soddisfatta a meta'**: il comando esiste (`scripts/checkpoint.py`) ed e' usato ogni giorno,
    ma non e' dichiarato dentro il nodo — nessuno dei 28 file lo cita come punto d'ingresso.
  - (b) **Contratto d'uscita reale ma solo per i checkpoint** (template in `company/Memory/templates/`).
    `WF-PRE-TASK-GATE.md` e `WF-AMNESIA-TEST.md` non hanno un esecutore: il gate memory-first e'
    applicato dalla disciplina in `CLAUDE.md`, non da un controllo.
  - (c) **La destinazione e' stabilita e rispettata** (`company/Memory/checkpoints/`,
    `/decisions/`) — questa e' l'unica condizione pienamente soddisfatta, con 299+25 prove su disco.
  - (d) **Nessun test**: `WF-AMNESIA-TEST.md` descrive la prova regina ("una chat nuova riprende da
    dove eravamo?") e non e' mai stata resa eseguibile.
  - **Difetto strutturale**: due agenti con lo stesso codice `ME-A00`
    (`ME-A00-conductor.md` e `ME-A00-memory-conductor.md`) — chi instrada per codice non sa quale prendere.

- **Difficolta'**: **BASSA** — tre condizioni su quattro sono gia' vere nei fatti; serve dichiarare nel
  nodo il comando che tutti gia' usano e rendere eseguibile il test di amnesia.

---

## 11 — APEX-7-CORE

- **Percorso**: `company/Ecosistemi/11-APEX-7-CORE/`

- **Cosa contiene davvero**: **489 file totali** (esclusi `__pycache__`, `node_modules`, `.git`) —
  **il nodo piu' grande del perimetro**. Ripartizione esatta:
  **189 `.json`** · **161 `.py`** · **62 `.md`** · **23 `.yaml`** · 15 `.png` · 9 `.ts` · 5 `.sh` ·
  4 `.mjs` · 3 `.txt` · 2 `.yml` · **2 `.sql`** · **2 `.rego`** · 2 `.gz` · **2 `.db`** · 1 `.toml` ·
  1 `.sig` · 1 `.ini` · 1 `.gitignore` · piu' 4 file senza estensione
  (`orchestration-layer/release/candidate/SHA256SUMS`,
  `orchestration-layer/quality/evidence/policy-bundle/SHA256SUMS`,
  `orchestration-layer/deploy/pilot/Dockerfile`, `orchestration-layer/CODEOWNERS`).
  **Dove stanno i 161 `.py`**: 96 in `orchestration-layer/src/`, 26 in `orchestration-layer/tests/`,
  8 in `orchestration-layer/scripts/`, 3 in `orchestration-layer/migrations/`, 7 in `agents/`,
  7 in `orchestration/`, 3 test di radice, `main.py`, `run_demo.py`, `arena_generator.py`,
  `orchestrator/ruflo_core.py`, `memory/memory_system.py`, `calc/*`.
  **I due `.db` sono SQLite reali**: `memory/data/decision_log.db` (45.056 byte) e
  `memory/data/youtube/decision_log.db` (40.960 byte).

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE, `BACKBONE.md` PRESENTE, **`README.md` PRESENTE**
  (unico nodo del perimetro che ce l'ha), piu' `EXECUTION_REPORT.md` e `UPGRADE_V2_REPORT.md`.
  Il README apre con un ADR citato per esteso (**ADR-012, 2026-08-26**): "`orchestration-layer/` e' il
  nuovo motore di orchestrazione canonico (governance OPA, contratti JSON Schema, adapter Postgres,
  bridge RuFlo pinnato, 148 test verdi)... `orchestrator/` e `orchestration/` restano ATTIVI e
  agganciati in produzione — NON cancellare finche' i consumatori non sono migrati".

- **Reparti**: **nessuna cartella `Reparti/`.** L'organizzazione non e' per reparti ma per moduli
  software: `agents/`, `orchestrator/`, `orchestration/`, `orchestration-layer/`, `memory/`,
  `workflows/`, `prompts/`, `skills/`, `calc/`, `outputs/`, `reference/`.

- **Workflow definiti**: `workflows/` (con `apex7_workflow.yaml`, RuFLO-compatible, routing
  condizionale score-based) + `orchestration-layer/builder_swarm/workflow.yaml` +
  3 gate YAML (`gates/architecture.yaml`, `gates/implementation.yaml`, `gates/release.yaml`).

- **Agenti definiti dentro il nodo**: **7 moduli Python veri, non schede**: `agents/base_agent.py`,
  `planner.py`, `writer.py`, `analyst.py`, `critic.py`, `refiner.py`, `meta_agent.py`.
  Piu' 4 skill scritte: `skills/apex7-master/`, `skills/carousel-machine/`, `skills/cold-outreach/`,
  `skills/skill-forge/`. **E' l'unico nodo dove "agente" significa codice eseguibile.**

- **Ha codice eseguibile?** **SI, in modo massiccio.** 161 moduli Python, 5 `.sh`, 4 `.mjs`, 2
  migrazioni SQL (`0001_core.sql`, `0002_privacy.sql`), 2 policy OPA in Rego
  (`policies/authorization.rego` + il suo `authorization_test.rego`), un `Dockerfile`,
  un `docker-compose.yml`, un `CODEOWNERS`, e **una pipeline CI reale**:
  `orchestration-layer/.github/workflows/ci.yml`.

- **Punto d'ingresso gia' esistente?** **SI, tre, tutti documentati e gia' eseguiti**:
  - `python main.py "<richiesta>"` — entry-point del sistema a 7 livelli
    (`main.py` gestisce esplicitamente il problema cp1252 di Windows con `sys.stdout.reconfigure`).
  - `python run_demo.py` — demo 3 stream paralleli.
  - `python arena_generator.py --model "GPT-4o" --demo`.

- **Motore reale corrispondente FUORI da `company/`**: **NO — e non serve: il motore e' qui dentro.**
  E' l'unico ecosistema del perimetro il cui codice vive nel nodo stesso. Riferimenti esterni:
  la skill ufficiale `apex-7` (`.claude/skills/apex-7/`, che `ECOSISTEMA.md` indica come
  `../../.agents/skills/apex-7/`) e il progetto esterno `github.com/ruvnet/ruflo` citato dal README
  come base del livello L4 — ma la cartella `ruflo/` alla radice del repo **e' vuota (0 file)**.

- **COSA MANCA PERCHE' SIA VIVO** — qui la domanda si rovescia: **e' gia' vivo su tutte e quattro le
  condizioni**, e cio' che manca e' il collegamento agli altri 14:
  - (a) SODDISFATTA: `python main.py`, `python run_demo.py`, `python arena_generator.py` — comandi
    dichiarati nel README e nell'`EXECUTION_REPORT.md`.
  - (b) SODDISFATTA: contratti JSON Schema in `orchestration-layer/contracts/` (14 `.json`),
    quality gate a 5 dimensioni con soglie numeriche (Completezza ≥8, Precisione ≥8, Creativita' ≥7,
    Actionability ≥8, Coerenza ≥9), 3 gate YAML del builder swarm, policy OPA in Rego.
  - (c) SODDISFATTA: `outputs/` contiene **10 file prodotti davvero** (7 PNG di carosello,
    `SKILL_20260723_075817.md`, `SKILL_20260813_111030.md` + il suo `.gate.json`), e i due
    `decision_log.db` SQLite registrano le decisioni.
  - (d) SODDISFATTA: **27 file di test** (`test_calc.py`, `test_multi_tenant.py`,
    `test_orchestration.py` di radice + 24 in `orchestration-layer/tests/`, inclusi
    `integration/test_postgres_real.py`, `test_opa_real.py`, `test_api_worker_real.py`),
    piu' CI GitHub Actions e SHA256SUMS di release firmati.
  - **Cio' che manca davvero**:
    - **nessuno degli altri 14 ecosistemi lo invoca**: `ECOSISTEMA.md` dichiara che tutti "DEVONO
      obbligatoriamente implementare e interfacciarsi con la Skill Ufficiale APEX-7", ma nei nodi
      01-10 e 12-14 non esiste una sola chiamata a `main.py` ne' un riferimento ai suoi gate;
    - **tre motori di orchestrazione convivono** (`orchestrator/`, `orchestration/`,
      `orchestration-layer/`) e l'ADR-012 li tiene tutti e tre in vita di proposito: finche' la
      migrazione non finisce, "quale motore risponde" non e' univoco;
    - **la dipendenza RuFLO e' scoperta**: il livello L4 poggia su un progetto la cui cartella
      locale e' vuota, e il server MCP correlato non risponde in questa sessione.

- **Difficolta'**: **BASSA per se stesso** (e' gia' vivo e testato), **MEDIA per l'Impero**: il lavoro
  non e' costruire, e' far si' che gli altri 14 lo chiamino davvero e chiudere la migrazione dei tre
  orchestratori prevista da ADR-012.

---

## 12 — STREAM-S7-BOT

- **Percorso**: `company/Ecosistemi/12-STREAM-S7-BOT/`

- **Cosa contiene davvero**: **81 file totali** (esclusi `__pycache__`). Ripartizione esatta:
  **31 `.py`** · **31 `.md`** · 8 `.txt` · 6 `.json` · **2 `.csv`** · 1 `.yaml` · 1 `.gitignore` ·
  1 `.example` (`.env.example`). Piu' una cartella `.claude/` con `settings.json` e
  `settings.local.json` propri del nodo.
  Sottocartelle: `agents/` (con `conductor/`, `execution/`, `forge/`, `meta/`, `quant/` e i loro
  sotto-agenti `chief-forge`, `ingestion`, `mkd-builder`, `silent-observer`,
  `expectancy-calculator`), `memory/` (`architectures/`, `checkpoints/`, `decisions/`, `nft_cache/`),
  `prompts/`.
  **E' il gemello evoluto di `08-STREAM-S7-BOT`**: contiene gli stessi 5 moduli
  (`main.py`, `data_manager.py`, `analysis_engine.py`, `execution_engine.py`, `risk_manager.py`)
  piu' 26 moduli aggiuntivi.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE, `BACKBONE.md` PRESENTE, `LEGGIMI.md` PRESENTE
  (con front-matter `Owner: 08-STREAM-S7-BOT (R&D Speculativo)`, `Status: EXPERIMENTAL`), piu' una
  documentazione insolitamente ricca: `STATO-RIPRESA.md`, `LOGICA-COMPLETA-S7.md`,
  `PIANO-STRATEGICO-S7.md`, `STUDIO-NFT-FASE0.md`, `FAILURE-MODES-NFT.md`, `APEX-7.md`,
  `report-studio.md`, `task_max.md`. README di radice ASSENTE.

- **Reparti**: nessuna cartella `Reparti/`; l'organizzazione e' per team di agenti dentro `agents/`:
  **conductor · execution · forge · meta · quant**.

- **Workflow definiti**: `apex7_workflow.ruflo.yaml` (unico `.yaml` del nodo).

- **Agenti definiti dentro il nodo**: **agenti-codice**, non schede: `agents/conductor/team_conductor.py`,
  `agents/execution/team_execution.py`, `agents/forge/team_forge.py`, `agents/quant/team_quant.py`,
  piu' `meta_agent.py`, `gate_agent.py`, `worker_agent.py` alla radice.

- **Ha codice eseguibile?** **SI**: 31 moduli Python, di cui **6 sono test**
  (`test_apex7.py`, `test_level_1.py`, `test_nft_s7.py`, `test_nft_ondata2.py`,
  `test_nft_ondata3.py`, `test_nft_ondata4.py`). Motori NFT dedicati: `nft_analysis_engine.py`,
  `nft_magiceden_client.py`, `nft_monte_carlo.py`, `nft_ondata2/3/4.py`. Infrastruttura:
  `event_bus.py`, `orchestrator.py`, `quality_gates.py`, `gate_verifiers.py`,
  `memory_interface.py`, `ruflo_adapter.py`, `position_monitor.py`.

- **Punto d'ingresso gia' esistente?** **SI, due, e uno e' verificato verde**:
  - `python main.py` (paper trading);
  - `python test_apex7.py` — `STATO-RIPRESA.md` riporta "gate finale L6→L7 **PASSED 7/7, score 1.0**
    (riverificato il 2026-08-03)".
  **Ma il `LEGGIMI.md` di questo nodo dice di entrare nella cartella sbagliata**: "1. Entrare nella
  cartella: `cd company/Ecosistemi/08-STREAM-S7-BOT`" — cioe' manda nel nodo gemello, dove il codice
  e' compresso e il comando fallisce. E' un puntatore stale copiato insieme al file.

- **Motore reale corrispondente FUORI da `company/`**: **NO.** Nessuna cartella di trading alla radice.
  Il motore e' il nodo stesso; la duplicazione e' interna (08 vs 12).

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) SODDISFATTA nei fatti (`python main.py`, `python test_apex7.py`), ma **il documento che
    istruisce l'operatore punta alla cartella sbagliata** — va corretto prima di ogni altra cosa.
  - (b) SODDISFATTA: `quality_gates.py` + `gate_verifiers.py` + `apex7_workflow.ruflo.yaml`
    definiscono e verificano i gate; `STATO-RIPRESA.md` cita 89/89 controlli reali sul layer NFT.
  - (c) SODDISFATTA parzialmente: le uscite vanno in `paper_trade_log.csv` (**7 righe**) e
    `paper_trade_log_nft.csv` (**3 righe**), piu' `memory/` con checkpoint e decisioni proprie.
    Sono volumi da prova, non da esercizio.
  - (d) SODDISFATTA: 6 file di test, gate finale documentato come 7/7.
  - **Cio' che manca non e' tecnico.** `STATO-RIPRESA.md` lo dice in un blocco intitolato
    "non manca codice, manca una decisione": expectancy **negativa**, ">85% di perdere il capitale
    entro il primo mese", e il layer NFT "bocciato per live" da 89/89 controlli reali
    (`CP-20260730-007`). Il prerequisito bloccante e' economico (B-010: RPC Solana a pagamento —
    l'endpoint pubblico risponde `429` dopo 2 chiamate).
  - **Duplicazione da sanare**: 08 e 12 sono lo stesso sistema in due stadi; il registro
    (`REGISTRO-NUMERI.md`) segnala la collisione e la lascia aperta.

- **Difficolta'**: **BASSA** tecnicamente (gia' verde), **ALTA** come decisione: due analisi
  indipendenti dicono di non andare live, e finche' Max non decide, ogni lavoro qui e' a vuoto —
  lo scrive il nodo stesso.

---

## 13 — ARENA-APEX

- **Percorso**: `company/Ecosistemi/13-ARENA-APEX/`

- **Cosa contiene davvero**: **19 file totali** — **9 `.md`**, **9 `.json`**, **1 `.py`**.
  Struttura: `config/` (1), `memory/` (5 sottocartelle da 1 file), `output/` (1),
  `prompts/` (3), `skills/` (1), `workflows/` (3), + `README.md`, `ARCHITECTURE.md`,
  `ECOSISTEMA.md`, `BACKBONE.md`, `orchestrator.py`.

- **Documenti di governo**: `ECOSISTEMA.md` PRESENTE, `BACKBONE.md` PRESENTE,
  **`README.md` PRESENTE** (con Quick Start eseguibile), `ARCHITECTURE.md` PRESENTE.
  E' uno dei due soli nodi con README (l'altro e' 11-APEX-7-CORE).

- **Reparti**: nessuno. **Workflow definiti (3, come JSON eseguibili, non prosa)**:
  `workflows/carousel-workflow.json`, `workflows/cold-outreach-workflow.json`,
  `workflows/skill-forge-workflow.json`.

- **Agenti definiti dentro il nodo**: nessuna scheda agente. Ci sono 3 prompt operativi
  (`prompts/skill-forge-v2.md`, `prompts/carousel-engine-v2.md`, `prompts/cold-outreach-v2.md`)
  e 1 skill (`skills/client-onboarding.md`).

- **Ha codice eseguibile?** **SI, uno solo ma completo**: `orchestrator.py`, **453 righe**, con
  `if __name__ == "__main__"` alla riga 452 e una CLI a 6 sottocomandi documentata nel docstring.

- **Punto d'ingresso gia' esistente?** **SI**: `python3 orchestrator.py status | memory <layer> |
  workflow <name> | critique <file> | decision <cosa> <perche'> | snapshot`.
  **Il README pero' fa entrare in una cartella che non esiste**: "`cd digital-empire`" — nel repo
  non c'e' nessuna cartella con quel nome; il comando va lanciato dentro `13-ARENA-APEX/`.

- **Motore reale corrispondente FUORI da `company/`**: **NO in senso stretto** — il motore e' il
  nodo. Ma e' **la versione ridotta e stand-alone di 11-APEX-7-CORE**: stessi tre stream
  (skill-forge, carousel, cold-outreach), stessa idea di memoria a layer, stesso quality gate.
  Il collegamento esterno reale e' Arena.ai (i prompt in `prompts/` sono da incollare li'), lo stesso
  motore che `03-CONTENT-FACTORY` chiama "Ramo D" e che `CF-2026-PREVENTA-002` ha dichiarato
  **fermo su questa macchina** dal 2026-08-25 (`playwright_stealth` non installato, sessione assente).
  Alla radice del repo esiste anche `imported-from-arena/`.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) SODDISFATTA a meta': la CLI esiste e funziona, ma il README indirizza a una cartella
    inesistente (`cd digital-empire`) — chi segue le istruzioni non parte.
  - (b) SODDISFATTA: quality gate dichiarato a **≥ 7.5/10** e 3 workflow descritti in JSON
    (formato macchina, non prosa).
  - (c) SODDISFATTA in minima parte: `output/` contiene **un solo prodotto**,
    `output/outreach-concessionari-20260723/sequenza-email.md`; i 5 file di memoria
    (`memory/decisions/log.json` 2.849 byte, `knowledge/base.json` 2.136,
    `strategies/store.json` 2.273, `architecture/snapshots.json` 1.273,
    `working/context.json` 570) sono **tutti fermi al 25 luglio 2026**.
  - (d) **NESSUN test**: zero `test_*.py`, a differenza dei fratelli 11 e 12.
  - **Sovrapposizione da sciogliere**: 11-APEX-7-CORE, 12-STREAM-S7-BOT e 13-ARENA-APEX sono tre
    implementazioni della stessa architettura APEX; solo la 11 ha CI e 27 test.

- **Difficolta'**: **BASSA** — un comando gia' funzionante, un README da correggere, e la decisione
  se tenerlo come sistema separato o fonderlo in 11-APEX-7-CORE.

---

## 14 — TESORERIA

- **Percorso**: `company/Ecosistemi/14-TESORERIA/`

- **Cosa contiene davvero**: **1 file** — `README.md`. Piu' **due cartelle completamente vuote**:
  `agenti/` (0 file) e `workflow/` (0 file), create il 2026-09-03 e mai riempite.
  Nessun `.py`, `.json`, `.yaml`, `.zip`.

- **Documenti di governo**: `ECOSISTEMA.md` **ASSENTE**, `BACKBONE.md` **ASSENTE**.
  **`README.md` PRESENTE** ed e' il migliore del perimetro: dichiara la data di nascita
  (2026-09-03), l'ADR che lo istituisce (`ADR-020`), il motivo misurato
  ("Digital Empire non misurava un solo euro"), i **cinque comandi esatti**, la tabella degli organi
  con i path, e tre leggi operative ("Previsto non e' incassato. Mai.").

- **Reparti**: nessuno (la cartella `agenti/` esiste vuota). **Workflow**: nessuno (`workflow/` vuota).

- **Agenti definiti dentro il nodo**: **zero.** I 5 agenti esistono e sono registrati, ma **fuori**:
  `.claude/agents/tesoreria-conductor.md`, `-entrate.md`, `-spese.md`, `-report.md`, `-previsione.md`
  (tutti verificati presenti).

- **Ha codice eseguibile?** **NO nel nodo.** Il motore e' fuori: `scripts/tesoreria.py`,
  **18.443 byte**, del 2026-09-03.

- **Punto d'ingresso gia' esistente?** **SI, cinque comandi dichiarati e funzionanti**, scritti nel
  README con la sintassi completa:
  `python scripts/tesoreria.py entrata|spesa|incassa|report [--mese YYYY-MM] [--scrivi]`.
  Piu' la skill registrata `.claude/skills/tesoreria/SKILL.md`.

- **Motore reale corrispondente FUORI da `company/`**: **SI, ed e' l'unico caso del censimento in cui
  il motore e' completo, recente e perfettamente puntato dal nodo.**
  - `scripts/tesoreria.py` (18.443 byte) — registra, calcola, riferisce.
  - `.claude/skills/tesoreria/SKILL.md` — il comando.
  - `.claude/agents/tesoreria-*.md` — i 5 agenti.
  - `company/Memory/tesoreria/` — i dati: `entrate.jsonl`, `spese.jsonl`, `README.md`.
  - `company/Memory/TESORERIA.md` — il rapporto, rigenerato da `report --scrivi`.

- **COSA MANCA PERCHE' SIA VIVO**:
  - (a) SODDISFATTA: cinque comandi dichiarati, motore presente.
  - (b) SODDISFATTA: il formato e' una riga JSON per movimento, e le tre leggi sono un contratto
    scritto ("Un numero che non esiste si dichiara, non si stima").
  - (c) SODDISFATTA come destinazione, **vuota come contenuto**: `company/Memory/tesoreria/entrate.jsonl`
    e `spese.jsonl` sono **entrambi di 0 byte**, creati il 2026-09-03 alle 13:03 e mai scritti.
    `company/Memory/TESORERIA.md` lo certifica da solo: "**Nessun movimento registrato** — non
    significa che l'azienda non incassi e non spenda: significa che non lo sta ancora scrivendo da
    nessuna parte."
  - (d) **NESSUN test**: nessun `test_tesoreria.py` in `scripts/`.
  - **Il nodo e' un guscio**: 1 file e 2 cartelle vuote. Tutto cio' che vive sta altrove, e questo
    ecosistema non contiene nemmeno i suoi documenti di governo.

- **Difficolta'**: **BASSA** tecnicamente — il motore e' pronto e i comandi funzionano; il vero
  ostacolo non e' informatico: **serve che qualcuno registri il primo euro**. Finche' i due `.jsonl`
  restano a 0 byte, l'ecosistema e' vivo come macchina e morto come organo.

---
