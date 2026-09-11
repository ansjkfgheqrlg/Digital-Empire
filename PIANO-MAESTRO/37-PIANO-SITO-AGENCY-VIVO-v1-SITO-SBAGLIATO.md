---
Type: PROJECT
Status: Active
Tags: #agency #sito #andrei-pascu #tono #immagini-aura #fabbrica-siti #piano
Created: 2026-09-11
Last updated: 2026-09-11
---

# DOSSIER 37 — SITO AGENCY VIVO
## Tono, elementi, immagini: quello che Andrei Pascu ha e il nostro sito no — in ottica nostra

**Ordine di Max (2026-09-11, sera):** «Rimettiamoci sui siti, si parte dal sito dell'Agenzia. Prendere
tutta la conoscenza dei siti di Andrei Pascu — gli ultimi due lanci, Claude Speedrun e quello piccolo
(Armageddon). Ci manca il suo tono (provocatorio, simpatico), e soprattutto il design, la struttura, gli
elementi dentro: i suoi siti sono vivi perché hanno immagini; noi ne abbiamo zero e una cartella piena
(`Caroselli Style/immagini AURA`). Il tutto abbinato al copy. **Non partire a modificare: un piano
strutturato nel minimo dettaglio.**»

**Cosa è questo documento.** Il piano, non il build. Scritto in quattro giri come vuole Max: P0 (il
piano), Critica 1 → P1, Critica 2 → P2, Critica 3 → P3, poi il **V4 esecutivo** in fondo. I giri restano
scritti. Il build parte **solo su ordine di Max**, con blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md`.

**Perimetro:** `agency-empire/` (Next.js 16.2.3, Corsia B della Fabbrica Siti), live su
`https://agency-empire-kohl.vercel.app`. **Non tocca:** `PIANO-MAESTRO/31-*/V4-ESECUTIVO/` (in scrittura,
EMP-D9HD), EMP-8M9F, LANCI. Zero collisione di file.

**Fonti (tutte già su disco, misurate a macchina):**
- `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md` — 34 tavole, la pagina su cui ha speso più lavoro (33.756 px, 40 CTA)
- `competitor/Andrei Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md` — il lancio piccolo, 5.103 px, costruito con Claude Code
- `competitor/Andrei Pascu/site-study/SINTESI-SISTEMA-COPY.md` — 22 formule, 10 regole del suo copy
- `competitor/Andrei Pascu/site-study/SINTESI-SISTEMA-VISIVO.md` — 52 pagine, la temperatura del traffico governa la forma
- `competitor/Andrei Pascu/ANATOMIA-DEI-LANCI.md` — sei mosse, otto costanti, sette difetti
- `competitor/Andrei Pascu/site-study/capture/10-noi-post-restyling/` — **il nostro sito catturato con lo stesso strumento**
- `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` — la legge (§1-§12), i 13 pattern già estratti

---

# PARTE I — DIAGNOSI MISURATA: il nostro sito contro i suoi due lanci

Stesso strumento (`site_capture.py`), stesse metriche. Nessun giudizio a occhio.

| Misura | **Noi** (agency-empire) | Claude Speedrun | Armageddon | Cosa dice |
|---|---|---|---|---|
| Altezza desktop | **43.359 px** | 33.756 px | 5.103 px | Siamo il 28% più lunghi della sua pagina più lunga |
| Altezza mobile | **70.173 px** | — | 2.830 px | 14 schermate di telefono in più |
| Sezioni | 21 + **16 divider** | 34 | 4 | Un terzo dei nostri "blocchi" è un separatore |
| CTA | **11** → una ogni **3.940 px** | 40 → una ogni 844 px | 7 → una ogni 729 px | La sua media su 25 pagine calde: **1 ogni ~1.100 px**. Noi 3,6× più radi |
| Fotografie | **0** | ~15 foto/meme + 59 media recensioni | 3 foto + 2 biglietti | Le nostre 147 "immagini" sono icone SVG di Lucide |
| Dimensioni tipografiche distinte | **195** | — | ~14 (tutte frazioni di `--u`) | §1 della legge violato: nessuna scala, ogni sezione inventa |
| Colori testo / sfondo | **64 / 48** | 2 neutri + accento | `#000` `#fff` `#bc0807` | Il suo guscio non cambia mai; il nostro cambia a ogni sezione |
| Heading | **125** (h3 da 11px uppercase usati come etichette) | 34 sezioni, 3 H1 deliberati | 4 | Gerarchia semantica sporca |
| Accento `#fb4604` | ovunque: bubble, chip, marquee, corsivi, bottoni | cerchi, badge, CTA, **una** fascia piena | solo hover + celle contatore | §12: "l'accento si spende una volta" — noi lo spendiamo cento volte |
| Prima persona | **zero** ("noi costruiamo", "il sistema") | "Ti voglio bene, ma… non sai usare l'AI. Sul serio." | "Sei pronto?" | Il suo sito parla; il nostro descrive |
| Prova visiva reale | 0 screenshot dei nostri sistemi | screenshot cancellazione ChatGPT, SERP reale, dashboard | video 13:29 | Diciamo "dashboard live" senza mostrarla |

**Diagnosi in una riga:** il nostro sito è **un documento tecnico impaginato bene** — corretto,
lungo, grigio, senza volto. Il suo è **una persona che ti parla**, con le foto sul tavolo. Max ha
visto giusto: la differenza non è la qualità del codice (il nostro è più pulito del suo), è **vita**.

**Tre cose che abbiamo già e lui no** (non si buttano): grana a 4 strati, marquee metallico, il canone
Empire con Onest dichiarato (lui su 38 pagine su 52 non dichiara un carattere), il gate `gate_siti.py`.

---

# PARTE II — I TRE ASSI (nell'ordine di Max)

## Asse A — IL TONO: cos'ha lui, cosa prendiamo, cosa no

**Come parla lui, misurato** (SINTESI-SISTEMA-COPY §2, ATLANTE Speedrun):
1. **Prima persona singolare, sempre.** "Io stesso sono un marketer. Ho un'agenzia."
2. **Insulto affettuoso.** "Ti voglio bene, ma... Non sai usare l'AI. Sul serio." — "Lo stupido sei tu LOL. JK."
3. **Dichiara il proprio interesse prima che tu lo sospetti.** "Perché dopo ti propongo di entrare, quindi ci guadagno sia io che tu."
4. **Rifiuto secco + delega del conto.** FAQ: "No. Fai tu il conto prima di comprare." — "No, e diffida di chi lo fa."
5. **Negazione ×3-4 → una affermazione.** "Niente balletti. Niente hype. Niente scam. Solo una skill."
6. **Autoironia sulla manipolazione stessa.** La spirale ipnotica: "Vediamo se questo funziona."
7. **La provocazione paga sempre con una prova.** "Questi stronzi investono miliardi" → screenshot articolo $110B. "ChatGPT è mid" → screenshot cancellazione abbonamento.
8. **L'obiezione detta con le parole del lettore.** "Andrei, chiunque tu sia… Parli tanto. Ma chi pensi di essere???"
9. **Il meme come argomento**, non come decorazione (tre teste / gattino / doccia fredda alle 5).
10. **Aritmetica esplicita al posto dell'aggettivo.** Produttività = output/tempo → 6/2=3, 10/2=5, +66%.

**LA VOCE DIGITAL EMPIRE — dieci regole (in ottica nostra, non sua):**

| # | Regola | Suo | Nostro |
|---|---|---|---|
| V1 | **Parla una persona.** Prima persona: "io" dove parla Max, "noi" dove parla il team — mai "il sistema" come soggetto di una frase persuasiva | "Io stesso sono un marketer" | "Ho costruito il primo Outreach Factory per me, perché mandavo 30 DM a mano ogni mattina." |
| V2 | **Provocare è lecito, insultare no.** Il nostro lettore è un titolare (concessionario, coach, agenzia). Si può dirgli che spreca, non che è stupido | "Lo stupido sei tu LOL" | "Ti voglio bene, ma stai pagando uno stipendio a un lavoro che si fa da solo." |
| V3 | **Ogni provocazione paga entro due righe con un numero verificabile.** Senza numero la frase non entra | "$110 miliardi" + screenshot | "300+ messaggi al giorno" + screenshot vero della dashboard |
| V4 | **Il "No." secco nelle FAQ e nelle obiezioni.** Poi il conto lo fa lui | "No. Fai tu il conto." | "Canone mensile? No. Fai tu il conto: 12 × quello che paghi oggi." |
| V5 | **Negazione ×3 → una affermazione**, una volta per pagina, nel punto di massima diffidenza | "Niente balletti…" | "Niente slide. Niente demo finta. Niente 'ti richiamiamo'. In chiamata il sistema gira davanti a te." |
| V6 | **Dichiara l'interesse.** Vendiamo una chiamata, e lo diciamo | formula 16 | "Sì, alla fine ti proponiamo di lavorare insieme. Ci guadagniamo tutti e due, o non lo faremmo." |
| V7 | **L'obiezione in bocca al lettore**, con virgolette, poi la risposta | "Andrei, chiunque tu sia…" | "«Sì ok, ma voi chi siete?» — Giusto. Guarda." |
| V8 | **Zero Barnum.** Dove lui mette la diagnosi universale ("sei disinformato") noi mettiamo il caso reale con nome | formula 22 | Novacar / Preventa, con i numeri che abbiamo davvero |
| V9 | **Aritmetica al posto dell'aggettivo.** Una formula esplicita per pagina | produttività 6/2 vs 10/2 | "30 DM a mano = 2,5 ore. 300 dal sistema = 0 ore tue. Fai tu la divisione." |
| V10 | **Lista nera di parole.** Non entrano: *stronzi, cazzo, cagata, mid, brokie, LOL, JK, daddy*. Entrano: *sul serio, ti voglio bene ma, fai tu il conto, guarda, no.* | — | gate meccanico in F1 |

**Cosa NON copiamo (deciso, non discutibile nel build):** le parolacce (V10); la scarsità di tempo
(non vendiamo un lancio, vendiamo una chiamata: un countdown sarebbe la bugia che lui stesso rifiuta);
il "curiosity gap totale" (griglia `???`): un'agenzia che nasconde cosa fa perde la chiamata; il
secondo e terzo H1 a metà pagina (effetto sì, ma lo otteniamo con tipografia-manifesto fuori
gerarchia, come il suo "GET. SHIT. DONE.").

## Asse B — DESIGN, STRUTTURA, ELEMENTI: l'inventario di ciò che è "vivo"

Ogni elemento con la tavola d'origine, cosa fa **per lui**, e cosa farebbe **per noi**. Dove il pattern
esiste già nella Fabbrica (`.claude/skills/fabbrica-siti/pattern/`) è segnato: si avvolge in
componente React (§5: dal vanilla si sale), non si reinventa.

| # | Elemento | Origine | Funzione per lui | Per noi | Pattern Fabbrica |
|---|---|---|---|---|---|
| E1 | **Hero a due colonne**: foto sfocata a sinistra + testo su nero a destra, zero CTA | Speedrun T1 | vende l'atmosfera prima di chiedere | prima schermata con un volto, non con un H1 gigante centrato | `hero-due-strati` (da adattare) |
| E2 | **Tipografia-manifesto fuori gerarchia** ("GET. SHIT. DONE." su fascia arancione, "5X" in contorno) | Speedrun T3 | intensità senza sporcare la SEO | una parola-manifesto per pagina ("FATTO." / "H24.") | nuovo: `tipografia-manifesto` |
| E3 | **Fascia-lampo a colore pieno**, 431 px, la sezione più corta con testo | Speedrun T12 | cambio di ritmo fra due sezioni lunghe | "Hai competitor e non lo sai" — l'unico punto dove `#fb4604` è sfondo | nuovo: `fascia-lampo` |
| E4 | **Finta chat / prova d'imbarazzo** ("Ciao ChatGPT correggilo daddy 🥴") | Speedrun T6 | specchio: ti riconosci prima della promessa | il DM copia-incolla che manda un concessionario oggi, vero, anonimizzato | nuovo: `specchio` |
| E5 | **Micro-sondaggio "Dimmi se ti ritrovi"** — due pulsanti fantasma, stesso scroll | Speedrun T7 | micro-commitment: un clic fisico | sotto i 4 segnali della diagnosi: "Sì, mi ritrovo / No" → stesso ancoraggio | nuovo: `micro-sondaggio` |
| E6 | **"ASCOLTA BENE." in casella arancione** + prova numerica sotto | Speedrun T8 | climax dell'aggravamento | **abbiamo già la sezione `05b-ascolta-bene`** — oggi è una riga; diventa il climax | esistente da rifare |
| E7 | **Tris di autodiagnosi** con cerchi arancioni numerati | Speedrun T9 | segmenta le obiezioni | i 3 motivi per cui non hai ancora automatizzato | Corsia B semplice |
| E8 | **Confronto a due colonne ORA / CON** (pallino vuoto / pieno) | Speedrun T20 | prima/dopo in 6 parole | "OGGI: 30 DM a mano, 2,5 h / CON: 300, 0 h tue" | nuovo: `ora-con` |
| E9 | **Diagramma posizionale** BROKIE → TU → COMPETITOR, "sei qui" | Speedrun T18 | mette il lettore fisicamente su un asse | "A MANO → TU → AUTOMATIZZATO" | nuovo: `asse-posizionale` |
| E10 | **Oggetto-icona del prodotto** (biglietto) mostrato intero, poi **richiamato in filigrana** più avanti | Speedrun T17+T20, Armageddon T3 | un asset, due usi: il prodotto diventa oggetto | il nostro oggetto: **la dashboard** (screenshot vero, cornice) — intera in Servizi, in filigrana dietro la CTA finale | `oggetto-che-si-posa` |
| E11 | **Numeri in filigrana translucidi** nelle card (1/2/3 enormi, opacità bassa) | Speedrun T15 | ritmo senza peso | card Processo 4 fasi | CSS canone |
| E12 | **Stanza a parte**: sfondo `#202021` usato una sola volta, per la bio | Speedrun T16 | "qui si esce dal ritmo di vendita" | Chi siamo: unico sfondo diverso, **facce vere** | canone: aggiungere `--ink-room` |
| E13 | **Carosello del sito di un cliente**, navigabile, incastonato | Speedrun T24 | prova che "funziona anche per chi fa altro" | Preventa/Novacar: il loro sito vero dentro il nostro | nuovo: `vetrina-cliente` |
| E14 | **Recensioni con una a 4 stelle** su 14 | Speedrun T23 | credibilità per imperfezione | testimonial con nome, foto, e una che dice cosa non è andato | esistente da rifare |
| E15 | **Formula aritmetica** + grafico a barre a due colori | Speedrun T26 | persuasione per il lettore analitico | "Produttività = messaggi utili / ore tue" con i nostri numeri | nuovo: `formula` |
| E16 | **Snippet di terze parti riprodotto** (SERP, articolo) | Speedrun T27, T8 | prova esterna verificabile | articolo reale su AI + PMI italiane, screenshot con data | Corsia B semplice |
| E17 | **Checklist pre-CTA** con spunte arancioni + bottone a bagliore `0 0 40px rgba(251,70,4,.3)` | Speedrun T28 | tutta l'offerta in dieci righe prima del sì | "Cosa ottieni se prenoti": **abbiamo già `11b-carte-scoperte`**, va messa prima della CTA finale | esistente da spostare |
| E18 | **Titolo in due strati** (pieno sotto il volto, contorno sopra) | Armageddon T1 | la parola diventa incisione | hero: "Digital Empire" che passa dietro il volto | `hero-due-strati` ✅ esiste |
| E19 | **Cucitura fotografica** fra due sezioni (stesso gradiente, due superfici) | Armageddon T2 | una foto attraversa il confine senza linea | **sostituisce i nostri 16 divider** dove c'è una foto | `cucitura-fotografica` ✅ esiste |
| E20 | **Parallax a 4 velocità**, sui figli non sui contenitori, `rAF` + `passive` | Armageddon T1 | profondità senza libreria | hero e stanza Chi siamo, con `prefers-reduced-motion` (§7) | scheda in `hero-due-strati` |
| E21 | **Testata-targa**: un link solo, disegnato come parte dell'oggetto | Armageddon T1 | su una pagina di lancio la nav è attrito | NO per la home (ci serve la nav); SÌ per la pagina-ponte dell'outreach | `testata-targa` ✅ esiste |
| E22 | **FAQ native `<details>`**, `+` che diventa `–`, allineate a sinistra "perché si leggono" | Armageddon T5 | funziona senza JS | sostituisce `faq-accordion.tsx` | `faq-native` ✅ esiste |
| E23 | **Disclaimer a 88ch** più largo delle risposte a 64ch + firma legale con P.IVA | Armageddon T6, Speedrun T30 | il legale si legge davvero | **il nostro footer va verificato: P.IVA e indirizzo presenti?** | `coda-legale` ✅ esiste |

**Regola di composizione presa da lui (SINTESI-VISIVO §2-3):** *un guscio, un accento*. Fondo, testo,
secondo tono **non cambiano mai**; il colore vive su CTA, cerchi numerati, una fascia. I nostri 48
sfondi diventano **3** (`ink`, `paper`, `ink-room`) + la fascia-lampo.

## Asse C — LE IMMAGINI AURA + IL COPY CHE LE ACCOMPAGNA

**Cosa c'è nella cartella** (`Caroselli Style/immagini AURA/`, 41 file + `Stile/` con 3 esempi
applicati): still cinematografici scuri, luce di taglio, un volto — Peaky Blinders, Oppenheimer, Tony
Stark, American Psycho, Interstellar, Tyson, Ali, Wolf of Wall Street, Kingdom of Heaven, Sauron,
templari. **Lo stile AURA** (da `Stile/Max_a_Allora_questo_è_il_m.png`): still + grana pesante + **una
riga bianca sottile sopra il volto**. È esattamente il registro delle sue foto (templare con ascia,
cavaliere sfocato, scheletro con spada): **stessa famiglia visiva, e noi ne abbiamo 41 pronte**.

**⚠️ Il fatto che va detto prima del casting.** Sono fotogrammi di film e volti di attori/atleti
reali. Su un carosello Instagram passano; **sul sito pubblico di un'agenzia che fattura** sono
un'esposizione legale (diritto d'autore dello studio + diritto d'immagine della persona), e Pascu non
lo fa: le sue foto sono templari/scheletri generati o meme anonimi, il volto vero è **il suo**.
Decisione (mia, dichiarata, Max può ribaltarla): **due corsie, stesso piano, cambia solo il file.**

- **Corsia I — AURA originali.** Si usano **solo in staging/preview** e per validare la composizione.
  Mai in un deploy pubblico.
- **Corsia II — AURA nostre.** Ogni still originale diventa il **brief** di un'immagine generata nello
  stesso registro (Higgsfield, già valutato in `documentazione Empire/` dossier 28: da comprare Plus
  mensile): stessa luce, stesso taglio, stesso mood, volto non riconducibile. Più **due categorie che
  valgono più di qualunque still**: le **facce vere** del team (Pascu insegna: sopra i 349 € servono
  facce) e gli **screenshot reali dei nostri sistemi** (la dashboard, il log dei 300 messaggi, la
  cartella Drive coi caroselli).

**Il manifest è la chiave dello swap**: `agency-empire/public/aura/manifest.json` con una riga per
immagine (`id`, `sezione`, `ruolo`, `alt`, `didascalia`, `sorgente: originale|generata|team|screenshot`,
`brief_generazione`). Cambiare corsia = cambiare un file, non un componente.

**Regole d'uso (per non diventare una pagina di meme):**
1. **Densità ≤ 0,6 foto ogni 1.000 px** (il gate della sintesi visiva mette WARN sopra 5,0; il nostro
   target è dieci volte sotto: siamo un'agenzia, non un negozio).
2. **Mai una foto muta.** Ogni immagine porta la sua riga di copy (la riga bianca dello stile AURA) e
   un `alt` descrittivo — il contrario del suo difetto delle 42 immagini con `alt=""`.
3. **Mai due foto consecutive** senza una sezione di testo in mezzo.
4. **La foto argomenta, non decora.** Se togliendola il paragrafo regge uguale, non ci va.
5. **14 immagini in pagina, non 41.** Le altre restano in riserva nel manifest.

### Il casting — 14 posti, 14 immagini, 14 righe

Numeri = ordine nel foglio-contatti (`aura_sheet.jpg`, in ordine alfabetico di nome file).

| Posto | Sezione (nuova numerazione, Parte III) | Immagine AURA | Perché questa | La riga bianca sopra (copy) |
|---|---|---|---|---|
| 1 | **N1 Hero** — colonna sinistra | **02** Oppenheimer, cappello, sguardo dritto | chi ha costruito la macchina; è il ruolo che Max rivendica | «Ho costruito il primo sistema per me. Poi ho smesso di venderlo come "tool".» |
| 2 | **N2 Problema** — specchio | **22** Stark, mano sul viso | il momento in cui capisci che lo facevi a mano | «Ogni mattina. Trenta DM. A mano. Da tre anni.» |
| 3 | **N4 Servizi** — Outreach | **14** Stark in armatura che mangia una ciambella | il sistema lavora mentre tu fai colazione | «Alle 7:40 ha già mandato 300 messaggi. Tu stai facendo colazione.» |
| 4 | **N4 Servizi** — Content | **21** Stark occhiali, al lavoro | il costruttore che fa girare la fabbrica | «Un argomento entra. Carosello, reel, caption escono. Senza toccare niente.» |
| 5 | **N6 Fascia-lampo competitor** | **16** silhouette in controluce, senza volto | il competitor che non vedi | «Non ha un nome. Ha un sistema. E ha i tuoi clienti.» |
| 6 | **N6b Asse posizionale** | **15** DiCaprio nella folla | tutti uguali, uno esce dalla fila | «Stessi limiti tuoi. Il primo che li risolve non lo raggiungi più.» |
| 7 | **N8 ASCOLTA BENE** | **30** Ali sopra Liston | il KO: chi ha automatizzato per primo | «Non è più forte. È arrivato prima.» |
| 8 | **N9 Formula / produttività** | **01** Breaking Bad, soldi nell'asciugatrice | i canoni mensili che girano a vuoto | «Dodici canoni all'anno per un tool che non sa chi sei.» |
| 9 | **N10 Processo — fase 4 "gira da solo"** | **35** Stark, bicchiere, fine giornata | il momento dopo: il sistema gira, tu no | «Il giorno dopo il go-live: 30 giorni di monitoraggio nostri. Le serate tue.» |
| 10 | **N11 Chi siamo — stanza a parte** | **nessuna AURA: foto vere di Max e Gael** | qui servono facce, non film | «Parli con chi ha le mani sui workflow. Per scelta, non per limite.» |
| 11 | **N12 Per chi / non per chi** | **36** Bale, mani giunte, ufficio | il titolare che decide, seduto | «Se vuoi delegare *senza capire*, non siamo noi. Sul serio.» |
| 12 | **N14 Garanzia** | **25** elmo da cavaliere, visiera | la protezione che si vede | «Se il sistema non gira come scritto, lo rifacciamo. Non "ti richiamiamo".» |
| 13 | **N15 Obiezioni — "No."** | **29** Stark, segno di pace dall'auto | l'agenzia progettata per essere licenziata | «Ci licenzi quando vuoi. Il codice resta tuo. Ciao.» |
| 14 | **N18 CTA finale** — filigrana | **oggetto-icona: la dashboard vera** in controluce (E10) | il prodotto richiamato, non ridescritto | «In chiamata la vedi girare. Cinque minuti. Niente slide.» |

**Riserva** (nel manifest, non in pagina): 00, 04, 05, 07, 09, 11, 18, 19, 26, 28, 31, 33, 38, 39 —
per la pagina-ponte dell'outreach, i caroselli, le A/B future. **Scartate per il sito** (troppo
"villain" per un'agenzia B2B): 12, 20, 27, 34 (occhi rossi, Sauron).

## Asse D — IL LOOK: la direzione estetica, tavola per tavola

**Si vede prima di leggersi:** [Tavola Estetica Agency Vivo](https://claude.ai/code/artifact/f3fc31e1-b258-4be6-8074-341c021781c9)
(copia locale: `agency-empire/cantiere/aura-preview/tavola-estetica-agency.html`, fuori da git — decisione C2.2).
Dieci tavole (Tavola 0 = la grana) composte con le foto vere della cartella AURA dentro il canone. Quello che segue è la stessa
direzione scritta, perché lo scagnozzo di F4 riceve parole e numeri, non un link.

**Il guscio (non cambia mai):** inchiostro `#0d0d0d` · carta `#faf6ee` · stanza `#202021` (una volta) ·
argento `#d9d4e1` per il testo secondario · azione `#fb4604` su bottoni, «No.», numeri e **una** fascia.
Onest 900 per i titoli, Playfair corsivo per la mezza riga che gira il senso, JetBrains Mono per etichette
e misure. Grana a 4 strati nostra, resta. Marquee metallico resta, arancione al 10% della lunghezza.

**Il trattamento delle foto — quattro modi, due ammessi:**

| Sigla | Nome | Ricetta | Dove |
|---|---|---|---|
| A | originale | — | **mai**: la palette del film non è nostra |
| **B** | **AURA** | `saturate(.78) contrast(1.08) brightness(.9)` + vignetta radiale verso l'inchiostro + grana `feTurbulence 1.1` overlay 55% + **riga bianca** Onest 400 a ~46% dell'altezza (o in basso se il volto è alto), ombra `0 1px 14px rgba(0,0,0,.9)`. Su carta: saturazione `.6`, la foto resta un blocco d'inchiostro | i 12 volti |
| C | duotone | inchiostro → arancione | **solo** dentro la fascia N6, se serve una foto |
| **D** | **filigrana** | grigio, `opacity .16`, `contrast(1.3)`, sotto al testo | i 2 richiami dell'oggetto-icona (dashboard) |

**LA GRANA — legge di Max, non opzione (2026-09-11: «la mia cosa preferita, non dimenticarla mai, in tutto,
anche nelle sfumature»).** Tre livelli, tutti obbligatori: (1) i **4 strati fissi** di `globals.css` (overlay
.55/240px, hard-light .30/180px, fibra .18/400×800) — non si toccano; (2) **grana locale su ogni superficie
composta** — ogni gradiente, fascia, stanza, cucitura, chiusura porta la propria grana in overlay + soft-light
nello stesso stack o in uno pseudo-elemento sopra: la fissa da sola su una sfumatura si perde; (3) **grana dentro
il trattamento B** delle foto (feTurbulence 1.1, overlay 55%). Carta = due grane in multiply (1.45 / 0.72) sotto
il gradiente. Arancione pieno = grana 0.72 in multiply. **Gate F5:** nessun `background` con gradiente senza un
`feTurbulence` nello stesso stack o sopra → FAIL. Entra in `gate_siti.py`.

**LA RIGA SI LEGGE SEMPRE — legge di Max (2026-09-11: «le scritte si devono vedere per sempre perfettamente»).**
Ogni testo sopra una foto poggia su **una banda scura** (`rgba(0,0,0,.86)` al centro, sfumata sopra e sotto,
`backdrop-filter: blur(3px)`), Onest 600, tripla ombra (`0 1px 2px #000, 0 2px 6px, 0 0 24px`), e sotto ogni
foto la parte bassa scende verso il nero (`.78`). La grana locale sopra il testo resta leggera (overlay ≤ .5)
per non spegnerlo. **Gate F5:** contrasto misurato ≥ 7:1 su ogni riga, altrimenti la foto si taglia o si
scurisce — mai si accetta.

**La foto non ha mai un bordo.** Finisce nel fondo con un gradiente (hero: `55%→100%` a destra e in
basso) oppure attraversa due sezioni con la cucitura (`--consegna .992`, `--coda .71`). I 16 divider di
oggi spariscono tutti.

**Tavola per tavola (le misure che lo scagnozzo deve rispettare):**

| Tav. | Sezione | Foto · trattamento | Composizione | Testo |
|---|---|---|---|---|
| 2 | N1 hero | posto 1 · B + dissolvenza; in produzione **ritratto di Max** con la stessa luce | 46/54; "EMPIRE" pieno sotto il volto, contorno sopra (`hero-due-strati`); parallax .155/.09, spento con reduced-motion; **≤ 30 parole sopra il fold, zero bottoni** | H1 provoca, riga sotto paga con 3 numeri |
| 3 | N2 specchio | posto 2 · B su carta (`.6`) · quadrata 300 px a sinistra | il DM vero in bolla bianca (pattern `specchio`), etichetta mono, riga in corsivo con i numeri | «Ti voglio bene, ma lo stai facendo a mano.» |
| 4 | N4 fabbriche | posto 3 · una sola `--foto` sotto due sezioni (offset 20% / 55%) | cucitura fotografica; **la dashboard vera** si posa sul bordo (`oggetto-che-si-posa`, margine negativo) | il numero nel titolo (300); sei parole sulla foto |
| 5 | N6 fascia + asse | posto 5 · grigio 40%, contrasto alto; posto 6 sull'asse | fascia 431 px **unico fondo arancione**, filetto bianco a sinistra del corpo; asse a 3 nodi, "TU" cerchiato, nodo arancione a destra | definizione secca del competitor; sull'asse zero aggettivi |
| 6 | N8 ascolta bene | posto 7 · B, riga bassa (9%) | casella arancione col titolo dentro = tipografia-manifesto fuori gerarchia; 3 celle di prova, numeri tabellari | negazione ×3 → una; «fai tu la divisione» |
| 7 | N11 chi siamo | **nessuna AURA**: ritratti veri di Max e Gael, trattamento B | fondo `#202021` una volta sola; due riquadri 4:5; finché mancano i ritratti: silhouette con nome | l'interesse dichiarato (V6) |
| 8 | N14 garanzia · N15 obiezioni | posto 12 · su carta, `.5` quasi acciaio; posto 13 · B su inchiostro | garanzia 50/50; obiezioni in `<dl>` con filetti, domanda fra virgolette, «No.» arancione unico accento | «No. Fai tu il conto» |
| 9 | N18 chiusura | nessuna foto: **dashboard in filigrana** (D) tagliata dal bordo basso | fondo `#050505`; **unica sezione centrata** (va guardata, non letta); bottone con bagliore `0 0 40px rgba(251,70,4,.3)` | il costo del no: «cinque minuti e un caffè» |

**Cinque regole misurabili** (già in Asse C, qui con i numeri del cantiere): ≤ 0,6 foto/1.000 px (14 su
~28.000 = 0,5) · mai una foto muta (riga + `alt`) · mai due foto di fila · la foto argomenta o non entra ·
un guscio, un accento.


---

# PARTE III — LA NUOVA STRUTTURA: da 21 sezioni + 16 divider a 19 sezioni cucite

La sua formula a 11 tappe (hero → agitazione → prova con fonte → metodo → benefici → curriculum →
qualificazione negativa → obiezioni → autorevolezza → prezzo → FAQ) adattata a una pagina che vende
**una chiamata**, non un corso. Le fusioni riducono altezza e ripetizioni; l'ordine segue la
temperatura: prima specchio e agitazione, poi prova, poi metodo, poi chi siamo, poi il sì.

| N | Sezione nuova | Da (file attuali) | Elemento vivo (Parte II) | Foto | CTA |
|---|---|---|---|---|---|
| N1 | **Hero a due colonne** — volto + H1 nella voce nuova, marquee metallico sopra (nostro, resta) | `01-hero` | E1, E18, E20 | 02 | 1 (sotto il fold) |
| N2 | **Specchio** — "Ti voglio bene, ma…" + il DM vero copia-incolla | `04-problema` (metà) | E4 | 22 | — |
| N3 | **Stats** — 3 numeri, ognuno con la sua prova cliccabile | `02-stats` | E16 | — | — |
| N4 | **Due fabbriche** — Outreach / Content, con screenshot veri e l'oggetto-icona intero | `03-servizi` + `07-funnel-viz` | E10 | 14, 21 | 1 |
| N5 | **Vetrina cliente** — Preventa/Novacar: il loro sito dentro il nostro + numeri | `03b-preventa` + `09b-prove-novacar` + `09-portfolio` | E13 | — | 1 |
| N6 | **Fascia-lampo** "Hai competitor e non lo sai" (431 px, fondo pieno) → **asse posizionale** | `04-problema` (metà competitor) | E3, E9 | 16, 15 | — |
| N7 | **Diagnosi** — 4 segnali + micro-sondaggio "ti ritrovi?" | `05-diagnosi-cro` | E5, E7 | — | 1 |
| N8 | **ASCOLTA BENE.** — casella arancione + la prova | `05b-ascolta-bene` | E6 | 30 | 1 |
| N9 | **La formula** — produttività = messaggi utili / ore tue, barre a due colori, ORA/CON | `06-metodo-apsoc` (parte) | E15, E8 | 01 | — |
| N10 | **Il processo** — 4 fasi con numeri in filigrana + lo stack in una riga | `08-processo` + `17-stack` | E11 | 35 | 1 |
| N11 | **Chi siamo** — stanza a parte `#202021`, facce vere, l'interesse dichiarato (V6) | `16-chi-siamo` | E12 | team | — |
| N12 | **Per chi / non per chi** — qualificazione negativa secca | `10-per-chi` | — | 36 | 1 |
| N13 | **Cosa dicono** — testimonial con nome/foto, una imperfetta | `11-testimonial` | E14 | — | — |
| N14 | **Garanzia** — una frase, una condizione, zero asterischi | `12-garanzia` | — | 25 | 1 |
| N15 | **Obiezioni** — sei "No." con il conto delegato | `15-objections` | V4 | 29 | — |
| N16 | **Cosa ottieni se prenoti** — checklist + bottone a bagliore | `11b-carte-scoperte` (spostata qui) | E17 | — | **1 (principale)** |
| N17 | **FAQ** native `<details>` | `13-faq` | E22 | — | — |
| N18 | **CTA finale + form** — dashboard in filigrana dietro | `14-cta-finale` | E10 (richiamo) | dashboard | 1 |
| N19 | **Disclaimer + coda legale** (P.IVA, indirizzo, privacy) | footer | E23 | — | — |

**Divider:** i 16 `divider-silver-navy` spariscono. Dove c'è una foto → `cucitura-fotografica` (E19).
Dove non c'è → alternanza piatta `ink`/`paper` con `section-border-t` del canone. Il `metodo-apsoc`
come sezione a sé **si fonde** in N9 (il metodo si mostra con la formula, non si spiega).

**Obiettivi numerici del dopo** (si misurano con lo stesso `site_capture.py`, tabella di Parte I rifatta):

| Misura | Oggi | Obiettivo | Perché quel numero |
|---|---|---|---|
| Altezza desktop | 43.359 | **≤ 28.000 px** | sotto la sua Speedrun (33.756), sopra apsales (12.565): pagina calda ma per una chiamata |
| CTA | 11 (1/3.940 px) | **18-20 (1 ogni ~1.400 px)** | la sua media è 1/1.100 su prodotti a prezzo; per una call B2B si allarga del 25% |
| Fotografie | 0 | **14** (0,5/1.000 px) | Parte II-C regola 1 |
| Dimensioni tipografiche | 195 | **≤ 12** | la scala del canone, §1 |
| Sfondi | 48 | **3 + fascia** | un guscio, un accento |
| Accento come sfondo | ovunque | **1 sezione** (N6) | §12 |
| H1 | 1 | 1 (+ manifesto fuori gerarchia) | SEO pulita, effetto suo |
| Lighthouse a11y / perf mobile | da misurare in F0 | **≥ 95 / ≥ 85** | — |
| Link che risolvono 200 | da misurare | **100%** (controllo 8 ANATOMIA) | il suo difetto n.1 |

---

# PARTE IV — LE FASI (ciclo a 9 passi, ADR-006) — P0

| Fase | Cosa | Uscita su disco | Gate (comando + condizione) | Forze | Ore |
|---|---|---|---|---|---|
| **F0 RECALL+SPEC** | Baseline misurata (rifare `site_capture.py` sul live), `BRIEF.md` con corsia B motivata, estrazione `COPY-ATTUALE.md`, manifest immagini 41/41, verifica P.IVA nel footer | `agency-empire/cantiere/BRIEF.md`, `COPY-ATTUALE.md`, `public/aura/manifest.json` | manifest 41 righe, ogni riga con `alt` e `sorgente`; Lighthouse baseline salvata | Emperator | 3 |
| **F1 VOCE** (§3: il copy prima del layout) | `COPY-V2.md` **intero**, 19 sezioni nella voce nuova (V1-V10), 14 didascalie, 6 "No.", una formula, una negazione×3 | `agency-empire/cantiere/COPY-V2.md` | `cro-copy-architect` APSOC ≥ 80; `sentinel-brandvoice` PASS; `gate_voce.py` (nuovo): lista nera = 0, ogni frase con "?" o "No." ha un numero entro 200 caratteri, prima persona ≥ 1 per sezione | 1 scagnozzo sonnet (bozza) + Emperator (riscrittura) + `apex-critic` | 8 |
| **F2 IMMAGINI** | `aura_prep.py` (nuovo): resize 1600w, WebP q80, grana, crop 3:4 e 16:9, `alt` dal manifest; Corsia II: 14 brief di generazione + facce team + 6 screenshot reali dei sistemi | `public/aura/*.webp`, `scripts/aura_prep.py`, `manifest.json` aggiornato | ogni file ≤ 250 KB; `alt ≠ ""` 14/14; nessun file `sorgente: originale` in `public/` al deploy | Emperator + Max (foto team, acquisto Higgsfield) | 6 |
| **F3 PATTERN** | 8 pattern nuovi scritti **prima in vanilla** nella Fabbrica (`fascia-lampo`, `specchio`, `micro-sondaggio`, `ora-con`, `asse-posizionale`, `vetrina-cliente`, `formula`, `tipografia-manifesto`), poi avvolti in componenti Corsia B; 5 esistenti avvolti (`hero-due-strati`, `cucitura-fotografica`, `oggetto-che-si-posa`, `faq-native`, `coda-legale`) | `.claude/skills/fabbrica-siti/pattern/<nome>/{pattern.html,scheda.md}` + `agency-empire/src/components/pattern/*.tsx` | `gate_siti.py` PASS su ogni `pattern.html`; `galleria.py` rigenerata; `prefers-reduced-motion` spegne CSS **e** JS (§7) | 2 scagnozzi sonnet (4 pattern ciascuno) + 1 sentinella opus (review) | 10 |
| **F4 BUILD** | Le 19 sezioni, nell'ordine nuovo, su `COPY-V2.md`; `globals.css` ridotto al canone (3 sfondi, scala ≤ 12); i 16 divider tolti | `src/sections/N01…N19.tsx`, `src/app/page.tsx`, `globals.css` | build verde; per sezione: scala tipografica dal canone, nessun hex fuori canone (`canone_sync.py`), `alt` presente, CTA ogni ≤ 1.500 px | 3 scagnozzi sonnet su aree disgiunte (N1-N6 · N7-N13 · N14-N19) **solo sui file di sezione**; `globals.css`/`page.tsx`/canone **solo Emperator** | 18 |
| **F5 GATE + REVIEW** | `gate_siti.py` sull'export; `site_capture.py` sul preview → tabella Parte I rifatta; review indipendente | `cantiere/MISURA-DOPO.md` | tutti gli obiettivi numerici di Parte III raggiunti o deroga scritta con articolo | `apex-critic` + `guild-design` | 3 |
| **F6 TEST** | mobile 390 px, Lighthouse, ogni `href` → 200 (controllo 8), form `/prenota` invia davvero, `reduced-motion` a mano | `cantiere/TEST.md` | a11y ≥ 95, perf ≥ 85, 0 link rotti, 1 invio di prova ricevuto | `site-qa-mobile`, `site-qa-accessibility`, `site-qa-performance` | 3 |
| **F7 COMMIT + DEPLOY** | commit per fase; deploy Vercel sullo stesso URL; ULTIMO METRO (ADR-016): senza URL vivo il cantiere resta aperto | git, `agency-empire-kohl.vercel.app` | `curl` 200 sul live; screenshot del live salvato | Emperator | 1 |
| **F8 RETRO** | `LEZIONE.md`, pattern promossi, wiki, checkpoint, `gate_voce.py` entra nella Fabbrica per tutti i siti | `cantieri/agency-empire-vivo/LEZIONE.md`, wiki, CP | riga in `cantieri/INDICE.md` | Emperator | 2 |
| | | | | **Totale P0** | **54 h** |

---

# CRITICA 1 → P1 (attacca P0)

**C1.1 — P0 copia gli elementi senza chiedersi da dove arriva il traffico.** La sintesi visiva §5 dice
che *la forma la decide la temperatura, non il prezzo*: freddo → una decisione, < 2.000 px; caldo →
lungo. Il nostro traffico arriva da **due porte diverse**: chi cerca l'agenzia (caldo, legge) e chi
clicca dal link in un DM/email di outreach (freddo, decide in 30 secondi). P0 costruisce **una** pagina
per tutti e due. **Correzione:** si aggiunge **N0 — pagina-ponte** (`/ponte` o `/da-outreach`): 1.593
px, 36 blocchi, un video o un'immagine, **una** decisione (pattern `pagina-ponte` ✅ esiste già, con
`testata-targa` E21). Costo: 2 h, ma **dopo** la home (F7.5), non insieme.

**C1.2 — P0 non misura un solo clic.** B-043: Digital Empire non misura un euro. Rifare il sito senza
un evento sul bottone significa non sapere mai se la voce nuova converte più della vecchia.
**Correzione:** in F0 si accendono Vercel Web Analytics (gratis, zero cookie banner, coerente con la
lezione `dnt=1` di Armageddon) + 2 eventi custom: `cta_click` (con `data-sezione`) e `form_submit`.
Tre settimane di baseline sul vecchio **mentre** si costruisce il nuovo. Costo: 1 h.

**C1.3 — "1 CTA ogni 1.400 px" è preso dal suo numero, non dal nostro caso.** Lui vende un prodotto a
249 € a un lettore che si è già scaldato per 30.000 px; noi vendiamo una chiamata gratuita a un
titolare B2B. Troppe CTA su B2B = insistenza, non ritmo. **Correzione:** la cadenza si lega alla
**temperatura della sezione**, non ai pixel: CTA dopo ogni sezione che *chiude un argomento* (N1, N4,
N5, N7, N8, N10, N12, N14, N16, N18) = **10 CTA**, una ogni ~2.800 px. Meno della metà di P0, il
doppio di oggi. Si misura con C1.2 e si corregge sui dati, non sul gusto.

**C1.4 — La lista nera è dichiarata ma non è un gate.** V10 dice "gate meccanico in F1" e poi F1 lo
chiama `gate_voce.py` senza dire cosa controlla. **Correzione:** `gate_voce.py` controlla quattro
cose, tutte deterministiche: (1) zero parole della lista nera; (2) per ogni frase che finisce con `?`
o che è esattamente `No.`, entro 200 caratteri successivi c'è una cifra o un `%` o un `€`; (3) almeno
un pronome di prima persona (`io|ho|noi|abbiamo|ci`) per sezione; (4) zero frasi dalla lista Barnum
del `sentinel-brandvoice`. Exit 0/1. Entra nella Fabbrica, non solo in questo cantiere.

**C1.5 — 41 immagini nel manifest ma "facce vere" e "screenshot" dipendono da Max.** Le foto del team
e l'acquisto Higgsfield sono gesti di Max. **ADR-028: non bloccano.** Si costruisce tutto con la
Corsia I in preview; le 14 posizioni sono cablate nel manifest; quando arrivano i file veri si
sostituiscono **senza toccare un componente**. La sezione N11 (Chi siamo) in assenza di foto usa il
pattern "silhouette + nome" — mai uno still di attore al posto di una faccia del team.

**P1 = P0 + N0 ponte (dopo) + analytics in F0 + 10 CTA a temperatura + gate_voce.py definito + swap
immagini senza dipendenze. Ore: 54 + 3 = 57.**

---

# CRITICA 2 → P2 (attacca P1)

**C2.1 — P1 aggiunge la pagina-ponte e l'analytics ma non dice chi manda traffico alla ponte.** Una
ponte senza il link nei messaggi dell'outreach è la ventiseiesima cosa finita mai usata (ADR-016).
**Correzione:** N0 esce **solo insieme** alla modifica di una riga nella Bibbia dei Messaggi
(`Outreach Workflow/`): il link nel DM/email punta a `/ponte`, non alla home. È un file, è una riga, e
va nel gate di F7.5: "ponte deployata **e** linkata da almeno un template vivo". Altrimenti non si
costruisce.

**C2.2 — P1 tiene la Corsia I "in preview" ma la preview Vercel è pubblica per URL.** Un deploy di
preview con still di film è comunque un file servito da un dominio nostro. **Correzione:** le
immagini `sorgente: originale` **non entrano mai in `public/`**: `aura_prep.py` le scrive in
`cantiere/aura-preview/` (gitignored) e le serve solo dal dev server locale (`next dev`). In
`public/aura/` entrano solo `generata|team|screenshot`. Il gate di F2 diventa: `ls public/aura` ∩
`manifest[sorgente=originale]` = ∅.

**C2.3 — Tre scagnozzi in parallelo su 19 sezioni con un `COPY-V2.md` solo = tre interpretazioni
della voce.** Il rischio non è il codice, è che N3 e N15 sembrino scritti da due persone.
**Correzione:** F1 produce anche `VOCE.md` (una pagina: le 10 regole + 8 esempi prima/dopo presi da
`COPY-V2.md`), e ogni prompt di scagnozzo la riceve **per intero e idempotente**. In F5 la review
indipendente legge le 19 sezioni **di fila** con una sola domanda: "è una voce sola?".

**C2.4 — Le ore sono ottimiste sul copy.** 19 sezioni + 14 didascalie + 6 obiezioni + FAQ nella voce
nuova, con APSOC ≥ 80 e tre gate, in 8 ore: no. Lo studio del Libro Agency ha insegnato che "denso"
costa (feedback 2026-09-10). **Correzione:** F1 = **12 h**, e si spacca in F1a (sezioni N1-N9, la
metà che vende) e F1b (N10-N19): F3/F4 possono partire su F1a mentre F1b si scrive. Budget-guard
(ADR-006): a < 20% risorse di sessione si chiude con COMMIT, non si apre la sezione dopo.

**C2.5 — La fascia-lampo arancione (N6) è la sola sezione a fondo pieno — ma il marquee metallico
dell'hero contiene già `#fb4604` al 90%.** Due "accensioni" a schermo pieno nella stessa pagina
diluiscono §12. **Correzione:** il marquee resta (è nostro, Max lo vuole) ma l'arancione dentro il
gradiente scende al **10%** della lunghezza (era il punto 50% con alpha .90 su una fascia intera) —
esattamente la regola CCM "colore dell'azione < 10%". La fascia N6 resta l'unico fondo pieno.

**P2 = P1 + ponte legata alla Bibbia + originali mai in `public/` + `VOCE.md` in ogni prompt + F1 in
due metà a 12 h + marquee al 10%. Ore: 57 + 4 = 61.**

---

# CRITICA 3 → P3 (attacca P2)

**C3.1 — P2 ha ancora una dipendenza silenziosa: `globals.css` da 195 dimensioni a 12 mentre tre
scagnozzi scrivono sezioni che usano le classi di oggi.** Se il canone cambia sotto i piedi, F4 si
rompe a metà. **Correzione:** F3 chiude con `globals.css` **già ridotto e congelato** (commit
dedicato, tag `canone-v3`), e F4 parte solo dopo quel commit. Gli scagnozzi ricevono la lista delle
utility ammesse (`canone.json`) nel prompt. Nessuno aggiunge una classe: se manca, la chiede a
Emperator, che la mette **nel canone** (§1).

**C3.2 — "Una a 4 stelle" (E14) presuppone testimonial che oggi non abbiamo in numero.** Pascu ne ha
14 verificate; noi abbiamo Preventa/Novacar e poco altro con nome. Inventarne una imperfetta sarebbe
la sua debolezza n.2 (screenshot muti). **Correzione:** N13 esce con **quelle vere che abbiamo, con
nome e faccia**, anche se sono due; il resto della sezione è il **caso** (numeri di Novacar) e il
link alla vetrina N5. L'imperfezione dichiarata non è una stella in meno finta: è la riga "cosa non
è andato al primo giro" scritta da noi sul caso reale (V8, zero Barnum). Quando ci saranno ≥ 6
testimonial, si applica E14 come da lui.

**C3.3 — Il piano misura l'altezza ma non il tempo di lettura della prima schermata.** L'hero a due
colonne (E1) di Pascu ha **18 parole e zero CTA**. Il nostro H1 attuale + sottotitolo sono 78 parole.
Se la voce nuova aggiunge "Ti voglio bene, ma…" sopra il fold, l'hero esplode. **Correzione:** gate
di F1 per N1: **≤ 30 parole visibili sopra il fold a 1440×900**, una CTA sotto il fold; lo specchio
"ti voglio bene" sta in N2, non in N1.

**C3.4 — Il casting mette Oppenheimer nell'hero (posto 1) anche in Corsia II.** La foto dell'hero è
l'unica che il visitatore vede al 100%: se è generata "nello stile di" un attore riconoscibile, è la
posizione a rischio più alto. **Correzione:** in Corsia II il posto 1 **è Max** (ritratto vero,
trattamento AURA: luce di taglio, grana, riga bianca), esattamente come il volto nell'hero di
Armageddon è quello di Andrei. Oppenheimer resta il brief di **luce e taglio**, non di volto. Il
resto del casting non cambia.

**C3.5 — Il totale ore è un numero senza margine.** 61 h di P2 non contengono il ricambio (una
sezione bocciata in review, un pattern che non passa il gate). **Correzione:** +15% = **70 h**, e
il numero si dichiara come stima, non promessa; il battito di ogni sessione riporta la percentuale
**calcolata sul disco** (sezioni con gate PASS / 19, pesate: F1 30%, F3 15%, F4 35%, F5-F8 20%).

**P3 = P2 + canone congelato prima di F4 + testimonial veri e pochi + hero ≤ 30 parole + posto 1 = Max
+ 70 h con pesi dichiarati.**

---

# V4 ESECUTIVO — quello che si esegue, nell'ordine, con i comandi

**Pre-condizione unica:** ordine di Max «vai» + blocco ⚠️ COORDINAMENTO in `STATO-EMPIRE.md` + push.

| # | Fase | Comandi / file esatti | Gate (condizione → exit) | Forze (ADR-015) | Ore | Peso % |
|---|---|---|---|---|---|---|
| 0 | **F0 Baseline** | `python "competitor/Andrei Pascu/site-study/scripts/site_capture.py" https://agency-empire-kohl.vercel.app --slug 61-agency-baseline` · `npx @vercel/analytics` + eventi `cta_click`,`form_submit` in `src/components/magnetic-button.tsx` e `src/app/prenota/page.tsx` · `agency-empire/cantiere/BRIEF.md` · `public/aura/manifest.json` (41 righe) | manifest 41/41 con `alt`,`sorgente`,`brief_generazione`; baseline salvata; analytics visibile su Vercel → 0 | Emperator | 4 | 5 |
| 1a | **F1a Voce — N1-N9** | `agency-empire/cantiere/VOCE.md` (10 regole + esempi) · `COPY-V2.md` sezioni N1-N9 · `python .claude/skills/fabbrica-siti/scripts/gate_voce.py cantiere/COPY-V2.md` | gate_voce exit 0; APSOC ≥ 80 (`cro-copy-architect`); `sentinel-brandvoice` PASS; N1 ≤ 30 parole sopra il fold | 1 scagnozzo sonnet (bozza) → Emperator riscrive → `apex-critic` | 7 | 15 |
| 1b | **F1b Voce — N10-N19 + ponte N0** | idem su N10-N19 + `COPY-PONTE.md` (≤ 90 parole, una decisione) | idem | idem | 5 | 15 |
| 2 | **F2 Immagini** | `python agency-empire/scripts/aura_prep.py --manifest public/aura/manifest.json --preview cantiere/aura-preview --out public/aura` · brief Higgsfield ×13 + ritratto Max + 6 screenshot reali (`Outreach Workflow` dashboard, log invii, Drive caroselli) | `public/aura/` ∩ `sorgente=originale` = ∅; 14 file ≤ 250 KB; `alt` 14/14 | Emperator + Max (ritratto, screenshot, Higgsfield) — **non blocca**: preview locale con Corsia I | 6 | 5 |
| 3 | **F3 Pattern + canone** | 8 pattern nuovi in `.claude/skills/fabbrica-siti/pattern/<nome>/` (prima `pattern.html` vanilla, poi `src/components/pattern/<Nome>.tsx`) · 5 esistenti avvolti · `globals.css` → canone v3 (3 sfondi, scala ≤ 12, marquee arancione ≤ 10%) · `python .claude/skills/fabbrica-siti/scripts/galleria.py` · **commit + tag `canone-v3`** | `gate_siti.py` PASS ×13; `canone_sync.py` 0 hex fuori canone; reduced-motion spegne JS; tag esiste | 2 scagnozzi sonnet (4 pattern ciascuno, prompt con `VOCE.md` + `canone.json` interi) + 1 sentinella opus | 10 | 15 |
| 4 | **F4 Build 19 sezioni** | `src/sections/N01-hero.tsx … N19-coda-legale.tsx` · `src/app/page.tsx` nuovo ordine · divider rimossi · solo classi di `canone.json` | build verde; per sezione: 0 hex fuori canone, `alt` presente, una voce sola (review di fila); 10 CTA nelle sezioni dichiarate | 3 scagnozzi sonnet: N1-N6 · N7-N13 · N14-N19 (**solo file di sezione**); `globals.css`,`page.tsx`,canone: **solo Emperator** | 20 | 25 |
| 5 | **F5 Gate + misura** | `gate_siti.py` sull'`out/` · `site_capture.py http://localhost:3000 --slug 62-agency-dopo` · `cantiere/MISURA-DOPO.md` (tabella Parte I rifatta) | ≤ 28.000 px; 14 foto; ≤ 12 dimensioni; 3 sfondi + 1 fascia; 10 CTA; ogni scarto ha deroga con articolo | `apex-critic` + `guild-design` | 3 | 5 |
| 6 | **F6 Test** | Lighthouse mobile · script `href` → HTTP 200 su tutti i link · invio di prova su `/prenota` · `reduced-motion` a mano | a11y ≥ 95, perf ≥ 85, 0 link rotti, 1 invio ricevuto | `site-qa-mobile`, `site-qa-accessibility`, `site-qa-performance` | 3 | 5 |
| 7 | **F7 Deploy** | commit per fase · `vercel --prod` su `agency-empire-kohl.vercel.app` · `curl -I` 200 · screenshot del live in `cantiere/` | URL vivo con la versione nuova (ADR-016) | Emperator | 1 | 5 |
| 7.5 | **F7.5 Ponte** | `src/app/ponte/page.tsx` (pattern `pagina-ponte` + `testata-targa`) · **una riga** nella Bibbia dei Messaggi → link `/ponte` | ponte 200 **e** linkata da ≥ 1 template vivo dell'outreach, altrimenti non si deploya | Emperator | 3 | 3 |
| 8 | **F8 Retro** | `cantieri/agency-empire-vivo/LEZIONE.md` · riga in `cantieri/INDICE.md` · `gate_voce.py` promosso a gate della Fabbrica per tutti i siti · wiki + CP | LEZIONE esiste; CP coniato con `scripts/checkpoint.py` | Emperator | 2 | 2 |
| | | | | **Totale (con +15%)** | **≈ 70 h** | **100** |

**Politica di guasto (ogni fase):** una sezione che non passa il gate torna allo scagnozzo **una**
volta con il verdetto esatto; alla seconda bocciatura la riscrive Emperator. Un pattern che non passa
`gate_siti.py` non entra in F4: la sezione usa il canone piatto e il pattern va in `BACKLOG.md`
(ADR-005). Nessun guasto ferma le sezioni intorno (ADR-028).

**Cosa dipende da Max (ADR-026, in cima a STATO-EMPIRE quando parte il build):** il ritratto suo per
il posto 1; le foto del team per N11; l'acquisto Higgsfield Plus (dossier 28) per la Corsia II; il
«vai». Nient'altro. Tutto il resto si costruisce senza.

---

# PRE-MORTEM — come fallisce, e il gate che lo impedisce

| # | Modo di fallire | Segnale | Gate che lo ferma |
|---|---|---|---|
| PM1 | Il tono scivola nell'insulto e un concessionario chiude la pagina | parole della lista nera, "tu" accusatorio senza numero | `gate_voce.py` (1)(2) |
| PM2 | Il sito diventa una pagina di meme, non un'agenzia | foto consecutive, foto senza didascalia | regole C-1/2/3, gate F2 `alt` 14/14, review F5 |
| PM3 | Un still di film finisce sul dominio pubblico | file `sorgente: originale` in `public/` | gate F2 ∩ = ∅ |
| PM4 | Tre voci diverse nelle 19 sezioni | review di fila trova cambi di registro | `VOCE.md` in ogni prompt + F5 "è una voce sola?" |
| PM5 | Il canone cambia sotto i piedi del build | classi che spariscono, build rossa | tag `canone-v3` **prima** di F4 |
| PM6 | Sito nuovo, zero dati: non si sa se converte di più | nessun evento | analytics in F0, 3 settimane di baseline |
| PM7 | La ponte è finita e nessun DM la linka | 0 visite su `/ponte` | gate F7.5 "linkata da un template vivo" |
| PM8 | Un'altra sessione (Gael) tocca `agency-empire/` | commit non previsti sul perimetro | blocco ⚠️ COORDINAMENTO prima del «vai» |
| PM9 | Le ore finiscono a metà F4 | budget < 20% | budget-guard: COMMIT della sezione chiusa, la prossima non si apre |

---

# CONSIGLI — cosa nasce da questo studio oltre al sito (le 4 domande obbligatorie)

1. **Manca un agente?** No. Serve **una voce scritta**: `VOCE.md` diventa `.claude/skills/voce-empire/SKILL.md`
   (le 10 regole + le 22 formule di Pascu con placeholder già pronte in `SINTESI-SISTEMA-COPY.md` §2),
   letta da `cro-copy-architect`, `web-copy-writer`, `outreach-message-writer` e da CONOSCENZA-EMPIRE.
2. **Manca una skill?** `gate_voce.py` è **codice**, non skill: entra in `fabbrica-siti/scripts/` accanto a
   `gate_siti.py` e vale per ogni sito e ogni pagina di lancio.
3. **Un flusso da ridisegnare?** Il flusso "immagini per un sito": oggi non esiste. Nasce `aura_prep.py` +
   il manifest come contratto fra copy, immagine e componente. Riusabile per CCM, Preventa, LANCI.
4. **Del codice?** 8 pattern nuovi nella Fabbrica (E2-E5, E8, E9, E13, E15). Il pattern `vetrina-cliente`
   (E13) vale da solo per ogni pagina di case study che faremo.

---

## Connessioni
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` · `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` — la legge che questo cantiere applica
- `competitor/Andrei Pascu/site-study/SINTESI-SISTEMA-COPY.md` · `SINTESI-SISTEMA-VISIVO.md` · `ANATOMIA-DEI-LANCI.md`
- `competitor/Andrei Pascu/site-study/reports/12-claude-speedrun-ATLANTE.md` · `11-armageddon-ATLANTE-VISIVO.md`
- `second-brain-vault/wiki/synthesis/Synthesis_Sistema_Visivo_Andrei_Pascu.md` · `concepts/Concept_CCM_Brand_Guidelines.md`
- `documentazione Empire/` dossier 28 (Higgsfield) — la Corsia II delle immagini
- `company/Memory/decisions/ADR-023` (corsie) · `ADR-024` (canone v2) · `ADR-016` (ultimo metro) · `ADR-028` (niente blocca tutto)
