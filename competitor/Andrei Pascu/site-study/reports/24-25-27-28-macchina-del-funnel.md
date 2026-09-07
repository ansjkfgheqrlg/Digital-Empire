---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #funnel #pre-checkout #pagine-ponte #onda-b
Created: 2026-09-07
Last updated: 2026-09-07
---

# La macchina del funnel — quattro pagine che non vendono niente

**Onda B, catture `24-asa` · `25-define` · `27-armadeggon-strp` · `28-outfunnel-1`, tutte del
2026-09-07.** Erano classificate T2, *«pagine che vendono su Squarespace»*. **Non vendono.** Sono i
gradini fra una pagina e la cassa, e messe in fila raccontano come Andrei Pascu porta uno sconosciuto
al pagamento senza mai chiedergli i soldi nella pagina che glielo fa desiderare.

---

## DELTA ALLA FABBRICA

**CANONE.** Fra la pagina di vendita e la cassa ci va **un gradino**. La legge nuova è questa: *un
prodotto one-shot non manda mai dal bottone di vendita direttamente al pagamento; in mezzo sta una
pagina di pre-cassa che riafferma cosa si sta comprando, mostra la cifra da sola e consegna lì — e
solo lì — l'eventuale codice sconto.* Il motivo è misurato più sotto: lo sconto messo prima abbassa
il prezzo percepito mentre il lettore sta ancora decidendo; messo dopo, toglie attrito quando ha già
deciso.

**PATTERN — due nuovi, entrambi dimostrati da più di un uso (§10 della legge: due usi = pattern).**

1. **`pagina-ponte`** (dimostrato da `/define` e `/asa`): una sola sezione, un video, **un solo
   bottone**, zero prezzo, zero prova sociale, zero obiezioni. Densità misurata: **35-36 blocchi di
   testo** contro i **259** di `/outemail`. Serve a spostare, non a convincere.
2. **`pre-cassa`** (dimostrato da `/outfunnel-1` e `/armadeggon-strp`): occhiello in corsivo, nome
   del prodotto grande, scheda prezzo isolata, bottone d'acquisto, **niente altro** — 1.512 e
   1.752 px di altezza totale, cioè meno di uno schermo e mezzo.

**GATE.** Nel controllo di un sito di vendita entra una domanda nuova: *esiste il gradino di
pre-cassa, e il codice sconto sta lì e non prima?* Se un cantiere manda dritto alla cassa, non è a
norma finché non lo dichiara come scelta motivata. Secondo controllo: **l'accento per prodotto**
(sotto) — un solo colore d'azione per pagina, usato **una volta sola**.

---

## LE DUE CATENE, MISURATE

### Catena 1 — la scala dell'educazione: `/define` → `/asa` → `/copy-base`

| | `/define` | `/asa` |
|---|---|---|
| Titolo | «Cos'è il copywriting e come funziona?» | «Come funziona monetizzare Il copywriting come autonomo» |
| Altezza | 1.802 px | 1.936 px |
| Sezioni | 1 (1 distinta) | 1 (1 distinta) |
| Blocchi di testo | 36 | 35 |
| Bottoni utili | **1** | **1** |
| Dove porta | `/asa` — «Scopri la strategia A.S.A» `[y=949]` | `/copy-base` — «Diventa un copywriter.» `[y=1073]` |
| Prezzo in pagina | nessuno | nessuno |
| Prova sociale | nessuna | nessuna |

Due domande in fila: prima *cos'è* il mestiere, poi *come ci si guadagna*. Ogni pagina risponde con
**un video** («Te lo spiego in questo video con un esempio pratico», `/define` `[y=327]`) e con un
solo bottone che porta alla domanda dopo. Il prodotto compare al terzo passo, non prima.

**La riga che vale il viaggio** — `/asa` `[y=878]`, un `h3` da 38,4 px, cioè il secondo testo più
grande della pagina:

> «Ti consiglio di vedere e finire il video prima di cliccare il pulsante per capirne i contenuti.»

Non è cortesia: è **controllo del consumo**. Chiede di spendere il tempo *prima* del clic. Chi arriva
al bottone ha già visto il video, quindi clicca sapendo cosa compra — meno rimborsi, meno assistenza,
click di qualità più alta. Nessuna delle nostre pagine dice una cosa simile.

### Catena 2 — la cassa: `/outfunnel-1` e `/armadeggon-strp`

**`/outfunnel-1` — la pre-cassa completa.** 1.512 px, 40 blocchi, e in quest'ordine esatto:

| y | Cosa | Testo misurato |
|---|---|---|
| 149 | occhiello in corsivo | «Stai acquistando…» |
| 189 | `h1` 68,3 px | «out**Funnel**» — «out» in `#13989a`, «Funnel» in `#fafafa` |
| 261 | istruzione + sconto | «Adesso devi solo loggare nel tuo account, inserire i tuoi dati ed entrare. Ricorda di usare il codice sconto "CWSHOP" per avere il 20% di sconto.» |
| 460 | nome prodotto | «outFunnel» |
| 500 | **cifra**, 35,2 px | «98,00 €» |
| 543 | condizione | «Una tantum» |
| 602 | bottone | «Acquista outFunnel» |

Tre cose che qui sono decisioni, non caso:

1. **Lo sconto sta dopo la decisione.** «CWSHOP», 20%, compare **solo** in questa pagina — cioè dopo
   che il lettore ha già cliccato «compra» altrove. 98,00 € diventano 78,40 € **mentre inserisce i
   dati**, non mentre valuta.
2. **«Stai acquistando…» in corsivo, prima del nome.** Riafferma l'atto invece di ricominciare a
   vendere. È l'anti-ripensamento più economico che esista: due parole e tre puntini.
3. **«Una tantum» attaccato alla cifra.** Toglie il sospetto dell'abbonamento nel punto esatto in cui
   nasce, senza una riga di spiegazione.

**`/armadeggon-strp` — il gradino di aggiunta.** 1.752 px, 28 blocchi, e **un solo bottone**:
«Aggiungi all'account ora» `[y=879]`. Nessun titolo di testo nel DOM, nessun prezzo scritto: il
prodotto è un'immagine e l'azione è *aggiungere a un account che esiste già*. È il gradino di chi ha
già comprato — un ordine aggiuntivo, non una vendita nuova. Il nome del file lo dichiara: `strp` =
Stripe.

**Dove va il bottone: verificato, non supposto.** Nessuno dei due bottoni ha un `href` (campo vuoto
in `scheda.json`), e la ricerca di `stripe|checkout|buy` su **tutti i file serviti** delle due pagine
(`src/`, 40+ file ciascuna) non trova nemmeno un URL di cassa. La cassa è avviata dal JavaScript di
Squarespace Commerce a runtime. **Quindi:** l'URL finale del pagamento non è ricavabile da questa
cattura, e non lo scrivo. Va preso da un clic vero, se e quando servirà.

---

## L'ACCENTO PER PRODOTTO — un colore, usato una volta

Il guscio non cambia mai: fondo `#a8a8a8` dietro alla pagina, testo `#fafafa`, un secondo grigio
`#ebe9e0` per il piede, nessun font dichiarato oltre `sans-serif`. Su questo guscio identico, ogni
pagina accende **un solo colore**, e lo usa **una volta sola** — il conteggio d'uso nel DOM è
letteralmente `1`:

| Pagina | Accento | Usi misurati | Su cosa |
|---|---|---|---|
| `/define` | `#efab00` ambra | 1 | la parola «copywriting» nel titolo |
| `/asa` | `#06a506` verde | 1 | la parola «monetizzare» nel titolo |
| `/outfunnel-1` | `#13989a` foglia di tè | 1 (+1 sfumatura `#139699` sul codice sconto) | le tre lettere «out» del nome prodotto |
| `/armadeggon-strp` | **nessuno** | 0 | — |

**Questa è la lezione trasferibile.** Non «usa il colore con parsimonia»: *un colore per pagina, su
una parola sola, e quella parola è il verbo della promessa*. Su `/asa` non è evidenziato
«copywriting» ma **«monetizzare»** — la parola che porta i soldi, non quella che descrive il mestiere.
Il nostro canone dice «colore d'azione sotto il 10%»: qui siamo a **un'occorrenza su quattordici**
(7%), e il risultato è più forte di qualunque bottone acceso.

---

## LA TRIAGE ERA SBAGLIATA, E ORA SI SA DI QUANTO

`ECOSISTEMA.md` metteva queste quattro pagine in **T2 — «pagine che vendono»**, con lo stesso peso di
`/outemail` (26.032 px, 24 sezioni, 259 blocchi). Misurate:

| | pagine di vendita (T2 vere) | queste quattro |
|---|---|---|
| Altezza media | 15.653 px | **1.750 px** — nove volte meno |
| Sezioni | 11-24 | **1** |
| Blocchi di testo | 132-259 | **28-40** |

**Quattro delle otto pagine di Onda B appartengono a T3, la macchina del funnel.** Non è un errore di
enumerazione: è che l'elenco delle pagine era stato letto dai *nomi*, e i nomi mentono
(`/outfunnel-1` sembra la pagina del prodotto outFunnel; è la sua cassa).

E la macchina è **più grande dell'elenco**: `/vendita` porta a `/acquista-v101` `[y=3219]`, una
pagina di pre-cassa che **non è nella lista T3** del piano. Se un solo campione ne rivela una nuova,
l'elenco delle 14 pagine `-pre` va riaperto quando si apre l'Onda D.

---

## I DIFETTI, PERCHÉ CE NE SONO

1. **Il codice sconto è pubblico e permanente.** «CWSHOP» sta scritto in chiaro su una pagina
   indicizzabile: chiunque cerchi «outFunnel sconto» lo trova. Uno sconto che c'è sempre non è uno
   sconto, è il prezzo. Il listino reale di outFunnel è 78,40 €, e 98,00 € è una decorazione.
2. **`/armadeggon-strp` non dice cosa costa.** Nessuna cifra nel DOM: chi arriva lì da un link
   esterno vede un'immagine e un bottone «Aggiungi all'account ora» senza sapere quanto.
3. **Titolo con un refuso, e pubblicato:** la pagina si chiama `armadeggon-strp` e il titolo del
   documento è «Armageggon STRP» — due grafie sbagliate dello stesso nome (`Armageddon`), in URL e in
   `<title>`. Piccolo, ma è la prova che queste pagine sono fatte in fretta: sono impalcatura, non
   vetrina. **Anche questo è un insegnamento**: lui non lucida i gradini, lucida le pagine che
   convincono.

---

## Connessioni
- [[ECOSISTEMA]] — la triage da correggere: queste quattro passano da T2 a T3
- [[PRE-MORTEM-ESECUZIONE]] — la causa 3 (lo stato scritto a mano mente) vale anche per la triage
- [[33-PIANO-STUDIO-TOTALE-ANDREI-PASCU]] — l'Onda D va riaperta: `/acquista-v101` non era in elenco
- [[32-DOSSIER-FABBRICA-SITI]] — dove finiscono i due pattern nuovi e il gate
