# CLAUDE-SITI.md — la legge della Fabbrica Siti

**Digital Empire · Dossier 32 · in vigore dal 2026-09-06**

Questo file è **l'arbitro**. Quando due regole si scontrano, vince quella scritta qui, e vince
l'articolo con il numero più basso.

Un agente che deroga **cita l'articolo** che glielo permette, nel codice, nel punto esatto:

```css
/* Deroga §4: il committente ha un design system suo, questo colore è il suo. */
```

Una deroga senza citazione è un errore, non una scelta.

> **Perché questo file esiste.** Il 6 settembre 2026 lo studio del sito `armageddon.bsns.it` ha
> trovato, nei commenti del CSS servito in chiaro, la frase *"CLAUDE.md §4 says his design wins
> here"*. Il nostro concorrente ha una legge numerata che i suoi agenti citano. Noi avevamo quattro
> skill che si vietavano a vicenda e si dichiaravano tutte obbligatorie. Questo file chiude quella
> distanza.
> Rapporto: `competitor/Andrei Pascu/site-study/reports/11-armageddon.md`

---

## §1 — Il canone vince sul gusto

Colori, caratteri, curve, spaziature e raggi vengono da `canone/canone.css`.
**Nessun agente inventa un valore.**

Se serve un valore che il canone non ha, si aggiunge **al canone** — non alla pagina. Un valore che
esiste in una pagina sola e non nel canone è debito, e alla terza pagina è caos.

*Non derogabile.*

---

## §2 — La colonna vince sul breakpoint

Ogni misura di composizione è una frazione della colonna di progetto `--u`:

```css
width: calc(var(--u) * 0.7631);   /* sì */
width: 733px;                      /* no */
```

La pagina deve **scalare come una sola immagine**, non riorganizzarsi a scatti.

I media query esistono **solo** dove una frazione produrrebbe un elemento non leggibile o non
toccabile, e vanno motivati in un commento **con la misura reale**:

```css
/* A 390px il bottone verrebbe 117x29 con testo da 10px: non si tocca. */
--btn: clamp(206px, calc(var(--u) * 0.2996), 288px);
```

*Non derogabile.*

---

## §3 — Il copy prima del layout

Nessuna sezione si disegna prima che il suo testo esista, per intero, in `COPY.md`.

Il testo non è contenuto da versare in un contenitore: **è il contenitore a nascere dalla lunghezza
e dal ritmo del testo.** Una sezione disegnata su lorem ipsum va rifatta due volte.

*Non derogabile.*

---

## §4 — Il design del committente vince sul brand di casa

Se il committente ha un design system suo — un mockup, una palette, un carattere — **il suo vince**.
Il canone Empire arretra a fare da impianto: misura, curve, gate, accessibilità.

La deroga si dichiara nel CSS, in cima al file, con la ragione e la fonte:

```css
/* Deroga §4: il design è quello del cliente (mockup rev.3, 12 ago).
   Palette e caratteri sono suoi. Misura, curve e gate restano canone Empire. */
```

*(Articolo preso di peso dal `CLAUDE.md` di Andrei Pascu. È il suo §4, ed è giusto.)*

*Derogabile solo verso l'alto: il canone cede sull'estetica, mai sull'impianto.*

---

## §5 — La corsia si sceglie dal lavoro, non dal gusto

> **Corsia A — PAGINA.** ≤ 3 pagine **e** nessuno stato lato server (niente login, niente form che
> scrive, niente dati che cambiano da soli).
> → **HTML + CSS + JS vanilla. Colonna `--u`. Zero build, zero dipendenze.**
> Lanci, landing singole, one-pager, pagine di vendita, pagine evento.

> **Corsia B — SITO.** Tutto il resto.
> → **Next.js 16 App Router + Tailwind v4 + Lenis + Framer Motion + GSAP.**
> Siti multi-pagina, LMS, aree riservate, dashboard, e-commerce.

**Entrambe leggono lo stesso `canone.css` e gli stessi pattern.** Il canone è uno, la resa è due.
Una pagina di Corsia A e una di Corsia B messe fianco a fianco devono sembrare la stessa mano.

La corsia si scrive nel `BRIEF.md` **prima** di aprire un file, e si motiva in una riga.

**Un pattern nuovo si scrive prima in vanilla, poi la Corsia B lo avvolge in un componente.**
Mai il contrario: dal vanilla al framework si sale, dal framework al vanilla si riscrive.

*Non derogabile. Decisione registrata in ADR-023.*

---

## §6 — Ogni numero non ovvio dichiara la sua origine

Un numero senza origine è un errore in attesa di essere scoperto.

```css
top: calc(var(--u) * 0.86487);   /* mockup p.2, riga della domanda */
height: calc(var(--u) * 1.28);   /* misurato a 390px: il player pieno è 56% della colonna */
```

Chi legge fra sei mesi deve poter **rimisurare**, non indovinare. E chi vuole "semplificare" un
numero deve prima leggere perché non si può.

*Non derogabile.*

---

## §7 — Niente animazione senza `prefers-reduced-motion`

E il blocco deve spegnere **anche il JavaScript**, non solo il CSS:

```css
@media (prefers-reduced-motion: reduce) {
  .in, .parallax-layer { animation: none; transition: none; }
}
```
```js
var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reduce) { /* parallax, autoplay, contatori animati */ }
```

Un CSS che si spegne mentre il JavaScript continua a muovere i livelli non è accessibile: è rotto.

*Non derogabile.*

---

## §8 — Nessun dato duplicato in pagina

Prezzi, totali, risparmi, conteggi, scadenze: **un dato solo nel sorgente**, il resto calcolato.

```html
<li data-price="199">outEmail</li>
<span data-total></span> di valore, paghi <span data-pay></span>
```

Il motivo è misurato, non teorico: lo studio dei siti di Andrei ha trovato **otto cifre per quattro
metriche** fra pagine dello stesso negozio, a volte nella stessa pagina. Lui ha risolto il problema
con il codice, non con la disciplina — perché la disciplina si stanca.

*Non derogabile.*

---

## §9 — Il gate decide, non l'agente

Una consegna che non passa `scripts/gate_siti.py` **non è consegnata**.

Il gate è deterministico. Non discute, non valuta lo stile, non ha opinioni: controlla dieci cose e
dice PASS o FAIL. Se il gate sbaglia, si corregge il gate — con un commit e una riga di motivo —
non si aggira.

*Non derogabile.*

---

## §10 — Ogni cantiere lascia una lezione

Nessun sito è finito finché non esiste `cantieri/<nome>/LEZIONE.md` e la sua riga in
`cantieri/INDICE.md`.

**L'anello di ritorno:**
- una soluzione che ha funzionato in **due** cantieri diversi → diventa un **pattern**;
- un errore accaduto **due** volte → diventa un **controllo del gate**.

Il sistema si stringe da solo, o non è un sistema.

**E — ADR-016, ULTIMO METRO —** il passo finale non è "consegna", è **deploy**. Un cantiere senza
URL vivo resta aperto nell'indice e continua ad apparire nel battito finché non chiude. Digital
Empire ha 25 pezzi finiti mai pubblicati: la Fabbrica Siti non ne aggiunge un ventiseiesimo.

*Non derogabile.*

---

## §11 — La cassa ha un gradino

Un prodotto one-shot **non manda mai** dal bottone di vendita direttamente al pagamento. In mezzo
sta una **pre-cassa**: meno di uno schermo e mezzo, sei elementi in quest'ordine —

1. occhiello in corsivo che riafferma l'atto (*«Stai acquistando…»*)
2. nome del prodotto, grande
3. istruzione operativa **e codice sconto, se c'è**
4. la cifra, isolata
5. la condizione attaccata alla cifra (*«Una tantum»*)
6. il bottone

**Il codice sconto vive lì e non prima.** Nella pagina di vendita abbassa il prezzo percepito mentre
il lettore sta ancora decidendo; nella pre-cassa toglie attrito quando ha già deciso. E il codice è
**a scadenza o legato alla sessione**: uno sconto permanente non è uno sconto, è il prezzo.

**La pre-cassa non si scrive a mano: si stampa.** Sei elementi sempre uguali sono uno stampo, non
una pagina — e ciò che si ripete diventa uno stampo (`SINTESI-METODO.md` §4). Il comando è:

```
python .claude/skills/fabbrica-siti/scripts/precassa.py \
  --prodotto "..." --accento "..." --prezzo "..." --bottone "..." --cassa "<url>" \
  [--codice "..." --scadenza "..."] --out <file.html>
```

Rifiuta un codice sconto senza finestra di scadenza — la regola qui sopra, applicata dalla macchina
e non dalla buona volontà. L'uscita passa da `scripts/gate_siti.py` come qualunque altra consegna.
Scrivere una pre-cassa a mano quando lo stampo esiste è una deroga, e va motivata.

*Origine: `andrei-copy.com/outfunnel-1` e `/armadeggon-strp`, misurate il 2026-09-07 — ADR-024.
Lo stampo `precassa.py` è del 2026-09-10, dallo studio del metodo (`SINTESI-METODO.md` §4).*

*Non derogabile.*

---

## §12 — L'accento si spende una volta

Una pagina accende **un solo** colore d'azione e lo spende su **una sola** parola: quella che porta
i soldi, non quella che descrive il mestiere.

Misurato su quattro pagine dello stesso guscio: conteggio d'uso dell'accento nel DOM pari a **1**
per pagina — su `/asa` è evidenziato *monetizzare*, non *copywriting*. Un'occorrenza su quattordici,
il **7%**, e regge più di qualunque bottone acceso.

Il guscio (fondo, testo, piede) **non cambia mai** fra le pagine di uno stesso sito: cambia solo
l'accento, e cambia per prodotto.

*Origine: `/define` `#efab00` · `/asa` `#06a506` · `/outfunnel-1` `#13989a`, misurate il 2026-09-07
— ADR-024.*

*Non derogabile.*

---

## §13 — Un sito online si può solo aggiungere

Un sito **pubblicato e visto dal committente** è suo. Chi ci lavora sopra **aggiunge soltanto**: file
nuovi, componenti nuovi, inserimenti puri in `page.tsx` e `layout.tsx` (righe `+`, **zero righe `-`**
sui file esistenti), CSS scopato sotto un wrapper proprio (`.vivo`), pagine nuove in cartelle nuove.

Ciò che c'era **non si tocca** — testo, ordine, CTA, link, `noindex`, footer — anche se sbagliato,
anche se «si migliorerebbe». Un difetto dell'esistente si **segnala** al committente e si aspetta la
sua parola. Una riscrittura si fa **solo se il committente la ordina con quelle parole**, e comunque
**prima in anteprima** (`npx vercel` senza `--prod`), mai in produzione al primo colpo.

**Il «prima» è il live, non il repo.** Il sorgente può contenere restyling mai deployati: prima di
qualunque cantiere si prova `build == live` e si mette un tag (`<sito>-live-YYYYMMDD`).

**Il gate è meccanico** e va passato prima di ogni deploy:

```
python .claude/skills/fabbrica-siti/scripts/gate_solo_aggiunte.py   --live <url-live> --build <out/index.html> --base <tag-del-live> --cartella <cartella-sito>
```

Parte A: il testo del live è contenuto, nello stesso ordine, nel testo della build (difflib: solo
`equal`/`insert`). Parte B: dal tag del live ogni file esistente ha 0 righe rimosse e nessun file è
cancellato. Exit 0 o non si deploya. Le deroghe (`--ignora` per stringhe che cambiano da sole,
`--consenti` per correggere un refuso in una sezione **nostra**) vanno scritte nel checkpoint.

*Origine: il 12 settembre 2026 il Sito Agency Vivo v2 è andato in produzione al primo colpo al posto
del sito che Max aveva visto per 100 giorni; bocciato dopo un'ora, ripristinato integralmente
(CP-20260912-7ZNY). Ordine testuale di Max: «Non puoi modificare niente di ciò che già c'è, puoi
solamente aggiungere.» — ADR-030.*

*Non derogabile.*

---

## §14 — L'immagine si vede intera

Un'immagine di contenuto — fotografia, illustrazione, oggetto, screenshot — **non si ritaglia con il CSS e non si
ingrandisce oltre il suo pixel**. Il contenitore ha il rapporto del file (`aspect-ratio: w/h`), `object-fit:
contain` o nessun `object-fit`. È servita a **2× della resa** (o `srcset` 1×/2×), porta `width` e `height`,
`alt` che descrive (mai vuoto sul contenuto), `loading="lazy" decoding="async"` — tranne **una** immagine per
pagina, l'hero, con `fetchPriority="high"`.

Le immagini di fondo e le texture sono l'unica eccezione al ritaglio, e si dichiarano nel commento. La materia
(grana, carta) vive nel file o nel CSS scopato, **mai come maschera che copre il soggetto**. Un'immagine troppo
piccola per il posto non si allarga: **si cambia il posto** — una colonna al suo pixel, non una fascia.

*Origine: la critica di Max del 13/09 («le immagini devono rimanere originali, devono vedersi completamente,
qualità assoluta») e `funneloperator.it`, misurato il 13/09: 40 raster su 60 a 2× esatto, 1 sola immagine
ritagliata in 30 sezioni, `width/height` su ogni `<img>` — `reports/66-funneloperator-STILE.md` §7 — ADR-031.*

*Non derogabile.*

---

## §15 — Il volto prima, la richiesta dopo

In una pagina che vende una chiamata o un servizio: il **primo volto vero entro il 10%** dell'altezza, la
**prima prova** (numeri con fonte, screenshot, video) **entro il 30%**, la **prima CTA di vendita nuova non sopra
il 50%**. Nella prima metà si usano micro-CTA di scorrimento («↓», ancore), non bottoni di vendita.

**Una sola CTA fissa**, flottante, che compare dopo il primo schermo e **sparisce** quando la CTA di sezione o il
footer sono in vista (`inert` quando nascosta). Le sezioni alternano superficie chiara/scura e testo/immagine:
mai due blocchi da 150+ parole di fila, mai due immagini di fila senza testo.

Sui siti già online (§13) i due articoli valgono **per le aggiunte**: l'esistente non si tocca, ma ogni aggiunta
li rispetta e, dove può, cura il difetto dell'esistente.

*Origine: `funneloperator.it` — primo volto a y=2.793 (8,5%), rail dei numeri a y=3.156, primo bottone di
acquisto a y=20.998 (64%), bottone flottante a tre sentinelle — `reports/66-funneloperator-STRUTTURA-STRATEGIA.md`
§3, `66-funneloperator-COSTRUZIONE.md` §9 r.8 — ADR-031.*

*Non derogabile.*

---

## Come si cambia questa legge

Non si cambia in una conversazione. Si cambia con un **ADR** in `company/Memory/decisions/`, che
dice quale articolo cambia, perché, e cosa si rompe.

Un articolo modificato in silenzio riporta il sistema al 5 settembre 2026, quando quattro skill si
contraddicevano e nessuna aveva torto.

---

## Riferimenti
- `canone/canone.css` · `canone/canone.json` — i valori
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — l'architettura completa, 6 livelli, 5 fasi
- `company/Memory/decisions/ADR-023-fabbrica-siti-due-corsie.md` — la decisione delle corsie
- `company/Memory/decisions/ADR-024-canone-v2-primo-strato.md` — §11 e §12, i pattern `pre-cassa` e
  `pagina-ponte`, i quattro controlli in attesa del gate
- `company/Memory/decisions/ADR-030-sito-online-solo-aggiungere.md` — §13 e `scripts/gate_solo_aggiunte.py`
- `company/Memory/decisions/ADR-031-immagine-intera-e-ritmo-della-pagina.md` — §14 e §15, da `reports/66-funneloperator-*.md`
- `competitor/Andrei Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md` — le misure da cui
  nasce metà di questo canone
- `competitor/Andrei Pascu/site-study/reports/24-25-27-28-macchina-del-funnel.md` — la macchina del
  funnel: da qui §11 e §12
- `competitor/Andrei Pascu/site-study/reports/18-20-apsales-servizi-COSTRUZIONE.md` — il kit
  condiviso e i due difetti che diventano controlli del gate
- `competitor/Andrei Pascu/site-study/reports/18-20-apsales-servizi-COPY.md` — l'asimmetria di
  prezzo fra prodotto a listino e prodotto su misura
