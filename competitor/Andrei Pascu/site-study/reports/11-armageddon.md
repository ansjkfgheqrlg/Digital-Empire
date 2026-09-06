---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #site-study #landing-page #lancio #design-system
Created: 2026-09-06
Last updated: 2026-09-06
---

# 11 — armageddon.bsns.it — la pagina di lancio

**URL:** `https://armageddon.bsns.it/`
**Catturata:** 2026-09-06 · 6 slice desktop (1440×900) · 4 mobile (390×844)
**Altezza:** 5.103px desktop · 2.830px mobile · larghezza 1.430px
**Blocchi di copy:** 57 · **CTA:** 2 · **Media:** 7
**Prodotto:** Armageddon Pack — outEmail + outFunnel + outHeadline + outViral 2 + voucher 199€ su Funnel Operator. **199€** contro 784€ di listino. Scadenza **10 settembre 2026, mezzanotte**.

> Questo è il decimo report dello studio siti dell'ecosistema Andrei Pascu, ed è il primo su una **pagina di lancio a tempo**. Non è una sales page: è una biglietteria.

---

## 0. LA COSA PIÙ IMPORTANTE TROVATA IN QUESTA PAGINA — non è il design

Il CSS della pagina è servito in chiaro, commentato, e i commenti dicono come è stata costruita:

```
/* Built to Andrei's mockup, `docs/homepage-design/full-page-mockup.pdf`.
   Every number below is a fraction of `--u`, the design column, read off that
   file: the mockup is 826.46 units wide and 2851.92 tall, so `.7631` means
   "76.31% of the design width" ... Do not round them by eye — re-measure the PDF instead.

   `assets/brand.css` does not govern this page. His design has rounded
   buttons, a red palette and a numeric counter; CLAUDE.md §4 says his design wins here. */
```

E più avanti:

```
/* Andrei's note on AP-138: the type scale is his rough pass, fix it. */
/* Andrei asked on 5 September for a line and an arrow over the player. */
/* Andrei, 5 September: he wants people to actually press play. */
```

Cosa dicono questi commenti, letti insieme:

| Evidenza | Cosa significa |
|---|---|
| `CLAUDE.md §4` citato come autorità | Il sito ha un **CLAUDE.md con regole numerate**, e l'agente lo cita per giustificare una deroga |
| `AP-138` | Esiste un **sistema di ticket** con prefisso `AP-`, e le note di Andrei ci entrano dentro |
| `docs/homepage-design/full-page-mockup.pdf`, 826.46 × 2851.92 unità | Il design **nasce in un PDF misurato**, e il codice ne è la traduzione proporzionale |
| `assets/brand.css` | Esiste un **brand.css di casa** che questa pagina deroga per scelta dichiarata |
| Commenti in inglese, in prima persona, che spiegano *perché* una riga esiste | Scritti da un agente, non da lui: il resto del sito è in italiano |
| `Andrei asked on 5 September` | Le richieste del committente sono **datate dentro il codice** |

**Andrei Pascu costruisce le sue landing con Claude Code, con un CLAUDE.md, un brand.css, un mockup PDF misurato e un ticket system.** Non con un page builder. Non con Framer. Con lo stesso strumento con cui lavoriamo noi.

Questa è intelligence competitiva più preziosa del suo stile: è il suo **metodo di produzione**, ed è pubblico.

---

## 1. LO STACK — quello che NON c'è

| Cosa | armageddon.bsns.it | La nostra `empire-premium-style` |
|---|---|---|
| Framework | **nessuno** | Next.js 16 App Router |
| CSS | **1 file, 1.020 righe, scritto a mano** | Tailwind v4 |
| JS | **1 IIFE inline, 5,6 KB, vanilla** | Framer Motion + GSAP + Lenis |
| Build step | **nessuno** | `npm run build` |
| Dipendenze runtime | **zero** | 7+ pacchetti |
| Smooth scroll | nativo del browser | Lenis |
| Animazioni | 3 `@keyframes` + 1 parallax rAF | Framer + ScrollTrigger |
| Accordion | `<details>` nativo | componente React |
| Modale | `<dialog>` nativo + `::backdrop` | componente React |
| Peso trasferito | ~21 KB HTML + ~25 KB CSS + font | bundle JS + hydration |

**Funziona con JavaScript disattivato.** Le FAQ si aprono (`<details>`), il testo si legge, il bottone COMPRA porta a Stripe. Si perdono solo il contatore, il parallax e la modale.

Questo va detto con precisione: **la sua pagina di lancio è tecnicamente più leggera e più robusta della nostra skill di punta**, e non le manca niente sul piano visivo.

---

## 2. IL SISTEMA DI MISURA — `--u`, la colonna di progetto

Il pezzo più copiabile di tutta la pagina.

```css
.page, .incl {
  --u: min(100cqw, 960px);        /* container query, fallback min(100vw, 960px) */
  --col: calc(50% - var(--u) / 2); /* bordo sinistro della colonna */
  --btn: clamp(206px, calc(var(--u) * 0.2996), 288px);
  --cell: clamp(56px, calc(var(--u) * 0.0886), 85px);
}
```

**Ogni singola misura della pagina è una frazione di `--u`.** Non ci sono breakpoint di stile: c'è un unico media query a 720px, e serve solo a tre cose (video a tutta larghezza, altezza sezione, posizione della domanda).

Esempi presi dal CSS:

| Elemento | Valore | Cioè |
|---|---|---|
| Altezza hero | `var(--u)` | un quadrato perfetto sulla colonna |
| "Armageddon" | `calc(var(--u) * 0.1996)` | 19,96% della colonna |
| "is here" | `calc(var(--u) * 0.2025)`, top `0.62125` | 20,25%, a 62,1% dall'alto |
| Video | left `calc(var(--col) + var(--u) * 0.1321)`, width `0.7631` | 76,31% della colonna |
| "Sei pronto?" | `calc(var(--u) * 0.15832)`, top `0.86487` | quinta cifra decimale |
| Ticket davanti | width `0.330483`, top `0.043192` | sesta cifra decimale |

Le cifre **non sono arrotondate**: `0.86487`, `0.330483`, `0.155062`. Sono lette dal PDF e trascritte. Il commento lo vieta esplicitamente: *"Do not round them by eye — re-measure the PDF instead."*

**Effetto:** la composizione si ridimensiona **come una sola immagine**. Su 390px e su 1440px le proporzioni sono identiche. Non "responsive": **scalare**.

Due sole eccezioni, e sono dichiarate: `--btn` e `--cell` hanno un pavimento in `clamp()`, perché ai suoi rapporti esatti il bottone su telefono verrebbe 117×29px con testo 10px — troppo piccolo da toccare. Il commento lo scrive per esteso.

---

## 3. PALETTE — misurata dal DOM

### Testo

| Hex | Occorrenze | Ruolo |
|---|---|---|
| `#ffffff` | 41 | corpo, nomi prodotto, numeri contatore |
| `#ffffff @0.76` | 11 | risposte FAQ |
| **`#bc0807`** | **5** | **l'unico colore della pagina** |
| `#ffffff @0.5` | 4 | etichette contatore (GIORNI/ORE/…) |
| `#ffffff @0.55` | 3 | riga "€784 di valore, paghi €199" |
| `#ffffff @0.42` | 2 | disclaimer legale |
| `#ffffff @0.78` | 1 | wordmark BSNS.IT |
| `#ffffff @0.62` | 1 | link privacy |
| `#000000` | 1 | testo dentro il bottone COMPRA |
| `#0000ee` | 1 | ⚠️ `mailto:help@apsales.eu` — **difetto, vedi §8** |

### Sfondi

| Hex | Occorrenze |
|---|---|
| `#000000` | 4 |
| `#bc0807` | 4 (le quattro celle del contatore) |
| `#000000 (+img)` | 2 (le due sezioni con fotografia) |
| `#ffffff` | 1 (bottone COMPRA) |

**Due colori. Nero e `#bc0807`.** Il bianco è testo, non superficie, tranne che sul bottone che incassa. Le gradazioni di bianco (0.42 → 0.5 → 0.55 → 0.62 → 0.76 → 0.78 → 1) fanno tutto il lavoro di gerarchia che altrove farebbe una scala di grigi.

**La regola sotto:** più un testo è vicino al denaro, più è opaco. Il disclaimer sta a 0.42, il prezzo a 1.

---

## 4. TIPOGRAFIA — due caratteri, e uno se lo è comprato

```
"Plus Jakarta Sans", system-ui, -apple-system, sans-serif   → 59 usi
Curseyt, "Times New Roman", serif                            → 12 usi
```

**Curseyt** è un blackletter (gotico) servito da lui, `/assets/fonts/curseyt.woff`, con `font-display: block` e non `swap`. Il commento spiega perché:

```css
font-display: block; /* the blackletter IS the design — no swap flash */
```

Preferisce **bloccare il rendering** piuttosto che mostrare Times New Roman per 100ms. È una scelta che paga il Core Web Vital per non tradire l'identità.

### Dove va il gotico e dove no

| In Curseyt (12 usi) | In Plus Jakarta Sans (59 usi) |
|---|---|
| "Armageddon" ×2 · "is here" | Tutto il corpo |
| "Guarda il video" | Le domande FAQ |
| "Sei pronto?" | Tutte le risposte |
| "Risparmi €585" | I bottoni |
| "Domande" | I numeri del contatore |
| I 4 nomi prodotto | Le etichette |
| I titoli della modale | Il legale |

**Il gotico grida, la grottesca spiega.** Nessuna eccezione in tutta la pagina. E dentro la modale c'è la conferma della regola: i quattro nomi prodotto sono in Curseyt, la riga del voucher — che è una descrizione, non un nome — torna in Plus Jakarta Sans. Commento:

```css
/* The four names are set the way the ticket sets them; this one is a line of
   plain description, so it stays in the text face where it can be read. */
```

### Scala misurata

| px | Peso | Elemento |
|---|---|---|
| 194,4 / 191,6 | 400 | "Armageddon" (due strati sovrapposti) |
| 152,0 | 400 | "Sei pronto?" |
| 94,1 | 400 | "Guarda il video" |
| 81,6 | 400 | "Risparmi" / "€585" |
| 72,0 | 400 | "Domande" |
| 59,5 | 400 | i 4 nomi prodotto |
| 28,3 | 800 | cifre del contatore |
| 25,0 | 800 | testo dei bottoni |
| 19,0 | 700 | domande FAQ |
| 16,5 | 400/700 | risposte FAQ |
| 14,9 | 400 | riga valore |
| 13,9 | 800 | wordmark |
| 12,0 | 400/700 | etichette + legale |

**Rapporto fra il più grande e il più piccolo: 16,2×.** Su apsales.eu era 6,4×. Questa pagina urla molto più forte.

Tutto il display è peso **400**: il gotico non ha bisogno di grassetto, ha già il nero suo. Tutto ciò che deve essere *cliccato* è **800**. Il grassetto qui non significa "importante", significa "toccabile".

### Raggi — ce ne sono due in tutta la pagina

| Raggio | Dove |
|---|---|
| 15,19px | i due bottoni (`calc(var(--btn) * 0.0528)`) |
| 6,375px | le celle del contatore (`calc(var(--cell) * 0.075)`) |
| 8px | la modale |

Anche i raggi sono frazioni dell'elemento, non valori fissi: il bottone che si rimpicciolisce si arrotonda meno. È il livello di coerenza che nessun page builder produce.

---

## 5. LA STRUTTURA — quattro schermate e basta

| # | Sezione | Altezza | Cosa fa |
|---|---|---|---|
| 1 | `.topbar` | ~90px | Filetto rosso in dissolvenza + occhio + `BSNS.IT` → torna al brand |
| 2 | `.hero` | `--u` (quadrato) | Ritratto + splatter + il titolo in due strati |
| 3 | `.stage` | `--u × 1.0866` | Cielo rosso, "Guarda il video" + freccia, player Vimeo 13:29, "Sei pronto?" |
| 4 | `.offer` | flusso | Fiamme, i due biglietti, COMPRA, COSA INCLUDE?, contatore, "Risparmi €585" |
| 5 | `.tail` | flusso | I 4 nomi prodotto, le 11 domande, il disclaimer, la P.IVA |

**Non c'è una sezione di benefici. Non c'è una lista di cosa impari. Non ci sono testimonianze. Non c'è una bio. Non c'è una garanzia.**

57 blocchi di testo su 5.103px. Per confronto, dallo stesso studio:

| Pagina | Blocchi | Altezza |
|---|---|---|
| `/copy` mentorship | 337 | 26.952px |
| `outheadline` | 241 | 21.119px |
| `apsales.eu` | 168 | 12.565px |
| **`armageddon`** | **57** | **5.103px** |

**Scoperta 11 dello studio siti: la pagina di lancio non vende, incassa.** La persuasione è già avvenuta altrove — nel video da 13 minuti, nella lista email, su Instagram. Alla pagina restano tre lavori soli: dire cos'è, dire quando scade, prendere i soldi. Tutto il resto sarebbe attrito.

Corollario onesto: **chi arriva a freddo e non guarda il video non ha niente da leggere** tranne le FAQ. È una scommessa deliberata su un pubblico caldo (vedi §8, difetto 3).

---

## 6. GLI EFFETTI — uno per uno, con i numeri

### 6.1 Il titolo disegnato due volte

```html
<span class="hero__word hero__word--1" data-par="word">Armageddon</span>
<span class="hero__word hero__word--1 hero__word--edge" aria-hidden="true" data-par="word">Armageddon</span>
```

```css
.hero__word--1    { z-index: 1; }                              /* DIETRO il ritratto */
.hero__word--edge { z-index: 3; color: transparent;
                    -webkit-text-stroke: max(1px, calc(var(--u)*0.0013)) var(--red); }
```

Stessa parola, stessa posizione, **due z-index diversi**: uno sotto il volto, uno sopra, e quello sopra è solo contorno. Risultato: la parola è **piena** dove attraversa il nero e diventa **un'incisione rossa** dove passa sui capelli. Un solo tag in più, un effetto che sembra composito.

La copia in contorno ha `aria-hidden="true"`: lo screen reader legge la parola una volta sola.

### 6.2 Parallax a quattro velocità

```js
var RATE = { splat: 0.2, word: 0.09, word2: 0.04, man: 0.155 };
```

Quattro gruppi, quattro rapporti di scorrimento. Il commento spiega la scelta:

```
/* The man travels about 15% of what the page does and the splatter behind him
   20%, so the separation between him and the words is ~60px across the hero —
   enough to read as depth. The gap a downward-moving layer opens at the top of
   the hero is black on black, which is why this does not need oversized artwork. */
```

Notare: gli schizzi (dietro) vanno **più veloci** del ritratto (davanti). È l'inverso del parallax da manuale, e funziona perché lo sfondo è nero — il buco che si apre non si vede.

Implementazione: `translate3d` scritto su `style.transform`, dentro `requestAnimationFrame`, listener `{ passive: true }`, `y` limitato all'altezza dell'hero. **Nessuna libreria.**

### 6.3 L'atterraggio — 3 keyframes, 3 tempi

| Animazione | Durata | Delay | Cosa |
|---|---|---|---|
| `ag-zoom` | 1700ms | 0 | ritratto da `scale(1.055)` a 1 |
| `ag-fade` | 1400ms | 120ms | gli schizzi in dissolvenza |
| `ag-rise` (a) | 1200ms | **180ms** | "Armageddon" sale di `--u × 0.026` |
| `ag-rise` (b) | 1200ms | **340ms** | "is here" sale di `--u × 0.022` |

Curva unica: `cubic-bezier(0.16, 0.86, 0.3, 1)`. Il commento la chiama `--ease-land`.

Il dettaglio da rubare: l'animazione sta **sui figli** (`<i class="in">`), non sui contenitori, *"so it never fights the parallax transforms the script writes onto the layers themselves"*. Due sistemi di trasformazione sullo stesso elemento si annullano — lui li mette su due nodi diversi.

### 6.4 I biglietti — l'unico micro-teatro della pagina

Stato iniziale in HTML: `class="tickets is-spread is-locked"`.

1. Arrivano **separati** (già visibili così, non c'è flash).
2. `IntersectionObserver` con `threshold: 0.3` li vede.
3. Dopo **2.500ms** parte `unlock()`: via `is-spread` → si accavallano con `transition: transform 820ms cubic-bezier(0.65, 0, 0.25, 1)`.
4. Dopo altri **900ms** via `is-locked` → solo ora rispondono al mouse.

Il blocco `is-locked` serve a una cosa sola: impedire che l'hover parta a metà volo. È il tipo di dettaglio che nessuno nota e che tutti sentono.

Trasformazioni all'hover:
```css
.ticket--front { transform: translate(calc(var(--u)*-0.03), calc(var(--u)*0.008)) scale(1.05); }
.ticket--back  { transform: translate(calc(var(--u)*0.055), calc(var(--u)*-0.02)) rotate(8.9deg); }
.ticket--back img { transform: scale(0.95); }
```

Il retro ruota **da 7,16° a 8,9°** e la sua immagine si rimpicciolisce mentre il contenitore si sposta: due trasformazioni contrarie sullo stesso oggetto, ed è quello che dà la sensazione di carta che si scosta.

Ombre: due `drop-shadow` sovrapposti, entrambi in frazioni di `--u` — l'ombra scala col biglietto.

### 6.5 La cucitura fra hero e cielo — il pezzo più tecnico della pagina

Due pseudo-elementi che si passano il testimone su un valore di opacità:

```css
.hero::before { top: calc(var(--u)*0.78); bottom: calc(var(--u)*0.1215);
                background: linear-gradient(to bottom, rgba(0,0,0,0) 0, rgba(0,0,0,0.992) 100%); }
.hero::after  { top: calc(var(--u)*0.8785); bottom: 0;
                background: linear-gradient(to bottom, rgba(0,0,0,0.992) 0, rgba(0,0,0,0.71) 100%),
                            url("/assets/home/sky.webp") ... }
.stage        { background: linear-gradient(to bottom, rgba(0,0,0,0.71) 0, ...) }
```

`0.992` → `0.992`. `0.71` → `0.71`. **Le tre superfici si agganciano sullo stesso numero**, così la stessa fotografia del cielo attraversa due sezioni HTML diverse senza che si veda una linea. Il commento: *"the two halves of his one gradient meet without a step."*

Questo è il livello a cui va portata la nostra `section-border-t`.

### 6.6 Il prezzo si calcola da solo

```js
var total = 0;
dlg.querySelectorAll('[data-price]').forEach(p => total += Number(p.dataset.price));
var pay = Number(dlg.dataset.packPrice);
write('[data-total]', money(total));
write('[data-pay]',   money(pay));
write('[data-save]',  money(total - pay));
```

I 784€, i 199€ e i 585€ **non sono scritti tre volte nella pagina**: sono scritti una volta come `data-price` sulle righe della modale, e sommati a runtime. Commento: *"so moving one price cannot leave a stale total behind it."*

Questo è direttamente il rimedio al **difetto n.6 dello studio siti** (otto cifre per quattro metriche fra le sue vecchie pagine). Lo ha risolto con il codice, non con la disciplina.

### 6.7 Il contatore

`data-until="2026-09-11T00:00:00+02:00"` — **su un attributo solo, in un posto solo.** `setInterval` a 1s, `tabular-nums` così le cifre non ballano, e un `aria-label` riscritto ogni secondo:

```js
count.setAttribute('aria-label', 'Mancano ' + d + ' giorni, ' + h + ' ore, ...');
```

Un contatore accessibile. Non ne ho visti molti.

### 6.8 Cose native usate come si deve

| Cosa | Come |
|---|---|
| Modale | `<dialog>` + `showModal()` + `::backdrop { backdrop-filter: blur(4px) }` + chiusura al click fuori (calcolata sul `getBoundingClientRect`) + `html.is-modal { overflow: hidden }` |
| FAQ | `<details>` / `<summary>`, marcatore `+` che diventa `–` via `content`, `::-webkit-details-marker { display: none }` per Safari |
| Fallback | Se `showModal` non esiste → `location.hash = '#cosa-include'`, e il footer **ha quell'id** |
| Scrollbar | `scrollbar-gutter: stable` + thumb rosso — nessun salto di layout quando appare |
| Motion | `@media (prefers-reduced-motion: reduce)` spegne **tutto**: animazioni, transizioni, e in JS il parallax e il timer dei biglietti |

---

## 7. IL COPY — undici domande e nient'altro

Il corpo scritto della pagina è **quasi interamente FAQ**. E sono le migliori dell'ecosistema.

### La regola: rispondere contro il proprio interesse

| Domanda | Cosa risponde |
|---|---|
| *"outFunnel e Funnel Operator sono lo stesso corso?"* | *"No, sono due prodotti diversi, e il nome simile confonde."* — **ammette che il naming è confuso** |
| *"Sono già dentro Funnel Operator. Ha senso comprarlo?"* | *"Sì, ma compralo per i quattro corsi, non per il voucher. […] il voucher non ti serve e non viene convertito in credito, sconto o rimborso. Nessuno ti deve niente su quella parte, ed è giusto tu lo sappia prima di pagare."* |
| *"Ho già uno dei quattro corsi. Posso pagare meno?"* | *"No. […] Se ne hai già uno, stai pagando 199€ per gli altri tre più il voucher — **fai tu il conto prima di comprare**."* |
| *"Mi garantite dei risultati?"* | *"No, e diffida di chi lo fa."* |
| *"Come e quando ricevo l'accesso?"* | *"[…] controlla lo spam: quella email è il tuo accesso."* |
| *"Ho un problema con l'accesso?"* | *"[…] se non ti è arrivata niente entro pochi minuti, guarda nello spam **prima di ricomprare — non pagare due volte**."* |

Sei risposte su undici **allontanano un acquisto** o riducono il valore percepito. Nessuna promessa. Nessun "trasformerai la tua vita".

**Il meccanismo:** dicendo apertamente le cose che gli costano, si compra il diritto di essere creduto su quelle che gli rendono. È la stessa mossa della garanzia di rimedio su apsales, applicata al testo.

### Il voucher spiegato come un contratto

> *"È uno sconto di 199€ sul prezzo di Funnel Operator, da usare al lancio. Vale una volta sola e solo su Funnel Operator: **non è denaro, non si incassa, non si divide su più acquisti e non si passa a un'altra persona**. Se decidi di non comprare Funnel Operator, il voucher semplicemente non lo usi — non diventa un rimborso."*

Quattro negazioni consecutive. Chiude ogni contestazione futura **prima** che il denaro cambi mano. Questo paragrafo vale più di un ticket di assistenza risparmiato: vale un chargeback evitato.

### La scadenza detta due volte, in due modi

- Nel contatore: quattro celle rosse che scendono al secondo.
- Nel testo: *"Fino a giovedì 10 settembre compreso: l'offerta chiude a mezzanotte fra il 10 e l'11, ora italiana. È quello che conta il timer qui sopra. Dopo quel momento questa pagina non vende più il pacchetto: i corsi tornano ai loro prezzi singoli e il voucher su Funnel Operator non viene più emesso."*

**Il testo spiega il timer.** Il timer da solo è un trucco visto mille volte; il timer più la frase che dice esattamente cosa succede dopo è una condizione contrattuale. E dichiara *cosa* torna com'era — prezzi singoli, niente voucher — che è verificabile.

### Il disclaimer

> *"Questo sito e i consigli contenuti al suo interno sono opinioni personali a scopo educativo […] I suoi risultati non sono tipici e i tuoi potrebbero variare in base a esperienza, effort, situazione economica e generale contesto. Andrei Pascu e i suoi collaboratori non fanno e non trattano argomenti come crypto, personal finance, fiscalità, risorse umane, recruiting, network marketing o in genere metodi di arricchimento veloce."*

Elenca **cosa non è** per nome. È la versione più serrata di quello già trovato su claude-speedrun. In un mercato dove il 90% dei lanci italiani non ha nemmeno una P.IVA in fondo alla pagina, qui c'è disclaimer + privacy + `Andrei Pascu Sales · P.I. 02001850474 · Viale Giacomo Matteotti 15, 50121 Firenze (FI)`.

---

## 8. DIFETTI REALI — misurati, non supposti

| # | Difetto | Evidenza | Gravità |
|---|---|---|---|
| 1 | **Link email blu di default** | `help@apsales.eu` è `#0000ee`, l'unico colore fuori palette in tutta la pagina. In una tavolozza di due colori si vede da lontano. | Bassa, ma è l'unica sbavatura visiva |
| 2 | **Il contatore non gestisce la scadenza** | `Math.max(0, until - Date.now())` si ferma a `00 00 00 00`, ma la pagina continua a vendere a 199€ e il bottone Stripe resta vivo. Dopo l'11 settembre la pagina si contraddice da sola. | **Alta** — è la promessa più esplicita della pagina |
| 3 | **Nessun testo per chi non guarda il video** | Zero benefici, zero prova, zero bio. Chi arriva da un'inserzione fredda e non ha 13 minuti non ha nulla da leggere tranne le FAQ. | **Alta a freddo**, nulla a caldo |
| 4 | **Zero dati strutturati** | Niente JSON-LD `Product`/`Offer`, niente `FAQPage` — con 11 FAQ scritte bene, è un rich result regalato. Nessun `<link rel="canonical">`. | Media |
| 5 | **Nessuna prova sociale** | Nemmeno un numero. Su una pagina che chiede 199€ è una scelta forte: regge solo perché il pubblico è già suo. | Media, dipende dal traffico |
| 6 | **`<h1>` letto come "Armageddon Armageddon is here"** dagli estrattori | Lo strato in contorno ha `aria-hidden`, quindi gli screen reader stanno bene, ma i crawler leggono il doppione. | Bassa |
| 7 | **Il video è l'unico punto di fallimento** | Se Vimeo non carica, la pagina perde il 90% del suo argomento. Nessun fallback testuale. | Media |

### Da non copiare

L'assenza totale di corpo testuale. **Funziona perché il traffico è caldo.** Su una pagina che riceve traffico a pagamento freddo, questa struttura non converte — e lui lo sa, perché su `outheadline` (98€, traffico freddo) scrive 241 blocchi.

**La regola vera che se ne ricava:** la lunghezza della pagina non dipende dal prezzo, dipende da **quanto lavoro di persuasione la pagina deve ancora fare quando il visitatore arriva.** Questa è la formulazione definitiva della scoperta #7 dello studio siti.

---

## 9. LE 12 MOSSE DA PORTARE DENTRO DIGITAL EMPIRE

Ordinate per rapporto valore/costo.

| # | Mossa | Dove va |
|---|---|---|
| 1 | **La colonna `--u`** — ogni misura è una frazione di una colonna sola, la pagina scala come un'immagine | Design system, token di base |
| 2 | **Il prezzo calcolato dal DOM** — un solo `data-price`, il resto sommato a runtime | Ogni pagina di vendita |
| 3 | **Il titolo in due strati** (pieno dietro + contorno davanti) | Pattern hero |
| 4 | **La cucitura fra sezioni sullo stesso valore di opacità** | Sostituisce `section-border-t` dove c'è una fotografia |
| 5 | **`is-locked`** — l'hover non risponde finché l'animazione d'ingresso non è finita | Regola generale di interazione |
| 6 | **Il contatore accessibile** — `aria-label` riscritto, `tabular-nums`, scadenza su un attributo solo | Componente lancio |
| 7 | **`<details>` e `<dialog>` nativi** al posto dei componenti React | Riduzione stack |
| 8 | **`font-display: block`** quando il carattere *è* il design | Regola tipografica |
| 9 | **FAQ che rispondono contro il proprio interesse** — 6 su 11 allontanano l'acquisto | Standard di copy |
| 10 | **Il testo che spiega il timer** — la scadenza detta due volte, e dichiarata verificabile | Standard di lancio |
| 11 | **Le quattro negazioni del voucher** — chiudere le contestazioni prima del pagamento | Standard legale/commerciale |
| 12 | **`prefers-reduced-motion` che spegne anche il JS**, non solo il CSS | Gate di qualità |

### E una da non copiare
Il vuoto testuale. Va replicato **solo** su pagine che ricevono traffico già scaldato, e mai su traffico a pagamento freddo.

---

## 10. IL VERDETTO

`armageddon.bsns.it` non è la sua pagina più bella — `apsales.eu` è più matura, `claude-speedrun.com` è più ricca. È la sua pagina **meglio costruita**.

È anche la prova che il nostro problema con i siti non è di gusto: è di **impianto**. Lui ha un CLAUDE.md, un brand.css, un mockup misurato in unità e un sistema di ticket. Noi abbiamo quattro sistemi che si contraddicono sullo stack (vedi il dossier `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md`).

Il pezzo da rubare non è il rosso. È la colonna `--u` e il CLAUDE.md che la difende.

---

## Connessioni

- [[Report_07_Claude_Speedrun]] — `competitor/Andrei Pascu/site-study/reports/07-claude-speedrun.md` — l'altro sito con un design system vero
- [[Report_08_APSales]] — `competitor/Andrei Pascu/site-study/reports/08-apsales.md` — la garanzia di rimedio, stesso registro delle FAQ qui
- [[Report_09_Linktree]] — `competitor/Andrei Pascu/site-study/reports/09-linktree.md` — dove `outViral` è stato trovato per la prima volta
- `11-armageddon-ATLANTE-VISIVO.md` — schermata per schermata, con le misure di ogni elemento
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — il sistema che nasce da questo studio
