# 📥 BACKLOG — cose rimandabili (NON bloccano la costruzione)

> Regola (ADR-005): quando spunta un task minore/decisione non strutturale, finisce QUI,
> non ferma mai una fase. Si svuota nei momenti morti o quando una fase lo richiede davvero.
> Chiunque (Max, Gael, agenti) aggiunge righe; si spunta con data.

| # | Cosa | Note | Quando serve davvero | Stato |
|---|---|---|---|---|
| B-001 | Rinnovare token FB (scraper outreach) | developers.facebook.com/tools/explorer → .env | solo per run scraper FB reale (gli altri canali outreach girano) | ⬜ |
| B-002 | Prezzo "Manuale Claude Code" + ruolo (prodotto vs lead magnet) | NON si decide a mano: lo proporrà il **team prezzi** (B-003) | gate F6 (lancio reale) | ⬜ |
| B-003 | Team agenti PREZZI | skill `pricing` (installata) come motore + beast-preventivi; team L4 in 04-MARKETING/Analytics o 02-INFO-BUSINESS/Vendite; propone prezzi data-driven, Max approva | fase F5/F6 | ⬜ |
| B-004 | Gael: completare `git config user.email` reale | cosmetico (firma commit) | mai bloccante | ⬜ |
| B-005 | Estendere skill `empire-context` con references/ (Mandato esteso, brand guide, listino) | previsto da dossier 07 §3.2.1 | fase F2-bis/B3 backbone | ⬜ |
| B-006 | Pulire 5 stub v1 in `03-CONTENT-FACTORY/Reparti/` (Strategia, Produzione-Video, Produzione-Testuale, Visual-Design, Pubblicazione — README singoli del F1-bis 2026-06-11) | superati dalle cartelle v2 `CF-RN-*` complete; sono solo README orfani che sporcano il gate. Da archiviare/rimuovere con ok (non creati in questa sessione) | pulizia, non urgente | ⬜ |
| B-007 | PreventivoForge: normalizzare trattini/spazi nel match glossario S3 | Oggi `xenon-scheinwerfer` ≠ `xenonscheinwerfer` ≠ `xenon scheinwerfer`: servono voci separate. Un normalizzatore (togli `-`/spazi prima del lookup) coprirebbe tutte le varianti in un colpo. Vedi CP-20260702-001 | quando Gate B blocca spesso per varianti trattino | ⬜ |
| B-008 | Blob video ingestioni (SKILL & Agenti: frame+mp4, ~900MB history) → Git LFS o gitignore + storage locale | Il push del main completo muore (pack 899MB, rete instabile): oggi risolto con work-sync leggero 1b7842ad, ma ogni sync futuro con video ripropone il problema. Decidere: LFS, o ignore + backup locale | prima della prossima ingestione grossa | ⬜ |
| B-009 | **Collisione ID checkpoint: 3 volte in 15 minuti il 2026-07-22** | Max/Claude e Gael hanno creato CP-20260722-002 e CP-20260722-003 in parallelo → 3 conflitti add/add di fila, risolti a mano rinumerando in 005 e 006. Causa: l'ID si assegna contando i file a occhio. Fix già specificato: lock su file in `empire/memory/store.py` (GEM-02 §4, "Regola anti-collisione ID"), che legge il max NNN sia da atoms.jsonl sia dai nomi file in checkpoints/. Precedente: CP-20260719-006 (002/003 rinumerati 004/005) | **✅ CHIUSO 2026-07-23** da M-A (`empire/memory/store.py`): lock `O_CREAT\|O_EXCL` + lettura del max NNN sia dagli atomi sia dai nomi file su disco. Provato sul campo: il runtime si è assegnato `CP-20260723-004` mentre Gael aveva già 001/002/003 → zero collisioni. Test `test_concurrent_ids_never_collide`: 20 scritture parallele → 20 ID distinti. **⚠️ Ma il 2026-07-23 è successo ANCORA**: una sessione parallela ha scritto il suo `CP-20260723-004` **a mano** mentre il runtime assegnava lo stesso numero → rinumerato in 005. **Il lock protegge solo chi lo usa.** **REGOLA: i checkpoint si scrivono SOLO con `python -m empire mem write --kind checkpoint --view` — la scrittura a mano È il bug.** Vale per Max, Gael, Claude e ogni sessione parallela | ✅ (fix fatto, resta da far adottare il comando) — **⚠️ RIACCADUTO il 2026-07-30 (4ª volta)**: due sessioni parallele hanno creato `CP-20260729-001` e `CP-20260729-002` con contenuti completamente diversi (YouTube vs "centro di comando"), scoperti solo al merge come conflitti add/add; risolti rinumerando i miei in **009/010**. Conferma che la regola non è ancora adottata: **il comando `empire mem write` non è stato usato da nessuna delle due sessioni** |
| B-010 | STREAM-S7-BOT: serve un RPC provider Solana a pagamento (Helius/QuickNode/Alchemy) | L'endpoint pubblico `api.mainnet-beta.solana.com` rate-limita `getTransaction` a ~2 chiamate ravvicinate poi `429 Too Many Requests` — verificato in CP-20260728-006 durante la validazione del parser G-A. Il parser stesso è corretto (5/5 coppie volume/token reali estratte quando diluito nel tempo), ma un bot live su Raydium/Pump.fun genera più transazioni al secondo di quante il nodo gratuito ne regga | prima di qualunque passo verso `TRADE_MODE=LIVE` o verso un run di validazione prolungato (10+ min) su dati live | ⬜ |
| B-011 | `fliki_client.py`: ricollegare il parser scene all'orchestratore (togliere la copia standalone) | Il 2026-07-30 una sessione parallela ha trovato `apex7_orchestrator.py` con un merge Git a metà (non importabile) e si è difesa creando `_parse_script_scenes_standalone()`, copia locale della stessa logica. Il commento nel codice dice esplicitamente "Da rimuovere/ri-collegare una volta risolto il conflitto". **Il conflitto è risolto** (merge `dc076a64`): ora la copia è duplicazione che può divergere dall'originale | quando quella sessione ha finito la sua run Fliki (non toccare a metà generazione) | ⬜ |
| B-012 | Magic Eden: confermare fee marketplace e royalty creator da fonte primaria | Il modello di costo NFT (`nft_analysis_engine.py`) usa `MARKETPLACE_FEE_PCT = 0.02` come valore pubblicamente noto **non riverificato** in sessione: il tentativo è finito su `HTTP 429` (rate limit) e la pagina doc tentata dava 404. Il payload `/listings` reale non espone la royalty. Entrambi marcati "DA CONFERMARE" nel codice, non spacciati per misurati | prima di dare qualunque peso decisionale all'expectancy netta (oggi comunque bocciata per altri motivi) | ⬜ |
| # | Cosa | Note | Quando serve davvero | Stato |
|---|---|---|---|---|
| B-001 | Rinnovare token FB (scraper outreach) | developers.facebook.com/tools/explorer → .env | solo per run scraper FB reale (gli altri canali outreach girano) | ⬜ |
| B-002 | Prezzo "Manuale Claude Code" + ruolo (prodotto vs lead magnet) | NON si decide a mano: lo proporrà il **team prezzi** (B-003) | gate F6 (lancio reale) | ⬜ |
| B-003 | Team agenti PREZZI | skill `pricing` (installata) come motore + beast-preventivi; team L4 in 04-MARKETING/Analytics o 02-INFO-BUSINESS/Vendite; propone prezzi data-driven, Max approva | fase F5/F6 | ⬜ |
| B-004 | Gael: completare `git config user.email` reale | cosmetico (firma commit) | mai bloccante | ⬜ |
| B-005 | Estendere skill `empire-context` con references/ (Mandato esteso, brand guide, listino) | previsto da dossier 07 §3.2.1 | fase F2-bis/B3 backbone | ⬜ |
| B-006 | Pulire 5 stub v1 in `03-CONTENT-FACTORY/Reparti/` (Strategia, Produzione-Video, Produzione-Testuale, Visual-Design, Pubblicazione — README singoli del F1-bis 2026-06-11) | superati dalle cartelle v2 `CF-RN-*` complete; sono solo README orfani che sporcano il gate. Da archiviare/rimuovere con ok (non creati in questa sessione) | pulizia, non urgente | ⬜ |
| B-007 | PreventivoForge: normalizzare trattini/spazi nel match glossario S3 | Oggi `xenon-scheinwerfer` ≠ `xenonscheinwerfer` ≠ `xenon scheinwerfer`: servono voci separate. Un normalizzatore (togli `-`/spazi prima del lookup) coprirebbe tutte le varianti in un colpo. Vedi CP-20260702-001 | quando Gate B blocca spesso per varianti trattino | ⬜ |
| B-008 | Blob video ingestioni (SKILL & Agenti: frame+mp4, ~900MB history) → Git LFS o gitignore + storage locale | Il push del main completo muore (pack 899MB, rete instabile): oggi risolto con work-sync leggero 1b7842ad, ma ogni sync futuro con video ripropone il problema. Decidere: LFS, o ignore + backup locale | prima della prossima ingestione grossa | ⬜ |
| B-009 | **Collisione ID checkpoint: 3 volte in 15 minuti il 2026-07-22** | Max/Claude e Gael hanno creato CP-20260722-002 e CP-20260722-003 in parallelo → 3 conflitti add/add di fila, risolti a mano rinumerando in 005 e 006. Causa: l'ID si assegna contando i file a occhio. Fix già specificato: lock su file in `empire/memory/store.py` (GEM-02 §4, "Regola anti-collisione ID"), che legge il max NNN sia da atoms.jsonl sia dai nomi file in checkpoints/. Precedente: CP-20260719-006 (002/003 rinumerati 004/005) | **✅ CHIUSO 2026-07-23** da M-A (`empire/memory/store.py`): lock `O_CREAT\|O_EXCL` + lettura del max NNN sia dagli atomi sia dai nomi file su disco. Provato sul campo: il runtime si è assegnato `CP-20260723-004` mentre Gael aveva già 001/002/003 → zero collisioni. Test `test_concurrent_ids_never_collide`: 20 scritture parallele → 20 ID distinti. **⚠️ Ma il 2026-07-23 è successo ANCORA**: una sessione parallela ha scritto il suo `CP-20260723-004` **a mano** mentre il runtime assegnava lo stesso numero → rinumerato in 005. **Il lock protegge solo chi lo usa.** **REGOLA: i checkpoint si scrivono SOLO con `python -m empire mem write --kind checkpoint --view` — la scrittura a mano È il bug.** Vale per Max, Gael, Claude e ogni sessione parallela | ✅ (fix fatto, resta da far adottare il comando) — **⚠️ RIACCADUTO il 2026-07-30 (4ª volta)**: due sessioni parallele hanno creato `CP-20260729-001` e `CP-20260729-002` con contenuti completamente diversi (YouTube vs "centro di comando"), scoperti solo al merge come conflitti add/add; risolti rinumerando i miei in **009/010**. Conferma che la regola non è ancora adottata: **il comando `empire mem write` non è stato usato da nessuna delle due sessioni** |
| B-010 | STREAM-S7-BOT: serve un RPC provider Solana a pagamento (Helius/QuickNode/Alchemy) | L'endpoint pubblico `api.mainnet-beta.solana.com` rate-limita `getTransaction` a ~2 chiamate ravvicinate poi `429 Too Many Requests` — verificato in CP-20260728-006 durante la validazione del parser G-A. Il parser stesso è corretto (5/5 coppie volume/token reali estratte quando diluito nel tempo), ma un bot live su Raydium/Pump.fun genera più transazioni al secondo di quante il nodo gratuito ne regga | prima di qualunque passo verso `TRADE_MODE=LIVE` o verso un run di validazione prolungato (10+ min) su dati live | ⬜ |
| B-011 | `fliki_client.py`: ricollegare il parser scene all'orchestratore (togliere la copia standalone) | Il 2026-07-30 una sessione parallela ha trovato `apex7_orchestrator.py` con un merge Git a metà (non importabile) e si è difesa creando `_parse_script_scenes_standalone()`, copia locale della stessa logica. Il commento nel codice dice esplicitamente "Da rimuovere/ri-collegare una volta risolto il conflitto". **Il conflitto è risolto** (merge `dc076a64`): ora la copia è duplicazione che può divergere dall'originale | quando quella sessione ha finito la sua run Fliki (non toccare a metà generazione) | ⬜ |
| B-012 | Magic Eden: confermare fee marketplace e royalty creator da fonte primaria | Il modello di costo NFT (`nft_analysis_engine.py`) usa `MARKETPLACE_FEE_PCT = 0.02` come valore pubblicamente noto **non riverificato** in sessione: il tentativo è finito su `HTTP 429` (rate limit) e la pagina doc tentata dava 404. Il payload `/listings` reale non espone la royalty. Entrambi marcati "DA CONFERMARE" nel codice, non spacciati per misurati | prima di dare qualunque peso decisionale all'expectancy netta (oggi comunque bocciata per altri motivi) | ⬜ |
| B-013 | **`ruflo_core.py`: `execute_workflow` cade su console Windows (cp1252)** | `print(f"[FLOW] → {stage}")` (riga ~347) solleva `UnicodeEncodeError` nel percorso principale, non su un ramo d'errore: qualsiasi consumatore Windows che chiami `RuFLOOrchestrator.execute_workflow` con stdout cp1252 muore. Trovato durante l'innesto dell'orchestration layer (CP-20260813-001) facendo girare il motore per davvero. Fix: sostituire `→` con `->`. Non applicato: il motore è condiviso da YouTube/carousel-machine/skill-forge/cold-outreach e si tocca in un ciclo dedicato con le loro suite verdi, non di straforo (ADR-003). Contenuto intanto da `orchestration/pipeline.py::stdout_tollerante()`; difetto fissato da `TestDifettiDelMotore` | — | **✅ CHIUSO 2026-08-13** (CP-20260813-002). Scoperto piu' grave del previsto: **`main.py`, l'entry point del motore canonico, non partiva affatto su Windows** — crashava alla riga 21 sul proprio banner box-drawing, prima ancora di arrivare al workflow. Fix con lo split giusto: **la libreria** (`ruflo_core.py`) stampa solo ASCII, perche' non puo' imporre un encoding ai chiamanti; **gli entry point** (`main.py`, `run_demo.py`) forzano UTF-8 e si tengono i loro banner. Verificato: `main.py "prova"` ora gira end-to-end. Suite: 49 orchestration + 4 multi-tenant + 11 YouTube tutte verdi |
| B-014 | **`ruflo_core.py`: ricorsione infinita con punteggio di critica < 4.0** | `execute_workflow` genera un `task_id` nuovo a ogni restart (`str(uuid.uuid4())` dentro `current_context`), quindi `DynamicWorkflowRouter.loop_count` riparte sempre da zero e il ramo "Restart totale se disastro" si richiama per sempre → `RecursionError`. Il guard-rail dei 3 giri esiste nel router ma non può mai scattare. Fix: propagare il `task_id` attraverso la ricorsione. Non applicato per lo stesso motivo di B-013. Contenuto: la pipeline lo intercetta come guasto e blocca a L4 invece di appendersi. Difetto dimostrato senza innescarlo da `test_DIFETTO_loop_count_non_accumula_fra_restart` | — | **✅ CHIUSO 2026-08-13** (CP-20260813-002). Il `task_id` ora sopravvive ai restart (`_apex7_task_id` nel context), quindi `DynamicWorkflowRouter.loop_count` accumula e il guard-rail dei 3 giri scatta davvero. Verificato: un workflow con critic score 2.0 termina con "Final Score: 2.0" invece di andare in `RecursionError` |
| B-015 | **Reimplementazioni APEX-7 divergenti: ora sono 5, non 4** | ADR-010 ne censiva 4 (YouTube, skill `.agents/skills/apex-7/`, `11-APEX-7-CORE`, `12-STREAM-S7-BOT`). L'audit del 2026-08-13 ne ha trovata una **quinta non documentata**: `empire/intelligence/apex7/` (agents/backends/memory/orchestrator/quality/ruflo_adapter, ~650 righe). È la più onesta di tutte — `backends.py` dichiara esplicitamente il mock e offre un `LLMBackend` vero, `ruflo_adapter.py` alza `NotImplementedError` scrivendo che il binding Rust non c'è — ma resta una linea parallela al motore canonico. Da censire in ADR-010 e decidere: deprecare, o promuovere i suoi `backends.py`/`ruflo_adapter.py` dentro `11-APEX-7-CORE` (oggi il motore canonico non ha un seam per il backend LLM) | alla Fase 2 di ADR-010 (estensione ai 13 ecosistemi), prima di scalare su altri ecosistemi | ⬜ |
| B-016 | **Tesseract OCR non installato: il controllo del titolo in copertina non gira** | Il pacchetto Python `pytesseract` c'e', il motore no. Percio' `valida_copertina_testo` ritorna "VERIFICA A MANO" e da oggi finisce in `verifiche_non_eseguite` dentro `validazione.json` (prima si perdeva fra gli avvisi). E' l'unico dei controlli bloccanti della consegna che al momento **non ha mai detto di si'** sui tre pacchetti. Installare da https://github.com/UB-Mannheim/tesseract/wiki, il codice lo trova gia' nel percorso standard | prima di caricare i libri, o si guarda la copertina a occhio | **✅ CHIUSO 2026-08-23** (stessa sessione): installato con `winget install --id UB-Mannheim.TesseractOCR --exact` (v5.4.0), che lo mette proprio in `C:\Program Files\Tesseract-OCR` — il percorso che il codice cerca gia' da solo, senza toccare il PATH. Provato sulle tre copertine vere: **titolo letto 3 volte su 3** in meno di mezzo secondo (l'ordine delle varianti OCR di CP-20260819-002 fa centro alla prima). I tre pacchetti riconsegnati escono ora con **`verifiche_non_eseguite: 0`**: e' la prima volta che ogni controllo bloccante della consegna gira davvero |
| B-017 | **`kdp titolo-libero`: verificare su Amazon che il titolo non collida** | Oggi il titolo di un libro non viene mai confrontato con quelli esistenti nella nicchia: si rischia di uscire con un titolo identico a un concorrente forte, che e' il modo piu' semplice di essere invisibili nella ricerca. `amazon_research.py` gia' fa lo scraping e funziona senza login: servono ~30 righe per un sottocomando che cerchi il titolo e mostri le collisioni. Non fatto ora perche' richiede rete e non era negli errori da chiudere | prima del prossimo libro, alla scelta del titolo (Fase 2) | ⬜ |
| B-018 | **Decisione di catalogo: una nicchia e UN nome d'autore** | Non e' un task tecnico, e' una scelta di Gael, ma senza di essa i libri non si sommano. Oggi: nicchia attiva `small town romance suspense`, e i tre libri sono in `psychological thriller` (autore "Digital Empire"), `amish romance suspense` ("Rebecca Miller") e `cozy fantasy bookshop` ("Maren Ashcroft"). Conseguenza gia' visibile nel prodotto: la pagina **"Also by" esce vuota su tutti e tre**. Il codice ora impedisce di divergere in silenzio (`kdp nuovo` rifiuta senza `--motivo`), ma la nicchia da tenere la sceglie una persona | prima del prossimo libro (dark academia e' gia' in magazzino) | **✅ CHIUSO 2026-09-01** (CP-20260902-001, FIX-2). Decisione presa sui numeri rimisurati **lo stesso giorno** su tutte e sei le candidate, perche' quelli in magazzino erano del 13 agosto e uno era passato da 83,1 a 72,9. **Nicchia: `witch bookshop cozy fantasy` (83,5/100)** — recensioni mediana **62** contro le **1272** di `small town romance suspense` che si lascia (venti volte piu' facile posizionarsi, ed e' il motivo per cui quella aveva 0 libri), 9 concorrenti deboli su 20, prezzo medio **$11,36**, il piu' alto misurato. **Autore unico: Maren Ashcroft**, che gia' firma 2 libri su 5. *The Second-Hand Spellbook* (cozy fantasy in una libreria di libri di magia usati) e' esattamente questo scaffale: appena caricato su KDP diventa il primo titolo del catalogo, non un esordio isolato. Trovato e corretto anche il guardrail che rendeva la decisione impossibile: `nicchia_attiva.cambia()` pretendeva 12 punti di margine SEMPRE, ma il margine protegge "il pubblico gia' raggiunto" — che con 0 libri pubblicati non esiste. Difendeva il nulla e blindava il catalogo nella nicchia peggiore. Ora vale solo con libri pubblicati. **I 4 libri gia' scritti fuori nicchia restano come sono ma NON contano come catalogo**: da qui in avanti tutto nasce dentro. |
| B-019 | Wiki (`second-brain-vault/wiki/`): audit + backfill del periodo PRE-luglio (creazione monorepo 2026-06-10 → primo log wiki 2026-07-04, ~3 settimane senza entry) | Trovato il 2026-08-23 durante l'indagine sul gap 06→22 agosto (colmato, vedi log.md 2026-08-23): la wiki ha avuto almeno 2 finestre senza aggiornamenti nonostante lavoro reale continuo in `company/Memory/` (checkpoint mai mancanti). Il gap di agosto è stato chiuso su richiesta esplicita di Max; questo periodo precedente resta aperto — Max ha scelto scope ridotto ("solo agosto") per ora | quando Max dà il via libera esplicito a un audit dell'intera estate (lavoro grande, richiede swarm per ADR-006) | ⬜ |
| B-020 | 🔴 **Chiave API Brevo in chiaro su repo PUBBLICO — da RUOTARE** | La chiave `xkeysib-1b440a32…4J8p0TDOcRTChJz9` (form opt-in newsletter) è in chiaro nel codice e sta in `HEAD` dal **commit iniziale `57a0ba0b`**: `Crea siti/Siti CCM/index.html`, `Lancio corso skill beast/Leanding Page CCM/index.html`, `Lancio corso skill beast/Sale pag/Siti CCM/icro-empire/src/components/optin-form.tsx` — più le copie nelle build CCM/Landing committate il 2026-08-25 (CP-20260825-001). Repo `ansjkfgheqrlg/Digital-Empire` verificato **PUBLIC** (`gh repo view`). **Rimuoverla dal codice NON basta**: la storia Git pubblica è già indicizzabile, quindi va **revocata e rigenerata su Brevo**. Poi decidere se il form deve chiamare un endpoint server invece di esporre la chiave in JS client-side (una chiave Brevo dà accesso all'account, non solo alla lista) | **subito** — è l'unica voce di questo backlog che è un'esposizione attiva, non un debito tecnico | ⬜ |
| B-021 | 🔴 **Credenziali Arena + 2 API key in chiaro su repo PUBBLICO — da RUOTARE** | `SKILL & Agenti/Workflow agency creative/caroselli - agency/config.py` è **tracciato** e contiene in chiaro `ARENA_EMAIL`, `ARENA_PASSWORD`, `GROQ_API_KEY`, `OPENROUTER_API_KEY`. Trovato il 2026-08-27 lavorando su TASK-CAROSELLI-W1 (CP-20260825-003). È **peggio di B-020**: lì è una API key, qui c'è la **password di un account**. Stato verificato in sessione: la chiave Groq è già morta (risponde `401 Invalid API Key`), la chiave OpenRouter è **viva e funzionante** (ha generato il copy del carosello di oggi). `config_preventa.py` importa da qui apposta per non duplicare le credenziali, quindi il punto da sistemare è uno solo. Fix: spostare tutto su variabili d'ambiente / `.env` (già gitignorato dal repo), **ruotare la password Arena e la chiave OpenRouter** (la storia git pubblica resta leggibile anche dopo la rimozione dal codice) | **subito**, come B-020 | ⬜ |
| B-022 | `Inter-Regular.ttf` del brand `mentalita-brutale` non è un font | `Workfolw crea caroselli à/carousel-factory/brands/mentalita-brutale/assets/fonts/Inter-Regular.ttf` sono 304KB di **HTML** salvati con estensione .ttf (magic bytes `0a0a0a0a...<!DOCTYP`, verificato): è una pagina di errore di download. Fino al 2026-08-27 nessuno se n'era accorto perché il font non veniva caricato comunque (bug di origine su `page.setContent`, ora corretto). Ora `render.js` lo rileva, lo dice e ripiega su un font di sistema dichiarato, quindi **non blocca**: le slide `mentalita-brutale` escono col corpo in Arial invece che in Inter | quando si torna a produrre per quel brand | ⬜ |
| B-023 | 🔴 **Password Instagram in chiaro su repo PUBBLICO — da RUOTARE** | `SKILL & Agenti/Workflow pubblicazione automatica/Instagram/config.py` è **tracciato** e contiene `IG_USERNAME = "digitalempireagency.e"` + `IG_PASSWORD` in chiaro. Trovato il 2026-08-27 su TASK-PUBLISHER-W1 (CP-20260827-001). Stessa classe di B-020/B-021, e come B-021 è una **password di account**, non una API key: chi legge il repo pubblico entra nell'account Instagram dell'agenzia. Fix: spostare su `.env` (già gitignorato) e **cambiare la password su Instagram** — la storia git pubblica resta leggibile anche dopo la rimozione dal codice. Nota: cambiare la password invalida anche eventuali `session_data/` già salvate, quindi va fatto PRIMA del login una tantum, non dopo | **subito**, come B-020/B-021 | ⬜ |
| B-024 | 🔴 **`push_social.py` è una simulazione ma `CLAUDE.md` lo dichiara obbligatorio** | Il `CLAUDE.md` di `Workflow pubblicazione automatica/` impone «esegui lo script `push_social.py`» come unica via di pubblicazione. Eseguito davvero il 2026-08-27: stampa `Pubblicazione completata con successo (SIMULATA)!` ed esce **0** senza pubblicare niente — la `requests.post` è commentata e il payload non contiene nemmeno i media (`# "mediaUrls"`). È un PASS finto che inganna l'exit code. Decidere: (a) implementarlo davvero su un aggregatore (Ayrshare/Make), oppure (b) ritirarlo e correggere `CLAUDE.md` perché punti a `pubblica.py`. Finché non è deciso, `pubblica.py` non lo usa | prima che qualcuno si fidi di quell'exit code | ⬜ |
| B-025 | **`main_orchestrator.py` non parte e dichiara successo comunque** | Verificato 2026-08-27: `IMPORT FAIL main_orchestrator -> OpenAIError: Missing credentials`. Catena `main_orchestrator` → `Core/copy_generator` → `Core/AI_Team/ai_client`, che istanzia `OpenAI(...)` **a livello di modulo** con `OPENROUTER_API_KEY`/`GROQ_API_KEY` assenti: muore all'import, prima di eseguire una riga. In più stampa `FLUSSO COMPLETATO CON SUCCESSO!` **incondizionatamente**, senza guardare l'esito di `publish_ig()`. Fix: client LLM istanziato lazy dentro la funzione + esito reale propagato. Non fatto ora: `pubblica.py` non passa da qui (ADR-003, non tocco motori che non mi servono) | quando serve la catena Drive→IA→IG automatica, non per pubblicare una cartella già pronta | ⬜ |
| B-026 | **`TikTok/tiktok_publisher.py` non importa** | Riga 10: `import config` invece di `from TikTok import config` → `ModuleNotFoundError: No module named 'config'` (verificato 2026-08-27). Il canale TikTok — catena 3 di `REGOLE.md`, "Codice dei Potenti" — è oggi inutilizzabile. Fix da una riga, non fatto in questa task perché fuori dal gate (che chiedeva **un** canale reale) e perché il canale resterebbe comunque bloccato da B-027/sessione assente. `pubblica.py` lo dichiara NON pronto a runtime invece di fallire a sorpresa | quando si apre la catena TikTok | ⬜ |
| B-027 | **`do_login()` cerca un campo che Instagram non ha più** | `scripts/ig_carousel_publish.py::do_login()` riempie `input[name="username"]`. Verificato dal vivo il 2026-08-27 sulla home loggata-fuori: i campi reali sono `input[name="email"]` e `input[name="pass"]`. Quindi il **login automatico non funziona** su IG 2026 (il resto del publisher sì). Mitigazione già in atto: `pubblica.py` non si appoggia al login automatico — pretende una sessione già autenticata (`setup_session.py`, login manuale una tantum) e in mancanza **rifiuta il `--live`** invece di sbatterci contro. Fix vero solo se si vuole il login non presidiato (sconsigliato: è il percorso che si becca i captcha) | se si vuole automazione senza login manuale iniziale | ⬜ |
| B-028 | 🟠 **`empire mem write --view` scrive le viste in CRLF: è la causa a monte del guaio di merge di B-009** | Trovato il 2026-08-27 (CP-20260827-001) scrivendo un checkpoint con lo strumento anti-collisione: la vista Markdown rigenerata esce con **CRLF** mentre tutto il repo è LF. Effetto misurato: `CP-20260825-003.md` (checkpoint di un'altra sessione, riscritto come effetto collaterale) risultava `100 insertions / 90 deletions` — cioè **il file intero** — mentre il contenuto davvero cambiato era `12 insertions / 2 deletions`. È esattamente la forma del problema che il 2026-08-23 stava per duplicare ~6500 righe di `STATO-EMPIRE.md`: git vede un file riscritto da capo e al merge non sa più cosa tenere. Normalizzato a mano a LF in quella sessione. **Due fix, entrambi utili a TASK-MEMORY-SYNC-W1**: (a) far scrivere le viste con `newline='
'` esplicito in `empire/memory/store.py`; (b) `.gitattributes` con `*.md text eol=lf`, che rende il repo immune a chiunque scriva CRLF, non solo a questo strumento. Nota collegata: lo strumento **non partiva affatto** (`ModuleNotFoundError: No module named 'yaml'`) finché non ho fatto `pip install pyyaml` — probabile vero motivo per cui la regola "usa `mem write`" veniva ignorata da 5 sessioni: non era pigrizia, era rotto. Aggiungere `pyyaml` alle dipendenze dichiarate | insieme a TASK-MEMORY-SYNC-W1 (è la stessa ferita) | **✅ CHIUSO 2026-09-03** (CP-20260903-002). Causa trovata: `Path.write_text(..., encoding="utf-8")` senza `newline`, che su Windows traduce ogni `\n` in `\r\n`. Due punti, non uno: `empire/memory/render.py::write_view` (le viste dei checkpoint) e **`empire/memory/state.py`** (STATO-EMPIRE.md — proprio il file che il 2026-08-23 stava per duplicarsi per ~6500 righe). Aggiunto `newline="\n"` a entrambi. Verificato sui BYTE, non a occhio: un checkpoint nuovo esce **CRLF 0 / LF 16**. Il `.gitattributes` non bastava: dice `* -text`, cioè *nessuna* conversione — quindi i CRLF prodotti dallo strumento arrivavano intatti in git. Resta da fare: `pyyaml` fra le dipendenze dichiarate (vedi B-032) |
| B-029 | **Il ramo Arena dei caroselli ha una SECONDA dipendenza mancante: `playwright_recaptcha`** | Chiudendo TASK-ARENA-SESSION-W1 (CP-20260827-004) e' stato tolto il primo blocco: `Core/browser_manager.py` moriva all'import su `playwright_stealth`, ora opzionale. Ma `ArenaAI/arena_generator.py` ha `from playwright_recaptcha import recaptchav2` a livello di modulo, e quel pacchetto **non e' installato**: il ramo Arena dei caroselli continua a non partire, per un motivo diverso da prima. Non installato in quella sessione perche' il solver captcha si porta dietro dipendenze audio (ffmpeg/pydub) e la scelta se dipenderci va fatta con Max, non di straforo. Due strade: (a) `pip install playwright-recaptcha` + dipendenze di sistema, (b) rendere opzionale anche questo import come fatto per lo stealth, cosi' il generatore parte e fallisce solo SE incontra davvero un captcha. La (b) e' coerente con la lezione appena imparata (un motore non deve morire per una dipendenza che serve a un ramo raro) | quando si riapre il ramo Arena dei caroselli (oggi la produzione usa il Ramo C, render locale) | ⬜ |
| B-030 | **`ArenaSession.stato_login()`: il ramo 'autenticato' non e' mai stato verificato su un profilo davvero loggato** | Il modulo condiviso decide lo stato della sessione dai cookie. Il ramo NEGATIVO e' verificato dal vivo (2026-08-27): `provisional_user_id` = identita' anonima, ed e' dominante perche' si e' scoperto che `arena-auth-prod-v1` - il cookie che *sembra* di autenticazione - **e' presente anche su un profilo sloggato**, quindi da solo non prova niente. Il ramo POSITIVO invece e' inferito, non provato: il 2026-08-27 non esisteva nessun profilo Arena autenticato su questa macchina con cui confrontare. Conseguenza accettata e dichiarata nel codice: in dubbio risponde `non_autenticato`/`ignoto`, mai `autenticato` - sbagliare per prudenza costa un login inutile, sbagliare al contrario costa un run che muore a meta'. Da confermare al primo login Arena reale: guardare quali cookie compaiono e stringere `COOKIE_SESSIONE` sul nome esatto | al primo login Arena reale | ⬜ |
| B-031 | **`empire mem write` non legge UTF-8 da stdin su Windows** | Verificato il 2026-08-27 scrivendo i checkpoint: `cat corpo.md | python -m empire mem write --body -` muore con `UnicodeEncodeError: surrogates not allowed` appena il testo contiene accenti, emoji o box-drawing - cioe' praticamente ogni checkpoint scritto in italiano. Aggirato in sessione mettendo `PYTHONIOENCODING=utf-8` davanti al comando, ed e' cosi' che sono stati scritti CP-20260827-001..004. Fix vero: leggere stdin come binario e decodificarlo esplicitamente in UTF-8 dentro il CLI (`sys.stdin.buffer.read().decode('utf-8')`) invece di affidarsi al codec di default della console. Stessa famiglia di B-028: lo strumento anti-collisione esiste e funziona, ma ogni asperita' che incontra e' un motivo in piu' per tornare a scrivere i checkpoint a mano - ed e' cosi' che B-009 e' riaccaduto 5 volte | insieme a B-028, prima che qualcuno riprovi a usarlo senza conoscere il trucco | ⬜ |
| B-032 | **`py -3` e `python` sono due interpreti diversi: solo uno regge `empire`** | Verificato il 2026-09-01: `py -3` risolve a **Python 3.12** che **non ha PyYAML** → `py -3 -m empire ...` muore con `ModuleNotFoundError: No module named 'yaml'` prima di eseguire qualsiasi comando. `python` risolve a **Python 3.11** (Store, `PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0`) e ha PyYAML, quindi `python -m empire mem write` funziona. È la stessa ferita di B-028 ("probabile vero motivo per cui la regola `usa mem write` veniva ignorata: non era pigrizia, era rotto") ma con la causa **precisa**: non manca il pacchetto, manca *nell'interprete che le regole invitano a usare*. Gli hook non ne soffrono (`emperator_hook.py` è solo stdlib e gira con `py -3`). Fix: `py -3 -m pip install pyyaml` per allineare i due, **oppure** dichiarare ovunque `python` come interprete degli strumenti di misura. Regola operativa intanto: **ogni comando `empire` si lancia con `python`, mai con `py -3`** | insieme a B-028, prima che una sessione ricada nella scrittura a mano dei checkpoint | ⬜ |

- **B-033** — `memory-empire/knowledge/` esiste in **3 copie**: due ferme al 2026-07-09
  (`.claude/skills/memory-empire/`, `Empire Studio Suite/memory-empire/`) e una viva con 53
  cartelle (`Empire Studio Suite/empire-studio/memory-empire/`). Chi ingerisce senza verificare
  scrive in un archivio morto. Da consolidare in uno solo, con le altre due ridotte a puntatore.
  Trovato durante CP-20260902-001. Non blocca l'ingestione: si scrive nella viva.

- **B-034** — PROPOSTA (da approvare da Max, non costruita): skill nuova `live-verification`.
  Prende una lista di claim CRO da verificare (spedizioni, form, CTA, recensioni, prezzo) e
  restituisce un blocco "Verificato dal vivo / Smentito dal vivo" con browser realmente
  renderizzato, riusabile da `market-audit`, `cro-ricerca` e `market-competitors`. Origine:
  video `yJOCyyP77bA` (Giovanni Beggiato / Gentes AI, batch max17 2/8) — il sistema mostrato
  smentisce dal vivo claim che un fetch statico avrebbe dato per veri (hreflang, traduzioni JS).
  Non costruita in questa sessione: solo proposta, il gap concreto e' gia' stato patchato
  direttamente dentro `market-audit/SKILL.md` (§1.1b).

- **B-035** — PROPOSTA (da approvare da Max, non costruita): valutare un MCP browser
  (Playwright) a livello progetto. Oggi `.mcp.json` di progetto ha solo `claude-flow`
  (risultato disconnesso in sessione, CONNECT_TIMEOUT) — nessun MCP di tipo browser-automation,
  il che limita ogni audit `market-*` alla lettura statica via `WebFetch`. Origine: video
  `yJOCyyP77bA`, stessa sessione di B-034. Decisione di stack, non una patch di skill.

- **B-036** — PROPOSTA (da approvare da Max, non costruita): skill nuova che applichi la
  tabella Mistake/Fix del profilo LinkedIn come sales page (headline = chi aiuti + risultato,
  custom button = link a calendario, featured section = case study/testimonial/metodologia)
  come deliverable di audit — sui profili del team DE e, in prospettiva, dei clienti CRO.
  Origine: video `-gq8euRvNR4` (Paolo Trivellato, batch max17 4/8). Non costruita in questa
  sessione: il gap concreto è già stato patchato direttamente dentro `avvia-linkedin/SKILL.md`
  (Fase 0), che copre l'uso operativo ma non un deliverable di audit dedicato/parametrizzato.

- **B-037** — PROPOSTA (da approvare da Max, non costruita): agente `outreach-profile-signal`
  che monitori i profile-view su LinkedIn (segnale di buying-intent: chi visita ripetutamente
  il profilo si è mosso per primo) e triggeri l'invio del messaggio soft del Meccanismo 2,
  adattato alla Bibbia dei Messaggi DE invece dello script fisso del video. Nessun agente
  outreach esistente (`outreach-message-writer`, `outreach-followup-sequencer`, team
  DEEP-INTEL) intercetta oggi questo segnale. Origine: video `-gq8euRvNR4`, stessa sessione
  di B-036.

- **B-038** — PROPOSTA (da approvare da Max, non costruita): workflow "Lead Magnet Post →
  Connessione → DM" — a partire da un post LinkedIn con call-to-comment, automatizza l'invio
  della risorsa gratuita a chi commenta e invia richiesta di connessione, loggando ogni nuova
  connessione come lead qualificato nel CRM (Areus o equivalente). Aggiungerebbe un canale
  organico "in entrata" che oggi manca del tutto: tutto lo stack outreach DE (Preventa, Areus,
  scraping) parte sempre da liste fredde/scraping, mai da engagement spontaneo su un post.
  Origine: video `-gq8euRvNR4`, stessa sessione di B-036/B-037.

- **B-039** — **115 delle 170 SKILL.md superano le 150 righe (68%).** Peggiori: `cro-youtube-lead-magnet`
  5.160 righe, `cro-call` 5.146, `cro-strategy-social-(ig-tiktok)` 3.942, `printing-press` 3.639,
  `cro-funnel-architect.md` 2.771. Una skill si carica **intera** quando si attiva: migliaia di righe
  caricate per rispondere a una domanda che ne richiede decine sono budget bruciato a ogni
  invocazione. Rimedio proposto: refactoring a router + file dedicati (progressive disclosure),
  affidabile a `skill-creator` e `chief-forge`, che esistono già — **nessuna skill o agente
  nuovo serve**. Da approvare da Max prima di partire: tocca 115 file. Origine: video `8NSyI-npJCU`
  (Jay E | RoboNuggets, batch max17 5/8) — soglia "150+ righe" presa dal suo prompt "Skills Level 3",
  non uno standard Anthropic. Non costruito in questa sessione per vincolo esplicito del task
  (refactoring di 115 file, non da eseguire di slancio).

- **B-040** — PROPOSTA (da approvare da Max, non costruita): ricerca semantica sulla wiki
  (salto al Livello 3). Con 1.831 pagine in `second-brain-vault/wiki/` la ricerca resta
  lessicale: si trova solo cio' di cui si conosce gia' il nome file o il wikilink esatto.
  Opzione a costo zero indicata dal video: plugin Obsidian "Smart Connections" installato
  direttamente sulla vault esistente (ricerca per significato/embeddings, locale, gratuito).
  Impatto diretto su `conoscenza-empire`, che oggi puo' dichiarare un vuoto di conoscenza che
  in realta' e' solo un termine mancato — patchato in questa stessa sessione con la nota di
  onesta' epistemica corrispondente. Origine: video `DTCyvo6cC54` (Nate Herk | AI Automation,
  batch max17 8/8).

- **B-041** — PROPOSTA (da approvare da Max, non costruita): logica di pruning della wiki
  (two-bucket test: cosa resta consultabile come conoscenza core, cosa si archivia perche'
  specifico/mutevole). Una wiki che cresce e non pota diventa rumore — rischio concreto con
  1.831 pagine e nessun criterio esplicito scritto oggi in `second-brain-vault/wiki/` su cosa
  NON va mai ingerito. Origine: video `DTCyvo6cC54`, stessa sessione di B-040.

---

## Aggiornamenti del 2026-09-03 (ordine di Max: *"approvo tutto, prendi il controllo"*)

- **B-040 — PARZIALMENTE CHIUSA.** Costruito `scripts/cerca_wiki.py`: indice su 1.547 pagine,
  dizionario dei sinonimi del mestiere, radici (taglio delle desinenze), peso per rarita' della
  parola, normalizzazione per stazza della pagina, deduplica dei doppioni, riga di contesto nei
  risultati. Verificato: *"quanto spesso pubblicare"* ora trova *"Come generare oltre 50.000 a
  settimana postando ogni giorno"*, che prima era invisibile; *"gestione delle obiezioni sul
  prezzo"* ora restituisce cinque pagine sulle obiezioni, dove prima dava pagine di lancio corsi.
  **Resta aperta la parte semantica vera** (embeddings): richiede o un modello locale non
  installato, o mandare 1.837 pagine private a un servizio esterno — decisione di Max, non presa.

- **B-042 — CHIUSA, diventata ADR-017.** La proposta di revisione con un modello di famiglia
  diversa e' stata approvata da Max il 2026-09-03 e attivata in **pilota su Preventa Outreach**
  (perimetro stretto perche' l'istruttoria stessa dichiarava di non avere prove sufficienti per
  un'estensione totale). Vedi `decisions/ADR-017-revisione-modello-diverso.md`.

- **B-043 — NUOVA, la piu' grave emersa oggi.** **Digital Empire non misura un solo euro:**
  ne' ricavi, ne' costi effettivi, ne' una sola metrica del percorso di vendita (contatti,
  chiamate, preventivi, chiusure). Scoperta lavorando ai file del Board: il CFO sorveglia i costi
  di un'azienda che non ha mai misurato un incasso, il CRO ha uno `stato_pipeline` che e'
  un'opinione, il CMO ha un ciclo di analisi senza dati in ingresso. **E' la ragione per cui
  nessuno si era accorto che il magazzino era pieno e le vendite zero.** Nessuna decisione presa:
  va deciso da Max cosa iniziare a misurare per primo.

- **B-044 — NUOVA.** Non esiste un caricatore automatico per Amazon KDP: i libri pronti vanno
  caricati a mano. Costruirlo o rinunciarci e' una decisione aperta (origine: ADR-016).

- **B-045 — NUOVA.** I caroselli non sono sorvegliati dall'Ultimo Metro: sono sparsi in cartelle
  senza schema comune. Va prima deciso dove vive un carosello finito (origine: ADR-016).

- **B-046 — Rinumerare uno dei due ADR-012 e correggere i quindici puntatori.**
  Due file portano il numero 012 (`ponte-memory-wiki` del 23 ago, di Max; `orchestration-layer-canonico`
  del 26 ago, di Neri). Quindici file citano "ADR-012" senza dire quale. Da fare **a mano**, un
  puntatore alla volta, e **solo dopo** la decisione di Max su quale motore di orchestrazione sia
  canonico (ADR-018 §4) — perche' quella decisione potrebbe rendere uno dei due un ADR superato,
  e allora la rinumerazione sarebbe lavoro diverso.
  I quindici: `company/Memory/STATO-EMPIRE.md`, `company/Memory/INDEX.md`,
  `company/Memory/checkpoints/CP-20260826-001.md`, `company/Memory/checkpoints/CP-20260823-007.md`,
  `company/Ecosistemi/11-APEX-7-CORE/README.md`,
  `company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/docs/adr/012-nonproduction-pilot-package.md`,
  `company/Board-CSuite/CTO/state/README.md`, `company/Board-CSuite/CTO/agenti/cto-memoria.md`,
  `company/Board-CSuite/CTO/agenti/cto-conductor.md`, `.claude/agents/sentinel-drift.md`,
  `.claude/agents/guild-quality.md`, `.claude/skills/ocp-control-plane/SKILL.md`,
  `.claude/skills/ruflo/v3/@claude-flow/hooks/src/workers/index.ts`, piu' i due ADR stessi.
  Origine: ADR-018.

- **B-047 — DECISIONE APERTA PER MAX, la piu' urgente: due motori di orchestrazione sono
  entrambi canonici.** `11-APEX-7-CORE` (per ADR-010/011) e `orchestration-layer` (per
  ADR-012 del 26 ago, che dichiara da se' di contraddirli, con la Fase 2 di migrazione mai
  iniziata). Aperto da otto giorni. Tre strade con i loro costi in ADR-018 §4. Raccomandazione
  di Emperator: strada A, ma non prima di averne parlato con Neri.

- **B-048 — La soglia di 0,50 EUR per chiamata non ha nessuna fonte in casa.** Esisteva solo
  dentro il file che la applicava: nessun documento dell'Impero la stabilisce. Declassata a
  soglia di attenzione non normata dentro `sentinel-cost`. Va decisa da Max o eliminata.
  Seconda incoerenza nella stessa area: `cfo-empire.md` dice allarme al 70%, i principi e i KPI
  del CFO dicono 80%, il README del Cost Sentinel dice 60/80/95/100. Applicata la scala a quattro
  gradini; il 70% va sanato. Origine: lavoro sulle sentinelle del 2026-09-03.

## Aggiornamenti del 2026-09-03, secondo turno (delega piena di Max)

- **B-043 — CHIUSA.** Nasce il reparto TESORERIA (ADR-020): motore `scripts/tesoreria.py`,
  skill `tesoreria`, 5 agenti, dati in `company/Memory/tesoreria/`. Digital Empire adesso
  puo' contare ogni euro che entra e ogni euro che esce, e avere il quadro in qualunque
  momento. Collaudato con 5 movimenti di prova (verificato che una rettifica non venga
  contata due volte), poi ripulito: i file dell'azienda partono vuoti.

- **B-047 — CHIUSA.** Decisione presa da Emperator per delega esplicita di Max (ADR-019):
  il motore di orchestrazione canonico e' **`orchestration-layer`**. Ragioni misurate oggi:
  133 file di codice contro 28, 24 test contro 3, e sta gia' DENTRO `11-APEX-7-CORE`
  (quindi nessuna violazione territoriale: ADR-011 vietava le linee divergenti FUORI).
  **Il fatto che ha chiuso la questione: nessuno script dell'azienda chiama nessuno dei
  due motori.** Le citazioni stanno tutte nei documenti di memoria, mai nel codice. La
  Fase 2 di migrazione riguardava zero consumatori. Era una guerra per un trono su cui
  non si e' mai seduto nessuno.
  Condizione scritta nell'ADR: se entro tre mesi nessun lavoro reale usa il motore, l'ADR
  si riapre e la domanda diventa se all'Impero serva un motore di orchestrazione.

- **B-049 — NUOVA. Il percorso di vendita non e' misurato.** La tesoreria conta i soldi,
  non cio' che li precede: contatti generati, chiamate fatte, preventivi mandati, tasso di
  chiusura, tempo fra primo contatto e incasso. **Resta il buco piu' grande del CRO**, il
  cui `stato_pipeline` e' oggi un'opinione. Va chiuso con lo stesso metodo della tesoreria:
  prima uno strumento che gira, poi il reparto attorno. Origine: ADR-020 par. 5.

## Dallo studio di Will Barron, "Sistemi di vendita" (5swDtQFyIws) — 2026-09-03

> NOTA DI SERVIZIO: lo scagnozzo che ha chiuso questo ciclo aveva numerato le proprie
> proposte B-042..B-045, **numeri gia' occupati**. Rinumerate qui da Emperator in
> B-050..B-053. Lezione per i prossimi: **il numero di pratica si prende leggendo il
> backlog, non ricominciando da dove sembra libero.**

**La diagnosi che le tiene insieme:** il fatturato oscilla perche' **la consegna e' un
processo scritto e la vendita no**. Digital Empire ha gia' lo script migliore per la
chiamata (`cro-call`, 5.170 righe, piu' profondo della fonte), ma **non ha niente nei due
tratti che la circondano**: fra "ha prenotato" e "e' in chiamata" non tocca il potenziale
cliente, e dopo la chiamata non blocca ne' misura niente. Un sistema di vendita non e' una
chiamata fatta bene: e' la catena che la precede e la segue, e la catena si spezza dove
nessuno guarda.

- **B-050 — PROPOSTA: skill `pre-call-indoctrination`.** Fra la prenotazione e la chiamata
  oggi DE non fa nulla (la checklist pre-chiamata ha 10 punti, **tutti dalla nostra parte,
  nessuno verso il cliente**). La skill coprirebbe: email di conferma, pagina con video,
  verifica preliminare, risposte alle 4 obiezioni classiche. Verificato assente: la ricerca
  su `indottrin|indoctrinat|pre-call` trova solo `cro-call` (preparazione nostra) e
  `discovery-call-brief` (dopo la chiamata).

- **B-051 — PROPOSTA: agente `sales-funnel-auditor`.** Legge le schede post-chiamata di
  `cro-call` e i brief di `discovery-call-brief` e restituisce **la conversione per fase**:
  contatto→incontro, incontro→scoperta, scoperta→proposta, proposta→chiuso. Nessun agente
  in `.claude/agents/` lo fa oggi: `cro-empire` supervisiona senza misurare, `cfo-empire`
  conta i costi e non le conversioni. **Si sovrappone a B-049** (il percorso di vendita non
  e' misurato): vanno decisi insieme, e probabilmente sono lo stesso lavoro.

- **B-052 — PROPOSTA: workflow "dopo la chiamata".** Documento di sintesi + prossimo passo
  gia' in calendario come **unica azione non completabile a meta'**. Fa partire anche il
  timer di 48 ore che `proposal-gate` gia' pretende e che **oggi nessuno avvia**.

- **B-053 — DECISIONE APERTA PER MAX (tensione reale, non risolta):** pubblicare il prezzo
  **prima** della chiamata, come fa la fonte (mette gli 8.000 dollari nelle domande
  frequenti), contro la **Regola Assoluta n.6 di `cro-call`** che vieta il prezzo prima
  della diagnosi. Le due posizioni sono entrambe difendibili e **si escludono**: la fonte
  filtra chi non puo' permetterselo prima di sprecare una chiamata, la nostra regola evita
  che il prezzo venga giudicato senza il valore accanto. Nessuna delle due e' stata
  misurata su dati DE. Va decisa, non appianata.

**Applicato subito, non proposto (+64 righe, 0 cancellazioni):**
`cro-call` +24 (citazione diretta obbligatoria in apertura di Pagina 2, con modello,
principio di coerenza, caso socio/capo/coniuge, errore del "linguaggio da agenzia");
`icp-radar` +29 (campo `trigger_evento` + prova del riconoscimento in 1 secondo);
`discovery-call-brief` +11 (campi `trigger_evento`, `prossimo_passo_data_ora`,
`prossimo_passo_in_calendario` + 2 punti di controllo).

**"Niente da fare" dichiarato, e vale quanto le proposte:** `proposal-gate` non toccato
(il suo criterio 1 impone gia' il problema con le parole del cliente: un criterio
quasi-duplicato allunga il controllo senza stringerlo). `beast-preventivi`,
`cro-copy-architect`, `cold-email` non toccati: **su contatto a freddo e copy l'Impero e'
gia' piu' avanti della fonte**, che da' principi senza testi.

- **B-054 — DA CORREGGERE, errore trovato oggi.** Uno scagnozzo ha dichiarato che «nessun
  hook pre-commit risulta installato». **Falso, e verificato:** `git config core.hooksPath`
  vale `.githooks`, dove vivono `check_memory.py` e `check_blob.py`. Lo stesso guardiano ha
  bloccato un commit di Emperator il 2026-09-03 alle 12:5x per CRLF in `company/Memory/`.
  L'errore nasce dal cercare in `.git/hooks/` invece che nella cartella configurata.
  **Da scrivere nei prompt degli scagnozzi e in `guild-prompt`:** i guardiani di questo
  repo stanno in `.githooks/`, non in `.git/hooks/`.
