# Claude Code + Codex: Il Setup di cui NESSUNO Parla

- **ID video**: `T7PPX5M6Puo`
- **Titolo**: "Claude Code + Codex: Il Setup di cui NESSUNO Parla"
- **Canale**: Riccardo Belli Contarini (fondatore/CEO di Martes AI — "partner AI a 360°", 65+ aziende clienti, 75+ soluzioni AI in produzione, agosto 2026)
- **Durata**: 1852s (30m52s)
- **Lingua**: italiano
- **Copertura frame**: **197/197 frame unici guardati, su 926 frame densi estratti** (soglia 3.0, riduzione 78.7%)
- **Trascrizione**: letta integralmente (`T7PPX5M6Puo.it-orig.vtt`, 850 segmenti puliti)

---

## 1. Walkthrough cronologico

### 0:00–1:16 — Intro e posizionamento
Belli apre dicendo che la domanda "Claude Code o Codex?" è sbagliata; la domanda giusta è "come ottengo il massimo da entrambi?" (frame-001–010, testo in overlay "Come posso ottenere il massimo da entrambi?"). Si presenta come ingegnere informatico, fondatore di **Martes AI**, agenzia che forma aziende su Claude Code/Claude Cowork e costruisce soluzioni AI custom: **65+ aziende clienti, 75+ soluzioni AI portate in produzione** (frame-030, frame-031 — card statistiche animate). Dichiara di usare Claude Code e Codex ogni giorno lui e il suo team, ed è "esattamente il metodo" del video.

Nota di naming: nei grafici a schermo (frame-008) compaiono le etichette **"Fable 5"** e **"GPT-5.6 Sol"** come nomi informali/colloquiali che Belli usa per riferirsi rispettivamente a un modello Claude (Opus) e a un modello Codex/GPT durante il video — non sono nomi ufficiali dei modelli. ➕ Inferenza: nel terminale reale (frame-734, frame-748) il modello Claude selezionato appare come **"Opus 5 [1M context]"**; "Fable 5" sembra essere il nickname personale di Belli per quel tier, non un nome di prodotto Anthropic.

### 1:16–3:18 — Lavagna: punti di forza/debolezza (frame-039–frame-118)
Lavagna con confronto diretto:

**Claude Code — punti di forza** (dichiarati verbalmente, 1:24–2:28):
- Fortissimo su copywriting, design, gusto estetico
- Molto forte a pianificare / visione complessiva del progetto anche con idee poco chiare
- Scrive tanto codice e in fretta
- Ha "tutto l'ecosistema di skills, plugin, MCP, hook" — a parere di Belli superiore a quello di Codex

**Claude Code — debolezze**:
- "Si entusiasma": dichiara "fatto" senza aver testato end-to-end
- Salta gli edge case, dà sempre ragione all'utente
- Si scrive i test da solo (rischio di test auto-compiacenti)
- "È innamorato del codice" (frase chiave ripetuta più volte)

**Codex — punti di forza**:
- Esegue alla lettera ("se gli dici 1 2 3 4 5, fa 1 2 3 4 5", mentre Claude "ci mette sempre un po' della sua iniziativa")
- Trova più edge case, anche a livello di developer senior
- Vede conseguenze di secondo e terzo ordine
- Efficiente sulle modifiche mirate
- "Non è innamorato del codice" — non essendone l'autore, non ha remore a criticarlo

**Codex — debolezze**:
- Copy e design "secondo me non ci siamo"
- Va sfruttato con istruzioni molto precise
- Un po' più lento (secondo l'esperienza personale di Belli)
- (agosto 2026) i limiti di utilizzo di Codex si esauriscono molto più lentamente di quelli di Claude — Codex "sta marciando tantissimo" nell'alzare i propri limiti

Frame-093–118 mostrano la lavagna con il concetto cardine scritto a mano: **"CHI COSTRUISCE ≠ CHI GIUDICA"**. Il metodo dichiarato: il piano lo scrive Claude, Codex lo contesta ("adversarial review"), Claude produce piano v2, si ripete il ciclo finché Codex non ha più obiezioni, solo allora si scrive codice — sempre con revisione umana nel mezzo ("non vogliamo essere pipecoder seriali... altrimenti quello che abbiamo costruito diventa un mostro incontrollabile").

### 3:18–4:14 — I cinque comandi (whiteboard, frame-118–130)
Belli introduce il tool su cui si basa tutto il video: la **repo GitHub ufficiale di OpenAI, "Codex Plugin"**, che porta Codex dentro Claude Code. Elenca a lavagna i 5 comandi fondamentali (testo esatto, frame-846 recap + frame-121–130 lavagna live):

1. **`/codex:review`** — "Legge e basta. Legge quello che hai scritto e ti dice cosa non va. Non tocca niente e non lo puoi indirizzare su un punto preciso."
2. **`/codex:adversarial-review`** — "Lo stesso, ma lo puoi puntare addosso a qualcosa. Gli dici cosa contestare e lui attacca quella scelta lì. Anche su un piano, non solo sul codice."
3. **`/codex:rescue`** — "Non commenta, lavora. Gli passi il problema e ci mette le mani. Indaga, prova una correzione, sblocca il punto dove eri fermo."
4. **`/codex:transfer`** — "Prende la conversazione che hai in corso con Claude e la porta dentro Codex. Non riparti da zero: continui da dove eri."
5. **`/codex:status` / `/codex:result`** — "Le review lunghe girano in background: status dice a che punto è, result ti consegna la risposta quando ha finito."

### 6:20–8:25 — I due pattern d'uso in pratica (whiteboard, frame-170–222 e frame-694)
Sezione dichiarata come "la parte fondamentale... se non capite questa parte, tutto il resto del video non avrà senso":

**Pattern 1 — "Far controllare l'app prima di mandarla online"**
```
App pronta per andare online
   → /codex:review
   → TU REVISIONI LA REVIEW  (umano nel mezzo, in rosso sulla lavagna)
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

Belli chiarisce esplicitamente la distinzione critica fra `/codex:review` e `/codex:rescue`: `review` guarda **solo le modifiche non committate su Git** ("è come un Google Drive per il codice: guarda tutto ciò che non abbiamo ancora mandato sul nostro Drive"). Se l'app è già finita e committata, `review` non troverebbe nulla da dire — bisogna usare **`rescue`** per farsi analizzare un'app già completa. Dichiara che questo è "l'errore che sbagliano tutti i video online che ho visto".

### 8:25–10:40 — Installazione passo-passo (VS Code, frame-239–330)
Setup mostrato dal vivo dentro **Visual Studio Code** con l'estensione **Claude Code** (prerequisiti dichiarati: VS Code + Claude Code già installati). Sequenza in terminale integrato di VS Code:

1. Ricerca Google "codex plugin" → primo risultato: repo GitHub ufficiale di OpenAI (frame-255–261)
2. Apre terminale VS Code, lancia `claude`
3. `/plugin marketplace add openai/codex-plugin-cc` → risposta: **"Successfully added marketplace: openai-codex"**
4. `/plugin install codex@openai-codex` → risposta: **"Installed codex. Plugin is now active."**
5. `/reload-plugins` → risposta osservata: **"Reloaded: 8 plugins · 18 skills · 7 agents · 4 hooks · 5 plugin MCP servers · 8 plugin LSP servers"**
6. `/codex:setup` → Claude Code esegue uno shell command (`node ".../scripts/codex-companion.mjs" setup --json"`) e rileva che Codex non è installato; propone un menu interattivo:
   ```
   1. Install Codex (Recommended)
      Runs `npm install -g @openai/codex`, then re-checks setup status.
   2. Skip for now
      Leaves Codex uninstalled; the setup output is reported as-is.
   ```
   Belli sceglie l'opzione 1. Il primo tentativo fallisce ("zsh: command not found: codex" — il pacchetto npm non aveva ancora linkato il binario). Claude Code stesso rileva il problema e attende: "Hold off on codex login for a moment — the npm install hasn't linked the binary yet." Dopo l'attesa (~8 minuti, install log), il comando riesce.
7. **Tabella di stato finale `/codex:setup`** (frame-423, trascritta esatta):

   | Check | Result |
   |---|---|
   | Ready | ✅ |
   | Node | v24.19.0 |
   | npm | 11.17.4 |
   | Codex CLI | codex-cli@0.148.0 — advanced runtime available |
   | Auth | ✅ ChatGPT login active for engineering@martes-ai.com (verified) |
   | Session runtime | direct startup — no shared runtime yet; the first review or task command starts one on demand |
   | Review gate | disabled |

   Nota finale: "Optional next step: run `/codex:setup --enable-review-gate` to require a fresh review before setup..." — opzione **mai attivata né dimostrata** nel video.

8. Login manuale alternativo indicato a voce: `codex login` (interattivo, richiede account ChatGPT).

**Requisiti dichiarati nel README ufficiale** (frame-121–130, letti a schermo):
- ChatGPT subscription (incl. Free) **o** OpenAI API key. "Usage will contribute to your Codex usage limits."
- Node.js 18.18 o superiore
- Alternativa manuale a `/codex:setup`: `npm install -g @openai/codex`

**Consiglio economico dato subito a voce** (9:55–10:35): usare il piano **Claude Max ($100)** + il piano **Codex/ChatGPT da $20** — non serve il piano Claude da $200 assieme a un secondo piano Codex da $200.

### 10:40–19:00 — Caso reale 1: audit di "MaReply" (clone ManyChat)
Belli apre il progetto **MaReply**, un'applicazione interna costruita dal loro CTO che replica ManyChat (automazioni "Commenta X, ti mando Y in DM" su Instagram, inclusi reel schedulati — funzione che ManyChat stesso non offre). Motivazione dichiarata: pagavano ManyChat $80/mese e le loro API erano troppo limitate, quindi l'hanno ricostruito in-house.

Claude Code, interrogato in precedenza, aveva dato il via libera per la produzione. Belli, prima di mandarlo online, lancia:
```
/codex:rescue --background
```
seguito dal prompt (trascritto, 15:12–15:34):
> "Fai un audit completo di questa app. È molto utente e custodisce gli account Instagram dei clienti. Concentrati su potenziali falle. Siccome voglio lanciarla in prod. Ad esempio, se un utente può vedere e toccare i dati di un altro, come sono protetti gli accessi di Instagram, cosa può far partire un DM sbagliato doppio, eccetera eccetera."

Motivazione per usare `rescue` invece di `review`: l'app era già committata, quindi `review` non avrebbe trovato nulla.

Flusso osservato:
- Claude Code risponde: "sta passando la richiesta a un sotto-agente di Codex... adesso è partito in background"
- `/codex:status <ID agente>` → "running"
- Dopo attesa → "completo"
- `/codex:result <ID agente>` → riepilogo esecutivo: **0 falle critiche, 2 falle alte, 2 falle medie, 2 falle basse**

Findings principali riportati a voce (16:59–18:52):
1. **(Alta)** Autenticazione email/password senza verifica dell'email: un attaccante può pre-registrare l'email della vittima con una password sotto il proprio controllo, impedendole di registrarsi normalmente; se ottiene un URL/token di invito, può dirottare l'account preregistrato. **Impatto**: accesso al workspace della vittima incluse conversazioni Instagram e automazioni. **Fix**: rendere obbligatoria la verifica email prima di considerare utilizzabile un account email/password, rifiutare l'accettazione di inviti se l'email di sessione non è verificata.
2. **(Alta)** DM duplicati per assenza di claim atomico prima dell'invio: l'endpoint che invia il messaggio Instagram diretto non controlla l'ID del destinatario, quindi un admin, una sessione rubata o un client difettoso può chiamarlo ripetutamente. **Impatto**: spam, doppio consumo del budget Meta, possibile abuso del dominio MaReply per phishing e danno reputazionale.

Belli commenta: "Considerate che Claude Code mi aveva detto che questa applicazione era pronta per essere mandata in produzione... meno male che ho chiamato Codex."

### 19:00–24:00 — Caso reale 2: audit del form candidature
Seconda finestra/progetto: un **form di candidatura interattivo** ("Lavora con noi" — replica di Typeform, ospitato su Cloudflare, dati salvati su **Airtable** come CRM). Belli mostra dal vivo il form compilandolo (nome, email, telefono, poi domande specifiche per ruolo — formatore vs sviluppatore). Stesso schema: `clod` (Claude Code) → `/codex:rescue --background` con prompt di audit su upload CV, permessi di lettura file, rischio di spam sull'endpoint, trattamento dati personali candidati.

Durante l'attesa, Belli mostra una funzionalità aggiuntiva del comando: **`--model`** e **`--effort`** (minimal/low/medium/high/xhigh), es. `/codex:rescue --model gpt-5.1-... --effort xhigh` per un'analisi più pesante (sintassi esatta letta a schermo nel README, frame-609/617 — vedi sezione comandi sotto).

**Risultato completo dell'audit** (`/codex:result`, trascritto per intero da frame-648/676/690, in ordine di severità):

**Alto:**
1. *Endpoint pubblico privo di protezioni anti-abuso* — `functions/api/candidature.js`, `onRequestPOST`: accetta POST senza autenticazione, rate limiting, CAPTCHA. Impatto: candidature false, consumo quota Cloudflare/Airtable, upload di file dannosi. Fix: validazione server-side, rate limiting Cloudflare, Turnstile/CAPTCHA.
2. *Upload completamente fidato lato server* — stesso file, righe ~148-149: non verifica dimensione, estensione, MIME reale né contenuto dei file caricati. Impatto: possibile caricamento di eseguibili/archivi. Fix: rinominare gli allegati con hash server-side, scansione malware prima del rendering.
3. *Nessun limite server-side sulla dimensione dei campi* — righe 87-137, 144-168: nessun limite massimo su lunghezza campi/array. Fix: rifiutare payload oltre soglia definita, limitare separatamente allegati.
4. *Codice di terze parti senza SRI né CSP* — `public/index.html` righe 19-29: React/ReactDOM/Babel caricati da unpkg.com senza `integrity`, nessuna Content Security Policy configurata. Fix: bundler locale o SRI, header `_headers` con CSP restrittiva su Cloudflare.

**Medio:**
5. Validazione server-side assente/non vincolata ad allowlist (solo client-side)
6. CORS completamente permissivo (`Access-Control-Allow-Origin: *`)
7. Errori Airtable esposti al chiamante (rischio di ricognizione dello schema interno)
8. Possibile formula/CSV injection sui futuri export da Airtable
9. Accesso ai dati dipendente dai permessi della base Airtable, non verificato lato app
10. Assenza di informativa privacy, consenso e indicazioni di retention (GDPR)
11. Messaggi di errore upstream (Airtable) loggati integralmente, senza redazione PII
12. Allowlist degli allegati incoerente fra quanto mostrato all'utente e quanto realmente accettato dal backend
13. ID dei record Airtable restituiti al client senza necessità
14. Deploy non riproducibile: dipendenza `wrangler` non fissata a versione/lockfile

**Info:**
15. Header di sicurezza HTTP non configurati nel repository

Belli commenta esplicitamente che **non implementerà tutti i fix** — esempio: rifiuta di sistemare il "doppio DM" perché lo considera comportamento accettabile (un utente potrebbe voler ricevere di nuovo la risorsa cliccando due volte). Lo usa come dimostrazione pratica del principio "non vogliamo essere Vibe coder": ogni segnalazione va letta e filtrata dall'umano, non applicata alla cieca.

### 24:00–27:44 — Caso reale 3: piano "sosia di Bitly" contestato da Codex
Terzo esempio, questa volta sul **pattern 2** (piano prima del codice). Obiettivo dichiarato: costruire un accorciatore di link con tracciamento (clone di Bitly) per tracciare da quali video arrivano le prenotazioni di call. Belli mostra il **`PLAN.md`** già scritto con Claude ("Fable 5" nel suo linguaggio, "Opus 5 [1M context]" nell'interfaccia):

**Piano — "Piano: accorciatore di link con tracciamento"** (trascritto da frame-697–718):
> Obiettivo: replicare le funzioni principali di Bitly. Un utente incolla un URL lungo, riceve un link corto, e una dashboard vede quanti click ha ricevuto, da dove arrivano e con che dispositivo.
> Stack: Cloudflare Workers + D1 + React. Stesso stack degli altri progetti, così il deploy e i segreti funzionano come già sappiamo.

**1. Modello dati** — due tabelle su D1:

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

**§5 Il redirect e il tracciamento** (procedura numerata a passi):
1. Arriva `GET /:code`
2. Si legge la riga di `links` con `SELECT url FROM links WHERE code = ?`
3. Se non esiste, si risponde 404 con una pagina "link non trovato"
4. Se esiste, si scrive la riga di click su `clicks` (`code`, `ts`, referer e user-agent dagli header, IP da `request.cf-connecting-ip`)
5. Si incrementa il contatore: `UPDATE links SET clicks = clicks + 1 WHERE code = ?`
6. Si risponde `301 Moved Permanently` con header `Location` verso l'URL di destinazione (il 301 è la risposta corretta per i motori di ricerca)
7. Per non far aspettare il visitatore, i passi 4 e 5 girano dentro `ctx.waitUntil()`, così il redirect parte subito e la scrittura avviene dopo.

**§6 Parsing dello user agent** — per la colonna "dispositivo" della dashboard: se contiene "Mobile" → mobile, se contiene "Tablet"/"iPad" → tablet, altrimenti → desktop; browser cercato nell'ordine Edg, Chrome, Safari, Firefox.

Comando lanciato: `/codex:adversarial-review --background contesta questo piano, voglio creare un sosia di Bitly` con il file `PLAN.md` allegato via `@plan.md` o tasto destro → "copia il percorso" (entrambi i metodi accettati dal plugin, mostrati in alternativa).

**Verdetto Codex Adversarial Review**: "**needs attention**" — "il piano lascia aperti isolamento tra utenti, accuratezza dei dati e gestione dei dati personali. plan.md:46-58 compromette il tracciamento, che è una funzione centrale del prodotto."

Findings (trascritti da frame-755, per severità):
1. **(critical)** L'API stats/delete non impone l'ownership del link (`plan.md:46-58`) — l'autenticazione è descritta, ma il piano non richiede che `GET /stats` o `DELETE` verifichino `owner_id`, quindi chiunque può modificare/cancellare link altrui. Fix: verificare la sessione + `owner_id` su ogni chiamata.
2. **(high)** I redirect permanenti (301) restano in cache nel browser/CDN anche dopo la cancellazione di un link (`plan.md:72-74`). Fix: usare 302 con cache breve, `Cache-Control: no-store`, oppure Cloudflare purge cache alla cancellazione.
3. **(high)** Il contatore di eventi/click viene gonfiato da eventi duplicati (prefetch, preload, richieste multiple del browser).
4. **(medium)** Ogni click registra IP, user-agent, referer e geolocalizzazione senza finalità, retention o minimizzazione dichiarate (rischio privacy).
5. **(medium)** Esistono 2 API pubbliche di creazione/cancellazione con requisiti di autenticazione non chiariti nel piano — possibile abuso.

Belli passa il verdetto a Claude ("Fable"): *"controlla queste obiezioni che ha fatto Codex al nostro piano @PLAN.md per ricreare Bitly."* Risposta di Claude, punto per punto (frame-772/776, trascritta):

1. **Ownership su stats/delete: fondata, la più importante.** Vera lacuna — chiunque legge il codice/URL può cancellare link altrui.
2. **Il 301 rompe il tracciamento: fondata.** Verificato: il 301 viene cachato indefinitamente dal browser, dopo la prima visita il Worker non viene più interpellato per quel link. Nota: **Bitly stesso usa 302 dal 2016** per questo motivo.
3. **Contatore eventi duplicati: fondata ma gonfiata, fix banale.** Il problema esiste ma "high" è eccessivo (perdita di qualche unità di conteggio, non integrità critica). Fix rapido: contare visitatori unici via hash (IP + user-agent + salt giornaliero, come fa Plausible) invece di richieste totali; aggiungere `FOREIGN KEY(code) REFERENCES links(code)` per eliminare i click orfani.
4. Punto privacy: accettato.
5. **Ordine di implementazione: respinto in gran parte.** Costruire l'API POST prima dell'auth è normale sviluppo incrementale; il rischio reale (record senza owner) è già coperto fixando il punto 1. Accetta solo di scambiare l'ordine dei passi 3 e 4.

**Verdetto sintetico di Claude**: "4 obiezioni su 5 hanno un nucleo valido." Belli approva: *"bene, applica tali correzioni Fable"* → il piano viene aggiornato (v2) prima di scrivere qualsiasi riga di codice applicativo.

### 27:44–28:47 — Comandi aggiuntivi, /codex:transfer, sicurezza pre-produzione
Prima di andare in produzione Belli dichiara di fare **sia** una review con Claude (cita a voce una "security review", comando nativo di Claude Code, digitato ma il relativo output non è ripreso a schermo nei frame catturati) **sia** un controllo con Codex.

**`/codex:transfer`** — comando descritto come uno dei preferiti: "quando Claude proprio non riesce ad aggiustare qualcosa, si impappina, trasferisco la conversazione da quel punto lì a Codex per provarla a fare aggiustare a lui." Dal README (frame-617): crea un thread Codex persistente a partire dalla sessione Claude Code corrente e stampa un comando `codex resume <session-id>`; da usare quando si è iniziata una conversazione di debug/implementazione in Claude Code e si vuole continuarla in Codex senza ripartire da zero.

**I tre comandi preferiti dichiarati esplicitamente da Belli** (26:48–27:39): `/codex:rescue` (per gli audit), `/codex:adversarial-review` (sui piani, "fondamentale"), `/codex:transfer` (quando Claude si blocca). `/codex:review` e `/codex:status`/`/codex:result` sono definiti "di contorno" (di supporto, secondari).

### 27:44–30:45 — Costi e chiusura
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

Raccomandazione finale esplicita: usare il piano **Free di ChatGPT** per testare la combo con qualsiasi piano Claude si abbia già (minimo richiesto per Claude Code: piano **Pro da $20**), verificare se si notano miglioramenti passando le review una o due volte, e solo se il miglioramento è netto passare a pagare Codex separatamente.

Chiusura: pitch per Martes AI (coaching one-to-one/one-to-many, formazione aziendale in loco, analisi processi per soluzioni AI custom) con CTA a prenotare una call in descrizione.

---

## 2. IL SETUP INTEGRALE (riepilogo comandi/config, tutti verificati a schermo)

**Fonte**: repository GitHub ufficiale OpenAI, "Codex Plugin" (`openai/codex-plugin-cc`), licenza Apache-2.0 (visibile in frame-609/617/630, header pagina README).

**Requisiti**:
- ChatGPT subscription (incl. Free) oppure OpenAI API key — l'utilizzo consuma la quota Codex
- Node.js ≥ 18.18

**Installazione (dentro Claude Code)**:
```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```
Installazione manuale alternativa di Codex CLI: `npm install -g @openai/codex`; login manuale: `codex login`.

**Output osservato dopo `/reload-plugins`**: `Reloaded: 8 plugins · 18 skills · 7 agents · 4 hooks · 5 plugin MCP servers · 8 plugin LSP servers` (i singoli 7 agenti/4 hook non sono elencati individualmente nel video).

**I 5 comandi**, con sintassi e opzioni osservate/lette a schermo:

| Comando | Cosa fa | Note/flag osservati |
|---|---|---|
| `/codex:review` | Legge le modifiche **non committate** su Git e segnala problemi. Read-only, non indirizzabile su un punto preciso. | — |
| `/codex:adversarial-review` | Come `review` ma puntabile: contesta un target specifico (codice o un piano/file passato con `@nomefile` o percorso). | `--background` |
| `/codex:rescue` | Delega un task a Codex tramite il subagente `codex:codex-rescue`: indaga un bug, prova un fix, continua un task Codex precedente, o fa un pass più economico con un modello più piccolo. Read-only per investigazione, ma può applicare fix. | `--background`, `--wait`, `--resume`, `--fresh`, `--model <nome>`, `--effort minimal\|low\|medium\|high\|xhigh` |
| `/codex:transfer` | Crea un thread Codex persistente dalla sessione Claude Code corrente; stampa `codex resume <session-id>`. | — |
| `/codex:status` / `/codex:result` | Mostra lo stato dei job Codex attivi/recenti per la repo / restituisce il report completo di un job terminato. | richiede l'ID del task (es. `task-e01joed-m2kcxz`) |
| `/codex:setup` | Verifica se Codex CLI è pronto e opzionalmente abilita il "review gate". | `--enable-review-gate` (mai attivato nel video) |

**Esempi `/codex:rescue` letti dal README** (frame-609/617):
```
/codex:rescue investigate why the tests started failing the smallest safe patch
/codex:rescue --resume apply the top fix from the last run
/codex:rescue --model gpt-5.1-mini --effort medium investigate the flaky integration test
/codex:rescue --model spark fix the issue quickly
/codex:rescue --background investigate the regression
```
Nota testuale dal README: se non si passano `--model`/`--effort`, Codex sceglie i suoi default; se si scrive `spark`, il plugin lo mappa a `gpt-5.1-codex-spark`; le richieste di rescue successive possono continuare l'ultimo task Codex nella stessa repo. ⚠️ Il nome esatto passato a `--model` in questo esempio (font piccolo nel frame) è riportato con confidenza moderata — la stringa `spark` → `gpt-5.1-codex-spark` è invece leggibile con certezza.

**Tabella di stato reale osservata (`/codex:setup`, frame-423)**:
```
Ready: ✅
Node: v24.19.0
npm: 11.17.4
Codex CLI: codex-cli@0.148.0 — advanced runtime available
Auth: ✅ ChatGPT login active for engineering@martes-ai.com (verified)
Session runtime: direct startup — no shared runtime yet
Review gate: disabled
```

---

## 3. Divisione dei ruoli fra i due strumenti

| | Claude Code | Codex (via plugin) |
|---|---|---|
| **Ruolo nel metodo** | COSTRUISCE (scrive piano, scrive codice, applica i fix) | GIUDICA (contesta, audita, non scrive quasi mai) |
| **Punti di forza dichiarati** | copywriting, design, gusto estetico, pianificazione anche con idee poco chiare, ecosistema skills/plugin/MCP/hook, velocità di scrittura | esecuzione letterale delle istruzioni, edge case, conseguenze di 2°/3° ordine, non è "innamorato" del codice che legge |
| **Debolezza dichiarata** | si entusiasma, dichiara "fatto" senza testare, salta edge case, si scrive i test da solo | copy/design deboli, richiede istruzioni precise, un po' più lento |
| **Costo consigliato** | piano Max $100/mese | piano ChatGPT Plus $20/mese (o gratis per test) |

Principio ripetuto più volte: **"chi costruisce è diverso da chi giudica"** — usare lo stesso modello per scrivere e per revisionare il proprio lavoro produce blind spot correlati; un secondo modello di famiglia diversa (GPT vs Claude), senza "ego" sul codice altrui, trova classi di problemi diverse (qui dimostrato 3 volte su 3 casi reali: falle di sicurezza non viste da Claude Code su due app in produzione, e obiezioni architetturali fondate su un piano nuovo).

---

## 4. Il flusso di lavoro reale, passo per passo

1. Si costruisce/pianifica con Claude Code.
2. **Prima di andare live** (app quasi pronta): `/codex:rescue --background` con un prompt di audit mirato (sicurezza, dati personali, endpoint pubblici) — non `/codex:review`, perché quest'ultimo guarda solo le modifiche non committate.
3. Si controlla l'avanzamento con `/codex:status <id>`; quando è "completed", si legge il report con `/codex:result <id>`.
4. **L'umano legge e filtra** i finding — non tutti vanno implementati (esempio esplicito: il "doppio DM" viene scartato come falso problema).
5. Si torna a Claude Code per applicare i fix scelti.
6. **Per un piano nuovo** (prima ancora di scrivere codice): si scrive `PLAN.md` con Claude, si passa a `/codex:adversarial-review --background` con il file allegato (`@file.md` o percorso incollato), si legge il verdetto Codex, lo si fa validare di nuovo da Claude ("controlla queste obiezioni..."), si applicano solo le correzioni che Claude conferma fondate, si ripete finché Codex non ha più obiezioni sostanziali.
7. Solo allora si passa alla scrittura del codice vero e proprio con Claude.
8. Se durante lo sviluppo Claude si blocca su un problema, si usa `/codex:transfer` per portare la conversazione dentro Codex e farla proseguire da lì.
9. Prima della produzione: review di sicurezza sia lato Claude sia lato Codex.

---

## 5. Costi (dati visibili a schermo)

- Piano "tutto Claude": $200/mese, "nessuno che lo controlla"
- Piano "tutto Codex": $200/mese, "nessuno che serve bene"
- **Combo consigliata**: Claude Max $100 + Codex/ChatGPT Plus $20 = **$120/mese totali** ("venti dollari in più, non il doppio")
- Motivazione: "Codex legge e critica, e scrive quasi mai — l'auditor costa molto meno che generare"
- Alternativa a costo zero per testare: piano **ChatGPT Free**, che include Codex con limiti di utilizzo stretti (fonte citata a schermo: pagina ufficiale "Codex Pricing" di ChatGPT — incluso in Free/Go/Plus/Pro/Business/Enterprise)
- Requisito minimo Claude per usare la combo: piano Claude Code **Pro da $20/mese**

Non vengono mostrati costi per singola chiamata API, consumo di token per esecuzione di `/codex:rescue`/`/codex:adversarial-review`, né una stima di quante esecuzioni "consumano" la quota mensile.

---

## 6. Cosa il video NON mostra (dichiarato esplicitamente)

- **Nessun benchmark quantitativo**: tutte le prove sono aneddotiche/narrative su 3 progetti reali di Martes AI (MaReply, form candidature, plan.md Bitly-clone). Nessun dato aggregato su quante falle Codex trova "in media" o tasso di falsi positivi su un campione più ampio.
- **`/codex:review` non viene mai eseguito dal vivo**: è descritto e mostrato solo nel README/lavagna, non testato in terminale nei frame catturati (tutte e tre le demo usano `/codex:rescue` o `/codex:adversarial-review`).
- **`/codex:security-review`** (o "security review" nativa di Claude Code) viene solo citata a voce ("spessissimo io mi vado a fare una security review") come step pre-produzione, ma l'esecuzione e il relativo output **non sono ripresi a schermo** nei frame disponibili.
- **`--enable-review-gate`** viene menzionato una sola volta come "optional next step" nell'output di `/codex:setup`, ma **non è mai attivato né spiegato** cosa cambi in pratica.
- **I 7 agenti e i 4 hook** installati dal plugin (contati nell'output di `/reload-plugins`) non vengono mai elencati o descritti singolarmente.
- **Nessun costo per singola esecuzione**: solo il costo mensile flat dei piani, non il consumo di quota per chiamata.
- **Nessuna gestione del disaccordo**: nel caso "Bitly" Claude accetta 4/5 obiezioni Codex; non viene mostrato cosa succede se Claude e Codex restano in disaccordo per più cicli, né un limite massimo al numero di iterazioni del ciclo review↔fix.
- **Solo ambiente Mac + VS Code**: nessuna dimostrazione su Windows, terminale nativo, o altri editor.
- **Nessun confronto diretto "prima vs dopo" a livello di codice**: si vedono solo i report testuali di Codex, non un diff applicato in tempo reale davanti alla camera per nessuno dei tre casi.

---

## CONFRONTO CON DIGITAL EMPIRE

**Il problema che questo setup risolve esiste già in Digital Empire — ma DE lo ha già risolto, con un'architettura diversa.**

Il principio cardine del video — "chi costruisce è diverso da chi giudica" — **non è nuovo per DE**: è già codificato come regola operativa in `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` (ADR-006), il ciclo a 9 passi obbligatorio per ogni fase di costruzione:
`RECALL → SPEC → PRE-MORTEM → BUILD → GATE → REVIEW indipendente → TEST → COMMIT → RETRO`

Il passo "**REVIEW indipendente**" è concettualmente identico al pattern 1 del video ("far controllare l'app prima di mandarla online"). E DE ha già un intero strato di agenti dedicati esattamente al ruolo di "giudice" che nel video viene delegato a Codex:
- `sentinel-security` — vigila su segreti/credenziali esposte/PII, attivo su ogni commit
- `sentinel-drift` — blocca modifiche architetturali non documentate senza ADR
- `sentinel-quality` — vigila su output senza proof/APSOC sotto soglia
- `review-and-heal` — protocollo di audit strutturale, testing e self-healing
- `security.agent` — verifica sicurezza, vulnerabilità, secret exposure

**Differenza reale, non cosmetica**: nel setup di Belli, il "giudice" è un **modello di famiglia diversa** (GPT/OpenAI) che legge codice scritto da un modello di famiglia diversa (Claude/Anthropic). In DE oggi, tutti i sentinel/reviewer sopra elencati girano **sullo stesso fornitore di modello** (Claude, solo con tier diversi — Haiku per i sentinel leggeri, Sonnet/Opus per i reviewer più profondi). Questo è un limite reale: se Claude ha un blind spot sistemico (un tipo di vulnerabilità che l'intera famiglia di modelli tende a non vedere, o un bias di "compiacenza" verso codice scritto dalla stessa famiglia), nessuno dei sentinel attuali di DE lo intercetterebbe, perché condividono la stessa origine di addestramento. Il video dimostra empiricamente questo scenario tre volte su tre: Claude Code dà il via libera a due app "pronte per la produzione", e un modello di famiglia diversa trova falle alte in entrambe.

**Verdetto**: il guadagno non è marginale sul principio (diversità di giudice), ma **è marginale sull'implementazione mostrata nel video** per il contesto specifico di DE. Aggiungere Codex come "secondo giudice" avrebbe senso soprattutto per gli step di security/audit più critici (pre-produzione di app client-facing, es. PreventivoForge, Formazione Empire con dati studenti, Outreach con credenziali WhatsApp/Areus), non come sostituto del ciclo ADR-006 già esistente. Il costo aggiuntivo dichiarato nel video ($20/mese oltre al piano Claude esistente, o gratis in fase di test) è basso abbastanza da giustificare un pilota mirato — ma introdurre un secondo strumento a pagamento con un secondo account/login (ChatGPT) su tutta la organizzazione aggiungerebbe complessità di gestione credenziali e un secondo ecosistema da mantenere, per un guadagno che oggi DE ottiene già in parte (anche se con minore diversità di modello) tramite i sentinel esistenti.

---

## CONSIGLI

1. **Cosa migliorare in DE**: i sentinel di sicurezza/qualità attuali (`sentinel-security`, `sentinel-quality`, `sentinel-drift`, `review-and-heal`, `security.agent`) girano tutti su Claude. Andrebbe valutato — solo per i deliverable a più alto rischio (dati personali, credenziali, endpoint pubblici: es. Preventa Outreach con Areus/WhatsApp, Formazione Empire con dati studenti, PreventivoForge multi-tenant) — un secondo passaggio di audit con un modello di famiglia diversa prima del go-live, non come sostituto del ciclo ADR-006 ma come step opzionale aggiuntivo dentro la fase GATE, sul modello del pattern 1 del video (build → review indipendente cross-model → umano filtra i finding → fix → online).

2. **Quale skill nuova**: nessuna skill nuova dedicata a "Codex plugin" ha senso oggi — DE non ha un gap di skill di audit (esistono già `security-review`, `verification-quality`, `swarm-advanced`), ha semmai un gap di **diversità di modello** nei controlli esistenti. Non c'è un vuoto reale da colmare con una skill nuova; introdurre `/codex:*` richiederebbe comunque configurare un secondo abbonamento OpenAI/ChatGPT per l'intera org, cosa che va decisa a livello di ADR (costo ricorrente + nuova credenziale da gestire), non come skill leggera.

3. **Quale agente nuovo**: se Max decide di procedere, l'unico agente che avrebbe senso creare non è un clone dei sentinel esistenti, ma un **"cross-model-reviewer"** che invochi esplicitamente un secondo provider (via API OpenAI o Codex CLI) *solo* sui deliverable in fase GATE marcati come "rischio alto" (dati personali, pagamenti, credenziali di terzi) — con lo stesso schema di severità visto nel video (critical/high/medium/low/info) per restare comparabile ai report che i sentinel Claude già producono.

4. **Quale workflow nuovo**: nessuno strettamente nuovo. Il workflow "piano contestato da un secondo giudice prima di scrivere codice" (pattern 2 del video) è già coperto concettualmente dai passi SPEC → PRE-MORTEM di ADR-006; non serve un workflow nuovo, serve eventualmente inserire un cross-model-check dentro PRE-MORTEM per i progetti a rischio alto, non un intero nuovo workflow parallelo.

5. **Quale esistente potenziare**: il passo **REVIEW indipendente di ADR-006** (`PIANO-MAESTRO/10-METODO-CICLO-FASE.md`) è il pezzo esatto da potenziare — oggi è "indipendente" solo nel senso di agente diverso, non di modello diverso. Aggiungere una clausola opzionale ("per fasi a rischio alto, la REVIEW indipendente include un secondo modello di provider diverso") sarebbe l'unico intervento realmente giustificato da questo video, e andrebbe proposto come ADR, non implementato in silenzio (per REGOLA UNO di CLAUDE.md).
