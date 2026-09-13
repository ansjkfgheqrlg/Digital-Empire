---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #site-study #sales-page #funnel-operator #struttura #strategia #confronto-digital-empire
Created: 2026-09-13
Last updated: 2026-09-13
---

# 66 — funneloperator.it — STRUTTURA E STRATEGIA della sales page

**URL:** `https://www.funneloperator.it/`
**Catturata:** 2026-09-13 · 37 schermate desktop (1440×900) · 44 mobile · 30 schermate per sezione in `sezioni/`
**Cartella cattura:** `competitor/Andrei Pascu/site-study/capture/66-funneloperator-it/`
**Rapporto gemello:** nessuno ancora (questo è il primo report sul dominio funneloperator.it; il prodotto Funnel Operator era già stato studiato sulla vecchia pagina in `reports/02-funnel-operator.md`).

> Questo è il sito che Max indica come il più nuovo e il migliore di Andrei Pascu. Il rapporto risponde a una domanda sola: **come è costruita la pagina e con quale strategia vende**, sezione per sezione, con numeri presi dai file di cattura e mai stimati. Ogni affermazione porta il file da cui viene.

---

## 0. Le cinque cose da sapere prima di leggere tutto

1. **La pagina non chiede di comprare per 21.000 px.** Il primo bottone di acquisto nel flusso («Iscriviti adesso») sta a y=20.998 su 32.807 px, cioè al 64% della pagina (`scheda.json` → `cta[]`). Sopra ci sono 18 sezioni di hook, problema, storia, prova e meccanismo. La copertura è data da un bottone flottante «Ottieni accesso» (`href="#prezzo"`) fisso in basso a destra, che compare già dalla seconda schermata (`desktop-03.png`, `desktop-30.png`) e resta per tutta la pagina.
2. **L'urgenza è vera e leggibile nel codice.** In `src/29-index-CLKYm5hM.js` c'è la costante `Ip={ATTUALE:434,VALUTA:"EUR",PROSSIMO:{importo:560,dal:"2026-10-12"}}`: il countdown («Il prezzo sale tra 28 giorni 13 ore…») è calcolato dalla data, uguale per tutti i visitatori, non da un cookie per-utente. Il rincaro 434 → 560 € è uno scaglione dichiarato, non uno sconto barrato.
3. **La «garanzia» non è un rimborso: è una consulenza condizionata.** «E se non trovi clienti dopo aver finito il Funnel Operator e aver contattato 50 persone… puoi fissare una consulenza con Andrei Pascu a €0» (`copy-integrale.md`, y=2532-2871). Ripresa nella tessera dell'offerta (sez. 19, alt della `tessera.webp`) e nella sez. 21 («5 ore a disposizione… forever»). La FAQ «È garantito che avrò risultati?» risponde «No.» (`src/29-index-CLKYm5hM.js`, array `Hp`).
4. **Zero testimonianze di studenti, ma il volto di Andrei compare in almeno 17 immagini** su 68 file media (`media-inventario.md`). La prova è tutta in prima persona: numeri (4.8/5 Trustpilot linkato, 4000+ ordini, 1500+ studenti, 13k leads, 28 test), due VSL, screenshot di call pixelate, template, portfolio di 3 landing dell'agenzia.
5. **La pagina è un'applicazione, non una landing.** Stack TanStack Start + React + Vite, Tailwind v4 (oklch), Radix (accordion, dialog, dropdown), Lucide, Supabase Auth con secondo fattore, rotte `/auth`, `/_authenticated`, `/assistenza`, `post-checkout`, area admin nascosta con `noindex` (`src/29-index-CLKYm5hM.js`, `src/05-buy-button-DX_4IxaR.js`, `src/_INDICE.json`). Il bottone di acquisto chiama una server function che restituisce l'URL di pagamento (`buy-button`: `let{url:e}=await r();window.location.href=e`). La FAQ è anche iniettata come JSON-LD `FAQPage` con tutte le 18 domande (`Xp()` nel bundle).

---

## 1. Carta d'identità

| Campo | Valore | Fonte |
|---|---|---|
| URL | `https://www.funneloperator.it/` | `scheda.json` → `url` |
| Titolo pagina | «Funnel Operator — Impara a fare landing pages per le aziende» | `scheda.json` → `titolo` |
| Meta description | «Impara a fare landing pages per le aziende e a trovare i clienti che te le pagano. Accesso a vita, pagamento unico.» | `scheda.json` → `meta.description` |
| Costruzione | React (TanStack Start/Router, Vite, Tailwind v4 oklch, Radix, Lucide, Supabase) | `scheda.json` → `costruzione`; `src/29-index-CLKYm5hM.js`; `src/38-styles-Cm6i-gBj.css` |
| Altezza desktop | **32.807 px** a 1440 px di larghezza | `scheda.json` → `altezza`, `larghezza` |
| Altezza mobile | **36.630 px** | `scheda.json` → `altezza_mobile` |
| Sezioni | **30** (26 firme distinte) + header fisso | `scheda.json` → `sezioni_totali`, `sezioni_distinte` |
| Blocchi di testo | 386 | `scheda.json` → `blocchi_testo` |
| Parole nel copy (blocchi dedup) | **2.376** | conteggio Python su `dom-blocks.json` |
| Headings | 56 (1 h1, 22 h2, 33 h3) | `scheda.json` → `headings` |
| Elementi in `cta[]` | 26 = 4 CTA di vendita + 4 tab programma + 18 trigger accordion | `scheda.json` → `cta[]` |
| CTA di vendita vere | **4**: «Iscriviti adesso» (y=20.998), «Cosa contiene il corso?» (→`#programma`, y=20.998), «Sono pronto» (y=30.648), «Ottieni accesso» flottante (→`#prezzo`) | `scheda.json` → `cta[]`; `desktop-30.png` |
| Media nel DOM | 122 riferimenti `img`/`picture` (con duplicati dei rail) → **68 file unici, 2.511 KB** | `scheda.json` → `media`; `media-inventario.md` |
| Fotografie di persone | almeno 17 immagini con il volto di Andrei; 0 volti di clienti/studenti non pixelati | `media-inventario.md` (alt), `sezioni/13-*.png`, `sezioni/26-*.png` |
| Video | 2 VSL con poster (`vsl-principale.webp` 830×466 in sez. 9; `vsl-consulenza.webp` 582×327 in sez. 21) | `media-inventario.md`; `sezioni/09-*.png`, `sezioni/21-*.png` |
| Prezzo | **434 €** pagamento unico, accesso a vita; **560 €** dal 12 ottobre 2026; fino a 3 rate Klarna/PayPal | `copy-integrale.md` y=20.732-20.855; `src/29-index-CLKYm5hM.js` (`Ip`, `Up()`) |
| Prodotto | Corso video «Funnel Operator»: 4 sezioni (01 Intro, 02 Landing pages, 03 Trovare clienti, 04 Domande comuni), «8:30 ore di corso» prima di iniziare a cercare clienti, template landing/sezioni/script chiamate/script messaggi, community Telegram, registrazioni di call reali, consulenza 5 ore condizionata | `copy-integrale.md` sez. 19-26; alt `tessera.webp` |
| A chi si rivolge | «Copywriter e website creator che non riescono a trovare clienti», «Giovani tra i 18 e i 28 anni», «Chiunque sia stanco di sperimentare con 50 business diversi», chi ha «le basi ovvie (Canva)» | `copy-integrale.md` y=12.058-12.401 |
| Promessa | «Diventa funnel operator oggi» · «1° landing page online entro 24h da inizio corso» · «Metodo chiaro e testato per trovare clienti» · «Carriera avviata» · «cambiare vita» | `copy-integrale.md` y=1.499, 2.162-2.201, 7.685, 30.195 |
| Titolare legale | Andrei Pascu Sales · P.IVA 02001850474 · Viale Giacomo Matteotti 15, 50121 Firenze | footer, `copy-integrale.md` y=32.640; JSON-LD in `scheda.json` → `meta.jsonld` |
| Lingua / tono | Italiano, seconda persona singolare, registro colloquiale-aggressivo («Ma chi cazzo pensi di essere?», «Perché mi paghi, lol», «Meno teoria huh») | `copy-integrale.md` |
| Sfondi | 2 soli: scuro `oklch(0.178 0 89.9)` (16.795 px, 51,2%) e chiaro `oklch(0.946 0 89.9)` (15.674 px, 47,8%); accento blu `oklch(0.656 0.134 235.9)`; verde `oklch(0.598 0.199 143.2)` solo per «Carriera avviata» e «Fare landing pages»; rosso `#bd0000` solo per «morirai» e il barrato «L'AI ti ruba il lavoro» | `scheda.json` → `palette_sfondi`, `palette_testo`; `estratto-css.md` |
| Caratteri | Inter Tight (172 usi), Plus Jakarta Sans (102), DM Mono (10, numeri del countdown e numerazione 01-04), Curseyt blackletter (3, solo l'h1 «Un giorno morirai.») | `scheda.json` → `caratteri` |
| Gradienti | nessuna famiglia di gradiente di sfondo: superfici piatte; l'unico colore pieno è il blu della colonna «01» in sez. 18 | `scheda.json` → `palette_sfondi`; `sezioni/18-*.png` |
| Animazioni | 13 keyframes: `fo-rail` (nastri scorrevoli 45s/70s), `fo-comparsa`, `fo-momento`, `fo-foglio-su`, `fo-luccichio`, `fo-gira`, `fo-dissolvenza`, accordion Radix | `scheda.json` → `keyframes`, `effetti.animazioni`; `estratto-css.md` |

### 1.1 Cosa vende, in una riga
Un corso una-tantum da 434 € che promette una **carriera** (non un tool, non una skill isolata): fare landing page per aziende con l'AI e trovare i clienti che le pagano, con un metodo «testato da AP Sales su 13k+ leads da agosto 2025 a giugno 2026» (`copy-integrale.md` y=19.562).

### 1.2 Cosa NON c'è (e pesa quanto ciò che c'è)
- Nessun bottone di acquisto nell'header: solo loghi Funnel Operator | APsales e «Accedi →» (`desktop-01.png`; `copy-integrale.md` y=22).
- Nessuna CTA nella hero (sez. 1, cta=0) né nella promessa (sez. 2, cta=0) (`scheda.json` → `sezioni[0..1].cta`).
- Nessuna testimonianza testuale, nessuna stellina con nome, nessun logo cliente (`copy-integrale.md`: la parola «testimonian» non compare).
- Nessun prezzo barrato, nessun «valore reale 1.997 €», nessun bonus con prezzo a fianco (`copy-integrale.md` sez. 19, 22).
- Nessun rimborso «soddisfatti o rimborsati» (FAQ `Hp` e disclaimer y=32.336).
- Nessun gradiente, nessuna ombra portata (`scheda.json` → `ombre`: una sola voce, trasparente).

---

## 2. Macrostruttura: le 30 sezioni in ordine

Classificazione fatta **guardando** ogni file in `sezioni/` (30 schermate viste una per una) e rileggendo il copy della sezione in `copy-integrale.md`. Altezze, media, CTA e sfondo da `scheda.json` → `sezioni[]`. «Prima frase» = primo blocco di testo della sezione nel copy.

| # | Titolo (file `sezioni/` / copy) | y | h px | % pag. | Ruolo nel funnel | Media | CTA | Sfondo | Prima frase |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Un giorno morirai. | 65 | 1.243 | 3,8 | **Hook** (pattern interrupt, memento mori) | 1 | 0 | Scuro | «Un giorno morirai.» |
| 2 | Diventa funnel operator oggi | 1.308 | 1.068 | 3,3 | **Promessa** (3 carte-beneficio) | 4 | 0 | Scuro + texture | «Diventa funnel operator oggi» |
| 3 | (senza titolo) — garanzia consulenza | 2.377 | 780 | 2,4 | **Garanzia** (condizionata, con volto) | 2 | 0 | Chiaro | «E se non trovi clienti dopo aver finito il Funnel Operator e aver contattato 50 persone…» |
| 4 | (senza titolo) — barra numeri | 3.156 | 273 | 0,8 | **Prova** (rail numerico) | 8 | 0 | Chiaro | «4000+ ordini nel mio store» |
| 5 | (senza titolo) — le aziende le vogliono | 3.429 | 910 | 2,8 | **Problema di mercato** (domanda insoddisfatta) | 1 | 0 | Scuro | «Le aziende le vogliono.» |
| 6 | La realtà dei fatti? | 4.340 | 1.848 | 5,6 | **Agitazione + educazione** (anti get-rich-quick, storia del mestiere) | 5 | 0 | Scuro | «Non diventerai ricco con un software, copiando «trade» di altri…» |
| 7 | Come funziona | 6.188 | 1.692 | 5,2 | **Meccanismo** (percorso 7 step → «Carriera avviata») | 8 | 0 | Chiaro | «Step 1 — Studia Funnel Operator.» |
| 8 | Fare siti / Fare landing pages. | 7.880 | 969 | 3,0 | **Posizionamento** (prima/dopo visivo) | 2 | 0 | Scuro | «Nel 2026 tutti fanno siti.» |
| 9 | Perché fare landing pages è il servizio che ho scelto | 8.849 | 902 | 2,7 | **Autorità** (VSL 1) | 1 | 1 (play) | Chiaro | «(spoiler: mi piacciono i soldi)» |
| 10 | Titolare AP Sales | 9.751 | 1.076 | 3,3 | **Autorità** (agenzia reale, albero «tu sei qui») | 2 | 0 | Chiaro | «Recentemente ho cambiato la mia impresa. Adesso facciamo solo landing pages.» |
| 11 | Esempi di pagine fatte da APsales | 10.827 | 934 | 2,8 | **Prova** (portfolio a nastro) | 37 (3 file ripetuti) | 0 | Scuro | «Esempi di pagine fatte da» |
| 12 | Per chi ho creato Funnel Operator: | 11.761 | 780 | 2,4 | **Qualificazione** (5 profili) | 1 | 0 | Scuro | «Copywriter e website creator che non riescono a trovare clienti» |
| 13 | «Ma chi cazzo pensi di essere?» | 12.541 | 1.924 | 5,9 | **Storia personale / autorità** (7 foto) | 7 | 0 | Chiaro | «Andre :)» |
| 14 | LA CRISI DEL 2025 | 14.465 | 603 | 1,8 | **Storia / agitazione** (l'agenzia che non cresce) | 0 | 0 | Chiaro | «Inizio 2025: non riuscivamo più a crescere.» |
| 15 | Ho fatto 28 test di 28 servizi diversi. È sopravvissuto solo uno. | 15.068 | 1.044 | 3,2 | **Storia → meccanismo** (reason-why del servizio) | 3 | 0 | Scuro | «Dal 2024 mi sono fatto una domanda sola: qual è il servizio giusto da vendere a un'azienda?» |
| 16 | Schiavizzerai l'AI. | 16.112 | 928 | 2,8 | **Meccanismo** (AI senza slop) | 3 | 0 | Chiaro + illustrazione piena | «Imparerai a usare l'AI per fare landing pages. Senza fare AI SLOP.» |
| 17 | L'AI ti ruba il lavoro. / Ruberai il lavoro a chi non sa usare l'AI. | 17.040 | 1.254 | 3,8 | **Obiezione** (AI) + polarizzazione «2 tipi» | 14 (loghi) | 0 | Chiaro | «Una domanda che molte persone mi fanno è: «Ma Andrei, come farai ora che l'AI fa i siti da sola?»» |
| 18 | «Non è un business sexy… Ma funziona» | 18.294 | 1.600 | 4,9 | **Meccanismo in 4 mosse** (carte, «carta leggendaria») | 1 | 0 | Scuro | «Vuoi fare cose divertenti o vuoi fare soldi?» |
| 19 | FUNNEL OPERATOR (`#offerta`) | 19.894 | 1.246 | 3,8 | **Offerta + prezzo + urgenza** | 1 | 2 | Scuro + texture | «Avvia una carriera come FUNNEL OPERATOR» |
| 20 | (senza titolo) — raccoglitore (`#programma`) | 21.140 | 846 | 2,6 | **Contenuto** (4 tab del programma) | 1 | 4 | Chiaro | «01 Intro» |
| 21 | Il corso copre quasi ogni possibilità. | 21.986 | 1.423 | 4,3 | **Garanzia** (consulenza 5 ore) + VSL 2 + mini-FAQ | 15 | 5 | Scuro | «Ma se fai 50 contatti, finisci il corso e non hai alcun tipo di riscontro… Puoi parlare con me.» |
| 22 | Asset pronti per te | 23.409 | 1.236 | 3,8 | **Stack / bonus** (4 asset) | 4 | 0 | Scuro | «Ho già preparato tutto ciò che ti serve.» |
| 23 | Prima pagina online entro 24h | 24.645 | 795 | 2,4 | **Promessa di velocità** | 1 | 0 | Chiaro | «Se entri in Funnel Operator oggi e inizi subito le lezioni… La tua prima landing page sarà online domani.» |
| 24 | Community su Telegram | 25.440 | 885 | 2,7 | **Bonus / appartenenza** | 4 | 0 | Chiaro | «Ho creato un gruppo su Telegram per confronti e consigli.» |
| 25 | Troverai veramente clienti? | 26.325 | 2.301 | 7,0 | **Obiezione n.1 + prova del metodo** (stack DM→Loom→Call→Chiusura) | 6 | 0 | Chiaro | «Se sei titubante, lo capisco. È pieno di… Promesse… Sui social…» |
| 26 | Registrazioni chiamate di vendita di AP Sales | 28.626 | 698 | 2,1 | **Prova** (call reali pixelate) | 2 | 0 | Chiaro | «Abbiamo registrato alcune delle nostre call di vendita…» |
| 27 | «Se questo metodo funziona così bene, perché lo insegni?» | 29.324 | 775 | 2,4 | **Obiezioni «cattive»** (3 domande) | 0 | 0 | Scuro | «Perché mi paghi, lol.» |
| 28 | Questo percorso lo descrivo con una sola frase: cambiare vita. | 30.099 | 717 | 2,2 | **Chiusura + ancoraggio prezzo** | 3 | 1 | Chiaro | «Se potessi trovare la direzione nella tua vita e ottenere molteplici stipendi al mese… quanto pagheresti?» |
| 29 | FAQ | 30.816 | 1.719 | 5,2 | **FAQ** (14 domande in 2 gruppi) + disclaimer | 28 (icone) | 14 | Scuro | «Sono disponibili tutte le lezioni da subito?» |
| 30 | Footer | 32.535 | 272 | 0,8 | **Legale** | 1 | 1 | Trasparente | «Agenzia · Corsi» |

Fonti della tabella: `scheda.json` → `sezioni[]` (y, h, media, cta, bg), `copy-integrale.md` (prime frasi), `sezioni/01..30-*.png` (classificazione visiva).

### 2.1 Note di lettura visiva, sezione per sezione (cosa la scheda non dice)

- **Sez. 1** (`sezioni/01-un-giorno-morirai.png`): h1 in blackletter Curseyt a 220 px, «morirai» in rosso `#bd0000` a 290 px; sotto, illustrazione in bianco e nero di un cavaliere inginocchiato trafitto da frecce, aureola e topi (`soldato-caduto.webp`, 1664×1236 resa 832×618). Sottotitolo a 49 px: «Tanto vale provare a fare soldi nel frattempo.» Nessun bottone. L'header sopra ha solo i due loghi e «Accedi →» (`desktop-01.png`).
- **Sez. 2** (`02-diventa-funnel-operator-oggi.png`): logomark a gradiente, h2 63 px con «funnel operator» in blu, tre carte inclinate in stile «carta collezionabile» con illustrazioni b/n (terminale «0 to landing page», mappa topografica, cronometro 24) e spunta blu. Sfondo con texture (`bg_img: true`). È l'unica sezione con `bg_img` oltre alla 19.
- **Sez. 3** (`03-section.png`): due blocchi incrociati testo/foto. Foto 1: portatile con «ZERO CLIENTI?» sullo schermo. Foto 2: **Andrei alla scrivania con microfono — è il primo volto della pagina, y=2.793** (`scheda.json` → `media`, `andrei-scrivania.webp`). Testo a 37 px con grassetti «finito il Funnel Operator», «50 persone», «consulenza», «Andrei Pascu».
- **Sez. 4** (`04-section.png`): nastro orizzontale animato (`fo-rail 70s`) con 4 numeri e icone: 4.8/5 Trustpilot (link a `it.trustpilot.com/review/andrei-copy.com`), 4000+ ordini, 1500+ studenti, 2020 apertura store. Alta solo 273 px: una riga di prova, non una sezione.
- **Sez. 5** (`05-section.png`): tre frasi centrate a 36 px («Le aziende le vogliono. / Non le trovano. / E son disposte a pagare tanto per averle.»), poi un'insegna b/n con «LANDING PAGES.» in trasparenza e il micro-CTA testuale «Ti spiego tutto ↓».
- **Sez. 6** (`06-la-realt-dei-fatti.png`): la sezione più verbosa (332 parole, densità 18). Contiene la card dell'avviso SEC (immagine con citazione tradotta, link a sec.gov), tre screenshot di Apple/Amazon/Notion come «i 3 siti che hai visitato oggi», e la chiusura sull'AI: «L'AI ti tira su la pagina in 10 minuti, ma non sa cosa scriverci dentro, e non sa trovarti il cliente che te la paga.»
- **Sez. 7** (`07-come-funziona.png`): 7 card a zig-zag collegate da linee tratteggiate, icone b/n (logo FO, checklist, carta, globo, persone, grafico, PayPal), arrivo in verde «Carriera avviata ✓» e la riga «E tutto ciò è insegnato nel corso al 100%».
- **Sez. 8** (`08-fare-siti-fare-landing-pages.png`): prima/dopo con due foto di profilo dello stesso ragazzo: «Fare siti» barrato + foto b/n con taglio sbagliato, «Fare landing pages.» in verde + foto a colori con taglio curato e bordo verde. Sotto: «Nel 2026 tutti fanno siti. E servono a poco. Sito = vetrina.»
- **Sez. 9** (`09-perch-fare-landing-pages-il-serviz.png`): VSL 1, poster di Andrei alla scrivania con libreria retroilluminata blu, bottone play; sottotitolo ironico «(spoiler: mi piacciono i soldi)».
- **Sez. 10** (`10-titolare-ap-sales.png`): foto di Andrei in giacca e cravatta al telefono con skyline notturno; testo su AP Sales; poi diagramma «albero»: AP Sales → Formazione / Agenzia con puntatore blu «Tu sei qui» sul ramo Formazione (`albero-apsales.webp`).
- **Sez. 11** (`11-esempi-di-pagine-fatte-da.png`): due nastri orizzontali contrapposti (`fo-rail`) con 3 landing dell'agenzia ripetute (monouso certificato, massaggi, «Chi siamo» AP Sales) — 37 riferimenti `img` per 3 file da 209×293. È «portfolio» ma con solo 3 pezzi.
- **Sez. 12** (`12-per-chi-ho-creato-funnel-operator.png`): foto di Andrei in felpa che indica il portatile con il logo FO, elenco di 5 profili target.
- **Sez. 13** (`13-ma-chi-cazzo-pensi-di-essere.png`): la sezione biografica. Avatar tondo + «Andre :)», sottotitolo «Dalla scrivania nella casa di un paesino a un ufficio e un'azienda in centro a Firenze», poi 3 coppie di foto (ufficio/cucina; monitor di notte/tavolo anni prima; palestra/riunione con team dai volti sfocati). Numeri: «Ho solo 24 anni… +270K follower, clienti da 8 paesi… più di 1500 ragazzi e ragazze».
- **Sez. 14** (`14-la-crisi-del-2025.png`): solo testo, h2 in maiuscolo a 63 px. Racconto della crisi dell'agenzia e del ribaltamento «dal nulla, sono entrati troppi clienti insieme… Ti auguro lo stesso problema».
- **Sez. 15** (`15-ho-fatto-28-test-di-28-servizi-div.png`): h2 con «28 test» e «28 servizi» in blu, «uno» in grassetto; tre righe con icone gotiche (teschio, spade incrociate, lapide) per i tre motivi di fallimento; chiusura «A settembre 2025 ho provato a vendere solo landing pages».
- **Sez. 16** (`16-schiavizzerai-l-ai.png`): illustrazione a tutta larghezza di due serpenti b/n a fauci aperte (`carta-serpenti.webp` 1440×928 + `serpente-testa.webp` ×2) con una fascia chiara al centro che porta titolo e due paragrafi. È l'unica sezione «poster».
- **Sez. 17** (`17-l-ai-ti-ruba-il-lavoro-ruberai-il.png`): titolo barrato in rosso «L'AI ti ruba il lavoro.» e titolo vero sotto; nastro di loghi (ChatGPT, GitHub, Lovable, Krea, Claude, Gemini, Vercel); due card «1.» / «2.» con numeri a 81 px, la seconda con bordo blu; chiusura «L'azienda non ti paga per generare la pagina. Ti paga perché sai quale pagina generare.»
- **Sez. 18** (`18-non-un-business-sexy-ma-funziona.png`): quattro carte da gioco illustrate (K, Q, J, A con seme «$»), frase «Tu adesso puoi accedere a una carta leggendaria», poi griglia 4 colonne 01-04 con la prima colonna a fondo blu pieno (unico blocco di colore saturo della pagina).
- **Sez. 19** (`19-funnel-operator.png`): «Avvia una carriera come FUNNEL OPERATOR», tessera blu con laccio e moschettone (badge da evento) che elenca 4 punti tra cui «Garanzia consulenza con Andrei» e un QR; prezzo 434 € a 60 px; riga «Pagamento unico, accesso a vita. Dal 12 ottobre 2026: 560 €.»; countdown a 4 cifre in DM Mono; due bottoni: blu «Iscriviti adesso» e grigio «Cosa contiene il corso?».
- **Sez. 20** (`20-section.png`): un raccoglitore a cartelle con 4 linguette nere («01 Intro», «02 Landing pages», «03 Trovare clienti», «04 Domande comuni») e il logo Funnel Operator sulla cartella frontale. Le linguette sono `button` (4 elementi in `cta[]`): il programma si apre a richiesta, non è elencato in pagina.
- **Sez. 21** (`21-il-corso-copre-quasi-ogni-possibil.png`): nastro di 3 screenshot di consulenze in videochiamata, paragrafo sulla consulenza «5 ore… forever», VSL 2 (poster con sottotitolo «centinaia di consulenze.»), poi 4 accordion chiusi sulla consulenza.
- **Sez. 22** (`22-asset-pronti-per-te.png`): 4 righe alternate testo/screenshot (Template landing, Template sezioni, Script chiamate, Script messaggi) separate da linee sottili; gli screenshot sono 2 file riusati (`template-fasi.webp`, `template-messaggi.webp`).
- **Sez. 23** (`23-prima-pagina-online-entro-24h.png`): titolo, due righe, screenshot del sito Notion (stesso file di sez. 6) usato come esempio di pagina, riga «Tutorial chiarissimi.»
- **Sez. 24** (`24-community-su-telegram.png`): icona Telegram, titolo con «Telegram» in blu, due righe, mockup iPhone del gruppo con membri sfocati, aeroplanini di carta sfumati ai lati.
- **Sez. 25** (`25-troverai-veramente-clienti.png`): la sezione più alta (2.301 px). Titolo-domanda, ammissione «La verità: dipende… non è facile. Ma con Funnel Operator… È più facile.», h3 «Per 10 mesi abbiamo testato…», diagramma a zig-zag DM su Instagram → Loom → Call → Chiusura progetto (stesso schema grafico di sez. 7), riga «13k leads», h3 «Ti diamo materiale di vendita» con 5 spunte.
- **Sez. 26** (`26-registrazioni-chiamate-di-vendita.png`): due screenshot sovrapposti di call reali con volti pixelati e una lavagna con schema di lead magnet.
- **Sez. 27** (`27-se-questo-metodo-funziona-cos-ben.png`): tre domande «cattive» in h3 37 px con risposte brutali; nessuna immagine. Contiene la matematica «4 milioni di partite IVA / 1500 studenti = 3333 aziende per studente».
- **Sez. 28** (`28-questo-percorso-lo-descrivo-con-un.png`): foto di un ragazzo con cuffie sul davanzale, testo con ancoraggio «Una singola landing page venduta a un'azienda vale tra i €300 e i €600. Il corso si ripaga con il primo cliente.», bottone blu «Sono pronto ↗».
- **Sez. 29** (`29-faq.png`): 14 accordion chiusi in due gruppi etichettati in DM Mono blu («FUNNEL OPERATOR» 9 domande, «PAGAMENTO» 5 domande), disclaimer a 12 px in fondo.
- **Sez. 30** (`30-footer.png`): logo, link «Agenzia» (apsales.eu) e «Corsi» (bsns.it), ragione sociale, P.IVA, indirizzo, link legali, «Preferenze cookie», «Assistenza».

### 2.2 Distribuzione dei ruoli (px e %)

| Ruolo | Sezioni | px totali | % pagina |
|---|---|---|---|
| Hook + promessa | 1, 2 | 2.311 | 7,0 |
| Problema / agitazione | 5, 6, 14 | 3.361 | 10,2 |
| Meccanismo / posizionamento | 7, 8, 15, 16, 18 | 6.233 | 19,0 |
| Autorità / storia | 9, 10, 13 | 3.902 | 11,9 |
| Prova | 4, 11, 25 (parte), 26 | 4.206 | 12,8 |
| Qualificazione | 12 | 780 | 2,4 |
| Obiezioni | 17, 27 | 2.029 | 6,2 |
| Garanzia | 3, 21 | 2.203 | 6,7 |
| Offerta / prezzo / contenuto / bonus | 19, 20, 22, 23, 24 | 5.008 | 15,3 |
| Chiusura | 28 | 717 | 2,2 |
| FAQ + legale | 29, 30 | 1.991 | 6,1 |

(Somma altezze da `scheda.json` → `sezioni[].h`; la sez. 25 è contata per intero in «Prova» perché il suo peso è il diagramma del metodo e i 13k leads.)

Lettura: **il 51% della pagina (hook, problema, meccanismo, autorità, prova, qualificazione) viene prima della prima CTA**; offerta e bonus insieme sono il 15%. È una pagina «lunga davanti e corta dietro»: convince a lungo, vende in fretta.

---

## 3. Ritmo

### 3.1 Dove stanno le CTA (y in px, da `scheda.json` → `cta[]`)

| CTA | Testo | y | x | Tipo | Colore | Distanza dalla precedente |
|---|---|---|---|---|---|---|
| flottante | «Ottieni accesso» → `#prezzo` | fisso, basso-destra, compare da ~1.800 px in giù | 1.265 | ancora al prezzo | blu | — |
| 1 | «Iscriviti adesso» | 20.998 | 536 | acquisto (server fn → URL pagamento) | blu | 20.998 dall'inizio |
| 2 | «Cosa contiene il corso?» → `#programma` | 20.998 | 702 | ancora al programma | grigio `oklch(0.22)` | 0 (stessa riga) |
| 3 | «Sono pronto» | 30.648 | 650 | acquisto | blu, testo bianco | 9.650 |
| — | fine pagina | 32.807 | | | | 2.159 dopo l'ultima |

Fonti: `scheda.json` → `cta[]`; il bottone flottante è visibile in `desktop-03.png` (y≈1.800-2.700) e `desktop-30.png` (y≈26.100-27.000), assente in `desktop-01.png`.

- **Una CTA di acquisto ogni 16.400 px** nel flusso (2 bottoni su 32.807 px). Senza il flottante, un lettore che scorre a 900 px per schermata vede il primo bottone alla **schermata 24 su 37**.
- **Con il flottante**, una CTA è sempre a schermo dalla seconda schermata in giù: la pagina è «a zero CTA nel testo, una CTA nell'angolo». È una scelta, non una svista: nelle sez. 3-18 ci sono 3 micro-CTA testuali con freccia («Ti spiego tutto ↓» y=4.213, «Quello che le aziende vogliono? Landing pages ↓» y=8.719, «Ecco cos'era cambiato ↓» y=14.952) che spingono a scorrere, non a comprare.
- I 18 trigger accordion (4 in sez. 21 + 14 in sez. 29) e i 4 tab (sez. 20) sono interattivi ma non vendono: aprono contenuto.

### 3.2 Alternanza chiaro / scuro

Sequenza (S = scuro `oklch(0.178)`, C = chiaro `oklch(0.946)`, T = footer trasparente), da `scheda.json` → `sezioni[].bg`:

```
S S C C S S C S C C S S C C S C C S S C S S C C C C S C S T
1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
```

- 17 cambi di sfondo su 29 giunzioni: mediamente **un cambio ogni 1,7 sezioni** (ogni ~1.900 px).
- Corsa più lunga: 4 sezioni chiare consecutive (23-26: 24h, Telegram, Troverai clienti, Registrazioni) = 4.679 px di chiaro nella zona «prove e bonus».
- Scuro 51,2% / chiaro 47,8% (`scheda.json` → somma `h` per `bg`): equilibrio quasi perfetto. Apre scuro (hook), chiude scuro (FAQ, footer); l'offerta (19) è scura con texture; la chiusura emotiva (28) è chiara.
- Il **blu d'azione compare solo 6 volte come sfondo** (`palette_sfondi` → `oklch(0.656 0.134 235.9)`: 6): i 3 bottoni blu, il flottante, la colonna «01» della griglia in sez. 18, la tessera. Tutto il resto è grigio-nero e grigio-chiaro.

### 3.3 Alternanza testo / immagine

- 28 sezioni su 30 hanno almeno un media; le sole «tutto testo» sono la 14 (LA CRISI DEL 2025) e la 27 (le 3 domande cattive) (`scheda.json` → `sezioni[].media`).
- Sezioni con più parole: 6 (332), 17 (194), 13 (192), 27 (165), 22 (154), 29 (152), 15 (139). Sezioni con meno: 11 (5), 20 (11), 1 (11), 9 (15), 5 (19).
- Schema ricorrente: **una sezione densa di testo è sempre seguita da una sezione «visiva» a poche parole** — 6 (332 parole) → 7 (diagramma, 65); 13 (192) → 14 (testo breve, 92) → 15 (139) → 16 (poster serpenti, 29); 17 (194) → 18 (carte, 120); 22 (154) → 23 (screenshot, 26).
- Impaginazione a due colonne testo/foto (3, 10, 12, 16, 22, 28) alternata a colonna singola centrata (1, 2, 5, 7, 9, 18, 19, 20).

### 3.4 Prezzo, garanzia, primo volto

| Elemento | Dove | y | Occorrenze nel copy | Fonte |
|---|---|---|---|---|
| Prezzo 434 € | sez. 19 | 20.732 | 1 volta nel body; ripreso dinamicamente nella FAQ «Quanto costa Funnel Operator?» (chiusa) | `copy-integrale.md`; `src/29-index-CLKYm5hM.js` → `Up()` |
| Prezzo futuro 560 € | sez. 19 | 20.804 | 1 volta + FAQ | idem |
| Ancoraggio (300-600 € a landing) | sez. 28 | 30.499 | 1 volta | `copy-integrale.md` |
| «Pagamento unico» / «UNICO pagamento» | sez. 19, 28; meta description | 20.804, 30.588 | 2 + meta | `copy-integrale.md`, `scheda.json` → `meta` |
| Garanzia-consulenza | sez. 3 (testo), sez. 19 (tessera), sez. 21 (testo + 4 FAQ) | 2.532, 20.131, 22.442 | 3 esposizioni; la parola «garan-» compare 2 volte nel testo visibile (tessera alt e FAQ) | `copy-integrale.md`; `media-inventario.md` (alt `tessera.webp`) |
| «50 contatti / 50 persone» | sez. 3, 21 (x2) | 2.638, 22.442, 23.211 | 4 | `copy-integrale.md` |
| Primo volto (Andrei alla scrivania) | sez. 3 | **2.793** (8,5% della pagina) | — | `scheda.json` → `media` (`andrei-scrivania.webp`) |
| Primo video (VSL 1) | sez. 9 | 9.188 (28%) | — | `scheda.json` → `media` (`vsl-principale.webp`) |
| Primo numero di prova | sez. 4 | 3.257 (9,9%) | — | `copy-integrale.md` |
| Prima menzione «AP Sales» | sez. 10 (h2) | 9.847 | 7 volte in totale | conteggio Python su `dom-blocks.json` |
| Prima menzione «Andrei Pascu» | sez. 3 | 2.903 | «Andrei» 4 volte | idem |

### 3.5 Mobile
- 36.630 px di altezza contro 32.807 desktop (+11,7%) (`scheda.json` → `altezza_mobile`): la pagina cresce poco in verticale perché le sezioni sono già a colonna singola stretta (`--colonna: 832px` in `estratto-css.md`).
- In `mobile-01.png` la hero tiene h1, illustrazione e sottotitolo nella prima schermata (390×844): il pattern interrupt regge anche da telefono.

---

## 4. Strategia di persuasione

### 4.1 Come apre (hook)
Tre battute in 2.300 px, nessuna delle quali parla del prodotto:
1. **Memento mori** — «Un giorno morirai.» in blackletter con «morirai» rosso su cavaliere trafitto (`sezioni/01`). Serve a fermare lo scroll e a dichiarare il tono: la pagina non sarà gentile.
2. **Ribaltamento** — «Tanto vale provare a fare soldi nel frattempo.» (y=1.094, 49 px): sposta dalla morte al denaro in una riga.
3. **Promessa in 3 carte** — «Diventa funnel operator oggi» + Metodo chiaro / Lezioni complete / 1° landing page in 24h (`sezioni/02`).
Poi, prima ancora di spiegare cosa sia un funnel operator, mette la **garanzia** (sez. 3) e i **numeri** (sez. 4): rassicura chi è stato spaventato dall'apertura. È un'apertura «shock → promessa → rete di sicurezza → prova», con il volto del venditore già alla terza sezione.

### 4.2 Come costruisce il problema
Il problema non è del lettore, è del **mercato**: «Le aziende le vogliono. Non le trovano. E son disposte a pagare tanto per averle.» (sez. 5). Il lettore è collocato come fornitore mancante, non come persona in difficoltà. La sez. 6 fa poi un lavoro di **pulizia delle alternative**: dropshipping, trading, software, Aliexpress sono bocciati con un link all'avviso SEC; il mestiere di «fare pagine che vendono» è presentato come «il lavoro più vecchio del marketing, solo su uno schermo diverso» (dal 1994). La sez. 8 restringe ancora: siti = vetrina, landing = quello che le aziende vogliono. La sez. 14-15 aggiungono un problema vissuto in prima persona (la crisi dell'agenzia) che diventa la prova del meccanismo.

### 4.3 Il «meccanismo unico»
Non c'è un nome di metodo brevettato. Il meccanismo è la **combinazione di quattro pezzi**, ripetuta tre volte con grafiche diverse:
- sez. 7 — 7 step (studia → landing → prima landing reale → sito → parte clienti → caso studio → primo cliente pagante → «Carriera avviata»);
- sez. 18 — 4 mosse (Impara a fare landing page / Impara a trovare clienti / Chiudi un caso studio / Fatti pagare);
- sez. 25 — lo stack di acquisizione DM Instagram → Loom → Call → Chiusura progetto «testato su 13k leads in 10 mesi».
Il differenziatore dichiarato è **l'AI usata da chi sa cosa deve stare nella pagina** («Schiavizzerai l'AI», «Ruberai il lavoro a chi non sa usare l'AI», «2 tipi di persone»), con stack esplicito nella FAQ: Claude Code, Lovable, Vercel, Canva (`src/29-index-CLKYm5hM.js` → `Hp`, «Mi serve saper programmare?»). L'altra leva è il **reason-why del servizio**: «28 test di 28 servizi… è sopravvissuto solo uno» (sez. 15), con i tre criteri (richiesto dal mercato, non già offerto da tutti, margine).

### 4.4 La storia personale
| Sezione | Contenuto | px | parole |
|---|---|---|---|
| 10 Titolare AP Sales | agenzia, team, «tu farai le stesse cose da solo», albero Formazione/Agenzia | 1.076 | 64 |
| 13 «Ma chi cazzo pensi di essere?» | biografia: paesino → Firenze, introverso 2019, 24 anni, +270K follower, 8 paesi, 1500 studenti; 7 foto | 1.924 | 192 |
| 14 LA CRISI DEL 2025 | agenzia ferma, sperimentazione, troppi clienti a settembre | 603 | 92 |
| 15 28 test | i servizi falliti, il brand OTTO chiuso, i 3 motivi | 1.044 | 139 |
| **Totale** | | **4.647 px = 14,2% della pagina** | **487 parole = 20,5% del copy** |

(Da `scheda.json` → `sezioni[]`.) La storia è **posizionata a metà pagina (y 9.751-16.112)**, dopo il meccanismo e prima dell'obiezione AI: prima convince che il mestiere esiste, poi dice chi è lui. Il tono anti-guru è esplicito («non sono a Dubai (per un giorno) in una Lamborghini (affittata)», sez. 13) e la debolezza è confessata («fino a 6 anni fa ero privo di carisma»). Le foto sono tutte «di lavoro» (scrivania, cucina, monitor, riunione) più una in palestra.

### 4.5 Le prove

| Tipo | Elementi | Sezione | Verificabile? |
|---|---|---|---|
| Numeri di vendita | 4000+ ordini, 1500+ studenti, store dal 2020, 4.8/5 Trustpilot | 4, 27 | Trustpilot linkato (`it.trustpilot.com/review/andrei-copy.com`); gli altri no |
| Numeri di metodo | 13k+ leads (3 volte), 10 mesi, «tasso di risposta ai DM fino al 50%», 28 test | 18, 22, 25, 15 | no |
| Numeri di persona | 24 anni, +270K follower, clienti da 8 paesi | 13 | no (nessun link social in pagina) |
| Numeri di mercato | 4 milioni di partite IVA → 3333 aziende per studente; landing 300-600 € | 27, 28 | il primo è pubblico, il secondo è un'affermazione |
| Autorità esterna | avviso SEC sul trading a breve termine (immagine + link sec.gov) | 6 | sì, linkato |
| Screenshot | 3 landing del portfolio (nastro), 3 consulenze in videochiamata, 2 call di vendita pixelate, 2 template, gruppo Telegram, editor Lovable, siti Apple/Amazon/Notion | 11, 21, 26, 22, 24, 23, 6 | visivi, non verificabili |
| Video | VSL 1 «perché ho scelto le landing», VSL 2 sulla consulenza | 9, 21 | poster in pagina, video su richiesta |
| Volti | Andrei in ≥17 immagini; clienti e team sfocati/pixelati | 3, 8, 9, 10, 12, 13, 21, 26, 28 | — |
| Testimonianze | **nessuna** | — | — |
| Loghi clienti | **nessuno** (solo loghi di tool: ChatGPT, GitHub, Lovable, Krea, Claude, Gemini, Vercel, Instagram, Loom, PayPal, Telegram) | 17, 25, 7, 24 | — |

Fonti: `copy-integrale.md`, `media-inventario.md`, `sezioni/*.png`. La prova è **auto-referenziale e quantitativa**: lui, i suoi numeri, i suoi materiali. L'assenza totale di studenti che parlano è la scelta più rischiosa e più coerente della pagina (il disclaimer dice «I risultati di Andrei non sono tipici»).

### 4.6 Come gestisce le obiezioni
Quattro strati, dal più emotivo al più burocratico:
1. **Obiezione di mercato** («l'AI fa i siti da sola») — sez. 17, con il barrato rosso, i loghi dei tool e le due card «1. / 2.». Risolta con: «L'azienda non ti paga per generare la pagina. Ti paga perché sai quale pagina generare.»
2. **Obiezione di risultato** («Troverai veramente clienti?») — sez. 25, la più lunga della pagina: ammette «dipende… non è facile», poi mostra il metodo e il materiale.
3. **Obiezioni al venditore** («perché lo insegni?», «non ti crei concorrenza?», «perché vendi anche corsi?») — sez. 27, risposte deliberatamente ciniche («Perché mi paghi, lol», «Semplice: soldi») che disarmano il sospetto rendendolo esplicito.
4. **Obiezioni pratiche** — 14 FAQ in due gruppi (corso / pagamento) + 4 FAQ sulla consulenza (sez. 21). Risposte estratte dal bundle (`src/29-index-CLKYm5hM.js`, array `Hp`, `Up()`, `Wp`): tutte le lezioni subito; principianti sì; «divento ricco? No. Lol.»; stack Claude Code/Lovable/Vercel/Canva; abbonamenti richiesti a Lovable, Claude pagato e Vercel; P.IVA «a un certo punto sì»; garanzia «No… non esiste in nessun business»; 3 rate Klarna/PayPal; fattura entro 24h; bonifico «consiglio di no».
Le risposte non sono nel DOM (accordion chiusi) ma **sono nel JSON-LD FAQPage**, quindi Google le legge anche se il visitatore non apre nulla.

### 4.7 Come chiude
Sez. 28: la domanda «quanto pagheresti?», l'ancoraggio «una singola landing page… tra i €300 e i €600. Il corso si ripaga con il primo cliente», la rassicurazione «UNICO pagamento», il bottone «Sono pronto ↗». Poi FAQ e disclaimer. La chiusura è **razionale (matematica del ritorno) dopo una pagina emotiva**, e il titolo la incornicia con la parola più grande della promessa: «cambiare vita».

### 4.8 Che urgenza usa
- **Vera, a data fissa**: rincaro da 434 a 560 € dal 12 ottobre 2026, con countdown a giorni/ore/minuti/secondi (`sezioni/19`, `copy-integrale.md` y=20.855). Nel codice `Rp()`/`Vp()` calcolano il residuo da `PROSSIMO.dal`; se la data è passata il blocco sparisce (`return null`) (`src/29-index-CLKYm5hM.js`). Nessun timer «per te» che riparte ad ogni visita.
- **Nessuna scarsità di posti**, nessun «ultimi 3», nessun bonus a scadenza.
- **Urgenza implicita nel copy**: «oggi» (hero 2, sez. 23), «domani» (sez. 23), «Nel 2026 tutti fanno siti» (sez. 8), «Ora lo standard è rappresentato dall'AI» (sez. 17).

### 4.9 Come è costruita l'offerta
| Componente | Presente? | Dove |
|---|---|---|
| Prezzo unico | sì, 434 € | sez. 19 |
| Prezzo ancorato a un «valore» gonfiato | **no** | — |
| Prezzo barrato / sconto | **no** (scaglione futuro, non sconto passato) | sez. 19 |
| Rate | sì, 3 rate Klarna/PayPal (solo in FAQ) | sez. 29 |
| Stack di contenuti | sì, ma **a richiesta** (4 tab del raccoglitore) | sez. 20 |
| Bonus con valore a fianco | **no**: asset (template, script), community, registrazioni call presentati senza prezzo | sez. 22, 24, 26 |
| Garanzia | consulenza 5 ore a €0 dopo corso finito + 50 contatti | sez. 3, 19, 21 |
| Artefatto fisico dell'offerta | sì: tessera/badge con laccio e QR | sez. 19 |
| Accesso a vita | sì, dichiarato 2 volte + meta | sez. 19, FAQ |
| Disclaimer | sì, 12 px, in fondo alle FAQ | sez. 29 |

L'offerta è **piatta e onesta per scelta**: un numero, una data, una condizione di garanzia. Tutta la percezione di valore è costruita **prima** (18 sezioni) e **dopo** (asset, community, call reali) invece che dentro il blocco prezzo.

### 4.10 Le parole che ricorrono
Conteggio Python su `dom-blocks.json` (tag p/h1/h2/h3/li/button/a, blocchi deduplicati, minuscolo, stop-word italiane escluse; 2.376 parole totali). Il token «i» (27) è escluso dalla tabella come stop-word.

| # | Parola | n | # | Parola | n | # | Parola | n |
|---|---|---|---|---|---|---|---|---|
| 1 | landing | 20 | 11 | cliente | 8 | 21 | persone | 6 |
| 2 | clienti | 17 | 12 | sales | 8 | 22 | serve | 6 |
| 3 | funnel | 15 | 13 | testato | 7 | 23 | call | 6 |
| 4 | operator | 15 | 14 | trovare | 7 | 24 | parte | 5 |
| 5 | corso | 15 | 15 | business | 7 | 25 | pagare | 5 |
| 6 | pages | 11 | 16 | anni | 7 | 26 | pagine | 5 |
| 7 | pagina | 10 | 17 | azienda | 7 | 27 | lavoro | 5 |
| 8 | soldi | 9 | 18 | step | 7 | 28 | avuto | 5 |
| 9 | online | 8 | 19 | ap | 7 | 29 | siti | 5 |
| 10 | aziende | 8 | 20 | page | 6 | 30 | funziona | 5 |

| # | Bigramma | n | # | Bigramma | n |
|---|---|---|---|---|---|
| 1 | funnel operator | 15 | 11 | page online | 2 |
| 2 | landing pages | 11 | 12 | online 24h | 2 |
| 3 | ap sales | 7 | 13 | andrei pascu | 2 |
| 4 | trovare clienti | 6 | 14 | aziende vogliono | 2 |
| 5 | landing page | 5 | 15 | corso insegno | 2 |
| 6 | primo cliente | 3 | 16 | caso studio | 2 |
| 7 | i soldi | 3 | 17 | cliente pagante | 2 |
| 8 | 13k leads | 3 | 18 | agenzia ap | 2 |
| 9 | metodo chiaro | 2 | 19 | nostri clienti | 2 |
| 10 | chiaro testato | 2 | 20 | page venduta | 2 |

Altri conteggi utili (stessa base): «client-» 25, «aziend-» 15, «l'AI» 12, «non» 38 (la negazione è lo strumento retorico più usato: «Non diventerai ricco…», «non sono a Dubai», «Non è un business sexy», «non è facile», «No. Lol.»), «soldi» 9, «garan-» 2, «test-» 8, «carriera» 4, «vita» 5.

Lettura: il lessico è **transazionale** (clienti, pagare, soldi, azienda, cliente pagante) e **operativo** (landing, pagina, step, call, testato). Non compaiono «libertà», «passione», «successo», «mindset». La parola «soldi» detta 9 volte è il registro anti-guru dichiarato.

---

## 5. Confronto con il sito di Digital Empire

Sito nostro: `https://agency-empire-landing.vercel.app` (catturato in `capture/63-agency-landing-vero/`: `design-tokens.json`, `dom-blocks.json`, `copy-integrale.md`). Misure note da brief: 38.683 px desktop, 37 blocchi, 10 CTA, 0 fotografie, 5 famiglie di gradiente; confermate da `design-tokens.json` → `page_height: 38683`, `mobile_page_height: 64255`, `ctas: 10`, `images: 0`.

| Dimensione | funneloperator.it | agency-empire-landing | Lettura |
|---|---|---|---|
| Cosa vende | corso 434 € una tantum (B2C, carriera) | servizio agenzia (sistemi AI proprietari), prezzo non esposto, CTA «Prenota una chiamata» | modelli diversi: lui chiude in pagina, noi chiudiamo in call |
| Altezza desktop | 32.807 px | 38.683 px (+18%) | noi più lunghi con meno immagini |
| Altezza mobile | 36.630 px (+12% vs desktop) | 64.255 px (+66% vs desktop) | il nostro mobile raddoppia quasi; il suo cresce di un decimo |
| Sezioni | 30 | 37 blocchi (+5 divider) | — |
| Parole nel copy | 2.376 | 3.978 (`dom-blocks.json` 63) | noi +67% di testo |
| Headings | 56 (1 h1, 22 h2, 33 h3) | 120 | noi il doppio di titoli |
| CTA di vendita nel flusso | 2 bottoni (y=20.998, 30.648) + 1 flottante + 1 ancora | 10, la prima a y=800, poi 910, 1.943, 1.943, 16.028, 24.995, 31.682, 33.081, 38.174 | lui rimanda la richiesta al 64%; noi chiediamo dalla prima schermata |
| Testo delle CTA | 3 varianti («Iscriviti adesso», «Sono pronto», «Ottieni accesso») | 1 variante ripetuta («Prenota una Chiamata Gratuita 30 MIN · GRATUITA · ZERO IMPEGNO») | — |
| CTA flottante | sì («Ottieni accesso», basso-destra) | no (10 CTA in linea) | — |
| Fotografie | 68 file, ≥17 con il volto del fondatore, 7 foto biografiche | **0** (`images: 0`) | il nostro sito non ha un volto |
| Video | 2 VSL | 0 | — |
| Primo volto | y=2.793 (8,5%) | mai | — |
| Prezzo | 434 € esplicito, +560 € futuro, ancoraggio 300-600 € | nessun prezzo (0 occorrenze di «prezzo»; «€» 5 volte in esempi) | — |
| Urgenza | countdown reale a data (12/10/2026) | nessuna | — |
| Garanzia | consulenza condizionata; «garan-» 2 volte; FAQ «No» | «Garanzia 30 giorni», «garanzia» 4 volte, «30 giorni» 8 volte, «Se il sistema non funziona come promesso, lo sistemiamo.» | la nostra è più forte a parole; la sua è più concreta (5 ore, calendario, Meet) |
| Storia personale | 4 sezioni, 4.647 px, 7 foto, numeri | 4 h2 («Sei anni fa ero un ragazzo ossessionato da Internet», «Poi un giorno ho deciso di non lavorare più da solo», «Tre persone…», team Maximilian/Gael/Leonardo) senza foto | noi abbiamo il team, lui ha le immagini |
| Prove numeriche | 4.8/5, 4000+, 1500+, 13k, 50%, 28 | nessun numero di risultato cliente (placeholder) | — |
| Testimonianze | 0 | 0 | pari |
| Portfolio | 3 landing in nastro | 0 screenshot di sistemi | — |
| Obiezioni | sez. 17 (AI) + sez. 27 (3 domande) + 18 FAQ | «Le 4 obiezioni che demoliamo» + 5 FAQ | lui 21 risposte, noi 9 |
| FAQ in JSON-LD | sì (18 Q/A `FAQPage`) | non rilevato nei token | — |
| Sfondi | 2 tinte piatte + blu; 0 gradienti | `#1c1c1c`, `#fafafa`, `#0a0a0a`, `#fb4604`, 5 famiglie di gradiente, grana | lui piatto, noi materico |
| Caratteri | Inter Tight + Plus Jakarta Sans + DM Mono + Curseyt (1 uso) | Onest + Instrument Serif + mono | pari per numero di famiglie |
| Colore d'azione | blu `oklch(0.656 0.134 235.9)`, 6 sfondi | arancio `#fb4604`, 8 sfondi | entrambi sotto il 10% |
| Micro-CTA di scorrimento («↓») | 3 | 0 | — |
| Header | loghi + «Accedi», nessuna CTA | «Prenota» in header (y=-62) | — |
| Costruzione | app React/TanStack con auth, checkout, area membri, admin | Next.js (landing) | il suo dominio è anche la piattaforma del corso |

### 5.1 Cosa lui fa che noi non facciamo
1. Mostra il **volto** del fondatore entro 3.000 px e lo ripete 17 volte.
2. Espone **numeri di prova** in un nastro alto 273 px, subito dopo la garanzia.
3. Dà una **garanzia condizionata concreta** (cosa devi fare tu, cosa ottieni, come si fissa, dove).
4. Mette **un prezzo, una data e un countdown vero**.
5. Fa una **storia biografica con fotografie** e una crisi raccontata.
6. Spiega **perché quel servizio e non altri** (28 test, 3 criteri).
7. Mostra **call di vendita registrate** e **template** come prova del «dentro».
8. Risponde a **domande ostili** sul venditore stesso, con cinismo dichiarato.
9. Usa un **bottone flottante** che sostituisce 8 CTA in linea.
10. Inietta le FAQ come **FAQPage** per il motore di ricerca.
11. Usa **micro-CTA di scorrimento** («↓») nella prima metà.
12. Chiude con una **matematica del ritorno** (300-600 € per landing → si ripaga col primo cliente).

### 5.2 Cosa noi facciamo che lui non fa
1. Un **team di tre nomi** («Tre persone. Zero filtri tra te e chi costruisce.»): lui è solo.
2. Una **garanzia a parole più larga** («Se il sistema non funziona come promesso, lo sistemiamo», 30 giorni).
3. Un **framework nominato** (F.L.O.W.) e uno stack tecnico dichiarato in 15 loghi/h3.
4. **CTA dalla prima schermata** e in header.
5. Un **percorso post-chiamata** in 6 step («Cosa succede esattamente dopo la chiamata»).
6. Il **confronto a tre livelli** (Operatività manuale / SaaS di terze parti / Sistema AI proprietario).
7. Grana, gradienti, argento: una **materia visiva** che lui non ha (le sue superfici sono piatte).
8. Testo più lungo (+67%) e più titoli (+114%).

---

## 6. Le 15 lezioni di struttura

Vincolo (legge di Max 12/09, `feedback_sito_online_solo_aggiungere`): sul sito online si può **solo aggiungere** sezioni o elementi nuovi, mai modificare o sostituire l'esistente. Ogni traduzione qui sotto è quindi un'aggiunta pura: un file nuovo, un inserimento puro, CSS scopato.

| # | Cosa fa lui (sezione) | Perché funziona | Aggiunta al nostro sito (solo nuovo) |
|---|---|---|---|
| 1 | **Nastro di 4 numeri** alto 273 px subito dopo la garanzia (sez. 4: 4.8/5, 4000+, 1500+, 2020) | Una riga di cifre pesa poco e chiude la domanda «ma chi sei?» prima che nasca; l'animazione `fo-rail` la rende viva senza rubare spazio | Nuova sezione `numeri-rail` sotto la hero attuale: 4 numeri veri di DE (anni di attività, sistemi consegnati, email/giorno gestite, ore risparmiate misurate) con icona e nastro CSS scopato `.vivo` |
| 2 | **Garanzia condizionata con il volto** a y=2.377 (sez. 3): «se fai X e non ottieni Y, hai Z» con foto del fondatore | Trasforma la garanzia da slogan a contratto: dice cosa deve fare il cliente, cosa dà lui, e lo firma con la faccia | Nuova sezione `cosa-succede-se-non-funziona`: testo a 37 px in due blocchi incrociati con foto di Max, che rende concreta la «Garanzia 30 giorni» già online (chi fa cosa, entro quando, dove si chiede) |
| 3 | **Percorso a 7 step con arrivo verde** (sez. 7) | La sequenza numerata risponde a «e poi?» senza testo; l'arrivo colorato è l'unico verde della pagina e fa da traguardo | Nuova sezione `come-funziona-7-passi` con lo stesso zig-zag: chiamata → proposta → contratto → setup → go-live → supporto → «Sistema che gira da solo» in verde; complementare a «Cosa succede esattamente dopo la chiamata» già online |
| 4 | **Prima/dopo visivo con due foto** e titolo barrato (sez. 8: «Fare siti» barrato / «Fare landing pages.» verde) | Il confronto è letto in un secondo; il barrato dice cosa lasciare, il colore dice dove andare | Nuova sezione `agenzia-classica-vs-sistema`: due colonne con foto (sinistra b/n: pila di fatture mensili; destra a colori: dashboard consegnata), titolo barrato «Canone mensile» / titolo pieno «Asset tuo.» |
| 5 | **VSL con il volto a 900 px di altezza** (sez. 9) + seconda VSL sulla garanzia (sez. 21) | Il video sposta la fiducia dal testo alla persona; il poster da solo, con il play, già umanizza la pagina | Nuova sezione `video-max` sotto «Perché Digital Empire?»: poster di Max alla scrivania, bottone play, 2-3 minuti su «perché sistemi proprietari e non abbonamenti» |
| 6 | **Albero «Tu sei qui»** (sez. 10: AP Sales → Formazione / Agenzia) | Colloca la pagina dentro un'azienda più grande: chi legge capisce che dietro c'è una struttura, non un funnel | Nuova sezione `mappa-empire`: Digital Empire → Agency / Formazione / SaaS con puntatore arancione «Tu sei qui» sul ramo Agency; linka Manuale Claude Code e app senza toccare le sezioni esistenti |
| 7 | **Portfolio a nastro** con screenshot delle landing dell'agenzia (sez. 11) | Anche solo 3 pezzi ripetuti in un nastro danno l'idea di «ne facciamo tante»; sono prove visive, non parole | Nuova sezione `sistemi-in-produzione`: nastro di screenshot reali delle dashboard consegnate (Outreach, Content Factory, Second Brain) con dati oscurati; 3-6 immagini bastano |
| 8 | **Storia con 7 fotografie di lavoro** (sez. 13) e crisi raccontata (sez. 14) | Le foto «brutte» (cucina, monitor di notte) sono la prova che non è un attore; la crisi ammessa rende credibile il successo | Nuova sezione `dietro-le-quinte` accanto a «Sei anni fa ero un ragazzo…»: 6 foto vere di Max, Gael e Leonardo al lavoro, con una riga per ciascuna; niente stock, niente render |
| 9 | **Reason-why del servizio** («28 test, uno sopravvissuto», 3 criteri con icone, sez. 15) | Spiega perché vende proprio quello, non solo cosa vende: chi legge smette di chiedersi «perché non altro?» | Nuova sezione `perche-sistemi-e-non-ore`: «Abbiamo venduto consulenza, siti, gestione social… è sopravvissuto uno: il sistema che resta al cliente», con 3 criteri (richiesto, non commodity, margine) |
| 10 | **Polarizzazione «2 tipi di persone»** sull'obiezione AI (sez. 17) | Trasforma la paura («l'AI mi sostituisce») in una scelta di campo; la card 2 con bordo blu è dove il lettore vuole stare | Nuova sezione `due-tipi-di-aziende`: card 1 «Chi compra un abbonamento e resta in affitto» / card 2 «Chi possiede il sistema»; rinforza «ChatGPT fa già tutto questo, gratis» già online senza modificarla |
| 11 | **Domande ostili sul venditore** con risposte ciniche (sez. 27: «Perché mi paghi, lol») | Dire ad alta voce il sospetto lo neutralizza; il tono spiazza e rende umano | Nuova sezione `le-domande-che-non-ci-fate`: «Se i sistemi funzionano così bene perché non li usate solo per voi?», «Perché una chiamata gratis?», «Cosa ci guadagnate?» con risposte dirette in una frase |
| 12 | **Ancoraggio economico in chiusura** («una landing vale 300-600 €, il corso si ripaga col primo cliente», sez. 28) | Riporta il prezzo a un'unità che il lettore già conosce e fa il conto al posto suo | Nuova sezione `quanto-costa-non-farlo` prima della CTA finale: ore/mese di operatività manuale × costo orario vs setup una volta; «il sistema si ripaga in N mesi» con la formula visibile |
| 13 | **FAQ in due gruppi + JSON-LD FAQPage** (sez. 29 + bundle) | La divisione (prodotto / pagamento) fa trovare la risposta in un colpo; lo schema fa leggere le risposte a Google anche con gli accordion chiusi | Nuova sezione `faq-contratto-e-pagamento` (fattura, rate, cosa succede se cambiamo idea, chi possiede il codice) sotto le 5 FAQ attuali + `<script type="application/ld+json">` FAQPage in `layout.tsx` come inserimento puro |
| 14 | **Bottone flottante «Ottieni accesso»** dal secondo scroll in giù (`desktop-03.png`) | Una sola CTA sempre visibile permette al testo di non interrompersi mai; il lettore decide quando | Nuovo componente `prenota-flottante` fisso in basso a destra (compare dopo 1.000 px, nasconde quando il footer è visibile), link a `/prenota/` già esistente; nessuna delle 10 CTA attuali viene toccata |
| 15 | **Artefatto dell'offerta** (tessera con laccio, 4 spunte e QR, sez. 19) + **countdown a data vera** | Un oggetto rende tangibile un servizio immateriale; una scadenza reale (verificabile) non consuma fiducia come i timer finti | Nuova sezione `la-tua-tessera`: card «Sistema Empire» con 4 spunte (codice consegnato, 90 giorni supporto, garanzia 30 giorni, zero canoni) e, se esiste un vincolo reale (posti al mese, listino che cambia a data), un contatore calcolato dalla data e non dal cookie |

Regole trasversali imparate dalla pagina (valgono per tutte le 15 aggiunte):
- **Un solo colore d'azione**, usato solo per ciò che si clicca (`palette_sfondi`: blu 6 volte su 30 sezioni). Per noi resta `#fb4604` sotto il 10%.
- **Sezione densa → sezione visiva**: mai due blocchi di 150+ parole consecutivi (schema di §3.3).
- **Il volto prima del 10% della pagina**, il video prima del 30%.
- **Una CTA testuale di scorrimento («↓») è meglio di una CTA di vendita** nella prima metà: spinge avanti senza chiedere.

---

## 7. Cosa NON copiare (difetti visti, da tenere come gate)

1. **Portfolio con 3 pezzi ripetuti 37 volte** (sez. 11, `scheda.json` → `media: 37` per 3 file): il nastro lo maschera, ma chi guarda due volte lo nota. Gate per noi: un nastro parte solo con ≥5 immagini distinte.
2. **Screenshot riusati** (`sito-notion.webp` in sez. 6 e 23; `template-fasi.webp` e `template-messaggi.webp` due volte ciascuno in sez. 22) — `media-inventario.md`.
3. **Zero testimonianze e zero nomi di clienti**: coerente col tono, ma lascia tutta la prova su una persona. Noi abbiamo lo stesso vuoto (0 volti): non è un pareggio da difendere.
4. **Il programma del corso è nascosto dietro 4 tab** (sez. 20): chi non clicca non sa cosa compra. Il nostro «Ogni sistema, nel dettaglio» è più leggibile: tenerlo.
5. **Accordion chiusi con risposte solo nel JS**: buono per SEO, ma il lettore da telefono deve toccare 18 volte. Se aggiungiamo FAQ, la prima risposta di ogni gruppo va aperta di default.
6. **Rail a 70 s** con icone e numeri: su mobile il movimento continuo può stancare; usare `prefers-reduced-motion`.

---

## 8. Fonti (file letti per questo rapporto)

Tutti sotto `C:\Users\Utente\Desktop\qui tutto\Digital Empire\competitor\Andrei Pascu\site-study\`:

- `capture/66-funneloperator-it/scheda.json` — sezioni (y, h, bg, media, cta, parole), `cta[]`, `media[]`, headings, palette, scala tipografica, keyframes, effetti, meta e JSON-LD, altezze desktop/mobile, costruzione.
- `capture/66-funneloperator-it/copy-integrale.md` — tutto il testo in ordine di y (1.472 righe), letto per intero.
- `capture/66-funneloperator-it/dom-blocks.json` — 386 blocchi con tag/colore/corpo, base per il conteggio parole e bigrammi.
- `capture/66-funneloperator-it/design-tokens.json` — struttura token (chiavi verificate).
- `capture/66-funneloperator-it/estratto-css.md` — variabili `--fo-*`, `--spazio-*`, `--colonna: 832px`, 13 keyframes.
- `capture/66-funneloperator-it/media-inventario.md` — 68 file, px originali vs resi, peso, alt.
- `capture/66-funneloperator-it/sezioni/01..30-*.png` — 30 schermate viste una per una (classificazione visiva di §2 e note di §2.1).
- `capture/66-funneloperator-it/desktop-01.png`, `desktop-03.png`, `desktop-24.png`, `desktop-30.png` — header, bottone flottante, blocco prezzo.
- `capture/66-funneloperator-it/mobile-01.png` — hero da telefono.
- `capture/66-funneloperator-it/src/29-index-CLKYm5hM.js` — costante prezzo `Ip`, funzioni `Rp/Vp/zp/Lp`, array FAQ `Hp`, `Up()`, `Wp`, generatore JSON-LD `Xp()`, rotte auth/admin, Supabase.
- `capture/66-funneloperator-it/src/05-buy-button-DX_4IxaR.js` — logica del bottone di acquisto.
- `capture/66-funneloperator-it/src/_INDICE.json` e nomi dei chunk in `src/` — stack (TanStack Router, Radix accordion/dialog/dropdown, Lucide, Vite).
- `capture/63-agency-landing-vero/design-tokens.json`, `dom-blocks.json`, `copy-integrale.md` — sito Digital Empire per il confronto di §5.
- `reports/11-armageddon.md` — formato del frontmatter e della testata.
- `company/Memory/checkpoints/CP-20260911-JF6H.md`, `company/Memory/riprese/EMP-2AW3.md` — conferma delle misure del sito DE (38.683 px, 37 sezioni, 10 CTA, 0 foto).

Conteggi eseguiti con Python nella sessione del 2026-09-13 (parole, bigrammi, somme px per ruolo e sfondo, distanze CTA); nessun numero è stimato a occhio.
