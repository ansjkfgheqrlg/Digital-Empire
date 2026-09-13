---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #funnel-operator #stile #design-system #palette #tipografia #reference
Created: 2026-09-13
Last updated: 2026-09-13
---

# STILE — funneloperator.it: colori, tipografia, superfici, effetti, movimento

**Ogni valore di questo documento viene dai file della cattura**, mai stimato a occhio: il CSS servito intero (`capture/66-funneloperator-it/src/38-styles-Cm6i-gBj.css`, 148.142 byte), i token campionati dal DOM (`scheda.json`, `design-tokens.json`), il bundle React che assegna le classi (`src/36-routes-DT2uV_Ni.js`, `src/32-raccoglitore-Bj4iyfd5.js`, `src/04-button-rHPgEXhH.js`), l'inventario dei media (`media-inventario.md`) e le 30 schermate di sezione (`sezioni/01..30`). Le conversioni OKLCH→HEX sono calcolate in Python con la trasformazione OKLab→lineare sRGB→gamma (Björn Ottosson), i contrasti con la formula WCAG 2.x.

Sito catturato il 2026-09-13 a 1440px (altezza pagina 32.807px desktop, 36.630px mobile — `scheda.json`, chiavi `altezza`/`altezza_mobile`). Stack dichiarato dal bundle: React + TanStack Router + Tailwind v4 + shadcn/ui (variabili `--radius`, `--sidebar-*`, `--chart-*` sono lo scaffold shadcn, poi sovrascritte dai token `--fo-*` scritti a mano).

Il documento è materiale di lavoro per la Fabbrica Siti: si apre quando si costruisce, non quando si decide. Il confronto col canone Digital Empire è al §9.

---

## 0. La tesi in tre righe

1. **Un solo nero, cinque livelli.** Tutto il fondo scuro è `oklch(17.8% 0 89.9)` = `#111111`, e sopra ci sono quattro grigi neutri a croma zero (`#1b1b1b`, `#222222`, `#2c2c2c`, `#454545`). Nessun colore ha saturazione tranne l'azzurro dell'azione e tre semantici che in pagina non compaiono quasi mai.
2. **Un solo accento, spesso per il testo e quasi mai per i bottoni.** L'azzurro `--fo-blue` `#1d9cd7` compare in 6 sfondi (tutti bottoni) contro 13 occorrenze in testo (`text-fo-blue` 4 + `text-fo-chiaro-blu` 7 + `text-fo-blue-light` 3 nel bundle route) e 2 in decorazione (il gradiente della tabella 01-04). L'accento parla, non spinge.
3. **Niente grana CSS applicata, tanta grana nelle immagini.** La classe `.fo-grain:after` esiste nel CSS con un `feTurbulence` a 4,5% ma non è assegnata da nessun bundle; il fondo misurato negli screenshot è piatto al pixel (dev. standard 0,0 su 200×200 px). La materia arriva dalle WebP: carta (`carta-serpenti.webp`), roccia (`roccia.webp`), incisioni a mezzatinta.

---

## 1. Palette completa

### 1.1 I token, convertiti

Fonte: blocco `:root{...}` a offset 134.789 del CSS servito (`src/38-styles-Cm6i-gBj.css`). Conversione con `scratchpad/oklch.py` (OKLab → LMS → sRGB lineare → gamma 2.4).

```css
/* src/38-styles-Cm6i-gBj.css — :root, i token "fo" scritti a mano (estratto letterale) */
--fo-bg:oklch(17.8% 0 89.9);--fo-surface:oklch(22% 0 89.9);--fo-elevated:oklch(25.1% 0 89.9);
--fo-line:oklch(29.3% 0 89.9);--fo-line-forte:oklch(39.1% 0 89.9);--fo-text:oklch(93.4% 0 89.9);
--fo-muted:oklch(63.3% 0 89.9);--fo-blue:oklch(65.6% .134 235.9);--fo-blue-hover:oklch(54.6% .143 246.7);
--fo-blue-deep:oklch(45.9% .121 247.3);--fo-blue-light:oklch(80.8% .09 238.3);
--fo-chiaro-fondo:oklch(94.6% 0 89.9);--fo-chiaro-testo:oklch(17.8% 0 89.9);--fo-chiaro-muto:oklch(47.3% 0 89.9);
--fo-chiaro-riga:oklch(87% 0 89.9);--fo-chiaro-superficie:oklch(100% 0 89.9);--fo-chiaro-verde:oklch(59.8% .199 143.2);
--fo-chiaro-blu:oklch(61% .14 240.1);--fo-chiaro-riga-foto:oklch(80.6% 0 89.9);--fo-chiaro-nero:oklch(0% 0 0);
--fo-chiaro-testo-alzato:oklch(22% 0 89.9);--fo-chiaro-riga-scura:oklch(51.4% 0 89.9);
--fo-action:var(--fo-blue);--fo-action-hover:var(--fo-blue-light);--fo-action-press:var(--fo-blue-hover);
--fo-on-action:var(--fo-bg);--fo-link:var(--fo-blue);--fo-link-hover:var(--fo-blue-light);
--fo-focus:var(--fo-blue-light);--fo-selected:var(--fo-blue-deep);--fo-velo:oklch(17.8% 0 89.9/.72);
--fo-success-text:oklch(78% .15 155);--fo-success-line:oklch(60% .13 155);--fo-success-surface:oklch(24.5% .045 155);
--fo-warning-text:oklch(84% .145 85);--fo-warning-line:oklch(66% .13 85);--fo-warning-surface:oklch(25% .045 85);
--fo-error-text:oklch(72% .16 25);--fo-error-line:oklch(58% .19 25);--fo-error-surface:oklch(24.5% .06 25);
--fo-error-solid:oklch(52% .21 27);--fo-error-solid-hover:oklch(46% .21 27);
--fo-info-text:var(--fo-blue-light);--fo-info-line:var(--fo-blue-hover);--fo-info-surface:oklch(25% .05 240);
--sagoma-luce:oklch(28.8% 0 89.9);
```

| Token | OKLCH | HEX calcolato | RGB | Ruolo |
|---|---|---|---|---|
| `--fo-bg` | `oklch(17.8% 0 89.9)` | `#111111` | 17,17,17 | fondo scuro di tutta la pagina (body, 14 sezioni) |
| `--fo-surface` | `oklch(22% 0 89.9)` | `#1b1b1b` | 27,27,27 | scheda, bottone outline, fondo video, sfondo miniature rail |
| `--fo-elevated` | `oklch(25.1% 0 89.9)` | `#222222` | 34,34,34 | `.scheda-alta`, hover di outline/ghost, `--riga-passaggio` |
| `--fo-line` | `oklch(29.3% 0 89.9)` | `#2c2c2c` | 44,44,44 | bordo 1px di schede, FAQ, footer, tabella 01-04 |
| `--fo-line-forte` | `oklch(39.1% 0 89.9)` | `#454545` | 69,69,69 | definito, mai referenziato nel bundle route |
| `--sagoma-luce` | `oklch(28.8% 0 89.9)` | `#2b2b2b` | 43,43,43 | picco di luce dello skeleton `.sagoma` |
| `--fo-text` | `oklch(93.4% 0 89.9)` | `#e9e9e9` | 233,233,233 | testo su scuro (non bianco puro) |
| `--fo-muted` | `oklch(63.3% 0 89.9)` | `#8a8a8a` | 138,138,138 | testo secondario, domande FAQ, footer |
| `--fo-chiaro-fondo` | `oklch(94.6% 0 89.9)` | `#ededed` | 237,237,237 | fondo delle 15 sezioni chiare (non bianco) |
| `--fo-chiaro-superficie` | `oklch(100% 0 89.9)` | `#ffffff` | 255,255,255 | scheda su chiaro (surface ed elevated coincidono su chiaro) |
| `--fo-chiaro-testo` | `oklch(17.8% 0 89.9)` | `#111111` | 17,17,17 | testo su chiaro = identico al fondo scuro |
| `--fo-chiaro-testo-alzato` | `oklch(22% 0 89.9)` | `#1b1b1b` | 27,27,27 | = `--fo-surface` |
| `--fo-chiaro-muto` | `oklch(47.3% 0 89.9)` | `#5c5c5c` | 92,92,92 | testo secondario su chiaro |
| `--fo-chiaro-riga` | `oklch(87% 0 89.9)` | `#d4d4d4` | 212,212,212 | bordi su chiaro, fondo delle cartelle del raccoglitore |
| `--fo-chiaro-riga-foto` | `oklch(80.6% 0 89.9)` | `#bfbfbf` | 191,191,191 | bordo 1px attorno alle foto su chiaro |
| `--fo-chiaro-riga-scura` | `oklch(51.4% 0 89.9)` | `#676767` | 103,103,103 | bordo 1px delle foto "scrivania/telefono" e delle miniature rail |
| `--fo-chiaro-nero` | `oklch(0% 0 0)` | `#000000` | 0,0,0 | bordo delle 7 schede "Come funziona" e linee tratteggiate |
| `--fo-blue` | `oklch(65.6% .134 235.9)` | `#1d9cd7` | 29,156,215 | **l'accento**: azione, link, parola evidenziata su scuro |
| `--fo-blue-light` | `oklch(80.8% .09 238.3)` | `#88c9f4` | 136,201,244 | hover del bottone, focus ring, bordo hover FAQ |
| `--fo-blue-hover` | `oklch(54.6% .143 246.7)` | `#0075be` | 0,117,190 | stato :active del bottone (`--fo-action-press`) |
| `--fo-blue-deep` | `oklch(45.9% .121 247.3)` | `#015b97` | 1,91,151 | link su chiaro, tab selezionata |
| `--fo-chiaro-blu` | `oklch(61% .14 240.1)` | `#008cce` | 0,140,206 | parola evidenziata su chiaro (7 usi, il più frequente) |
| `--fo-chiaro-verde` | `oklch(59.8% .199 143.2)` | `#009b12` | 0,155,18 | "Carriera avviata", "Fare landing pages." (2 usi) |
| `--fo-success-text/line/surface` | `oklch(78% .15 155)` / `oklch(60% .13 155)` / `oklch(24.5% .045 155)` | `#59d38c` / `#2c965d` / `#0c2717` | — | semantico, non in home |
| `--fo-warning-text/line/surface` | `oklch(84% .145 85)` / `oklch(66% .13 85)` / `oklch(25% .045 85)` | `#f6c24b` / `#b68b16` / `#2b2005` | — | semantico, non in home |
| `--fo-error-text/line/surface` | `oklch(72% .16 25)` / `oklch(58% .19 25)` / `oklch(24.5% .06 25)` | `#f97770` / `#d33a3c` / `#381311` | — | semantico (toast del bottone acquista: `text-red-400`) |
| `--fo-error-solid` / `-hover` | `oklch(52% .21 27)` / `oklch(46% .21 27)` | `#c50516` / `#b00000` (fuori gamut, clippato) | — | variante `destructive` del bottone |
| `--fo-info-surface` | `oklch(25% .05 240)` | `#062437` | 6,36,55 | semantico, non in home |
| `--fo-velo` | `oklch(17.8% 0 89.9/.72)` | `#111111` al 72% | — | velo dialog (raccoglitore aperto) |
| letterale | `#BD0000` | `#bd0000` | 189,0,0 | **solo** la parola "morirai" (h1) e "L'AI ti ruba il lavoro." barrato |
| letterale | `#676767` | `#676767` | 103,103,103 | bordo delle 3 carte hero (= `--fo-chiaro-riga-scura`, scritto a mano) |

Nota di metodo: l'hue 89.9 su croma 0 è irrilevante (grigio puro); l'autore l'ha lasciato come firma del tool di generazione (Tailwind v4 esporta i neutri così). Tutti i grigi hanno croma **esattamente 0**: la palette scura è acromatica al 100%.

### 1.2 Quante volte e dove (campionamento DOM)

Fonte: `scheda.json` → `palette_testo`, `palette_sfondi` (conteggio degli elementi testuali/sfondo campionati).

**Colori di testo** (12 distinti):

| Colore campionato | Occorrenze | Cos'è |
|---|---|---|
| `oklch(0.178 0 89.9)` = #111111 | 111 | testo su sezioni chiare (`--fo-chiaro-testo`) |
| `oklch(0.934 0 89.9)` = #e9e9e9 | 78 | testo su sezioni scure (`--fo-text`) |
| `oklch(0.633 0 89.9)` = #8a8a8a | 51 | muted su scuro: domande FAQ (26), footer, sottotitoli |
| `#ffffff` | 15 | prezzo, "FUNNEL", contatore, testo bottone "Sono pronto", h1 |
| `oklch(0.473 0 89.9)` = #5c5c5c | 7 | muted su chiaro |
| `oklch(0.61 0.14 240.1)` = #008cce | 7 | parola evidenziata su chiaro |
| `oklch(0.656 0.134 235.9)` = #1d9cd7 | 6 | parola evidenziata su scuro + "Accedi →" |
| `oklch(0.87 0 89.9)` = #d4d4d4 | 4 | numero della linguetta del raccoglitore |
| `#bd0000` | 2 | "morirai", "L'AI ti ruba il lavoro." |
| `oklch(0.459 0.121 247.3)` = #015b97 | 2 | link su chiaro ("questo" studio SEC, Trustpilot) |
| `oklch(0.598 0.199 143.2)` = #009b12 | 2 | verde "Carriera avviata" / "Fare landing pages." |
| `oklch(0.808 0.09 238.3)` = #88c9f4 | 2 | testo azzurro chiaro (tab attiva raccoglitore) |

**Colori di sfondo** (10 distinti):

| Sfondo campionato | Occorrenze | Cos'è |
|---|---|---|
| `oklch(0.22 0 89.9)` = #1b1b1b | 38 | `.scheda`, tab 01-04, bottone outline, video, miniature |
| `oklch(0.178 0 89.9)` = #111111 | 23 | sezioni scure, carte hero, linguette raccoglitore |
| `oklch(0.946 0 89.9)` = #ededed | 23 | sezioni chiare |
| `oklch(0.656 0.134 235.9)` = #1d9cd7 | 6 | **bottoni primari** (Iscriviti adesso, Sono pronto, Ottieni accesso + duplicati mobile) |
| `oklch(0.87 0 89.9)` = #d4d4d4 | 6 | cartelle del raccoglitore |
| `oklab(0 0 0 / 0.45)` | 2 | cerchio play sul video (`bg-black/45`) |
| `oklch(1 0 0)` | 1 | body (mai visibile: coperto da `main.bg-fo-bg`) |
| `oklch(0.293 0 89.9)` = #2c2c2c | 1 | separatore |
| `oklch(0.178 0 89.9) (+img)` | 1 | sezione "Diventa funnel operator" con `roccia.webp` |
| `oklch(1 0 89.9)` | 1 | scheda bianca su chiaro |

### 1.3 I neri: quanti livelli di scuro

Cinque, tutti acromatici, tutti separati da 3-5 punti di L in OKLCH — una scala percettivamente uniforme:

| L | HEX | Token | Contrasto col fondo |
|---|---|---|---|
| 17,8% | `#111111` | `--fo-bg` | — |
| 22,0% | `#1b1b1b` | `--fo-surface` | 1,10:1 |
| 25,1% | `#222222` | `--fo-elevated` | 1,19:1 |
| 28,8% | `#2b2b2b` | `--sagoma-luce` | 1,30:1 |
| 29,3% | `#2c2c2c` | `--fo-line` | 1,35:1 |
| 39,1% | `#454545` | `--fo-line-forte` | 2,0:1 (non usato) |

Il bordo `--fo-line` su `--fo-bg` ha contrasto 1,35:1: è un filetto *appena* visibile, voluto così (vedi FAQ, sezione 29: le righe si vedono ma non pesano). Il passo `--fo-surface` → `--fo-elevated` è 1,08:1: la scheda alta si distingue dalla scheda solo per un soffio, e infatti nel bundle `.scheda-alta` non è usata (0 occorrenze), solo `.scheda` (2).

### 1.4 I chiari

Tre: `#ededed` (fondo), `#ffffff` (scheda, testo forte), `#d4d4d4` (riga/cartella). Il fondo chiaro **non è bianco**: 94,6% di L, e il bianco puro è riservato alle superfici che devono staccare (la scheda `.scheda` su chiaro diventa `#ffffff` grazie al rimapping in `.sezione-chiara`).

### 1.5 L'accento: uno solo, e dove si spende

L'accento è **un solo azzurro** in quattro luminosità (deep 45,9% → hover 54,6% → base 65,6% → light 80,8%), tutte attorno a hue 236-247. Il gradiente della tabella 01-04 è la scala stessa messa in fila:

```css
/* src/38-styles-Cm6i-gBj.css — utilities */
.bg-\[linear-gradient\(90deg\,\#88C9F4_0\%\,\#1E9CD7_33\%\,\#0075BE_66\%\,\#005B97_100\%\)\]{background-image:linear-gradient(90deg,#88c9f4 0%,#1e9cd7 33%,#0075be 66%,#005b97 100%)}
@media (width>=64rem){.lg\:bg-\[linear-gradient\(180deg\,\#88C9F4_0\%\,\#1E9CD7_33\%\,\#0075BE_66\%\,\#005B97_100\%\)\]{background-image:linear-gradient(#88c9f4 0%,#1e9cd7 33%,#0075be 66%,#005b97 100%)}}
```

`#88C9F4` = `--fo-blue-light`, `#1E9CD7` = `--fo-blue` (calcolato `#1d9cd7`, 1 punto di differenza per arrotondamento), `#0075BE` = `--fo-blue-hover`, `#005B97` = `--fo-blue-deep` (calcolato `#015b97`). Il gradiente è stato scritto a mano coi valori HEX dei token: **una scala, non un gradiente inventato**.

Conteggio dell'uso dell'accento nel bundle route (`36-routes-DT2uV_Ni.js`) + shell (`29-index-CLKYm5hM.js`):

| Uso | Classi | Occorrenze | Esempi |
|---|---|---|---|
| **Bottoni** (sfondo) | variant `default` → `bg-fo-action` via `buttonVariants` | 3 istanze in home (Sono pronto, Iscriviti adesso, Ottieni accesso) + Accedi (link) | sezioni 19, 28, sticky |
| **Testo** | `text-fo-blue` 4, `text-fo-chiaro-blu` 7, `text-fo-blue-light` 3, `text-fo-link` 2 | **16** | "funnel operator", "ho scelto", "3 siti", "28 test", "28 servizi", "Funnel Operator", "carta leggendaria", "OPERATOR", "Telegram", "cambiare vita", "qui" |
| **Decorazione** | gradiente 01-04 (2), `border-fo-blue-light` hover (5), `border-fo-chiaro-blu` (1: la scheda "2."), logomark gradiente SVG (1) | 9 | tabella percorso, FAQ hover, scheda "2.", logo |

Rapporto: **testo 16 : decorazione 9 : bottoni 3**. L'accento si spende in **una parola per titolo**, quasi sempre l'ultima o il nome del prodotto. I bottoni sono pochi per scelta: nella pagina di 32.807px ci sono 3 CTA primarie (più la sticky).

### 1.6 I colori semantici

Definiti ma fuori dalla home: `--fo-success-*`, `--fo-warning-*`, `--fo-error-*`, `--fo-info-*`. Struttura a tre livelli (text / line / surface) con L rispettivamente ~78 / ~60 / ~25 e croma ~0,15 / ~0,13 / ~0,045: **le superfici semantiche hanno la stessa luminosità dell'elevated** (25%), tinte appena. Sono tokens dell'area riservata (`/auth`, `.lezione`), non della pagina di vendita.

Il rosso `#BD0000` non è un semantico: è un letterale usato due volte, per la morte e per l'AI barrata. Contrasto su `#111111`: 2,84:1 — non passa AA per il testo, ma è a 290px (h1) e 49px (barrato), fuori dalla soglia del testo lungo.

### 1.7 Contrasti misurati (WCAG)

| Coppia | Contrasto | Esito |
|---|---|---|
| `--fo-text` #e9e9e9 su `--fo-bg` #111111 | 15,55:1 | AAA |
| `--fo-muted` #8a8a8a su `--fo-bg` | 5,47:1 | AA (usato per le domande FAQ a 22px) |
| `--fo-blue` #1d9cd7 su `--fo-bg` | 6,10:1 | AA |
| `--fo-bg` #111111 su `--fo-blue` (testo del bottone "Iscriviti adesso") | 6,10:1 | AA |
| `#ffffff` su `--fo-blue` (testo del bottone "Sono pronto", `text-white`) | **3,09:1** | fallisce AA a 14px |
| `--fo-chiaro-testo` #111111 su `--fo-chiaro-fondo` #ededed | 16,13:1 | AAA |
| `--fo-chiaro-muto` #5c5c5c su chiaro | 5,71:1 | AA |
| `--fo-chiaro-blu` #008cce su chiaro | **3,18:1** | fallisce AA (ma è a 37-49px) |
| `#bd0000` su `--fo-bg` | 2,84:1 | fallisce (h1 290px) |

Difetto misurato: il bottone "Sono pronto" (sezione 28) forza `text-white` sul blu e scende a 3,09:1, mentre il bottone canonico usa `--fo-on-action` = `--fo-bg` (nero su azzurro, 6,10:1). Due bottoni primari, due colori di testo diversi: incoerenza reale, verificabile in `scheda.json` → `cta[0].color = oklch(0.178…)` contro `cta[10].color = #ffffff`.

---

## 2. Tipografia

### 2.1 Le famiglie e chi fa cosa

Fonte: `@layer theme` (offset 2.526) e `@font-face` (13 blocchi) nel CSS servito.

```css
/* src/38-styles-Cm6i-gBj.css — @layer theme */
--font-sans:"Inter Tight", "Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
--font-mono:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
--font-display:"Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
--font-lapide:"Curseyt", "Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
--default-font-family:"Inter Tight", "Plus Jakarta Sans", ui-sans-serif, system-ui, sans-serif;
```

```css
/* @layer base */
body{background-color:var(--color-background);color:var(--color-foreground);font-family:var(--font-sans)}
h1,h2,h3,h4,h5,h6{font-family:var(--font-display)}
```

| Famiglia | Variabile | Ruolo | Pesi serviti | Campionamento DOM (`scheda.json` → `caratteri`) |
|---|---|---|---|---|
| **Inter Tight** | `--font-sans` | corpo, interfaccia, didascalie, bottoni, footer | 400-700 variabile (normal + italic), latin + latin-ext | 172 elementi |
| **Plus Jakarta Sans** | `--font-display` | tutti gli heading h1-h6, `.titolo-*`, prezzo, numeri grandi | 200-800 variabile (normal + italic) | 102 elementi |
| **DM Mono** | `.font-tech` / `.codice` | numeri 01-04 della tabella, etichette FAQ ("FUNNEL OPERATOR", "PAGAMENTO"), unità del contatore (giorni/ore), indice lezioni | 400 e 500 statici | 10 elementi |
| **Curseyt** | `--font-lapide` | **solo** l'h1 "Un giorno morirai." (gotico/blackletter) | 400, `font-display:block` | 3 elementi (h1 + 2 span) |

La parola "lapide" nel nome del token dice tutto: il gotico è la lapide. Il corsivo non è una famiglia: è Inter Tight italic (`<em class="font-bold italic">chiarissimi</em>`, `<p class="font-medium italic">«Chi fa costruire…»</p>`), mentre `<em>` viene spesso **neutralizzato** con `not-italic` per usare l'enfasi solo come colore (`<em class="not-italic text-fo-blue">3 siti</em>`).

### 2.2 Come sono servite

Tutte **self-hosted** da `/caratteri/`, formato woff2 unico, con `unicode-range` split latin / latin-ext (13 `@font-face` in totale). Niente Google Fonts, niente terze parti.

```css
/* src/38-styles-Cm6i-gBj.css — @font-face (i 4 significativi) */
@font-face{font-family:Curseyt;src:url(/caratteri/curseyt.woff2)format("woff2");font-weight:400;font-style:normal;font-display:block}
@font-face{font-family:DM Mono;font-style:normal;font-weight:400;font-display:swap;src:url(/caratteri/dm-mono-400-normal-latin.woff2)format("woff2");unicode-range:U+??,U+131,U+152-153,...}
@font-face{font-family:Inter Tight;font-style:normal;font-weight:400 700;font-display:swap;src:url(/caratteri/inter-tight-400-700-normal-latin.woff2)format("woff2");unicode-range:U+??,U+131,...}
@font-face{font-family:Plus Jakarta Sans;font-style:italic;font-weight:200 800;font-display:swap;src:url(/caratteri/plus-jakarta-sans-200-800-italic-latin-ext.woff2)format("woff2");unicode-range:U+100-2BA,...}
```

Regola implicita: **`font-display:block` solo su Curseyt** (il carattere È il design dell'h1, come su armageddon), `swap` su tutto il resto. Stessa scelta già letta in `reports/11-armageddon-ATLANTE-VISIVO.md`.

### 2.3 La scala: token e classi semantiche

Tailwind è stato **ri-tarato**: `--text-base` non è 16px ma **17px** (`1.0625rem`), e ogni misura porta il proprio `line-height` e `letter-spacing` di default.

```css
/* @layer theme */
--text-base:1.0625rem;--text-base--line-height:1.6;--text-lg:1.375rem;--text-lg--line-height:1.4;--text-6xl:3.75rem;--text-6xl--line-height:1;
--tracking-tight:-.025em;--tracking-normal:0em;--tracking-wide:.025em;--tracking-widest:.1em;
--leading-tight:1.25;--leading-normal:1.5;--leading-relaxed:1.625;--text-sm--letter-spacing:.03em
```

```css
/* @layer utilities — la scala ridefinita */
.text-xs{font-size:.75rem;line-height:var(--tw-leading,1.5);letter-spacing:var(--tw-tracking,.035em)}
.text-sm{font-size:.875rem;line-height:var(--tw-leading,1.5);letter-spacing:var(--tw-tracking,.03em)}
.text-base{font-size:1.0625rem;line-height:var(--tw-leading,1.6);letter-spacing:var(--tw-tracking,.025em)}
.text-lg{font-size:1.375rem;line-height:var(--tw-leading,1.4);letter-spacing:var(--tw-tracking,-.005em)}
.text-xl{font-size:1.8125rem;line-height:var(--tw-leading,1.3);letter-spacing:var(--tw-tracking,-.01em)}
.text-2xl{font-size:2.3125rem;line-height:var(--tw-leading,1.2);letter-spacing:var(--tw-tracking,-.015em)}
.text-3xl{font-size:3.0625rem;line-height:var(--tw-leading,1.15);letter-spacing:var(--tw-tracking,-.02em)}
.text-4xl{font-size:clamp(2.3125rem,1.639rem + 2.873vw,3.9375rem);line-height:var(--tw-leading,1.1);letter-spacing:var(--tw-tracking,-.025em)}
.text-5xl{font-size:clamp(3.0625rem,2.208rem + 3.646vw,5.125rem);line-height:var(--tw-leading,1.05);letter-spacing:var(--tw-tracking,-.03em)}
```

Le classi semantiche in italiano (le "voci" della pagina):

```css
/* @layer utilities — le voci */
.didascalia{font-family:Inter Tight,Plus Jakarta Sans,ui-sans-serif,system-ui,sans-serif;font-size:.75rem;line-height:var(--tw-leading,1.5);letter-spacing:var(--tw-tracking,.035em);--tw-font-weight:var(--font-weight-normal);font-weight:var(--font-weight-normal)}
.interfaccia{font-family:Inter Tight,Plus Jakarta Sans,ui-sans-serif,system-ui,sans-serif;font-size:.875rem;line-height:var(--tw-leading,1.5);letter-spacing:var(--tw-tracking,.03em);--tw-font-weight:var(--font-weight-medium);font-weight:var(--font-weight-medium)}
.codice{font-family:DM Mono,ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.875rem;line-height:var(--tw-leading,1.5);letter-spacing:var(--tw-tracking,.03em);--tw-font-weight:var(--font-weight-normal);font-weight:var(--font-weight-normal)}
.corpo{font-family:Inter Tight,Plus Jakarta Sans,ui-sans-serif,system-ui,sans-serif;font-size:1.0625rem;line-height:var(--tw-leading,1.6);letter-spacing:var(--tw-tracking,.025em);--tw-font-weight:var(--font-weight-normal);font-weight:var(--font-weight-normal)}
.titolo-blocco{font-family:Plus Jakarta Sans,ui-sans-serif,system-ui,sans-serif;font-size:1.375rem;line-height:var(--tw-leading,1.4);letter-spacing:var(--tw-tracking,-.005em);--tw-font-weight:var(--font-weight-semibold);font-weight:var(--font-weight-semibold)}
.titolo-scheda{font-family:Plus Jakarta Sans,ui-sans-serif,system-ui,sans-serif;font-size:1.8125rem;line-height:var(--tw-leading,1.3);letter-spacing:var(--tw-tracking,-.01em);--tw-font-weight:var(--font-weight-semibold);font-weight:var(--font-weight-semibold)}
.titolo-sezione{font-family:Plus Jakarta Sans,ui-sans-serif,system-ui,sans-serif;font-size:2.3125rem;line-height:var(--tw-leading,1.2);letter-spacing:var(--tw-tracking,-.015em);--tw-font-weight:var(--font-weight-bold);font-weight:var(--font-weight-bold)}
.titolo-pagina{font-family:Plus Jakarta Sans,ui-sans-serif,system-ui,sans-serif;font-size:clamp(3.0625rem,2.208rem + 3.646vw,5.125rem);line-height:var(--tw-leading,1.05);letter-spacing:var(--tw-tracking,-.03em);--tw-font-weight:var(--font-weight-bold);font-weight:var(--font-weight-bold)}
.titolo-gancio{font-family:var(--font-display);letter-spacing:-.0376em;font-size:clamp(1.375rem,1.0361rem + 1.3487vw,2.25rem);font-weight:500;line-height:1.003}
.titolo-garanzia{font-family:var(--font-display);letter-spacing:-.035em;font-size:clamp(1.6875rem,1.4454rem + .9634vw,2.3125rem);font-weight:500;line-height:1.003}
.titolo-chiusura{font-family:var(--font-display);letter-spacing:-.035em;font-size:clamp(1.6875rem,1.155rem + 2.1195vw,3.0625rem);font-weight:700;line-height:1.003}
.titolo-offerta{font-family:var(--font-display);letter-spacing:-.06em;font-size:clamp(3.125rem,4.252rem - 1.2524vw,3.9375rem);font-weight:800;line-height:1.003}
.titolo-gaia{font-family:var(--font-display);font-weight:700;line-height:1.003;letter-spacing:-.036em!important}
.etichetta-confronto{font-family:var(--font-display);letter-spacing:-.03em;font-size:2.0625rem;font-weight:700;line-height:1.003}
.lapide-uno{font-family:var(--font-lapide);letter-spacing:-.03em;font-size:min(29.85vw,220px);font-weight:400;line-height:.67}
.lapide-due{font-family:var(--font-lapide);letter-spacing:-.03em;font-size:min(29.85vw,290px);font-weight:400;line-height:.67}
```

Curiosità reale: `.titolo-offerta` ha un clamp **decrescente** (`4.252rem - 1.2524vw`): il titolo "FUNNEL OPERATOR" è più grande su mobile (63px) che su desktop (50px), perché su desktop convive con la tessera.

### 2.4 La scala completa campionata (px / line-height / peso), ordinata

Fonte: `scheda.json` → `scala_tipografica` (top 40 combinazioni). Riordinata per corpo.

| Corpo | line-height | peso | occorrenze | Cos'è |
|---|---|---|---|---|
| 14px | 21px (1,5) | 500 | 18 | `.interfaccia`: bottoni, nav, footer, tab |
| 14px | 21px | 400 | 6 | `.codice`: unità contatore, etichette FAQ |
| 16px | 24px | 400 | 5 | consenso cookie (`text-sm` di shadcn), disclaimer |
| 17px | 27,2px (1,6) | 400 | **28** | `.corpo`: il paragrafo standard |
| 17px | 22,1px (1,3) | 400 | 13 | `.corpo leading-[1.3]` |
| 17px | 20,57px (1,21) | 400 | 7 | `.corpo leading-[1.21] text-justify` (storia) |
| 17px | 20,23px (1,19) | 400 | 6 | `.corpo leading-[1.19]` (crisi 2025) |
| 17px | 19,89px (1,17) | 400 | 18 | `.corpo leading-[1.17]` (28 test, AI) |
| 17px | 17px (1,0) | 400 | 16 | `.corpo leading-none` (elenchi sotto le foto) |
| 17px | 27,2px | 700 | 3 | `<strong>` nel corpo |
| 18,9px | 28,4px | 500 | 8 | linguette raccoglitore (`--corpo: max(13px, 2.275cqw)`) |
| 22px | 30,8px (1,4) | 500 | **22** | domande FAQ + accordion consulenza (`text-lg font-medium`) |
| 22px | 30,8px | 700 | 6 | `.titolo-blocco text-lg font-bold` (h3 tabella 01-04) |
| 22px | 25,74px (1,17) | 400 | 4 | i 3 motivi (teschio/spade/lapide) |
| 29px | 29px (1,0) | 600 | 11 | `.titolo-blocco text-xl leading-none` ("Step 1..7") |
| 29px | 29px | 700 | 4 | `.titolo-scheda` |
| 37px | 44,4px (1,2) | 700 | **18** | `.titolo-sezione` (h2 standard) |
| 37px | 37,1px (1,003) | 700/500 | 6 | `.etichetta-confronto`, `.titolo-gaia` |
| 49px | 56,35px (1,15) | 700 | 5 | `.text-3xl` h2 grandi |
| 49px | 49px (1,0) | 500/600/700 | 8 | h2 "leading-none" ("Il corso copre…", "Registrazioni…") |
| 49px | 57,82px (1,18) | 700 | 3 | "Ho fatto 28 test…" |
| 49px | 59,29px (1,21) | 500 | 2 | "Esempi di pagine fatte da" |
| 50px | 50,15px | 800 | 2 | `.titolo-offerta` desktop ("FUNNEL OPERATOR") |
| 63px | 69,3px (1,1) | 800 | 4 | `.text-4xl` ("Asset pronti per te", "Come funziona") |
| 63px | 63px (1,0) | 600 | 2 | "Diventa funnel operator oggi" |
| 81px | 81,2px | 800 | 2 | il prezzo "434 €" (`text-5xl font-extrabold tracking-[-0.04em]`), "1." / "2." (`text-[81px] tracking-[-0.15em]`) |
| 290px | 194,3px (0,67) | 400 | 2 | "morirai" e "." in Curseyt (`.lapide-due`) |

**Corpi distinti: 14 · 16 · 17 · 18,9 · 22 · 29 · 37 · 49 · 50 · 63 · 81 · 290 = 12 valori**, di cui 5 sono la spina dorsale (14, 17, 22, 37, 49). Il rapporto tra un gradino e il successivo è ≈1,3 (14→17→22→29→37→49→63→81: fattore 1,21-1,32, una scala "major third" leggermente irregolare).

### 2.5 Letter-spacing e text-transform

- **Corpo positivo**: `.corpo` +0,025em, `.interfaccia`/`.codice` +0,03em, `.didascalia` +0,035em. Più il testo è piccolo, più è spaziato.
- **Titoli negativi e crescenti col corpo**: `-.005em` (22px) → `-.01em` (29) → `-.015em` (37) → `-.02em` (49) → `-.025em` (63) → `-.03em` (81) → `-.06em` (`.titolo-offerta`) → **`-.15em`** sui numeri "1."/"2." (`tracking-[-0.15em]`). Il tracking più stretto in pagina è sulle cifre giganti.
- Classi arbitrarie nel CSS: `-0.008em, -0.01em, -0.02em, -0.03em, -0.04em, -0.15em, 0.2em, 0.4em, 0.5em` (le tre positive larghe non sono nel bundle home, restano dal dominio auth).
- **`text-transform: uppercase`: 1 solo uso** nel bundle route — "LA CRISI DEL 2025" (`text-4xl font-bold uppercase`). Le etichette FAQ ("FUNNEL OPERATOR", "PAGAMENTO") sono scritte maiuscole nel testo, in DM Mono azzurro. Non c'è nessun occhiello maiuscolo tracciato largo: il pattern "eyebrow uppercase tracking-widest" **è assente**.
- `text-balance` su tutti gli h2 via `T()` (`titolo-sezione text-balance`), `text-justify` su **25** paragrafi lunghi (le sezioni-lettera: storia, crisi, 28 test, AI). Giustificato con `leading-[1.17..1.22]`: è la voce "lettera di vendita", diversa dal `.corpo` 1,6 dei paragrafi brevi.
- `tabular-nums` su tutte le cifre (numeri Trustpilot/ordini, contatore, `dt` delle schede).

### 2.6 Larghezza massima del testo

```css
/* @layer utilities */
.colonna{width:100%;max-width:calc(var(--colonna) + var(--margine-pagina) * 2);padding-inline:var(--margine-pagina);margin-inline:auto}
/* :root */ --colonna:832px;--modulo:400px;--finestra:520px;--barra:256px;--margine-pagina:24px;
```

- **Colonna di testo: 832px** (880 col padding). Verificato in `scheda.json`: blocchi testo a `x:304`, larghezza 832, `(1440-832)/2 = 304`.
- A 17px Inter Tight, 832px sono ≈ **95-100 caratteri per riga** nei paragrafi giustificati: **sopra** il canone tipografico dei 65-75ch. Andrei lo compensa con `text-justify` + interlinea stretta (1,17-1,22), ottenendo un blocco compatto "da lettera".
- Restringimenti dichiarati: `max-w-[534px]` (crisi 2025), `max-w-[580px]` (Fare siti), `max-w-[598px]` (i 3 motivi), `max-w-[618px]` (tabella), `max-w-[666px]` ("Ma chi cazzo…"), `max-w-[11em]` (sottotitolo hero), `max-w-[28ch]`, `max-w-prose` (65ch, shadcn, non in home).
- `--modulo: 400px` è la larghezza dei form (auth), `--finestra: 520px` dei dialog, `--barra: 256px` della sidebar.

### 2.7 Il rapporto heading/body

h2 standard 37px / corpo 17px = **2,18**. h2 grande 49/17 = 2,88. h2 "gancio" (`.titolo-gancio`, 36px desktop) usato come **paragrafo a tre righe centrato** ("Le aziende le vogliono. / Non le trovano. / E son disposte a pagare tanto") — la voce a metà tra titolo e corpo, peso 500. Il bottone (14px) è **più piccolo del corpo** (17px): l'azione non grida.

---

## 3. Griglia e spazi

### 3.1 La colonna e le variabili di misura

```css
/* :root — misure */
--spazio-blocchi:clamp(32px, 7.5vw, 48px);--spazio-sezioni:clamp(40px, 10vw, 64px);
--spazio-vendita:clamp(56px, 15vw, 96px);--spazio-area:clamp(64px, 17.5vw, 112px);
--scheda-dentro:16px;--scheda-riga:8px;--colonna:832px;--modulo:400px;--finestra:520px;--barra:256px;
--margine-pagina:24px;--griglia-colonne:12;--griglia-colonna:40px;--griglia-canale:32px;
--bottone-minimo:7.5rem;--piede-campo:1.125rem;
@media (width>=640px){:root{--scheda-dentro:24px;--scheda-riga:12px}}
```

- Griglia dichiarata: **12 colonne × 40px + 11 canali × 32px = 832px**. La colonna non è un numero a caso, è la somma della griglia.
- Nessun `container` Tailwind: una sola classe `.colonna`.
- Le larghezze interne sono **frazioni della colonna scritte come calc**: `md:basis-[calc(100%*299/832)]`, `[calc(100%*351/832)]`, `[calc(100%*428/832)]`, `[calc(100%*447/832)]`, `[calc(100%*336/832)]`, `basis-[calc(100%*494/598)]`. Il designer ha misurato in Figma a 832 e trascritto la frazione: la pagina scala come un'immagine.
- Il raccoglitore usa **container query units**: `[--gradino:max(48px,7.239cqw)] [--linguetta:max(46px,6.826cqw)] [--sporgenza:max(37px,5.481cqw)] [--taglio:calc(var(--linguetta)*0.246)] [--fianco:max(12px,3.5cqw)] [--corpo:max(13px,2.275cqw)]` su un `@container` largo max 967px (`src/32-raccoglitore-Bj4iyfd5.js`).

### 3.2 Padding verticale delle sezioni

Ogni sezione è `py-vendita` = `clamp(56px, 15vw, 96px)` → **96px a 1440**, 56px sotto 373px. Quattro tempi disponibili (blocchi 32-48 / sezioni 40-64 / vendita 56-96 / area 64-112) ma la home usa quasi solo `vendita`; `mt-blocchi` (48px) separa titolo e contenuto dentro la sezione; `mt-sezioni` (64px) e `mt-vendita` (96px) i sotto-blocchi. Eccezioni scritte a mano: `pt-[103px] pb-[92px]` sull'offerta, `mt-[78px]`, `mt-[94px]`, `mt-[53px] md:mt-[97px]`.

Misurato sulle 30 sezioni (`scheda.json` → `sezioni[].h`): altezza mediana ~930px; la più bassa il rail-numeri (273px, `py-0!` con `py-10` interno), la più alta "Troverai veramente clienti?" (2.301px).

### 3.3 Gap

56 valori di gap nel CSS. I ricorrenti: `gap-4` (16px, griglie schede), `gap-blocchi` (48), `gap-scheda` (16/24), `gap-[22px]`, `gap-[35px]`, `gap-[38px]`, `gap-[45px]`, `gap-[49px]`, `gap-[60px]`, `gap-[61px]`, `gap-24` (96px, rail numeri). Gap in **em** per i paragrafi giustificati: `gap-[1.17em]`, `[1.19em]`, `[1.21em]`, `[1.22em]` — **l'interparagrafo è uguale all'interlinea** della sezione (leading 1,17 ↔ gap 1,17em): il blocco di testo respira alla stessa misura dentro e fuori la riga.

### 3.4 Raggi (tutti)

```css
/* :root */ --radius:.5rem;
/* @layer theme */ --radius-sm:calc(var(--radius) - 4px);--radius-md:calc(var(--radius) - 2px);--radius-lg:var(--radius);
/* utilities */
.rounded-sm{border-radius:calc(var(--radius) - 4px)}  /* 4px */
.rounded-md{border-radius:calc(var(--radius) - 2px)}  /* 6px */
.rounded-lg{border-radius:var(--radius)}              /* 8px — bottoni, foto, .scheda */
.rounded-xl{border-radius:calc(var(--radius) + 4px)}  /* 12px — foto con bordo, raccoglitore */
.rounded-2xl{border-radius:calc(var(--radius) + 8px)} /* 16px */
.rounded-4xl{border-radius:calc(var(--radius) + 16px)}/* 24px — le 7 schede "Come funziona" */
.rounded-5xl{border-radius:calc(var(--radius) + 24px)}/* 32px */
.rounded-\[5px\]{border-radius:5px}   /* miniature del rail esempi */
.rounded-\[13px\]{border-radius:13px} /* le 3 carte hero */
.rounded-\[15px\]{border-radius:15px} /* schede "1." e "2." */
.rounded-t-\[12px\]{...}              /* immagine dentro la carta hero (13 - 1px bordo) */
.rounded-full{border-radius:3.40282e38px} /* avatar, play, "?" FAQ */
```

Campionati nel DOM (`scheda.json` → `raggi`): **8px ×52**, 5px ×36, pill ×21, 12px ×8, 24px ×7, 4px ×7, 13px ×3, 10px ×3, 15px ×2. Il raggio dominante è **8px** (una `--radius` sola, `.5rem`, scala di shadcn con ±4). Dettaglio da artigiano: la carta hero ha bordo 1px e raggio 13, l'immagine dentro raggio 12 (`rounded-t-[12px]`) — raggio interno = raggio esterno − spessore bordo, così le curve sono concentriche.

### 3.5 Ombre (tutte)

Nel DOM campionato le ombre sono quasi assenti (`scheda.json` → `ombre`: 14 elementi con ombra nulla). Nel CSS le ombre scritte a mano sono 7, tutte nere e morbide, **una sola colorata**:

```css
.shadow-\[7px_11px_39\.5px_rgb\(0_0_0\/0\.2\)\]{--tw-shadow:7px 11px 39.5px var(--tw-shadow-color,#0003);...}      /* le 3 carte hero */
.shadow-\[2px_2px_17\.3px_rgb\(0_0_0\/0\.32\)\]{--tw-shadow:2px 2px 17.3px var(--tw-shadow-color,#00000052);...}  /* foto zero-clienti, andrei-telefono */
.shadow-\[3px_4px_15\.5px_rgba\(0\,0\,0\,0\.31\)\]{--tw-shadow:3px 4px 15.5px var(--tw-shadow-color,#0000004f);...} /* foto cambiare-vita */
.shadow-\[0_4px_20px_rgb\(0_0_0\/0\.19\)\]{--tw-shadow:0 4px 20px var(--tw-shadow-color,#00000030);...}           /* le 7 schede "Come funziona" */
.shadow-\[0_0_97\.2px_9px_rgb\(0_0_0\/0\.91\)\]{--tw-shadow:0 0 97.2px 9px var(--tw-shadow-color,#000000e8);...}  /* non in home (auth) */
.shadow-\[0_6px_28px_color-mix\(in_oklab\,var\(--fo-blue\)_22\%\,transparent\)\]{--tw-shadow:0 6px 28px var(--tw-shadow-color,var(--fo-blue))} /* sticky CTA "Ottieni accesso" */
.shadow-\[0_0_0_1px_…\]{--tw-shadow:0 0 0 1px var(--tw-shadow-color,…)}
```

Le ombre delle foto sono **spostate a destra e in basso** (2-7px x, 2-11px y): una luce da sinistra-alto, come su una scrivania. Le decine con decimali (39.5, 17.3, 15.5, 97.2) sono valori Figma trascritti, non arrotondati. **L'unico glow colorato** è sul bottone sticky: `0 6px 28px color-mix(in oklab, var(--fo-blue) 22%, transparent)`.

### 3.6 Bordi

- Spessore standard **1px**; **2px** solo sul raccoglitore (`border-2 border-fo-chiaro-testo`), sulla `.girandola` e su `border-t-2`; `1.5px` definito ma non in home.
- Colori: `--fo-line` #2c2c2c (11 usi: schede, FAQ, tabella, footer), `--fo-chiaro-riga-scura` #676767 (4: foto su chiaro), `--fo-chiaro-nero` #000 (3: le 7 schede "Come funziona" e i loro connettori), `--fo-chiaro-riga-foto` #bfbfbf (1), `#676767` letterale (carte hero), `border-white/80` (cerchio play), `border-white/15` (banner cookie).
- `border-dashed border-fo-chiaro-nero`: i connettori tratteggiati tra gli step (sezione 07) sono **div con bordo dashed**, non SVG.
- Le foto su chiaro hanno **sempre** un bordo 1px scuro (#676767 o #bfbfbf) + ombra: la foto non galleggia, è "incollata".
- Il filetto luminoso: `.filo-sfumato{background-image:linear-gradient(90deg,#fff0,#ffffff7e 50.4808%,#fff0);height:1px}` — riga alta 1px bianca al 49% che sfuma ai lati, tra i 3 motivi (sezione 15). È l'unico "bordo luminoso" della pagina.

### 3.7 Alternanza delle superfici

Fonte: `scheda.json` → `sezioni[].bg` e `tono` nel bundle (`tono:\`chiaro\`` 15, `tono:\`scuro\`` 14).

```
01 scuro (hero)        11 scuro              21 scuro
02 scuro (+roccia)     12 scuro              22 scuro
03 CHIARO              13 CHIARO             23 CHIARO
04 CHIARO (rail)       14 CHIARO             24 CHIARO
05 scuro               15 scuro              25 CHIARO
06 scuro               16 CHIARO (+carta)    26 CHIARO
07 CHIARO              17 CHIARO             27 scuro
08 scuro               18 scuro              28 CHIARO
09 CHIARO              19 scuro (+roccia)    29 scuro (FAQ)
10 CHIARO              20 CHIARO             30 scuro (footer)
```

15 chiare / 15 scure (contando il footer). Mai più di **due chiare consecutive** salvo 23-26 (quattro, la parte "prova"); mai più di due scure salvo 18-19 e 21-22. Il ritmo è a coppie: un'idea scura, una prova chiara.

Il meccanismo tecnico è **un solo set di variabili rimappato**, non due palette:

```css
.sezione-chiara{--fo-bg:var(--fo-chiaro-fondo);--fo-text:var(--fo-chiaro-testo);--fo-muted:var(--fo-chiaro-muto);--fo-line:var(--fo-chiaro-riga);--fo-surface:var(--fo-chiaro-superficie);--fo-elevated:var(--fo-chiaro-superficie);--fo-link:var(--fo-blue-deep);--fo-link-hover:var(--fo-blue-hover);background-color:var(--fo-bg);color:var(--fo-text)}
```

Dentro `.sezione-chiara` la stessa `.scheda` (`bg-fo-surface border-fo-line`) diventa bianca con bordo #d4d4d4, e il link scende da `--fo-blue` a `--fo-blue-deep` per tenere il contrasto. **Superfici distinte in pagina: 6** (#111111, #1b1b1b, #222222 su scuro; #ededed, #ffffff, #d4d4d4 su chiaro) + 2 texture immagine (roccia, carta).

---

## 4. Effetti e materia

### 4.1 Grana / noise: c'è, ma non è accesa

Nel CSS esiste una grana SVG:

```css
/* src/38-styles-Cm6i-gBj.css — dopo @keyframes fo-rail */
.fo-grain:after{content:"";z-index:50;pointer-events:none;opacity:.045;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E");position:fixed;inset:0}
```

Un solo strato, `feTurbulence fractalNoise` baseFrequency 0,85, 3 ottave, tile 160px, **opacità 4,5%**, fisso, z-50, senza blend mode. Ma la classe **`fo-grain` non compare in nessuno dei 44 bundle JS** (grep su `src/*.js`: 0 risultati) e negli screenshot il fondo è **piatto al pixel**: su `sezioni/01`, `05`, `29` il crop 200×200 misura media 17 / dev.std 0,000 (=#111111 esatto); su `sezioni/14` media 237 / dev 0,000 (=#ededed). Solo `sezioni/19` ha dev 1,72, ed è `offerta-roccia.webp` al 28%. **Conclusione: la grana CSS è codice morto o riservata a un'altra rotta; la home è senza grana CSS.**

La materia viene dalle immagini:
- **`roccia.webp`** in `bg-[url('/vendita/roccia.webp')] bg-cover bg-center [background-blend-mode:lighten]` sulla sezione "Diventa funnel operator" (02), con un velo superiore `bg-gradient-to-b from-fo-bg to-transparent h-[132px] lg:h-[172px]` che la fonde con l'hero;
- **`offerta-roccia.webp`** in `absolute inset-0 -z-10 bg-cover bg-center opacity-28` sotto l'offerta (19);
- **`carta-serpenti.webp`** (1440×928, 21 KB): una carta grigio-chiarissima con fibre e puntini, `absolute inset-0 size-full object-cover`, sotto la sezione "Schiavizzerai l'AI" (16).
(`roccia.webp` e `offerta-roccia.webp` non sono in `media/` perché sono background CSS, non `<img>`.)

### 4.2 Blend mode: su cosa

Sei classi nel CSS, quattro usate in home (`scheda.json` → `effetti.blend`: hard-light 2, difference 1, screen 1, color-dodge 1):

| Blend | Elemento | Classe completa | Effetto visibile |
|---|---|---|---|
| **difference** | l'h1 "Un giorno morirai." | `lapide-uno mix-blend-difference text-center text-white` | il testo bianco diventa **bianco su nero e nero dove copre il soldato**: la "morirai" rossa `#BD0000` in difference su nero resta rossa, sull'immagine si inverte |
| **screen** | `soldato-caduto.webp` | `-mt-[calc(min(29.85vw,220px)*0.34)] aspect-[402/496] w-full object-cover mix-blend-screen sm:aspect-[832/618]` | il nero della WebP sparisce nel fondo #111111 (la mezzatinta bianca resta), e la figura sale di 34% dell'altezza del gotico dentro il titolo |
| **color-dodge** | `gancio-insegna.webp` "LANDING PAGES." | `w-full mix-blend-color-dodge outline-2 -outline-offset-1 outline-white` | brucia i chiari, cornice bianca 2px disegnata con `outline` (non border) |
| **hard-light** ×2 | `serpente-testa.webp` (due istanze, una `rotate-180`) | `pointer-events-none absolute … opacity-85 mix-blend-hard-light` | i serpenti su carta: neri profondi, lucidi, opacità 85% |
| `[background-blend-mode:lighten]` | sezione 02 | `bg-fo-bg bg-[url('/vendita/roccia.webp')] … [background-blend-mode:lighten]` | la roccia schiarisce il #111111 solo dove è più chiara |

Le tre tecniche (screen per il nero, difference per il testo, hard-light per l'inchiostro su carta) sono tutte al servizio della stessa idea: **immagini in bianco e nero che si fondono col fondo senza ritaglio né maschera.**

### 4.3 Clip-path: il poligono della linguetta

Il `polygon(0px 100%, 12.2709px 6.9px, 13.4709px 4.1px, 15.4709px 1.9px, 18.0709px 0.5px, 21.0709px 0px, calc(100% - 21.0709…)` campionato nel DOM (4 occorrenze) **non è nel CSS**: è uno `style` inline generato in `src/32-raccoglitore-Bj4iyfd5.js`:

```js
clipPath:`polygon(0 100%, calc(var(--taglio) - 1.7px) 6.9px, calc(var(--taglio) - 0.5px) 4.1px, calc(var(--taglio) + 1.5px) 1.9px, calc(var(--taglio) + 4.1px) 0.5px, calc(var(--taglio) + 7.1px) 0, calc(100% - var(--taglio) - 7.1px) 0, calc(100% - var(--taglio) - 4.1px) 0.5px, calc(100% - var(--taglio) - 1.5px) 1.9px, calc(100% - var(--taglio) + 0.5px) 4.1px, calc(100% - var(--taglio) + 1.7px) 6.9px, 100% 100%)`
```

Cos'è: **un trapezio con gli angoli superiori arrotondati**, 12 vertici. La base è tutta la larghezza (0 100% → 100% 100%), i lati salgono inclinati di `--taglio` = 24,6% dell'altezza della linguetta (`calc(var(--linguetta)*0.246)`, 46px → 11,3px), e i 5 punti intermedi per lato (6.9 / 4.1 / 1.9 / 0.5 / 0 px) sono una **curva di Bézier discretizzata a mano** che arrotonda lo spigolo. È la linguetta delle cartelle del **raccoglitore** (sezione 20, `sezioni/20-section.png`): 4 cartelle #d4d4d4 con bordo 2px #111111 impilate con `--gradino` (48px+) e una linguetta nera `bg-fo-chiaro-testo` con numero in `#d4d4d4` e nome in bianco, alternate sinistra/destra (`left-[4%]` / `right-[4%]`, su sm: `left: var(--linguetta-x)` = 3.9% / 66.9% / 5.5% / 60.3%). Il logo bianco PNG diventa nero con `brightness-0`.

Il secondo clip nel DOM è `inset(50%)` = `.sr-only` (screen reader), non decorativo.

### 4.4 Backdrop blur

```css
.backdrop-blur{--tw-backdrop-blur:blur(8px);…}     /* banner consenso cookie: fixed inset-x-0 bottom-0 z-50 border-t border-white/15 bg-fo-bg/95 text-white backdrop-blur */
.backdrop-blur-sm{--tw-backdrop-blur:blur(var(--blur-sm));…}  /* --blur-sm:8px — cerchio play del video: border-white/80 bg-black/45 backdrop-blur-sm */
```

Due usi (`scheda.json`: `backdrop: blur(8px)` ×2): il banner cookie e il **bottone play** (cerchio 64→80px, bordo bianco 80%, nero 45%, blur 8px; hover: `group-hover:border-fo-blue-light group-hover:bg-black/60`). Niente header vetro: la nav non è sticky-glass.

### 4.5 Filtri

- `blur-[3.55px]` ×2 + `opacity-50`/`opacity-100`, `rotate-[-167.43deg]`, `-scale-y-100`: i due **aeroplani di carta** sfocati dietro la sezione Telegram (24) — profondità di campo finta, con valori Figma non arrotondati.
- `brightness-0` ×1: il logo bianco reso nero nel raccoglitore.
- `blur-[5px]` definito, non in home.

### 4.6 Gradienti (elenco completo con codice)

```css
/* 1 — la scala blu della tabella percorso (orizzontale su mobile, verticale su lg) */
.bg-\[linear-gradient\(90deg\,\#88C9F4_0\%\,\#1E9CD7_33\%\,\#0075BE_66\%\,\#005B97_100\%\)\]{background-image:linear-gradient(90deg,#88c9f4 0%,#1e9cd7 33%,#0075be 66%,#005b97 100%)}
.lg\:bg-\[linear-gradient\(180deg\,…\)\]{background-image:linear-gradient(#88c9f4 0%,#1e9cd7 33%,#0075be 66%,#005b97 100%)}
/* 2 — la sottolineatura animata dei link FAQ (larghezza 0 → 100%) */
.bg-\[linear-gradient\(currentColor\,currentColor\)\]{background-image:linear-gradient(currentColor,currentColor)}
.bg-\[length\:0\%_1px\]{background-size:0% 1px}  .bg-\[position\:0_100\%\]{background-position:0 100%}
@media (hover:hover){.group-hover\:bg-\[length\:100\%_1px\]:is(:where(.group):hover *){background-size:100% 1px}}
/* 3 — il velo che fonde hero e roccia */
.bg-gradient-to-b{--tw-gradient-position:to bottom in oklab;background-image:linear-gradient(var(--tw-gradient-stops))}
.from-fo-bg{--tw-gradient-from:var(--fo-bg);…}  .to-transparent{--tw-gradient-to:transparent;…}
/* 4 — il filetto luminoso */
.filo-sfumato{background-image:linear-gradient(90deg,#fff0,#ffffff7e 50.4808%,#fff0);height:1px}
/* 5 — lo skeleton */
.sagoma{border-radius:var(--radius-sm);background:linear-gradient(90deg, var(--fo-elevated) 0%, var(--sagoma-luce) 50%, var(--fo-elevated) 100%);background-size:200% 100%;animation:1.4s linear infinite fo-luccichio}
/* 6-9 — le maschere dei rail (non sono sfondi: sfumano i bordi dello scorrimento) */
.\[mask-image\:linear-gradient\(to_right\,transparent\,black_6\%\,black_94\%\,transparent\)\]{-webkit-mask-image:linear-gradient(90deg,#0000,#000 6% 94%,#0000);mask-image:linear-gradient(90deg,#0000,#000 6% 94%,#0000)}
.\[mask-image\:…black_13\%\,black_87\%…\]{…mask-image:linear-gradient(90deg,#0000,#000 13% 87%,#0000)}
.\[mask-image\:…black_22\%\,black_78\%…\]{…mask-image:linear-gradient(90deg,#0000,#000 22% 78%,#0000)}
.\[mask-image\:…black_28\%\,black_72\%…\]{…mask-image:linear-gradient(90deg,#0000,#000 28% 72%,#0000)}
```

Nessun gradiente decorativo su testo o sfondo di sezione. **Il gradiente più visibile (tabella 01-04) è la palette dell'accento in fila.** Il logomark SVG (`funops-logomark-gradiente.svg`) ha un `linearGradient` verticale azzurro (paint0/paint1) — il gradiente vive nel logo, non nel CSS.

### 4.7 Ombre di testo, bordi luminosi, maschere

- **`text-shadow`: 0 occorrenze** nel CSS.
- Bordo luminoso: solo `.filo-sfumato` (§3.6) e `outline-2 -outline-offset-1 outline-white` attorno a "LANDING PAGES." (cornice disegnata *dentro* l'immagine di 1px).
- Maschere: le 4 `mask-image` dei rail (6/94, 13/87, 22/78, 28/72 %): più il rail è stretto in colonna, più la sfumatura è larga. Rail loghi AI 22/78; rail numeri (full width) 6/94; rail esempi (pagine) 28/72; rail consulenze (max 777px) 13/87.
- Rotazioni "a mano": `rotate-2`/`-rotate-2` (carte hero mobile), `lg:rotate-3`/`lg:-rotate-3` (carte hero desktop), `-rotate-3 md:rotate-0` (SEC su mobile), `-rotate-[1.32deg]` (foto telefono), `rotate-[2.4deg]` (tessera), `rotate-[-167.43deg]` (aeroplano). La carta storta è la firma delle foto "vere".
- `[box-decoration-break:clone]` sulla sottolineatura FAQ, così funziona anche su due righe.

---

## 5. Movimento

### 5.1 Le variabili del tempo e la curva

```css
/* :root */
--moto-stato:.12s;--moto-comparsa:.16s;--moto-momento:.32s;--moto-battuta:90ms;--curva:cubic-bezier(.2, 0, 0, 1)
/* @layer theme */
--default-transition-duration:var(--moto-stato);--ease-in-out:cubic-bezier(.4, 0, .2, 1);--animate-pulse:pulse 2s cubic-bezier(.4, 0, .6, 1) infinite;
```

Quattro tempi con nomi italiani: **stato** 120ms (hover/colore), **comparsa** 160ms (apparire), **momento** 320ms (un ingresso), **battuta** 90ms (il ritmo tra un figlio e il successivo). **Una curva sola** `cubic-bezier(.2, 0, 0, 1)` (ease-out deciso, "Material standard decelerate") ereditata da **tutte** le `.transition-*` grazie a `transition-timing-function:var(--tw-ease,var(--curva))`. Le altre due curve del DOM (`.4,0,.2,1` e `.4,0,.6,1`) sono Tailwind/shadcn: `ease-in-out duration-700` sul gradiente della tabella (`transition-opacity duration-700 ease-in-out`) e `pulse`.

Campionamento (`scheda.json` → `effetti.transizioni`): `all` 825 (default Tailwind su elementi senza transizione dichiarata), `color/background-color/border-color 0.12s cubic-bezier(0.2,0,0,1)` 53, `background-size 0.3s` 18 (sottolineature FAQ), `transform 0.3s` 18 (chevron), `0.7s cubic-bezier(.4,0,.2,1)` 5 (gradiente tabella).

### 5.2 I 13 @keyframes con il corpo completo

```css
/* --- scritti a mano (prefisso fo-) --- */
@keyframes fo-comparsa{0%{opacity:0;transform:translateY(4px)}}
@keyframes fo-momento{0%{opacity:0;transform:translateY(8px)}}
@keyframes fo-foglio-su{0%{transform:translateY(0)}10%{transform:translateY(-2.2px)}20%{transform:translateY(-4.1px)}30%{transform:translateY(-5.6px)}40%{transform:translateY(-6.6px)}50%{transform:translateY(-7px)}60%{transform:translateY(-6.9px)}70%{transform:translateY(-6.4px)}80%{transform:translateY(-5.8px)}90%{transform:translateY(-5.3px)}to{transform:translateY(-5px)}}
@keyframes fo-gira{to{transform:rotate(360deg)}}
@keyframes fo-luccichio{to{background-position:-200% 0}}
@keyframes fo-rail{0%{transform:translate(0)}to{transform:translate(-50%)}}
@keyframes fo-dissolvenza{0%{opacity:0}}
/* --- Tailwind / tw-animate-css / shadcn --- */
@keyframes pulse{50%{opacity:.5}}
@keyframes enter{0%{opacity:var(--tw-enter-opacity,1);transform:translate3d(var(--tw-enter-translate-x,0),var(--tw-enter-translate-y,0),0)scale3d(var(--tw-enter-scale,1),var(--tw-enter-scale,1),var(--tw-enter-scale,1))rotate(var(--tw-enter-rotate,0));filter:blur(var(--tw-enter-blur,0))}}
@keyframes exit{to{opacity:var(--tw-exit-opacity,1);transform:translate3d(var(--tw-exit-translate-x,0),var(--tw-exit-translate-y,0),0)scale3d(var(--tw-exit-scale,1),var(--tw-exit-scale,1),var(--tw-exit-scale,1))rotate(var(--tw-exit-rotate,0));filter:blur(var(--tw-exit-blur,0))}}
@keyframes accordion-down{0%{height:0}to{height:var(--radix-accordion-content-height,var(--bits-accordion-content-height,var(--reka-accordion-content-height,var(--kb-accordion-content-height,var(--ngp-accordion-content-height,auto)))))}}
@keyframes accordion-up{0%{height:var(--radix-accordion-content-height,var(--bits-accordion-content-height,var(--reka-accordion-content-height,var(--kb-accordion-content-height,var(--ngp-accordion-content-height,auto)))))}to{height:0}}
@keyframes caret-blink{0%,70%,to{opacity:1}20%,50%{opacity:0}}
```

### 5.3 Chi li usa, con quale durata

| Keyframe | Classe / uso | Durata · easing | Dove |
|---|---|---|---|
| `fo-comparsa` | `.comparsa{animation:fo-comparsa var(--moto-comparsa) var(--curva)}` | 160ms · curva | dialog e dropdown (`12-dialog`, `28-dropdown-menu`), sticky CTA (`transition-[opacity,visibility] duration-(--moto-comparsa)`) |
| `fo-momento` | `.battuta{animation:fo-momento var(--moto-momento) var(--curva) both;animation-delay:calc(var(--battuta,0) * var(--moto-battuta))}` | 320ms · curva · **delay = indice × 90ms** | staggered entrance: l'indice si passa come `--battuta: n` inline. **Non usato nel bundle home** (0 occorrenze di `battuta` nei JS) |
| `fo-foglio-su` | `motion-safe:has-[button:hover]:animate-[fo-foglio-su_var(--moto-foglio)_linear_forwards]` con `--moto-foglio:calc(var(--moto-momento)*1.6)` | **512ms · linear** (la curva è nei keyframe: 11 step con **overshoot a −7px e ritorno a −5px**) | la cartella del raccoglitore che si alza al passaggio del mouse sulla linguetta (`:has(button:hover)`). È un ease-out-back scritto a mano |
| `fo-gira` | `.girandola{border:2px solid;border-right-color:#0000;border-radius:9999px;width:.875rem;height:.875rem;animation:.7s linear infinite fo-gira}` | 700ms · linear · infinito | spinner 14px (bottone "Apro il pagamento…") |
| `fo-luccichio` | `.sagoma` (§4.6) | 1,4s · linear · infinito | skeleton shimmer (area riservata) |
| `fo-rail` | `.fo-rail{will-change:transform;animation:70s linear infinite fo-rail}` + `.[animation-duration:45s]!` + `.[animation-direction:reverse]` | **70s** (default) / **45s** · linear · infinito | i 5 rail (§5.5) |
| `fo-dissolvenza` | sostituisce `fo-comparsa` e `fo-momento` sotto `prefers-reduced-motion` | — | §5.4 |
| `pulse` | `.animate-pulse{animation:var(--animate-pulse)}` | 2s · `cubic-bezier(.4,0,.6,1)` | skeleton shadcn |
| `enter` / `exit` | `.animate-in`/`.animate-out` con `data-[state=open]`… | 150ms · ease | Radix dialog/popover/select |
| `accordion-down/up` | `data-[state=open]:animate-accordion-down` | 200ms · ease-out | **FAQ e accordion consulenza** (Radix Accordion) |
| `caret-blink` | `.animate-caret-blink` | 1,25s · ease-out · infinito | input OTP (auth) |

Movimento **non** CSS: la tabella 01-04 ruota ogni **1.500ms** via `setInterval` (`Me=1500` in `36-routes`), con `transition-opacity duration-700 ease-in-out` sul gradiente e `motion-reduce:transition-none`; sotto reduced-motion si ferma sull'indice 2. Il chevron FAQ gira con `transition-transform duration-300` (`rotate-` in `02-accordion`). Il resto dello scroll **non ha reveal on scroll**: nessun IntersectionObserver, nessuna classe `.in`, nessun parallax. La pagina appare tutta, subito.

### 5.4 prefers-reduced-motion: c'è, in tre strati

```css
@media (prefers-reduced-motion:reduce){*,:before,:after{--tw-enter-translate-x:0!important;--tw-enter-translate-y:0!important;--tw-enter-scale:1!important;--tw-enter-rotate:0!important;--tw-exit-translate-x:0!important;--tw-exit-translate-y:0!important;--tw-exit-scale:1!important;--tw-exit-rotate:0!important}
.comparsa{animation-name:fo-dissolvenza}
.battuta{animation-name:fo-dissolvenza;animation-delay:0s}
.animate-accordion-down,.animate-accordion-up,.animate-collapsible-down,.animate-collapsible-up{animation-duration:1ms}
.fo-rail{animation:none}
.sagoma{background:var(--fo-elevated);animation:none}
.girandola{animation-duration:2s}}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
```

1. **CSS**: gli ingressi diventano dissolvenze pure (non si spengono: `fo-dissolvenza` toglie il movimento e tiene l'opacità), i rail si fermano, lo skeleton diventa piatto, lo spinner rallenta a 2s (non si ferma: deve dire "sto caricando"), gli accordion vanno a 1ms, lo smooth scroll esiste **solo** sotto `no-preference`.
2. **Tailwind variant**: `motion-safe:` sul foglio-su, `motion-reduce:transition-none` sul gradiente.
3. **JS**: `window.matchMedia('(prefers-reduced-motion: reduce)')` in due punti — ferma il carosello 01-04 e cambia `scrollIntoView({behavior: 'smooth'})` in `'auto'` sullo sticky CTA.

È esattamente la regola del canone DE §14 ("il gemello in JavaScript è obbligatorio"): qui è applicata.

### 5.5 I rail / marquee: cosa scorre

Tutti costruiti allo stesso modo: `div.fo-rail-track.overflow-hidden.[mask-image:…]` > `div.fo-rail.flex.w-max` > [contenuto] + [copia `aria-hidden` del contenuto]; `translate(-50%)` fa il loop perfetto perché il contenuto è duplicato. Hover: `.fo-rail-track:hover .fo-rail{animation-play-state:paused}`.

| Rail | Sezione | Durata | Gap | Maschera | Cosa scorre |
|---|---|---|---|---|---|
| Numeri AP Sales | 04 (chiaro) | **45s** `[animation-duration:45s]!` | `gap-24 pr-24` (96px) | 6/94 | 4 coppie icona SVG + cifra: 4.8/5 Trustpilot, 4000+ ordini, studenti, apertura (`titolo-sezione tabular-nums` + `.corpo`) |
| Esempi pagine, riga 1 | 11 (scuro) | **70s** | `gap-[35px] pr-[35px]` | 28/72 | 8 miniature `aspect-[211/282] w-[136px] md:w-[211px] rounded-[5px] border border-fo-chiaro-riga-scura bg-fo-surface` (3 landing AP Sales ripetute) |
| Esempi pagine, riga 2 | 11 | 70s **reverse** `[animation-direction:reverse]` | idem | 28/72 | stesse miniature, ordine ruotato di 1 |
| Loghi AI | 17 (chiaro) | 70s | `gap-[61px] pr-[61px]` | 22/78 | ChatGPT, GitHub, Lovable, Krea, Claude (WebP 80×80 → 40px), Gemini, Vercel |
| Consulenze | 21 (scuro) | 45s | `gap-[38px] pr-[38px]` | 13/87 | 3 screenshot di videochiamate (`consulenza-1/2/3.webp`, 321×181, resi 1×) in `max-w-[777px]` |

Le velocità: 45s per i rail "corti" (numeri, consulenze), 70s per quelli lunghi. Tutti `linear`: il marquee non accelera mai.

---

## 6. I bottoni

### 6.1 Il componente (cva) — l'unica fonte

```js
// src/04-button-rHPgEXhH.js (buttonVariants)
[`inline-flex items-center justify-center gap-2 whitespace-nowrap`,
 `interfaccia rounded-lg border border-transparent cursor-pointer`,
 `transition-colors`,
 `disabled:bg-spento-fondo disabled:text-spento-testo disabled:border-transparent`,
 `disabled:cursor-not-allowed disabled:pointer-events-none`,
 `[&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0`].join(` `),
{variants:{
  variant:{
    default:`bg-fo-action text-fo-on-action hover:bg-fo-action-hover active:bg-fo-action-press`,
    outline:`bg-fo-surface text-fo-text border-fo-line hover:bg-fo-elevated`,
    ghost:`text-fo-muted hover:bg-fo-surface hover:text-fo-text`,
    "ghost-bordo":`bg-transparent text-fo-text border-fo-text hover:bg-fo-elevated`,
    destructive:`bg-fo-error-solid text-fo-text hover:bg-fo-error-solid-hover`,
    link:`collegamento h-auto border-0 p-0`},
  size:{sm:`h-8 px-4`,default:`h-10 px-5`,lg:`h-12 px-6`,"icon-sm":`size-8 p-0`,icon:`size-10 p-0`,"icon-lg":`size-12 p-0`}},
 defaultVariants:{variant:`default`,size:`default`}}
```

Sei varianti, sei taglie. **In home se ne usano due** (`default` e `outline`) in **una taglia** (`lg`, 4 chiamate `f({size:'lg'})` + 1 `f({variant:'outline',size:'lg'})`).

### 6.2 Le CTA misurate (`scheda.json` → `cta[]`)

| Testo | Sezione | bg | color | h | padding | font | radius | border | shadow |
|---|---|---|---|---|---|---|---|---|---|
| **Iscriviti adesso** | 19 offerta | `oklch(0.656 0.134 235.9)` #1d9cd7 | `oklch(0.178 0 89.9)` #111111 | **48px** | `0 24px` | 14px / 500 | 8px | `1px solid transparent` | none |
| Cosa contiene il corso? | 19 offerta | `oklch(0.22 0 89.9)` #1b1b1b | `oklch(0.934 0 89.9)` #e9e9e9 | 48px | `0 24px` | 14px / 500 | 8px | `1px solid transparent` (campionato; in classe `border-fo-line` = #2c2c2c) | none |
| **Sono pronto** ↗ | 28 chiusura | #1d9cd7 | **#ffffff** (`text-white` forzato) | 48px | `0 24px` | 14px / 500 | 8px | 1px transparent | none |
| **Ottieni accesso** (sticky, `#prezzo`) | fixed bottom-right | #1d9cd7 | #111111 | 48px | `0 24px` | 14px / 500 | 8px | 1px transparent | `0 6px 28px color-mix(in oklab, var(--fo-blue) 22%, transparent)` |
| 01 Intro / 02 Landing pages / 03 Trovare clienti / 04 Domande comuni | 20 raccoglitore | #111111 | #111111 (il testo è negli span: #d4d4d4 + #fff) | 57px | `0 29.12px` (`--fianco`) | 18,9px / 500 | 0 + clip-path | 0 | none |
| Le 18 domande accordion (`Dove si fa la consulenza?` … `Ho un problema con un ordine…`) | 21, 29 | transparent | `oklch(0.633 0 89.9)` #8a8a8a | 80px (102 se a capo) | `20px 0` | 22px / 500 | 0 | 0 | none |
| Accedi → | header | transparent (link) | #1d9cd7 | — | — | 14px / 500 | — | — | — |

**Varianti effettive in pagina: 2 + 2 speciali.** Primaria: azzurro pieno, testo scuro, 48×~150px, min-width `--bottone-minimo: 7.5rem` (120px) via `.bottone-che-lavora{min-width:var(--bottone-minimo)}`. Secondaria: `#1b1b1b` con bordo `#2c2c2c` e testo `#e9e9e9` — su fondo `#111111` è un bottone che si vede appena (1,10:1 di sfondo, il bordo fa il lavoro). Le linguette del raccoglitore e le domande accordion sono `<button>` ma non CTA.

### 6.3 Hover, active, focus, disabled

```css
/* utilities generate dal componente */
@media (hover:hover){.hover\:bg-fo-action-hover:hover{background-color:var(--fo-action-hover)}}   /* → #88c9f4: il bottone SI SCHIARISCE */
.active\:bg-fo-action-press:active{background-color:var(--fo-action-press)}                          /* → #0075be: e si scurisce alla pressione */
@media (hover:hover){.hover\:bg-fo-elevated:hover{background-color:var(--fo-elevated)}}             /* outline → #222222 */
.transition-colors{transition-property:color,background-color,border-color,…;transition-timing-function:var(--tw-ease,var(--curva));transition-duration:var(--tw-duration,var(--moto-stato))}  /* 120ms cubic-bezier(.2,0,0,1) */
/* @layer base */
:focus-visible{outline:2px solid var(--fo-focus);outline-offset:2px}                                  /* anello #88c9f4 */
button:disabled,…,[aria-disabled=true]{background-color:var(--spento-fondo);color:var(--spento-testo);border-color:var(--fo-line);cursor:not-allowed}  /* #1b1b1b / #8a8a8a */
```

Il bottone primario **non si scurisce in hover, si schiarisce** (65,6% → 80,8% L) e si scurisce solo in `:active` (54,6%). Niente `transform`, niente scale, niente ombra che cresce: cambia **solo il colore, in 120ms**. Il testo resta `#111111` (`--fo-on-action`), che su `#88c9f4` sale a contrasto ~12:1. Stato caricamento: testo "Apro il pagamento…" + `disabled`, errore sotto in `text-xs text-red-400`.

Il link testuale: `.collegamento{color:var(--fo-link);text-underline-offset:3px;transition:color var(--moto-stato) var(--curva);text-decoration:underline;text-decoration-thickness:1px}`, hover → `--fo-link-hover` (#88c9f4); su chiaro `--fo-link` è rimappato a `--fo-blue-deep`.

---

## 7. Le immagini come stile

Fonte: `media-inventario.md` (68 file, 2.511 KB = 2,45 MB), `media/` (peso reale verificato: 2.511 KB), classi `<img>` nel bundle route.

### 7.1 Formato e peso

- **59 WebP, 8 SVG, 1 PNG** (il logo bianco `funops-logo-bianco.png`, 804×240, 30 KB: l'unico PNG, ed è anche l'unico servito a 7,5× la resa — 107×32 — probabilmente per essere riusato a 804px nel raccoglitore).
- Peso totale **2,45 MB** per 32.807px di pagina; le 5 più pesanti: `carte-mano` 256 KB, `soldato-caduto` 218, `tessera` 185, `gancio-insegna` 169, `albero-apsales` 105. Le mezzetinte bianco/nero costano (rumore = poca compressione).
- **SVG solo per icone e loghi** (Trustpilot, carrello, studenti, apertura, sigillo "carriera avviata", AP Sales, logomark). Le icone dei 7 step (`passo-*.webp`, 256×256, 2-5 KB) sono **WebP raster nere**, non SVG: coerenti con lo stile "stampato".

### 7.2 Rapporto px originali / resi: è 2× esatto?

Calcolato su 60 immagini con dimensioni (SVG esclusi):

- **32 esattamente 2×** (±3%): tutte le foto di Andrei, le carte, il soldato, il gancio, l'albero, i "siti", le icone AI (80→40), gli step 4-7, Telegram, l'aeroplano.
- **9 a 1×** (servite alla misura resa): `carta-serpenti` (1440 full-bleed), `community-iphone` (326×404), le 3 `consulenza-*` (321×181), `sito-apple` (830→832, unico caso di **upscaling** di 2px), i 3 `motivo-*` (60px, e sono 2-3 KB: piccole apposta).
- **19 altri**: 2,85× `tessera` (840→295: è a `w-[97%] max-w-[272px]`, in Figma era più grande), 3,16× `template-fasi` (773→245), 2,75× `vsl-consulenza` (1600→582), 2,45× `template-messaggi`, 2,11× `call-*`, 1,89-1,95× (`carta-landing` 314px perché è la carta in primo piano più grande, `andrei-telefono`), 1,80× `lovable`, 1,91× i 3 `esempio-*` (400→209), 1,59-2,33× gli step (icona `absolute max-w-none` posizionata in % del riquadro).
- **Regola dell'autore: export 2× dalla tavola a 832, con `width`/`height` HTML sempre dichiarati** (ogni `<img>` nel bundle ha `width:` e `height:` — zero CLS). L'hero ha `srcSet` a due misure (`soldato-caduto-832.webp 832w, soldato-caduto.webp 1664w` con `sizes="(min-width: 832px) 832px, 100vw"`) e la tessera pure (`tessera-420.webp 420w, tessera.webp 840w`): **srcset solo sulle 2 immagini più pesanti sopra la piega o al prezzo.**

### 7.3 Ritagli CSS

Confronto rapporto originale vs reso (soglia 2%): **57 su 60 identici**. I 3 diversi: `tessera` (0,488 → 0,519: `rotate-[2.4deg]` allarga il box misurato, non è un crop), `carta-landing` (0,796 → 0,816: la carta ruotata `lg:rotate-3`), `lovable` (1,843 → 2,329: **l'unico vero ritaglio**, `h-full w-full object-cover object-top` dentro un riquadro 666×286 — mostra solo l'header della pagina Notion). `object-cover` compare 5 volte ma quasi sempre su box dello stesso rapporto (`aspect-[297/373]` per carte 594×746, `aspect-[211/282]` per esempi 400×560 ≈ 0,714): **il rapporto è dichiarato in CSS e l'immagine è esportata in quel rapporto** — object-cover è cintura di sicurezza, non ritaglio.

### 7.4 Stile grafico — cosa ho guardato (23 file) e cosa vedo

**Incisioni a mezzatinta bianco su nero (la famiglia "morte e gloria")** — `soldato-caduto.webp` (1664×1236): cavaliere in ginocchio trafitto da frecce, aureola, topi ai piedi, resa a puntinato/xilografia, **fondo nero pieno** (per il `mix-blend-screen`), nessuna scala di grigi intermedia — solo bianco e nero con grana da stampa. `gancio-insegna.webp` (1662×518): stesso cavaliere, di lato con la spada, sopra una texture nera macchiata; la scritta "LANDING PAGES." in Inter Tight bold grigio chiaro è **dentro l'immagine**, non HTML. `carte-mano.webp` (1504×680): quattro carte da gioco K/Q/J/A con semi "$", re-teschio, regina-teschio con calice, fante-caprone, asso-calice pieno di monete, tratto da incisione ottocentesca, **carte bianche con ombra morbida** su trasparente. `motivo-teschio/spade/lapide.webp` (60px): tre icone incise in bianco, stesso tratto. Tutte con la stessa firma: **inchiostro bianco, fondo nero, texture di stampa, iconografia memento mori** (teschi, lapidi, frecce, spade, aureole).

**Le carte-oggetto del metodo** — `carta-metodo.webp` (594×746): mappa topografica nera con isoipse bianche, un percorso tratteggiato tra 5 waypoint quadrati fino a una bandierina, bussola in alto a destra; `carta-lezioni.webp`: terminale anni '80 con tastiera, sullo schermo "0 to landing page" in monospace, tutto in negativo ruvido; `carta-landing.webp`: cronometro digitale "24 ✓" con cassa arrugginita e macchie di ossido chiaro. Tre oggetti **in negativo, texture di ruggine/polvere, un solo dettaglio leggibile ciascuno** (percorso, schermo, cifra).

**Il serpente e la carta** — `serpente-testa.webp` (1438×1708): serpente nero **lucido, fotografico** (non inciso), fauci aperte, denti bianchi, su bianco puro; è l'unica immagine "liscia" della famiglia scura, e per questo viene appoggiata in `hard-light` su `carta-serpenti.webp` (1440×928): una carta grigio-chiara (#f0f0f0 circa) con fibre, capelli e puntini neri sparsi — **grana vera, fotografata, non generata**.

**Le fotografie di Andrei** — `fare-siti.webp` (596×726): profilo in bianco e nero, AirPod, catenina, sfondo grigio uniforme, bordo 1px chiaro **già nell'immagine**; `per-chi.webp` (642×682): a colori, hoodie beige, laptop col logo azzurro, LED blu verticale, poster gotico rosso "INRI" — **la luce blu è sempre presente** (`zero-clienti`, `andrei-scrivania`, `vsl-*`, `per-chi`: studio con LED azzurro, che rima con `--fo-blue`); `zero-clienti.webp` (700×534): laptop su fondo di pannelli blu, schermo CRM bianco con "ZERO CLIENTI?" in Plus Jakarta bold. Le foto **a colori sono tutte blu/nero/beige**, le foto "prima" sono in B/N.

**Gli oggetti di prodotto** — `tessera.webp` (840×1721): badge con laccio grigio e moschettone cromato, fronte azzurro `#1d9cd7`-circa con il cavaliere in **cianotipia** (bianco su azzurro, grana da stampa serigrafica), striscia inferiore grigio chiara con 4 check, logo e QR: la tessera **riusa l'illustrazione hero nel colore dell'accento**. `albero-apsales.webp` (1586×656): tre pill grigie `#ededed` con bordo nero 1px, testo Plus Jakarta bold, icone lineari; è un **diagramma raster** disegnato con la palette del sito, con il "Tu sei qui" azzurro incluso. `stack-clienti.webp` (1152×1832): quattro schede bianche con bordo nero e raggio ~24px, icone Instagram/Loom/FaceTime/Verified **sfumate verso il basso in bianco** (fade-out), connettori tratteggiati — stesso linguaggio dei 7 step (che invece sono HTML+CSS). `sec-avviso.webp` (894×624): carta di credito metallica argento con logo SEC e testo in monospace maiuscolo: **rendering 3D fotorealistico**, l'unica immagine "materica lucida".

**Icone e piccoli** — `passo-2-checklist.webp` (256×256): pittogramma nero pieno, tratto spesso arrotondato (stile SF Symbols bold); `aeroplano.webp` (808×473): aeroplano di carta bianco, rendering 3D pulito, usato sfocato; `telegram.webp` (178×182): icona iOS con glow azzurro; `template-fasi.webp` (773×1094): screenshot di un documento con pill nere e **evidenziatore giallo-verde fluo `#c8ff00`-circa** — l'unico colore fuori palette di tutta la pagina, ed è in una miniatura di un PDF. `lovable.webp`: screenshot della home Notion (a colori, molto bianco), ritagliato all'header.

**Sintesi dello stile**: tre registri e tre sole palette — (1) **incisione bianco/nero** per la mitologia (morte, guerra, carte, mappa, terminale, cronometro), (2) **fotografia con LED blu** per la prova personale, (3) **diagramma raster grigio/nero/azzurro** per la spiegazione (albero, stack, tessera). Cornici: **mai** nelle incisioni (si fondono in blend), **sempre** 1px + ombra nelle foto su chiaro, **raggio 8-13px** ovunque. Nessuna illustrazione vettoriale "flat", nessuna foto stock, nessun mockup 3D di schermi tranne la tessera e la SEC.

### 7.5 Coerenza col sito

Alta: le incisioni sono nere come `--fo-bg` (screen le fonde), la carta è `#ededed` come `--fo-chiaro-fondo`, l'albero e lo stack usano `#ededed`/`#000`/`#1d9cd7`, la tessera è `--fo-blue`. Le uniche note fuori: il giallo fluo del template e i colori di Notion/Amazon/Apple/Loom/Instagram (screenshot altrui: sono "il mondo", non il brand).

### 7.6 Lazy loading

`dom-blocks.json` contiene solo blocchi testuali (386 voci, nessun attributo `loading`), quindi **la verifica è sul bundle**: in `36-routes-DT2uV_Ni.js` ogni `<img>` dichiara `loading` e `decoding` (25 occorrenze di `loading:`): **`loading:"eager" decoding:"sync" fetchPriority:"high"` solo sul soldato dell'hero**, `loading:"lazy" decoding:"async"` su tutto il resto (il componente `O()` lo decide con la prop `priorita`). Il `<picture>` con `<source media="(max-width: 767px)">` serve una `sorgenteStretta` per le foto orizzontali (es. `cambiare-vita-stretta.webp`) sotto 768px.

---

## 8. Il canone in 20 regole

1. **Il nero di fondo è `oklch(17.8% 0 89.9)` ≈ `#111111`**, croma zero; le superfici salgono a passi di 3-5 punti di L: `#1b1b1b` (22%) scheda, `#222222` (25,1%) rialzato, `#2c2c2c` (29,3%) bordo. Mai `#000` come fondo (il `#000` è solo bordo).
2. **Il chiaro di fondo è `oklch(94.6% 0 89.9)` ≈ `#ededed`**, non bianco; il bianco `#ffffff` è la scheda su chiaro. Il testo su chiaro è lo stesso `#111111` del fondo scuro: **due superfici, un solo inchiostro**.
3. **Testo su scuro `oklch(93.4% 0 89.9)` ≈ `#e9e9e9`** (15,5:1), muted `oklch(63.3% 0 89.9)` ≈ `#8a8a8a` (5,5:1). Il bianco puro solo su prezzo, contatore, h1 e "FUNNEL".
4. **Un accento, quattro luci**: `#88c9f4` (80,8%) hover/focus, `#1d9cd7` (65,6%) base, `#0075be` (54,6%) pressione, `#015b97` (45,9%) link su chiaro. Nessun secondo colore di marca. Il verde `#009b12` e il rosso `#bd0000` sono **2 parole ciascuno** in 32.807px.
5. **L'accento si spende in testo (16) più che in decorazione (9) più che in bottoni (3)**: una parola per titolo, sempre il nome del prodotto o l'ultima parola.
6. **Due sans più una mono più un gotico**: Plus Jakarta Sans per i titoli (`--font-display`, h1-h6 in `@layer base`), Inter Tight per il corpo (`--font-sans`), DM Mono per cifre/etichette (`.codice`, `.font-tech`), Curseyt **solo per l'h1** con `font-display:block`. Tutto self-hosted woff2 in `/caratteri/`.
7. **Il corpo è 17px/1,6 con tracking +0,025em** (`.corpo`); i titoli hanno tracking negativo crescente con il corpo (−0,005 a 22px → −0,03 a 81px → −0,15 sulle cifre giganti). Il bottone è 14px/500/+0,03em (`.interfaccia`), **più piccolo del corpo**.
8. **La colonna è 832px** = 12 colonne × 40 + 11 canali × 32, margine pagina 24px; ogni larghezza interna è `calc(100% * n/832)` con n misurato in Figma.
9. **Padding di sezione `clamp(56px, 15vw, 96px)`** (`--spazio-vendita`); sotto-blocchi a 48/64/96 (`blocchi/sezioni/vendita`); interparagrafo dei testi giustificati in **em uguali al leading** (1,17–1,22).
10. **Raggio unico `--radius: .5rem`** = 8px su bottoni, foto, schede; 12px con bordo, 24px sulle schede "step", pill per avatar/play; raggio interno = raggio esterno − bordo (13 → 12).
11. **Bordi 1px** `#2c2c2c` su scuro, `#676767`/`#bfbfbf` su chiaro attorno alle foto, `#000` sulle schede diagramma; **2px solo sul raccoglitore**. Le foto su chiaro hanno sempre bordo + ombra spostata a destra-basso (2-7px, 2-11px, blur 15-40px, nero 19-32%).
12. **Una sola ombra colorata** in tutta la pagina: `0 6px 28px color-mix(in oklab, var(--fo-blue) 22%, transparent)` sotto il bottone sticky.
13. **Niente grana CSS** (la `.fo-grain` a 4,5% esiste ma non è assegnata: fondo piatto misurato al pixel). La materia è nelle WebP: roccia (blend lighten / opacity 28%), carta con fibre, mezzatinta.
14. **Immagini scure in bianco/nero fuse col fondo via blend**: `screen` per far sparire il nero, `difference` sul titolo che le attraversa, `color-dodge` per bruciare i chiari, `hard-light` per l'inchiostro su carta. Mai una maschera di ritaglio.
15. **Una curva sola** `cubic-bezier(.2, 0, 0, 1)` (`--curva`) e quattro tempi: 120ms stato, 160ms comparsa, 320ms momento, 90ms battuta (stagger). Hover del bottone = solo colore, 120ms, **si schiarisce** (`#88c9f4`) e si scurisce in `:active` (`#0075be`).
16. **Nessun reveal on scroll**: la pagina è tutta visibile subito. I soli movimenti continui sono i 5 marquee (`fo-rail`, 70s o 45s, linear, pausa in hover, maschera laterale 6-28%).
17. **`prefers-reduced-motion` in tre strati**: CSS (ingressi → dissolvenza, rail fermi, spinner a 2s, smooth scroll solo in `no-preference`), variant Tailwind (`motion-safe:`/`motion-reduce:`), JS (`matchMedia` ferma il carosello e lo scroll).
18. **I bottoni sono due**: primario `bg-fo-action text-fo-on-action` (azzurro con testo **nero** #111111, 6,1:1) e outline `bg-fo-surface border-fo-line`; taglia `lg` = 48px × padding 24px, `min-width: 7.5rem`, raggio 8px, mai ombra (tranne la sticky), mai transform.
19. **Immagini esportate a 2× dalla tavola 832**, sempre con `width`/`height`, `loading="lazy" decoding="async"` tranne l'hero (`eager sync fetchPriority=high`), `srcset` solo su hero e tessera, rapporto dichiarato in `aspect-[w/h]` uguale al file (zero ritagli reali salvo uno screenshot).
20. **Le forme "fisiche" sono CSS puro**: la linguetta del raccoglitore è un `clip-path: polygon()` a 12 vertici con spigoli arrotondati a mano (`--taglio = linguetta × 0.246`), i connettori tra step sono `border-dashed`, la sottolineatura dei link cresce da `background-size: 0% 1px` a `100% 1px`, il filetto luminoso è un gradiente alto 1px.

---

## 9. Confronto col canone Digital Empire

Fonte DE: `.claude/skills/fabbrica-siti/canone/canone.json` (v1.0.0, 2026-09-06) e `canone.css` (444 righe). Il perimetro è: **cosa portare nelle SEZIONI AGGIUNTE di agency-empire-landing** (CSS scopato sotto `.vivo`, legge 12/09: solo aggiungere, mai toccare il live).

| Area | Funnel Operator (misurato) | Digital Empire (canone) | Adottare nelle sezioni `.vivo`? |
|---|---|---|---|
| **Fondo scuro** | `#111111` (L 17,8%) unico | `--ink #1c1c1c`, `--ink-2 #0a0a0a` | **No**: il nostro `#1c1c1c` è già più chiaro e il live lo usa. Ma la sua **scala a 5 passi di 3-5 punti di L** (bg/surface/elevated/line) è un metodo da adottare: oggi il canone ha ink e ink-2 e basta, senza un `--surface` intermedio. Proposta: `--ink-surface: #262626` (L≈22% di 1c1c1c+4). |
| **Fondo chiaro** | `#ededed` (94,6%), non bianco | `--paper #fafafa`, `--grey #e8e8e6` | **Già simile** (`--grey` ≈ il suo). Niente da cambiare. |
| **Inchiostro su chiaro** | stesso `#111111` del fondo scuro | `--fg-on-light #1c1c1c` = `--ink` | **Già identico come principio** (un inchiostro solo). Confermato. |
| **Testo su scuro** | `#e9e9e9` pieno + `#8a8a8a` muted (due grigi) | `--fg #f9f9f9` con **scala di opacità** 1/.78/.76/.62/.55/.5/.42 | **No**: la nostra scala di opacità (da armageddon) è più raffinata dei suoi due grigi fissi. Teniamo la nostra. |
| **Accento** | azzurro `#1d9cd7` in 4 luci, saturazione ~0,76 HSL | `--orange #fb4604` (+bright/deep), regola saturazione max 0,70 con eccezione dichiarata | Il colore no (è suo). **Sì al metodo delle 4 luci**: noi abbiamo 3 (`orange`, `bright`, `deep`); manca la **quarta, chiarissima** per hover/focus su fondo scuro (il suo `#88c9f4` L 80,8%). Proposta: `--orange-light` ≈ `#ff8a4a` già presente in `text-silver-orange` → promuoverlo a token. |
| **Dove si spende l'accento** | testo 16 : decorazione 9 : bottoni 3 | "colore dell'azione, <10%" (memoria CCM) | **Sì, adottare la proporzione come gate**: nelle sezioni `.vivo` l'arancione va su **una parola per titolo** + il bottone, non su bordi/bubble/step-num tutti insieme (`canone.css` §10 ha 5 componenti arancioni: bubble, step-num, hl-block, card-dark:hover, btn). Ridurre. |
| **Hover del bottone** | solo colore, 120ms, si **schiarisce**; niente transform, niente glow che cresce | `.btn-orange:hover` → `translateY(-1px)` + glow da 40 a 60px | **Parzialmente**: teniamo il glow (è nostro), ma la regola "hover = più chiaro, active = più scuro" è più leggibile dello spostamento di 1px. Proposta per `.vivo .btn`: `hover → --orange-bright`, `active → --orange-deep`, senza translate. |
| **Testo del bottone** | **nero su azzurro** (6,1:1), non bianco (3,1:1) | bianco su arancione `#fb4604`: contrasto ≈ 3,3:1 | **Sì, da studiare**: il bianco su `#fb4604` non passa AA 4,5:1 a 14-16px (gate 6 del canone). O il testo del bottone diventa `#1c1c1c` (≈5,9:1 su fb4604) o il corpo del bottone sale a ≥24px. Andrei ha risolto col nero; noi abbiamo un gate che ce lo chiede. |
| **Tipografia: famiglie** | 4 (display / corpo / mono / gotico h1) | **max 2** (Onest + Onest) | **No**: la regola "una grida, una spiega" è più forte. Ma la sua **mono per le cifre** (DM Mono su contatore ed etichette) è un'idea: Onest non ha tabular? Ha `tabular-nums` (`.num-tabular` esiste). Restiamo a 2. |
| **Corpo** | 17px / 1,6 / +0,025em, colonna 832px (≈95ch giustificato) | body 1,66, `--measure-body 64ch`, `--measure-legal 88ch` | **No alla colonna a 95ch**: il nostro 64ch è più leggibile. **Sì al tracking positivo sul corpo piccolo** (+0,025/+0,03em sotto 17px): il canone dichiara solo `--tracking-display -0.025em`; aggiungere `--tracking-body: 0.01em` e `--tracking-ui: 0.03em` per bottoni/etichette. |
| **Tracking dei titoli** | negativo crescente col corpo: −0,005 → −0,15em | fisso −0,025em | **Sì**: rendere il tracking display una funzione del corpo (es. `clamp(-0.06em, calc(-0.0006em * (corpo_px)), -0.005em)`), almeno tre gradini: −0,015 (37px), −0,03 (63px), −0,04 (prezzo). |
| **Interlinea titoli** | 1,003 sui titoli "gancio", 1,0-1,2 sugli h2 | 1,08 | **Già in linea**. Il suo 1,003 su tre righe centrate (`titolo-gancio`) è un pattern da copiare come componente: "tre frasi, tre righe, peso 500, una sola parola bold". |
| **Padding sezione** | `clamp(56px, 15vw, 96px)` | `.section 6rem` (96px fisso), `.section-tight 4rem` | **Sì**: il clamp con `vw` scala su mobile senza breakpoint (il gate 3 del canone punisce i breakpoint non motivati: il clamp li evita). Proposta `.vivo .section { padding-block: clamp(56px, 15vw, 96px) }`. |
| **Colonna** | 832px = 12×40 + 11×32, frazioni `calc(100%*n/832)` | `--u: min(100vw, 1200px)`, frazioni di `--u` | **Già nostro** (da armageddon). La novità è che **la colonna è la somma di una griglia dichiarata** (`--griglia-colonne:12; --griglia-colonna:40px; --griglia-canale:32px`): dichiarare anche noi i tre numeri di `--u 1200` (es. 12 × 76 + 11 × 26,2) rende i `calc` leggibili. |
| **Raggi** | `--radius .5rem` unico, ±4px, interno = esterno − bordo | raggio come frazione dell'elemento (`--r-btn 0.0528`) + scala fissa 8/12/20/22 | **Già più raffinato il nostro**. Aggiungere solo la regola "raggio interno = raggio esterno − bordo" come nota in `canone.css` §5. |
| **Ombre** | nere, spostate a destra-basso (luce da sinistra-alto), valori Figma; 1 sola colorata | glow arancioni centrati (0 0 40px) su btn, bubble, step-num, hl-block, card-dark | **Sì, una regola**: "una sola ombra colorata per viewport" (lui: la sticky). Nelle sezioni `.vivo` il glow arancione va sul solo bottone primario; `card-dark:hover` e `bubble-orange` senza glow. |
| **Bordi** | 1px `#2c2c2c` (1,35:1 col fondo): filetto appena visibile | `--line-dark rgba(249,249,249,.08)` ≈ 1,3:1 | **Già identici in resa**. Confermato. |
| **Foto su chiaro** | sempre bordo 1px `#676767`/`#bfbfbf` + ombra 2-7px destra-basso + leggera rotazione (1,3-3°) | nessuna regola per le foto | **Sì**: aggiungere `.vivo .foto-incollata { border:1px solid rgba(28,28,28,.4); box-shadow: 2px 2px 17px rgba(0,0,0,.32); }` e la rotazione solo su ordine (rima con "grana sempre + scritte leggibili": la foto non galleggia). |
| **Grana** | CSS presente ma **spenta**; texture nelle WebP | doppio strato SVG turbulence, overlay + hard-light, fisso, **firma DE** | **No, la nostra resta** (legge di Max 2026-09-11: grana su tutto). Ma il dato è utile come prova: **il fondo piatto di Andrei sembra "pulito" perché le immagini portano la materia**; noi con grana + immagini lisce rischiamo l'effetto opposto. Nota per il brief immagini `.vivo`: mezzatinta o texture nelle immagini, coerenti con la grana. |
| **Blend delle immagini** | screen/difference/color-dodge/hard-light su WebP B/N a fondo nero | nessuna regola; `mix-blend-mode` solo sulla grana | **Sì, come tecnica**: le immagini scure delle sezioni `.vivo` esportate **con fondo nero pieno e in `mix-blend-mode: screen`** si fondono col `#1c1c1c` senza bordi visibili (attenzione: screen su `#1c1c1c` lascia un velo di 28 livelli: va testato, con `#111111` funziona, con `#1c1c1c` la trasparenza "nera" dell'immagine resta più scura del fondo). |
| **Curve** | 1 curva `cubic-bezier(.2,0,0,1)` + 4 tempi (120/160/320/90ms) | 2 curve (`ease-land`, `ease-heavy`) + 4 tempi (120/250/820/1200) | **Già nostro** e più espressivo (armageddon). La sua idea da prendere: **`--moto-battuta` 90ms come token dello stagger** con `animation-delay: calc(var(--battuta) * var(--moto-battuta))` → i nostri `.in--a/b/c` (180/340/500ms) diventano un solo `.in` con `--i: n`. |
| **Reveal on scroll** | assente; tutto visibile subito | `.in` con `reveal-rise`, `settle`, `is-locked` | **No**: le nostre sezioni `.vivo` possono avere l'ingresso (è armageddon). Ma il suo dato dice che la pagina regge senza. |
| **Marquee** | 5 rail con maschera 6-28%, 45/70s, pausa hover, copia `aria-hidden` | nessun componente | **Sì**: componente `.vivo .rail` per loghi/prove (`translate(-50%)` + duplicato `aria-hidden` + `mask-image` laterale + `:hover { animation-play-state: paused }` + spento in `prefers-reduced-motion`). |
| **reduced-motion** | CSS + variant + JS matchMedia | CSS §14 + "il gemello JS è obbligatorio" | **Già identici**. Il suo dettaglio da copiare: **gli ingressi non si spengono, diventano dissolvenze** (`fo-dissolvenza`), e lo spinner rallenta invece di fermarsi. Il nostro `animation: none !important` fa sparire i contenuti che entrano con `opacity: 0`? Verificare `.in` con `both`: se `from{opacity:0}` e l'animazione è `none`, l'elemento resta visibile (ok), ma la regola "dissolvenza al posto del movimento" è più elegante. |
| **Bottoni: quante varianti** | 2 in pagina (primario + outline), 1 taglia, 48px | `.btn-orange`, `.btn-ghost`, misure in frazioni di `--btn` | **Già in linea**. Sua regola da prendere: **`min-width` del bottone** (7.5rem) così "Sono pronto" e "Iscriviti adesso" hanno larghezze simili. |
| **Immagini** | WebP 2×, width/height sempre, lazy tranne hero, srcset sulle 2 pesanti | gate 9 peso ≤250 KB corsia A; nessuna regola su `loading`/`srcset` | **Sì, aggiungere al gate**: `width`+`height` obbligatori, `loading="lazy"` di default, `eager`+`fetchpriority="high"` solo sulla prima, `srcset` se il file > 100 KB. |
| **Clip-path forme** | linguetta a 12 vertici parametrica in cqw | nessuna | Curiosità tecnica, **non serve** alle sezioni `.vivo`. |
| **Uppercase** | 1 uso in tutta la pagina; niente occhielli | `.label` uppercase tracking .1em | Dato, non regola: il suo sito **non ha occhielli** e regge. Il nostro `.label` resta, ma nelle sezioni `.vivo` usare gli occhielli solo se portano informazione (non "SEZIONE 03"). |

### 9.1 In sintesi — 8 cose da portare nelle sezioni `.vivo`

1. Scala di superfici scure a passi di L (aggiungere `--ink-surface` tra `--ink` e le card).
2. Quarta luce dell'arancione per hover/focus + regola "hover schiarisce, active scurisce, niente translate".
3. Testo del bottone: verificare il contrasto bianco su `#fb4604` (3,3:1) contro il gate 6; valutare `#1c1c1c`.
4. Tracking: positivo sotto 17px (+0,025/+0,03em), negativo e crescente sui titoli (tre gradini).
5. Padding di sezione in `clamp(56px, 15vw, 96px)` al posto del `6rem` fisso.
6. Foto su chiaro "incollate": bordo 1px + ombra 2-7px destra-basso.
7. Componente rail/marquee con maschera laterale e copia `aria-hidden`.
8. Gate immagini: `width`/`height`, `loading`, `srcset` sopra 100 KB.

### 9.2 Cosa NON prendere e perché

- L'azzurro (è il suo brand; il nostro è `#fb4604`).
- La colonna a 95 caratteri giustificata (leggibilità; il nostro 64ch è misurato).
- Le 4 famiglie (regola DE "una grida, una spiega").
- Il fondo piatto senza grana (legge di Max; la grana è la firma).
- L'assenza di reveal (le nostre sezioni possono entrare; è armageddon, già canone).
- I due grigi fissi del testo (la nostra scala di opacità è più fina).

---

## 10. Fonti

Tutti i path sono relativi a `competitor/Andrei Pascu/site-study/`.

- `capture/66-funneloperator-it/src/38-styles-Cm6i-gBj.css` — CSS servito intero (148.142 byte): `@layer theme` (offset 2.526), `@layer base` (4.496), `@layer utilities` (8.602, 1.719 regole), `@font-face` ×13, `:root` (134.789), `@keyframes` ×13, `.fo-grain`, `.fo-rail`, `.sagoma`, `.girandola`, `.comparsa`, `.battuta`, `.lezione`, `@media (prefers-reduced-motion)`. Fonte online: `https://www.funneloperator.it/assets/styles-Cm6i-gBj.css`.
- `capture/66-funneloperator-it/estratto-css.md` — variabili (102), keyframes, filtri, blend, clip/mask, gradienti, curve, @font-face (generato da `scripts/analizza_css.py`).
- `capture/66-funneloperator-it/scheda.json` — `palette_testo`, `palette_sfondi`, `caratteri`, `scala_tipografica`, `pesi`, `raggi`, `ombre`, `effetti`, `keyframes`, `cta[]` (26), `sezioni[]` (30), `media[]`, `headings[]`.
- `capture/66-funneloperator-it/design-tokens.json` — gemello di `scheda.json` (chiavi in inglese: `palette_text`, `type_scale`, `radii`, `ctas`, `slices_desktop` 37, `slices_mobile` 44).
- `capture/66-funneloperator-it/src/36-routes-DT2uV_Ni.js` — il bundle della home: tutte le `className` citate (rail, blend, ombre, rotazioni, `loading`, `srcSet`, `tono: chiaro/scuro`, `setInterval` 1500ms, `matchMedia`).
- `capture/66-funneloperator-it/src/32-raccoglitore-Bj4iyfd5.js` — il raccoglitore: `clipPath: polygon(...)`, variabili `--gradino/--linguetta/--sporgenza/--taglio/--fianco/--corpo` in cqw.
- `capture/66-funneloperator-it/src/04-button-rHPgEXhH.js` — `buttonVariants` (cva): 6 varianti × 6 taglie.
- `capture/66-funneloperator-it/src/05-buy-button-DX_4IxaR.js` — stato caricamento/errore del bottone acquista.
- `capture/66-funneloperator-it/src/29-index-CLKYm5hM.js` — shell: header, footer, banner consenso (`backdrop-blur`), 404.
- `capture/66-funneloperator-it/media-inventario.md` + `media/` (68 file, 2.511 KB) — formato, px originali/resi, peso, alt.
- `capture/66-funneloperator-it/sezioni/01..30-*.png` — le 30 schermate di sezione, tutte guardate; misura della grana (dev. std 0,0) su `01`, `05`, `14`, `29`; `19` = roccia al 28%.
- `capture/66-funneloperator-it/media/` — guardati: `soldato-caduto`, `carta-metodo`, `carta-lezioni`, `carta-landing`, `carte-mano`, `gancio-insegna`, `serpente-testa`, `carta-serpenti`, `tessera`, `stack-clienti`, `motivo-teschio`, `motivo-spade`, `sec-avviso`, `albero-apsales`, `aeroplano`, `passo-2-checklist`, `fare-siti`, `zero-clienti`, `template-fasi`, `per-chi`, `telegram`, `lovable` (WebP) + `funops-logomark-gradiente`, `trustpilot`, `apertura`, `ordini`, `carriera-avviata` (SVG, letti come testo).
- `capture/66-funneloperator-it/dom-blocks.json` — 386 blocchi testuali (nessun attributo `loading`: la verifica lazy è sul bundle).
- `.claude/skills/fabbrica-siti/canone/canone.json` (v1.0.0) e `canone.css` — il canone Digital Empire per il §9.
- `reports/11-armageddon-ATLANTE-VISIVO.md` — frontmatter di riferimento e confronto col precedente studio Pascu.
- Conversioni: `scratchpad/oklch.py` (OKLCH → OKLab → LMS → sRGB lineare → gamma; contrasto WCAG 2.x). Valori dichiarati "calcolati": l'errore massimo atteso è ±1 su 255 per canale (verificato: `#1E9CD7` scritto a mano dall'autore vs `#1d9cd7` calcolato).

Cose che **non** ho potuto verificare e lo dichiaro: `roccia.webp` e `offerta-roccia.webp` non sono in `media/` (background CSS, non catturati); l'`index.html` non è in cattura, quindi non so se `fo-grain` sia sul `<html>` — ma la misura al pixel degli screenshot esclude che sia attiva sulla home; le pagine `/auth` e `.lezione` (area riservata) non sono state catturate: i token semantici e `.sagoma`/`.girandola`/`caret-blink` sono descritti dal solo CSS.
