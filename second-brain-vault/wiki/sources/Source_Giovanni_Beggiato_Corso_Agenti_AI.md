---
Type: SOURCE
Status: Active
Tags: #agenti-ai #prompt-engineering #adaptive-guardrails #prompt-contracts #pre-mortem #agent-polling #agent-debates #browser-swarm #audit #otde #n8n #claude-code #giovanni-beggiato #max18
Created: 2026-09-09
Last updated: 2026-09-09
---

# Source: Giovanni Beggiato — Corso Completo Agenti AI: le tecniche che NESSUNO ti spiega (2026)

## Overview

Corso di 1h50m20s (canale Giovanni Beggiato) — il piu' denso del lotto `max18` per numero di
atomi (228 su 5 video) — in cui l'autore costruisce dal vivo, su lavagna Excalidraw e poi in
pratica su n8n e Claude Code/Antigravity, un intero repertorio di tecniche agentiche che va
dalla teoria base (architettura di un agente, loop OTDE Observe-Think-Do-Evaluate, memoria a
quattro tipi) fino a otto tecniche avanzate di prompt engineering e orchestrazione multi-agente:
Adaptive Guardrails (correction log auto-scritto), gerarchia di specificita' dei prompt,
Step-Back Prompting, Reverse Prompting, Prompt Contracts, Pre-Mortem, Agent Polling, Agent
Debates, Browser Swarm e Audit multi-agente. Ogni tecnica viene definita su lavagna e poi
eseguita **dal vivo e per davvero** dentro il progetto di produzione reale dell'autore ("Social
Media Manager"), la cui cartella `.claude/skills/` mostrata due volte nel video (KA-036, KA-209)
contiene letteralmente una skill per ognuna delle tecniche insegnate — il corso non teorizza,
mostra il proprio codice di produzione. La tesi implicita e' che un agente AI smette di essere
un giocattolo solo quando il suo comportamento e' vincolato da contratti verificabili
(obiettivo/vincoli/formato/fallimento), corretto da un registro di regole che sopravvive tra le
sessioni, e messo alla prova da piu' menti indipendenti prima di essere eseguito.

## Dati Tecnici

- **Video ID:** JTn5pqm9ecM · **Durata:** 1h50m20s (6.620s) · **Canale:** Giovanni Beggiato
- **Copertura:** 376 scene su 376 (100%), `video-analysis.md` 1.919 righe
- **KA:** 228 atomi, 427 archi tipizzati, **1 sola componente connessa, 0 orfani**
- **Run:** `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/max18-v06-JTn5pqm9ecM`
- **Formato:** talking-head + lavagna Excalidraw disegnata dal vivo (schemi e diagrammi restano
  a schermo per intere sezioni) + screen-share denso (n8n cloud, Claude Code/Antigravity IDE,
  VS Code, browser Chrome)
- **14 capitoli ufficiali** (da `ingest-manifest.json`): Introduzione → Cos'e un agente AI →
  DEMO in n8n → Come gli agenti svolgono le task → DEMO in Claude Code → Adaptive Guardrails →
  4 livelli di specificita' → Back Prompt Engineering → Prompt Contracts → Premortem Prompting →
  Agent Polling → Agent Debates → Browser Swarm → Audit

## Cos'e' un agente AI, e la prima demo in n8n

Lo schema base costruito sulla lavagna (sei componenti: Istruzioni, Utente, Agente AI, Strumenti,
LLM, Memoria) marca il box "Istruzioni" con un cerchio arancione etichettato "IP": *"questo sarà
a livello effettivo l'unica vostra proprietà intellettuale"* — JTn5pqm9ecM#5:18-6:00 (KA-007). Il
principio guida l'intera prima meta' del corso: cio' che va scritto con cura non e' il modello
sottostante (intercambiabile) ma il prompt/le istruzioni che lo dirigono.

La teoria passa subito alla pratica in n8n cloud, dove l'autore collega un nodo AI Agent a
OpenAI Chat Model, Simple Memory e allo strumento "Send a message in Gmail". Prima esecuzione
reale: l'utente chiede di mandare un'email di saluto senza specificare testo, l'agente genera
oggetto e corpo autonomamente e la invia davvero — confermata anche sul telefono del relatore —
chiudendo con *"L'email è stata inviata a Giovanni con un saluto."* —
JTn5pqm9ecM#13:54-15:42 (KA-021). Il progetto "Social Media Manager" mostrato poco dopo come
salto di livello espone nella sidebar `.claude/skills/` un lungo elenco alfabetico che include
gia', per esteso, i nomi di quasi tutte le tecniche che il corso insegnera' nell'ora successiva:
*"agent-debates, agent-polling, audit, auphonic, browser-swarm, commit, contract, corso-skool,
deploy-check, diagram-generator, draft-to-youtube, email-digest, linkedin-post, pre-mortem,
prompt-contracts, query-anthropic, reverse-prompting, schedule-meeting, shorts, sign,
skill-creator, skool-community-replies"* — JTn5pqm9ecM#23:42-24:12 (KA-036). Il corso, cioe',
non inventa un curriculum teorico: mostra ed espande la cartella `.claude/skills/` reale
dell'autore.

## Come gli agenti svolgono i task: il loop OTDE e i quattro tipi di memoria

Il framework centrale del corso e' **OTDE — Observe, Think, Do, Evaluate** — disegnato per
intero come sei riquadri colorati in ciclo (Osserva, Memoria, Riflessione, Pensa, Agisci,
Ambiente) piu' un ottagono rosso di terminazione: il nodo Osserva *"Riceve input dall'ambiente:
messaggi utente, output strumenti, risposte API, segnali errori"*, il nodo Pensa e' dichiarato
esplicitamente **basato sul paradigma ReAct**, il nodo Agisci fa dispatch a tool esterni e
richiude il loop rientrando su Osserva — JTn5pqm9ecM#34:24-34:30 (KA-059).

Prima di arrivare a OTDE, l'autore introduce pero' un bias molto concreto: chiede all'agente di
progettare la strategia di vendita B2B migliore per se stesso, ottiene una raccomandazione
centrata su LinkedIn (dove ha gia' 50K follower), poi rifa' la stessa domanda imponendo *"come
se io partissi da zero e non avessi media presence"* e la raccomandazione cambia radicalmente
verso cold email + referral. Il principio: *"biased da cose interne a se stesso. Quindi tendono
a essere un po' pigri questi LLM"* — JTn5pqm9ecM#28:54-29:12 (KA-048). Questo bias viene poi
formalizzato nel diagramma "Memoria Semantica" (una delle quattro memorie del loop di
ragionamento agentico, assieme a episodica/procedurale/di lavoro) con un'annotazione manoscritta
"LinkedIn bias": *"E capite bene quanto sbagliato sia dire ad una persona"* che deve fare per
forza outbound senza considerare gli asset che gia' possiede — JTn5pqm9ecM#30:24-31:00 (KA-051).
Interrogato direttamente se il proprio output sia biased dai follower dell'utente, l'agente in
Claude Code ammette: *"Sì, assolutamente. Il mio output è biased dal tuo asset esistente."* —
JTn5pqm9ecM#33:18 (KA-055) — la dimostrazione pratica piu' diretta del principio.

## Adaptive Guardrails: il correction log che sopravvive tra le sessioni

Sezione piu' densa del corso in termini di materiale di produzione reale mostrato per intero.
Nel `CLAUDE.md` vero del progetto "Social Media Manager", la sezione `## Adaptive Guardrails`
recita: *"This is a living correction log. When the user corrects you, or when a wrong
assumption causes a bug, append a new entry immediately. Entries are permanent — never delete,
only supersede."* — JTn5pqm9ecM#39:54-40:00 (KA-083). Il formato di ogni voce e' fisso: *"N.
[ACTIVATION] Directive — reason."* dove ACTIVATION e' una di tre modalita' — `ALWAYS` (si applica
sempre), `NEVER` (proibizione dura), `WHEN:surface` (si attiva solo su una superficie specifica,
es. `WHEN:n8n`, `WHEN:git`) — JTn5pqm9ecM#39:54 (KA-084). Quando due voci del registro entrano in
conflitto, la risoluzione segue un ordine esplicito a tre livelli: *"When two entries clash,
apply in order:"* (1) **Supersession** — una voce che dichiara `(supersedes #N)` uccide la voce
N; (2) **Specificity** — una regola `WHEN:loom` batte una regola `ALWAYS` sui task Loom, lo scope
piu' stretto vince sempre; (3) **Recency** — a parita' di specificita', vince il numero di voce
piu' alto — JTn5pqm9ecM#40:12 (KA-086). Il relatore mostra poi il registro reale gia' popolato
con 33+ voci numerate (regole su n8n, Gemini, Skool, Loom accumulate in mesi di produzione), a
prova che non e' un esempio giocattolo.

Il meccanismo viene poi formalizzato in un "Diagramma a spirale ascendente" a due cicli:
*"DIAGRAMMA A SPIRALE ASCENDENTE: LOOP DI AUTO-MIGLIORAMENTO DELL'AGENTE AI"* — Ciclo 1
(Inizio sessione → Esegui task → Errore → Scrivi regola → Continua a lavorare → Fine sessione),
poi Ciclo 2 che **carica** la conoscenza accumulata prima di iniziare —
JTn5pqm9ecM#49:36 (KA-098). Il punto cardine, dimostrato con un esperimento live (un GEMINI.md
vuoto risponde "42" a "dammi un numero da 1 a 100"; con la regola "sempre 27" scritta nel file,
risponde correttamente anche a un prompt vocale mal trascritto): senza un file esterno
persistente si perde *"questa correzione continua"* — il continuous improvement del prompt nel
tempo — JTn5pqm9ecM#51:42-52:12 (KA-102 in relazione a KA-172).

## I quattro livelli di specificita' del prompt

Per risolvere un conflitto dal vivo (regola "24" scritta in GEMINI.md contro un prompt inline
che dice "77" — quale vince?), l'autore disegna quattro cerchi concentrici: **Global CLAUDE.md**
(viola, esterno — *"Regole globali utente, attive su TUTTI i progetti"*), **Project CLAUDE.md**
(blu — *"Regole specifiche del repo"*), **Matched Skills** (verde — *"SOP per task, caricate
on-demand"*), **Inline Prompt** (arancione, centrale — *"Istruzione specifica del momento"*), con
una freccia che punta al centro etichettata *"Più specifico = Vince"* —
JTn5pqm9ecM#53:42 (KA-104). Il principio: *"Più siamo vicini al centro, più questo prompt andrà
ad influire sull'output"* — JTn5pqm9ecM#54:12 (KA-105): l'inline batte la skill, la skill batte
il project, il project batte il global.

## Back Prompt Engineering: Step-Back Prompting e Reverse Prompting

Due tecniche gemelle raggruppate sotto lo stesso titolo *"box viola con icona a lampadina:
BACK PROMPT ENGINEERING"* — JTn5pqm9ecM#56:18 (KA-113), poi separate in due rami: **Step-Back
Prompting**, *"TECNICA DI FARE UN PASSO INIETRO PER IDENTIFICARE IL PRINCIPIO GUIDA PRIMA DI
RISPONDERE"* (refuso "INIETRO" riportato com'e' a schermo) — JTn5pqm9ecM#56:18 (KA-114); e
**Reverse Prompting**, *"TECNICA DI FAR EMERGERE LE ASSUNZIONI E PORRE DOMANDE DI CHIARIMENTO
PRIMA DI INIZIARE"* — JTn5pqm9ecM#56:18 (KA-115). La massima che chiude il primo diagramma:
*"Chi capisce il principio risolve 100 problemi."* (contro chi memorizza la soluzione e ne
risolve solo 1) — JTn5pqm9ecM#57:36 (KA-117).

Demo dal vivo: al comando `/step-back-prompting creami un bel sito web`, l'agente non produce
codice ma rifiuta la domanda superficiale e risponde con il principio guida ("un sito e' uno
strumento con un compito") e tre domande di framing (chi atterra sulla pagina, qual e' l'UNICA
azione, sotto quale brand). Applicato poi con `/reverse-prompting su questo output`, lo stesso
output produce cinque domande di chiarimento nel formato fisso Default+Perche'-conta (es. *"Q1
[...] Dove punta il CTA -- Skool direttamente o una call con te? [...] Perché conta: se punta a
una call di vendita la struttura cambia"*), chiuse da: *"Rispondimi anche con una parola per
ognuna -- 'ok' o la correzione. Poi parto."* — JTn5pqm9ecM#1:05:00-1:05:06 (KA-130). La
didascalia sotto il diagramma Reverse Prompting e' il principio cardine di entrambe le tecniche:
*"Le assunzioni invisibili sono la causa #1 di output sbagliati. Meglio 5 minuti di domande che 5
ore di lavoro buttato."* — JTn5pqm9ecM#1:03:18 (KA-128).

Invece di rispondere punto per punto, l'utente delega: *"decidi tu, eh perché questa è una demo,
però ehm aspetta prima di procedere con l'esecuzione"* — e l'agente risponde dichiarando le
cinque scelte fatte una per una, chiudendo con *"Aspetto il tuo via libera per partire."* —
JTn5pqm9ecM#1:10:24 (KA-133).

## Prompt Contracts

Introdotti per rispondere alla domanda "come definiamo il successo di un task?": quattro
componenti impilati — **OBIETTIVO** (*"Metrica di successo quantificabile"*), **VINCOLI**
(*"Limiti rigidi e confini"*), **FORMATO** (*"Forma esatta dell'output"*), **FALLIMENTO**
(*"Condizioni esplicite di fallimento"*) — che trasformano un "Compito vago: Costruisci un rate
limiter" in un "Output preciso, qualità professionale" — JTn5pqm9ecM#1:10:48 (KA-137). La
didascalia spiega perche' il quarto componente non e' decorativo: *"La clausola FALLIMENTO
impedisce all'agente di prendere scorciatoie che altrimenti razionalizzerebbe come
accettabili."* — JTn5pqm9ecM#1:10:48-1:11:24 (KA-139). Nella demo reale sulla sales page di
Avanguardia+, il contratto generato elenca nove condizioni di fallimento esplicite — non
responsive, CTA non visibile senza scroll, piu' di un file generato, testo in inglese, sezione
mancante, font < 16px, nessuna animazione, JS oltre 50 righe *"perché è una sales page, non
un'app"* — e si chiude con *"Aspetto il tuo OK per eseguire contro questo contract."* —
JTn5pqm9ecM#76:18-76:48 (KA-151).

## Pre-Mortem

*"Il post-mortem arriva troppo tardi. Il pre-mortem trova gli stessi problemi PRIMA che costino
tempo e denaro."* — didascalia sotto un diagramma a tre domande (Perche' e' fallito? / Cosa non
avevamo previsto? / Quali segnali abbiamo ignorato?) applicate a un "futuro immaginario" in cui
il progetto e' gia' fallito — JTn5pqm9ecM#77:30 (KA-154). La giustificazione economica e'
numerica: se un sistema va giu' per l'1% del tempo e un cliente arriva a comprare esattamente in
quella finestra, *"1% = 100%"* del fatturato perso per quell'occasione —
JTn5pqm9ecM#80:00-80:42 (KA-156). Applicato dal vivo alla stessa sales page di Avanguardia+ con
`/pre-mortem sull'ultimo output`, la prima causa di fallimento trovata (classificata TIGER, non
Paper Tiger) e' la piu' pericolosa perche' invisibile finche' non te la mostrano: *"Copy generica
da template -- il testo suona come ogni altra sales page AI [...] frasi che il target ha già
letto 100 volte. Il visitatore chiude in 5 secondi perché non sente la voce di Gio."* —
JTn5pqm9ecM#81:42-81:54 (KA-158). Il pre-mortem chiude senza agire da solo: offre tre opzioni
esplicite all'utente (procedi accettando i rischi / aggiungi le mitigazioni e procedi /
aggiorna il contract) — la decisione resta umana.

## Agent Polling

*"Opinioni indipendenti si rafforzano a vicenda. Opinioni di gruppo si contaminano."* — principio
scritto sotto un diagramma a cinque "Esperti indipendenti" che convergono in una fase di
Aggregazione dove *"3 su 5 concordano -> alta confidenza"* — JTn5pqm9ecM#83:18 (KA-164/KA-165).
La tecnica serve per *"decisioni strategiche o ricerche [...] che richiedono l'intervento di più
di una mente"*. Nella demo reale, la domanda *"qual è la soluzione migliore che io possa
implementare quest'anno per raggiungere 100.000 sottoscrittori su YouTube"* lancia dieci agenti
paralleli, ciascuno con un'angolazione diversa (neutral, risk-averse, contrarian,
first-principles, data-driven, systems-thinking...): *"Launching 10 agents in parallel, each
with a different analytical lens. This will cost ~$0.30-0.50 with Sonnet."* —
JTn5pqm9ecM#91:06 (KA-173). Il verdetto aggregato e' brutalmente onesto invece che compiacente:
*"All 10 agents agree: 100K by Dec 2026 is a moonshot (avg confidence 3.2/10)."* —
JTn5pqm9ecM#93:24 (KA-180) — con il problema reale identificato come distribuzione, non qualita'
dei contenuti.

## Agent Debates

*"Il sostenitore rafforza i punti deboli. Il critico riconosce i punti forti."*, con entrambi i
ruoli che *"aggiornano la propria posizione con le critiche ricevute"* attraverso tre round
espliciti, convergendo in *"SINTESI FINALE -- Il meglio di entrambe le posizioni. Nessun punto
debole sopravvive a 3 round di critica."* — JTn5pqm9ecM#94:36 (KA-184/KA-185). Lanciato dal vivo
sulle tre strategie emerse dal polling YouTube (Volume Machine / Breakout Engineer / Collab
Strategist, ciascuno con un system prompt che lo forza deliberatamente a un ruolo sbilanciato,
mai neutrale), il verdetto dopo tre round non sceglie un vincitore ma trova una sintesi
temporale: *"il sequencing conta piu della scelta della strategia [...] Tutte e tre le strategie
sono corrette -- ma applicate in fasi diverse."* — JTn5pqm9ecM#99:24 (KA-193), da cui nasce un
piano a tre mesi con un decision gate esplicito (*"Se il video proof-of-income fa < 5K views in
30 giorni, salta le collab"*).

## Browser Swarm

*"Lo stesso compito, diviso tra N browser indipendenti, finisce N volte piu in fretta."* —
principio sotto un diagramma dove un compito da 5 ore sequenziali (compilare 50 moduli) diventa 1
ora reale spalmato su 5 browser paralleli — JTn5pqm9ecM#100:06 (KA-199/KA-200). Non e' teoria:
la demo lancia davvero tre istanze Chrome su porte CDP distinte (`swarm_driver.py`) che navigano
in parallelo verso query Google diverse — *"[1] port 9223: navigating -> ...LinkedIn"*, *"[2]
port 9224: ...YouTube"*, porta 9225 per Instagram — con tutti e tre i browser completati in *"~11
secondi"* — JTn5pqm9ecM#103:48-104:00 (KA-205). L'uso pratico citato e' bypassare pagine con
autenticazione umana o consenso cookie richiesto; l'autore aggiunge pero' un disclaimer esplicito
su un caso limite (raccogliere email autenticandosi come l'utente): *"Ovviamente io non lo
raccomando."* — JTn5pqm9ecM#105:06-105:24 (KA-208).

## Audit

Tecnica di chiusura, presentata come risposta alla domanda "dopo aver usato tutte le tecniche
precedenti, come mi assicuro di aver fatto davvero bene?" — JTn5pqm9ecM#105:30 (KA-225). Tre
"ispettori" paralleli — **Codice** (*"Qualità, bug, pattern errati"*), **Configurazione**
(*"Drift, file mancanti, coerenza"*), **Sicurezza** (*"Vulnerabilità, segreti esposti,
permessi"*) — convergono in un *"REPORT UNIFICATO -- Stato di salute completo, priorità di
intervento"*, con il principio: *"Un singolo punto di vista trova solo i problemi che sa cercare.
Specialisti multipli coprono gli angoli ciechi."* — JTn5pqm9ecM#105:36-106:06 (KA-210/KA-211).
Un'annotazione manoscritta chiave, *"0 contesto!"* accanto all'Ispettore Codice, specifica che il
primo ispettore deve lavorare senza contesto pregresso del progetto, altrimenti diventa biased
dalle stesse informazioni accumulate che dovrebbe valutare in modo indipendente —
JTn5pqm9ecM#106:06-106:36 (KA-212). Il file `SKILL.md` reale della skill `audit` (git blame
conferma autore *"Giovanni Beggiato (2 months ago)"*, prova che non e' materiale costruito per il
video) dichiara: *"Catch everything -- code bugs, skill drift, broken chains, stale rules,
missing hooks, env gaps -- in one pass with 3 parallel agents. No manual checklist needed."* —
JTn5pqm9ecM#107:42 (KA-215).

## Cosa ne ricava Digital Empire

Sezione mia, dichiarata come tale: nessuna patch applicata, nessuno script toccato, nessuna
skill modificata — `EMP-QQ2R` Fase 1 resta solo studio. Confronto fatto leggendo per intero le
istruzioni operative attive di questa sessione (i CLAUDE.md caricati in questa stessa
conversazione), `emperator.md`, `PIANO-MAESTRO/15-DOSSIER-ISPETTORATO.md`, i file di memoria
`feedback_procedi_senza_chiedere.md` e `feedback_piano_criticato_tre_volte.md`, e con `Grep`
mirato su `agent-factory`, `master-build-architecture`, `sparc-methodology`, `swarm-orchestration`
— non a memoria.

**Il match piu' diretto e piu' forte di tutto il lotto max18 — Pre-Mortem e' gia' legge in DE**:
`ADR-006` (il "Ciclo di fase a 9 passi") e' testualmente RECALL → SPEC → **PRE-MORTEM** → BUILD →
GATE → REVIEW indipendente → TEST → COMMIT → RETRO — la stessa parola, lo stesso posizionamento
concettuale (prima del BUILD, non dopo), la stessa domanda-guida (*"è il giorno dopo e questa cosa
è fallita. Perché?"*, citata testualmente in `emperator.md` riga 2046, contro il *"Il task è
completato. È considerato un fallimento. Ecco le 3 cause più probabili"* di KA-157). DE applica
gia' questo principio come step obbligatorio di ogni fase di costruzione (non solo come skill
opzionale invocabile), quindi qui non c'e' gap: c'e' conferma indipendente, con DE che lo ha reso
**strutturale** (parte del metodo, non un comando a scelta) invece che facoltativo come nel corso.

**Il secondo match piu' forte — la gerarchia di specificita' dei 4 livelli e' gia' l'architettura
reale di questa sessione**: il diagramma KA-104 (Global CLAUDE.md → Project CLAUDE.md → Matched
Skills → Inline Prompt, "più specifico = vince") descrive esattamente la stessa gerarchia che
governa questa stessa conversazione — `C:\Users\Utente\.claude\CLAUDE.md` (globale), il CLAUDE.md
di root "Digital Empire" e quello annidato in `.claude/CLAUDE.md` (progetto), le skill caricate on
demand via `Skill` tool, e le istruzioni dirette date da Max in chat (inline). DE non ha mai
nominato questa gerarchia come principio esplicito da insegnare o applicare consapevolmente ai
propri agenti costruiti (mba-*, cf-*, ytf-*): la usa perche' e' l'architettura nativa di Claude
Code, ma non la sfrutta a livello di *progettazione* — nessuno skill/agent-spec in
`agent-factory` o `master-build-architecture` cerca "specificity" o "livelli" come concetto
esplicito (verificato con Grep, zero risultati). Potenziale gap operativo reale: quando due
istruzioni di agenti DE sembrano confliggere, non esiste una regola scritta di risoluzione
analoga a "più vicino al centro vince" — si risolve caso per caso.

**Adaptive Guardrails vs REGISTRO-ERRORI (Ispettorato Generale) — pattern convergente, non
identico**: `PIANO-MAESTRO/15-DOSSIER-ISPETTORATO.md` descrive un registro quasi-gemello a quello
mostrato nel corso — voci `ERR-YYYYMMDD-NNN` con sintomo/causa-radice/contromisura/owner/stato,
append-only, con un agente dedicato (`isp-recidiva-sentinel`) che confronta ogni errore nuovo col
registro e blocca con "gate ROSSO" in caso di recidiva. E' strutturalmente **piu' rigoroso** del
correction log del corso (agenti dedicati, KPI, escalation agli alti ranghi, contro un singolo
file Markdown), ma manca di un pezzo specifico che il corso rende esplicito: il protocollo di
**risoluzione dei conflitti fra regole** (KA-086: Supersession → Specificity → Recency). Il
dossier 15 dice "il registro viene consultato prima di ogni build" ma non specifica cosa succede
quando due contromisure registrate si contraddicono a vicenda su casi diversi — un gap concreto e
piccolo, facilmente colmabile prendendo in prestito lo schema a tre livelli del corso.

**Reverse Prompting vs "procedi senza chiedere" — non e' la contraddizione che sembra**: la
memoria di sessione `feedback_procedi_senza_chiedere.md` (ordine di Max, 2026-09-06) vieta le
domande di conferma: *"Non mi chiedere più niente, per qualsiasi cosa hai già un permesso,
procedi senza fermarti."* — all'apparenza l'opposto del principio del corso (*"Le assunzioni
invisibili sono la causa #1 di output sbagliati [...] meglio 5 minuti di domande che 5 ore di
lavoro buttato"*, KA-128). Ma la demo reale del corso (KA-132/KA-133) non applica il Reverse
Prompting chiedendo effettivamente all'utente: l'utente delega con *"decidi tu [...] però aspetta
prima di procedere con l'esecuzione"*, e l'agente risponde dichiarando le cinque decisioni prese
una per una prima di eseguire. Questo e' **esattamente** il pattern gia' scritto nella
`feedback_procedi_senza_chiedere.md`: *"si decide, si dichiara la decisione presa e la ragione, si
va avanti"*. Non e' un gap, e' una convalida indipendente dello stesso compromesso. La differenza
sottile e reale: il corso rende **visibile** l'elenco delle assunzioni prima di risolverle da solo
(le 5 domande Q1-Q5 compaiono comunque a schermo, con Default + Perché-conta, anche se poi
l'agente le risponde da se'); la prassi DE osservata salta direttamente alla dichiarazione delle
decisioni senza mostrare prima le domande sottostanti. Il valore che il corso attribuisce proprio
a quel passaggio intermedio (rendere visibili le assunzioni, non solo le conclusioni) potrebbe
andare perso nella forma attuale della prassi DE.

**Agent Debates vs "il piano si critica tre volte" — stessa forma, ruolo mancante**: la regola
attiva (`feedback_piano_criticato_tre_volte.md`, `emperator.md §6.20`) e' P0 il piano → P1 critica
di P0 → P2 critica **di P1** (non dell'originale) → P3 critica di P2, fino a tre giri. E'
strutturalmente il fratello maggiore di Agent Debates (round multipli, ogni round costruisce sul
round precedente, non sull'originale) ma con una differenza netta: Agent Debates istanzia sempre
**due ruoli opposti e dichiarati** nello stesso round — un Sostenitore con un system prompt che lo
forza a difendere ("Your role: Defend...") e un Critico che lo forza ad attaccare, ed entrambi
aggiornano la propria posizione — mentre la regola DE e' critica pura, sequenziale, senza un ruolo
esplicito che difenda il piano mentre viene attaccato. Rischio teorico reale che il corso rende
visibile: un elemento valido del piano puo' essere tagliato da un giro di critica semplicemente
perche' nessuno lo ha difeso attivamente, non perche' fosse davvero debole.

**Agent Polling — tecnica che DE non ha, verificato con Grep**: nessun match per
"polling"/"consensus"/"majority"/"outlier" in `swarm-orchestration/SKILL.md` ne' negli agenti
`apex-*` (planner/analyst/critic/writer/refiner/gate/meta — un'architettura a **ruoli
specializzati in pipeline**, non a **N agenti omogenei che rispondono indipendentemente alla
stessa domanda** per poi aggregare confidenza e trovare outlier). E' la tecnica del corso piu'
distante da cio' che DE gia' fa: nessun agente DE lancia oggi 10 pareri indipendenti sulla stessa
decisione strategica con un formato fisso Confidenza/Ragionamento/Avvertenze per poi leggere sia
il consenso sia l'outlier isolato. Costo dichiarato nel corso per farlo con Sonnet: $0.30-0.50 a
polling — abbastanza economico da essere un candidato concreto per decisioni ad alto rischio
(es. pricing, go/no-go di lancio) dove oggi DE si affida a un singolo ragionamento o al ciclo
P0-P3 critica-sequenziale.

**Prompt Contracts — nessun equivalente leggero per singolo task, verificato con Grep**: la
struttura GOAL/CONSTRAINTS/FORMAT/FAILURE non compare in `sparc-methodology/SKILL.md` (zero
match). DE ha `prd-architect-os` per requisiti di prodotto interi (2-30 pagine, 4 motori,
Quality Score) — uno strumento molto piu' pesante, pensato per un prodotto o una feature, non per
vincolare in due minuti una singola invocazione di agente con una clausola di fallimento
esplicita ("cosa NON e' accettabile"). Gap reale e piccolo: manca una skill leggera equivalente a
`/prompt-contracts`, usabile prima di ogni task medio (non prodotto interi) per dichiarare in 4
righe cosa renderebbe l'output un fallimento.

**Browser Swarm — gap operativo concreto per l'outreach**: la memoria di sessione descrive
l'automazione WhatsApp di Preventa come *"profilo Chromium persistente"* — un singolo browser,
non uno swarm parallelo su piu' porte CDP come mostrato in KA-205. Se lo scraping/compilazione
massiva di moduli (es. concessionari, lead) oggi gira sequenziale, la tecnica del corso (N browser
indipendenti = N volte piu' veloce, dimostrata con 3 istanze reali completate in 11 secondi)
sarebbe un candidato diretto di velocizzazione per i workflow di outreach — non verificato se gia'
tecnicamente possibile con l'infrastruttura Playwright esistente, solo segnalato come divario.

**Audit — qui DE e' avanti, non indietro**: i tre ispettori del corso (Codice/Configurazione/
Sicurezza) coprono meno terreno delle 5 Sentinelle DE gia' operative — `sentinel-drift`
(modifiche architetturali senza ADR), `sentinel-security` (segreti/credenziali esposte),
`sentinel-cost` (spesa API/dry-run), `sentinel-quality` (score APSOC, output senza proof),
`sentinel-brandvoice` (claim senza prova, tono) — piu' specializzate e granulari dei tre
ispettori generici del corso. L'unico dettaglio del corso che vale la pena verificare contro le
Sentinelle DE (non confermato in questa sessione) e' la regola *"0 contesto!"* per il primo
ispettore (KA-212): se le Sentinelle DE operano con il contesto pieno del progetto invece che a
contesto zero, potrebbero ereditare lo stesso bias da auto-riferimento gia' documentato nella
sezione memoria di questo stesso video (KA-048/KA-051) — domanda aperta, non un gap dichiarato.

**Cosa non ho verificato**: se l'infrastruttura Playwright/Chromium di DE supporti gia'
tecnicamente il multi-porta CDP necessario per un vero Browser Swarm (probabile, non testato in
questa sessione di solo-studio); se le 5 Sentinelle DE lavorino a contesto pieno o zero; se
esista gia', fuori dai percorsi cercati con Grep, un meccanismo DE equivalente ad Agent Polling in
un ecosistema non ancora ispezionato in questa sessione.

## Connessioni

- [[sources/Source_Giovanni_Beggiato_Second_Brain_Obsidian_Claude]] — stesso autore, stesso lotto
  `max18`, stesso stile di lavagna Excalidraw + demo dal vivo: quel video costruisce la company
  brain (dati/memoria), questo costruisce il repertorio di tecniche di prompting/orchestrazione
  (comportamento); letti assieme coprono la stessa filosofia di produzione applicata a due strati
  diversi dello stesso sistema agentico.
- [[Concept_Decisioni_Architetturali_ADR]] — indice degli ADR di DE, incluso `ADR-006` (ciclo a
  9 passi con PRE-MORTEM obbligatorio): il match piu' diretto e verificato di questa pagina, DE
  applica gia' come step strutturale del metodo cio' che il corso insegna come tecnica opzionale.
- [[Tool_APEX7_Core_Motore_Condiviso]] — motore di orchestrazione multi-agente condiviso di DE
  (planner/analyst/critic/writer/refiner/gate/meta): punto di confronto diretto con Agent Polling
  e Agent Debates, le due tecniche del corso piu' lontane da cio' che l'architettura APEX-7
  attuale gia' implementa (pipeline di ruoli specializzati, non fan-out omogeneo ne' dibattito
  Sostenitore/Critico a round).
- [[Tool_Nerve_Solve_Orchestration_Layer]] — il layer cognitivo di problem-solving di DE
  (postura mentale prima di risolvere qualsiasi problema): la sezione "piano criticato tre volte"
  citata in questa pagina come confronto per Agent Debates e' esplicitamente radicata in
  NERVE-SOLVE ("portato dal problema al piano"); utile leggerli assieme per capire dove DE
  gia' pratica un ciclo di critica strutturata e dove manca ancora il ruolo esplicito di
  Sostenitore che il corso invece formalizza.

