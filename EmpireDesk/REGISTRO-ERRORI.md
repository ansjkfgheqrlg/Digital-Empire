# REGISTRO-ERRORI — Empire Desk (memoria di debug)

**Scopo:** ogni errore riscontrato va scritto QUI con causa radice + fix + **regola per non
ripeterlo**. Prima di modificare o buildare: leggere questo file. **Nessun errore va commesso
due volte.** Pattern ereditato da `Clienti/Prof Autocad/preventivo-forge/REGISTRO-ERRORI.md`
(ISPETTORATO GENERALE — REGISTRO-ERRORI + gate anti-recidiva).

---

## Lezioni EREDITATE da PreventivoForge — applicate FIN DALL'INIZIO in Empire Desk

Queste non sono errori nuovi: sono errori già commessi in un'app gemella (stesso stack GUI),
qui applicati come regola preventiva invece di ri-scoprirli.

| Da (PreventivoForge) | Lezione | Come si applica qui |
|---|---|---|
| E11 (CP-20260715-001) | pywebview dipende da WebView2 Runtime: se manca sul PC, **fallisce IN SILENZIO** e l'utente vede un'app diversa/vecchia senza errore visibile | Motore **Chrome-app PRIMO** (server locale + `chrome --app`), non dipende da WebView2. pywebview è fallback #2, Tkinter fallback #3. Vedi `app.py::main()` |
| E8, E9 | Rebuild/zip con l'app aperta blocca file (log, dll) → build fallisce in silenzio, exe vecchio consegnato | `build_exe.bat` ricorda di chiudere EmpireDesk.exe + i Chrome aperti prima di ribuildare |
| E1 | "Riuscito" ≠ "non bloccato": un processo può aprirsi senza fare nulla di reale | Ogni tile mostra **l'exit code reale** del subprocess (mai un finto "fatto") — Gate 1 dossier 17 |
| R3 (E3/E4) | Bloccare su difetti che NON sono nostri genera falsi negativi | Il **selftest** di Empire Desk verifica solo path/eseguibilità (nostro dominio), MAI il contenuto/esito dei runtime esterni (non è compito nostro giudicarli) |
| Pattern generale | "Bottone finto" = promessa falsa (Mandato Art.2) | Ogni tile v0.1 lancia un `subprocess.Popen` su un file REALE verificato in `TileManager._resolve_check` — zero placeholder |

---

## Regole permanenti (nuove, specifiche di Empire Desk)

1. **L'app è un LAUNCHER, non riscrive nulla** (ADR-003): se una tile "richiederebbe" logica
   nuova, si wrappa lo script/bat esistente — mai copiare la logica di un motore dentro app.py.
2. **Selftest non lancia mai un'automazione a costo reale** (Mandato Art.4.3, dry-run prima di
   spendere): verifica solo che il comando SIA lanciabile (path esiste, eseguibile trovato),
   non lo esegue. Il lancio vero avviene solo al click esplicito dell'utente.
3. **Path robusti**: `REPO_ROOT` si risolve risalendo le cartelle cercando `PIANO-MAESTRO/` +
   `company/` (marcatori del monorepo), non un path assoluto hardcoded — l'exe può stare in
   qualsiasi sottocartella del repo (dev o `dist/`).
4. **Zero secrets nell'app**: nessuna chiave/API hardcoded; le automazioni lanciate leggono i
   propri `.env` locali (invariato, Empire Desk non li tocca).
5. **Un solo processo per tile alla volta**: `TileManager.launch` rifiuta un secondo lancio se
   la tile è già `running` (evita doppie automazioni concorrenti sullo stesso runtime).

## Come si usa
- Nuovo errore → nuova riga in tabella (ID progressivo EDE-1, EDE-2, …) + eventuale nuova regola.
- Prima di un fix, controllare se la causa è già nota qui O nel registro gemello di PreventivoForge.

## Errori registrati (Empire Desk, in ordine cronologico)

| ID | Sintomo | Causa radice | Fix | Regola |
|----|---------|--------------|-----|--------|
| **EDE-1** | Tile Outreach Email/Instagram restano "in corso" per sempre | `AVVIA-EMAIL-LIVE.bat` e `_avvia_ig.bat` finiscono con `pause` (aspettano un tasto); il subprocess senza stdin chiuso resta appeso in attesa per sempre | `subprocess.Popen(..., stdin=subprocess.DEVNULL)` in `TileManager.launch` — `pause` con stdin chiuso stampa il messaggio e prosegue subito (`app.py`) | Ogni subprocess lanciato da un launcher deve avere `stdin` esplicito (mai ereditato), specialmente se il target è un `.bat` scritto per uso interattivo |
| **EDE-2 (noto, NON risolto — fuori scope EmpireDesk)** | Tile LinkedIn (e potenzialmente Email/Instagram) falliscono al lancio su PC diversi da quello originale | `run_daily.bat` ha un path Python hardcoded di UN'ALTRA macchina (`C:\Users\Utente\AppData\...\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe`); `AVVIA-EMAIL-LIVE.bat`/`_avvia_ig.bat` hanno `cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\..."` hardcoded (percorso di un PC diverso da questo) | **NON risolto qui**: sono script del runtime Outreach ATTIVO (ADR-003 — wrap, mai riscrittura; sistemi attivi intoccabili). EmpireDesk li lancia così come sono | Il **selftest** di EmpireDesk verifica solo che il FILE .bat esista (suo dominio), non che il suo CONTENUTO sia portabile — quello è responsabilità di chi possiede lo script Outreach. Segnalato a Max/Gael: da sistemare nei bat originali (path relativi), non in EmpireDesk |
| **EDE-3 (rischio noto, non ancora verificato)** | Se EmpireDesk crasha/si riavvia mentre una finestra Chrome-app precedente è ancora aperta con lo stesso `chrome-profile/`, il nuovo `chrome.exe --app` potrebbe fondersi nel processo Chrome già aperto (singleton su user-data-dir) ed uscire subito, lasciando il server locale (thread daemon) terminato ma la finestra visivamente aperta e "morta" (fetch falliranno) | Comportamento singleton di Chrome su user-data-dir condiviso | Non ancora mitigato in v0.1 (basso rischio: capita solo su doppio avvio/crash). Mitigazione futura (P5): lock file proprio + rilevazione "processo tornato subito" → riavviare server e riaprire finestra, o avvisare l'utente di chiudere la finestra vecchia | — |
| **EDE-4** (trovato da Max col selftest reale, 7/8) | Tile Caroselli: selftest FAIL — "script non trovato" | `"script": "scripts/generate.js"` era relativo alla CWD della tile, ma `_resolve_check`/`_build_argv` lo risolvono sempre da `REPO_ROOT` (come tutte le altre tile) → puntava a `<repo>/scripts/generate.js`, inesistente | `TILES["caroselli"]["script"]` corretto al path completo da REPO_ROOT: `"Workfolw crea caroselli à/carousel-factory/scripts/generate.js"` (`app.py`) | Il campo `script` di OGNI tile è SEMPRE relativo a `REPO_ROOT`, mai alla sua `cwd` — le due cose sono facili da confondere quando `cwd` e cartella dello script coincidono quasi (lezione da riapplicare se si aggiungono nuove tile) |
| **EDE-5** (trovato da Max, non rilevabile dal selftest — solo lanciando davvero) | Tile Caroselli avrebbe lanciato `generate.js` senza argomenti → `process.argv[2]` assente → lo script stampa l'uso ed esce con `exit 1` SEMPRE, a prescindere da cosa fa l'utente: bottone che "sembra" funzionare (parte, produce un log, ha un exit code) ma non fa mai il suo lavoro | `generate.js` richiede un file JSON carosello come argomento; la tile non aveva un campo `input` per fornirlo | Aggiunto `"input": "path"` alla tile; generalizzato il meccanismo "input" (prima solo `"url"` per Studio) a qualsiasi tipo — l'UI mostra un placeholder diverso per tipo (`INPUT_PLACEHOLDER` in `ui/index.html`); `TileManager.launch` ora valida che il path esista (assoluto, relativo alla cwd della tile, o relativo a REPO_ROOT) PRIMA di lanciare, invece di lasciar fallire il subprocess | Il **selftest statico** (path/eseguibile esiste) NON basta a garantire "zero bottoni finti" (Gate 1) quando lo script richiede argomenti runtime — va sempre controllato anche COSA si aspetta lo script come input, leggendone il codice, non solo la sua esistenza |
| **EDE-6** (trovato in autorevisione, prima di qualsiasi lancio — B1) | I 2 bottoni header ("Pannelli"+"Selftest") erano posizionati con `right:Npx` calcolato a mano su elementi `position:absolute` indipendenti → a font/finestra diversi rischiavano di sovrapporsi visivamente (difetto grafico silenzioso, nessun errore in console) | Calcolo manuale dei pixel invece di un layout che si adatta da solo | Header convertito a `display:flex; justify-content:space-between` con `.htext` (brand+sottotitolo) e `.hactions` (bottoni, `display:flex;gap:10px`) come due blocchi flex — zero calcolo a mano, zero rischio sovrapposizione a qualsiasi lunghezza testo/finestra (`ui/index.html`) | Mai posizionare più elementi UI con `position:absolute` + offset calcolati a mano quando un contenitore flex risolve lo stesso layout senza rischio — specialmente se altri moduli (B2-B4, A1-A4) aggiungeranno altri bottoni header in futuro |
| **EDE-7** (trovato in autorevisione, prima di qualsiasi lancio — B1) | Una tile fornita da un modulo con schema sbagliato (es. manca `script`/`cwd`, o `kind` sconosciuto) avrebbe fatto **KeyError** in `TileManager._resolve_check`/`_build_argv` al primo `list_tiles()`/selftest — un modulo scritto male avrebbe fatto cadere la lettura di TUTTE le tile, incluse le 8 core | `_load_modules()` metteva la tile del modulo in `_MODULE_TILES` senza validarne lo schema prima | `_validate_module_tile()` verifica campi obbligatori (id/icon/name/desc/kind + script+cwd o path) e collisioni di `id` con tile già esistenti PRIMA di accettarla; se invalida, va in `_MODULE_LOAD_ERRORS` (visibile nel selftest) e le routes/panel dello stesso modulo restano comunque montati | "Un modulo rotto non deve mai far cadere l'app" vale per OGNI pezzo che un modulo può fornire (tile, routes, panel) — vanno validati e isolati singolarmente, non solo l'import del file |

## EDE-A1 (2026-07-19, Max — PREVENTIVO, non ancora manifestato)
**Cosa:** `modules/licenze.py::_run` usa `sys.executable` per lanciare gestione-licenze.py.
In dev funziona; da exe FROZEN `sys.executable` = `EmpireDesk.exe` stesso → rilancerebbe l'app
invece di python (stesso identico problema già risolto in `app.py::_python_bin()`).
**Fix da fare (Max, prima del primo build exe con moduli):** riusare `_python_bin()` (o copia
locale) in licenze.py. **Regola:** in OGNI modulo che lancia python, MAI `sys.executable` nudo —
sempre il resolver frozen-aware.
