# ADR-031 — L'immagine si vede intera (§14) e il volto viene prima della richiesta (§15) — dallo studio di funneloperator.it

- **Data:** 2026-09-13
- **Stato:** ATTIVO — due articoli nuovi del canone della Fabbrica Siti
- **Decisori:** Max (critica testuale del 13/09), Emperator (codifica)
- **Nasce da:** Max, 13/09: *«hai messo le immagini tutte tagliate e dimensionate malissimo, cioè le immagini devono rimanere originali,
  devono vedersi completamente tutte e devono avere una buona nitidezza, una buona chiarezza. Devono avere una qualità assoluta. Tu le hai
  ingrandite e sono tagliate»* + lo studio in quattro rapporti di `funneloperator.it` (`reports/66-funneloperator-*.md`), il sito che
  Max indica come il migliore di Andrei Pascu.

## Contesto

La Tavola Estetica del 12/09 mostrava still di 400-1200 px ingranditi e ritagliati in bande 21/7 con `object-fit: cover`. Il sito
studiato fa l'opposto, e lo fa per regola: **40 raster su 60 serviti esattamente a 2× della resa, rapporto del contenitore uguale al
rapporto del file, `width`/`height` su ogni `<img>`, lazy ovunque tranne l'hero, una sola immagine ritagliata dal CSS in 30 sezioni**
(`66-funneloperator-STILE.md` §7, `66-funneloperator-ATLANTE-VISIVO.md` §C). Nello stesso sito **il primo volto compare all'8,5%
della pagina, i numeri al 9,6%, il primo bottone di acquisto al 64%**; la richiesta è coperta da un solo bottone flottante che sparisce
quando è ridondante (`66-funneloperator-STRUTTURA-STRATEGIA.md` §3). Il nostro sito agency chiede dieci volte a partire da y=800 e
non mostra un volto mai.

## Decisione

**§14 — L'immagine si vede intera.** Un'immagine di contenuto (fotografia, illustrazione, oggetto, screenshot) non si ritaglia con il
CSS e non si ingrandisce oltre il suo pixel: il contenitore ha il rapporto del file (`aspect-ratio: w/h`), `object-fit: contain` o
nessun `object-fit`; è servita a **2× della resa** (o `srcset` 1×/2×), porta `width` e `height`, `alt` che descrive (mai vuoto sul
contenuto), `loading="lazy" decoding="async"` tranne **una** immagine per pagina (`fetchPriority="high"`). Le immagini di fondo e le
texture sono l'unica eccezione al ritaglio, e si dichiarano. La materia (grana, carta) vive nel file o nel CSS scopato, mai come
maschera che copre il soggetto. Un'immagine troppo piccola per il posto **non si allarga: si cambia il posto** (colonna, non fascia).

**§15 — Il volto prima, la richiesta dopo.** In una pagina che vende una chiamata o un servizio: il primo volto vero compare entro il
**10%** dell'altezza, la prima prova (numeri con fonte, screenshot, video) entro il **30%**, la prima CTA di vendita nuova **non sopra
il 50%**; nella prima metà si usano micro-CTA di scorrimento («↓», ancore), non bottoni di vendita. Una sola CTA fissa (flottante),
che compare dopo il primo schermo e **sparisce** quando la CTA di sezione o il footer sono in vista (`inert` quando nascosta). Le
sezioni alternano superficie chiara/scura e testo/immagine: mai due blocchi da 150+ parole di fila; mai due immagini di fila senza testo.

Sui siti già online (§13) i due articoli valgono **per le aggiunte**: l'esistente non si tocca, ma ogni aggiunta li rispetta e, dove
può, cura il difetto dell'esistente (es. una CTA fissa nuova che sparisce; una firma col volto sotto l'hero).

## Alternative scartate
- **Lasciare le regole nell'ATLANTE** — gli agenti della Fabbrica leggono il canone, non 3.000 righe di rapporti.
- **`object-fit: cover` con `object-position` curato** — il ritaglio resta ritaglio: la critica di Max è sul principio, non sulla posizione.
- **Ingrandire gli still con upscaling AI** — si parte dal brief e si genera alla risoluzione giusta (2×): l'upscaling maschera, non risolve.

## Conseguenze
- `CLAUDE-SITI.md` guadagna §14 e §15; `gate_siti.py` riceve tre controlli (B-086/087/088): `<img` senza `width/height`, più di un
  `fetchPriority`, `FINTO —`/`— da girare` nella build, rail con < 5 immagini distinte, `object-fit: cover` su `.foto` di contenuto.
- La Tavola Estetica si rifà: ogni still al suo pixel nativo, intero, in una composizione che lo ospita (colonna, non fascia).
- Il Dossier 38 diventa v2: le aggiunte al sito agency si riordinano sul ritmo di §15 (firma col volto sotto l'hero, numeri, prova,
  storia, poi le porte) e si moltiplicano con gli elementi dell'atlante (scala, albero, tessera, card gemelle, griglia 01-04).
- Manifest AURA: campo `sfondo_ammesso` (illustrazioni bn solo su nero; foto su chiaro o con luce d'accento su nero).

## Contradiction-check
- §7 (reduced-motion), §8 (dato unico), §12 (accento una volta), §13 (solo aggiunte): nessun conflitto; §14/§15 li presuppongono.
- Legge di Max «grana su tutto» (11/09): la grana resta **sul fondo e sul CSS scopato**, mai come maschera che copre il soggetto — §14 lo dice.
- Composizione A (posto → `null` senza file): confermata; §14 aggiunge «un'immagine piccola cambia il posto, non si allarga».
