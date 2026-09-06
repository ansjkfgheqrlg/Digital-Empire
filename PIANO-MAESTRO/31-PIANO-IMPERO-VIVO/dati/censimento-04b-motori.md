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
