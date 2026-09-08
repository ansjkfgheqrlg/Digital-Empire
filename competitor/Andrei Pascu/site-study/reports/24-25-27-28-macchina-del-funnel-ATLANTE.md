---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #atlante-visivo #funnel #squarespace #onda-b
Created: 2026-09-08
Last updated: 2026-09-08
---

# ATLANTE VISIVO — le quattro pagine-macchina del funnel

**Cosa si vede, non come funziona il funnel né cosa dice il testo.** La meccanica delle catene
`/define → /asa → /copy-base` e `/outfunnel-1` / `/armadeggon-strp` è già scritta in
[24-25-27-28-macchina-del-funnel.md](24-25-27-28-macchina-del-funnel.md); il copy integrale è in
[24-25-27-28-macchina-del-funnel-COPY.md](24-25-27-28-macchina-del-funnel-COPY.md). Questo documento
non ripete né l'uno né l'altro: guarda le quattro schermate come oggetti visivi — dove cade il video, dove
il bottone, quanto spazio vuoto, dove l'accento colorato — con lo stesso metodo di
[13-apsales-ATLANTE.md](13-apsales-ATLANTE.md), aperte una per una con lo strumento di visione. Le quattro
pagine sono cortissime (1.512-1.936px) e ciascuna è **una sola sezione** — non per scelta di
impaginazione ma perché `scheda.json` dichiara `"segmentazione": "fallita"` su tutte e quattro: l'euristica
che divide le pagine con `page-section.layout-engine-section` (usata sulle 12 pagine studiate altrove in
questo ecosistema) non trova alcun elemento di quel tipo qui. Il DOM reale è un solo `<div id="siteWrapper"
class="clearfix site-wrapper">` non segmentato — un indizio di costruzione, non solo di misura: queste
quattro pagine usano un template Squarespace più semplice ("pagina vuota"/freeform) rispetto alle dodici
pagine di vendita a blocchi (`page-section`) studiate nei dossier gemelli. Quattro tavole, una per pagina,
1.500-1.950px ciascuna.

---

## LA CORNICE CONDIVISA (non ripetuta in ogni tavola)

Tutte e quattro le schermate condividono tre elementi identici, verificati sovrapponendo gli screenshot:

1. **Header nero fisso**: a sinistra il link testuale "Claude Speedrun" (`href
   https://claude-speedrun.com`), al centro un logo a forma di origami/freccia bianco-crema, a destra
   "Accedi". Stesso identico blocco, stessa altezza, su tutte e quattro.
2. **Un toast scuro fluttuante in basso a sinistra**, con un pallino arancione, il testo "Stiamo
   aggiornando il brand — Potresti trovare colori strani, font sbagliati, o simili." e un bottone blu
   "Capito". Visibile negli screenshot di `24-asa`, `25-define` e `27-armadeggon-strp`; **non visibile
   nello screenshot di `28-outfunnel-1`** — osservazione, non spiegazione: può essere stato già chiuso
   (cookie di sessione) al momento di quello scatto, o comparire con un ritardo che lo scatto non ha
   atteso. È di per sé una scoperta: il sito **ammette in un banner permanente** di essere a metà di un
   restyling di brand — coerente con l'incoerenza cromatica già misurata fra `21-outemail` e le altre
   pagine del dominio nel documento di COSTRUZIONE gemello.
3. **Footer blu pieno** (`#0062ff`): wordmark "APsales" bianco, quattro icone social (Instagram, YouTube,
   Spotify, un'icona a catena/link generica), una sagoma di templare in pixel-art blu-su-blu (stesso trucco
   di blend visto altrove nell'ecosistema), cinque link testuali (La mia storia / Store / Recensioni /
   Risorse / Blog), un paragrafo di disclaimer legale, l'indirizzo (Firenze, Viale Giacomo Matteotti 15) e
   la P.IVA. In basso a sinistra, sempre, un piccolo bottone nero "Gestisci Preferenze Cookie" — il banner
   nativo di consenso cookie di Squarespace, non un elemento di brand.

Le quattro tavole sotto descrivono **solo la parte centrale**, quella che cambia da pagina a pagina.

---

## TAVOLA 1 — `/asa` (24-asa, 1.936px)
![sezione 01](../capture/24-asa/sezioni/01-come-funziona-monetizzare-il-copyw.png)

### Cosa si vede
Sfondo nero pieno con un lieve bagliore radiale scuro (`glow-almost-black.png`, 1440×1231, campo `media`
di `scheda.json`). Sopra, un H1 su quattro righe centrato: "Come funziona" (bianco) / "**monetizzare**"
(verde acceso, tutta la riga) / "Il **copywriting** come" (bianco, con "copywriting" sottolineato a mano
da un tratto arancione simile a un evidenziatore) / "autonomo" (bianco). Sotto, un video incorporato con
thumbnail personalizzata: il fondatore con cuffie e microfono a sinistra, e a destra le lettere gigantesse
gialle "A.S.A" impilate, con sotto una pillola bordata gialla "cos'è e come funziona". Il player ha
controlli reali visibili (barra di avanzamento, volume, ingranaggio impostazioni, schermo intero) e
dichiara **07:51** di durata. Sotto il video, un paragrafo bianco bold su tre righe che chiede di guardare
tutto il video prima di cliccare. Il bottone blu pieno "Diventa un copywriter." chiude la sezione, prima
del footer.

### Misure — campi di `scheda.json`
| Elemento | Coordinate | Dimensioni |
|---|---|---|
| H1 (4 righe) | y=185 | — |
| Video Vimeo (`iframe`, id 1099333295) | y=507, x=421 | 597×336 |
| CTA "Diventa un copywriter." | y=1073, x=611 | 218×53, radius 10px, `#0062ff` |
| Logo footer APsales | y=1307 | 200×38 |

### Dove cade l'accento colorato
Due accenti, non uno: il **verde** `#06a506` (1 sola occorrenza in `palette_testo`, l'intera parola
"monetizzare") e il **tratto arancione** dell'evidenziatore sotto "copywriting" — quest'ultimo non
misurato in `palette_testo` come colore-testo (è un decoro SVG/di sottolineatura, non testo colorato), ma
visibile nello screenshot come lo stesso arancione-giallo caldo usato altrove nell'ecosistema per il
sottolineato a mano. La parola scelta per il verde non è "copywriting" (il soggetto) ma **"monetizzare"**
(il verbo-guadagno) — stessa logica già registrata nel documento gemello sulla meccanica del funnel per
`#efab00` su `/define`.

### Spazio vuoto
Dal fondo del bottone CTA (y=1073+53=1126) al wordmark del footer (y=1307) corrono **181px** di sfondo
scuro senza alcun contenuto — una cerniera silenziosa fra la fine della sezione e l'inizio del footer, più
lunga della stessa distanza misurata su `/define` (vedi Tavola 2).

---

## TAVOLA 2 — `/define` (25-define, 1.802px)
![sezione 01](../capture/25-define/sezioni/01-cos-il-copywriting-e-come-funziona.png)

### Cosa si vede
Stesso sfondo nero pieno, nessun'immagine di sfondo dichiarata in `media` questa volta (a differenza di
`/asa`, qui il nero è puro CSS). H1 su una riga sola: "Cos'è il **copywriting** e come funziona?", di nuovo
con "copywriting" sottolineato dallo stesso tratto arancione. Sotto, un sottotitolo piccolo e grigio-chiaro
("Te lo spiego in questo video con un esempio pratico") seguito da una freccia-chevron rivolta in basso,
unico invito-a-scorrere di tutte e quattro le pagine. Il video ha una thumbnail diversa da `/asa`: una
lavagna bianca fisica con la scritta a pennarello "COPYWRITING" cerchiata in arancione e "spiegato ea[sy]"
tagliata dal pulsante play, con lo stesso fondatore a fianco. Durata dichiarata: **06:28**. Sotto, il
bottone blu "Scopri la strategia A.S.A" — che porta esattamente alla Tavola 1.

### Misure
| Elemento | Coordinate | Dimensioni |
|---|---|---|
| H1 (1 riga) | y=165 | — |
| Chevron di invito a scorrere | — (SVG, non quotato in `media`) | — |
| Video Vimeo (id 1099334931) | y=460, x=354 | 732×413 — il video più grande delle quattro pagine |
| CTA "Scopri la strategia A.S.A" | y=949, x=606 | 228×53 |
| Logo footer APsales | y=1172 | 200×38 |

### Dove cade l'accento colorato
Un solo accento testuale: **ambra** `#efab00` (1 occorrenza), sulla parola "copywriting" nel titolo —
stesso esadecimale già misurato nel documento di COSTRUZIONE gemello come colore del segno di spunta
dell'area corsi (`.course-list`, `custom.css`): lo stesso ambra riappare qui, su un dominio visivo
completamente diverso (un titolo di pagina, non un componente UI), a distanza di un solo file CSS
condiviso. Nessun secondo accento: a differenza di `/asa`, qui non c'è una seconda parola in un secondo
colore.

### Spazio vuoto
Dal fondo del bottone CTA (949+53=1002) al wordmark del footer (1172) corrono **170px** — quasi identico
al gap di `/asa` (181px), nonostante la pagina intera sia più corta di 134px: la cerniera vuota fra
contenuto e footer è una costante assoluta di questa famiglia di pagine, non proporzionale all'altezza
totale.

---

## TAVOLA 3 — `/armadeggon-strp` (27-armadeggon-strp, 1.752px)
![sezione 01](../capture/27-armadeggon-strp/sezioni/01-div.png)

### Cosa si vede
La schermata più diversa delle quattro: **nessun H1 testuale** (`headings: []` in `scheda.json` — verificato,
non un'omissione di questo Atlante). Il titolo "Armageddon is here" è un'illustrazione — lettering gotico
rosso fuoco con un forte bagliore al neon, su uno sfondo che sfuma dal nero al rosso scuro con vignettatura
ai bordi. Sotto, una placca rettangolare bordata come un'insegna vintage: a sinistra uno schizzo a matita
in stile ASCII/inchiostro di un occhio con una piccola fiamma disegnata sotto; a destra, in un font gotico
blackletter, una griglia 2×2 di nomi prodotto — "outEmail · outFunnel" sopra, "outHeadline · outViral"
sotto — l'unico punto di tutta questa cattura dove i quattro prodotti "out" compaiono elencati insieme come
un unico bundle. Sotto la placca, una riga bianca ("Il tuo bundle è pronto. Clicca sotto per aggiungerlo
adesso al tuo account.") e il bottone blu "Aggiungi all'account ora". **Nessun prezzo compare da nessuna
parte sullo schermo** — confermato anche dal testo, non solo dal DOM.

### Misure
| Elemento | Coordinate | Dimensioni |
|---|---|---|
| Titolo illustrato + placca | — | non presenti come voci distinte in `media` (vedi nota sotto) |
| CTA "Aggiungi all'account ora" | y=863, x=605 | 229×53 |
| Logo footer APsales (via templare pixel-art) | y=1064 | 412×413 |

**Nota di copertura**: il titolo "Armageddon is here" e la placca con i quattro prodotti non compaiono
come voci proprie nell'array `media` di `scheda.json` (che per questa pagina elenca solo il logo header,
l'immagine del templare del footer, il logo footer e quattro icone SVG). O sono `<img>`/`<svg>` con `src`
non risolto al momento dello scatto (lo stesso schema già visto per i molti wrapper `<picture>`/`<svg>`
vuoti sulle altre pagine dell'ecosistema), o sono contenuto di un blocco di codice incorporato — questa
pagina è l'unica delle quattro, insieme a `26-mpo2` e `21-outemail`, a caricare il componente
`website.components.code` (visto nel documento di COSTRUZIONE gemello). **Non decido quale delle due
ipotesi sia corretta: lo dichiaro come osservazione aperta**, non risolvibile dai soli file serviti.

### Dove cade l'accento colorato
**Nessuno, in `palette_testo`**: la voce di colore-testo aggiuntivo che compare su `/asa` e `/define` è
qui assente (`palette_testo` di questa pagina ha solo `#fafafa` e `#ebe9e0`, zero terzo colore). Questo
non significa che la pagina sia priva di accento visivo — il rosso del bagliore "Armageddon" è fortissimo
a schermo — significa che quell'accento **vive dentro un'immagine**, non in un nodo di testo colorato dal
CSS: la metrica "un colore, una parola, un uso" già registrata nel documento gemello per `/asa` e
`/define` **non si estende automaticamentre alle pagine dove l'accento è pittorico invece che
tipografico** — un'osservazione che corregge e affina, non contraddice, quel pattern.

### Spazio vuoto
Dal fondo del bottone CTA (863+53=916) al primo elemento del footer (il templare, y=1064) corrono
**148px** — il gap più corto delle quattro pagine, ma visivamente il più "vuoto" percepito: a differenza
delle altre tre tavole, qui non c'è nessun paragrafo di disclaimer o trust-badge a riempire otticamente la
fascia, solo sfondo scuro pieno.

---

## TAVOLA 4 — `/outfunnel-1` (28-outfunnel-1, 1.512px — la più corta)
![sezione 01](../capture/28-outfunnel-1/sezioni/01-outfunnel.png)

### Cosa si vede
Sfondo scuro con una texture a puntini/griglia sottilissima e diagonale (`LS-pattern-gradint-variant-grid.jpg`,
1440×807 — il nome del file suggerisce esplicitamente un pattern testato in più varianti). Tutto il
contenuto è centrato in colonna stretta: un occhiello corsivo piccolo "Stai acquistando…", poi il nome
prodotto gigante "**out**Funnel" (le tre lettere "out" in un petrolio/teal acceso, "Funnel" in bianco
crema), un paragrafo che spiega la procedura di login e cita il codice sconto "**CWSHOP**" (in grassetto,
nello stesso teal del titolo, leggermente più scuro), una linea sottile orizzontale, poi la ripetizione del
nome prodotto più piccolo, il prezzo grande **98,00 €**, "Una tantum" in grigio, il bottone blu pieno
"Acquista outFunnel", una seconda linea sottile, e infine una riga di fiducia: un'icona di spunta verde
con "Pagamento sicuro SSL" e sotto una fila di loghi di pagamento (PayPal, Visa, Mastercard, Amex,
Apple Pay). È l'unica delle quattro pagine con questa riga di trust-badge visibile.

### Misure
| Elemento | Coordinate | Dimensioni |
|---|---|---|
| H1 "outFunnel" | y=189 | — (68,3px/w700 ×2, dalla `scala_tipografica` — le due parti "out"/"Funnel" condividono la stessa taglia) |
| Riga fiducia SSL | y=691 | 131×34 |
| Loghi pagamento | y=725 | 170×34 |
| CTA "Acquista outFunnel" | y=586, x=623 | 195×53 |
| Logo footer APsales | y=882 | 200×38 |

### Dove cade l'accento colorato
Due tonalità di teal quasi identiche, entrambe a un solo uso: **`#13989a`** sulla parola "out" del titolo
e **`#139699`** sul codice sconto "CWSHOP" — un solo valore esadecimale di differenza fra le due, non lo
stesso token riusato ma due varianti vicinissime, probabilmente due proprietà di stile risolte in modo
leggermente diverso invece di un'unica variabile di colore condivisa nel codice del blocco. È l'accento
più "prezioso" delle quattro pagine: cade sia sul nome del prodotto sia sull'unico elemento realmente
azionabile del paragrafo (il codice sconto).

### Spazio vuoto
Qui il "vuoto" non è una sola fascia ma **distribuito**: dal fondo del bottone CTA (586+53=639) alla riga
SSL (691) corrono 52px; dai loghi di pagamento (725+34=759) al wordmark del footer (882) corrono 123px.
Nessun grande buco unico come nelle altre tre tavole — la pagina più corta è anche quella con la
composizione più densa, senza pause lunghe fra un blocco e l'altro.

---

## DELTA ALLA FABBRICA

**CANONE:** ogni pagina di pre-cassa o pagina-ponte della Fabbrica Siti mantiene la stessa cornice fissa
(header di navigazione minimale, footer di dominio) e concentra tutta la variazione nella sola sezione
centrale — mai il contrario. La cerniera vuota fra l'ultimo elemento utile e il primo elemento del footer
va dimensionata come un intervallo fisso di riferimento (qui misurato fra 123px e 181px a seconda della
densità della sezione sopra), non lasciata al caso: è quello spazio, non il contenuto, che dà alla pagina
la sensazione di essere "finita" prima del footer.

**PATTERN:** quando l'accento di prodotto deve leggersi anche a colpo d'occhio su un'illustrazione (non
solo su testo), va applicato **anche** al lettering dell'immagine, non solo alle classi CSS del testo —
altrimenti l'audit automatico (e chiunque misuri via DOM) lo dichiara "assente" mentre è fortissimo a
schermo, come misurato qui su `/armadeggon-strp`. Il verbo/leva di conversione (non il sostantivo del
prodotto) resta il bersaglio giusto per il colore-accento: "monetizzare", "copywriting" (nel senso di leva
= imparare la skill), "CWSHOP" (il codice che sblocca lo sconto) — mai il nome del brand.

**GATE:** prima di dichiarare "zero colore d'accento" su una schermata a partire dai soli dati
`palette_testo`/`palette_sfondi`, aprire lo screenshot: un accento può vivere dentro un asset immagine e
restare invisibile a un'estrazione di colore basata sul DOM testuale, come dimostrato qui su
`/armadeggon-strp`. Secondo controllo per la Fabbrica: se una cattura dichiara `"segmentazione": "fallita"`
o una sola sezione su una pagina lunga più di 1.000px, verificare a mano se si tratta davvero di una
pagina a blocco singolo o di un template diverso (qui: pagina "freeform" senza `page-section`) prima di
trattare il dato come un difetto dello strumento di misura.

---

## Nota di copertura

Quattro pagine, **una sezione ciascuna** (dichiarato in `scheda.json`, `sezioni_totali: 1` su tutte e
quattro — nessuna sezione non vista per economia, copertura 4/4, 100%). Read utilizzate: 4 screenshot di
sezione aperti con lo strumento di visione, 4 `scheda.json` letti per intero, incrocio con `_INDICE.json`
(peso file) e con `dom-blocks.json` già consultato nel documento di COSTRUZIONE gemello per il controllo
sul componente `website.components.code`. Non aperti: i file `desktop-NN.png` (tessere di scroll grezze,
ridondanti con lo screenshot di sezione già completo per ciascuna pagina) e i quattro `design-tokens.json`
(stesso schema ridondante già verificato altrove nell'ecosistema).

## Connessioni

- [24-25-27-28-macchina-del-funnel.md](24-25-27-28-macchina-del-funnel.md) — la meccanica, le catene, i
  due pattern `pagina-ponte`/`pre-cassa`
- [24-25-27-28-macchina-del-funnel-COPY.md](24-25-27-28-macchina-del-funnel-COPY.md) — il testo integrale
- [21-22-23-26-vendita-COSTRUZIONE.md](21-22-23-26-vendita-COSTRUZIONE.md) — dove il colore ambra
  `#efab00` e l'asimmetria del tracciamento di terze parti sono misurati sul resto dello stesso dominio
- [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) — il modello di questo stesso formato
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
