# CENSIMENTO 04b — I MOTORI REALI, TUTTO CIO' CHE NON E' `Outreach/`

> **Complemento di** `censimento-04-motori.md` (che copre la sola famiglia `Outreach/` e non va toccato).
> **Metodo:** ogni riga viene da un file aperto o da un comando lanciato. Mai dedotta dal nome della cartella.
> **Esclusi dai conteggi:** `node_modules/`, `.git/`, `__pycache__/`, `venv/`, `.venv/`, `site-packages/`, `.next/`.
> **Nessuno script e' stato eseguito.** Sola lettura e ispezione: nessun invio, nessuna spesa, nessun account toccato, nessuna pubblicazione.
> **Soglia VIVO:** ha prodotto un output datato negli ultimi 60 giorni, cioe' dal **2026-07-08** in poi (oggi 2026-09-06).
> **Data del censimento:** 2026-09-06.

## Mappa preliminare — dove sta il codice fuori da `Outreach/`

Conteggio `find` sulla radice del repository (file `.py` | file totali | cartella), esclusi i percorsi di cui sopra:

| .py | file tot | cartella radice |
|---:|---:|---|
| 774 | 3.591 | `company/` |
| 451 | 55.750 | `SKILL & Agenti/` |
| 251 | 8.403 | `WORKFLOW-ESTATE/` |
| 136 | 9.558 | `YOUTUBE-AUTOMATION-FACTORY/` |
| 125 | 6.704 | `DIGITAL-EMPIRE/` |
| 97 | 122 | `empire/` |
| 75 | 9.913 | `Clienti/` |
| 42 | 90 | `Agenti/` |
| 42 | 196 | `System OMEGA - Creazione proggetti e skill per Claude/` |
| 31 | 4.933 | `Agency page/` |
| 15 | 399 | `Crea siti/` |
| 15 | 19 | `scripts/` |
| 14 | 3.975 | `EmpireDesk/` |
| 13 | 3.414 | `second-brain-vault/` |
| 7 | 78 | `Workflow-libri/` |
| 5 | 408 | `master-build-architecture/` |
| 4 | 104 | `PIANO-MAESTRO/` |
| 1 | 10.193 | `Lancio corso skill beast/` |
| 1 | 803 | `KDP - prodottti digitali/` |
| 0 | 1.854 | `agency-empire/` |
| 0 | 1.774 | `agency-empire-landing/` |
| 0 | 721 | `SaaS/` |

Le cartelle a 0 `.py` non sono per forza vuote di motori: contengono siti Next.js, dashboard HTML e materiale. Sono aperte una per una piu' avanti.

---

## 2. FAMIGLIA YOUTUBE — `YOUTUBE-AUTOMATION-FACTORY/`

Radice: `c:\Users\Utente\Desktop\qui tutto\Digital Empire\YOUTUBE-AUTOMATION-FACTORY`
**136 file `.py`, 17.099 righe di Python.** I 9.558 file totali sono gonfiati da quattro profili
Chromium persistenti (`chrome-profile-arena/`, `-fliki/`, `-legamidiamore/`, `-youtube/`): non sono codice,
sono le sessioni browser vive del sistema.
`README.md`: *"Ecosistema APEX-7 per la generazione automatica di video YouTube. Tavolo di lavoro per Gael."*

### 2.1 apex7_orchestrator — il cervello a 6 fasi
- **Percorso:** `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py`
- **A cosa serve:** dal docstring — *"APEX-7 Adaptive Prompt EXecution Engine (Level 7), orchestratore Swarm + Memory per la Fabbrica YouTube Automation. Esegue le 6 fasi del workflow in modo completamente automatico o guidato, con persistenza dello stato, recupero dagli errori e ottimizzazione continua delle regole."* Autore dichiarato: Gael. Governo: ADR-008 / MANDATO Art.8.
- **Dimensione:** **101.506 byte**, il singolo file Python piu' grande del repository fuori da `Outreach/`.
- **PUNTO D'INGRESSO:** `python apex7_orchestrator.py run --phase N` (invocato anche da `run_youtube_apex7.py` e da `produci_video_completo.py`).
- **GIRA ANCORA? VIVO.** Prova: `memory/decision_log.json` (104 KB) e `memory/firme.json` scritti il **2026-09-04 14:37**; `memory/coda_produzione.json` il 2026-09-04 10:52.
- **DIPENDENZE ESTERNE:** `memory/*.json` (stato persistente), cache canali `memory/channel_videos/*.json`, script adattati a mano in `05-TEMPLATES-E-KIT/script-adattati/<videoId>.md`.
- **CHI LO POSSIEDE:** `03-CONTENT-FACTORY` — censito in `company/REGISTRO-IMPRESA.md` riga 52 come **YOUTUBE-AUTOMATION-FACTORY (fabbrica video APEX-7 a 6 fasi F1-F6)**, con test `test_youtube_apex7.py` 11/11. NON orfano.
- **COME SI AVVOLGE:** gia' avvolto da `produci_video_completo.py`; manca solo che il codice di uscita per fase sia leggibile da un comando dell'Impero senza aprire `decision_log.json`.

### 2.2 produci_video_completo — il comando "vai"
- **Percorso:** `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py`
- **A cosa serve:** dal docstring — *"Un solo comando (= un solo pulsante in Aureus) che produce DAVVERO video + copertina. Non reimplementa niente (ADR-003: wrap, mai riscrittura). Incatena i tre pezzi reali: 1. apex7_orchestrator.py run --phase 5, 2. arena_thumbnail.py -> COPERTINA reale, 3. fliki_client.py -> VIDEO reale mp4 (API Fliki, consuma crediti veri)."* Si ferma al primo fallimento e lo dichiara.
- **Dimensione:** 24.051 byte, ultima modifica **2026-09-04 15:09**.
- **PUNTO D'INGRESSO:** questo file. E' il piu' vicino a un "pulsante unico" che la fabbrica abbia.
- **GIRA ANCORA? VIVO ma con l'ultimo giro FALLITO.** Prova esatta, `memory/produzione_completa_stato.json`: `{"fase": "fallito", "ts": "2026-09-04T14:56:06", "passo": "video", "exit_code": 1, "video_id": "XABjAjqfUxw"}`. Nonostante il fallimento della catena, `VIDEO-PRONTI/video-08/video.mp4` (286 MB) risulta scritto alle 15:02 dello stesso giorno e `fliki_poll_only.py` toccato alle 15:06: il video e' stato recuperato a mano ripescando il job Fliki gia' pagato.
- **DIPENDENZE ESTERNE:** `FLIKI_API_KEY` in `YOUTUBE-AUTOMATION-FACTORY/.env` (unica chiave nel file, presente), sessione Arena in `chrome-profile-arena/`, crediti Fliki reali.
- **CHI LO POSSIEDE:** `03-CONTENT-FACTORY`. NON orfano.
- **COME SI AVVOLGE:** e' gia' il wrapper. Serve che l'uscita sia una riga JSON (`video`, `copertina`, `esito`) invece di uno stato scritto solo su file.

### 2.3 fliki_client — il motore che paga
- **Percorso:** `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/fliki_client.py` (26.395 byte)
- **A cosa serve:** dal docstring — *"Client reale per l'API Fliki Enterprise. Legge la spec reale di produzione-spec.json e lo script reale di F3, genera il video via API (non Playwright: qui esiste una vera API con FLIKI_API_KEY), fa polling dello stato e scarica il file finale."* Endpoint dichiarati verificati il 2026-07-29: `POST /v1/generate/video`, `GET /v1/generate/status`.
- **PUNTO D'INGRESSO:** chiamato da `produci_video_completo.py`; lanciabile da solo. Accanto ci sono `fliki_login.py`, `fliki_poll_only.py` (recupero job gia' avviati, 2026-09-04) e `fliki_subtitle_presets.py`.
- **GIRA ANCORA? VIVO.** E' il pezzo che **consuma crediti veri** — non e' stato eseguito in questo censimento.
- **DIPENDENZE ESTERNE:** `FLIKI_API_KEY` (presente in `.env`), crediti dell'abbonamento Fliki.
- **CHI LO POSSIEDE:** `03-CONTENT-FACTORY`. NON orfano.
- **COME SI AVVOLGE:** gia' avvolto; e' l'unico punto del repository dove un comando spende soldi veri, quindi va tenuto dietro un gate esplicito.

### 2.4 arena_thumbnail — la copertina, ROTTA
- **Percorso:** `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/arena_thumbnail.py` (23.039 byte, 2026-08-31)
- **A cosa serve:** genera la copertina reale pilotando arena.ai con Playwright sul profilo `chrome-profile-arena/`.
- **PUNTO D'INGRESSO:** questo file, invocato come passo 2 di `produci_video_completo.py`.
- **GIRA ANCORA? ROTTO.** Guasto esatto, da `memory/arena_thumbnail_status.json`: `{"status": "tentativo_fallito", "ts": "2026-09-04T11:47:35", "n": 3, "errore": "Locator.count: Target page, context or browser has been closed"}`. **Tre tentativi, tutti falliti**, con lo stesso identico guasto dell'Instagram Automation censito nel file 04: il contesto Playwright muore a meta' run.
- **DIPENDENZE ESTERNE:** sessione arena.ai in `chrome-profile-arena/` (ultima scrittura 2026-09-04), Playwright/Chromium.
- **CHI LO POSSIEDE:** `03-CONTENT-FACTORY`. NON orfano.
- **NOTA:** la rottura non blocca la produzione perche' **la copertina la fa Max a mano** — il flusso e' progettato cosi'. Il motore automatico e' una ridondanza rotta, non un blocco.

### 2.5 youtube_uploader_playwright — la pubblicazione
- **Percorso:** `YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/youtube_uploader_playwright.py` (30.689 byte, **2026-09-04 15:01**)
- **A cosa serve:** carica il video su YouTube Studio pilotando il browser. Dal codice: gestisce i menu Polymer di Studio cercando le opzioni **per testo** invece che per tag, perche' *"Studio apre i menu in un overlay fuori dal dialog (tp-yt-iron-dropdown agganciato al body)"*. Ha una `upload_mock()` esplicita per le prove a vuoto.
- **PUNTO D'INGRESSO:** questo file. Esiste anche `youtube_uploader.py` (5.109 byte, 2026-07-25), la versione vecchia via API.
- **GIRA ANCORA? VIVO.** Prova: `chrome-profile-youtube/` scritto il 2026-09-04 15:06, e la trentina di script `_check_*`, `_ads_*`, `_resume_*` datati **2026-09-03** sono la traccia di una sessione reale di lavoro su YouTube Studio (monetizzazione, claim, upload bloccati) durata un giorno intero.
- **DIPENDENZE ESTERNE:** sessione YouTube in `chrome-profile-youtube/`.
- **CHI LO POSSIEDE:** `03-CONTENT-FACTORY`. NON orfano.
- **COME SI AVVOLGE:** serve che restituisca l'URL del video pubblicato; oggi l'esito si legge dagli screenshot in `memory/`.

### 2.6 Pacchetto `youtube_automation_factory/` — la fabbrica "pulita"
- **Percorso:** `YOUTUBE-AUTOMATION-FACTORY/youtube_automation_factory/`
- **A cosa serve:** dal suo `README.md` — *"Fabbrica multi-agentica per la produzione di contenuti YouTube originali, con gerarchia decisionale, workflow di approvazione e controlli regolatori applicati dal codice, non soltanto descritti nella documentazione. La nicchia operativa e' Dose Mentale, ed e' protetta."* I modelli **rifiutano** uno script marcato `derived_from_transcript=True` o una copertina `replicates_competitor_layout=True`: l'anti-copia e' nel tipo, non nella prosa.
- **Dimensione:** 4.601 righe di Python, 11 agenti in `src/.../agents/`, 8 file di test.
- **PUNTO D'INGRESSO:** `pyproject.toml` dichiara `[project.scripts] yaf = "youtube_automation_factory.cli:app"` — si lancia con **`yaf`** dopo installazione, tramite Typer.
- **GIRA ANCORA? DORMIENTE.** Tutto il pacchetto (sorgenti e test) e' fermo al **2026-08-04**, 33 giorni fa. Nessun output datato prodotto da qui: la produzione reale passa dagli script di `02-AUTOMAZIONI-E-SCRIPTS`, non da questo pacchetto. E' la versione ordinata che la fabbrica sporca ha scavalcato.
- **DIPENDENZE ESTERNE:** `pydantic>=2.7`, `pydantic-settings`, `typer`, `playwright` opzionale. Dichiarate in `pyproject.toml`, quindi installabili.
- **CHI LO POSSIEDE:** `03-CONTENT-FACTORY` (dentro la voce YTAF del registro). NON orfano, ma il registro **non distingue** questo pacchetto dagli script sciolti: chi legge il registro crede che la fabbrica sia questa, e invece la produzione vera passa altrove.
- **COME SI AVVOLGE:** e' l'unico pezzo YouTube gia' avvolto bene (`yaf` come comando, Typer, tests). Il problema non e' l'avvolgimento: e' che nessuno lo usa.

### 2.7 Satelliti YouTube
- `assemble_piano_editoriale.py` (40 KB) + `generate_piano_editoriale_pdf.py` (24 KB) + `generate_calendario_md.py` + `build_candidate_pool.py` — la catena che ha prodotto il **piano editoriale 70 video** di Legami d'Amore: `memory/piano_editoriale_70.json` (109 KB, **2026-09-03 22:12**) e `memory/candidate_pool_70_20260826.json` (186 KB). **VIVO.**
- `copy_study_legamidiamore.py` / `copy_study_dosementale.py` + `memory/copy_intelligence_legamidiamore.json` (2026-09-03) — studio del copy per canale. **VIVO.**
- `channel_discovery.py`, `niche_discovery.py`, `youtube_hunter_playwright.py`, `thumbnail_analyzer.py`, `seo_score.py`, `cashcow_check.py` — ricerca nicchie e canali; output `memory/proposte_canali.json` e `proposte_nicchie.json` fermi al **2026-08-05/06**. **DORMIENTI.**
- `agents.py`, `regolatori.py` (24 KB), `memory.py`, `meta_agent.py`, `gate_agent.py`, `quality_gate.py`, `event_bus.py`, `self_improve.py`, `validate_schemas.py`, `ruflo_connector.py` — l'impalcatura APEX-7 locale, ferma tra il 2026-07-25 e il 2026-08-24.
- **~40 script `_*.py` datati 2026-09-03** (`_ads_on_single.py`, `_check_claims.py`, `_resume_video05_v4.py`, `_delete_stuck_video05.py`…) — non sono un motore: sono i **ferri chirurgici** di una giornata passata a sbloccare a mano video incastrati su YouTube Studio. Vanno archiviati, non censiti come sistema.
- `VIDEO-PRONTI/video-01..video-08` — la consegna: `video.mp4` + `copy.md` + `metadata.json`. **Otto video prodotti, l'ultimo il 2026-09-04.**
- `.claude/commands/avvia-yt.md` + `.claude/agents/credential-keeper.md` — la fabbrica ha un comando di Impero proprio (`/avvia-yt`) e un agente dedicato che legge `FLIKI_API_KEY` dal `.env` senza chiedere conferma.

### 2.8 VERIFICA DELL'ACCUSA — "nessun ecosistema nomina la fabbrica"

**L'accusa e' vera, ma va riformulata.** Comandi lanciati:

- `grep -ril "youtube-automation-factory\|YTAF" company/Ecosistemi/05-MULTI-BUSINESS/` -> **0 file**.
- `grep -ri "youtube" company/Ecosistemi/05-MULTI-BUSINESS/` -> **64 occorrenze** in 10+ file.

Cioe': `05-MULTI-BUSINESS` **parla molto di YouTube** e ha una sua filiera YouTube completa di sette agenti
propri — `Agenti/MB-YT-A02-niche-scout.md`, `MB-YT-A03-competitor-mapper.md`, `MB-YT-A04-keyword-miner.md`,
`MB-YT-A05-brandkit-builder.md`, `MB-YT-A06-calendar-planner.md`, `MB-YT-A09-opt-coord.md`, piu'
`Funzioni/T-niche-scout.md` — **ma non nomina mai il motore che quei compiti li esegue davvero**.

Il quadro reale, quindi, non e' "la fabbrica e' orfana": la fabbrica **e'** censita, in
`company/REGISTRO-IMPRESA.md` riga 52, sotto `03-CONTENT-FACTORY`. Il guasto e' un altro e piu' grave:
**due filiere YouTube parallele che non si conoscono.** Una scritta come agenti-documento in
`05-MULTI-BUSINESS` (niche scout, competitor mapper, keyword miner) e una scritta come Python funzionante in
`YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS` (`niche_discovery.py`, `channel_discovery.py`,
`seo_score.py`, `thumbnail_analyzer.py`) — **gli stessi identici mestieri, due volte**, e nessuno dei due lato
cita l'altro. Chi legge l'ecosistema 05 crede di dover ancora costruire cio' che in 02-AUTOMAZIONI-E-SCRIPTS
gira gia'.

---

## 3. FAMIGLIA `SKILL & Agenti/` — la piu' popolosa e la piu' disordinata

Conteggio per sottocartella (file `.py` | file totali), esclusi `node_modules/`, `__pycache__/`, `venv/`:

| .py | file tot | sottocartella |
|---:|---:|---|
| 271 | 38.793 | `Empire Studio Suite/` |
| 64 | 6.004 | `Workflow agency creative/` |
| 40 | 2.921 | `Workflow pubblicazione automatica/` |
| 22 | 145 | `caveman-extracted/` |
| 20 | 2.091 | `Orchestracion Layer - Problem solving/` |
| 17 | 298 | `apex7/` |
| 16 | 554 | `SKILL/` |
| 0 | 4.514 | `ruflo-main-extracted/` |
| 0 | 189 | `Copy-Workflow-manuale/` |
| 0 | 157 | `github-repos/` |
| 0 | 34 | `Skill Master Architecture/` |

Piu' **20 archivi `.zip`/`.tar.gz` sciolti nella cartella** (`Context-Engineering-main.zip`,
`Forge-caroselli-empire.zip`, `caroselli-forge.zip`, `ruflo-main.zip`, `sparc-main.zip`,
`impeccable-main.zip`, `nova-main.zip`, `vibing-main.zip`, `playwright-main.zip`,
`marketingskills-main.zip`, `stop-slop-main.zip`, `infinity-ui-main.zip`, `ai-video-main.zip`,
`cli-printing-press-main.zip`, `book-to-skill-master.zip`, `caveman-opencode-plugin.zip`,
`REPORT SITE - WORKFLOW.zip`, `apex7-ultra-grain-playwright-bridge*.tar.gz` x2,
`Copy-Workflow-manuale.zip`, `Orchestracion Layer - Problem solving.zip`) — aperti piu' avanti al §3.9.

### 3.1 Empire Studio — il motore che gira ADESSO
- **Percorso:** `SKILL & Agenti/Empire Studio Suite/empire-studio/`
- **Nome vero:** *Empire Studio* (v2.0), dichiarato nel `README.md`.
- **A cosa serve:** dal `README.md` — *"Workflow gerarchico per trasformare link grezzi (YouTube, TikTok, siti web, progetti/repo) in conoscenza operativa dentro la wiki di Digital Empire — con visione reale dei video, organizzazione a reparti, memory-first, CLI-only."* Il README dichiara anche di cosa e' la riparazione: *"la ricostruzione pulita (v2.0), nata dall'audit del primo tentativo che era in gran parte impalcatura: stub spacciati per 'fatti', video-watcher finto, pipeline senza codice, due copie divergenti."*
- **Dimensione:** 271 file `.py` nell'intera Suite, **6.433 righe di Python** nel solo `empire-studio/`; 38.793 file totali (gonfiati da 35 cartelle `runs/` con video e frame).
- **PUNTO D'INGRESSO:** **non c'e' un comando unico, ed e' voluto.** Il README: *"ATTIVAZIONE NATURALE — nessun comando. Non si digita niente di tecnico. Basta passare un link o chiedere a parole."* Il motore reale sta in 19 script di `scripts/`: `yt_ingest.py`, `frame_extractor.py`, `scene_detector.py`, `wiki_writer.py`, `validator.py`, `memory_manager.py`, `skill_factory.py`, `agent_factory.py`, `package.py`, `corso_ingest.py` / `corso_prepara.py` / `corso_trascrivi.py`, `save_to_memory_empire.py`, `ruflo_bridge.py`, `catalog_status.py`, `setup_check.py`, `generate_strategy_manifest.py`. Prerequisiti: `python scripts/setup_check.py`. Gate di chiusura: *"'fatto' finche' `python scripts/validator.py` non da' 0 violazioni."*
- **GIRA ANCORA? VIVO — e' il motore piu' caldo del repository.** Prova: la cartella `runs/` contiene **35 run**, e le ultime scrivono **oggi, 2026-09-06**: `runs/max18-v07-O2IDhISyy8Y/_parte-022-042.md`, `_transcript_full_0_330.txt`, `_scene_index.json` tutti datati 2026-09-06; `runs/max18-v09-NmoOZVTrTXA/_scene_index.json` 2026-09-06; `runs/max18-v01-second-brain-obsidian/_ancoraggi.txt`, `_componenti.txt`, `_grafo_analisi.py` 2026-09-06. Nove run `max18-*` aperte tra il 4 e il 6 settembre.
- **ANOMALIA DA DICHIARARE:** in `runs/max18-v09-NmoOZVTrTXA/` il video e' **`video.mp4.part` (94 MB)** — un download `yt-dlp` **interrotto a meta'**, mai completato, con le scene gia' estratte attorno. Una run appesa.
- **DIPENDENZE ESTERNE:** `yt-dlp` e `ffmpeg` obbligatori, `playwright` opzionale per il web (dichiarati nel README). Nessuna chiave API: e' l'unico motore grosso dell'Impero che **non spende** per girare.
- **CHI LO POSSIEDE:** censito **due volte**. `company/REGISTRO-IMPRESA.md` riga 44: *Empire Studio (ingestione video → knowledge) | 10-MEMORY (knowledge) + Reparto Competitor Research | WATCH-001 match check | ADR-002 (integrale, mai riassunti)*. E `company/skills-map.yaml` lo registra **in due voci distinte e sovrapposte**: `id: empire-studio` (riga 423) e `id: empire-studio-suite` (riga 544), entrambe con lo stesso percorso `SKILL & Agenti/Empire Studio Suite/`. NON orfano, ma **doppio in mappa**.
- **RUMORE NEL REGISTRO:** `REGISTRO-IMPRESA.md` righe 551-559 censiscono come skill attive nove file che stanno dentro `_Riferimenti-e-Archivio/_vecchio-tentativo-rotto/` — cioe' **il registro elenca come patrimonio proprio la versione che il README dichiara rotta e sostituita**.
- **COME SI AVVOLGE:** e' il caso piu' difficile del repository. Non ha un punto d'ingresso perche' l'ingresso e' Claude stesso. Perche' un comando dell'Impero lo lanci servirebbe un `run_studio.py <url>` che incateni ingest → frame → scene → forge → wiki e stampi una riga d'esito (`run_id`, `wiki_pages`, `violazioni_validator`); oggi l'esito si legge solo aprendo la cartella `runs/`.

### 3.2 Carousel Factory — `caroselli.py`
- **Percorso:** `SKILL & Agenti/Workflow agency creative/caroselli.py` (21.052 byte, **2026-08-31**)
- **Nome vero:** *Carousel Factory*, dal docstring.
- **A cosa serve:** dal docstring — *"UN comando, un argomento, un carosello nell'Arsenale."* Catena: `argomento -> copy (modello via API) -> piano slide -> render locale -> Arsenale Caroselli/<Prodotto>/<data>_<slug>/ -> GATE`. Il docstring dichiara anche cosa ha sostituito: *"Prima di questo file il flusso esisteva ma era in pezzi... Cinque passaggi manuali per un carosello, piu' un login interattivo e un captcha."*
- **Dimensione:** 64 file `.py` nella famiglia, **731 righe di Python** (il grosso dei 6.004 file totali sono gli ZIP e i PNG dell'Arsenale). Un test: `tests/test_caroselli.py`.
- **PUNTO D'INGRESSO:** chiarissimo, ed e' l'unico motore del repository che dichiara i propri codici d'uscita nel docstring: `python caroselli.py "<argomento>" [--prodotto Preventa] [--slide 6]` — *"Exit code: 0 ok | 1 gate fallito (carosello non valido) | 2 parametri/config errati | 3 errore di sistema."*
- **GIRA ANCORA? VIVO.** Prova: `Arsenale Caroselli/Preventa/2026-08-27_quanto-tempo-perdi-a-fare-un-preventivo/` e `.../2026-08-27_tradurre-a-mano-un-annuncio-tedesco-e-ri/` contengono `slide-01.html`, `copy.json`, `caption.txt` scritti il **2026-08-31**. Prima di quelli, un carosello completo 8 slide PNG 4K del 2026-08-06.
- **RAMO ROTTO DICHIARATO DAL CODICE STESSO:** il ramo Arena (browser) e' fermo, e il docstring elenca **tre guasti verificati, non ipotizzati**: *"`playwright_stealth` non e' installato (ogni script muore all'import), `ArenaAI/session_data/` non esiste (serve un login Google interattivo, ed e' gitignorato quindi non arriva col repo), e anche funzionando richiede attesa e sorveglianza umana per ogni run."* Il ramo locale e' stato scritto proprio per aggirarli, e `--engine arena` e' gia' predisposto per quando la sessione tornera'.
- **DIPENDENZE ESTERNE:** una API di modello per il copy (via `Agents/ai_client.py`, importato — ADR-003 wrap); `carousel-factory` (Puppeteer + template HTML) invocato come **processo esterno**. Per il ramo morto: `playwright_stealth` (mancante) e sessione Google in `ArenaAI/session_data/` (mancante).
- **CHI LO POSSIEDE:** **semi-orfano.** `company/REGISTRO-IMPRESA.md` conosce il reparto `03-CONTENT-FACTORY/Reparti/CF-R5-Visual-Design-Caroselli` (riga 120) e censisce un `tsconfig.json` della dashboard caroselli (riga 168), **ma non censisce mai `caroselli.py`**. `company/skills-map.yaml` registra due voci caroselli (righe 170 e 179) che puntano a **`caroselli/` e `Workfolw crea caroselli a/`, cioe' altre due cartelle**, non a questa. Il motore che produce davvero non e' in nessun registro col suo percorso.
- **COME SI AVVOLGE:** **e' gia' avvolto meglio di chiunque altro** — un argomento in ingresso, quattro codici d'uscita distinti, cartella di consegna deterministica. E' il modello da copiare sugli altri motori. Manca solo che il registro sappia che esiste.

### 3.3 `caroselli - agency/` — il cantiere di debug sotto la Carousel Factory
- **Percorso:** `SKILL & Agenti/Workflow agency creative/caroselli - agency/` (2026-08-06)
- **A cosa serve:** e' il progetto da cui `caroselli.py` importa `Agents/ai_client.py`. Contiene `Agents/` (copywriter, orchestrator, ai_client), `ArenaAI/` (arena_generator, read_arena_chat, setup_arena_session), `Core/browser_manager.py`, `GoogleDrive/drive_uploader.py` + `setup_drive_session.py`, e una `dashboard. Produzione caroselli Agency/` in TypeScript.
- **GIRA ANCORA? ROTTO nella meta' browser, VIVO come libreria.** Nove dei suoi file sono `debug_*.py` / `inspect_*.py` / `find_send_button.py`: sono i **ferri lasciati sul banco** dal tentativo di pilotare arena.ai, lo stesso muro contro cui ha sbattuto `arena_thumbnail.py` della fabbrica YouTube (§2.4). La parte che sopravvive e' `ai_client.py`, che gira ogni volta che gira `caroselli.py`.
- **DIPENDENZE ESTERNE:** `playwright_stealth` (mancante), sessione Google Drive in `GoogleDrive/`, sessione Arena.
- **CHI LO POSSIEDE:** `03-CONTENT-FACTORY / CF-R5`. Censito solo per un `tsconfig.json`.

### 3.4 `andrei-pascu-system/` — non e' un motore
- **Percorso:** `SKILL & Agenti/Empire Studio Suite/andrei-pascu-system/`
- **Contenuto reale, aperto:** **3 soli file, zero Python** — `LEGGIMI.md`, `playbook.md` (12 KB), `checklist_APSOC.md`, tutti fermi al **2026-07-25**. E' materiale di studio del competitor Andrei Pascu, non codice.
- **CHI LO POSSIEDE:** `company/skills-map.yaml` riga 434 lo registra come skill con percorso proprio. **Il registro lo chiama motore, ma non lo e'.**

### 3.5 `memory-empire/` dentro la Suite — due cartelle vuote di codice
- **Percorso:** `SKILL & Agenti/Empire Studio Suite/empire-studio/memory-empire/`
- **Contenuto reale:** due sole sottocartelle, `memory/` e `knowledge/`, **zero file `.py`**, ferme al **2026-07-19**. E' il deposito su cui scrive `scripts/save_to_memory_empire.py`, non un motore a se'.

### 3.6 Workflow pubblicazione automatica — L'ULTIMO METRO, misurato
- **Percorso:** `SKILL & Agenti/Workflow pubblicazione automatica/`
- **A cosa serve:** dal docstring di `pubblica.py` — *"UN comando per pubblicare una cartella di contenuti gia' pronti sul canale giusto (TASK-PUBLISHER-W1). La cartella e' un output gia' pronto (es. un prodotto dell'Arsenale Caroselli): slide_01.png ... slide_NN.png + caption.txt. Non genera contenuto, non tocca i motori: li WRAPPA (ADR-003)."*
- **Dimensione:** 40 file `.py`, **3.497 righe di Python**, 2.921 file totali. Piu' un **`DE_Publisher.exe` da 75,5 MB** (2026-07-19) — un eseguibile impacchettato dell'app, non codice sorgente.
- **PUNTO D'INGRESSO:** `python pubblica.py "<cartella>"` (dry-run VERIFICATO, default) / `--live` per pubblicare davvero. Esistono anche `app.py` (27 KB, GUI), `run_daily.py`, `setup_scheduler.py`, `alert.py` — tutti fermi al 2026-07-19.
- **GIRA ANCORA? DORMIENTE, e con la prova piu' pesante del censimento.** Il registro delle pubblicazioni, `published.json`, contiene **letteralmente `{}`** — 2 byte, ultima scrittura **2026-07-19**. Cioe': **questo motore non ha mai pubblicato niente, e non lo fa da 49 giorni.** `pubblica.py` invece e' stato riscritto il **2026-08-31**: qualcuno ha rimesso in ordine il braccio, ma non l'ha ancora usato.
- **AUTODIAGNOSI GIA' SCRITTA IN CASA:** `DIAGNOSI-PUBLISHER.md` (2026-08-27) e' un audit *"eseguito, non letto"*, e dichiara due guasti che qui vanno citati parola per parola perche' sono la ragione dell'Ultimo Metro:
  - **`Instagram/instagram_publisher.py::publish()` non puo' fallire.** *"Il `try/except` finale cattura ogni eccezione, la stampa e ritorna `None`: la funzione 'riesce' sempre, anche se non ha pubblicato niente. In piu' non fa login."*
  - **`main_orchestrator.py` non parte proprio.** *"IMPORT FAIL main_orchestrator -> OpenAIError: Missing credentials."* Catena: `main_orchestrator` → `Core/copy_generator` → `Core/AI_Team/ai_client` che istanzia `OpenAI(...)` **a livello di modulo** con `OPENROUTER_API_KEY`/`GROQ_API_KEY` assenti — muore all'import, prima di eseguire una riga. E *"stampa `FLUSSO COMPLETATO CON SUCCESSO!` incondizionatamente"*.
  - Cio' che invece **funziona verificato**: `Core/browser_manager.py` (Chrome 151 avviato), `scripts/ig_carousel_publish.py` (`is_ready() -> (True, '6 img OK')`, 6 immagini, caption 924 char su cartella Arsenale reale), la navigazione a instagram.com. `LinkedIn/linkedin_publisher.py` importa ma **mai eseguito end-to-end**, e la diagnosi si rifiuta di dichiararlo funzionante.
- **DIPENDENZE ESTERNE:** `OPENROUTER_API_KEY` / `GROQ_API_KEY` — **MANCANTI, ed e' questo che uccide l'orchestratore**. Sessione Instagram e sessione Google Drive in `Google_Drive/session_data/` e `Google Drive/session_data/` (**due cartelle quasi omonime, una con lo spazio e una con l'underscore**: sono due sessioni browser separate, e nessuna delle due e' dichiarata come quella buona). Playwright + Chrome reale.
- **CHI LO POSSIEDE:** **ORFANO.** Ne' `company/REGISTRO-IMPRESA.md` ne' `company/skills-map.yaml` censiscono `pubblica.py` o la cartella `Workflow pubblicazione automatica/`. Esiste solo una skill omonima `/workflow-pubblicazione-auto` nell'elenco skill di Claude, e una skill locale `.claude/skills/social-publisher/` **dentro** la cartella stessa.
- **COME SI AVVOLGE:** e' l'unico motore che **ha gia' il contratto giusto** (dry-run verificato di default, `--live` esplicito, exit 0 solo su PASS reale, *"nessun PASS finto"*) e **non viene chiamato da nessuno**. Perche' l'Impero lo lanci non serve scrivere codice: serve una chiave modello nel `.env` e che il comando che chiude la Carousel Factory passi la cartella prodotta a `pubblica.py --live`. **I due motori sono a un argomento di distanza e nessuno li ha collegati.**

### 3.7 `apex7/` — la copia autonoma di APEX-7 (non quella della fabbrica YouTube)
- **Percorso:** `SKILL & Agenti/apex7/`
- **A cosa serve:** dal docstring di `main.py` — *"APEX-7 Main Entry - Sistema Completo Adaptive Prompt Execution"*. Orchestratore async a 6 agenti che importa `orchestrator/ruflo_core.py::RuFLOOrchestrator` e monta `PlannerAgent`, `WriterAgent`, `AnalystAgent`, `CriticAgent`, `RefinerAgent`, `MetaAgent`.
- **Dimensione:** 17 file `.py`, **3.383 righe di Python**, 298 file totali.
- **PUNTO D'INGRESSO:** `main.py` (`run_apex7_system(user_input, context)`), piu' `run_demo.py` per la prova a vuoto.
- **GIRA ANCORA? DORMIENTE.** Tutto il sistema e' fermo al **2026-08-23** (14 giorni). Ha pero' girato davvero: `memory/data/` contiene `decision_log.db` (SQLite, 61 KB), `architecture_snapshots.json`, `compressed_knowledge.json`, `strategy_store.json` e **cinque `working_memory_<uuid>.json`**, uno da 142 KB e uno da 101 KB — sessioni reali, non stub. L'ultimo prodotto e' `outputs/carousel/Content_Factory_per__20260805_064447/` con `slides_copy.json` e 8 coppie `slide_NN_copy.json` + `slide_NN_prompt.txt`, del **2026-08-05**.
- **DUPLICAZIONE DA DICHIARARE:** questo APEX-7 **non e'** l'`apex7_orchestrator.py` della fabbrica YouTube (§2.1), ne' l'ecosistema `company/Ecosistemi/11-APEX-7-CORE`. Sono **tre APEX-7 distinti** nello stesso repository, con memorie separate (`memory/data/` qui, `memory/*.json` la'), che non si parlano.
- **DIPENDENZE ESTERNE:** `requirements_playwright.txt` presente; `playwright_bridge/` e `arena_generator.py` puntano di nuovo ad arena.ai — la terza copia dello stesso tentativo (dopo §2.4 e §3.3).
- **CHI LO POSSIEDE:** non censito col suo percorso. **ORFANO** (l'ecosistema `11-APEX-7-CORE` esiste, ma parla dell'APEX-7 di `company/`, non di questa cartella).
- **COME SI AVVOLGE:** `main.py` e' gia' una funzione con ingresso e contesto; basterebbe un `if __name__ == "__main__"` con argparse e un dump JSON dell'esito. Ma prima va deciso **quale dei tre APEX-7 e' quello vero**, altrimenti si avvolge un doppione.

### 3.8 NERVE-SOLVE / Orchestration Layer — architettura enorme, motore appena nato
- **Percorso:** `SKILL & Agenti/Orchestracion Layer - Problem solving/`
- **A cosa serve:** e' l'Orchestration Layer 1 di Digital Empire (motore di problem solving). La cartella e' quasi tutta **documentazione di progetto**: 15 file `.md` di architettura, audit, validazione e piani di produzione L1-L7 (`ARCHITETTURA_DEFINITIVA_NERVE-SOLVE_..._v2.1.md` e `v2.2`, `AUDIT_..._v2.0.md`, `RAPPORTO_VALIDAZIONE_...v2.1/v2.2`, `INGESTION_REPORT_...`).
- **Dimensione:** 20 file `.py`, **3.414 righe di Python**, 2.091 file totali. **Ma le righe di Python sono quasi tutte concentrate in un solo modulo appena abbozzato:** `implementation/src/orchestration_layer/constitutional/` (`kernel.py`, `canonical.py`, `models.py`, `ports.py`, `signing.py`, `errors.py`) piu' tre script `verify_*.py` e i test.
- **PUNTO D'INGRESSO:** **NON CE N'E' UNO.** Non esiste un `main`, un CLI o un comando. Si entra solo dai tre `implementation/scripts/verify_*.py` (`verify_constitution_candidate.py`, `verify_m1_authority_decision.py`, `verify_m3_response.py`), che sono verifiche, non esecuzione.
- **GIRA ANCORA? DORMIENTE.** Tutto fermo al **2026-08-23**. Nessun output di produzione: solo `validation/` e `implementation/`. Il rapporto di sproporzione e' il dato: **quindici documenti di architettura contro un unico package `constitutional/` implementato.**
- **DIPENDENZE ESTERNE:** nessuna chiave; e' logica pura piu' test.
- **CHI LO POSSIEDE:** esiste la skill `/nerve-solve` nell'elenco skill di Claude, quindi la conoscenza e' raggiungibile. La **cartella** non e' censita nei registri. **ORFANA come codice.**
- **COME SI AVVOLGE:** oggi non si avvolge: non c'e' niente da lanciare. Serve prima che qualcuno decida se questo layer va costruito o archiviato — sta consumando spazio in mappa senza produrre.

### 3.9 I 19 ARCHIVI `.zip` di `SKILL & Agenti/` — aperti uno per uno
Ordine ricevuto: **se trovi archivi, dichiara cosa contengono.** Ogni riga qui viene da
`zipfile.ZipFile(...).namelist()` eseguito sull'archivio, non dal nome del file. **Peso complessivo: ~379 MB.**

| archivio | peso | data | file | .py | cosa contiene davvero |
|---|---:|---|---:|---:|---|
| `Forge-caroselli-empire.zip` | 91 MB | 2026-08-05 | 112 | 17 | **la cartella `apex7/` gia' estratta al §3.7**, piu' i due `apex7-ultra-grain-playwright-bridge*.tar.gz` |
| `Orchestracion Layer - Problem solving.zip` | 88 MB | 2026-08-22 | 2.130 | 20 | **la cartella §3.8 gia' estratta**, ma con dentro anche `.claude-flow/policy/state.json` e un'installazione `gh 2.97.0` — un ambiente di lavoro intero, non un progetto |
| `caroselli-forge.zip` | 72 MB | 2026-08-05 | 89 | 16 | **quasi identico a `Forge-caroselli-empire.zip`**: stesso `apex7/`, un tar.gz invece di due |
| `playwright-main.zip` | 41 MB | 2026-05-22 | 3.564 | 2 | repo pubblico della skill `playwright-dev` |
| `Context-Engineering-main.zip` | 37 MB | 2026-05-22 | 357 | 31 | repo pubblico: gli agenti `alignment.agent`, `research.agent`, `test.agent`… **gia' installati come skill di Claude** |
| `cli-printing-press-main.zip` | 33 MB | 2026-05-22 | 3.921 | 7 | repo pubblico `printing-press` — gia' skill installata |
| `impeccable-main.zip` | 27 MB | 2026-05-22 | 2.149 | 0 | repo pubblico `impeccable` — gia' skill installata |
| `ruflo-main.zip` | 27 MB | 2026-05-29 | 5.921 | 0 | repo pubblico `ruflo` — **gia' estratto accanto in `ruflo-main-extracted/` (4.514 file)** |
| `Copy-Workflow-manuale.zip` | 18 MB | 2026-05-26 | 46 | 0 | **gia' estratto accanto in `Copy-Workflow-manuale/` (189 file)** |
| `sparc-main.zip` | 15 MB | 2026-05-31 | 511 | **88** | repo pubblico SPARC — **il singolo archivio con piu' Python**; gia' skill `/sparc-methodology` |
| `REPORT SITE - WORKFLOW.zip` | 1,1 MB | 2026-08-05 | 133 | 12 | `lp-audit-skill/` + una cartella `formazione/` (copywriting landing, funnel, psicologia colori) |
| `marketingskills-main.zip` | 896 KB | 2026-05-22 | 465 | 0 | repo pubblico delle skill marketing — gia' installate (`ads`, `cro`, `seo-audit`…) |
| `vibing-main.zip` | 804 KB | 2026-05-31 | 101 | 0 | repo pubblico, app con deploy Fly.io |
| `caveman-opencode-plugin.zip` | 272 KB | 2026-06-05 | 210 | 22 | plugin caveman — **gia' estratto accanto in `caveman-extracted/`** e gia' plugin installato |
| `infinity-ui-main.zip` | 260 KB | 2026-05-31 | 94 | 0 | repo UI (gpt-engineer), mai integrato |
| `ai-video-main.zip` | 248 KB | 2026-05-31 | 12 | 1 | repo `app.py` per video AI, mai integrato |
| `nova-main.zip` | 92 KB | 2026-05-31 | 98 | **56** | repo `nova` con `conjecture/` — 56 file Python, **mai estratto e mai citato in nessun registro** |
| `book-to-skill-master.zip` | 32 KB | 2026-05-23 | 9 | 1 | repo `book-to-skill` — gia' skill installata |
| `stop-slop-main.zip` | 12 KB | 2026-05-23 | 9 | 0 | repo `stop-slop`, sola `SKILL.md` |

**Cosa dicono questi archivi, messi in fila:**
1. **Nessuno e' un bot nascosto** — a differenza del caso `08-STREAM-S7-BOT`, qui non c'e' un sistema vivo dentro uno `.zip`. Sono materia prima scaricata.
2. **Cinque sono doppioni gia' estratti accanto** (`ruflo`, `Copy-Workflow-manuale`, `caveman`, e i due `caroselli-forge`/`Forge-caroselli-empire` che contengono `apex7/`): **~209 MB di pura duplicazione**.
3. **Nove sono repo pubblici gia' diventati skill installate** — tenerli qui non aggiunge nulla.
4. **Due sono materiale mai aperto:** `nova-main.zip` (56 file `.py`) e `infinity-ui-main.zip`. Sono l'unica cosa in questa lista che nessuno ha mai guardato.

---

## 4. `empire/` — IL RUNTIME. La risposta alla domanda "come si avvolge"

- **Percorso:** `c:\Users\Utente\Desktop\qui tutto\Digital Empire\empire\`
- **Nome vero:** *Core Runtime di Digital Empire*.
- **A cosa serve:** dal `README.md`, che dichiara anche il problema che risolve — *"Il livello che mancava. L'azienda aveva 1.267 file `.md` e 0 file `.py`: un organigramma completo, nessun processo. Questo pacchetto rende gli artefatti descritti in Markdown interrogabili, validabili e misurabili da codice."* E la riga che conta piu' di tutte: **"Non esegue il lavoro. Lo rende osservabile."**
- **Dimensione:** 97 file `.py`, **14.628 righe di Python**, 122 file totali — cioe' **e' quasi tutto codice**, senza zavorra. E' la densita' piu' alta del repository.
- **PUNTO D'INGRESSO:** `python -m empire <comando>` (`__main__.py` -> `cli.py::main`). Sette comandi nel core: `status`, `paths`, `links`, `art8`, `adr001`, `conform`, `doctor`. **Contratto gia' dichiarato nel README:** *"Ogni comando di lettura accetta `--json`. Exit code: 0 ok · 1 finding bloccanti · 2 errore interno."*
- **ARCHITETTURA A LOTTI — il pezzo piu' intelligente del repository:** `cli.py` non conosce i sottocomandi degli altri. Li carica per plugin, con un commento che spiega perche': *"Ogni lotto aggiunge i propri sottocomandi nel PROPRIO modulo, esponendo `register(sub)`. Cosi' nessuno modifica questo file e non ci sono collisioni di merge tra Max, Gael e Gemini."* I sette moduli, con l'autore scritto accanto nel codice: `empire.loader_cli` (Gael — agents, ecosystems, workflows, skills), `empire.index_cli` (Gael — index, find, show), `empire.flow.cli` (Gael), `empire.memory.cli` (Claude — mem *), `empire.inspect.cli` (Claude), `empire.registry.cli` (Gemini), `empire.dash.cli` (Gemini). Un lotto mancante non rompe niente: `except ImportError: continue  # lotto non ancora costruito: normale`.
- **GIRA ANCORA? VIVO.** Prova: `empire/memory/` scritto il **2026-09-03**; `WORKFLOW-ESTATE/06-DASHBOARD-E-METRICHE/DASHBOARD.md` rigenerato il **2026-09-05** (e' l'uscita di `empire dash`); la skill `/avvia-estate-wk` esiste e dichiara di *"rigenerare la dashboard, valutare i gate, misurare gli agenti, contare le tracce"*.
- **DIPENDENZE ESTERNE:** `requirements.txt` presente; **nessuna chiave API, nessuna sessione browser, nessun credito**. E' l'unico motore grosso che non puo' rompersi per una credenziale scaduta.
- **CHI LO POSSIEDE:** `company/REGISTRO-IMPRESA.md` riga 84: *"`empire/` (core runtime Python — completato via LMarena, GEM-01) | MAX | Claude (gate) · esecutore LMarena/Antigravity · Governo: ADR-003 wrap + ADR-008"*. **NON orfano, e con proprietario nominale: MAX.**
- **COME SI AVVOLGE:** **non va avvolto: e' l'involucro.** E' gia' costruito per ricevere i motori altrui — un motore che espone `register(sub)` diventa un sottocomando `python -m empire <x>` senza toccare una riga di `cli.py`. **Il guasto dell'Impero non e' che manchi un posto dove agganciare i motori: e' che nessuno dei motori dei paragrafi 2 e 3 si e' mai agganciato qui.** Carousel Factory, publisher, Empire Studio, fabbrica YouTube: nessuno espone `register(sub)`.

## 5. `WORKFLOW-ESTATE/` — il cervello di campagna, pilotato da `empire`
- **Percorso:** `WORKFLOW-ESTATE/`
- **A cosa serve:** da `AVVIO-OPERATIVO.md` — *"Il cervello della campagna estiva. Operativo da: 2026-07-27. Questo file e' il bottone di accensione: apri qui, sai in 10 secondi cosa fare e come farlo partire."*
- **Dimensione:** 251 file `.py` contati sull'albero, **5.690 righe di Python**, 8.403 file totali. Nove cartelle numerate `01-FLUSSI-E-PIANI` ... `07-VIDEO-RUN`, piu' `forge-run-2026-07-22T10-21-00`.
- **PUNTO D'INGRESSO:** **non e' un suo file — sono tre comandi del runtime `empire`**, elencati in `AVVIO-OPERATIVO.md`: `python -m empire estate` (*"lo STATO VERO: cosa e' finito, cosa e' fermo, di chi e'"*), `python -m empire forge scan` (*"gli AGENTI: quanti operativi, quali da promuovere"*), `python -m empire trace stato` (*"la MEMORIA: decisioni, errori, lezioni registrate"*). Piu' la skill `/avvia-estate-wk` e `02-AUTOMAZIONI-E-SCRIPTS/run_checkpoint_eod.bat`.
- **GIRA ANCORA? DORMIENTE, con un solo segno di vita recente.** Il codice e la memoria sono fermi al **2026-07-25 / 2026-07-29** (`memory_manager.py` 2026-07-25, `errors/` 2026-07-29, `decisions/`, `performances/`, `sessions/` 2026-07-28). L'unico file aggiornato e' `06-DASHBOARD-E-METRICHE/DASHBOARD.md`, **2026-09-05** — cioe' **la dashboard viene ancora rigenerata su una campagna che non produce piu' da 40 giorni.** `CANTIERE.md` fermo al 2026-07-31, `AZIONI-MAX.md` e `lead.csv` al 2026-07-25/28.
- **DIPENDENZE ESTERNE:** il runtime `empire/` (che e' vivo), nessuna chiave propria.
- **CHI LO POSSIEDE:** censito — `empire art8 WORKFLOW-ESTATE` e `empire conform WORKFLOW-ESTATE` sono negli esempi del README di `empire/`, cioe' e' un artefatto sorvegliato dal runtime. **NON orfano.**
- **COME SI AVVOLGE:** e' **l'unico caso del repository gia' avvolto correttamente** — non ha un suo lanciatore, si interroga dal runtime. E' il modello che i motori dei §2-3 non hanno seguito.

---

## 6. `DIGITAL-EMPIRE/` — il workshop estate, e il TERZO cervello che dice le stesse cose

- **Percorso:** `DIGITAL-EMPIRE/`
- **Nome vero:** *DIGITAL-EMPIRE / ESTATE-2026 REVENUE WORKSHOP*.
- **A cosa serve:** dal `README.md` — *"Il piano estate trasformato in workflow eseguibile: reparti, agenti, skill, memoria, gates. Costruito il 21/07/2026 da CHIEF-FORGE."* Otto cartelle numerate `00-MEMORY` ... `07-CONTROL`.
- **Dimensione:** 125 file `.py`, **14.679 righe di Python**, 6.704 file totali.
- **PUNTO D'INGRESSO:** `python3 00-MEMORY/memory_manager.py status` (piu' `03-WORKFLOWS/workflows.yaml` per l'orchestrazione macchina). **Non e' un motore di produzione: e' un motore di memoria e di gate.**
- **GIRA ANCORA? DORMIENTE.** Tutto fermo tra il **2026-07-21 e il 2026-07-25**. Il README stesso e' datato: manda Max a decidere *"prezzo Manuale OGGI h20:00"* del 21 luglio, e Claude a fare il *"Batch copy 21/07 sera"*. E' un cruscotto congelato su una giornata di 47 giorni fa.
- **ANOMALIA DI DATA:** tre cartelle (`01-PLANNING/`, `02-ARCHITECTURE/`, `06-NERVOUS-SYSTEM/`) hanno mtime **1980-01-02** — timestamp azzerato, tipico di file estratti da un archivio ZIP che non conservava le date. Quelle cartelle non sono mai state toccate dopo l'estrazione.
- **DUPLICAZIONE GRAVE:** `05-SKILLS/` contiene **`content-forge2.0`, `master-build-architecture` e `ruflo` clonati** — e le stesse tre cartelle esistono **identiche nella radice del repository**. Il README lo ammette senza girarci attorno: *"(clonati)"*. Sono la seconda copia di tre sistemi interi.
- **TERZA SOVRAPPOSIZIONE:** questo e' il **terzo** impianto memoria+gate del repository, dopo `company/Memory/` e `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/memory_manager.py` — e i due `memory_manager.py` (qui e in WORKFLOW-ESTATE) sono due file distinti che fanno lo stesso mestiere.
- **DIPENDENZE ESTERNE:** nessuna chiave; `ruflo` clonato dipende dal server MCP `claude-flow`, che **in questa sessione non si connette** (`CONNECT_TIMEOUT` dopo 30 s).
- **CHI LO POSSIEDE:** censito due volte. `company/REGISTRO-IMPRESA.md` riga 81: *"`DIGITAL-EMPIRE/` (workflow estate NUOVO, sostituisce planning-workshop+workflows+ESTATE-WORKSHOP*) | MAX (import) → Chief-Forge (build originale)"*, e `company/skills-map.yaml` riga 517 come `digital-empire-estate-workflow`. **NON orfano.**
- **NOTA CHE CONTA:** il registro lo chiama *"workflow estate NUOVO"*, ma esiste **anche** `WORKFLOW-ESTATE/` (§5), che si dichiara *"operativo da 2026-07-27"* — cioe' **sei giorni dopo** questo. Due workshop estate paralleli, entrambi fermi, ciascuno convinto di essere quello buono.
- **COME SI AVVOLGE:** non ne vale la pena finche' non si decide quale dei due workshop estate sopravvive. Avvolgerli entrambi significherebbe dare all'Impero due comandi che rispondono in modo diverso alla stessa domanda.

---

## 7. FAMIGLIA `Clienti/` — l'unico codice del repository che un cliente paga

Quattro cartelle, contate: `EXPONIUM/` (49 `.py`, 811 file, fermo al **2026-06-04**),
`Prof Autocad/` (26 `.py`, 8.888 file, **2026-09-02**), `preventivo-exponium/` (0 `.py`, 234 file, 2026-08-23),
`presentazione-empire/` (0 `.py`, 574 file, 2026-05-20).

### 7.1 PreventivoForge — VIVO, consegnato quattro giorni fa
- **Percorso:** `Clienti/Prof Autocad/preventivo-forge/` (sorgente) + `Clienti/Prof Autocad/CONSEGNA-NOVACAR-2SET2026/PreventivoForge-Novacar-v2.2.zip` (consegna).
- **A cosa serve:** genera preventivi auto per il concessionario Novacar leggendo gli annunci di **mobile.de** e traducendoli dal tedesco. Moduli reali in `implementation/`: `ai_translate.py`, `parser.py`, `dealers.py`, `glossary_de_it.py`, `cdp.py`, `archivio.py`, `licenza.py`.
- **Dimensione:** **3.583 righe di Python** in `preventivo-forge/`.
- **PUNTO D'INGRESSO:** per il cliente e' **`PreventivoForge.exe`**, non un comando Python: lo ZIP di consegna contiene **1.979 file, 13 `.py` e 3 `.exe`**, con `_internal/` (numpy, cryptography, playwright, fontTools) — un pacchetto PyInstaller autonomo. In casa si entra da `implementation/`.
- **GIRA ANCORA? VIVO — ed e' l'unico motore del repository con un guasto esterno gia' riparato.** Prova, da `CONSEGNA-NOVACAR-2SET2026/LEGGIMI.txt` del **2026-09-02**: *"A fine agosto mobile.de ha rifatto il proprio sito e ha cambiato il modo in cui pubblica i dati degli annunci. Le versioni precedenti dell'app leggevano i dati nel 'vecchio' formato: da quel cambio in poi non li trovavano piu' e ogni preventivo finiva con 'Non riuscito'. Questa versione legge il NUOVO formato di mobile.de (e continua a leggere anche il vecchio, per sicurezza)."* Cioe': il fornitore ha rotto il motore a fine agosto, e **entro il 2 settembre era gia' uscita la v2.2 che lo ripara**. Nessun altro motore dell'Impero ha questo tempo di reazione.
- **Le run vecchie** (`preventivo-forge/runs/AF-20260713-*`, `logs/AF-20260713-*.log`) sono di luglio: la produzione reale ora avviene **sulla macchina del cliente**, non qui — ed e' per questo che qui non si vedono log recenti.
- **DIPENDENZE ESTERNE:** `.env` (dentro lo ZIP di consegna), `licenze.config.json` (**kill-switch abbonamento**), `browser-profile/`, Playwright impacchettato, mobile.de come fonte dati — **la dipendenza fragile: e' cambiata una volta e ricambiera'**.
- **CHI LO POSSIEDE:** censito bene, due volte. `company/REGISTRO-IMPRESA.md` riga 40: *"PreventivoForge (+ fabbrica `/nuovo-concessionario`, kill-switch licenze) | 01-AGENCY / A4-Delivery + S1/S6 dossier 16 | Gate IMG/R + regole-check + A10"*. `company/skills-map.yaml` riga 535, con nota: *"PRODOTTO LIVE (Novacar consegnato)"*. **NON orfano.**
- **RUMORE NEL REGISTRO:** le righe 163 e 264 di `REGISTRO-IMPRESA.md` censiscono come "dashboard" e "skill" dell'Impero **due file interni della libreria Playwright impacchettata** (`.../driver/package/lib/vite/dashboard/index.html`, `.../cli-client/skill/SKILL.md`). Sono file di terze parti finiti in registro per scansione automatica.
- **COME SI AVVOLGE:** e' l'unico motore **che non deve essere avvolto dall'Impero**: gira a casa del cliente. Cio' che l'Impero deve poter lanciare e' la *fabbrica* (`/nuovo-concessionario`) e il *kill-switch* licenze, non il preventivo.

### 7.2 EXPONIUM — cantiere cliente fermo
- **Percorso:** `Clienti/EXPONIUM/` — 49 file `.py`, 811 file, **fermo al 2026-06-04 (94 giorni)**.
- **Contenuto reale, aperto:** `MASTER_PLAN.md`, `GAEL_TASKS.md`, `GIORNATA.md`, `CLAUDE_CODE_SESSIONS.md`, `CLAUDE.md`, `sync.ps1`, piu' tre sottosistemi: `content-factory/`, `outreach/`, `shared/`. E' un **monorepo cliente in miniatura**, con la sua governance separata.
- **GIRA ANCORA? DORMIENTE.** Nessun output dopo il 4 giugno. Accanto, `Clienti/preventivo-exponium/` (0 `.py`) e' stato toccato il **2026-08-23**: la relazione col cliente e' viva, il codice no.
- **CHI LO POSSIEDE:** **ORFANO.** Ne' `REGISTRO-IMPRESA.md` ne' `skills-map.yaml` censiscono `Clienti/EXPONIUM/`. 49 file Python di un cliente reale, fuori da ogni registro.
- **COME SI AVVOLGE:** prima va deciso se il cliente e' ancora attivo. Avvolgere un cantiere chiuso e' spreco.

---

## 8. `Crea siti/` — Web Creation System: 19 agenti, un solo file eseguibile
- **Percorso:** `Crea siti/`
- **A cosa serve:** dal `README.md` — *"Digital Empire — Web Creation System. Navigazione master del sistema. Tutto il sistema e' qui."* Dichiara **19 agenti AI in 6 categorie** (`orchestrators/`, `market/` 5 sub-agenti, `omega/` 2, `site-build/` 3, `site-copy/` 3, `site-qa/`), piu' `skills/`, `system/` (5 SOP: ACTIVATION-GUIDE, ARCHITETTURA-SISTEMA-SITE, SOP-MARKETING, SOP-OPUS, SOP-SITE).
- **Dimensione:** 15 file `.py`, **3.865 righe di Python**, 399 file totali.
- **DOVE STA DAVVERO IL PYTHON (aperto, non dedotto):** quasi tutto **non e' del sistema siti**. E' dentro `skills/market/scripts/` (`analyze_page.py`, `competitor_scanner.py`, `generate_pdf_report.py`, `social_calendar.py`) e `skills/skill-creator/scripts/` (`package_skill.py`, `aggregate_benchmark.py`, `generate_report.py`, `improve_description.py`) — cioe' **copie locali delle skill `market` e `skill-creator` gia' installate in Claude**. L'unico Python scritto per questo progetto e' **un solo file**: `Siti CCM/builder.py`, 18 righe utili — carica `data.json`, renderizza `template.html` con Jinja2, scrive `index.html`. Nient'altro.
- **PUNTO D'INGRESSO:** **non esiste per il sistema, esiste per il sito.** I 19 "agenti" sono file Markdown, si attivano da Claude (skill `/site-build`, `/opus`, `/website-creator`). L'unico comando reale e' `python builder.py` dentro `Siti CCM/`.
- **GIRA ANCORA? Il sistema e' DORMIENTE, il sito e' VIVO.** `README.md`, `OPUS-CONTEXT.md`, `agents/`, `skills/`, `system/` sono fermi al **2026-03-29** (161 giorni). Ma `Siti CCM/` e' del **2026-08-25**: `index.html` (65 KB), `template.html` (36 KB), `index_empire.html`, piu' `ccm-elite-ultimate/`, `ccm-full-empire/`, `ccm-sale-page-empire/`, `ccm-webinar/`, `emails/`, `CONTESTO/`. Cioe' **il sito CCM si costruisce ancora, ma senza passare dal sistema che era stato scritto per costruirlo.**
- **SEGNO DI DISORDINE:** in `Siti CCM/` convivono `index.html`, `index - Copia.html` (byte per byte identico, 65.653 byte entrambi), `index_backup.html` e `index_empire.html`. Quattro versioni della stessa pagina, nessuna dichiarata come quella buona.
- **DIPENDENZE ESTERNE:** `jinja2` per `builder.py`. Le skill copiate hanno le loro (`generate_pdf_report.py` richiede il motore PDF).
- **CHI LO POSSIEDE:** **ORFANO come cartella.** Nessun registro censisce `Crea siti/`. Esistono le skill `/site-build`, `/site-copy`, `/site-qa`, `/opus`, `/website-creator`, `/empire-premium-style` nell'elenco skill di Claude — ma puntano alle skill installate, non a questa cartella.
- **COME SI AVVOLGE:** `builder.py` e' gia' un comando (`python builder.py`), gli manca solo di accettare il percorso invece di leggere la cartella corrente. Il "sistema a 19 agenti" invece non e' avvolgibile: e' documentazione, e va o riattivato come skill o archiviato.

---

## 9. `Agenti/Agency/` — il PRIMO motore outreach, l'antenato dimenticato
- **Percorso:** `Agenti/Agency/`
- **A cosa serve:** dal docstring di `orchestrator/run.py` — *"Orchestrator — Digital Empire Agency. Punto di ingresso unico per tutte le pipeline."* Quattro pipeline dichiarate nell'uso: `--pipeline no-website` (citta' + settore), `cro-funnel` (url), `ai-implementation`, `full`.
- **Dimensione:** **CORREZIONE DI CONTEGGIO.** La mappa preliminare dava 42 `.py` per `Agenti/`; il conteggio corretto e' **3.192 file `.py` in totale, ma 3.150 stanno in `Agenti/.venv/Lib/site-packages/`** (un virtualenv completo con dentro l'SDK `anthropic`, `pydantic`, ecc.) — che va escluso. **Il codice vero e' 42 file `.py` per 10.456 righe**, di cui `scripts/generate_pdf_report.py` da solo ne fa 741.
- **PUNTO D'INGRESSO:** `python run.py --pipeline <nome> --citta "<x>" --settore "<y>"`, dichiarato nel docstring. E' un ingresso pulito con argomenti espliciti.
- **GIRA ANCORA? DORMIENTE, ed e' il piu' vecchio del repository.** Tutto fermo tra il **2026-03-07 e il 2026-03-18** — **172 giorni**. Ma ha prodotto sul serio: `output/` contiene **almeno 20 run reali numerate** (`run_01_Milano_ristoranti`, `run_18_Reggio_Calabria_ristoranti`, `run_19_Parma_fisioterapisti`, `run_20_Messina_estetiste`…), piu' `process_log.txt` e `recovered/`. Venti citta', venti settori, marzo 2026.
- **PERCHE' CONTA:** e' **l'antenato di `Outreach/`** (censito nel file 04). Fa lo stesso mestiere — trovare aziende senza sito in una citta' e un settore, qualificarle, scrivere. Ha `outreach/implementation/qualify_leads.py`, `draft_emails.py`, `search_ads_leads.py`, `search_ai_prospects.py`, `import_leads_finder.py`; `sub-agents/no-website/scraper.py`. Nessuno dei due sistemi cita l'altro.
- **DIPENDENZE ESTERNE:** `requirements.txt` presente (2026-03-08); `.venv/` con l'SDK `anthropic` gia' installato — **una chiave API attesa**; Apify (`process_apify_data.py`).
- **CHI LO POSSIEDE:** **ORFANO.** Nessun registro censisce `Agenti/`. Un motore con venti run di produzione documentate, fuori da ogni mappa.
- **COME SI AVVOLGE:** ha gia' il contratto giusto (`run.py --pipeline`), gli manca solo un `--json` d'uscita. Ma prima va deciso se sopravvive lui o `Outreach/`: **sono due risposte alla stessa domanda, e la seconda e' piu' recente.**

## 10. `System OMEGA/` — generatore di progetti e skill
- **Percorso:** `System OMEGA - Creazione proggetti e skill per Claude/`
- **A cosa serve:** genera progetti e skill per Claude secondo la metodologia OMEGA. Documenti di governo: `Archittetatura Progetti e skill.md`, `CLAUDE.md`, `REGOLE.md`.
- **Dimensione:** 42 file `.py`, **14.583 righe**, 196 file totali.
- **DOVE STA IL PYTHON (aperto):** **non e' suo.** Sta in `.claude/skills/skill-creator/scripts/` (`package_skill.py`, `run_eval.py`, `run_loop.py`, `quick_validate.py`, `aggregate_benchmark.py`, `generate_report.py`, `improve_description.py`) — cioe' **la skill `skill-creator` copiata dentro il progetto**, la stessa gia' copiata in `Crea siti/skills/skill-creator/` (§8) e gia' installata come skill di Claude. **Tre copie della stessa skill.**
- **PUNTO D'INGRESSO:** **non e' Python.** E' la skill `/omega-create project` / `/omega-create skill`, che lancia l'agente `omega-executor` (con `omega-verifier` che approva ogni file generato). Il motore e' Claude, il codice e' contorno.
- **GIRA ANCORA? INCERTO.** Ha una cartella `Output/` e una `Attività temporanea/`, ma il sistema e' fatto di prompt e regole: **un censimento a indizi di file non puo' dire se una skill viene invocata.** Gli agenti `omega-executor` e `omega-verifier` risultano registrati e attivabili.
- **CHI LO POSSIEDE:** censito come skill (`/omega-create`) e come due agenti. La **cartella** non e' nei registri di `company/`.
- **COME SI AVVOLGE:** e' gia' avvolto nel modo giusto per la sua natura — un comando di Claude. Non serve un CLI.

## 11. `scripts/` — la cassetta degli attrezzi di EMPERATOR (viva, ieri)
- **Percorso:** `scripts/` (radice)
- **A cosa serve:** 15 file `.py` + 4 `.ps1`, **19 file in tutto**, nessuna zavorra. Sono gli strumenti che governano il lavoro quotidiano, non un prodotto.
- **GIRA ANCORA? VIVO — e' il codice piu' recente del repository dopo Empire Studio.** Date reali: `test_gate_battito.py`, `gate_battito_hook.py`, `emperator_hook.py`, `checkpoint.py`, `verifica_recap.py` tutti **2026-09-05**; `emperator_boot.py` 2026-09-04; `task_codice.py`, `tesoreria.py`, `peso_skill.py`, `ultimo_metro.py`, `cerca_wiki.py` **2026-09-03**; `verify-agents.py`, `verify-skills.py` 2026-09-01; `empire-sync.ps1` 2026-08-31. Solo `gen-empire.py`, `verify-empire.ps1`, `agency-trace.ps1`, `hooks-sync.json` sono di giugno.
- **PUNTO D'INGRESSO:** uno per strumento. Quello dichiarato in `CLAUDE.md` come obbligatorio: **`python scripts/checkpoint.py cp --titolo "..."`** — *"il codice si conia con lo script, mai a mano e mai progressivo (due chat parallele sceglierebbero lo stesso numero)"*.
- **PEZZI CHE CONTANO:** `ultimo_metro.py` (13,4 KB) e' il codice che **misura** il problema descritto al §3.6 — l'Impero ha uno strumento che conta i pezzi finiti e mai usciti. `tesoreria.py` (18,4 KB) e' il motore del reparto conti. `gate_battito_hook.py` + `test_gate_battito.py` sono l'hook che sorveglia la forma dei recap, **con il proprio test accanto**: uno dei pochissimi casi nel repository in cui un motore nuovo nasce gia' con la sua prova.
- **DIPENDENZE ESTERNE:** nessuna chiave; `hooks-sync.json` e la configurazione hook di Claude Code.
- **CHI LO POSSIEDE:** **MAX / EMPERATOR**, per uso diretto — `checkpoint.py` e' prescritto in `CLAUDE.md`, quindi e' governato dalla regola di casa piu' alta. Non censito voce per voce nei registri, ma non e' orfano: e' il braccio di chi scrive i registri.
- **COME SI AVVOLGE:** e' gia' l'unico posto dove un comando dell'Impero **e'** un file. Il passo mancante e' agganciarlo a `python -m empire` (§4) come lotto `register(sub)`, cosi' che `checkpoint`, `tesoreria` e `ultimo_metro` diventino sottocomandi del runtime invece di script sciolti.

---

## 12. `EmpireDesk/` — L'INVOLUCRO CHE ESISTE GIA'. La risposta a "come si avvolge"

- **Percorso:** `EmpireDesk/`
- **Nome vero:** *EMPIRE DESK*.
- **A cosa serve:** dal docstring di `app.py` — *"Un solo .exe = l'app gestionale di Digital Empire. Il server locale serve la piattaforma **Aureus Agency OS** (React/Vite, grafica di Max — `platform/`, INTOCCABILE) come root, mantenendo vive le stesse API `/api/*` (tiles/launch/poll/modules/...)."* E la riga che risolve la domanda di questo censimento: **"Ogni tile/automazione lanciata resta un subprocess su un runtime ESISTENTE (ADR-003: launcher/wrapper, mai riscrittura dei motori)."**
- **Dimensione:** 14 file `.py`, **2.628 righe di Python**, 3.989 file totali (gonfiati da `platform/` React, `chrome-profile/`, `dist/`, `build/`).
- **PUNTO D'INGRESSO:** `python app.py` (dev, richiede `platform/dist/` gia' buildata con `npm install && npm run build`), `python app.py --selftest` (*"verifica tile/moduli/build platform, NON lancia nulla"*), `build_exe.bat` per l'eseguibile, `cron_dash.bat` per lo schedulato.
- **SCELTA TECNICA MOTIVATA DA UN BUG REALE, citata dal codice:** *"ordine motori = Chrome-app (server locale + finestra `chrome --app`) -> pywebview -> Tkinter. Motivo: su alcuni PC WebView2 manca e pywebview fallisce IN SILENZIO (bug reale trovato in PreventivoForge, CP-20260715-001) -> qui si parte gia' col motore che NON dipende da WebView2."*
- **GIRA ANCORA? VIVO, scritto OGGI.** Prova: `state/taskboard.json` **38 KB, 2026-09-06**; `state/preventa_leads.json` **1,31 MB, 2026-08-31**; `state/revenue.json` 2026-07-19.
- **QUALI MOTORI AVVOLGE GIA' — verificato leggendo i moduli, non il README:**
  - `modules/yt_produzione.py` righe 11/133-134: lancia **`YOUTUBE-AUTOMATION-FACTORY/02-AUTOMAZIONI-E-SCRIPTS/produci_video_completo.py`** (§2.2), con `cwd` dichiarato.
  - `modules/outreach.py` righe 8/120-121: lancia **`Outreach/preventa-maps-scraper/02-AUTOMAZIONI-E-SCRIPTS/run.py`** (file 04, §1.1).
  - `modules/preventa.py`: serve alla UI Areus i lead che `Outreach/preventa-maps-scraper` scrive.
  - `modules/licenze.py` riga 12: punta a **`Clienti/Prof Autocad/preventivo-forge/gestione-licenze.py`** (§7.1) — e' il kill-switch abbonamenti.
  - `modules/metrics.py` riga 20: conta i caroselli, **ma da `Workfolw crea caroselli à/carousel-factory`** — cioe' da una TERZA cartella caroselli, non da `SKILL & Agenti/Workflow agency creative/` dove `caroselli.py` scrive davvero (§3.2). **Il cruscotto sta contando la cartella sbagliata.**
  - Altri moduli: `dash.py`, `libri.py`, `libri_kdp.py`, `metrics.py`, `notify.py`, `revenue.py`, `scheduler.py`, `taskboard.py`, `youtube.py`.
- **DIPENDENZE ESTERNE:** Node/npm per buildare `platform/`; Chrome installato; `chrome-profile/` proprio; i motori avvolti con le loro chiavi (Fliki, WhatsApp).
- **CHI LO POSSIEDE:** `company/REGISTRO-IMPRESA.md` riga 47: *"EmpireDesk.exe (completato via LMarena zip) | 06-CORE/Platform (interim: Genesi-Core) | selftest 8/8 tile + 5-bis | dossier 17 | Art.2 (zero bottoni finti) · ADR-003 (solo launcher)"*. `skills-map.yaml` riga 563. **NON orfano.**
- **RUMORE NEL REGISTRO:** `skills-map.yaml` righe 1123-1124 censiscono come artefatto dell'Impero **un file JavaScript di un'estensione Chrome dentro `EmpireDesk/chrome-profile/Default/Extensions/`** — spazzatura da scansione automatica.
- **COME SI AVVOLGE:** **non si avvolge: e' lui l'involucro.** Insieme a `empire/` (§4) chiude il cerchio — `empire` per *osservare*, EmpireDesk per *lanciare*. **Il patrimonio dell'Impero non e' privo di un guscio: ne ha due, gia' costruiti e vivi. Il guasto e' che dentro EmpireDesk sono agganciati quattro motori su quindici, e uno dei quattro (metrics/caroselli) punta alla cartella sbagliata.**

---

## 13. Le cartelle senza motore — aperte e dichiarate, non dedotte

| cartella | .py | file | ultimo | cosa contiene davvero |
|---|---:|---:|---|---|
| `second-brain-vault/` | 13 | 3.415 | **2026-09-06** | la wiki di Digital Empire (Markdown + Obsidian). **VIVA oggi**, ma non e' un motore: e' l'uscita di Empire Studio (§3.1) |
| `agency-empire/` + `agency-empire-landing/` | 0 | 1.854 + 1.774 | 2026-07-25 | siti Next.js (vetrina agenzia). `09b-prove-novacar.tsx` e' censito in REGISTRO riga 55. Nessun Python |
| `Lancio corso skill beast/` | 1 | 10.193 | 2026-05-13 | **materiale di lancio**, non codice: 10.193 file per un solo `.py`. Fermo da 116 giorni |
| `SaaS/` | 0 | 721 | 2026-06-10 | zero Python. Non e' un SaaS: e' una cartella di materiale |
| `KDP - prodottti digitali/` | 1 | 803 | 2026-04-08 | un solo `.py`. Fermo da 151 giorni |
| `Workflow-libri/` | 7 | 80 | **2026-03-21** | 7 script libri, **il piu' vecchio motore attivo mai censito: 169 giorni**. DORMIENTE |
| `master-build-architecture/` | 5 | 408 | 2026-07-20 | metodologia MBA; il Python e' contorno. Esiste **anche clonata** in `DIGITAL-EMPIRE/05-SKILLS/` (§6) |
| `competitor/` | 1 | 485 | 2026-09-01 | studio competitor: `Andrei Pascu/`, `Martes Ai/`. Materiale, non motore |
| `Formazzione/` | 0 | 23 | 2026-05-31 | materiale |
| `App/` | 0 | **1** | 2026-05-01 | **un solo file in tutta la cartella.** Non esiste nessuna "App" |
| `content-forge2.0/` | 0 | **0** | — | **CARTELLA COMPLETAMENTE VUOTA** (creata 2026-07-21). Ma `DIGITAL-EMPIRE/05-SKILLS/content-forge2.0` esiste e ha contenuto, e la skill `/content-forge2.0` e' installata: **il registro punta a un guscio vuoto** |
| `data/`, `shared/`, `tests/` (radice) | 0-1 | 2 | 2026-07/09 | segnaposto da 2 file ciascuno |

**Nota su `content-forge2.0/` in radice:** e' l'unico caso in cui il rischio "cartella vuota" si e' avverato **al contrario** rispetto al caso `08-STREAM-S7-BOT`: li' una cartella dichiarata vuota conteneva un bot; qui una cartella che il repository tratta come sistema vivo **non contiene nemmeno un file**.

---

## 14. `Workfolw crea caroselli à/carousel-factory/` — il motore di render, che NON e' Python
- **Percorso:** `Workfolw crea caroselli à/carousel-factory/` (il nome della cartella contiene un refuso e una `à` finale: e' questo che ha confuso i registri).
- **A cosa serve:** e' il **motore di render Puppeteer + template HTML** che `caroselli.py` (§3.2) invoca come processo esterno. Non e' Python: `scripts/` contiene `generate.js`, `render.js`, `export-all.js`; ha `package.json`, `package-lock.json`, `templates/`, `brands/`, `context/`, `node_modules/`.
- **PUNTO D'INGRESSO:** gli script Node, chiamati da `caroselli.py`. Non ha un lancio proprio dichiarato.
- **GIRA ANCORA? VIVO come libreria, morto come cartella d'uscita.** `scripts/`, `templates/`, `brands/`, `package-lock.json` sono **2026-08-31** — la stessa data di `caroselli.py`, cioe' sono stati toccati insieme. Ma `output/` contiene **una sola cartella, del 2026-03-22** (`2026-03-22-il-90-dei-freelance-fallisce-per-questo-motivo`): da quando `caroselli.py` esiste, l'uscita va nell'Arsenale, non qui.
- **PERCHE' E' IMPORTANTE PER IL CENSIMENTO:** e' la cartella che `EmpireDesk/modules/metrics.py` riga 20 usa per contare i caroselli prodotti. **Il cruscotto legge `output/`, che e' fermo a marzo, invece di `Arsenale Caroselli/`, che e' di fine agosto. Quel numero sul cruscotto e' sbagliato per costruzione.**
- **CHI LO POSSIEDE:** `company/skills-map.yaml` riga 179 lo censisce come `workflow-caroselli-alt` — *"Workflow Crea Caroselli (alternativo)"*. E' l'unica delle tre cartelle caroselli ad avere una voce col percorso giusto, e il registro la marca come "alternativa" mentre e' il motore vero del render.
- **LA TERNA CAROSELLI, per chiarezza:** `caroselli/` in radice (contiene solo `3-sistemi-ai/` — materiale), `Workfolw crea caroselli à/carousel-factory/` (**il render, Node**), `SKILL & Agenti/Workflow agency creative/` (**il comando e l'Arsenale, Python**). Tre cartelle, un solo flusso, e i registri ne conoscono le due sbagliate.

## 15. `.claude/` — il livello skill/agenti: 172 skill, 129 agenti, 21.535 righe
- **Percorso:** `.claude/skills/` + `.claude/agents/`
- **Dimensione reale, contata:** **172 skill**, **129 agenti**, **440 file `.py` per 21.535 righe di Python** (esclusi `__pycache__`). E' la seconda concentrazione di Python del repository dopo `company/`.
- **A cosa serve:** e' il livello che l'Impero usa davvero ogni giorno — `/avvia-outreach-preventa`, `/empire-studio`, `/tesoreria`, `/ultimo-metro`, `/graphify`, `/memory-empire`, `/checkpoint`. Gli script Python dentro le skill (`agency-scalping/scripts/coverage_checker.py`, `lint_anti_summary.py`, `schema_validator.py`, `agente-max/scripts/generate_agent.py`, `context_calculator.py`) sono **gate deterministici**, non contorno: fanno fallire la skill quando l'output non e' conforme.
- **PUNTO D'INGRESSO:** i comandi slash. Non c'e' e non serve un CLI.
- **GIRA ANCORA? VIVO.** E' il livello attraverso cui questo stesso censimento viene eseguito.
- **DUPLICAZIONE RILEVATA:** `skill-creator` esiste **tre volte** (`.claude/skills/skill-creator/`, `Crea siti/skills/skill-creator/`, `System OMEGA .../.claude/skills/skill-creator/`); `market`/`marketingskills` esiste come skill installata **e** come copia in `Crea siti/skills/market/` **e** come `marketingskills-main.zip` (§3.9).
- **CHI LO POSSIEDE:** `company/skills-map.yaml` e' proprio la mappa di questo livello. **NON orfano** — anzi, e' l'unica parte del repository che il registro copre bene.
- **NOTA:** `.claude/agents/` contiene 129 agenti; `.claude/commands/` e' **vuota** (0 file), mentre `YOUTUBE-AUTOMATION-FACTORY/.claude/commands/avvia-yt.md` esiste. I comandi di progetto stanno nelle cartelle dei motori, non al centro.

## 16. I due archivi in radice, aperti
- **`APEX SKILL.zip`** — **3.873 file, 128 `.py`**. Contiene `apex-7/` completo: `ARCHITECTURE.md`, `SKILL.md`, e gli agenti `analyst`, `critic` (con `failure-modes.md` e `playbook.md`) e gli altri. E' **il QUARTO APEX-7 del repository** dopo `YOUTUBE-AUTOMATION-FACTORY` (§2.1), `SKILL & Agenti/apex7/` (§3.7) e `company/Ecosistemi/11-APEX-7-CORE`. La skill `/apex-7` e' gia' installata in `.claude/skills/apex-7/`: **questo zip e' materia prima gia' consumata.**
- **`digital-empire-team---sito.zip`** — 49 file, **0 `.py`**. Componenti React/TypeScript (`components/ui/GoldButton.tsx`, `Navbar.tsx`, `types.ts`, `metadata.json`) di un sito team. Nessun motore.

## 19. Due cartelle che contengono copie di motori gia' censiti
- **`Agency page/`** (31 `.py`, 4.957 file, 2026-08-04): e' un sito Vite/React (`App.tsx`, `index.tsx`, `vite.config.ts`, `package.json`), **ma dentro `Agency page/Clienti/Prof Autocad/preventivo-forge/` c'e' una COPIA INTERA di PreventivoForge**, `dist/` compreso. Con `Clienti/Prof Autocad/preventivo-forge/` (§7.1) e lo ZIP di consegna, **PreventivoForge esiste in tre copie nel repository**. Piu' `Agency page - Copia/` (74 file), copia della copia.
- **`second-brain-vault/`** (13 `.py`, 3.415 file): gli script (`compile_to_wiki.py`, `check_broken_links.py`, `fix_links.py`, `interlink_advanced.py`, `create_stubs.py`, `clean_wiki.py`, `extract_to_raw.py`, `garbage_cleanup.py`) sono **fermi al 2026-05-06/07**, ma `wiki/` e' scritta **2026-09-06**. Cioe': **la wiki e' viva, i suoi manutentori automatici sono morti da quattro mesi.** Chi la scrive oggi e' Empire Studio (§3.1) e Claude a mano, non questi script. Se un link si rompe, oggi non se ne accorge nessuno: `check_broken_links.py` non gira dal 6 maggio.
