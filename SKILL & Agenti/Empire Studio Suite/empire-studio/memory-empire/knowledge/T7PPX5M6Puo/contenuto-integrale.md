# Contenuto Integrale — T7PPX5M6Puo
## "Claude Code + Codex: Il Setup di cui NESSUNO Parla" — Riccardo Belli Contarini (Martes AI)

**Fonte audio:** trascrizione italiana auto-generata YouTube (`T7PPX5M6Puo.it.vtt`), letta integralmente in sessione precedente (850 segmenti puliti dopo deduplicazione) e riportata per esteso in `video-analysis.md`.
**Fonte visiva:** 197/197 frame unici letti nativamente su 926 frame densi estratti (soglia scene-detector 3.0, interval 2.0s, riduzione 78.7%). Coverage 100% dei frame unici, 0 illeggibili in modo persistente. Dettaglio completo in `runs/max17-v06-belli-codex/coverage.md`.
**Durata:** 30:52 (1852s) · **Canale:** Riccardo Belli Contarini — fondatore/CEO di **Martes AI**, agenzia AI "partner a 360°" (65+ aziende clienti, 75+ soluzioni AI in produzione, agosto 2026) · **Lingua:** italiano
**Run sorgente:** `empire-studio/runs/max17-v06-belli-codex`
**Archiviato:** 2026-09-02 (Memory Empire Stage C)

> **Regola applicata:** questo file espande e riorganizza `video-analysis.md` (già completo, walkthrough cronologico verificato su 197/197 frame) per categoria — setup, ruoli, i 3 casi reali con i finding integrali, costi — **senza riassumere**: ogni comando, ogni tabella, ogni finding di sicurezza trascritto compare qui per intero. Nessuna nuova visione dei frame in questa sessione: fonti usate sono `video-analysis.md`, `atoms.json` (70 KA) e `coverage.md`, già certificati NO-FINTO PASS.

---

## PARTE 1 — IL SETUP INTEGRALE

### 1.1 Posizionamento e premessa (0:00–1:16)

Belli apre dicendo che la domanda "Claude Code o Codex?" è sbagliata; la domanda giusta è **"come ottengo il massimo da entrambi?"** (frame-001–010, overlay a schermo: *"Come posso ottenere il massimo da entrambi?"*). Si presenta come ingegnere informatico, fondatore di **Martes AI**, agenzia che forma aziende su Claude Code/Claude Cowork e costruisce soluzioni AI custom: **65+ aziende clienti, 75+ soluzioni AI portate in produzione** (frame-030, frame-031, card statistiche animate). Dichiara di usare Claude Code e Codex ogni giorno lui e il suo team.

Nota di naming (dichiarata a confidenza moderata/inferita): nei grafici a schermo (frame-008) compaiono le etichette **"Fable 5"** e **"GPT-5.6 Sol"**, nomi informali/colloquiali che Belli usa rispettivamente per un modello Claude (Opus) e un modello Codex/GPT — non nomi ufficiali. Nel terminale reale (frame-734, frame-748) il modello Claude selezionato appare come **"Opus 5 [1M context]"**.

### 1.2 Requisiti ufficiali (dal README, frame-121–130)

- ChatGPT subscription (incl. Free) **oppure** OpenAI API key — l'utilizzo consuma la quota Codex.
- Node.js ≥ 18.18.
- Fonte: repository GitHub ufficiale OpenAI, **"Codex Plugin"** (`openai/codex-plugin-cc`), licenza Apache-2.0 (visibile in frame-609/617/630, header pagina README).

### 1.3 Installazione — sequenza esatta osservata in terminale VS Code (8:25–10:40, frame-239–330)

Setup mostrato dal vivo dentro **Visual Studio Code**, estensione **Claude Code**, terminale integrato. Prerequisiti dichiarati: VS Code + Claude Code già installati. Ambiente: **solo Mac + VS Code** dimostrato — nessuna prova su Windows, terminale nativo o altri editor.

Sequenza:

1. Ricerca Google "codex plugin" → primo risultato: repo GitHub ufficiale di OpenAI (frame-255–261).
2. Apre terminale VS Code, lancia `claude`.
3. `/plugin marketplace add openai/codex-plugin-cc` → risposta osservata: **"Successfully added marketplace: openai-codex"**.
4. `/plugin install codex@openai-codex` → risposta osservata: **"Installed codex. Plugin is now active."**
5. `/reload-plugins` → risposta osservata: **"Reloaded: 8 plugins · 18 skills · 7 agents · 4 hooks · 5 plugin MCP servers · 8 plugin LSP servers"**. I singoli 7 agenti e 4 hook non vengono mai elencati o descritti individualmente nel video.
6. `/codex:setup` → Claude Code esegue uno shell command (`node ".../scripts/codex-companion.mjs" setup --json`) e rileva che Codex non è installato; propone un menu interattivo:
   ```
   1. Install Codex (Recommended)
      Runs `npm install -g @openai/codex`, then re-checks setup status.
   2. Skip for now
      Leaves Codex uninstalled; the setup output is reported as-is.
   ```
   Belli sceglie l'opzione 1. Il primo tentativo fallisce: **"zsh: command not found: codex"** — il pacchetto npm non aveva ancora linkato il binario. Claude Code stesso rileva il problema e attende: *"Hold off on codex login for a moment — the npm install hasn't linked the binary yet."* Dopo l'attesa (~8 minuti, install log), il comando riesce.
7. Login manuale alternativo indicato a voce: `codex login` (interattivo, richiede account ChatGPT).
8. Installazione manuale alternativa di Codex CLI (dal README): `npm install -g @openai/codex`.

**Tabella di stato finale `/codex:setup`** (frame-423, trascritta esatta, osservata alle 14:04):

| Check | Result |
|---|---|
| Ready | ✅ |
| Node | v24.19.0 |
| npm | 11.17.4 |
| Codex CLI | codex-cli@0.148.0 — advanced runtime available |
| Auth | ✅ ChatGPT login active for engineering@martes-ai.com (verified) |
| Session runtime | direct startup — no shared runtime yet; the first review or task command starts one on demand |
| Review gate | disabled |

Nota finale dell'output, mai eseguita nel video: *"Optional next step: run `/codex:setup --enable-review-gate` to require a fresh review before setup..."* — opzione **mai attivata né spiegata**.

### 1.4 I cinque comandi — testo esatto a lavagna (3:18–4:14, frame-118–130) + README (frame-609/617)

| Comando | Cosa fa (parole di Belli a lavagna) | Flag osservati/letti a schermo |
|---|---|---|
| `/codex:review` | "Legge e basta. Legge quello che hai scritto e ti dice cosa non va. Non tocca niente e non lo puoi indirizzare su un punto preciso." Guarda **solo le modifiche non committate su Git** — "è come un Google Drive per il codice: guarda tutto ciò che non abbiamo ancora mandato sul nostro Drive". | — |
| `/codex:adversarial-review` | "Lo stesso, ma lo puoi puntare addosso a qualcosa. Gli dici cosa contestare e lui attacca quella scelta lì. Anche su un piano, non solo sul codice." | `--background` |
| `/codex:rescue` | "Non commenta, lavora. Gli passi il problema e ci mette le mani. Indaga, prova una correzione, sblocca il punto dove eri fermo." Delega un task al subagente `codex:codex-rescue`. | `--background`, `--wait`, `--resume`, `--fresh`, `--model <nome>`, `--effort minimal\|low\|medium\|high\|xhigh` |
| `/codex:transfer` | "Prende la conversazione che hai in corso con Claude e la porta dentro Codex. Non riparti da zero: continui da dove eri." Crea un thread Codex persistente e stampa `codex resume <session-id>`. | — |
| `/codex:status` / `/codex:result` | "Le review lunghe girano in background: status dice a che punto è, result ti consegna la risposta quando ha finito." | richiede l'ID del task (es. `task-e01joed-m2kcxz`) |
| `/codex:setup` | Verifica se Codex CLI è pronto e opzionalmente abilita il "review gate". | `--enable-review-gate` (mai attivato nel video) |

**Esempi `/codex:rescue` letti dal README** (frame-609/617, sintassi `--model` a confidenza moderata per il font piccolo, tranne `spark` letto con certezza):
```
/codex:rescue investigate why the tests started failing the smallest safe patch
/codex:rescue --resume apply the top fix from the last run
/codex:rescue --model gpt-5.1-mini --effort medium investigate the flaky integration test
/codex:rescue --model spark fix the issue quickly
/codex:rescue --background investigate the regression
```
Nota testuale dal README: se non si passano `--model`/`--effort`, Codex sceglie i suoi default; se si scrive `spark`, il plugin lo mappa a `gpt-5.1-codex-spark`; le richieste di rescue successive possono continuare l'ultimo task Codex nella stessa repo.

**Formato osservato dello status di un job in background** (15:47–16:00, frame-627): *"L'audit è ancora in corso (27 secondi trascorsi, fase running). Codex ha appena finito di mappare la struttura dell'app e lo stato git, sta iniziando a leggere i file."*

**Formato osservato del report di un job completato** (16:41–16:48, frame-635): *"Codex Job Status — task-<id> · completed · rescue · Codex Task. Summary: Audit completato in sola lettura. Non sono stati eseguiti fix contro l'endpoint live. Status: Done. Codex session id: <uuid>. Codex resume command: codex resume <session-id>."*

### 1.5 I due pattern d'uso — testo a lavagna (6:20–8:25, frame-170–222 e frame-694)

Sezione dichiarata da Belli come "la parte fondamentale... se non capite questa parte, tutto il resto del video non avrà senso".

**Pattern 1 — "Far controllare l'app prima di mandarla online"**
```
App pronta per andare online
   → /codex:review
   → TU REVISIONI LA REVIEW  (umano nel mezzo, scritto in rosso sulla lavagna)
   → Claude sistema quello che esce
   → online
```
Nota a lavagna: "Codex si legge tutto il branch contro main, mentre tu continui a lavorare" (review gira in background, non blocca).

**Pattern 2 — "Il piano prima di scrivere una riga"**
```
Piano scritto con Claude ("Fable 5")
   → /codex:adversarial-review sul piano
   → le critiche tornano a Claude
   → piano v2
   → (ciclo, freccia rossa indietro) finché Codex non ha più obiezioni
   → solo ora si scrive il codice
```

Belli chiarisce esplicitamente la distinzione critica fra `review` e `rescue`: se l'app è già finita e committata, `review` non troverebbe nulla da dire (guarda solo le modifiche non committate) — bisogna usare **`rescue`** per farsi analizzare un'app già completa. Dichiara: **"è l'errore che sbagliano tutti i video online che ho visto"**.

### 1.6 Il principio cardine — testo esatto a lavagna (frame-093–118)

**"CHI COSTRUISCE ≠ CHI GIUDICA"**

Il metodo dichiarato: il piano lo scrive Claude, Codex lo contesta ("adversarial review"), Claude produce piano v2, si ripete il ciclo finché Codex non ha più obiezioni, solo allora si scrive codice — **sempre con revisione umana nel mezzo**: *"non vogliamo essere pipecoder seriali... altrimenti quello che abbiamo costruito diventa un mostro incontrollabile."*

---

## PARTE 2 — DIVISIONE DEI RUOLI FRA I DUE STRUMENTI

### 2.1 Lavagna forze/debolezze (1:16–3:18, frame-039–118)

**Claude Code — punti di forza** (dichiarati verbalmente, 1:24–2:28):
- Fortissimo su copywriting, design, gusto estetico.
- Molto forte a pianificare / visione complessiva del progetto anche con idee poco chiare.
- Scrive tanto codice e in fretta.
- Ha "tutto l'ecosistema di skills, plugin, MCP, hook" — a parere di Belli superiore a quello di Codex.

**Claude Code — debolezze**:
- "Si entusiasma": dichiara "fatto" senza aver testato end-to-end.
- Salta gli edge case, dà sempre ragione all'utente.
- Si scrive i test da solo (rischio di test auto-compiacenti).
- **"È innamorato del codice"** (frase chiave ripetuta più volte nel video).

**Codex — punti di forza**:
- Esegue alla lettera ("se gli dici 1 2 3 4 5, fa 1 2 3 4 5", mentre Claude "ci mette sempre un po' della sua iniziativa").
- Trova più edge case, anche a livello di developer senior.
- Vede conseguenze di secondo e terzo ordine.
- Efficiente sulle modifiche mirate.
- **"Non è innamorato del codice"** — non essendone l'autore, non ha remore a criticarlo.

**Codex — debolezze**:
- Copy e design "secondo me non ci siamo".
- Va sfruttato con istruzioni molto precise.
- Un po' più lento (secondo l'esperienza personale di Belli).
- (agosto 2026) i limiti di utilizzo di Codex si esauriscono molto più lentamente di quelli di Claude — Codex "sta marciando tantissimo" nell'alzare i propri limiti.

### 2.2 Tabella di sintesi ruoli

| | Claude Code | Codex (via plugin) |
|---|---|---|
| **Ruolo nel metodo** | COSTRUISCE (scrive piano, scrive codice, applica i fix) | GIUDICA (contesta, audita, non scrive quasi mai) |
| **Punti di forza dichiarati** | copywriting, design, gusto estetico, pianificazione anche con idee poco chiare, ecosistema skills/plugin/MCP/hook, velocità di scrittura | esecuzione letterale delle istruzioni, edge case, conseguenze di 2°/3° ordine, non "innamorato" del codice che legge |
| **Debolezza dichiarata** | si entusiasma, dichiara "fatto" senza testare, salta edge case, si scrive i test da solo | copy/design deboli, richiede istruzioni precise, un po' più lento |
| **Costo consigliato** | piano Max $100/mese | piano ChatGPT Plus $20/mese (o gratis per test) |

**I tre comandi preferiti dichiarati esplicitamente da Belli** (26:48–27:39): `/codex:rescue` (per gli audit), `/codex:adversarial-review` (sui piani, "fondamentale"), `/codex:transfer` (quando Claude si blocca). `/codex:review` e `/codex:status`/`/codex:result` sono definiti "di contorno" (secondari).

---

## PARTE 3 — I TRE CASI REALI (finding di sicurezza trascritti per intero)

### 3.1 Caso 1 — Audit di "MaReply" (clone ManyChat), 10:40–19:00

Belli apre il progetto **MaReply**, applicazione interna costruita dal loro CTO che replica ManyChat (automazioni "Commenta X, ti mando Y in DM" su Instagram, incluse reel schedulati — funzione che ManyChat stesso non offre). Motivazione dichiarata: pagavano ManyChat $80/mese e le loro API erano troppo limitate, quindi l'hanno ricostruito in-house.

Claude Code, interrogato in precedenza, **aveva dato il via libera per la produzione**. Belli, prima di mandarlo online, lancia:
```
/codex:rescue --background
```
seguito dal prompt (trascritto integralmente, 15:12–15:34):
> "Fai un audit completo di questa app. È molto utente e custodisce gli account Instagram dei clienti. Concentrati su potenziali falle. Siccome voglio lanciarla in prod. Ad esempio, se un utente può vedere e toccare i dati di un altro, come sono protetti gli accessi di Instagram, cosa può far partire un DM sbagliato doppio, eccetera eccetera."

Motivazione per usare `rescue` invece di `review`: l'app era già committata, quindi `review` non avrebbe trovato nulla.

Flusso osservato:
- Claude Code risponde: "sta passando la richiesta a un sotto-agente di Codex... adesso è partito in background".
- `/codex:status <ID agente>` → "running".
- Dopo attesa → "completo".
- `/codex:result <ID agente>` → riepilogo esecutivo: **0 falle critiche, 2 falle alte, 2 falle medie, 2 falle basse**.

**Findings principali, trascritti per intero (16:59–18:52):**

1. **(Alta) Autenticazione email/password senza verifica dell'email.** Un attaccante può pre-registrare l'email della vittima con una password sotto il proprio controllo, impedendole di registrarsi normalmente; se ottiene un URL/token di invito, può dirottare l'account preregistrato. **Impatto**: accesso al workspace della vittima incluse conversazioni Instagram e automazioni. **Fix**: rendere obbligatoria la verifica email prima di considerare utilizzabile un account email/password, rifiutare l'accettazione di inviti se l'email di sessione non è verificata.
2. **(Alta) DM duplicati per assenza di claim atomico prima dell'invio.** L'endpoint che invia il messaggio Instagram diretto non controlla l'ID del destinatario, quindi un admin, una sessione rubata o un client difettoso può chiamarlo ripetutamente. **Impatto**: spam, doppio consumo del budget Meta, possibile abuso del dominio MaReply per phishing e danno reputazionale.

Belli commenta: **"Considerate che Claude Code mi aveva detto che questa applicazione era pronta per essere mandata in produzione... meno male che ho chiamato Codex."**

### 3.2 Caso 2 — Audit del form candidature, 19:00–24:00

Seconda finestra/progetto: un **form di candidatura interattivo** ("Lavora con noi" — replica di Typeform, ospitato su Cloudflare, dati salvati su **Airtable** come CRM). Belli mostra dal vivo il form compilandolo (nome, email, telefono, poi domande specifiche per ruolo — formatore vs sviluppatore). Stesso schema: `clod` (Claude Code) → `/codex:rescue --background` con prompt di audit su upload CV, permessi di lettura file, rischio di spam sull'endpoint, trattamento dati personali candidati.

Durante l'attesa, Belli mostra una funzionalità aggiuntiva del comando: **`--model`** e **`--effort`** (minimal/low/medium/high/xhigh), es. `/codex:rescue --model gpt-5.1-... --effort xhigh` per un'analisi più pesante (sintassi letta a schermo, frame-609/617/630).

**Risultato completo dell'audit** (`/codex:result`, trascritto per intero da frame-648/676/690, in ordine di severità):

**Alto:**
1. *Endpoint pubblico privo di protezioni anti-abuso* — `functions/api/candidature.js`, `onRequestPOST`: accetta POST senza autenticazione, rate limiting, CAPTCHA. Impatto: candidature false, consumo quota Cloudflare/Airtable, upload di file dannosi. Fix: validazione server-side, rate limiting Cloudflare, Turnstile/CAPTCHA.
2. *Upload completamente fidato lato server* — stesso file, righe ~148-149: non verifica dimensione, estensione, MIME reale né contenuto dei file caricati. Impatto: possibile caricamento di eseguibili/archivi. Fix: rinominare gli allegati con hash server-side, scansione malware prima del rendering.
3. *Nessun limite server-side sulla dimensione dei campi* — righe 87-137, 144-168: nessun limite massimo su lunghezza campi/array. Fix: rifiutare payload oltre soglia definita, limitare separatamente allegati.
4. *Codice di terze parti senza SRI né CSP* — `public/index.html` righe 19-29: React/ReactDOM/Babel caricati da unpkg.com senza `integrity`, nessuna Content Security Policy configurata. Fix: bundler locale o SRI, header `_headers` con CSP restrittiva su Cloudflare.

**Medio:**
5. Validazione server-side assente/non vincolata ad allowlist (solo client-side).
6. CORS completamente permissivo (`Access-Control-Allow-Origin: *`).
7. Errori Airtable esposti al chiamante (rischio di ricognizione dello schema interno).
8. Possibile formula/CSV injection sui futuri export da Airtable.
9. Accesso ai dati dipendente dai permessi della base Airtable, non verificato lato app.
10. Assenza di informativa privacy, consenso e indicazioni di retention (GDPR).
11. Messaggi di errore upstream (Airtable) loggati integralmente, senza redazione PII.
12. Allowlist degli allegati incoerente fra quanto mostrato all'utente e quanto realmente accettato dal backend.
13. ID dei record Airtable restituiti al client senza necessità.
14. Deploy non riproducibile: dipendenza `wrangler` non fissata a versione/lockfile.

**Info:**
15. Header di sicurezza HTTP non configurati nel repository.

Belli commenta esplicitamente che **non implementerà tutti i fix** — esempio: rifiuta di sistemare il "doppio DM" perché lo considera comportamento accettabile (un utente potrebbe voler ricevere di nuovo la risorsa cliccando due volte). Lo usa come dimostrazione pratica del principio "non vogliamo essere Vibe coder": ogni segnalazione va letta e filtrata dall'umano, non applicata alla cieca.

### 3.3 Caso 3 — Piano "sosia di Bitly" contestato da Codex, 24:00–27:44

Terzo esempio, questa volta sul **pattern 2** (piano prima del codice). Obiettivo dichiarato: costruire un accorciatore di link con tracciamento (clone di Bitly) per tracciare da quali video arrivano le prenotazioni di call. Belli mostra il **`PLAN.md`** già scritto con Claude ("Fable 5" nel suo linguaggio, "Opus 5 [1M context]" nell'interfaccia):

**Piano — "Piano: accorciatore di link con tracciamento"** (trascritto integralmente da frame-697–718):
> Obiettivo: replicare le funzioni principali di Bitly. Un utente incolla un URL lungo, riceve un link corto, e una dashboard vede quanti click ha ricevuto, da dove arrivano e con che dispositivo.
> Stack: Cloudflare Workers + D1 + React. Stesso stack degli altri progetti, così il deploy e i segreti funzionano come già sappiamo.

**§1 Modello dati** — due tabelle su D1:

Tabella `links`:
| campo | tipo | note |
|---|---|---|
| code | TEXT PRIMARY KEY | il codice corto, es. `a78x2k` |
| url | TEXT NOT NULL | l'URL di destinazione |
| created_at | INTEGER | timestamp unix |
| owner_id | TEXT | chi ha creato il link |
| clicks | INTEGER DEFAULT 0 | contatore, incrementato a ogni redirect |

Tabella `clicks`:
| campo | tipo | note |
|---|---|---|
| id | INTEGER PRIMARY KEY AUTOINCREMENT | |
| code | TEXT | riferimento a `links.code` |
| ts | INTEGER | timestamp unix |
| country | TEXT | da `request.cf.country` |
| city | TEXT | da `request.cf.city` |

**§5 Il redirect e il tracciamento** (procedura numerata a passi, trascritta integralmente):
1. Arriva `GET /:code`.
2. Si legge la riga di `links` con `SELECT url FROM links WHERE code = ?`.
3. Se non esiste, si risponde 404 con una pagina "link non trovato".
4. Se esiste, si scrive la riga di click su `clicks` (`code`, `ts`, referer e user-agent dagli header, IP da `request.cf-connecting-ip`).
5. Si incrementa il contatore: `UPDATE links SET clicks = clicks + 1 WHERE code = ?`.
6. Si risponde `301 Moved Permanently` con header `Location` verso l'URL di destinazione (il 301 è la risposta corretta per i motori di ricerca, secondo il piano).
7. Per non far aspettare il visitatore, i passi 4 e 5 girano dentro `ctx.waitUntil()`, così il redirect parte subito e la scrittura avviene dopo.

**§6 Parsing dello user agent** — per la colonna "dispositivo" della dashboard: se contiene "Mobile" → mobile, se contiene "Tablet"/"iPad" → tablet, altrimenti → desktop; browser cercato nell'ordine Edg, Chrome, Safari, Firefox.

Comando lanciato: `/codex:adversarial-review --background contesta questo piano, voglio creare un sosia di Bitly` con il file `PLAN.md` allegato via `@plan.md` o tasto destro → "copia il percorso" (entrambi i metodi accettati dal plugin, mostrati in alternativa).

**Verdetto Codex Adversarial Review**: **"needs attention"** — *"il piano lascia aperti isolamento tra utenti, accuratezza dei dati e gestione dei dati personali. plan.md:46-58 compromette il tracciamento, che è una funzione centrale del prodotto."*

**Findings, trascritti integralmente da frame-755, per severità:**

1. **(critical)** L'API stats/delete non impone l'ownership del link (`plan.md:46-58`) — l'autenticazione è descritta, ma il piano non richiede che `GET /stats` o `DELETE` verifichino `owner_id`, quindi chiunque può modificare/cancellare link altrui. **Fix**: verificare la sessione + `owner_id` su ogni chiamata.
2. **(high)** I redirect permanenti (301) restano in cache nel browser/CDN anche dopo la cancellazione di un link (`plan.md:72-74`). **Fix**: usare 302 con cache breve, `Cache-Control: no-store`, oppure Cloudflare purge cache alla cancellazione.
3. **(high)** Il contatore di eventi/click viene gonfiato da eventi duplicati (prefetch, preload, richieste multiple del browser).
4. **(medium)** Ogni click registra IP, user-agent, referer e geolocalizzazione senza finalità, retention o minimizzazione dichiarate (rischio privacy).
5. **(medium)** Esistono 2 API pubbliche di creazione/cancellazione con requisiti di autenticazione non chiariti nel piano — possibile abuso.

**Belli passa il verdetto a Claude ("Fable"):** *"controlla queste obiezioni che ha fatto Codex al nostro piano @PLAN.md per ricreare Bitly."* Risposta di Claude, punto per punto, trascritta integralmente (frame-772/776):

1. **Ownership su stats/delete: fondata, la più importante.** Vera lacuna — chiunque legge il codice/URL può cancellare link altrui.
2. **Il 301 rompe il tracciamento: fondata.** Verificato: il 301 viene cachato indefinitamente dal browser, dopo la prima visita il Worker non viene più interpellato per quel link. Nota aggiuntiva: **Bitly stesso usa 302 dal 2016** per questo motivo.
3. **Contatore eventi duplicati: fondata ma gonfiata, fix banale.** Il problema esiste ma "high" è eccessivo (perdita di qualche unità di conteggio, non integrità critica). Fix rapido: contare visitatori unici via hash (IP + user-agent + salt giornaliero, come fa Plausible) invece di richieste totali; aggiungere `FOREIGN KEY(code) REFERENCES links(code)` per eliminare i click orfani.
4. **Punto privacy: accettato.**
5. **Ordine di implementazione: respinto in gran parte.** Costruire l'API POST prima dell'auth è normale sviluppo incrementale; il rischio reale (record senza owner) è già coperto fixando il punto 1. Accetta solo di scambiare l'ordine dei passi 3 e 4.

**Verdetto sintetico di Claude**: *"4 obiezioni su 5 hanno un nucleo valido."* Belli approva: *"bene, applica tali correzioni Fable"* → il piano viene aggiornato (v2) prima di scrivere qualsiasi riga di codice applicativo. Poi si cambia modello con `/model` tornando a Opus per lo sviluppo vero e proprio.

### 3.4 Comandi aggiuntivi e sicurezza pre-produzione (27:44–28:47)

Prima di andare in produzione Belli dichiara di fare **sia** una review con Claude (cita a voce una "security review", comando nativo di Claude Code, digitato ma il relativo output non è ripreso a schermo nei frame catturati) **sia** un controllo con Codex.

**`/codex:transfer`** — comando descritto come uno dei preferiti: *"quando Claude proprio non riesce ad aggiustare qualcosa, si impappina, trasferisco la conversazione da quel punto lì a Codex per provarla a fare aggiustare a lui."* Dal README (frame-617): crea un thread Codex persistente a partire dalla sessione Claude Code corrente e stampa un comando `codex resume <session-id>`; da usare quando si è iniziata una conversazione di debug/implementazione in Claude Code e si vuole continuarla in Codex senza ripartire da zero.

---

## PARTE 4 — COSTI (dati visibili a schermo, integrali)

**Lavagna finale "QUANTO COSTA AVERLI TUTTI E DUE"** (frame-846, trascritta esatta):

```
TUTTO SU UNO SOLO                    LA COPPIA
$200 solo Claude                     $100 Claude Max — serve
   nessuno che lo controlla          + $20 Codex — controlla
$200 solo Codex                            ↓
   nessuno che serve bene              $120 AL MESE

venti dollari in più. Non il doppio.
perché qui Codex legge e critica, e scrive quasi mai.
l'auditor costa molto meno che generare.
e per provarlo basta anche il piano ChatGPT gratuito
```

A supporto, Belli mostra una ricerca a schermo (frame-879) che conferma: *"Yes, Codex is available on the ChatGPT Free plan, but it comes with strict usage limits."* — Cost: $0/mese, incluso con account ChatGPT, limiti di utilizzo più bassi di ogni altro tier, adatto a "quick testing" più che a sviluppo pesante. Fonte citata a schermo: pagina ufficiale ChatGPT "Codex Pricing" — Codex incluso in Free, Go, Plus, Pro, Business, Enterprise.

**Consiglio economico dato a voce (9:55–10:35):** usare il piano **Claude Max ($100)** + il piano **Codex/ChatGPT da $20** — non serve il piano Claude da $200 assieme a un secondo piano Codex da $200.

**Raccomandazione finale esplicita**: usare il piano **Free di ChatGPT** per testare la combo con qualsiasi piano Claude si abbia già (minimo richiesto per Claude Code: piano **Pro da $20**), verificare se si notano miglioramenti passando le review una o due volte, e solo se il miglioramento è netto passare a pagare Codex separatamente.

Non vengono mostrati costi per singola chiamata API, consumo di token per esecuzione di `/codex:rescue`/`/codex:adversarial-review`, né una stima di quante esecuzioni "consumano" la quota mensile.

Chiusura del video: pitch per Martes AI (coaching one-to-one/one-to-many, formazione aziendale in loco, analisi processi per soluzioni AI custom) con CTA a prenotare una call in descrizione.

---

## PARTE 5 — COSA IL VIDEO NON MOSTRA (dichiarato esplicitamente)

- **Nessun benchmark quantitativo**: tutte le prove sono aneddotiche/narrative su 3 progetti reali di Martes AI (MaReply, form candidature, plan.md Bitly-clone). Nessun dato aggregato su quante falle Codex trova "in media" o tasso di falsi positivi su un campione più ampio.
- **`/codex:review` non viene mai eseguito dal vivo**: è descritto e mostrato solo nel README/lavagna, non testato in terminale nei frame catturati (tutte e tre le demo usano `/codex:rescue` o `/codex:adversarial-review`).
- **`security-review` nativa di Claude Code** viene solo citata a voce ("spessissimo io mi vado a fare una security review") come step pre-produzione, ma l'esecuzione e il relativo output **non sono ripresi a schermo** nei frame disponibili.
- **`--enable-review-gate`** viene menzionato una sola volta come "optional next step" nell'output di `/codex:setup`, ma **non è mai attivato né spiegato** cosa cambi in pratica.
- **I 7 agenti e i 4 hook** installati dal plugin (contati nell'output di `/reload-plugins`) non vengono mai elencati o descritti singolarmente.
- **Nessun costo per singola esecuzione**: solo il costo mensile flat dei piani, non il consumo di quota per chiamata.
- **Nessuna gestione del disaccordo**: nel caso "Bitly" Claude accetta 4/5 obiezioni Codex; non viene mostrato cosa succede se Claude e Codex restano in disaccordo per più cicli, né un limite massimo al numero di iterazioni del ciclo review↔fix.
- **Solo ambiente Mac + VS Code**: nessuna dimostrazione su Windows, terminale nativo, o altri editor.
- **Nessun confronto diretto "prima vs dopo" a livello di codice**: si vedono solo i report testuali di Codex, non un diff applicato in tempo reale davanti alla camera per nessuno dei tre casi.

---

## PARTE 6 — CONFRONTO CON DIGITAL EMPIRE E IL VERDETTO

**Il problema che questo setup risolve esiste già in Digital Empire — ma DE lo ha già risolto, con un'architettura diversa.**

Il principio cardine del video — "chi costruisce è diverso da chi giudica" — **non è nuovo per DE**: è già codificato come regola operativa in `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` (ADR-006), il ciclo a 9 passi obbligatorio per ogni fase di costruzione:
`RECALL → SPEC → PRE-MORTEM → BUILD → GATE → REVIEW indipendente → TEST → COMMIT → RETRO`

Il passo "**REVIEW indipendente**" è concettualmente identico al pattern 1 del video ("far controllare l'app prima di mandarla online"). E DE ha già un intero strato di agenti dedicati esattamente al ruolo di "giudice" che nel video viene delegato a Codex: `sentinel-security`, `sentinel-drift`, `sentinel-quality`, `review-and-heal`, `security.agent`.

**Differenza reale, non cosmetica**: nel setup di Belli, il "giudice" è un **modello di famiglia diversa** (GPT/OpenAI) che legge codice scritto da un modello di famiglia diversa (Claude/Anthropic). In DE oggi, tutti i sentinel/reviewer sopra elencati girano **sullo stesso fornitore di modello** (Claude, solo con tier diversi — Haiku per i sentinel leggeri, Sonnet/Opus per i reviewer più profondi). Questo è un limite reale: se Claude ha un blind spot sistemico, nessuno dei sentinel attuali di DE lo intercetterebbe, perché condividono la stessa origine di addestramento. **Il video dimostra empiricamente questo scenario tre volte su tre**: Claude Code dà il via libera a due app "pronte per la produzione" (MaReply, form candidature), e un modello di famiglia diversa trova falle alte in entrambe; sul terzo caso (piano Bitly), lo stesso Claude conferma che 4 obiezioni su 5 di Codex erano fondate su un piano che lui stesso aveva scritto.

**VERDETTO (già emesso, non ribaltato):** il setup completo (plugin Codex, 5 comandi, doppio abbonamento OpenAI/ChatGPT per l'intera organizzazione) **non serve a DE**. Il ciclo ADR-006 e i sentinel esistenti coprono già il principio "chi costruisce non è chi giudica". L'unico gap reale, provato empiricamente 3 volte su 3 nel video, è che **tutti i giudici di DE oggi condividono la famiglia di modello di chi produce**. Questo non è un problema di "quale modello è migliore" — è che un giudice della stessa famiglia condivide i punti ciechi di chi ha scritto. Il guadagno è marginale sull'implementazione mostrata nel video (Codex Plugin specifico), ma reale sul principio di diversità di giudice, e solo per i deliverable a più alto rischio dati/credenziali.

---

## PARTE 7 — CONSIGLI INTEGRALI (da video-analysis.md, sezione CONSIGLI)

1. **Cosa migliorare in DE**: i sentinel di sicurezza/qualità attuali (`sentinel-security`, `sentinel-quality`, `sentinel-drift`, `review-and-heal`, `security.agent`) girano tutti su Claude. Andrebbe valutato — solo per i deliverable a più alto rischio (dati personali, credenziali, endpoint pubblici: es. Preventa Outreach con Areus/WhatsApp, Formazione Empire con dati studenti, PreventivoForge multi-tenant) — un secondo passaggio di audit con un modello di famiglia diversa prima del go-live, non come sostituto del ciclo ADR-006 ma come step opzionale aggiuntivo dentro la fase GATE, sul modello del pattern 1 del video (build → review indipendente cross-model → umano filtra i finding → fix → online).
2. **Quale skill nuova**: nessuna skill nuova dedicata a "Codex plugin" ha senso oggi — DE non ha un gap di skill di audit (esistono già `security-review`, `verification-quality`, `swarm-advanced`), ha semmai un gap di **diversità di modello** nei controlli esistenti. Non c'è un vuoto reale da colmare con una skill nuova; introdurre `/codex:*` richiederebbe comunque configurare un secondo abbonamento OpenAI/ChatGPT per l'intera org, cosa che va decisa a livello di ADR (costo ricorrente + nuova credenziale da gestire), non come skill leggera.
3. **Quale agente nuovo**: se Max decide di procedere, l'unico agente che avrebbe senso creare non è un clone dei sentinel esistenti, ma un **"cross-model-reviewer"** che invochi esplicitamente un secondo provider (via API OpenAI o Codex CLI) *solo* sui deliverable in fase GATE marcati come "rischio alto" (dati personali, pagamenti, credenziali di terzi) — con lo stesso schema di severità visto nel video (critical/high/medium/low/info) per restare comparabile ai report che i sentinel Claude già producono.
4. **Quale workflow nuovo**: nessuno strettamente nuovo. Il workflow "piano contestato da un secondo giudice prima di scrivere codice" (pattern 2 del video) è già coperto concettualmente dai passi SPEC → PRE-MORTEM di ADR-006; non serve un workflow nuovo, serve eventualmente inserire un cross-model-check dentro PRE-MORTEM per i progetti a rischio alto, non un intero nuovo workflow parallelo.
5. **Quale esistente potenziare**: il passo **REVIEW indipendente di ADR-006** (`PIANO-MAESTRO/10-METODO-CICLO-FASE.md`) è il pezzo esatto da potenziare — oggi è "indipendente" solo nel senso di agente diverso, non di modello diverso. Aggiungere una clausola opzionale ("per fasi a rischio alto, la REVIEW indipendente include un secondo modello di provider diverso") sarebbe l'unico intervento realmente giustificato da questo video, e andrebbe proposto come ADR, non implementato in silenzio (per REGOLA UNO di CLAUDE.md). **→ Questa proposta è ora scritta in `company/Memory/decisions/ADR-PROPOSTA-cross-model-review.md`, come PROPOSTA non attiva, da approvare da Max.**

---

*(Contenuto integrale ricostruito a partire da `video-analysis.md`, walkthrough completo con 197/197 frame unici certificati NO-FINTO PASS, e `atoms.json`, 70 knowledge atoms. Nessuna nuova visione dei frame in questa sessione — vedi `ingest-manifest.json` per i dettagli di coverage.)*
