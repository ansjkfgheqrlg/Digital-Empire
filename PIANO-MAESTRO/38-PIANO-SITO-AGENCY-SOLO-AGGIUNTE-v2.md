---
Type: PROJECT
Status: Active
Tags: #agency #sito #solo-aggiunte #fabbrica-siti #piano #adr-030 #adr-031 #funneloperator
Created: 2026-09-13
Last updated: 2026-09-13 (v2 — riscritto dopo lo studio di funneloperator.it; P5 → C5 → P6 → C6 → P7 → C7 → V4; §I = le 5 decisioni di Max D1-D5; build su «vai»)
---

# DOSSIER 38 v2 — SITO AGENCY, PIANO «SOLO AGGIUNTE» RISCRITTO SU FUNNELOPERATOR.IT
## `agency-empire-landing/` → https://agency-empire-landing.vercel.app · leggi: CLAUDE-SITI §13 (solo aggiungere), §14 (immagine intera), §15 (volto prima, richiesta dopo)

> **Perché una v2.** Max, 13/09, sulla v1 e sulla sua tavola: *«sezioni veramente poche, stile brutto, immagini tagliate e dimensionate
> malissimo, nessuna logica»*. Aveva ragione su tutte e quattro: la v1 aveva 13 aggiunte pensate una per una, senza un ritmo; la
> tavola ingrandiva still di 400-1200 px in bande 21/7 con `object-fit: cover`. Prima di riscrivere, il suo ordine: **studiare
> funneloperator.it da cima a fondo**. Fatto (4 rapporti, 3.174 righe, `competitor/Andrei Pascu/site-study/reports/66-funneloperator-*.md`
> + sintesi con le strategie classificate `66-funneloperator-SINTESI-STRATEGIE.md`), ufficializzato (ADR-031 → §14, §15; 14 pattern
> candidati; B-083…B-088). **Questa v2 è costruita sulle strategie FO-\*, non sul gusto.** La v1 resta come storia
> (`38-PIANO-SITO-AGENCY-SOLO-AGGIUNTE.md`); §0, §1 e §7-§8 della v1 restano validi e non si ripetono.
>
> Cinque giri: **P5** (catalogo nuovo) → C5 → **P6** → C6 → **P7** → C7 → **V4 esecutivo**. Tavola Estetica v2 e artefatto del piano
> rifatti con le immagini **intere, al pixel nativo**. Nessuna riga di codice prima del «vai».

---

# §A — COSA HA INSEGNATO FUNNELOPERATOR.IT AL NOSTRO SITO (la diagnosi che regge il piano)

| Misura | funneloperator.it | agency-empire-landing (live) | Conseguenza per le aggiunte |
|---|---|---|---|
| Primo volto | y=2.793 (**8,5%**) | **mai** | **V0 «La firma»** subito sotto l'hero (§15: ≤ 10%) |
| Prima prova numerica | rail a y=3.156 (9,6%) | numeri finti «99,7%» in `science-stats` | **rail dei 4 fatti veri** subito dopo la firma |
| Prima CTA di vendita | y=20.998 (**64%**) | y=800 (2%) e altre 9 | nessuna CTA di vendita **nuova** sopra il 50%; **una CTA fissa** che sparisce (FO-S02) |
| Storia personale | 4 sezioni, 14% della pagina, **7 foto di lavoro** | 4 h2 in prima persona, **0 foto** | **stanza dei 3 volti + dietro-le-quinte** (6 foto vere) |
| Prove visive | 68 media: 15 foto, 10 xilografie, screenshot di call/template/siti, tessera, insegna, cartella | **0 immagini** di contenuto | PDF e dashboard veri, rail dei sistemi (≥ 5), frame di call, oggetti costruiti |
| Schemi | scala a 7 step, albero «tu sei qui», stack DM→Loom→Call, griglia 01-04, card gemelle, cartella | liste e card senza connettori | **scala, albero, cartella, card gemelle in HTML** (testo selezionabile: meglio di lui) |
| Obiezioni | ostili + polarizzanti + 18 FAQ in 2 gruppi + JSON-LD | «4 obiezioni» + 5 FAQ | **3 registri**: domande ostili, due tipi di aziende, FAQ contratto + FAQPage |
| Chiusura | ancoraggio economico («si ripaga col primo cliente») + tessera dell'offerta | listino + «cosa ottieni» | **quanto costa non farlo** + **tessera del cliente** |
| Superfici | 23 scure / 23 chiare alternate | quasi tutto scuro | almeno **5 aggiunte su carta** (`#faf6ee`) |
| Immagini | 2× esatto, mai ritagliate, width/height, lazy | — | **§14** su ogni immagine nuova; still AURA = brief, mai in pagina |
| Mobile | +12% sul desktop | **+66%** | ogni aggiunta: mobile ≤ 1,4× desktop |
| Movimento | 0 reveal, 5 rail, reduced-motion in 3 strati | reveal ovunque | le aggiunte: **0 reveal**, rail CSS, `matchMedia` |

**La logica del piano, in una riga:** le 37 sezioni di giugno restano; **sopra** di esse si stende un secondo strato in **sei atti** che
segue il ritmo di §15 — *volto → fatti → problema visto → meccanismo → prova → chi siamo → offerta → chiusura* — e ogni atto porta
**almeno un'immagine intera, uno schema in HTML e una superficie chiara**.

---

# §B — P5: IL CATALOGO NUOVO, IN SEI ATTI (28 aggiunte)

Legenda: **▸** = una riga `+` in `page.tsx` dopo il componente indicato · **[H]** = HTML/CSS puro, nessuna immagine necessaria · **[I]** =
immagine (§14: intera, 2×, `width/height`) · **[M]** = pezzo di Max che accende (senza, rende `null`) · **h** = altezza desktop massima ·
**FO** = strategia di origine.

## ATTO I — Il volto e i fatti (0-10% della pagina)
| # | Aggiunta | ▸ dopo | Tipo | Cosa | h | FO |
|---|---|---|---|---|---|---|
| A01 | **La firma** | `<Hero />` | [I][M] | ritratto di Max al pixel (colonna 4/5, luce di taglio calda), riga in prima persona «Ho costruito il primo sistema per me…», eyebrow «Fondatore»; micro-CTA «↓ Guarda come funziona» (ancora a A07) | 480 | S01, S03, I03 |
| A02 | **Rail dei quattro fatti** | `<Firma />` | [H] | 4 numeri da `FATTI.ts` con fonte: `giorniSetup` 7 · `messaggiGiorno` 300 · `canoneMese` 0 · `giorniSupporto` 90; icona SVG mono, 37/17 px, nastro CSS 70 s, fermo in reduced-motion | 273 | E01 |
| A03 | **CTA fissa «Prenota»** | componente in `page.tsx` | [H] | pill in basso a destra, compare dopo 1 schermo, sparisce quando `#cosa-ottieni` o il footer sono in vista; `inert` quando nascosta; → `/prenota/?da=fissa` | 0 | S02, T05 |

## ATTO II — Il problema, visto (10-30%)
| # | Aggiunta | ▸ dopo | Tipo | Cosa | h | FO |
|---|---|---|---|---|---|---|
| A04 | **Foto nello Specchio** | dentro `specchio.tsx` (sezione nostra) | [I][M] | colonna destra con l'immagine **intera** (1/1, 736 px nativi → resa 368, 2×), riga «Ogni mattina. Trenta DM. A mano.»; senza file la colonna si chiude | +0 | I01, I02 |
| A05 | **Prima / dopo** | `<Competitors />` | [I][M] | due immagini della stessa cosa: a sinistra in `grayscale(1)` «Canone mensile» (barrato), a destra a colori con bordo arancione «Asset tuo.» — screenshot di una dashboard consegnata (nostro) o still generato | 700 | I06 |
| A06 | **Insegna «SISTEMI.»** | `<ListenUp />` | [I][M] | parola del servizio in maiuscolo grigio su un'immagine simbolica intera, cornice 1 px; superficie **carta** | 520 | E-insegna |

## ATTO III — Il meccanismo (30-50%)
| # | Aggiunta | ▸ dopo | Tipo | Cosa | h | FO |
|---|---|---|---|---|---|---|
| A07 | **La scala a 7 gradini** | `<FlowFramework />` | [H] | card sfalsate (raggio 24), connettori tratteggiati a gomito, icone: chiamata → proposta → contratto → setup 7 gg → go-live → 30 gg di guardia → **«Gira da solo»** in verde (unico verde) — superficie carta | 900 | E02 |
| A08 | **Cartella delle consegne** | `<SystemsShowcase />` | [H] | 4 linguette in `clip-path` (container query): Codice · Dashboard · Documentazione · Formazione; ogni linguetta apre la lista di ciò che il cliente riceve | 700 | E07 |
| A09 | **Guardalo girare** | `<OutreachInside />` | [I][M] | poster WebP (frame vero) + `button aria-label` + durata «1:30»; iframe solo al click (`youtube-nocookie`); senza `src` rende `null`; sotto: cucitura «Ha già mandato 300 messaggi. Tu stai facendo colazione.» con still intero in colonna | 620 | E09, T03 |
| A10 | **Due tipi di aziende** | `<ContentOutput />` | [H] | card gemelle «1. / 2.» numero 81 px: «Chi affitta un tool e resta in affitto» / «Chi possiede il sistema» — bordo arancione solo sulla 2 | 500 | E04 |

## ATTO IV — La prova (50-65%)
| # | Aggiunta | ▸ dopo | Tipo | Cosa | h | FO |
|---|---|---|---|---|---|---|
| A11 | **Immagini vere in prove-vere** | dentro `prove-vere.tsx` | [I] | PDF PreventivoForge (nome coperto, banda ≥ 7:1) e dashboard Preventa, **intere**, 2×, con didascalia e fonte | +0 | I07 |
| A12 | **Rail dei sistemi in produzione** | `<ProveVere />` | [I] | **≥ 5 screenshot distinti** verticali (Outreach Factory, PreventivoForge, Content Factory, Second Brain, dashboard Preventa), oscurati, 2 rail controcorrente | 520 | E10 (gate ≥ 5) |
| A13 | **Frame di call** | `<Results />`… no: dopo `<NoFluff />` | [I][M] | 2 frame di call con volti pixelati sovrapposti in diagonale + 1 lavagna; superficie carta | 560 | I07 |

## ATTO V — Chi siamo (65-75%)
| # | Aggiunta | ▸ dopo | Tipo | Cosa | h | FO |
|---|---|---|---|---|---|---|
| A14 | **La stanza — tre volti** | `<WhoGuides />` | [I][M] | 3 ritratti 4/5 interi (Max, Gael, Leonardo), nome, ruolo, una riga; b/n con luce d'accento | 640 | I03 |
| A15 | **Dietro le quinte** | `<BuilderNotTrainer />` | [I][M] | 6 foto di lavoro vere in coppie, colonna stretta 670, una riga ciascuna; anche «brutte»: mai stock | 900 | S05 |
| A16 | **Mappa Empire — «Tu sei qui»** | `<Dietro />` | [H] | albero: Digital Empire → Agency / Formazione / SaaS, connettori con raccordo, puntatore arancione animato sul ramo Agency; link al Manuale e alle app | 600 | E03 |

## ATTO VI — L'offerta e la chiusura (75-100%)
| # | Aggiunta | ▸ dopo | Tipo | Cosa | h | FO |
|---|---|---|---|---|---|---|
| A17 | **La tessera del cliente** | `<PricingROI />` | [H]+[I] | card verticale (laccio PNG) con 4 spunte: codice consegnato · 90 gg supporto · garanzia 30 gg · 0 canoni; QR → `/prenota/`; prezzi da `listino.ts` | 600 | E06 |
| A18 | **Quanto costa non farlo** | `<Clarity />` | [H] | formula visibile: ore/mese a mano × costo orario vs setup una volta → «si ripaga in N mesi», numeri da `FATTI`/`LISTINO` (`MESI_PAREGGIO`) | 500 | S09 |
| A19 | **Cosa succede se non funziona** | `<MyPromise />` | [I][M] | la garanzia come contratto in due quadri incrociati: «se il sistema non fa X entro Y → noi facciamo Z» con la foto di Max; superficie carta | 600 | S07 |
| A20 | **Le domande che non ci fate** | `<Objections />` | [H] | 3 domande ostili con risposta in una frase: «Se funziona così bene perché non lo tenete per voi?» · «Perché la chiamata è gratis?» · «Cosa ci guadagnate?» | 500 | S08 |
| A21 | **FAQ contratto e pagamento** | `<FAQ />` | [H] | accordion unico, 2 gruppi (Sistema / Contratto & pagamento), prima risposta aperta; alimenta il JSON-LD `FAQPage` | 700 | E08, T09 |
| A22 | **Coda legale** | prima del `<footer>` | [H][M] | ragione sociale, P.IVA, sede, PEC, link privacy/cookie, «Preferenze cookie»; `null` senza `legal.ts` | 160 | — |

## Strato tecnico (0 px)
| # | Aggiunta | Dove | Cosa | FO |
|---|---|---|---|---|
| T1 | `Immagine.tsx` | `sezioni-aggiunte/` | `width/height/alt` **obbligatori**, lazy di default, `priorita` (una per pagina) | T01, T02 |
| T2 | `VideoAClick.tsx` | idem | facade, zero iframe al load, «— da girare» visibile in anteprima, bloccato in prod | T03 |
| T3 | `Sezione.tsx` + `.vivo .sezione-chiara` | idem + `vivo.css` | tema per sezione via variabili; le figlie leggono solo `var(--vivo-*)` | T06 |
| T4 | `Consenso.tsx` + `lib/misura.ts` | idem | consenso onesto, tag solo dopo il sì, evento `visit` first-party + 5 eventi (`?da=`, `call_prenotata`, scroll) | T07, T08 |
| T5 | `schema.ts` | `layout.tsx` +1 | JSON-LD `@graph` (Organization, Person, Service×3, FAQPage) dagli stessi array delle FAQ e da `listino.ts` | T09 |
| T6 | `manifest.json` + `aura_prep.py` | `public/aura/`, `scripts/` | posti A01/A04/A05/A06/A09/A13/A14/A15/A19; campo `sfondo_ammesso`; `--check` | I01, I05 |

**Conto di P5:** 22 aggiunte in pagina + 6 tecniche · **11 superfici carta** · **13 con immagine**, 9 in HTML puro · altezza **+≈ 10.900 px**
(38.683 → ≈ 49.600, +28%) · pezzi di Max: 4 ritratti, 6 foto di lavoro, 1 video, 1 still per A05/A06 se non si usa uno screenshot, dati
legali, Calendly 30 min, Higgsfield per gli still generati.

---

# §C — CRITICA 5 → P6 (contro P5)

**C5.1 — «+10.900 px su un sito che ha già 6.000 px di troppo: raddoppi il male».** Vero. P6 taglia per **valore per pixel**: cadono
**A06 Insegna** (520 px per una parola: il suo contesto era l'assenza di un nome; noi il nome lo abbiamo nell'hero) e **A13 Frame di
call** (560 px, dipende da registrazioni che non esistono; la prova della chiamata la dà già A09 video). **A10** e **A20** si fondono in
una sezione carta sola (card gemelle sopra, 3 domande sotto): −500 px. **A15** passa da 6 a **4 foto** (−300 px). Nuovo conto: **+≈ 8.800 px
(+23%)**, dichiarato. Non si scende sotto: le immagini sono l'oggetto del cantiere, e uno schema in HTML pesa 500-900 px per natura.

**C5.2 — «Il ritmo di §15 misura la pagina intera, ma il 10% della NOSTRA pagina è già passato quando finisce l'hero+VSL».** L'hero
esistente misura ≈ 1.100 px, la VSL ≈ 900: il volto in A01 sta a y≈1.100 = **2,2%**: dentro. Il rail dei fatti a y≈1.600 (3,2%). La prima
prova visiva (A05 prima/dopo) a y≈8.000 = **16%**: dentro il 30%. P6 aggiunge la verifica al gate: **y del primo volto / altezza totale
≤ 0,10** misurato sulla build.

**C5.3 — «Tre schemi in HTML (scala, cartella, albero) sono tre componenti da scrivere: chi li disegna?»** Sono i tre pattern che
funneloperator fa in raster o CSS e noi facciamo in HTML **perché il testo resti selezionabile** (ATLANTE §D, vantaggio dichiarato). P6 li
ordina: **A07 scala** per prima (è la spiegazione del servizio, 0 dipendenze), poi **A16 albero** (0 dipendenze), poi **A08 cartella**
(`clip-path` parametrico: il più costoso, 2 h). Ognuno nasce nel cantiere e diventa pattern al secondo uso (§10).

**C5.4 — «A05 prima/dopo: che immagine mettiamo a sinistra? Non abbiamo un "canone mensile" da fotografare».** P6 concretizza: a sinistra
**lo screenshot di una pagina di fatturazione SaaS anonima** (prezzo mensile in evidenza, desaturata), a destra **la dashboard di
un nostro sistema** a colori. Due screenshot nostri, 2×, interi: nessun still generato serve. Titolo barrato «200 € al mese, per sempre» /
pieno «4.000 € una volta. Tuo.» (cifre da `LISTINO`).

**C5.5 — «La CTA fissa (A03) si sovrappone allo sticky esistente in basso»**. Lo `StickyCTA` esistente occupa **tutta la base** su scroll
> 70% viewport e va al netlify del corso; non si tocca. P6: la CTA fissa nuova sta **in basso a destra sopra lo sticky** (`bottom: 84px`
desktop, `calc(72px + env(safe-area-inset-bottom))` mobile) e **si nasconde quando lo sticky è visibile**? No: coesisterebbero due CTA.
Decisione: A03 si attiva **solo nelle pagine nostre** (`/prenota/`, future) e in home resta **spenta finché Max non decide** sulle CTA
vecchie (§7 v1). In home la porta nostra resta nelle sezioni aggiunte (A17 tessera, A19, `cosa-ottieni`).

**C5.6 — «Dove sta scritto che le immagini generate saranno all'altezza? La tavola v1 faceva schifo».** P6 fissa il **brief unico** delle
immagini generate (FO-I02): *incisione/xilografia argento su nero, grana, nessun grigio medio, soggetti = strumenti del mestiere e figure
al lavoro, volto non riconducibile, formato = quello del posto (1/1 per lo specchio, 4/5 colonne, 3/2 poster), 2× della resa*. Ogni
immagine passa un **controllo visivo di Max in anteprima** prima del `--prod` (§13: è roba sua). Gli still AURA restano brief.

**C5.7 — «Undici superfici carta su un sito scuro: sembrerà un altro sito».** Il live ha già `bg-grey` in 6 sezioni (hierarchy, no-fluff,
audience…): la carta non è estranea. Ma P6 le riduce a **7** (A02 rail, A07 scala, A17 tessera, A19 garanzia, A21 FAQ, A10+A20, A15) e
impone la regola di alternanza: **mai due aggiunte chiare consecutive senza una sezione di giugno in mezzo**.

---

# §D — CRITICA 6 → P7 (contro P6)

**C6.1 — «P6 ha tagliato a occhio (valore per pixel): non c'è una misura».** P7 la scrive: ogni aggiunta ha un **punteggio di ruolo**
(volto 5 · prova 5 · meccanismo 4 · obiezione 3 · offerta 3 · vita 2) diviso per **altezza in schermate (900 px)**. Sopravvivono le
aggiunte con punteggio ≥ 3/schermata. Applicato: A06 = 2/0,58 = 3,4 → sarebbe rientrata: **resta tagliata per la ragione di C5.1**
(non ha contenuto) e lo si dichiara come eccezione al punteggio. A15 (vita 2 / 0,67 = 3) al limite: tenuta perché è l'unica sezione con
Gael e Leonardo al lavoro (§15: storia con foto = credibilità che il sito non ha).

**C6.2 — «Il gate del ritmo (C5.2) legge la build, ma il volto è `null` finché Max non dà il ritratto: il gate fallirà per mesi».** Giusto:
P7 distingue **gate strutturale** (il posto esiste al ≤ 10%: PASS anche con `null`) e **gate di accensione** (il file esiste: PASS solo
quando Max lo dà). Il battito riporta i due numeri separati: *struttura nostra X% · accensioni di Max Y%*.

**C6.3 — «A12 rail dei sistemi: 5 screenshot distinti "oscurati" — oscurati da chi, con quale regola?»** P7: `aura_prep.py --oscura`
copre con banda `#0a0a0a` ogni riga che contiene un numero di telefono, un'email, un cognome o una targa (regex + zone dichiarate nel
manifest); lo screenshot **non** si sfoca (la sfocatura fa «finto»); la banda porta l'etichetta mono «dato del cliente». Il gate `gate_fatti`
esteso a email/telefono (B-074) controlla la build.

**C6.4 — «A21 FAQ contratto: il testo di 8 domande nuove chi lo scrive, con quale voce?»** P7: `COPY.md` §A21 con le 8 domande, scritte
con la Voce DE (`VOCE.md`, 10 regole) e passate da `gate_voce.py` (ogni provocazione paga con un numero) e `gate_fatti.py` (ogni cifra in
`FATTI.md`). Stesso per A18, A19, A20, A10: **tutto il copy nuovo si scrive PRIMA del codice** (§3 del canone) e passa i due gate.

**C6.5 — «A03 spenta in home: allora la lezione S02 (una sola CTA fissa) non la applichiamo dove serve».** È il costo del vincolo §13: lo
sticky esistente non si tocca. P7 la mette **in cima alla lista di Max** come decisione con anteprima: *«sostituire lo sticky del corso con
la CTA fissa nostra che sparisce»* è una **modifica**, e vale un'anteprima. Finché non decide, A03 vive in `/prenota/` e nelle pagine future.

**C6.6 — «Le altezze massime sono stime. Chi le misura?»** P7: `MISURA-DOPO.md` con `capture` prima/dopo per ogni fase (px desktop/mobile,
CTA, media, superfici, y del primo volto e della prima prova, densità foto/1.000 px, peso immagini). Il gate di fase fallisce se un'aggiunta
supera la sua `h` dichiarata del 15%.

---

# §E — CRITICA 7 → P8 (contro P7)

**C7.1 — «Il piano è lungo; il primo giorno cosa succede?»** P8 fissa **il primo giorno**: F1 = A01 (firma, `null` senza ritratto) + A02
(rail dei fatti) + T1 (`Immagine.tsx`) + T6 (manifest): 5 ore, tutto nostro, e il sito ha già il posto del volto e i fatti veri. Il secondo
giorno: A07 scala + A17 tessera. Il valore arriva a giorni, non a fine cantiere.

**C7.2 — «La Tavola v1 è stata bocciata: la v2 con che regole?»** P8 le scrive (e la Tavola v2 le segue): **(1)** ogni still al pixel
nativo o più piccolo, mai più grande; **(2)** intero: `object-fit: contain`, contenitore col rapporto del file; **(3)** composizione che lo
ospita (colonna 4/5 o 1/1, non fascia 21/7); **(4)** JPEG q≥ 88 nell'artefatto, nessun filtro che sfoca; **(5)** gli schemi in HTML si
mostrano **costruiti in HTML** nella tavola stessa (scala, albero, tessera, rail, card gemelle, cartella), non disegnati; **(6)** ogni tavola
dichiara «dove entra», «altezza», «input», «FO-\*», «§14/§15 rispettati».

**C7.3 — «"Solo dopo procederai": procedere significa costruire?»** No: significa **consegnare piano + tavola e fermarsi al «vai»**. Il
12/09 ho letto un «vai» su un piano come licenza di rifare: non si ripete. P8 lo scrive nel criterio di fine di questo dossier: **il
dossier è chiuso quando Max ha visto piano e tavola; il cantiere apre solo con il suo «vai» su questo file.**

**C7.4 — «Le 37 sezioni di giugno hanno difetti che le aggiunte non curano (VSL finta, results segnaposto, 5 gradienti): il lettore li
vedrà comunque».** Sì, e resta scritto in §7 della v1: sono decisioni di Max. P8 aggiunge una cosa sola: **ogni aggiunta vicina a un difetto
lo compensa senza toccarlo** — A11/A12 (prove vere) subito dopo `results` (segnaposto); A02 (fatti veri con fonte) sotto l'hero, prima di
`science-stats` (numeri finti); A09 (video vero) dopo la VSL finta. Il lettore vede il vero subito dopo il finto.

---

# §F — P8: IL CATALOGO FINALE (24 aggiunte + 6 tecniche), IN ORDINE DI PAGINA

| Ordine | # | Aggiunta | ▸ dopo | Sup. | Tipo | h max | Input | FO |
|---|---|---|---|---|---|---|---|---|
| 1 | A01 | La firma (ritratto intero + riga + «↓») | Hero | ink | I·M | 480 | ritratto Max | S01 S03 I03 |
| 2 | A02 | Rail dei quattro fatti | Firma | **carta** | H | 273 | — | E01 |
| 3 | A04 | Foto intera nello Specchio | in specchio | carta | I·M | +0 | still 1/1 | I01 I02 |
| 4 | A05 | Prima/dopo: fattura SaaS b/n vs dashboard nostra | Competitors | ink | I | 700 | 2 screenshot nostri | I06 |
| 5 | A07 | La scala a 7 gradini | FlowFramework | **carta** | H | 900 | — | E02 |
| 6 | A08 | Cartella delle consegne | SystemsShowcase | ink | H | 700 | — | E07 |
| 7 | A09 | Guardalo girare + cucitura in colonna | OutreachInside | ink | I·M | 620 | video | E09 T03 |
| 8 | A10+A20 | Due tipi di aziende + le domande che non ci fate | ContentOutput | **carta** | H | 800 | — | E04 S08 |
| 9 | A11 | PDF e dashboard interi in prove-vere | in prove-vere | carta | I | +0 | — | I07 |
| 10 | A12 | Rail dei sistemi in produzione (≥ 5, oscurati) | ProveVere | ink | I | 520 | — | E10 |
| 11 | A14 | La stanza — tre volti | WhoGuides | ink | I·M | 640 | 3 ritratti | I03 |
| 12 | A15 | Dietro le quinte (4 foto) | BuilderNotTrainer | **carta** | I·M | 600 | 4 foto | S05 |
| 13 | A16 | Mappa Empire «Tu sei qui» | Dietro | ink | H | 600 | — | E03 |
| 14 | A17 | La tessera del cliente | PricingROI | **carta** | H·I | 600 | — | E06 |
| 15 | A18 | Quanto costa non farlo | Clarity | ink | H | 500 | — | S09 |
| 16 | A19 | Cosa succede se non funziona (con il volto) | MyPromise | **carta** | I·M | 600 | ritratto Max | S07 |
| 17 | A21 | FAQ contratto e pagamento + JSON-LD | FAQ | **carta** | H | 700 | — | E08 T09 |
| 18 | A22 | Coda legale | prima del footer | ink | H·M | 160 | dati legali | — |
| — | A03 | CTA fissa che sparisce | `/prenota/` e pagine nuove (home: decisione di Max) | — | H | 0 | — | S02 |
| — | T1-T6 | Immagine · VideoAClick · Sezione · Consenso+misura · schema · manifest+aura_prep | — | — | H | 0 | toggle Vercel | T01-T09 |

**Conto di P8:** 18 inserimenti in pagina + 3 estensioni di sezioni nostre + CTA fissa + 6 tecniche · **7 superfici carta** alternate ·
**9 con immagine** (di cui 5 solo con pezzi di Max) · **9 in HTML puro** (nessuna dipendenza) · altezza **+≤ 8.800 px** (+23%) ·
mobile ≤ 1,4× per aggiunta · **0 righe rimosse** · immagini: §14 su tutte.
**Controlli di ritmo sulla mappa:** primo volto y≈1.100 (2%) ✔ · prima prova visiva y≈8.000 (16%) ✔ · nessuna CTA di vendita nuova
sopra il 50% (la prima porta nuova è A17 a ≈ 70%) ✔ · mai due aggiunte chiare consecutive ✔ · mai due immagini di fila senza testo ✔.

---

# §G — V4 ESECUTIVO v2

Gate comuni (G\*) a ogni fase: `npm run build` · `gate_solo_aggiunte.py --live … --base agency-empire-landing-live-20260912` exit 0 ·
`gate_fatti.py` + `gate_voce.py` sul copy nuovo · **§14**: nessun `<img` senza `width/height`, un solo `fetchPriority`, nessun `cover`
su `.foto` · **§15**: y primo volto / h ≤ 0,10 (posto), CTA di vendita nuove > 50% · screenshot 1440 + 390 **guardati** · console 0 errori ·
altezza ≤ `h` dichiarata +15% · `npx vercel` anteprima · commit · `--prod` da Max.

| F | Fase | Cosa | Gate proprio | h | Peso |
|---|---|---|---|---|---|
| F0 | Apertura | BRIEF (URL + `project.json` + frase di Max) · baseline `capture` (px, CTA, media, y volto) · **COPY.md** di tutto il copy nuovo (A10/A18/A19/A20/A21, righe delle immagini) con `gate_voce`+`gate_fatti` PASS · domanda C3.3 (le 3 sezioni del 12/09 restano?) | copy PASS prima del codice (§3) | 4 | 8% |
| F1 | **Primo giorno**: A01 + A02 + T1 + T6 | firma (`null` senza ritratto) + rail dei fatti + `Immagine.tsx` + manifest/`aura_prep` | posto del volto ≤ 10%; rail fermo in reduced-motion | 5 | 12% |
| F2 | Meccanismo in HTML: A07 + A16 + A17 | scala, albero, tessera — pattern nascenti | testo selezionabile; 0 KB JS; `h` rispettata | 8 | 15% |
| F3 | Prova: A05 + A11 + A12 + T2 + A09 (scheletro) | 2 screenshot prima/dopo, PDF/dashboard interi, rail ≥ 5 (`--oscura`), `VideoAClick` | 2× su ogni raster; rail ≥ 5 distinte; B-074 email/telefono = 0 | 7 | 15% |
| F4 | Obiezioni e chiusura: A10+A20, A18, A21 + T5 | card gemelle + domande ostili, formula del pareggio, FAQ 2 gruppi + `schema.ts` | FAQPage valida; prima risposta aperta; cifre da `LISTINO` | 7 | 12% |
| F5 | Vita: A04, A14, A15, A19 (scheletri), A08 cartella, A22, T3, T4 | posti che rendono `null`; cartella `clip-path`; coda legale; tema per sezione; consenso+misura | `aura_prep --check`; consenso: tag solo dopo il sì; 5 eventi in dev | 9 | 13% |
| F6 | **Accensioni** (Max) | ritratti (A01, A14, A19), foto di lavoro (A15), video (A09), still generati (A04 + cucitura A09), dati legali (A22), slug Calendly, toggle Analytics, decisioni (CTA fissa in home, noindex, footer) | **anteprima a Max** prima del `--prod`; screenshot guardati da lui | 6 | 15% |
| F7 | Chiusura | `MISURA-DOPO.md` (px, y volto, densità, peso), `LEZIONE.md`, pattern promossi (§10), CP, STATO, wiki, ripresa chiusa | criterio C3.4 v1 + C7.3 | 2 | 10% |

**Totale nostro (F0-F5, F7): ≈ 42 h · 85%. Max (F6): 15%** — per gesto: ritratti 4 · foto 3 · video 3 · still/Higgsfield 2 · legale 1 ·
Calendly 1 · decisioni 1.

**Politica di guasto** (ADR-028): gate FAIL → non si deploya, mai `--consenti` sul testo di giugno · `--prod` negato al bot → comando nel
battito · pezzo di Max assente → posto `null`, fase chiusa · `h` superata del 15% → si riduce l'aggiunta, non il gate · Max boccia
un'aggiunta vista online → si toglie quel file nostro, LEZIONE, il resto resta.

**Criterio di fine del dossier (C7.3):** Max ha visto piano e Tavola v2. **Criterio di fine del cantiere:** corsia nostra online col gate
a exit 0 · scheletri esistono · primo numero misurato · LEZIONE · pattern promossi. Le accensioni arrivano quando arrivano.

---

# §H — LA LISTA DI MAX (gesti che accendono; nessuno ferma)

| Gesto | Accende | Fase |
|---|---|---|
| `cd agency-empire-landing && npx vercel --prod --yes` | og.jpg + refusi (X3A4) e ogni fase | tutte |
| **4 ritratti** (Max ×2 — firma e garanzia —, Gael, Leonardo): luce di taglio, fondo scuro, anche da telefono | A01, A14, A19 | F6 |
| **4 foto di lavoro** (scrivania, call, riunione, notte) | A15 | F6 |
| **Video 60-90 s** del sistema che gira (o «sì» alla mia registrazione oscurata) | A09 | F6 |
| **Higgsfield Plus** (dossier 28) — o un «sì» al brief unico su un altro generatore | A04, cucitura A09 | F6 |
| Ragione sociale, P.IVA, sede, PEC | A22, privacy, cookie | F6 |
| Evento Calendly «Chiamata Digital Empire · 30 min» | `/prenota/` coerente (oggi «90% formazione 10% Peach · 1 h») | F6 |
| Toggle Web Analytics su Vercel | i 5 eventi arrivano | F5 |
| **Decisione con anteprima:** sostituire lo sticky del corso con la CTA fissa nostra che sparisce | A03 in home | — |
| Decisioni: `noindex` · CTA vecchie → `/prenota/` · footer con link veri | — | — |
| Risposta C3.3: specchio, prove-vere, cosa-ottieni, /prenota/ restano? | F0 | F0 |

---

---

# §I — LE CINQUE DECISIONI DI MAX (13/09, testuali: «modifiche che già sono sicuro che voglio»)

Sono **ordini espliciti**: le prime due **modificano l'hero esistente** — ammesso da §13 solo su ordine con quelle parole (c'è) e
**prima in anteprima, mai in produzione al primo colpo**. Le altre tre sono aggiunte. Entrano nel catalogo come **D1-D5**, con priorità
sopra ogni A\*.

| # | Decisione di Max | Come si fa (chirurgico) | Dipende da |
|---|---|---|---|
| **D1** | **La texture 1** (onde di linee puntinate arancioni su nero — allegato 1) è **lo sfondo dell'hero**. «Gli elementi si devono vedere, le scritte si devono vedere, tutto in estrema qualità; se serve oscurare leggermente la texture». | `hero.tsx` riceve un layer di sfondo NUOVO (`<div class="hero-texture">` con `<img>` 2× WebP, `object-fit: cover` **dichiarato** come eccezione §14 perché è sfondo) + overlay `linear-gradient(180deg, rgba(10,10,10,.55), rgba(10,10,10,.35) 40%, rgba(10,10,10,.7))` **calibrato al contrasto ≥ 7:1** su ogni riga di testo (misurato con lo screenshot, non a occhio); grana locale sopra il gradiente ma **non sopra le scritte**. Anteprima → Max → prod. | **il file della texture** (non è sul disco: Max lo mette in `agency-empire-landing/public/texture/hero-onde.jpg`, ≥ 2.880 px di larghezza) |
| **D2** | **Headline e sottotitolo dell'hero un po' più in alto**, e sotto **uno schema a blocchi collegati da frecce artistiche** (curve, con puntini che finiscono in punta), che racconta il funnel del cliente: «dall'operatività di merda al workflow che gira». «Estremamente persuasivo, qualità estrema». | in `hero.tsx`: `padding-top` ridotto e `margin` del blocco titolo (modifica ordinata); componente NUOVO `sezioni-aggiunte/funnel-hero.tsx`: 4 blocchi — **Oggi: tutto a mano** (30 DM al giorno · follow-up dimenticati · contenuti quando riesci) → **Chiamata 30′** (vedi il sistema che gira) → **Setup 7 giorni** (sul tuo server, coi tuoi account) → **Il tuo workflow gira** (300 messaggi/giorno · 0 ore tue · 0 canoni · codice tuo) — frecce in **SVG**: `path` curvi (bezier), `stroke-dasharray` a puntini, punta triangolare `marker`, `stroke-dashoffset` animato lentamente (ferme in reduced-motion); numeri da `FATTI`/`LISTINO`. Anteprima → Max → prod. | nessuno (HTML/SVG) |
| **D3** | **La texture 2** (grana arancione su nero con strisce scure diagonali — allegato 2) fa lo sfondo di **una sezione piccola**, «quasi un elemento», con qualcosa scritto dentro. | nuova **fascia-manifesto** (≤ 320 px) dopo `<PowerDeck />`: la texture intera come sfondo (`cover`, eccezione §14 dichiarata), vignetta scura ai bordi per la leggibilità, una frase sola in grande — **«I tool si pagano. I sistemi si possiedono.»** — e un micro-CTA «↓». | **il file della texture** (`public/texture/grana-fuoco.jpg`) |
| **D4** | **La sezione «Hai competitor e non lo sai»** (allegato 3 = N5 della v2: fascia arancione + asse «A MANO — TU sei qui — AUTOMATIZZATO» + silhouette con riga) **la voglio ad ogni costo**, migliorata nella qualità. | nuova `sezioni-aggiunte/competitor-vivo.tsx` dopo `<Competitors />` (A05 prima/dopo scivola dopo `<ListenUp />`): fascia arancione col titolo (unico fondo pieno arancione della pagina, §12) · corpo ink a due colonne · **immagine intera** al suo rapporto (§14: colonna 4/5, 2×, mai `cover`) con la **riga sotto l'immagine**, non sopra · asse in HTML con i tre punti e «sei qui» animato · testo «Stessi limiti tuoi. Il primo che li risolve non lo raggiungi più.» | still generato 4/5 (Higgsfield) o foto vera; il file v2 `n5-fascia.webp` era 949×1178 → va rifatto a 2× |
| **D5** | **Lo Specchio con l'immagine** (allegato 4 = N2 della v2) **lo voglio assolutamente**, ma «le scritte sopra l'immagine più sottili, più eleganti, molto più leggibili; grana e professionalità migliorate molto». | in `specchio.tsx`: colonna foto a sinistra (`due-col--foto-sx`) con l'immagine **intera 1/1 a 2×** (il file v2 era 400×400: **va rigenerato ≥ 800×800**) · la riga **sopra l'immagine** come vuole Max, ma: peso 400-500 (non 600), corsivo serif o sans leggero, corpo 17-19, letter-spacing +0,01em, banda scura sfumata ≥ 7:1 misurata, nessun `text-shadow` pesante · grana **solo sul fondo carta**, mai sull'immagine (§14) · bordo 1 px + ombra bassa come fa funneloperator sulle foto su chiaro. | still 1/1 rigenerato a 2× |

**Effetti sul piano:** D1+D2 sono la **prima fase dopo il «vai»** (F1 diventa: D2 funnel-hero + D1 texture + A01 firma + A02 rail) perché
toccano ciò che si vede per primo; **anteprima obbligatoria** (`npx vercel`) e sua parola prima del `--prod`. D4 e D5 entrano in F3/F5 con
le immagini rigenerate a 2×. D3 in F2. Le due texture sono **gesti di Max** (lista §H): finché non ci sono, D1 e D3 restano `null`
e il sito è intero. Tavola v2: le tavole D1-D5 si aggiungono con approssimazioni CSS delle texture dichiarate come tali.

**Nota di metodo:** gli allegati 3 e 4 sono sezioni della v2 bocciata il 12/09: Max boccia l'insieme, non i pezzi. Da oggi nella
LEZIONE: «una v2 bocciata si smonta in pezzi da rivalutare uno a uno, non si archivia in blocco».

## Connessioni
- `competitor/Andrei Pascu/site-study/reports/66-funneloperator-{STRUTTURA-STRATEGIA,STILE,ATLANTE-VISIVO,COSTRUZIONE,SINTESI-STRATEGIE}.md`
- `company/Memory/decisions/ADR-030-…`, `ADR-031-immagine-intera-e-ritmo-della-pagina.md` · `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` §13-§15
- `.claude/skills/fabbrica-siti/pattern/_CANDIDATI-FUNNELOPERATOR.md` · `scripts/gate_solo_aggiunte.py` · `og_stampo.py`
- `38-PIANO-SITO-AGENCY-SOLO-AGGIUNTE.md` (v1, superata in §2/§5-bis/§6; §0, §1, §7, §8 restano) · `37-PIANO-SITO-AGENCY-VIVO.md` (diagnosi)
- ripresa `EMP-XR4F` · CP-20260912-X3A4 · CP-20260913-T3U6 · wiki `Progetto_Sito_Agency_Vivo`, `Source_Funnel_Operator_Sito_2026`, `Tool_Fabbrica_Siti`
