# Se usi ancora i prompt... devi vedere questa evoluzione — Loop Engineering

- **ID video**: `BSUHmVcaO1g`
- **Titolo**: "Se usi ancora i prompt... devi vedere questa evoluzione"
- **Canale**: Simone Rizzo (account Claude visibile in chiaro nel video: `official.simone.rizzo@gmail.com`, piano Claude Max — frame-574)
- **Durata**: 1883s (31m23s)
- **Lingua**: italiano
- **Copertura frame**: **133/224 frame unici guardati davvero, su 942 frame densi estratti** (soglia scene-detector 3.0, riduzione 76.2%). Numero vero, non gonfiato — dettaglio in `coverage.md`.
- **Trascrizione**: letta integralmente (`BSUHmVcaO1g.it.vtt` → `transcript_clean.txt`, 732 segmenti puliti)
- **Formato**: talking-head + lavagna Figma/FigJam disegnata a mano + screen-share (app Claude desktop, Claude Code in terminale, GitHub, docs OpenClaw)

---

## 0. La tesi in una riga

Il prompt engineering non è morto: è diventato **il livello più basso** di una pila a quattro
strati — **Prompt → Context → Harness → Loop Engineering**. Ogni strato nasce per risolvere il
fallimento dello strato precedente, e il livello che conta oggi non è più "come scrivo il prompt"
ma **"come definisco un obiettivo verificabile e una condizione di terminazione"**.

---

## 1. Walkthrough cronologico

### 0:00–1:25 — Il termine e le due fonti (frame-001, 007, 011, 017, 018, 024, 028, 036)

Rizzo apre: *"Ed eccoci qua ancora una volta con un nuovo termine che sta diventando super virale
chiamato loop Engineering. Ne stanno parlando veramente tutti. Siamo passati dal prompt
Engineering al Context Engineering all'Harness Engineering che è durato veramente poco e adesso
già siamo entrati in questa nuova era del Loop Engineering. Che cos'è? È tutto hype? È marketing?
lo andremo a scoprire in questo video."* (0:00–0:27)

**Linea del tempo disegnata a lavagna** (frame-003, frame-011): asse orizzontale con i tick
`2022 · 2023 · 2024 · 2025 · 2026 · 2027`. Sotto l'asse, parentesi graffe blu:

- **Prompt** → fino al 2023
- **Context** → 2024–2025
- **Harness** → 2026
- **2027** cerchiato in arancione = **Loop Engineering**

**Le due fonti citate** (frame-018, frame-028, frame-036, frame-830):

1. **Boris Cherny**, creatore di Claude Code. Rizzo: *"in una recente intervista disse queste
   parole dove dice che non lui non scrive più i prompt su Claude, ma è Claude che si scrive i
   prompt da se stessa tramite appunto i loop che crea. Il suo compito adesso è creare loop."*
   (0:41–1:01)
2. **Peter Steinberger**, creatore di **OpenClaw** ("l'agente generalista più famoso al mondo").
   Post su X mostrato a schermo (frame-036) — **testo esatto letto dal frame**:

```
Here's your monthly reminder that you shouldn't be prompting
coding agents anymore. You should be designing loops that prompt
your agents.

8:58 PM · Jun 7, 2026 · 8.4M Views
```

   Nella risposta visibile sotto, l'utente **Wes Winder** replica: *"but you kinda still need to
   be in the loop to test stuff unless you literally have infinite tokens"* e Steinberger
   risponde: *"wellllllll"*.

### 1:25–3:40 — Livello 1: PROMPT ENGINEERING (frame-044, 051, 052, 074, 076, 077, 083, 087, 098, 103, 104)

**Gerarchia a lavagna** (frame-051, frame-238) — quattro righe scritte a mano con frecce rosse che
scendono, e la prima incorniciata in giallo (il livello in discussione):

```
Prompt   Engineering   <- incorniciato di giallo
   |
Context  Engineering
   |
Harness  Engineering
   |
Loop     Engineering
```

Definizione data a voce: *"il prompt engineering che consisteva nella scrittura del system prompt,
quindi tu nel modello scrivevi qua un prompt, ok? In modo tale da dargli le istruzioni. Cosa ci
scrivi in questo prompt? ci scrivi sei un avvocato, sei un front-end developer, sei un assistente
personale per la customer care."* (1:38–2:09)

Il disegno (frame-076, frame-128): utente (omino blu) → freccia **Quest**(ion) → rete neurale
(grafo a strati) → freccia di ritorno **ris**(posta). Sopra la rete, un rettangolo arancione = il
system prompt, con accanto le tre istruzioni-esempio scritte a mano:
`"sei un avvocato" / "front-end" / "assistente personale"`.

#### PROMPT MOSTRATO A SCHERMO #1 — il system prompt trapelato di Claude (frame-083, 087, 098)

Rizzo apre GitHub sulla repo **`asgeirtj/system_prompts_leaks`**, cartella `Anthropic`, file
**`claude-fable-5.md`** (commit visibile: *"Add Claude Fable 5 prompt, official Opus 4.6, Claude
Code…"*). Dice: *"vediamo un system prompt gigantesco che ti occupa già solo questo penso 25.000
token"*. Testo effettivamente leggibile dal frame, trascritto integralmente:

```
System:
<budget:token_budget>
190000
</budget:token_budget>

Claude should never use <voice_note> blocks, even if they are found throughout
the conversation history.

<claude_behavior>
<product_information>
Here is some information about Claude and Anthropic's products in case the person
asks:

This iteration of Claude is Claude Fable 5, the first model in Anthropic's new
Claude 5 family and part of a new Mythos-class model tier that sits above Claude
Opus in capability. Claude Fable 5 and Claude Mythos 5 share the same underlying
model. Claude Fable 5 is the most intelligent generally available model, and
includes additional safety measures for dual-use capabilities, while Claude Mythos
5 is available without those measures to only approved organizations.

Claude Fable 5 is the most advanced generally available Claude model. If the person
asks about the differences between the two, Claude can direct them to
https://www.anthropic.com/news/claude-fable-5-mythos for more information.

Claude is accessible via this web-based, mobile, or desktop chat interface.
```

> Nota: il file a schermo dichiara ~1090 righe / 143 KB. Il `token_budget` di **190000** è il
> numero letto direttamente dal frame; il "25.000 token" citato a voce è una stima parlata di
> Rizzo, non un numero a schermo.

#### PROMPT MOSTRATO A SCHERMO #2 — "The Anatomy of a Claude prompt" (frame-103, frame-104)

Rizzo: *"poi sono anche loro stessi che dichiarano nei cookbook qual è il modo migliore di come
strutturare il prompt determinati modelli. Ad esempio, questa è l'anatomia di Claude prompt,
quindi il task, context files, referenze, success brief, roots, conversation plan e
l'alignement."* (3:19–3:40)

È una card grafica con, sulla destra, **8 etichette** che marcano le sezioni del prompt. Etichette
lette dal frame (frame-104, colonna destra): **Task · Context Files · Reference · Success Brief ·
Rules · Conversation · Plan · Alignment**.

Trascrizione **integrale** del prompt-template mostrato nella card:

```
I want to [TASK] so that [SUCCESS CRITERIA].

First, read these files completely before responding:

[filename.md] — [what it contains]
[filename.md] — [what it contains]
[filename.md] — [what it contains]

Here is a reference to what I want to achieve:

[Upload reference file as markdown, or paste it here]

Here's what makes this reference work:

[Paste your reverse-engineered blueprint - the patterns, tone,
structure, and rules you extracted from the reference. Format
each one as a rule starting with "Always" or "Never."]

Here's what I need for my version:

SUCCESS BRIEF

Type of output + length:
[Contract, memo, report, proposal, landing page, post?]

Recipient's reaction:
[What should they think/feel/do after reading?]

Does NOT sound like:
[What to avoid - generic AI, too casual, formal, jargon-heavy?]

Success means:
[They sign? They approve? They reply? They take action?]

My context file contains my standards, constraints, landmines,
and audience. Read it fully before starting. If you're about to break
one of my rules, stop and tell me.

DO NOT start executing yet. Instead, ask me clarifying questions
[use `AskUserQuestion` tool] so we can refine the approach
together step by step.

Before you write anything, list the 3 rules from my context file that
matter most for this task.

Then give me your execution plan (5 steps maximum).

Only begin work once we've aligned.
```

> Questo è **il pezzo di prompt engineering di maggior valore del video**: non è un system prompt
> (identità dell'agente), è un **template di prompt di TASK** — cosa scrive l'umano quando affida
> un lavoro. Le tre mosse che lo rendono diverso da un prompt normale:
> (a) *"If you're about to break one of my rules, stop and tell me"* — obbligo di fermarsi, non di
> arrangiarsi;
> (b) *"DO NOT start executing yet… ask me clarifying questions"* con tool `AskUserQuestion` —
> il lavoro comincia dopo l'allineamento, non prima;
> (c) *"list the 3 rules from my context file that matter most for this task"* — un **recall
> forzato** che dimostra che il contesto è stato davvero letto, prima di produrre una riga.

### 3:41–7:50 — Livello 2: CONTEXT ENGINEERING (frame-112, 117, 121, 124, 128, 130, 135, 140, 144, 151, 154, 159, 162, 183, 202, 205, 208, 213, 217, 220, 224)

Rizzo: *"Qua è dove si è lavorato per più tempo perché qui entra in gioco la finestra di contesto…
la Context Window che non è altro che la memoria che può gestire il modello, intesa come quanti
token in input può leggere."* (3:46–4:02)

**Disegno** (frame-140, frame-159): sotto la rete neurale compare una **barra orizzontale** da `0`
a `1M`. La porzione iniziale è colorata di **arancione** = il system prompt. *"Il prompt di
sistema… effettivamente occupa una porzione di questo context window. Tutto il resto invece sono
contesto e informazioni che possiamo ancora utilizzare. Tipicamente ad oggi i modelli di frontiera
possono gestire al massimo 1 milione di token in input."* (4:02–4:25)

Il salto: **l'LLM diventa un agente**. A lavagna (frame-162, frame-205) compaiono, collegati con
frecce verdi bidirezionali, i tre bersagli dei tool: **Files** (icona cartelle) · **WEB** (nuvola)
· **APP**, raggiunto tramite l'etichetta verde **`MCP`**.

*"adesso l'agente… può in autonomia leggere e scrivere e chiamare delle funzioni che gli
permettono di interagire con il web, con i files e con le app… con il protocollo MCP."* (5:00–5:17)

Ogni chiamata riempie la barra: nel frame-205 la barra `0 → 1M` si è riempita di segmenti verdi.
*"Vai sul web, fammi la ricerca e ti riempie contesto. Scrivimi il report sul file locale e ti
riempie contesto. Vai nel mio CRM, quindi usa l'MCP…"* (5:41–5:57)

#### IL PROBLEMA — CONTEXT ROT (frame-183)

Rizzo mostra a schermo il grafico di riferimento. Titolo letto dal frame:

```
Repeated Words - Performance by Input Length (Tokens)
```

Legenda (4 serie, lette dal frame): **Claude Sonnet 4 · GPT-4.1 · Qwen3 32B · Gemini 2.5 Flash**.
Asse X: *Input Length (Tokens)*, scala logaritmica. Tutte e quattro le curve partono vicino a 1.0
e crollano verso destra.

Parole esatte: *"Questa qui si chiama **context rot** e dice che all'aumentare dei token in input
degradano appunto le performance, soprattutto superati i 200.000 token… le performance iniziano a
degradare drasticamente perché ha talmente tanti token nella Context Window che inizia a
confondersi."* (6:02–6:34)

**La risposta del context engineering**: tenere il contesto compatto (risposte dei tool più brevi,
contesto accorciato) e, quando si satura, la **compaction**. Rizzo apre la documentazione ufficiale
di Claude sulla compaction (frame-240, 248, 252) e disegna il meccanismo (frame-220, 224, 248):
barra piena → barra riassunta più corta → si riempie di nuovo → si ricompatta ancora. *"Prova a
riassumere facendo appunto la cosiddetta compaction… e poi che fa? Rifà nuovamente un'altra
compaction e ricompatta ancora."* (7:26–7:44)

### 7:50–11:33 — Livello 3: HARNESS ENGINEERING (frame-260, 264, 272, 274, 283, 298, 301, 334)

*"Tutto questo approccio qua viene poi gestito in autonomia dal nuovo approccio che è nato che si
chiama **Harness Engineering**, dove invece di fare il riassunto e poi riassunto e poi riassunto
che comunque perdi un sacco di performance tramite la compaction… l'harness engineering dice
'Aspetta un attimo, perché non facciamo tutta una struttura esterna per gestire in modo efficace ed
efficiente il contesto'."* (7:45–8:22)

**Disegno** (frame-272, frame-283, frame-334): tutto il blocco precedente (utente + rete + tool +
context window) viene racchiuso in **un rettangolo unico** — "questo diventa un componente unico".
A destra si costruisce **l'impalcatura**: una colonna con quattro righe numerate `1 · 2 · 3 · 4`
(gli step), cerchiate in arancione una alla volta man mano che vengono eseguite, e sotto un
riquadro con l'elenco dei **file markdown** scritto a mano:

```
.MD
Claude.MD
Ag(ents).M(D)
Mem(ory).(md)
```

*"per ogni sottotask abbiamo tutta la finestra del contesto del modello che quindi si va a
riempire, poi termina qui, allora si passa allo step 2, questa viene tutta svuotata e si passa a
lavorare lo step 2 e così via fino al raggiungimento dell'obiettivo finale."* (11:13–11:32)

Il meccanismo chiave dichiarato a voce (9:24–9:51): *"Perché questo? senza dover compattare il
contesto ogni volta. Quindi quando andiamo a saturarlo, senza doverlo compattare, quello che fa
l'agente è scrive su dei file cosa ha fatto, svuota tutta la memoria e si va a leggere il file ogni
qualvolta che riparte la sessione, in modo tale che ha memoria in modo persistente sui file."*

#### PROVA A SCHERMO — la memoria di OpenClaw (frame-301)

Rizzo apre la documentazione OpenClaw, pagina **"Memory overview"**. Testo trascritto dal frame:

```
OpenClaw remembers things by writing plain Markdown files in your agent's
workspace (default ~/.openclaw/workspace). The model only remembers what gets
saved to disk; there is no hidden state.

How it works
Your agent has three memory-related files:

- MEMORY.md — long-term memory. Durable facts, preferences, and decisions.
  Loaded at the start of a session.
- memory/YYYY-MM-DD.md (or memory/YYYY-MM-DD-<slug>.md) — daily notes.
  Running context and observations. Today...
```

Indice laterale destro della pagina (letto dal frame): *How it works · What goes where ·
Action-sensitive memories · Inferred commitments · Memory tools · Memory search · Memory backends ·
Knowledge wiki · Automatic memory · Dreaming · Grounded back… · CLI · Further reading*. Nella
navigazione a sinistra: *Session management · Channel docking · Session pruning · Session tools ·
Memory overview · Builtin memory engine · QMD memory engine · Honcho memory · Memory search ·
Active memory*.

Rizzo aggiunge a voce (10:28–11:05): *"lì poi ha il file che si chiama **Dreams.md** che è
opzionale, che è il Dream Diary… ma sono tutti file. **Si usa il file system come estensione della
context window del modello** e poi gli si dà al modello degli strumenti tipo `memory search`,
`memory get` per poter cercare in quei file… La memory search viene fatta sia in modo semantico —
vedi, *using semantic search* — ma anche facendogli leggere direttamente il file che è stato
scritto sul file system."*

### 11:33–13:35 — I tre test pratici (frame-348, 358, 362, 373, 374, 378, 389, 391, 394, 396, 399, 406)

Rizzo apre l'**app Claude desktop**. Nel pannello statistiche visibile (frame-348) si leggono i suoi
numeri d'uso reali: **Sessioni 97 · Messaggi 8626 · Token totali 9.9M · Giorni attivi 18 · Serie
attuale 0d · Serie più lunga 4d · Ora di punta 16 · Modello preferito Opus 4.6**. In alto un
banner: *"Claude Fable 5 funziona al meglio con l'ultima versione dell'app desktop."*

#### PROMPT MOSTRATO A SCHERMO #3 — test di puro prompt engineering (frame-348, 358, 362)

```
di che colore è fatta la ferrari?
```

Risposta: le Ferrari sono celebri per il rosso, nello specifico il **Rosso Corsa**. Nessun tool
chiamato. *"in questo primo prompt abbiamo semplicemente fatto prompt engineering chiamando solo il
modello e abbiamo ottenuto la risposta. Non abbiamo usato nessun tool."* (11:52–11:59)

#### PROMPT MOSTRATO A SCHERMO #4 — test di context engineering (frame-374, 378, 406)

```
come si chiama l'ultimo modello lanciato da ferrari?
```

Claude risponde *"Lascia che controlli le notizie più recenti, così ti do il modello davvero
aggiornato"*, poi la riga di stato **"Esplorato il web, utilizzando uno strumento"**. Risposta
letta dal frame-378:

> *"Il modello più recente lanciato da Ferrari è la **Ferrari Elettrica** (chiamata anche
> **"Luce"**), la prima auto 100% elettrica della casa di Maranello, svelata completamente il **25
> maggio 2026**. Alcuni dettagli chiave: 4 porte, 4 posti e 4 motori elettrici per oltre 1.000 CV
> complessivi; batteria strutturale da 122 kWh con oltre 530 km di autonomia…"*

Piede della risposta: **"24s · 120 token · ha pensato per 2s"**. In frame-406 si vedono le fonti
citate (*Motorbox · HDmotori · Motor1*) e la coda della risposta: *"Se ti riferisci invece
all'ultimo modello termico/ibrido, i più recenti sono la **849 Testarossa** (hypercar ibrida da
1.050 CV, anche in versione Spider) e la **Amalfi** (gran turismo V8 da 640 CV, erede della Roma).
In totale Ferrari prevede il lancio di 5 nuovi modelli nel 2026."*

*"Questo qua già è context engineering, sta chiamando dei tool per prendere contesto,
informazioni."* (12:16–12:23)

#### PROMPT MOSTRATO A SCHERMO #5 — test di harness engineering (frame-406)

```
clonami il sito della ferrari così com'è
```

*"dato che il sito della Ferrari è molto complesso… questa richiesta è talmente grande che non
entrerebbe dentro tutto un milione di context, quindi va strutturata in sottotask e va gestito
tutto tramite l'Harness Engineering."* (12:52–13:30). In frame-394 si vede il sito ufficiale
**ferrari.com** aperto come riferimento (hero *"CHARLES DELIVERS FERRARI ITS 250TH WIN"*).

### 13:35–15:00 — Livello 4: LOOP ENGINEERING, la definizione (frame-409, 411, 414, 416, 421, 424, 429, 432, 434, 441, 443, 447)

Il disegno finale del video, costruito a strati (frame-443 e frame-447 mostrano lo stato completo):
**tre cicli annidati**, tutti tracciati in viola.

```
LOOP 3  (loop engineering)  +----------------------------------------------+
                            | LOOP 2 (harness)  +-----------------------+   |
                            |                   | step 1  (fatto)       |   |
                            |                   | step 2  (fatto)       |   |
                            |                   | step 3  (fatto)       |   |
                            |                   | step 4                |   |
                            |                   | .MD  Claude.MD        |   |
                            |                   | Agents.MD  Memory.md  |   |
                            |                   +-----------------------+   |
                            | LOOP 1 (tool use)                            |
                            |  utente -> Quest -> [rete neurale] -> tool   |
                            |            ^               Files/WEB/APP-MCP |
                            |            +----- ris <--------------+       |
                            +----------------------------------------------+
```

Parole esatte (13:41–14:19): *"di base il large language model quando chiama i suoi strumenti e
riceve le risposte, questo qua è già un loop, ok? Perché può ciclare sui suoi tool. Questo è un
loop. Non solo, ma quando poi usiamo l'Harness Engineering, quest'altro pezzo, questo qui è un
altro loop perché cicliamo fino a quando tutti i task sono stati risolti. Ok, quindi questo è un
loop, questo è un loop e adesso col loop engineering che facciamo? Prendiamo tutto questo e lo
mettiamo dentro un altro loop, **un loop su loop sul loop**. Questo è il loop engineering."*

Il perché (14:30–14:53): *"fare loop qua sopra evita che tu ogni volta devi fare tutte queste
richieste e ottenere le risposte perché **è l'agente stesso che si fa le domande e le risposte**.
Cioè tu parti con la prima richiesta, setti il loop e da lì in poi il modello cicla e praticamente
tutto l'harness entra dentro un loop."*

### 15:00–16:45 — Due esempi di loop (frame-449, 456, 458, 460, 463, 467, 476, 478, 484, 487)

Lavagna intitolata **"Esempio"** (frame-456), due casi disegnati con screenshot reali accanto:

**Esempio 1 — App mondiali.** Prompt scritto a mano: *"Creami pagina web con portale dei
Mondiali"*. Accanto, lo screenshot dell'app generata (dashboard "Match Highlights" con le tab *All
Matches / Round of 16 / Round of 32 / Group Stage*). Sopra, cerchiato in arancione, **LOOP APP**
(frame-476). *"possiamo mettere l'applicazione in un loop dove ad ogni news, a ogni novità che
l'agente pesca, va e riscrive tutto il codice dell'app, la sistema, la migliora, aggiorna il link e
fa tutto… mantenendo così l'applicazione sempre aggiornata, senza che noi dobbiamo fare questo
lavoro."* (15:24–15:51)

**Esempio 2 — Assistente meeting in locale.** Prompt scritto a mano: *"Creami app per AI per meeting
locale"* (frame-484), con screenshot di un'app di *Live Transcription* (tab *Recording / Summary /
Meetings / Insert*). Il loop qui è **triggerato dalle issue GitHub** (frame-487, annotato `n loop`
in rosso): *"io potrei mettere l'applicazione tramite loop engineering, dove qualsiasi issue aprono
su GitHub, cioè qualsiasi problema incontrano nell'applicazione, parte questo loop dove controlla
l'errore e scrive di nuovo il codice, utilizza i tool e parte di nuovo l'harness engineering che
luppa sopra questa applicazione per migliorarla, senza io dover stare a scrivere il prompt 'risolvi
questo problema'."* (16:11–16:44)

### 16:45–18:05 — Il precedente: Auto Research di Karpathy (frame-504, 505, 508, 510, 522, 535)

*"Andrej Karpathy è stato il primo a creare una struttura del genere per la ricerca, quindi ha
chiamato questo progetto **Auto Research** e alla fine è un loop engineering: ha creato tutto un
harness, l'ha messo dentro un ciclo, dentro un loop, dove fa una serie di esperimenti sul codice
fino al raggiungimento di una condizione, fino al raggiungimento di un obiettivo."* (16:51–17:18)

**Repo mostrata a schermo**: `karpathy/autoresearch` (frame-508), pubblica. Dati letti dal frame:
descrizione **"AI agents running research on single-GPU nanochat training automatically"**,
**90.2k stars · 702 watching · 13k forks**. File nella root: `.gitignore`, `.python-version`,
`README.md`, `analysis.ipynb`, `prepare.py`, `program.md`, `progress.png`, `pyproject.toml`,
`train.py`, `uv.lock`.

**README trascritto dai frame-510 / 522** — l'epigrafe:

```
One day, frontier AI research used to be done by meat computers in between eating,
sleeping, having other fun, and synchronizing once in a while using sound wave
interconnect in the ritual of "group meeting". That era is long gone. Research is
now entirely the domain of autonomous swarms of AI agents running across compute
cluster megastructures in the skies. The agents claim that we are now in the
10,205th generation of the code base, in any case no one could tell if that's right
or wrong as the "code" is now a self-modifying binary that has grown beyond human
comprehension. This repo is the story of how it all begins.

-@karpathy, March 2026
```

E il funzionamento (frame-522), il pezzo operativamente più prezioso:

```
The idea: give an AI agent a small but real LLM training setup and let it
experiment autonomously overnight. It modifies the code, trains for 5 minutes,
checks if the result improved, keeps or discards, and repeats. You wake up in the
morning to a log of experiments and (hopefully) a better model.

How it works
The repo is deliberately kept small and only really has three files that matter:

- prepare.py — fixed constants, one-time data prep (downloads training data,
  trains a BPE tokenizer), and runtime utilities (dataloader, evaluation).
  Not modified.
- train.py — the single file the agent edits. Contains the full GPT model,
  optimizer (Muon + AdamW), and training loop. Everything is fair game.
  This file is edited and iterated on by the agent.
- program.md — baseline instructions for one agent. Point your agent here and
  let it go. This file is edited and iterated on by the human.

By design, training runs for a fixed 5-minute time budget (wall clock, excluding
startup/compilation), regardless of the details of your compute. The metric is
val_bpb (validation bits per byte) — lower is better, and vocab-size-independent
so architectural changes are fairly compared.
```

Nel grafico dei risultati mostrato (frame-510) si legge il titolo: **"Autoresearch Progress: 63
Experiments, 15 kept improvements"**.

> **Il pattern generale, esplicito**: l'umano non tocca più il codice, l'umano **scrive
> `program.md`** — il file di istruzioni che governa il loop. Rizzo lo riformula: *"lui ha fatto uno
> script dove ci sta il dataset… uno script dove si fa il training loop… vengono scritti i risultati
> dentro un file markdown e si continua così a ciclare fino al raggiungimento di una condizione
> finale, del tipo: voglio che mi addestri il modello e che abbia recall superiore al 90%. Oppure
> termina con un limite massimo di iterazioni o di ore che sono passate."* (17:18–17:53)
>
> E la ragione per cui il loop è potente e non solo un `while`: *"sta facendo un loop sopra un
> harness che **si porta con sé tutti i server MCP, tutte le skills**, tutto quel contesto e
> strumenti che può continuare ad utilizzare nel ciclo successivo."* (17:53–18:07)

### 18:05–19:05 — I 4 step del Loop Engineering (frame-544, 546, 551, 553, 557, 560, 564, 567)

Quattro riquadri colorati disegnati in Figma, con una freccia nera che dall'ultimo torna al primo
(frame-564, frame-829):

```
+---------+   +-----------+   +---------------+   +------------------+
| Trigger |-->| Execution |-->| Goal - Verify |-->| OUTPUT + Memory  |
+---------+   +-----------+   +---------------+   +------------------+
     ^                                                       |
     +-------------------------------------------------------+
```

Le parole esatte per ciascuno (18:08–19:05):

1. **Trigger** — *"Dobbiamo avere un trigger, quindi un qualcosa che ci fa avviare il loop. Nel
   caso di questa applicazione potrebbero essere le issue su GitHub. Nel caso di quest'altra
   potrebbero essere delle news che ci arrivano via mail, news che ci arrivano via chiamate API,
   news in un qualsiasi modo."*
2. **Execution** — *"triggerato il loop parte l'execution, quindi qua parte l'harness."*
3. **Goal – Verify** — *"verifica che quella issue è stata risolta o che quelle news sono state
   implementate, c'è una parte di verifica."*
4. **OUTPUT + Memory** — *"e poi viene scritto su file cosa è stato effettuato, tipo memoria, e ci
   si prepara per il loop successivo. Loop successivo che parte quando vi è un nuovo trigger."*

**Tipi di trigger**: *"Trigger che può essere settato manualmente, del tipo 'ogni giorno a
quest'ora parte', oppure ad evento, cioè quando avviene un determinato evento."* (18:57–19:05)

### 19:05–20:30 — I DUE COMANDI: `/loop` e `/goal` (frame-574, 580, 581 → 645)

Rizzo apre **Claude Code nel terminale**. Schermata iniziale letta dai frame-574 / 580:

```
 Claude Code v2.1.193
 Welcome back Simone!

  Opus 4.8 (1M context) with lo… - Claude Max -
  official.simone.rizzo@gmail.com's Organization
  D:\video

 Tips for getting started
 Run /init to create a CLAUDE.md file with instructions for Cla…

 What's new
 Added a "dynamic_workflow_size" setting in /config for contr…
 Added "workflow.run_id" and "workflow.name" OpenTelemetry attr…
 Fixed a crash in the inline Ctrl+R history search when accepti…
 /release-notes for more

! 4 MCP servers need authentication · run /mcp

* Fable 5 is back.
  Until July 7, you can use up to 50% of your plan's weekly usage limit on
  Fable 5. If you hit your limit, you can continue on Fable 5 with usage
  credits. Fable 5 draws down usage faster than Opus 4.8. Learn more
  (https://support.claude.com/en/articles/15424964-claude-fable-5-promotional-access)

> try "create a util logging.py that..."
  / for shortcuts · > for agents
```

> **CORREZIONE IMPORTANTE ALLA TRASCRIZIONE AUDIO.** La trascrizione automatica rende il secondo
> comando come *"slg"*, *"gol"*, *"slash gol"*. **A schermo il comando è `/goal`** — verificato
> carattere per carattere sui frame 585–643. Chi seguisse solo la trascrizione digiterebbe un
> comando inesistente.

**SINTASSI ESATTA LETTA A SCHERMO** (autocomplete di Claude Code, frame-590 e frame-620):

```
/loop [interval] [prompt]
/goal [<condition> | clear]
```

#### PROMPT MOSTRATI A SCHERMO #6 e #7 — i due esempi digitati dal vivo (frame-601, frame-634)

```
/goal sdasa | fai al massimo 100 tentativi
```

```
/goal effetuami la migrazione di questo servizio
```

> (`sdasa` è testo-riempitivo che Rizzo digita per mostrare la posizione della condizione; il pezzo
> che conta è la **barra verticale `|`** che separa l'obiettivo dalla condizione di terminazione. Il
> refuso *effetuami* è suo, riportato tale e quale.)

Gli esempi dati a voce per `/loop` (19:23–19:41): *"i comandi sono `/loop` spazio, appunto si mette
l'intervallo ed il prompt. Quindi intervallo, ad esempio, ogni mattina alle 9:00 prendimi le
informazioni da quella parte e aggiorna il codice, fa partire test bla bla bla. Oppure `/loop` ogni
settimana, oppure ogni… e si mette il tempo."*

E per `/goal` (19:41–20:06): *"Qui possiamo mettere, ad esempio, **ottimizzami tutto il codice della
mia pagina web in modo tale che si possa aprire in meno di 100 millisecondi**, e poi ci si mette la
sbarra dritta. Dopo la condizione, sbarra dritta: **fai al massimo 100 tentativi**, o **fai al
massimo tentativi per 8 ore totali**."*

**LA REGOLA PIÙ IMPORTANTE DEL VIDEO — la condizione di terminazione** (20:06–20:25): *"Perché si
mette quest'altra condizione? Perché mettiamo il caso che gli abbiamo chiesto un qualcosa di
impossibile, magari non si riuscirà mai a ottimizzare la pagina web sotto ai 100 millisecondi.
Quello che succede è che **entra in un ciclo infinito e ci fa consumare tanti tanti token**, quindi
gli si mette la condizione: è sempre un'altra condizione di terminazione."*

**LA SECONDA REGOLA — l'obiettivo deve essere valutabile** (20:26–21:27): *"Il goal deve essere un
qualcosa di **valutabile**… è un qualcosa di verificabile, cioè l'AI parte, modifica il codice, poi
testa effettivamente se sta sotto i 100 millisecondi, se non sta allora parte con l'altro loop."*

Gli altri due esempi di goal verificabile dati a voce:

- *"Effettuami la migrazione di questo servizio in quell'altra parte — è verificabile perché una
  volta che ha effettuato tutta la migrazione di tutto il pacchetto, allora sa se ha terminato o
  no."*
- *"Fammi il training su questo Large Language Model in modo tale che nel validation set raggiunga
  tot % di accuratezza… poi gli mettiamo sempre l'altra condizione, al massimo fai 1000 tentativi."*

### 20:30–24:25 — I 5 LIVELLI DI VERIFICA (frame-645, 647, 648, 665, 719, 727, 795, 800, 829)

La slide più densa del video. **Trascrizione integrale letta dai frame-648 / 800 / 829**:

```
I 5 Livelli di Verifica
dal più forte al più debole. Conosci quale il tuo gate usa davvero.

PIÙ FORTE
    |
    |   1  DETERMINISTICO        asserzioni di codice · exit 0 · schema ·
    |                            golden output match
    |
    |   2  REGOLE / VINCOLI      regole programmatiche sul testo:
    |                            conteggio caratteri · contiene X · lint · policy
    |
    |   3  VERITÀ TERRENA        risposte del mondo reale: test passati ·
    |      (RITARDATA)           deploy · risposta del cliente · engagement
    |
    |   - - - livelli 1-3 = CICLO AUTONOMO VERO - - -
    |
    |   4  LLM COME GIUDICE      secondo modello che valuta rispetto a rubric –
    |                            modello giudicante, non verità terrena
    |
    |   5  CHECKPOINT UMANO      tu approvi – supervisione, NON verifica
    v                            automatizzata
PIÙ DEBOLE
        livelli 4-5 = FLUSSO ASSISTITO (umano nel ciclo)
```

Nel frame-800 Rizzo cerchia in rosso, a fianco del livello 3, la scritta **`/loop`** — cioè: il
livello 3 è il territorio del comando `/loop`, non di `/goal`. E a fianco del livello 4 disegna un
cerchio con una freccia (il ciclo di auto-giudizio).

**Livello 1 — DETERMINISTICO** (21:28–21:44): *"realizzami questa applicazione che deve compilare
senza errori. Non mi deve dare errori. Questa è una cosa booleana deterministica, true/false."*

**Livello 2 — REGOLE / VINCOLI** (21:44–22:09): *"voglio che ci metta sotto 100 millisecondi, o che
l'accuratezza sia sopra il 90%, o che mi consumi tot RAM questo programma, o che il testo sia lungo
al massimo 100 caratteri. Quindi sono regole e vincoli numerici, non booleani."*

**Livello 3 — VERITÀ TERRENA RITARDATA** (22:09–23:57). Il caso mostrato: *"creami un post prendendo
le ultime news da pubblicare su LinkedIn e che sia virale. **Che sia virale è una condizione
vaga**, non è un qualcosa di deterministico, non è un qualcosa che ha delle regole. Quindi magari lo
dovrei cambiare e dirgli: fammi un post che su LinkedIn raggiunga 300 reazioni."*

E qui la mossa: *"Quello che fa l'agente: crea il post, lo carica, ma **non ha modo di verificare
direttamente** che ha raggiunto queste 300 reazioni, perché le reazioni magari maturano in 2-3
giorni. E quindi in questo caso è perfetto il `/loop`, dove gli si spiega l'obiettivo: **ogni giorno
alle tot, controlla i miei ultimi post fatti su LinkedIn e migliora il tuo modo di crearmi caroselli
in modo tale da raggiungere 300 reazioni ad ogni post**."*

*"Ed è ottimo perché **il mondo reale molto spesso ha dei risultati ritardati**: ad esempio, che il
deploy non abbia molti problemi, che i clienti siano soddisfatti, che l'engagement sia tot, o
'ottimizzami questa campagna pubblicitaria' — come goal gli dici di ottimizzare la campagna, ma il
risultato lo vedremo tra giorni."*

**Livello 4 — LLM COME GIUDICE** (23:57–24:25): *"fammi il refactoring del codice fino a che sei
soddisfatto. Il fatto di essere soddisfatto significa che nella fase di goal-verifica è l'AI stessa
che assegna un valore — tra 1 e 10, tra 1 e 20, tra 1 e 100, decide lui — assegna un valore e decide
lei stessa se è arrivata a conclusione oppure no."*

### 24:25–27:55 — Il caso LLM-come-giudice: clonare un'interfaccia (frame-732, 734–737, 741, 747, 751, 755, 762, 768, 776, 783, 790, 806, 809)

Il disegno completo (frame-783, frame-806) si legge così: in alto a sinistra il prompt iniziale
(`Prompt:` con una freccia verso il riquadro della pagina web generata); a destra lo **screenshot**
della pagina reale (ferrari.com, hero *"CHARLES DELIVERS FERRARI ITS 250TH WIN"* — frame-737); in
mezzo la parola **loop** con una freccia in giù; sotto, in rosso, il goal scritto a mano; e a
sinistra la **pila di render successivi** della pagina, uno sotto l'altro, ciascuno più somigliante
all'originale (frame-783: quattro riquadri impilati). Sulla freccia, il punteggio di auto-giudizio:
**`0,30`** che diventa **`0,90`** (frame-783).

#### PROMPT MOSTRATO A SCHERMO #8 — il goal di cloning, scritto a lavagna (frame-762, 776, 806)

```
/goal migliora l'applicazione dal punto di vista della UI/UX
      in modo tale che sia esattamente uguale a questa immagine
      che ti allego   [+ immagine allegata]
      ~ 80 modifiche ~
```

Le parole con cui lo detta (24:56–25:33): *"Ti trovi dentro la codebase di questa applicazione qua.
`/goal` migliora l'applicazione dal punto di vista della UI/UX in modo tale che sia esattamente
uguale a questa immagine che ti allego — e gli alleghi questa immagine qua — **provaci fino a 80
modifiche e di ogni modifica fammi vedere il render della pagina web che hai modificato**."*

Il ciclo (25:33–26:15): *"modifica la pagina, poi si legge di nuovo l'immagine e fa un confronto e
**lei si autogiudica**, dice 'Ok, l'immagine reale con l'immagine render della pagina web quanto
sono vicine?' Dice 'Eh, stanno lontane 0.30'. Ok, allora faccio altre modifiche… Magari arriva a un
punto che si autogiudica che sta a 0,90 perché vede che ha sistemato tutto — header e bottoni, ha
messo gli stessi effetti, stesso font, esattamente le stesse cose. Dice: sono arrivato, ho
concluso."*

**Livello 5 — CHECKPOINT UMANO** (26:36–26:51): *"nel caso peggiore sei tu che fai la valutazione, il
checkpoint umano. Sei tu che guardi ogni pagina, ogni modifica della pagina web e gli dici sì, no, o
gli dai uno score per fargli capire se sta andando bene o male."*

**IL CAVEAT ONESTO DEL VIDEO** (26:52–27:55) — la parte che nessun altro dice: *"Questo approccio
funziona molto bene a loro due perché loro due sono degli sviluppatori, scrivono codice, e quindi
senza dover stare a babysittare quello che fa l'agente definiscono in modo chiaro un loop del tipo
'fammi il refactoring di tutto questo servizio in modo tale che sia più efficiente, che la memoria
occupi meno, in modo tale che i token vengano ridotti del 70%' e gli danno un task ben definito e lo
lasciano andare fino a che non raggiunge quell'obiettivo. **Quindi funziona molto bene a loro perché
è verificabile questo task. Per questo lo dicono: 'io non scrivo più prompt, faccio solo loop'. Ma
in altri casi questo approccio va visto nel dettaglio, perché ci sono cose in cui non è verificabile
in automatico, non è deterministico, e quindi bisogna che noi facciamo da giudici, o l'LLM fa da
giudice, oppure bisogna metterci noi ad avere più controllo di quello che sta accadendo."*

### 27:55–31:23 — LA DEMO REALE: ottimizzazione del prodotto fra matrici (frame-839, 851, 863, 865, 870–894, 906, 924, 934, 935)

Il pezzo migliore per capire cosa **produce davvero** un loop.

#### PROMPT MOSTRATO A SCHERMO #9 — la baseline (frame-839)

```
creami uno script python basico per effettuare il prodotto fra matrici di grandi
dimensioni e valutami il tempo che ci impiega
```

Risposta (letta dal frame-839): *"Fatto. Ho creato `matrix_mult.py` e l'ho eseguito."*

```
Cosa fa lo script
· Genera due matrici quadrate casuali n × n con NumPy
· Le moltiplica con l'operatore @ (prodotto matriciale)
· Misura il tempo con time.perf_counter() e stima i GFLOP/s (usando ~2·n³ operazioni)

Risultati sul tuo PC
   n     | tempo    | throughput
   500   | 0.003 s  |  88 GFLOP/s
   1000  | 0.014 s  | 140 GFLOP/s
   2000  | 0.100 s  | 160 GFLOP/s
   3000  | 0.329 s  | 164 GFLOP/s
```

Esecuzione reale nel terminale (frame-851, frame-863) — `C:\Users\Simone\Desktop\test>`:

```
C:\Users\Simone\Desktop\test>python matrix_mult.py
Benchmark prodotto matriciale (NumPy)

n =   500 |  tempo =  0.004 s |   70.22 GFLOP/s
n =  1000 |  tempo =  0.018 s |  108.46 GFLOP/s
n =  2000 |  tempo =  0.119 s |  134.88 GFLOP/s
n =  3000 |  tempo =  0.398 s |  135.59 GFLOP/s
```

#### PROMPT MOSTRATO A SCHERMO #10 — IL GOAL DELLA DEMO

Digitato dal vivo, carattere per carattere sui frame 866–890, trascritto integralmente:

```
/goal migliora i tempi impiegati per fare il prodotto fra matrici in questo script
python, ad ogni test che fai scrivilo su di un file markdown scrivendo anche in
breve le modifiche fatte per avere tracciabilità | fai al massimo 10 tentativi di
ottimizzazione
```

> Il modello selezionato nella barra inferiore durante la digitazione è **Opus 4.8 · Veloce · Alto**,
> modalità **Auto** (frame-870/885). Il placeholder dell'input è *"Digita / per i comandi"*.
>
> **Anatomia del goal — quattro pezzi in una riga sola:**
> 1. **obiettivo misurabile** — "migliora i tempi impiegati per fare il prodotto fra matrici"
> 2. **perimetro** — "in questo script python"
> 3. **memoria/tracciabilità obbligatoria** — "ad ogni test che fai scrivilo su di un file markdown
>    scrivendo anche in breve le modifiche fatte per avere tracciabilità"
> 4. **condizione di terminazione dopo la `|`** — "fai al massimo 10 tentativi di ottimizzazione"

#### IL RISULTATO (frame-906, 924, 934)

Risposta finale di Claude:

> *"Fatto. **Obiettivo raggiunto: 10 tentativi di ottimizzazione (A0–A9)**, ognuno tracciato in
> `OPTIMIZATION_LOG.md` con la modifica applicata, e lo script principale `matrix_mult.py`
> riscritto con la strategia vincente."*

```
Risultati chiave (matrici 4000×4000)

 Strategia                                    | Best    | Speedup
 A0  Baseline NumPy @ float64                 | 870 ms  |   —
 A1  float32                                  | 433 ms  |  2.0x
 A3  float32 + out preallocato (miglior CPU)  | 331 ms  |  2.6x
 A6  GPU float32, solo calcolo                | 10.4 ms |  84x
 A7  GPU float32, incluso transfer CPU→GPU    |  56 ms  |  15x
 A9  GPU float16 (tensor core)                |  2.7 ms | 320x

Cosa ho imparato dai test:
· float64 → float32 = 2x gratis (la doppia precisione qui non serve).
· Riusare il buffer del risultato con np.matmul(out=...) è il meglio su CPU (2.6x).
· Thread tuning (A2) e scipy sgemm (A4) peggiorano o scartati (OpenBLAS si gestisce
  già bene, sgemm ricopia i dati).
· La GPU stravince: il collo di bottiglia diventa il transfer CPU→GPU, non il calcolo.
```

#### IL FILE `OPTIMIZATION_LOG.md` PRODOTTO DAL LOOP (frame-924, pannello destro)

È la memoria del ciclo, cioè lo step 4 "OUTPUT + Memory". Trascritto integralmente dal frame:

```
Log ottimizzazione prodotto matriciale

Matrici 4000 × 4000, mediana su 5 run (dopo warmup). Speedup calcolato sul best
rispetto alla baseline.

Hardware: CPU 8 core, GPU NVIDIA RTX 5060 Ti (CUDA), NumPy 2.2.6 + OpenBLAS 0.3.29.

 #  | Metodo                    | Mediana | Best  | GFLOP/s | Speedup | Modifica
    |                           |  (ms)   | (ms)  |         |         |
 A0 | NumPy @ float64 (baseline)|  884.1  | 870.6 |   147.0 |    —    | Script originale, dtype float64 di default
 A1 | NumPy @ float32           |  439.1  | 432.7 |   295.8 |  2.01x  | dtype float32, meta' dati, ~2x banda memoria
 A2 | float32 + BLAS 4 thread   |  492.8  | 482.7 |   265.2 |  1.80x  | threadpool_limits=4 (core fisici, evita oversubscription HT)
 A3 | float32 + out preallocato |  428.1  | 331.4 |   386.2 |  2.63x  | np.matmul(out=...) riusa il buffer del risultato
 A4 | scipy sgemm float32       |  575.4  | 567.6 |   225.5 |  1.53x  | Chiamata BLAS sgemm diretta, salta overhead ufunc NumPy
 A5 | PyTorch CPU float32       |  391.2  | 377.9 |   338.7 |  2.30x  | torch.mm su CPU (backend ATen/BLAS)
 A6 | PyTorch GPU float32       |   12.0  |  10.4 | 12367.0 | 84.12x  | Dati residenti su GPU, sync CUDA, esclude transfer
    | (solo calcolo)            |         |       |         |         |
 A7 | PyTorch GPU float32       |   61.4  |  56.3 |  2274.0 | 15.47x  | Include copia CPU→GPU e risultato GPU→CPU
    | (+ transfer)              |         |       |         |         |
 A8 | PyTorch GPU TF32          |    6.4  |   5.5 | 23311.3 | 158.56x | allow_tf32=True: tensor core, precisione TF32
    | (solo calcolo)            |         |       |         |         |
```

E la nota finale (frame-934):

> *"Script finale: `matrix_mult.py` usa la GPU float32 quando c'è CUDA (precisione singola piena,
> nessun trucco tensor-core che degrada l'accuratezza), con fallback automatico a NumPy float32
> ottimizzato su macchine senza GPU. Eseguito e verificato → 4000×4000 in circa ~113 ms end-to-end
> (sulla CPU si ottiene circa 870 ms end-to-end)."*
>
> *"Nota: TF32 (A8) e float16 (A9) sono ancora più veloci ma riducono la precisione — non li ho messi
> nello script di default perché adatti al ML, non al calcolo numerico esatto. Se vuoi massimizzare a
> scapito della precisione, posso attivarli con un flag."*

Rizzo commenta (29:56–30:41): *"Ecco qua che ha fatto tutti e 10 i tentativi. Abbiamo qua lo speedup,
quindi ha raggiunto un'ottimizzazione di **320 volte** dal punto di vista della velocità usando
appunto i tensor core. Qua su optimization log vediamo tutte le modifiche che ha fatto."*

### 31:00–31:23 — Chiusura (frame-937–942)

*"Questo è un esempio molto semplice, però che ti fa capire le potenzialità di questo approccio,
soprattutto nel coding e nelle app, ma lo si può utilizzare anche per fargli creare modelli 3D, post
sui social, praticamente qualsiasi cosa, perché poi Claude con i vari server MCP lo puoi collegare a
tutto e quindi puoi utilizzare il loop engineering praticamente per qualsiasi cosa."* (30:41–31:06)

Rizzo cita anche (19:05–19:20) che ha *"preparato tutta una lezione dentro la mia accademia dove nel
dettaglio mostro casi d'uso reali di loop engineering e soprattutto quando serve utilizzarlo e
quando no"* — contenuto non mostrato nel video.

---

## 2. I dieci prompt trascritti — indice rapido

| # | Cosa | Timestamp | Frame | Sezione |
|---|---|---|---|---|
| 1 | System prompt trapelato `claude-fable-5.md` (token_budget 190000) | 2:44–3:18 | frame-083 | PROMPT #1 |
| 2 | **"The Anatomy of a Claude prompt"** — template a 8 sezioni, integrale | 3:19–3:40 | frame-104 | PROMPT #2 |
| 3 | `di che colore è fatta la ferrari?` | 11:35 | frame-348 | PROMPT #3 |
| 4 | `come si chiama l'ultimo modello lanciato da ferrari?` | 12:02 | frame-374 | PROMPT #4 |
| 5 | `clonami il sito della ferrari così com'è` | 12:44 | frame-406 | PROMPT #5 |
| 6 | `/goal sdasa \| fai al massimo 100 tentativi` | 19:56 | frame-601 | PROMPT #6 |
| 7 | `/goal effetuami la migrazione di questo servizio` | 20:48 | frame-634 | PROMPT #7 |
| 8 | `/goal migliora l'applicazione dal punto di vista della UI/UX…` (cloning) | 25:01 | frame-762 | PROMPT #8 |
| 9 | `creami uno script python basico per effettuare il prodotto fra matrici…` | 27:56 | frame-839 | PROMPT #9 |
| 10 | `/goal migliora i tempi impiegati per fare il prodotto fra matrici…` | 28:48–30:05 | frame-870→890 | PROMPT #10 |

Più le due **sintassi di comando** lette dall'autocomplete: `/loop [interval] [prompt]` e
`/goal [<condition> | clear]` (frame-590, frame-620).

---

## 3. I quattro livelli in tabella — il modello mentale da portare a casa

| Livello | Cosa progetta l'umano | Cosa fallisce e obbliga al livello dopo | Prova nel video |
|---|---|---|---|
| **Prompt Engineering** | Il system prompt: identità e istruzioni | Il modello sa solo ciò che ha in pancia | `di che colore è fatta la ferrari?` (11:35) |
| **Context Engineering** | Quali tool, quanto contesto, come comprimerlo | **Context rot**: oltre ~200k token le performance crollano; la compaction perde informazione | grafico context rot (6:02) + doc compaction (8:05) |
| **Harness Engineering** | L'impalcatura: sottotask + file markdown come memoria persistente | Serve comunque un umano che rilanci e giudichi ogni giro | doc memoria OpenClaw: `MEMORY.md`, `memory/YYYY-MM-DD.md`, `Dreams.md` (9:55) |
| **Loop Engineering** | **Il trigger, il goal verificabile e la condizione di terminazione** | Fallisce quando il goal non è verificabile in automatico (→ LLM giudice o umano) | demo matrici: 10 tentativi, 320x, `OPTIMIZATION_LOG.md` (27:55) |

---

## 4. Le regole operative estratte (in ordine di importanza)

1. **Ogni goal porta SEMPRE due condizioni**: l'obiettivo *e* il limite (tentativi o ore), separate
   dalla `|`. Senza il limite, un obiettivo impossibile produce un **ciclo infinito che brucia
   token** (20:06).
2. **Un goal vale solo se è valutabile** dall'agente stesso. "Che sia virale" non è un goal; "che
   raggiunga 300 reazioni" lo è (22:20).
3. **Sapere su quale dei 5 livelli sta il proprio gate.** Livelli 1-3 = ciclo autonomo vero. Livelli
   4-5 = flusso assistito, c'è un umano o un giudice-modello nel ciclo. Il testo a schermo è
   esplicito: *"Conosci quale il tuo gate usa davvero."*
4. **Ogni giro scrive su file.** La memoria del loop non sta nel contesto: sta in un markdown
   (`OPTIMIZATION_LOG.md` nel video, `program.md` in autoresearch, `MEMORY.md` in OpenClaw). È ciò
   che permette di svuotare il contesto senza perdere il lavoro.
5. **Per obiettivi a verità ritardata (social, campagne, deploy, soddisfazione cliente) si usa
   `/loop` a cadenza, non `/goal` a tentativi**: il risultato matura fuori dalla sessione, il ciclo
   successivo lo legge e corregge la strategia (22:50).
6. **Il loop si porta dietro l'harness intero** — MCP, skill, contesto — quindi il ciclo N+1 non
   riparte a mani vuote (17:53).
7. **Il loop engineering funziona benissimo dove il lavoro è verificabile in automatico (codice), e
   va guardato con attenzione dove non lo è.** È il caveat dichiarato dall'autore stesso (27:26).

---

## 5. Cosa il video NON dice (vuoti dichiarati)

- **Non mostra `/loop` in esecuzione.** Mostra la sintassi nell'autocomplete e un esempio digitato,
  ma la demo reale è fatta solo con `/goal`.
- **Non dice se `/loop` e `/goal` siano comandi nativi di Claude Code o custom slash command
  dell'utente.** Compaiono nell'autocomplete della sua installazione con le rispettive descrizioni
  di parametri; il video non mostra né `~/.claude/commands/` né la fonte. ➕ *Inferenza non
  verificata dal video: potrebbero essere comandi installati o custom.* Chi vuole replicare deve
  verificarlo sulla propria installazione.
- **Non quantifica il costo** in token o in euro di una sessione `/goal` da 10 tentativi.
- **Non mostra il contenuto di `program.md`** di autoresearch (lo cita solo il README).
- **Non dà un criterio per scegliere il numero di tentativi**: 100, 80, 10, 1000 compaiono come
  numeri diversi in esempi diversi, senza regola.

---

*Analisi prodotta il 2026-09-03 · Empire Studio · run `max17-v07-rizzo-prompt` · NO-FINTO: ogni riga
fra virgolette proviene da un frame effettivamente guardato o dalla trascrizione; le inferenze sono
marcate `➕`.*
