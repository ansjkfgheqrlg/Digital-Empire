# Video Analysis — Keyword Research System (Claude Code / Claude.ai) di Nico | AI Ranking

- **ID video**: `E8Ax92etrMc`
- **Titolo**: "Steal My Claude Code Keyword Research System to Rank #1 on Google"
- **Canale**: Nico | AI Ranking
- **Durata**: 800s (13m20)
- **Data analisi**: 2026-09-02
- **Frame letti**: 400/400 (coverage 100%) — nessun frame saltato, nessun frame illeggibile
- **Fonte audio**: sottotitoli auto-generati `E8Ax92etrMc.en.vtt` (deduplicati), incrociati con lettura visiva di tutti i 400 frame

---

## NOTA METODOLOGICA IMPORTANTE (da leggere prima del resto)

Il report che il video usa per spiegare "come deve essere fatto il tuo output" **non è l'output della demo dal vivo**. Nico digita un prompt che chiede di analizzare "the plumbing market in Austin, Texas" (frame-152, @ 5:02), ma il report che scorre in dettaglio per i successivi ~7 minuti (frame-155 → frame-360, @ 5:08 → 11:58) è intestato **"Roofing, Dallas, Texas"** — un settore e una città diversi da quelli digitati nel prompt. La narrazione stessa è incoerente su questo punto: a 5:30 Nico dice *"I specifically chose Texas and plumbing, by the way, so that I did have some good data"* mentre lo schermo mostra chiaramente "Roofing" (idraulico vs. tetti/coperture sono settori diversi). ➕ Inferenza: il report "Roofing, Dallas, Texas" è un esempio precostituito/di repertorio usato per illustrare l'anatomia del documento, non l'output live del prompt digitato in video. L'unico dato riconducibile alla vera run "plumbing, Austin, Texas" è la card finale "The First Live Run" (frame-379, @ 12:36), che riporta numeri diversi (5.895 righe grezze vs. 1.713, 1.404 recensioni lette vs. 941) e nessun contenuto di dettaglio. Questo è marcato esplicitamente in "COSA NON SI VEDE" più sotto.

---

## WALKTHROUGH CRONOLOGICO

### 0:00–1:07 — Hook e promessa
- **frame-001.png @ 0:00**: talking head, apertura. Voce: *"A third of the questions that your customers are actually asking have zero search volume. Not low, but zero."*
- **frame-005.png @ 0:08**: illustrazione grafica generica "Keyword research tool" con barra di ricerca "Best productivity tips" e colonna "Search volume" (mockup stock, non un tool reale nominato) — usata per rappresentare "il tool che stai usando ora".
- Narrazione 0:10–0:41: la ricerca delle keyword mancanti (quelle a volume zero ma reali) è "a big part of the SEO game now" perché l'obiettivo non è più ranking su una keyword, ma **topical authority** su un intero argomento — questo è ciò che porta ad essere citati da GPT Search e Google AI Overviews.
- **frame-020.png @ 0:38**: screenshot reale di Reddit, thread `r/AskPortland`, titolo *"How much does a plumber typically cost?"* — b-roll illustrativo di "dove si trovano già scritte le domande" (Reddit, recensioni, autocomplete, People Also Ask, fan-out).
- Narrazione 0:44–1:06: elenco fonti — *"Reddit, yours [reviews], and your customers reviews, autocomplete, people also ask, fan out queries, and a few more things."* Problema dichiarato: raccogliere tutte queste domande e capire cosa farne "can be quite time consuming" → Nico ha costruito "a skill and a workflow with Claude" per estrarle automaticamente e dire esattamente cosa farne (FAQ in fondo alla pagina servizio? blog? video?).

### 1:07–2:10 — Framework di classificazione (voce fuori campo, nessun elemento a schermo nuovo)
- Spiegazione verbale (nessuno screenshot nuovo, talking head): i tool esistenti "aren't wrong, they're just incomplete". Ogni domanda va classificata su due assi:
  1. **Transazionale vs. Informazionale**: se la domanda implica che l'utente è vicino all'acquisto → contenuto va sulla service page; se è puramente informazionale → contenuto dedicato.
  2. **Formato**: FAQ, blog post/pagina dedicata, o video — a seconda dell'intento di ricerca reale (verificabile guardando cosa Google mostra già per quella query).
- **frame-036.png @ 1:10**: card titolo "THE POINT OF THIS VIDEO — The tools aren't wrong. They're incomplete. So you go somewhere else for the rest. It's already written down."

### 2:09–4:11 — Setup dei connettori: DataForSEO + Zernio (Reddit) → Claude
- Narrazione 2:09–2:38: *"by default, Claude doesn't have access to all of these things"*. Nico ricorda di avere già altri video sul collegamento **DataForSEO** a Claude (link promesso in descrizione, tutorial di circa 1 minuto).
- Narrazione 2:38–2:44: serve una seconda connessione, gratuita se se ne collega solo una: **"Zio"/"Zonio"/"Zerno"** nei sottotitoli auto-generati (trascrizione errata) — verificato visivamente: il prodotto si chiama **Zernio**.
- **frame-090.png @ 2:58**: homepage Zernio, menu prodotti a tendina — piattaforme disponibili: Twitter/X, TikTok, LinkedIn, YouTube, Discord, Bluesky, Snapchat, Instagram, WhatsApp, Facebook, Threads, Pinterest, Telegram, Google Business, Slack, Google Ads, TikTok Ads, LinkedIn Ads, Pinterest Ads, X Ads, OpenAI Ads, Meta Ads, **Reddit**; sezione Telephony (Phone Numbers, SMS & MMS, Voice & Calls); sezione APIs (Posting API, Comments API, Messaging API, Analytics API, Ads API, Comment to DM); sezione "For Agents" (AI Agents, **Claude Code**, Cursor, Codex, OpenClaw, Hermes).
- **frame-093.png @ 3:04**: landing "Ship Your 🔴 Reddit Integration In Minutes, Not Months" — "Stop wrestling with Reddit's API. Zernio handles OAuth, rate limits, subreddit rules, and API changes." CTA "Start Free Trial" / "View API Docs". Snippet codice sotto: `import Zernio from "@zernio/node"` (TypeScript).
- Narrazione 3:04–3:10: *"the pricing here... if you want to connect two accounts, it's completely free."*
- Narrazione 3:10–3:23: creare un account (link in descrizione), andare su "create a new connection", cercare Reddit, autenticare l'account Reddit, cliccare "Allow".
- Narrazione 3:23–4:09: collegare Zernio a Claude via **connettore MCP custom**:
  - Claude → **Settings → Customize → Connectors → Add new → Add custom connector**
  - Campo "Remote MCP server URL" → incollare `mcp.zernio.com/mcp`
  - Campo "Name" → libero (Nico usa "Zernio")
  - Nessuna advanced setting necessaria se si è loggati a Zernio nello stesso browser (facilita l'autenticazione)
  - Popup di conferma connessione → click "Connect"

### 4:09–4:57 — Skill Claude + prompt di lancio
- Narrazione 4:09–4:23: con Reddit + DataForSEO collegati, si è pronti; Nico rimanda a un ulteriore video-tutorial (~1 minuto) per il collegamento DataForSEO.
- **frame-108.png @ 3:34** *(mostrato prima del prompt, mentre apre le impostazioni Skills di Claude)*: pannello **Settings → Skills** di Claude, lista skill presenti nell'account di Nico (con pulsante "Add" → "Create with Claude / Write skill instructions / Upload a skill"):
  - `internal-link-architect`
  - `onpage-optimizer`
  - `keyword-fanout-map`
  - `ai-visibility-checker`
  - `seo-content-writer`
  - `site-brief-builder`
  - `seo-gsc-analyzer`
  - `revive-content`
  - `blog-to-video`
  - `cite-me`
  - `local-page-auditor`
  - `local-citations-auditor`
  - ➕ Inferenza: questa è la libreria personale di skill SEO di Nico (visibile solo come contesto/vetrina), non necessariamente lo stesso identico contenuto del file che regala. Non è chiaro se `keyword-fanout-map` sia il nome interno della skill regalata come `keyword-language.zip`, o una skill diversa correlata.
- Narrazione 4:23–4:41: *"I have a zipped file that I'm going to give you in the video description below. It's going to be available in our free community... it's just kind of a keyword language[-fanout-map], is essentially a skill plus a set of really detailed instructions."*
- **frame-138.png @ 4:34**: interfaccia chat Claude, home "What can we tackle together?", file allegato mostrato come card: **`keyword-language.zip`** (icona "ZIP"). Modello selezionato: **Opus 5, "High"** (effort). Presente anche un connettore/icona "vidiQ" accanto al selettore modello (non spiegato nel video; ➕ inferenza: residuo di un altro workflow nell'account di Nico, non parte del sistema descritto).
- **frame-152.png @ 5:02**: prompt digitato per intero (dettato vocalmente, popup "Messages / Stop / Space / Cancel" visibile in un frame intermedio), testo esatto:
  > **"I want you to unzip the file, understand all of the instructions, and then run those instructions on the plumbing market in Austin, Texas."**
- Narrazione 4:57–5:07: *"The more broad you go here, the better, which usually is something that I do not say, but in this case, we want to find as many of these questions that people are asking."*

### 5:08–11:58 — Anatomia del report (esempio "Roofing, Dallas, Texas")
- **frame-155.png @ 5:08**: prima comparsa del report, titolo **"Site Plan from Customer Language"**, sottotitolo **"Roofing, Dallas, Texas. Every question below came from something a real customer wrote."** Riga fonte: *"Reddit via site:reddit.com SERP fallback · Google reviews, People Also Ask, autocomplete, related searches and AI Overview structure (DataForSEO)."*
  - Contatori riassuntivi: **1.713** raw lines of customer language · **37** canonical questions · **26** FAQs for service pages · **14** blog posts · **4** videos · **941** reviews read.
  - Box evidenziato: **"15 of the 37 questions have zero Google search volume. Every one came from a real customer."** — con spiegazione: *"Questions that are objections become FAQs on the service page that has to overcome them. Questions with real demand become their own page, linked from that FAQ. Questions that need showing rather than telling become videos. Nothing is discarded."*
  - Sezione "WHERE THE QUESTIONS CAME FROM", 4 colonne:
    - **Reddit**: 502 threads across 111 subreddits (esempi: "Roof leaking - what to do in short term everywhere is" r/HomeImprovement; "Got a leak in my roof. Wondering what my next step would" ; "Roof leak, is this an emergency?" r/homeowners; "Leaking roof in the middle of winter, what should I do?" r/DIY; "Best way to seal roof leak from the inside"; "Roofers can't find source of leak and at a loss")
    - **People Also Ask**: 40 questions, "Google's own expansion" (esempi: "How often should you replace a roof?"; "Is $30,000 too much for a roof?"; "How long do shingles on a roof last?"; "Is a 20 year old roof too old?"; "Is $25,000 a lot for a new roof?"; "What is the 25% rule for roofing?")
    - **Autocomplete**: 150 suggestions (esempi: "why is my roof leaking water"; "...when it rains"; "...after heavy rain"; "...when it's not raining"; "...in minecraft" [outlier]; "...in winter")
    - **Fan-out**: 80 related searches + AI Overview structure (esempi: "How much does a roof cost"; "How long does a roof last asphalt shingles"; "How long does a shingle roof last on a house")
  - Nota metodologica a schermo: *"Reddit came through the site:reddit.com SERP fallback on this run, so thread comment counts are not available and the demand signal is weaker."* — ammissione esplicita di un limite tecnico nella run mostrata.
- **frame-343/344.png @ 11:24–11:26**: sezione **"FAN-OUT: What the engine breaks your question into"** — *"Take one mixed question and look at what Google's own AI Overview does with it. The sections it needs are the outline of the piece you should build, and the references tell you who is being cited for it today."* Esempio: query **"metal roof vs shingle?"** → l'AI Overview la scompone in 4 sezioni: (1) Cost & Installation, (2) Lifespan & Durability, (3) Energy Efficiency & Climate, (4) Maintenance & Weight. Box "Currently cited": roofmaxx.com, sheffieldmetals.com, nerdwallet.com, reddit.com — nota: *"4 sections, so this is article-sized rather than a one-paragraph FAQ."*
  - Sotto, legenda **"How each question was routed"** (4 tag/etichette, testo integrale):
    1. **"answered here" — FAQ, terminal**: *"A real objection with no standalone demand. Nobody ranks a page for it, but leaving it unanswered costs the job, and a direct question-and-answer pair is what AI engines quote."*
    2. **"links to full post" — FAQ that links out**: *"An objection that also has demand. A short answer on the service page to unblock the sale, then a link to the full piece."*
    3. **"post" — Its own page**: *"Upstream research. Earns a page when demand is real, or when the AI Overview splits the answer into two or more sections, which means it cannot be answered in a paragraph."*
    4. **"video" — Video**: *"The answer is something in your hands, and the live [demonstration]..."* (testo parzialmente tagliato dal riquadro webcam).
  - Sotto ancora: **"The plan, service page by service page"** — *"Left column is what gets added to the page itself. Right column is what gets built and linked from it. Every line carries the evidence that earned it."*
- **frame-292/295.png @ 9:42–9:48** (sezione "Roof replacement" / "Roof repair"):
  - "Roof replacement": *"What is the cheapest way to replace a roof?"* Google N/A, AI wins:142 · *"How long does a roof replacement take?"* Google 1.600, AI wins:78, tag "links to full post", PAA: "The objection that stops people booking" · in alto a destra: *"How long does a roof last?"* (post) Google 12.100, AI: 3.553, AI Overview: 2 sections, PAA x2, "AI Overview splits into Lifespan by Material and Factors That Change Roof Life"
  - "Roof repair" — FAQ Block on this page: 3: *"Can you fix a roof leak without replacing the whole roof?"* (answered here) Google N/A, AI wins:30 · *"How serious is a small roof leak?"* (answered here) Google 0/15, AI wins:4 · *"How much does roof repair cost?"* (links to full post) Google 720/255, PAA: "What is the cheapest way to fix a leaking roof?" — Linked from this page: 2: video *"Why is my roof leaking when it rains?"* Google 10/16, AI Overview: 2 sections · video *"How do I stop a roof leak until a roofer arrives?"* Google N/A, AI wins:0
  - "Storm & hail damage repair" — FAQ Block: 3: *"Will insurance replace my roof after a hailstorm?"*; *"Is this actually hail damage?"*; *"How much does hail damage roof repair cost?"* (66 storm threads, "the deductible question sits under all of them") — Linked: 1 video *"How can I tell if my roof has hail damage?"* Google 260, AI Overview: 3 sections, PAA x2 + 85 hail-and-storm threads
  - "Roof inspection" — FAQ Block: 4, prima voce *"How much should a roof inspection cost?"* Google 10/0
- **frame-321–340.png @ 10:40–11:18**: sezione **"What else goes on the service pages: From 941 reviews, unprompted"** — tabella comparativa "Share of 1-2★ reviews (44)" vs "Share of 5★ reviews (880)" su attributi di sentiment (non domande, ma temi ricorrenti nelle recensioni): *Price shock, went and got a second opinion* (4,5% / 0,5%); *Explained what they were doing* (11,4% / 14,1%); *Turned up when they said they would* (0,0% / 8,1%); *Cleaned up after themselves* (4,5% / 6,6%); *Stood behind the work* (15,9% / 3,5%); *Never called back* (0,0% / 0,0%); *Had to come back and redo it* (4,5% / 0,8%); *Handled the paperwork or claim* (34,1% / 25,2%). Nota a schermo: *"Attributes nobody was asked about. A wide gap between the two columns is a differentiator worth putting on the page. A narrow gap means it's table stakes and wins you nothing. With only 44 reviews at 1-2 stars, the left column is a small sample and should be read as direction, not precision."* Footer dati: *"502 Reddit threads · 941 on-topic reviews from up to 5 competitors · 40 People Also Ask questions · 150 autocomplete suggestions · 80 related searches. Volume figures are monthly averages. A Google figure of 0 means it wasn't queried, and genuinely zero. n/a means it could not be queried, because Google Ads rejects keywords over ten words."*
  - Sopra la tabella, esempio concreto usato dal narratore: query Reddit *"Should I sign with a door to door roofer after a storm?"* (answered here) — *"The scam and fraud thread cluster, plus 'Hail damage — what should I be wary of'"*
- **frame-345–360.png @ 11:30–11:58**: sequenza b-roll di Google Search reale, query digitata **"how to do a bicep curl"** — mostra un AI Overview con istruzioni testuali, poi una fila di risultati video YouTube ("Bicep Curls for Beginners" BowFlex, "How to bicep curl" Oliver Sjostrom) e la tab "Short videos" attiva con miniature TikTok/Instagram/YouTube — usato per dimostrare visivamente che l'intento di ricerca per certe query è dominato da video, non da testo.

### 11:47–12:11 — Aside promozionale: "AI Search Kickstarter" (community gratuita)
- **frame-347–351.png @ 11:32–11:40**: schermata community Skool-style **"AI Ranking (FREE)"**, sezione Classroom, corso **"AI Search Kickstarter"**, lezioni elencate: *Lesson 1 | SEO in 2026 · Lesson 2 | DataWise · Lesson 3 | Review Your Site · Lesson 4 | Fixing Your Site · Lesson 5 | AI Visibility · Lesson 6 | Write Content That AI Loves (selezionata) · Lesson 7 | What To Do Next.*
- Contenuto visibile della Lezione 6: *"Lesson 6 is the heart of the kit: writing content that AI engines actually cite."* **5 regole** mostrate: (1) use real questions as your H2s and H3s, not generic labels; (2) back every claim with a high-quality source linked from the contextual keyword; (3) add your own experience because that is the one thing AI cannot copy; (4) include one or two tables; (5) internally link to other sections of your site. **Errori comuni da evitare**: "rewriting for the sake of it, chasing an arbitrary word count, and stuffing your prompt with 25 personas." — **Walkthrough** citato: *"use DataWise's People Also Ask to pull dozens of real questions around your keyword, pick a clustered set for one post, then run the Cite-Me Prompt in ChatGPT (linked below). Go phase by phase: research, then structure with Canvas, then draft with...".* ➕ Nota: questa è una lezione di un corso separato ("AI Search Kickstarter"), citata solo di sfuggita/come cross-reference; non fa parte del sistema di keyword research illustrato nel resto del video, e usa un tool diverso ("DataWise") e ChatGPT invece di Claude.

### 12:11–13:00 — Statistiche reali della run + costo
- **frame-378.png @ 12:34**: card **"The First Live Run"**: **5.895** raw lines of customer language · **203.065** Reddit comments behind them · **1.404** reviews read · **$0.59** total cost. Sotto: *"Eight minutes, most of it waiting on the review API."*
- Narrazione 12:14–12:47 (audio, coerente coi numeri a schermo): *"running that report does have a cost, but a very little one. The only cost is really coming from data for SEO... There is a price for that... the only thing that it cost us was around 59 [cents]. I've done this flow a couple of times and it ranges from 50 cents all the way to like 80 cents, but I find that the average is around 59 cents... particularly when you're not going to be running this all the time... Once every 6 months will be great because you should get some new questions when they come up."*

### 13:00–13:20 — Chiusura
- **frame-388–392.png @ 12:54–13:02**: card finale **"Why it's shaped like this — You're not ranking for a keyword. You're ranking for the topic."** Due colonne: **"The old way"**: *"One page, one keyword, optimised hard. Repeat 12 times and hope."* vs. **"What actually works now"**: *"Answer every real question in the topic, properly, in their words, and link it together. Google and the AI engines both decide who covers a subject completely."* Sotto: *"That's why the output is a connected plan, not a list. The service page can't win the topic on its own."*
- **frame-393–400.png @ 13:04–13:18**: talking head di chiusura, CTA "Link in the description", ringraziamenti, fine video (13:20).

---

## IL SISTEMA INTEGRALE

### Comando/prompt esatto usato nella demo (frame-152.png @ 5:02, dettato vocalmente e trascritto in chat Claude)
```
I want you to unzip the file, understand all of the instructions, and then run those instructions on the plumbing market in Austin, Texas.
```
Nota narrativa che accompagna il prompt: *"The more broad you go here, the better... in this case, we want to find as many of these questions that people are asking."* → indicazione di metodo: più ampio è il target geografico/di nicchia specificato, più dati vengono raccolti.

### File fornito (regalato in community gratuita)
- **Nome file**: `keyword-language.zip` (frame-138/142/148/152.png)
- **Natura dichiarata**: *"it's just kind of a keyword [fanout] language, is essentially a skill plus a set of really detailed instructions for all this"* (transcript @ 4:23–4:37) → una **Claude Skill** (istruzioni impacchettate + probabile logica di orchestrazione) distribuita come zip da scaricare e allegare direttamente in una chat Claude.
- **Distribuzione**: link in descrizione video → community gratuita "AI Ranking (FREE)" (piattaforma community stile Skool).
- ➕ Inferenza: il contenuto interno dello zip (system prompt della skill, step-by-step, eventuali script) **non è mai mostrato a schermo** — solo il nome del file e il prompt di lancio.

### Setup dei connettori (step-by-step verbatim dal video)
1. **DataForSEO → Claude**: connessione richiamata come "già spiegata in altri video del canale" (non ripetuta in questo video, solo linkata in descrizione, tutorial dichiarato di ~1 minuto).
2. **Zernio → Reddit**: creare account su Zernio (link in descrizione) → "create a new connection" → cercare "Reddit" → autenticare/autorizzare l'account Reddit ("Allow").
3. **Zernio → Claude** (MCP custom connector):
   - Claude → Settings → Customize → **Connectors** → **Add new** → **Add custom connector**
   - Campo "Remote MCP server URL": `mcp.zernio.com/mcp`
   - Campo "Name": libero (es. "Zernio")
   - Nessuna advanced setting richiesta se loggati a Zernio nello stesso browser
   - Confermare nel popup "Connect"

### Skill/agenti Claude visibili nell'account di Nico (contesto, non necessariamente parte del regalo)
Elenco esatto da frame-108.png (@ 3:34), pannello Settings → Skills:
`internal-link-architect`, `onpage-optimizer`, `keyword-fanout-map`, `ai-visibility-checker`, `seo-content-writer`, `site-brief-builder`, `seo-gsc-analyzer`, `revive-content`, `blog-to-video`, `cite-me`, `local-page-auditor`, `local-citations-auditor`.

### Output — struttura del documento "Site Plan from Customer Language"
Sezioni ricostruite (ordine di scorrimento nel video):
1. **Header**: nome piano, niche + location, fonti dichiarate (Reddit SERP fallback, Google reviews, PAA, autocomplete, related searches, AI Overview structure via DataForSEO)
2. **Contatori sommario**: raw lines → canonical questions → FAQs for service pages → blog posts → videos → reviews read
3. **Box "X of Y questions have zero Google search volume"** con spiegazione della logica "nothing is discarded"
4. **"Where the questions came from"**: 4 colonne fonte (Reddit / People Also Ask / Autocomplete / Fan-out) con esempi reali e conteggi
5. **Esempi puntuali di routing per singola domanda**: query reale → tag di categoria (answered here / links to full post / post / video) → dati di supporto (Google volume, AI wins/AI Overview sections, fonte PAA/autocomplete/Reddit)
6. **"Fan-out: what the engine breaks your question into"**: esempio di scomposizione AI Overview di una query mista in sotto-sezioni, con box "currently cited" (domini citati oggi)
7. **Legenda "How each question was routed"**: 4 categorie fisse (FAQ terminal / FAQ that links out / Its own page / Video) con definizione
8. **"The plan, service page by service page"**: piano diviso per pagina servizio (es. Roof replacement, Roof repair, Storm & hail damage repair, Roof inspection), ciascuna con FAQ block + "linked from this page"
9. **"What else goes on the service pages: From N reviews, unprompted"**: tabella sentiment comparata 1-2★ vs 5★, con nota metodologica su gap ampio = differenziatore, gap stretto = table stakes
10. **Footer metodologico**: conteggi totali fonte + note su come interpretare "Google 0" vs "n/a" vs figure mensili medie

---

## I TOOL USATI

| Tool | Ruolo nel sistema | Gratis/A pagamento | Prezzo/dettagli visti a schermo |
|---|---|---|---|
| **Claude** (claude.ai, chat) | Motore che esegue la skill, orchestrando le chiamate ai connettori MCP e producendo il report finale | Freemium (serve un piano che supporti Skills + Connectors + modello Opus) | Modello usato: **Opus 5**, effort **"High"**. Nessun prezzo Claude mostrato esplicitamente. |
| **DataForSEO** | Fonte dati per Google reviews, People Also Ask, autocomplete, related/fan-out searches, AI Overview structure, volumi di ricerca | A pagamento (pay-per-call) | Non viene mostrata una pagina prezzi; costo aggregato dichiarato: **~$0,50–$0,80 a run, media $0,59** (per l'intero report). Collegato a Claude via connettore dedicato (tutorial esterno, non in questo video). |
| **Zernio** (`mcp.zernio.com`) | Connettore MCP che dà a Claude accesso a Reddit (OAuth, scraping) e potenzialmente ad altre piattaforme social/ads | Freemium | **Collegare fino a 2 account è gratis** (dichiarato a voce, @ 3:04). Nessun prezzo per tier superiori mostrato. Snippet SDK: `import Zernio from "@zernio/node"`. |
| **keyword-language.zip** (Claude Skill) | La "ricetta"/skill regalata da Nico che orchestra l'intero flusso (unzip → leggi istruzioni → interroga Reddit via Zernio e PAA/autocomplete/reviews/fan-out via DataForSEO → produce il Site Plan) | Gratis (regalata in community) | Nessun costo diretto per il file; il costo emerge solo dalle chiamate DataForSEO che la skill effettua durante l'esecuzione. |
| **AI Ranking (FREE)** community | Piattaforma (stile Skool) dove Nico distribuisce il file zip e ospita il corso gratuito "AI Search Kickstarter" | Gratis | — |
| **vidiQ** | Icona/connettore visibile accanto al selettore modello nella chat Claude di Nico | Non spiegato nel video | ➕ Inferenza: irrilevante per il sistema descritto, probabile residuo di altro workflow. |
| **DataWise** (citato in Lezione 6, non dimostrato) | Tool per estrarre "People Also Ask" in blocco, usato in un flusso *diverso* (content-writing con ChatGPT, non con questo sistema Claude) | Non chiarito | Solo citato a voce/testo, nessuna demo. |

---

## IL METODO SEO

**Tesi centrale** (card finale, frame-388): *"You're not ranking for a keyword. You're ranking for the topic."*
- **Vecchio approccio** ("The old way"): una pagina, una keyword, ottimizzata duramente, ripetuta per 12 keyword e sperare.
- **Approccio dichiarato efficace oggi** ("What actually works now"): rispondere a ogni domanda reale sul topic, nelle parole reali del cliente, collegando tutto insieme — perché sia Google sia i motori AI decidono chi copre un argomento in modo completo.

**Fonti di "domanda" mai coperte dai tool di keyword research classici**:
1. Reddit (thread reali, anche via fallback `site:reddit.com` quando l'API diretta non è disponibile)
2. Recensioni Google proprie **e di fino a 5 competitor** (per intercettare sentiment/obiezioni non dichiarate)
3. People Also Ask (espansione nativa di Google)
4. Autocomplete di Google
5. **Fan-out queries**: le sotto-domande che un motore AI (Google AI Overviews, ChatGPT-style) si pone internamente prima di rispondere a una domanda complessa — "nascoste" ma recuperabili via DataForSEO

**Criteri di classificazione di ogni domanda estratta**:
- **Asse 1 — Intento**: Transazionale (utente vicino all'acquisto → va sulla service page) vs. Informazionale (va su contenuto di supporto).
- **Asse 2 — Formato/routing** (4 categorie fisse, vedi sopra): FAQ terminale (senza domanda propria di ranking) / FAQ-che-linka-fuori (obiezione con domanda reale) / Post/pagina propria (domanda con volume reale o AI Overview a più sezioni) / Video (quando l'intento di ricerca è dominato da risultati video — verificabile a mano su Google, es. "how to do a bicep curl").

**Soglie e metriche numeriche usate nel metodo**:
- **Volume di ricerca Google = 0** non è motivo di scarto: nel dataset esempio, **15 domande su 37 (≈40%)** hanno volume zero ma sono mantenute perché derivano da linguaggio cliente reale.
- **N. di sezioni nell'AI Overview** (es. 4 sezioni per "metal roof vs shingle?") è usato come segnale: 2+ sezioni → serve una pagina propria, non un semplice paragrafo FAQ.
- **Gap tra share di menzione nelle recensioni 1-2★ vs 5★**: gap ampio → attributo differenziante da mettere in pagina; gap stretto → "table stakes", non vale la pena menzionarlo. Soglia di affidabilità dichiarata: con soli **44 recensioni** a 1-2 stelle, il dato va letto "come direzione, non precisione".
- **Convenzioni di lettura dei dati**: "Google 0" = interrogato e genuinamente zero; "n/a" = non interrogabile (Google Ads rifiuta keyword sopra le 10 parole).
- **Cadenza consigliata di esecuzione**: una volta ogni 6 mesi per business (non continuativo), per intercettare nuove domande emergenti.

**Come si passa dalla domanda al contenuto** (flusso dichiarato end-to-end):
1. Estrazione domande grezze da 4-5 fonti (Reddit, reviews, PAA, autocomplete, fan-out)
2. Deduplica/canonicalizzazione in "canonical questions"
3. Classificazione automatica intento + formato
4. Instradamento in un piano per-pagina-servizio, con evidenza a supporto per ogni riga
5. (Rimando a un lesson/prompt separato, non in questo sistema) — scrittura del contenuto vero e proprio seguendo regole per essere citati dagli AI Overview: domande reali come H2/H3, claim sempre con fonte linkata, esperienza personale/originale (l'unica cosa che l'AI non può copiare), 1-2 tabelle, link interni.

---

## OUTPUT REALE MOSTRATO

### A) Report d'esempio "Site Plan from Customer Language — Roofing, Dallas, Texas" (usato per spiegare l'anatomia dell'output, non generato in diretta nel video)
- 1.713 raw lines of customer language → 37 canonical questions → 26 FAQs → 14 blog posts → 4 videos → 941 reviews read
- 15/37 domande a volume zero
- 502 thread Reddit / 111 subreddit; 40 domande PAA; 150 suggerimenti autocomplete; 80 fan-out/related searches
- Esempi concreti di piano per pagina: Roof replacement, Roof repair, Storm & hail damage repair, Roof inspection — ciascuno con FAQ numerate, dati Google/AI wins, e link a video/post
- Tabella sentiment da 941 recensioni (7 attributi comparati 1-2★ vs 5★)

### B) "The First Live Run" — statistiche reali di una run effettiva (frame-378.png @ 12:34), senza contenuto di dettaglio mostrato
- 5.895 raw lines of customer language
- 203.065 Reddit comments behind them
- 1.404 reviews read
- **$0,59** costo totale
- **8 minuti** di esecuzione, "most of it waiting on the review API"

---

## COSA NON SI VEDE (dichiarato esplicitamente)

1. **Il salto Claude-al-lavoro → report pronto non è mostrato**: tra il prompt digitato (frame-152, @ 5:02) e la comparsa del report (frame-155, @ 5:08) non c'è alcuna schermata delle chiamate MCP a Zernio/DataForSEO, del ragionamento di Claude, o di log di esecuzione — è un taglio netto.
2. **Il report mostrato in dettaglio (Roofing, Dallas, Texas) non è l'output del prompt demo (plumbing, Austin, Texas)** — vedi nota metodologica in cima al documento. Non viene mai mostrato un report reale per "plumbing, Austin, Texas": solo le statistiche aggregate finali ("The First Live Run"), diverse nei numeri dal report d'esempio.
3. **Il contenuto interno di `keyword-language.zip` non è mai mostrato**: nessuna vista del system prompt della skill, degli step interni, o di eventuale codice/script che orchestra le chiamate a DataForSEO/Zernio.
4. **Il tutorial di collegamento Claude ↔ DataForSEO non è incluso in questo video** — solo rimandato ("I'll leave a video for you below").
5. **Nessuna pagina prezzi ufficiale di DataForSEO o di Zernio (tier a pagamento) è mostrata** — solo cifre dichiarate a voce.
6. **La sezione "AI Search Kickstarter — Lesson 6" è mostrata solo come aside/cross-reference di ~20 secondi**, non spiegata: il "Cite-Me Prompt" citato non è leggibile per intero a schermo, e usa un flusso diverso (ChatGPT + DataWise, non Claude + Zernio + DataForSEO).
7. **Nessun risultato di ranking/traffico reale (prima/dopo) viene mostrato** a supporto dell'efficacia SEO del metodo — il video si chiude sui numeri di esecuzione del report (righe, commenti, recensioni, costo), non su risultati di posizionamento.
8. **Icona "vidiQ" visibile ma mai spiegata** nell'interfaccia chat di Claude — non è chiaro se abbia un ruolo nel sistema o sia incidentale.

---

## COSA PORTA A DIGITAL EMPIRE

Digital Empire possiede già un impianto skill SEO maturo: `ai-seo`, `seo-audit`, `programmatic-seo`, `schema`, `site-seo` (oltre a `market-seo`, `market-competitors`, `content-strategy`, ecc.), più un ecosistema skill/agenti Claude Code consolidato (Empire Studio Suite, reparti multi-agente).

### Cosa è NUOVO rispetto alle skill esistenti di DE
1. **Il pattern "Reddit + recensioni (proprie e di fino a 5 competitor) + PAA + autocomplete + fan-out" come corpus unificato di "customer language"**, con deduplica in "canonical questions" e conteggio esplicito di quante hanno volume zero. Nessuna skill DE attuale (`ai-seo`, `seo-audit`, `programmatic-seo`) fa esplicitamente mining di Reddit + gap-analysis tra recensioni 1-2★ e 5★ come fonte di keyword/contenuto. Questo è un gap reale.
2. **Zernio come connettore MCP per Reddit** (OAuth gestito, free per 2 account) è un tool concreto, economico e subito operativo che DE non ha ancora in stack — utile non solo per SEO ma per l'intero reparto Outreach/Competitor Research (già esiste `project_competitor_research_dept` in Memory: studio sistematico competitor via video — Zernio potrebbe alimentare anche quello).
3. **Il routing a 4 categorie (FAQ terminale / FAQ-che-linka / Post proprio / Video) con soglia "N sezioni AI Overview → serve pagina propria"** è una euristica operativa chiara e riusabile, più fine-grained di quanto probabilmente coperto oggi da `site-seo`/`schema` (che si concentrano più su markup tecnico che su decisione "che formato di contenuto creare").
4. **La logica "fan-out query" come categoria di keyword research esplicita e interrogabile via DataForSEO** — DE ha già `ai-seo` (presumibilmente orientato a GEO/AI visibility) ma andrebbe verificato se copre già l'estrazione sistematica di fan-out queries o solo l'ottimizzazione del contenuto per essere citato.

### Cosa è RIDONDANTE
- La scrittura del contenuto "che l'AI ama" (H2/H3 come domande reali, claim con fonte, tabelle, link interni, evitare stuffing di persona) è **sostanzialmente coperta** da quanto DE probabilmente già codifica in `ai-seo` e `seo-content-writer`-equivalenti interni (cro-copy-architect, content-strategy). Non richiede una nuova skill, solo eventuale allineamento/arricchimento con queste 5 regole specifiche se non già presenti.
- Il concetto "non stai rankando per una keyword ma per un topic" è un principio già presente concettualmente in `programmatic-seo` e `site-seo` (topic clustering, pillar/cluster pages) — nessuna novità architetturale qui, solo conferma di validità dell'approccio.

### Cosa è DIRETTAMENTE RIUSABILE
- Lo **schema del documento output "Site Plan from Customer Language"** (contatori sommario → box "N domande a volume zero" → 4 fonti con esempi → routing per singola domanda → fan-out breakdown → piano per pagina servizio → tabella sentiment recensioni → footer metodologico) è un **template di deliverable pronto da clonare** per un audit/proposta commerciale DE verso clienti agenzia CRO — si sposa bene con `market-report` / `market-report-pdf` esistenti: potrebbe diventare una sezione aggiuntiva standard in quei report.
- Il **prompt minimale** ("unzip the file, understand all of the instructions, and then run those instructions on the [nicchia] market in [città]") è un pattern riusabile: skill Claude "broad-target, self-contained instructions" — utile come riferimento di design per come DE già impacchetta le proprie skill (vedi `.claude/skills/empire-studio/agents/*`), conferma che l'approccio "skill + zip regalato" di Nico è meno strutturato del sistema a 7 file (system-prompt/tools/playbook/evals/failure-modes/memory) che DE usa già — su questo DE è oggettivamente più maturo.

### Raccomandazione concreta
**Non serve una skill nuova da zero.** Conviene un **arricchimento mirato di `ai-seo` e/o `programmatic-seo`** con:
1. Un nuovo modulo/step "customer-language mining" che formalizzi le 5 fonti (Reddit via connettore tipo Zernio, recensioni proprie+competitor, PAA, autocomplete, fan-out via DataForSEO o equivalente) e produca l'output "N domande, N a volume zero, routing a 4 categorie" come sotto-agente dedicato (es. `keyword-fanout-map` — nome già "rubato" concettualmente da Nico, da reinterpretare per DE).
2. Valutare l'integrazione di **Zernio** (o di un MCP Reddit equivalente) nello stack Empire Studio, visto il costo quasi nullo (2 account gratis) e l'applicabilità trasversale a Outreach/Competitor Research oltre che a SEO.
3. Aggiungere alla libreria dei deliverable di `market-report`/`market-seo` il **template "Site Plan from Customer Language"** come sezione opzionale per gli audit clienti, differenziando l'offerta DE da audit SEO generici basati solo su keyword tool classici (Ahrefs/Semrush-style), leva commerciale concreta vista la promessa del video stesso ("un terzo delle domande dei tuoi clienti ha volume zero e i tool che usi non te le mostrano").
