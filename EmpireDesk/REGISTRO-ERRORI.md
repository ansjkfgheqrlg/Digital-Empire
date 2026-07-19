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

## EDE-A1 (2026-07-19, Max — PREVENTIVO, non ancora manifestato)
**Cosa:** `modules/licenze.py::_run` usa `sys.executable` per lanciare gestione-licenze.py.
In dev funziona; da exe FROZEN `sys.executable` = `EmpireDesk.exe` stesso → rilancerebbe l'app
invece di python (stesso identico problema già risolto in `app.py::_python_bin()`).
**Fix da fare (Max, prima del primo build exe con moduli):** riusare `_python_bin()` (o copia
locale) in licenze.py. **Regola:** in OGNI modulo che lancia python, MAI `sys.executable` nudo —
sempre il resolver frozen-aware.
