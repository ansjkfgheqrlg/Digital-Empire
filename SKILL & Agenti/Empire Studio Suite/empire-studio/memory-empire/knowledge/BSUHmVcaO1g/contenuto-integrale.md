# Contenuto Integrale — BSUHmVcaO1g
## "Se usi ancora i prompt... devi vedere questa evoluzione" — Simone Rizzo

**Fonte audio:** trascrizione italiana auto-generata YouTube (`BSUHmVcaO1g.it.vtt`), letta
integralmente, deduplicata in `transcript_clean.txt` (732 segmenti puliti).
**Fonte visiva:** 176 frame guardati su 942 estratti (133 dei 224 frame unici indicati da
`scenes.md`), 0 illeggibili. Copertura dichiarata **parziale ma completa per capitolo** — dettaglio
in `runs/max17-v07-rizzo-prompt/coverage.md`.
**Durata:** 31:23 (1883s) · **Canale:** Simone Rizzo · **Lingua:** italiano
**Run sorgente:** `empire-studio/runs/max17-v07-rizzo-prompt`
**Archiviato:** 2026-09-03 (Memory Empire Stage C)

> **Regola applicata:** questo file **espande e riorganizza per categoria** `video-analysis.md`
> (walkthrough cronologico) senza riassumere. Ogni prompt, ogni comando, ogni tabella trascritta
> compare qui per intero.

---

## PARTE 1 — LA PILA A QUATTRO LIVELLI

### 1.1 La tesi

Il prompt engineering non è morto: è diventato il **livello più basso** di una pila.
**Prompt → Context → Harness → Loop Engineering.** Ogni strato nasce per risolvere il fallimento
dello strato precedente.

Linea del tempo disegnata a lavagna (frame-003, frame-011), con i tick `2022 → 2027`:

| Periodo | Paradigma |
|---|---|
| fino al 2023 | **Prompt** |
| 2024–2025 | **Context** |
| 2026 | **Harness** |
| 2027 (cerchiato in arancione) | **Loop Engineering** |

Rizzo (0:11): *"Siamo passati dal prompt Engineering al Context Engineering all'Harness Engineering
che è durato veramente poco e adesso già siamo entrati in questa nuova era del Loop Engineering."*

### 1.2 Le due fonti che hanno lanciato il termine

**Boris Cherny** (creatore di Claude Code), citato a 0:41: non scrive più i prompt; è Claude che si
scrive i prompt da sola tramite i loop che crea. Il suo compito adesso è **creare loop**.

**Peter Steinberger** (creatore di **OpenClaw**), post su X mostrato a schermo (frame-036):

```
Here's your monthly reminder that you shouldn't be prompting
coding agents anymore. You should be designing loops that prompt
your agents.

8:58 PM · Jun 7, 2026 · 8.4M Views
```

Con l'unica obiezione visibile nel video, di **Wes Winder**: *"but you kinda still need to be in
the loop to test stuff unless you literally have infinite tokens"* — risposta di Steinberger:
*"wellllllll"*.

### 1.3 Livello 1 — Prompt Engineering

Definizione data: scrittura del **system prompt**, cioè le istruzioni di identità ("sei un
avvocato", "sei un front-end developer", "sei un assistente personale per la customer care"). Il
modello risponde a ogni domanda in base a quel prompt.

Disegno (frame-076): utente → **Quest**(ion) → rete neurale → **ris**(posta). Sopra la rete, un
rettangolo arancione = il system prompt.

### 1.4 Livello 2 — Context Engineering

**Context Window** = la memoria che il modello può gestire, cioè quanti token in input può leggere.
Il system prompt ne occupa una porzione fissa; il resto è spazio disponibile. Disegnata come barra
da `0` a **`1M`** (frame-140, frame-159): *"Tipicamente ad oggi i modelli di frontiera possono
gestire al massimo 1 milione di token in input."*

Il salto: **l'LLM diventa un AGENTE** e può leggere/scrivere e chiamare funzioni verso tre bersagli
(frame-162): **Files** · **WEB** · **APP** (via **MCP**). Ogni chiamata riempie la barra.

**IL PROBLEMA — CONTEXT ROT** (frame-183). Grafico mostrato:
titolo `Repeated Words - Performance by Input Length (Tokens)`, legenda **Claude Sonnet 4 · GPT-4.1
· Qwen3 32B · Gemini 2.5 Flash**. Tutte e quattro le curve crollano.

Parole esatte: *"all'aumentare dei token in input degradano le performance, soprattutto superati i
**200.000 token**… perché ha talmente tanti token nella Context Window che inizia a confondersi."*

**Le due risposte del context engineering:** (a) tenere il contesto compatto — accorciarlo, chiedere
risposte più brevi ai tool; (b) **compaction** — riassumere il contesto per liberare spazio, e
ripetere. Il limite dichiarato: *"riassunto e poi riassunto e poi riassunto — comunque perdi un
sacco di performance"*.

### 1.5 Livello 3 — Harness Engineering

**Definizione:** costruire un'**impalcatura esterna** al modello che struttura il task in sottotask
numerati e che, per ogni sottotask, riempie e poi **svuota completamente** la context window prima
di passare al successivo. L'intero blocco modello+tool+contesto diventa "un componente unico"
(frame-283).

**Il meccanismo che sostituisce la compaction** (9:24): l'agente **scrive su file** cosa ha fatto,
**svuota tutta la memoria**, e **rilegge il file** ogni volta che riparte la sessione. Memoria
persistente su file invece che nel contesto.

File tipici disegnati a lavagna (frame-334): `.MD` · `Claude.MD` · `Agents.MD` · `Memory.md`.

**PRINCIPIO CARDINE, parole esatte (10:35):**
> *"Si usa il file system come estensione della context window del modello, e poi gli si dà al
> modello degli strumenti tipo `memory search`, `memory get` per poter cercare in quei file e
> leggersi in modo dinamico quello che gli serve."*

La memory search è **sia semantica sia lettura diretta del file**.

### 1.6 Livello 4 — Loop Engineering

**Tre cicli annidati** (frame-443, frame-447):

- **Loop 1** — il ciclo tool-use nativo: l'LLM chiama gli strumenti e riceve le risposte, ciclando.
- **Loop 2** — l'harness: cicla finché tutti i sottotask sono risolti.
- **Loop 3** — il loop engineering: mette **tutto l'harness** dentro un altro ciclo.

Parole esatte (14:12): *"Prendiamo tutto questo e lo mettiamo dentro un altro loop, **un loop su
loop sul loop**. Questo è il loop engineering."*

**Il valore** (14:30): *"è l'agente stesso che si fa le domande e le risposte. Cioè tu parti con la
prima richiesta, setti il loop e da lì in poi il modello cicla."*

**Perché è più di un `while`** (17:53): *"sta facendo un loop sopra un harness che **si porta con sé
tutti i server MCP, tutte le skills**, tutto quel contesto e strumenti che può continuare ad
utilizzare nel ciclo successivo."*

---

## PARTE 2 — I DIECI PROMPT TRASCRITTI

### 2.1 PROMPT #1 — Il system prompt trapelato di Claude (frame-083, 2:44)

Repo GitHub **`asgeirtj/system_prompts_leaks`**, cartella `Anthropic`, file **`claude-fable-5.md`**
(~1090 righe / 143 KB). Prima schermata, testo integrale letto dal frame:

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

### 2.2 PROMPT #2 — "The Anatomy of a Claude prompt" (frame-104, 3:19) — IL PEZZO PIÙ PREZIOSO

Card grafica con **8 sezioni etichettate**: **Task · Context Files · Reference · Success Brief ·
Rules · Conversation · Plan · Alignment**. Trascrizione **integrale** del template:

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

**Perché conta — le tre mosse che nessun prompt normale ha:**

1. **Fermarsi invece di arrangiarsi** — *"If you're about to break one of my rules, stop and tell
   me."* Trasforma la violazione di una regola da errore silenzioso in escalation esplicita.
2. **Divieto di esecuzione prima dell'allineamento** — *"DO NOT start executing yet. Instead, ask me
   clarifying questions [use `AskUserQuestion` tool]."* Il lavoro comincia dopo l'accordo, non
   prima.
3. **Recall forzato** — *"Before you write anything, list the 3 rules from my context file that
   matter most for this task."* È una **prova di lettura**: dimostra che il contesto è stato
   davvero assorbito prima di produrre una riga.

Più due chiusure sobrie: *"give me your execution plan (5 steps maximum)"* — il piano ha un tetto —
e *"Only begin work once we've aligned."*

### 2.3 PROMPT #3, #4, #5 — I tre test comparativi (11:35–12:44)

| # | Prompt esatto | Livello dimostrato | Frame |
|---|---|---|---|
| 3 | `di che colore è fatta la ferrari?` | **Prompt engineering** — solo conoscenza del modello, nessun tool. Risposta: Rosso Corsa | frame-348 |
| 4 | `come si chiama l'ultimo modello lanciato da ferrari?` | **Context engineering** — Claude dice *"Lascia che controlli le notizie più recenti"*, esegue *"Esplorato il web, utilizzando uno strumento"*, cita fonti (Motorbox, HDmotori, Motor1). Piede: 24s, 120 token, ha pensato per 2s | frame-378, 406 |
| 5 | `clonami il sito della ferrari così com'è` | **Harness engineering** — *"questa richiesta è talmente grande che non entrerebbe dentro tutto un milione di context, quindi va strutturata in sottotask"* | frame-406 |

Risposta al #4, letta dal frame: *"Il modello più recente lanciato da Ferrari è la **Ferrari
Elettrica** (chiamata anche **"Luce"**), la prima auto 100% elettrica della casa di Maranello,
svelata completamente il 25 maggio 2026. Alcuni dettagli chiave: 4 porte, 4 posti e 4 motori
elettrici per oltre 1.000 CV complessivi; batteria strutturale da 122 kWh con oltre 530 km di
autonomia… Se ti riferisci invece all'ultimo modello termico/ibrido, i più recenti sono la 849
Testarossa (hypercar ibrida da 1.050 CV, anche in versione Spider) e la Amalfi (gran turismo V8 da
640 CV, erede della Roma). In totale Ferrari prevede il lancio di 5 nuovi modelli nel 2026."*

### 2.4 PROMPT #6 e #7 — I due `/goal` digitati dal vivo (19:56, 20:48)

```
/goal sdasa | fai al massimo 100 tentativi
```

```
/goal effetuami la migrazione di questo servizio
```

(`sdasa` è testo-riempitivo; il refuso *effetuami* è dell'autore.)

### 2.5 PROMPT #8 — Il goal di cloning con LLM giudice (24:56, frame-762/776/806)

```
/goal migliora l'applicazione dal punto di vista della UI/UX
      in modo tale che sia esattamente uguale a questa immagine
      che ti allego   [+ screenshot allegato]
      ~ 80 modifiche ~
      e di ogni modifica fammi vedere il render della pagina web che hai modificato
```

Il ciclo di auto-giudizio disegnato a lavagna (frame-783): pila di render successivi, con il
punteggio di somiglianza che passa da **0,30** (lontane) a **0,90** (*"ha sistemato tutto, header e
bottoni, stessi effetti, stesso font"*) → *"sono arrivato, ho concluso"*.

### 2.6 PROMPT #9 — La baseline della demo (27:56, frame-839)

```
creami uno script python basico per effettuare il prodotto fra matrici di grandi
dimensioni e valutami il tempo che ci impiega
```

Risposta: *"Fatto. Ho creato `matrix_mult.py` e l'ho eseguito."*

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

Esecuzione reale nel terminale (frame-863):

```
C:\Users\Simone\Desktop\test>python matrix_mult.py
Benchmark prodotto matriciale (NumPy)

n =   500 |  tempo =  0.004 s |   70.22 GFLOP/s
n =  1000 |  tempo =  0.018 s |  108.46 GFLOP/s
n =  2000 |  tempo =  0.119 s |  134.88 GFLOP/s
n =  3000 |  tempo =  0.398 s |  135.59 GFLOP/s
```

### 2.7 PROMPT #10 — IL GOAL DELLA DEMO (28:48, frame-866→890)

Ricostruito carattere per carattere dai frame di digitazione:

```
/goal migliora i tempi impiegati per fare il prodotto fra matrici in questo script
python, ad ogni test che fai scrivilo su di un file markdown scrivendo anche in
breve le modifiche fatte per avere tracciabilità | fai al massimo 10 tentativi di
ottimizzazione
```

Ambiente: app Claude desktop, modello **Opus 4.8 · Veloce · Alto**, modalità **Auto**, placeholder
*"Digita / per i comandi"*.

---

## PARTE 3 — I DUE COMANDI E LA LORO SINTASSI

**⚠️ CORREZIONE ALLA TRASCRIZIONE AUDIO.** La trascrizione automatica rende il comando come *"slg"*,
*"gol"*, *"slash gol"*. **A schermo è `/goal`** — verificato carattere per carattere sui frame
585–643. Chi seguisse solo l'audio digiterebbe un comando che non esiste.

Sintassi esatta letta dall'autocomplete di Claude Code:

```
/loop [interval] [prompt]
/goal [<condition> | clear]
```

| Comando | Quando si usa | Esempi dati nel video |
|---|---|---|
| `/loop` | Obiettivi a **verità ritardata**: il risultato matura fuori dalla sessione (social, campagne, deploy, soddisfazione cliente). Livello 3 della scala di verifica | *"ogni mattina alle 9:00 prendimi le informazioni da quella parte e aggiorna il codice, fai partire i test"* · *"/loop ogni settimana"* · *"ogni giorno alle tot controlla i miei ultimi post fatti su LinkedIn e migliora il tuo modo di crearmi caroselli in modo tale da raggiungere 300 reazioni ad ogni post"* |
| `/goal` | Obiettivi **verificabili nella sessione stessa**, a tentativi. Livelli 1-2 (e 4 con LLM giudice) | *"ottimizzami tutto il codice della mia pagina web in modo tale che si possa aprire in meno di 100 millisecondi \| fai al massimo 100 tentativi"* · *"effettuami la migrazione di questo servizio"* · *"fammi il training su questo LLM in modo tale che nel validation set raggiunga tot % di accuratezza \| al massimo fai 1000 tentativi"* |

**La barra verticale `|` separa l'obiettivo dalla condizione di terminazione.**

---

## PARTE 4 — LE REGOLE OPERATIVE

### 4.1 REGOLA 1 — La condizione di terminazione è obbligatoria

Parole esatte (20:06): *"Perché si mette quest'altra condizione? Perché mettiamo il caso che gli
abbiamo chiesto un qualcosa di impossibile, magari non si riuscirà mai a ottimizzare la pagina web
sotto ai 100 millisecondi. Quello che succede è che **entra in un ciclo infinito e ci fa consumare
tanti tanti token**, quindi gli si mette la condizione: è sempre un'altra condizione di
terminazione."*

Forme viste nel video: `fai al massimo 100 tentativi` · `fai al massimo tentativi per 8 ore totali`
· `al massimo fai 1000 tentativi` · `fai al massimo 10 tentativi di ottimizzazione` · `provaci fino
a 80 modifiche`.

### 4.2 REGOLA 2 — Il goal deve essere valutabile dall'agente stesso

*"Il goal deve essere un qualcosa di **valutabile**… è un qualcosa di verificabile, cioè l'AI parte,
modifica il codice, poi testa effettivamente se sta sotto i 100 millisecondi, se non sta allora
parte con l'altro loop."*

| Goal NON valido | Perché | Riformulazione valida |
|---|---|---|
| "creami un post… **e che sia virale**" | *"è una condizione vaga, non è deterministico, non ha regole"* | "fammi un post che su LinkedIn **raggiunga 300 reazioni**" |
| "fai del tuo meglio" | non c'è terminazione | "sotto i 100 ms" / "sopra il 90% di accuratezza" |

### 4.3 REGOLA 3 — I 5 LIVELLI DI VERIFICA

Slide trascritta integralmente (frame-648 / 800 / 829). Sottotitolo: *"dal più forte al più debole.
**Conosci quale il tuo gate usa davvero.**"*

```
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

**Esempi per livello, dalle parole dell'autore:**

- **1 Deterministico** — *"realizzami questa applicazione che deve compilare senza errori. Non mi
  deve dare errori. Questa è una cosa booleana deterministica, true/false."*
- **2 Regole/vincoli** — *"sotto 100 millisecondi, o accuratezza sopra il 90%, o mi consumi tot RAM,
  o il testo sia lungo al massimo 100 caratteri. Sono regole e vincoli numerici, non booleani."*
- **3 Verità terrena ritardata** — *"il mondo reale molto spesso ha dei risultati ritardati: che il
  deploy non abbia molti problemi, che i clienti siano soddisfatti, che l'engagement sia tot, o
  'ottimizzami questa campagna pubblicitaria' — il risultato lo vedremo tra giorni."* Nel frame-800
  Rizzo cerchia `/loop` proprio a fianco di questo livello.
- **4 LLM come giudice** — *"fammi il refactoring del codice fino a che sei soddisfatto. Nella fase
  di goal-verifica è l'AI stessa che assegna un valore — tra 1 e 10, tra 1 e 20, tra 1 e 100, decide
  lei — e decide lei stessa se è arrivata a conclusione oppure no."*
- **5 Checkpoint umano** — *"sei tu che guardi ogni pagina, ogni modifica della pagina web e gli dici
  sì, no, o gli dai uno score."*

### 4.4 REGOLA 4 — Ogni giro scrive su file

La memoria del loop non sta nel contesto: sta in un markdown. Tre prove nel video:

| Sistema | File di memoria del loop |
|---|---|
| demo prodotto matrici | `OPTIMIZATION_LOG.md` |
| autoresearch (Karpathy) | `program.md` (istruzioni, scritto dall'umano) + log degli esperimenti |
| OpenClaw | `MEMORY.md` · `memory/YYYY-MM-DD.md` · `Dreams.md` (opzionale) |
| harness generico | `.MD` · `Claude.MD` · `Agents.MD` · `Memory.md` |

### 4.5 REGOLA 5 — L'anatomia del goal, quattro pezzi in una riga

Estratta dal PROMPT #10, è il template riutilizzabile:

```
/goal  [1 OBIETTIVO MISURABILE]  [2 PERIMETRO]  ,
       [3 TRACCIABILITÀ SU FILE: ad ogni tentativo scrivi cosa hai cambiato]
       | [4 CONDIZIONE DI TERMINAZIONE: max N tentativi oppure max N ore]
```

Applicato al caso reale:

1. obiettivo misurabile → *"migliora i tempi impiegati per fare il prodotto fra matrici"*
2. perimetro → *"in questo script python"*
3. tracciabilità → *"ad ogni test che fai scrivilo su di un file markdown scrivendo anche in breve
   le modifiche fatte per avere tracciabilità"*
4. terminazione → *"| fai al massimo 10 tentativi di ottimizzazione"*

### 4.6 IL CAVEAT ONESTO (26:52)

Il pezzo che nessun altro dice, riportato integralmente:

> *"Questo approccio funziona molto bene a loro due perché loro due sono degli sviluppatori,
> scrivono codice, e quindi senza dover stare a babysittare quello che fa l'agente definiscono in
> modo chiaro un loop del tipo 'fammi il refactoring di tutto questo servizio in modo tale che sia
> più efficiente, che la memoria occupi meno, in modo tale che i token vengano ridotti del 70%' e
> gli danno un task ben definito e lo lasciano andare fino a che non raggiunge quell'obiettivo.
> Quindi funziona molto bene a loro **perché è verificabile questo task**. Per questo lo dicono: io
> non scrivo più prompt, faccio solo loop. **Ma in altri casi questo approccio va visto nel
> dettaglio**, perché ci sono cose in cui non è verificabile in automatico, non è deterministico, e
> quindi bisogna che noi facciamo da giudici, o l'LLM fa da giudice, oppure bisogna metterci noi ad
> avere più controllo di quello che sta accadendo."*

---

## PARTE 5 — I QUATTRO STEP DEL LOOP (il ciclo operativo)

Quattro riquadri colorati con freccia di ritorno (frame-564):

```
+---------+   +-----------+   +---------------+   +------------------+
| Trigger |-->| Execution |-->| Goal - Verify |-->| OUTPUT + Memory  |
+---------+   +-----------+   +---------------+   +------------------+
     ^                                                       |
     +-------------------------------------------------------+
```

| Step | Definizione dell'autore | Esempi dati |
|---|---|---|
| **1 Trigger** | *"un qualcosa che ci fa avviare il loop"* | issue su GitHub · news via mail · news via chiamate API. Può essere **a cadenza** ("ogni giorno a quest'ora parte") o **ad evento** |
| **2 Execution** | *"parte l'harness"* | l'intero blocco harness gira |
| **3 Goal – Verify** | *"verifica che quella issue è stata risolta o che quelle news sono state implementate"* | qui si applica la scala dei 5 livelli |
| **4 OUTPUT + Memory** | *"viene scritto su file cosa è stato effettuato, tipo memoria, e ci si prepara per il loop successivo"* | `OPTIMIZATION_LOG.md`, `program.md`, `MEMORY.md` |

---

## PARTE 6 — I CASI D'USO MOSTRATI

### 6.1 App mondiali (15:24) — loop su news

App "portale dei Mondiali" (dashboard *Match Highlights*, tab *All Matches / Round of 16 / Round of
32 / Group Stage*) generata con harness, poi messa in loop: *"ad ogni news, a ogni novità che
l'agente pesca, va e riscrive tutto il codice dell'app, la sistema, la migliora, aggiorna il link e
fa tutto… mantenendo così l'applicazione sempre aggiornata, senza che noi dobbiamo fare questo
lavoro."*

### 6.2 App meeting open source (16:11) — loop su issue GitHub

App di assistente meeting in locale (*Live Transcription*), open source su GitHub. Trigger =
qualsiasi issue aperta: *"parte questo loop dove controlla l'errore e scrive di nuovo il codice,
utilizza i tool e parte di nuovo l'harness engineering che luppa sopra questa applicazione per
migliorarla, senza io dover stare a scrivere il prompt 'risolvi questo problema'."*

### 6.3 `karpathy/autoresearch` (16:58) — il precedente accademico

Repo mostrata a schermo: descrizione **"AI agents running research on single-GPU nanochat training
automatically"**, **90.2k stars · 702 watching · 13k forks**. File in root: `.gitignore`,
`.python-version`, `README.md`, `analysis.ipynb`, `prepare.py`, `program.md`, `progress.png`,
`pyproject.toml`, `train.py`, `uv.lock`.

**Epigrafe del README**, integrale:

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

**Il funzionamento**, integrale:

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

Grafico dei risultati mostrato: **"Autoresearch Progress: 63 Experiments, 15 kept improvements"**.

> **La divisione del lavoro è la lezione:** `prepare.py` **non si tocca** (l'ambiente è fisso e
> confrontabile) · `train.py` è **dell'agente** · `program.md` è **dell'umano**. L'umano smette di
> scrivere codice e scrive **il file di istruzioni che governa il loop**.
>
> E il budget fisso di 5 minuti a run **è la condizione di terminazione a livello di esperimento**:
> senza, esperimenti diversi non sarebbero confrontabili.

### 6.4 La demo reale: prodotto fra matrici (27:55) — il risultato di un loop `/goal`

Risposta finale di Claude dopo il loop:

> *"Fatto. **Obiettivo raggiunto: 10 tentativi di ottimizzazione (A0–A9)**, ognuno tracciato in
> `OPTIMIZATION_LOG.md` con la modifica applicata, e lo script principale `matrix_mult.py` riscritto
> con la strategia vincente."*

**Risultati chiave (matrici 4000×4000):**

| Strategia | Best | Speedup |
|---|---|---|
| A0 Baseline NumPy @ float64 | 870 ms | — |
| A1 float32 | 433 ms | 2.0x |
| A3 float32 + out preallocato (miglior CPU) | 331 ms | 2.6x |
| A6 GPU float32, solo calcolo | 10.4 ms | 84x |
| A7 GPU float32, incluso transfer CPU→GPU | 56 ms | 15x |
| A9 GPU float16 (tensor core) | 2.7 ms | **320x** |

**Il file `OPTIMIZATION_LOG.md` prodotto dal loop** (frame-924) — è lo step 4 "OUTPUT + Memory" reso
visibile:

```
Log ottimizzazione prodotto matriciale

Matrici 4000 × 4000, mediana su 5 run (dopo warmup). Speedup calcolato sul best
rispetto alla baseline.

Hardware: CPU 8 core, GPU NVIDIA RTX 5060 Ti (CUDA), NumPy 2.2.6 + OpenBLAS 0.3.29.

 #  | Metodo                    | Mediana | Best  | GFLOP/s | Speedup | Modifica
 A0 | NumPy @ float64 (baseline)|  884.1  | 870.6 |   147.0 |    —    | Script originale, dtype float64 di default
 A1 | NumPy @ float32           |  439.1  | 432.7 |   295.8 |  2.01x  | dtype float32, meta' dati, ~2x banda memoria
 A2 | float32 + BLAS 4 thread   |  492.8  | 482.7 |   265.2 |  1.80x  | threadpool_limits=4 (core fisici, evita oversubscription HT)
 A3 | float32 + out preallocato |  428.1  | 331.4 |   386.2 |  2.63x  | np.matmul(out=...) riusa il buffer del risultato
 A4 | scipy sgemm float32       |  575.4  | 567.6 |   225.5 |  1.53x  | Chiamata BLAS sgemm diretta, salta overhead ufunc NumPy
 A5 | PyTorch CPU float32       |  391.2  | 377.9 |   338.7 |  2.30x  | torch.mm su CPU (backend ATen/BLAS)
 A6 | PyTorch GPU float32       |   12.0  |  10.4 | 12367.0 | 84.12x  | Dati residenti su GPU, sync CUDA, esclude transfer
 A7 | PyTorch GPU float32 (+tr) |   61.4  |  56.3 |  2274.0 | 15.47x  | Include copia CPU→GPU e risultato GPU→CPU
 A8 | PyTorch GPU TF32          |    6.4  |   5.5 | 23311.3 | 158.56x | allow_tf32=True: tensor core, precisione TF32
```

**Cosa il loop ha imparato da solo** (scritto nella sua risposta):

- *"float64 → float32 = 2x gratis (la doppia precisione qui non serve)."*
- *"Riusare il buffer del risultato con `np.matmul(out=...)` è il meglio su CPU (2.6x)."*
- *"Thread tuning (A2) e scipy sgemm (A4) peggiorano o scartati (OpenBLAS si gestisce già bene,
  sgemm ricopia i dati)."*
- *"La GPU stravince: il collo di bottiglia diventa il transfer CPU→GPU, non il calcolo."*

**E la scelta di prudenza che il loop ha fatto da sé** — vale come esempio di goal-verify maturo:

> *"Script finale: `matrix_mult.py` usa la GPU float32 quando c'è CUDA (precisione singola piena,
> nessun trucco tensor-core che degrada l'accuratezza), con fallback automatico a NumPy float32
> ottimizzato su macchine senza GPU. Eseguito e verificato → 4000×4000 in circa ~113 ms end-to-end
> (sulla CPU si ottiene circa 870 ms end-to-end). Nota: TF32 (A8) e float16 (A9) sono ancora più
> veloci ma riducono la precisione — non li ho messi nello script di default perché adatti al ML,
> non al calcolo numerico esatto. Se vuoi massimizzare a scapito della precisione, posso attivarli
> con un flag."*

---

## PARTE 7 — AMBIENTE E CONTORNO (dati verificati a schermo)

| Dato | Valore | Frame |
|---|---|---|
| Claude Code, versione | **v2.1.193** | frame-574 |
| Modello in Claude Code | Opus 4.8 (1M context), piano Claude Max | frame-574 |
| Account | `official.simone.rizzo@gmail.com` | frame-574 |
| Working directory | `D:\video` | frame-574 |
| Avviso MCP | *"4 MCP servers need authentication - run /mcp"* | frame-574 |
| Promo Anthropic a schermo | *"Fable 5 is back. Until July 7, you can use up to 50% of your plan's weekly usage limit on Fable 5… Fable 5 draws down usage faster than Opus 4.8"* | frame-580 |
| Modello nell'app desktop durante la demo | Opus 4.8 · Veloce · Alto, modalità Auto | frame-885 |
| Statistiche d'uso dell'autore | Sessioni 97 · Messaggi 8626 · Token totali 9.9M · Giorni attivi 18 · Ora di punta 16 · Modello preferito Opus 4.6 | frame-348 |
| Hardware della demo | CPU 8 core · GPU NVIDIA RTX 5060 Ti (CUDA) · NumPy 2.2.6 · OpenBLAS 0.3.29 | frame-924 |

---

## PARTE 8 — VUOTI DICHIARATI

1. **Non è dichiarato se `/loop` e `/goal` siano nativi di Claude Code o slash command custom.**
   Compaiono nell'autocomplete dell'installazione dell'autore con i rispettivi parametri, ma il
   video non mostra né `~/.claude/commands/` né la fonte. ➕ *Va verificato sulla propria
   installazione prima di costruirci sopra.*
2. **`/loop` non è mai mostrato in esecuzione.** L'unica demo reale usa `/goal`.
3. **Nessun dato di costo**: quanto consuma in token una sessione `/goal` da 10 tentativi non è
   detto. È esattamente la voce che a Digital Empire serve per decidere se adottarlo.
4. **Nessun criterio per il numero di tentativi**: nel video compaiono 10, 80, 100, 1000 senza
   regola che li leghi al tipo di task.
5. **Il contenuto di `program.md` di autoresearch non è mostrato** — solo citato dal README. È il
   file che conterrebbe la parte più istruttiva (come si scrive il "programma" di un loop).
6. **La lezione dell'accademia dell'autore** su "quando serve il loop engineering e quando no" è
   citata (19:05) ma non mostrata.

---

*Archiviato in Memory Empire il 2026-09-03 · run `max17-v07-rizzo-prompt` · 71 atomi in
`atoms.json` · NO-FINTO: PASS con copertura frame parziale dichiarata (133/224 scene).*
