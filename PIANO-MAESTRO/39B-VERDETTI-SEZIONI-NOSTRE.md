# 39B — VERDETTI SEZIONE PER SEZIONE, SITO AGENCY (anteprima del 13/09/2026)

**Chi**: doom bot, critico senior della Fabbrica Siti · **Su cosa**: 55 screenshot a 1440 px (`scratchpad/nostro/NN-id.png`) + `misure.json` + codice di `agency-empire-landing/src`.
**Ordine di Max**: «è tutto troppo ingrandito; il competitor è centrato e non ingrandito; alcune sezioni sono brutte e vanno rifatte, altre restano; lo schema con le frecce sa di AI».
**Riferimento di scala (competitor: Armageddon, Claude Speedrun, funneloperator.it)**: body 16-17 px · titoli di sezione 33-37 px · h1 50-60 px (Armageddon 59) · colonna 830-1100 px · pochi bottoni · nero/bianco + un accento.
**Legge che vale**: sezioni di giugno (`components/sections/*`) → il testo non si tocca, la forma sì (CSS additivo o componente nuovo con lo stesso testo parola per parola). Aggiunte di oggi (`sezioni-aggiunte/*`) → tutto modificabile. TOGLI è sempre una proposta: decide Max.

---

## §1 · LA SCALA DEL NOSTRO SITO, MISURATA

### 1.1 Distribuzione (da `misure.json`, 55 sezioni)

| Grandezza | n | min | mediana | max | Riferimento competitor | Scarto sulla mediana |
|---|---|---|---|---|---|---|
| Titolo di sezione (≥24 px) | 52 | 24 | **48** | **88** | 33-37 | **+11 ÷ +15 px (+30/45 %)** |
| Paragrafo (≥13 px) | 40 | 14 | **17,5** | 20 | 16-17 | +0,5 ÷ +1,5 (quasi a norma) |
| Contenitore | 54 | 768 | **1088** | **1400** | 830-1100 | al limite alto; 27 sezioni su 54 sono a 1152-1400 |
| Padding verticale | 55 | 0 | **96** | 96 | ~64-80 (stimato dagli screenshot competitor) | +16 ÷ +32 |
| Altezza sezione | 55 | 91 | — (media 915) | **2578** | — | pagina totale ≈ 50.300 px |

Dettaglio titoli: 47 su 52 sono ≥ 46 px (i competitor non superano i 37 per un titolo di sezione); 18 su 52 sono ≥ 52 px; 6 sono ≥ 64 px (`ASCOLTA BENE` 88, `AI Proprietaria` 88, `Ok ma chi siete?` 72, `Noi siamo` 68, `Niente black box` 64, manifesto 64).
Dettaglio paragrafi: 14 sezioni a 18 px, 4 a 19-20 px (hero, ASCOLTA BENE, FinalOffer, ultimo CTA about): il corpo è **quasi a norma**, il problema è la **gerarchia sopra il corpo**: il rapporto titolo/corpo da noi è 48/17,5 = **2,7×**, dal competitor 35/16,5 = **2,1×**.
Dettaglio contenitori: 19 sezioni a 1024 (ok), 10 a 1152, 16 a 1200 (le aggiunte `.vivo`, `--u: 1200px`), 1 a 1400 (FinalOffer).
Hero: h1 in tre righe da **42 / 148 / 88 px** (inline style in `hero.tsx`: `clamp(82px,13.5vw,148px)` per «operatività»). L'h1 di Armageddon è 59 px: la nostra parola-hero è **2,5×** e l'intero blocco h1 è alto ≈ 280 px contro ≈ 130 del competitor.
Padding: 35 sezioni a 96 px (`.section {padding: 6rem 0}` in `globals.css`, usata da 37 componenti) + 10 a 88 px (`.vivo .sv-section`).
Bottoni: in 50 screenshot su 55 compare la CTA fissa `StickyCTA` in basso + il «Prenota» dell'header: ogni schermata ha **almeno 2 bottoni arancioni permanenti** prima ancora della CTA di sezione (in 02, 06, 15, 36, 45, 46 si arriva a 3-5 nella stessa vista).

### 1.2 Ricetta di de-ingrandimento (classe/valore attuale → nuovo)

Regola: titolo di sezione **36-40 px**, mai sopra 44 salvo hero; corpo 16-17; padding 64-72; colonna ≤ 1100.

| Cosa | Attuale | Nuovo | Dove vive |
|---|---|---|---|
| Hero parola («operatività») | 148 px | **96 px** (`clamp(56px, 8vw, 96px)`) | `hero.tsx` inline → serve `!important` |
| Hero riga intro | 42 | **28** | idem |
| Hero riga accento («con AI Workflows.») | 88 | **52** | idem |
| Hero sottotitolo | 20 (`text-xl`) | **17** | classe |
| `text-[88px]` (ListenUp, FinalOffer) | 88 | **52** | 2 occorrenze |
| `text-[72px]` (WhoGuides) | 72 | **44** | 1 |
| `text-[68px]` (About «Noi siamo», FinalOffer prezzo) | 68 | **44** | 2 |
| `text-[64px]` (ToolStack, About «Vuoi entrare») | 64 | **42** | 2 |
| `text-[58px]` (MyPromise, About ×3) | 58 | **40** | 4 |
| `text-[56px]` (About, FinalOffer) | 56 | **40** | 2 |
| `text-[52px]` (Pillars, Bonuses, Competitors, FlowFramework, PowerDeck, PricingROI, MasteryMap…) | 52 | **38** | 9 |
| `text-[48px]` (Results, Clarity, NoFluff, Objections, SystemsShowcase) | 48 | **36** | 5 |
| `md:text-6xl` (FinalCTA) | 60 | **42** | 1 |
| `md:text-5xl` (Problems, Hierarchy, FAQ, Roadmap) | 48 | **36** | 4 |
| `md:text-4xl` / `text-4xl` | 36 | **32** | 2 |
| `text-2xl` / `md:text-2xl` (lead) | 24 | **19** | 9 |
| `text-xl` / `md:text-xl` (lead) | 20 | **17** | 10 |
| `text-lg` (corpo) | 18 | **16,5** | 17 |
| `text-[18px]` / `text-[19px]` / `text-[20px]` (corpo aggiunte/hero) | 18-20 | **16,5 / 17 / 17** | 18 |
| `.section` padding | 96 | **72** | 37 sezioni |
| `md:py-32` / `py-24` | 128 / 96 | **80 / 64** | 2 |
| `.vivo .sv-section` | 88 | **64** | 10 |
| `max-w-6xl` | 1152 | **1080** | 12 |
| `max-w-5xl` | 1024 | **960** | 19 |
| `max-w-[1400px]` (FinalOffer) | 1400 | **1100** | 1 |
| `--u` (vivo) | 1200 | **1100** | 16 sezioni |
| `--fs-h2` | `clamp(28px,3.4vw,46px)` | **`clamp(26px,2.6vw,36px)`** | vivo |
| `--fs-h1` | `clamp(30px,3.6vw,50px)` | **`clamp(28px,3vw,40px)`** | vivo |
| `--fs-manifesto` | `clamp(34px,5vw,64px)` | **`clamp(28px,3.6vw,48px)`** | vivo (31) |
| `--fs-word` | `clamp(54px,6.4vw,100px)` | **`clamp(40px,5vw,72px)`** | vivo |
| `--fs-lead` | `clamp(16px,1.25vw,18px)` | **`clamp(15px,1.1vw,17px)`** | vivo |
| `--fs-stat` | `clamp(30px,3vw,40px)` | **`clamp(26px,2.4vw,34px)`** | vivo |
| `--fs-h3` | `clamp(20px,2.2vw,28px)` | **`clamp(18px,1.8vw,24px)`** | vivo |
| `--fs-riga` (didascalie su foto) | `clamp(15px,1.35vw,18px)` | **`clamp(14px,1.1vw,16px)`** | vivo |

### 1.3 CSS additivo pronto — `src/app/scala.css`

Si importa in `layout.tsx` **dopo** `globals.css`, `vivo.css` e le `aggiunte-*.css`. Non tocca nessun componente. Vale solo da 768 px in su (sotto, le classi mobile restano com'erano). `!important` è necessario perché le utility Tailwind e gli inline style dell'hero hanno pari o maggiore priorità.

```css
/* ============================================================================
   SCALA.CSS — de-ingrandimento del sito agency (ordine di Max, 13/09/2026).
   Solo aggiunte: nessun componente modificato. Obiettivo: titoli 36-40,
   corpo 16-17, padding 64-72, colonna <= 1100 (scala del competitor).
   ============================================================================ */

/* --- 1. Variabili delle sezioni aggiunte (vivo.css) ------------------------ */
:root {
  --u: min(100vw, 1100px);
  --fs-lead:      clamp(15px, 1.1vw, 17px);
  --fs-riga:      clamp(14px, 1.1vw, 16px);
  --fs-h3:        clamp(18px, 1.8vw, 24px);
  --fs-h2:        clamp(26px, 2.6vw, 36px);
  --fs-h1:        clamp(28px, 3vw, 40px);
  --fs-stat:      clamp(26px, 2.4vw, 34px);
  --fs-manifesto: clamp(28px, 3.6vw, 48px);
  --fs-word:      clamp(40px, 5vw, 72px);
}
.vivo .sv-section { padding: 64px 0; }

@media (min-width: 768px) {

  /* --- 2. Padding e contenitori delle sezioni di giugno -------------------- */
  .section { padding-top: 4.5rem; padding-bottom: 4.5rem; }
  [class*="md:py-32"] { padding-top: 5rem !important; padding-bottom: 5rem !important; }
  [class*="py-24"]    { padding-top: 4rem !important; padding-bottom: 4rem !important; }
  [class*="max-w-6xl"]      { max-width: 1080px !important; }
  [class*="max-w-5xl"]      { max-width: 960px !important; }
  [class*="max-w-[1400px]"] { max-width: 1100px !important; }

  /* --- 3. Hero (hero.tsx usa inline style: serve !important) --------------- */
  h1 > span:nth-child(1) { font-size: 28px !important; }
  h1 > span:nth-child(2) { font-size: clamp(56px, 8vw, 96px) !important; line-height: .92 !important; }
  h1 > span:nth-child(3) { font-size: 52px !important; }
  h1 { margin-bottom: 1.75rem !important; }

  /* --- 4. Titoli con px arbitrari (Tailwind: text-[Npx] e md:text-[Npx]) --- */
  [class*="text-[88px]"] { font-size: 52px !important; line-height: 1.02 !important; }
  [class*="text-[72px]"] { font-size: 44px !important; line-height: 1.04 !important; }
  [class*="text-[68px]"] { font-size: 44px !important; line-height: 1.04 !important; }
  [class*="text-[64px]"] { font-size: 42px !important; line-height: 1.05 !important; }
  [class*="text-[58px]"] { font-size: 40px !important; line-height: 1.08 !important; }
  [class*="text-[56px]"] { font-size: 40px !important; line-height: 1.08 !important; }
  [class*="text-[52px]"] { font-size: 38px !important; line-height: 1.08 !important; }
  [class*="text-[48px]"] { font-size: 36px !important; line-height: 1.1  !important; }
  [class*="text-[44px]"] { font-size: 34px !important; }
  [class*="text-[40px]"] { font-size: 34px !important; }

  /* --- 5. Titoli con scala Tailwind ---------------------------------------- */
  [class*="md:text-6xl"] { font-size: 42px !important; line-height: 1.05 !important; }
  [class*="md:text-5xl"] { font-size: 36px !important; line-height: 1.1  !important; }
  [class*="md:text-4xl"], [class*="text-4xl"] { font-size: 32px !important; line-height: 1.15 !important; }
  [class*="text-3xl"] { font-size: 26px !important; }

  /* --- 6. Lead e corpo ----------------------------------------------------- */
  [class*="text-2xl"] { font-size: 19px !important; line-height: 1.5 !important; }
  [class*="text-xl"]  { font-size: 17px !important; line-height: 1.6 !important; }
  [class*="text-lg"]  { font-size: 16.5px !important; line-height: 1.65 !important; }
  [class*="text-[20px]"], [class*="text-[19px]"] { font-size: 17px !important; }
  [class*="text-[18px]"] { font-size: 16.5px !important; }
  [class*="text-[17px]"] { font-size: 16px !important; }

  /* --- 7. Decorazioni che gonfiano senza dire niente ----------------------- */
  [class*="text-[130px]"] { display: none !important; }   /* lettere C/P/B in filigrana, Objections */
}

/* --- 8. Bottoni permanenti: la CTA fissa non compare finché la sezione
         prezzi non è passata (il body riceve .dopo-prezzi da un observer
         di 6 righe; finché non c'è, si può alzare la soglia a 3 viewport
         direttamente in sticky-cta.tsx: innerHeight * 3) ------------------- */
```

Avvertenza sui selettori `[class*=…]`: `text-xl` non intercetta `text-2xl` (sottostringa diversa), `text-[52px]` intercetta anche `md:text-[52px]` (voluto). `text-[36px]` e `text-[32px]` non si toccano perché sono già dentro la scala buona o sono numeri-stat. Se un `text-[48px]` fosse un numero e non un titolo, non è un danno: 36 è comunque la misura giusta per una cifra.

Effetto atteso sulla pagina (stima dal foglio misure, senza rimuovere sezioni): −96×0,25×37 ≈ −900 px di padding, −15/20 % di altezza dei blocchi titolo su 52 sezioni, ≈ −4.000/5.000 px sui 50.300 totali. Il resto dell'altezza si recupera solo con TOGLI e RIFAI di §2-§4.

---

## §2 · VERDETTO SEZIONE PER SEZIONE (ordine di pagina)

Formato: `NN · id/componente · voto · verdetto · motivo (misura o difetto visibile) · cosa fare`. G = giugno (testo intoccabile), A = aggiunta di oggi.

| NN | Sezione | Voto | Verdetto | Motivo (visto/misurato) | Cosa fare |
|---|---|---|---|---|---|
| 00 | Hero (G) + FunnelHero + HeroTexture (A) | 2 | **RITOCCA h1 · RIFAI funnel** | Parola-hero 148 px (2,5× Armageddon); 3 righe di h1 a 42/148/88; 4 pill fluttuanti agli angoli (7 giorni, €0, 300+, codice) che ripetono il rail 01 identico; badge + pre-headline + h1 + lead 20 px + CTA + link + 3 trust = 11 elementi prima del funnel; poi 4 card uguali con 3 frecce bezier tratteggiate animate: è lo schema che Max dice «sa di AI». 1327 px. | h1 a 28/96/52 (scala.css §3); nascondere le 4 pill (`display:none` su `.hero-pill`, sono ridondanti col rail); funnel → §5. |
| 01 | rail-fatti (A) | 4 | **TIENI** | 91 px, 3 numeri + etichetta, un accento, marquee. Fa in una riga quello che 03, 15-stat e 33-stat ripetono in 1.400 px. | Niente. |
| 02 | VSL «Tre sistemi» (G) | 2 | **RIFAI** (stesso testo) | Sfondo `vsl-bg.png` rosa/bianco a grana grossa: la fascia sotto le card («ALL SYSTEMS ONLINE», «Prenota una Chiamata Strategica», «Prenota una Chiamata Gratuita») è **illeggibile**, si vede nello screenshot; 3 card rosso/oro/blu = 3 accenti; titolo 38 su banda arancio piena; 2 CTA + sticky nella stessa vista. 1076 px. | Nuovo componente `vsl-piatta.tsx` con lo stesso testo: sfondo ink, 3 card argento hairline con solo la cifra in accento, una CTA sola. |
| 03 | ScienceStats «AUTOMAZIONE AI PROPRIETARIA =» (G) | 3 | **RITOCCA** (proposta TOGLI) | 3 card a gradiente argento→arancio pieno (vietato dal canone: mai card a gradiente pieno); titolo maiuscolo+corsivo mescolati a 34; le tre cifre (7 gg, 300+, 0€) sono le stesse del rail 01, 1.200 px più su. | Card piatte via CSS (`.card-fill-*{background:#1c1c1c}`); oppure togliere: il rail la copre. |
| 04 | Audience «Ideato su misura» (G) | 4 | **TIENI** (solo scala) | Due colonne chiare, corpo 16; h2 48 → 36; la colonna «non è per te» ha 3 punti contro 5 e lascia ≈ 140 px vuoti in basso a destra. | scala.css; `align-items:start` sulle due card. |
| 05 | Problems «Il problema non è» (G) | 4 | **TIENI** | Confronto grigio/arancio pulito, corpo 15-16, gerarchia netta; solo l'h2 48 a due righe. | scala.css. |
| 06 | specchio (A) | 4 | **TIENI** (1 ritocco) | Foto + testo + DM ricostruito + 4 segnali in 2 colonne: densità giusta. Difetto: 2 bottoni («Sì, mi ritrovo» pieno + «Non mi ritrovo» ghost) + sticky = 3 CTA nella stessa vista. | `--fs-h2` via scala.css; «Non mi ritrovo» → link testuale. |
| 07 | Competitors «Mentre leggi questa pagina» (G) | 2 | **RIFAI** (stesso testo) · proposta TOGLI | «colli di bottiglia» **esce dalla card** (tagliato ai due bordi, visibile); 4 card tutte centrate con 6 livelli tipografici ciascuna; chiusura con card citazione 770 px + altra frase: 1243 px per un concetto che 08 dice meglio subito dopo. | Nuovo componente: lista 2 colonne senza card, citazione in una riga; oppure togliere (08 la sostituisce). |
| 08 | competitor-vivo (A) | 4 | **TIENI** | Banda rossa + foto + slider «Tu sei qui»: leggibile, un accento. Difetto: 45 % di larghezza a destra dello slider vuota; didascalia «E ha i tuoi clienti» spezzata su una parola. | Nota del «punto Tu» spostata sotto lo slider a destra; `text-wrap:balance` sulla didascalia. |
| 09 | ListenUp «ASCOLTA BENE.» (G) | 2 | **RITOCCA** | Titolo 88 px (il più grande dopo l'hero) per una sezione di solo testo; 7 paragrafi a 20 px in colonna 896 = 879 px di lettura continua. | scala.css: 88→52, 20→17; colonna a 680 (`max-w-3xl`→`max-w-[680px]`). |
| 10 | prima-dopo (A) | 2 | **RIFAI** | Timbro «RICORDA / PIANO PRO» sovrapposto e illeggibile; a destra un **preventivo auto** di PreventivoForge (cruise control, cabrio, €20.200) incollato in un confronto su un abbonamento outreach: il nesso non si capisce; 60 % del riquadro è grigio vuoto; titolo 46. | Al posto del PDF una seconda scheda HTML «4.000 € una volta» simmetrica alla prima (canone / rinnovo / proprietà / totale). Il PDF vero resta in 26. Togliere il timbro. |
| 11 | Hierarchy «In quale livello sei» (G) | 4 | **TIENI** | 3 card chiare, numero + eyebrow + corpo 15: buona. h2 48. | scala.css. |
| 12 | Pillars «Perché Digital Empire?» (G) | 3 | **RITOCCA** | 3 card a gradiente lilla→arancio pieno; nota a margine con **freccia rossa disegnata a mano** («Sì, il sistema lavora mentre dormi») fuori griglia a x 1225-1410: decorazione da template. h2 52. | Card piatte via CSS; nascondere freccia+nota (`display:none`); scala.css. |
| 13 | FlowFramework «Framework F.L.O.W.» (G) | 4 | **TIENI** | Lista verticale F/L/O/W in colonna 768, corpo 18: la forma giusta. h2 52. | scala.css (52→38, 18→16,5). |
| 14 | scala (A) | 3 | **RITOCCA** | 7 gradini a scaletta diagonale: il 7° arriva a x 1190 con blocco **verde** (terzo colore); 968 px per 7 righe di 2-6 parole. | 7 righe piatte allineate a sinistra, numero mono a 11, ultima con bordo accento; verde → argento. Altezza attesa ≈ 480. |
| 15 | servizi / SystemsShowcase «Ogni sistema, nel dettaglio» (G) | 2 | **RIFAI** (stesso testo) | 1677 px; 3 colonne rosso/oro/blu con 6 blocchi ciascuna (cifra, come funziona, incluso, stack, risultato, CTA) = **3 «Prenota ora»** + 4 stat card sotto (312+/7/0€/100 %) = quarta ripetizione degli stessi numeri; ripete anche 02 (312/24/1.4k). | Nuovo componente: 3 colonne monocrome con eyebrow in accento, cifra 34 px, liste a 15; una CTA sola; stat finali nascoste (`display:none`). |
| 16 | cartella (A) | 5 | **TIENI** | Cartella con linguette, corpo 16, 4 check, piede mono 11: scala e colonna già giuste. | Niente. |
| 17 | OutreachDeep «Outreach automatico» (G) | 4 | **TIENI** | Testo + pannello workflow, corpo 16,3, eyebrow rosso pieno: ok. Pannello rosso a gradiente. h2 46,4. | scala.css; pannello → ink piatto con bordo hairline (CSS). |
| 18 | OutreachInside «Cosa include la tua piattaforma» (G) | 2 | **RITOCCA** | 3 card **rosso / viola / verde** pieni, testo bianco al 60 % su verde (contrasto basso, visibile); eyebrow «What's inside» in inglese in un sito tutto italiano. | Card argento piatte con icona in accento (CSS additivo sulle 3 classi di sfondo); eyebrow non si tocca (testo di giugno). |
| 19 | guardalo-girare (A) | 3 | **RITOCCA** (o TOGLI finché non c'è il video) | 630 px per una foto + titolo 42 + una riga; metà destra (x > 900) vuota; il numero 300 è già nel rail 01 e in 39. Il video previsto non c'è. | Quando c'è il video: qui. Finché non c'è: fascia da 320 px con foto piccola a sinistra, oppure togliere. |
| 20 | ContentDeep «Fabbrica di Contenuti» (G) | 4 | **TIENI** | Speculare di 17, buona. h2 46,4. | scala.css. |
| 21 | ContentOutput «Cosa produce la tua fabbrica» (G) | 1 | **RIFAI** (stesso testo) | **6 card in 6 colori pieni** (rosso, blu, verde, rosa, ocra, viola): la sezione più lontana dal canone nero/bianco/accento del sito; corpo 14 su colore. 820 px. | Nuovo componente: griglia 3×2 piatta (bordo hairline, sfondo carta), «DELIVERABLE 0N» mono in accento, titolo 18, corpo 15. |
| 22 | due-tipi (A) | 4 | **TIENI** | Card 1./2. con la seconda in bordo accento + «Le domande che non ci fate» in 3 colonne a 15 px: densità da competitor. h2 46. | scala.css. |
| 23 | BrainDeep «Second Brain» (G) | 4 | **TIENI** | Come 17; pannello **blu** (colore fuori palette). | Pannello → ink piatto (CSS); scala.css. |
| 24 | SecondBrainInside «Cosa include il tuo Second Brain» (G) | 3 | **RITOCCA** | 3 card blu / viola / teal (tre colori fuori palette), «What's inside»; h2 46,4. | Card ink piatte, icone e link in accento unico (CSS). |
| 25 | risultati / Results «Fatti, non slogan» (G) | 3 | **RITOCCA** | 6 card ok; sotto, riquadro «16:9 · PLACEHOLDER» con play **visibile in produzione**; «Prenota la demo» coperto dallo sticky; 1211 px. | Nascondere il blocco video finché non c'è il file (CSS su quel wrapper); scala.css. |
| 26 | prove-vere (A) | 4 | **TIENI** | Testo denso e onesto (65 preventivi, 3-13 luglio), PDF vero, nota sulle testimonianze: buona prova. Colonna PDF 400×490 con margine morto sotto. h2 46. | scala.css; PDF `align-self:start`. |
| 27 | rail-sistemi (A) | 2 | **RIFAI** · proposta **TOGLI** | Rail di screenshot **del sito stesso** («Sito agency · HERO» compare 2 volte nel loop, «SPECCHIO», «/prenota/») + i 2 PDF già mostrati in 10 e 26: prova che si guarda allo specchio. 699 px. | Togliere finché non ci sono 5 cose di clienti; se resta: solo i 2 PDF + /prenota/, senza loop. |
| 28 | NoFluff «Non vendiamo abbonamenti» (G) | 4 | **TIENI** | Due colonne ×/✓ chiare, corpo 16, un accento. h2 48. | scala.css. |
| 29 | ToolStack «Niente black box» (G) | 2 | **RIFAI** (stesso testo) | **12 card a gradiente argento→arancio pieno**, 1414 px; 3-4 righe di 15 px su arancio in ogni card; h2 64. | Nuovo componente: lista a 3 colonne senza card, nome bold 17 + una riga 15, separatori hairline; h2 42. Altezza attesa ≈ 700. |
| 30 | PowerDeck «Non solo il sistema» (G) | 4 | **TIENI** | 6 card ink con eyebrow in accento e icona: la griglia più pulita del sito. h2 52. | scala.css. |
| 31 | manifesto (A) | 4 | **TIENI** | Fascia 347 px, una frase; `--fs-manifesto` 64; cerchio-freccia sotto è decorazione. | scala.css (64→48); togliere il cerchio. |
| 32 | WhoGuides «Ok ma chi siete?» (G) | 3 | **RITOCCA** | Titolo 72 px per 3 paragrafi; chip «50+ sistemi» in arancio pieno dentro il paragrafo. Duplica 51 (Tre persone). | scala.css (72→44); chip → `background:none; color:#fb4604` via CSS. |
| 33 | BuilderNotTrainer «Prendo quello che uso io» (G) | 3 | **RITOCCA** | Titolo 51 px in **3 pesi e 3 colori** su 3 righe (bianco / corsivo beige / arancio); a destra 3 stat (7 gg / €0 / 100 %) = quinta ripetizione. | scala.css; stat card → `display:none` (ridondanza col rail 01). |
| 34 | mappa (A) | 2 | **RIFAI** · proposta TOGLI | Organigramma con 3 box e linee tratteggiate; il pill «TU SEI QUI» **copre l'angolo del box Agency ed è illeggibile** (10 px bianco su arancio sopra il bordo); 510 px per dire «siamo l'agency». | Una riga: «Digital Empire → **Agency** · Formazione · SaaS» con Agency in accento, 120 px; oppure togliere. |
| 35 | Bonuses «Non solo il codice» (G) | 3 | **RITOCCA** | h2 52 con 4 parole in corsivo accento su 8; lista 01-03 buona; poi 4 card a gradiente argento→arancio con «VALORE €350/200/500/300». Dice le stesse cose di 30 (dashboard, proxy, CRM, 90 gg). | Card piatte (CSS); scala.css; proposta: togliere 35 o 30. |
| 36 | prenota / PricingROI «Un sistema AI proprietario» (G) | 3 | **RITOCCA** | 2260 px (la più lunga); 3 card rosso/blu/oro + Engine Room + «La matematica» + CTA + trust = **5 CTA**; nella card Engine Room la lista a 2 colonne strette va a capo ogni 2 parole («Tutto di / Outreach / Factory / incluso»). h2 52. | Colori → monocromo con eyebrow accento (CSS); lista Engine Room a una colonna piena (CSS `grid-template-columns:1fr`); scala.css. |
| 37 | tessera (A) | 4 | **TIENI** | Testo + badge appeso: composizione buona; corpo 18; l'URL «agency-empire-landing.vercel.app/pren ota/» va a capo dentro la tessera. | scala.css; `overflow-wrap:anywhere` o togliere l'URL. |
| 38 | Clarity «Cosa succede esattamente» (G) | 4 | **TIENI** | 6 card chiare allineate, eyebrow accento, corpo 15: buona. h2 48. | scala.css. |
| 39 | quanto-costa (A) | 4 | **TIENI** | Due schede + «vs» + una riga di conto: pulita, un accento. Etichetta «OGGI» mono 11 px grigio su scuro quasi invisibile. | Etichette a 12 px e colore `--sv-silver-dim`. |
| 40 | MyPromise «Se il sistema non funziona» (G) | 3 | **RITOCCA** · proposta TOGLI | Titolo 58 in 3 colori/2 stili; 4 blocchi centrati a 18; 815 px. Dice la stessa garanzia di 41 (subito sotto) e della card in 25. | scala.css (58→40, 18→16,5); proposta: togliere 40 e tenere 41. |
| 41 | se-non-funziona (A) | 4 | **TIENI** | SE/ALLORA in due card + foto casco: chiaro, un accento; corpo 16. | Niente (scala via variabile). |
| 42 | Objections «Le 4 obiezioni» (G) | 2 | **RIFAI** (stesso testo) | **2578 px**, la più alta del sito: 4 obiezioni × 3 card (claim/proof/benefit) = 12 card da 220 px di larghezza con corpo 14-15, lettere C/P/B da **130 px** in filigrana dietro. | Nuovo componente: per obiezione una citazione a 24 + 3 paragrafi in colonna 720 con etichetta mono; niente card, niente lettere. Altezza attesa ≈ 1.300. |
| 43 | FAQ «Domande frequenti» (G) | 4 | **TIENI** | Domanda in accento 19 + risposta 16, colonna 768: la sezione più vicina alla scala del competitor. h2 48. | scala.css. |
| 44 | faq-contratto (A) | 4 | **TIENI** | Accordion 2 colonne a 16, primo aperto: buona. Doppia 3 domande di 43 (server, canoni, garanzia/durata). | Vedi §4. |
| 45 | cosa-ottieni (A) | 4 | **TIENI** | Card con bordo accento, 6 check, un bottone; il bottone pieno + lo sticky sono **due bottoni rossi identici** a 150 px di distanza (y 505 e 655). h2 46. | scala.css; sticky nascosto qui (§1.3 punto 8). |
| 46 | FinalCTA «Pronto a far lavorare» (G) | 3 | **RITOCCA** | Due card A/B + titolo 60 in gradiente argento→arancio + CTA ghost + riga trust + sticky: 3 richieste di prenotare nella stessa schermata; 898 px. | scala.css (60→42); ridurre a una CTA (nascondere la riga trust doppia). |
| 47 | FinalOffer «AI Proprietaria» (G) | 1 | **RIFAI** (stesso testo) · proposta **TOGLI** | 1472 px, contenitore **1400** (il più largo); dentro un mock-schermo nero che mostra solo la scritta «AI Proprietaria» a 88 px (uno schermo che non mostra niente), sfondo argento→arancio, prezzo «da €2.500» a 68, checklist, CTA ghost: riassume 36 + 45 + 46. | Togliere. Se resta: componente nuovo senza mock-schermo, 1100 px, prezzo a 44, una CTA. |
| 48 | AboutStory/a «Noi siamo Digital Empire» (G) | 3 | **RITOCCA** | Titolo 68; 4 chip sotto; 557 px per un'apertura di capitolo. | scala.css (68→44). |
| 49 | AboutStory/b «Sei anni fa ero un ragazzo» (G) | 3 | **RITOCCA** | Titolo 56; 5 paragrafi a 17 in colonna 768 + citazione in box: 1293 px di autobiografia in coda alla pagina. | scala.css; colonna a 680; è la sezione dove il testo lungo è accettabile (è la storia). |
| 50 | AboutStory/c «Poi un giorno ho deciso» (G) | 4 | **TIENI** | Testo breve centrato, 680 px: chiude bene. Titolo 58. | scala.css. |
| 51 | AboutStory/d «Tre persone» (G) | 4 | **TIENI** | 3 card team, un accento; mancano le facce (lo ammette 26). Titolo 58. | scala.css; foto quando ci sono. |
| 52 | AboutStory/e «Installiamo sistemi AI» (G) | 2 | proposta **TOGLI** | 3 card Outreach/Content/Second Brain = **quinta descrizione dei 3 sistemi** (02, 15, 17-24, 36) + card «missione: dominare» a gradiente. 979 px. | Togliere; se resta: scala.css + card piatte. |
| 53 | AboutStory/f «Vuoi entrare in Empire?» (G) | 3 | proposta **TOGLI** | **Quarta CTA finale** (45, 46, 47, 53): titolo 64 per una riga + bottone ghost. 581 px. | Togliere; se resta: 64→40. |
| 54 | coda-legale (A) + footer | 3 | **RITOCCA** | Footer a 9-10 px maiuscolo, testo grigio al 10 % su nero: il disclaimer è illeggibile; «Privacy Policy» e «Termini» puntano a `#` mentre `/privacy` e `/cookie` esistono. | 12 px, colore al 40 %, link veri. |

Trasversale (non è una sezione): **StickyCTA** compare in 50 schermate su 55. Con il «Prenota» dell'header sono 2 bottoni arancioni permanenti su ogni vista, prima delle CTA di sezione. Il competitor ha un bottone per schermata. Rimedio in `sticky-cta.tsx` (aggiunta di oggi): soglia da `innerHeight*0.7` a `innerHeight*3`, e `display:none` quando una `.btn-orange` di sezione è nel viewport (IntersectionObserver, 6 righe).

Conteggio: TIENI 27 · RITOCCA 17 · RIFAI 11 (di cui 5 con proposta TOGLI) · TOGLI secco proposto 2 (52, 53). Le screenshot 07, 13, 14, 15, 25, 26, 29, 30, 35, 42, 43, 49 mostrano l'header sticky a metà sezione: è un artefatto della cattura a scorrimento, non un difetto del sito.

---

## §3 · LE 10 PEGGIORI (rimedio preciso) E LE 10 MIGLIORI (non toccare)

### 3.1 Le 10 peggiori

| # | NN | Rimedio | File | Misure |
|---|---|---|---|---|
| 1 | 47 FinalOffer | **Togliere** dal `page.tsx` (una riga commentata, reversibile). Se Max la vuole: `sezioni-aggiunte/offerta-piatta.tsx` con lo stesso testo di `final-offer.tsx`, senza mock-schermo. | `src/app/page.tsx` (riga `<FinalOffer />`) | contenitore 1400→1100; «AI Proprietaria» 88→0 (sparisce il mock); prezzo 68→44; altezza 1472→≈600 |
| 2 | 21 ContentOutput | Nuovo `sezioni-aggiunte/output-piatto.tsx` con i 6 titoli+testi copiati parola per parola da `content-output.tsx`; griglia 3×2 su carta, bordo hairline, eyebrow mono accento. In `page.tsx` si sostituisce l'import. | `content-output.tsx` → nuovo file | card 6 colori→1 sfondo; corpo 14→15; h2 46→36; altezza 820→≈620 |
| 3 | 42 Objections | Nuovo `sezioni-aggiunte/obiezioni-piatte.tsx`: per ognuna delle 4 obiezioni, citazione (24 px serif), risposta in maiuscoletto accento (12 mono), poi 3 paragrafi in colonna 720 con etichetta «Claim / Proof / Benefit» in mono. Testo identico. | `objections.tsx` → nuovo file | 12 card→0; lettere 130 px→0; corpo 14→16; altezza 2578→≈1300 |
| 4 | 15 SystemsShowcase | Nuovo `sezioni-aggiunte/sistemi-piatti.tsx`: 3 colonne ink con bordo hairline, eyebrow in accento, cifra 34, liste a 15; **una** CTA sotto le 3 colonne; le 4 stat finali non si rendono (il rail 01 le copre). | `systems-showcase.tsx` → nuovo file | 3 colori→1; 3 CTA→1; cifra 56→34; altezza 1677→≈1100 |
| 5 | 29 ToolStack | Nuovo `sezioni-aggiunte/stack-piatto.tsx`: 12 voci in 3 colonne senza card, nome 17 bold + una riga 15, separatori hairline; testo identico. | `tool-stack.tsx` → nuovo file | 12 card gradiente→0; h2 64→42; altezza 1414→≈700 |
| 6 | 02 VSL | Nuovo `sezioni-aggiunte/vsl-piatta.tsx`: sfondo ink piatto (niente `vsl-bg.png`), 3 card argento con cifra in accento, una CTA; testo identico. | `vsl.tsx` → nuovo file | banda titolo→nessuna; 3 colori→1; 2 CTA→1; altezza 1076→≈760 |
| 7 | 10 prima-dopo | Modificare `prima-dopo.tsx`: togliere il timbro; colonna destra = scheda HTML «4.000 € una volta · Tuo» con 4 righe (canone 0 / rinnovo — / proprietà del codice tua / totale a 12 mesi 4.000 €), stessa griglia della sinistra. | `sezioni-aggiunte/prima-dopo.tsx` | PDF 400×470→scheda 380×230; altezza 825→≈520 |
| 8 | 07 Competitors | Preferito: togliere (08 dice la stessa cosa). Alternativa: nuovo `competitor-piatto.tsx` con lista a 2 colonne (4 voci) e citazione in una riga; testo identico. | `page.tsx` o nuovo file | «colli di bottiglia» non più tagliato; 4 card→0; altezza 1243→≈520 |
| 9 | 34 mappa | Riscrivere `mappa.tsx`: una riga di testo con i 3 rami e Agency in accento, eyebrow «La mappa»; niente box né linee. | `sezioni-aggiunte/mappa.tsx` | 3 box + pill illeggibile→1 riga; altezza 510→≈140 |
| 10 | 00 funnel dell'hero | Vedi §5: `funnel-hero.tsx` riscritto come linea del tempo tipografica, senza SVG; `aggiunte-hero.css` senza `.fh-fr*`. | `sezioni-aggiunte/funnel-hero.tsx`, `src/app/aggiunte-hero.css` | 4 card + 3 frecce→1 riga + 4 tappe; altezza ≈290→≈130 |

Fuori classifica ma da fare lo stesso: 27 rail-sistemi (togliere), 52 e 53 (togliere), 09 ListenUp (solo scala, ma è la più «gridata»).

### 3.2 Le 10 migliori (da non toccare, salvo la scala di §1)

| # | NN | Perché resta |
|---|---|---|
| 1 | 16 cartella | Corpo 16, 4 check, piede mono, una linguetta attiva: già alla scala del competitor. |
| 2 | 43 FAQ | Colonna 768, domanda 19 in accento + risposta 16: la forma «Armageddon». |
| 3 | 30 PowerDeck | 6 card ink allineate, eyebrow accento, corpo 15: la griglia più pulita. |
| 4 | 05 Problems | Grigio contro arancio, un solo confronto, corpo 15-16. |
| 5 | 39 quanto-costa | Due schede, un «vs», una riga di conto: niente in più. |
| 6 | 22 due-tipi | 1./2. + tre domande a 15 px: densità giusta. |
| 7 | 26 prove-vere | Prova vera, numeri contati, nota onesta sulle testimonianze. |
| 8 | 38 Clarity | 6 tappe con giorno/eyebrow/testo: leggibile in 10 secondi. |
| 9 | 44 faq-contratto | Accordion 2 colonne a 16, primo aperto. |
| 10 | 41 se-non-funziona | SE / ALLORA: la garanzia in due frasi. |

Menzione: 01 rail-fatti (91 px che valgono 3 sezioni), 13 FlowFramework, 06 specchio.

---

## §4 · RIDONDANZE (giugno vs aggiunte di oggi) — proposta, decide Max

| # | Cosa si ripete | Dove | Proposta |
|---|---|---|---|
| R1 | I 4 numeri «7 giorni · 300+ · €0 · codice tuo» | 00 pill hero · **01 rail** · 03 ScienceStats · 15 stat finali · 25 card · 33 stat | Tenere **01**. Nascondere le pill dell'hero, togliere 03, nascondere le stat di 15 e 33 (CSS). |
| R2 | Il competitor che automatizza | 07 Competitors (G) · **08 competitor-vivo** (A) | Tenere **08**, togliere 07. |
| R3 | I 3 sistemi descritti da capo | 02 VSL · 15 SystemsShowcase · 17-24 deep+inside · 36 pricing · 52 About | Togliere **52**; ridurre 02 a 3 card di 3 righe (è l'anteprima) e lasciare il dettaglio a 15 e 17-24. |
| R4 | La garanzia | 25 card «Garanzia 30 giorni» · 40 MyPromise (G) · **41 se-non-funziona** (A) · 44 domanda «Se cambiamo idea» | Tenere **41** (+ la card in 25). Togliere 40. |
| R5 | Il conto SaaS vs una tantum | 10 prima-dopo · 36 «La matematica» · **39 quanto-costa** · 37 tessera · 47 FinalOffer | Tenere **39** e la tessera 37 (prezzi). Togliere 47; 10 solo se rifatta (§3.1 #7) altrimenti togliere. |
| R6 | Le FAQ | 43 FAQ (G): server, garanzia, tempi, un solo sistema · **44 faq-contratto** (A): server, canoni, rate, durata | Tenere entrambe ma spostare in 44 le 3 domande doppie (nascondendo in 43 «server», «garanzia», «in quanto tempo» via CSS `:nth-child`), o unire in 44. |
| R7 | Le CTA finali | **45 cosa-ottieni** · 46 FinalCTA · 47 FinalOffer · 53 «Vuoi entrare in Empire?» | Tenere **45** e 46 ridotta a una CTA. Togliere 47 e 53. |
| R8 | «Cosa è incluso» (dashboard, proxy, CRM, 90 gg) | 18/21/24 inside · 15 «cosa è incluso» · **30 PowerDeck** · 35 Bonuses | Tenere **30**. Togliere 35 (o viceversa: 35 ha i «valore €», 30 è più pulita). |
| R9 | La prova | 25 Results · **26 prove-vere** · 27 rail-sistemi · 19 guardalo-girare | Tenere **26** + le card di 25. Togliere 27; 19 solo col video. |
| R10 | Chi siamo | 32 WhoGuides · 33 BuilderNotTrainer · 48-51 About | Tenere 48-51; 32 duplica 51 (proposta: togliere 32); 33 resta ma senza le 3 stat. |

Stima se Max accetta tutte le proposte TOGLI (03, 07, 27, 40, 47, 52, 53 + eventualmente 32, 35): −9 sezioni, ≈ −8.000 px. Con la scala di §1 e i 6 RIFAI di §3.1: pagina da ≈ 50.300 a ≈ **30.000 px**, che è ancora una pagina lunga ma leggibile.

---

## §5 · IL FUNNEL DELL'HERO (screenshot 00): perché «sa di AI» e come renderlo umano

**Perché sa di AI (quello che si vede):**
1. Quattro card identiche, stessa larghezza (205/1000 del viewBox), stessa altezza, centrate in riga: la «process row» di ogni landing generata.
2. Dentro ogni card la stessa formula: eyebrow mono arancio + titolo 17 + **tre bullet** + piede mono. Nessuna delle quattro ha una forma sua; l'ultima è l'unica «diversa» ed è tutta arancio a gradiente (`.fh-bl-fine`).
3. Tre frecce bezier tratteggiate a puntini **che scorrono** (`fh-scorri` 3,2 s in loop), con marker triangolare, una che «passa sotto» il blocco: è movimento per il movimento, la firma delle demo AI.
4. Le 4 pill fluttuanti agli angoli dell'h1 (7 giorni / €0 / 300+ / codice) messe in posizione simmetrica: decorazione a specchio, non informazione.
5. Tutto centrato: la riga si legge come un diagramma, non come una frase.

**Come renderlo umano (operativo, 10 righe):**
1. Via l'SVG e le classi `.fh-fr`, `.fh-fr-ghost`, `.fh-frecce` da `aggiunte-hero.css`; via l'animazione. Le frecce non si sostituiscono con altre frecce: la sequenza la fa la tipografia.
2. Una **linea del tempo tipografica**: un filetto orizzontale hairline (`rgba(255,255,255,.16)`, 1 px) con 4 tappe; sopra il filetto la tappa in mono 11 («Oggi · Chiamata 30′ · Setup 7 giorni · Da qui in poi»), sotto il titolo a 17 bold, poi **una sola riga** a 14 (non tre bullet): «2,5 ore tue al giorno» / «vedi il sistema che gira, gratis» / «sul tuo server, 50 % alla firma» / «300 messaggi al giorno, 0 ore tue».
3. Solo l'ultima tappa porta l'accento: il punto sul filetto e la cifra «300» in `#fb4604`. Il resto bianco e argento. Niente sfondo, niente bordo, niente card.
4. Allineamento a sinistra dentro una colonna di 830-900 px, non centrato: il lettore lo legge come una riga di testo.
5. Spaziatura: 40 px tra le tappe, 56 px dal blocco CTA sopra; altezza totale ≈ 130 px contro i ≈ 290 attuali.
6. Le 4 pill fluttuanti spariscono: le stesse quattro cifre sono già nel rail 01 subito sotto (si nascondono con una riga CSS, non si toccano i file di giugno).
7. L'h1 scende a 28/96/52 (§1.3): con la parola-hero a 96 la linea del tempo non deve più «reggere» un titolo da 148.
8. Il testo del funnel resta tutto: i numeri continuano a venire da `FATTI` e `LISTINO` (nessuno scritto a mano), cambia solo la forma.
9. Su mobile: le 4 tappe in colonna con il filetto verticale a sinistra (già previsto nel CSS attuale, si conserva).
10. Prova del nove: se coprendo i colori si vede ancora «una riga con quattro momenti» e non «quattro scatole con frecce», è pronto.

---

*Fonti: 55 screenshot in `scratchpad/nostro/`, `misure.json`, `src/app/page.tsx`, `src/app/globals.css` (`.section`), `src/app/vivo.css` (`--fs-*`, `--u`, `.sv-section`), `src/app/aggiunte-hero.css` (`.fh-*`), `src/components/sections/hero.tsx` (h1 inline), censimento classi via grep (`text-[52px]` ×9, `text-[88px]` ×2, `text-lg` ×17, `max-w-6xl` ×12, `max-w-5xl` ×19, `.section` ×37).*
