---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #apsales #costruzione #cro-agency #fabbrica-siti #react #tanstack-start
Created: 2026-09-07
Last updated: 2026-09-07
---

# 18-20 — apsales.eu — Servizi, Landing Page, Consulenza: LA COSTRUZIONE

Terzo giro di studio su `apsales.eu`, il concorrente diretto. I rapporti
[13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) e [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) hanno
già misurato stack (React + TanStack Start), i sei token `--brand-*` e la pagina radice (14 sezioni). Questo
rapporto studia **come sono costruite le tre pagine di servizio** — `/servizi` (5 sezioni, 4229px), `/landing-page`
(17 sezioni, 16.039px), `/consulenza` (15 sezioni, 16.832px) — dai file serviti in `capture/18-apsales-servizi/`,
`capture/19-apsales-landing-page/`, `capture/20-apsales-consulenza/`. Non ripete copy, palette o token già
acquisiti: guarda componenti, effetti, misure tipografiche e la verità sul footer. Il copy delle tre pagine è
oggetto di uno studio parallelo (agente `copy-apsales`), non duplicato qui.

Fonti primarie per ogni numero: `scheda.json` (misurato dal DOM reale), `design-tokens.json` (stesso dato,
schema rinominato — usato solo per incrociare), `src/_INDICE.json` (mappa dei file scaricati) e i file sorgente
in `src/*.js`/`src/*.css` aperti uno per uno. Ogni cifra qui sotto dichiara il campo e il file da cui viene.

---

## DELTA ALLA FABBRICA

**CANONE — l'architettura "un solo kit condiviso, mai reinventato per pagina".** Aprendo `06-servizi-IDBk2DyL.js`
si vede che il componente di pagina non definisce quasi nessuno stile proprio: importa da
`RevealFooter-B34lvwld.js` undici export condivisi — un `Section` che accetta una prop `tone` (`void`/`pitch`/
`paper`, misurato dall'uso `tone:"pitch"` / `tone:"void"` nel codice, coerente con le classi `bg-pitch`/`bg-void`
lette in `scheda.json`), un componente Heading, un Deck/sottotitolo, una Card, due varianti di Button (primario
pieno blu, secondario fantasma), due varianti di testo-evidenziato (`<em class="font-bolder italic">` e un mark
colorato), e il Footer stesso. **Tre pagine diverse, zero stili inventati sul posto**: ogni sezione nuova nasce
dentro un vincolo tipografico e cromatico che non permette la deriva. Questo entra nel canone della Fabbrica
Siti: un unico modulo "kit" (Section-con-tono, Heading, Deck, Card, Button×2, Highlight×2) importato da ogni
pagina, mai una sezione che scrive `className` di sfondo/colore a mano.

**PATTERN — due strumenti interattivi data-driven, non decorativi.** Il calcolatore ROI di `/landing-page`
(sezione `#calcolo`, "Fai due conti.") e il selettore diagnostico di `/consulenza` (sezione `#vincolo`) sono
entrambi costruiti sullo stesso principio: uno stato React minimo (2 input o 1 indice selezionato) che pilota un
output leggibile subito, con l'assunzione dichiarata in chiaro invece che nascosta. Il secondo, in particolare,
usa una struttura dati pulita — `{title, steps:[...], constraint:<indice>, effect:"..."}` — che è la Teoria dei
Vincoli resa componente. Pattern riusabile per le pagine di servizio della Fabbrica: non un elenco statico di
bullet, ma un piccolo motore che qualifica il visitatore mentre gli mostra qualcosa.

**GATE — due controlli nuovi, nati da difetti misurati qui (vedi §I DIFETTI):** (1) *coerenza og:image* — prima
di pubblicare N pagine, verificare che l'URL di `og_image` non sia identico su più pagine con `meta.description`
diverso (qui lo è su tutte e tre, byte per byte); (2) *onestà dell'input* — se una sezione mostra due campi
editabili, il gate deve verificare che entrambi entrino nel calcolo mostrato, o che la UI dichiari esplicitamente
quale dei due è solo di contesto.

---

## I COMPONENTI

Otto file sorgente ricorrono nelle tre cattive con lo stesso hash in ogni cartella dove compaiono — prova che è
lo stesso bundle servito da build unica, non tre pagine scritte a sé:

| Componente | Peso (bytes, da `_INDICE.json`) | Dove compare (delle 3 pagine) | Cosa fa, misurato |
|---|---|---|---|
| `Ascii` | 706 | servizi, landing-page (non in consulenza — nessuna illustrazione ASCII in quella pagina) | wrapper immagine unico: `mix-blend-screen` + `[filter:contrast(1.3)_brightness(1.45)]`, identico al dossier 13 |
| `RevealFooter` | 47.460 — il file più pesante fra i componenti nominati | tutte e tre, identico byte per byte | non è solo il footer: è il **kit UI condiviso** (vedi CANONE) più il footer a tenda più un motore a canvas (vedi sotto) |
| `StickyCta` | 1.689 | tutte e tre, identico | CTA fissa in basso a destra, appare oltre il 90% di `innerHeight` scrollato; legge `[data-blend-surface]` per il trucco del doppio bottone (dossier 13 §3) |
| `CallDialog` | 6.063 | **solo `/landing-page`** | l'unica delle tre pagine con un modal di prenotazione-chiamata: `/servizi` rimanda con link, `/consulenza` vende direttamente (bottone di pagamento, non un dialog) |
| `accordion` | 9.211 | **solo `/consulenza`** (non in servizi, non in landing-page) | wrapper Radix Collapsible/Accordion — vedi discrepanza FAQ sotto |
| `dialog` | 35.358 — il secondo più pesante | landing-page, consulenza (non servizi) | **non è il popup**: è il chunk di utility Radix condivise (Presence, `composeRefs`, `createContextScope`, icone lucide come `chevron-down`) usato sia da `CallDialog` sia da `accordion` |
| `forms.functions` | 589 | landing-page, consulenza (non servizi — coerente: `/servizi` non ha form) | 5 riferimenti a server function (`createServerFn({method:"POST"}).handler(hash)`), stesso pattern del dossier 13 |
| `useServerFn` | 368 | landing-page, consulenza (non servizi) | hook TanStack Start che invoca la server function e gestisce il redirect via router |

**Perché la presenza/assenza conta più del contenuto.** Nessuno dei tre file `_INDICE.json` include componenti a
caso: `/servizi` non carica né `dialog` né `forms.functions` né `useServerFn` perché non ha nessun form —
solo link verso le altre due pagine. `/consulenza` non carica `CallDialog` perché non propone "prenota una
chiamata conoscitiva gratuita": vende direttamente l'ora a pagamento (`"Paga, poi scegli data e ora →"`,
misurato in `cta[]` di `20-apsales-consulenza/scheda.json`, y=10862, bg blu). Il code-splitting rispecchia
esattamente l'intento commerciale di ogni pagina — un dato di architettura, non un'osservazione di superficie.

### CallDialog, in dettaglio (letto per intero, 6.063 byte)

Il modal ha cinque campi (nome, email, azienda opzionale, argomento opzionale con `maxLength=400`, e una scelta
di fascia oraria a chip: `Mattina` / `Pomeriggio` / `Sono flessibile`), validazione client con regex email e
nome ≥2 caratteri, tre stati (`idle`/`sending`/`done`), messaggio di rate-limit esplicito ("Hai già inviato
diverse richieste. Riprova tra un'ora o scrivici via email.") catturato via `/troppe richieste/i` sul testo
d'errore della server function. Lo stato `done` mostra un segno di spunta in un riquadro **quadrato bordato blu,
senza `rounded`** — coerente con la disciplina "zero raggi" del brand anche dentro un componente che nessuno
screenshot della pagina intera cattura mai (il modal si apre solo al click). Le chip di fascia oraria non hanno
`rounded` nemmeno loro: bottoni sempre spigolosi, in ogni stato del sito.

### RevealFooter, in dettaglio — il file che nasconde un motore a canvas

Oltre al kit UI e al footer (vedi sezione dedicata "LA VERITÀ SU RevealFooter" più sotto), il file contiene un
**componente canvas separato dal semplice logo SVG**. Il sito ha due modi di mostrare il wordmark "APsales":

1. Un SVG statico (`viewBox="0 0 1058.96 1055.74"`, `fill="currentColor"`, path a poligoni) — la versione
   leggera, colorata via classe (`text-blue`), usata in nav/header/modal.
2. Un **canvas interattivo** nello stesso file: crea un canvas offscreen, carica un'immagine (`new Image` con
   `crossOrigin`), ne legge i pixel con `getImageData`, calcola la **luminanza** per pixel con la formula
   standard `0.2126·R + 0.7152·G + 0.0722·B` e l'alpha (`W[t+3]/255`), e usa quei due valori per pilotare un
   sistema di particelle (`Float32Array`, `Map` per i nodi, palette `#a9c6ff`/`#ffffff`). È **interattivo al
   puntatore** (`onPointerLeave`, `targetX`/`targetY` in un ref), **rispetta `prefers-reduced-motion`**
   esplicitamente (`matchMedia('(prefers-reduced-motion: reduce)')`), ed è **retina-aware**
   (`devicePixelRatio`, clampato a 2, con `ResizeObserver` per il resize).

Questo risolve — con più dettaglio di quanto il dossier 13 potesse dire — l'enigma dei filtri `url("#luma-alpha")`
mai trovati nei chunk: non erano filtri SVG mancanti, erano il nome descrittivo (probabile classe Tailwind
arbitraria) di **questo stesso principio (luminanza→alpha) implementato in JavaScript su canvas**, non come
filtro CSS. Non affermo che siano lo stesso identico codice — il file `url("#luma-alpha")` resta non risolto nei
chunk — ma la tecnica concettuale (luminanza del pixel → intensità dell'effetto) è ora osservata e misurata
altrove nello stesso sito, nello stesso file component.

### accordion — usato solo su una pagina su tre, con conseguenza diretta sulla FAQ

`accordion-LU6_yz4t.js` (9.211 B) implementa Radix Collapsible/Accordion completo: chevron che ruota 180°
(`[&[data-state=open]>svg]:rotate-180`), altezza animata via `@keyframes accordion-down{0%{height:0}to{height:
var(--radix-accordion-content-height,var(--bits-accordion-content-height,...))}}` — la catena di variabili CSS
di fallback (`--radix-`, `--bits-`, `--reka-`, `--kb-`, `--ngp-accordion-content-height`) rivela che il plugin di
animazione Tailwind in uso è generico multi-libreria (compatibile con Radix, Bits UI, Reka UI, Kobalte...), non
scritto a mano per questo progetto — un dettaglio di build, non di design. Timing di default:
`animation:accordion-down var(--tw-animation-duration,var(--tw-duration,.2s)) var(--tw-ease,ease-out)`, cioè
**0,2s ease-out** salvo override.

Ma questo componente **non è caricato su `/landing-page`** (assente da `19-apsales-landing-page/src/_INDICE.json`).
Eppure anche `/landing-page` ha una sezione "Domande frequenti." (i=15, id `faq`). Misurato in `scheda.json`:
quella sezione ha **`blocchi_testo: 1`** e **182 parole** — un solo blocco di testo, non 7-14 righe cliccabili
come sul resto del sito. Conclusione misurata: la FAQ di `/landing-page` **non è un accordion interattivo**, è
contenuto statico (quasi certamente reso visibile solo tramite lo schema `FAQPage` in JSON-LD, misurato nello
stesso `meta.jsonld[]`, per la SEO, senza controparte visiva espandibile). Su `/consulenza`, invece, la stessa
sezione (i=13, id `faq`) ha **14 media e 14 CTA** — una riga cliccabile per ciascuna delle 14 domande, ognuna
`33.9997px/w600` (i "34px grassetto" misurati nella scala tipografica). **Due implementazioni diverse della
stessa componente di prodotto (FAQ) sulla stessa build**, non un'unica scelta di design applicata ovunque.

### forms.functions e useServerFn — confermano, non aggiungono

Stesso pattern del dossier 13: `createServerFn({method:"POST"}).handler(hash)` × 5 riferimenti in
`forms.functions-DiYx6QCP.js` (589 B), e `useServerFn-C9O_qu9A.js` (368 B) che avvolge la chiamata con gestione
del redirect via `t.stores.location.get()` / `t.navigate(t.resolveRedirect(e).options)`. Nessuna novità rispetto
a quanto già misurato; li elenco per completezza dell'inventario degli otto componenti richiesti.

---

## LO SCHEMA DELLE TRE PAGINE

Tabelle costruite da `sezioni[]` di ogni `scheda.json`. Colonna "ruolo" è descrittiva/interpretativa dove non
c'è un `id`/heading esplicito — dichiarato come "probabile" quando dedotto solo da densità di parole o posizione.

### `/servizi` — 4229px, 5 sezioni, **4 firme distinte** (i=1 e i=4 condividono la stessa firma di layout)

| i | y / h | bg | heading / id | blocchi / parole | media | cta | ruolo |
|---|---|---|---|---|---|---|---|
| 1 | 65 / 684 | void | "Facciamo solo due cose. Per scelta." | 11 / 39 | 0 | 2 | hero, posizionamento per restrizione di scopo |
| 2 | 749 / 845 | pitch, id `landing` | "Landing page." | 11 / 67 | 1 | 1 | dettaglio servizio 1: 25 giorni, prezzo su preventivo |
| 3 | 1594 / 813 | void, id `consulenza` | "Consulenza." | 22 / 70 | 0 | 1 | dettaglio servizio 2: €610, cosa resta al cliente |
| 4 | 2407 / 640 | void, id `parti` | "Dove stai perdendo conversioni?" | 6 / 27 | 0 | 2 | bivio finale — stessa firma di i=1 (`rappresentante:false`) |
| 5 | 3048 / 1182 | transparent | — (footer) | 19 / 32 | 1 | 0 | footer |

### `/landing-page` — 16.039px, 17 sezioni, **17 firme distinte (100% uniche)**

| i | y / h | bg | heading / id | blocchi / parole | cta | ruolo |
|---|---|---|---|---|---|---|
| 1 | 65/885 | void | "Il traffico lo paghi con le ads. Ma poi il tuo sito lo perde." | 9/55 | 2 | hero, doppia CTA (rifare / calcolare) |
| 2 | 950/393 | pitch | — | 1/29 | 0 | probabile riga di qualificazione cliente (bassa densità) |
| 3 | 1343/692 | void | — | 6/18 | 0 | transizione |
| 4 | 2035/609 | pitch | "Il nostro lavoro è aumentare quante persone comprano." | 4/53 | 0 | posizionamento di servizio |
| 5 | 2644/756 | void | — | 6/23 | 0 | lead-in al calcolatore |
| 6 | 3400/805 | pitch, id `calcolo` | "Fai due conti." | 9/43 | 0 | **calcolatrice ROI interattiva** (vedi sotto) |
| 7 | 4205/402 | void | — | 3/5 | 0 | separatore minimale |
| 8 | 4607/1192 | pitch | "Come lavoriamo." + 5 sotto-step | 21/82 | 0 | processo in 5 fasi (tracciamento→conversioni) |
| 9 | 5799/1019 | **paper** (unica chiara), id `offerta` | "Cosa facciamo." | 16/72 | 1 | dettaglio offerta landing page |
| 10 | 6818/796 | void, id `contatto` | "Parla con AP Sales subito." | 8/24 | 4 | form di qualificazione (B2B/SaaS/Altro) + invio |
| 11 | 7614/980 | pitch | "AP Sales, o un'altra agenzia?" | 35/73 | 0 | confronto competitivo |
| 12 | 8594/2000 | void | "Cosa succede dopo che ci contatti." + 5 sotto-step (di 10 totali in heading) | 59/157 | 0 | timeline dal contatto alla consegna — sezione più alta della pagina (2000px) |
| 13 | 10594/1170 | pitch | "Tecniche sostenibili." White Hat/Black Hat | 29/96 | 0 | disclosure etica |
| 14 | 11764/900 | void | "Hai un buon prodotto. Noi influenziamo la percezione." | 12/49 | 0 | manifesto |
| 15 | 12664/1615 | pitch, id `faq` | "Domande frequenti." | **1**/182 | 0 | FAQ **non interattiva** (vedi §accordion) |
| 16 | 14279/579 | void | "Fai convertire il tuo traffico." | 4/9 | 1 | CTA finale |
| 17 | 14858/1182 | transparent | — (footer) | 19/32 | 0 | footer |

### `/consulenza` — 16.832px, 15 sezioni, **14 firme distinte** (i=5 e i=8 condividono firma)

| i | y / h | bg | heading / id | blocchi / parole | cta | ruolo |
|---|---|---|---|---|---|---|
| 1 | 65/1005 | void | "Consulenza di problem solving con Andrei Pascu" | 8/48 | 1 | hero, 1 media (`knight.webp`) |
| 2 | 1070/644 | pitch, id `processo` | "Qualsiasi cosa tu faccia… Hai un processo." | 23/13 | 0 | probabile diagramma dei 5 step (bassa densità parole) |
| 3 | 1714/1155 | void, id `vincolo` | "E ogni processo ha un limite che gli impedisce di crescere." | 44/95 | **6** | **selettore diagnostico** (Funnel/Ads/Content/Onboarding/Retention/Referral) |
| 4 | 2869/1233 | **paper**, id `andrei` | "Ma chi è Andrei Pascu?" | 10/65 | 0 | bio fondatore, 1 media (`andrei-consulenza.webp`) |
| 5 | 4102/1695 | void, id `sblocco` | "Scopri e/o rimuovi il tuo vincolo." | 19/184 | 0 | sezione più densa di parole della pagina |
| 6 | 5797/1022 | void, id `diagnosi` | "I soldi si bloccano in uno di questi punti." | 27/72 | **4** | selettore sintomi (marketing/vendita/team/decisione) |
| 7 | 6819/1323 | pitch, id `contesto` | "Nel 2024 ci sono stati 4,1 milioni di dichiaranti IVA in Italia." | 8/98 | 0 | statistica shock, probabile numero gigante (vedi §LE MISURE) |
| 8 | 8142/1531 | void | — | 9/147 | 0 | continuazione di "sblocco" (stessa firma di i=5) |
| 9 | 9673/644 | void, id `disponibilita` | — | 8/17 | 1 | probabile widget disponibilità/calendario |
| 10 | 10316/839 | **paper**, id `offerta` | "Consulenza con Andrei Pascu." | 17/52 | 1 | offerta finale, prezzo |
| 11 | 11155/847 | void | "Cosa succede dopo il pagamento." | 18/34 | 0 | timeline post-acquisto |
| 12 | 12003/1097 | pitch, id `confronto` | "Andrei Pascu vs consulente medio." | 20/88 | 0 | tabella comparativa |
| 13 | 13100/1856 | void, id `faq` | "Quello che chiedono prima di pagare." | 29/95 | **14** | FAQ **esplosa** (14 righe cliccabili, vedi §accordion) |
| 14 | 14956/694 | void | "Sblocca il vincolo. Ottieni il tuo piano." | 7/15 | 1 | CTA finale |
| 15 | 15650/1182 | transparent | — (footer) | 19/32 | 0 | footer |

**Osservazione di struttura:** `/consulenza` ha 31 CTA totali su 15 sezioni (media 2,1 per sezione) contro le 9
di `/servizi` su 5 sezioni (1,8) e le 11 di `/landing-page` su 17 (0,65) — la pagina che vende direttamente
(`/consulenza`, pagamento immediato) è quella con più punti di decisione cliccabili per sezione, mentre la
pagina più lunga (`/landing-page`, che punta a portare a una chiamata) dilaziona le CTA lungo un percorso più
lento. Coerente con l'intento commerciale di ciascuna, non un caso.

---

## GLI EFFETTI

Tutti e tre i fogli `styles-CHG2jDaU.css` pesano **esattamente 127.394 byte** (misurato in ogni `_INDICE.json`),
identici a quello del dossier 13: è **un unico foglio Tailwind globale per l'intero sito**, non compilato per
pagina. Le 13 maschere `mask-image` e i sei token `--brand-*` già misurati nel dossier 13 valgono quindi
identici anche qui — non li rimisuro. Ciò che è **nuovo** in queste tre catture:

**Due classi utility non ancora documentate**, trovate leggendo `06-servizi-IDBk2DyL.js` e verificate in CSS:
```
.bg-dotfield  { background-image: radial-gradient(circle, #f9f9f921 .5px, #0000 .5px); background-size: 22px 22px }
.bg-hairgrid  { background-image: linear-gradient(90deg, #f9f9f90b 1px, #0000 1px),
                                  linear-gradient(#f9f9f90b 1px, #0000 1px); background-size: 64px 64px }
```
`bg-dotfield` è un campo di puntini bianchi al 13% di opacità (`#f9f9f9` = `--brand-paper`, canale alpha `21`
esadecimale ≈ 13%) ogni 22px — usato nell'hero e nel finale di `/servizi`, sempre dentro una maschera
`mask-image:linear-gradient(...)` che lo dissolve verso l'alto o il basso (misurato nello stesso file:
`[mask-image:linear-gradient(to_bottom,black,transparent_80%)]` sull'hero, `to_top` sul finale). `bg-hairgrid` è
una griglia di linee sottilissime (8% di opacità) ogni 64px, usata dietro l'illustrazione `laptop.webp` nella
card "Landing page" — un dettaglio texture-su-texture (ASCII sopra hairgrid sopra bg-void) che nessuno dei due
dossier precedenti aveva nominato perché non compariva nella pagina radice.

**Le nove `@keyframes` sono le stesse del dossier 13** (stesso foglio CSS), ma qui per la prima volta si leggono
per intero le definizioni di tre di esse, prima solo elencate per nome:
```
@keyframes node-in      { 0% { opacity:0; transform:translateY(6px) }  to { opacity:1; transform:none } }
@keyframes rail-marquee { 0% { transform:translate(0) }                to { transform:translate(-50%) } }
@keyframes accordion-down { 0% { height:0 }  to { height:var(--radix-accordion-content-height,
                            var(--bits-accordion-content-height, var(--reka-accordion-content-height,
                            var(--kb-accordion-content-height, var(--ngp-accordion-content-height, auto))))) } }
```
`node-in` (misurata in uso su `/consulenza`: **9 elementi, 0,42s, `cubic-bezier(0.16,1,0.3,1)`** — una curva ad
"overshoot" morbido, non un semplice ease-out) è un fade-up di 6px — probabile animazione d'ingresso scaglionata
sui 5 step del funnel in sezione `#processo` e/o sui 4 sintomi in `#diagnosi` (9 elementi totali è compatibile
con 5+4). `rail-marquee` è un secondo meccanismo di scorrimento infinito oltre a `logo-marquee` (dossier 13,
40s linear) — **non osservato attivo su nessuna delle tre pagine studiate qui** (il campo `animazioni` di
`servizi` e `landing-page` è vuoto in `scheda.json`; solo `node-in` compare, e solo su `/consulenza`), quindi la
fila di loghi cliente e qualunque rail secondario sembrano **esclusivi della pagina radice**, non ripetuti sulle
pagine di servizio.

**Accessibilità del movimento, misurata nel CSS stesso:**
```
@media (prefers-reduced-motion: reduce) {
  .animate-node-in, .animate-rail-marquee, .animate-logo-marquee { animation: none !important }
}
```
Le tre animazioni custom (non le utility generiche Tailwind `enter`/`exit`/`pulse`/`caret-blink`) sono
esplicitamente disattivate per chi ha impostato "riduci movimento" nel sistema operativo — stesso principio già
visto nel motore a canvas di `RevealFooter` (`matchMedia('(prefers-reduced-motion: reduce)')`). È un impegno
sistematico, non un caso isolato: **da adottare come gate**, non solo come pattern, nella Fabbrica Siti.

**Filtri, blend, clip — confermati, con una terza intensità.** `contrast(1.3) brightness(1.45)` (servizi,
landing-page) e **`contrast(1.35) brightness(1.5)`** (consulenza, misurato in `effetti.filtri` del suo
`scheda.json`) — una scala di boost leggermente più forte su questa pagina, coerente con la nota già scritta nel
dossier 13 ("almeno tre livelli di intensità dello stesso trucco"), qui confermata con un quarto punto dati.
`backdrop: blur(12px)` ricorre identico su tutte e tre — l'overlay del modal/menu mobile. `blend: screen` (1
uso rilevato per pagina, lo stesso componente `Ascii`) e `clip: inset(0px)` / `inset(50%)` identici al dossier
13 (`sr-only` e la tenda del footer).

---

## LE MISURE

### Scala tipografica — le taglie che ricorrono di più, per pagina (fonte: `scala_tipografica` di ogni `scheda.json`)

| Pagina | Corpo testo dominante | Titoli H2 | H1 | Cifra/numero gigante unico |
|---|---|---|---|---|
| `/servizi` | 15px/w400 ×17 | 60px/w600 ×3 + w900 ×2 | 80px/w600 ×4 + w900 ×2 | — nessuna taglia oltre 80px |
| `/landing-page` | 17px/w400 ×45, 15px/w400 ×36 | 60px/w600 ×15 | 80px/w600 ×3 | **112px/w800 ×1** (uso singolo, non identificato con certezza dal solo codice) |
| `/consulenza` | 17px/w400 ×36, 15px/w400 ×29 | 60px/w600 ×14 | 80px/w600 ×4 | **256px/w800 ×1, 112px/w700 ×1, 112px/w600 ×1** — tre momenti tipografici giganti distinti |

`/consulenza` è misurabilmente la pagina più "drammatica" tipograficamente: tre taglie sopra i 110px contro
l'unica di `/landing-page` e nessuna di `/servizi`. La sezione a più bassa densità di parole della pagina (i=7,
"Nel 2024 ci sono stati 4,1 milioni di dichiaranti IVA in Italia.", 8 blocchi/98 parole su 1323px di altezza) è
la candidata più plausibile per il 256px, ma **non è verificabile con certezza dal solo codice sorgente
scaricato** — lo dichiaro come inferenza, non come misura diretta.

### Pesi — la stessa gerarchia dovunque

| Peso | `/servizi` | `/landing-page` | `/consulenza` |
|---|---|---|---|
| 400 | 23 | 92 | 98 |
| 500 | 19 | 54 | 35 |
| 600 | 8 | 30 | 43 |
| 700 | 4 | 33 | 13 |
| 900 | 4 | 5 | 8 |
| 800 | — | 4 | 1 |

Il 400 domina ovunque (corpo testo), il 900 resta raro e riservato (enfasi massima, coerente col dossier 13). Il
rapporto 600/700 si inverte fra `/landing-page` (30 vs 33, il 700 leggermente più usato — compatibile con le 28
occorrenze di "25px/w700" misurate, probabile stile delle citazioni/quote nella sezione confronto) e
`/consulenza` (43 vs 13, il 600 nettamente più usato — compatibile con le 18 occorrenze di "34px/w600" delle
domande FAQ).

### Colori di sfondo — il blu resta unico colore d'azione, confermato una terza e quarta volta

| Sfondo (HEX, dossier 13) | `/servizi` | `/landing-page` | `/consulenza` |
|---|---|---|---|
| `#0a0a0b` (void) | 5 | 12 | 17 |
| `#0062ff` (blue) | 5 | 12 | 14 |
| `#111111` (pitch) | 2 | 12 | 7 |
| `#f9f9f9` (paper) | 1 | 2 | 3 |

Nessun quinto colore di sfondo compare mai in nessuna delle tre pagine: la disciplina cromatica del dossier 13
(tre neutri + un solo accento) regge su tre capture aggiuntive, non solo sulla home.

### Raggi — la scoperta più netta di questo giro di studio

| Pagina | `raggi` misurato (`scheda.json`) |
|---|---|
| `/servizi` | **`[]` — zero, nessun elemento arrotondato, nemmeno lo `50%` dei 2 elementi del dossier 13** |
| `/landing-page` | `3.35544e7px` (= `rounded-full` calcolato) ×14, `8px` ×1 |
| `/consulenza` | `3.35544e7px` ×20, `8px` ×3 |

Il dossier 13 aveva scritto "ancora zero raggi, tranne 50% su 2 elementi" parlando della sola pagina radice.
Qui si vede che la regola **non è uniforme sul sito**: `/servizi` è ancora più rigida della home (zero assoluto),
ma `/landing-page` e `/consulenza` misurano 14-23 elementi con raggio pieno (`rounded-full`) o smussato (8px).
Ho controllato ogni bottone e chip letto nel codice sorgente di queste pagine (CTA, chip orario di `CallDialog`,
righe del selettore vincolo/sintomi, checkmark di conferma): **nessuno dichiara `rounded-*` nelle classi
Tailwind lette**. Non riesco quindi ad attribuire con certezza questi 14-23 conteggi a un elemento visibile
preciso dagli 8 file sorgente aperti — è plausibile che vengano da controlli nativi del browser (radio/range non
ancora incontrati nel codice letto) o da un componente non incluso in questi file. **Lo dichiaro come dato
misurato ma di origine non identificata**, non come stima.

---

## LA VERITÀ SU RevealFooter

Il dossier 13 aveva lasciato aperta una domanda: il componente dichiara `bg-blue` su un layer `fixed` dentro un
contenitore con `clipPath:inset(0)`, ma lo screenshot della pagina radice mostra fondo quasi nero con solo il
wordmark blu. Qui, con lo stesso file (`RevealFooter-B34lvwld.js`, identico su tutte e tre le nuove catture) letto
riga per riga, la risposta è **misurabile e non è un bug di cattura**:

```
<footer aria-label="Footer" className="relative">
  <div className="relative pt-24 md:pt-32">
    <Wordmark className="mx-auto -mb-px block w-[min(54vw,1040px)] translate-y-[6.5%] text-blue" />
  </div>
  <div data-blend-surface style={{ clipPath: "inset(0)" }} className="relative h-screen min-h-[720px]">
    <div className="fixed bottom-0 left-0 h-screen min-h-[720px] w-full overflow-hidden bg-blue text-white">
      <span className="sr-only">AP Sales</span>
      ...
    </div>
  </div>
</footer>
```

Sono **due elementi separati**, non uno:

1. Il wordmark "APsales" (colorato `text-blue`) sta in un `<div>` normale, in flusso, **sopra** il pannello
   `bg-blue` — è sempre visibile, a prescindere dallo scroll. È questo che lo screenshot cattura.
2. Il pannello `bg-blue` **esiste davvero** ed è `position:fixed` — ma è avvolto da un contenitore
   `clipPath:inset(0)` alto **un intero viewport** (`h-screen`). Per un elemento `fixed`, un ancestor con
   `clip-path` (non `overflow`) ritaglia visivamente il figlio al proprio riquadro pur senza diventarne
   containing block di posizionamento — è la tecnica nota come "sticky reveal footer": il pannello blu resta
   agganciato al viewport, ma è visibile solo per la porzione che rientra nel riquadro dell'ancestor via via che
   la pagina scorre oltre quel riquadro.

Trovato anche il calcolo che pilota la progressione, nello stesso file:
```js
a = 1 - element.getBoundingClientRect().top / window.innerHeight   // 0 quando il contenitore entra dal basso,
                                                                     // →1 quando il suo top tocca la cima del viewport
opacity = clamp((a - 0.3) / 0.5, 0, 1)                              // fade-in ritardato di un layer aggiuntivo
u = max(0, offsetHeight - 64)                                       // 64px = altezza della nav fissa, sottratta
```

**Conclusione misurata: non è una discrepanza fra codice e screenshot, è una singola cattura statica di
un'animazione legata allo scroll.** Il pannello blu si "svela" progressivamente mentre l'utente scorre oltre il
contenitore alto un intero viewport; uno script di cattura automatica che scrolla la sezione all'inizio del suo
riquadro (comportamento tipico di un tool "una schermata per sezione") fotografa quasi certamente il fotogramma
`a≈0`, cioè **prima** che il pannello si sia rivelato — esattamente lo stato "nero con solo il wordmark" misurato
in tutti e quattro gli screenshot del footer raccolti finora (dossier 13 più queste tre). Non ho eseguito uno
scroll reale in un browser per fotografare il fotogramma `a≈1`: la certezza qui è sulla **logica del codice**
(letta per intero, non dedotta), non su un pixel osservato a pannello rivelato — ma la logica non lascia margini
di ambiguità su come il componente sia *progettato* per comportarsi.

---

## I DIFETTI

1. **Il calcolatore ROI di `/landing-page` ha un campo che non entra nel calcolo mostrato.** Letto per intero in
   `09-landing-page-CRAikniJ.js`: due input, "Spesa ads mensile (€)" (default 3000) e "Acquisti al mese"
   (default 60). L'output (`+N acquisti extra al mese`, in blu, taglia grande) è calcolato come
   `Math.round(Number(acquisti) * 0.5)` — **dipende solo dal secondo campo**. Il primo campo (spesa ads) è
   stato in React valido (`useState`) ma non compare in nessun punto della formula. Sotto, in corpo piccolo, il
   sito lo dichiara: *"Assunzione: conversion rate 2,75% → 4,13% (+50%), stesso budget."* — quindi non è
   inganno (l'assunzione a budget costante è dichiarata), ma **visivamente i due campi hanno lo stesso peso
   grafico**, e solo leggendo la nota in piccolo si capisce che uno dei due è decorativo/di contesto. Difetto
   reale, misurato nel codice, non nello screenshot.

2. **`og_image` identica, byte per byte, su tre pagine con scopi diversi.** `meta.og_image` di `/servizi`,
   `/landing-page` e `/consulenza` è **la stessa identica URL**:
   `.../id-preview-9bb40a2b--7478fc2d-006d-4669-95bd-7b45e31d5956.lovable.app-1787155303721.png` — un nome file
   che contiene letteralmente `lovable.app`, la piattaforma di generazione AI di siti, verosimilmente uno
   screenshot di anteprima mai sostituito con un'immagine social dedicata. Chi condivide il link di
   `/consulenza` (€610, prodotto specifico) su LinkedIn vede la stessa anteprima generica di chi condivide
   `/servizi`. Difetto di rifinitura concreto, verificabile confrontando tre stringhe.

3. **Due implementazioni diverse della stessa componente FAQ sulla stessa build.** Già descritto sopra
   (§accordion): `/landing-page` mostra le FAQ come blocco statico (`blocchi_testo:1`, presumibilmente solo
   via JSON-LD), `/consulenza` le mostra come 14 righe cliccabili con l'accordion Radix vero. Non è un
   'progressive enhancement' dichiarato: è un'incoerenza di componente fra due pagine dello stesso sito.

4. **La disciplina "zero raggi" non è applicata in modo uniforme.** `/servizi` misura zero elementi arrotondati
   (`raggi: []`), mentre `/landing-page` e `/consulenza` ne misurano 14-23 (vedi §LE MISURE) di origine non
   identificabile dal codice letto. O è una scelta di design non documentata da nessuna parte nel CSS ispezionato,
   o sono elementi nativi del browser mai stilizzati — in entrambi i casi è un'incoerenza fra pagine dello stesso
   sito, non una regola applicata con disciplina uniforme come il dossier 13 lasciava supporre guardando solo
   la home.

Non ripeto qui il difetto di contrasto testo/sfondo già calcolato e misurato nel dossier 13 (testo a opacità
`.4`/`.5`/`.55`/`.6` su fondo quasi nero): le tre nuove `palette_testo` confermano lo stesso pattern (es.
`/consulenza`: `oklab(0.9821 0 0 / 0.4)` ×11, `/0.55` ×11, `/0.45` ×9) — stesso difetto, stessa causa, niente di
nuovo da aggiungere oltre alla conferma numerica.

---

## Connessioni

- [08-apsales.md](08-apsales.md) — il primo passaggio sulla home: copy, palette, struttura
- [13-apsales-STACK-E-TOKEN.md](13-apsales-STACK-E-TOKEN.md) — stack, token OKLCH→HEX, il primo inventario componenti
- [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) — la tavola per sezione della pagina radice, stesso formato di lettura
- `.claude/skills/fabbrica-siti/canone/canone.css` — dove va il pattern "Section con tono" del §DELTA ALLA FABBRICA, se confermato in produzione
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
