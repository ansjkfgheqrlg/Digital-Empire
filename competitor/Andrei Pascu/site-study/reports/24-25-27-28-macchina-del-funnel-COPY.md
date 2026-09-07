---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #copy #funnel #pagine-ponte #pre-cassa #onda-b
Created: 2026-09-07
Last updated: 2026-09-07
---

# Il testo della macchina del funnel — inventario riga per riga

**Le stesse quattro catture del rapporto di costruzione** (`24-asa`, `25-define`, `27-armadeggon-strp`,
`28-outfunnel-1`, tutte 2026-09-07), lette qui non per come sono fatte ma per cosa dicono. Il
rapporto `reports/24-25-27-28-macchina-del-funnel.md` copre catene, accenti e misure in pixel — non
lo ripeto. Questo documento copre solo il testo: ogni riga, in ordine, con la funzione che svolge.

Fonte: `capture/25-define/copy-integrale.md`+`scheda.json`, `capture/24-asa/copy-integrale.md`+`scheda.json`,
`capture/28-outfunnel-1/copy-integrale.md`+`scheda.json`, `capture/27-armadeggon-strp/copy-integrale.md`+`scheda.json`.

---

## DELTA ALLA FABBRICA

**CANONE.** Il testo di un gradino si misura in *parole reali* (fuori menu, piede, legale), non in
blocchi DOM. Le quattro pagine misurate ne usano **20, 27, 36 e 3** per arrivare al clic (conteggio
in dettaglio più sotto). La soglia che se ne ricava: **una pagina-ponte non supera le 30 parole di
contenuto proprio, una pre-cassa non supera le 40, un gradino di sola-aggiunta non supera le 5.**
Sopra soglia il gradino ha smesso di spostare e ha cominciato a vendere — è nel punto sbagliato
della catena, va spostato a monte o tagliato.

**PATTERN — due, entrambi nel testo e non nella grafica.**

1. **Video-poi-bottone.** Una frase esplicita chiede di guardare il video *prima* di cliccare:
   «Ti consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.»
   (`/asa` `[y=878]`). Non accelera il click, lo *qualifica*: il pattern è testuale, riusabile ovunque
   un video introduce un passo, indipendente dal layout che lo ospita.
2. **Riafferma → istruzione → condizione.** La pre-cassa non ricomincia a vendere: riafferma l'atto
   («Stai acquistando…», `/outfunnel-1` `[y=149]`), dà l'istruzione operativa (login + dati,
   `[y=261]`), isola la natura del pagamento («Una tantum», `[y=543]`) — in quest'ordine, sempre
   prima del bottone finale.

**GATE.** Due domande nuove per il controllo copy di un gradino: **(1)** le parole di contenuto
reale restano sotto soglia (30 / 40 / 5)? **(2)** se il gradino cita una prova sociale in un link di
navigazione («Recensioni»), quel link porta a una pagina viva o a un placeholder? Su tutte e quattro
le pagine qui misurate, il link «Recensioni» del piede porta a `/presto-disponibile` — verificato in
tutti e quattro gli `scheda.json`, campo `cta`. Un link di prova sociale che punta a una pagina non
pubblicata non è un'omissione, è una bugia strutturale: il gate blocca la clonazione del pattern
finché quel link non ha una destinazione reale o non viene rimosso.

---

## L'INVENTARIO RIGA PER RIGA

Nota di metodo: ogni riga tabellata è una riga **visibile** del testo (il file `copy-integrale.md`
ricompone già i figli in linea, fix B-057 — niente buchi). Dove il DOM spezza la stessa riga visibile
in più nodi per applicare un colore a una sola parola (l'accento per prodotto, già misurato nel
rapporto di costruzione), la riga compare una volta sola qui, con l'accento segnalato in nota.

**Menu e piede sono identici, testo per testo, su tutte e quattro le pagine** (cambia solo la `y`):
tre righe di menu — «Passa al contenuto» (skip-link accessibilità), «Claude Speedrun» (link a
prodotto esterno), «Accedi» (login) — e nove righe di piede — cinque voci di navigazione (La mia
storia, Store, Recensioni, Risorse, Blog), il disclaimer legale, l'indirizzo con P.IVA, il link
privacy, il bottone cookie. **Le salto in tutte e quattro le tabelle sotto e lo dichiaro qui una
volta sola: 3 righe di menu + 9 righe di piede = 12 righe saltate per pagina, 48 in totale.**

### `/define` — «Cos'è il copywriting e come funziona?» (1.802px)

| [y] | Testo esatto | Funzione |
|---|---|---|
| 165 | «Cos'è il copywriting e come funziona?» — h1, «copywriting» in `#efab00` ambra | promessa |
| 327 | «Te lo spiego in questo video con un esempio pratico» | istruzione |
| 949 | «Scopri la strategia A.S.A» — bottone → `/asa` | azione |

Righe di contenuto proprio: **3**. Menu+piede saltati: **12** (dichiarati sopra).

### `/asa` — «Come funziona monetizzare Il copywriting come autonomo» (1.936px)

| [y] | Testo esatto | Funzione |
|---|---|---|
| 185 | «Come funziona monetizzare Il copywriting come autonomo» — h1, «monetizzare» in `#06a506` verde | promessa |
| 878 | «Ti consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.» — h3 | istruzione |
| 1073 | «Diventa un copywriter.» — bottone → `/copy-base` | azione |

Righe di contenuto proprio: **3**. Menu+piede saltati: **12**.

### `/outfunnel-1` — «outFunnel» (1.512px, la pre-cassa completa)

| [y] | Testo esatto | Funzione |
|---|---|---|
| 149 | «Stai acquistando…» — occhiello in corsivo (`em`) | promessa |
| 189 | «outFunnel» — h1, «out» in `#13989a` foglia di tè | promessa |
| 261 | «Adesso devi solo loggare nel tuo account, inserire i tuoi dati ed entrare. Ricorda di usare il codice sconto "CWSHOP" per avere il 20% di sconto.» — «CWSHOP» in `#139699` | istruzione |
| 460 | «outFunnel» — nome prodotto nella scheda prezzo | promessa |
| 500 | «98,00 €» — cifra, 35,2px | istruzione |
| 543 | «Una tantum» — condizione di pagamento | istruzione |
| 602 | «Acquista outFunnel» — bottone | azione |

Righe di contenuto proprio: **7**. Menu+piede saltati: **12**.

### `/armadeggon-strp` — il gradino di aggiunta (1.752px, nessun titolo nel DOM)

| [y] | Testo esatto | Funzione |
|---|---|---|
| 879 | «Aggiungi all'account ora» — unico bottone della pagina | azione |

Righe di contenuto proprio: **1**. Menu+piede saltati: **12**. Nessun titolo, nessuna descrizione,
nessuna cifra: il `heading` in `scheda.json` è vuoto (`"headings": []`) — confermato, non dedotto.

**Totale contenuto proprio sulle quattro pagine: 14 righe.** Totale righe visibili (contenuto +
menu/piede, contate una sola volta per riga visibile, non per nodo DOM): 15 + 15 + 19 + 13 = 62.

---

## IL RAPPORTO PAROLE/AZIONE

Parole contate per davvero, `.split()` sulla stringa esatta di ogni riga di contenuto proprio (non
menu, non piede, non legale):

| Pagina | Righe | Parole | Porta a |
|---|---|---|---|
| `/define` | 3 | **20** | bottone «Scopri la strategia A.S.A» |
| `/asa` | 3 | **27** | bottone «Diventa un copywriter.» |
| `/outfunnel-1` | 7 | **36** | bottone «Acquista outFunnel» |
| `/armadeggon-strp` | 1 | **3** | bottone «Aggiungi all'account ora» |
| **Totale catena** | **14** | **86** | — |

**86 parole** portano uno sconosciuto da «cos'è il copywriting?» fino a un account con outFunnel
aggiunto e pagato — quattro clic, quattro gradini, zero pagine di vendita vere in mezzo.

Confronto misurato, non stimato: `capture/21-outemail/scheda.json` dichiara **1.140 parole** su 24
sezioni (259 blocchi); `capture/23-vendita/scheda.json` dichiara **1.560 parole** su 18 sezioni (185
blocchi). Una sola pagina di vendita usa da 13 a 18 volte le parole che l'intera catena dei quattro
gradini usa per chiudere un acquisto. Il campo `parole` di `scheda.json` per le quattro pagine qui
studiate (che include menu, piede e legale, non solo il contenuto proprio) è comunque basso — 128
(`/define`), 135 (`/asa`), 144 (`/outfunnel-1`), 111 (`/armadeggon-strp`), **518 in tutto** — e
conferma che anche col rumore incluso la macchina resta un ordine di grandezza sotto una pagina di
vendita.

---

## LE FRASI CHE FANNO IL LAVORO

**«Ti consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.»**
(`/asa` `[y=878]`) — Perché funziona: è un h3 da 38,4px, il secondo testo più grande della pagina
dopo il titolo, e chiede esplicitamente di *spendere tempo prima di spendere soldi*. Non vende il
video, controlla il consumo: chi arriva al bottone «Diventa un copywriter.» lo fa avendo già visto
la spiegazione, quindi con un'obiezione in meno da gestire dopo. Toglierla: il bottone resterebbe lì
sotto un video muto, cliccabile da chiunque scorra la pagina senza guardare nulla — più click,
probabilmente più rimborsi e più assistenza a valle, perché il compratore saprebbe meno di cosa ha
comprato.

**«Stai acquistando…»** (`/outfunnel-1` `[y=149]`) — Perché funziona: due parole e tre puntini,
corsivo, sopra al nome del prodotto. Non ripropone l'offerta, la dà per presa: il lettore non sta
più decidendo, sta osservando cosa sta già facendo. È l'anti-ripensamento più economico possibile,
perché non contiene un solo argomento di vendita — non ce n'è bisogno, la decisione risale a una
pagina precedente. Toglierla: la pre-cassa si aprirebbe direttamente su «outFunnel» come se fosse la
prima volta che il lettore la vede, riaprendo lo spazio mentale per il dubbio.

**«Una tantum»** (`/outfunnel-1` `[y=543]`) — Perché funziona: due parole attaccate alla cifra
(«98,00 €» sopra, «Una tantum» subito sotto, 17,6px), senza una riga di spiegazione. Anticipa e
chiude l'obiezione più comune sui prodotti digitali — «è un abbonamento?» — nel punto esatto in cui
nascerebbe, cioè un istante dopo aver letto il prezzo. Toglierla: la cifra resterebbe ambigua, e
un'ambiguità sul rinnovo in un modulo di pagamento è la ragione più comune per abbandonare un
carrello prima di inserire la carta.

**«Adesso devi solo loggare nel tuo account, inserire i tuoi dati ed entrare.»** (`/outfunnel-1`
`[y=261]`, prima parte del blocco) — Perché funziona: tre verbi, tre passi, zero aggettivi. Non
motiva più — quella fase è finita altrove — dà solo la sequenza meccanica dell'azione residua. Il
verbo «devi» non è un ordine scortese, è un cambio di registro deliberato: dalla persuasione
all'istruzione operativa, lo stesso registro di un manuale. Toglierla: il lettore arriverebbe alla
scheda prezzo senza sapere che l'unico passo restante è tecnico, non decisionale — un micro-attrito
in più esattamente dove Andrei Pascu ne mette meno.

---

## LE FORMULE IN BIANCO

**Per una pagina-ponte:**

- H1: «[DOMANDA APERTA SUL PRIMO CONCETTO]?» — con **una sola parola** dell'intera frase colorata,
  il verbo o il termine che porta al passo successivo (non il nome del mestiere/argomento).
- Corpo: «Te lo spiego in questo video [DETTAGLIO CHE RENDE CONCRETO IL VIDEO]» — es. «con un
  esempio pratico», «in due minuti», «con i numeri veri».
- Gate opzionale (da usare quando il passo dopo ha un costo, in tempo o denaro): «Ti consiglio di
  vedere e finire il video prima di cliccare [NOME BOTTONE] per capirne [COSA SERVE CAPIRE].»
- CTA: «[VERBO AL PRESENTE] [OGGETTO DEL PASSO SUCCESSIVO]» — es. «Scopri [STRATEGIA]», «Diventa
  [IDENTITÀ CHE IL PASSO SUCCESSIVO COSTRUISCE]».

**Per una pre-cassa:**

- Occhiello: «Stai [VERBO GERUNDIO]…» — es. «Stai acquistando…», «Stai per iscriverti…».
- Nome prodotto in h1, con **una sola parola/prefisso** colorato — coerente con l'accento già usato
  nella pagina-ponte precedente, per continuità visiva della catena.
- Istruzione: «Adesso devi solo [AZIONE-1], [AZIONE-2] ed [AZIONE-3].» — mai più di tre verbi.
- Sconto (solo qui, mai prima): «Ricorda di usare il codice sconto "[CODICE]" per avere il [XX]% di
  sconto.» — va nella stessa riga dell'istruzione operativa, non in una riga a parte.
- Prezzo isolato: «[CIFRA] €» seguito, riga a parte, da «[Una tantum / Al mese / Ogni anno]» — mai
  una frase di spiegazione fra i due.
- CTA: «Acquista [NOME PRODOTTO]».

**Per un gradino di sola-aggiunta (upsell su account esistente):**

- Nessun titolo di testo, nessuna cifra: solo un'immagine del prodotto e un bottone.
- CTA: «Aggiungi [NOME PRODOTTO] all'account ora» — verbo «Aggiungi», mai «Acquista»: chi è qui ha
  già un account, ricordarglielo è la leva, non il prezzo.

---

## COSA NON C'E', E PERCHÉ È UNA SCELTA

Conteggio, non impressione — cercato per intero nei quattro `copy-integrale.md`:

- **Prezzo sulle pagine-ponte:** 0 occorrenze del simbolo «€» su `/define` e `/asa`. Compare solo
  su `/outfunnel-1`, cioè due gradini dopo. Deliberato: se il prezzo comparisse a `/define`, il
  lettore deciderebbe sul costo prima di aver capito cosa sta comprando.
- **Prova sociale:** 0 testimonianze, 0 citazioni, 0 loghi cliente in tutte e quattro le pagine. E
  non è solo assenza — è verificabile come scelta strutturale: il link «Recensioni» nel piede di
  **tutte e quattro** le pagine punta a `/presto-disponibile` (campo `cta` di ogni `scheda.json`).
  La pagina delle recensioni non esiste ancora: la prova sociale non manca per dimenticanza, manca
  perché il pezzo che la conterrebbe non è stato ancora costruito, e nel frattempo il link resta
  comunque nel piede — coerenza del guscio sopra la sostanza.
- **Obiezioni:** 0 frasi del tipo «non è per te se…», «so cosa stai pensando», FAQ o accordion in
  tutte e quattro le pagine. Le uniche due obiezioni gestite nel testo — abbonamento vs una tantum,
  cosa faccio dopo aver pagato — sono risolte con **una riga ciascuna** dentro la pre-cassa
  (`[y=543]`, `[y=261]`), non con una sezione dedicata.
- **Garanzie:** 0 occorrenze di «garanzia», «rimborso», «soddisfatti o rimborsati» in tutte e
  quattro le pagine — nemmeno sulla pre-cassa, dove un venditore più insicuro la metterebbe.
- **Urgenza/scarsità:** 0 countdown, 0 «offerta limitata», 0 «solo oggi».

La lettura che ne segue, e non è retorica: su un gradino, ogni elemento persuasivo che non sia
«spostati al passo dopo» è peso morto. Le pagine di vendita vere (dove tutto questo esiste, vedi
`/outemail` e `/vendita`) sono altrove nella catena — qui sarebbe ridondante, non mancante.

---

## IL DIFETTO

**Il titolo scritto male, e pubblicato in due modi diversi.** Verificato di persona sui due
`scheda.json`: il campo `titolo`/`og_title` di `27-armadeggon-strp` è **«Armageggon STRP»** (due
`g` di fila: Armag-e-ggon), mentre lo slug in `url` è **«armadeggon-strp»** (con una `d`:
Armad-eggon). Sono **due refusi diversi dello stesso nome** (`Armageddon`), uno nel `<title>` e uno
nell'URL, e non coincidono nemmeno fra loro — chi ha scritto il secondo non ha copiato il primo. Il
nome corretto non compare da nessuna parte nel documento servito. Piccolo, ma pubblico e
indicizzabile.

**Un secondo difetto, non nel rapporto di costruzione perché è di lingua, non di pixel.** L'h1 di
`/asa` — «Come funziona monetizzare Il copywriting come autonomo» — ha una maiuscola a metà frase
(«Il» capitalizzato) dove il resto del titolo è minuscolo, e ripete «come» due volte a otto parole
di distanza («Come funziona… come autonomo») in una frase che in italiano corrente si scriverebbe
«Come monetizzare il copywriting da autonomo». È il testo con l'accento di pagina più importante di
tutta la catena — l'h1 che tiene il verbo colorato «monetizzare» — scritto con meno cura del
bottone sotto.

---

## Nota di lunghezza

Il materiale è corto: **14 righe di contenuto proprio, 86 parole totali per portare al clic lungo
l'intera catena.** Questo documento pesa quanto serve a un inventario esaustivo di quel materiale,
non un carattere di più — gonfiarlo con paragrafi di contorno sarebbe un difetto peggiore
dell'essere breve. Conteggio parole di questo file: vedi risposta finale.

## Connessioni
- [[24-25-27-28-macchina-del-funnel]] — il rapporto di costruzione: catene, accenti, misure in pixel
- [[ECOSISTEMA]] — la triage T2→T3 di queste quattro pagine
- [[33-PIANO-STUDIO-TOTALE-ANDREI-PASCU]] — dove questa lettura del testo si aggancia allo studio totale
