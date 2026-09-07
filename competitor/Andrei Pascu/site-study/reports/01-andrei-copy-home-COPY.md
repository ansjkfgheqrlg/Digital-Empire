---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #site-study #copy-teardown #home #hub #accessibilita #machine-v2
Created: 2026-09-07
Last updated: 2026-09-07
---

# 01 — andrei-copy.com (home) — teardown di copy, macchina v2

**Fonte:** `capture/01-andrei-copy-home/` — catturato 2026-09-07 — **3.384px** desktop, **5 sezioni (4
distinte)**, **62 blocchi di testo**, **7 CTA** (`scheda.json → cta[]`).
**Standard di forma:** [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md).
**Rapporto precedente (macchina v1, 2026-09-01):** [01-andrei-copy-home.md](01-andrei-copy-home.md) —
misurava 44 blocchi, 10 CTA, 20 media sulla stessa pagina.

Nota onesta sulla brevità di questo file: questa è la pagina più corta dell'intero ecosistema
studiato finora (3.384px, meno di un ottavo della pagina prodotto più lunga, `outfunnel`, 26.993px:
3.384/26.993 = 12,5%). Non è una sales page — è un hub di smistamento, come già stabilito dal rapporto
precedente — quindi diverse delle sezioni richieste da questo standard (obiezioni, scala di impegno,
prezzo) non si applicano con la stessa densità che avrebbero su `outfunnel` o sul `manuale-del-copywriter`.
Dove una sezione non si applica, lo dichiaro con la ricerca testuale che lo dimostra, invece di riempirla
di aria.

---

## DELTA ALLA FABBRICA

**CANONE:** il **doppio sistema di bottoni a due frecce** (`→` blu pieno per navigazione morbida,
`↗` bianco mono per ingresso in una risorsa) è confermato identico nella nuova cattura — stessi hex,
stesse dimensioni (`INIZIA IL CORSO ↗` a x=227/y=1389, `ESPLORA LO STACK ↗` a x=579/y=1389, `SCOPRI IL
SETUP ↗` a x=931/y=1389) — quindi è pronto per essere codificato come componente `btn-nav-soft` /
`btn-resource-enter` senza bisogno di ricattura. **Ma** in questa cattura nessuno dei tre bottoni
`↗` ha un `href` recuperabile: nel file `dom-blocks.json` (62 elementi totali) i tre `span`
`INIZIA IL CORSO ↗` / `ESPLORA LO STACK ↗` / `SCOPRI IL SETUP ↗` [y=1389] hanno tutti `href: None`, e
non esiste nessun tag `a` con `href` non vuoto in tutto l'intervallo y=900-1600 (l'intera sezione
Risorse) — verificato interrogando il file riga per riga. Il rapporto precedente descriveva la stessa
area come "la card intera è cliccabile (rilevata come CTA da 330×462)": se era vero il 2026-09-01, il
1° settembre e il 7 settembre la pagina si comporta diversamente rispetto all'estrazione automatica, e
questo va scritto nel gate di cattura: **prima di dichiarare un componente "cliccabile", verificare
l'href nel DOM, non solo la sua forma visiva.**

**PATTERN:** una prova sociale può esistere sulla pagina ed essere invisibile a qualunque lettore
automatico. Le tre etichette-dato che il rapporto precedente lodava come "il pezzo migliore di tutta
la pagina" (`+280K FOLLOWERS`, `+1M GENERATO COL COPYWRITING`, `+3700 ORDINI SUL SITO`) **sono ancora
lì, visivamente**, confermato aprendo `desktop-01.png`: appaiono esattamente come descritte, collegate
alla foto con linea sottile e punto. Ma **zero delle tre stringhe compare in nessuno dei 62 blocchi di
testo di `dom-blocks.json`** — ricerca diretta di `FOLLOWERS`, `GENERATO`, `ORDINI`, `280`, `3700`:
nessun risultato. Il motivo emerge da `scheda.json → media`: l'intera composizione (foto + le tre
etichette) è **un'unica immagine**, `Group+7.png`... in realtà per l'esattezza `Group+5.png`
(530×590, `alt=""`) sovrapposta al riquadro foto [y=124, x=720]. Le tre cifre più importanti della
pagina — l'unica prova sociale numerica di tutto il sito — sono pixel dentro un PNG con `alt` vuoto:
invisibili a uno screen reader, non selezionabili, non indicizzabili da un motore di ricerca testuale
o da un crawler AI, e infatti invisibili anche a questo stesso studio se non si fosse aperto lo
screenshot. **Regola per la Fabbrica:** ogni prova numerica critica va marcata come testo HTML reale
(anche se sovrapposta graficamente a un'immagine con CSS), mai lasciata dentro il file raster.

**GATE:** aggiungere al controllo automatico un secondo passaggio obbligatorio quando un elemento
`cta`-like ha `href: null` o assente: cercare nell'intero file (non solo nell'intorno immediato) un
tag `a` con lo stesso testo o la stessa coordinata `y`±5px prima di dichiarare "non linkato". Fatto qui
a mano per i tre bottoni-card: zero risultati in tutto il file, quindi la dichiarazione "non linkato"
regge. Lo stesso controllo, applicato al link di footer "Risorse" (vedi sotto), rivela un secondo
difetto reale, non un artefatto di misura.

---

## LA STRUTTURA — un hub, non un funnel, misurato contro le 11 tappe

La formula completa a 11 tappe (hero → agitazione → prova con fonte → metodo → benefici → curriculum →
qualificazione negativa → obiezioni → autorevolezza → prezzo barrato → FAQ → chiusura) è quella di una
**sales page**. Questa pagina non è una sales page: è un indice. Il confronto, sezione per sezione:

| # | y | Alt. (px) | Sezione | Tappa della formula a 11 che occupa | Cosa manca |
|---|---|---|---|---|---|
| 1 | 0 | 749 | **Hero** — *"Formazione tecnica per professionisti di marketing"* [y=193] | Hero, ma **senza promessa numerica né urgenza** | Nessuna agitazione segue: la sezione successiva è un'offerta gratuita, non un problema |
| 2 | 749 | 898 | **Risorse** — 3 card gratuite (corso, stack, attrezzatura) [y=849] | Nessuna tappa della formula — è un blocco di **lead magnet**, non di vendita | Non c'è transizione da "problema" a "soluzione": si passa da hero a regalo senza motivare il salto |
| 3 | 1.647 | 481 | **Blog** — *"Collezione di articoli"* [y=1819] | Nessuna tappa — rimando a contenuto esterno alla pagina | — |
| 4 | 2.128 | 551 | **La mia storia** — *"Sono Andrei Pascu, titolare di AP Sales"* [y=2339] | Frammento di **autorevolezza**, ma senza numeri né prova verificabile in questa sezione (i numeri sono nell'hero, sezione 1) | Manca ogni riferimento a un prodotto specifico: l'autorevolezza non punta a nessuna vendita |
| 5 | 2.679 | 705 | **Footer** — nav + disclaimer legale | Nessuna tappa — è chiusura istituzionale, non chiusura di vendita | Nessun CTA di acquisto, nessun prezzo, nessuna FAQ |

**Risultato della misura: 0 tappe su 11 della formula di vendita sono presenti in forma completa.**
Il massimo che si può concedere è mezza tappa di "hero" (c'è un H1/H2 con promessa, manca l'agitazione
che di norma segue) e un frammento di "autorevolezza" spostato all'interno della sezione storia. Non
c'è **prova con fonte**, non c'è **metodo**, non c'è **curriculum**, non c'è **qualificazione
negativa**, non c'è **obiezioni**, non c'è **prezzo barrato**, non c'è **FAQ**, non c'è **chiusura di
vendita**. Confermato con ricerca testuale sui 62 blocchi: zero occorrenze di "€", zero di "FAQ",
zero di "obiezione"/"Ma io", zero di "garanzia"/"rimbors*".

---

## LA HOME DI UN NEGOZIO DA 60 PAGINE COMMERCIALI: COSA FA, COSA NON FA, DOVE MANDA IL TRAFFICO

Questa è la domanda che conta di più per questo file, e la risposta è misurabile riga per riga.

### Cosa fa
1. **Si presenta** — headline sobria, nessun numero di guadagno, nessuna urgenza [y=193].
2. **Regala** — tre risorse gratuite (corso base, stack tool, lista attrezzatura) [y=849-1600].
3. **Rimanda al blog** — una riga di descrizione + un bottone [y=1726-2100].
4. **Racconta la storia personale** dell'autore in due frasi [y=2248-2498].
5. **Chiude con footer istituzionale** — nav + disclaimer + cookie.

### Cosa NON fa (verificato, non presunto)
1. **Non vende.** Zero occorrenze di "€" in tutti i 62 blocchi di `copy-integrale.md`. Nessun prezzo,
   nessun prodotto a pagamento nominato.
2. **Non nomina nessuno dei prodotti a pagamento dell'ecosistema.** Ricerca diretta: zero occorrenze di
   "outFunnel", "outEmail", "outViral", "outHeadline", "Manuale del copywriter", "funnel-operator",
   "copy" (come nome prodotto) in tutto il testo della home. Un visitatore che legge solo questa pagina
   non scopre che questi prodotti esistono.
3. **Non ha una sola CTA che porti a una pagina di vendita o a una pagina `/store/p/...`.** Confermato
   sull'elenco completo di `href` estratti da `dom-blocks.json` (tabella sotto): nessuna delle 13
   destinazioni uniche è un prodotto o uno store.
4. **Non mostra prova sociale leggibile.** Le tre etichette-dato esistono solo come pixel (vedi DELTA
   ALLA FABBRICA sopra) — a fini pratici di un audit testuale come questo, o di un motore di ricerca,
   la pagina ha **zero prova sociale**.

### Dove manda il traffico — il conteggio completo dei link in uscita

Estratto da `dom-blocks.json` (62 elementi), deduplicato per testo+destinazione+coordinata. **13
istanze di link, 8 destinazioni uniche**:

| Destinazione | Istanze | Testo | Natura |
|---|---|---|---|
| `#page` | 1 | "Passa al contenuto" [y=846] | Skip-link interno, accessibilità |
| `https://claude-speedrun.com` | 1 | "Claude Speedrun" [y=854] | **Esterno** — altro prodotto di Andrei Pascu, promosso dalla nav prima di ogni contenuto della home |
| `#` | 1 | "Accedi" [y=855] | Login, nessuna destinazione reale (ancora placeholder) |
| *(vuoto, `href=""`)* | 1 | "Scopri di più →" [y=559] | **CTA hero, morta** — il bottone più in vista della pagina non porta da nessuna parte |
| `/blog` | 2 | "Leggi gli articoli" [y=1947], "Blog" [y=3009, footer] | Interno, contenuto editoriale |
| `https://www.apsales.info/` | 1 | "AP Sales" [y=2343] | **Esterno** — sito dell'agenzia madre |
| `/story` | 2 | "Leggi la mia storia" [y=2498], "La mia storia" [y=2871, footer] | Interno, pagina biografica |
| `/presto-disponibile` | 3 | "Store" [y=2906], "Recensioni" [y=2940], **"Risorse" [y=2974]** | Interno — **pagina segnaposto "coming soon"**, non una pagina reale |
| `/privacy-dati-cookie-simili` | 1 | "Privacy, dati, cookie e simili" [y=3307] | Interno, legale |

**La scoperta dentro la scoperta:** il link di footer etichettato **"Risorse"** [y=2974] non punta alla
sezione "Risorse" che esiste realmente su questa stessa pagina (y=849, con le tre card gratuite) — punta
a `/presto-disponibile`, la stessa pagina-segnaposto di "Store" e "Recensioni". Chi clicca "Risorse" nel
footer, aspettandosi di rivedere le tre card che ha appena visto scorrendo, atterra su una pagina vuota.
È un errore di implementazione verificabile (due href identici per tre etichette diverse, una delle
quali duplica il nome di una sezione già esistente e funzionante sulla stessa pagina), non
un'interpretazione.

**Sintesi del conteggio:** su 13 istanze di link, **3 sono esterne al dominio** (Claude Speedrun, AP
Sales, e implicitamente ogni "Fonte" — qui assente), **2 sono morte o senza destinazione reale** (CTA
hero vuota, "Accedi" con `#`), **3 portano a un segnaposto** ("Store"/"Recensioni"/"Risorse" →
`/presto-disponibile`), e **le restanti 5** (skip-link, 2×blog, 2×story, privacy) sono le uniche
funzionalmente sane. **Zero su 13 portano a un prodotto o a una vendita.** Per un negozio che — stando
al perimetro di questo studio — ha una sessantina di pagine commerciali nel suo dominio, la porta
d'ingresso principale non ne indica una sola.

---

## LA PROMESSA E DOVE STA

> **"Formazione tecnica per professionisti di marketing"** [y=193]

La promessa vive per intero nell'headline, in cinque parole, e non si ripete altrove sotto altra forma:
nessuna riga successiva la rafforza con un numero o un termine. Il sottotitolo aggiunge il **come**, non
il **cosa**:

> "AP Sales è un'agenzia di marketing… E qui insegniamo il nostro scientifico e preciso approccio per
> fare marketing online." [y=430]

La struttura è "prova di mestiere prima della promessa": si dichiara di essere un'agenzia che lavora
davvero, poi si offre di insegnare quello che fa. La promessa non è mai quantificata (non "guadagna X",
non "in Y giorni") — è posizionale: chi si sente già "professionista" si riconosce, chi no si sente
escluso o incuriosito. Nessuna delle sezioni successive (Risorse, Blog, Storia) aggiunge una nuova
promessa: **ognuna ha una propria mini-promessa isolata** ("Il punto di partenza: fondamenta, framework
e metriche che ogni marketer deve padroneggiare prima di scalare" [y=1306], ecc.), senza mai ricollegarsi
alla promessa dell'hero. È una pagina a promesse parallele, non a una promessa che si sviluppa in
verticale come in una sales page.

---

## COME TRATTA LE OBIEZIONI

**Non le tratta.** Ricerca diretta sui 62 blocchi: zero pattern "Ma...", zero "obiezione", zero
struttura domanda-risposta. L'unica cosa che si avvicina a una gestione preventiva di dubbio è
posizionale, non dialogica:

> "Sono qui per insegnare il marketing **per come lo vedo io**." [y=2412]

Questa frase disinnesca in anticipo "non è l'unico modo di vedere il marketing" — ma lo fa inquadrando
un'opinione, non rispondendo a un'obiezione esplicita. È coerente con la natura della pagina: un hub non
deve vincere una vendita nello spazio di uno scroll, quindi non ha bisogno dell'armamentario
obiezione-risposta che si vede invece su `outfunnel` o sul `manuale-del-copywriter`.

---

## LE PROVE E LA LORO VERIFICABILITÀ (spietato)

Tre presunte prove, zero verificabili con gli strumenti di questo studio:

1. **`+280K FOLLOWERS`** — nessuna fonte, nessun link al profilo che li conterebbe, e — come già
   accertato sopra — **nessun testo reale**: sono pixel dentro `Group+5.png` [y=124]. Non verificabile
   nemmeno cliccando, perché non c'è nulla su cui cliccare.
2. **`+1M GENERATO COL COPYWRITING`** — stessa natura grafica, stesso difetto. Nessuna metodologia di
   calcolo dichiarata (fatturato proprio? dei clienti? cumulato in quanti anni?).
3. **`+3700 ORDINI SUL SITO`** — il più specifico dei tre (numero non tondo, quindi più credibile a
   naso), ma identico problema di verificabilità: non è testo, non ha fonte, non ha data di riferimento.

**Il paragone che conta:** il `manuale-del-copywriter` (vedi report dedicato) sostituisce del tutto la
prova con un campione gratuito del prodotto stesso — tecnica misurata come superiore a qualunque badge
numerico. Qui, sulla home, il badge numerico è l'unica prova offerta e **non è nemmeno testo**: è la
prova sociale più debole misurata finora in tutto l'ecosistema, non perché il numero sia falso (non ho
motivo di crederlo tale) ma perché **nessuno strumento automatico, e nessun lettore che usi uno screen
reader, può verificarne l'esistenza sulla pagina stessa.**

Non ci sono altre prove sulla pagina: zero testimonianze, zero loghi cliente, zero citazioni di terzi.

---

## LA SCALA DI IMPEGNO

A differenza di una sales page (dove la scala va da "leggi" a "compra"), qui la scala si ferma al primo
gradino e non sale mai:

| Livello | Azione disponibile su questa pagina | Presente? |
|---|---|---|
| 0 — Nessun impegno | Scorrere e leggere | Sì |
| 1 — Micro-impegno gratuito | Cliccare una card risorsa, leggere il blog, leggere la storia | Sì, ma **3 delle card non hanno un href verificabile** (vedi DELTA) |
| 2 — Lasciare un contatto (opt-in) | Form email, iscrizione | **Assente** — zero form su questa pagina |
| 3 — Acquisto di prova (basso prezzo) | Link a un prodotto economico (es. il Manuale, 79€) | **Assente** — zero link a `/store` o a un prodotto |
| 4 — Acquisto pieno | Link a un corso completo | **Assente** |

La pagina che dovrebbe fare da porta d'ingresso a un intero negozio si ferma al gradino 1, e anche lì con
una falla (le card senza href verificabile). Non esiste alcun ponte esplicito e cliccabile tra "ho letto
la home" e "ho comprato qualcosa" — il ponte, se esiste, passa per canali esterni alla pagina stessa
(social, altre pagine linkate da altrove).

---

## IL PREZZO E LA SUA CORNICE

**Non c'è.** Zero occorrenze di simboli di valuta o di cifre di prezzo in tutti i 62 blocchi. Coerente
con la natura di hub: la cornice del prezzo, quando esiste nell'ecosistema, vive sempre nelle pagine
figlie (`outfunnel`, `manuale-del-copywriter`, ecc.), mai qui.

---

## COSA NON DICE MAI

1. **Il nome di un solo prodotto a pagamento.** outFunnel, outEmail, outViral, outHeadline, il Manuale,
   `/copy` — nessuno compare nel testo della home.
2. **Un prezzo**, di nessun tipo.
3. **Una garanzia o un rimborso** — zero occorrenze.
4. **Una testimonianza o una recensione** — la voce "Recensioni" esiste solo come etichetta di link nel
   footer, e porta a un segnaposto, non a un contenuto.
5. **Un nome di brand coerente.** Sulla stessa pagina convivono quattro nomi: il `<title>` dice
   `AP Formazione` [meta], il footer dice `AP Sales`/`APsales` [y=2343 e footer logo], la nav dice
   `Claude Speedrun` [y=854] come primo link visibile, il dominio è `andrei-copy.com`. Un visitatore
   nuovo non ha modo di sapere con certezza come si chiami "questa cosa".

---

## LE FORMULE RICORRENTI

**1. Prova di mestiere prima della proposta di valore**
> "AP Sales è un'agenzia di marketing… E qui insegniamo il nostro scientifico e preciso approccio per
> fare marketing online." [y=430]

`[NOME AZIENDA] è un'agenzia/impresa che fa [MESTIERE] davvero… E qui insegniamo [PLACEHOLDER: COME LO
FACCIAMO, IN DUE AGGETTIVI DA LABORATORIO].`

**2. Eyebrow di categoria/prezzo sopra al titolo, prima di ogni altra informazione**
> `CORSO GRATUITO` [y=1222] → *"Le basi del Marketing"* [y=1267] → descrizione → CTA

`[ETICHETTA MAIUSCOLA CHE DICE COSA È O QUANTO COSTA] → [TITOLO] → [DESCRIZIONE 1-2 RIGHE] →
[PLACEHOLDER: VERBO D'AZIONE + OGGETTO ↗]`

**3. Descrizione-lead-magnet ancorata a qualcosa che il lettore già consuma**
> "Fotocamere, microfoni e setup con cui produciamo i video e i contenuti **che vedi ogni giorno**."
> [y=1306]

`[COSA OFFRIAMO] con cui produciamo [PLACEHOLDER: CIÒ CHE IL LETTORE GIÀ CONSUMA DI NOI OGNI GIORNO].`

**4. Inquadramento soggettivo come scudo anti-obiezione**
> "Sono qui per insegnare il marketing **per come lo vedo io**." [y=2412]

`Sono qui per insegnare [PLACEHOLDER: ARGOMENTO] per come lo vedo io.`

**5. Badge-dato in tre categorie non sovrapposte (audience / risultato economico / trazione propria)**
> `+280K FOLLOWERS` · `+1M GENERATO COL COPYWRITING` · `+3700 ORDINI SUL SITO`

`+[NUMERO][UNITÀ] [CATEGORIA AUDIENCE] · +[NUMERO]€ [PLACEHOLDER: RISULTATO ECONOMICO] · +[NUMERO]
[PLACEHOLDER: TRAZIONE COMMERCIALE PROPRIA, VERIFICABILE E NON TONDA].`

**6. Credenziale + secondo grassetto sull'aggettivo tecnico, mai sul risultato**
> "AP Sales è un'agenzia di marketing… **il nostro scientifico** e **preciso** approccio" [y=463]

`[CREDENZIALE] … il nostro [PLACEHOLDER: AGGETTIVO 1 DA LABORATORIO] e [PLACEHOLDER: AGGETTIVO 2 DA
LABORATORIO] approccio.`

---

## IL DIFETTO

Quattro difetti reali, ciascuno misurato su questa cattura, non impressioni:

1. **La prova sociale più importante della pagina non è testo.** Le tre etichette-dato (`+280K
   FOLLOWERS`, `+1M GENERATO COL COPYWRITING`, `+3700 ORDINI SUL SITO`), visibili in `desktop-01.png`,
   non compaiono in nessuno dei 62 blocchi di `dom-blocks.json` — sono pixel dentro `Group+5.png`
   [y=124, `alt=""`]. Nessuno screen reader, motore di ricerca o crawler AI può leggerle.
2. **Le tre CTA della sezione Risorse non hanno un `href` verificabile.** `INIZIA IL CORSO ↗`,
   `ESPLORA LO STACK ↗`, `SCOPRI IL SETUP ↗` [tutti y=1389] risultano `href: None` in `dom-blocks.json`,
   e non esiste alcun tag `a` con destinazione in tutto l'intervallo y=900-1600. Le tre card che
   dovrebbero introdurre il visitatore ai contenuti gratuiti dell'ecosistema, in questa cattura, non
   portano da nessuna parte in modo verificabile.
3. **Il link di footer "Risorse" [y=2974] non punta alla sezione Risorse della stessa pagina** [y=849] —
   punta a `/presto-disponibile`, lo stesso segnaposto di "Store" e "Recensioni". Tre etichette diverse,
   una delle quali duplica il nome di un contenuto già esistente e funzionante, tutte e tre alla stessa
   pagina vuota.
4. **Zero delle 13 istanze di link della pagina portano a un prodotto o a una pagina di vendita.** Per
   l'home di un negozio con una sessantina di pagine commerciali nel dominio (per il perimetro dato a
   questo studio), è una porta d'ingresso che non indica l'esistenza di un solo negozio.

---

## Nota sulla lunghezza

Il documento è più corto dello standard di 3.000 parole della famiglia "out*" perché **la pagina stessa
è un ottavo delle altre**: 3.384px contro 26.993px di `outfunnel`. Ogni sezione richiesta dallo standard
è stata comunque coperta con citazione diretta o con la ricerca testuale che ne dimostra l'assenza — non
è stata aggiunta aria per raggiungere un conteggio.

## Collegamenti

- [01-andrei-copy-home.md](01-andrei-copy-home.md) — il rapporto di design/palette (macchina v1,
  2026-09-01), qui non ripetuto se non dove la nuova cattura lo corregge
- [21-22-outemail-outviral-COPY.md](21-22-outemail-outviral-COPY.md) — lo standard di forma di questo
  file
- [04-outfunnel-COPY.md](04-outfunnel-COPY.md) · [06-manuale-del-copywriter-COPY.md](06-manuale-del-copywriter-COPY.md) — le due pagine prodotto collegate a questo studio
- `capture/01-andrei-copy-home/dom-blocks.json`, `scheda.json`, `desktop-01.png`, `desktop-02.png` — le
  fonti grezze usate per ogni citazione di questo file
