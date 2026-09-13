---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #funneloperator #strategie #ufficializzate #fabbrica-siti
Created: 2026-09-13
Last updated: 2026-09-13
---

# funneloperator.it — SINTESI E STRATEGIE CLASSIFICATE (ufficializzate)

**Il sito più nuovo e migliore di Andrei Pascu** (Max, 12/09), studiato il 13/09 in quattro rapporti paralleli sulla cattura
forense `capture/66-funneloperator-it/` (30 sezioni, 32.807 px, 26 CTA, 68 immagini originali, 44 file sorgente, 13 keyframes):

| Rapporto | Righe | Cosa contiene |
|---|---|---|
| [66-funneloperator-STRUTTURA-STRATEGIA.md](66-funneloperator-STRUTTURA-STRATEGIA.md) | 463 | 30 sezioni classificate a vista, ritmo delle CTA, persuasione, confronto con DE, 15 lezioni, 6 difetti |
| [66-funneloperator-STILE.md](66-funneloperator-STILE.md) | 846 | palette OKLCH→hex, tipografia, griglia 832, effetti, 13 keyframes col corpo, bottoni, **canone in 20 regole**, confronto col canone DE |
| [66-funneloperator-ATLANTE-VISIVO.md](66-funneloperator-ATLANTE-VISIVO.md) | 987 | 30 tavole, 42 tipi di elemento, 50+ immagini schedate, **17 schemi con ricostruzione**, 15 punti di qualità, 20 lezioni |
| [66-funneloperator-COSTRUZIONE.md](66-funneloperator-COSTRUZIONE.md) | 878 | stack (React 19 + TanStack Start + Tailwind v4 + Supabase), design system `fo-`, prezzo-dato-unico, tracking, 15 regole tecniche |

Questo documento **non ripete** i quattro rapporti: li **classifica in strategie**, ognuna con un codice, la misura che la prova,
e **dove viene ufficializzata** dentro Digital Empire (legge, canone, gate, pattern, backlog, wiki). Una strategia senza un posto
dove vivere non è ufficializzata: è una nota.

---

## 0. La tesi in cinque righe

1. **La pagina non chiede per il 64% della sua lunghezza** (primo bottone di acquisto a y=20.998 su 32.807): prima volto (8,5%), numeri (9,6%), storia (14% della pagina), prova; la richiesta è coperta da **un solo bottone flottante** e da tre micro-CTA «↓» che spingono a scorrere.
2. **Una disciplina misurabile, non uno stile**: colonna 832 px ovunque, 2 sfondi alternati (`#111111` / `#ededed`, mai nero né bianco puri), 1 accento in 4 luci, 0 ombre (tranne la sticky), raggi in scala 8/12/24, 4 famiglie a ruolo fisso, 6 corpi.
3. **Le immagini sono la materia**: 68 file, 15 foto vere del fondatore + 10 xilografie di una sola mano + oggetti costruiti (tessera, badge, carte, insegna, cartella); **servite a 2× esatto, mai ritagliate dal CSS, con `width/height`, lazy tranne l'hero**. La grana CSS esiste ma è spenta: la texture sta dentro le WebP.
4. **Ogni cosa che si ripete è un dato o un componente**: prezzo = un oggetto (`Ip`) da cui nascono cifra, «Dal 12 ottobre: 560 €», countdown, FAQ e JSON-LD; 17 componenti per 30 sezioni; sezioni che rendono `null` se l'array è vuoto; placeholder che si dichiarano («VSL 1 — da girare»).
5. **I difetti sono gli stessi che il nostro canone già vieta** (numeri magici, colori fuori token, testo giustificato, portfolio di 3 pezzi ripetuti 12 volte, alt vuoto sull'hero, bundle che espone l'ambiente): conferma che una legge scritta non basta senza il gate.

---

## I. STRATEGIE DI STRUTTURA E RITMO

| ID | Strategia | La misura che la prova | Ufficializzata in |
|---|---|---|---|
| FO-S01 | **Il volto prima del 10%, la prova prima del 30%, la richiesta dopo il 60%** | primo volto y=2.793 (8,5%); rail numeri y=3.156; primo bottone di acquisto y=20.998 (64%) | **CLAUDE-SITI §15** (ADR-031) — legge del ritmo |
| FO-S02 | **Una sola CTA sempre visibile, che sparisce quando è ridondante** | bottone flottante «Ottieni accesso» dal 2° schermo; 3 `IntersectionObserver` (primo schermo, `#offerta-azioni`, footer); `inert` quando nascosta | §15 + pattern candidato `cta-fissa`; per DE: aggiunta `prenota-flottante` |
| FO-S03 | **Micro-CTA di scorrimento («↓») al posto delle CTA di vendita nella prima metà** | 3 ancore testuali; CTA di vendita: 2 in tutto il flusso | §15; regola per le aggiunte DE: nessuna nuova CTA di vendita sopra il 50% |
| FO-S04 | **Alternanza rigida chiaro/scuro e testo/immagine** | 23 sezioni scure / 23 chiare campionate; mai due blocchi da 150+ parole di fila | canone DE: le aggiunte creano **almeno 3 sezioni chiare** (oggi il sito è quasi tutto scuro) |
| FO-S05 | **Storia personale con foto «brutte»** (4 sezioni, 14% della pagina, 7 foto di lavoro) | sez. 13-15; foto cucina/monitor di notte/riunione | aggiunta DE `dietro-le-quinte`; regola: foto vere, mai stock |
| FO-S06 | **Prezzo, data e ancoraggio come un dato solo** | `Ip={ATTUALE:434,PROSSIMO:{importo:560,dal:"2026-10-12"}}` → cifra, countdown, FAQ, `Offer.priceValidUntil` | già nostro: `listino.ts`/`fatti.ts` (§8); si aggiunge `prossimoCambio()` se mai servirà una data |
| FO-S07 | **Garanzia come contratto con il volto**: «se fai X e non ottieni Y, hai Z», firmata dalla foto | sez. 3 (y=2.377) + sez. 21, esposta 3 volte | aggiunta DE `cosa-succede-se-non-funziona` con la foto di Max |
| FO-S08 | **Obiezioni in tre registri**: ostili («Perché mi paghi, lol»), polarizzanti («2 tipi di persone»), FAQ in 2 gruppi (18, JSON-LD) | sez. 17, 27, 29 | aggiunte DE `le-domande-che-non-ci-fate`, `due-tipi-di-aziende`, `faq-contratto-e-pagamento` + FAQPage |
| FO-S09 | **Ancoraggio economico in chiusura**: riporta il prezzo a un'unità nota e fa il conto | sez. 28: «una landing vale 300-600 €, il corso si ripaga col primo cliente» | aggiunta DE `quanto-costa-non-farlo` (ore/mese × costo orario vs setup) |
| FO-S10 | **Mobile che cresce del 12%, non del 66%** | 36.630 vs 32.807 px; noi 64.255 vs 38.683 | gate DE per le aggiunte: altezza mobile ≤ 1,4× desktop per ogni aggiunta |

## II. STRATEGIE DI STILE (il canone che si misura)

| ID | Strategia | Valore esatto | Ufficializzata in |
|---|---|---|---|
| FO-C01 | **Due superfici, un inchiostro**: fondo scuro `oklch(17.8% 0 89.9)` ≈ `#111111`, chiaro `oklch(94.6% 0)` ≈ `#ededed`, testo `#111111` su chiaro / `#e9e9e9` su scuro; bianco puro solo su prezzo, contatore, h1 | STILE §1, §8 r.1-3 | canone DE conferma i suoi neri (`#1c1c1c`/`#0a0a0a`) e la carta (`#faf6ee`): **regola** «mai `#000`/`#fff` come fondo di sezione» → `canone.json` nota |
| FO-C02 | **Un accento in quattro luci** (hover più chiaro, active più scuro, link su chiaro più profondo) e speso in **testo 16 : decorazione 9 : bottoni 3** | `#88c9f4` / `#1d9cd7` / `#0075be` / `#015b97` | canone DE: scala dell'arancione `--orange-light/-base/-hover/-deep` (B-084); §12 resta |
| FO-C03 | **Colonna unica 832 px** = 12×40 + 11×32; margine pagina 24 | STILE §3.1; ATLANTE q.1 | canone DE già ha `--u` (§2); le aggiunte al sito agency usano **una** colonna: `--sv-container` 832 |
| FO-C04 | **Quattro spazi in clamp**: `--spazio-blocchi clamp(32px,7.5vw,48px)` · `-sezioni clamp(40,10vw,64)` · `-vendita clamp(56,15vw,96)` · `-area clamp(64,17.5vw,112)` | STILE §3.2 | `canone.css`: scala a 4 spazi (B-085) |
| FO-C05 | **Raggi in scala 8/12/24 + pill**; bordi 1 px; **0 ombre** (1 sola colorata sotto la sticky) | STILE §3.4-3.5 | canone DE: le aggiunte non portano ombre; raggio 8 bottoni, 12 foto/card |
| FO-C06 | **Sei corpi**: 17-22-29-37-49-63 (≈×1,3); corpo 17/1,6/+0,025em; titoli con tracking negativo crescente; bottone 14px **più piccolo del corpo**; mono solo per metadati | STILE §2.3-2.5 | le aggiunte DE usano 6 corpi soli (noi oggi: 186 dimensioni) → gate `gate_siti.py` sulle sezioni nuove |
| FO-C07 | **Una curva, quattro tempi**: `cubic-bezier(.2,0,0,1)`; 120/160/320/90 ms; hover = solo colore | STILE §5.1, §6 | canone DE: `--curva` + 4 tempi (B-085) |
| FO-C08 | **Nessun reveal on scroll**: tutto visibile subito; movimento solo nei 5 rail (70s/45s, pausa in hover, maschera laterale) | STILE §5.4-5.5 | regola per le aggiunte DE: **niente reveal** (il sito di giugno ne è pieno: non si tocca) |
| FO-C09 | **`prefers-reduced-motion` in tre strati** (CSS dissolvenza al posto del movimento, variant Tailwind, `matchMedia` nel JS) | STILE §5.4; COSTRUZIONE r.6-7 | forma esatta per §7 del canone: copiata in `vivo.css` |
| FO-C10 | **Immagini scure fuse col fondo via blend, mai via ritaglio** (`screen`, `difference`, `color-dodge`, `hard-light`) | STILE §4.2 | tecnica per le xilografie DE su nero: `mix-blend-mode: screen` |

## III. STRATEGIE DELLE IMMAGINI E DEGLI OGGETTI

| ID | Strategia | Misura | Ufficializzata in |
|---|---|---|---|
| FO-I01 | **L'immagine si vede intera**: esportata a **2× della resa**, rapporto dichiarato = rapporto del file, `width/height` su ogni `<img>`, lazy tranne l'hero (`eager sync fetchPriority=high srcset`) | 40 raster su 60 a 2× (±5%); **1 sola ritagliata** dal CSS; 2,5 MB per 68 file (mediana 30 KB) | **CLAUDE-SITI §14** (ADR-031) — la critica di Max del 13/09 è la sua regola n.1 |
| FO-I02 | **Un solo registro illustrativo** (xilografia bianco su nero, grana, nessun grigio medio) per 10 immagini, di una sola mano | ATLANTE §C | DE: **incisione argento su nero con grana** (Brand CCM): un brief unico per Higgsfield, mai still di terzi |
| FO-I03 | **Foto vere del fondatore con luce = colore d'accento** (15 foto, luce blu su fondo nero) | ATLANTE q.9 | DE: ritratti con luce calda/arancione di taglio su nero; 4 ritratti (firma + stanza) |
| FO-I04 | **Oggetti-prova costruiti**: tessera SEC (fonte terza), badge al collo con QR (offerta), carte da gioco (promesse), insegna (servizio), cartella con linguette (programma) — ognuno una volta sola | ATLANTE §B, §D | pattern candidati: `tessera-fonte`, `tessera-cliente`, `carte-promessa`, `insegna`, `cartella-linguette` |
| FO-I05 | **Regia per sfondo**: illustrazioni bn solo su nero; foto soprattutto su chiaro; mai foto calde su nero | ATLANTE q.9 | regola nel manifest AURA DE (`sfondo_ammesso`) |
| FO-I06 | **Prima/dopo con la stessa cosa** (2 ritratti bn/colore; titolo barrato/colorato) | sez. 8 | pattern candidato `prima-dopo`; per DE: landing cliente `grayscale(1)` vs a colori |
| FO-I07 | **Screenshot come prova** (call pixelate, template con evidenziatore, siti terzi) | sez. 6, 22, 25, 26 | DE: dashboard reali oscurate, PDF PreventivoForge, frame di call |

## IV. STRATEGIE DEGLI SCHEMI E DEGLI ELEMENTI (17 schemi ricostruiti nell'ATLANTE §D)

| ID | Elemento | Forma | Per DE (aggiunta) |
|---|---|---|---|
| FO-E01 | **Rail di 4 numeri** con icona, 37/17 px, 273 px di altezza | `fo-rail` 70s, duplicato `aria-hidden`, maschera | `numeri-rail`: anni · sistemi consegnati · messaggi/giorno · giorni di supporto — **fatti da `FATTI.ts`** |
| FO-E02 | **Scala a 7 gradini** (card sfalsate, connettori tratteggiati a gomito, traguardo verde) | HTML | `come-funziona-7-passi`: chiamata → proposta → contratto → setup → go-live → 30 gg guardia → «gira da solo» |
| FO-E03 | **Albero «Tu sei qui»** (3 pillole, connettori con raccordo, puntatore animato) | raster da lui; **HTML per noi** | `mappa-empire`: Digital Empire → Agency / Formazione / SaaS |
| FO-E04 | **Card gemelle 1./2.** (numero 81 px, bordo colorato solo sulla card giusta) | HTML | `due-tipi-di-aziende` |
| FO-E05 | **Griglia 01-04 in mono** con una colonna colorata (fissa) | HTML | `quattro-fasi` (4 fasi dello sprint/sistema) |
| FO-E06 | **Tessera con laccio, 4 spunte e QR** | WebP + HTML | `la-tua-tessera`: codice consegnato · 90 gg supporto · garanzia 30 gg · zero canoni, QR → `/prenota/` |
| FO-E07 | **Cartella con linguette** in `clip-path` a 12 vertici, container query | CSS puro | `cartella-consegne`: 4 linguette = 4 consegne |
| FO-E08 | **Accordion unico** per FAQ e obiezioni, 2 gruppi, JSON-LD dagli stessi array | Radix | `faq-contratto-e-pagamento` (prima risposta aperta di default — difetto suo corretto) |
| FO-E09 | **Poster video con play sobrio** (facade, iframe solo al click, `dnt=1`) | button + WebP | `video-max` / `guardalo-girare` con durata dichiarata |
| FO-E10 | **Portfolio a rail** controcorrente | 2 rail | `sistemi-in-produzione`: **≥ 5 immagini distinte** (gate: il suo ha 3 pezzi ripetuti 12 volte) |

## V. STRATEGIE DI COSTRUZIONE (COSTRUZIONE §9, 15 regole)

| ID | Regola | Ufficializzata in |
|---|---|---|
| FO-T01 | Componente immagine unico con `width/height/alt` **obbligatori** in TypeScript, lazy di default, `<picture>` solo con versione stretta | `sezioni-aggiunte/Immagine.tsx` + gate «nessun `<img` senza width/height» (B-086) |
| FO-T02 | Una sola immagine `fetchPriority=high` per pagina | gate (B-086) |
| FO-T03 | Facade video: zero iframe al load; sorgente mancante → etichetta «— da girare» visibile in anteprima e **bloccata dal gate** in produzione | `VideoAClick.tsx` + gate `FINTO —`/`— da girare` (B-087) |
| FO-T04 | Rail CSS con duplicato `aria-hidden`, pausa in hover, spento in reduced-motion | pattern `rail` |
| FO-T05 | CTA fissa a tre sentinelle + `inert` + `env(safe-area-inset-bottom)` | `CtaFissa.tsx` |
| FO-T06 | Tema per sezione via override di variabili (`.sezione-chiara{--bg…}`) | `vivo.css` |
| FO-T07 | Consenso onesto: tag iniettati solo dopo il sì, revoca = stop + reload, «Preferenze cookie» | `Consenso.tsx` + `misura.ts` |
| FO-T08 | Analytics first-party minimale (visit: path, referrer esterno, utm troncati) | B-043 chiude col primo numero vero |
| FO-T09 | JSON-LD generato dagli stessi dati della pagina (`@graph`, `@id` stabili) | `schema.ts` |
| FO-T10 | Font self-hosted, subset, preload dei 2 critici, `font-display:block` solo sul display | `layout.tsx` +2 |
| FO-T11 | Sezioni alimentate da liste → `null` se vuote; placeholder autodichiarati | già nostro (composizione A); si aggiunge il prefisso `FINTO —` |
| FO-T12 | **Da NON copiare**: inlining dell'`import.meta.env` intero (espone repo, autore, chiavi) | gate «`process.env)` chiuso senza chiave» (B-086) |

## VI. I DIFETTI SUOI → GATE NOSTRI

| Difetto misurato | Gate DE |
|---|---|
| Portfolio: 3 pezzi ripetuti 12-37 volte | un rail parte solo con ≥ 5 immagini distinte |
| 8 immagini a 1×, 1 ritagliata dal CSS, alt errato su `lovable.webp`, hero `alt=""` | §14: 2× obbligatorio per raster, rapporto = file, alt pieno |
| Testo giustificato con fiumi in 7 sezioni | le aggiunte DE: `text-align:left` sempre |
| Bottone primario: testo nero in una sezione, bianco in un'altra | un solo componente bottone; contrasto ≥ 6:1 misurato (il nostro `#fb4604` col bianco è 3,3:1 → testo ink su arancio o arancio più scuro sulla CTA) |
| Nessun accordion aperto | prima risposta aperta di default |
| Numeri magici residui (`mt-[53px]`, `top-[60.3%]`) e 7 colori fuori token | §6 del canone + gate `gate_siti.py` sulle sezioni nuove |
| Bundle 589 KB per l'anonimo; `/cantiere` pubblica | le aggiunte DE: 0 KB JS oltre il player e la CTA fissa; nessuna rotta di prova in produzione |
| Tre sezioni predisposte e vuote in produzione | composizione A: il posto sparisce, nessuna cornice |

---

## VII. DOVE VIVONO ORA (atto di ufficializzazione, 13/09)

- **Legge**: `ADR-031` → `CLAUDE-SITI.md` **§14 «L'immagine si vede intera»** (FO-I01) e **§15 «Il volto prima, la richiesta dopo»** (FO-S01/S02/S03).
- **Canone**: `canone.json` nota su fondi mai puri (FO-C01); B-084 scala dell'accento in 4 luci; B-085 quattro spazi in clamp + curva/tempi.
- **Pattern candidati** (nascono al secondo uso, §10): `pattern/_CANDIDATI-FUNNELOPERATOR.md` — rail-numeri, scala-step, albero-tu-sei-qui, card-gemelle, griglia-01-04, tessera, cartella-linguette, prima-dopo, cta-fissa, poster-video.
- **Gate**: B-086 (immagini: width/height, 2×, un solo fetchPriority, env per chiave), B-087 (`FINTO —`/`— da girare` bloccati in prod), B-088 (rail ≥ 5 distinte, accordion prima aperta, text-align left).
- **Piano**: `PIANO-MAESTRO/38-PIANO-SITO-AGENCY-SOLO-AGGIUNTE-v2.md` (le aggiunte al sito agency riscritte su queste strategie).
- **Ecosistema**: `ECOSISTEMA.md` riga funneloperator.it = studiata (4 rapporti + sintesi); `MIGLIORAMENTI-DIGITAL-EMPIRE.md` +12 candidati.
- **Wiki**: `sources/Source_Funnel_Operator_Sito_2026.md`, `Tool_Fabbrica_Siti` (§14-15), `index.md`, `log.md`.

## Fonti
I quattro rapporti sopra; `capture/66-funneloperator-it/{scheda.json, media-inventario.md, estratto-css.md, copy-integrale.md, sezioni/, media/, src/}`; `scripts/site_capture2.py`, `analizza_css.py`, `scarica_media.py` (nuovo, 13/09).
