# 40 — PIANO F4 · gli ordini di Max del 13/09 sera (18 allegati) — hero pulito, colori, storia dei preventivi, cervello

- **Data:** 2026-09-13 sera · **Cantiere:** `agency-empire-landing` (EMP-XR4F) · **Stato:** PIANO V4 esecutivo, si costruisce su «vai»
- **Allegati:** `agency-empire-landing/brief/F4-allegati/01..18` (estratti dal transcript, §6.25). Texture salvate intatte:
  `public/texture/grana-fuoco-ORIGINALE.jpg` (all. 13, 867×1093) · `public/texture/cervello-ORIGINALE.jpg` (all. 18, 1200×628).
- **Regola del piano:** ogni ordine = una task con file, modifica esatta, prova di chiusura. Niente si interpreta in silenzio: dove ho dovuto
  leggere fra le righe c'è la riga «INTERPRETO», e Max la corregge con una parola.

## 0. Mappa allegato → sezione → file

| All. | Cosa mostra | Sezione in pagina | File |
|---|---|---|---|
| 01 | hero attuale (sfondo ok) | `Hero` | `src/components/sections/hero.tsx`, `aggiunte-hero.css`, `funnel-hero.tsx` |
| 02 | 3 card scure (computer, mappa, timer 24) | riferimento per le card fluttuanti dell'hero | nuovo `src/sezioni-aggiunte/hero-card.tsx` |
| 03 | nastro grigio che scorre | `RailFatti` | `src/sezioni-aggiunte/rail-fatti.tsx` + css |
| 04 | «Tre sistemi…» con 3 card scure LIVE | `VslV2` | `src/sezioni-rifatte/vsl-v2.tsx`, `rifatte-a.css` |
| 05 | titolo largo su due righe, pesi misti | riferimento titolo per 04 | — |
| 06 | 3 blocchi 7gg/300+/0€ con gradiente argento→arancio + grana | **IL COLORE** | riferimento per 04 e 08 |
| 07 | «I numeri parlano chiaro» + «Per chi è» | `ScienceStats` + `Audience` | `science-stats.tsx`, `audience.tsx` |
| 08 | i 3 blocchi piccoli ora scuri | `ScienceStats` | idem |
| 09 | frase barrata | `FraseBarrata` | `src/sezioni-aggiunte/frase-barrata.tsx` |
| 10 | prima/dopo | `PrimaDopo` — la storia va PRIMA | nuovo `src/sezioni-aggiunte/storia-preventivi.tsx` |
| 11 | Service #02 Content Factory | `ContentDeep` | `src/components/sections/service-deep.tsx:107` |
| 12 | Due tipi di aziende + domande | `DueTipi` | `src/sezioni-aggiunte/due-tipi.tsx` |
| 13 | texture grana-fuoco | sfondo di 12 | `public/texture/grana-fuoco-ORIGINALE.jpg` |
| 14 | Service #03 Second Brain, blocco workflow scuro | `BrainDeep` | `service-deep.tsx:168` |
| 15 | blocco workflow blu-notte gradiente | **IL COLORE** del blocco di 14 | riferimento |
| 16 | 3 card blu/viola/teal gradiente | **IL COLORE** delle 3 card di 17 | riferimento |
| 17 | le due sezioni Second Brain intere | `BrainDeep` + `SecondBrainInside` | `second-brain-inside.tsx` |
| 18 | cervello a rete bianco su nero | sfondo che attraversa 14→17 | `public/texture/cervello-ORIGINALE.jpg` |

## 1. Le task (22) — blocco per blocco

### BLOCCO A — HERO (all. 01, 02, 03)
- **A1 · Pulizia.** `hero.tsx`: nascondere (CSS `display:none` in `aggiunte-hero.css`, non cancellare il JSX: gate B) → chip «Automazione AI
  Proprietaria · 2026» (r.75), pre-headline «Digital Empire · Agency · …» (r.80), link «Vedi prezzi e pacchetti ↓» (r.145), riga «SETUP IN 7
  GIORNI · GARANZIA · ZERO DIPENDENZE» (r.~150). **Restano:** «Automatizziamo la tua / operatività / con AI Workflows.», il paragrafo, il bottone,
  il funnel. INTERPRETO: «il titolo e il suo titolo» = titolo + il paragrafo sotto (è lui il «sottotitolo» di A2). *Prova:* screenshot 1920:
  nell'hero esistono solo 4 elementi + le card di A5.
- **A2 · Titolo largo quanto il sottotitolo.** Misuro col DOM la larghezza del paragrafo (oggi ≈ 800 px a 1920). Il titolo si porta a quella
  larghezza: `operatività` e `con AI Workflows.` scalate (`clamp`) finché la riga più larga = larghezza paragrafo ± 8 px; «Automatizziamo la
  tua» in proporzione. Mobile: `clamp` scende, mai oltre il viewport (chiude anche il bug «operativit» tagliata). *Prova:* `getBoundingClientRect`
  titolo vs paragrafo, differenza ≤ 8 px a 1920 e 1440; a 390 nessun overflow.
- **A3 · Bottone più piccolo.** `Prenota una Chiamata Gratuita →`: padding 18/40 → 12/26, corpo 17 → 15, altezza ≈ 46 px. *Prova:* misura.
- **A4 · Funnel più in alto.** Con A1 sparisce ≈ 120 px sopra: il funnel sale da solo; in più `margin-top` 96 → 48. Il funnel resta dentro il
  primo viewport a 1080. *Prova:* `bottom` del funnel ≤ 1000 px a 1920×1080.
- **A5 · 5 card fluttuanti originali** (2 a destra, 3 a sinistra, negli spazi liberi dell'hero). Stile dall'all. 02 (card scura arrotondata,
  illustrazione monocroma + titolo + riga) ma **contenuto e immagini completamente nostri**, un tocco d'arancio in ogni card. Contenuto
  (persuasivo, d'impatto, immediato): SX «300 messaggi/giorno · partono da soli» · «Setup in 7 giorni · dal contratto al go-live» · «0 € di
  canone · il codice è tuo»; DX «Gira sui tuoi server · nessuna dipendenza» · «Primo lead qualificato · entro la settimana 1». Immagini:
  5 still monocromi generati nostri (terminale, calendario, lucchetto aperto, server, busta): SVG/HTML puro dove possibile, altrimenti PNG
  2× ≥ 800 px, grana su tutto (D6). Desktop 1920: 3+2, assolute, ruotate ±3°, `z` sotto il testo; 1440: 2+2; ≤ 1279 px: nascoste (non c'è
  spazio libero). Nuovo file `src/sezioni-aggiunte/hero-card.tsx` + `aggiunte-hero.css`. *Prova:* nessuna card sovrappone
  titolo/paragrafo/bottone/funnel (bounding box disgiunte) a 1920 e 1440.
- **A6 · Nastro molto più sottile** (all. 03). `rail-fatti`: altezza ≈ 96 → 44 px, numero 40 → 20, etichetta 15 → 12, padding 0. *Prova:* misura ≤ 46 px.

### BLOCCO B — I COLORI (all. 04, 05, 06, 07, 08)
- **B1 · Titolo «Tre sistemi»** (all. 04→05). `vsl-v2.tsx`: da 4 righe strette a **due righe larghe**, struttura identica all'all. 05:
  riga 1 «Tre **sistemi**. Un'unica **operatività**» (400 + bold), riga 2 «**che gira da sola.**» (bold, corpo maggiore), allineato a sinistra
  sulla colonna 960, font del sito, il grassetto pesante come nell'allegato, grana come ora. Testo invariato → gate A intatto.
  *Prova:* screenshot a confronto con l'all. 05.
- **B2 · Il gradiente ufficiale.** UNA variabile in `rifatte-a.css`: `--grad-max: linear-gradient(160deg, #cfcbd6 0%, #b9b4c2 38%,
  #d98a5e 72%, #e8712f 100%)` + grana locale (`::before` fractalNoise, opacità .28, `overlay`) — campionato dall'all. 06 (argento lilla →
  arancio in basso a destra). Testo sopra: ink `#141414`, contrasto misurato ≥ 7:1 sulle zone chiare e ≥ 4,5:1 sull'arancio (testo bold).
- **B3 · Le 3 card grosse «Tre sistemi»** (all. 04) riempite con `--grad-max`: fondo gradiente + grana, testo ink, il numero grande
  `312/24/1.4k` in `#c93a12` (leggibile sull'argento), punto LIVE ink. Bordo 1 px `rgba(0,0,0,.25)`, ombra bassa. *Prova:* contrasto misurato
  su 6 punti, screenshot 2×.
- **B4 · I 3 blocchi piccoli 7gg/300+/0€** (all. 08→06): stesso `--grad-max`, esattamente come l'all. 06 (numero 40 ink, etichetta mono 12,
  riga 15). Sono le card di `science-stats.tsx` (i «ritocchi» di F3 le avevano spente: `ritocchi.css` → si toglie quella regola, dichiarato).
- **B5 · Un minimo di grana** su tutto lo sfondo di all. 07 (`ScienceStats` + `Audience`): la grana globale c'è ma lì è coperta dal fondo
  `#0d0d0d` opaco delle due sezioni → fondo trasparente + grana locale `.18`. *Prova:* crop 200×200 dello sfondo: rumore visibile.

### BLOCCO C — LE PICCOLE AGGIUNTE DI COPY (all. 09, 11)
- **C1 · Frase barrata + «=»** (all. 09). Accanto alla riga barrata «~~Ti serve un altro tool.~~» aggiungo « = » e «**Ovvero:** è un processo
  lungo e ripetitivo» (serif corsivo 400, argento, stessa riga a desktop, a capo su mobile). INTERPRETO: l'uguale sta sulla riga barrata
  (un altro tool = processo lungo e ripetitivo), non sulla riga «Ti serve un sistema»: se Max lo voleva sull'altra, sposto in 1 minuto.
- **C2 · La freccia elegante di Service #02** (all. 11). In `ContentDeep`: SVG hairline 1,2 px arancio, parte 12 px sopra il blocco di testo
  (mai a contatto), sale con una semicurva (bezier), punta 5 px; alla punta un testo piccolo (serif corsivo 15, argento):
  «Lo so, stiamo andando un po' di fretta… Ti sto già spiegando il mio secondo servizio. Nessuna confusione, mi raccomando: questo è un altro
  servizio. Non si tratta più di Outreach.» Ferma (39B §5: il movimento «sa di AI»). Mobile: freccia verticale corta, testo sopra.

### BLOCCO D — LA STORIA DEI PREVENTIVI (all. 10) — sezione NUOVA `StoriaPreventivi`, prima di `PrimaDopo`
- **D1 · Copy** in `brief/COPY-F4.md`, gate `gate_voce` + `gate_fatti` PASS prima del codice (§3 del 38). Nome del cliente **mai** («un'azienda
  che importa auto dalla Germania»). Apertura testuale di Max: «Ok, sto andando troppo veloce. Adesso ti faccio un esempio concreto…».
  Arco: 1) il rito quotidiano — annunci sul portale tedesco, decine di preventivi a mano, ore ogni giorno; 2) la richiesta; 3) l'app privata —
  incolli il link dell'annuncio → PDF col loro logo, le caratteristiche che hanno chiesto, il prezzo calcolato, in pochi secondi; 4) prima/dopo:
  ore → minuti; 5) la morale che aggancia la sezione dopo («la stessa cosa, pagata in due modi»).
- **D2 · Struttura visiva** (0 KB JS, HTML+CSS): a) apertura in serif grande su banda scura; b) **schema a 4 blocchi con frecce** (annuncio →
  link → app → PDF) nello stile del funnel-hero (frecce ferme, hairline); c) **un pezzetto in stile chat** — 3 bolle (cliente / noi / cliente)
  ricostruite in HTML, nomi generici, con orario, come una conversazione vera ma senza dati reali; d) **prima/dopo a due colonne** (ore vs
  minuti, numeri grandi); e) chiusura di una riga. Grana su tutto, palette ink/argento/accento, altezza ≤ 1.400 px desktop.
- **D3 · Gate:** `--parole` A PASS (è un'aggiunta), altezza misurata, contrasto delle bolle ≥ 7:1, 0 dati personali.

### BLOCCO E — DUE TIPI DI AZIENDE (all. 12, 13)
- **E1 · Copy aggiuntivo** sotto le due card: 2 righe eleganti (serif 18, argento), persuasive: «Il primo paga per sempre e non possiede nulla. Il
  secondo paga una volta e possiede tutto. Da qui in poi parliamo solo con il secondo.» — passa da `gate_voce`.
- **E2 · Sfondo = grana-fuoco di Max.** Dalla `grana-fuoco-ORIGINALE.jpg` (867×1093): **mai ingrandita** (§6.25 bis), tessera intera a tutta altezza,
  ripetuta in orizzontale con giunti sfumati a nero (stesso generatore `texture_hero_tile.py` parametrizzato → `grana-fuoco.jpg/.webp`).
  Sopra: velo nero **dietro il testo** (banda `rgba(0,0,0,.55)` con blur di bordo 24 px, solo dove passano titolo/card/domande), il resto
  della texture resta visibile. Card «Chi affitta / Chi possiede» restano argento (contrasto ≥ 7:1 misurato). *Prova:* screenshot 2× + contrasto.

### BLOCCO F — SECOND BRAIN (all. 14, 15, 16, 17, 18)
- **F1 · Blocco «Come funziona il workflow»** (all. 14→15): riempito col gradiente dell'all. 15: `linear-gradient(180deg, #0f1a33 0%, #132548
  50%, #0c1730 100%)` + bordo 1 px `#2b4a8a`, puntini blu `#4f7ad9`, testo bianco/argento. **Deroga di palette dichiarata** (blu su ordine
  testuale di Max, nota ADR-030). Contrasto ≥ 7:1.
- **F2 · Le 3 card Second Brain** (all. 16): riempite esattamente come l'allegato: card 1 blu-notte (`#0f1c3a→#0a1224`, icona in cerchio blu,
  piede «Struttura & Architettura» `#4f8de8`), card 2 viola (`#1b1636→#0f0c22`, `#7c5ce8`), card 3 teal (`#0f2a30→#0a1a1e`, `#26b5c4`), bordo
  1 px del colore a .35, testo bianco 600/argento 400. `second-brain-inside.tsx` + `ritocchi.css` (togliere la regola che le aveva appiattite).
- **F3 · Il cervello che attraversa le due sezioni** (all. 18 → 14+17): `cervello-ORIGINALE.jpg` (1200×628) **mai ingrandito**: posto a scala
  1:1 come layer assoluto di un contenitore che avvolge `BrainDeep` + `SecondBrainInside` (nuovo wrapper `src/sezioni-aggiunte/cervello.tsx`,
  in `page.tsx` +2 righe intorno ai due tag), allineato a destra, che **inizia nell'ultimo terzo della prima sezione e finisce nel primo terzo
  della seconda**; opacità .55, `mix-blend-mode: screen`, velo nero sfumato ai bordi (nessun taglio), sotto i testi. Mobile: opacità .3 e
  centrato. *Prova:* screenshot delle due sezioni intere; testo sopra il cervello con contrasto ≥ 7:1.

## 2. Ordine di costruzione, forze, gate

1. **Copy prima del codice** (D1, E1, C1, C2, A5): `brief/COPY-F4.md` → `gate_voce` + `gate_fatti`.
2. **Swarm** (aree disgiunte, prompt idempotenti): scagnozzo α = BLOCCO A · β = B + C · γ = D · δ = E + F. Io: B2 (il gradiente è uno solo,
   lo definisco prima e lo passo a β e δ), integrazione, gate, screenshot.
3. **Gate:** `gate_solo_aggiunte.py --parole` — DEROGA dichiarata: A1 nasconde 4 righe di testo dell'hero di giugno su ordine testuale di Max
   («devono scomparire») → `--consenti` su quelle 4 stringhe, scritto nel CP e in nota ADR-030. B: file di giugno toccati solo in aggiunta
   (hero.tsx: 0 righe rimosse, `display:none` da CSS).
4. **Prove:** screenshot 1920/1440/390 di ogni sezione toccata, guardati; misure DOM (A2, A3, A4, A6, D2); contrasti (B3, B4, E2, F1, F3).
5. **Anteprima** `npx vercel` → apro a Max → `--prod` suo.

## 3. I tre giri di critica

**P1 → P2.** (1) Il P1 diceva «ridurre il velo dell'hero» — Max non l'ha chiesto: tolto. (2) Il P1 metteva le card fluttuanti anche a 1440:
lì il paragrafo largo 800 lascia 320 px per lato → 2 card sì, 3 no: **a 1440 restano 2+2, a 1920 3+2**. (3) Il P1 scriveva la storia in 2.000 px:
troppo, la pagina è già 43.000 → tetto 1.400. (4) «=» su quale riga: ambiguità dichiarata invece che risolta in silenzio (C1).
**P2 → P3.** (1) Il P2 usava 3 gradienti diversi per B3/B4: Max ha detto «esattamente quello» → **una variabile**, `--grad-max`, e basta. (2) Il
cervello in P2 era `background-size: cover` → ingrandito 1,6×: viola §6.25 bis → 1:1, sfumato ai bordi. (3) La freccia di C2 in P2 era animata:
39B §5 la vieta → ferma. (4) F1 blu: il P2 lo «adattava» all'arancio — Max ha allegato il blu due volte: si fa blu, deroga dichiarata.
**P3 → V4 (questo).** (1) Aggiunto: contrasto misurato su OGNI riempimento colorato (l'all. 06 ha l'arancio sotto il testo). (2) Aggiunto A1
come `display:none` da CSS e non cancellazione JSX (gate B). (3) Mobile dichiarato per ogni task (card nascoste, freccia verticale, cervello .3).
(4) Peso: F4 ≈ 9 h nostre; la pagina cresce di ≈ +1.400 (storia) −120 (hero) −50 (nastro) = +1.230 px.

## 4. Cosa resta a Max
«vai» · guardare l'anteprima F4 · `--prod` · le 10 ridondanze 39B §4 (ancora aperte) · (se vuole) correggere le 2 righe INTERPRETO (A1, C1).
