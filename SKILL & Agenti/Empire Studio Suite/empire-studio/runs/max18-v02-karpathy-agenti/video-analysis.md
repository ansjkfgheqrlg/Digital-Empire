# Video Analysis — "Claude Code + Karpathy = Agenti AI da 10.000€"

- **ID YouTube:** LCNk5e5EiCA
- **Titolo:** Claude Code + Karpathy = Agenti AI da 10.000€
- **Canale/Autore:** Giovanni Beggiato (agenzia **Gentes AI** / gentes.ai — CEO Strategy & Systems, letto in `frame-012`)
- **URL:** https://www.youtube.com/watch?v=LCNk5e5EiCA
- **Durata:** 1503s = **25m03s**
- **Lingua:** italiano (sottotitoli auto IT + traduzione EN-US, entrambi scaricati)
- **Ingested:** 2026-09-04T11:23:28
- **Run:** `runs/max18-v02-karpathy-agenti`
- **Frame:** 501 densi @3s → 69 unici (soglia 6.0). **Frame guardati nativamente: 80/501 (16,0%) — 69/69 unici (100%) + 11 mirati** — vedi `coverage.md`
- **Trascrizione:** 612/612 righe uniche lette (100% del parlato sottotitolato, 0:02→24:59)

## Capitoli ufficiali (da `ingest.json` — 16, titoli in inglese anche se il parlato è italiano)

| Start | Titolo |
|---|---|
| 0:00 | 10,000 AI agents: what we build today |
| 0:43 | Karpathy's pattern: what an LLM wiki is |
| 1:59 | The three layers: raw sources, atomic notes, schema |
| 3:41 | The three AI operations: ingest, query, lint |
| 5:07 | The structure of the company brain we build |
| 6:51 | Generic output vs company brain output |
| 8:53 | Setup: Claude Code and the first prompt |
| 11:08 | The flow: call, brain, signable document |
| 12:43 | PandaDoc: template, dynamic variables and signature |
| 15:10 | Building the proposal generation skill |
| 17:27 | Live test: from call transcript to proposal |
| 19:22 | How to price: cost based or value based |
| 21:01 | Value based pricing: how to calculate the value |
| 21:59 | ROI: what the saved time is worth |
| 23:44 | Entry level pricing and when you need a retainer |
| 24:42 | Wrap up |

---

## LA TESI DEL VIDEO

Detto a voce in apertura (00:00:02–00:00:28): *"In questo momento alcune aziende pagano fino a €10.000 per agenti che possono essere costruiti in un solo pomeriggio. In questo video costruisco un MVP live dall'inizio alla fine con Cloud Code e vi lascerò tutti i prompt per replicarlo. Per costruirlo però non andremo a caso. Useremo la teoria di cui Andrej Karpathy parla quando costruisce con AI, costruendo attorno a questo agente una piccola Company Brain che potremo utilizzare per costruire automazioni successive."*

Il video ha quindi **due tesi sovrapposte**, non una:

1. **Tecnica** — un agente vale poco da solo; vale quando è costruito *dentro* una memoria aziendale persistente (il "Company Brain"), perché smette di richiedere il riassunto dell'azienda a ogni prompt. Il pattern della memoria non è inventato dall'autore: è la **LLM Wiki di Andrej Karpathy**.
2. **Commerciale** — lo stesso identico artefatto vale €3.000 o €15.000 a seconda dell'azienda che lo compra, quindi si prezza sul valore generato, mai sulle ore di sviluppo.

Il video le tiene insieme con una dimostrazione A/B live: lo stesso transcript di call dato a due Claude Code — uno in cartella vuota, uno dentro il Company Brain — e il confronto dei due output (`frame-138`, `frame-155`, `frame-162`).

---

## PARTE 1 — IL PATTERN DI KARPATHY (0:43 → 5:06)

### La fonte primaria, mostrata a schermo

`frame-007` / `frame-037` mostrano il **post originale di Andrej Karpathy su X** (URL nella barra: `x.com/karpathy/status/2039800565266...`), intitolato **"LLM Knowledge Bases"**, letto a schermo. Testo recuperato dai frame:

> *"Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:*
>
> ***Data ingest:*** *I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.*
>
> ***IDE:*** *I use Obsidian as the IDE "frontend" where I can view the raw data, the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).*
>
> ***Q&A:*** *Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining [...]"*

La slide dell'autore (`frame-017`, `frame-029`, `frame-041`) data il post **"Andrej Karpathy, aprile 2026"**.

### La slide "LLM WIKI — il pattern di Karpathy"

Excalidraw, letta integralmente in `frame-017`/`frame-041`/`frame-044` (dettaglio) e `frame-075`/`frame-097` (dettaglio operazioni):

Sottotitolo: *"invece di rispiegare tutto a ogni chat, una base di conoscenza in file markdown che l'AI mantiene da sola"*

**I TRE STRATI**
1. **FONTI GREZZE** — trascrizioni, documenti, email; *si leggono e non si toccano*
2. **IL WIKI** — note collegate che l'AI aggiorna, *una per cliente e una per concetto*
3. **LO SCHEMA** — le regole, com'è organizzato e come mantenerlo

**LE TRE OPERAZIONI**
- **INGEST** — materiale nuovo, l'AI legge e aggiorna le note
- **QUERY** ✅ — una domanda, l'AI risponde **e cita le note**
- **LINT** ❌ — controlla contraddizioni, dati vecchi, note orfane

Claim di chiusura della slide: **"L'UMANO CURA LE FONTI E FA LE DOMANDE, L'AI FA IL RESTO"**.

Al centro della slide, l'esempio: `cliente-rossi.md` (settore: logistica / budget: da definire / prossimo passo: proposta) → **WIKI** → **Obsidian**.

### Il grafo Obsidian reale dell'autore

`frame-008` e `frame-022` mostrano il vault Obsidian personale in "Galaxy view" (plugin 3D). Cartelle leggibili nella sidebar: `_showcase`, `areas`, `code`, `concepts`, `data`, `docs`, `engine`, `entities`, `labs`, `outputs`, `projects`, `scripts`, `self`, `sources`, `workspace`, più `CLAUDE`, `CONVENTIONS`, `README`. Contatore note: **"3515 notes"** (letto in `frame-022`; ⚠️ testo piccolo, confidenza media — in `frame-008` la stessa etichetta è meno nitida). Un nodo selezionato porta l'etichetta `metriche-mrr-churn`.

➕ **Inferenza mia:** la presenza di `CLAUDE`, `CONVENTIONS` e cartelle `engine`/`scripts` accanto a `concepts`/`sources` suggerisce che il vault dell'autore sia già a un livello più avanzato del Company Brain demo del video (che ha solo 4 cartelle). Non è dichiarato a voce, lo deduco dalla struttura letta a schermo.

### Il limite dichiarato dall'autore

A voce (00:04:33–00:04:55): *"questa infrastruttura è molto molto buona per una conoscenza di tipo personale [...] va molto bene se siete un solo founder. Nel caso in cui vi interessi qualcosa di un po' più strutturato, in community qua dentro abbiamo un corso di Company Brain nel quale andremo a spiegare che cos'è una Company Brain, come si struttura e come scalare queste company brain ad un contesto aziendale."*

⚠️ **Onestà**: la scalabilità aziendale del pattern **non è mostrata nel video** — è nominata e rinviata al prodotto a pagamento.

---

## PARTE 2 — LA STRUTTURA DEL COMPANY BRAIN (5:07 → 6:50)

### La slide "IL COMPANY BRAIN — la LLM Wiki, sul tuo business"

Letta integralmente in `frame-009`, `frame-107`, `frame-106`.

**LA STRUTTURA**
```
company-brain/
├── CLAUDE.md      → LO SCHEMA
├── fonti/         → STRATO 1, INTOCCABILE
├── clienti/       → IL WIKI
├── offerta.md     → I PREZZI
├── proposte/      → IL WIKI
├── index.md       → IL CATALOGO
└── log.md         → IL REGISTRO
```

**L'INGEST DAL VIVO**
`chiamata-rossi.txt` --INGEST--> `clienti/rossi.md` (settore: logistica · budget: 8k · prossimo passo: proposta)
✅ `index.md` aggiornato ✅ `log.md` aggiornato → grafo Obsidian

Claim di chiusura: **"DAI UNA CALL, TORNA UNA NOTA"**.

### Il PROMPT 1 integrale — recuperato parola per parola

Mostrato due volte a schermo: in anteprima nel Notion (`frame-005`, 0:12) e incollato dentro Claude Code (`frame-204`, 10:09, versione più nitida usata per la trascrizione). Testo recuperato:

```
<obiettivo>
Crea la struttura di un Company Brain seguendo il pattern "LLM Wiki" di
Andrej Karpathy: tre strati (fonti grezze immutabili, wiki in markdown
mantenuto dall'AI, schema di regole) e tre operazioni (ingest, query, lint).
Il cervello e' la memoria dell'azienda: clienti, offerta e proposte vivono
come note di testo collegate che Claude Code legge e aggiorna.
</obiettivo>

<struttura>
company-brain/
├── CLAUDE.md            -> lo SCHEMA: regole, naming, operazioni
├── fonti/               -> strato 1: materiale grezzo IMMUTABILE
│                           (trascrizioni di call, brief, email).
│                           Si legge, mai si modifica.
├── clienti/             -> strato 2 (wiki): una nota per cliente
│   └── _template.md
├── offerta/
│   └── offerta.md       -> strato 2 (wiki): l'UNICO posto dove vivono i prezzi
├── proposte/            -> strato 2 (wiki): una nota per proposta generata
│   └── _template.md
├── index.md             -> catalogo: una riga per nota, per categoria
├── log.md               -> registro append-only di ingest e proposte
├── .claude/
│   └── skills/          -> vuota per ora, la riempiamo dopo
└── .env                 -> chiavi API (crea il file vuoto, lo compilo io)
</struttura>

<CLAUDE.md deve contenere>
- Chi e' l'azienda e cosa vende (lascia i segnaposto, li compilo io).
- La mappa dei tre strati: fonti/ e' immutabile; il wiki (clienti/, offerta/,
  proposte/) lo mantieni tu; lo schema e' questo file.
- Le tre operazioni:
  INGEST: quando arriva un file nuovo in fonti/, leggilo, estrai le
  informazioni e crea o aggiorna la nota cliente; poi aggiorna index.md e
  appendi una riga in log.md. Se qualcosa contraddice cio' che gia' sai,
  segnalalo, non sovrascriverlo in silenzio.
  QUERY: quando ti faccio una domanda sul business, rispondi leggendo il
  wiki e cita le note da cui prendi la risposta.
  LINT: quando te lo chiedo, controlla note in contraddizione, dati vecchi
  e note orfane senza collegamenti.
- Regola 1: i prezzi vivono SOLO in offerta/offerta.md. Mai inventare un
  numero, mai copiarli altrove.
- Regola 2: ogni proposta generata scrive SEMPRE una nota nuova in proposte/
  con data, cliente, importo, stato e link, piu' l'aggiornamento di index.md
  e log.md. Nessuna proposta senza nota.
- Regola 3: mai leggere o mostrare il contenuto di .env, solo i nomi delle
  [chiavi]
</CLAUDE.md deve contenere>
```

⚠️ **Onestà sulla trascrizione**: l'ultima riga della Regola 3 esce dal bordo inferiore dello schermo in entrambi i frame; la parola finale (`[chiavi]`) è **ricostruita per senso, non letta**. Tutto il resto è letto carattere per carattere.

Le tre regole sono poi **confermate dall'output di Claude** (`frame-296`, 14:45), che le rilegge in prosa: *"CLAUDE.md → lo schema: i tre strati, le tre operazioni (INGEST, QUERY, LINT), le tre regole (prezzi solo in offerta, ogni proposta scrive una nota, mai mostrare .env)"*.

### Cosa Claude ha effettivamente creato (`frame-296`)

Output letto a schermo dopo il Prompt 1:

- `CLAUDE.md` — lo schema
- `fonti/` — vuota, strato grezzo immutabile
- `clienti/_template.md` — campi: nome, azienda, email, telefono, contesto, problema, note decisorie, budget, fonte
- `offerta/offerta.md` — unico posto dei prezzi. **Listino demo lead generation: Setup, Starter, Growth, Scale**
- `proposte/_template.md` — cliente, data, importo, stato, link, nota
- `index.md` — catalogo per categoria · `log.md` — registro append-only
- `.claude/skills/` vuota · `.env` vuoto

Claude chiude proponendo il passo successivo: *"appena butti un file in fonti/ (es. la trascrizione di una discovery call di lead generation) posso fare il primo INGEST e vedi nascere la prima nota cliente più le righe in index.md e log.md."*

Verifica eseguita da Claude stesso (visibile nello stesso frame): un comando **Bash** `find . -not -path "*/.git/*" | sort` per elencare l'albero e confermare che non ci fossero file extra.

---

## PARTE 3 — IL CONFRONTO A/B: BRAIN vs NO-BRAIN (6:51 → 8:52)

### Il setup

`frame-138` (6:51) mostra **due finestre Antigravity IDE affiancate**, ognuna con una sessione Claude Code aperta e `Bypass permissions` attivo:
- **sinistra** → progetto `Prova No Brain`, Explorer vuoto
- **destra** → progetto `Brain-Karpathy`, Explorer con `.claude`, `.env`, `clienti`, `fonti`, `offerta`, `proposte`, `CLAUDE.md`, `index.md`, `log.md`

Stesso transcript incollato in entrambe, stessa richiesta (00:07:13): *"Ehi, per favore, generami una proposta per questo cliente."*

### Output A — senza cervello

`frame-155` (7:42): un **artifact di claude.ai**, tema scuro, intestato *"Gentes.AI — PROPOSTA · 23 LUGLIO 2026 / PER ROSSI MARKETING · MARCO ROSSI"*, titolo *"Un flusso di appuntamenti prevedibile"*, sottotitolo *"Sistema di lead generation a freddo su Instantly. A seguito della call del 10 luglio."* Riga di sintesi a 4 colonne: **OBIETTIVO** Appuntamenti prevedibili · **SISTEMA** Cold email su Instantly · **INVESTIMENTO** Da 600 € · **DURATA** 3 mesi. Poi la sezione *"#1 Il punto di partenza"*.

`frame-162` (8:03, riquadro sinistro) mostra il messaggio di Claude che accompagna l'artifact. Testo recuperato:

> *"Fatto. Proposta pronta e pubblicata (privata, la vedi solo tu finché non condividi) [link claude.ai/public/artifacts/...]. Cosa contiene, nell'ordine: il punto di partenza (per fargli vedere che hai capito il problema), obiettivo, il sistema in 4 punti, cosa cambia per Davide, le due opzioni di prezzo affiancate, condizioni, i numeri (ROI), prossimi passi, contatti.*
> *Due scelte che ho fatto e che vale la pena tu confermi:*
> *1. Performance evidenziata come "la sua preferenza in call", ma ho messo la stima trimestrale a ~3.000 € (600 setup + 30 × 80). Cioè: onestamente costa più della standard (2.000 €) se i 30 meeting arrivano davvero. Ho lasciato la cosa trasparente perché è vera e perché se ne accorge da solo. Se preferisci non mostrare quel totale stimato, lo tolgo.*
> *2. [Il documento] è pronto per stampa/PDF (Cmd+P da browser tiene i colori e non spezza le carte), così lo alleghi alla mail.*
> *Vuoi che ti scriva anche la mail di accompagnamento breve da inviare a marco.rossi@rossimarketing.it? Se sì la butto giù nel tuo tono, 4-5 righe."*

Giudizio dell'autore a voce (00:07:37–00:08:00): *"non c'è il mio logo, non c'è niente, è una cosa abbastanza anonima, direi quasi AI slop [...] lasciando che il tutto sia generico, non ha nemmeno il nostro logo."*

⚠️ **Cautela di lettura mia**: guardando davvero `frame-155`, l'artifact **non è brutto**: è un documento scuro impaginato con gerarchia tipografica, e il nome "Gentes.AI" c'è in alto come testo. Quello che manca davvero è il **logo immagine**, il template brandizzato e il canale di firma — non "tutto", come suona la frase a voce. La differenza reale che il video dimostra è **funzionale** (firma+pagamento+nota di memoria), non solo estetica. Il claim "AI slop" è retorica dell'autore, non un fatto verificato a schermo.

### Output B — con il cervello

`frame-162` (riquadro destro), messaggio di Claude nella sessione `Brain-Karpathy`:

> *"Fatto. Proposta generata e verificata. Proposta — Rossi Marketing*
> *• Documento: [DEV] Proposta Gentes AI × Rossi Marketing (PDF brand Gentes), caricato su PandaDoc come **bozza***
> *• Dove trovarlo: dashboard PandaDoc*
> *• Note registrate: `proposte/rossi-marketing-2026-07-23.md` + `index.md` e `log.md` aggiornati*
> ***Check brand/prezzi (dal tuo PDF reale):***
> *• Copertina con logo, "Preparata per Marco Rossi – Rossi Marketing", data 23 luglio 2026 ✓*
> *• Pag. "La tua situazione oggi" — 3 paragrafi presi dalla call (agenzia a Vicenza, pipeline altalenante, Davide su LinkedIn a mano, 1.500-2.000/mese a cliente) ✓*
> *• Prezzi identici a `offerta/offerta.md`: Standard 2.000 € (1.000 setup + 500/mese × 2), Performance 600 € setup + 80 €/meeting (~30/trimestre), pagamento 50/50 ✓*
> *• Nessuna delle due opzioni pre-evidenziata ✓*
> *• Pagina Firma pulita, campi firma/data presenti ✓*
> *[...] Ho usato la chiave sandbox, quindi il documento nasce con prefisso [DEV] — normale, non blocca nulla."*

**Questa è la differenza operativa più importante del video, e va letta bene**: l'agente col cervello non si limita a produrre un documento più bello — produce un **check-list di autoverifica contro la fonte** (`offerta/offerta.md`) e **registra una nota di memoria** del fatto avvenuto. Il no-brain chiede all'umano di confermare due scelte inventate da lui; il brain dichiara cinque controlli superati contro un file che esiste.

---

## PARTE 4 — IL FLUSSO DISEGNATO PRIMA DEL CODICE (11:08 → 12:42)

Slide letta in `frame-224` — **"IL FLUSSO, PRIMA DEL CODICE — i tre strati di Karpathy calati sul business"**:

```
LA FONTE          →   IL CERVELLO         →   PANDADOC          →   LA MEMORIA
la trascrizione       trasforma la call       produce il            registra la
della call entra      in note e aggiunge      documento             proposta come
                      i prezzi                firmabile             nota
                           ↑
                      offerta.md
                    "i prezzi vivono qui"
```

Post-it sulla slide: *"Il flusso lo disegno io, poi Claude genera"* e *"Claude scrive più veloce, ma il progetto è mio"*.
Claim di chiusura: **"PRIMA DISEGNO IL FLUSSO, POI GENERO"**.

Nota a voce (00:11:54–00:12:03): la fonte in demo è copia-incolla dal Notion, ma *"una volta che questo workflow è fatto"* si può **collegare al proprio note-taker** — cita "Fathom" (pronunciato "FOM") e "Fireflies".

---

## PARTE 5 — PANDADOC: TEMPLATE, VARIABILI, CHIAVI API (12:43 → 15:09)

### Cos'è e perché

`frame-260`/`frame-267`/`frame-312` mostrano la **dashboard PandaDoc reale** dell'autore, workspace "Sales & Revenue", intestata *"Welcome back, Giovanni"*, con contatori **Your drafts 1 doc / Action required 0 / Waiting for others 0 / Finalized 0** e un solo documento in elenco: **`[DEV] Proposta Gentes — Rossi Marketing (demo firma, tag fix)`**, destinatario Marco Rossi, stato **DRAFT**, data **Jul 22, 2026**.

### Le chiavi API — pagina di configurazione letta integralmente

`frame-321` (16:00) mostra il pannello *Settings → API and Integrations*; `frame-322` (16:03) apre il **Dev Center → Configuration**, dove il testo delle due chiavi è leggibile per intero:

| Chiave | Cosa dà | Limiti dichiarati a schermo |
|---|---|---|
| **Sandbox key** | *"Test PandaDoc API for free"* | tutti i documenti includono un **prefisso developer**; **10 richieste/minuto** |
| **Production key** | *"Go live with PandaDoc API"* | **pieno controllo sui nomi dei documenti, nessun watermark sui PDF, fino a 300 chiamate/minuto**; richiede "Request a demo" |

Sotto: **Applications** (per aumentare la sicurezza dello scambio dati) e **Webhooks** (fino a **100 webhook**, sottoscrivibili a eventi dell'account). In alto a destra il badge **"Trial 14"** (14 giorni di prova, coerente con il *"14 giorni gratuiti"* detto a voce a 00:12:50).

Il Notion (`frame-179`) aggiunge il vincolo operativo che questo comporta:
> *"Chiave API: con la chiave sandbox i documenti escono marcati [DEV] e l'invio a email esterne fallisce con **403**. Per una bozza in dashboard basta la sandbox; per l'invio vero serve la chiave production (o un invio a un'email della tua organizzazione)."*

Questo spiega il prefisso `[DEV]` visto su tutti i documenti del video: **l'invio reale al cliente non è mai stato dimostrato**, solo la creazione della bozza.

### Il template e le variabili dinamiche

A voce (00:13:23–00:14:44) + `frame-364`/`frame-383`: il template è preparato **prima** del video, brandizzato (logo aziendale, "proposta di collaborazione", elenco servizi), con **firma digitale** già configurata (signer: Marco Rossi) e **variabili dinamiche / text fields** che l'AI popola. La demo di trascinamento di un campo dentro il documento è mostrata ma non ingrandita.

`frame-364` conferma a schermo: documento `[DEV] Proposta Gentes AI – Rossi Marketing`, **Step 3 of 5**, pulsante *Review and send*, **pagina 2 di 7**, intestazione *"PROPOSTA DI COLLABORAZIONE — Un sistema di acquisizione clienti per Rossi Marketing — Preparata per Marco Rossi — Rossi Marketing — 23 luglio 2026"*. Sidebar *Add fillable fields*: **Signature, Initials, Text field, Date**, destinatario `marco.rossi@rossimarketing.it`.

### Il rinvio al prodotto

`frame-265`/`frame-266` mostrano la lezione Skool citata a voce: community **Avanguardia Plus** (`skool.com/avanguardia-plus`), corso *"2. Claude Code Per Aziende"*, modulo **Automazioni Aziendali Claude → PandaDoc**, con abstract letto a schermo:
> *"PandaDoc: preventivi e contratti che si firmano e si pagano da soli. Il punto dolente di ogni preventivo è l'attesa: lo mandi via email, il cliente lo apre, lo perde, ti scrive 'ci penso'. Con PandaDoc il preventivo diventa un documento che il cliente firma con un click e paga online sul posto. Meno solleciti, e i sì arrivano prima."*

Player: **49 min** di lezione (indicatore **1.5×** → 29 min). A voce l'autore dice *"una trentina di minuti"* — coerente con la durata accelerata, non con quella reale.

---

## PARTE 6 — LA SKILL `/genera-proposta` (15:10 → 17:26)

### La slide di architettura — il pezzo di ingegneria più utile del video

`frame-328` (16:21) — **"L'INTEGRAZIONE PANDADOC — ogni pezzo testato da solo"**:

**1. TESTA IL PEZZO**
`inspect_template.py` → stampa `ruolo: Client`, `token: client.name`, `pricing: Prezzi`
> *"i nomi nel codice devono combaciare col template"* — ❌ *"indovinare + vibe coding che rompe tutto"*

**2. LA SKILL**
- `pandadoc.py` → *"il client: crea, legge, aspetta la bozza"*
- `create_proposal.py` → *"orchestra il tutto"*
- `SKILL.md` → *"il comando `/genera-proposta`"*

**IL DETTAGLIO ASINCRONO**
```
POST /documents  →  uploaded  --(aspetta)-->  draft ✅
```
> *"PandaDoc non crea il documento all'istante: risponde `uploaded`, tu aspetti `draft`"* — ❌ *"mandarlo prima = fallisce"*

Claim di chiusura: **"OGNI PEZZO TESTATO DA SOLO"**.

### La struttura reale creata a disco

`frame-345` (17:15) mostra l'Explorer di Antigravity dopo la generazione, che **corrisponde esattamente** alla slide:
```
.claude/skills/genera-proposta/
├── scripts/
│   ├── __pycache__/
│   ├── create_proposal.py
│   ├── inspect_template.py
│   └── pandadoc.py
└── SKILL.md
```

### Il prompt 2 e la clausola anti-allucinazione

`frame-323` (16:06) mostra la coda del Prompt 2 incollato in Claude Code, con una clausola che vale la pena isolare:

```
Se una parte di queste istruzioni e' ambigua o sembra contraddittoria,
fermati e spiegami il dubbio invece di indovinare. Non aggiungere librerie,
file o funzionalita' extra non richieste.
</in_caso_di_dubbio>
---
Per favore utilizza il PandaDoc in questo URL e poi questo template:
https://app.pandadoc.com/a/#/dashboard
```

Al prompt sono allegati **l'URL della dashboard e uno screenshot del template** (`image.png` visibile come allegato nel frame). L'autore spiega a voce (00:15:37–00:15:43): *"andremo anche ad incollargli il nostro screenshot"*.

Definizione di "skill" data a voce (00:16:57–00:17:10): *"la skill non è altro che un modo di dire a Claude 'automatizza questo workflow' perché gli step sono sempre quelli, e quindi abbiamo automatizzato un piccolo pezzo di processo."*

---

## PARTE 7 — IL TEST DAL VIVO (17:27 → 19:21)

### La fonte: il transcript di discovery call, letto integralmente a schermo

`frame-387` (19:18) mostra il file `2026-07-10-call-rossi-marketing.md` aperto nell'editor (convenzione di naming **data-ISO + slug**). Testo recuperato dal frame:

> **# Discovery call: Gentes AI × Rossi Marketing**
>
> **Giovanni:** *Quello che facciamo noi è un sistema di lead generation a freddo sopra Instantly. Prima estraiamo la lista dei tuoi clienti ideali con Apify [...]. Poi le arricchiamo con Claude, così ogni contatto ha i dati per scrivergli su misura. Scriviamo le sequenze di email a freddo, personalizzate, non il solito copia-incolla. E Instantly gestisce l'infrastruttura di invio da più caselle per non finire in spam, con il follow-up automatico. A te in calendario arrivano solo gli appuntamenti con chi ha risposto interessato.*
> **Marco:** *Quindi Davide smette di fare il lavoro a mano.*
> **Giovanni:** *Davide fa la call, non la caccia. Il sistema riempie il calendario, lui chiude.*
> **Marco:** *Mi piace. E come funziona il prezzo?*
> **Giovanni:** *Ci sono due modi di pagarlo, stesso identico sistema. Il primo è l'opzione standard: costo certo, definito dal primo giorno. **Setup mille euro una tantum**, che copre l'infrastruttura Instantly, l'estrazione lead con Apify, l'enrichment con Claude e la scrittura delle sequenze. Poi un **retainer cinquecento euro al mese per due mesi**, per la gestione della campagna e i report con i KPI. **In tutto duemila euro sui tre mesi.***
> **Marco:** *E il secondo?*
> **Giovanni:** *L'opzione performance, per chi vuole pagare a risultato. **Setup ridotto a seicento euro**, e poi **ottanta euro per ogni meeting** che ti prenotiamo in calendario. Su un trimestre la stima è di **circa 30 meeting** [...] si paga sul meeting prenotato, mai su quanto chiudi tu.*
> **Marco:** *Questa mi parla di più, onestamente. Preferisco pagare sui risultati che vedo, non voglio pagare per email mandate nel vuoto.*
> **Giovanni:** *Ci sta. Te le metto tutte e due nella proposta, così scegli con calma. **Il pagamento in entrambi i casi è metà alla firma e metà a fine campagna.** A che mail te la mando?*
> **Marco:** *marco.rossi@rossimarketing.it, cellulare 347 210 8838. Siamo a Vicenza.*

⚠️ **Onestà**: alcune righe del transcript sono parzialmente coperte dal pannello Explorer nella parte sinistra del frame; le porzioni riportate sopra sono quelle **leggibili con certezza**. La barra di stato conferma `Ln 33, Col 163 (141 selected)`, quindi il file è di ~33 righe: quanto sopra ne copre la sostanza, non la totalità carattere per carattere.

### Il documento prodotto — pagina prezzi

`frame-383` (19:06) e `frame-004` (0:09, stessa pagina in anteprima nell'hook) mostrano la pagina **"Le due opzioni"** del PDF PandaDoc:

> *"Stesso sistema, due modi di pagarlo. Scegli quello che preferisci: nessuna delle due è 'quella giusta', dipende da come vuoi distribuire l'investimento."*

| | **OPZIONE STANDARD** | **OPZIONE PERFORMANCE** |
|---|---|---|
| Cifra grande | **2.000 €** (totale a 3 mesi) | **600 €** (setup, poi a risultato) |
| Setup | 1.000 € — infrastruttura lead, estrazione Apify, enrichment Claude, copywriting sequenze | 600 € — infrastruttura, estrazione + enrichment, copywriting |
| Ricorrente | Retainer × 2 mesi — 500 €/mese (gestione campagne, report) | A risultato — 80 € / meeting |
| Nota | — | *"Un meeting = lead qualificato, che si presenta"* |
| Pagamento | **50% alla firma, 50% a fine campagna** — per entrambe le opzioni | idem |

**Verifica di coerenza fatta da me su tre fonti indipendenti dentro lo stesso video**: i prezzi del transcript-fonte (`frame-387`), quelli dichiarati da Claude nel check (`frame-162`) e quelli stampati sul PDF finale (`frame-383`) **coincidono esattamente** (1.000 + 500×2 = 2.000; 600 + 80/meeting; 50/50). Nessuna deriva tra fonte e output. ✅

Verifica fatta anche dall'autore a voce (00:18:32–00:19:22): torna nel file grezzo dentro `fonti/` per confrontare i numeri con quelli finiti sul PDF, e conferma la corrispondenza.

---

## PARTE 8 — COME PREZZARE (19:22 → 24:41)

Questa sezione è una **lavagna Excalidraw costruita a mano dal vivo**, sopra la slide preparata. Ricostruita da 11 frame guardati a intervalli di 30s (`frame-389` → `frame-490`).

### La slide preparata — "PREZZARE E OFFRIRE, sul valore non sul costo"

Letta integralmente in `frame-389` (19:24), stato completo:

**① PREZZA SUL VALORE** — Azienda A: **3.000 euro** / Azienda B: **15.000 euro** → *"stesso agente, valore diverso"* ❌ *non prezzare a ore*
**② L'OFFERTA IN CHIARO** — **3 GIORNI → 1 ORA** · *"la proposta pronta appena arriva il lead, la rivedi e premi invia"*
**③ LA STRUTTURA** — **SETUP una tantum: da 1.000 a 5.000 euro** · **RETAINER al mese: da 500 a 2.000 euro** · *"range indicativi"*
Claim di chiusura: **"PREZZA IL VALORE, NON LE ORE"**

### La lavagna costruita dal vivo — evoluzione verificata frame per frame

| Frame | ts | Cosa compare di nuovo sulla lavagna |
|---|---|---|
| `frame-400` | 19:57 | Le due parole `COSTO` (in alto) e `VALORE` (in basso), collegate da due frecce alla slide |
| `frame-420` | 21:00 | Accanto a `COSTO`: **`$ 200`** e **`$ 59`** |
| `frame-430` | 21:30 | Riquadrato `VALORE` → sotto **`VBP`** → freccia → **`TEMPO`** |
| `frame-440` | 22:00 | La formula: **`(TEMPO PERSONA PROPOSTA) × (# PROPOSTE MESE)`** |
| `frame-450` | 22:30 | Nuovo ramo: **`ROI` → `10h` ⇒ `$ ?`** |
| `frame-460` | 23:00 | Il risultato: **`⇒ 5.000 €/mese`** (cerchiato) |
| `frame-480` | 24:00 | Secondo numero: **`6.000 €/mese`** (cerchiato) accanto al primo |
| `frame-490` | 24:27 | A destra, elenco verticale: **`EN` / `IT` / `FR` / `DE`** con freccia |

⚠️ **Nota metodologica importante**: `scene_detector.py` a soglia 6.0 dichiara questo tratto (19:24→24:45) come **una sola schermata di 321 secondi**. È **falso**: la lavagna cambia continuamente. La scrittura a mano su area bianca non muove abbastanza la miniatura 64×64 su cui il detector calcola la differenza. Ho campionato questo tratto **a mano**, ogni 30 secondi, proprio perché il detector lo dava per statico. Vedi `coverage.md`.

### Il ragionamento, dal parlato (100% letto)

**Il costo (00:20:28–00:20:56)** — *"queste automazioni richiedono un costo abbastanza basso per farle: parliamo di un abbonamento molto probabilmente da 100 o 200 dollari per Claude, e poi un'automazione che possiamo fare con, se non mi sbaglio, 59 dollari per PandaDoc più un paio di altre cose. Quindi il costo è una strategia che vi farà perdere e vi farà sempre più schiacciare i margini."*
→ i numeri `$200` e `$59` sulla lavagna (`frame-420`) **sono questi**, verificati contro il parlato.

**L'ordine di grandezza del valore (00:19:57–00:20:16)** — *"un one day training di 8 ore su AI può arrivare a costare 10-15.000. Un'automazione del genere può arrivare a costare anche €10.000. Sarà forse la prima che venderete? Assolutamente no."*
→ ⚠️ Onestà: la cifra del titolo (€10.000) è **un tetto dichiarato con riserva esplicita dall'autore stesso**, non un prezzo realizzato e non mostrato in nessun documento.

**Metodo 1 — il tempo (00:21:13–00:21:46)** — *"il valore si può vedere come tempo che l'azienda sta salvando [...] è il tempo che una persona impiega per fare una proposta, quindi **tempo persona proposta moltiplicato per il numero di proposte al mese**. Questo è una proxy."*

**Metodo 2 — il ROI (00:21:59–00:23:16)** — *"non è un **o**, ma è un **e**"*. Il calcolo detto a voce, con l'autore che avverte *"facciamo numeri a casissimo"*:
```
10 ore/mese liberate
  → in quelle 10 ore la persona prende 2 clienti
  → cliente medio 2.500 €
  → 2 × 2.500 = 5.000 €/mese di upside
  (+ va moltiplicato il valore orario di chi paghi)
  ⇒ l'automazione si prezza intorno ai 6.000 €/mese
```
→ i due numeri cerchiati sulla lavagna (`frame-460` = 5.000, `frame-480` = 6.000) **sono esattamente questi**. ✅ Coerenza parlato/lavagna verificata.

**Le condizioni poste dall'autore (00:23:16–00:23:32)** — *"ovviamente dovete avere un business che ne ha bisogno, dovete avere un mercato che ve lo permette, dovete avere un avatar che è disposto a pagare [...] e poi per scalarle non è poi così semplice come farle one-shot."*

**Entry level e retainer (00:23:47–00:24:31)** — *"questi sono prezzi che potete considerare entry level, quindi potete cominciare ad offrire questa automazione **dopo ovviamente averne fatte un po'**, tra i 1.000 e i 5.000 €, e poi potete avere un retainer se l'azienda ha bisogno che questa automazione venga mantenuta."*
Esempio dato per il retainer: *"persone che hanno preventivi molto grossi, magari aziende che vendono macchinari pesanti [...] che vendono in un mercato inglese, italiano, francese, tedesco, e quindi queste automazioni cominciano ad avere lingue diverse, ma soprattutto a seconda del tipo di macchinario devono prendere forme diverse."*
→ le sigle `EN / IT / FR / DE` scritte a mano in `frame-490` **sono questo esempio**. ✅

**La chiusura (00:24:31–00:24:45)** — *"prezzate in base al valore e non in base alle ore che ci mettete a sviluppare, perché altrimenti i vostri margini andranno giù, e nessuna azienda di successo prezza mai al costo."*

---

## APPENDICE — Cosa mostra l'autore di sé (contesto commerciale, letto a schermo)

Non è formazione, è la cornice commerciale del video. Riportato perché **verificato a schermo**, non perché rilevante come metodo.

- **gentes.ai** (`frame-011`, `frame-012`, `frame-013`): headline *"AI Growth Partner for B2C Service Businesses"*; riga loghi *Value Group, Higgsfield, Anthropic, Notion, Amazon, P&G, Google*; claim *"Ten years driving change in Fortune 500 companies like Amazon and P&G [...] Gentes AI builds solutions that work in 30 days and get used from day one."*
- **Team** (`frame-012`): *Giovanni Beggiato, CEO / Strategy & Systems — "Led AI initiatives at Amazon delivering $4M+ in savings. Won CEO Award, top 2% of employees worldwide."*; *Jean-Marc Herrada, COO / Marketing & Operations — "worked with P&G in Manufacturing and Supply Chain, leading teams of 40 people and $100M projects."*
- **Servizi** (`frame-013`): tre fasi — **Audit** (call gratuita 30 min), **Engineering**, **Training & Launch**; due linee — **Lead Generation** (Lead Reactivation, Ad Campaigns, Content Systems) e **Voice AI** (AI Receptionist, Lead Qualification, Appointment Setting).
- **Community Skool "Avanguardia Plus"** (`frame-014`, `frame-100`, `frame-262`, `frame-263`): **91 membri, 6 online, 2 admin** al momento della registrazione. Classroom: *Comincia Qui · 1. Fondamenta AI/Business · 2. Claude Code Per Aziende · Creare Un'Offerta A Prova Di AI · 3. Hermes Corso Completo · 4. Implementa AI In Azienda · 5. Costruisci La Tua Company Brain · 6. Personal Brand Masterclass · 7. Agenti Vocali · Social Media Automation · Registrazioni Weekly Call · Cassaforte Skills*. Dentro il corso Claude: *Corso Completo Claude Code (**4h52:49**)* con indice a schermo — **1. Setup · 2. Subagents · 3. Team di agenti · 4. Gestione Contesto · 5. Skills · 6. MCP** — e il modulo *Automazioni Aziendali Claude* (Lead Generation, PandaDoc, Preventivi Automatici, GHL, Onboarding).
- **Ambiente di lavoro** (`frame-188`, `frame-198`): l'IDE usato è **Google Antigravity** (cercato su Google a schermo, descritto dal knowledge panel come *"an agentic development environment [...] designed to orchestrate autonomous artificial intelligence agents"*), con **Claude Code installato come estensione VS Code (Anthropic)** dal marketplace Open VSX. L'autore precisa a voce che *"non cambia assolutamente nulla"* rispetto alla desktop app di Claude Code.

---

## LIMITI E COSE NON DIMOSTRATE (dichiarazione esplicita)

1. **L'invio reale al cliente non è mai avvenuto.** Tutti i documenti hanno prefisso `[DEV]` (chiave sandbox) e restano in stato **DRAFT** nella dashboard. La firma e il pagamento sono mostrati come *campi configurati*, non come *transazione completata*.
2. **Il cliente è finto.** "Rossi Marketing / Marco Rossi" è dichiarato come demo dall'autore stesso nel prompt (*"sto facendo una demo per YouTube [...] il resto inventatelo pure"*, `frame-296`).
3. **Nessun euro incassato è mostrato.** La cifra €10.000 del titolo è un tetto teorico, con riserva dell'autore incorporata (*"sarà forse la prima che venderete? Assolutamente no"*).
4. **Il codice della skill non è mai stato ingrandito.** `pandadoc.py`, `create_proposal.py`, `inspect_template.py` compaiono solo come nomi di file nell'Explorer (`frame-345`) e come riquadri sulla slide (`frame-328`). Il loro contenuto **non è mai visibile a schermo**, quindi non è riportato qui.
5. **Il `CLAUDE.md` generato non è mai stato aperto a schermo.** Il suo contenuto è noto solo da (a) il prompt che lo commissiona e (b) il riassunto che Claude ne fa. Sono due fonti indipendenti e concordi, ma nessuna delle due è il file.
6. **La scalabilità aziendale del pattern è rinviata** al corso a pagamento, non mostrata.
7. **La trascrizione automatica si ferma a 24:59** su 25:03 di durata: gli ultimi ~4 secondi non hanno sottotitoli. La frase finale rimane troncata (*"...entrate in [community]"*), completata dalla traccia EN (*"join the community and you'll find"*). ➕ La parola mancante è ricostruita, non letta.
