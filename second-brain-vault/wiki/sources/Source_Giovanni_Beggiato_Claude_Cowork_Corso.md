---
Type: SOURCE
Status: Active
Tags: #claude-cowork #claude-code #cowork #subagenti #skills #connectors #plugin #computer-use #dispatch #scheduled-tasks #project-instructions #giovanni-beggiato #max18
Created: 2026-09-09
Last updated: 2026-09-09
---

# Source: Giovanni Beggiato — Claude Cowork Corso Completo: Da ZERO ad Impiegato AI (in 2h)

## Overview

Corso di 1h53m31s (6811s, canale Giovanni Beggiato) organizzato in **18 capitoli ufficiali** e
interamente dedicato a **Claude Cowork**, il prodotto Anthropic per knowledge worker (non
sviluppatori) che esegue task complessi in autonomia dentro una sandbox isolata, senza terminale.
Il corso alterna quattro demo dal vivo — report CRM per un direttore vendite, riordino automatico
di fatture PDF, proposta commerciale da documentazione grezza, riadattamento di un PowerPoint con
brand guidelines — a spiegazioni teoriche su architettura (Chat vs Code vs Cowork), gestione del
contesto (Projects, Instructions locali e globali, il parallelo esplicito con `CLAUDE.md`),
sub-agenti (pipeline vs paralleli), Skills/Connectors/Plugin, e le funzioni più sperimentali
(Computer Use, Dispatch da telefono, Scheduled Tasks). **229 atomi (KA-001..KA-229), 226 archi, 18
componenti connesse, 1 solo orfano reale** (KA-164 "Guest pass", lasciato isolato di proposito).
Video 8 del lotto `max18`, checkpoint `EMP-W4K7`, studio chiuso il 2026-09-09.

## L'apertura: promessa quantificata e credenziali del relatore

Il corso apre con una promessa di produttività seguita immediatamente da una cifra concreta:
*"Cowork è uno strumento che, se imparato bene, vi permette di aumentare drasticamente la vostra
produttività."* — DI5aWJiFAt8#0:06 (KA-001) — subito quantificata: *"Task che prima vi
richiedevano 2 ore, 3 ore, li farete letteralmente in 10 minuti."* — DI5aWJiFAt8#0:18 (KA-002).
La credenziale che segue non è generica: *"Io ci gestisco consulenze per aziende che vanno da
€10.000.000 al mese fino ai 50 milioni l'anno e lo insegno anche alle persone nel mio coaching
program."* — DI5aWJiFAt8#0:24 (KA-003), relazione esplicita verso la chiusura del corso (vedi
sotto). L'obiettivo dichiarato non è generico "imparare uno strumento": è mettere lo spettatore in
grado di usare Cowork *"meglio del 99% delle persone"*, per poterlo implementare in azienda o
venderlo come servizio — DI5aWJiFAt8#2:24 (KA-005). L'indice del corso, scritto per intero su
lavagna Excalidraw, elenca **15 argomenti sequenziali** (con un salto dal punto 7 al 9, il punto 8
non compare mai a schermo) — DI5aWJiFAt8#0:36 (KA-004).

## Setup e i tre volti di Claude: Chat, Code, Cowork

Claude Cowork richiede come minimo un abbonamento **Pro**, non è disponibile nel piano Free —
DI5aWJiFAt8#3:30 (KA-007). Al momento della registrazione i piani erano: Free a $0; Pro a $17/mese
(fatturazione annuale, o $20/mese mensile) — *"Includes Claude Code and Claude Cowork"*; Max da
$100/mese con 5x o 20x più utilizzo — DI5aWJiFAt8#3:36 (KA-008).

Il cuore teorico del capitolo "Differenza Claude Chat vs Code vs Cowork" è una tabella comparativa
Excalidraw costruita voce per voce, e sono le tre definizioni più citabili di tutto il corso.
Claude (Chat): *"Una chat. Tu scrivi, Claude risponde. Non fa nulla senza che tu lo chieda."* —
DI5aWJiFAt8#4:36 (KA-010). Claude Code: *"Un assistente che lavora direttamente sui tuoi file di
codice — non solo suggerisce, ma modifica e crea file sul tuo computer."* — DI5aWJiFAt8#5:00
(KA-011). Claude Cowork: *"Come Claude Code, ma senza terminale. Accede a cartelle sul tuo
computer, legge file, crea documenti — tutto da solo, fino alla fine."* — DI5aWJiFAt8#5:42
(KA-012), pensato esplicitamente per i knowledge worker, cioè per chi non scrive codice. Sul "come
funziona" la differenza è ancora più netta: *"Descrivi il risultato che vuoi. Claude fa un piano,
lo esegue, e ti consegna il lavoro finito. Non devi intervenire ad ogni step."* —
DI5aWJiFAt8#7:18 (KA-016), contro Claude Code dove invece si può fermare l'esecuzione ad ogni
singolo passo, e Claude Chat dove è sempre l'utente a dover riprendere la conversazione.

## Demo #1 — il report vendite e la regola dell'azione "azionabile"

Dalla cartella di progetto con un solo file CSV (17 KB, 24 colonne), Cowork riceve un prompt
dettato a voce, trascritto integralmente nel corso, che chiede un report a 4 fogli con pipeline,
tassi di conversione, deal fermi da 30+ giorni e *"5 raccomandazioni per il nostro direttore
commerciale"* — DI5aWJiFAt8#13:00 (KA-028). Cowork scompone il task in una todo list visibile nel
pannello "Progress" e produce un report a 4 fogli con un tasso di conversione globale del 55,6% su
una pipeline attiva di 4.273.119 €. Il passaggio di maggior valore didattico arriva dopo: la prima
versione delle raccomandazioni viene bocciata come
*"abbastanza generiche"* — *"sarebbe un disastro perché non c'è un owner, non c'è niente"* —
DI5aWJiFAt8#16:54 (KA-037), da cui il principio esplicito: *"Ciò che rende una raccomandazione o
un'azione azionabile è che deve essere misurabile e avere un owner."* — DI5aWJiFAt8#17:54 (KA-038).
La correzione richiesta usa un formato a 4 campi — *"Azione specifica ... Nome del venditore o
della persona che deve prendere azioni ... Tempistica entro quando questa azione deve essere fatta
... Impatto stimato sulla base dei dati che trovi all'interno del CRM"* — DI5aWJiFAt8#18:42
(KA-039). Risultato finale: 5 raccomandazioni azionabili per un valore coinvolto di **1.283.727
EUR**, prodotte in pochi minuti contro le *"2-3 ore"* stimate per farlo a mano —
DI5aWJiFAt8#19:48 (KA-042).

## Come pensare con Cowork: il loop FAI-VERIFICARE-GAP

Chiusura della prima demo con un principio generale: *"il valore di Cowork [...] è tanto più
elevato per un'azienda quanto [...] più chiaro è l'obiettivo che dovete andare a raggiungere"* —
DI5aWJiFAt8#20:12 (KA-043). Il rapporto utente-Cowork viene poi disegnato come un omino che deve
raggiungere una bandiera (il goal) attraversando dei blocchi intermedi (i task delegati) —
DI5aWJiFAt8#21:12 (KA-044), da cui il ciclo operativo ricorrente di tutto il corso: *"FAI ...
VERIFICARE ... GAP ... e poi gli diremo sulla base di queste gap vai a rifare"* —
DI5aWJiFAt8#24:12 (KA-045), esplicitamente paragonato all'onboarding di un nuovo dipendente.

## La formazione AI che conta è sul processo, non sullo strumento

Argomento controintuitivo per un corso che insegna uno strumento: inseguire ogni nuova release con
un corso ad hoc ha scarsa utilità perché la tecnologia cambia nel giro di *"due settimane"* —
DI5aWJiFAt8#25:24 (KA-046). Il modello proposto in tre passi è: *"1 — MAPPARE PROCESSO, 2 —
IMPLEMENTAZIONE, 3 — FORMA[ZIONE]"* — DI5aWJiFAt8#27:48 (KA-048), motivato da un principio
generale scritto in rosso sulla lavagna: *"COSÌ È L'UNICA COSA CHE NON CAMBIA SE CAMBIA TECH?"* —
DI5aWJiFAt8#28:18 (KA-049), risposta implicita: il processo aziendale, non lo strumento. Sul flusso
di lavoro reale oggi più diffuso, il relatore dichiara un'opinione netta: *"il maggiore [R]OI che
abbiamo. Pochi sviluppi possono essere fatti"* dentro Cowork direttamente — DI5aWJiFAt8#30:00
(KA-052) — la combinazione vincente resta Claude Code per lo sviluppo + Cowork come interfaccia.

## Walkthrough della piattaforma: modelli e dettatura

Tre modelli selezionabili, ciascuno con compromesso dichiarato in interfaccia: *"Opus 4.6 — Most
capable for ambitious work ... Sonnet 4.6 — Most efficient for everyday tasks ... Haiku 4.5 —
Fastest for quick answers"* — DI5aWJiFAt8#31:36 (KA-056). La regola pratica che ne deriva: usare
Sonnet per la maggior parte dei task quotidiani e riservare Opus a codice o ragionamento
prolungato, perché l'interfaccia stessa avverte che *"Opus consumes usage limits faster than other
models"* — DI5aWJiFAt8#31:36 (KA-057). Sul trasferimento di memoria da altri provider AI, Claude
offre un flusso guidato in due passi che esporta *"tutte le memorie salvate"* dal vecchio provider
e le incolla per l'aggiunta con *"Add to memory"* — DI5aWJiFAt8#33:12 (KA-058).

## Demo #2 — le tre regole d'oro del prompt (e l'aneddoto degli 11 giga cancellati)

Task: riorganizzare fatture PDF con nomi file casuali. Il prompt integrale chiede sottocartelle per
cliente, un formato di rinomina esatto, una cartella `da-verificare` per i casi dubbi, e due
divieti espliciti (KA-064). Da questo prompt il corso estrae tre best practice
mostrate a colori sulla lavagna: **(1) Siate precisi** — *"Non ho scritto 'metti ordine' o
'pulisci'. Ho detto esattamente cosa fare [...] Più siete specifici, meno margine di
interpretazione lasciate."* — DI5aWJiFAt8#36:42 (KA-065); **(2) Dite cosa non fare** — *"'Non
cancellare niente. Non sovrascrivere.' Sembra ridondante? Non lo è."* — DI5aWJiFAt8#36:18 (KA-066);
**(3) Prevedete l'incertezza** — *"Metti in 'da-verificare' quello che non riesci a classificare.
Cowork non può sempre sapere cosa sia un file dal nome."* — DI5aWJiFAt8#38:36 (KA-069). La regola
2 viene motivata con un aneddoto citato due volte nel corso come monito diretto: *"Vi ricordate la
storia dello YouTuber che ha chiesto di 'pulire' una cartella e Cowork ha cancellato 11 giga di
file?"* — DI5aWJiFAt8#37:00 (KA-067), con la morale esplicita: *"La parola 'pulisci' lascia spazio
all'interpretazione [...] sistemare per un linguaggio di programmazione vuol dire cancellare"* —
DI5aWJiFAt8#37:12 (KA-068). Nel task reale, applicando queste regole, Cowork ha classificato 20
fatture su 3 clienti lasciando **0 file** nella cartella dubbi, senza toccare gli originali non
esplicitamente destinati alla cancellazione.

## Projects: la memoria che passa da "per chat" a "per progetto"

Il capitolo si apre con una metafora diretta sul limite di un'AI senza memoria persistente: un
collega *"con un IQ di 8 milioni"* ma da reintrodurre da zero ogni giorno — DI5aWJiFAt8#42:30
(KA-080) — da cui il principio: senza memoria tra sessioni, un'AI per quanto capace *"non porta un
ROI aziendale reale"* perché il tempo per rifare l'onboarding annulla il vantaggio —
DI5aWJiFAt8#42:42 (KA-081), verificato dal vivo chiedendo a un task già concluso se ricordasse il
proprio lavoro passato: la risposta è che ogni sessione riparte sempre da zero, senza eccezioni.
"Projects" risolve questo limite
spostando la memoria *"da una memoria che va per chat ad una memoria che va per progetto"* —
DI5aWJiFAt8#43:18 (KA-083). La regola operativa per chi lavora con più clienti è netta: un progetto
per cliente, mai mescolare — *"dividete i vari clienti come se fossero un progetto a [sé] stante"*
— DI5aWJiFAt8#45:48 (KA-088), preferendo questa organizzazione a quella per funzione aziendale
perché *"altrimenti vi esplode l'universo"* — DI5aWJiFAt8#49:24 (KA-094): ogni progetto è un silo
indipendente, dimostrato creando un secondo progetto vuoto e verificando che la domanda posta al
primo progetto non trapeli nel secondo.

## Global Instructions e il parallelo esplicito con CLAUDE.md

Sopra le istruzioni di singolo progetto esiste un livello unico per l'intero account, le "Global
instructions" — DI5aWJiFAt8#50:36 (KA-096) — verificate con un test diretto: dopo aver scritto a
livello globale *"il mio colore preferito è il verde"*, la domanda ripetuta in due progetti isolati
tra loro produce la stessa risposta identica, *"Il tuo colore preferito è il verde"* —
DI5aWJiFAt8#53:42 (KA-099), a dimostrazione che le Global Instructions attraversano i silos di
progetto mentre le istruzioni locali no. Il corso rende poi esplicito, per chi già conosce Claude
Code, un doppio parallelismo: `CLAUDE.md` di progetto sta alle "Project Instructions" locali di
Cowork, come il "Global CLAUDE.md" sta alle "Global Instructions" di Cowork — DI5aWJiFAt8#56:24
(KA-110). Un `CLAUDE.md` ben scritto, mostrato integralmente in editor, si organizza in tre sezioni
— *"## WHAT ... ## HOW ... ## WHY"* — DI5aWJiFAt8#54:12 (KA-101). Il livello globale personale del
relatore contiene anche regole di stile molto specifiche e insolite per un file di configurazione
(fino al divieto letterale dell'em-dash nel testo generato, KA-107). Sul perché scrivere regole
"DOs & DON'Ts" abbia valore, la metafora
usata è quella di uno schermo di dimensioni limitate su cui si può delimitare in anticipo una
"zona rossa" da evitare —
*"nella 1000 soluzioni che tu puoi fare [...] questa parte qui evitala perché so già che non va
bene"* — DI5aWJiFAt8#57:36 (KA-114) — collegata al concetto di token come *"moneta"* di ogni
interazione, il cui spreco costa *"tempo e denaro"* — DI5aWJiFAt8#58:06 (KA-115).

## Demo #3 e i subagenti: pipeline contro parallelo

Prima di generare una proposta commerciale, l'istruzione esplicita è: *"Per favore, prima di
procedere, leggi tutta la documentazione che hai a disposizione."* — DI5aWJiFAt8#62:18 (KA-120),
seguita dal principio metodologico di far sempre fare a Claude un giro di brainstorming di opzioni
alternative prima di produrre un deliverable definitivo (KA-123). Il capitolo
dedicato ai subagenti introduce il concetto con una lavagna: quando una task è difficile, *"quello
che Cowork fa sostanzialmente è spezzare questa task in più agenti"* — DI5aWJiFAt8#67:42 (KA-126),
ciascuno dei quali *"riparte con contesto vuoto"* perché tecnicamente è una nuova conversazione,
senza ereditare la cronologia del subagente precedente — DI5aWJiFAt8#69:12 (KA-128). La distinzione
Pipeline vs Parallelo viene quantificata con un esempio numerico esplicito: tre step da 5, 5 e 2
secondi in sequenza (pipeline) sommano **12 secondi totali**; eseguendo i due step da 5 secondi in
parallelo il tempo scende a **7 secondi** — DI5aWJiFAt8#72:18 (KA-132), da cui il consiglio
operativo di scrivere prompt "ingegnosi" che sfruttino il parallelismo quando possibile —
DI5aWJiFAt8#72:24 (KA-133).

## Skills: cosa sono davvero, e la Demo #4 col brand-guidelines

Definizione minima e volutamente sgonfiante: *"vedete che queste skill non sono altro che dei
semplici file in cui noi andiamo a dare delle specifiche di che cos'è che vogliamo fare"* —
DI5aWJiFAt8#77:54 (KA-140), confermata a livello di sistema quando Cowork crea davvero una skill:
il comando eseguito è un semplice `mkdir -p .../.claude/skills/saluto` — DI5aWJiFAt8#83:36
(KA-153) — con l'avvertimento pratico che se la cartella di sistema è in sola lettura, la skill va
salvata altrove e poi copiata a mano dentro `~/.claude/skills/`. Sul valore economico della skill
come asset riusabile, il principio è netto: *"la parte difficile
[...] è creare questa skill, ma una volta creata l'utilizzo è estremamente semplice"* —
DI5aWJiFAt8#81:36 (KA-150), dimostrato nella Demo #4 applicando la skill nativa `brand-guidelines`
a un PowerPoint cliente — non prima di un avviso che le uniche linee guida disponibili sono quelle
di Anthropic stessa, non del cliente (KA-147) — con colori e font specifici: *"sfondo scuro (quasi
nero) #141413 ... Sfondo chiaro #FAF9F5 (crema) ... Font: Poppins per tutti i titoli ... Lora per
il corpo del testo"* — DI5aWJiFAt8#81:00 (KA-148).

## Comandi, Connectors, Plugin

Un dettaglio tecnico non ovvio: comando e skill si invocano nello stesso identico modo (il simbolo
"/"), ma concettualmente sono cose diverse — *"quando parliamo di skill, noi parliamo di un file
[...] scritto in markdown [...] Quando parliamo di un comando, parliamo di una serie di istruzioni
che sono già state automatizzate"* — DI5aWJiFAt8#90:30 (KA-178). I "Connectors" collegano Claude
alle app già in uso (Canva, Drive, Gmail, Calendar, GitHub) — DI5aWJiFAt8#93:42 (KA-190) — mentre i
"Plugin" impacchettano skill, comandi ed eventuali connector in un unico insieme installabile; il
catalogo ufficiale Anthropic li organizza per funzione aziendale, e il plugin "Sales" da solo
bundla **9 skill e 14 connector** via Model Context Protocol — DI5aWJiFAt8#100:42 (KA-202).

## Computer Use e Dispatch: i limiti dichiarati dall'autore stesso

"Computer Use" è la modalità in cui Claude prende il controllo reale di mouse e tastiera —
*"Cloud sta cliccando letteralmente con il mio mouse"* — DI5aWJiFAt8#107:00 (KA-213), attivabile
anteponendo o posponendo la frase letterale "computer use" alla richiesta. Il relatore ne dà un
giudizio esplicito e non celebrativo: *"richiede il computer sempre acceso, l'app sempre
funzionante e aperta ed inoltre non potete fare grandi altre cose con il computer"* —
DI5aWJiFAt8#107:00 (KA-216) — giudicandolo ancora troppo acerbo per un uso aziendale serio.
"Dispatch" estende questo controllo al telefono — *"Dispatch to Claude and check in from
anywhere—a task, a code session, in one continuous thread."* — DI5aWJiFAt8#109:18 (KA-220) — ma
eredita lo stesso limite: il computer deve restare acceso perché tutto funzioni, dichiarata dallo
stesso relatore come la limitazione più grande del sistema allo stato attuale.

## Chiusura

Il corso si chiude con una doppia call-to-action che riporta esplicitamente alla credenziale di
apertura (KA-003): un coaching program 1-1 per *"cominciare a vendere questi servizi nei prossimi
90 giorni"* e una risorsa separata per chi vuole applicare la tecnologia direttamente nella propria
azienda — DI5aWJiFAt8#113:30 (KA-229).

## Cosa ne ricava Digital Empire

Sezione mia, dichiarata come tale: nessuna patch applicata, nessuno script o skill toccati — Fase 1
resta solo studio. Confronto fatto con `Grep` mirato su `company/Memory/`, `.claude/` e
`second-brain-vault/wiki/`, non a memoria.

**Scoperta principale — DE ha già studiato Claude Cowork, ma da un corso diverso e molto più
superficiale**: tre pagine stub esistono già — [[Source_CS2_Bonus_05_Projects_Cowork]] (Projects in
Cowork: memoria persistente, file allegati, cartella device), [[Source_CS2_Bonus_06_Automatizzare_Skills_FINALE]]
(SOP → skill Obsidian, pattern "rifiutati se mancano dati obbligatori") e
`Source_CS2_Bonus_03_Collegare_Claude.md` (MCP, Connectors, Zapier, scheduling Cowork) — tutte e tre
dal corso a pagamento **"Claude Speedrun 2" di Andrei Pascu**, ingerite il 2026-08-29. Sono pagine
di 19-22 righe che rimandano al contenuto grezzo senza svilupparlo (nessuna citazione letterale,
nessun timestamp, nessun KA numerato nel corpo della pagina). Questo video di Beggiato copre lo
stesso prodotto con un ordine di grandezza di profondità in più (229 atomi contro pagine che non
enumerano nemmeno gli atomi grezzi) e aggiunge interi capitoli che quelle pagine non toccano affatto:
il parallelo esplicito Project Instructions↔CLAUDE.md e Global Instructions↔Global CLAUDE.md
(KA-110), il loop FAI-VERIFICARE-GAP (KA-045), la distinzione quantificata pipeline vs parallelo
per i subagenti (KA-132), e Computer Use/Dispatch (non menzionati nei tre stub CS2).

**Conferma cross-fonte su un gap già segnalato ma non ancora chiuso**: la pagina
`Source_CS2_Bonus_06_Automatizzare_Skills_FINALE.md` registra esplicitamente un gap in
`beast-preventivi` — assenza del pattern "rifiutati se mancano dati obbligatori" — dichiarandolo
*"NON applicato, serve conferma cross-fonte (3 occorrenze finora tutte nello stesso corso)"*.
Questo video, di un **corso e canale diversi**, contiene un principio strutturalmente identico:
*"Non proporre mai soluzioni senza dati a supporto. Se non hai un dato, dillo — non inventarlo."*
— DI5aWJiFAt8#50:30 (KA-091), regola scritta esplicitamente nelle Instructions di un progetto-
cliente. Verificato con `Grep` mirato (`rifiut|missing.data|dati obbligatori`) dentro
`.claude/skills/beast-preventivi/`: **zero occorrenze**, il gap è confermato reale e ora ha una
quarta conferma indipendente, non più solo interna allo stesso corso a pagamento. Non ho applicato
la patch (fuori perimetro Fase 1): la porto qui come raccomandazione pronta per chi lavora su
`beast-preventivi`.

**Cosa DE non ha ancora, verificato come vuoto reale**: nessuna pagina wiki esistente documenta il
ciclo **FAI-VERIFICARE-GAP** (KA-045) come principio operativo esplicito per delegare lavoro a un
agente autonomo — il concetto più vicino in wiki è il ciclo Empire a 9 passi
(RECALL→SPEC→PRE-MORTEM→BUILD→GATE→REVIEW→TEST→COMMIT→RETRO, `PIANO-MAESTRO/10-METODO-CICLO-FASE.md`),
che è più elaborato ma copre lo stesso bisogno di fondo (delegare, verificare, correggere) con un
linguaggio diverso — non li ho fusi, li segnalo come imparentati. Allo stesso modo, la distinzione
quantificata "pipeline vs parallelo" per i subagenti (KA-130-133, esempio 12s→7s) non ha un
equivalente numerico in [[Source_Riccardo_Belli_Risparmiare_Token_Claude_Code]], che pure tratta i
subagenti a lungo ma sul solo asse del costo in token ("i sub-agenti spostano il conto invece di
ridurlo"), mai su quello del tempo di completamento in parallelo — le due fonti si completano, non
si sovrappongono.

**Cosa non ho verificato**: se le demo del corso (report vendite, riordino fatture, proposta
commerciale, PowerPoint con brand guidelines) corrispondano a servizi che Digital Empire offre già
ai clienti in una forma equivalente. Ho cercato riscontri diretti e non ne ho trovati nella wiki né
in `.claude/skills/` oltre a `beast-preventivi` (preventivi, non proposte commerciali generiche) e
`client-handover`/`delivery-playbook` (consegna, non produzione di report interni per il cliente):
non è un gap che dichiaro chiuso né aperto con certezza, è un'area che richiede una lettura mirata
di `company/01-agency` che questa sessione di studio non copriva.

## Connessioni

- [[Source_CS2_Bonus_05_Projects_Cowork]] — stesso prodotto (Claude Cowork), stesso concetto
  (Projects come memoria persistente), ma da un corso diverso (Claude Speedrun 2, Andrei Pascu) e
  con una profondità molto minore: questa pagina espande a piena citazione ciò che lì è solo
  accennato in 3 righe.
- [[Source_CS2_Bonus_06_Automatizzare_Skills_FINALE]] — stesso concetto (Skills come file SKILL.md,
  pattern "rifiutati se mancano dati"), e la pagina dove nasce il gap su `beast-preventivi` che
  KA-091 di questo video conferma indipendentemente (quarta occorrenza, primo corso diverso).
- [[Source_Giovanni_Beggiato_Company_Brain_Karpathy]] — stesso autore, stesso lotto `max18`: quel
  video tratta la memoria persistente lato Claude Code/Company Brain (LLM Wiki di Karpathy,
  regola "nessuna proposta senza nota"), questo la tratta lato Cowork/Projects — la stessa
  ossessione dell'autore per "mai inventare un dato" attraversa entrambi i video (KA-091 qui,
  regola *single source of truth* là).
- [[Source_Giovanni_Beggiato_Second_Brain_Obsidian_Claude]] — stesso autore, stesso lotto `max18`,
  stesso principio del parallelo CLAUDE.md-come-indice applicato su due prodotti diversi (Claude
  Code nel corso Second Brain, Cowork/Projects qui).
- [[Source_Riccardo_Belli_Risparmiare_Token_Claude_Code]] — stesso lotto `max18`, stesso argomento
  tecnico (subagenti, `CLAUDE.md`, gestione del contesto) osservato però sull'asse costo-in-token
  invece che tempo-di-completamento: le due fonti si completano senza sovrapporsi, vedi nota sopra.
