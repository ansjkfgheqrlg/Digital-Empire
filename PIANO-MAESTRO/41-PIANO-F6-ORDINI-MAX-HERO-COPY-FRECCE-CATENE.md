# 41 — PIANO F6 · gli ordini di Max del 15/09 (18 allegati) — foto, headline nuova, card spillate, frecce, copy generico, catene

- **Data:** 2026-09-15 · **Cantiere:** `agency-empire-landing` (EMP-XR4F) · **Stato:** PIANO V4 esecutivo, si costruisce su «vai»
- **Allegati:** `agency-empire-landing/brief/F6-allegati/01..18` (estratti dal transcript, §6.25).
- **Regola del piano:** ogni ordine = una task con file, modifica esatta, prova di chiusura (misurata, non a occhio). Ogni task ha un
  CONTROLLO e un RICONTROLLO (due prove diverse). Dove ho letto fra le righe c'è «INTERPRETO»: Max corregge con una parola.
- **Legge di F6 (nuova, da Max):** fino alla sezione «Tre sistemi» il copy resta GENERICO — processi meccanici, ore perse, automatizzare
  la cosa giusta nel modo giusto — mai il nome di un prodotto (Outreach/Content/Brain) e mai «lavora mentre dormi» (non è sempre vero).
  I prodotti compaiono solo dalle loro sezioni in poi.

## 0. Mappa allegato → sezione → file

| All. | Cosa | Sezione | File |
|---|---|---|---|
| 01 | hero attuale | `Hero` | `hero.tsx`, `hero-foto.tsx`, `hero-card.tsx`, `f5-hero.css`, `f5-card.css` |
| 02 | Tre sistemi con «Cioè:» | `VslV2` | `vsl-v2.tsx`, `f5-frecce.css` |
| 03 | Per chi è questo sistema (2 blocchi) | `Audience` | `audience.tsx` (giugno) + css |
| 04 | frase barrata + smorfia | `FraseBarrata` | `frase-barrata.tsx`, `f5-frecce.css` |
| 05 | «Ti voglio bene, ma lo stai facendo a mano» | `Specchio` | `specchio.tsx` |
| 06 | «ASCOLTA BENE» | `ListenUp` | `listen-up.tsx` (giugno) |
| 07 | storia preventivi | `StoriaPreventivi` | `storia-preventivi.tsx`, `f4-storia.css` |
| 08 | «La stessa cosa, pagata in due modi» | `PrimaDopo` | `prima-dopo.tsx` |
| 09 | Scala dell'operatività + Perché Digital Empire | `Hierarchy` + `Pillars` | css |
| 10 | Framework F.L.O.W. | `FlowFramework` | `flow-framework.tsx` (giugno) + css |
| 11 | le 3 card gradiente (riferimento colore) | — | `--grad-max` |
| 12 | «Ogni sistema, nel dettaglio» 3 blocchi scuri | `SystemsShowcaseV2` | `systems-showcase-v2.tsx`, css |
| 13-15 | le 3 tessere CTA | `CtaProdotto` ×3 | `cta-prodotto.tsx`, `f5-cta.css` |
| 16 | Service #02 con freccia | `ContentDeep` | `service-deep.tsx`, `f5-frecce.css` |
| 17 | il laccio della tessera | `CtaProdotto` | `f5-cta.css` |
| 18 | blocco workflow Second Brain (blu) | `BrainDeep` / `SecondBrainInside` | `f4-brain.css` |

## 1. Le task (31) — blocco per blocco

### BLOCCO A — HERO (all. 01)
- **A1 · Foto più a sinistra, più grandi, meno nascoste.** `f5-hero.css` (`.hf-group`, `.hf-photo--1/2/3`): gruppo da `right: 3vw` a
  `right: 9vw` (≈ 170 px a 1920), larghezza 330 → 400 px; foto 1 100 %, foto 2 88 % spostata sotto-sinistra con sovrapposizione ≤ 20 %
  (non più 40 %), foto 3 55 % in basso-destra che tocca appena la 2. Distanza minima dal paragrafo ≥ 60 px. *Controllo:* bounding box
  foto vs h1/p/bottone/card = 0 intersezioni a 1920 e 1440; foto 2 visibile ≥ 80 % della sua area (calcolo delle sovrapposizioni).
  *Ricontrollo:* screenshot 1920 guardato: le tre foto si leggono tutte.
- **A2 · Headline NUOVA, pesi misti.** `hero.tsx` è di giugno (0 righe rimosse): il testo di giugno si NASCONDE da CSS e il nuovo va in
  un componente aggiunto `src/sezioni-aggiunte/hero-titolo.tsx` (`HeroTitolo`), montato con 2 righe aggiunte. Testo esatto di Max:
  «Siamo l'**agenzia** che elimina il **lavoro ripetitivo** dal tuo business. **Per sempre.**» — 3 righe, 400 argento + 800 bianco
  sulle parole in grassetto; `operatività`-style scala (≈ 64-72 px a 1920, clamp), line-height 1.02.
  Sottotitolo esatto di Max: «Hai **processi meccanici** che ti mangiano ore ogni settimana e che potrebbero **girare da soli** — ma ogni
  tool che hai provato era più complicato del problema stesso. Noi costruiamo l'**automazione su misura** e te la consegniamo in
  un'**app privata** dove basta **un click** per far partire tutto. **Zero configurazione. Zero manuali.** Il tuo processo gira in
  automatico, tu torni a fare quello che conta. È una soluzione **concreta e semplice**, senza complicazioni inutili, a un **problema
  reale**.» — 18 px argento, grassetti bianchi 600. INTERPRETO: le parole in grassetto le ho scelte io (termini importanti, minoranza);
  Max ne cambia quante vuole. DEROGA ADR-030 dichiarata: il titolo di giugno sparisce su ordine testuale (gate `--consenti`).
- **A3 · Le ombre strane sopra le scritte.** Causa vera (letta nel CSS): `operatività` ha `background-clip: text` con gradiente + la
  `text-shadow` di F5 + la grana `::after` del velo in `mix-blend-mode: overlay` che passa SOPRA il testo → macchie scure. Fix: il
  titolo nuovo è bianco/argento pieno (niente clip), `text-shadow` tolta, la grana del velo va sotto il testo (`z-index`), l'ombra
  resta solo nel layer dietro (radial nero). *Controllo:* campiono 30 pixel dentro le lettere bianche: luminanza ≥ 235 su tutti.
- **A4 · Card: bordo bianco sottile con grana, spilla d'argento, una sopra l'altra, più piccole a sinistra.** `f5-card.css`: bordo
  `1px solid rgba(255,255,255,.22)` non luminoso + grana sul bordo (secondo `::before` con `mask` sul bordo, opacity .5); **spilla**:
  elemento `.f4-card-spilla` (aggiunto in `hero-card.tsx`) 10 px, in alto al centro, gradiente argento radiale con riflesso e ombra
  di 2 px, realistica; sinistra: scala .80 → .70, impilate con sovrapposizione 8-14 px sugli angoli (rotazioni alternate); destra:
  le 2 card una sopra l'altra con sovrapposizione ≈ 16 px. Leggibilità: il testo di ogni card resta interamente visibile (le
  sovrapposizioni toccano solo gli angoli senza testo). *Controllo:* per ogni card, l'area del testo (`h3`+`p`) non è coperta da un'altra
  card (bounding box). *Ricontrollo:* screenshot ravvicinato dei due gruppi guardato.

### BLOCCO B — TRE SISTEMI (all. 02): le frecce
- **B1 · Tre frecce diverse, tutte complete, sottili, eleganti** (`vsl-v2.tsx` + `f5-frecce.css`): card 1 (Outreach) → freccia parte
  8 px fuori dall'ANGOLO alto-destro e sale verso destra (curva, 90-110 px, punta 5 px), nota in alto a destra della card;
  card 2 (Content) → parte dal BASSO (centro, 8 px sotto), scende con curva più lunga e visibile (80 px), nota sotto;
  card 3 (Brain) → parte dal BORDO destro a metà altezza (8 px fuori, non da un angolo), va verso l'alto-destra, nota lì.
  Stroke 1,3 px, arancio, `marker` punta sempre visibile. Le tre note («Cioè: …») restano. Niente animazione. Mobile: tutte dal basso.
  *Controllo:* 3 misure: distanza inizio-freccia dal bordo card 6-10 px; nessuna intersezione freccia/card/testi; la punta dentro il
  viewport. *Ricontrollo:* screenshot 2× guardato.

### BLOCCO C — PER CHI È (all. 03)
- **C1 · Via i blocchi, restano le scritte, grassetti.** `audience.tsx` è di giugno → da CSS (`f6.css`): le due card perdono fondo,
  bordo, ombra, padding (diventano colonne di testo su fondo section); le due etichette «È per te se / Non è per te se» restano come
  righe mono. Grassetti: da CSS non si può → aggiungo (solo aggiunte) `<b>` intorno ai termini importanti nelle `<li>` — testo
  identico parola per parola (gate parole). *Controllo:* `--parole` PASS; numstat audience.tsx: 0 righe cancellate (le righe con
  `<b>` sono righe MODIFICATE = 1 cancellata per il gate git → INTERPRETO: uso `f6-grassetti.tsx` che sovrascrive il testo
  via componente aggiunto? no — troppo. Scelta: le `<li>` di giugno restano intatte, aggiungo DENTRO ogni `<li>` niente. Alternativa
  pulita: nascondo le `<li>` di giugno da CSS e monto una lista gemella con i grassetti in `sezioni-aggiunte/audience-grassetti.tsx`
  (stesso testo). DEROGA dichiarata come A2.)

### BLOCCO D — FRASE BARRATA (all. 04)
- **D1 · Nota sotto la punta della freccia.** `f5-frecce.css`: la nota della smorfia si allinea alla punta (freccia che scende dalla
  foto 10 px fuori, nota 8 px sotto la punta, allineata a sinistra della punta). *Controllo:* distanza punta-nota 6-12 px, 0 intersezioni.
- **D2 · Testo nuovo della nota:** «La faccia di chi ha una nostra applicazione custom che gli sostituisce 5 tool da 60 € al mese
  ognuno.» (numeri: 5 e 60 vanno in `FATTI` come `toolSostituiti: 5`, `toolEuroMese: 60` → gate fatti PASS).
- **D3 · Il «= Ovvero»** va DOPO «Ti serve un sistema che gira senza di te.» e la frase è «**Ovvero:** *automatizzare un processo
  lungo e ripetitivo*». La riga barrata torna sola. *Controllo:* screenshot; `--parole` PASS.

### BLOCCO E — COPY GENERICO (all. 05, 06) — la legge di F6
- **E1 · Specchio «Ti voglio bene, ma lo stai facendo a mano».** `specchio.tsx` (nostra): riscrivo il corpo senza Outreach e senza DM
  di concessionario: esempi GENERICI in serie (preventivi ricopiati a mano, lo stesso report ogni lunedì, i dati da un foglio all'altro,
  la stessa mail 30 volte), il principio «se lo fai ogni giorno uguale, è una macchina che lo deve fare», poi: automatizzare lo fa
  anche MEGLIO o più IN GRANDE (a seconda del processo); poi la chiamata gratuita: «non tutto va automatizzato — in 30 minuti guardiamo
  la tua situazione e ti diciamo se possiamo aiutarti davvero, su un problema concreto»; chiusura: «oggi con l'AI si automatizza tutto;
  la differenza è automatizzare le cose giuste nel modo giusto — le aziende che l'hanno capito scalano così». La finta chat resta ma
  con un esempio generico (un foglio di preventivo, non un DM). Grassetti misti. Copy in `brief/COPY-F6.md` §E1, gate voce+fatti.
- **E2 · «ASCOLTA BENE».** `listen-up.tsx` è di giugno → il testo di giugno si nasconde da CSS e il nuovo va in
  `sezioni-aggiunte/ascolta-bene-v2.tsx` (DEROGA dichiarata, come A2): via «Outreach», via «lavora mentre dormono»; resta la struttura
  (titolo, 4-5 paragrafi, una citazione): la citazione diventa «*Loro hanno smesso di fare a mano quello che una macchina fa uguale.*»
  Generico ma concreto. Copy in `COPY-F6.md` §E2.
- **E3 · Prima/Dopo (all. 08):** sopra il titolo una riga grande nuova: «**La differenza** tra un prodotto **custom** e i tool del
  mercato…» (INTERPRETO: Max ha scritto «La mia differenza»: la rendo «La differenza» — se la vuole «mia», una parola). Le due
  schede restano ma SENZA la parola «outreach»: «Abbonamento outreach» → «Abbonamento a un tool», «Sistema outreach» → «Sistema
  custom, tuo»; prezzo `LISTINO.outreach` resta come esempio numerico senza nominarlo. Anche il ponte sopra (fine storia) senza nomi.

### BLOCCO F — STORIA PREVENTIVI (all. 07)
- **F1 · Più bella:** due colonne a desktop (testo a sinistra 56 %, a destra un'immagine dalla cartella di Max: INTERPRETO «la cartella»
  = `brief/F5-allegati` + `F6-allegati` + `public/foto`: scelgo `rif-pensa.jpg` è già usato → uso un still nostro generato dal
  generatore di card (stile stampa: un PDF che esce da uno schermo) — se Max intende un'altra cartella, mi dà il path); la chat più
  bella (bolle con ombra, avatar iniziali, «visto» in mono, larghezza 420, sfondo carta scura); schema a 4 blocchi con frecce curve
  invece che rette; 2 frecce con spiegazione (una dalla chat → «questa è la richiesta vera, riassunta», una dallo schema → «ogni
  passaggio che prima era una persona»), note su spazi vuoti, mai sopra il testo; grassetti misti nel racconto. *Controllo:* altezza
  ≤ 1.500 px; 0 intersezioni frecce/testo.

### BLOCCO G — SFONDI E FRAMEWORK (all. 09, 10)
- **G1 · Scala + Perché DE: stesso sfondo, nessun divisore.** `f6.css`: le due section (`hierarchy`, `pillars`) prendono lo stesso fondo
  (carta con grana identica), `border-top` e ombre di giunzione azzerate, padding continuo. *Controllo:* campiono 5 pixel sopra e sotto
  la giunzione: stesso colore ±3.
- **G2 · F.L.O.W.: freccia verso il basso + nota.** Da un punto sotto il titolo/sottotitolo, freccia sottile che scende un po' verso il
  basso-destra fino a una nota mono: «Questo è un framework generico e sintetico: serve a far capire, in modo vago, come lavoriamo.
  Ogni lavoro è personalizzato e diverso — F.L.O.W. è uno slogan, non il progetto.» Aggiunta in `flow-framework.tsx` (solo righe
  aggiunte) o wrapper. *Controllo:* 0 intersezioni.

### BLOCCO H — I COLORI (all. 11, 12, 13-15, 18)
- **H1 · «Ogni sistema, nel dettaglio»:** i 3 blocchi riempiti con `.grad-max` (identico alle card di «Tre sistemi»): testo ink,
  numeri `#c93a12`, spunte ink, «Prenota ora» resta arancio. `systems-showcase-v2.tsx` + css. *Controllo:* contrasto ≥ 4,5:1 su 6 punti.
- **H2 · Le 3 tessere CTA:** riempite con `.grad-max`, testo ink. *Controllo:* idem.
- **H3 · Second Brain (blocco workflow + 3 card):** grana identica a `.grad-max` (stesso `::before` feTurbulence .30 overlay) ma coi
  loro colori blu/viola/teal. `f4-brain.css`. *Controllo:* crop 200×200: rumore visibile come nelle card arancio.

### BLOCCO I — SERVICE #02 (all. 16)
- **I1 · Freccia sistemata, nota più grande e più esterna:** parte 10 px a destra del badge, va in alto a destra più lunga (120 px), la
  nota a 14-15 px (era 12), max-width 240, ancorata al bordo destro della colonna con 24 px di aria dal testo. *Controllo:* 0
  intersezioni; distanza nota-testo ≥ 24 px.

### BLOCCO L — CATENE (all. 17)
- **L1 · Via il laccio, catene realistiche** attaccate alla scritta sopra (la lettera «O» di FACTORY/BRAIN… INTERPRETO: «attaccate alla
  lettera» = la tessera pende da una lettera della seconda parola del titolo): due catenelle in CSS/SVG (anelli 8×5 px argento con
  ombra e riflesso, 14-18 anelli, leggermente oblique), dal punto basso della lettera al foro della tessera; la tessera oscilla di -2°.
  Realistiche: gradiente metallico per anello + `drop-shadow`. `f5-cta.css` + `cta-prodotto.tsx`. *Controllo:* screenshot 2× guardato;
  la catena parte entro 4 px dal glifo (misuro col `Range.getBoundingClientRect` della lettera).

### BLOCCO M — VIA UNA SEZIONE
- **M1 · «Niente black box. Ogni tool spiegato e consegnato.»** = `ToolStackV2` (sezione di giugno rifatta): si SMONTA da `page.tsx`
  (1 riga −1: DEROGA-B dichiarata su ordine testuale «va completamente eliminata»; il testo di giugno resta nel repo). `NoFluff` che sta
  prima resta. *Controllo:* il gate `--parole` con `--deroga-b page.tsx`; la stringa «Niente black box» assente dal build.

## 2. Ordine, forze, gate
1. **Copy prima del codice:** `brief/COPY-F6.md` (A2, D2, D3, E1, E2, E3, F1 note, G2) → `gate_voce` + `gate_fatti` (con `FATTI.toolSostituiti`, `toolEuroMese`).
2. **Swarm** (4 scagnozzi, prompt idempotenti): α = A (hero) · β = B + D + I + G2 (tutte le frecce) · γ = C + E + F (copy generico +
   storia) · δ = G1 + H + L + M (sfondi, colori, catene, smontaggio). Io: COPY-F6 e il generatore dello still per F1, integrazione, gate.
3. **Gate:** `gate_solo_aggiunte.py --parole --consenti <titolo giugno hero|audience li|listen-up>` con le deroghe scritte nel CP e in
   nota ADR-030 (3ª deroga su ordine); `--deroga-b page.tsx` per M1. Prezzi: grep 0.
4. **Prove:** ogni task ha controllo + ricontrollo (sopra); screenshot 1920/1440/390 delle 12 sezioni toccate guardati da me.
5. **Anteprima** → apro a Max → `--prod` suo.

## 3. I tre giri di critica
**P1→P2.** (1) P1 modificava `hero.tsx`/`audience.tsx`/`listen-up.tsx` in place: viola ADR-030 (giugno intatto) → tutto via componenti
gemelli + CSS che nasconde, deroghe dichiarate. (2) P1 non spiegava le «ombre strane»: cercata la causa nel CSS (clip-text + overlay
sopra il testo) — si cura la causa, non il sintomo. (3) P1 lasciava «outreach» nelle schede prima/dopo: Max l'ha detto due volte → via.
**P2→P3.** (1) P2 usava un'immagine di stock per F1: vietato (§14/originalità) → still nostro generato. (2) Le catene in P2 erano un PNG:
a 2× sfocano → CSS/SVG vettoriale. (3) P2 ingrandiva le foto del 40 %: a 2× DPR 400 px = 800 device px < 1101: ok, ma la 3ª (555 px) a
220 CSS px = 440 device px: ok — verificato che nessuna supera 1:1.
**P3→V4.** (1) Aggiunto il RICONTROLLO (seconda prova) a ogni task, come ordinato («controllata e ricontrollata»). (2) La legge del copy
generico scritta in cima come regola, non come task: vale anche per chi lavora dopo. (3) 3 INTERPRETO dichiarati: grassetti scelti da
me (A2), «La differenza» vs «La mia differenza» (E3), «la cartella» (F1), «attaccate alla lettera» (L1).

## 4. Cosa resta a Max
«vai» · le 4 INTERPRETO se vuole cambiarle · guardare l'anteprima · `--prod`.
