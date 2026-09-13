---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #atlante-visivo #funneloperator #design-system #reference
Created: 2026-09-13
Last updated: 2026-09-13
---

# ATLANTE VISIVO DEGLI ELEMENTI — funneloperator.it

**Ogni sezione della pagina, con sotto ogni elemento grafico che la compone e un giudizio di qualità.** Descrizioni prese guardando gli screenshot (`sezioni/`, `desktop-*`, `mobile-*`) e i file originali in `media/`; misure, colori e font letti da `scheda.json`, `design-tokens.json`, `media-inventario.md`, `copy-integrale.md`. Niente stimato a occhio dove esiste un numero nel DOM.

Questo documento è **materiale di lavoro per la Fabbrica Siti**: si apre quando si costruisce. Fonte: `capture/66-funneloperator-it/` (cattura del 2026-09-13, 1440 px desktop, 390 px mobile, pagina alta 32.807 px desktop / 36.630 px mobile, 30 sezioni, 26 distinte, 122 riferimenti media a 68 file unici per 2.511 KB totali).

> **Le immagini** vivono in `../capture/66-funneloperator-it/` (fuori dal repo). Si rigenerano con
> `python "competitor/Andrei Pascu/site-study/scripts/site_capture.py" "https://www.funneloperator.it/" --slug "66-funneloperator-it"`.

## Il sistema di misura della pagina (da `scheda.json` / `design-tokens.json`)

| Cosa | Valore letto |
|---|---|
| Colonna di contenuto | 832 px (x 304 → 1136 a 1440 di viewport): la larghezza di `soldato-caduto`, `gancio-insegna`, `vsl-principale`, `sito-apple`, delle righe FAQ |
| Sfondo scuro | `oklch(0.178 0 89.9)` (~#121212), 23 usi; card scure `oklch(0.22 0 89.9)` (~#1c1c1c), 38 usi |
| Sfondo chiaro | `oklch(0.946 0 89.9)` (~#eeeeee), 23 usi — **mai bianco puro** nelle sezioni (il body è `oklch(1 0 0)` ma non si vede mai) |
| Testo su scuro | `oklch(0.934 0 89.9)` (~#ececec) 78 usi; grigio secondario `oklch(0.633 0 89.9)` (~#8a8a8a) 51 usi |
| Testo su chiaro | `oklch(0.178 0 89.9)` 111 usi; grigio `oklch(0.473 0 89.9)` per i sottotitoli degli step |
| Accento | azzurro `oklch(0.656 0.134 235.9)` (il blu AP Sales `#008CCE` dell'SVG del marchio) — 6 sfondi (bottoni) + 6 testi; variante `oklch(0.61 0.14 240.1)` per parole evidenziate nei titoli |
| Secondo accento | verde `oklch(0.598 0.199 143.2)` — solo 2 usi: "Fare landing pages." e "Carriera avviata" |
| Terzo accento | rosso `#bd0000` — solo 2 usi: "morirai" nell'hero e la frase barrata "L'AI ti ruba il lavoro." |
| Font | `Inter Tight` (172 nodi, corpo e titoli), `Plus Jakarta Sans` (102, titoli grandi e etichette), `DM Mono` (10: timer, eyebrow FAQ, numeri 01-04), `Curseyt` (3: solo l'hero) |
| Scala | 17 px corpo (lh 27,2) · 22 · 29 · 37 · 49 · 63 · 81 · 220/290 (hero). 40 combinazioni totali |
| Pesi | 400 (120) · 500 (72) · 700 (57) · 600 (29) · 800 (9) |
| Raggi | 8 px (52 usi: bottoni, card), 5 px (36: immagini nei rail), pill (21), 12 px (8), 24 px (7: nodi dell'albero) |
| Ombre | **nessuna** ombra colorata: 14 dichiarazioni tutte `rgba(0,0,0,0)` — il rilievo lo fanno i bordi 1 px e i bordi luminosi |
| Animazioni | `fo-rail 70s linear` ×3 e `fo-rail 45s linear` ×2 (i marquee); keyframes dichiarati: `fo-comparsa`, `fo-dissolvenza`, `fo-foglio-su`, `fo-gira`, `fo-luccichio`, `fo-momento`, `caret-blink`, `accordion-up/down` |
| Effetti | `backdrop-filter: blur(8px)` ×2 (header e bottone sticky mobile), blend `hard-light`, `difference`, `screen`, `color-dodge` (le texture), `clip-path: polygon(...)` ×4 (le linguette delle cartelle) |
| CTA | 26 elementi cliccabili, di cui **3 soli bottoni pieni azzurri** (Iscriviti adesso, Sono pronto, Ottieni accesso sticky) — il resto sono tab, accordion e link |

---

# A. LE TAVOLE

## TAVOLA 1 — L'hero: «Un giorno morirai.»
![](../capture/66-funneloperator-it/sezioni/01-un-giorno-morirai.png)

### Cosa si vede
Sfondo nero pieno. Al centro, in alto, il titolo in **carattere gotico (blackletter, font `Curseyt`)** su due righe: «Un giorno» in bianco a 220 px, «morirai» in rosso `#bd0000` a 290 px, il punto finale bianco. Sotto, incassata tra il titolo e la frase di chiusura, l'illustrazione in bianco e nero di un cavaliere in ginocchio trafitto da decine di frecce, con un'aureola sopra l'elmo, circondato da topi. **L'aureola tocca quasi la base della parola «morirai»**: titolo e figura sono composti come un unico oggetto. Sotto l'illustrazione, la frase «Tanto vale provare a fare soldi nel frattempo.» a 49 px, peso 500, centrata su due righe. Tutto centrato, colonna 832 px. Sopra (in `desktop-01.png`) la testata: logo Funnel Operator bianco, un filetto verticale, il marchio APsales, a destra «Accedi →» in azzurro; bordo inferiore 1 px grigio.

### Elementi
- **Testata** (`interfaccia`): `funops-logo-bianco.png` (804×240 → 107×32, servito a 7,5×: sovradimensionato), logomark `apsales.svg` 206×41 come immagine inline, link «Accedi →» azzurro 14 px w500. `backdrop-filter: blur(8px)`.
- **H1** «Un giorno morirai.» — 220 px, w400, `Curseyt`; span «morirai» 290 px `#bd0000`. È l'unico H1 della pagina.
- **Illustrazione** `soldato-caduto.webp` — 1664×1236 → 832×618, **2× esatto, non ritagliata**, 218 KB. Tratto a inchiostro/xilografia, bianco su nero, grana fine, nessun grigio medio.
- **Paragrafo di chiusura** 49 px w500 `oklch(0.934)`.
- Nessun bottone, nessun sottotitolo, nessuna eyebrow, nessuna freccia di scroll.

### Qualità grafica
Nitidezza massima (2×). Coerenza: il blackletter, il rosso sangue e la xilografia parlano la stessa lingua «memento mori». La cura sta nel **posizionamento dell'aureola sotto il punto finale**: titolo e immagine sono impaginati come una copertina di disco, non come «titolo + immagine». Professionale perché rinuncia a tutto: niente CTA, niente sottotitolo, niente badge — una sola idea. Il bianco puro del testo su nero puro dà contrasto 21:1.

### Mobile (`mobile-01.png`)
Titolo scende a circa 80 px su due righe, l'illustrazione occupa tutta la larghezza (a filo), la frase di chiusura resta a 2 righe. Testata: solo il logomark FO (senza wordmark), APsales, Accedi. Ordine identico, nulla sparisce.

### Cosa impariamo
Un hero può essere **un'illustrazione + una frase di 3 parole**: la forza è nella rinuncia, e nel far toccare titolo e immagine.

---

## TAVOLA 2 — «Diventa funnel operator oggi» + le tre carte
![](../capture/66-funneloperator-it/sezioni/02-diventa-funnel-operator-oggi.png)

### Cosa si vede
Sfondo nero con **texture di grana/roccia** (sezione con `bg_img: true`, l'unica del sito). In alto centrato il logomark FO in gradiente azzurro (`funops-logomark-gradiente.svg`, 58×54). Sotto l'H2 a 63 px: «Diventa **funnel operator** oggi» con le due parole in azzurro w700. Al centro **tre carte verticali** disposte a ventaglio: quella centrale più alta (parte da y 1627) e più avanti, le due laterali più basse (y 1755-1769) e leggermente ruotate verso l'esterno; le carte hanno sfondo `oklch(0.22)`, bordo 1 px grigio scuro, raggio 12 px, e ognuna contiene un'illustrazione nera che riempie i 2/3 superiori e in basso un titolo 29 px w700 + una riga grigia 17 px + un **badge di verifica** azzurro (cerchio dentellato con spunta) accanto al titolo.

### Elementi
- **Logomark** `funops-logomark-gradiente.svg` (1 KB, due path con `linearGradient` verticale).
- **H2** 63 px w500 `Plus Jakarta Sans`, con `<strong>` azzurro.
- **Carta 1 (sinistra, «Lezioni complete»)**: `carta-lezioni.webp` 594×746 → 295×370 (2×), computer retro anni '80 in bianco e nero con scritta a monitor `0 to landing page`; sottotitolo «anche per chi parte da zero».
- **Carta 2 (centro, «Metodo chiaro»)**: `carta-metodo.webp` 594×746 → 295×370 (2×), mappa topografica in negativo con nodi (quadrati con icone: X, edificio, cerchio, bandierina), tratteggi, mirini e una bussola; sottotitolo «e testato per trovare clienti».
- **Carta 3 (destra, «1° landing page»)**: `carta-landing.webp` 594×746 → 314×385 (1,9×), cronometro militare arrugginito con display a segmenti «24» e una spunta; sottotitolo «online entro 24h da inizio corso».
- **Badge verificato** ×3 (icona inline, azzurro).
- **Texture di fondo**: grana scura con macchie chiare, applicata via CSS con blend (`hard-light`/`screen` tra gli effetti letti).

### Qualità grafica
Le tre illustrazioni sono **della stessa mano**: negativo bianco su nero, grana, oggetti «da operazione militare» (mappa, cronometro, terminale). Il ventaglio con la carta centrale sollevata dà profondità senza ombre. Il badge di verifica ripete il gesto della «promessa certificata». Le carte hanno esattamente lo stesso raggio delle card che tornano nelle tavole 7, 17, 25: il sistema è uno. Peso: 3 immagini per 153 KB totali.

### Mobile (`mobile-02.png`, `mobile-03.png`)
Le carte si **impilano a cascata** con sovrapposizione e leggera rotazione (la seconda spunta da sotto la prima), a larghezza quasi piena. Compare per la prima volta il **bottone sticky «Ottieni accesso»** azzurro pill in basso a destra, che resterà fisso in tutte le schermate mobile successive.

### Cosa impariamo
Tre promesse = tre carte illustrate nello stesso registro, con badge «verificato»: le promesse si mostrano, non si elencano.

---

## TAVOLA 3 — La garanzia: «E se non trovi clienti…»
![](../capture/66-funneloperator-it/sezioni/03-section.png)

### Cosa si vede
Prima sezione chiara (`oklch(0.946)`). **Layout a zig-zag in due righe**: riga 1 → testo a sinistra (37 px, w500, allineato a sinistra, 4 righe) e foto a destra; riga 2 → foto a sinistra e testo a destra allineato a destra. Le due frasi sono una sola frase spezzata dai puntini di sospensione: «E se non trovi clienti dopo aver **finito il Funnel Operator** e aver contattato **50 persone**…» / «…puoi fissare una **consulenza** con **Andrei Pascu** a €0 per trovarli.» Nessun titolo, nessun bottone.

### Elementi
- **Paragrafo 1** 37 px w500 nero, grassetti w700 dentro.
- **Foto 1** `zero-clienti.webp` 700×534 → 350×267 (2×): portatile su un supporto, schermo bianco con un finto CRM e la scritta «ZERO CLIENTI?» in maiuscolo nero, tutto immerso in luce blu su parete a doghe. Angoli arrotondati 12 px.
- **Foto 2** `andrei-scrivania.webp` 702×534 → 351×267 (2×): Andrei di profilo alla scrivania con monitor HP, microfono ad asta, tastiera retroilluminata, due stampe incorniciate al muro, luce fredda. Stesso raggio.
- **Paragrafo 2** speculare, allineato a destra.

### Qualità grafica
Le due foto sono **della stessa sessione** (stessa luce blu/fredda, stesso ambiente): la garanzia diventa un dialogo in due quadri. Lo zig-zag dà movimento senza ornamenti. Le foto sono servite esattamente a 2×. Debole: il testo a destra allineato a destra è meno leggibile su 4 righe.

### Mobile (`mobile-04.png`)
Ordine lineare: testo 1 → foto 1 → testo 2 → foto 2, tutto allineato a sinistra, foto a piena larghezza con raggio 12 px.

### Cosa impariamo
Una garanzia va **fotografata**: problema (schermo «ZERO CLIENTI?») e soluzione (l'uomo che lavora per te).

---

## TAVOLA 4 — Il rail dei numeri
![](../capture/66-funneloperator-it/sezioni/04-section.png)

### Cosa si vede
Fascia chiara alta 273 px, **marquee orizzontale infinito** (`fo-rail 45s linear`) di quattro coppie icona + numero: stella Trustpilot verde + «4.8/5 / score Trustpilot» (link sottolineato azzurro), carrello nero + «4000+ / ordini nel mio store», gruppo di persone (in grigio nello screenshot, sta entrando) + «1500+ / studenti formati», doppia freccia + «2020 / apertura dello store». Lo screenshot coglie il rail a metà corsa: a sinistra si legge il residuo «…ore» di «store». I 4 item sono duplicati (8 media nel DOM) per il loop.

### Elementi
- **Icone SVG** monocrome `#111111`: `ordini.svg` (carrello, 72×81), `studenti.svg` (tre figure, 74×71), `apertura.svg` (due frecce che si incastrano, 76×76), `trustpilot.svg` (stella `#00B67A` con metà scura `#005128`, 80×75).
- **Numero grande** 37 px w700 + **didascalia** 17 px w400.
- **Link** «Trustpilot» → `it.trustpilot.com/review/andrei-copy.com`.
- **Rail**: `transform: matrix(1,0,0,1,-349,0)` letto nel DOM, `animation: fo-rail 45s linear`.

### Qualità grafica
Icone in un solo peso e un solo colore, numeri nella stessa scala 37/17 dei sottotitoli della pagina: il rail è pulito. Il verde Trustpilot è l'unico colore fuori palette, ed è il colore ufficiale del marchio citato, quindi legittimo. Debole: il rail taglia sempre un item a metà (inevitabile nel marquee).

### Mobile (`mobile-05.png`)
Stessa fascia, si vedono 1-2 item alla volta; il numero cresce in proporzione (~37 px).

### Cosa impariamo
La prova sociale numerica può essere **un nastro che scorre**, con icone SVG a un colore; niente card, niente cornici.

---

## TAVOLA 5 — «Le aziende le vogliono.» + insegna
![](../capture/66-funneloperator-it/sezioni/05-section.png)

### Cosa si vede
Sfondo nero. Tre frasi centrate una sotto l'altra a 36 px w500, spaziate: «Le aziende le vogliono.» / «Non le trovano.» / «E son disposte a **pagare tanto** per averle.» Sotto, un **pannello orizzontale con bordo bianco 1 px** (832×259) che contiene l'illustrazione `gancio-insegna`: un cavaliere in bianco e nero che regge una spada su fondo di macchie bianche, con sopra la scritta grigia in maiuscolo «LANDING PAGES.» che passa **davanti** alla figura. In basso, «Ti spiego tutto ↓» a 22 px.

### Elementi
- **Tre paragrafi** 36 px w500 (non sono heading nel DOM).
- **Insegna** `gancio-insegna.webp` 1662×518 → 832×259 (2× esatto, non ritagliata, 169 KB). Alt: «Landing pages.» — la scritta è **dentro l'immagine**, non HTML.
- **Cornice** 1 px bianca attorno all'insegna (l'unico bordo bianco pieno del sito).
- **Invito allo scroll** «Ti spiego tutto ↓» 22 px w500 con freccia Unicode.

### Qualità grafica
La scansione «vogliono / non trovano / pagano» è quasi un haiku tipografico; il pannello con bordo bianco sembra una targa. L'immagine è coerente con l'hero (stesso cavaliere, stessa xilografia). La parola «LANDING PAGES.» è resa in grigio medio, non in bianco: resta leggibile ma non urla. Debole: il testo nell'immagine non si può selezionare né tradurre.

### Mobile (`mobile-05.png`)
Le tre frasi vanno a capo (la terza su due righe), l'insegna si stringe alla larghezza del viewport mantenendo il bordo bianco e la proporzione.

### Cosa impariamo
Il **nome del servizio** merita un'insegna: una parola sola, in maiuscolo, sopra un'immagine simbolica, dentro una cornice.

---

## TAVOLA 6 — «La realtà dei fatti?» (il blocco lungo)
![](../capture/66-funneloperator-it/sezioni/06-la-realt-dei-fatti.png)

### Cosa si vede
Sezione nera alta 1.848 px, la più «editoriale» della pagina. H2 «La realtà dei fatti?» 49 px w700 allineato a sinistra. Due paragrafi giustificati a 17 px con grassetti «Non/non» e il link azzurro «questo» (verso sec.gov). Poi **una tessera metallica** (l'avviso SEC) a sinistra e un paragrafo a destra in due capoversi giustificati. Poi H3 «L'evoluzione del copywriting» 37 px + paragrafo lungo. Poi H3 «Apri i **3 siti** che hai visitato oggi.» con «3 siti» azzurro + una riga di testo + **tre screenshot di siti famosi**: Apple iPhone a piena larghezza (832×221) e sotto, affiancati, Amazon e Notion (408×221 ciascuno). Chiude un paragrafo sull'AI.

### Elementi
- **H2** 49 px w700; **H3** ×2 37 px w700; `em` azzurro «3 siti».
- **Paragrafi** 17 px lh 27,2, **giustificati** (si vedono le spaziature irregolari tra parole).
- **Link** «questo» azzurro sottolineato.
- **Tessera SEC** `sec-avviso.webp` 894×624 → 447×312 (2×, 98 KB): card metallica argento con riflesso diagonale, sigillo SEC in alto a sinistra e in filigrana a destra, citazione in monospaziato maiuscolo tra virgolette grandi, in basso una banda nera con «SEC» e una riga in monospaziato piccolo «ENTE GOVERNATIVA AMERICANA…». Angoli arrotondati e ombra **dentro l'immagine**.
- **Screenshot** `sito-apple.webp` 830×220 → 832×221 (**1×**, 6 KB, sfocato a ingrandirlo), `sito-amazon.webp` 814×440 → 408×221 (2×), `sito-notion.webp` 814×440 → 408×221 (2×). Raggio 12 px.

### Qualità grafica
Il colpo è la **tessera SEC**: prende un link a un PDF governativo e lo trasforma in un oggetto fisico argentato — la citazione diventa un reperto. Gli screenshot dei tre siti sono la prova «guarda tu stesso». Debole: i paragrafi giustificati su 832 px creano righe di fiume; l'immagine Apple è servita a 1× e appare meno nitida delle altre due.

### Mobile (`mobile-08.png` per la coda)
Tessera a piena larghezza sopra il testo, i tre screenshot in colonna (Apple, Amazon, Notion) a piena larghezza; i paragrafi restano giustificati anche a 390 px (fiumi più evidenti).

### Cosa impariamo
Una **fonte esterna** si rende credibile trasformandola in un oggetto (tessera, targa, documento), non in un link.

---

## TAVOLA 7 — «Come funziona»: la scala a 7 gradini
![](../capture/66-funneloperator-it/sezioni/07-come-funziona.png)

### Cosa si vede
Sezione chiara. H2 «Come funziona» 63 px w600 centrato. Sotto, **sette card rettangolari (290×140 circa, raggio 24 px, bordo 1 px nero) disposte a scala**: le card impari a sinistra (x≈480), le pari a destra (x≈670), ogni card collegata alla successiva da una **linea tratteggiata nera che esce dal lato destro, scende in verticale, e rientra dal lato sinistro** della card sotto (percorso a gomito). Dentro ogni card: a sinistra un'icona nera piena grande (che **sborda oltre il bordo sinistro** della card, tagliata dal `overflow`), a destra «Step N» 29 px w600 e una riga grigia 17 px. In fondo la linea tratteggiata scende con una **freccia** verso «Carriera avviata» in verde 49 px + badge verde di verifica, e sotto «E tutto ciò è insegnato nel corso al 100%» 22 px.

### Elementi
- **H2** 63 px w600.
- **7 card**: bordo `1px solid` nero, raggio 24, sfondo trasparente (stesso grigio della sezione).
- **Icone**: Step 1 `funops-logomark-scuro.svg` (121×115), Step 2 `passo-2-checklist.webp` (256 → 110), Step 3 `passo-3-dispositivo.webp` (256 → 161, un dispositivo/carta con schermo), Step 4 `passo-4-globo.webp` (256 → 125), Step 5 `passo-5-persone.webp` (256 → 117), Step 6 `passo-6-grafico.webp` (256 → 119, istogramma), Step 7 `passo-7-paypal.webp` (256 → 127, il logo PayPal in bianco su nero). Tutte a 2×, tutte nere piene, stile glifo.
- **Connettori** tratteggiati 1 px, angoli vivi, freccia finale.
- **Testo finale** verde `oklch(0.598 0.199 143.2)` 49 px w500 + `carriera-avviata.svg` (28×28, badge dentellato).
- **Riga di chiusura** 22 px w400.

### Qualità grafica
È un **diagramma di flusso a scala** costruito in HTML: le card sono vere card, i connettori sono bordi tratteggiati di div vuoti. Le icone che escono dal bordo sinistro sono una scelta deliberata (il glifo «buca» la card) e uniforme su tutte e sette. La ripetizione «Step N» nella stessa posizione fa leggere il percorso in un colpo d'occhio. Il verde finale compare qui per la prima volta ed è riservato al traguardo.

### Mobile (`mobile-08.png`, `mobile-09.png`)
Le card si allineano in una **colonna unica** a piena larghezza, i connettori scompaiono; le icone continuano a sbordare a sinistra. Ordine 1→7 conservato.

### Cosa impariamo
Un percorso in N passi si disegna come **scala a zig-zag con connettori tratteggiati**: card + bordo + icona che sborda, niente immagini di flusso.

---

## TAVOLA 8 — «Fare siti» vs «Fare landing pages.»
![](../capture/66-funneloperator-it/sezioni/08-fare-siti-fare-landing-pages.png)

### Cosa si vede
Sfondo nero. Due colonne: a sinistra «Fare siti» **barrato**, in grigio, 37 px; a destra «Fare landing pages.» in **verde** w700. Sotto ciascuna, un ritratto di profilo dello stesso ragazzo: a sinistra in **bianco e nero**, capelli corti disordinati, auricolare, espressione stanca; a destra **a colori**, capelli curati, collana d'oro, **bordo verde 1 px**. Sotto, centrato: «Nel 2026 tutti fanno siti.» 29 px w600, «E servono a poco. Sito = vetrina.» 17 px, «Ma tante aziende:» 22 px w600, elenco puntato di 2 voci, chiusura «Quello che le aziende vogliono? Landing pages ↓».

### Elementi
- **H2** con due `span`: il primo con `text-decoration: line-through` grigio, il secondo verde.
- **Foto «prima»** `fare-siti.webp` 596×726 → 298×362 (2×): bianco e nero, raggio 12 px.
- **Foto «dopo»** `fare-landing.webp` 594×726 → 298×364 (2×): a colori, **il bordo verde è dentro il file** (si vede nel WebP originale), raggio 12 px.
- **Testo centrale** 29/17/22 px + `ul` a puntini bianchi.
- **Freccia** ↓ Unicode.

### Qualità grafica
Il **prima/dopo con la stessa persona** (bianco e nero vs colore, taglio sbagliato vs curato) è comunicazione visiva pura, senza una parola di spiegazione. Il barrato + verde ripete il codice della tavola 17. Debole: le due foto non sono della stessa sessione (fondo grigio in entrambe ma luce diversa) — l'effetto regge comunque perché il codice colore/bn fa il lavoro.

### Mobile (`mobile-11.png`)
Le due foto si impilano (prima bn, poi colore col bordo verde) a piena larghezza; i titoli barrato/verde stanno sopra ciascuna foto; il testo centrale resta centrato.

### Cosa impariamo
Il confronto tra due servizi si fa con **due ritratti, uno in bianco e nero e uno a colori**: il registro fotografico è il giudizio.

---

## TAVOLA 9 — La VSL: «Perché fare landing pages è il servizio che ho scelto»
![](../capture/66-funneloperator-it/sezioni/09-perch-fare-landing-pages-il-serviz.png)

### Cosa si vede
Sezione chiara. H2 centrato su due righe a 49 px w700 con «ho scelto» in azzurro; sotto, in tondo 17 px, «(spoiler: mi piacciono i soldi)». Poi il **poster video** 830×466 (16:9) con raggio 12 px: Andrei seduto a una scrivania di legno, maglietta nera, occhiali, mani intrecciate, libreria retroilluminata di **blu** alle spalle con oggetti (lampade rosse, macchina da scrivere, giradischi); al centro un **bottone play** circolare bianco semitrasparente (`oklab(0 0 0 / 0.45)` di fondo, triangolo bianco).

### Elementi
- **H2** 49 px w700 + `em` azzurro.
- **Battuta** 17 px w400 tra parentesi (funziona da sottotitolo).
- **Poster** `vsl-principale.webp` 1600×900 → 830×466 (1,93×, 45 KB), raggio 12 px.
- **Play** cerchio ~80 px, sfondo nero al 45 %, `backdrop-filter`.
- Un CTA conteggiato nel DOM (il play stesso).

### Qualità grafica
Il poster è **fotografia da studio** (tre punti luce, blu di fondo, primo piano nitido): dà autorità. La palette del poster (blu + nero + rosso delle lampade) coincide con la palette del sito. Il play è discreto e centrato sul torace, non sul viso. Debole: nessuna durata, nessun sottotitolo, nessun «guarda 2 min» — il video non dice quanto costa in tempo.

### Mobile (`mobile-12.png`, non campionata direttamente; pattern dedotto da `mobile-30.png` che mostra la stessa VSL di tavola 21)
Poster a piena larghezza, play centrato, titolo su 3-4 righe.

### Cosa impariamo
Il video di vendita ha un **poster fotografico della stessa palette del sito**, con un play sobrio; il set (libreria blu) diventa marchio.

---

## TAVOLA 10 — «Titolare AP Sales» + l'albero
![](../capture/66-funneloperator-it/sezioni/10-titolare-ap-sales.png)

### Cosa si vede
Sezione chiara in due parti. **Parte alta**: a sinistra una foto quadrata (306×324) di Andrei in giacca e cravatta al tavolo di un ristorante in alto, con lo skyline notturno di una città alle spalle, che guarda il telefono; la foto è **leggermente ruotata** (inclinazione di 2-3 gradi, angoli arrotondati). A destra H2 «Titolare **AP Sales**» 49 px + due paragrafi giustificati. **Parte bassa**: frase centrata 37 px «Questa pagina è parte del mio ramo **formazione tecnica per marketer**.» e sotto **l'albero a tre nodi**: in alto una pillola «AP Sales» con il logomark, una linea nera scende e si biforca ad angolo retto in due pillole «Formazione» (icona portatile) e «Agenzia» (icona tre persone). A sinistra della pillola Formazione, un **puntatore azzurro** (pallino + chevron ∨) con l'etichetta «Tu sei qui».

### Elementi
- **Foto** `andrei-telefono.webp` 598×634 → 306×324 (1,95×), con `rotate` leggero.
- **H2** 49 px w500 + strong w700.
- **2 paragrafi** 17 px giustificati.
- **Frase ponte** 37 px w500 + strong.
- **Albero** `albero-apsales.webp` 1586×656 → 793×328 (2× esatto, 105 KB): **è un'immagine**, non HTML. Tre pillole grigio chiaro con bordo 1 px nero (raggio pieno), linee nere 2 px, icone lineari, etichetta «Tu sei qui» con «qui» in azzurro, pallino azzurro con alone.

### Qualità grafica
La foto inclinata rompe la griglia con misura (unica foto ruotata del sito). L'albero spiega in un colpo la struttura dell'impresa e **colloca il lettore** («Tu sei qui»): è un organigramma che diventa mappa. Coerenza: le pillole dell'albero hanno lo stesso bordo 1 px e lo stesso grigio delle card della tavola 7. Debole: essendo un'immagine, il testo dell'albero non è HTML (però l'alt lo descrive per intero).

### Mobile (`mobile-13.png`, `mobile-14.png`)
Foto a piena larghezza sopra il titolo (che va su due righe «Titolare / AP Sales»); l'albero si stringe a 390 px restando leggibile perché ha solo tre nodi.

### Cosa impariamo
Prima di vendere un prodotto, si mostra **dove sta nel sistema**: un albero a tre nodi con «Tu sei qui».

---

## TAVOLA 11 — «Esempi di pagine fatte da APsales» (doppio rail)
![](../capture/66-funneloperator-it/sezioni/11-esempi-di-pagine-fatte-da.png)

### Cosa si vede
Sfondo nero. H2 «Esempi di pagine fatte da» 49 px w500 seguito, sulla stessa riga, dal **marchio APsales in azzurro** (`apsales.svg`) al posto del nome. Sotto, **due rail orizzontali** di screenshot verticali di landing page (209×293, raggio 5 px), uno sopra l'altro, **che scorrono in direzioni opposte** (matrici `-881`, `-902`, `-890` lette nel DOM): riga alta e riga bassa sfalsate di mezzo modulo. Tre soggetti che si ripetono: una landing verde/beige di prodotti monouso, una pagina crema di massaggi con foto, la pagina «Chi siamo» scura di AP Sales con box blu «La speranza non è una strategia».

### Elementi
- **H2** + `apsales.svg` inline (206×41) come parola del titolo.
- **Screenshot** ×3 ripetuti (37 nodi `img` nel DOM): `esempio-monouso.webp`, `esempio-massaggi.webp`, `esempio-apsales.webp`, tutti 400×560 → 209×293 (1,9×, 13-18 KB ciascuno).
- **Rail** ×2 con `fo-rail 70s linear`, direzioni opposte.

### Qualità grafica
Il portfolio come **nastro doppio controcorrente** dà l'idea di abbondanza con soli 3 file (56 KB in tutto). Il marchio dentro il titolo è un tocco da art director. Debole: sono solo tre esempi e si nota dopo pochi secondi; gli screenshot sono piccoli e non cliccabili.

### Mobile (`mobile-14.png`, `mobile-15.png`)
Titolo su tre righe con APsales sulla terza; i due rail restano orizzontali e occupano quasi due schermate.

### Cosa impariamo
Un portfolio di 3 pezzi si mostra come **due rail controcorrente**: l'occhio legge movimento, non conteggio.

---

## TAVOLA 12 — «Per chi ho creato Funnel Operator:»
![](../capture/66-funneloperator-it/sezioni/12-per-chi-ho-creato-funnel-operator.png)

### Cosa si vede
Sfondo nero. H2 centrato su due righe 63 px, «Funnel Operator» in azzurro. Sotto, due colonne: a sinistra una foto quadrata (321×341) di Andrei sulla sedia, di traverso, felpa grigia, che **punta il dito** verso il portatile che regge con l'altra mano e sul cui schermo c'è il logomark FO azzurro; alle spalle luce al neon azzurra e un poster rosso. A destra un **elenco puntato di 5 voci** 17 px con puntini bianchi e spaziatura generosa (≈50 px tra voce e voce).

### Elementi
- **H2** 63 px w500 + strong azzurro.
- **Foto** `per-chi.webp` 642×682 → 321×341 (2×), bordo 1 px grigio chiaro (unica foto con bordo visibile), raggio 12 px.
- **Lista** `ul` 5 `li`, 17 px lh 27,2.

### Qualità grafica
La foto è **una didascalia gestuale**: indica «questo qui» (il corso sul portatile) e il testo dice «per chi». Coerenza cromatica totale col sito (neon azzurro + rosso). L'elenco arioso si legge come cinque frasi, non come un blocco. Debole: la posa è da social più che da sales page — funziona per il target 18-28.

### Mobile (`mobile-15.png`)
Foto a piena larghezza sotto il titolo, lista sotto la foto.

### Cosa impariamo
La sezione «per chi è» ha bisogno di **una foto che indichi** il prodotto: il gesto sostituisce il sottotitolo.

---

## TAVOLA 13 — «Ma chi cazzo pensi di essere?» (la biografia a sei foto)
![](../capture/66-funneloperator-it/sezioni/13-ma-chi-cazzo-pensi-di-essere.png)

### Cosa si vede
Sezione chiara alta 1.924 px, **colonna stretta** (≈670 px, x 387→1053), la più stretta della pagina. H2 tra virgolette 49 px centrato su due righe. Sotto, **avatar rotondo** (124 px) di Andrei al microfono che fa il segno di pace, accanto la firma «Andre :)» 37 px. Poi il racconto: sottotitolo 29 px «Dalla scrivania nella casa di un paesino a un ufficio…», paragrafi 17 px allineati a sinistra, e **tre coppie di foto** (313×172 la prima e la seconda coppia, 313×235 la terza) intercalate ai paragrafi: 1) ufficio con neon blu / cucina gialla al portatile; 2) da ragazzo di notte al monitor / da ragazzo che si sporge verso la webcam (foto amatoriali, sgranate); 3) in palestra allo specchio / riunione con quattro uomini in giacca con **volti pixelati**. Chiude un paragrafo su AP Sales.

### Elementi
- **H2** 49 px w600, virgolette tipografiche.
- **Avatar** `andrei-tondo.webp` 248×248 → 124×124 (2×), `border-radius: 50%`.
- **Firma** 37 px w500 «Andre :)».
- **Sottotitolo** 29 px w500; **«Anche se a dire il vero…»** 22 px.
- **6 foto** con raggio 12 px e bordo 1 px chiaro: `storia-ufficio`, `storia-cucina`, `storia-monitor`, `storia-tavolo` (tutte 642×342 → 321×172, 2×), `storia-palestra`, `storia-riunione` (626×470 → 313×235, 2×). Peso totale ≈200 KB.
- **6 paragrafi** 17 px.

### Qualità grafica
È una **pagina di diario** impaginata: colonna stretta da lettura, foto piccole e a coppie che scandiscono il tempo (oggi → passato → oggi). Le foto vecchie sono volutamente brutte (grana, luce da webcam) e questo le rende vere. I volti pixelati nella riunione sono una scelta di rispetto che aumenta la credibilità. Debole: la griglia 2×3 con formati diversi (172 vs 235 di altezza) fa saltare il ritmo nell'ultima coppia.

### Mobile (`mobile-19.png`)
Le coppie di foto si impilano in colonna a piena larghezza; il testo giustificato produce fiumi, la lettura resta lineare.

### Cosa impariamo
La biografia si racconta con **foto piccole, a coppie, cronologiche, anche brutte**: la qualità bassa delle foto vecchie è una prova, non un difetto.

---

## TAVOLA 14 — «LA CRISI DEL 2025»
![](../capture/66-funneloperator-it/sezioni/14-la-crisi-del-2025.png)

### Cosa si vede
Sezione chiara, bassa (603 px), **solo testo**. H2 in maiuscolo 63 px w700 centrato. Sotto, una colonna ancora più stretta (≈535 px, x 452→987) con cinque capoversi 17 px giustificati; grassetto su «Inizio 2025»; un'emoji 😅; chiusura «Ecco cos'era cambiato ↓».

### Elementi
- **H2** uppercase 63 px w700 (unico titolo maiuscolo oltre a FUNNEL OPERATOR).
- **5 paragrafi** 17 px, colonna ~535 px, giustificati.
- **Freccia** ↓.
- Zero media, zero CTA.

### Qualità grafica
La sezione respira perché è vuota: dopo 6 foto, un blocco di sola tipografia. La colonna stretta (≈60 caratteri) è la misura giusta per leggere. Il maiuscolo pesante dice «titolo di giornale». Debole: la giustificazione a 535 px produce righe con buchi visibili.

### Mobile (non campionata: `mobile-20.png`; pattern deducibile)
Titolo su due righe, paragrafi a piena larghezza.

### Cosa impariamo
Ogni tanto una sezione **senza immagini** è il modo per far pesare le immagini che seguono.

---

## TAVOLA 15 — «Ho fatto 28 test di 28 servizi diversi.» + i tre motivi
![](../capture/66-funneloperator-it/sezioni/15-ho-fatto-28-test-di-28-servizi-div.png)

### Cosa si vede
Sfondo nero. H2 49 px w500 allineato a sinistra su due righe, con «28 test» e «28 servizi» in azzurro e «uno» in grassetto bianco. Tre capoversi 17 px. Poi una **lista a tre righe separate da filetti sottili** (bordo `oklch(0.293)`), ognuna con a sinistra una piccola **incisione in bianco e nero** (60×60) e a destra il motivo a 22 px w400: teschio → «Non erano richiesti dal mercato.», due spade incrociate → «Li stavano già offrendo altre agenzie e professionisti.», lapide → «Non c'era margine.». Chiudono due capoversi 17 px.

### Elementi
- **H2** 49 px con `strong` azzurri e bianco.
- **3 paragrafi + 2 paragrafi** 17 px.
- **Lista a filetti**: 3 `li`, ogni riga alta ~105 px, separatori 1 px.
- **Incisioni** `motivo-teschio.webp` (60×61), `motivo-spade.webp` (60×60), `motivo-lapide.webp` (60×60) — servite a **1×**, 2-3 KB ciascuna, stile xilografia bianca su nero come l'hero.

### Qualità grafica
I tre glifi sono **micro-illustrazioni nello stesso registro dell'hero** (teschio, spade, lapide = morte, guerra, tomba): il codice visivo «memento mori» torna in piccolo. La lista a filetti senza card è elegante. Debole: le incisioni a 1× su schermi retina risultano leggermente morbide.

### Mobile (`mobile-21.png`)
Identica: titolo, paragrafi, tre righe con glifo a sinistra (il testo va su due righe).

### Cosa impariamo
Un elenco di 3 motivi si illustra con **tre glifi disegnati nello stesso stile dell'hero**: il sistema iconografico si estende, non si spezza.

---

## TAVOLA 16 — «Schiavizzerai l'AI.» (i serpenti)
![](../capture/66-funneloperator-it/sezioni/16-schiavizzerai-l-ai.png)

### Cosa si vede
Sezione chiara alta 928 px con **sfondo di carta granulosa** a piena larghezza (`carta-serpenti.webp`, 1440×928, la texture con pelucchi e puntini). Sopra la carta, **due teste di serpente nero a fauci aperte, gigantesche e speculari** (una da sinistra in alto, l'altra ruotata da destra in basso), che si fronteggiano: zanne bianche, lingue biforcute. Al centro una **fascia orizzontale grigio chiaro a piena larghezza** (y 372→555, ≈183 px) che copre i serpenti e contiene a sinistra H2 «Schiavizzerai l'AI.» 49 px w600 e a destra due paragrafi 17 px giustificati.

### Elementi
- **Texture** `carta-serpenti.webp` 1440×928 → 1440×928 (**1×**, 21 KB): grana di carta con fibre.
- **Serpente** `serpente-testa.webp` 1438×1708 → 719×854 (2×, 78 KB) usato **due volte**, la seconda con `rotate(180deg)` (i due `img` letti nel DOM).
- **Fascia** `oklch(0.946)` piena, senza bordo.
- **H2** 49 px w600 + **2 paragrafi** 17 px.

### Qualità grafica
È la sezione più «poster»: una sola immagine duplicata e ruotata crea una composizione simmetrica a S; la fascia di testo che **taglia** le figure è un gesto editoriale (copertina di rivista). La carta di fondo dà materia. Debole: sul desktop la fascia copre proprio le bocche, il punto più forte dell'immagine (su mobile invece si vedono).

### Mobile (`mobile-23.png` per la coda)
La testa del serpente occupa la parte alta a piena larghezza, la fascia con titolo e testo sta sotto; la simmetria si perde, l'impatto resta.

### Cosa impariamo
**Una sola immagine forte, duplicata e ruotata**, più una fascia di testo che la attraversa: composizione da poster con un file solo.

---

## TAVOLA 17 — «L'AI ti ruba il lavoro.» → «Ruberai il lavoro a chi non sa usare l'AI.»
![](../capture/66-funneloperator-it/sezioni/17-l-ai-ti-ruba-il-lavoro-ruberai-il.png)

### Cosa si vede
Sezione chiara alta 1.254 px. In alto la frase **rossa barrata** «L'AI ti ruba il lavoro.» 37 px, sotto il titolo vero 49 px w700 nero su due righe. Poi un **rail di loghi AI** (ChatGPT, GitHub, Lovable, Krea, Claude, Gemini, Vercel) in colore, 40 px, a passo regolare. Tre capoversi 17 px (uno in corsivo tra virgolette basse). H3 «Ci sono 2 tipi di persone che usano l'AI per fare pagine:» 29 px. **Due card affiancate** (≈255×345, raggio 12 px): la sinistra con bordo nero 1 px e un enorme «1.» 81 px w800 nero; la destra con **bordo azzurro** 1 px e «2.» 81 px azzurro; sotto i numeri, due capoversi giustificati per card. Chiude «L'azienda non ti paga per generare la pagina.» 22 px w700 + due righe 17 px centrate.

### Elementi
- **Frase barrata** `#bd0000` con `line-through`, 37 px.
- **H2** 49 px w700 (nel DOM è un unico H2 con span).
- **Rail loghi**: `ai-chatgpt`, `ai-github`, `ai-lovable`, `ai-krea`, `ai-claude` (tutti 80×80 → 40×40, 2×, 1-4 KB) ripetuti ×2 per il loop; Gemini e Vercel come SVG inline; `fo-rail 70s`.
- **H3** 29 px w700.
- **Card 1 / Card 2**: `ol` a due colonne, numero come `span` 81 px w800, card 2 con bordo azzurro e «desiderati dalle aziende» in grassetto.
- **Chiusura** 22 px w700 + 17 px.

### Qualità grafica
Il **numero gigante come titolo della card** (81 px) è il pattern più riconoscibile della pagina. Il bordo azzurro sulla card «giusta» è la sola differenza tra le due: minimo segnale, massima leggibilità. Il rail dei loghi a colori è l'unico punto in cui entrano colori terzi (verde ChatGPT, arancio Lovable, ecc.), contenuti a 40 px. Debole: i paragrafi giustificati dentro card da 255 px creano fiumi enormi («Buttano via i soldi» con spazi doppi).

### Mobile (`mobile-23.png`, `mobile-25.png`)
Titolo su quattro righe; il rail dei loghi mostra 3 loghi per volta; le due card si **impilano** (la 2 con bordo azzurro sotto la 1).

### Cosa impariamo
Il confronto «tipo 1 / tipo 2» si fa con **due card gemelle e un numero a 81 px**: colora solo il bordo di quella giusta.

---

## TAVOLA 18 — «Non è un business sexy… Ma funziona» (carte da gioco + griglia 01-04)
![](../capture/66-funneloperator-it/sezioni/18-non-un-business-sexy-ma-funziona.png)

### Cosa si vede
Sfondo nero, sezione alta 1.600 px. H2 tra virgolette basse 63 px w700 centrato su due righe. Sottotitolo «Vuoi fare cose divertenti o vuoi fare soldi?» 22 px w700, poi due righe grigie 17 px. Al centro **quattro carte da gioco illustrate** (K, Q, J, A, seme «$») in bianco e nero a inchiostro, leggermente sventagliate: re scheletro con corona e forziere, regina scheletro velata con calice, fante caprone con collane e pugnale, asso con calice traboccante d'oro. Sotto: «A differenza di tutte le milioni di persone… Tu adesso puoi accedere a una **carta leggendaria**.» 22 px con azzurro. Poi la **griglia a quattro colonne** (832 px, alta ≈600 px): ogni colonna ha in alto un grande numero in monospaziato «01 02 03 04» 49 px, un filetto orizzontale, un H3 22 px w700 e un paragrafo grigio 17 px; le colonne sono separate da filetti verticali sottili. **La colonna 01 è riempita da un gradiente azzurro** verticale (chiaro in alto, saturo in basso) con testo bianco.

### Elementi
- **H2** 63 px w700; **sottotitolo** 22 px w700; **2 righe** 17 px grigio.
- **Carte** `carte-mano.webp` 1504×680 → 752×340 (2× esatto, **256 KB, il file più pesante del sito**): una sola immagine con le quattro carte già sventagliate, con ombra dentro il file.
- **Frase ponte** 22 px + strong azzurro.
- **Griglia 4 colonne**: numeri `DM Mono` 49 px w400, filetti `oklch(0.293)`, H3 22 px, p 17 px grigio; colonna attiva con `linear-gradient` azzurro.
- Nel DOM la colonna attiva **cambia**: su desktop è 01, nello screenshot mobile (`mobile-27.png`) è 04 → l'evidenza **cicla nel tempo** (keyframe `fo-momento`/`fo-luccichio`).

### Qualità grafica
Le carte da gioco sono l'illustrazione più curata del sito: coerenti con l'hero (inchiostro, teschi, oro), e la metafora «la mano che ti è stata data» viene dal testo. La griglia 01-04 con **numeri monospaziati** è il pattern di «indice di programma» che torna nel timer e nelle FAQ. Il gradiente azzurro sulla colonna attiva è **l'unico gradiente di tutta la pagina** oltre al logomark: usato una volta, si nota. Debole: 256 KB per una sola immagine; la colonna attiva animata può distrarre dalla lettura.

### Mobile (`mobile-25.png`, `mobile-26.png`, `mobile-27.png`)
Carte a piena larghezza (si vedono solo le parti alte); la griglia diventa **una colonna di quattro blocchi impilati**, ognuno con numero + filetto + titolo + testo; il blocco attivo (04 alla cattura) ha il gradiente azzurro.

### Cosa impariamo
Il programma in 4 punti si mostra come **griglia numerata in monospaziato con una colonna accesa**: un solo gradiente, sulla cosa importante.

---

## TAVOLA 19 — L'offerta: la tessera al collo, il prezzo, il timer
![](../capture/66-funneloperator-it/sezioni/19-funnel-operator.png)

### Cosa si vede
Sezione `#offerta`, sfondo nero con **texture di graffi e macchie bianche** a piena larghezza (CSS, non in `media/`). In alto «Avvia una carriera come» 37 px w500 bianco e sotto «FUNNEL **OPERATOR**» 50 px w800 con la seconda parola azzurra. Al centro **una tessera appesa a un laccio grigio con moschettone d'acciaio**: la tessera è azzurra con un'illustrazione fotocopiata in negativo (un uomo che corre con una lancia), in basso un pannello grigio chiaro con **quattro voci con spunta** («Prima pagina online in 24h», «Inizi a cercare clienti dopo 8:30 ore di corso», «Inizia carriera come Funnel Operator», «Garanzia consulenza con Andrei»), il logo Funnel Operator e un **QR code**. Sotto, «434 €» a 60 px w800, la riga grigia «Pagamento unico, accesso a vita. Dal 12 ottobre 2026: **560 €**.», poi il **timer** a quattro numeri 63 px w800 («28 13 08 12») con etichette in monospaziato minuscolo spaziato («giorni ore minuti secondi»), infine **due bottoni affiancati**: «Iscriviti adesso» azzurro pieno, testo nero, e «Cosa contiene il corso?» grigio scuro `oklch(0.22)`, testo bianco; entrambi 48 px alti, raggio 8 px, 14 px w500.

### Elementi
- **Eyebrow** 37 px + **H2** 50 px w800 + span azzurro.
- **Tessera** `tessera.webp` 840×1721 → 295×568 (2,85× in larghezza, 3,03× in altezza: **rapporto leggermente diverso**, 0,488 vs 0,519 → contain con bordi o crop minimo), 185 KB; laccio, moschettone, foro, QR e ombra sono **tutti dentro il file**.
- **Prezzo** 60 px w800 bianco; **riga prezzo futuro** 17 px grigio con `strong` bianco.
- **Timer**: 4 cifre 63 px w800 `Inter Tight` + etichette 14 px `DM Mono` con letter-spacing; la frase completa nel DOM è «Il prezzo sale tra 28 giorni 13 ore 08 minuti 14 secondi».
- **Bottone primario** `oklch(0.656 0.134 235.9)` fondo, testo `oklch(0.178)`; **bottone secondario** `oklch(0.22)` → `#programma`.
- **Texture** scura via CSS con blend.

### Qualità grafica
La tessera è **l'oggetto-prodotto**: il corso diventa un badge da evento che si può «indossare», con le quattro promesse stampate sopra. È fotorealistica (moschettone con riflessi) ma l'illustrazione dentro è in negativo azzurro, coerente col resto. Il timer usa la coppia «cifra grande sans / etichetta monospaziata» come la griglia 01-04. I due bottoni sono l'unica coppia CTA della pagina e stanno **sotto** prezzo e timer, non sopra. Debole: il testo del bottone primario è nero su azzurro (contrasto ~5:1, sufficiente ma meno netto del bianco); la tessera è servita a ~2,9× (più pesante del necessario).

### Mobile (`mobile-27.png`, `mobile-28.png`, `mobile-29.png`)
Titolo su due righe, tessera a ~60 % della larghezza, prezzo e timer a piena larghezza (cifre ~50 px), i due bottoni **impilati** a piena larghezza (azzurro sopra, grigio sotto).

### Cosa impariamo
L'offerta si **oggettivizza in una tessera fisica** con le promesse stampate; prezzo, scadenza e timer stanno sotto l'oggetto, i bottoni per ultimi.

---

## TAVOLA 20 — Il programma: la cartella con quattro linguette
![](../capture/66-funneloperator-it/sezioni/20-section.png)

### Cosa si vede
Sezione chiara `#programma`, alta 846 px, **senza titolo**. Al centro una **cartella d'archivio** disegnata in HTML: quattro fogli grigi (`oklch(0.87)`) con bordo nero 1 px e raggio 12 px, uno dietro l'altro, ogni foglio più piccolo del precedente e sfalsato in alto di ~60 px; ogni foglio ha **una linguetta nera trapezoidale** (`clip-path: polygon(...)` letto nel DOM, 4 volte) alternata a sinistra e a destra con la scritta bianca «01 Intro», «02 Landing pages», «03 Trovare clienti», «04 Domande comuni» (numero in grigio chiaro, testo bianco, 18,9 px w500). Davanti a tutto, la **cartella principale** (832×360) con il logo Funnel Operator nero grande al centro. Le linguette sono `button` (4 CTA nel DOM): cliccando si apre il modulo.

### Elementi
- **4 fogli** con linguetta: `button` 212×57 (238 per il quarto), `clip-path: polygon(0 100%, 12.27px 6.9px, … )` che disegna il trapezio con angoli arrotondati.
- **Cartella frontale** con `funops-logo-bianco.png` reso 372×111 con `filter: brightness(0)` (letto negli effetti: il PNG bianco reso nero).
- Nessun testo fuori dalla metafora.

### Qualità grafica
È il componente più originale della pagina: **un accordion travestito da raccoglitore**. Tutto CSS (bordi, clip-path, sovrapposizione), zero immagini oltre al logo. L'alternanza sinistra/destra delle linguette rende leggibili i quattro titoli senza sovrapporli. Debole: lo screenshot statico non dice che si può cliccare; nessuna «apri» o freccia. Il filtro `brightness(0)` sul PNG bianco è un trucco che funziona ma non è nitido come un SVG.

### Mobile (`mobile-29.png`)
La cartella si stringe a 390 px e **funziona ugualmente**: le linguette si alternano, il logo resta centrato. È il componente che regge meglio il passaggio a mobile.

### Cosa impariamo
Un indice di 4 moduli può essere **una cartella con linguette in clip-path**: metafora fisica costruita in puro CSS.

---

## TAVOLA 21 — «Il corso copre quasi ogni possibilità.» (consulenze + VSL 2 + accordion)
![](../capture/66-funneloperator-it/sezioni/21-il-corso-copre-quasi-ogni-possibil.png)

### Cosa si vede
Sfondo nero, sezione alta 1.423 px. H2 37 px w500 centrato. Sotto, un **rail di screenshot di videochiamate** (322×181, raggio 12 px): due riquadri con due volti affiancati e la barra di controlli rossa/bianca di una call (telefono rosso, condividi, chat, ingranaggio), un terzo con una persona in cuffia. Poi un paragrafo centrato 17 px con grassetti. Poi un **secondo poster video** 582×327 (stesso set della tavola 9, con sottotitolo bruciato «centinaia di consulenze.») con play. Infine un **accordion a quattro voci** su 832 px: ogni riga alta 80 px con a sinistra un **cerchio con «?»** (bordo 1 px grigio), la domanda 22 px w500 grigio chiaro, a destra un «+»; separatori 1 px.

### Elementi
- **H2** 37 px w500.
- **Rail consulenze**: `consulenza-1/2/3.webp` (321-329×181 → stessa misura, **1×**, 9 KB ciascuno) ×2 per il loop.
- **Paragrafo** 17 px con 2 `strong`.
- **Poster** `vsl-consulenza.webp` 1600×900 → 582×327 (2,75×), sottotitolo dentro il frame.
- **Accordion**: 4 `button` 594×80, cerchio «?» 40 px, testo `oklch(0.633)` 22 px, «+» a destra; keyframes `accordion-down/up`.

### Qualità grafica
Il rail delle call è **prova di servizio** (le consulenze esistono davvero, con volti veri). Il secondo video riprende lo stesso set: l'identità visiva del «set blu» si consolida. L'accordion con il «?» in cerchio è sobrio e coerente con le FAQ finali (stesso componente). Debole: i thumbnail delle call sono a 1× e sgranati; il sottotitolo bruciato nel poster è un artefatto.

### Mobile (`mobile-30.png`)
Titolo su due righe, rail delle call a piena larghezza (un riquadro per volta), paragrafo, poster a piena larghezza, accordion (righe più alte per il testo a capo).

### Cosa impariamo
La garanzia di consulenza si prova con **screenshot di call reali in un rail** + un secondo video nello stesso set + un accordion di dubbi.

---

## TAVOLA 22 — «Asset pronti per te» (le quattro righe alternate)
![](../capture/66-funneloperator-it/sezioni/22-asset-pronti-per-te.png)

### Cosa si vede
Sfondo nero. H2 63 px w600 centrato, sottotitolo 22 px w500, riga grigia 17 px. Poi **quattro righe separate da filetti**, ognuna alta ~166 px, in **zig-zag**: riga 1 testo a sinistra («Template landing» 29 px w600 + paragrafo grigio) e a destra un **foglio bianco** (245×347) con il documento «Fase 1 - Small talk / Fase 2 - Conferma discovery» con evidenziazioni giallo-verdi; riga 2 foglio a sinistra («Template - Struttura primo messaggio (M1)») e testo a destra allineato a destra («Template sezioni»); riga 3 come la 1 («Script chiamate», stesso foglio della riga 1); riga 4 come la 2 («Script messaggi», stesso foglio della riga 2). **I fogli sono tagliati dal filetto della riga successiva** (`overflow: hidden`): si vede solo la parte alta di ogni documento. Chiude «E tanto altro» 22 px + riga grigia.

### Elementi
- **H2** 63 px w600; **sottotitolo** 22 px; **riga** 17 px grigio.
- **4 righe** con `border-bottom` 1 px `oklch(0.293)`.
- **Fogli** `template-fasi.webp` 773×1094 → 245×347 (3,15×, 57 KB, usato 2 volte) e `template-messaggi.webp` 600×851 → 245×347 (2,45×, 44 KB, usato 2 volte): documenti reali con fondo bianco puntinato, pill nere con etichetta «Fase N» in giallo-verde, testo evidenziato, footer «Hack My Drive».
- **Titoli riga** 29 px w600; **paragrafi** 17 px grigio.

### Qualità grafica
I **documenti veri** (con evidenziatore) sono la prova che gli asset esistono; il taglio dal filetto li fa sembrare «archiviati» in un raccoglitore. Lo zig-zag riprende la tavola 3. Debole: due soli file per quattro righe (le righe 1/3 e 2/4 mostrano lo stesso documento) e l'alt della riga 3 dice «copione di una chiamata» mentre il file è lo stesso della riga 1.

### Mobile (`mobile-32.png`)
Ogni riga diventa foglio sopra + titolo + testo sotto, a piena larghezza; i fogli restano tagliati in basso.

### Cosa impariamo
Gli asset del corso si mostrano come **fogli veri tagliati dal filetto**, in righe alternate: il documento parziale incuriosisce più del documento intero.

---

## TAVOLA 23 — «Prima pagina online entro 24h»
![](../capture/66-funneloperator-it/sezioni/23-prima-pagina-online-entro-24h.png)

### Cosa si vede
Sezione chiara. H2 49 px w500 su due righe centrato («24h» in grassetto). Due righe 17 px centrate, la seconda in grassetto. Sotto, uno **screenshot largo** (666×286, raggio 12 px) di una home page di software (Notion: «Dove i team e gli agenti pensano insieme.» con bacheca sotto), **tagliato in basso** dal contenitore. Chiude «Tutorial **chiarissimi**.» 29 px con corsivo grassetto.

### Elementi
- **H2** 49 px + strong.
- **2 righe** 17 px, seconda w700.
- **Screenshot** `lovable.webp` 1200×651 → 666×286: rapporto originale 1,84, reso 2,33 → **ritagliato dal CSS in altezza** (`object-fit: cover`, si perde il fondo). **Nota**: l'alt descrive «L'editor di Lovable con una landing page in costruzione», ma il file mostra la **home page di Notion** (identica a `sito-notion.webp`): immagine e didascalia non coincidono.
- **Chiusura** 29 px w500 + `em strong`.

### Qualità grafica
Sezione leggera e veloce, funziona come pausa. Debole: è l'unica immagine ritagliata dal CSS, e mostra il sito sbagliato rispetto all'alt (o un placeholder rimasto): un errore di produzione visibile a chi conosce Notion.

### Mobile (non campionata: tra `mobile-33.png` e `mobile-34.png`)
Screenshot a piena larghezza, titolo su tre righe.

### Cosa impariamo
Anche un sito curato lascia **un'immagine placeholder**: il gate «alt = contenuto» va nel nostro processo.

---

## TAVOLA 24 — «Community su Telegram» (iPhone + aeroplani)
![](../capture/66-funneloperator-it/sezioni/24-community-su-telegram.png)

### Cosa si vede
Sezione chiara. In alto centrata l'**icona Telegram** in stile iOS (quadrato arrotondato azzurro con alone, 89×91). H2 49 px w600 con «Telegram» azzurro. Due righe 17 px centrate. Sotto, un **iPhone frontale** (326×404, si vede solo la metà superiore: notch, schermata del gruppo «Funnel Operator» con avatar FO, tre pulsanti «mute / search / more», «Add Members», due membri con nomi sfocati). **Due aeroplani di carta** bianchi, grandi e sfumati, uno a sinistra dietro il testo e uno a destra dietro il telefono, con `blur(3.55px)` letto negli effetti.

### Elementi
- **Icona** `telegram.webp` 178×182 → 89×91 (2×).
- **H2** 49 px + strong azzurro; **2 paragrafi** 17 px.
- **iPhone** `community-iphone.webp` 326×404 → 326×404 (**1×**, 11 KB; il frame del telefono è nel file), tagliato dal fondo sezione.
- **Aeroplani** `aeroplano.webp` 808×473 → 405×237 e 297×212 (2 istanze, una specchiata), `filter: blur(3.55px)`, opacità ridotta.

### Qualità grafica
Il **doppio piano** (aeroplani sfocati dietro, telefono nitido davanti) dà profondità di campo con due file leggeri (14 KB + 11 KB). La metafora Telegram (aeroplano di carta) è letterale ma elegante perché desaturata. Debole: il mockup iPhone a 1× è morbido su retina; i nomi sfocati nell'immagine sono un po' grezzi.

### Mobile (`mobile-35.png`)
Icona, titolo su due righe, testo, iPhone a ~80 % della larghezza centrato; gli aeroplani scompaiono o restano ai margini.

### Cosa impariamo
Un mockup di telefono vale di più con **un elemento sfocato dietro**: profondità a costo zero.

---

## TAVOLA 25 — «Troverai veramente clienti?» (lo stack a scala + la checklist)
![](../capture/66-funneloperator-it/sezioni/25-troverai-veramente-clienti.png)

### Cosa si vede
Sezione chiara alta 2.301 px, colonna stretta (≈620 px, x 410→1030), allineata a sinistra. H2 49 px w700, tre paragrafi corti con corsivi e grassetti. H3 37 px w700 «Per 10 mesi abbiamo testato metodi…». Paragrafo giustificato. Poi **lo stack: quattro card a scala** (290×185, raggio 24, bordo 1 px nero) sfalsate sinistra/destra, collegate da **linee tratteggiate a gomito** come la tavola 7, ma qui ogni card contiene **un'icona a colori grande centrata che sfuma verso il basso** (fade) e sotto l'etichetta 22-24 px: logo Instagram (gradiente viola-rosa) «DM su Instagram», logo Loom (viola) «Loom», icona FaceTime (giallo-arancio) «Call», **badge blu di verifica** «Chiusura progetto»; la linea finale scende con una freccia. Sotto: «E lo abbiamo testato su più di **13k leads** nel corso di 10 mesi.» 29 px centrato. H3 «Ti diamo materiale di vendita» 37 px, «Ovvero:» 17 px, e una **tabella a una colonna** (365 px larga, bordo 1 px nero, raggio 8, righe separate da filetti) con **cinque righe con segno di spunta** «Che messaggi mandare / Cosa dire nelle call / Come fare i preventivi, con template / Template per farti il sito / E molto altro…».

### Elementi
- **H2** 49 px w700; **H3** ×2 37 px w700; **paragrafi** 17 px.
- **Stack** `stack-clienti.webp` 1152×1832 → 576×916 (2× esatto, 93 KB): **è un'immagine**, card, connettori e icone compresi (ecco perché le icone sfumano: è un effetto raster). Alt vuoto; il testo è però ripetuto nel DOM come `ul` di 4 `li` (letto in `copy-integrale.md`: «DM su Instagram / Loom / Call / Chiusura progetto»).
- **Frase 13k** 29 px w500 + strong.
- **Checklist**: `ul` 5 `li`, bordo 1 px nero, raggio 8, filetti interni, spunta ✓ come icona inline 16 px, testo 16 px.

### Qualità grafica
Lo stack ripete la **grammatica della tavola 7** (card a scala + connettori tratteggiati) cambiando il contenuto: icone a colori invece di glifi neri. Il lettore riconosce «un processo» prima di leggere. Le icone che sfumano verso il basso danno l'effetto «riflesso» tipico degli app icon. La checklist con bordo e filetti è la forma più pulita di «lista di consegne» del sito. Debole: lo stack è raster (non selezionabile), e i colori vividi delle icone sono l'unico punto in cui la palette si apre in una sezione chiara.

### Mobile (`mobile-36.png`, `mobile-37.png`)
Lo stack si stringe (le card restano sfalsate perché è un'immagine), la freccia finale resta; la frase 13k va su tre righe; la checklist a piena larghezza con righe che vanno a capo.

### Cosa impariamo
Un metodo di acquisizione si disegna come **stack a scala con le icone reali dei tool** (Instagram, Loom, FaceTime) e finisce con un badge: il lettore lo riconosce in mezzo secondo.

---

## TAVOLA 26 — «Registrazioni chiamate di vendita di AP Sales»
![](../capture/66-funneloperator-it/sezioni/26-registrazioni-chiamate-di-vendita.png)

### Cosa si vede
Sezione chiara, bassa. H2 37 px w600 centrato, paragrafo 17 px centrato su due righe con «per davvero» in grassetto. Sotto, **due screenshot sovrapposti in diagonale**: a sinistra e più in alto un frame di videochiamata con un uomo dal **volto pixelato** con la mano sul mento (458×251); a destra e più in basso, **sovrapposto** al primo, uno screenshot di una lavagna digitale con appunti a mano («pain point imprenditori…», «lead magnet: come scegliere la giusta agenzia», «1) come lavorano la agency 2) red flags ✗ 3) green flags ✓», frecce disegnate) e, in alto a destra, il cerchio della webcam con un altro volto pixelato.

### Elementi
- **H2** 37 px w600; **paragrafo** 17 px + strong.
- **Frame call** `call-cliente.webp` 966×530 → 458×251 (2,1×, 44 KB), raggio 12 px.
- **Lavagna** `call-lavagna.webp` 966×530 → 458×251 (2,1×, 50 KB), raggio 12 px, **sovrapposta** con `translate` e z-index superiore.

### Qualità grafica
La **sovrapposizione diagonale** di due screenshot dice «materiale grezzo, tanto» con due soli file. I volti pixelati (non sfocati: pixel grossi) sono una scelta stilistica coerente con la tavola 13. La lavagna con scrittura a mano è la prova più «umana» di tutta la pagina. Debole: senza bordo o ombra i due frame si confondono col grigio di fondo dove le immagini sono chiare.

### Mobile (`mobile-38.png`)
I due frame si **impilano** (call sopra, lavagna sotto) a piena larghezza, senza sovrapposizione.

### Cosa impariamo
Le registrazioni si mostrano con **due frame sovrapposti in diagonale, volti pixelati**: il grezzo è la prova.

---

## TAVOLA 27 — Le tre obiezioni («Se questo metodo funziona così bene, perché lo insegni?»)
![](../capture/66-funneloperator-it/sezioni/27-se-questo-metodo-funziona-cos-ben.png)

### Cosa si vede
Sfondo nero, **solo testo**, allineato a sinistra su 832 px. Tre blocchi: H3 tra virgolette basse 37 px w700 (su due righe) + paragrafo 17 px lh 27 grigio chiaro. Nessuna immagine, nessun CTA, nessun filetto.

### Elementi
- **3 H3** 37 px w700 `Plus Jakarta Sans`.
- **3 paragrafi** 17 px w400 `oklch(0.934)`.

### Qualità grafica
Tipografia nuda: i titoli a 37 px tra virgolette funzionano da «voce del lettore», le risposte in tondo da «voce di Andrei». Ritmo regolare (titolo/risposta ×3). È la sezione più leggibile della pagina proprio perché non giustifica il testo. Debole: nulla.

### Mobile (non campionata: `mobile-39.png`)
Titoli su 3-4 righe, testo a piena larghezza.

### Cosa impariamo
Le obiezioni non hanno bisogno di componenti: **titolo tra virgolette + risposta**, per tre volte.

---

## TAVOLA 28 — «Questo percorso lo descrivo con una sola frase: cambiare vita.»
![](../capture/66-funneloperator-it/sezioni/28-questo-percorso-lo-descrivo-con-un.png)

### Cosa si vede
Sezione chiara. H2 49 px w700 centrato su due righe con «cambiare vita» in azzurro. Sotto, due colonne: a sinistra una foto verticale (269×354) di un ragazzo seduto sul davanzale di una finestra con **infissi rossi**, cuffie, canotta, che guarda il telefono, palazzi chiari fuori; a destra tre paragrafi 17 px giustificati e il **bottone «Sono pronto ↗»** azzurro pieno con testo bianco, 154×48, raggio 8, freccia in alto a destra.

### Elementi
- **H2** 49 px w700 + strong azzurro.
- **Foto** `cambiare-vita.webp` 538×710 → 269×354 (2×, 52 KB), raggio 12 px, dentro un `<picture>`.
- **3 paragrafi** 17 px giustificati.
- **Bottone** `oklch(0.656 0.134 235.9)` con testo `#ffffff` (qui bianco, nella tavola 19 nero) + icona freccia ↗.

### Qualità grafica
La foto porta il **rosso** (infissi) che il sito usa con parsimonia: la palette torna a chiudersi. Il bottone con la freccia ↗ è il più leggibile della pagina (bianco su azzurro). Debole: incoerenza minima tra questo bottone (testo bianco) e «Iscriviti adesso» (testo nero) — stesso fondo, due colori di testo.

### Mobile (`mobile-41.png`)
Foto a piena larghezza sopra il testo, bottone a larghezza contenuto allineato a sinistra.

### Cosa impariamo
Il CTA di chiusura sta **accanto a una foto di vita**, non sotto il prezzo: prima l'immagine di dove si arriva, poi il bottone.

---

## TAVOLA 29 — FAQ (due gruppi, quattordici voci) + disclaimer
![](../capture/66-funneloperator-it/sezioni/29-faq.png)

### Cosa si vede
Sfondo nero, sezione alta 1.719 px. H2 «FAQ» 37 px w700 allineato a sinistra. Due gruppi introdotti da una **eyebrow in monospaziato azzurro chiaro** 14 px («FUNNEL OPERATOR», «PAGAMENTO») seguita da un filetto bianco più marcato; sotto, righe di accordion alte 80 px: **cerchio con «?»** a sinistra, domanda 22 px w500 grigio, «+» a destra, filetto sottile tra le righe. 9 voci nel primo gruppo, 5 nel secondo. In fondo, dopo un filetto, il **disclaimer** 12 px grigio su tre righe con «Disclaimer.» in grassetto bianco.

### Elementi
- **H2** 37 px w700.
- **Eyebrow** ×2 `DM Mono` 14 px `oklch(0.808 0.09 238.3)` (azzurro desaturato) + filetto 1 px chiaro.
- **Accordion** 14 `button` 832×80: cerchio 40 px bordo 1 px `oklch(0.293)`, «?» 16 px, testo `oklch(0.633)` 22 px, «+» 16 px; 28 nodi media (icone inline ripetute).
- **Disclaimer** 12 px `oklch(0.633)` + strong.

### Qualità grafica
Le FAQ riusano **esattamente** il componente della tavola 21 (cerchio «?» + riga + «+»), e le eyebrow in monospaziato riusano il carattere del timer e dei numeri 01-04: tre pattern, un sistema. Il raggruppamento in due sezioni con etichetta azzurra è ordine visivo puro. Debole: 14 voci chiuse sono una parete uniforme; nessuna aperta di default.

### Mobile (`mobile-41.png`, `mobile-44.png`)
Identico impianto; le domande vanno su due righe, il cerchio resta allineato in alto.

### Cosa impariamo
Le FAQ si **raggruppano con eyebrow in monospaziato** e riusano il componente accordion già visto: zero componenti nuovi a fine pagina.

---

## TAVOLA 30 — Footer
![](../capture/66-funneloperator-it/sezioni/30-footer.png)

### Cosa si vede
Fascia scura (272 px) con bordo superiore 1 px (`border-t border-fo-line`). A sinistra il logo Funnel Operator bianco (107×32) e, sulla stessa riga, i link «Agenzia» e «Corsi» in grigio 14 px. Sotto, la ragione sociale «Andrei Pascu Sales · P.IVA 02001850474 · Viale Giacomo Matteotti 15, 50121 Firenze (FI)». Sotto, i link «Privacy · Termini · Cookie · Preferenze cookie · Assistenza» separati da punti mediani. Sotto, «© 2026 Funnel Operator». Tutto allineato a sinistra su 832 px, tutto 14 px w500 grigio.

### Elementi
- **Logo** `funops-logo-bianco.png` (terzo uso).
- **Link** ×2 esterni (`apsales.eu`, `bsns.it`), ×4 interni + 1 `button` («Preferenze cookie»).
- **Ragione sociale** con P.IVA e indirizzo (coincide con il JSON-LD `Organization` letto in `design-tokens.json`).
- **Copyright**.

### Qualità grafica
Footer in quattro righe, un solo corpo, un solo colore: sobrio come le FAQ. La P.IVA e l'indirizzo fisico in chiaro sono un elemento di fiducia. Debole: il PNG del logo a 107 px da un file 804 px è sovradimensionato; niente social, niente newsletter (scelta coerente con la pagina di vendita).

### Mobile (`mobile-44.png`)
Identico, i link vanno a capo su due righe.

### Cosa impariamo
Footer = **ragione sociale + legale + un logo**, quattro righe; niente colonne.

---

# B. CATALOGO TRASVERSALE DEGLI ELEMENTI

| # | Nome nostro | Volte | Sezioni | Funzione persuasiva | Qualità (1-5) e motivo | File in `media/` |
|---|---|---|---|---|---|---|
| 1 | **Illustrazione-xilografia** (bianco su nero, grana) | 6 | 1, 2, 5, 15, 18, 19 (dentro la tessera) | Registro «memento mori»: morte, guerra, tesoro — spinge all'azione ora | 5 — stessa mano su tutta la pagina, 2× esatto | `soldato-caduto`, `gancio-insegna`, `carta-*` ×3, `carte-mano`, `motivo-*` ×3 |
| 2 | **Carta da gioco / carta-promessa** | 3 + 4 | 2, 18 | Le promesse come oggetti da collezione; «la mano che ti è stata data» | 5 — badge verificato + ventaglio + stesso raggio delle card | `carta-lezioni`, `carta-metodo`, `carta-landing`, `carte-mano` |
| 3 | **Mappa** (topografica con nodi e tratteggi) | 1 | 2 | «Metodo chiaro» = percorso su una mappa | 4 — leggibile ma piccola, i nodi non sono spiegati | `carta-metodo` |
| 4 | **Tessera / badge fisico** | 1 | 19 | Il corso diventa un oggetto da indossare con le promesse stampate | 5 — fotorealismo + QR + spunte dentro il file | `tessera` |
| 5 | **Insegna** (parola in maiuscolo su immagine, in cornice) | 1 | 5 | Battezza il servizio | 4 — cornice bianca unica, ma testo raster | `gancio-insegna` |
| 6 | **Avviso / documento ufficiale** (tessera metallica SEC) | 1 | 6 | Fonte terza resa oggetto | 5 — l'idea più forte del blocco editoriale | `sec-avviso` |
| 7 | **Screenshot di siti famosi** | 3 | 6, 23 | «Guarda tu stesso»: prova per esperienza | 3 — Apple a 1×, Notion usato al posto di Lovable | `sito-apple`, `sito-amazon`, `sito-notion`, `lovable` |
| 8 | **Screenshot di call** (volti pixelati) | 5 | 21, 26 | Le consulenze e le vendite esistono | 4 — grezzo convincente, ma 1× nei rail | `consulenza-1/2/3`, `call-cliente`, `call-lavagna` |
| 9 | **Template / foglio di lavoro** | 2 (×2) | 22 | Gli asset esistono e sono usati in agenzia | 4 — documenti veri, ma due soli per quattro righe | `template-fasi`, `template-messaggi` |
| 10 | **Portfolio in rail** | 3 (×12) | 11 | Abbondanza di lavori | 3 — tre soggetti che si ripetono | `esempio-*` ×3 |
| 11 | **Stack / scala a card con connettori tratteggiati** | 2 | 7 (HTML), 25 (immagine) | Il metodo è un percorso in passi | 5 — la grammatica più riconoscibile del sito | `passo-*` ×6, `funops-logomark-scuro`, `stack-clienti` |
| 12 | **Albero / organigramma** | 1 | 10 | Colloca il lettore nel sistema («Tu sei qui») | 5 — tre nodi, un puntatore | `albero-apsales` |
| 13 | **Cartella con linguette** (clip-path) | 1 | 20 | Indice del programma come raccoglitore fisico | 5 — puro CSS, regge su mobile | `funops-logo-bianco` (brightness 0) |
| 14 | **Griglia numerata 01-04** con colonna accesa | 1 | 18 | I 4 passi del programma | 4 — monospaziato + gradiente unico; l'animazione distrae | — |
| 15 | **Card gemelle con numero gigante** (1. / 2.) | 1 | 17 | Confronto tipo A / tipo B | 5 — bordo azzurro come unica differenza | — |
| 16 | **Prima/dopo fotografico** (bn vs colore) | 1 | 8 | Giudizio senza parole | 5 — codice colore/bn + barrato/verde | `fare-siti`, `fare-landing` |
| 17 | **Rail / marquee** | 5 | 4, 11 (×2), 17, 21 | Movimento = vita, abbondanza | 4 — `fo-rail` 45/70 s lineare, sempre taglia un item | vari |
| 18 | **Accordion con «?» in cerchio** | 18 righe | 21 (4), 29 (14) | Dubbi e FAQ | 4 — un solo componente riusato; nessuno aperto | — |
| 19 | **Numero grande + didascalia** | 4 + 4 + 4 | 4 (rail), 19 (timer), 18 (01-04) | Prova sociale, urgenza, indice | 5 — stessa coppia «cifra sans / etichetta piccola» ovunque | `ordini`, `studenti`, `apertura`, `trustpilot` |
| 20 | **Timer** | 1 | 19 | Urgenza (prezzo che sale) | 4 — cifre 63 px w800 + etichette DM Mono; manca la data in evidenza (c'è ma in grigio) | — |
| 21 | **Badge di verifica** (cerchio dentellato con spunta) | 3 + 1 + 1 | 2, 7, 25 | «Promessa certificata», traguardo | 5 — sempre lo stesso glifo, azzurro o verde | `carriera-avviata` |
| 22 | **Foto di Andrei** (documentaristiche) | 12 | 3, 9, 10, 12, 13, 21, 28 | Identità, storia, presenza | 4 — 2× quasi sempre, set blu ricorrente; la 10 è ruotata | `andrei-*`, `per-chi`, `storia-*`, `vsl-*`, `cambiare-vita` |
| 23 | **Avatar rotondo + firma** | 1 | 13 | Voce personale («Andre :)») | 4 | `andrei-tondo` |
| 24 | **Poster video con play** | 2 | 9, 21 | Il fondatore parla | 4 — stesso set = marchio; manca la durata | `vsl-principale`, `vsl-consulenza` |
| 25 | **Mockup telefono** | 1 | 24 | La community esiste | 3 — 1×, nomi sfocati grezzi | `community-iphone` |
| 26 | **Elemento sfocato di sfondo** (aeroplani) | 2 | 24 | Profondità di campo | 4 — `blur(3.55px)` + 14 KB | `aeroplano` |
| 27 | **Texture di fondo** (grana scura / carta / graffi) | 3 | 2, 16, 19 | Materia, non pixel | 4 — carta a 1× ma leggera, blend hard-light/screen | `carta-serpenti` (+ CSS) |
| 28 | **Fascia di testo che attraversa un'immagine** | 1 | 16 | Composizione da poster | 5 — un file duplicato e ruotato | `serpente-testa` |
| 29 | **Frase barrata + frase vera** (rosso/grigio → nero/verde) | 2 | 8, 17 | Sostituzione di una credenza | 5 — due colori, zero componenti | — |
| 30 | **Lista a filetti con glifo** | 1 | 15 | Tre motivi | 4 — incisioni a 1× | `motivo-*` |
| 31 | **Checklist in tabella** (bordo + spunte) | 1 | 25 | Cosa ricevi | 4 | — |
| 32 | **Zig-zag testo/immagine** | 2 | 3, 22 | Ritmo, dialogo | 4 — il testo allineato a destra pesa | — |
| 33 | **Fogli tagliati dal filetto** | 4 | 22 | Curiosità (documento parziale) | 4 | `template-*` |
| 34 | **Bottone pieno azzurro** | 3 | 19, 28, sticky mobile | Azione | 4 — testo nero in 19, bianco in 28 (incoerenza) | — |
| 35 | **Bottone secondario grigio** | 1 | 19 | Ancora al programma | 4 | — |
| 36 | **CTA sticky mobile** «Ottieni accesso» | 1 | tutte (mobile) | Azione sempre a portata | 5 — pill, blur, angolo basso destro, non copre il testo | — |
| 37 | **Eyebrow in monospaziato** | 2 + 4 | 29, 19 (etichette timer) | Ordine, «schedario» | 5 — DM Mono usato solo per metadati | — |
| 38 | **Titolo con marchio inline** | 1 | 11 | Firma d'autore | 5 | `apsales.svg` |
| 39 | **Logo AI a colori in rail** | 7 | 17 | Attualità, tool reali | 4 — 40 px contenuti | `ai-*` ×5 |
| 40 | **Sovrapposizione diagonale di screenshot** | 1 | 26 | Materiale grezzo, tanto | 4 | `call-*` |
| 41 | **Footer legale** | 1 | 30 | Fiducia | 4 | `funops-logo-bianco` |
| 42 | **Testata con doppio marchio** (FO + APsales) | 1 | header | Il corso appartiene a un'agenzia | 4 — PNG sovradimensionato | `funops-logo-bianco`, `apsales.svg` |

---

# C. LE IMMAGINI

Fonte: `media-inventario.md` (68 file, 2.511 KB) + visione diretta di 38 file + lettura del sorgente degli 8 SVG. «Servita a» = px originali / px resi (ideale 2×). «Ritaglio» = confronto tra rapporto originale e rapporto reso.

| File | Cosa rappresenta | Stile | Legame col testo (alt / sezione) | Formato · peso | Servita a | Ritaglio CSS |
|---|---|---|---|---|---|---|
| `carte-mano.webp` | 4 carte K Q J A seme «$»: re e regina scheletri con tesori, fante caprone col pugnale, asso-calice d'oro | Illustrazione a inchiostro, bn, ombra nel file | Alt completo; T18 «conoscere la mano che ti è stata data» | WEBP 256 KB (il più pesante) | 1504×680 → 752×340 = **2,0×** | No (2,21 = 2,21) |
| `soldato-caduto.webp` | Cavaliere in ginocchio trafitto da frecce, aureola, topi | Xilografia bianco su nero | Alt vuoto; T1 «Un giorno morirai.» | WEBP 218 KB | 1664×1236 → 832×618 = **2,0×** | No |
| `tessera.webp` | Badge azzurro con laccio e moschettone, 4 spunte, logo, QR | Fotorealismo + illustrazione in negativo | Alt completo (elenca le 4 promesse); T19 | WEBP 185 KB | 840×1721 → 295×568 = **2,85× / 3,03×** | Minimo (0,488 vs 0,519): contain o crop di ~6 % |
| `gancio-insegna.webp` | Cavaliere con spada + scritta «LANDING PAGES.» | Xilografia bn con testo raster | Alt «Landing pages.»; T5 | WEBP 169 KB | 1662×518 → 832×259 = **2,0×** | No |
| `albero-apsales.webp` | Organigramma 3 pillole + «Tu sei qui» | Grafica vettoriale rasterizzata, chiaro | Alt descrive l'albero; T10 | WEBP 105 KB | 1586×656 → 793×328 = **2,0×** | No |
| `sec-avviso.webp` | Tessera metallica argento con citazione SEC in monospaziato | Rendering metallico (riflessi), bn | Alt cita il testo; T6 link sec.gov | WEBP 98 KB | 894×624 → 447×312 = **2,0×** | No |
| `stack-clienti.webp` | 4 card a scala con icone Instagram, Loom, FaceTime, badge blu, connettori tratteggiati | Grafica UI a colori con fade | Alt vuoto (testo ripetuto in `ul`); T25 | WEBP 93 KB | 1152×1832 → 576×916 = **2,0×** | No |
| `serpente-testa.webp` | Testa di serpente nero a fauci aperte, zanne, lingua | Fotografia/3D bn ad alto contrasto | Alt vuoto; T16 «Schiavizzerai l'AI» — usata ×2 (una ruotata 180°) | WEBP 78 KB | 1438×1708 → 719×854 = **2,0×** | No (ma tagliata dal contenitore di sezione) |
| `sito-amazon.webp` | Home Amazon con griglia offerte | Screenshot a colori | Alt «La pagina iniziale di Amazon»; T6 | WEBP 62 KB | 814×440 → 408×221 = **2,0×** | No |
| `andrei-telefono.webp` | Andrei in giacca e cravatta, ristorante in alto, skyline notturno | Fotografia a colori, luce ambiente | Alt completo; T10 «Titolare AP Sales» | WEBP 59 KB | 598×634 → 306×324 = **1,95×** | No |
| `template-fasi.webp` | Documento «Fase 1 Small talk / Fase 2 / Fase 3» con evidenziatore | Screenshot documento, fondo bianco puntinato | Alt ok (T22 riga 1) ma riga 3 lo riusa con alt «copione di chiamata» | WEBP 57 KB | 773×1094 → 245×347 = **3,15×** | No (tagliato dal filetto, non dal CSS dell'img) |
| `carta-metodo.webp` | Mappa topografica in negativo con nodi, tratteggi, bussola | Illustrazione bn granulosa | Alt vuoto; T2 «Metodo chiaro» | WEBP 57 KB | 594×746 → 295×370 = **2,0×** | No |
| `vsl-consulenza.webp` | Andrei al set blu, sottotitolo «centinaia di consulenze.» | Fotogramma video a colori | Alt vuoto; T21 | WEBP 56 KB | 1600×900 → 582×327 = **2,75×** | No |
| `cambiare-vita.webp` | Ragazzo sul davanzale rosso con cuffie e telefono | Fotografia a colori | Alt completo; T28 «cambiare vita» | WEBP 52 KB | 538×710 → 269×354 = **2,0×** | No |
| `per-chi.webp` | Andrei che indica il portatile col logo FO, neon azzurro | Fotografia a colori | Alt completo; T12 | WEBP 52 KB | 642×682 → 321×341 = **2,0×** | No |
| `call-lavagna.webp` | Lavagna digitale con appunti a mano + webcam pixelata | Screenshot a colori | Alt completo; T26 | WEBP 50 KB | 966×530 → 458×251 = **2,1×** | No |
| `vsl-principale.webp` | Andrei al set blu, mani intrecciate | Fotogramma video a colori | Alt vuoto; T9 | WEBP 45 KB | 1600×900 → 830×466 = **1,93×** | No |
| `fare-landing.webp` | Profilo curato a colori, **bordo verde nel file** | Fotografia a colori | Alt completo; T8 «dopo» | WEBP 45 KB | 594×726 → 298×364 = **2,0×** | No |
| `template-messaggi.webp` | Documento «Template - Struttura primo messaggio (M1)» Instagram/LinkedIn | Screenshot documento | Alt completo; T22 righe 2 e 4 | WEBP 44 KB | 600×851 → 245×347 = **2,45×** | No |
| `call-cliente.webp` | Uomo con volto pixelato in call, mano sul mento | Screenshot a colori sfocato | Alt completo; T26 | WEBP 44 KB | 966×530 → 458×251 = **2,1×** | No |
| `carta-landing.webp` | Cronometro militare con «24» a segmenti e spunta | Illustrazione bn granulosa | Alt vuoto; T2 «1° landing page» | WEBP 43 KB | 594×746 → 314×385 = **1,9×** | No |
| `fare-siti.webp` | Profilo bn con taglio disordinato e auricolare | Fotografia bianco e nero | Alt completo; T8 «prima» | WEBP 42 KB | 596×726 → 298×362 = **2,0×** | No |
| `storia-riunione.webp` | 5 uomini in giacca a un tavolo, volti pixelati, MacBook | Fotografia a colori desaturata | Alt completo; T13 | WEBP 41 KB | 626×470 → 313×235 = **2,0×** | No |
| `andrei-scrivania.webp` | Andrei alla scrivania con monitor HP e microfono | Fotografia a colori, luce fredda | Alt completo; T3 | WEBP 41 KB | 702×534 → 351×267 = **2,0×** | No |
| `carta-lezioni.webp` | Terminale anni '80 con «0 to landing page» | Illustrazione bn granulosa | Alt vuoto; T2 «Lezioni complete» | WEBP 39 KB | 594×746 → 295×370 = **2,0×** | No |
| `storia-cucina.webp` | Andrei al portatile in cucina gialla | Fotografia a colori | Alt completo; T13 | WEBP 35 KB | 642×342 → 321×172 = **2,0×** | No |
| `lovable.webp` | **Home page di Notion** («Dove i team e gli agenti pensano insieme») | Screenshot a colori | **Alt errato**: «L'editor di Lovable con una landing page in costruzione»; T23 | WEBP 35 KB | 1200×651 → 666×286 = **1,8× / 2,28×** | **Sì**: rapporto 1,84 → 2,33, tagliata in basso (`object-fit: cover`) — unica del sito |
| `zero-clienti.webp` | Portatile con «ZERO CLIENTI?» su finto CRM, luce blu | Fotografia a colori | Alt completo; T3 | WEBP 31 KB | 700×534 → 350×267 = **2,0×** | No |
| `funops-logo-bianco.png` | Wordmark + logomark bianchi | PNG con alfa | Alt «Funnel Operator»; header, T20 (reso nero via `brightness(0)`), footer | PNG 30 KB | 804×240 → 107×32 = **7,5×** (sovradimensionato); in T20 372×111 = 2,2× | No |
| `sito-notion.webp` | Home Notion | Screenshot | Alt ok; T6 | WEBP 28 KB | 814×440 → 408×221 = **2,0×** | No |
| `carta-serpenti.webp` | Texture di carta con fibre e puntini | Foto di carta, quasi bianca | Alt vuoto; T16 sfondo | WEBP 21 KB | 1440×928 → 1440×928 = **1,0×** | No (è la sezione stessa) |
| `esempio-apsales.webp` | Pagina «Chi siamo» di AP Sales, box blu «La speranza non è una strategia» | Screenshot scuro | Alt ok; T11 | WEBP 13 KB | 400×560 → 209×293 = **1,9×** | No |
| `aeroplano.webp` | Aeroplano di carta bianco | Rendering 3D bianco | Alt vuoto; T24 sfondo sfocato ×2 | WEBP 14 KB | 808×473 → 405×237 = **2,0×** (e 297×212 = 2,7×) | No |
| `andrei-tondo.webp` | Andrei al microfono, segno di pace | Fotografia a colori | Alt completo; T13 avatar | WEBP 14 KB | 248×248 → 124×124 = **2,0×** | No (cerchio via CSS) |
| `community-iphone.webp` | iPhone con schermata gruppo Telegram «Funnel Operator» | Mockup + screenshot | Alt completo; T24 | WEBP 11 KB | 326×404 → 326×404 = **1,0×** | Tagliato dal fondo sezione |
| `consulenza-1/2/3.webp` | Riquadri di videochiamata con controlli rossi | Screenshot | Alt ok; T21 rail | WEBP 9 KB ×3 | ~322×181 → stessa = **1,0×** | No |
| `sito-apple.webp` | Home iPhone Apple | Screenshot | Alt ok; T6 | WEBP 6 KB | 830×220 → 832×221 = **1,0×** | No |
| `passo-2…7.webp` | Glifi neri pieni: checklist, dispositivo, globo, persone, grafico, PayPal | Icone raster monocrome | Alt vuoto; T7 step 2-7 | WEBP 2-5 KB | 256×256 → 110-161 = **1,6-2,3×** | No (sbordano per `overflow`) |
| `ai-claude/chatgpt/github/lovable/krea.webp` | Loghi ufficiali a colori | Icone raster | Alt = nome tool; T17 rail | WEBP 1-4 KB | 80×80 → 40×40 = **2,0×** | No |
| `motivo-teschio/spade/lapide.webp` | Incisioni bn: teschio, spade incrociate, lapide | Xilografia in miniatura | Alt vuoto; T15 lista | WEBP 2-3 KB | 60×60 → 60×60 = **1,0×** | No |
| `telegram.webp` | Icona Telegram stile iOS con alone | Icona raster | Alt vuoto; T24 | WEBP 3 KB | 178×182 → 89×91 = **2,0×** | No |
| `apsales.svg` | Wordmark «APsales» con logomark, `#008CCE` | Vettoriale | Alt «AP Sales»; header, T11 | SVG 3 KB | vettoriale | — |
| `funops-logomark-gradiente.svg` | Logomark FO due path con gradiente verticale | Vettoriale | Alt vuoto; T2 | SVG 1 KB | vettoriale | — |
| `funops-logomark-scuro.svg` | Logomark FO `#131313`, `aria-label` «Funnel Operator» | Vettoriale | T7 step 1 | SVG 1 KB | vettoriale | — |
| `ordini.svg` / `studenti.svg` / `apertura.svg` | Carrello / tre persone / doppia freccia, `#111111` | Vettoriali monocromi | Alt vuoto; T4 rail | SVG 1-7 KB | vettoriali | — |
| `trustpilot.svg` | Stella `#00B67A` con lembo `#005128` | Vettoriale ufficiale | T4 | SVG 359 B | vettoriale | — |
| `carriera-avviata.svg` | Badge dentellato con spunta | Vettoriale | T7 traguardo | SVG 4 KB | vettoriale | — |

## Sintesi delle immagini

**Conteggio per natura (68 file unici):**
- **Illustrazioni originali** (xilografia/inchiostro/negativo): 10 — `soldato-caduto`, `gancio-insegna`, `carta-lezioni`, `carta-metodo`, `carta-landing`, `carte-mano`, `motivo-teschio`, `motivo-spade`, `motivo-lapide`, più l'illustrazione dentro `tessera`. Un solo registro: bianco su nero, grana, nessun grigio medio, soggetti «morte/guerra/tesoro/strumenti».
- **Foto vere di Andrei**: 12 — `andrei-scrivania`, `andrei-telefono`, `andrei-tondo`, `per-chi`, `storia-ufficio`, `storia-cucina`, `storia-monitor`, `storia-tavolo`, `storia-palestra`, `fare-siti`/`fare-landing` (stesso soggetto, verosimilmente lui), `cambiare-vita`; più 2 fotogrammi video (`vsl-principale`, `vsl-consulenza`) e 1 foto di team (`storia-riunione`). Totale 15 fotografie.
- **Foto-oggetto costruite** (still life fotografici con grafica dentro): 3 — `zero-clienti`, `tessera`, `sec-avviso`.
- **Screenshot**: 13 — 3 siti famosi (`sito-apple`, `sito-amazon`, `sito-notion`) + `lovable` (Notion), 3 portfolio (`esempio-*`), 3 call (`consulenza-*`), 2 registrazioni (`call-*`), 2 documenti (`template-*`), 1 mockup telefono (`community-iphone`).
- **Diagrammi rasterizzati**: 2 — `albero-apsales`, `stack-clienti`.
- **Icone/glifi raster**: 6 `passo-*` + 5 `ai-*` + `telegram` = 12.
- **SVG**: 8 — 3 marchi (`apsales`, `funops-logomark-gradiente`, `funops-logomark-scuro`), 4 icone del rail numeri (`ordini`, `studenti`, `apertura`, `trustpilot`), 1 badge (`carriera-avviata`).
- **Texture/atmosfera**: 2 — `carta-serpenti`, `aeroplano` (+ `serpente-testa` come figura di poster).
- **Logo PNG**: 1 — `funops-logo-bianco`.

**Servizio a 2×:** 40 file su 60 raster sono serviti tra 1,9× e 2,1×; 5 oltre 2,4× (`tessera` 2,9×, `template-fasi` 3,15×, `vsl-consulenza` 2,75×, `template-messaggi` 2,45×, `funops-logo-bianco` 7,5×); **8 a 1×** (`carta-serpenti`, `community-iphone`, `consulenza-1/2/3`, `sito-apple`, `motivo-*` ×3). **Una sola immagine ritagliata dal CSS**: `lovable.webp` (T23), che è anche quella con alt sbagliato.

**Il registro visivo comune.** Tre famiglie, una palette:
1. **Nero + bianco a grana** (illustrazioni, insegna, serpenti, texture): nessun grigio medio, tratto inciso.
2. **Fotografia «luce blu»** (set con libreria retroilluminata, neon azzurro, ufficio con LED): le foto di Andrei hanno quasi tutte una dominante blu fredda che coincide con l'azzurro di accento del sito (`oklch(0.656 0.134 235.9)`). Le uniche foto calde sono la cucina gialla (passato) e gli infissi rossi di `cambiare-vita` (futuro).
3. **Grafica UI chiara** (albero, stack, cartella, tessera SEC): grigio `oklch(0.946)`/`oklch(0.87)`, bordi 1 px neri, raggi 8-24.

**Come tiene insieme fotografia e illustrazione.** Con tre regole applicate ovunque: (a) le illustrazioni stanno **solo sulle sezioni nere**, le foto stanno **soprattutto sulle sezioni chiare** (eccezioni: T12 e T21 su nero, ma con luce blu che si fonde col fondo); (b) le foto sono **desaturate verso il blu**, così non litigano con il bn delle illustrazioni; (c) tutto ha **lo stesso raggio** (12 px foto e card, 24 px nodi) e lo stesso bordo 1 px. Il rosso compare in tre punti soli (hero, barrato, infissi) e il verde in tre (Trustpilot, «Fare landing pages.», «Carriera avviata»): sono segnali, non palette.

---

# D. GLI SCHEMI, LE MAPPE, I DIAGRAMMI

| # | Nome | Sezione | Forma esatta | Nodi e testo dentro | Funzione | Come lo ricostruiamo |
|---|---|---|---|---|---|---|
| D1 | **Scala dei 7 step** | T7 | 7 card 290×140 raggio 24 bordo 1 px, sfalsate sinistra/destra di ~190 px, collegate da linee tratteggiate a gomito (esce a destra → scende → entra a sinistra), freccia finale verso il traguardo | «Step 1 Studia Funnel Operator.» → «Step 7 Primo cliente pagante.» → «Carriera avviata ✓» verde | Mostra che il percorso è finito e lineare | **HTML/CSS**: `ol` con `li` in grid a 2 colonne alternate (`nth-child(odd/even)`), connettori come `::after` con `border: 1px dashed` su due lati (L rovesciata), icona in `position:absolute; left:-20px` con `overflow:hidden` sulla card. Freccia finale SVG 8×8. Zero immagini per i connettori |
| D2 | **Albero AP Sales** | T10 | 3 pillole (raggio pieno, bordo 1 px nero, grigio `oklch(0.946)`): 1 in alto centrata, 2 sotto affiancate; linea verticale 2 px dal nodo alto, che si biforca ad angolo retto con raccordo arrotondato verso i due figli; puntatore azzurro (pallino + chevron) con etichetta «Tu sei qui» a sinistra del figlio sinistro | «AP Sales» (logomark) / «Formazione» (icona portatile) / «Agenzia» (icona persone) | Colloca il prodotto e il lettore nel sistema | **HTML/CSS o SVG inline**: 3 `div` pill in grid 2 righe, connettori con `border-left/top` e `border-radius` sull'angolo; puntatore `position:absolute` con animazione `translateY` ±4 px. Nel sito è raster (`albero-apsales.webp`) — noi lo facciamo in HTML per avere testo selezionabile |
| D3 | **Stack di acquisizione** | T25 | 4 card 290×185 raggio 24 bordo 1 px, sfalsate come D1, connettori tratteggiati a gomito, freccia finale; dentro ogni card un'icona a colori 120 px che **sfuma verso il basso** (maschera lineare) e sotto l'etichetta 22 px | «DM su Instagram» (logo IG) → «Loom» (logo Loom) → «Call» (icona FaceTime) → «Chiusura progetto» (badge blu ✓) → ↓ | Il metodo di vendita come catena riconoscibile dai loghi | Stessa struttura di D1; icona con `mask-image: linear-gradient(black 40%, transparent 95%)`. Loghi come SVG ufficiali. Nel sito è raster (`stack-clienti.webp`) |
| D4 | **Cartella con linguette** | T20 | 5 livelli sovrapposti: 4 fogli grigi `oklch(0.87)` raggio 12 bordo 1 px, ognuno più stretto e più alto del precedente (sfalsamento ~60 px verticale, ~20 px laterale), con una linguetta trapezoidale nera (`clip-path: polygon(0 100%, 12.27px 6.9px, 13.47px 4.1px, 15.47px 1.9px, 18.07px 0.5px, 21.07px 0px, calc(100% - 21.07px) 0px, … 100% 100%)`) alternata sx/dx; davanti la cartella 832×360 con logo | Linguette: «01 Intro», «02 Landing pages», «03 Trovare clienti», «04 Domande comuni» (numero grigio chiaro `oklch(0.87)`, testo bianco); logo FO nero al centro | Indice del programma come oggetto fisico; le linguette sono `button` | **Puro CSS**: `position:absolute` con `z-index` crescente, `clip-path` sulla linguetta (o `border-radius: 8px 8px 0 0` + pseudo-elementi per i raccordi), `button` con `aria-expanded`. Ricostruibile in 60 righe |
| D5 | **Griglia 01-04** | T18 | 4 colonne uguali (208 px) alte ~600 px separate da filetti verticali 1 px; in ogni colonna: numero `DM Mono` 49 px in alto (y +150), filetto orizzontale, H3 22 px, p 17 px grigio; colonna attiva con `linear-gradient(180deg, azzurro chiaro, azzurro saturo)` e testo bianco | «01 Impara a fare landing page» / «02 Impara a trovare clienti» / «03 Chiudi un caso studio» / «04 Fatti pagare» + sottotitoli | I 4 passi del corso; l'evidenza che cicla dice «sono tutti importanti» | **CSS Grid** 4 colonne, `border-left` 1 px, classe `.attiva` con gradiente; ciclo con `@keyframes` su `background-position` o con JS `setInterval` 4 s. Un solo gradiente in tutta la pagina |
| D6 | **Card gemelle 1./2.** | T17 | 2 card ~255×345 raggio 12, bordo 1 px (nero / azzurro), numero 81 px w800 in alto (nero / azzurro), due paragrafi giustificati | «1.» + «Quelli che scrivono un prompt…» / «2.» + «Quelli che sanno cosa deve esserci dentro…» | Il confronto tipo A / tipo B con un solo segnale (bordo) | **HTML**: `ol` con 2 `li` in flex, `counter` o span, `.giusta { border-color: var(--accento) }`. Testo allineato a sinistra (non giustificato) |
| D7 | **Mappa topografica** | T2 (dentro `carta-metodo`) | Rettangolo verticale in negativo: curve di livello, fiume, un abitato di quadratini al centro, 4 nodi quadrati con icona (X, edificio, cerchio, bandierina) collegati da tratteggi curvi con 3 mirini intermedi, bussola in alto a destra | Nessun testo | «Metodo chiaro» = ci si arriva seguendo una mappa | **Immagine** (illustrazione generata/ritoccata); non ha senso rifarla in SVG. Per noi: una mappa vera del territorio del cliente in negativo + nodi SVG sovrapposti |
| D8 | **Tessera SEC** | T6 | Card metallica 894×624 con riflesso diagonale, sigillo in alto a sinistra e in filigrana a destra, citazione in monospaziato maiuscolo tra virgolette grandi, banda nera in basso con «SEC» + riga descrittiva | Citazione di 4 righe + «SEC — ENTE GOVERNATIVA AMERICANA…» | Fonte terza come oggetto | **HTML/CSS** riproducibile: `div` con `background: linear-gradient(135deg, #d9d9d9, #f4f4f4 45%, #bdbdbd)`, `border-radius: 12px`, testo `DM Mono`, sigillo come SVG con `opacity .25`. Vantaggio: testo selezionabile e traducibile |
| D9 | **Tessera-badge del corso** | T19 | Rettangolo verticale 840×1721: laccio tessuto grigio, moschettone metallico, foro, tessera azzurra con illustrazione in negativo, pannello chiaro con 4 righe ✓, logo, QR | «Prima pagina online in 24h / Inizi a cercare clienti dopo 8:30 ore di corso / Inizia carriera come Funnel Operator / Garanzia consulenza con Andrei» | L'offerta come oggetto da indossare | **Ibrido**: laccio+moschettone come immagine PNG con alfa (una volta sola, riusabile), tessera in HTML (div azzurro con `background-image` in negativo + lista ✓ + logo + QR SVG). Così le promesse restano testo |
| D10 | **Timer** | T19 | 4 gruppi affiancati: cifra 63 px w800 + etichetta `DM Mono` 14 px letter-spacing sotto; nessuna cornice | «28 giorni · 13 ore · 08 minuti · 14 secondi» + riga «Il prezzo sale tra» (visivamente nascosta o piccola) | Urgenza | **HTML** con `<time>` e JS; `font-variant-numeric: tabular-nums` per evitare il salto delle cifre |
| D11 | **Lista a filetti con glifo** | T15 | 3 righe alte ~105 px, `border-top/bottom` 1 px, glifo 60 px a sinistra (x 425), testo 22 px a destra (x 500) | «Non erano richiesti dal mercato.» (teschio) / «Li stavano già offrendo…» (spade) / «Non c'era margine.» (lapide) | Tre motivi con peso emotivo | **HTML** `ul` con `li` flex, glifi come SVG o WebP 2× |
| D12 | **Checklist in tabella** | T25 | 1 colonna 365 px, bordo 1 px nero raggio 8, 5 righe alte ~60 px separate da filetti, ✓ 16 px + testo 16 px | 5 voci «Che messaggi mandare … E molto altro…» | Cosa ricevi | **HTML** `ul` con `border` e `li + li { border-top }` |
| D13 | **Zig-zag garanzia** | T3 | 2 righe: [testo sx 37 px / foto dx 350×267] poi [foto sx 351×267 / testo dx allineato a destra] | «E se non trovi clienti…» / «…puoi fissare una consulenza…» | Problema → soluzione | **CSS Grid** 2 colonne, `direction` alternata per riga |
| D14 | **Prima/dopo** | T8 | 2 colonne: titolo barrato grigio / titolo verde; foto bn / foto colore con bordo verde | «Fare siti» / «Fare landing pages.» | Giudizio senza parole | **HTML** con `filter: grayscale(1)` sulla foto «prima» (così basta una foto a colori) e `border: 1px solid var(--verde)` sulla «dopo» |
| D15 | **Sovrapposizione diagonale** | T26 | 2 frame 458×251 raggio 12; il secondo spostato di +270 px in x e +90 px in y, z-index superiore | Frame call / lavagna | Materiale grezzo | **CSS** `position:relative` + `translate` sul secondo; su mobile `flex-direction: column` |
| D16 | **Rail (marquee)** | T4, T11, T17, T21 | Traccia orizzontale con contenuto duplicato ×2, `animation: fo-rail 45s|70s linear infinite`, `translateX(-50%)` a fine ciclo; T11 ha due tracce in direzioni opposte | numeri / screenshot / loghi / call | Movimento, abbondanza | **CSS** `@keyframes rail { to { transform: translateX(-50%) } }`, `prefers-reduced-motion` per fermarlo, `mask-image` ai bordi per la dissolvenza |
| D17 | **Accordion «?»** | T21, T29 | Riga 80 px: cerchio 40 px bordo 1 px con «?», domanda 22 px grigio, «+» a destra, `border-bottom` 1 px; eyebrow `DM Mono` azzurro chiaro + filetto marcato sopra ogni gruppo | 4 + 14 domande | Dubbi / FAQ | **HTML** `details/summary` o `button[aria-expanded]` + `@keyframes accordion-down` sull'altezza; il «+» ruota a «×» |

---

# E. QUALITÀ GRAFICA — il giudizio

## Cosa lo rende «bello e professionale» (15 punti misurabili)

1. **Una sola colonna di progetto: 832 px.** Tutto ciò che è largo (insegna, VSL, FAQ, footer, rail delle FAQ, cartella) misura esattamente 832 px, da x 304 a x 1136. Le colonne di lettura strette (T13 ≈670, T14 ≈535, T25 ≈620) stanno dentro e sono centrate. Zero elementi «quasi allineati».
2. **Due sfondi soli, alternati.** 23 sezioni su `oklch(0.178)` e 23 su `oklch(0.946)`: l'alternanza scuro/chiaro è quasi regolare (1-2 scure, 3-4 chiare, 5-6 scure, 7 chiara…) e non c'è mai bianco puro né nero puro nelle sezioni: il contrasto resta alto senza abbagliare.
3. **Un accento, due segnali.** L'azzurro (`oklch(0.656 0.134 235.9)`) è l'unico colore di marca e compare in 12 nodi di testo/sfondo su 386 blocchi; il rosso in 2, il verde in 2. In una pagina di 32.807 px il colore è un evento.
4. **Un solo gradiente** (la colonna 01 di T18) più quello del logomark. Nessuna ombra colorata: 14 dichiarazioni `box-shadow` tutte trasparenti. Il rilievo è dato da bordi 1 px e da bordi luminosi dentro le foto.
5. **Raggi in scala.** 8 px bottoni (52 usi), 12 px foto/card (8+), 24 px nodi dei diagrammi (7), pill per gli albero/sticky (21). Nessun raggio fuori scala.
6. **Tipografia a 4 famiglie con ruoli fissi.** Inter Tight per corpo e titoli medi, Plus Jakarta Sans per titoli grandi e etichette, DM Mono **solo per metadati** (timer, eyebrow, numeri 01-04), Curseyt **solo nell'hero**. La scala 17-22-29-37-49-63 è quasi una progressione ×1,3.
7. **Coppia «cifra grande + didascalia piccola»** identica nel rail numeri (37/17), nel timer (63/14 mono), nella griglia (49 mono/22/17), nelle card gemelle (81/17). Chi ha letto la prima la riconosce nelle altre.
8. **Un solo sistema iconografico per gli schemi**: card con bordo 1 px + connettori tratteggiati a gomito (T7 e T25). Il lettore impara la grammatica una volta.
9. **Regia delle immagini per tipo di sfondo**: illustrazioni bn solo su nero; foto soprattutto su chiaro; le foto su nero hanno luce blu che si fonde col fondo. Nessuna foto a colori caldi su fondo nero.
10. **Nitidezza: 40 raster su 60 serviti a 2×** (±5 %), con rapporti conservati. Una sola immagine ritagliata dal CSS. Il peso totale delle immagini è 2,5 MB per una pagina di 30 sezioni con 68 file: mediana 30 KB.
11. **Un componente, molti usi.** L'accordion è identico in T21 e T29; il rail è lo stesso in 5 punti; la card a scala in 2; il badge di verifica in 5 punti; il barrato+colore in 2. Su 30 sezioni si contano circa 17 componenti distinti (sezione D).
12. **Gerarchia in ogni sezione: un solo H2, al massimo due H3.** 56 heading in 30 sezioni. Nessuna sezione con due titoli concorrenti.
13. **Densità controllata dal contenuto, non dal template.** Sezioni di solo testo (T14, T27) alte 600-775 px dopo sezioni con 6 foto (T13, 1.924 px): il ritmo alterna pieni e vuoti. Densità media 7,6 parole per 100 px di altezza (2.560 parole / 32.807 px).
14. **Metafore fisiche costruite, non scaricate**: tessera SEC, badge al collo, cartella con linguette, carte da gioco, insegna. Ogni oggetto ha un solo scopo e appare una volta sola.
15. **Mobile con la stessa grammatica**: gli sfalsamenti diventano colonne, i rail restano rail, la cartella resta cartella, e un solo CTA sticky (pill azzurra, blur, angolo basso destro) sostituisce tutte le ripetizioni di bottone. La pagina mobile è solo 12 % più alta della desktop (36.630 vs 32.807 px).

## Dove è debole

- **Testo giustificato** in T6, T10, T13, T14, T17 (dentro card da 255 px), T25, T28: fiumi visibili, peggio su mobile. Le sezioni migliori per leggibilità (T27, T15) sono quelle allineate a sinistra.
- **Immagini a 1×**: `sito-apple`, `community-iphone`, `consulenza-1/2/3`, `motivo-*`, `carta-serpenti` — su retina si vedono morbide (accettabile per la texture, non per il telefono e le call).
- **`lovable.webp`**: alt che descrive Lovable, file che mostra Notion, unica immagine ritagliata dal CSS. Errore di produzione.
- **Bottone primario incoerente**: testo nero su azzurro in T19, bianco su azzurro in T28 e nello sticky.
- **Portfolio di 3 pezzi** ripetuti 12 volte: la ripetizione si vede dopo 5 secondi.
- **Testo dentro immagini raster** (insegna, albero, stack, tessera): non selezionabile, non traducibile, non indicizzato oltre l'alt.
- **Nessun accordion aperto** di default: 18 domande chiuse sono una parete.
- **Colonna attiva animata** in T18: mentre si legge la colonna 02, il gradiente si sposta.
- **Logo PNG a 7,5×** nell'header e reso nero con `brightness(0)` in T20: bastava un SVG (che esiste: `funops-logomark-scuro.svg`).
- **Il video non dichiara la durata**, né in T9 né in T21.

---

# F. CONFRONTO VISIVO CON IL NOSTRO SITO (agency-empire-landing.vercel.app)

Dati nostri: 0 fotografie, 5 famiglie di gradiente, 186 dimensioni tipografiche, 880 blocchi. Dati suoi: 15 fotografie + 3 foto-oggetto, 1 gradiente (+ logomark), 40 combinazioni tipografiche, 386 blocchi.

| Elemento | Lui (funneloperator.it) | Noi (agency-empire-landing) | Cosa ci manca, elemento per elemento |
|---|---|---|---|
| Fotografia del fondatore | 15 foto vere (scrivania, ristorante, set video, cucina, palestra, riunione, finestra) + 2 fotogrammi video | 0 fotografie | **Un volto.** Almeno 3 foto: al lavoro, in call, di profilo; luce coerente col nostro argento/arancione |
| Illustrazione originale | 10 xilografie di una sola mano | Nessuna illustrazione, solo gradienti | **Un registro illustrativo unico** (per noi: incisione argento su nero con grana, coerente con le Brand Guidelines CCM) |
| Oggetti-prova | tessera SEC, badge al collo, carte, insegna, cartella | Nessuno | **Almeno un oggetto**: la «tessera del cliente» con le 3 promesse dello sprint e un QR alla pagina /prenota/ |
| Schema di processo | scala a 7 step + stack a 4 con connettori tratteggiati | Liste e card senza connettori | **Uno schema a scala** per il nostro sprint 2-4 settimane, in HTML |
| Organigramma «Tu sei qui» | albero a 3 nodi | Nessuno | **Albero Digital Empire** (Agency / Info products / SaaS) con «Tu sei qui» sulla foglia Agency |
| Prima/dopo | 2 ritratti bn/colore | Nessuno | **Prima/dopo di una landing cliente** (screenshot desaturato vs a colori con bordo arancione) |
| Screenshot di siti terzi | Apple, Amazon, Notion | Nessuno | **3 screenshot dei siti dei nostri clienti / casi** a 2× |
| Screenshot di call | 5 (volti pixelati) | Nessuno | **2 frame di call CRO** pixelati + 1 lavagna |
| Documenti reali | 2 template con evidenziatore | Nessuno | **Il nostro report CRO** o il brief, fotografato come foglio tagliato dal filetto |
| Portfolio in rail | 2 rail controcorrente | Griglia statica o assente | **Rail dei casi** (3-6 screenshot verticali) |
| Numeri con icona | rail 4 metriche (4000+, 1500+, 2020, 4.8/5) | Numeri in card con gradiente | **Rail di 4 metriche** con icone SVG monocrome, senza card |
| Timer / urgenza | timer + prezzo futuro | Assente | (non applicabile al pay-on-performance; al massimo «posti sprint del mese: N») |
| Accordion | 18 righe, 1 componente | Presente ma con stile proprio | Riuso di **un solo** componente accordion per FAQ e obiezioni |
| Gradiente | 1 (colonna attiva) | 5 famiglie | Ridurre no (vincolo solo aggiunte): ma **ogni aggiunta nuova senza gradiente**, così le nuove sezioni abbassano la media |
| Tipografia | 40 combinazioni, 4 famiglie a ruolo fisso | 186 dimensioni | **Le aggiunte usano 6 corpi soli** (17-22-29-37-49-63) e un mono solo per metadati |
| Texture | grana su 3 sezioni, carta su 1 | grana presente (legge di Max) | Va bene: **la grana è già nostra**; aggiungere la variante «carta» chiara per una sezione chiara |
| Sfondi | alternanza scuro/chiaro | quasi solo scuro | **Almeno 3 sezioni chiare** (`oklch(0.946)`) tra le aggiunte, con foto |
| Mobile | CTA sticky pill unico | CTA ripetuti in pagina | **Un CTA sticky** «Prenota» in basso a destra su mobile (aggiunta, non modifica) |
| Video | 2 poster stesso set + play | Nessun video | **Un poster video** (anche 60 s) nello stesso set delle foto |
| Marchio nel titolo | «fatte da APsales» inline | Nessuno | **Logo inline in un H2** («Sprint firmati Digital Empire») |
| Footer | 4 righe: logo, P.IVA, legale, © | Presente | Aggiungere **P.IVA e indirizzo** in chiaro se mancano |
| Densità | 386 blocchi / 2.560 parole / 30 sezioni | 880 blocchi | Le aggiunte a **≤ 15 blocchi per sezione** |

---

# G. LE 20 LEZIONI DELL'ATLANTE (ognuna = un'aggiunta al nostro sito, mai una modifica)

1. **Aggiungere un'illustrazione-manifesto** sopra il primo blocco esistente: incisione argento su nero con grana, una frase di 3-5 parole, nessun bottone (da T1).
2. **Aggiungere tre «carte-promessa»** (card 295×370, raggio 12, bordo 1 px, illustrazione + titolo 29 px + riga grigia + badge ✓) per le tre garanzie dello sprint (da T2).
3. **Aggiungere una sezione «garanzia in due quadri»** a zig-zag: foto del problema (schermo «Conversioni ferme?») + foto di noi al lavoro (da T3).
4. **Aggiungere un rail di 4 metriche** con icone SVG monocrome e numero 37 px / didascalia 17 px, senza card (da T4).
5. **Aggiungere un'insegna del servizio**: la parola «SPRINT CRO.» in maiuscolo grigio su un'immagine simbolica, dentro una cornice 1 px (da T5).
6. **Aggiungere una «tessera-fonte»** per ogni dato di terzi che citiamo (Baymard, Nielsen…): card metallica in HTML/CSS con citazione in mono e sigillo in filigrana (da T6/D8).
7. **Aggiungere lo schema a scala dello sprint** (7 card sfalsate, connettori tratteggiati, icone che sbordano, traguardo in colore) in puro HTML (da T7/D1).
8. **Aggiungere un prima/dopo** di una landing cliente: la stessa pagina in `grayscale(1)` e a colori con bordo arancione, titolo barrato/colorato sopra (da T8/D14).
9. **Aggiungere un poster video** del fondatore nello stesso set delle foto, con play sobrio e durata dichiarata (migliorando T9).
10. **Aggiungere l'albero «Tu sei qui»** di Digital Empire in HTML (3 pillole, connettori con raccordo, puntatore animato) (da T10/D2).
11. **Aggiungere due rail controcorrente** con gli screenshot verticali dei nostri casi (da T11).
12. **Aggiungere una sezione biografica a colonna stretta** (≈670 px) con foto piccole a coppie, anche vecchie e sgranate, e avatar rotondo con firma (da T13).
13. **Aggiungere una lista a filetti con glifi** per «i 3 motivi per cui i siti non convertono», glifi nello stesso registro dell'illustrazione-manifesto (da T15).
14. **Aggiungere una sezione poster**: una sola immagine forte duplicata e ruotata, con una fascia di testo chiara che la attraversa (da T16).
15. **Aggiungere le card gemelle «1. / 2.»** con numero a 81 px e bordo colorato solo sulla card giusta, per «chi compra traffico vs chi ottimizza» (da T17/D6).
16. **Aggiungere la griglia numerata 01-04** in mono con **una** colonna colorata (fissa, non animata) per le 4 fasi dello sprint (da T18/D5).
17. **Aggiungere la «tessera del cliente»** in HTML (laccio come PNG, tessera come div con le promesse in lista ✓ e QR a /prenota/) accanto al prezzo/condizioni (da T19/D9).
18. **Aggiungere la cartella con linguette** in clip-path come indice dei deliverable dello sprint (4 linguette = 4 consegne) (da T20/D4).
19. **Aggiungere due frame di call sovrapposti in diagonale** con volti pixelati + una lavagna, come prova delle discovery call (da T26/D15).
20. **Aggiungere un CTA sticky mobile** «Prenota» (pill, blur, basso destra) e un footer legale a 4 righe con P.IVA e indirizzo; e mettere nel gate della Fabbrica Siti tre controlli imparati dai suoi difetti: **alt = contenuto**, **rapporto originale = rapporto reso**, **niente testo giustificato sotto 600 px** (da T23, T30, sezione E).

---

*Atlante compilato guardando 30 tavole, 24 schermate mobile (01-05, 08-09, 11, 13-15, 19, 21, 23, 25-30, 32, 35-38, 41, 44), 38 file raster in `media/` e gli 8 SVG a sorgente; numeri da `scheda.json`, `design-tokens.json`, `media-inventario.md`, `copy-integrale.md`.*
