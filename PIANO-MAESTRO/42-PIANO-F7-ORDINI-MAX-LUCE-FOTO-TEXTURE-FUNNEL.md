# 42 — PIANO F7 · gli ordini di Max del 15/09 sera (3 allegati) — luce sulle foto, texture nitida con nero dietro le scritte, sottotitolo corto, funnel rifatto, nota sinistra dei Tre sistemi

- **Data:** 2026-09-15 sera · **Cantiere:** `agency-empire-landing` (EMP-XR4F) · **Stato:** PIANO V4 esecutivo (P0→P3 sotto), si costruisce subito (permesso permanente).
- **Allegati:** `agency-empire-landing/brief/F7-allegati/01..03-ORIGINALE` (estratti dal transcript, §6.25): 01 hero intero, 02 il funnel, 03 i Tre sistemi.
- **Regola:** ogni ordine = una task con file, modifica esatta, prova misurata. «INTERPRETO» dove ho letto fra le righe. Legge F6 (copy generico fino ai Tre sistemi) resta in vigore.

## 0. Gli ordini di Max, parola per parola → task

| # | Ordine (testuale) | Task |
|---|---|---|
| 1 | «le mie foto sono brutte, sembra che ci sia un'ombra sopra … devono essere luminose e io nitido … più luminoso normalmente» | A1 |
| 2 | «un'immagine toglila, tre sono troppe, lasciamone due» | A2 |
| 3 | «da un'immagine deve partire una freccia che non disturba niente, va all'esterno, con la scritta "Questo sono io mentre parlo… Tra l'altro sono Maximilian, titolare di Digital Empire. (la mia storia è in fondo)"» | A3 |
| 4 | «la texture è tutta ombreggiata, oscurata … deve vedersi benissimo, nitida, più chiarezza … tranne dove ci sono le scritte: dietro completamente nero, un'ombreggiatura che si espande un minimo e poi sparisce, di qualità» | B1, B2 |
| 5 | «il sottotitolo è troppo lungo: quasi metà tagliata, riscrivilo mettendo il più possibile» | C1 |
| 6 | «lo schema (funnel) deve migliorare molto, contenuto ed estetica» | D1 |
| 7 | «Tre sistemi: la freccia sotto il titolo non va bene; fai come nel blocco di destra, anche a sinistra, chirurgico» | E1 |

## 1. I FATTI MISURATI (prima di pianificare — §3, niente a occhio)

- **Foto sorgente:** `max-hero-1.jpg` luminanza media **112,6**, `-2` 111,5, `-3` 91,0 (la 3 è la più scura e la più piccola: 555×544, ritaglio).
  **Foto in pagina (allegato 01):** foto1 **64,5**, foto2 63,4, foto3 41,4 — **−43 %** rispetto al sorgente. Max ha ragione: c'è un'ombra sopra.
- **Texture sorgente:** `hero-onde-ORIGINALE.jpg` media 18, picchi **238**. **In pagina:** media 3-4, picchi **34-64**. La texture è schiacciata a 1/5.
- **La causa vera (letta nel CSS, non supposta):** `globals.css` `.grain-fine::before/::after` — la grana globale del sito è **NERA**
  (`feColorMatrix` con R=G=B=**0**, alpha 1.6×rumore), `overlay` a .55 + `hard-light` a .28. Overlay/hard-light con il nero = **multiply**:
  scurisce tutto ciò che non è già nero — foto, texture, mezzitoni. È QUESTA l'ombra su tutto. Il velo `.hero-tex-velo` (.38 al centro,
  .80 in basso) e la grana `.hf-photo::after` (.25, chiara: NON scurisce) sono concause minori sulla texture, nessuna sulle foto.
- **Lettere a 210 (CP-U7WT, lezione 2):** era la conseguenza della grana nera, non una legge: la legge di Max è «grana sempre» (11/09), non
  «grana che scurisce». Una grana a luminanza neutra (rumore grigio attorno a 0,5) resta grana visibile e non toglie luce.
- **Nota «la mia storia è in fondo»:** la sezione di giugno `who-guides.tsx` («Ok ma chi siete?») **non ha id** → serve un'ancora aggiunta.
- **Funnel (all. 02):** «300 messaggi al giorno» nell'ultima tappa **viola la legge F6** (copy generico fino ai Tre sistemi: è un numero
  Outreach). Frecce tratteggiate + «ghost» sotto: leggibili male sulla texture, e con la texture più chiara lo saranno ancora meno.
- **Tre sistemi (all. 03):** la nota di card 1 è variante `top` (sotto il titolo). Card 3 è `right` (≥1600, fallback `bottom`). Il margine
  di pagina a sinistra a 1920 è ≈ 245 px (container 1024 centrato + ra-col): c'è spazio per una nota di 200 px.

## 2. LE TASK (piano V4 esecutivo)

### BLOCCO A — LE FOTO
- **A1 · Luce normale sulle foto (e su tutto).** File NUOVO `src/app/f7-luce.css` (importato per ultimo in `layout.tsx`, 1 riga aggiunta):
  ridefinisco `background-image` di `.grain-fine::before` e `::after` con la **stessa** feTurbulence (stesse frequenze, ottave, tile) ma
  `feColorMatrix` che porta il rumore su R=G=B (grigio attorno a 0,5) e alpha piena → stesse opacità (.55/.28), stessi blend: la grana resta
  identica per grana, **cambia solo che non scurisce più** (overlay/hard-light con 0,5 = identità in media). DEROGA dichiarata: tocca
  l'aspetto di tutto il sito (schiarisce i mezzitoni ovunque; il nero resta nero). Sulle foto in più: `.hf-photo::after` opacità .25 → .16
  e `filter: contrast(1.04)` sull'`img` (nitidezza percepita; niente sharpen artificiale). *Controllo:* luminanza media della foto 1 in
  screenshot ≥ 100 (era 64); picco ≥ 225. *Ricontrollo:* screenshot guardato: il volto è chiaro e netto.
- **A2 · Due foto, non tre.** `hero-foto.tsx` (file nostro di F5): tolgo il blocco `hf-photo--3` (INTERPRETO: è la più scura, la più piccola,
  un ritaglio: la peggiore delle tre). Layout ≥1280 in `f7-foto.css` (file NUOVO): foto1 in alto a destra 100 % del gruppo, rotate −3°;
  foto2 sotto-sinistra 84 %, rotate +2,5°, sovrapposizione ≤ 15 % sull'angolo, mai sul volto. Fascia 768-1279: due in riga. *Controllo:*
  DOM con 2 `.hf-photo`; bounding box foto2 ∩ foto1 ≤ 15 % dell'area di foto2.
- **A3 · La freccia che esce da una foto + la nota.** In `hero-foto.tsx` aggiungo dentro `.hf-group` un blocco `.hf-nota` (nota + SVG
  freccia). Freccia: parte 8 px sotto il bordo inferiore di foto2 (centro-sinistra), curva sottile (1,3 px, arancio, punta 5 px, NIENTE
  tratteggio) verso il basso-sinistra, ~90 px; la nota sta sotto le foto, allineata a sinistra del gruppo, mono 12,5 px argento, max 30 ch,
  con «Maximilian» e «Digital Empire» in bianco; «(la mia storia è in fondo)» = `<a href="#chi-siamo">` sottolineato tratteggio. Ancora:
  `<div id="chi-siamo" className="scroll-mt-24" />` AGGIUNTO in `page.tsx` prima di `<WhoGuides />`. Testo ESATTO di Max:
  «Questo sono io mentre parlo… Tra l'altro sono Maximilian, titolare di Digital Empire. (la mia storia è in fondo)».
  Il gruppo passa da `aria-hidden` decorativo a: foto `alt=""` (restano decorative) ma la nota è testo vero → `aria-hidden` tolto dal
  gruppo, messo sulle sole foto. Visibile ≥1280; sotto, nascosta (dichiarato: nella fascia 768-1279 le foto stanno in riga sotto il testo e
  la freccia non avrebbe un «esterno»). *Controllo:* bounding box nota ∩ (foto, funnel, card r1/r2, testo) = ∅ a 1920 e 1440; distanza
  inizio-freccia dal bordo foto 6-10 px. *Ricontrollo:* screenshot guardato: la freccia non disturba niente.

### BLOCCO B — LA TEXTURE
- **B1 · Texture nitida, chiara, senza velo.** `f7-luce.css`: `.hero-tex-velo { background: linear-gradient(180deg, transparent 0 84%,
  rgba(5,4,3,.85) 100%) }` (resta solo la sfumatura a nero in fondo, per cucire la sezione dopo) e `.hero-tex-velo::after` opacità .35 →
  .18 (grana locale resta, D6). Sull'`img`: `filter: brightness(1.28) contrast(1.12)` — la texture sale di luce e nitidezza senza un pixel
  inventato (regola §6.25: scala ≤ 1:1 invariata). *Controllo:* nella zona vuota della texture (in basso a sinistra, sotto il bottone)
  picco ≥ 170 (era 34-64), media ≥ 12 (era 4). *Ricontrollo:* screenshot: le onde si leggono nitide su tutta la sezione.
- **B2 · Nero dietro le scritte, che si espande e sparisce.** `.f6-titolo` e `.funnel-hero` ricevono un `::before` (`z-index:-1`, dentro
  il loro contesto a z 3 → sopra texture/velo/foto, sotto il testo): `inset: -56px -96px` (funnel: -40px -72px), fondo a **due strati**
  `radial-gradient(ellipse at 50% 50%, #000 0 48%, rgba(0,0,0,.92) 62%, rgba(0,0,0,.55) 78%, transparent 100%)` — nero pieno al centro
  (dove sta il testo), sfumatura lunga e morbida verso i bordi (niente `filter: blur` su elementi grandi: costo di paint, e il risultato
  a gradiente è più controllato). Le card di sinistra e le foto hanno già il loro fondo: nessuna aura. *Controllo:* 30 pixel campionati
  dietro le lettere (fra le righe del sottotitolo) luminanza ≤ 8; a 100 px oltre il bordo del blocco la texture è ≥ 60 % della sua
  luce. *Ricontrollo:* screenshot: il nero non ha un bordo visibile.

### BLOCCO C — IL SOTTOTITOLO
- **C1 · Metà.** `hero-titolo.tsx` (nostro): da 78 a ≤ 42 parole, tenendo i concetti nell'ordine di Max: processi meccanici che mangiano ore
  → potrebbero girare da soli → automazione su misura → app privata → un click → zero configurazione, zero manuali → torni a fare quello
  che conta. Testo V4: «Hai **processi meccanici** che ti mangiano ore ogni settimana e che potrebbero **girare da soli**. Noi costruiamo
  l'**automazione su misura** e te la consegniamo in un'**app privata**: **un click** e parte tutto. **Zero configurazione, zero manuali.**
  Tu torni a fare quello che conta.» (41 parole). Gate `--parole`: il sottotitolo F6 non è mai andato in prod → nessuna deroga nuova sul
  live; nel confronto con la build precedente è una riscrittura su ordine (dichiarata). *Controllo:* conteggio parole ≤ 42; `f6-sub`
  max-width invariata → 4 righe a 1920 (erano 6).

### BLOCCO D — IL FUNNEL
- **D1 · Rifatto: contenuto generico e forma pulita.** `funnel-hero.tsx` (nostro) + `f7-funnel.css` (NUOVO; le vecchie regole `.fh-*`
  restano, sovrascritte dove serve). Contenuto (legge F6, niente prodotto, numeri solo da FATTI/LISTINO):
  01 · Oggi — **Fai tutto a mano** — 2,5 ore al giorno se ne vanno in lavoro ripetitivo ·
  02 · Chiamata · 30′ — **Vedi il sistema che gira** — gratis, decidi tu ·
  03 · Setup · 7 giorni — **Lo costruiamo su misura** — 50 % alla firma, 50 % al go-live ·
  04 · Da qui in poi — **Gira da solo, ogni giorno** — 0 ore tue, 0 € di canone.
  Forma: numeri di tappa `01-04` in mono arancio-spento davanti all'etichetta; filetto che da grigio diventa **arancio nell'ultimo
  quarto** (gradient) e finisce nel punto pieno; titoli 19 px; riga 14,5 px argento; frecce: **tre archi pieni** (stroke 1,2, niente
  tratteggio, niente ghost), tutte sopra il filetto con la stessa curva, punta 4,5 px. Aura nera dietro (B2). Mobile: colonna come oggi,
  numeri davanti. *Controllo:* nessun «messaggi», «Outreach», «Content», «Brain» nel testo del funnel; SVG con 3 `path` senza
  `stroke-dasharray`; testo ⊂ build (gate). *Ricontrollo:* screenshot 2× guardato accanto all'allegato 02.

### BLOCCO E — TRE SISTEMI
- **E1 · Nota di card 1 fuori a sinistra, come card 3 a destra.** `vsl-v2.tsx`: `VARIANTE_FRECCIA.outreach: "top" → "left"`, variante
  `left` = specchio esatto di `right`: ≥1600 SVG `viewBox 0 0 96 72` con path specchiato (`M92,64 C60,64 40,22 6,8`) che esce **dal bordo
  sinistro a metà altezza** (8 px fuori) e sale verso l'alto-sinistra; nota a sinistra della card, allineata a destra, stessa larghezza
  (max 220 px) e stesso font della nota di destra; <1600 fallback `bottom` identico a card 3. `f6-frecce.css`: regole `.ra-fn--left`
  aggiunte in coda (specchio di `.ra-fn--right`, `right:` ↔ `left:`). *Controllo:* a 1920 la nota sinistra ha `getBoundingClientRect().left ≥ 16`
  e ∩ card = ∅; distanza inizio-freccia dal bordo card 6-10 px; simmetria: |x_nota_sx − (viewport − x_nota_dx_right)| ≤ 12 px.
  *Ricontrollo:* screenshot dei due lati affiancati.

### CHIUSURA (io)
Screenshot 1920/1440/390 guardati (hero, funnel, Tre sistemi); misure dei controlli via Playwright; `npm run build`;
gate `gate_solo_aggiunte.py --parole --consenti "^(65includono|[123]|[cpb])$" --deroga-b "src/app/page\.tsx$"` (stesse deroghe di
XR4F; parte B: toccati solo file nostri post-tag); `npx vercel` (anteprima, mai --prod); CP + STATO + wiki log; commit + push.

## 3. I GIRI — cosa è caduto e perché (§6.20)

**P0 → P1 (attacco: cosa ho dato per fatto senza misurare).**
- P0 diceva «le foto sono scure per il velo». Misurato: il velo NON copre le foto (z 0 vs z 2). La causa è la grana globale NERA di
  `globals.css`: senza toccarla, qualunque `brightness()` sulle foto è una compensazione che scurisce di nuovo le zone chiare della
  grana. → A1 agisce alla radice (grana a luminanza neutra), non sui sintomi.
- P0 diceva «togli una foto» senza dire quale. → INTERPRETO scritto: la 3 (misurata: la più scura, la più piccola, un ritaglio).
- P0 usava «un velo più leggero» per la texture. Un velo unico non può essere «nero pieno dietro le scritte e niente altrove». → B1 lo
  toglie, B2 mette un'aura per blocco di testo.
- P0 teneva «300 messaggi al giorno» nel funnel: viola la legge F6 firmata ieri. → D1 generico.
- «(la mia storia è in fondo)» senza ancora è una frase morta. → ancora aggiunta in `page.tsx` (solo aggiunta).

**P1 → P2 (attacco a P1: costi ombra e casi che lo fanno cadere).**
- Cambiare la grana globale cambia TUTTO il sito, non solo l'hero. Verificato sul piano: il nero resta nero (overlay/hard-light con
  base 0 = 0), le bande scure dietro i testi su foto (legge 11/09, ≥7:1) sono nere → invariate; salgono solo i mezzitoni, ed è
  esattamente ciò che Max chiede. Dichiarato come DEROGA d'aspetto nel CP, con screenshot di una sezione non-hero prima/dopo.
- B2 con `filter: blur(48px)` su un box di 1000×500: paint costoso a ogni scroll con Lenis. → gradiente radiale a 4 fermate, zero filtri.
- A3 a 1280-1599 il gruppo è largo 300 px: la nota da 30 ch (~230 px) ci sta, ma va misurata a 1440, non solo a 1920. → controllo
  a entrambe le larghezze; sotto 1280 nascosta e dichiarato.
- E1 a <1600 la nota sinistra non ha margine: → fallback `bottom` identico a card 3 (simmetria dichiarata, come già in F6 per card 3).
- A1 `.hf-photo::after` a .25 overlay chiaro «schiarisce a macchie»: con la grana globale neutra basta .16 per la firma. → ridotto.

**P2 → P3 (attacco a P2: l'ambizione).**
- Tagliato: rigenerare la tessera della texture con livelli alzati (`texture_hero_tile.py`): un `filter` CSS fa lo stesso senza toccare
  il file di Max né la regola «mai un pixel inventato». Si rigenera solo se il controllo B1 fallisce.
- Tagliato: rifare il funnel come componente nuovo con animazione di riempimento del filetto. Max vuole «migliore», non «animato»
  (le frecce sono FERME per ordine del 13/09). Il filetto che diventa arancio è statico.
- Tagliato: toccare il rail dei fatti in fondo all'hero («300 messaggi al giorno, zero a mano»): non è nell'ordine, e sta sotto la
  sezione dove i prodotti sono ancora anonimi — lo segno in BACKLOG (B-091) come candidato alla legge F6, decide Max.
- Tagliato: `sharpen` via SVG `feConvolveMatrix` sulle foto: inventa pixel; `contrast(1.04)` basta e si misura.
- Confermato tutto il resto: nessun giro a vuoto, nessuna task senza controllo misurabile. Si costruisce.

## 4. Le forze (ADR-015 — dichiarate)
4 scagnozzi (sonnet) in parallelo, aree disgiunte per FILE: α = A1+B1+B2 (`f7-luce.css`, `layout.tsx` +1 riga) · β = A2+A3
(`hero-foto.tsx`, `f7-foto.css`, `page.tsx` +1 riga) · γ = C1+D1 (`hero-titolo.tsx`, `funnel-hero.tsx`, `f7-funnel.css`) ·
δ = E1 (`vsl-v2.tsx`, `f6-frecce.css`). Integrazione, misure, screenshot, gate, deploy: Emperator.
