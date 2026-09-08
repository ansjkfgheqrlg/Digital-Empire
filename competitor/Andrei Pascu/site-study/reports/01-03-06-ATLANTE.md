---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #atlante-visivo #design-system #reference #onda-c
Created: 2026-09-08
Last updated: 2026-09-08
---

# ATLANTE VISIVO — le altre tre pagine dell'ecosistema Andrei Pascu

**La Home (01-andrei-copy-home) · outHeadline (03-outheadline) · Manuale del Copywriter
(06-manuale-del-copywriter).** Come nel report gemello sulle tre pagine grandi
([02-04-05-grandi-ATLANTE.md](02-04-05-grandi-ATLANTE.md)), ogni misura viene da `scheda.json`
(campionato dal DOM al momento della cattura v2, che per la prima volta su queste sei pagine include
sia `sezioni/` sia `scheda.json` — prima non c'erano). Le tavole descritte come "viste" sono state
aperte con lo strumento di visione in `../capture/<pagina>/sezioni/`; le sezioni non coperte da una
tavola restano comunque in tabella coi loro numeri, dichiarate esplicitamente come non verificate a
occhio in questa passata. Modello di forma: [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md). Il copy è
già coperto in `01-andrei-copy-home-COPY.md`, `03-outheadline-COPY.md`,
`06-manuale-del-copywriter-COPY.md` — qui si tratta solo la composizione visiva.

Tutte e tre le pagine sono sulla stessa piattaforma Squarespace (`www.andrei-copy.com`) delle tre
pagine grandi, ma qui la varietà di ruolo è più ampia: una è la home istituzionale (0€, non vende
nulla direttamente), una è un mini-corso da 98€ (stesso prezzo di outFunnel), una è un ebook.

| | La Home | outHeadline | Manuale del Copywriter |
|---|---|---|---|
| Prezzo | — (non vende, smista) | **98€** | ebook (prezzo non mostrato nelle sezioni viste) |
| URL | `/` | `/outheadline` | `/manuale-del-copywriter` |
| Altezza pagina | **3.384px** — la più corta di tutto l'ecosistema studiato | 21.119px | 11.067px |
| Sezioni totali / distinte | 5 / 4 | 19 / 16 | 13 / 12 |
| `body_bg` | `#a8a8a8` (grigio "brand in aggiornamento") | — | — |
| Palette sfondi dominante | `#1b1b1d` (10 occorrenze), blu `#0062ff` (6) | — | — |

---

## PARTE 1 — La Home (01-andrei-copy-home), 3.384px, 5 sezioni/4 distinte

È la pagina più corta misurata in tutto l'ecosistema — **5 sezioni contro le 13-28 delle altre**. Non
vende: smista verso risorse, blog e storia personale. Per questo motivo qui sono state aperte **tutte
e 4 le sezioni distinte** (compreso il footer, già documentato nel report gemello) — è l'unica pagina
di tutto lo studio coperta al 100% a occhio.

### Tavola H1 — L'hero: nav bar sovrapposta e riquadro identità con badge
![sezione 01](../capture/01-andrei-copy-home/sezioni/01-formazione-tecnica-per-professioni.png)

**Ruolo**: hero istituzionale, smista verso "Scopri di più" senza vendere un prodotto specifico.
**Altezza**: 749px — **22,1%** della pagina, quasi un quarto pur essendo l'hero più corto in assoluto
misurato in questo studio (contro i 750-1.330px delle pagine-prodotto).

**Cosa la compone**: H2 "Formazione tecnica per professionisti di marketing" (non H1 — unico caso fra
tutte le hero studiate dove il titolo massimo della pagina è un H2), paragrafo troncato dal viewport
("AP Sales è un'agenzia di marketing... E qui insegniamo **il nostro scientifico** e **preciso**..."),
bottone blu "Scopri di più →", e a destra un **ritratto fotografico reale in cornice rettangolare** con
due badge dati sovrapposti in stile "callout tecnico": riquadro bianco "+280K FOLLOWERS" collegato con
una linea all'orecchio del soggetto, riquadro blu "+1M GENERATO COL COPYWRITING" collegato alla spalla.
Sullo sfondo destro, un pattern di piccoli puntini/candlestick da grafico di borsa in bassissima
opacità. `blocchi_testo: 4`, `parole: 29`, `media: 5`, `cta: 1`. Firma
`section|page-section.has-section-divider.full-bleed-section|3|M|C|4`, gruppo 1, rappresentante.

**Difetto di cattura osservato**: come già documentato nel report gemello (Tavola O1, outFunnel), una
barra scura sticky con "Claude Speedrun" a sinistra e "Accedi" a destra è sovrapposta a metà altezza
dell'hero, tagliando in due sia il ritratto che il paragrafo. Non è un elemento di questa pagina (la
Home non menziona "Claude Speedrun") — stesso artefatto di cattura, confermato ora su **due pagine
diverse dell'ecosistema**, quindi sistemico e non isolato.

**Effetti attivi**: i due badge-callout hanno una linea di collegamento sottile (probabile SVG con
`stroke-dasharray`, coerente con le linee tratteggiate viste anche nella Tavola 2 di apsales.eu per un
pattern simile "etichetta collegata a un soggetto").

**Perché è costruita così**: i due numeri (+280K follower, +1M generato) sono lo stesso tipo di prova
usata più diffusamente nelle pagine-prodotto (numeri concreti vicino al volto dell'autore), qui
compressi in due soli badge invece di una sezione a parte — coerente con una home che deve restare
breve e rimandare l'approfondimento a pagine dedicate.

---

### Tavola H2 — "Risorse": tre card gratuite, stesso banner "brand in aggiornamento"
![sezione 02](../capture/01-andrei-copy-home/sezioni/02-risorse.png)

**Ruolo**: hub di navigazione verso risorse gratuite (corso base, stack tool, attrezzatura).
**Altezza**: 898px — **26,5%**, la sezione singola più alta della Home.

**Cosa la compone**: banner fisso in alto a sinistra "Stiamo aggiornando il brand — Potresti trovare
colori strani, font sbagliati, o simili." con bottone "Capito" (**questo è un banner reale del sito,
non un artefatto di cattura** — a differenza della barra "Claude Speedrun", questo è coerente con
`body_bg: #a8a8a8` misurato in `scheda.json` e riappare identico anche nel Manuale, Tavola M4), H1
"Risorse" a destra, poi **tre card identiche nella struttura** affiancate: illustrazione tratteggiata
in stile wireframe puntinato (un laptop con scritta "LE BASI", un fiore/asterisco a 8 punte, una
fotocamera Sony), etichetta categoria in blu monospace ("CORSO GRATUITO" / "TOOLS & AI" /
"ATTREZZATURA"), H3, paragrafo, bottone bianco con freccia diagonale ("INIZIA IL CORSO ↗" / "ESPLORA LO
STACK ↗" / "SCOPRI IL SETUP ↗"). `blocchi_testo: 23`, `parole: 81`, `media: 5`, `cta: 3` — un CTA per
card. Firma identica alla Tavola H1: `section|page-section.has-section-divider.full-bleed-section|3|M|C|4`,
stesso gruppo 1, ma **non rappresentante** — cioè secondo `scheda.json` questa sezione ha la stessa
"firma strutturale" dell'hero, pur essendo visivamente un hub a tre colonne e l'hero un hero a due
colonne. **Nota di misura**: è un caso, come già osservato per le "Tavole gemelle" del report apsales
(Tavola 5/9), in cui la firma coincide ma la composizione visiva reale è ben diversa — la firma
cattura profondità di annidamento e presenza di media/CTA, non il numero di colonne.

**Effetti attivi**: le tre illustrazioni sono in stile puntinato/wireframe (tecnica visiva simile
all'effetto `Ascii` documentato nel report apsales, qui applicata a un laptop, un fiore e una
fotocamera invece che a un occhio o a un guerriero — **stesso linguaggio visivo `Ascii`/dot-pattern
riusato su un dominio Squarespace diverso da quello Next.js di apsales**, segno che è un pattern di
figura ricorrente in tutto l'ecosistema Andrei Pascu, non solo del sito apsales.eu).

**Perché è costruita così**: tre card identiche per struttura (icona-etichetta-titolo-bottone) sono il
modo più economico di offrire tre percorsi diversi (corso/tool/attrezzatura) senza dover inventare tre
layout — la Home fa da directory, non da pagina di vendita, quindi la ripetizione di schema qui è una
scelta di chiarezza, non di pigrizia.

---

### Tavola H3 — "Blog": lista articoli con un elemento evidenziato
![sezione 03](../capture/01-andrei-copy-home/sezioni/03-blog.png)

**Ruolo**: hub secondario verso i contenuti editoriali.
**Altezza**: 481px — **14,2%**, la più corta delle 4 sezioni distinte della Home.

**Cosa la compone**: colonna sinistra con H1 "Blog", paragrafo descrittivo, bottone blu "Leggi gli
articoli"; colonna destra con una lista di articoli in riquadri orizzontali (thumbnail + titolo in
maiuscolo monospace): "ANDREI PASCU CORSI: LE REGOLE CON CUI COSTRUIAMO FORMAZIONE AD ALTO STANDARD",
**"COS'È UN FUNNEL OPERATOR?"** — questo secondo riquadro ha sfondo bianco pieno mentre gli altri sono
trasparenti/bordati, quindi risulta l'unico visivamente "acceso" nella lista — e "STAI PARLANDO
DAVVERO CON ANDREI PASCU?" con thumbnail rossa/warning. `blocchi_testo: 3`, `parole: 26`, `media: 2`,
`cta: 1`. Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|C|2`, gruppo 3,
rappresentante unico.

**Effetti attivi**: nessun filtro dichiarato; il contrasto bianco-pieno vs bordo-trasparente
sull'articolo "Funnel Operator" è puro colore, non un effetto — ma dato che è visivamente l'unico
"acceso" della lista visibile, funziona come una sezione featured senza dichiararsi tale.

**Perché è costruita così**: la lista blog che promuove esattamente l'articolo sul prodotto da 434€
(Funnel Operator) — non a caso, dato che è il prodotto di fascia media dell'ecosistema — mostra come la
Home instrada silenziosamente il traffico generico verso il prodotto che l'autore vuole spingere in
quel momento, senza che sembri una pubblicità diretta (è "solo" un articolo del blog).

---

### Tavola H4 — "La mia storia": collage fotografico 2019→2026
![sezione 04](../capture/01-andrei-copy-home/sezioni/04-la-mia-storia.png)

**Ruolo**: chiusura della Home con prova di percorso personale, prima del footer.
**Altezza**: 551px — **16,3%**.

**Cosa la compone**: **collage di due foto sovrapposte** a rotazione leggera (stile polaroid): foto
2019 in giacca e cravatta (bianco/nero, espressione seria, etichetta bianca "2019" in basso a
sinistra) parzialmente coperta da una foto 2026 (colore, occhiali, dito al mento, etichetta blu "2026"
in basso a destra) che sporge sopra e a destra della prima; a destra del collage, H1 "La mia storia",
due frasi ("Sono Andrei Pascu, titolare di AP Sales... Sono qui per insegnare il marketing per come lo
vedo io."), bottone blu "Leggi la mia storia". `blocchi_testo: 6`, `parole: 31`, `media: 3`, `cta: 1`.
Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|C|3`, gruppo 4, rappresentante
unico.

**Effetti attivi**: rotazione CSS leggera su entrambe le foto (`transform: rotate(...)`, coerente con
le `trasformazioni: matrix(...)` misurate a livello di pagina) per l'effetto polaroid-collage; nessun
filtro colore.

**Perché è costruita così**: **il contrasto bianco/nero-2019 vs colore-2026 è l'argomento stesso**,
senza bisogno di scriverlo: 7 anni di percorso in due fotografie, stesso principio della sequenza
"Piacere sono Andrei" di Funnel Operator (report gemello, Tavola F2) ma qui compresso al minimo — 2
foto invece di 3, perché la Home deve restare una pagina di transito, non di approfondimento.

---

### Tabella riepilogo Home

| i | h (px) | % pag. | media | cta | parole | firma/gruppo | note |
|---|---|---|---|---|---|---|---|
| 5 | 705 | 20,8% | 7 | 2 | 99 | footer, gr.5 | footer condiviso — visto e documentato nel report gemello (blu pieno, templare pixel-art) |

**Riepilogo pagina**: media totale = **22**, parole totali = **266**, blocchi_testo totale = **60**,
CTA totale = **8**. Nessun blocco "div-border" muto: tutte e 5 le sezioni della Home portano contenuto
verificabile — coerente con l'assenza quasi totale di "filler" tipica delle pagine più corte di questo
studio.

---

## PARTE 2 — outHeadline, 98€ (h=21.119px, 19 sezioni/16 distinte)

Stesso prezzo esatto di outFunnel (report gemello). Utile confronto diretto: due prodotti gemelli per
prezzo, ecosistema, piattaforma — ma con temi di superficie opposti (rosso/nero aggressivo qui, teal
tecnico in outFunnel).

### Tavola HL1 — L'hero rosso: headline come dimostrazione, non come promessa
![sezione 01](../capture/03-outheadline/sezioni/01-questa-una.png)

**Ruolo**: hero dimostrativo — il titolo stesso è l'esempio del prodotto che vende.
**Altezza**: 1.161px — **5,5%**.

**Cosa la compone**: sfondo con gradiente verticale nero→rosso acceso (`#a8a8a8`/nero in alto, rosso
pieno in basso, l'unico gradiente cromatico a due tinte nette osservato in queste sei pagine — le altre
usano quasi sempre variazioni di nero/blu), H1 "QUESTA È UNA" in bianco seguito da "HEADLINE." in
**rosso pieno enorme** (il doppio della dimensione del resto), un punto fermo bianco isolato dopo la
parola, freccia rossa curva a sinistra che punta verso l'alto, paragrafo con "solo" e "HEADLINE" in
rosso dentro il testo bianco, ultima riga in corsivo, e un **player video reale** in basso (thumbnail
volto con cuffie, 00:00/00:46, controlli funzionanti). `blocchi_testo: 39` — il valore più alto della
pagina insieme alla sezione 09 (94 blocchi, lista lezioni). `parole: 29`, `media: 13`, `cta: 0`. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|-|6`, gruppo 1, rappresentante
unico.

**Effetti attivi**: gradiente verticale nero-rosso (probabile `linear-gradient` sul body/sezione, non
un'immagine); nessun filtro dichiarato aggiuntivo.

**Perché è costruita così**: il titolo stesso ("QUESTA È UNA HEADLINE.") è un esempio meta-referenziale
— l'headline che stai leggendo dimostra da sola cosa il corso insegna a scrivere, invece di descrivere
il beneficio in astratto. È lo stesso principio didattico della Tavola F4 (Funnel Operator, "prima/dopo
CRO" con lo stesso spazzolino) applicato all'hero invece che a metà pagina.

---

### Tavola HL2 — Il div "border" che nasconde testo persuasivo pieno (secondo caso confermato)
![sezione 03](../capture/03-outheadline/sezioni/03-div.png)

**Ruolo**: gestione obiezione sul costo-opportunità di non saper scrivere headline.
**Altezza**: 2.169px — **10,3% della pagina, la sezione singola più alta di outHeadline**.

**Cosa la compone secondo scheda.json**: `tag: div`, `classi: section-border`, `bg: #1b1b1d`,
`blocchi_testo: 0`, `parole: 0`, `media: 1`. Firma `div|section-border|1|M|-|11`, gruppo 3 — la firma
più "pesante" (11 nell'ultimo segmento) fra tutti i div-separatori osservati in questo studio, segno
che il nodo ha effettivamente molto DOM annidato dentro, nonostante il conteggio testo a zero.

**Cosa mostra davvero lo screenshot**: H1 "Perché lasciare soldi sul tavolo?!" con "Perché" sottolineato
a mano libera, una fotografia reale (uomo in giacca, braccia conserte, dietro una pila di banconote su
un tavolo verde), un paragrafo esplicativo di 5 righe su sales page/ads/tempo perso, un secondo blocco
a due colonne (testo a sinistra "La sales page te la può scrivere il miglior copy al mondo... ma se il
titolo non fa leggere..." e un mockup telefono con un sito ristorante fittizio "The Sunday Bite" a
destra, con effetto fiamma), infine un blocco conclusivo a specchio con due frecce curve che collega
"titolo persuasivo → legge → forse compra" contro "titolo non persuasivo → non legge → al 100% non
compra". **Confermato per la terza volta in questo studio complessivo (le prime due nel report gemello:
outFunnel Tavola O2 e Copywriting Mentorship sez.4)**: la firma `div|section-border` con
`blocchi_testo: 0` è un falso negativo sistemico — qui nasconde probabilmente **il blocco di testo più
denso e argomentativo di tutta la sezione**, non un separatore vuoto.

**Effetti attivi**: il mockup telefono ha un effetto fiamma/fuoco sovrapposto (illustrazione, non
filtro CSS); le frecce curve del blocco finale sono SVG a mano libera, stesso stile della freccia
rossa nell'hero (Tavola HL1) — coerenza di un unico set di illustrazioni "disegnate a mano" per tutta
la pagina.

**Perché è costruita così (ipotesi)**: come nel caso gemello di outFunnel, il pattern sembra un
componente di reveal scroll-triggered che il DOM misura prima che il testo sia "montato" visivamente —
sistemico su tutte le pagine Squarespace di questo ecosistema che usano il blocco "divisore/curtain".

---

### Tavola HL3 — Il curriculum lezioni: 94 blocchi, doppia sezione, doppio accordion
![sezione 09](../capture/03-outheadline/sezioni/09-outheadline-lista-lezioni.png)

**Ruolo**: contenuto/programma — prova di sostanza didattica.
**Altezza**: 1.718px — **8,1%**.

**Cosa la compone**: H1 "outHeadline lista lezioni:", due macro-gruppi ciascuno con: sottotitolo H2,
paragrafo, **3 card di lezione affiancate** (thumbnail scura con badge verde "LEZIONE N", titolo
lezione, breve descrizione — stile identico alle card-lezione osservate anche in altri prodotti
dell'ecosistema) seguite da un accordion con più righe cliccabili (icona "+"): primo macro-gruppo
"Sezioni A & B: introduzione al copy" con Sezione A/B, secondo macro-gruppo "Sezioni 1,2,3,4 & 5: come
scrivere headline" con 5 righe accordion (Le basi degli headline / Come scrivere headline / La scienza
dietro alle headline / Andrei scrive headline / Headline checklist). `blocchi_testo: 94` — **il valore
più alto di tutta la pagina**, `parole: 97`, `media: 2`, `cta: 7` — un trigger per riga accordion. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|C|9`, gruppo 9, rappresentante
unico.

**Effetti attivi**: leggero effetto "glitch"/doppia-esposizione cromatica (rosso/ciano) visibile sul
titolo H2 del primo sottogruppo ("Sezioni A & B") — coerente con un `text-shadow` a doppio canale
colore, non documentato altrove nell'ecosistema come pattern ricorrente (elemento specifico di questa
pagina, in tema con l'estetica "hacker/rosso" dell'hero).

**Perché è costruita così**: dividere il curriculum in due macro-blocchi (introduzione vs corpo
tecnico) invece di un accordion piatto a 7 righe rende leggibile la progressione del corso — prima le
basi (2 lezioni), poi la parte "vera" (5 lezioni) — e le card visive sopra ogni accordion danno un
assaggio concreto (thumbnail reale della lezione) prima di chiedere il clic per espandere.

---

### Tavola HL4 — "ONE SHOT, ONE KILL": la metafora militare a tutta sezione
![sezione 13](../capture/03-outheadline/sezioni/13-one-shot.png)

**Ruolo**: framing concettuale del mestiere (copywriter = cecchino).
**Altezza**: 1.716px — **8,1%**, appaiata alla Tavola HL3 come seconda sezione più alta.

**Cosa la compone**: fondo bianco/crema (**unica sezione a fondo chiaro di outHeadline**, come già
osservato per apsales Tavola 10 e per il collage-Home Tavola H4 — il fondo chiaro come marcatore di
"sezione importante da isolare"), H1 enorme su due righe "ONE SHOT, ONE KILL" in nero pieno, fotografia
reale di un cecchino/tiratore in tenuta tattica con pistola puntata verso l'obiettivo (bandiera polacca
sulla manica — foto reale, non stock generico), due paragrafi che sviluppano l'analogia
copywriter/cecchino, filetto divisorio orizzontale, H2 "Copywriter : campagna di marketing = cecchino :
missione militare", due colonne "Uno sniper deve calcolare" (Vento/Distanza/Superficie/Atmosfera/
Altitudine) vs "Tu devi calcolare" (Consapevolezza/Targeting/Obiezioni/Elementi strategici/Headline),
chiusura paragrafo. `blocchi_testo: 33`, `parole: 166`, `media: 1`, `cta: 0`. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|-|9`, gruppo 13, rappresentante
unico.

**Effetti attivi**: nessuno oltre al cambio di fondo (chiaro su scuro); la foto non ha filtri
particolari, è trattamento fotografico standard.

**Perché è costruita così**: l'analogia a doppia colonna (5 variabili dello sniper ↔ 5 variabili del
copywriter, in corrispondenza riga per riga) è un dispositivo mnemonico — l'ultima riga di entrambe le
colonne è "Altitudine…"/"Headline", quindi l'headline è presentata come l'ultima, più difficile,
variabile da calcolare: struttura retorica a climax.

---

### Tavola HL5 — La CTA finale con prezzo identico a outFunnel
![sezione 18](../capture/03-outheadline/sezioni/18-outheadline-probabilmente-non-per.png)

**Ruolo**: CTA di chiusura + prezzo.
**Altezza**: 876px — **4,1%**.

**Cosa la compone**: fondo nero pieno, titolo su tre righe ("outHeadline? Probabilmente non è per te.
Ma se lo è… Stai per svoltare.") — **frase quasi identica parola per parola** alla chiusura di
outFunnel (Tavola O6 del report gemello: "outFunnel? Probabilmente non è per te. Ma se lo è… Stai per
svoltare.") — sottolineatura verde a mano libera sotto "outHeadline", card prezzo bianca con logo
verde sfumato "outHeadline", **"€98 / pagamento unico"** in verde, bottone scuro "Entra ora in
outHeadline". `blocchi_testo: 4`, `parole: 17`, `media: 3`, `cta: 1`. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|C|4`, gruppo 18, rappresentante
unico.

**Confronto diretto con outFunnel (stesso prezzo, 98€)**: template di chiusura **identico al pixel**
— stessa struttura, stesso verde, stessa impaginazione della card prezzo, persino lo stesso copy di
apertura frase. Prova diretta che, a parità di prezzo, l'ecosistema Andrei Pascu riusa lo stesso
componente di chiusura-vendita cambiando solo nome prodotto e colore di accento (verde in entrambi i
casi, qui e in outFunnel — mentre Funnel Operator a 434€ usa blu e Copywriting Mentorship a 999€ usa
oro/giallo). **Il colore di accento della card-prezzo sembra codificare la fascia, non il prodotto**:
verde=98€ (×2), blu=434€, oro=999€.

**Effetti attivi**: identici alla Tavola O6 (sottolineatura vettoriale animata).

**Perché è costruita così**: riusare lo stesso template di chiusura per prodotti allo stesso prezzo
riduce il tempo di produzione e rinforza — per chi ha visto entrambe le pagine (lo stesso pubblico di
follower) — un pattern di riconoscimento "questo è un prodotto della fascia base".

---

### Tabella completa — le altre 14 sezioni di outHeadline

| i | h (px) | % pag. | media | cta | parole | firma/gruppo | note |
|---|---|---|---|---|---|---|---|
| 2 | 1.467 | 6,9% | 5 | 0 | 40 | has-divider, gr.2 | "Ecco cosa succede se 1000 persone vedono la tua pagina" |
| 4 | 797 | 3,8% | 2 | 0 | 90 | full-bleed, gr.4 | "Se sei un copywriter…" |
| 5 | 1.053 | 5,0% | 2 | 1 | 32 | full-bleed, gr.5 | "Vedi la differenza tu stesso" — headline interattiva a bottone |
| 6 | 1.104 | 5,2% | 3 | 1 | 95 | full-bleed, gr.6 | "Dove troverai tutte le strategie…" |
| 7 | 1.074 | 5,1% | 5 | 0 | 174 | has-divider, gr.7 | "Le basi del copy sono ovunque…" |
| 8 | 754 | 3,6% | 1 | 0 | 0 | div-border, gr.8 | muta nel DOM — non vista, verosimile stesso difetto della Tavola HL2 |
| 10 | 686 | 3,2% | 3 | 0 | 5 | full-bleed, gr.10 | "outHeadline non è per principianti" |
| 11 | 748 | 3,5% | 3 | 0 | 79 | has-divider, gr.11 | "Per scrivere headline basta usare formule" |
| 12 | 1.263 | 6,0% | 1 | 0 | 0 | div-border, gr.12 | muta nel DOM — non vista |
| 14 | 1.069 | 5,1% | 2 | 0 | 143 | full-bleed, gr.14 (= sez.17) | "Un corso di più di 3 ore su come scrivere titoli?" |
| 15 | 973 | 4,6% | 3 | 0 | 138 | = sez.7 (gr.7) | "Entrando in outHeadline… multinazionali" |
| 16 | 715 | 3,4% | 1 | 0 | 0 | = sez.8 (gr.8) | muta — non vista |
| 17 | 1.004 | 4,8% | 3 | 0 | 94 | = sez.14 (gr.14) | "Ma io le faccio scrivere a ChatGPT" |
| 19 | 705 | 3,3% | 7 | 2 | 99 | footer, gr.19 | footer condiviso |

**Riepilogo pagina**: media totale = **55**, parole totali = **1.243**, blocchi_testo totale = **231**,
CTA totale = **12**. Blocchi "div-border" muti (sez.3, 8, 12, 16) sommano **4.901px = 23,2% della
pagina** — **la percentuale di filler-DOM più alta misurata in tutte e sei le pagine di questo studio**,
persino sopra outFunnel (19,5%, stesso prezzo di 98€). I due prodotti da 98€ dell'ecosistema sono
quindi anche i due con più blocchi "muti" secondo il DOM — coerente con quanto osservato nel report
gemello sulla relazione fra prezzo basso e alta quota di div-separatori.

---

## PARTE 3 — Manuale del Copywriter (ebook), h=11.067px, 13 sezioni/12 distinte

La pagina più corta fra le tre "pagine-prodotto" studiate in questo atlante (11.067px, meno della metà
di outHeadline) — coerente con un ebook, che richiede meno sezioni di scomposizione di un video-corso.

### Tavola M1 — L'hero: mockup tablet+telefono su fondo texture
![sezione 01](../capture/06-manuale-del-copywriter/sezioni/01-ebook-sul-copywriting.png)

**Ruolo**: hero prodotto fisico/digitale (ebook).
**Altezza**: 627px — **5,7%**, la più corta fra tutte le hero misurate in questo studio (escludendo la
Home che non vende).

**Cosa la compone**: fondo grigio con texture "a pietra"/marmorizzata (diverso da tutti i fondi neri
delle altre pagine — **unico fondo testurizzato chiaro usato come hero di un prodotto in vendita**),
**mockup a doppio device** (un tablet grande e uno smartphone più piccolo sovrapposto, entrambi con la
cover del libro "MANUALE DEL COPYWRITER" — copertina nera con un teschio/mano disegnata a tratto bianco
e testo a colonna verticale sui lati), a destra overline "– eBook sul Copywriting –", H1 "Impara la
skill più importante: la vendita scritta", sottotitolo "(in 115 pagine pratiche)", paragrafo, bottone
nero pieno "Acquista 🔥 Per accesso istantaneo". `blocchi_testo: 5`, `parole: 56`, `media: 2`, `cta: 1`.
Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|C|3`, gruppo 1, rappresentante
— **condivide la firma con la sezione 12** (i=12, muta, senza heading, chiusura pre-footer), diversa
composizione visiva ma stessa "firma strutturale" (stesso fenomeno già visto nella Tavola H2).

**Effetti attivi**: nessun filtro dichiarato specifico; la texture di fondo è verosimilmente
un'immagine/pattern CSS ripetuto (`grana`), diversa dal `bg-void` piatto delle altre pagine.

**Perché è costruita così**: il mockup a doppio device (tablet+telefono, non un singolo libro
fotografato) comunica "leggibile ovunque" prima ancora di leggere una parola — un argomento di formato
implicito, tipico di un prodotto digitale che vuole sembrare tanto solido quanto un libro fisico (115
pagine dichiarate subito, numero concreto).

---

### Tavola M2 — Il carosello mockup: tre varianti di copertina/contenuto
![sezione 06](../capture/06-manuale-del-copywriter/sezioni/06-section.png)

**Ruolo**: galleria prodotto — altre viste del mockup.
**Altezza**: 359px — **3,2%**, compatta.

**Cosa la compone**: fondo grigio pieno (`#a8a8a8`, stesso grigio-brand-in-aggiornamento della Home),
tre riquadri scuri affiancati con frecce di navigazione ai lati (‹ ›): il libro su una roccia scura, un
riquadro con lista "➜ Formule / ➜ Esempi / ➜ Strategie" e testo "Che vendono da far paura." su sfondo
nero con mockup telefoni, il libro su una roccia chiara. `blocchi_testo: 16`, `parole: 4` (quasi tutto
il "peso" testuale è nell'immagine centrale, non nel DOM — stesso limite di misura visto nelle Tavole
O3/C4 del report gemello: contenuto rasterizzato dentro un'immagine di marketing, invisibile al
contatore parole). `media: 16`, `cta: 2`. Firma
`section|page-section.user-items-list-section.full-bleed-section|2|M|C|2`, gruppo 6, rappresentante
unico — è l'unica sezione di tutto lo studio con la classe `user-items-list-section` (probabile
componente Squarespace nativo per gallerie prodotto, diverso dal generico `layout-engine-section` usato
ovunque altrove).

**Effetti attivi**: frecce carosello (stesso pattern di controllo visto nelle Tavole F3, C4); nessun
filtro colore dichiarato.

**Perché è costruita così**: mostrare il libro su superfici diverse (roccia scura, roccia chiara) più
un riquadro-benefit ("Formule/Esempi/Strategie... che vendono da far paura") in mezzo imita il
packaging shot tipico dell'e-commerce fisico — anche se il prodotto è un PDF, la messa in scena richiama
un oggetto reale su cui si può "girare intorno".

---

### Tavola M3 — L'anteprima gratuita: lead magnet a due card + form email
![sezione 07](../capture/06-manuale-del-copywriter/sezioni/07-anteprima-gratuita.png)

**Ruolo**: lead magnet — cattura email prima dell'acquisto.
**Altezza**: 2.179px — **19,7% della pagina, la sezione singola più alta di tutto l'atlante 2** (quasi
un quinto dell'intera pagina in una sola sezione).

**Cosa la compone**: icona regalo, overline "– Anteprima gratuita –" (con "gratuita" in verde), H1 "Il
manuale ti dice esattamente come/cosa scrivere per vendere…", H2 "…E se non ci credi, ho le prove.",
doppia freccia di scroll animata, **due card affiancate a fondo texture scura** ("La mia promessa per
te" con mockup telefoni-grafici a destra; "Per mostrarti che io mantengo le promesse…" con foto di un
orologio e telefono su sfondo rosso), sottotitolo "Ricevi un'anteprima gratuita del manuale", **mockup
a tre livelli sovrapposti** (telefono nero, foglio anteprima bianco, copertina "ANTEPRIMA — MANUALE DEL
COPYWRITER" in primo piano), form con placeholder "Indirizzo e-mail" e bottone grigio "Ricevi
l'anteprima", nota privacy. `blocchi_testo: 26`, `parole: 98`, `media: 8`, `cta: 1` (il form/bottone).
Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|C|11`, gruppo 7,
rappresentante unico — firma con il segmento finale più alto (11) di tutta la pagina, coerente con
l'essere la sezione più complessa (form + 2 card + mockup a 3 livelli).

**Effetti attivi**: doppia freccia di scroll con probabile animazione di bounce verticale (icona
`≫` ripetuta, coerente con pattern di invito-a-scorrere visto anche altrove); nessun filtro colore
dichiarato sulle card.

**Perché è costruita così**: un ebook a basso attrito d'acquisto (nessun prezzo mostrato prima di
questa sezione) investe comunque quasi il 20% della pagina in un form-email **prima** del bottone
d'acquisto — segno che l'obiettivo primario di questa pagina potrebbe non essere la vendita diretta ma
la costruzione di lista, con la vendita come esito secondario di chi si converte dopo aver ricevuto
l'anteprima.

---

### Tavola M4 — I capitoli del manuale: indice a due colonne, 18 CTA
![sezione 10](../capture/06-manuale-del-copywriter/sezioni/10-quali-sono-i-capitoli-del-manuale.png)

**Ruolo**: trasparenza di contenuto — indice completo prima dell'acquisto.
**Altezza**: 1.319px — **11,9%**.

**Cosa la compone**: H1 "Quali sono i capitoli del Manuale del copywriter?", sottotitolo, **due colonne
accordion affiancate**: "Elenco delle parti" (7 righe: Cos'è il copywriting / Perché questo libro è
importante / Come usare questo libro / Perché le persone comprano / La struttura base del copywriting
APSOC / I tipi di copywriting / Componente emotiva nel copywriting) e "Elenco dei manuali" (11 righe:
Fasi di scrittura di un copy / Attenzione / Problema / Soluzione / Obiezioni / CTA / Target / Funnel /
Storytelling VS Direct response / Conseguenza del non agire + urgenza di tempo / Altre strategie,
terminologia e regole). `blocchi_testo: 119` — **il valore più alto di tutte le sei pagine studiate in
questo atlante 2**, `parole: 173`, `media: 1`, `cta: 18` — **il valore più alto di CTA di qualunque
sezione in tutto lo studio (superiore anche alle FAQ da 10 CTA di Funnel Operator e alle 9 di
Copywriting Mentorship)**. Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|C|7`,
gruppo 10, rappresentante unico.

**Effetti attivi**: accordion su 18 righe indipendenti (stesso pattern height-animato osservato
ovunque); nessun filtro colore.

**Perché è costruita così**: mostrare l'indice **completo e dettagliato** (7+11=18 voci) prima
dell'acquisto è una scelta di trasparenza radicale per un ebook — a differenza dei corsi video (dove il
curriculum a volte resta parzialmente velato, es. outHeadline Tavola HL3 con solo 7 righe visibili),
qui non c'è nulla da nascondere: il framework APSOC citato esplicitamente (Parte 5) è lo stesso
framework che l'ecosistema Digital Empire usa come standard di copy — prova che l'autore mostra la
propria metodologia come parte della vendita, non la nasconde come segreto.

---

### Tabella completa — le altre 8 sezioni del Manuale

| i | h (px) | % pag. | media | cta | parole | firma/gruppo | note |
|---|---|---|---|---|---|---|---|
| 2 | 567 | 5,1% | 11 | 0 | 14 | full-bleed, gr.2 | "Guarda sto video" — 11 media, verosimile galleria di icone attorno al player |
| 3 | 519 | 4,7% | 0 | 0 | 88 | background-width--full-bleed, gr.3 | "Libri di business" — unica sezione a 0 media della pagina insieme alla FAQ |
| 4 | 403 | 3,6% | 1 | 0 | 91 | full-bleed, gr.4 | "Perché la maggior parte dei libri dicono tanto e nulla?" — densità 23, la più alta della pagina |
| 5 | 925 | 8,4% | 4 | 0 | 102 | full-bleed, gr.5 | "Il copywriting è un business, non un romanzo" |
| 8 | 711 | 6,4% | 1 | 3 | 127 | full-bleed, gr.8 | "Ho sempre odiato sfogliare libri" |
| 9 | 1.090 | 9,8% | 4 | 1 | 140 | full-bleed, gr.9 | "Okay, ma chi sono io per parlarti di copywriting?" |
| 11 | 868 | 7,8% | 0 | 8 | 55 | full-bleed, gr.11 | FAQ — 5 domande viste (Tavola M5 sotto), 8 CTA totali, 0 media |
| 12 | 689 | 6,2% | 3 | 3 | 11 | = Tavola M1 (gr.1) | chiusura pre-footer, senza heading |
| 13 | 705 | 6,4% | 7 | 2 | 99 | footer, gr.13 | footer condiviso |

### Tavola M5 — Le FAQ: fondo grigio, zero media, otto trigger
![sezione 11](../capture/06-manuale-del-copywriter/sezioni/11-faq.png)

**Ruolo**: gestione obiezioni finali pre-acquisto.
**Altezza**: 868px — **7,8%**.

**Cosa la compone**: fondo grigio pieno (`#a8a8a8`), titolo "FAQ", 7 righe accordion con icona "+" a
destra: "Il libro come lo scarico?" / "Quanto è lungo il libro?" / "Quanto costa?" / "Cosa cambia tra
il corso e il libro?" / "Questo manuale è adatto anche ai principianti?" / "Posso leggere il manuale su
tutti i dispositivi?" / "Questo manuale è solo per chi vuole diventare copywriter professionista?" (più
un'ottava riga tagliata dal viewport: "Ho degli amici interessati al libro, possiamo acquistarlo
insieme?"). `blocchi_testo: 60`, `parole: 55`, `media: 0` — **unica sezione FAQ di tutto lo studio senza
nemmeno un'icona-chevron dichiarata come media** (le FAQ di Funnel Operator e Copywriting Mentorship
hanno `media: 1`). `cta: 8`. Firma `section|page-section.full-bleed-section.layout-engine-section|2|-|C|4`
— **l'unica firma FAQ di tutto lo studio senza il flag `M` (media)** nella stringa, coerenza diretta col
dato numerico. Gruppo 11, rappresentante unico.

**Effetti attivi**: nessuno oltre all'accordion standard.

**Perché è costruita così**: la domanda "Quanto costa?" è presente qui esattamente come nelle FAQ di
apsales.eu (report gemello del modello di forma, Tavola 12) — confermando che affrontare di petto
l'obiezione sul prezzo dentro una FAQ è un pattern trasversale a tutto l'ecosistema Digital Empire
studiato finora, non solo di Andrei Pascu.

**Riepilogo pagina**: media totale = **32**, parole totali = **855**, blocchi_testo totale = **242**,
CTA totale = **33** (il totale CTA più alto di tutte e sei le pagine di questo studio, quasi
interamente dovuto alle 18 CTA della Tavola M4 e alle 8 della Tavola M5 — due sezioni-accordion
"pesanti di trigger" più di qualunque altra pagina). Nessun blocco "div-border" muto: come la Home,
anche il Manuale non usa il componente divisore-vuoto, a differenza delle due pagine da 98€
(outFunnel e outHeadline).

---

## Nota di raccordo con il report gemello (le tre pagine grandi)

Tre osservazioni valgono su entrambi gli atlanti e vanno lette insieme:

1. **Il difetto "div-border muto" è confermato in tutte e sei le pagine che usano quel componente**
   (outFunnel, outHeadline, Copywriting Mentorship) — mai in quelle che non lo usano (Home, Manuale,
   Funnel Operator ha zero div-border). È quindi legato al componente stesso, non al prezzo o al tipo
   di pagina.
2. **Il colore di accento della card-prezzo finale segue la fascia, non il singolo prodotto**: verde
   per i due prodotti da 98€ (outFunnel, outHeadline — CTA finali quasi identiche al pixel), blu per
   Funnel Operator (434€), oro per Copywriting Mentorship (999€, unico con pricing a due tier).
3. **La barra di cattura "Claude Speedrun / Accedi"** appare sia sulla Home sia su outFunnel: è un
   artefatto trasversale del capture tool, non legato a una pagina specifica — va scartato ovunque
   ricompaia.

---

## DELTA ALLA FABBRICA

**CANONE**: una pagina-directory a basso impegno (come la Home, 0€, 5 sezioni) non ha bisogno di
componenti-divisore vuoti né di curriculum espansi — la sua unica responsabilità è instradare in meno
di 4 blocchi (hero, hub risorse, hub blog, prova personale) prima del footer; aggiungere sezioni oltre
questo schema è friction, non valore.

**PATTERN**: quando due prodotti condividono lo stesso prezzo nello stesso ecosistema (qui: outFunnel e
outHeadline, entrambi 98€), la Fabbrica può aspettarsi — ed è lecito replicare — lo stesso template di
apertura tematica (hero rosso/teal ma stessa struttura a hero+player video) e lo stesso template di
chiusura-vendita (stessa frase, stesso colore verde, stessa card prezzo): il riuso di componente per
fascia di prezzo è una scelta editoriale efficiente, non un difetto da correggere.

**GATE**: prima di dichiarare una sezione "priva di CTA" o "a bassa interattività" dal solo conteggio
`cta` di `scheda.json`, verificare se la sezione è un accordion (dove ogni riga è tecnicamente una CTA)
— la Tavola M4 di questo atlante (18 CTA) e la Tavola HL3 (7 CTA) dimostrano che un curriculum/indice
ben scomposto può avere più punti di interazione di una sezione di vendita esplicita; il conteggio da
solo, senza aprire lo screenshot, porta a leggere come "pagina di vendita aggressiva" quello che è
semplicemente un indice cliccabile.
