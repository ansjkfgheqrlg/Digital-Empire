---
Type: PROJECT
Status: Active
Tags: #agency #landing #restyling #piano #cro #digital-empire
Created: 2026-09-02
Last updated: 2026-09-02
---

# PIANO RESTYLING — agency-empire-landing

**Fonti:** [IDEE-RESTYLING-2026-09-02.md](IDEE-RESTYLING-2026-09-02.md) (48 idee) · [AUDIT-2026-09-02.md](AUDIT-2026-09-02.md) · report competitor 06/08/09 + README dello studio Andrei Pascu.
**Codice:** `agency-empire-landing/` — Next.js 16.2.3 · React 19 · Tailwind 4 · `output: "export"` (statico). Ogni file:riga in questo piano è stato **verificato sul sorgente il 2026-09-02**, non copiato dall'audit.
**Chi esegue:** un altro agente. Ogni riga della tabella si legge da sola.

---

## 1. Verdetto del pianificatore

Questo restyling non è un lifting: trasforma una brochure invisibile (noindex, zero tracciamento, zero prove) in una macchina di acquisizione misurabile. Le tre leve reali sono: **accendere il contatore** (GA4+Clarity+index: oggi non sappiamo letteralmente quanti arrivano), **qualificare prima della chiamata** (oggi ogni curioso brucia 30 minuti di call), **pubblicare l'unica prova che nemmeno apsales.eu ha** (un caso studio misurato). L'unica cosa che, se non fatta, rende inutile il resto: **Fase 1 — tracciamento + uscita dal noindex + destinazione CTA giusta**. Senza dati ogni modifica successiva è un'opinione; ogni giorno di `noindex` è traffico perso per sempre; e ogni click di oggi atterra su una pagina intitolata "Claude Code Mastery" — il prodotto sbagliato nel momento in cui il cliente ha già deciso.

---

## 2. Le fasi

Ordinate per impatto/costo. Regole rispettate: tracciamento+noindex primi; contenuto umano separato dal codice; fusioni strutturali solo dopo che i dati hanno girato.

| Fase | Nome | Costo | Criterio di chiusura verificabile |
|---|---|---|---|
| **F1** | **Contatore e ossigeno** — tracciamento, index, CTA giusta, i 2 fix rotti | ~4 ore codice + 1 decisione Max | GA4 Realtime mostra `page_view` dalla produzione; Clarity ha ≥1 sessione registrata; `curl` dell'HTML di produzione NON contiene `noindex`; screenshot a 390px mostra "operatività" intera; la pagina di prenotazione non contiene più "Claude Code Mastery" nel `<title>`; Lighthouse mobile salvato come baseline |
| **F2** | **Parole che qualificano** — copy solo-codice, zero colli umani | ~1 giornata | Grep sul build `out/index.html`: "12 mesi" assente, "countdown" presente (in negazione), riga di qualificazione presente nell'hero, footer senza testo Facebook e con P.IVA, un solo bottone nel blocco CTA di `vsl.tsx`, le 4 CTA principali hanno 4 etichette diverse |
| **F3** | **Prove e gradini nuovi** — il collo di bottiglia umano, dichiarato | ~1 giornata codice + contenuto Max (parallelo, 2-5 gg) | `caseStudies.length ≥ 1` con dati veri; la stringa "placeholder" non esiste più nel DOM di `results`; 3 `<img>` nella sezione team; tabella comparativa a 4 colonne nel DOM; form del campione consegna il PDF a una mail di test |
| **F4** | **Sistema visivo** — da 77 colori a un sistema | ~1,5 giornate | Ri-esecuzione di `scripts/site_capture.py` sul nostro sito: `design-tokens.json` mostra ≤20 colori di testo (oggi 77), **2 raggi** (oggi 19), sfondi ≤15 (oggi 42); nessun gradiente arancione-rosso sotto testo nero nello stack |
| **F5** | **Taglio guidato dai dati** — fusioni strutturali | ~1,5 giornate, **solo dopo ≥7 giorni di dati F1** | Altezza desktop ≤ ~24.000px (oggi 38.683) e parole ~3.500 (oggi 6.666) senza perdita di informazioni; scroll-depth e heatmap Clarity allegati alla decisione su OGNI sezione fusa; ancore `#servizi` `#risultati` `#prenota` ancora funzionanti; Lighthouse mobile ≥ baseline F1 |

---

## 3. Gli interventi, uno per riga

Costo: **S** <1h · **M** mezza giornata · **L** 1-2 giorni · **XL** >2 giorni. "n/d" dove il numero non esiste nelle fonti.

### FASE 1 — Contatore e ossigeno

| ID | Cosa | File e riga (verificati) | Costo | Dipende da | Verifica |
|---|---|---|---|---|---|
| E4 | Togliere `robots: { index: false, follow: false }` | `src/app/layout.tsx:22` (⚠️ l'audit dice :26 — la riga vera è la **22**) | S | niente | `out/index.html` dopo build non contiene `<meta name="robots" content="noindex`; dopo deploy, `curl -s` della prod idem |
| F2a | `sitemap.xml` + `robots.txt` statici in `public/` (oggi `public/` contiene SOLO `vsl-bg.png`) | `public/` — file nuovi | S | E4 | `curl` di `/robots.txt` e `/sitemap.xml` risponde 200 con contenuto |
| F2b | Open Graph + Twitter card + JSON-LD `Organization` + immagine OG 1200×630 con headline e `#fb4604` (assorbe **D8**) | `src/app/layout.tsx:19-23` (blocco `metadata`) + `public/og.png` nuovo | S | E4 | Lo scraper di anteprima (es. opengraph.xyz) mostra titolo+immagine; `out/index.html` contiene `og:image` |
| E2 | GA4 + Microsoft Clarity via `<Script>` in layout (export statico: niente route server, solo snippet) | `src/app/layout.tsx` (dentro `<body>`) | S | N1 (consenso) | GA4 Realtime mostra `page_view` navigando la prod; il dashboard Clarity registra la sessione |
| N1 🆕 | **Consenso cookie GDPR + Privacy Policy vera.** Oggi i link "Privacy Policy" e "Termini" nel footer sono `href="#"` (morti). E2 in UE senza banner di consenso è un'esposizione legale, non un dettaglio | `src/app/page.tsx:79-97` (footer inline) + componente banner nuovo | M | prima di E2 | I due link del footer rispondono 200 su pagine reali; il banner compare alla prima visita; Clarity/GA4 partono solo dopo consenso |
| E3 | Evento per OGNI CTA con nome sezione (`cta_click` + param `section`) | `src/components/call-cta.tsx` (aggiungere prop `section` + onClick) · `src/components/sticky-cta.tsx` · CTA locali: `hero.tsx:8-23`, `vsl.tsx:337-343` | S | E2 | In GA4 DebugView si vedono `cta_click` con `section` diversi cliccando CTA diverse |
| B1 | Clamp H1 mobile: `clamp(82px, 13.5vw, 148px)` → `clamp(46px, 13.5vw, 148px)`. Stessa verifica sulla riga accento `clamp(44px, 7vw, 88px)` (:110) e sul numero decorativo a 130px | `src/components/sections/hero.tsx:98` (⚠️ l'audit dice :95 — la riga vera è la **98**) · controllo anche `hero.tsx:110` e `objections.tsx:145` | S | niente | Screenshot a 390px: "operatività" e "con AI Workflows." interamente dentro il viewport; nessuna scrollbar orizzontale a 360/390/414px |
| B2+F1 | `vsl-bg.png` (misurato: **3.179.420 byte**) → WebP ~200KB **+** velo scuro `rgba(10,10,10,.72)` sopra l'immagine per rendere leggibili occhiello e barra "ALL SYSTEMS ONLINE" | `public/vsl-bg.png` + `src/components/sections/vsl.tsx:64-73` (`backgroundImage` a :68) | S | niente | Il file servito pesa ≤250KB; screenshot desktop: l'occhiello "COME FUNZIONA IL SISTEMA" leggibile (contrasto ≥4,5:1 al color picker) |
| E1a | **[DECISIONE MAX]** Fermare l'emorragia CTA: o retitle/rebrand della pagina `chiamata-formazione.netlify.app` (oggi `<title>` = "Call Strategica 1:1 \| Claude Code Mastery"), o URL nuovo in `CALL_URL` | `src/components/call-cta.tsx:6` (`CALL_URL`) — la pagina di destinazione è FUORI da questo repo | S | decisione Max | Aprendo la destinazione delle CTA, `<title>` e H1 non contengono "Claude Code Mastery" |
| F1x | Baseline Lighthouse mobile + salvataggio metrica (serve a F5 per confronto) | tutta la pagina | S | niente | Report Lighthouse salvato in `company/01-agency/site-audit/` |

### FASE 2 — Parole che qualificano (solo codice, zero contenuto umano)

| ID | Cosa | File e riga | Costo | Dipende da | Verifica |
|---|---|---|---|---|---|
| A1 | Riga di qualificazione sotto la CTA hero, 15px, opacità 50%: "Lavoriamo con chi fattura già e perde ore in operatività manuale. Se stai ancora validando il prodotto, non siamo noi." | `src/components/sections/hero.tsx:133-146` (tra la CTA a :135 e il link "Vedi prezzi" a :137) | S | niente | La stringa è nel DOM sotto il bottone; a 390px sta su ≤3 righe |
| B9 | Sostituire la scarsità inventata con la posizione opposta: "Nessun countdown, nessuna finta scadenza. Il prezzo è quello." | `src/components/sections/competitors.tsx:158-164` (riga incriminata: **:162**) + ammorbidire la card ":28-29" ("La finestra si sta chiudendo") | S | niente | Grep su `out/`: "12 mesi. Dopo è chiusa" assente; "countdown" presente |
| B10 | **[DECISIONE MAX]** Una sola formulazione vera dei numeri su di noi, ripetuta identica. Oggi convivono: "50+ sistemi" (`who-guides.tsx:52`), "nata a Gennaio 2026" (`about-story.tsx:43`), "su decine di implementazioni non è mai successo" (`my-promise.tsx:72-73`), "decine di automazioni reali" (`flow-framework.tsx:64`) | i 4 file:riga elencati | S | Max dichiara il numero vero | Grep: la stessa formula esatta compare in tutti e 4 i punti; nessuna delle vecchie varianti sopravvive |
| A6 | Micro-sezione "Cosa NON facciamo": niente ads, niente social media management, niente consulenza a ore + una riga di perché | nuova sezione dopo `<NoFluff />` — `src/app/page.tsx:60` | S | niente | Le 3 negazioni sono nel DOM in una sezione dedicata ≤400px di altezza |
| A8 | Blocco "Cosa costa NON farlo" accanto alla matematica dei 20 mesi: ore/anno di outreach a mano, settimane di copy per lancio, valore dell'ora del lettore | `src/components/sections/pricing-roi.tsx:390-420` (la matematica vera è a **:414-416**) | S | niente | Il blocco è nel DOM dentro `#prenota`; nessun numero inventato: le formule lasciano calcolare al lettore |
| A9 | "Ti servono 2 ore in tutto: 30 min di call, 1 ora di brief, 30 min di formazione. Il resto lo facciamo noi." | `src/components/sections/clarity.tsx` (108 righe, sezione `bg-paper`) | S | niente | La stringa è nel DOM nella sezione Clarity |
| B13 | Accorciare "ASCOLTA BENE": da 6 paragrafi `Reveal` a 3 (tenere: "Ti svegli già in ritardo…", "Loro hanno qualcosa che lavora mentre dormono", "Non è fortuna. È un sistema.") | `src/components/sections/listen-up.tsx:24-71` | S | niente | Nel DOM restano esattamente 3 `<p>` nella sezione; le 3 frasi chiave presenti |
| B14 | Riscrivere le card problema come citazioni tra virgolette del cliente ("lo faccio a mano perché nessuno lo fa come voglio io", "ci ho provato con Zapier, si è rotto", "non ho tempo di seguirlo") | `src/components/sections/competitors.tsx:10-31` (array card) + eventuale eco in `problems.tsx` | S | niente | Le tre frasi virgolettate sono nel DOM |
| B6 | Le due CTA gemelle: tenere SOLO `btn-orange`, spostare la rassicurazione ("30 min · gratuita · zero impegno") in una riga sotto | `src/components/sections/vsl.tsx:335-344` (btn-orange a :337-341, `CallCTA` doppione a :343) | S | niente | Nel blocco CTA di `vsl` c'è UN solo `<a>` bottone; la riga di rassicurazione è testo sotto, non dentro |
| B7 | CTA con testo per sezione — `call-cta.tsx` **espone già** `label`/`sublabel` (:10-11), basta passarle: dopo problema → "Voglio smettere di farlo a mano" · prezzi → "Installa il sistema" · team/storia → "Voglio parlare con chi lo costruisce" · finale → "Vediamo se ha senso lavorare insieme" | `hero.tsx:10` · `vsl.tsx:340` · `pricing-roi.tsx` · `final-cta.tsx` · `about-story.tsx` (file che usano CallCTA/CTA) | S | E3 (così ogni label ha già il suo evento) | Le 4 etichette diverse sono nel DOM; nessuna sezione ripete l'etichetta di un'altra tra le 4 principali |
| B12 | **[DECISIONE MAX sulla parola]** Un colore intero MAI usato altrove per una parola sola (proposta: verde su "gratuita" nella sublabel CTA — il pattern misurato sul manuale: `#51b216` compare 1 volta in 11.067px) | `src/components/call-cta.tsx:11` (sublabel) o parola scelta da Max | S | B7 | Il colore scelto compare esattamente 1 volta in tutta la pagina (grep sul CSS/DOM) |
| E6 | **[DECISIONE MAX]** "Da €2.500. Pagamento unico." sotto la CTA hero (i prezzi in pagina sono: 2.500 / 3.500 / 4.000 / 8.000 — `pricing-roi.tsx:54,82,26,339`) | `src/components/sections/hero.tsx:143-145` | S | decisione Max | La stringa prezzo è nel DOM hero (oppure decisione documentata di non metterla) |
| B11 | Footer: via il disclaimer Facebook, dentro P.IVA, sede, email di contatto reale | `src/app/page.tsx:79-97` (footer inline; il testo Facebook è a :90-93) | S | N1 (i link legali veri arrivano lì) | Grep: "Facebook" assente da `out/index.html`; P.IVA presente |
| B8 | Sticky CTA più leggera su mobile: ridurre padding e riportare visibile il link "Prezzi" (oggi `hidden sm:inline-flex`). La decisione "comparire solo dopo i prezzi" va a F5 coi dati Clarity | `src/components/sticky-cta.tsx` (file a riga singola — riformattarlo prima di editarlo) | S | niente | A 390px la barra è ≤56px di altezza; il link Prezzi è visibile e cliccabile |
| N3 🆕 | I 4 silver-chip dell'hero ("7 giorni", "€0 canoni", "300+ email", "Codice tuo per sempre") sono `hidden md:inline-flex`: **su mobile la prova di scala sparisce del tutto**. Renderli visibili su mobile come riga compatta sotto l'H1 (assorbe **A11**: sono già le coppie Loro/Noi) | `src/components/sections/hero.tsx:56-67` | S | B1 (prima l'H1 deve stare nel viewport) | Screenshot 390px: i 4 valori visibili senza overflow orizzontale |
| C2 | Cancellare le 4 sezioni morte — misurate ORA: `mastery-map.tsx` 98 + `power-pillars.tsx` 229 + `roadmap.tsx` 188 + `service-cards.tsx` 298 = **813 righe** (⚠️ l'idea dice 829: il numero vero è 813). Cancellare anche il file orfano `next.config.mjs.tmp` | `src/components/sections/{mastery-map,power-pillars,roadmap,service-cards}.tsx` + `next.config.mjs.tmp` | S | niente | `npm run build` verde; i 5 file non esistono più; zero import rotti (nessuno li importa: verificato, 0 import in `page.tsx`) |

### FASE 3 — Prove e gradini nuovi (il collo umano, dichiarato)

| ID | Cosa | File e riga | Costo | Dipende da | Verifica |
|---|---|---|---|---|---|
| A2 | Tabella comparativa 4 colonne (Digital Empire · SaaS a canone · Freelancer · Assumere in casa), simboli ✓/✕/~, **un punto concesso** a un'alternativa (es. costo iniziale → Freelancer ✓) | nuova sezione dopo `<Competitors />` — `src/app/page.tsx:45` | M | niente | La tabella è nel DOM con 4 colonne e ≥6 righe; almeno un ✓ NON è nella nostra colonna; su mobile scrolla dentro un contenitore, non sfonda il viewport |
| N2 🆕 | **"Cosa succede dopo la chiamata"** — 3 passi: 30 min di call → proposta scritta entro 48h → decidi tu, zero follow-up aggressivi. Oggi la pagina chiede la chiamata 10 volte e non dice MAI cosa succede dopo (apsales promette "risposta entro 24 ore" ed è la sua unica promessa operativa) | micro-blocco dentro `final-cta.tsx` o sopra `#prenota` (`pricing-roi.tsx:110`) | S | tempi confermati da Max | I 3 passi sono nel DOM vicino a una CTA principale |
| A3 | **[CONTENUTO MAX]** UN caso studio, formato fisso: Situazione → Cosa installato → Baseline → Risultato misurato → Tempo. Anche interno (Digital Empire cliente di se stessa), dichiarato come tale. **La singola cosa a più alto impatto della lista: è l'unico buco che ha anche apsales.eu** | `src/components/sections/results.tsx:43-56` (array `caseStudies` vuoto di proposito; il template dei campi è già documentato a :24-38) | L (contenuto, non codice) | dati veri da Max | `caseStudies.length ≥ 1`; ogni campo compilato con numeri misurati; la card appare (il render condizionale esiste già a :315+) |
| A4 | **[CONTENUTO MAX]** Demo registrata 3-5 min (lead entra → qualifica → Slack → carosello → Drive) al posto del placeholder. ⚠️ Correzione all'audit: `results.tsx:265` con `IL_TUO_ID_LOOM` è **dentro un commento JSX** (:259-271), non un embed live — quello che si vede in pagina è il div placeholder :272-307 con l'etichetta "16:9 · placeholder" (:299-306). Fix = sostituire il div con l'iframe reale seguendo le istruzioni già scritte nel commento | `src/components/sections/results.tsx:272-307` | M (5 min di registrazione + montaggio zero) | video registrato da Max | La stringa "placeholder" non esiste nel DOM; l'iframe carica e il video parte |
| A10 | **[CONTENUTO MAX]** Tre ritratti veri, stesso trattamento (b/n o grana coerente), nelle 3 card team già esistenti: Maximilian (:313), Gael (:350), "Team Empire" (:385) | `src/components/sections/about-story.tsx:300-390` | M | foto consegnate | 3 `<img>` con `alt` compilato nella sezione team; stesso aspect ratio |
| A7 | **[DECISIONE MAX sui termini]** "Il rischio, scritto per intero": cosa succede se non regge, chi paga cosa, in quanti giorni, i 2 limiti veri (VPS tuo, accessi). La garanzia 2 gradini esiste già (`my-promise.tsx:67-74`: 30 giorni rimedio → rimborso integrale) ma è raccontata di sfuggita | `src/components/sections/my-promise.tsx:60-80` (espandere, MAI indebolire) | S | termini confermati | Il blocco elenca: giorni, rimedio, condizione di rimborso, i 2 limiti. Nessun termine vago ("presto", "rapidamente") |
| E1b + N4 🆕 | Pagina di prenotazione dedicata all'agenzia (brand giusto, offerta ripetuta, agenda della call) **+ 2-3 domande di qualificazione nel form** (fatturato sì/no, che processo vuoi automatizzare): il filtro di A1 diventa operativo dove si prenota | progetto esterno a questo repo (la destinazione di `CALL_URL`, `call-cta.tsx:6`) | M | E1a; decisione Max sull'hosting | `<title>` coerente con l'agenzia; il form chiede le domande; la conferma dice cosa succede dopo (raccordo con N2) |
| A5 | Campione gratuito "Mappa dei tuoi colli di bottiglia": form a UN campo (email) → PDF 2 pagine coi 3 task più costosi. ⚠️ Correzione tecnica: il sito è `output: "export"` — **niente API route**: il form deve puntare a un webhook esterno (n8n è già nello stack dichiarato, `tool-stack.tsx:11`) | nuova sezione a ~40% pagina (dopo `<SystemsShowcase />`, `page.tsx:52`) + secondo ingresso nel footer | L | n8n webhook + PDF scritto da Max | Invio con mail di test → il PDF arriva; l'evento opt-in compare in GA4 |
| E5 | Terzo gradino: "Mandami la proposta senza call" per chi odia le chiamate (link/mini-form vicino a FAQ e offerta finale) | `src/components/sections/faq.tsx` (41 righe) o `final-offer.tsx` | M | A5 (riusa lo stesso webhook) | Il percorso esiste nel DOM; una richiesta di test arriva a destinazione |

### FASE 4 — Sistema visivo

| ID | Cosa | File e riga | Costo | Dipende da | Verifica |
|---|---|---|---|---|---|
| B4 | Tavolozza: da 77 colori testo / 42 sfondi / 5 famiglie a **arancione `#fb4604` + argento + bianco a opacità**. Un prodotto = UN colore stabile su tutta la pagina (oggi i 3 sistemi in `vsl.tsx:9-60` usano rosso/ambra/blu, i deliverable altri colori ancora) | `src/app/globals.css:32-43` (token) + `vsl.tsx:9-60` + sezioni `*-inside`/`content-output`/`second-brain-inside` | M/L | F1 attivo (per vedere se qualche colore "lavorava") | Ri-cattura con `scripts/site_capture.py`: ≤20 colori di testo, ≤15 sfondi in `design-tokens.json` |
| B5 | Raggi: da 19 a 2 (`12px` card, `9999px` pill). `--radius: 0.75rem` esiste già (`globals.css:64`): normalizzare le utility `rounded-*` sparse (vsl 13 occorrenze, final-offer 13, about-story 10…) | `src/app/globals.css:64` + sweep `rounded-` nei componenti | S | niente | `design-tokens.json` ri-catturato: 2 valori di raggio (il `calc(infinity*1px)` delle pill è accettato come 9999px) |
| B3 | Stack: da 12 card a gradiente arancione-rosso con testo nero (gradiente a `tool-stack.tsx:70`: `linear-gradient(135deg,#e9e3da 0%,#d8cfc2 35%,#fb4604 100%)`) a griglia di etichette monospaziate su fondo neutro, descrizione all'hover/accordion | `src/components/sections/tool-stack.tsx:63-118` (griglia a :63, card style :66-74; i 12 tool sono l'array :5-18) | M | B4 | Nessun testo scuro su gradiente saturo nella sezione; contrasto ≥4,5:1; le 12 descrizioni restano raggiungibili |
| D4 | Etichette monospaziate per OGNI dato (`312 MSG/GIORNO`, `99.8% UPTIME`, `7 GG`, `€0`) — il mono oggi è usato 6 volte in tutta la pagina, apsales 240 | utility nuova in `globals.css` + `vsl.tsx:9-60` (metriche) + `science-stats.tsx:6-10` + chip hero | S | B3 (stesso pattern) | Ogni metrica numerica in pagina è in mono con lo stesso trattamento (controllo visivo su capture) |
| D7 | Grana: alleggerirla dove c'è testo ≤14px. ⚠️ Correzione all'idea: la grana è a **doppio layer** — `::before` opacity 0.55 `overlay` (`globals.css:123-132`) + `::after` opacity 0.28 `hard-light` (:133-142). Intervenire su entrambi (es. 0.55→0.35 e 0.28→0.18 nelle sezioni dense), non su un layer solo | `src/app/globals.css:123-142` | S | niente | Screenshot prima/dopo su una sezione a testo 12px; la grana resta visibile sui fondi vuoti |
| D5 | Inversioni di fondo: oggi **12 file di sezione renderizzati** usano `bg-paper`/`bg-grey` (misurato: about-story, bonuses, clarity, content-output, faq, hierarchy, no-fluff, objections, outreach-inside, pillars, problems, service-deep) contro l'UNICA inversione di apsales. Ridurre a 2-3 eventi | i 12 file + ordine in `page.tsx:40-76` | M | meglio DOPO C1 (le fusioni eliminano già sezioni chiare) | Conteggio nel DOM: ≤3 sezioni a fondo chiaro |
| F3t | Audit contrasto WCAG AA sulle sezioni con testo su gradiente (chiusura formale dopo B3/B4) | sezioni con `text-silver-*` su fondi attivi | M | B3, B4 | Report: zero blocchi di testo normale sotto 4,5:1 |

### FASE 5 — Taglio guidato dai dati (parte solo con ≥7 giorni di GA4+Clarity)

| ID | Cosa | File e riga | Costo | Dipende da | Verifica |
|---|---|---|---|---|---|
| C1 (+C3) | Fondere i 5 racconti dei tre sistemi in 2 livelli: vetrina + approfondimento espandibile. Catena attuale in `page.tsx:52-58`: `SystemsShowcase` (415 righe) → `OutreachDeep/ContentDeep/BrainDeep` (`service-deep.tsx`, 234) → `outreach-inside` (156) + `content-output` (132) + `second-brain-inside` (172). C3 (6.666→~3.500 parole) esce quasi tutto da qui | `src/app/page.tsx:52-58` + i 5 file elencati | L | **scroll-depth e heatmap di F1 letti e allegati**; [DECISIONE MAX] su quali blocchi muoiono | Altezza desktop ≤ ~24.000px; nessuna informazione persa (checklist dei contenuti prima/dopo); ancore `#servizi` (`systems-showcase.tsx:135`) e `#risultati` (`results.tsx:108`) intatte — le usa la nav (`header.tsx:7-11`) |
| B8b | Decidere QUANDO appare la sticky (dopo 0,7 viewport come oggi, o solo dopo `#prenota`) sulla base delle registrazioni Clarity | `src/components/sticky-cta.tsx` | S | dati Clarity | Decisione documentata con il dato che la giustifica; nessun rage-click sulla barra nelle sessioni successive |
| F4L | Lazy-load delle sezioni sotto la piega (`next/dynamic`): oggi ~38.000px di DOM montati insieme. NON toccare il pattern Reveal no-JS (`globals.css:96-118`): il contenuto deve restare visibile senza JS | `src/app/page.tsx:40-76` | M | C1 (prima si taglia, poi si ottimizza ciò che resta) | Lighthouse mobile ≥ baseline F1; la pagina resta completa con JS disattivato |
| F5t | Test mobile reale 360/390/414px su TUTTA la pagina (l'H1 era solo il primo overflow probabile) | tutta la pagina | S | tutte le fasi precedenti | Zero scrollbar orizzontali ai 3 viewport; screenshot archiviati |

---

## 4. Il giudizio del pianificatore sulle 48 idee

### Idee da uccidere (4)

| ID | Perché muore |
|---|---|
| **D1** (diagramma flusso animato, L) | **Esiste già.** `vsl.tsx:9-60` renderizza ORA un flusso INPUT→SISTEMA→OUTPUT con nodi, metriche, barre e animazioni (`flow-dash`, `pulse-dot`). D1 propone di costruire a costo L una cosa che la sezione sopra la vetrina già fa; la ridondanza con le card statiche della vetrina è un problema di C1 (fusione), non un build nuovo. |
| **D2** (mockup dashboard con heatmap, M) | Un mockup "con i lead che entrano" prima di avere A3/A4 significa **mostrare dati finti** su una pagina il cui unico asset di credibilità è lo scaffolding onesto di `results.tsx`. Quando A4 (demo vera) esiste, D2 è ridondante: la demo mostra la dashboard reale. |
| **D3** (card verticali collassate, M) | Import estetico dalla sezione team di apsales. Il problema della NOSTRA sezione team non è la densità: è che mancano le facce (A10). Titoli ruotati a 90° peggiorano la scansione su un mobile già a 64.255px. Decorazione durante una dieta. |
| **D6** (divisori con una riga di testo, S) | Contraddice C3: aggiunge parole a una pagina che deve scendere da 6.666 a ~3.500. I 5 `divider-silver-orange` (`page.tsx:47,51,66,73` + css `globals.css:507-533`) o restano filetti o spariscono con C1. |

### Idee da fondere

- **A11 → N3**: la "barra Loro/Noi" esiste già — sono i 4 silver-chip dell'hero (`hero.tsx:56-67`), che però su mobile sono `hidden`. Renderli visibili È l'A11, a costo zero di contenuto nuovo.
- **C3 ⊂ C1**: il taglio parole è il criterio di accettazione della fusione, non un task separato.
- **D8 ⊂ F2b**: l'immagine OG è un deliverable del blocco metadata.
- **B2 + F1**: stesso file, stesso commit (velo + WebP).
- **E3 ⊂ famiglia E2**: gli eventi si installano nello stesso giro del tracciamento.
- **A5 + E5**: due gradini diversi ma stesso webhook n8n e stessa infrastruttura form.
- **E1a + E1b + N4**: stessa destinazione (`CALL_URL`), due tempi — cerotto in F1, pagina vera in F3.

### Idee mancanti (4 aggiunte)

| ID | Cosa nessuno aveva visto |
|---|---|
| **N1** | **GDPR/consenso.** Le 48 idee chiedono GA4+Clarity (E2) ma nessuna nota che i link Privacy/Termini del footer sono `href="#"` (`page.tsx:86-88`) e che in UE il tracciamento senza banner di consenso è un rischio legale. N1 è prerequisito di E2, non un nice-to-have. |
| **N2** | **Cosa succede dopo la chiamata.** 10 CTA chiedono la call; zero righe dicono cosa succede dopo. È la gestione del "non sono pronto adesso" dal lato processo: chi teme il venditore-che-non-molla non prenota. apsales chiude con "Risposta entro 24 ore" — la sua unica promessa operativa. |
| **N3** | **La prova di scala è invisibile su mobile.** I 4 chip dell'hero sono `hidden md:inline-flex` (`hero.tsx:56-67`): sul dispositivo maggioritario l'hero perde "7 giorni / €0 / 300+ / codice tuo". Con mobile a 64.255px (+66% vs desktop), è il singolo pixel più costoso della pagina. |
| **N4** | **Qualificazione DENTRO il form di prenotazione.** A1 filtra a parole; N4 filtra a domande (fatturato, processo da automatizzare) dove il lead sta già investendo l'intenzione. Le call arrivano preparate, la mezz'ora bruciata sparisce davvero. |

### Correzioni tecniche alle fonti (idee/audit vs codice reale)

1. `noindex` sta a **`layout.tsx:22`**, non :26 (audit P0-1).
2. Il clamp dell'H1 sta a **`hero.tsx:98`**, non :95 (audit P0-2).
3. Le sezioni morte sono **813 righe**, non 829 (C2): 98+229+188+298.
4. `results.tsx:265` (`IL_TUO_ID_LOOM`) è **dentro un commento JSX** (:259-271), non un embed renderizzato: in pagina si vede il div placeholder :272-307. Il fix di A4 è sostituire il div, seguendo le istruzioni già scritte nel commento.
5. La grana (D7) è a **doppio layer**: `::before` 0.55/overlay + `::after` 0.28/hard-light (`globals.css:123-142`) — l'idea li fonde in uno.
6. A5/E5: il sito è **export statico** (`next.config.mjs`: `output: "export"`) — nessun form può usare una API route Next; serve un webhook esterno (n8n).
7. B7 costa davvero S: `call-cta.tsx` espone **già** le prop `label`/`sublabel` (:10-11).
8. Il config è `next.config.mjs` (non `.ts`) e accanto c'è un orfano `next.config.mjs.tmp` da cancellare (fuso in C2).

### Rischi — dove questo piano può rompere ciò che funziona

1. **Indicizzare prima di sistemare la CTA**: se E4 va live senza E1a, Google inizia a mandare gente su un funnel che atterra su "Claude Code Mastery". → E1a ed E4 nello stesso deploy.
2. **Tracciare senza consenso** (E2 senza N1): esposizione GDPR su un sito che vende a P.IVA italiane. → ordine vincolato.
3. **B4 può appiattire l'identità dei 3 sistemi**: i colori di `vsl.tsx:9-60` oggi distinguono Outreach/Content/Brain. La regola è "un prodotto = UN colore stabile", non "tutto arancione". Chi esegue non deve unificare i nodi in un colore solo.
4. **C1 può rompere le ancore**: `#servizi` vive su `systems-showcase.tsx:135`, `#risultati` su `results.tsx:108`, `#prenota` su `pricing-roi.tsx:110` — le usano header (`header.tsx:7-11`), sticky e hero. Checklist ancore dopo ogni fusione.
5. **F4L (lazy-load) può rompere la salvezza no-JS**: il pattern Reveal è costruito perché la pagina resti leggibile senza JS (`globals.css:87-118`). `next/dynamic` con placeholder vuoti la ucciderebbe. → test con JS disattivato nel criterio di chiusura.
6. **La riformattazione di `sticky-cta.tsx`** (file a riga singola) può introdurre regressioni invisibili al diff: farla in un commit isolato senza cambi di logica.
7. **WebP della grana rossa** (B2): il fondo `vsl-bg` è rumore ad alta frequenza — a compressione spinta banda. Verificare a occhio a qualità 80-85.
8. **Due sistemi di scarsità**: B9 toglie la riga a `competitors.tsx:162` ma anche `:28-29` parla di "finestra che si chiude". Toglierne una sola lascerebbe la contraddizione a metà.

---

## 5. Sequenza operativa per chi esegue

Ordine esatto. ⏸ = serve Max, non una scelta tecnica.

1. ⏸ **[MAX, 10 min]** Decisione E1a: retitle di `chiamata-formazione.netlify.app` o URL nuovo? (Basta cambiare titolo+H1 di quella pagina per oggi.)
2. N1 — banner consenso + 2 pagine legali vere + link footer (`page.tsx:86-88`).
3. E2 + E3 — GA4 + Clarity in `layout.tsx`, eventi `cta_click` con `section` su `call-cta.tsx`, `sticky-cta.tsx`, CTA di `hero.tsx` e `vsl.tsx`.
4. E4 — via il `noindex` (`layout.tsx:22`) + F2a (`robots.txt`, `sitemap.xml`) + F2b (OG/Twitter/JSON-LD + `og.png`). **Stesso deploy del punto 1.**
5. B1 — clamp `hero.tsx:98` → `46px` min; controllo `hero.tsx:110` e `objections.tsx:145`; screenshot 360/390/414.
6. B2+F1 — WebP + velo scuro su `vsl.tsx:64-73`.
7. F1x — Lighthouse mobile baseline, salvato. **→ chiusura F1: verificare i criteri della tabella fasi.**
8. A1 (hero) · B9 (`competitors.tsx:162` E :28-29) · B13 (`listen-up.tsx:24-71`) · B14 (`competitors.tsx:10-31`).
9. B6 (`vsl.tsx:335-344`) poi B7 (label per sezione) poi B12 (la parola colorata).
10. ⏸ **[MAX, 15 min]** B10: qual è la formulazione vera dei numeri? · E6: prezzo nell'hero sì/no?
11. A6 (nuova sezione dopo `page.tsx:60`) · A8 (`pricing-roi.tsx:390-420`) · A9 (`clarity.tsx`) · B11 (footer) · B8 (sticky) · N3 (chip mobile) · C2 (813 righe + `.tmp`). **→ chiusura F2.**
12. ⏸ **[MAX, in parallelo da subito — è il collo di bottiglia]** Consegna contenuti F3: dati del caso studio (A3), registrazione demo 5 min (A4), 3 foto (A10), termini garanzia (A7), PDF del campione (A5), tempi post-call (N2).
13. A2 — tabella comparativa (dopo `page.tsx:45`). Non dipende da Max: si fa mentre si aspetta il punto 12.
14. N2 · A7 · A4 (`results.tsx:272-307`) · A3 (`results.tsx:43-56`) · A10 — man mano che i contenuti arrivano.
15. E1b+N4 — pagina di prenotazione dedicata con domande di qualificazione. A5 + E5 — webhook n8n + form. **→ chiusura F3.**
16. B4 → B5 → B3 → D4 → D7 → F3t. D5 solo se C1 non è imminente. **→ chiusura F4 con ri-cattura `site_capture.py`.**
17. ⏸ **[MAX + dati]** Dopo ≥7 giorni di GA4/Clarity: lettura scroll-depth e heatmap, decisione su quali dei 5 racconti dei sistemi muoiono (C1).
18. C1+C3 — fusione; checklist ancore; conteggio parole. B8b con i dati Clarity. F4L lazy-load (test no-JS). F5t test mobile finale. **→ chiusura F5.**

---

## 6. Cosa NON tocchiamo

Protetto perché funziona (fonte: audit §4 "Quello che funziona" + verifiche sul codice):

1. **L'hero come struttura** — marquee metallico, occhiello, H1 gigante col gradiente argento→arancione, CTA arancione piena (`hero.tsx:27-151`). Si tocca SOLO il minimo del clamp (:98) e si AGGIUNGE la riga A1: nessun redesign.
2. **L'alternanza dei fondi come meccanismo** (nero ↔ argento) — D5 ne riduce la frequenza, non la elimina.
3. **Instrument Serif corsivo arancione** sulle parole chiave dei titoli — è la firma riconoscibile della pagina.
4. **La grana** (`grain-fine`, `globals.css:123-142`) — D7 la alleggerisce dove il testo è piccolo; non si rimuove: nessun competitor italiano ce l'ha.
5. **La nota manoscritta** "Sì, il sistema lavora mentre dormi. Per davvero." (`pillars.tsx:90-92`) — unico momento di voce umana, resta com'è.
6. **La garanzia a due gradini** (`my-promise.tsx:67-74`) — più forte di quella di apsales (2 gradini vs 1). A7 la espande, MAI la indebolisce.
7. **Lo scaffolding onesto di `results.tsx`** (array vuoti :43-56, render condizionale) — si riempie con dati veri, non si sostituisce con dati finti. Il commento-guida :24-38 resta per i prossimi case study.
8. **Le due colonne 1:1 "fuori/dentro"** (`no-fluff.tsx:6-20`, 5 voci vs 5 voci) — eseguite meglio di apsales, dice l'audit.
9. **Le 4 obiezioni CLAIM/PROOF/BENEFIT** (`objections.tsx`) — sono le quattro vere.
10. **La matematica dei 20 mesi contro il SaaS** (`pricing-roi.tsx:414-416`) — l'argomento economico più solido della pagina; A8 la affianca, non la riscrive.
11. **La tabella prezzi con Engine Room "MIGLIOR VALORE"** (`pricing-roi.tsx`) — prezzi trasparenti in pagina: è un vantaggio competitivo misurato contro apsales, che non li pubblica.
12. **Il pattern Reveal no-JS-safe e `prefers-reduced-motion`** (`globals.css:87-118`) — qualsiasi lazy-load o animazione nuova deve preservarlo: la pagina resta leggibile senza JavaScript.

---

## 7. AGGIUNTA DI MAX — le sezioni da `claude-speedrun.com` (report 07)

Decisione presa il 2026-09-02 su richiesta di Max. Lo studio 07 era stato letto come minaccia
competitiva per Claude Code Mastery; Max ha chiesto di estrarne anche **sezioni per il sito agenzia**.
Filtro applicato: sopravvive solo cio' che regge il cambio di pubblico (marketer -> titolare B2B)
e di ticket (249 EUR -> 2.500-8.000 EUR).

### Prese — 5 mosse

| ID | Mossa | Fonte | Dove va | Fase | Costo |
|---|---|---|---|---|---|
| **S1** | Urgenza competitiva senza scadenza + spiegazione consolatoria (*"sta usando strumenti che tu non usi"*) | 07 §5.7 | `competitors.tsx` — rimpiazza la scarsita' finta di B9 | F2 | S ✅ **fatto** |
| **S2** | Formula per una parola inflazionata: `produttivita' = robe utili / tempo` + grafico a 2 barre col delta calcolato | 07 §5.10 | vicino a `pricing-roi.tsx:414` (la matematica dei 20 mesi, oggi solo testo) | F2 | M |
| **S3** | Micro-sondaggio "Dimmi se ti ritrovi" a 2 bottoni | 07 §5.4 | dopo `problems.tsx` | F2 | M |
| **S4** | "Cosa facciamo OGGI" con delta temporale misurato (*"10 minuti invece di 2 giorni"*) sulla nostra operativita' reale | 07 §5.8 | `results.tsx`, accanto ad A3 | F3 | M |
| **S5** | Disclaimer GDPR + responsabilita' sui dati dei clienti | 07 §5.15 | footer, con N1 | F1 | S |

**Perche' S1 e S3 valgono doppio:** S1 non e' un'aggiunta, e' la **sostituzione** che mancava a B9
(togliere un countdown falso lascia un buco: qui il buco si riempie con un'urgenza che non scade e
non si puo' smentire). S3 fa tre lavori in uno: auto-diagnosi del problema, qualificazione A1 resa
interattiva, ed **evento GA4** — misura quanti si riconoscono nel problema, dato che oggi non abbiamo.

**Perche' S4 e' la piu' importante:** aggira il collo di bottiglia dei case study. Non richiede che
un cliente ci dia i suoi numeri — richiede la nostra operativita', che e' gia' documentata
(Empire Studio, i sistemi di outreach, questo stesso studio competitor). Il report 07 lo scrive in
chiusura: *"Digital Empire ha la stessa materia prima e non la sta usando come prodotto."*

### Respinte — 4, con motivo

1. **Il tono shitposting** (*"lo stupido sei tu LOL"*, *"A FUCKING WEAPON fr"*) — il report 07 lo
   elenca come difetto n.1: *"taglia fuori il pubblico B2B e over-35"*. Su un ticket da 8.000 EUR
   non segnala autenticita', segnala non-assumibilita'.
2. **Prezzo-come-assurdita' e CTA in prima persona** (*"ti do i miei dannati 249 EUR"*) — a 8.000 EUR
   chi clicca non e' impulsivo: sta costruendo un business case per se' o per un socio.
3. **Rilascio giornaliero con date + card `???`** — meccaniche di ritenzione da corso. Un servizio
   non ha lezioni che escono domani.
4. **Autorita' presa in prestito dagli investitori (110 miliardi)** — convince chi dubita che l'AI
   funzioni. Il nostro compratore quel dubbio non ce l'ha piu': il suo e' *"funziona DA ME?"*,
   a cui risponde S4.

**Nota di destinazione:** il grosso di Speedrun e' ottimizzato per vendere un corso a marketer. Il
posto naturale di quelle meccaniche non e' il sito agenzia ma **la landing di Claude Code Mastery**,
dove Speedrun e' il concorrente diretto e usa il nostro identico `#fb4604` + Onest. Le respinte
restano in magazzino per CCM, non vanno buttate.
