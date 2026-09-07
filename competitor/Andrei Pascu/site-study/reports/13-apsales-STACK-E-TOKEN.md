---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #apsales #stack #design-tokens #ccm #cro-agency
Created: 2026-09-07
Last updated: 2026-09-07
---

# 13 — apsales.eu — LO STACK E I TOKEN

**Il secondo passaggio sullo stesso sito.** Il [rapporto 08](08-apsales.md) del 2026-09-02 ha studiato
copy, palette e struttura **dalle immagini** (cattura `08-apsales`, 2026-09-01). Questo studia **come
è costruito**, dai file serviti nella nuova cattura `13-apsales-v2` (2026-09-07): 13 file sorgente
scaricati (12 JS + 2 CSS), 127 KB di CSS analizzati, 9 `@keyframes`, e i nomi dei suoi componenti.

È lo **strato 4** di `emperator.md §6.22` — *come l'ha fatta*, non *com'è fatta*. E qui conta doppio:
`apsales.eu` **è il concorrente diretto** dell'agenzia CRO di Digital Empire, non un adiacente.

> Cattura: `capture/13-apsales-v2/` · 12.565px desktop (15.354px mobile) · **14 sezioni (13
> firme distinte)** · 537 blocchi di copy · 19 CTA · ~50 media · 13 file sorgente · 9 keyframes propri.

---

## 1. LO STACK — React con TanStack Start, non un sito statico

Le prove non sono indiziarie: sono stringhe lette di persona nei file scaricati.

| Cosa | Evidenza misurata | File |
|---|---|---|
| **React** | chunk `jsx-runtime-CBeXhfNn.js` a parte, componenti per file, `useState`/`useRef`/`useEffect` | tutti |
| **TanStack Router** | le stringhe letterali `tanstack_root_error_component` e `tanstack_router_reload` | `08-index-CfVXeo8a.js` |
| **TanStack Start (server functions)** | `e({method:"POST"}).handler(t("<hash-64-char>"))` — il pattern esatto di `createServerFn(...).handler(...)`, 5 funzioni referenziate per hash (il corpo vive lato server, qui resta solo il riferimento) | `07-forms.functions-DiYx6QCP.js` |
| **`useServerFn` (hook ufficiale)** | il file si chiama esattamente come l'export che contiene: `t.stores.location.get()`, `t.navigate(t.resolveRedirect(e).options)` — chiama il router per gestire un redirect restituito dalla server function | `12-useServerFn-C9O_qu9A.js` |
| **Route table compilata** | i path reali della navigazione dentro il bundle: `/servizi`, `/consulenza`, `/landing-page`, `/chi-siamo`, `/about`, `/schema` | `10-routes-zpYcnjTA.js` (31 KB) |
| **Tailwind** | 127 KB di utility generate, variabili `--tw-*` ovunque, classi arbitrarie `[mask-image:...]` | `11-styles-CHG2jDaU.css` |
| **shadcn/ui** | il set completo di variabili: `--background --foreground --card --popover --primary --secondary --muted --accent --destructive --border --input --ring --radius` **e `--sidebar-*`** — identico a quello letto su `claude-speedrun.com` (dossier 12) | `11-styles-CHG2jDaU.css` |
| **Radix UI** | `@keyframes accordion-up/down` con `--radix-accordion-content-height`; primitive Dialog/Collapsible import-ate per nome (`Slot`, `Collection`, `useControllableState`) | `05-accordion-LU6_yz4t.js`, `06-dialog-CKatyLC6.js` |
| **Google Fonts self-hosted** | `13-css2.css` è il foglio scaricato da `fonts.googleapis.com` e servito come chunk statico, 39 `@font-face` con `unicode-range` a subset | `13-css2.css` |

**Un gradino sopra `claude-speedrun.com`** (dossier 12, stesso ecosistema): quel sito è React+Vite
client-only, senza rotte server. Questo usa **TanStack Start** — router con server functions vere
(il form di prenotazione chiamata invia dati a una funzione che gira sul server, non a un endpoint
esterno tipo Zapier/Make). È lo stesso stack che il nostro agente `site-premium-builder` dichiara
obbligatorio (Next+Tailwind+shadcn+Radix): qui l'autore ha scelto TanStack Start al posto di Next,
stessa filosofia (React + meta-framework con SSR), bundler diverso.

---

## 2. I TOKEN — la sua palette è OKLCH, convertita qui in HEX

Sei variabili di marca, lette da `estratto-css.md`. Conversione OKLCH → sRGB calcolata (matrice
OKLab → LMS → sRGB lineare → gamma-corretta), non stimata a occhio:

| Variabile | OKLCH misurato | HEX calcolato | Ruolo osservato |
|---|---|---|---|
| `--brand-void` | `oklch(14.48% .002 285)` | **`#0a0a0b`** | fondo dominante (20 usi in `palette_sfondi`) |
| `--brand-pitch` | `oklch(17.76% 0 0)` | **`#111111`** | card, un gradino sopra il fondo (10 usi) |
| `--brand-blue` | `oklch(55.6% .2453 261.33)` | **`#0062ff`** | l'unico colore della pagina: bottoni, numeri di processo, footer (13 usi testo + 13 usi sfondo) |
| `--brand-paper` | `oklch(98.21% 0 0)` | **`#f9f9f9`** | testo di default su fondo scuro (273 usi) **e** sfondo della sezione team invertita |
| `--brand-ink` | `oklch(22.73% .0038 286.09)` | **`#1c1c1e`** | testo scuro sulla sezione chiara (6 usi) |
| `--brand-bone` | `oklch(93.01% .0122 96.43)` | **`#eae8df`** | dichiarata nel CSS ma **non misurata in uso** su questa pagina (0 occorrenze in `palette_testo`/`palette_sfondi`) — probabile riserva per altre pagine del sito (`/servizi`, `/chi-siamo`) |

Calcolo mostrato per `--brand-blue` (lo stesso metodo per gli altri cinque):
```
OKLCH(0.556, 0.2453, 261.33°) 
  a = 0.2453·cos(261.33°) = -0.0370   b = 0.2453·sin(261.33°) = -0.2424
  OKLab → LMS' → LMS → sRGB lineare → gamma sRGB
  → R=0.000  G=0.384  B=1.000  (clampato)
  → rgb(0, 98, 255) → #0062ff
```

### Confronto col nostro canone (`canone.css`)

| Loro (`apsales.eu`) | Nostro (`canone.css`) | Distanza |
|---|---|---|
| `--brand-void` `#0a0a0b` | `--ink-2` `#0a0a0a` | **praticamente identico** — 1 unità sul canale blu |
| `--brand-paper` `#f9f9f9` | `--fg` `#f9f9f9` | **identico, cifra per cifra** |
| `--brand-ink` `#1c1c1e` (il LORO testo scuro) | `--ink` `#1c1c1c` (il NOSTRO fondo scuro) | stesso valore, **ruolo opposto**: loro lo usano come testo, noi come sfondo |
| `--brand-pitch` `#111111` | (nessuna corrispondenza diretta; il nostro gradino intermedio non esiste come token separato) | — |
| `--brand-bone` `#eae8df` | `--grey` `#e8e8e6` | vicini ma non identici — il loro è più caldo (beige), il nostro più freddo (grigio puro) |
| `--brand-blue` `#0062ff` | `--orange` `#fb4604` | **opposti**: loro blu (H≈261°), noi arancione (H≈16°) |

**A differenza di `claude-speedrun.com`** (dossier 12, dove tre valori su cinque coincidevano col
nostro canone, arancione compreso), qui **il colore d'azione non si sovrappone**: il blu di AP Sales
non è il nostro arancione, non c'è rischio di confusione di marca fra i due siti. Coincidono invece,
quasi esattamente, i due neutri di fondo (`void`/`ink-2` e `paper`/`fg`) — segno che sulla scelta dei
neutri "quasi nero, non nero puro" e "quasi bianco, non bianco puro" l'industria converge
indipendentemente (la stessa nota è già in `canone.css`: *"il nero puro NON è un fondo per testo
lungo"*).

---

## 3. GLI EFFETTI — 13 maschere di dissolvenza, un blend, due filtri custom

### Il componente `Ascii` — l'unico effetto grafico riusato

Il file `01-Ascii-BML5uz1H.js` (706 byte) è **un solo componente**, richiamato per tutte le immagini
in stile "ASCII art" bianco-su-nero (`occhio.webp`, `laptop.webp`, `mirino-dot.webp`,
`templare-pixel.webp`, i 5 guerrieri): 

```js
className: `pointer-events-none select-none mix-blend-screen
            ${boost ? '[filter:contrast(1.3)_brightness(1.45)]' : ''}`
```

**Blend `screen` + `contrast(1.3) brightness(1.45)`**: il nero della webp si annulla contro il fondo
scuro (screen su nero = trasparente), il bianco si "brucia" più chiaro e più contrastato. Un solo
componente, sei impieghi diversi, zero PNG con alpha da preparare a mano. Il CSS generale porta anche
`contrast(1.15)brightness(1.3)` e `contrast(1.35)brightness(1.5)`: almeno tre livelli di intensità
dello stesso trucco.

Due filtri SVG referenziati per nome — `url("#luma-alpha")` e `url("#luma-alpha-band")` — sono
misurati nell'elenco `effetti.filtri` di `scheda.json`, ma il nodo `<filter>` con il loro
`feColorMatrix` non è stato trovato nei 13 chunk scaricati (vive quasi certamente nel markup HTML
della pagina, non nei bundle JS/CSS): **dichiaro l'esistenza, non il contenuto** — sono probabilmente
una tecnica di conversione luminanza→trasparenza più precisa del semplice blend screen, riservata a
qualche immagine specifica.

### Le 13 maschere `mask-image` — tutte dissolvenze ai bordi

```
inset(50%)                                                    ← clip, non mask: pattern "sr-only"
linear-gradient(#000 78%, #0000 97%)
linear-gradient(#000, #0000 80%)
linear-gradient(#000, #0000 82%)
linear-gradient(#0000 22%, #000)
linear-gradient(#0000, #000 18% 82%, #0000)
linear-gradient(115deg, #000 55%, #0000)
linear-gradient(245deg, #000 55%, #0000)
linear-gradient(90deg, #0000, #000 10% 90%, #0000)
linear-gradient(90deg, #0000, #000 9% 91%, #0000)
radial-gradient(circle, #000 52%, #0000 72%)
radial-gradient(closest-side, #000, #0000)
```

Nota di misura: `estratto-css.md` abbina ogni valore CSS grezzo alla classe Tailwind arbitraria che lo
usa (es. `.[mask-image:linear-gradient(to_right,transparent,black_9%,black_91%,transparent)]`), ma
l'estrazione per regex mostra un disallineamento di una posizione fra valore e nome-classe — riporto
qui l'elenco grezzo così com'è, senza forzare un abbinamento che il file stesso non garantisce.

**Cosa fanno, per famiglia:**
- **`to_right` / `90deg` con doppia soglia simmetrica** (4 valori: i due `9%/91%` e `10%/90%`, più i
  due `18%/82%`) → dissolvenza sui **due bordi orizzontali**: è la tecnica standard per un marquee
  infinito (la fila di 10 loghi cliente, sezione 3) che non deve mostrare un taglio netto a sinistra
  e destra del loop.
- **`to_bottom` (4 valori: 78-97%, 80%, 82%, 245deg-55%)** → dissolvenza verticale, coerente con lo
  sfondo di rumore ASCII (`x o x`) dietro i guerrieri (sezione 2) che deve sparire prima di toccare il
  bordo della sezione.
- **`radial`/`closest-side`/`circle` (3 valori)** → dissolvenza dal centro verso i bordi, coerente col
  mirino a puntini della card "Consulenza con Andrei Pascu" (sezione 6, screenshot alla mano: il
  cerchio di puntini sfuma visibilmente verso l'esterno).
- **`inset(50%)`** → non è un effetto visivo: è il pattern di accessibilità "sr-only" (nasconde
  visivamente un elemento senza toglierlo dal DOM/screen reader), letto anche nel markup di
  `CallDialog` (`<span className="sr-only">AP Sales</span>`).

### La cucitura del footer — un dettaglio che il solo screenshot fraintende

`RevealFooter` (47 KB) marca il proprio contenitore con `data-blend-surface` e questo stile esatto:
```
relative h-screen min-h-[720px]  style:{ clipPath: "inset(0)" }
  └── fixed bottom-0 left-0 h-screen min-h-[720px] w-full  bg-blue text-white
```
**Il footer ha `bg-blue` nel codice.** Lo screenshot `sezioni/14-footer.png` mostra invece fondo quasi
nero con solo il wordmark "APsales" gigante in blu: la spiegazione più plausibile è che l'elemento
interno sia `position:fixed` dentro un contenitore `clipPath:inset(0)` — una tecnica di "cassetto che
si rivela" in cui il blu pieno resta ancorato al viewport e non al box della sezione, e una cattura a
sezione ritagliata (come questa) non lo mostra pieno. Lo dichiaro come **discrepanza misurata fra
codice e screenshot**, non come certezza sul render finale: andrebbe verificato con uno scroll reale
nel browser, non con un ritaglio automatico.

`StickyCta` (1,7 KB) legge la stessa superficie `[data-blend-surface]` via
`document.querySelector`: calcola quanto la CTA fissa si sovrappone al footer e usa quel numero per
ritagliare (`clipPath: inset(${u}px 0 0 0)`) una **seconda copia** del bottone, colorata `bg-pitch`,
sovrapposta a quella blu — così il bottone "cambia colore" con continuità mentre il footer sale sopra
di lui, invece di restare blu acceso su un fondo blu identico.

---

## 4. I COMPONENTI — la sua tassonomia di pagina

| Componente | Peso | Cosa fa, misurato dal codice |
|---|---|---|
| `Ascii` | 706 B | wrapper unico per tutte le immagini decorative bianco-su-nero (vedi §3) |
| `CallDialog` | 6,1 KB | il modal di prenotazione chiamata: form nome/email/azienda/argomento/orario, validazione client (regex email, nome ≥2 caratteri), invio via server function, tre stati (`idle`/`sending`/`done`), messaggio di rate-limit esplicito (*"Hai già inviato diverse richieste. Riprova tra un'ora"*) |
| `RevealFooter` | 47,5 KB — **il file più pesante fra i componenti nominati** | il footer/finale a piena altezza, con la superficie `data-blend-surface` (vedi §3); il peso alto suggerisce che contenga anche il marquee dei loghi o altra logica non isolata in file a parte |
| `StickyCta` | 1,7 KB | la CTA fissa in basso a destra, appare oltre il 90% di `innerHeight` scrollato, con il trucco del doppio bottone ritagliato (vedi §3) |
| `accordion` | 9,2 KB | wrapper Radix Collapsible/Accordion + classi shadcn — usato dalle 7 domande FAQ |
| `dialog` | 35,4 KB — il secondo file più pesante | primitiva Radix Dialog di base, usata da `CallDialog` e verosimilmente dal menu mobile |
| `forms.functions` | 589 B | 5 riferimenti a server function (`createServerFn({method:"POST"}).handler(hash)`) — solo una (la prenotazione chiamata) è visibile lato client su questa pagina; le altre 4 servono verosimilmente ad altre pagine (carriere, assistenza) |
| `useServerFn` | 368 B | l'hook TanStack Start che invoca la server function e gestisce il redirect tramite il router |
| `routes` | 31,3 KB | la route table compilata: `/servizi`, `/consulenza`, `/landing-page`, `/chi-siamo`, `/about`, `/schema` |

**Cosa insegna questo elenco:** solo **4 componenti su 9 hanno un nome che descrive un ruolo di
prodotto** (`CallDialog`, `RevealFooter`, `StickyCta`, `accordion`); gli altri 5 sono infrastruttura
di framework (routing, server function, dialog primitivo, jsx-runtime). È il rovescio della medaglia
di `claude-speedrun.com` (dossier 12), dove 21 sezioni numerate componevano quasi tutta la pagina:
qui **la pagina stessa non è divisa in componenti per sezione** — non esistono `Section1..N` — è
probabilmente **una sola route con markup inline**, e solo gli elementi realmente interattivi
(dialog, sticky, accordion, footer) meritano un file a parte. Due filosofie di scomposizione diverse
per due pagine diverse: quella lunga (34 sezioni) si spezza per sezione, questa più corta (14 sezioni)
si spezza per comportamento.

---

## 5. LA STRUTTURA MISURATA — 14 sezioni, 13 firme

**13 firme su 14 sezioni (93% uniche).** Solo una coppia si ripete: la sezione 5 (*"Il problema / La
soluzione"*, `firma: section|scroll-mt-16.bg-void|1|-|-|5`) e la sezione 9 (*"Agenzia generalista,
freelancer o assumere?"*) condividono esattamente la stessa firma strutturale — stesso schema di
layout, stesso conteggio di livelli, nessun media, nessuna CTA.

Da confronto con lo studio già fatto sull'ecosistema (dossier 12): `claude-speedrun.com` fa 34/32
(94% uniche su una pagina **quasi tre volte più lunga**), `armageddon` 4/4 (100%), `/outemail`
(Squarespace) 24/16 (67% uniche, 8 sezioni fotocopiate). **`apsales.eu` si comporta come i due siti
costruiti bene dello stesso ecosistema, non come quello a page-builder** — conferma da una **terza
fonte** la regola già scritta nel dossier 12: *più la pagina è lunga, più le sezioni devono essere
strutturalmente diverse*, e qui vale anche su una pagina breve (12.565px contro i 33.756px dell'altro
sito).

---

## 6. I DIFETTI REALI — misurati sui nuovi dati

1. **Contrasto sotto WCAG AA, confermato dalla palette.** `palette_testo` mostra 19 usi a opacità
   `.5`, 19 a `.35`, 16 a `.6` su fondo `oklch(0.1448 0.002 285)` (`#0a0a0b`, quasi nero): stesso
   difetto già misurato nel rapporto 08, ora confermato dai numeri della nuova cattura.
2. **Filtro SVG dichiarato ma non risolvibile nei chunk analizzati** (`url("#luma-alpha")`,
   `url("#luma-alpha-band")`, §3): se il nodo `<filter>` non viene renderizzato per qualche motivo di
   caricamento, l'immagine che lo referenzia perde l'effetto invece di fallire in modo visibile —
   rischio plausibile, non verificato in questo studio.
3. **Discrepanza fra codice e screenshot sul footer** (§3): il componente dichiara `bg-blue`, la
   cattura automatica mostra fondo nero. O la tecnica `fixed`+`clipPath` sfugge alla cattura a
   sezione, o il rendering reale in scroll differisce da quanto il solo screenshot suggerisce — va
   verificato a mano, non deciso da un ritaglio automatico.
4. **Ancora zero raggi**, tranne `50%` su 2 elementi (misurato identico al rapporto 08): nessun
   `border-radius` su bottoni, card, tabella, input.
5. **Nessun risultato di cliente pubblicato**, confermato anche sui nuovi `media[]`: loghi, foto team,
   wireframe heatmap generico — zero grafici prima/dopo, zero numero di CVR reale. Stesso buco già
   trovato nel rapporto 08, confermato dalla nuova cattura.

---

## 7. IL DELTA ALLA FABBRICA — cosa entra, e cosa no

| # | Cosa | Entra? | Dove / perché |
|---|---|---|---|
| 1 | Componente `Ascii` (immagine bianco-su-nero + `mix-blend-screen` + `contrast/brightness` boost) | **Sì** | pattern nuovo per illustrazioni tecniche/decorative su fondo scuro, Corsia A e B — evita di preparare PNG con alpha a mano |
| 2 | Tecnica del doppio bottone con `clipPath` animato da `requestAnimationFrame` per far "fondere" una CTA fissa con la sezione che le scorre sopra | **Sì, da valutare** | utile solo se una nostra CTA fissa deve attraversare zone di colore diverso; da tenere come pattern disponibile, non da applicare a forza |
| 3 | Le 13 maschere di dissolvenza ai bordi (marquee orizzontale, rumore verticale, mirino radiale) | **Parzialmente** | il principio (fade ai bordi di un marquee/pattern invece di un taglio netto) è generico e utile; i 13 valori esatti sono su misura di questa pagina e non si copiano 1:1 |
| 4 | I token colore (`--brand-*`) | **No** | nessuna sovrapposizione con `canone.css`: il loro blu è l'opposto del nostro arancione; i due neutri coincidono per coincidenza di settore, non per prestito reciproco — niente da importare |
| 5 | Lo stack (TanStack Start al posto di Next) | **No, solo conferma** | non cambia il nostro obbligo Next+Tailwind+shadcn+Radix in `site-premium-builder`; utile sapere che un concorrente diretto usa un meta-framework alternativo con lo stesso fondamento (React+Tailwind+shadcn+Radix) |
| 6 | La regola delle firme (sezioni strutturalmente distinte) | **No, solo conferma** | già acquisita dal dossier 12 con una fonte; qui arriva una terza conferma indipendente, utile per irrigidire il gate futuro "firme ripetute / sezioni totali sotto soglia", non per crearne uno nuovo |

**In sintesi: due elementi nuovi entrano davvero (`Ascii`, il doppio-bottone a clip animato); il
resto o non entra (i token, per assenza di sovrapposizione) o conferma da una fonte in più regole già
scritte altrove.**

---

## Connessioni

- [08-apsales.md](08-apsales.md) — il primo passaggio: copy, palette, struttura, le 9 mosse da copiare
- [12-claude-speedrun-STACK-E-TOKEN.md](12-claude-speedrun-STACK-E-TOKEN.md) — lo stesso tipo di studio sull'altro sito costruito bene dell'ecosistema, dove i token coincidevano davvero coi nostri
- [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md) — la tavola per sezione di questa stessa cattura
- `.claude/skills/fabbrica-siti/canone/canone.css` — dove i due elementi del §7 vanno a finire, se confermati in produzione
- `PIANO-MAESTRO/33-PIANO-STUDIO-TOTALE-ANDREI-PASCU.md`
