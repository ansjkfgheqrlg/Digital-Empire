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
- `competitor/Andrei Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md` — le misure da cui
  nasce metà di questo canone
