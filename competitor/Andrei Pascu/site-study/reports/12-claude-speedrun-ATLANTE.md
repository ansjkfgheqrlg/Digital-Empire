---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #claude-speedrun #atlante-visivo #design-system #reference
Created: 2026-09-07
Last updated: 2026-09-07
---

# ATLANTE VISIVO — claude-speedrun.com

**Ogni schermata della pagina, con sotto come è fatta.** Misure e composizione lette da
`capture/12-claude-speedrun-v2/scheda.json` (campionato dal DOM reale), effetti da
`estratto-css.md` e dai file sorgente in `src/`. Le 34 sezioni sono state aperte una per una con
lo strumento di visione — comprese le due varianti di firma ripetuta — prima di scrivere una sola
riga qui sotto.

Questo documento copre **la composizione sezione per sezione**: chi vuole lo stack (Vite+React,
shadcn, i 9 `@keyframes`, la prova numerica sull'arancione `#fb4604`) trova tutto in
[12-claude-speedrun-STACK-E-TOKEN.md](12-claude-speedrun-STACK-E-TOKEN.md), non ripetuto qui. Il
modello di forma è [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) e
[11-armageddon-ATLANTE-VISIVO.md](11-armageddon-ATLANTE-VISIVO.md).

> **Le immagini** vivono in `../capture/12-claude-speedrun-v2/sezioni/`. **34 sezioni misurate, 32
> firme strutturali distinte** — due coppie ripetono la firma della sezione precedente: Tavola 5
> (i=9, variante di i=5) e Tavola 14 (i=28, variante di i=14). Sono documentate come variante
> dentro la tavola del rappresentante, come previsto dal formato.
>
> Altezza totale pagina: **33.756px**. Ogni percentuale sotto è `altezza sezione / 33.756`.

---

## TAVOLA 1 — La testata a due colonne
![sezione 01](../capture/12-claude-speedrun-v2/sezioni/01-come-un-titolare-d-agenzia-usa-rea.png)

**Ruolo:** hero, primo contatto — qualifica l'audience prima ancora di vendere.

| Campo | Valore |
|---|---|
| y / altezza | 0px / 620px — **1,8%** della pagina |
| Sfondo | `#000000` (bg-black) |
| Heading | H1 — "Come un titolare d'agenzia usa realmente Claude nel suo lavoro (senza la roba hype)" |
| Blocchi di testo | 5 |
| Parole | 18 |
| Media | 3 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.bg-black\|1\|M\|-\|3` — gruppo 1, rappresentante |

**Composizione.** Due colonne: a sinistra un fotogramma sfocato (motion blur) di un cavaliere
templare medievale in armatura su fondo blu, con "WORKFLOW" in contorno arancione e "update" in
corsivo pieno sovrapposti in basso; a destra, su nero pieno, il logo "🏃 claude 2" in alto, la
pre-headline arancione maiuscola "CORSO ACCELERATO", poi l'H1 bianco con l'ultima parentesi in
corsivo. Nessun corpo lungo, nessuna CTA: è un fermo immagine, non un invito.

**Effetti attivi.** Nessuno oltre alla sfocatura fotografica stessa (probabile `blur()` statico
sull'immagine, non un filtro CSS in movimento — coerente con `filtri: blur(1.5px)
brightness(0.42) saturate(0.85)` misurato nel report stack, applicato a più elementi decorativi
della pagina).

**Perché è costruita così.** Zero CTA nella prima schermata è una scelta: la sezione vende
l'atmosfera ("titolare d'agenzia", "senza la roba hype") prima di chiedere qualunque azione. Il
"WORKFLOW update" fuori registro (fuori dall'heading semantico, solo grafica) segnala fin da
subito che la pagina userà tipografia enorme come decorazione, non solo come contenuto — un
pattern che si ripete per tutta la pagina (vedi Tavola 3, 13, 27).

---

## TAVOLA 2 — Il primo pitch con prova sociale in miniatura
![sezione 02](../capture/12-claude-speedrun-v2/sezioni/02-corso-per-marketer-che-vogliono-tr.png)

**Ruolo:** seconda hero, offerta esplicita con doppia via d'uscita.

| Campo | Valore |
|---|---|
| y / altezza | 620px / 980px — **2,9%** |
| Sfondo | `transparent` (eredita lo sfondo scuro grezzato sotto) |
| Heading | H2 — "Corso per marketer che vogliono trasformare Claude in un dipendente che non dorme, non beve e non chiede aumenti." |
| Blocchi di testo | 13 |
| Parole | 56 |
| Media | 4 |
| CTA | 2 |
| Firma / gruppo | `section\|relative.w-full.overflow-hidden\|5\|M\|C\|5` — gruppo 2, rappresentante |

**Composizione.** Un nastro diagonale verde "Versione 2: fuori ora." in alto a sinistra, tre
mockup fotografici sovrapposti a ventaglio (un'interfaccia scura con "Claude" e "Good evening,
Gaia", una foto ritratto dell'autore, un editor di codice scuro con etichetta "Speedrun"), l'H2 in
bianco su grana scura, e sotto due CTA impilate: piena arancione "Iscriviti" (448×60), e a contorno
verde "Vedi novità" (448×64, testo verde `#00751f`). Un banner cookie invadeva il crop al momento
della cattura — segno che sul sito reale compare subito, sopra il fold.

**Effetti attivi.** Sfondo a texture di grana verticale scura (probabile pattern ripetuto, coerente
con la palette-sfondi che elenca `#1a1a1a`/`#1b1b1b` a bassa frequenza). Nessuna animazione
rilevata su questa sezione specifica nell'elenco `animazioni` di `scheda.json`.

**Perché è costruita così.** Due CTA di colore diverso (arancione pieno vs verde a contorno) non
sono varianti A/B: sono **due destinazioni diverse** — "Iscriviti" va all'acquisto, "Vedi novità"
soddisfa chi ha già comprato la v1 e vuole solo sapere cosa cambia. È un bivio di segmentazione
messo prima di qualunque altro contenuto, non un test di colore.

---

## TAVOLA 3 — Il pattern-interrupt "5X" e il secondo artefatto-biglietto
![sezione 03](../capture/12-claude-speedrun-v2/sezioni/03-section.png)

**Ruolo:** rinforzo dell'offerta con artefatto grafico da collezione (primo apparire del "biglietto").

| Campo | Valore |
|---|---|
| y / altezza | 1600px / 1404px — **4,2%** |
| Sfondo | `#000000` (bg-black) |
| Heading | nessuno (`headings: []`) |
| Blocchi di testo | 6 |
| Parole | 56 |
| Media | 3 |
| CTA | 1 — "RUBA WORKFLOW" |
| Firma / gruppo | `section\|w-full.bg-black.overflow-hidden\|3\|M\|C\|7` — gruppo 3, rappresentante |

**Composizione.** "5X" gigantesco in contorno bianco con dietro un volto in bianco e nero
(occhi coperti da una barra sfocata, tecnica da meme "identità protetta"), poi una fascia arancione
piena a tutta larghezza con "GET. SHIT. DONE." in nero maiuscolo enorme — **testo decorativo, non
un heading HTML** (non compare in `headings`). Sotto, due paragrafi bianchi, l'immagine di un
biglietto a due colori (blu con "WORKFLOW" arancione in contorno, arancione con codice a barre) e
la CTA uppercase "RUBA WORKFLOW" (226×52, arancione).

**Effetti attivi.** Nessun filtro dichiarato per questa sezione oltre al blend fotografico sul
volto. Il biglietto stesso è un'immagine composita già renderizzata (non un componente vivo come
il biglietto di armageddon), coerente con l'assenza di JS specifico per questa sezione
nell'`_INDICE.json`.

**Perché è costruita così.** "GET. SHIT. DONE." vive fuori dalla gerarchia H1-H6: è pura
tipografia-manifesto, usata per intensità visiva senza pesare sulla SEO/accessibilità della
pagina. È il primo segnale che su questo sito **il testo enorme e il contenuto semantico sono due
strati separati** — utile da tenere a mente prima di copiare "quanto è grande il titolo" da uno
screenshot: non tutto il grande è un heading.

---

## TAVOLA 4 — La sezione fantasma (bg dichiarato scuro, resa chiara)
![sezione 04](../capture/12-claude-speedrun-v2/sezioni/04-section.png)

**Ruolo:** non verificabile dallo screenshot — anomalia di cattura documentata, non un difetto del sito.

| Campo | Valore |
|---|---|
| y / altezza | 3005px / 1079px — **3,2%** |
| Sfondo (dichiarato) | `#0a0a0a` (quasi nero) |
| Heading | nessuno |
| Blocchi di testo | 9 |
| Parole | 70 |
| Media | 2 |
| CTA | 1 |
| Firma / gruppo | `section\|w-full.py-16.md:py-24\|2\|M\|C\|5` — gruppo 4, rappresentante |

**Composizione — quello che si vede davvero.** Lo screenshot è **quasi vuoto**, sfondo chiaro
uniforme con un solo filetto nero in alto: nessuno dei 9 blocchi di testo, 2 media o 1 CTA
dichiarati in `scheda.json` è visibile nel fotogramma catturato, pur avendo il DOM un sfondo scuro
dichiarato.

**Effetti attivi.** Non determinabile da questa cattura.

**Perché è costruita così — e cosa cade se si fida ciecamente dello screenshot.** Questa è la
prova diretta che **misurare dal DOM (`scheda.json`) e guardare lo screenshot sono due controlli
diversi, non intercambiabili**: qui il DOM dichiara contenuto reale (9 blocchi, 70 parole, media,
un CTA) su sfondo scuro, ma il fotogramma è chiaro e vuoto — segno di un asset a caricamento
differito (probabile carosello o video) non ancora pronto al momento dello scatto automatico.
**Non invento cosa ci sia scritto**: lo dichiaro come sezione non verificabile, e lo segnalo nel
DELTA come gate mancante.

---

## TAVOLA 5 — Lo spazio bianco anonimo (e la sua variante, Tavola con i=9)
![sezione 05](../capture/12-claude-speedrun-v2/sezioni/05-section.png)

**Ruolo:** separatore/transizione — probabile ancora per media non caricato.

| Campo | Valore |
|---|---|
| y / altezza | 4084px / 572px — **1,7%** |
| Sfondo | `#f9f9f9` (bianco carta) |
| Heading | nessuno |
| Blocchi di testo | 0 |
| Parole | 0 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|1\|M\|-\|3` — **gruppo 5, rappresentante** |

**Composizione.** Rettangolo bianco piatto, letteralmente vuoto nello screenshot: nessun testo,
nessun bordo visibile oltre al filetto superiore. Coerente col dato `blocchi_testo: 0` — qui il
DOM stesso non dichiara testo, solo 1 media non renderizzato.

### La variante — i=9 (stessa firma, non rappresentante)
![sezione 09](../capture/12-claude-speedrun-v2/sezioni/09-come-io-uso-l-ai-luglio-2026.png)

Sezione i=9, y=7193 h=652 (**1,9%**), heading H2 "Come io uso l'AI: luglio 2026" — **stessa firma
esatta** (`section|w-full.py-24.border-t|1|M|-|3`, gruppo 5) della Tavola 5. Qui il titolo
compare, in nero su bianco, ma il corpo resta comunque vuoto: `blocchi_testo: 1`, `parole: 6` — il
sistema conta solo il titolo, il resto della sezione (il media dichiarato) non è arrivato in tempo
per lo scatto.

**Effetti attivi (entrambe).** Nessuno rilevabile.

**Perché è costruita così.** Le due sezioni del gruppo 5 condividono una funzione precisa: sono
**ancoraggi per contenuto multimediale a caricamento lento** (screenshot di prodotto, demo,
GIF) — il pattern si ripete identico anche nelle Tavole 4 e 14. Sul sito reale, con JavaScript
completamente caricato e un utente che scrolla, quello spazio bianco diventerebbe un'immagine
concreta; nella cattura statica resta un buco. È un limite dello strumento di cattura, non del
sito — ma è un limite che va conosciuto prima di dichiarare "atlante completo" (vedi DELTA).

---

## TAVOLA 6 — Il primo confronto ChatGPT vs realtà
![sezione 06](../capture/12-claude-speedrun-v2/sezioni/06-come-usi-l-ai.png)

**Ruolo:** diagnosi del problema — mostra l'uso sbagliato dell'AI prima di proporre quello giusto.

| Campo | Valore |
|---|---|
| y / altezza | 4656px / 537px — **1,6%** |
| Sfondo | `transparent` (eredita lo sfondo scuro) |
| Heading | H3 — "Come usi l'AI:" |
| Blocchi di testo | 6 |
| Parole | 39 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.pb-24.border-t\|1\|M\|-\|3` — gruppo 6, rappresentante |

**Composizione.** Frase di apertura ("Ti voglio bene, ma... Non sai usare l'AI. Sul serio."), poi
l'H3, poi una finta finestra di chat ChatGPT con un unico messaggio: *"Ciao ChatGPT; ecco il mio
testo, correggilo per favore daddy 🥴"* — didascalia sotto in corsivo grigio "Goofy ahh prompt" —
e infine una riga con icona triangolo blu: "NON HAI IDEA DI COSA SI PUÒ FARE CON L'AI" in
maiuscolo bianco.

**Effetti attivi.** Nessuno oltre al colore.

**Perché è costruita così.** La prova d'imbarazzo (il prompt goffo, con l'emoji) funziona come
specchio: il lettore riconosce se stesso nell'esempio ridicolo prima ancora di leggere una singola
promessa. È l'apertura del meccanismo PAS (Problema-Aggravamento-Soluzione) applicato con
autoironia invece che con tono accusatorio diretto.

---

## TAVOLA 7 — Il micro-sondaggio "Dimmi se ti ritrovi"
![sezione 07](../capture/12-claude-speedrun-v2/sezioni/07-l-ai-ganzo-ma-non-ti-cambia-la-vi.png)

**Ruolo:** engagement — invita a un'auto-diagnosi prima di proseguire, senza raccogliere davvero un voto.

| Campo | Valore |
|---|---|
| y / altezza | 5192px / 640px — **1,9%** |
| Sfondo | `#f9f9f9` (bg-brand-grey) |
| Heading | H3 — `" L'AI è ganzo… Ma non ti cambia la vita… "` |
| Blocchi di testo | 14 |
| Parole | 63 |
| Media | 0 |
| CTA | 2 — "Sì, mi ritrovo" (125×42) · "Non mi ritrovo" (136×42) |
| Firma / gruppo | `section\|w-full.py-24.bg-brand-grey\|1\|-\|C\|3` — gruppo 7, rappresentante |

**Composizione.** Citazione in apertura, poi "Dimmi se ti ritrovi" + istruzione "Leggi e poi vota
se ti ritrovi o no", un esempio banale in tre righe (invii un documento → ti dici che ti piace ma
non sei sicuro), e in fondo due pulsanti fantasma affiancati identici nella forma, diversi solo nel
testo.

**Effetti attivi.** Entrambi i pulsanti hanno lo stesso `bg: transparent`, `color: #39393c @0.7`,
`border: 1px solid rgba(57,57,60,0.3)` — nessuna gerarchia visiva fra le due opzioni, coerente con
un finto sondaggio dove **entrambe le risposte portano probabilmente allo stesso scroll**, non a
un ramo diverso del contenuto (né i due CTA hanno `href` dichiarato in `scheda.json`).

**Perché è costruita così.** Il "voto" non serve a raccogliere un dato: serve a far compiere
un'azione fisica (un clic) che aumenta l'investimento psicologico del lettore nella pagina —
tecnica di micro-commitment, non un vero fork di navigazione.

---

## TAVOLA 8 — "ASCOLTA BENE." e la prova dei miliardi
![sezione 08](../capture/12-claude-speedrun-v2/sezioni/08-ascolta-bene.png)

**Ruolo:** climax dell'aggravamento — sposta la colpa dal prodotto all'utente, poi la giustifica coi numeri.

| Campo | Valore |
|---|---|
| y / altezza | 5833px / 1360px — **4,0%** |
| Sfondo | `transparent` (reso visivamente nero) |
| Heading | H1 "ASCOLTA BENE." + H3 "Questi stronzi investono miliardi" |
| Blocchi di testo | 20 |
| Parole | 116 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|3\|M\|-\|7` — gruppo 8, rappresentante |

**Composizione.** "ASCOLTA BENE." in nero maiuscolo su casella arancione piena — è marcato **H1**,
non decorazione (a differenza del "GET. SHIT. DONE." della Tavola 3): è il secondo H1 della pagina,
dopo quello dell'hero. Sotto, tre paragrafi che ribadiscono "Non sai usarlo", poi il sottotitolo
"Questi stronzi investono miliardi" con lo screenshot reale di un articolo (Punto Informatico) su
un funding OpenAI da $110 miliardi, e tre caselle scure coi tre investitori (Amazon $50B, Nvidia
$30B, SoftBank $30B). Chiude con "110 MILIARDI!!! E tu pensi che sto modello AI non sia capace
di... Rivedere i tuoi banali documenti?! Ma per favore."

**Effetti attivi.** Nessuno oltre al colore pieno arancione della casella titolo.

**Perché è costruita così.** Usare un **secondo H1** a metà pagina (tecnicamente scorretto per la
gerarchia semantica classica, ma qui deliberato) segnala che l'autore tratta ogni sezione-shock
come un nuovo "inizio" retorico, non come continuazione. La prova ($110B) non dimostra che il
corso funzioni: dimostra che l'AI è seria — sposta l'obiezione da "l'AI è una moda" a "io non la so
usare", preparando il terreno alla sezione successiva (Tavola 10).

---

## TAVOLA 9 — Il tris di autodiagnosi con numeri arancioni
![sezione 10](../capture/12-claude-speedrun-v2/sezioni/10-l-ai-pi-capace-di-quanto-pensi-ecc.png)

**Ruolo:** segmentazione delle obiezioni — tre motivi tipici per cui il lettore non ha ancora agito.

| Campo | Valore |
|---|---|
| y / altezza | 7845px / 875px — **2,6%** |
| Sfondo | `#f9f9f9` (bg-brand-grey) |
| Heading | H3 multiplo: titolo + "Roba ganza… Poco utile" + "Non ti fidi dell'AI" + "L'hype ti sembra una cagata" + "ERO CONFUSO QUANTO TE…" |
| Blocchi di testo | 12 |
| Parole | 132 — **densità 15**, fra le più alte della pagina |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.bg-brand-grey\|1\|-\|-\|4` — gruppo 10, rappresentante |

**Composizione.** Tre voci numerate 1-2-3 in cerchi arancioni pieni, ciascuna con un titolo in
grassetto e 2-3 righe di corpo, poi la chiusura in corsivo/grassetto "ERO CONFUSO QUANTO TE… Poi
gli ai lord mi hanno illuminato" a fare da cerniera verso la sezione successiva.

**Effetti attivi.** Nessuno; solo tipografia e colore (cerchi `#fb4604`).

**Perché è costruita così.** I tre motivi non sono generici: "non ti fidi" viene disinnescato con
un'autoironia diretta ("Lo stupido sei tu LOL. JK, semplicemente non sai usarlo") — la stessa mossa
retorica della Tavola 6, ripetuta con variazione lessicale per non stancare chi ha già letto la
prima.

---

## TAVOLA 10 — Il meme "tre teste" e la prova di cancellazione
![sezione 11](../capture/12-claude-speedrun-v2/sezioni/11-ho-trovato-una-tua-foto.png)

**Ruolo:** prova concreta e verificabile — l'autore mostra di aver disdetto ChatGPT Plus davvero.

| Campo | Valore |
|---|---|
| y / altezza | 8720px / 1020px — **3,0%** |
| Sfondo | `#f9f9f9` |
| Heading | H3 "Ho trovato una tua foto:" + "Stai usando gli AI migliori???" |
| Blocchi di testo | 5 |
| Parole | 46 |
| Media | 2 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|3\|M\|-\|5` — gruppo 11, rappresentante |

**Composizione.** Un meme fotografico (dipinto classico a tre teste sovrapposte, sottotitolo "tu
che parli con chatgpt") seguito da "Stai usando gli AI migliori???", "Opinione personale: ChatGPT
è mid.", e uno screenshot reale dell'app ChatGPT con l'avviso rosso "You have cancelled your
subscription. Your subscription ended on 27 February." Chiude con "Ho sostituito ChatGPT con
Claude — E per l'amor del cielo, è la migliore scelta della mia vita."

**Effetti attivi.** Nessuno.

**Perché è costruita così.** Lo screenshot di cancellazione reale è **prova verificabile in prima
persona**, diversa dalla prova statistica della Tavola 8: qui l'autore mette in gioco la propria
credibilità con un artefatto che chiunque riconosce (l'interfaccia di ChatGPT), molto più
convincente di un'affermazione generica "preferisco Claude".

---

## TAVOLA 11 — Il doppio meme comparativo ChatGPT/Claude
![sezione 12](../capture/12-claude-speedrun-v2/sezioni/12-la-mia-vita-con-chatgpt.png)

**Ruolo:** contrasto diretto fra i due prodotti, in forma di meme fotografico a due pannelli.

| Campo | Valore |
|---|---|
| y / altezza | 9740px / 846px — **2,5%** |
| Sfondo | `transparent` (nero) |
| Heading | H3 "La mia vita con ChatGPT:" + "Con Claude, invece…" |
| Blocchi di testo | 5 |
| Parole | 47 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|3\|M\|-\|4` — gruppo 12, rappresentante |

**Composizione.** Meme a due riquadri (stesso format "distracted"/reaction, foto di un ragazzo che
passa dal sorriso alla delusione) con didascalie "Chiedo una cosa a ChatGPT sperando sia utile..."
/ "'Eccoti una guida step by step per..' (o almeno 30 '–')" — poi "Con Claude, invece..." e la
chiusura arancione "Ma non è questione di ChatGPT VS Claude. **È questione di come lo usi.**"

**Effetti attivi.** Nessuno.

**Perché è costruita così.** La frase finale in arancione è una **ammissione di onestà
calcolata**: dice esplicitamente che il prodotto non è la variabile decisiva, il metodo lo è —
posizionando il corso stesso (non Claude) come vero oggetto della vendita. È coerente col titolo
del corso ("come io uso Claude"), non un contenuto neutro.

---

## TAVOLA 12 — L'interstiziale arancione "Hai COMPETITOR"
![sezione 13](../capture/12-claude-speedrun-v2/sezioni/13-hai-competitor-e-non-lo-sai.png)

**Ruolo:** cambio di ritmo — blocco pieno-colore, brevissimo, fra due sezioni lunghe.

| Campo | Valore |
|---|---|
| y / altezza | 10586px / 431px — **1,3%**, la più bassa fra le sezioni piene di contenuto |
| Sfondo | `#fb4604` (bg-brand-orange, colore pieno) |
| Heading | H1 "Hai COMPETITOR e non lo sai" |
| Blocchi di testo | 4 |
| Parole | 75 — **densità 17**, seconda più alta della pagina |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.bg-brand-orange\|1\|-\|-\|2` — gruppo 13, rappresentante |

**Composizione.** Titolo bianco+nero misto su fondo arancione pieno, un filetto verticale bianco a
sinistra del corpo, due paragrafi: uno aggressivo ("sarei Elon adesso... È una cavolata."), uno
definitorio ("Un competitor = una persona che i tuoi clienti potrebbero scegliere al posto tuo.").

**Effetti attivi.** Nessuno: il colore pieno è l'unico effetto, e basta.

**Perché è costruita così.** È il terzo H1 della pagina, e la sezione più corta in altezza fra
quelle con testo reale (431px contro una media di ~900px): un blocco-lampo, pensato per essere
letto in pochi secondi di scroll veloce, non per essere studiato. Il fondo pieno arancione — colore
altrove riservato a piccoli accenti (badge, cerchi, CTA) — qui diventa **sfondo intero**: l'unica
sezione della pagina dove questo accade, segnale di massima urgenza percepita.

---

## TAVOLA 13 — La statistica "18 notizie" con placeholder mancante (e la sua variante, i=28)
![sezione 14](../capture/12-claude-speedrun-v2/sezioni/14-negli-ultimi-7-giorni-sono-uscite.png)

**Ruolo:** urgenza temporale — quanto velocemente cambia il campo, e quanto il lettore rischia di restare indietro.

| Campo | Valore |
|---|---|
| y / altezza | 11017px / 889px — **2,6%** |
| Sfondo | `transparent` (nero) |
| Heading | H3 "Negli ultimi 7 giorni sono uscite 18 notizie sull'AI" + "Voglio darti il vantaggio che ti serve" |
| Blocchi di testo | 6 |
| Parole | 42 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|1\|M\|-\|4` — **gruppo 14, rappresentante** |

**Composizione.** Titolo, poi "I tuoi competitor lo sanno. Tu no." in bianco/arancione, un
**riquadro nero vuoto** (bordato, senza contenuto visibile — lo stesso fenomeno di media non
caricato delle Tavole 4 e 5) al posto del media dichiarato, e la chiusura "Voglio darti il
vantaggio che ti serve... Mostrarti esattamente come io (titolare AP Sales) uso l'AI."

### La variante — i=28 (stessa firma, non rappresentante)
![sezione 28](../capture/12-claude-speedrun-v2/sezioni/28-top-motivi-per-comprare.png)

Sezione i=28, y=25961 h=707 (**2,1%**), heading H3 "Top motivi per comprare" — **stessa firma**
(`section|w-full.py-24.border-t|1|M|-|4`, gruppo 14). Qui il media *è* renderizzato: un riquadro
bianco con la coppia di meme gattino-che-piange/gattino-in-piedi sotto l'etichetta "#1", primo di
una sequenza a countdown che prosegue nella Tavola successiva (i=29, "#2").

**Effetti attivi (entrambe).** Nessuno oltre al colore.

**Perché è costruita così.** Il confronto fra le due sezioni della stessa firma è istruttivo: la
struttura (titolo + occhiello + riquadro media) è identica, ma in un caso il riquadro è vuoto per
mancato caricamento (Tavola 13) e nell'altro contiene il payload reale (meme "#1"). Conferma che
qui il "buco nero" è un problema di tempismo della cattura, non di progettazione — la stessa gabbia
regge contenuti diversi senza rompersi.

---

## TAVOLA 14 — Il tris di pillole "Strumenti / Strategia / Context"
![sezione 15](../capture/12-claude-speedrun-v2/sezioni/15-caaaazzo-ma-allora-non-inutile.png)

**Ruolo:** cerniera fra la parte-diagnosi e la parte-soluzione — introduce la tassonomia del metodo.

| Campo | Valore |
|---|---|
| y / altezza | 11906px / 799px — **2,4%** |
| Sfondo | `#f9f9f9` (bg-brand-white) |
| Heading | H3 `"CAAAAZZO… Ma allora non è inutile…"` + "Strumenti" |
| Blocchi di testo | 16 |
| Parole | 86 |
| Media | 1 |
| CTA | 3 — tre pillole cliccabili |
| Firma / gruppo | `section\|w-full.py-24.bg-brand-white\|1\|M\|C\|4` — gruppo 15, rappresentante |

**Composizione.** Citazione datata ("domenica 1 marzo 2026"), lista puntata di risultati ("Realmente
usabile", "No errori", "Considerando tutte le info che gli ho dato"), poi "Ecco però il punto
dolente: Non è bastato un messaggio. Mi è servita un'intera cartella con:" seguito da tre pulsanti
a barra (Strumenti attivo in arancione pieno, Strategia e Context in grigio scuro) — un selettore
di tab, non tre CTA di uscita: cliccando si scopre il contenuto sotto (qui solo "Strumenti" è
espanso, con testo "Gli strumenti giusti configurati nel modo giusto...").

**Effetti attivi.** Cambio di stato dei pulsanti (attivo=arancione, inattivo=grigio) — un
componente tab nativo, coerente con l'assenza di `dialog`/`accordion` dedicati per questa sezione
nell'indice sorgente.

**Perché è costruita così.** Introdurre la tassonomia in tre pilastri (Strumenti/Strategia/Context)
qui, prima ancora della lista lezioni (Tavola 20), prepara il lettore a riconoscere la stessa
struttura quando la incontrerà nel curriculum — coerenza narrativa fra promessa e contenuto
mostrato.

---

## TAVOLA 15 — Le tre applicazioni concrete con numeri translucidi
![sezione 16](../capture/12-claude-speedrun-v2/sezioni/16-ecco-esattamente-come-l-ai-sta-aiu.png)

**Ruolo:** prova di applicazione reale — tre casi d'uso specifici nell'agenzia dell'autore.

| Campo | Valore |
|---|---|
| y / altezza | 12705px / 637px — **1,9%** |
| Sfondo | `transparent` (nero) |
| Heading | H3 "Ecco esattamente come l'AI sta aiutando la mia azienda… Oggi stesso." + tre sotto-titoli |
| Blocchi di testo | 17 |
| Parole | 111 — **densità 17**, fra le più alte |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|1\|-\|-\|3` — gruppo 16, rappresentante |

**Composizione.** Tre card affiancate ("Il mio calendario", "Ricerca per i clienti", "Copy per Meta
Ads"), ciascuna con un numero gigante translucido (1/2/3) in filigrana nell'angolo e una frase
breve di risultato ("Analisi di mercato e competitor in 10 minuti invece che in 2 giorni").

**Effetti attivi.** I numeri in filigrana sono probabilmente `opacity` bassa su testo enorme —
nessuna animazione dichiarata.

**Perché è costruita così.** Contare "10 minuti invece che 2 giorni" è la prima cifra di risparmio
tempo dell'intera pagina — precede il calcolo esplicito di produttività che arriverà molto più
avanti (Tavola 27), preparandolo con un esempio concreto prima dell'astrazione matematica.

---

## TAVOLA 16 — La biografia dell'autore su fondo scuro pieno
![sezione 17](../capture/12-claude-speedrun-v2/sezioni/17-per-mesi-mi-sono-sentito-indietro.png)

**Ruolo:** autorità personale — chi parla, e perché ha credibilità.

| Campo | Valore |
|---|---|
| y / altezza | 13342px / 965px — **2,9%** |
| Sfondo | `#202021` — **unico uso di questo grigio-quasi-nero in tutta la pagina** |
| Heading | H3 lungo + "ANDREI PASCU…. L'UOMO DEI TUOI SOGNI (sì, anche se sei etero)" |
| Blocchi di testo | 10 |
| Parole | 149 — **la più alta densità testuale (15) fra le sezioni lunghe** |
| Media | 3 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24\|1\|M\|-\|5` — gruppo 17, rappresentante |

**Composizione.** Titolo-cerniera in due frasi, poi il titolo ironico sul nome, un paragrafo bio
completo: età (24 anni), percorso (mollata la scuola a 18, copywriter, poi agenzia AP Sales), cifre
(Copywriting Mentorship: 3.600+ ordini, 1.500+ studenti), e link social ("@andrei.bsns su TikTok
270K+ follower").

**Effetti attivi.** Nessuno oltre al colore di sfondo distinto.

**Perché è costruita così.** Il colore di sfondo unico (`#202021`, non riutilizzato altrove)
funziona come "stanza a parte": segnala visivamente che qui si esce dal ritmo persuasivo per un
momento di autorità/credenziali, prima di rientrare nel flusso di vendita.

---

## TAVOLA 17 — Il primo biglietto "Claude Speedrun" completo
![sezione 18](../capture/12-claude-speedrun-v2/sezioni/18-claude-speedrun.png)

**Ruolo:** presentazione formale del prodotto come artefatto fisico (il "biglietto").

| Campo | Valore |
|---|---|
| y / altezza | 14307px / 653px — **1,9%** |
| Sfondo | `transparent` (nero) |
| Heading | H3 "Claude Speedrun" |
| Blocchi di testo | 7 |
| Parole | 74 |
| Media | 4 |
| CTA | 1 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|1\|M\|C\|3` — gruppo 18, rappresentante |

**Composizione.** Logo "🏃 claude 2" centrato, sotto il "biglietto" (foto di un templare con
ascia in armatura, cornice arancione, etichetta "2 claude speedrun / WORKFLOW UPDATE", riquadro
nero "BIGLIETTO" con QR code), poi due CTA: piena arancione "Iscriviti adesso" e a contorno "Cosa
contiene il corso?" (quest'ultimo apre presumibilmente un `<dialog>`, coerente con lo stesso
pattern osservato su apsales.eu).

**Effetti attivi.** Nessuno oltre al colore.

**Perché è costruita così.** Il biglietto trasforma un prodotto digitale (video-corso) in un
oggetto da collezione tangibile — stessa logica del biglietto di armageddon.bsns.it (stesso
ecosistema Andrei Pascu), qui riproposto identico nel concept ma con grafica diversa (cavaliere +
ascia invece di scheletro + spada), a conferma che è un **pattern di prodotto ricorrente** nella
scuderia dell'autore, non un'invenzione isolata.

---

## TAVOLA 18 — Il muro persuasivo "Perché quei €249 sono ancora sulla tua carta"
![sezione 19](../capture/12-claude-speedrun-v2/sezioni/19-perch-quei-249-sono-ancora-sulla-t.png)

**Ruolo:** il blocco di copy più denso e diretto della pagina — obiezione al prezzo affrontata di petto.

| Campo | Valore |
|---|---|
| y / altezza | 14960px / 1421px — **4,2%**, seconda sezione più densa di testo |
| Sfondo | `transparent` (nero) |
| Heading | H3 "Perché quei €249 sono ancora sulla tua carta???" |
| Blocchi di testo | 18 |
| Parole | 182 — **il testo continuo più lungo di tutta la pagina** |
| Media | 2 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|1\|M\|-\|7` — gruppo 19, rappresentante |

**Composizione.** Icona carta di credito arancione, titolo, un lungo blocco narrativo in prima
persona (il racconto delle difficoltà iniziali di AP Sales, le citazioni social invidiate — "Ho
appena fatto €100k con la mia agency" — e la rivelazione "potrebbero star usando strumenti che tu
non usi"), chiuso da un diagramma a freccia orizzontale con tre nodi: BROKIE (sinistra, "indietro")
— TU (centro, cerchiato) — COMPETITOR (destra, "avanti"), con "sei qui" sotto il cerchio centrale.

**Effetti attivi.** Nessuno oltre al colore sulle frecce e sul cerchio "TU".

**Perché è costruita così.** Il diagramma BROKIE→TU→COMPETITOR è l'unica visualizzazione
posizionale (non numerica) di tutta la pagina: mette il lettore fisicamente al centro di un asse,
rendendo tangibile lo status quo come punto di partenza reversibile in entrambe le direzioni — un
frame più efficace di un semplice elenco puntato per motivare l'azione immediata.

---

## TAVOLA 19 — La citazione scettica con link alla storia personale
![sezione 20](../capture/12-claude-speedrun-v2/sezioni/20-andrei-chiunque-tu-sia-senti-parl.png)

**Ruolo:** disinnesco preventivo dello scetticismo, in forma di domanda retorica messa in bocca al lettore.

| Campo | Valore |
|---|---|
| y / altezza | 16381px / 704px — **2,1%** |
| Sfondo | `transparent` (nero) |
| Heading | H3 `"Andrei, chiunque tu sia… Senti. Parli tanto. Ma chi pensi di essere???"` |
| Blocchi di testo | 7 |
| Parole | 58 |
| Media | 1 |
| CTA | 1 — "Leggi la storia di Andrei Pascu" |
| Firma / gruppo | `section\|w-full.py-24.border-t\|1\|M\|C\|4` — gruppo 20, rappresentante |

**Composizione.** Un piccolo avatar circolare (persona con binocolo, foto reale) accanto alla
citazione-obiezione, poi la battuta autoironica ("Dammi €249 e scoprilo"), la correzione seria ("Ok
a parte gli scherzi"), e un box-link bordato con icona libro: "Leggi la storia di Andrei Pascu —
Clicca per scoprire chi c'è dietro questo corso".

**Effetti attivi.** Nessuno.

**Perché è costruita così.** Mettere l'obiezione ("chi pensi di essere") **nelle parole del
lettore stesso**, come se fosse lui a parlare, è una tecnica di ventriloquio persuasivo: disarma
prima che il lettore la formuli davvero, e la battuta scherzosa sul prezzo (€249 per "scoprirlo")
abbassa la tensione prima del link serio.

---

## TAVOLA 20 — Il confronto sintetico ORA / CON Claude
![sezione 21](../capture/12-claude-speedrun-v2/sezioni/21-section.png)

**Ruolo:** riepilogo visivo del prima/dopo, con secondo biglietto sullo sfondo.

| Campo | Valore |
|---|---|
| y / altezza | 17084px / 986px — **2,9%** |
| Sfondo | `transparent` |
| Heading | nessuno |
| Blocchi di testo | 2 |
| Parole | 6 |
| Media | 3 |
| CTA | 2 |
| Firma / gruppo | `section\|relative.w-full.py-24\|3\|M\|C\|5` — gruppo 21, rappresentante |

**Composizione.** Colonna sinistra grigia "ORA" (pallino vuoto) con due righe negative ("Fai una
richiesta a ChatGPT / ma il risultato non ti soddisfa", "Fai tutto a mano... mentre quelli che ti
superano vanno il doppio più veloce"); colonna destra arancione "CON claude" (pallino pieno) con
due righe positive ("Risultati usabili / buoni al primo colpo", "Superi competitor / fai più cose
in meno tempo"). Sullo sfondo, appena visibile, un secondo esemplare del biglietto "claude 2" già
visto in Tavola 17 — **stesso asset visivo riusato in due punti diversi della pagina**.

**Effetti attivi.** Nessuno oltre al colore (grigio vs arancione) a marcare i due stati.

**Perché è costruita così.** La ripetizione del biglietto come sfondo qui (dopo averlo mostrato in
primo piano alla Tavola 17) rinforza l'oggetto-simbolo del prodotto senza doverlo ridescrivere: il
lettore lo riconosce già, e la sua presenza (anche defilata) richiama l'acquisto senza bisogno di
nuove parole.

---

## TAVOLA 21 — L'indice lezioni: la sezione più lunga della pagina
![sezione 22](../capture/12-claude-speedrun-v2/sezioni/22-lista-lezioni.png)

**Ruolo:** il "menu" del prodotto — prova di sostanza tramite curriculum dettagliato.

| Campo | Valore |
|---|---|
| y / altezza | 18070px / 2838px — **8,4%**, seconda sezione più alta di tutta la pagina |
| Sfondo | `#0a0a0a` |
| Heading | H3 "Lista lezioni" + "LEZIONI DI CLAUDE SPEEDRUN 2" + "ALTRE LEZIONI INCLUSE" + "LE BASI" + "AI PER PENSARE" + "COME CI SCRIVO COPY" |
| Blocchi di testo | 89 — **il valore più alto di tutta la pagina** |
| Parole | 237 |
| Media | 15 |
| CTA | 8 |
| Firma / gruppo | `section\|w-full.py-24.relative\|2\|M\|C\|14` — gruppo 22, rappresentante |

**Composizione.** Occhiello "Una lezione nuova ogni giorno, dal 16 luglio..." più nota a piè
"fino a completamento lezioni", un box-anteprima ("Claude Speedrun 2, in due righe: i workflow che
uso ADESSO..."), badge verde "✦ NUOVE LEZIONI", poi dieci righe numerate in numeri romani (I-X) con
etichetta "NEW" verticale verde, titolo lezione e data di rilascio scalare (16-25 LUG) — righe
alternate arancione/nero. Sotto, "ALTRE LEZIONI INCLUSE" con tre sotto-categorie (LE BASI, AI PER
PENSARE, COME CI SCRIVO COPY), ciascuna riga con icona (omino corsa o fiore/asterisco), numero
romano, titolo, e pillola "Contenuto?" (alternata chiara/scura). Chiude con "Mostra tutte le 21
lezioni E le 6 bonus gratuite" e freccia d'espansione.

**Effetti attivi.** Nessuna animazione dichiarata specificamente qui, ma il componente
`LessonList` (20.294 byte, secondo file JS più pesante fra i componenti nominati) implica logica
di stato — filtro, espansione, forse tracciamento progressione, coerente col peso del file.

**Perché è costruita così.** La numerazione romana (non 1,2,3) segnala "capitoli" più che "task"
— un registro quasi editoriale/da manuale, coerente con l'idea di corso strutturato e non di
playlist casuale. Il rilascio scalare per data (16, 17, 18... luglio) crea un calendario di
consumo che allunga l'impegno percepito del cliente oltre il giorno dell'acquisto — un meccanismo
di retention integrato nel curriculum stesso, non aggiunto dopo.

---

## TAVOLA 22 — La griglia "Skills" bloccata (curiosity gap puro)
![sezione 23](../capture/12-claude-speedrun-v2/sezioni/23-skills.png)

**Ruolo:** teaser — 11 competenze annunciate ma non rivelate, per generare desiderio d'acquisto.

| Campo | Valore |
|---|---|
| y / altezza | 20909px / 991px — **2,9%** |
| Sfondo | `#0a0a0a` |
| Heading | H3 "Skills" |
| Blocchi di testo | 26 |
| Parole | 35 — pochissimo testo per 11 riquadri |
| Media | 11 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-20.md:py-24\|2\|M\|-\|5` — gruppo 23, rappresentante |

**Composizione.** Badge verde "✦ NOVITÀ", occhiello "INCLUSE NEL CORSO", H3 "Skills", sottotitolo
("Nuove skill di Claude pronte all'uso, svelate una alla volta insieme alle lezioni. E ne stiamo
aggiungendo altre."), e una griglia 4×3 (11 celle) dove **ogni singola icona è una sagoma arancione
sfocata su fondo nero** — un'ascia, una figura incappucciata, una croce, delle forbici, un fucile,
degli occhiali, una figura accovacciata, una figura in piedi, un lupo/cane in corsa, una lancia, un
buco nero — ciascuna etichettata solo `???`.

**Effetti attivi.** Le sagome sono probabilmente la stessa tecnica di boost/contrasto (`Ascii` o
simile) vista su apsales.eu, applicata qui a icone invece che a fotografie — coerente con la
palette-sfondi che elenca `#fb4604 @0.1`/`@0.15`/`@0.2`/`@0.3` a bassa opacità, tipica di
silhouette arancioni su nero.

**Perché è costruita così — il meccanismo, non la descrizione.** Undici incognite senza nemmeno un
nome parziale (non "??? — persuasione" ma proprio "???" nudo) è un curiosity gap calibrato al
massimo: **non c'è nessuna informazione da cui dedurre il contenuto**, solo una forma vaga che
suggerisce un tema (armi, animali, simboli) senza chiarirlo. È strutturalmente diverso dal FOMO
temporale (Tavola 12-13): qui la leva è la curiosità pura, non l'urgenza.

---

## TAVOLA 23 — Il muro di recensioni verificate
![sezione 24](../capture/12-claude-speedrun-v2/sezioni/24-cosa-dicono-i-membri.png)

**Ruolo:** prova sociale quantificata — voto aggregato più testimonianze nominali.

| Campo | Valore |
|---|---|
| y / altezza | 21900px / 1123px — **3,3%** |
| Sfondo | `#f9f9f9` |
| Heading | H3 "Cosa dicono i membri" |
| Blocchi di testo | 27 |
| Parole | 180 |
| Media | 59 — **il valore più alto di tutta la pagina** (stelle, badge, avatar) |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-16.md:py-24\|1\|M\|-\|6` — gruppo 24, rappresentante |

**Composizione.** Titolo, punteggio aggregato "★★★★★ 4,9/5" con sottotesto "su 14 recensioni
verificate dei membri", poi una griglia di card (2-3 colonne) con recensioni reali firmate
(Lorenzo, Donato, Simone Maiolino, Shanthosh, Croma_555, Alex...) ciascuna con badge verde
"Recensione verificata" e stelle proprie — **una card mostra 4 stelle su 5**, non tutte a 5: un
dettaglio di credibilità (recensioni non tutte massime).

**Effetti attivi.** Nessuno oltre al colore delle stelle (arancione pieno) e del badge di verifica
(verde).

**Perché è costruita così.** Includere una recensione a 4 stelle in mezzo a tredici a 5 stelle è
una scelta deliberata di credibilità: un mucchio di recensioni tutte perfette insospettisce più di
uno con qualche imperfezione dichiarata — coerente con la stessa logica di "concessione
all'avversario" vista nella tabella comparativa di apsales.eu (dossier 13).

---

## TAVOLA 24 — Il carosello esterno "Marius" (cross-sell incorporato)
![sezione 25](../capture/12-claude-speedrun-v2/sezioni/25-section.png)
![sezione 26](../capture/12-claude-speedrun-v2/sezioni/26-claude-speedrun-per-chi-lavora-nel.png)

**Ruolo:** prova di applicazione settoriale — e, di fatto, promozione incrociata di un prodotto terzo.

| Campo | Sezione 25 | Sezione 26 |
|---|---|---|
| y / altezza | 23024px / 1003px (**3,0%**) | 24026px / 1247px (**3,7%**) |
| Sfondo | `transparent` | `transparent` |
| Heading | nessuno | H3 "Claude Speedrun per chi lavora nel marketing" |
| Blocchi di testo | 0 | 8 |
| Parole | 0 | 20 |
| Media | 1 | 6 |
| Firma / gruppo | gruppo 25, rappresentante | gruppo 26, rappresentante |

**Composizione.** Le due sezioni sono adiacenti e visivamente continue: un carosello con frecce
sinistra/destra e quattro pallini di paginazione mostra la pagina web di **un consulente esterno**
("Marius", tema giallo/nero, "Trasforma il tuo business con Amazon", con un embed video Loom
"Trasforma il tuo business con Amazon" e una sezione "Consulenza gratuita" con widget Calendly) —
un sito completamente diverso per palette e font da claude-speedrun.com. Il testo di cornice
(sezione 26) recita "Io stesso sono un marketer. Ho un'agenzia, ho clienti in tutte le industrie."

**Effetti attivi.** Carosello con navigazione a frecce e paginazione a pallini — nessun dettaglio
di libreria rilevabile dal solo screenshot.

**Perché è costruita così — la scoperta di questa tavola.** Questo non è un caso studio interno:
è **l'incorporazione della landing di un cliente/studente terzo** (con il suo brand, il suo CTA
Calendly, la sua offerta "Amazon Wholesale") dentro la pagina di vendita di Claude Speedrun, come
prova che "i miei metodi funzionano anche per chi fa altro". È un pattern di prova sociale mai
visto negli altri rapporti di questo studio: non uno screenshot statico di risultato, ma un
**iframe/carosello di un sito esterno realmente navigabile**, incastonato nel funnel.

---

## TAVOLA 25 — La spirale ipnotica "Compra Claude Speedrun"
![sezione 27](../capture/12-claude-speedrun-v2/sezioni/27-non-ti-ho-ancora-convinto.png)

**Ruolo:** CTA in forma di illusione ottica — il componente `SectionSpirale` finalmente visibile.

| Campo | Valore |
|---|---|
| y / altezza | 25274px / 688px — **2,0%** |
| Sfondo | `#f9f9f9` (bg-brand-white) |
| Heading | H3 "Non ti ho ancora convinto?..." |
| Blocchi di testo | 1 |
| Parole | 9 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.bg-brand-white\|1\|M\|-\|3` — gruppo 27, rappresentante |

**Composizione.** Titolo, sottotitolo "Vediamo se questo funziona:", e un riquadro con una spirale
ipnotica bianco/nero (anelli concentrici che convergono verso il centro) con al centro, in un
bagliore arancione, il testo "Compra Claude Speedrun".

**Effetti attivi.** Il file sorgente `SectionSpirale-q8CvNpni.js` (661 byte, il più leggero fra i
componenti nominati) suggerisce un'animazione CSS pura, probabile rotazione continua o pulsazione
del bagliore centrale — coerente con l'effetto ipnotico visibile anche nel singolo fotogramma
statico.

**Perché è costruita così.** È l'unico momento della pagina dove la persuasione diventa
letteralmente un trucco ottico dichiarato ("Vediamo se questo funziona") — un momento di
autoironia sulla manipolazione stessa, che disinnesca la sospetta aggressività del messaggio
mostrando di conoscerla e giocarci sopra.

---

## TAVOLA 26 — Il countdown "Top motivi per comprare #2": la lezione di produttività
![sezione 29](../capture/12-claude-speedrun-v2/sezioni/29-la-produttivit-non-questo.png)

**Ruolo:** la sezione più elaborata della pagina dopo l'indice lezioni — dimostrazione matematica del valore.

| Campo | Valore |
|---|---|
| y / altezza | 26668px / 3144px — **9,3%, la sezione più alta di tutta la pagina** |
| Sfondo | `transparent` (nero) |
| Heading | H3 "La produttività NON è questo:" + "La produttività è questa:" + "PENSACI" |
| Blocchi di testo | 13 |
| Parole | 67 — **densità 2, la più bassa fra le sezioni con contenuto sostanziale** (molto spazio, poco testo per pixel) |
| Media | 3 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.border-t\|1\|M\|-\|16` — gruppo 29, rappresentante (prof=16, il valore di annidamento più alto della pagina) |

**Composizione.** "#2" in apertura (continua il countdown iniziato in Tavola 13-variante), tre
righe fotografiche di "falsa produttività" (doccia fredda alle 5am, jogging con podcast, laptop in
un furgone) ciascuna con foto reale + didascalia ironica, poi "La produttività è questa: (ed è
calcolabile)" con la formula "Produttività = robe utili che fai / unità di tempo", un grafico a
barre orizzontali (Giorno 1: 6 articoli in 2 ore, barra grigia; Giorno 2: 10 articoli in 2 ore,
barra arancione, più lunga), un riquadro di calcolo (Senza Claude 6/2=3 articoli/ora → Con Claude
10/2=5 articoli/ora), la conclusione "Nel giorno 2 sei stato **66% più produttivo**", "PENSACI", e
infine un riquadro bianco con "Ma come fa... a fare così tanto..." e un'emoji sorpresa.

**Effetti attivi.** Nessuno oltre al colore (barra arancione vs grigia).

**Perché è costruita così — il meccanismo che vale.** La formula esplicita
(produttività=output/tempo) e il calcolo passo-passo (6/2=3 → 10/2=5 → +66%) trasformano una
promessa vaga ("lavori meglio con l'AI") in un'equazione verificabile con numeri piccoli e
memorizzabili. È l'unico punto di tutta la pagina dove la persuasione passa per l'aritmetica
esplicita invece che per l'aneddoto o il meme — un registro deliberatamente diverso, forse per
raggiungere il lettore più analitico che le sezioni precedenti (tutte a base di tono/meme) non
avrebbero convinto.

---

## TAVOLA 27 — "Perché Claude e non altri?" con prova SERP
![sezione 30](../capture/12-claude-speedrun-v2/sezioni/30-perch-claude-e-non-altri.png)

**Ruolo:** giustificazione della scelta di piattaforma, con fonte esterna verificabile.

| Campo | Valore |
|---|---|
| y / altezza | 29813px / 736px — **2,2%** |
| Sfondo | `#f9f9f9` |
| Heading | H3 "Perché Claude e non altri?" |
| Blocchi di testo | 8 |
| Parole | 53 |
| Media | 6 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-24.bg-[hsl(var(--brand-white))]\|1\|M\|-\|4` — gruppo 30, rappresentante |

**Composizione.** Frase introduttiva, poi la riproduzione di un vero risultato Google/Fanpage
("Claude batte ChatGPT tra le app più scaricate: quali sono...", datato 4 mar 2026), e una lista
puntata con quattro segni di spunta arancioni: "Risposte meno cringe", "Meno spam di '-'", "No 'in
qualità di AI, non posso...'", "Dà meno la sensazione di *AI Slop*".

**Effetti attivi.** Nessuno.

**Perché è costruita così.** Riprodurre un vero snippet di ricerca (non solo citarlo a parole) dà
un livello di verificabilità superiore: il lettore può, in teoria, cercare la stessa frase e
trovare l'articolo — un artefatto di terze parti usato come prova, esattamente come lo screenshot
di cancellazione ChatGPT della Tavola 10.

---

## TAVOLA 28 — Il riepilogo checklist "Cosa ottieni se entri adesso"
![sezione 31](../capture/12-claude-speedrun-v2/sezioni/31-cosa-ottieni-se-entri-adesso.png)

**Ruolo:** riepilogo pre-CTA — tutta l'offerta condensata in una lista di spunte.

| Campo | Valore |
|---|---|
| y / altezza | 30549px / 1041px — **3,1%** |
| Sfondo | `#1a1a1a` (bg-card) |
| Heading | H3 "Cosa ottieni se entri adesso" |
| Blocchi di testo | 13 |
| Parole | 43 |
| Media | 11 — le 11 icone di spunta |
| CTA | 1 — "Iscriviti adesso" con bagliore arancione |
| Firma / gruppo | `section\|w-full.py-24.bg-card\|1\|M\|C\|5` — gruppo 31, rappresentante |

**Composizione.** Un riquadro bordato con dieci righe (30+ lezioni, Nuove skill di Claude,
Riassunti usabili, Quiz PDF, Contenuti extra, Tutorial completi, Workflow copiabili, Niente lezioni
noiose, Tutte le lezioni sono editate, Tutte le lezioni sono veloci, Andiamo dritto al punto),
ciascuna con un'icona di spunta arancione in cerchio, poi il pulsante "Iscriviti adesso" con
bagliore visibile (`shadow: rgba(251,70,4,0.3) 0px 0px 40px 0px`, misurato nell'array `ombre` di
`scheda.json`).

**Effetti attivi.** Bagliore arancione (`box-shadow` diffuso, non un blur CSS del filtro) sul
pulsante, coerente con la voce ombre a colore `rgba(251,70,4,*)` più ricorrente della pagina.

**Perché è costruita così.** Riportare "andiamo dritto al punto" come ultimo punto di una lista di
dieci — dopo nove item concreti — è un rinforzo di posizionamento (contro l'accusa implicita che i
corsi online sono lenti e pieni di riempitivo), messo a chiusura elenco dove resta più impresso.

---

## TAVOLA 29 — Le 16 domande frequenti
![sezione 32](../capture/12-claude-speedrun-v2/sezioni/32-faq.png)

**Ruolo:** rimozione delle ultime obiezioni pratiche prima dell'acquisto.

| Campo | Valore |
|---|---|
| y / altezza | 31590px / 1495px — **4,4%** |
| Sfondo | `transparent` (nero) |
| Heading | H2 "FAQ" + le 16 domande come H3 |
| Blocchi di testo | 33 |
| Parole | 106 |
| Media | 16 — le 16 icone chevron |
| CTA | 16 — i 16 trigger dell'accordion |
| Firma / gruppo | `section\|w-full.py-24\|1\|M\|C\|7` — gruppo 32, rappresentante |

**Composizione.** Titolo H2, poi 16 righe accordion chiuse separate da filetti sottili, ciascuna
con chevron a destra: dalle domande di metodo ("Devo per forza usare Claude?", "Tu sei un esperto
di AI?") a quelle commerciali pure ("Come si fa a pagare con PayPal in 3 rate?", "È un pagamento
unico o pago in maniera ricorrente?").

**Effetti attivi.** Accordion nativo (Radix `accordion-up`/`accordion-down`, stesso pattern misurato
nel report stack), con i 16 CTA che coincidono esattamente con i 16 media (chevron) — nessuna
domanda orfana di trigger.

**Perché è costruita così.** Includere "È un pagamento unico o pago in maniera ricorrente?" come
ultima delle 16 (non fra le prime) è una scelta di sequenza: le domande di fiducia/metodo vengono
prima, quelle più strettamente transazionali dopo, quando il lettore ha già attraversato tutto il
resto della pagina ed è più vicino alla decisione.

---

## TAVOLA 30 — Il Disclaimer come sezione a sé
![sezione 33](../capture/12-claude-speedrun-v2/sezioni/33-disclaimer.png)

**Ruolo:** tutela legale — nessuna promessa di reddito, nessuna garanzia di risultato.

| Campo | Valore |
|---|---|
| y / altezza | 33086px / 388px — **1,1%** |
| Sfondo | `transparent` |
| Heading | H3 "Disclaimer" |
| Blocchi di testo | 5 |
| Parole | 142 — **densità 37, la più alta di tutta la pagina** |
| Media | 0 |
| CTA | 0 |
| Firma / gruppo | `section\|w-full.py-16.border-t\|1\|-\|-\|2` — gruppo 33, rappresentante |

**Composizione.** Quattro paragrafi in grigio: nessuna garanzia di successo, il corso non promette
guadagni ("Non è un corso su come fare soldi"), la responsabilità dell'uso dell'AI (dati clienti,
GDPR) resta dell'utente, e il divieto di rivendita o "gruppi d'acquisto".

**Effetti attivi.** Nessuno — tipografia piccola e compatta, coerente con un blocco letto di rado
ma necessario.

**Perché è costruita così.** La densità di parole per pixel (37) è la più alta della pagina
proprio perché è l'unica sezione dove la compattezza informativa conta più della leggibilità
scenica: qui l'obiettivo non è persuadere, è documentare — stesso principio del disclaimer di
armageddon.bsns.it, dove la larghezza di lettura veniva volutamente allargata (`88ch`) per essere
"letta davvero", non solo presente.

---

## TAVOLA 31 — Il footer
![sezione 34](../capture/12-claude-speedrun-v2/sezioni/34-footer.png)

**Ruolo:** chiusura legale e di navigazione secondaria.

| Campo | Valore |
|---|---|
| y / altezza | 33474px / 282px — **0,8%, la sezione più bassa di tutta la pagina** |
| Sfondo | `transparent` |
| tag | `footer` (non `section`) |
| Heading | nessuno |
| Blocchi di testo | 11 |
| Parole | 27 |
| Media | 1 |
| CTA | 0 |
| Firma / gruppo | `footer\|w-full.py-12.border-t\|1\|M\|-\|1` — gruppo 34, rappresentante |

**Composizione.** Icona arancione "omino che corre" (logo, senza wordmark testuale accanto — a
differenza dell'header), tre colonne di link (Siti: Sito Formazione / Sito Agency; Social:
Instagram / TikTok; Legale: Cookie Policy), poi P.IVA `02001850474` e l'indirizzo "Viale Giacomo
Matteotti 15, Firenze 50121" — **lo stesso indirizzo e la stessa P.IVA misurati sul footer di
apsales.eu** (dossier 13) — e la nota "Questa pagina fa parte del sito www.andrei-copy.com".

**Effetti attivi.** Nessuno.

**Perché è costruita così.** L'indirizzo e la P.IVA identici a quelli di apsales.eu confermano,
con un dato di footer e non di intuito, che **Claude Speedrun e AP Sales sono la stessa entità
legale** — coerente col fatto che l'autore (Andrei Pascu) è lo stesso in entrambi i prodotti, e
che il footer rimanda esplicitamente al sito "andrei-copy.com" come contenitore ombrello di tutto
l'ecosistema.

---

## DELTA ALLA FABBRICA

**CANONE:** Il "biglietto" (artefatto grafico da collezione che rappresenta il prodotto digitale)
compare **due volte nella stessa pagina** in punti distanti (Tavola 17 in primo piano, Tavola 20 in
filigrana di sfondo) — non è un'illustrazione usa-e-getta, è un simbolo ricorrente che la Fabbrica
può adottare come "oggetto-icona" riusabile: un solo asset grafico, mostrato una volta per intero e
poi richiamato in controluce più avanti nella stessa pagina, invece di introdurne uno nuovo ogni
volta che serve rinforzare il ricordo del prodotto.

**PATTERN:** La griglia "Skills" a incognite pure (Tavola 22, 11 celle tutte etichettate "???"
senza nemmeno un indizio testuale parziale) è un pattern di curiosity-gap più estremo di quanto
documentato finora nello studio Andrei Pascu (dove di solito una parola-chiave accompagna il
teaser, es. "Contenuto?" nelle righe lezione). Da portare in Fabbrica Siti come variante
"curiosity-gap totale": utile in pagine dove il prodotto ha un elenco di componenti/moduli/bonus
che si vuole tenere del tutto sigillato fino all'acquisto.

**GATE:** Cinque sezioni su trentaquattro (Tavole 4, 5, la variante i=9, 14 e il riquadro nero della
sua rappresentante) mostrano un **media dichiarato nel DOM ma non renderizzato nello screenshot**
al momento della cattura. Prima di dichiarare un atlante "completo" sulla base di uno strumento di
cattura automatico, va aggiunto un controllo: se `media > 0` in `scheda.json` ma lo screenshot
della sezione è uniforme (varianza di pixel sotto una soglia, o area bianca/nera piatta oltre una
percentuale del riquadro), la sezione va ricatturata prima di scrivere l'atlante, non descritta a
scatola vuota. Qui è stato dichiarato onestamente invece di essere inventato — ma il gate serve a
non doverlo più fare a mano ogni volta.

---

## Connessioni

- [07-claude-speedrun.md](07-claude-speedrun.md) — il primo passaggio: copy, palette, struttura
- [12-claude-speedrun-STACK-E-TOKEN.md](12-claude-speedrun-STACK-E-TOKEN.md) — lo stack (Vite+React), i token, i componenti nominati, il delta di quel giro
- [12-claude-speedrun-COPY.md](12-claude-speedrun-COPY.md) — il teardown del copy sui blocchi di testo
- [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) e [11-armageddon-ATLANTE-VISIVO.md](11-armageddon-ATLANTE-VISIVO.md) — il modello di formato di questo stesso documento
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
