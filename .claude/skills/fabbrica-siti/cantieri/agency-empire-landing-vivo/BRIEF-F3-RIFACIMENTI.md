# BRIEF F3 — de-ingrandimento, rifacimenti, ritocchi, due sezioni nuove (ordine di Max, 13/09 pomeriggio)

Vale tutto il BRIEF-F2 (stessa cartella): legge §13/§14/§15, canone CSS `.vivo .sv-*`, FATTI/LISTINO, grana su ogni superficie composta, reduced-motion.
In più, i due dossier di oggi: `PIANO-MAESTRO/39A-ATLANTE-TRE-SITI-COMPETITOR.md` (gli elementi belli del competitor, con misure) e
`PIANO-MAESTRO/39B-VERDETTI-SEZIONI-NOSTRE.md` (§1 scala target, §2 verdetto per ogni sezione con il rimedio, §3 peggiori/migliori, §5 funnel).

## LA SCALA (già applicata da `src/app/scala.css`, importato per ultimo)
Titoli di sezione 36-40 px · h3 24 · corpo 16-17 · padding sezione 64-72 · colonna ≤ 1080 (5xl → 960) · un accento (#fb4604) su < 5 % dei nodi ·
bordi 1 px al posto delle ombre · un raggio per famiglia · niente card a gradiente pieno · niente colori fuori palette (rosso/oro/blu/viola/verde/rosa/teal → ink, carta, argento, un accento).
I componenti NUOVI nascono già in scala: usa `var(--fs-h2)` (36 max), `var(--fs-h3)`, `var(--fs-body)`, `var(--fs-lead)`.

## RIFARE UNA SEZIONE DI GIUGNO = stesso testo, parola per parola
Il testo delle sezioni di giugno (`src/components/sections/*.tsx`) è INTOCCABILE: copia ogni stringa esattamente (anche la punteggiatura, anche i `&apos;`),
nello stesso ordine di lettura. Cambia solo la forma. Il gate confronta il testo del live con quello della build: una parola diversa o mancante = FAIL.
I file nuovi vanno in `src/sezioni-rifatte/<nome>.tsx` con export `<Nome>V2`. NON toccare i file di giugno. Emperator fa lo scambio in `page.tsx`.
Niente CTA in più di quelle che il testo di giugno già contiene; se il testo ha 3 «Prenota ora», tienine il testo ma UNA sola come bottone e le altre come link testuali (il testo resta, identico).
Le CTA puntano a `prenotaDa("<id>")` di `@/lib/contatti` (mai a domini esterni del corso).

## FILE CSS: uno per scagnozzo, tutte le regole `.vivo .` + prefisso tuo.
A: `src/app/rifatte-a.css` · B: `src/app/rifatte-b.css` · C: modifica i SUOI `aggiunte-a/b/c.css` + `aggiunte-hero.css` · D: `src/app/ritocchi.css` (solo lui).

## BLOCCO A — RIFAI (giugno)
- 02 VSL → `vsl-v2.tsx` (`VslV2`): sfondo ink, 3 card argento hairline con la sola cifra in accento, una CTA (39B §2 r.02).
- 21 ContentOutput → `content-output-v2.tsx` (`ContentOutputV2`): griglia 3×2 piatta su carta, bordo hairline, eyebrow «DELIVERABLE 0N» mono accento, titolo 18, corpo 15.
- 29 ToolStack → `tool-stack-v2.tsx` (`ToolStackV2`): lista a 3 colonne senza card, nome bold 17 + una riga 15, separatori hairline, h2 ≤ 42, altezza ≈ 700.
Riferimenti nel 39A: E06 griglia 01-04 mono (funneloperator), E14 rail metriche, E42 checklist bordata.

## BLOCCO B — RIFAI (giugno)
- 15 SystemsShowcase → `systems-showcase-v2.tsx` (`SystemsShowcaseV2`): 3 colonne monocrome con eyebrow in accento, cifra 34 px, liste a 15, UNA CTA, le 4 stat finali restano nel testo ma piccole (una riga mono).
- 42 Objections → `objections-v2.tsx` (`ObjectionsV2`): per obiezione una citazione a 24 (virgolette, corsivo serif) + 3 paragrafi in colonna 720 con etichetta mono (claim/proof/benefit → «Dici», «I fatti», «Cosa cambia»), niente card, niente lettere giganti; altezza ≈ 1.300 (39A E33).
- 07 Competitors → `competitors-v2.tsx` (`CompetitorsV2`): lista a 2 colonne senza card, citazione in una riga, ≤ 600 px.
- 47 FinalOffer → `final-offer-v2.tsx` (`FinalOfferV2`): senza mock-schermo, colonna 1100, prezzo a 44, una CTA, ≤ 900 px.

## BLOCCO C — LE NOSTRE (libere) + DUE NUOVE
- Funnel hero (`funnel-hero.tsx` + `aggiunte-hero.css`): Max VUOLE le frecce (lunghe, sottili, punta piccola, una passa sotto) — restano, ma FERME (niente animazione di scorrimento) e più rade; le 4 card diventano 4 TAPPE senza scatola (39B §5): filetto orizzontale hairline con 4 punti, sopra la tappa in mono 11, sotto titolo 17 bold + UNA riga a 14 (non tre bullet); solo l'ultima tappa porta l'accento (punto + cifra); allineato a sinistra in colonna 900; altezza ≈ 150. Le frecce collegano i 4 punti sul filetto (arco sopra per la 1ª e 3ª, la 2ª passa sotto il filetto).
- 10 `prima-dopo.tsx`: togli il timbro; a destra, al posto del PDF, una seconda scheda HTML «4.000 € una volta» simmetrica alla prima (Setup una volta / Canone 0 € / Proprietà del codice: tua / Totale a 12 mesi = eur(LISTINO.outreach)); titolo con `--fs-h2`.
- 34 `mappa.tsx`: una riga sola: «Digital Empire → **Agency** · Formazione · SaaS», Agency con punto accento e «sei qui» mono; ≤ 200 px.
- 14 `scala.tsx`: 7 righe piatte allineate a sinistra (numero mono 11, titolo 17, riga 15), separatori hairline, ultima con bordo accento (via il verde); altezza ≈ 480.
- 19 `guardalo-girare.tsx`: finché VIDEO è null → fascia da ≤ 320 px: foto a 180 px a sinistra + la riga; niente metà vuota.
- 31 `fascia-manifesto.tsx`: via il cerchio-freccia. 37 `tessera.tsx`: via l'URL dentro la tessera. 39 `quanto-costa.tsx`: etichette 12 px `--sv-silver-dim`. 06 `specchio.tsx`: «Non mi ritrovo» da bottone ghost a link testuale. 08 `competitor-vivo.tsx`: nota del «punto Tu» sotto lo slider, didascalia `text-wrap:balance`. 45 `cosa-ottieni.tsx`: checklist bordata E42 (39A) + UN bottone 48 px testo ink su arancio.
- NUOVA `frase-barrata.tsx` (`FraseBarrata`, 39A E21): apertura del problema, subito prima di `<Specchio />`: una frase barrata (line-through accento 3 px, colore dim) e sotto la frase vera in bianco 36-40 px; ink; ≤ 320 px. Copy (voce di casa, senza numeri): barrata «Ti serve un altro tool.» → vera «Ti serve un sistema che gira senza di te.» (sottotitolo 17: «Il tool lo affitti. Il sistema lo possiedi.»).
- NUOVA `griglia-01-04.tsx` (`Griglia0104`, 39A E06): il meccanismo in 4 colonne mono numerate 01-04 con UNA colonna accesa (bordo accento), dopo `<Pillars />`: 01 Chiamata «${FATTI.minutiChiamata} minuti, il sistema in live» · 02 Setup «${FATTI.giorniSetup} giorni sul tuo server» · 03 Go-live «i primi messaggi veri davanti a te» · 04 (accesa) Gira da solo «${FATTI.messaggiGiorno} al giorno, codice tuo»; ≤ 420 px.

## BLOCCO D — RITOCCA (giugno) in SOLO CSS: `src/app/ritocchi.css`
Selettori precisi (leggi ogni componente per trovare classi/testi; puoi usare `:has()` e selettori per attributo sulle classi Tailwind arbitrarie; per i colori fuori palette sovrascrivi background/border con ink/argento/hairline; `!important` dove serve contro le utility):
03 ScienceStats card piatte · 04 Audience `align-items:start` · 09 ListenUp colonna 680 · 12 Pillars card piatte + freccia/nota disegnata `display:none` · 17 OutreachDeep pannello → ink piatto + hairline · 18 OutreachInside 3 card rosso/viola/verde → argento piatte, icone accento · 23 BrainDeep pannello blu → ink · 24 SecondBrainInside card blu/viola/teal → ink piatte · 25 Results: blocco «16:9 · PLACEHOLDER» nascosto · 32 WhoGuides chip «50+» senza sfondo · 33 BuilderNotTrainer stat card `display:none` (ridondanza) · 35 Bonuses card piatte · 36 PricingROI: colori delle 3 card → ink/argento con bordo accento sulla consigliata, lista Engine Room a 1 colonna · 40 MyPromise scala · 46 FinalCTA: riga trust doppia nascosta · 48/49 AboutStory colonna 680 · 54 footer: 12 px, colore al 40 %.
Più `src/sezioni-aggiunte/sticky-guard.tsx` (`StickyGuard`, "use client", 0 dipendenze, rende null): aggiunge `body.dopo-hero` quando `scrollY > innerHeight*3` e `body.cta-in-vista` quando un `[data-cta]`, `#prenota` o `footer` è nel viewport (IntersectionObserver); in `ritocchi.css`: la sticky di giugno (trova la sua classe/struttura in `src/components/sticky-cta.tsx`) è `display:none` finché il body non ha `.dopo-hero`, e `display:none` quando ha `.cta-in-vista`. Emperator la monta in page.tsx.

## CONSEGNA
`cd agency-empire-landing && npx tsc --noEmit -p .` verde. Rapporto in italiano: file, export, dove va montato / quale tag di giugno sostituisce, altezza stimata, da quale file di giugno hai copiato il testo, dubbi (non risolverli inventando).
