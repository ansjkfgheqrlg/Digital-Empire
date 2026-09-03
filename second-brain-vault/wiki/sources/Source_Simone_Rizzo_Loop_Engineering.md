---
Type: SOURCE
Status: Active
Tags: #prompt-engineering #context-engineering #harness-engineering #loop-engineering #claude-code #simone-rizzo #max17 #agenti-autonomi #verifica-automatica
Created: 2026-09-03
Last updated: 2026-09-03
---

# Source: Simone Rizzo — "Se usi ancora i prompt... devi vedere questa evoluzione" (Loop Engineering)

## Overview

Video di 31m23 (IT, batch `max17` v07) in cui l'autore ricostruisce una pila a quattro livelli
— **Prompt Engineering → Context Engineering → Harness Engineering → Loop Engineering** — dove
ogni strato nasce per risolvere il fallimento dello strato precedente. Il contenuto che vale per
Digital Empire non è la tassonomia in sé (gli strati 1-3 sono già in gran parte coperti da
`guild-prompt`, `prompt-engegniring-skill`, `nerve-solve`), ma il **quarto strato**: la sintassi
concreta di due comandi Claude Code (`/loop`, `/goal`) e — soprattutto — i **5 Livelli di
Verifica**, una tassonomia che dice esplicitamente *quanto ci si può fidare* di un ciclo
autonomo prima che serva un umano nel giro. Chiuso a valle di uno stop di sessione: la visione
dei frame e l'analisi erano già complete su disco (`video-analysis.md`, 922 righe, 133/224 scene
coperte), mancavano solo wiki, Memory Empire e i consigli.

## Dati Tecnici

- **Video ID:** BSUHmVcaO1g
- **Durata:** 31m23s (1883s)
- **Canale:** Simone Rizzo (account Claude Max visibile a schermo: `official.simone.rizzo@gmail.com`) · **Lingua:** IT
- **Formato:** Talking head + lavagna Figma/FigJam disegnata a mano + screen-share (app Claude desktop, Claude Code in terminale, GitHub, docs OpenClaw)
- **Frame:** 942 densi @2s → 224 unici sopra soglia (scene-detector 3.0, riduzione 76.2%) | **Frame letti: 176/942 (18,7%), 133/224 scene (59,4%)** | NO-FINTO: **PASS con copertura parziale dichiarata** — nessun capitolo del video resta scoperto, i frame non aperti sono quasi tutti stati intermedi dello stesso disegno a mano libera fra due frame guardati. Dettaglio blocco per blocco in `coverage.md`. Recupero critico fuori-`scenes.md`: il rilevatore aveva collassato 128s di digitazione dal vivo (i comandi `/loop`/`/goal` e il goal della demo) in un solo frame ciascuno — recuperati 74 stati di digitazione con un diff RMS mirato sulla riga di comando, altrimenti la sintassi esatta si sarebbe persa.
- **KA:** 71 (atoms.json)
- **Processing:** pipeline Empire Studio (sessione precedente, visione+analisi) · Memory Empire Stage C-H 2026-09-03 (questa sessione, dopo interruzione per limite di sessione)
- **Run:** `empire-studio/runs/max17-v07-rizzo-prompt`

## Il Principio — I Quattro Livelli, e Perché il Quarto Conta

```
PROMPT              CONTEXT              HARNESS              LOOP
Engineering          Engineering           Engineering          Engineering
────────────         ──────────────        ──────────────       ──────────────
Il system prompt:    Quali tool, quanto    L'impalcatura:       Il trigger, il goal
identità e           contesto, come        sottotask + file     verificabile e la
istruzioni           comprimerlo           markdown come        condizione di
                                            memoria persistente  terminazione
     |                     |                      |                    |
     v                     v                      v                    v
"di che colore è     context rot: oltre    serve comunque un    fallisce quando il
fatta la ferrari?"   ~200k token le        umano che rilanci    goal non è
(nessun tool)         performance          e giudichi ogni      verificabile in
                      crollano              giro                automatico
```

Le tre prove pratiche mostrate a video con lo stesso brief (*"di che colore è fatta la
ferrari?"* → *"come si chiama l'ultimo modello Ferrari?"* → *"clonami il sito Ferrari così
com'è"*) rendono visibile il salto: nessun tool → tool per informazioni fresche → richiesta
troppo grande per un solo giro di contesto, va spezzata in sottotask. Il Loop Engineering non è
un quinto strato indipendente — è **"un loop sopra un loop sopra un loop"**: il tool-use dentro
l'LLM è già un loop, l'harness che cicla sui sottotask è un secondo loop, il Loop Engineering
prende tutto questo insieme e lo mette dentro un terzo loop, quello che decide da solo quando
ripartire.

## I Due Comandi — Sintassi Esatta

```
/loop [interval] [prompt]
/goal [<condition> | clear]
```

Letta carattere per carattere dall'autocomplete di Claude Code (frame-590, frame-620) e
verificata sui 74 stati di digitazione recuperati fuori dall'elenco automatico delle scene — la
trascrizione automatica del parlato rendeva `/goal` come *"slg"* o *"gol"*, un comando
inesistente: **vale il frame, non l'audio**.

**Anatomia di un `/goal` — quattro pezzi in una riga sola**, dalla demo reale (28:48):

```
/goal migliora i tempi impiegati per fare il prodotto fra matrici in questo script
python, ad ogni test che fai scrivilo su di un file markdown scrivendo anche in
breve le modifiche fatte per avere tracciabilità | fai al massimo 10 tentativi di
ottimizzazione
```

1. **obiettivo misurabile** — "migliora i tempi impiegati..."
2. **perimetro** — "in questo script python"
3. **memoria/tracciabilità obbligatoria** — "scrivilo su un file markdown"
4. **condizione di terminazione dopo la `|`** — "fai al massimo 10 tentativi"

**La regola più importante del video**: senza la condizione di terminazione dopo `|`, un
obiettivo impossibile (es. "sotto i 100 millisecondi" quando non è raggiungibile) produce **un
ciclo infinito che consuma token indefinitamente**. La seconda regola: il goal deve essere
**valutabile dall'agente stesso** — "che sia virale" non è un goal, "che raggiunga 300 reazioni"
lo è.

## I 5 Livelli di Verifica — il pezzo di maggior valore operativo

Trascritti integralmente dai frame-648/800/829 (slide più densa del video):

| # | Livello | Cosa verifica | Esempio dal video |
|---|---|---|---|
| 1 | **Deterministico** | asserzioni di codice, exit 0, schema, golden output match | "deve compilare senza errori" — booleano |
| 2 | **Regole/vincoli** | conteggio caratteri, contiene X, lint, policy | "sotto i 100ms", "accuratezza sopra il 90%" — numerico, non booleano |
| 3 | **Verità terrena (ritardata)** | test passati, deploy, risposta cliente, engagement | "300 reazioni su LinkedIn" — il risultato matura in 2-3 giorni, si usa `/loop` a cadenza, non `/goal` a tentativi |
| 4 | **LLM come giudice** | secondo modello valuta contro una rubric — non è verità terrena | cloning UI: l'agente si autogiudica la somiglianza (0,30 → 0,90) fra render e screenshot originale |
| 5 | **Checkpoint umano** | supervisione, NON verifica automatizzata | "sei tu che guardi ogni modifica e dai uno score" |

I livelli 1-3 sono dichiarati **"ciclo autonomo vero"**; i livelli 4-5 sono **"flusso assistito,
umano nel ciclo"**. La frase esatta a schermo: *"Conosci quale il tuo gate usa davvero."* — è
una domanda che oggi nessun agente/skill di Digital Empire si pone esplicitamente prima di
lanciare un ciclo autonomo.

## La Demo Reale — cosa produce davvero un loop

Baseline: script Python di prodotto fra matrici, misurato a 870ms (4000×4000, float64, CPU). Il
goal (vedi sopra) lancia 10 tentativi di ottimizzazione (A0-A9), ognuno tracciato per intero in
un file `OPTIMIZATION_LOG.md` — trascritto integralmente in `video-analysis.md` — con mediana,
best, GFLOP/s, speedup e la modifica applicata per ciascuno. Risultato finale: **320x più
veloce** (2,7ms, GPU float16 tensor core) rispetto alla baseline, con motivazione esplicita del
perché la versione più veloce (TF32/float16) *non* è quella lasciata come default nello script
finale — riduce la precisione, adatta al ML non al calcolo numerico esatto. Questo è l'unico
punto del video in cui si vede un ciclo dei livelli 1-2 (deterministico + regola numerica)
girare fino alla condizione di terminazione senza intervento umano nel mezzo.

## Il Caveat Onesto — la parte che il video non nasconde

L'autore stesso, citando Boris Cherny e Peter Steinberger ("io non scrivo più prompt, faccio
solo loop"), dichiara il limite: *"funziona molto bene a loro due perché loro due sono
sviluppatori... è verificabile questo task. Ma in altri casi questo approccio va visto nel
dettaglio, perché ci sono cose in cui non è verificabile in automatico, non è deterministico, e
quindi bisogna che noi facciamo da giudici, o l'LLM fa da giudice, oppure bisogna metterci noi ad
avere più controllo."* (26:52–27:55) — coerente con la tassonomia a 5 livelli sopra: il loop
autonomo vero vive solo ai livelli 1-3.

## Key Quotes

> "Siamo passati dal prompt Engineering al Context Engineering all'Harness Engineering che è
> durato veramente poco e adesso già siamo entrati in questa nuova era del Loop Engineering."

> "Prendiamo tutto questo e lo mettiamo dentro un altro loop, un loop su loop sul loop. Questo è
> il loop engineering."

> "Perché mettiamo quest'altra condizione? Perché mettiamo il caso che gli abbiamo chiesto un
> qualcosa di impossibile... entra in un ciclo infinito e ci fa consumare tanti tanti token."

> "Conosci quale il tuo gate usa davvero." [testo a schermo, sui 5 Livelli di Verifica]

## Consigli (Stage 8 — proposte, NON applicate in questa sessione)

Coerente con la regola "Consigliare sempre dopo ogni studio": questi sono suggerimenti concreti,
non patch già scritte. Verificato prima di proporli che il gap è reale — nessuna delle due
sezioni sotto esiste oggi nei file citati.

1. **`.claude/agents/guild-prompt.md`** (363 righe) — governa lo standard dei prompt in tutto
   l'Impero, ha una sezione "⚠️ VUOTI DI CONOSCENZA DICHIARATI" già aperta (punti 1-4) ma non
   nomina mai Harness/Loop Engineering. Proposta: una sezione aggiuntiva che registri (a) la
   sintassi `/loop`/`/goal` **da verificare sulla propria installazione** (il video non dice se
   sono nativi o custom — vedi vuoto sotto), (b) i 5 Livelli di Verifica come griglia per
   giudicare se un agente Empire che gira in autonomia (es. le sentinelle di Empire Studio
   stesse) sta operando a un livello 1-3 (autonomo vero) o 4-5 (serve un checkpoint umano
   esplicito, non solo implicito).
2. **`.claude/skills/prompt-engegniring-skill/SKILL.md`** (114 righe) — ha già una sezione
   "GOLDEN PROMPT STRUCTURE (Template per PROMETHEUS)"; il template **"The Anatomy of a Claude
   prompt"** trascritto integralmente in questo video (Task · Context Files · Reference ·
   Success Brief · Rules · Conversation · Plan · Alignment — con le tre mosse operative "stop se
   stai per rompere una regola", "chiedi prima di eseguire", "elenca le 3 regole più importanti
   prima di iniziare") è un template diverso e complementare, riusabile con placeholder.
3. **Uso interno immediato, senza patch**: la griglia dei 5 Livelli si presta a un audit rapido
   dei processi che già girano da soli in Digital Empire (Empire Studio stesso, Ultimo Metro,
   Tesoreria-previsione) — nessuno di questi dichiara oggi esplicitamente su quale livello opera
   il proprio gate. Non proposto come patch perché serve prima una scelta di Max su dove vive
   quella dichiarazione (per-agente in `failure-modes.md`, o un campo nuovo in ADR).

**Nessuna patch scritta in questa sessione.** Il perimetro di questo lavoro (vedi
`company/Memory/riprese/EMP-QQ2R.md`) era chiudere il video fino alla wiki con i consigli, non
modificare skill/agenti condivisi mentre altre due sentinelle lavoravano in parallelo sullo
stesso repo.

## Nota di trasparenza — limiti della fonte (dichiarati dal video stesso)

- **Non è chiaro se `/loop` e `/goal` siano comandi nativi di Claude Code o slash command custom**
  dell'installazione dell'autore — il video non mostra `~/.claude/commands/` né la fonte. ➕
  *Inferenza non verificata: chi vuole replicare deve controllarlo sulla propria installazione
  prima di costruirci sopra.*
- **`/loop` non è mai mostrato in esecuzione** — la demo reale usa solo `/goal`.
- **Nessun dato di costo**: quanti token consuma una sessione `/goal` da 10 tentativi non è
  detto — è esattamente il dato che servirebbe a Digital Empire per decidere se adottarlo.
- **Nessun criterio per il numero di tentativi**: 10, 80, 100, 1000 compaiono in esempi diversi
  senza una regola che li leghi al tipo di task.
- **Il contenuto di `program.md`** (repo `karpathy/autoresearch`, citata come precedente storico
  del Loop Engineering) non è mostrato, solo citato dal README.

## Connessioni

- [[Source_Jay_E_Agentic_OS_Claude5]] — stesso batch `max17`, stesso dominio (context/agentic OS
  su Claude Code); Jay E costruisce un framework proprietario (ARMS) sopra funzioni Claude Code
  reali, Rizzo costruisce una tassonomia di livelli sopra due comandi Claude Code reali — stesso
  pattern editoriale, contenuti complementari e non sovrapposti.
- [[Source_CS2_Lezione_08_Context_Engineering]] — stessa distinzione di base (context engineering
  come costruzione dell'input, distinto dal prompt engineering come solo testo della richiesta);
  questo video la estende con due livelli in più (Harness, Loop) che la Lezione 8 non copre.
- [[concepts/Concept_Guardrail_Che_Si_Fanno_Rispettare]] — stesso principio da un'angolazione
  diversa: un `/goal` senza condizione di terminazione è esattamente "una regola che dipende
  dalla buona volontà" del sistema di fermarsi da solo — la condizione dopo `|` è il guardrail
  che si fa rispettare da solo, applicato al singolo comando invece che al processo.
- [[tools/Tool_Nerve_Solve_Orchestration_Layer]] — NERVE-SOLVE è il primo dei 3 orchestration
  layer previsti per il Modello Internet Artificiale DE; i 5 Livelli di Verifica di questo video
  sono un candidato diretto come griglia di classificazione per qualunque ciclo che quel layer
  o i layer successivi mettano in autonomia.
