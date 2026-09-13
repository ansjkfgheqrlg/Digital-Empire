---
Type: SYNTHESIS
Status: Active
Tags: #fabbrica-siti #competitor #andrei-pascu #atlante #design-system #sito-agency #dossier-39
Created: 2026-09-13
Last updated: 2026-09-13
---

# 39A — ATLANTE DEI TRE SITI — armageddon · claude-speedrun 2 · funneloperator

**Il repertorio degli elementi visivi professionali degli ultimi tre siti di Andrei Pascu, con le misure, per copiarli nel nostro sito agency (`agency-empire-landing`, vende una chiamata da 30′ per sistemi AI).**

Fonti: i report `11-armageddon*.md`, `12-claude-speedrun-ATLANTE.md` + `-STACK-E-TOKEN.md`, `66-funneloperator-ATLANTE-VISIVO.md` + `-STILE.md` (§1-§3) + `-COSTRUZIONE.md` (§2.4, §3, §4); i tre `design-tokens.json` (`type_scale`, `radii`, `ctas`, `media`, `page_width`, `page_height`, `weights`, `fonts`, `headings`); gli screenshot desktop guardati uno per uno (Armageddon 01-06; Speedrun 01, 02, 03, 06, 07, 09, 10, 12, 15-22, 25-27, 31, 32 + `sezioni/19`, `31`, `32`; Funnel Operator 01-05, 08, 09, 12, 13, 15, 18, 20-27, 31-33, 35, 37). Ogni misura porta il suo file.

> **Come leggere le coordinate.** Le schermate desktop sono fette di 1440×900: `desktop-NN.png` copre `y = (NN−1)·900 → NN·900` della pagina intera. Le `y` citate sono quelle della pagina (da `design-tokens.json`/`scheda.json`) o, dove dico «≈», lette sulla fetta.
> Tutto ciò che segue vale per il nostro sito come **aggiunta**, mai come modifica del live (ADR-030, `gate_solo_aggiunte.py`).

---

## §1 — LA SCALA DEI TRE

| Misura | **Armageddon** (lancio, 5.103 px) | **Claude Speedrun 2** (33.756 px) | **Funnel Operator** (32.807 px) | Nostro sito agency (per confronto) |
|---|---|---|---|---|
| **Corpo (px / interlinea / peso)** | 16,5 / 27,4 (1,66) / 400 — 31 nodi, il più usato (`type_scale`) | **16 / 25,6 (1,6) / 400** — 91 nodi; secondo corpo 19,2 / 26,9 / 500 (42) | **17 / 27,2 (1,6) / 400** — 28 nodi; varianti «lettera» 17 / 1,17-1,22 giustificate (49 nodi) | 16 / 1,6 su gran parte, ma **186 dimensioni distinte** (66-ATLANTE §F) |
| **Titolo di sezione (h2/h3)** | 72 px Curseyt w400 («Domande», `desktop-05` y≈3.930); 152 px («Sei pronto?») | **33,18 / 41,5 / 600** — 27 nodi, lo standard; 27,65 w600 (13); 47,78 w700 (4) per i grandi | **37 / 44,4 / 700** — 18 nodi (`.titolo-sezione`); 49 w700 (5+8); 63 w800 (4) per i tre titoli-manifesto | h2 a **48-52 px** su desktop (`text-[36px] md:text-[52px]`, `md:text-5xl`) — ~1,4× i suoi |
| **h1** | 191,6 / 194,4 px Curseyt w400 (due strati) | 47,78 w700 (hero testuale, `desktop-01` a destra); display decorativo fuori dagli heading: 80 w900 ×3, 104 w900 ×2 («GET. SHIT. DONE.», «5X») | **220 / 290 px Curseyt w400** («Un giorno / morirai», `desktop-01`) | — |
| **Rapporto h2 standard / corpo** | 4,4 (pagina di lancio: il gotico grida, il corpo è solo FAQ) | **2,07** | **2,18** | ~3,0-3,25 |
| **Colonna di contenuto** | `--u = min(100cqw, 960px)`: x 235 → 1.195 (ritratto 960, `media`); FAQ `max-width 760` (x 334 → 1.095 in `desktop-05`) | **800 px**: x 320 → 1.120 (righe lezioni, card ×3, FAQ in `desktop-15/21/22`, `sezioni/32`); media tipici 600 (×5), 670 (video), 448 (CTA impilate) | **832 px** = 12 col × 40 + 11 canali × 32: x 304 → 1.136 (insegna, VSL, FAQ, footer, `media`); colonne di lettura strette 535 / 620 / 670 dentro | `max-w-5xl` (1.024) e larghezze miste per sezione |
| **Padding verticale sezione** | `.offer`: top `--u×0,13` = 125 px, bottom 72 px; «Domande» → primo filetto ≈ 60 px (`desktop-05`) | **96 px** (`py-24`) su quasi tutte le firme; 80 (`py-20`), 64 (`py-16`) rare; footer 48. Titolo a ≈ 95 px dal bordo sezione (`desktop-15`: bordo y=105, titolo y=200) | **96 px a 1440** (`py-vendita = clamp(56px,15vw,96px)`), 48 px titolo→contenuto (`mt-blocchi`); titolo a ≈ 60-100 px dal bordo (`desktop-08`: «Come funziona» y≈40 dopo il bordo, `desktop-21`: titolo 120 px sotto il bordo) | variabile |
| **Sezioni per 10.000 px** | 5 / 5.103 → **9,8** | 34 / 33.756 → **10,1** (32 firme distinte) | 30 / 32.807 → **9,1** (26 distinte) | 880 blocchi: densità di blocco ~2,3× la sua |
| **CTA primarie (fondo pieno)** | **1** (COMPRA, bianco 288×71) + 1 outline | **7** arancioni di acquisto (Iscriviti 448×60, RUBA WORKFLOW 226×52, Entra adesso 164×50, «ok, voglio…» 497×59, Iscriviti adesso 177×60 e 177×56) + sticky pill 151×44 | **3** azzurre (Iscriviti adesso 147×48, Sono pronto 154×48, sticky 151×48) + 1 secondaria grigia 202×48 | CTA ripetute per sezione |
| **Testo bottone** | 25 px w800 | 14-19 px w600/700 | **14 px w500** — più piccolo del corpo (17) | — |
| **Raggi** | 15,19 (bottoni, = `--btn×0,0528`), 6,375 (celle), 8 (modale) — **3 valori** | pill 9999 (65), **12 (56)**, 16 (30) — 3 valori | **8 (52)**, 5 (36, miniature rail), pill (21), 12 (8, foto), 24 (7, nodi degli schemi) | misti |
| **Pesi** | 700 (34) · 400 (30) · 800 (7) — il grassetto = «cliccabile» | 400 (144) · 600 (98) · 700 (81) · 500 (43) · 900 (15) · 800 (13) | 400 (120) · 500 (72) · 700 (57) · 600 (29) · 800 (9) | — |
| **Famiglie** | Plus Jakarta Sans (59) + Curseyt (12) | **Onest (366)** + ui-serif/Georgia (28, i corsivi) — *è il nostro Onest* | Inter Tight (172) + Plus Jakarta Sans (102) + DM Mono (10, solo metadati) + Curseyt (3, solo hero) | Onest + Instrument Serif + mono |
| **Accento** | `#bc0807`: 5 nodi di testo + 4 celle | `#fb4604` (= il nostro, `16 97% 50%`): 9 fondi CTA + parole singole nei titoli; 1 sola sezione a fondo pieno | azzurro `#1d9cd7`: **16 testi : 9 decorazioni : 3 bottoni** su 386 blocchi | 5 famiglie di gradiente |
| **Ombre / gradienti** | 0 ombre box; 2 `drop-shadow` sui biglietti; 0 gradienti di colore (solo maschere nere) | glow arancione `0 0 40px rgba(251,70,4,.3)` sui CTA finali; ombre Tailwind standard | **14 `box-shadow` tutte trasparenti** nel DOM; 1 gradiente (colonna 01-04) + logomark; 7 ombre a mano nel CSS, tutte nere e spostate in basso a destra | gradienti su card e testo |

### Perché sembrano centrati e non ingranditi — le 5 misure che lo decidono

1. **Una colonna sola e stretta: 800 / 832 / 960 px**, con la stessa `x` di partenza in ogni sezione (320, 304, 235). Tutto ciò che è largo misura esattamente la colonna; il testo lungo scende a 535-670 px (FO) o 600 (CS). Niente elementi «quasi allineati»: l'occhio impara un bordo e lo ritrova per 33.000 px.
2. **Il corpo è 16-17 px con interlinea 1,6 e il titolo di sezione è solo 2,1-2,2× il corpo** (33/16, 37/17). I giganti (80-290 px) sono 2-3 per pagina e stanno in blackletter o in contorno: sono eventi, non la regola. I nostri h2 a 48-52 px con corpo 16 sono al rapporto 3,0-3,25: è questo, non il contenuto, a farli sembrare «ingranditi».
3. **Un solo passo verticale: 96 px** sopra e sotto ogni sezione (`py-24` / `py-vendita`), 48 px fra titolo e contenuto. Con ~1.000 px per sezione (9-10 sezioni ogni 10.000 px) il ritmo è metronomico; la variazione la fa l'alternanza scuro/chiaro (FO: 15 e 15, mai più di due uguali di fila salvo la parte «prova»), non il padding.
4. **Bottoni piccoli e rari**: testo 14 px (FO) o 14-18 (CS), altezza 44-60 px, larghezza 147-288 px, **3-7 primari su 33.000 px**. Su FO il bottone è più piccolo del corpo. Il colore d'azione compare in <5 % dei nodi (FO 12/386; Armageddon 9 nodi su 71). Da noi il CTA si ripete per sezione e il colore di marca è anche superficie.
5. **Un raggio per famiglia e zero rilievo**: 8 px bottoni, 12 foto/card, 24 nodi degli schemi (FO); 12/16/pill (CS); 15/6 (Arm). Bordi 1 px al posto delle ombre (14 `box-shadow` trasparenti su FO), 0-1 gradienti per pagina. Il «lusso» è nella coerenza dei raggi e nel 2× esatto delle immagini (40 su 60 raster), non nell'effetto.
6. Corollario: i tre siti hanno **12-17 combinazioni tipografiche di spina dorsale** (FO: 14·17·22·29·37·49·63·81, passo ≈1,3). Noi ne abbiamo 186. Ogni aggiunta nostra deve usare solo la scala di §2 «canone».
7. Corollario: **il colore accento va su una parola per titolo** (FO: «funnel operator», «ho scelto», «3 siti», «cambiare vita»), non su una superficie. Quando lo usano come fondo intero (CS «Hai COMPETITOR», 431 px) è una volta sola in 33.756 px.
8. Corollario: il **peso** non significa importanza ma funzione: Armageddon mette 800 solo su ciò che si clicca, FO mette 500 sui bottoni e 700 sui titoli, CS usa 900 solo nei display decorativi. Un solo peso per ruolo.

---

## §2 — ATLANTE

Ordine per famiglia. Per ogni voce: **NOME · SITO · SCREENSHOT · COSA SI VEDE · PERCHÉ È PROFESSIONALE · COME LO RIFAREMMO NEL NOSTRO CANONE** (ink `#0a0a0a` fondo / `#1c1c1c` superficie, carta `#faf6ee` per le sezioni chiare, arancione `#fb4604` solo accento <10 %, Onest per corpo e titoli, Instrument Serif corsivo per la parola-voce, mono per i metadati, grana fissa + locale su tutto; colonna 832 px dentro 880 con 24 px di margine; corpo 17/1,6; h2 37/1,2 w700; h3 22-29 w600; mono 14 px +0,03em; bottone 48 px, 14-16 px, raggio 8; raggi 8/12/24; filetti 1 px `rgba(255,255,255,.12)` su ink e `rgba(10,10,10,.14)` su carta; padding sezione 96 px).

### A. Schemi a blocchi, mappe, percorsi

**E01 · Scala a 7 gradini con connettori tratteggiati** · Funnel Operator · `66-funneloperator-it/desktop-08.png` (y 6.300-7.200) + `desktop-09.png` (7.200-8.100); h2 «Come funziona» a y=6.284.
*Cosa si vede.* Sezione carta (`#eeeeee`). Sette card 290×140, raggio 24, bordo 1 px nero, sfondo = sfondo sezione, sfalsate: dispari a x≈480, pari a x≈670, passo verticale ≈176 px. Dentro: icona nera piena che **sborda oltre il bordo sinistro** (tagliata da `overflow:hidden`), «Step N» 29 px w600, riga grigia 17 px. Connettori: div con `border: 1px dashed #000` a L rovesciata (escono dal lato destro, scendono, rientrano da sinistra); freccia finale CSS (border-trick) verso «Carriera avviata» 49 px verde + badge dentellato, poi riga 22 px.
*Perché è professionale.* È un diagramma di flusso in HTML: card vere, connettori di CSS, zero immagini di flusso; il glifo che buca la card è uniforme su 7/7 e la posizione di «Step N» è identica, quindi si legge in un colpo d'occhio. Sotto `lg` i connettori spariscono e resta una colonna (66-COSTRUZIONE §4 n.5).
*Come lo rifaremmo.* `ol` in grid a 2 colonne alternate (`nth-child(odd/even)`), card 290×140 raggio 24 bordo 1 px `rgba(10,10,10,.6)` su carta `#faf6ee` con grana; icone SVG monocrome ink, `position:absolute; left:-20px`; connettori `::after` con `border-right/bottom: 1px dashed`; «Passo N» 29 px Onest 600, riga 17 px grigio `#5c5c5c`; traguardo 49 px in Instrument Serif corsivo **arancione** (l'unico colore della sezione) + badge. Già previsto nel sorgente come `Scala`: queste sono le misure.

**E02 · Stack a 4 con le icone reali dei tool** · Funnel Operator · `desktop-31.png` (y 27.000-27.900); sezione «Troverai veramente clienti?» y=26.421.
*Cosa si vede.* Stessa grammatica di E01 (card 290×185, raggio 24, bordo 1 px, sfalsate, connettori tratteggiati) ma dentro ogni card un'icona a colori di 120 px (Instagram, Loom, FaceTime, badge blu) che **sfuma verso il basso** ed etichetta 22-24 px; freccia finale. Nel sito è un'immagine (`stack-clienti.webp` 1152×1832 → 576×916, 2×).
*Perché è professionale.* Il lettore riconosce «un processo» prima di leggere perché ha già imparato la forma in E01; i loghi veri dicono «strumenti reali» in mezzo secondo; l'unico punto di colore vivo della pagina chiara.
*Come lo rifaremmo.* Stessa struttura di E01 in HTML; loghi SVG ufficiali con `mask-image: linear-gradient(black 40%, transparent 95%)`; etichetta 22 px w600. Per noi: i 4 anelli del sistema (canale d'ingresso → qualifica → chiamata → consegna) con i loghi dei tool che usiamo davvero.

**E03 · Albero «Tu sei qui»** · Funnel Operator · `desktop-12.png` (y 9.900-10.800; albero a y≈10.450-10.770).
*Cosa si vede.* Tre pillole grigio chiaro bordo 1 px nero raggio pieno: «AP Sales» in alto (larga ≈370, alta ≈110), linea nera 2 px che scende e si biforca ad angolo retto con raccordo, «Formazione» e «Agenzia» sotto (≈395×110), icone lineari; a sinistra della foglia attiva un pallino azzurro con alone + chevron ∨ e «Tu sei **qui**» (17 px, «qui» azzurro). Sopra, la frase ponte 37 px w500 «Questa pagina è parte del mio ramo…». È raster (`albero-apsales.webp` 1586×656 → 793×328).
*Perché è professionale.* Un organigramma che diventa mappa: colloca prodotto e lettore nel sistema con tre nodi e un puntatore; pillole con lo stesso bordo 1 px e lo stesso grigio delle card di E01.
*Come lo rifaremmo.* In HTML (testo selezionabile): 3 `div` pill in grid 2 righe, connettori `border-left/top` 2 px ink con `border-radius` sull'angolo, pillole `#faf6ee` bordo 1 px ink raggio pieno, testo 29 px w600; puntatore arancione `#fb4604` con alone `0 0 0 6px rgba(251,70,4,.18)` e `translateY ±4px` animato, «Tu sei qui» con «qui» in Instrument Serif corsivo arancione. Per noi: Digital Empire → Agency / Info products / SaaS, puntatore su Agency. Già previsto come `Mappa`.

**E04 · Asse «BROKIE — TU — COMPETITOR / sei qui»** · Claude Speedrun · `12-claude-speedrun-v2/sezioni/19-perch-quei-249-sono-ancora-sulla-t.png` (sezione y 14.960-16.381; diagramma nell'ultimo quarto) — in `desktop-18/19.png` è coperto dal banner cookie.
*Cosa si vede.* Su nero, una freccia orizzontale bianca a sinistra («BROKIE / indietro», 20 px w700 + 16 px) e arancione a destra («COMPETITOR / avanti»), un cerchio 80 px bordo 2 px arancione con «TU» al centro, due tacche verticali sopra e sotto, una freccia ▲ e «sei qui» 16 px sotto; chiusura «Devi solo imparare come si fa.» 16 px w700 arancione.
*Perché è professionale.* L'unica visualizzazione posizionale della pagina: mette il lettore al centro di un asse reversibile; due colori, un cerchio, zero immagini.
*Come lo rifaremmo.* SVG inline 600×220: asse 2 px, punta sinistra ink su carta (o bianca su ink), punta destra arancione, cerchio 80 px con «TU» 20 px w700, etichette 20 px w700 + 16 px, «sei qui» in Instrument Serif corsivo. Sotto il problema: «fai tutto a mano ← TU → chi ha un sistema».

**E05 · Timeline verticale numerata** · Claude Speedrun · `desktop-10.png` (y 8.100-9.000).
*Cosa si vede.* Sezione carta. Una linea verticale 2 px arancione tenue a x≈400; su di essa cerchi 32 px arancioni pieni con il numero bianco 14 px w700; a destra titolo 23 px w600 e corpo 16 px grigio `#39393c`, elenco puntato; distanza fra voci ≈130 px; chiusura «ERO CONFUSO QUANTO TE… *Poi gli ai lord…*» 27,65 px con seconda metà in corsivo (ui-serif).
*Perché è professionale.* Tre motivi come stazioni su una linea, un solo colore; il corsivo serif nella chiusura cambia voce senza cambiare sezione.
*Come lo rifaremmo.* `ol` con `border-left: 2px solid rgba(251,70,4,.35)`, pallini 32 px `#fb4604` con cifra 14 px w700 bianca, h3 22 px w600, corpo 17 px `#5c5c5c`, gap 48 px; chiusura in Instrument Serif corsivo 29 px.

### B. Tabelle e griglie numerate

**E06 · Griglia 01-04 in mono con colonna accesa** · Funnel Operator · `desktop-22.png` (y 18.900-19.800; griglia da y≈19.250) + h3 a y=19.481.
*Cosa si vede.* Quattro colonne uguali (208 px) separate da filetti verticali 1 px `#2c2c2c`, alte ≈600; in ogni colonna numero `DM Mono` 49 px in alto (≈150 px sotto il bordo), filetto orizzontale, h3 22 px w700, paragrafo 17 px grigio. Le colonne attive (nella cattura 02 e 03) hanno un `linear-gradient(180deg, #88C9F4, #1E9CD7, #0075BE, #005B97)` — la scala dell'accento messa in fila — e testo bianco; l'evidenza cicla ogni 1,5 s (66-COSTRUZIONE §4 n.7) e si ferma su reduced-motion.
*Perché è professionale.* Coppia «cifra grande mono / etichetta» identica a timer e FAQ; l'unico gradiente della pagina è costruito con i quattro valori dei token, non inventato; le colonne sono tabella, non card.
*Come lo rifaremmo.* CSS Grid 4 × 208, `border-left` 1 px, numeri mono 49 px, h3 22 px w700, p 17 px; **una sola colonna accesa e fissa** con `linear-gradient(180deg, #fb4604 0%, #c83600 100%)` + grana locale, testo `#faf6ee`. Per noi: le 4 fasi della collaborazione o le 4 cose che escono dalla chiamata. Se su carta: filetti `rgba(10,10,10,.14)`.

**E07 · Card gemelle «1. / 2.» con numero a 81 px** · Funnel Operator · `desktop-20.png` (y 17.100-18.000; card da y≈17.750) + `desktop-21.png` (coda).
*Cosa si vede.* Due card ≈255×345, raggio 15, la sinistra bordo 1 px nero con «1.» 81 px w800 nero (`tracking -0.15em`), la destra **bordo 1 px azzurro** con «2.» azzurro; sotto i numeri due capoversi 17 px giustificati (fiumi visibili). Chiude «L'azienda non ti paga per generare la pagina.» 22 px w700 centrato + 2 righe 17 px.
*Perché è professionale.* Il confronto tipo A / tipo B con **un solo segnale** (il colore del bordo e del numero); il numero è il titolo.
*Come lo rifaremmo.* `ol` a 2 colonne, card 255×345 raggio 12 su `#1c1c1c` (o carta) bordo 1 px; numero 81 px Onest 800 `letter-spacing -0.06em`; `.giusta { border-color:#fb4604 }` e numero arancione; testo 17 px **allineato a sinistra**, mai giustificato sotto 600 px. Già previsto come `DueTipi`: queste le misure.

**E08 · Tris di card con numero in filigrana** · Claude Speedrun · `desktop-15.png` (y 12.600-13.500; card y≈13.100-13.245).
*Cosa si vede.* Tre card 256×144 su nero, sfondo `#1a1a1a`, bordo 1 px `rgba(255,255,255,.08)`, raggio 16; titolo 19,2 px w600, riga 14 px grigio; nell'angolo destro un numero 80 px w900 in `#fb4604` a opacità ~0,12, tagliato dal bordo. Sopra: h3 33 px con «Oggi stesso.» arancione, corpo 16 px, elenco numerato.
*Perché è professionale.* Il numero in filigrana ordina senza pesare; una sola riga di risultato per card («10 minuti invece che 2 giorni»); griglia a 3 dentro gli 800 px con gap 16.
*Come lo rifaremmo.* Grid 3 × (256×144, gap 16), superficie `#1c1c1c` con grana, bordo 1 px `rgba(255,255,255,.08)`, raggio 12; cifra 80 px w800 `rgba(251,70,4,.14)` in `position:absolute; right:-6px; bottom:-18px; overflow:hidden`; titolo 19 px w600, riga 14 px `#8a8a8a`. Per noi: «tre cose che il sistema fa da solo».

**E09 · Lista lezioni: righe con numero romano, etichetta verticale e data** · Claude Speedrun · `desktop-21.png` (y 18.000-18.900) + `desktop-22.png` (18.900-19.800).
*Cosa si vede.* Su fondo `#0a0a0a` con griglia sottile, righe 800×80 raggio 12, sfondo `#1a1a1a` bordo 1 px; a sinistra una linguetta verde 36 px con «NEW» ruotato di 90°, numero romano 33 px serif arancione, titolo 19 px w600, data 12 px w700 grigio a destra; la prima riga ha sfondo arancione al 15 % e bordo arancione. Sopra: box riassunto 800×120 bordo 1 px, pill verde «✦ NUOVE LEZIONI» 14 px w700, eyebrow «LEZIONI DI CLAUDE SPEEDRUN 2» 20 px w700 arancione `tracking .1em`. Sotto: «ALTRE LEZIONI INCLUSE» / «LE BASI» 23 px w700 grigio.
*Perché è professionale.* Ogni riga ha 4 slot fissi (linguetta, numero, titolo, data) e li ripete 10 volte; il romano dà registro editoriale; una sola riga accesa.
*Come lo rifaremmo.* Righe 832×80 raggio 8 su `#1c1c1c` bordo 1 px; numero in mono 22 px arancione (non romano: il mono è il nostro «schedario»), titolo 19 px w600, metadato 12 px mono grigio a destra; linguetta verticale 36 px solo per lo stato («NUOVO», «IN CORSO») in `#faf6ee` su ink. Per noi: l'elenco dei sistemi consegnati, con la data.

### C. Lapidi, titoli giganti, fasce

**E10 · Titolo in due strati (pieno dietro il volto, contorno davanti)** · Armageddon · `11-armageddon/desktop-01.png` (y 0-900).
*Cosa si vede.* Hero quadrato `--u` = 960 px: ritratto b/n 1024² con grana, splatter rossi, «Armageddon» 191,6 px Curseyt `#bc0807` a top `--u×0,0622` con **z-index 1 sotto il ritratto** e una copia identica `color:transparent; -webkit-text-stroke: max(1px, --u×0.0013)` a z-index 3 (`aria-hidden`); «is here» 194,4 px a top 0,621. Parallax a 4 velocità (splat 0,2 · man 0,155 · word 0,09 · word2 0,04) e atterraggio in 3 tempi (1700/1400/1200 ms, `--ease-land`).
*Perché è professionale.* La parola è piena sul nero e diventa incisione dove attraversa i capelli: costo un `<span>`; le animazioni stanno sui figli `<i class="in">` per non litigare col parallax.
*Come lo rifaremmo.* Non in Curseyt: Instrument Serif corsivo a `clamp(72px, 12vw, 160px)` in `#faf6ee` pieno dietro la foto del fondatore (b/n con grana) e stroke 1,5 px `#faf6ee` davanti; una parola sola in arancione. Solo per una pagina di lancio o per la `Firma`, mai sull'hero live.

**E11 · Lapide blackletter con illustrazione che tocca il titolo** · Funnel Operator · `desktop-01.png` (y 0-900) + `desktop-02.png` (900-1.800).
*Cosa si vede.* «Un giorno» 220 px bianco, «morirai» 290 px `#bd0000`, punto bianco; l'aureola dell'illustrazione (xilografia bianca su nero, 832×618, 2× esatto) tocca la base di «morirai»; sotto la frase 49 px w500 su due righe. Nessun bottone, nessuna eyebrow, nessuna freccia. `mix-blend-difference` sull'h1, `mix-blend-screen` sull'immagine (66-COSTRUZIONE §4 n.1).
*Perché è professionale.* Titolo e figura sono impaginati come una copertina di disco; contrasto 21:1; una sola idea nella prima schermata.
*Come lo rifaremmo.* Hero-manifesto **aggiunto sopra il primo blocco** (non al posto): titolo 3-5 parole Onest 800 a `clamp(56px, 9vw, 120px)` con l'ultima parola in Instrument Serif corsivo arancione, incisione argento su ink 832×618 in `mix-blend-mode: screen` con grana, frase 37 px w500 sotto. Zero bottoni: il bottone arriva dopo.

**E12 · Fascia a colore pieno con titolo-manifesto** · Claude Speedrun · `desktop-03.png` (y 1.800-2.700; fascia y≈2.125-2.250) e `desktop-07.png` (y 5.400-6.300; casella «ASCOLTA BENE.» y≈5.925).
*Cosa si vede.* Una banda `#fb4604` a tutta larghezza alta ≈125 px con «GET. SHIT. DONE.» 104 px w900 nero (testo decorativo, fuori dagli heading); più avanti la stessa idea ridotta a **casella** 390×64 arancione con «ASCOLTA BENE.» 56 px w700 bianco (questo è un H1). Sopra la banda, «5X» in contorno bianco 104 px con il volto b/n dietro e la barra sfocata sugli occhi.
*Perché è professionale.* Un blocco-lampo di 125-430 px fra due sezioni lunghe: cambia il ritmo senza aggiungere contenuto; il colore pieno è usato **una volta** come sezione intera e una come casella.
*Come lo rifaremmo.* Al massimo **una** fascia in tutta la pagina: 120 px, `#fb4604` con grana locale, testo ink 800 a `clamp(48px, 7vw, 96px)`, `letter-spacing -.02em`, tre parole con punto. In alternativa la versione «casella» 64 px per un h2 di svolta. Già presente in sorgente come `FasciaManifesto`: misure sopra.

**E13 · Insegna in cornice 1 px** · Funnel Operator · `desktop-05.png` (y 3.600-4.500; cornice y≈3.900-4.160).
*Cosa si vede.* Tre frasi centrate 36 px w500 (haiku «Le aziende le vogliono / Non le trovano / E son disposte a pagare tanto»), poi un pannello 832×259 con **bordo bianco 1 px** (l'unico bordo bianco pieno del sito) che contiene la xilografia del cavaliere e la scritta «LANDING PAGES.» in grigio medio dentro l'immagine; sotto «Ti spiego tutto ↓» 22 px.
*Perché è professionale.* Il nome del servizio ha una targa; la cornice trasforma un'immagine in un oggetto; la scritta grigia resta leggibile senza urlare.
*Come lo rifaremmo.* Pannello 832×259 bordo 1 px `#faf6ee` su ink, incisione argento con grana dentro, la parola («SISTEMI.» o il nome del servizio) in HTML sopra l'immagine: Onest 800 `clamp(48px, 8vw, 96px)` `rgba(250,246,238,.72)` con `mix-blend-mode: screen` — non raster, così è selezionabile e traducibile. Sopra: tre righe 36 px w500.

### D. Rail e nastri

**E14 · Rail delle metriche con icona monocroma** · Funnel Operator · `desktop-04.png` (y 2.700-3.600; rail y≈3.280-3.370).
*Cosa si vede.* Fascia carta alta 273 px; quattro coppie icona SVG `#111` (72-80 px) + numero 37 px w700 + didascalia 17 px («1500+ / studenti formati», «2020 / apertura dello store», «4.8/5 / score Trustpilot» col link sottolineato); `fo-rail 45s linear`, contenuto duplicato con `aria-hidden`, `mask-image` ai bordi, pausa al hover, spento in reduced-motion (66-COSTRUZIONE §4 n.3). Nessuna card.
*Perché è professionale.* Numeri nella stessa scala 37/17 dei sottotitoli, icone in un solo peso e un solo colore; la prova sociale diventa movimento, non griglia.
*Come lo rifaremmo.* `@keyframes rail { to { transform: translateX(-50%) } }` 45 s, traccia con `mask-image: linear-gradient(to right, transparent, black 6%, black 94%, transparent)`, item = SVG ink 72 px + numero 37 px w700 + riga 17 px `#5c5c5c`, gap 96 px, su carta `#faf6ee` con grana; `prefers-reduced-motion` ferma il nastro. I numeri li mette Emperator da FATTI.md. Già previsto come `RailFatti`.

**E15 · Doppio rail controcorrente di portfolio** · Funnel Operator · `desktop-13.png` (y 10.800-11.700).
*Cosa si vede.* H2 49 px w500 «Esempi di pagine fatte da» + il marchio APsales azzurro **inline nel titolo** (SVG 206×41); due nastri di screenshot verticali 209×293 raggio 5, uno sopra l'altro, sfalsati di mezzo modulo, `fo-rail 70s` in direzioni opposte (`animation-direction: reverse` sul secondo). Tre soggetti ripetuti 12 volte.
*Perché è professionale.* Tre file (56 KB) danno abbondanza; il marchio dentro l'h2 è firma d'autore.
*Come lo rifaremmo.* Due tracce 293 px di altezza, miniature 209×293 raggio 5 bordo 1 px `rgba(255,255,255,.1)`, 70 s e 70 s reverse, mask ai bordi; **almeno 6 soggetti** per non far vedere la ripetizione. Titolo 49 px w500 con il logotipo Digital Empire inline (SVG, altezza 0,8em). Già previsto come `RailSistemi`.

**E16 · Rail dei loghi degli strumenti** · Funnel Operator · `desktop-20.png` (y 17.100-18.000; loghi a y≈17.390).
*Cosa si vede.* Sette loghi a colori (Vercel, ChatGPT, GitHub, Lovable, Krea, Claude, Gemini) a 40 px, passo ≈100 px, su carta; `fo-rail 70s`. È l'unico punto della pagina chiara in cui entrano colori terzi, contenuti a 40 px.
*Perché è professionale.* Attualità e strumenti reali senza una parola; dimensione minima, quindi la palette non si rompe.
*Come lo rifaremmo.* Loghi 40 px in `filter: grayscale(1) contrast(1.1)` con `opacity .8` su ink (o a colori su carta come lui), gap 96 px, rail 70 s. Sotto il meccanismo: i tool dentro i nostri sistemi.

### E. Tessere, biglietti, oggetti-prodotto

**E17 · Tessera-badge al collo (l'offerta come oggetto)** · Funnel Operator · `desktop-23.png` (y 19.800-20.700).
*Cosa si vede.* Sezione `#offerta` con texture di graffi via CSS; «Avvia una carriera come» 37 px w500, «FUNNEL **OPERATOR**» 50 px w800 (seconda parola azzurra; il clamp è **decrescente**: 63 px su mobile, 50 su desktop perché convive con la tessera); una tessera 295×568 appesa a laccio grigio con moschettone d'acciaio, foro, illustrazione in negativo azzurro, pannello chiaro con 4 righe ✓, logo e QR — tutto dentro il file (`tessera.webp` 840×1721, 185 KB, servita a 2,9×).
*Perché è professionale.* Il corso diventa un badge da indossare con le promesse stampate; fotorealismo del moschettone + illustrazione coerente col resto.
*Come lo rifaremmo.* **Ibrido**: laccio + moschettone come PNG con alfa (una volta), tessera in HTML 295×568 raggio 12 su `#1c1c1c` con incisione argento in `background-image`, pannello `#faf6ee` con 4 righe ✓ 14 px, logotipo, QR SVG a `/prenota/`. Testo selezionabile. Titolo 50 px w800 con la seconda parola in Instrument Serif corsivo arancione. Già previsto come `Tessera`.

**E18 · Due biglietti sul fuoco che si accavallano** · Armageddon · `desktop-03.png` (y 1.800-2.700; biglietti da y≈2.290) + `desktop-04.png` (2.700-3.600).
*Cosa si vede.* Su fiamme mascherate in nero (`#000 0 → trasparente --u×0,43 → --u×0,69 → #000 --u×1,12`), due biglietti stampati 317×605 e 328×543, il dietro ruotato 7,16°, due `drop-shadow` in frazioni di `--u`; arrivano separati (`is-spread is-locked`), dopo 2.500 ms si accavallano (820 ms `--ease-heavy`), dopo altri 900 ms rispondono al mouse (front `scale 1.05`, back `rotate 8.9deg` con l'immagine a `scale .95`). Il biglietto copre di `--u×0,0116` il bordo del bottone COMPRA sotto.
*Perché è professionale.* Il micro-teatro ha un lucchetto (`is-locked`) che impedisce all'hover di partire a metà volo; il riquadro che riceve l'hover è l'ingombro dei biglietti, non la sezione.
*Come lo rifaremmo.* Un solo «biglietto della chiamata» 317×605 raggio 4, carta `#faf6ee` con grana e bordo dentellato, testo mono; ingresso con `IntersectionObserver` threshold .3 → dopo 800 ms `translate/rotate` 820 ms `cubic-bezier(.65,0,.25,1)`; classe `is-locked` finché l'animazione non è finita; ombre `0 12px 30px rgba(0,0,0,.55)` + `0 32px 78px rgba(0,0,0,.45)`. Il fuoco no: grana + vignetta.

**E19 · Biglietto arancione con QR e la sua copia in controluce** · Claude Speedrun · `desktop-20.png` (y 17.100-18.000) + `desktop-03.png` (y≈2.460-2.660).
*Cosa si vede.* Su nero con onde scure sfocate, un biglietto 300×560 arancione pieno, foto del templare, logo, «2 / claude speedrun» serif, etichetta nera «WORKFLOW UPDATE» mono `tracking .3em`, linea tratteggiata di strappo, «BIGLIETTO» + QR; dietro, una copia bianca ruotata. Lo stesso biglietto riappare più avanti come sfondo in filigrana e all'inizio come immagine orizzontale con codice a barre.
*Perché è professionale.* Un solo oggetto-simbolo, mostrato una volta intero e richiamato due volte in controluce: rinforza il ricordo senza nuove parole (12-ATLANTE, DELTA «CANONE»).
*Come lo rifaremmo.* Il biglietto di E18 usato tre volte: intero nell'offerta, a `opacity .08` in `position:absolute` dietro il confronto ORA/CON (E24), in miniatura 120 px nel footer. Arancione **solo** sulla banda del biglietto, non su tutto.

**E20 · Tessera-fonte metallica (l'avviso SEC)** · Funnel Operator · atlante T6 (`sezioni/06-la-realt-dei-fatti.png`; `media` y=4.765, 447×312).
*Cosa si vede.* Card argento con riflesso diagonale, sigillo in alto a sinistra e in filigrana a destra, citazione in monospaziato maiuscolo tra virgolette grandi, banda nera in basso con «SEC» + riga descrittiva; angoli e ombra dentro il file (894×624, 2×).
*Perché è professionale.* Prende un link a un PDF governativo e lo rende un reperto; la fonte terza diventa oggetto.
*Come lo rifaremmo.* HTML: `div` 447×312 raggio 12 `background: linear-gradient(135deg, #d9d9d9, #f4f4f4 45%, #bdbdbd)` + grana, citazione mono 14 px maiuscolo `letter-spacing .04em`, sigillo SVG `opacity .25`, banda ink 44 px con la sigla della fonte. Per ogni dato di terzi che citiamo (Baymard, Nielsen…). Testo selezionabile.

### F. Confronti prima/dopo

**E21 · Frase barrata + frase vera** · Funnel Operator · `desktop-20.png` (y≈17.190: «~~L'AI ti ruba il lavoro.~~» rosso `#bd0000` 37 px, sotto «Ruberai il lavoro a chi non sa usare l'AI.» 49 px w700 nero) e `desktop-09.png` (y≈8.030: «~~Fare siti~~» grigio / «Fare landing pages.» verde 37 px).
*Cosa si vede.* Un `<s>` semantico con `line-through` e un `span` colorato, sulla stessa riga o uno sopra l'altro; due colori, zero componenti.
*Perché è professionale.* Sostituzione di una credenza in un gesto tipografico; il rosso e il verde compaiono in 2 punti soli della pagina, quindi si notano.
*Come lo rifaremmo.* `<s class="text-[#8a8a8a] font-medium">` 37 px + `<span>` 49 px w700 con la parola chiave in Instrument Serif corsivo arancione; `text-decoration-thickness: 2px`. Apertura del problema.

**E22 · Prima/dopo con la stessa persona, b/n vs colore** · Funnel Operator · `desktop-09.png` (coda, y≈8.030-8.100) + atlante T8.
*Cosa si vede.* Due ritratti 298×362 raggio 12: sinistra in bianco e nero (taglio disordinato, auricolare), destra a colori con **bordo verde 1 px** dentro il file; sopra ciascuno il titolo barrato/verde di E21; sotto, testo centrato 29/17/22 px e freccia ↓.
*Perché è professionale.* Il registro fotografico è il giudizio: nessuna parola di spiegazione.
*Come lo rifaremmo.* Una sola immagine a colori: «prima» con `filter: grayscale(1) contrast(1.05)` + grana, «dopo» con `border: 1px solid #fb4604` e `box-shadow: 0 0 0 1px rgba(251,70,4,.25)`; 298×362 raggio 12; titoli di E21 sopra. Per noi: la stessa landing/inbox del cliente prima e dopo il sistema. Già previsto come `PrimaDopo`.

**E23 · Zig-zag garanzia in due quadri (foto + riga)** · Funnel Operator · `desktop-03.png` (y≈3.100-3.300) + `desktop-04.png` (y 2.700-3.100).
*Cosa si vede.* Sezione carta: riga 1 testo a sinistra 37 px w500 su 4 righe + foto a destra 350×267 («ZERO CLIENTI?» sullo schermo, luce blu); riga 2 foto a sinistra 351×267 (Andrei alla scrivania, stessa sessione) + testo a destra allineato a destra. Una sola frase spezzata dai puntini. Foto 2× esatte, raggio 12, bordo 1 px scuro + ombra `2px 2px 17.3px rgba(0,0,0,.32)` (luce da sinistra-alto).
*Perché è professionale.* La garanzia è fotografata: problema e soluzione in due quadri della stessa luce; lo zig-zag dà movimento senza ornamenti.
*Come lo rifaremmo.* Grid 2 colonne (`calc(100%*351/832)` per la foto), riga 2 con `direction: rtl` ma testo **allineato a sinistra** (il suo a destra pesa); 37 px w500 con grassetti 700; foto 350×267 raggio 12 bordo 1 px `#676767` + ombra spostata; grana sulle foto. Sotto la garanzia.

**E24 · Confronto ORA / CON su asse verticale** · Claude Speedrun · `desktop-26.png` (y≈23.100-23.400) + `desktop-27.png` (y 23.400-24.300).
*Cosa si vede.* Su nero, una linea verticale 3 px a x≈423 che passa da grigio ad arancione; in alto pallino grigio pieno + «ORA» 80 px w900 grigio con due righe (titolo 27 px w700 grigio + sottoriga grigia); in basso pallino arancione con alone + «CON» 80 px w900 arancione + logo «claude» inline, due righe (titolo 27 px w700 bianco + sottoriga arancione). Sullo sfondo il biglietto in filigrana.
*Perché è professionale.* Sei parole in tutto, il colore dell'asse racconta il passaggio; la voce «prima» è spenta anche nel peso del grigio.
*Come lo rifaremmo.* `border-left: 3px` con `linear-gradient(#5c5c5c, #fb4604)` via `border-image`, pallini 20 px, «ORA» / «CON» 80 px w800 (grigio `#5c5c5c` / arancione), righe 27 px w700 + 19 px; il biglietto E18 a `opacity .08` dietro. Sotto il meccanismo.

### G. Sezioni con foto + riga, biografia, prova

**E25 · Biografia a colonna stretta: avatar + firma + foto a coppie** · Funnel Operator · `desktop-15.png` (y 12.600-13.500) + atlante T13.
*Cosa si vede.* Sezione carta alta 1.924 px, colonna ≈670 (x 387→1.053); h2 tra virgolette 49 px w600 centrato; avatar 124 px rotondo + «Andre :)» 37 px w500; sottotitolo 29 px; paragrafi 17 px; tre coppie di foto 313-321×172 (la terza 235) raggio 12 bordo 1 px chiaro, intercalate ai paragrafi; foto vecchie volutamente sgranate; volti pixelati nella riunione.
*Perché è professionale.* È una pagina di diario: colonna da lettura, foto piccole che scandiscono il tempo; la bassa qualità delle foto vecchie è prova, non difetto.
*Come lo rifaremmo.* Colonna 670 centrata dentro gli 832, avatar 124 px con bordo 1 px `rgba(10,10,10,.14)`, firma 37 px in Instrument Serif corsivo, h3 29 px w500, corpo 17 px allineato a sinistra, coppie 321×172 raggio 12 bordo 1 px + grana. Già previsto come `Stanza`/`WhoGuides`: queste le misure.

**E26 · Screenshot di call sovrapposti in diagonale, volti pixelati** · Funnel Operator · `desktop-33.png` (y 28.800-29.700; frame y≈28.940-29.260).
*Cosa si vede.* Due frame 458×251 raggio 12: la call (uomo pixelato, mano sul mento) a sinistra e in alto, la lavagna digitale con appunti a mano (frecce, «red flags ✗ / green flags ✓», webcam pixelata) a destra, spostata di +270 px in x e +90 in y, z-index superiore. Sopra, h2 37 px w600 e paragrafo 17 px con «per davvero» in grassetto.
*Perché è professionale.* «Materiale grezzo, tanto» con due soli file; i pixel grossi (non blur) sono una scelta coerente in tutta la pagina.
*Come lo rifaremmo.* `position:relative`, secondo frame `translate(270px, 90px)`, entrambi 458×251 raggio 12 bordo 1 px `rgba(10,10,10,.2)` + ombra `3px 4px 15px rgba(0,0,0,.31)`; pixelatura fatta a monte (mosaico 24 px). Su mobile in colonna. Sotto la prova: due discovery call vere + una lavagna. Già previsto come `ProveVere`.

**E27 · Fogli veri tagliati dal filetto (asset)** · Funnel Operator · `desktop-27.png` (y 23.400-24.300; righe da y≈23.770).
*Cosa si vede.* H2 63 px w600 «Asset pronti per te», sottotitolo 22 px, riga 17 px grigio; quattro righe alte ≈166 px separate da filetti 1 px `#2c2c2c` in zig-zag: titolo 29 px w600 + paragrafo grigio da un lato, un documento bianco 245×347 dall'altro, **tagliato dal filetto della riga successiva** (`overflow:hidden`), con evidenziazioni giallo-verdi.
*Perché è professionale.* Il documento parziale incuriosisce più del documento intero; le righe a filetti fanno «archivio».
*Come lo rifaremmo.* Righe 832×166 `border-bottom 1px`, grid 2 colonne alternate, foglio 245×347 in `overflow:hidden` con `object-position: top`, grana; titolo 29 px w600, p 17 px `#8a8a8a`. Per noi: il brief, il report, la mappa del sistema fotografati come fogli. Già previsto come `DietroLeQuinte`/`Cartella`.

**E28 · Muro di recensioni con voto aggregato** · Claude Speedrun · `desktop-25.png` (y 21.600-22.500; da y≈21.990) + `desktop-26.png`.
*Cosa si vede.* Sezione carta: h3 33 px, «★★★★★ 4,9/5» 19 px con stelle arancioni 16 px, «su 14 recensioni verificate» 13 px grigio; griglia 3 colonne (card 256 px, gap 16, bianco, bordo 1 px `rgba(0,0,0,.06)`, raggio 12, padding 20), altezze diverse (masonry); citazione 16 px, autore 13 px w600 + badge verde «Recensione verificata»; **una card a 4 stelle**.
*Perché è professionale.* Massa (muro), non selezione; la 4 stelle in mezzo alle 5 è credibilità misurata.
*Come lo rifaremmo.* Grid 3 × 256 gap 16 su carta, card `#fff` bordo 1 px `rgba(10,10,10,.08)` raggio 12 + grana leggerissima, stelle SVG arancioni 16 px, citazione 17 px, firma 13 px w600 + spunta ink; il voto aggregato lo mette Emperator da FATTI.md. Sotto la prova.

**E29 · Grafico a barre orizzontali + riquadro di calcolo** · Claude Speedrun · `desktop-32.png` (y 27.900-28.800) + `desktop-31.png`.
*Cosa si vede.* Su nero, asse verticale 2 px grigio; etichette ruotate «GIORNO 1 / GIORNO 2» mono `tracking .2em` 14 px; barra grigia 272×137 raggio 8 e barra arancione 455×137; sopra ogni barra «6 articoli in 2 ore» / «10 articoli in 2 ore» 23 px w700 (grigio / arancione). Sotto, riquadro 496 px bordo 1 px `#333`: «SENZA CLAUDE» mono 19 px `tracking .15em`, «6 / 2 = 3 articoli/ora» 40 px w800 mono, freccia ↓. Prima: tre righe fotografiche di «falsa produttività» in una tabella bianca 600 px con bordi neri 2 px (`desktop-31`).
*Perché è professionale.* La persuasione passa per l'aritmetica con numeri piccoli e memorizzabili; il grafico è due `div` e un bordo.
*Come lo rifaremmo.* Due barre raggio 8 (`#5c5c5c` / `#fb4604` con grana locale), etichette mono 14 px ruotate, valori 23 px w700; riquadro 496 px bordo 1 px `rgba(255,255,255,.14)` con formula in mono 40 px w800. Sotto il meccanismo: ore a mano vs ore col sistema (numeri da FATTI.md).

**E30 · Tre carte-promessa a ventaglio con badge verificato** · Funnel Operator · `desktop-02.png` (y 900-1.800; da y≈1.400) + `desktop-03.png` (y 1.800-2.700).
*Cosa si vede.* Su nero con texture di roccia: logomark 58×54 in gradiente, h2 63 px w500 con due parole azzurre w700; tre carte 295×370 (raggio 13, bordo 1 px `#676767`, ombra `7px 11px 39.5px rgba(0,0,0,.2)`), la centrale più alta (y 1.627) e avanti, le laterali a y 1.755-1.769 ruotate ±3°; illustrazione (raggio interno 12 = 13 − 1) nei 2/3 superiori, titolo 29 px w700 + badge dentellato azzurro + riga grigia 17 px.
*Perché è professionale.* Tre promesse = tre oggetti dello stesso registro; profondità senza gradienti; raggio interno = raggio esterno − bordo (curve concentriche).
*Come lo rifaremmo.* Tre card 295×370 raggio 12 (interno 11) su `#1c1c1c` bordo 1 px `#676767`, ombra `7px 11px 40px rgba(0,0,0,.35)`, centrale `translateY(-140px)`, laterali `rotate(±3deg)`; incisione argento con grana nei 2/3 alti, titolo 29 px w700 + badge SVG arancione, riga 17 px `#8a8a8a`. Sopra l'offerta: le tre promesse della chiamata.

### H. Accordion, FAQ, obiezioni

**E31 · Accordion «?» con eyebrow in mono e gruppi** · Funnel Operator · `desktop-35.png` (y 30.600-31.500) + `desktop-37.png` (coda) + `desktop-26.png` (la stessa riga sotto la VSL 2, y≈23.000-23.350).
*Cosa si vede.* H2 «FAQ» 37 px w700 a sinistra; eyebrow `DM Mono` 14 px azzurro chiaro maiuscolo («FUNNEL OPERATOR», «PAGAMENTO») + filetto 1 px più marcato; righe 832×80 (102 se a capo): cerchio 40 px bordo 1 px `#2c2c2c` con «?» 16 px, domanda 22 px w500 `#8a8a8a`, «+» 16 px a destra che ruota a «×», `border-bottom` 1 px; la riga in hover si accende (testo bianco, cerchio azzurro, sottolineatura che cresce da sinistra `bg-[length:0%_1px] → 100%`). Radix con `forceMount` (contenuto sempre nel DOM). Stesso componente in 21 e 29.
*Perché è professionale.* Un solo componente per dubbi e FAQ; il mono solo per i metadati; i filetti a 1,35:1 si vedono e non pesano.
*Come lo rifaremmo.* `details/summary` nativo (o `button[aria-expanded]`): riga 832×80, cerchio 40 px bordo 1 px `rgba(255,255,255,.14)` con «?» mono, domanda 22 px w500 `#8a8a8a` → `#faf6ee` in hover/aperta, «+» → «×» con `rotate(45deg)` 120 ms; eyebrow mono 14 px arancione `letter-spacing .06em` + filetto 1 px `rgba(255,255,255,.3)`; **prima riga aperta di default** (lui ne lascia 18 chiuse). Gruppi: «PRIMA DELLA CHIAMATA» / «DOPO» / «SOLDI E CONTRATTO». Già previsto come `FaqContratto`.

**E32 · FAQ a filetti con «+» rosso, allineate a sinistra in un footer centrato** · Armageddon · `desktop-05.png` (y 3.600-4.500; prima riga y≈3.995) + `desktop-06.png` (4.500-5.103).
*Cosa si vede.* «Domande» 72 px Curseyt rosso centrato; blocco `max-width 760` **allineato a sinistra**; filetti 1 px `rgba(255,255,255,.15)` sopra ogni riga e sotto l'ultima; domanda 19 px w700 bianca, padding 15-22 px, `+` rosso 1,35em a destra che diventa `–`; risposte 16,5 px lh 1,66 `rgba(255,255,255,.76)` `max-width 64ch`; `<details>` nativo, marcatore Safari spento due volte.
*Perché è professionale.* Undici righe, un colore, un filetto; le FAQ si leggono, quindi hanno un margine fisso mentre il resto della pagina è centrato («because these are read»).
*Come lo rifaremmo.* Variante «leggera» di E31 senza cerchio: domanda 19 px w700, `+` arancione, filetti `rgba(255,255,255,.12)`, risposte 17 px lh 1,66 `rgba(250,246,238,.76)` `max-width 64ch`; `::-webkit-details-marker{display:none}` + `list-style:none`.

**E33 · Obiezioni tra virgolette + risposta, sola tipografia** · Funnel Operator · `desktop-33.png` (y≈29.450-29.700) + atlante T27.
*Cosa si vede.* Su nero, tre blocchi: h3 tra virgolette basse «Se questo metodo funziona così bene, perché lo insegni?» 37 px w700 su due righe, risposta 17 px lh 27 grigio chiaro; nessuna immagine, nessun filetto, allineato a sinistra su 832 px. È la sezione più leggibile della pagina perché non giustifica.
*Perché è professionale.* Le virgolette fanno «voce del lettore», il tondo «voce di Andrei»; ritmo regolare ×3; zero componenti.
*Come lo rifaremmo.* h3 37 px w700 con virgolette « » e l'ultima parola in Instrument Serif corsivo; risposta 17 px `rgba(250,246,238,.82)` `max-width 64ch`; gap 64 px fra blocchi. Tra garanzia e FAQ. Già previsto come `Objections`: allineare a queste misure.

**E34 · Citazione-obiezione con avatar e box-link bordato** · Claude Speedrun · `desktop-19.png` (y 16.200-17.100).
*Cosa si vede.* Avatar 112 px rotondo con bordo 2 px arancione sfumato; h3 tra virgolette 33 px w700 su due righe; corpo 16 px; un box-link 336×80 bordo 1 px arancione al 40 %, raggio 12, sfondo arancione al 6 %, icona 📖 + «Leggi la storia di Andrei Pascu» 16 px w700 + riga 14 px.
*Perché è professionale.* L'obiezione messa nelle parole del lettore, disinnescata con una battuta e un link serio; il box è l'unico elemento cliccabile della sezione.
*Come lo rifaremmo.* Avatar 112 px bordo 2 px `rgba(251,70,4,.6)`, h3 33 px w700, box-link 336×80 raggio 8 bordo 1 px `rgba(251,70,4,.4)` fondo `rgba(251,70,4,.06)` + grana, testo 16 px w700 + 14 px `#8a8a8a`. Sotto «chi guida».

### I. Bottoni, sticky, badge

**E35 · La coppia di bottoni sotto prezzo e timer** · Funnel Operator · `desktop-24.png` (y 20.700-21.600; bottoni y≈21.030) — e Armageddon `desktop-04.png` (y≈2.888 / 2.979).
*Cosa si vede.* FO: «Iscriviti adesso» 147×48 azzurro con **testo scuro** `#111` (6,1:1), «Cosa contiene il corso?» 202×48 `#1b1b1b` bordo `#2c2c2c` testo `#e9e9e9`; entrambi 14 px w500, raggio 8, padding 0 24, gap 19; hover **si schiarisce** (`#88c9f4`), active si scurisce, 120 ms, nessun transform; `focus-visible` anello 2 px offset 2. Armageddon: COMPRA 288×71 bianco su nero, testo nero 25 px w800, raggio 15,19 (= `--btn×0,0528`); COSA INCLUDE? stesso ingombro, `transparent` + bordo 3 px bianco; il rosso arriva solo in hover.
*Perché è professionale.* Il bottone è **più piccolo del corpo** (14 vs 17) e cambia solo colore; il colore di marca è tenuto in riserva (Armageddon) o usato su 3 bottoni in 32.807 px (FO); il raggio è una frazione del bottone (Armageddon).
*Come lo rifaremmo.* Primario 48 px, padding 0 24, 15 px w600, raggio 8, `#fb4604` con testo `#0a0a0a` (contrasto ~6:1, come FO) — non bianco; hover `#ff6a2e`, active `#c83600`, 120 ms `cubic-bezier(.2,0,0,1)`, niente scale; secondario `#1c1c1c` bordo 1 px `rgba(255,255,255,.14)` testo `#faf6ee`; `:focus-visible { outline: 2px solid #ff9a6e; outline-offset: 2px }`. **Un** primario per tema, mai due nella stessa schermata salvo la coppia dell'offerta.

**E36 · CTA sticky «Ottieni accesso»** · Claude Speedrun `desktop-06.png` (angolo basso destro, pill 151×44, 14 px w600, glow `rgba(251,70,4,.3) 0 0 40px`) e Funnel Operator `desktop-03…37.png` (151×48 raggio 8, `bottom: calc(24px + env(safe-area-inset-bottom))`, ombra `0 6px 28px color-mix(in oklab, var(--fo-blue) 22%, transparent)`).
*Cosa si vede.* Un bottone fisso in basso a destra da quando si supera il primo schermo; su FO sparisce quando l'offerta o il footer sono in vista e quando c'è il banner cookie (tre `IntersectionObserver`), `inert` quando nascosto, scroll a `#prezzo` con `block:center`.
*Perché è professionale.* L'azione è sempre a portata ma **non è mai ridondante**: si ritira dove c'è già un bottone.
*Come lo rifaremmo.* `position:fixed; right:24px; bottom:calc(24px + env(safe-area-inset-bottom))`, 151×48 raggio 8 `#fb4604` testo ink 14 px w600, ombra `0 6px 28px rgba(251,70,4,.22)`, `href="#prenota"`; sentinella `100svh` in cima + osservatori su `#prenota` e `footer`; `inert` + `opacity 0` quando nascosto. Su desktop e mobile. (`sticky-cta.tsx` esiste: tarare a queste regole.)

**E37 · Badge e nastri** · Claude Speedrun `desktop-01.png` (nastro diagonale verde «Versione 2: fuori ora.» in alto a sinistra, ruotato −35°, testo bianco 16 px w600), `desktop-21.png` (pill verde «✦ NUOVE LEZIONI» 14 px w700 con glow verde; linguetta verticale «NEW» 36 px), `desktop-17.png` (icone ⊗ / ✓ in cerchio 24 px per «Non ti dico… / Sì, ti sarà…»); Funnel Operator `desktop-03.png` (badge dentellato azzurro 20 px accanto ai titoli delle carte) e `desktop-09.png` (badge verde accanto a «Carriera avviata»).
*Cosa si vede.* Quattro forme: nastro diagonale (novità), pill con glow (novità), linguetta verticale (stato), badge dentellato con spunta (promessa certificata / traguardo). Sempre 14-16 px, sempre un colore solo.
*Perché è professionale.* Il badge dentellato è **lo stesso glifo** in 5 punti di FO (azzurro o verde): un simbolo, una promessa.
*Come lo rifaremmo.* Un solo badge SVG dentellato 20 px arancione (`mask-image` su `span` così il colore viene dal token, come fa lui con `spunta.svg`), pill 14 px w700 `#faf6ee` su ink bordo 1 px per gli stati, nessun nastro diagonale (troppo «offerta a tempo» per un'agenzia).

### J. Separatori e cuciture

**E38 · Cucitura fotografica fra due sezioni sullo stesso valore di opacità** · Armageddon · `desktop-01.png` (coda) → `desktop-02.png` (y 900-1.800).
*Cosa si vede.* Tre superfici — `.hero::before` (0 → 0,992 da `--u×0,78`), `.hero::after` (0,992 → 0,71 + `sky.webp`), `.stage` (0,71 → 0 → 0 → #000 + lo stesso `sky.webp`) — che si agganciano su `0.992` e `0.71`: la fotografia del cielo attraversa il confine fra due `<section>` senza una linea.
*Perché è professionale.* Sostituisce qualunque `border-top` dove c'è una fotografia; «the two halves of his one gradient meet without a step».
*Come lo rifaremmo.* Dove una foto o un'incisione passa da una sezione all'altra: stessi due valori di opacità nei tre gradienti, stessa immagine con `background-position` calcolata, grana sopra tutto. Da mettere nel canone al posto di `section-border-t` per le sezioni fotografiche.

**E39 · Filetti di sezione e filetto luminoso** · Funnel Operator (`.filo-sfumato`: `linear-gradient(90deg, #fff0, #ffffff7e 50%, #fff0)` alto 1 px fra i 3 motivi, `desktop-18.png` y≈15.580-15.890) · Claude Speedrun (`border-t` 1 px `rgba(255,255,255,.08)` fra sezioni, `desktop-10/16/17.png`) · Armageddon (`1px solid rgba(255,255,255,.12)` sopra il legale, `desktop-06.png`).
*Cosa si vede.* Tre gradi di filetto: quello che sfuma ai lati (luce), quello pieno appena visibile (1,35:1 su FO), quello del legale.
*Perché è professionale.* Il rilievo lo fanno i bordi, non le ombre; il filetto luminoso è uno solo in tutta la pagina.
*Come lo rifaremmo.* Tre token: `--filo: rgba(255,255,255,.12)` (sezioni), `--filo-luce: linear-gradient(90deg, transparent, rgba(250,246,238,.5), transparent)` (una volta per pagina), `--filo-carta: rgba(10,10,10,.14)`. Il nostro `divider-silver-orange` resta dov'è (solo aggiunte); le sezioni nuove usano questi.

**E40 · Lista a filetti con glifo inciso** · Funnel Operator · `desktop-18.png` (y 15.300-16.200; righe y≈15.580-15.890).
*Cosa si vede.* Tre righe alte ≈105 px separate da filetti, glifo 60×60 (teschio, spade, lapide: xilografia bianca su nero, serviti a 1×) a x≈425, testo 22 px w400 a x≈500; sopra e sotto paragrafi 17 px.
*Perché è professionale.* Tre motivi con peso emotivo, lo stesso registro dell'hero in piccolo; niente card.
*Come lo rifaremmo.* `ul` con `li` flex alti 105 px, `border-top/bottom` 1 px `--filo`, glifo SVG 60 px argento con grana (serviti a 2×), testo 22 px w400 `#faf6ee`. Per noi: i 3 motivi per cui i sistemi «quasi finiti» non partono.

### K. Prezzo, garanzia, timer

**E41 · Prezzo + riga futura + timer «cifra sans / etichetta mono»** · Funnel Operator · `desktop-24.png` (y 20.700-21.100).
*Cosa si vede.* «434 €» 81 px w800 (`tracking -0.04em`, `toLocaleString('it-IT') + nbsp + €`), riga 17 px grigia con «560 €» in grassetto bianco, timer: 4 cifre 63 px w800 `tabular-nums` + etichette `DM Mono` 14 px `letter-spacing .2em` minuscole («giorni ore minuti secondi»), nessuna cornice, `aria-live="off"` con etichetta `sr-only` «Il prezzo sale tra»; un solo dato (`Ip`) alimenta prezzo, riga, FAQ e JSON-LD. Armageddon (`desktop-04.png` y≈3.100): celle 85×85 `#bc0807` raggio 6,375, cifre 28,3 px w800 `tabular-nums`, etichette 12 px `letter-spacing .1em` `rgba(255,255,255,.5)`, `aria-label` riscritto ogni secondo, scadenza su un solo `data-until`.
*Perché è professionale.* Un dato solo, mai stale; `tabular-nums` tiene ferme le cifre; il timer è muto per gli screen reader ma etichettato.
*Come lo rifaremmo.* Per un'agenzia pay-on-performance il timer non serve; la **coppia tipografica sì**: cifra 63 px w800 `tabular-nums` + etichetta mono 14 px `letter-spacing .2em` `#8a8a8a`, per «posti sprint del mese» o per i numeri della prova (E14). Il prezzo/condizioni: 81 px w800 con riga 17 px sotto; il valore da un solo `data-*`, sommato a runtime come fa Armageddon (`data-price` → `[data-total]`).

**E42 · Checklist in tabella bordata** · Funnel Operator `desktop-32.png` (y 27.900-28.800; tabella 365×340 a y≈28.230) · Claude Speedrun `sezioni/31-cosa-ottieni-se-entri-adesso.png` (riquadro 512×670).
*Cosa si vede.* FO: una colonna 365 px, bordo 1 px nero, raggio 8, 5 righe alte ≈68 separate da filetti, ✓ 16 px + testo 16 px, su carta. CS: riquadro 512 px `#1a1a1a` bordo 1 px raggio 12, 11 righe alte 61 con filetti, spunta arancione in cerchio 28 px `rgba(251,70,4,.15)`, testo 16 px; sotto, il bottone con glow.
*Perché è professionale.* La forma più pulita di «lista di consegne»: un bordo, dei filetti, una spunta; l'ultima voce («Andiamo dritto al punto») è posizionamento.
*Come lo rifaremmo.* `ul` 512 px bordo 1 px `--filo` raggio 8, `li + li { border-top }`, righe 61 px, spunta SVG 16 px arancione in cerchio 28 px `rgba(251,70,4,.14)`, testo 17 px; subito sopra il bottone `/prenota`. Già previsto come `CosaOttieni`.

**E43 · Prezzo/valore calcolato dal DOM e «Risparmi» in due colori** · Armageddon · `desktop-04.png` (y≈3.280-3.380).
*Cosa si vede.* «Risparmi» 81,6 px Curseyt bianco + «€585» rosso, sottoriga 14,9 px `rgba(255,255,255,.55)` «€784 di valore, paghi €199»; i tre numeri non sono scritti: `Σ data-price` → `[data-total]`, `[data-pay]`, `[data-save]`.
*Perché è professionale.* Rimedio al difetto «otto cifre per quattro metriche»: un dato per riga, il resto a runtime.
*Come lo rifaremmo.* Stessa regola su ogni numero ripetuto del nostro sito (ore risparmiate, costo, valore): un `data-*` sorgente, gli altri derivati; visivamente 81 px w800 + parola in Instrument Serif corsivo arancione + riga 15 px `rgba(250,246,238,.55)`.

### L. Footer, legale, testata

**E44 · Footer a quattro righe** · Funnel Operator · `desktop-37.png` (y 32.400-32.807; footer da y≈32.630) — e Armageddon `desktop-06.png` (coda).
*Cosa si vede.* FO: fascia 272 px `border-t` 1 px; logo 107×32 + «Agenzia · Corsi» 14 px; ragione sociale + P.IVA + indirizzo 14 px; «Privacy · Termini · Cookie · Preferenze cookie · Assistenza» separati da punti mediani; «© 2026». Tutto a sinistra su 832 px, un corpo, un colore grigio. Armageddon: disclaimer 12 px lh 1,75 `rgba(255,255,255,.42)` `max-width 88ch` centrato, filetto, link privacy, firma con P.IVA.
*Perché è professionale.* Niente colonne, niente social, niente newsletter su una pagina di vendita; P.IVA e indirizzo in chiaro = fiducia; il legale è **più largo** (88ch) di proposito, per essere letto.
*Come lo rifaremmo.* Footer aggiunto sotto quello esistente (solo aggiunte) o come blocco `CodaLegale` già presente: 4 righe 14 px w500 `#8a8a8a` a sinistra su 832 px, logo 32 px, ragione sociale + P.IVA + indirizzo, link con «·», ©; `border-t` 1 px `--filo`. Disclaimer 12 px lh 1,75 `max-width 88ch`. **Il `mailto:` va stilizzato** (Armageddon lo lascia `#0000ee`: unico colore fuori palette).

**E45 · Testata come targa fra due filetti / testata a doppio marchio** · Armageddon `desktop-01.png` (y 0-90: filetto `linear-gradient(90deg, transparent, rgba(188,8,7,.85))` 1 px `flex:1`, occhio 36 px, «BSNS.IT» 13,9 px w800 `letter-spacing .26em` `rgba(255,255,255,.78)`, filetto specchiato; **un solo link**) · Funnel Operator `desktop-01.png` (y 0-64: logo 107×32 · filetto verticale · marchio APsales · «Accedi →» azzurro 14 px a destra; `backdrop-filter: blur(8px)`; sotto 640 px resta il solo logomark via `<picture>`).
*Perché è professionale.* Su una pagina che vende una cosa sola la navigazione è attrito: una targa, un link; il doppio marchio dice «il prodotto appartiene a un'agenzia».
*Come lo rifaremmo.* Non si tocca la testata live. Per le pagine di lancio future: filetti 1 px in gradiente verso `rgba(251,70,4,.6)`, logotipo 14 px w800 `letter-spacing .26em`, un solo link.

### M. Video e composizioni fotografiche

**E46 · Poster video con play sobrio e set ricorrente** · Funnel Operator `desktop-26.png` (y 22.500-23.400; poster 582×327 raggio 12, play 80 px cerchio bianco su nero al 45 % con `backdrop-filter`, sottotitolo bruciato) e atlante T9 (830×466); Claude Speedrun `desktop-09.png` (670×377, play rettangolare Vimeo, durata 05:57 visibile); Armageddon `desktop-02.png` («Guarda il video» 94 px bianco con ombra doppia, freccia SVG a mano `stroke-width 13` con `drop-shadow`, player 733×412 raggio 15, `dnt=1`, in pagina senza copertina).
*Cosa si vede.* Tre gradi: facade con poster fotografico e iframe solo al click (FO: 0 iframe al caricamento), iframe diretto (CS, Arm), freccia disegnata che punta al player (Arm, richiesta datata nel codice).
*Perché è professionale.* Lo stesso set (libreria blu) in due poster fa marchio; il facade azzera il peso; la freccia rende il play «la cosa più rumorosa dopo il player».
*Come lo rifaremmo.* Poster 830×466 raggio 12 con grana, play 80 px `rgba(10,10,10,.45)` + `backdrop-filter: blur(6px)` bordo 1 px `rgba(255,255,255,.8)`, **durata dichiarata** in mono 14 px nell'angolo (lui non la mette), iframe Vimeo `dnt=1&autoplay=1` creato al click; freccia SVG a mano solo nella pagina di lancio. Già previsto come `GuardaloGirare`/`VSL`.

**E47 · Una sola immagine forte, duplicata e ruotata, con fascia di testo che la attraversa** · Funnel Operator · atlante T16 (`sezioni/16-schiavizzerai-l-ai.png`; sezione 1.440×928 con `carta-serpenti.webp` a 1× e `serpente-testa.webp` 719×854 usata due volte, la seconda `rotate(180deg)`; fascia `oklch(0.946)` y 372→555 con h2 49 px w600 a sinistra e due paragrafi 17 px a destra).
*Perché è professionale.* Composizione da poster con un file solo; la fascia che taglia le figure è un gesto da copertina di rivista.
*Come lo rifaremmo.* Sezione carta 928 px con grana «carta» (variante chiara della nostra grana), un'incisione argento 719×854 ripetuta e ruotata, fascia `#faf6ee` 183 px con h2 49 px w600 + corpo 17 px; su mobile figura sopra e fascia sotto. Per il problema o per «chi guida».

**E48 · Doppio piano: mockup nitido davanti, elemento sfocato dietro** · Funnel Operator · atlante T24 (`sezioni/24-community-su-telegram.png`; iPhone 326×404 a 1×, due aeroplani 405×237 e 297×212 con `blur(3.55px)` e opacità ridotta).
*Perché è professionale.* Profondità di campo con 25 KB; la metafora è letterale ma desaturata.
*Come lo rifaremmo.* Mockup 2× (non 1×) raggio 12 + grana; dietro, un glifo del nostro sistema (incisione argento) a `filter: blur(3.5px); opacity .5`, due istanze specchiate. Per «dentro il sistema» (screenshot dell'inbox/CRM che il cliente vede).

**E49 · Cartella con linguette in clip-path (accordion travestito da raccoglitore)** · Funnel Operator · `desktop-24.png` (y≈21.270-21.600) + `desktop-25.png` (y 21.600-22.500; cartella frontale 832×360 col logo).
*Cosa si vede.* Cinque livelli: quattro fogli `oklch(0.87)` raggio 12 bordo 1 px, ognuno più stretto e più alto di ~60 px, con una linguetta nera trapezoidale (`clip-path: polygon(0 100%, calc(var(--taglio) − 1.7px) 6.9px, …)` alternata sx/dx, `button` 212×57, «01 Intro» 18,9 px w500, numero grigio chiaro + testo bianco); davanti la cartella 832×360 col logo reso nero via `brightness(0)`. Tutto in container-query units (`--gradino: max(48px, 7.239cqw)`, `--linguetta: max(46px, 6.826cqw)`); al hover il foglio si solleva (`:has(button:hover)` + `motion-safe`), al click un Dialog con l'elenco numerato `01, 02…` in mono; i nomi arrivano dal database.
*Perché è professionale.* Metafora fisica in puro CSS che regge a 390 px; geometria e contenuto separati; dialog accessibile con `aria-label`.
*Come lo rifaremmo.* Stesse variabili in `cqw` su un `@container` max 967 px; fogli `#e6e1d7` (carta scurita) raggio 12 bordo 1 px ink; linguette ink con testo `#faf6ee` 19 px w500 e numero in mono; cartella frontale `#faf6ee` con grana e logotipo; `button` + `<dialog>` nativo. 4 linguette = 4 consegne dello sprint. Già previsto come `Cartella`: queste le misure e la meccanica.

---

## §3 — I 10 DA PRENDERE SUBITO

Classifica per impatto sul sito agency (vende una chiamata da 30′ per sistemi AI). «Dove» segue l'ordine dei temi della pagina: problema → meccanismo → prova → offerta → garanzia → FAQ. Dove il sorgente ha già un componente con quel nome, l'elemento **dà le misure a quel componente**, non ne crea un doppione. Copy in voce di casa, prima persona, senza numeri (li mette Emperator da FATTI.md).

| # | Elemento (rif.) | Dove nel nostro sito | Copy di massima |
|---|---|---|---|
| 1 | **Scala a gradini con connettori tratteggiati** (E01) | **Meccanismo**, subito sotto «come funziona» (`FlowFramework` → `Scala`), su carta | «Dal primo messaggio al sistema che gira da solo: questi sono i passi, nell'ordine in cui li faccio davvero. Il traguardo non è il consegnato, è il giorno in cui non ti servo più.» |
| 2 | **Card gemelle «1. / 2.»** (E07) | **Problema**, dopo lo specchio e prima del meccanismo (`DueTipi`) | «Ci sono due modi di usare l'AI in azienda. 1. Chi compra strumenti e li lascia aperti in una scheda. 2. Chi si fa costruire un sistema che lavora anche quando non c'è nessuno. Io lavoro solo con il secondo.» |
| 3 | **Frase barrata + frase vera** (E21) | **Problema**, apertura del tema (sopra `Problems`) | «~~Ti serve un altro tool.~~ Ti serve un sistema che sappia cosa fare quando tu non ci sei.» |
| 4 | **Albero «Tu sei qui»** (E03) | **Meccanismo → chi guida**, prima dell'offerta (`Mappa`) | «Questa pagina è il ramo agenzia di Digital Empire. Gli altri due rami li vedi qui sopra; tu sei sulla foglia in cui costruisco io, con le mie mani, dentro la tua azienda.» |
| 5 | **Rail delle metriche con icona monocroma** (E14) | **Prova**, subito sotto il primo blocco (`RailFatti`) e ripetuto prima dell'offerta | «I numeri che seguono sono i miei, non quelli di un caso studio comprato. Li aggiorno quando cambiano.» |
| 6 | **Checklist in tabella bordata + un solo bottone** (E42 + E35) | **Offerta**, subito sopra `/prenota` (`CosaOttieni` → `FinalCTA`) | «Cosa esce dalla mezz'ora: una mappa di dove l'AI ti fa risparmiare tempo, una stima onesta di cosa costa costruirla, e un no chiaro se non ha senso. Poi decidi tu.» |
| 7 | **Accordion «?» con eyebrow in mono, prima riga aperta** (E31) | **FAQ**, in fondo, in tre gruppi (`FAQ` + `FaqContratto`) | Eyebrow: «PRIMA DELLA CHIAMATA» · «DOPO LA CHIAMATA» · «SOLDI E CONTRATTO». Prima domanda aperta: «Devo prepararmi qualcosa?» — «No. Porta il problema che ti fa perdere più tempo; il resto lo tiro fuori io.» |
| 8 | **Screenshot di call sovrapposti + lavagna, volti pixelati** (E26) | **Prova**, dopo i risultati (`ProveVere`) | «Due chiamate vere, con il permesso di chi c'era. La lavagna è quella che riempio mentre parliamo: te la porti via anche se non lavoriamo insieme.» |
| 9 | **Garanzia in due quadri a zig-zag** (E23) | **Garanzia**, dove sta `MyPromise` / `SeNonFunziona`, su carta | Quadro 1: «E se dopo la chiamata non vedi dove l'AI ti serve…» · Quadro 2: «…hai perso mezz'ora e io ho perso un cliente. Nessuna fattura, nessun seguito, nessuna email che ti insegue.» |
| 10 | **Obiezioni tra virgolette + risposta** (E33) | **Garanzia → FAQ**, fra la garanzia e le FAQ (`Objections`) | «“Se i sistemi funzionano così bene, perché non li tieni per te?” — Li tengo per me: sono quelli che uso ogni giorno. Te li costruisco perché il mio lavoro è costruirli, non venderti il mio tempo per sempre.» |

**Riserve immediate (11-14), da usare se una delle dieci non passa il gate solo-aggiunte:** asse «TU — sei qui» (E04) sotto il problema; griglia 01-04 mono con una colonna accesa (E06) per le 4 fasi del meccanismo; tessera del cliente (E17) accanto alle condizioni; CTA sticky che si ritira quando l'offerta è in vista (E36) — quest'ultima è una taratura di `sticky-cta.tsx`, non una sezione.

**Le tre regole di taratura che valgono per tutte e dieci** (da §1): colonna 832 dentro 880; corpo 17/1,6 e h2 37/1,2 w700 (**non** 48-52); padding 96 px, raggi 8/12/24, filetti 1 px al posto delle ombre, arancione su una parola per titolo e su un bottone per tema, grana su ogni superficie.

---

## Fonti

- `competitor/Andrei Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md`, `11-armageddon.md`
- `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md`, `12-claude-speedrun-STACK-E-TOKEN.md`
- `competitor/Andrei Pascu/site-study/reports/66-funneloperator-ATLANTE-VISIVO.md`, `66-funneloperator-STILE.md` (§0-§3, §6), `66-funneloperator-COSTRUZIONE.md` (§2.4, §3, §4)
- `competitor/Andrei Pascu/site-study/capture/{11-armageddon,12-claude-speedrun-v2,66-funneloperator-it}/design-tokens.json`
- Schermate: `capture/11-armageddon/desktop-01…06.png`; `capture/12-claude-speedrun-v2/desktop-01, 02, 03, 06, 07, 09, 10, 12, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 31, 32.png` + `sezioni/19, 31, 32`; `capture/66-funneloperator-it/desktop-01, 02, 03, 04, 05, 08, 09, 12, 13, 15, 18, 20, 21, 22, 23, 24, 25, 26, 27, 31, 32, 33, 35, 37.png`
- Ordine dei temi del nostro sito: `agency-empire-landing/src/app/page.tsx` (solo per collocare §3)
- Vincoli: ADR-030 (solo aggiunte), `gate_solo_aggiunte.py`, `PIANO-MAESTRO/38-PIANO-SITO-AGENCY-SOLO-AGGIUNTE-v2.md`
