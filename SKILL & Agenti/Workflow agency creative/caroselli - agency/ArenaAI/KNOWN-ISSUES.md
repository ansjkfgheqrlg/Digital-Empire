# ArenaAI — Bug reali trovati e corretti (leggere PRIMA di modificare questo motore)

Motore condiviso da `caroselli - agency/` (Agency) e `caroselli - preventa/`
(Preventa) — un bug qui rompe entrambi i progetti. Ogni bug qui sotto è stato
trovato con **screenshot reali**, non ipotizzato dal solo log: `force=True` su
Playwright bypassa il controllo "receives events", quindi un click che finisce
su un elemento sbagliato (nascosto, sotto un modal, ecc.) **non genera mai un
errore** — il log sembra pulito anche quando niente ha funzionato. Regola
pratica: se un run produce 0 risultati senza nessuna eccezione, non fidarti del
log da solo, prendi uno screenshot reale a metà flusso.

## 1. Crash su encoding console Windows (emoji)
- **Sintomo**: `UnicodeEncodeError: 'charmap' codec can't encode character` non
  appena il copywriter mette un'emoji nella caption (il prompt gliele chiede
  esplicitamente).
- **Causa**: console Windows di default = cp1252, non regge emoji/unicode esteso.
- **Fix**: `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` a inizio
  script, prima di qualunque `print`. Stesso bug/fix già noto nella fabbrica
  YouTube (CP-20260731-001).
- **Dove**: `orchestrator_preventa.py` (e qualunque futuro `orchestrator_X.py`).

## 2. Selettore che clicca un duplicato nascosto (mode-switch Battle→Direct)
- **Sintomo**: nessun errore, ma la UI restava sempre in "Battle Mode" — mai
  passata a "Direct" nonostante il log dicesse il contrario in alcuni run.
- **Causa**: `page.locator("button")` (senza `:visible`) matchava un bottone
  duplicato **nascosto** nel DOM con lo stesso testo "Battle Mode".
- **Fix**: `page.locator("button:visible")` + `wait_for(state="visible")`
  prima di cliccare — forza a prendere l'elemento che l'utente vede davvero.

## 3. Browser crashato a metà run mai recuperato
- **Sintomo**: dopo un crash di Chrome (spesso durante una risoluzione
  captcha), OGNI tentativo successivo — per tutte le slide rimanenti —
  falliva all'istante con `Target page, context or browser has been closed`.
- **Causa**: il codice riusava una variabile `page` ormai morta invece di
  accorgersi che il browser non c'era più.
- **Fix**: nel blocco `except`, se il messaggio contiene "closed", richiude il
  manager e ne riapre uno nuovo (`BrowserManager` + `get_context` +
  `new_page`) prima di ritentare.

## 4. Due modal mai gestiti bloccano tutto in silenzio (root cause del fallimento 9/9 tentativi)
- **Sintomo**: 2 run completi (9 tentativi totali, 3 slide × 3 tentativi), **0
  immagini generate, 0 eccezioni nel log**. Tutto sembrava funzionare
  (Direct mode attivata, Image toggle cliccato) ma non usciva mai nulla.
- **Causa reale** (trovata solo con screenshot):
  1. Al primo caricamento, Arena mostra un banner cookie ("This website uses
     cookies" / Accept Cookies). Mai gestito. Un click `force=True`
     successivo può far scivolare nel modal esteso "Manage Cookie
     Preferences", che copre **tutta** la UI.
  2. La prima volta che si invia davvero un prompt in una sessione, Arena
     apre un secondo gate: "Terms of Use & Privacy Policy / Agree". Il primo
     click su "submit" viene **assorbito da questo gate** invece di inviare
     il prompt — il prompt resta scritto, non parte mai.
- **Fix**: `dismiss_blocking_dialogs(page)` — riconosce ed accetta
  Accept Cookies/Accept all/Agree, con fallback a `Escape` per qualunque
  altro dialog residuo. Richiamata in **più punti** (non basta una volta
  sola, i due modal compaiono in momenti diversi): inizio `setup_arena_chat`,
  dopo il toggle Image, prima di ogni submit. Dopo il submit, se il gate
  compare, va ridato focus al textarea (il focus si perde quando il modal si
  apre/chiude) e rifatto il click — un secondo click "a freddo" non basta.

## 5. ⚠️ Login Google bloccato da Playwright — non è un bug di selettori
- **Sintomo**: sessione salvata (`session_data/`, ferma da mesi) scaduta a
  metà di un run automatico → Arena reindirizza a un vero login Google
  (`accounts.google.com`) → Google mostra "Questo browser o app potrebbe non
  essere sicuro" e blocca il login.
- **Causa**: non è un problema di stealth insufficiente — `BrowserManager`
  usa già Chrome reale (`channel="chrome"`), `--disable-blink-features=
  AutomationControlled`, `ignore_default_args=["--enable-automation"]`,
  `playwright-stealth`. Google rileva il protocollo CDP stesso (con cui
  Playwright parla al browser), non solo il fingerprint — è una misura
  anti-phishing lato server, non bypassabile in modo affidabile con altri
  trucchi lato client.
- **Fix reale**: NON tentare il login dentro una sessione guidata da
  Playwright. Aprire lo stesso `session_data/` con Chrome **normale** (un
  processo lanciato direttamente, non tramite `sync_playwright()`), far
  loggare un umano vero (mouse/tastiera reali), chiudere quella finestra. I
  cookie di sessione restano sul profilo — le run automatiche successive li
  riusano senza dover rifare il login (Google non ri-sfida ogni singola
  azione, solo il momento del login).
  ```
  "C:\Program Files\Google\Chrome\Application\chrome.exe" ^
    --user-data-dir="<percorso>\ArenaAI\session_data" https://arena.ai/
  ```
- **Prevenzione**: se il profilo resta inutilizzato per mesi la sessione può
  scadere di nuovo. Un uso periodico (anche solo aprire arena.ai una volta a
  settimana) riduce il rischio, non lo elimina — mettere in conto che potrà
  ricapitare.

## Come evitare di riscoprire questi bug alla cieca in futuro
Se un run produce 0 risultati senza errori, PRIMA di aggiungere altri
selettori/retry: scrivere uno script diagnostico minimo (1 solo prompt, no
retry, `page.screenshot()` a ogni step chiave) — è quello che ha trovato tutti
e 4 i bug sopra in meno tempo di quanto ne avrebbe richiesto continuare a
tirare a indovinare sui selettori. Vedi il pattern in
`caroselli - preventa/debug_arena_state.py`.
