---
Type: SOURCE
Status: Active
Tags: #competitor #andrei-pascu #atlante-visivo #design-system #reference
Created: 2026-09-06
Last updated: 2026-09-06
---

# ATLANTE VISIVO — armageddon.bsns.it

**Ogni schermata della pagina, con sotto come è fatta.** Colori campionati dal DOM, misure prese dal CSS servito, effetti letti nel codice — niente stimato a occhio.

Questo documento non è un rapporto strategico: è **materiale di lavoro per la Fabbrica Siti**. Si apre quando si costruisce, non quando si decide.

> **Le immagini.** Vivono in `../capture/11-armageddon/`, fuori dal repo (`.gitignore`, 371 file / 76 MB per l'intero studio). Si rigenerano con:
> ```bash
> python "competitor/Andrei Pascu/site-study/scripts/site_capture.py" "https://armageddon.bsns.it/" --slug "11-armageddon"
> ```

**Sistema di misura di tutta la pagina:**
```css
--u   = min(100cqw, 960px)        /* la colonna di progetto */
--col = calc(50% - var(--u) / 2)  /* il suo bordo sinistro */
--btn = clamp(206px, calc(var(--u) * 0.2996), 288px)
--cell= clamp(56px,  calc(var(--u) * 0.0886), 85px)
--red = #bc0807
--ease-heavy = cubic-bezier(0.65, 0, 0.25, 1)
--ease-land  = cubic-bezier(0.16, 0.86, 0.3, 1)
```
Ogni numero che segue è una frazione di `--u`. Le percentuali sono trascritte dal mockup PDF (826,46 × 2.851,92 unità), non arrotondate.

---

## TAVOLA 1 — La testata e l'hero
![desktop 01](../capture/11-armageddon/desktop-01.png)

### Cosa si vede
Un filetto rosso che nasce dal nero, l'occhio in fiamme, `BSNS.IT` in maiuscoletto spaziato, un altro filetto che torna nel nero. Sotto, un quadrato perfetto: il ritratto in bianco e nero grumoso, gli schizzi rossi, e "Armageddon" che **passa dietro la testa e riappare come contorno sui capelli**.

### La testata — `.topbar`
| Elemento | Valore misurato |
|---|---|
| Sfondo | `#000` |
| Filetto sinistro | `linear-gradient(90deg, transparent, rgba(188,8,7,0.85))`, alto **1px**, `flex: 1` |
| Filetto destro | lo stesso specchiato |
| Occhio | `clamp(23px, calc(var(--u) * 0.036), 36px)` |
| Wordmark | `clamp(11px, calc(var(--u)*0.0145), 15px)` · peso **800** · `letter-spacing: 0.26em` · `rgba(255,255,255,0.78)` |
| Padding verticale | `clamp(15px, calc(var(--u)*0.027), 28px)` |
| Hover | nome → `#bc0807`; occhio → `scale(1.08)` + `drop-shadow(0 0 10px rgba(188,8,7,0.75))`, `0.35s var(--ease-land)` |

**Perché è fatta così.** Il commento nel CSS lo dice: *"Built as a plate between two rules that dissolve into the black, so it reads as part of the same object rather than a website nav bolted on top."* Non c'è un menu, non c'è un logo in un angolo: c'è **una targa**. Un solo link, che riporta al brand madre.
→ **Da rubare:** su una pagina di lancio la navigazione è attrito. Un link solo, e disegnato come parte della composizione.

### L'hero — `.hero`
| Elemento | Valore |
|---|---|
| Altezza sezione | `var(--u)` — **un quadrato sulla colonna** |
| Ritratto | `1024×1024` webp, `object-fit: cover`, `fetchpriority="high"`, z-index 2 |
| Splatter sinistro | left `var(--col)`, top 0, `--u × 0.158225` × `--u × 0.930436` |
| Splatter destro | left `--col + --u × 0.51767`, top `--u × 0.223077`, `0.481008` × `0.680359` |
| "Armageddon" pieno | `--u × 0.1996` ≈ **191,6px** · Curseyt · `#bc0807` · top `0.0622` · **z-index 1** |
| "Armageddon" contorno | stessa posizione · `color: transparent` · `-webkit-text-stroke: max(1px, --u×0.0013) #bc0807` · **z-index 3** · `aria-hidden` |
| "is here" | `--u × 0.2025` ≈ **194,4px** · top `0.62125` · z-index 3 |

### I tre effetti di questa tavola

**1 — Il titolo in due strati.** Stesso testo, stessa posizione, due z-index: uno *sotto* il volto, uno *sopra* e in solo contorno. La parola è piena sul nero e diventa **incisione** dove attraversa i capelli. Costo: un `<span>` in più.

**2 — L'atterraggio a tre tempi.**
```
ritratto  ag-zoom  scale(1.055) → 1     1700ms, delay 0
splatter  ag-fade  opacity 0 → 1        1400ms, delay 120ms
"Armageddon"  ag-rise  ↑ --u×0.026      1200ms, delay 180ms
"is here"     ag-rise  ↑ --u×0.022      1200ms, delay 340ms
```
Curva unica `--ease-land`. **L'animazione sta sui figli `<i class="in">`, non sui contenitori** — perché i contenitori li muove il parallax, e due sistemi di `transform` sullo stesso nodo si annullano.

**3 — Parallax a quattro velocità.**
```js
RATE = { splat: 0.2, word: 0.09, word2: 0.04, man: 0.155 }
```
Gli schizzi (dietro) vanno **più veloci** del ritratto (davanti): inverso rispetto al manuale, e funziona perché il buco che si apre in alto è nero su nero. `translate3d` in `requestAnimationFrame`, listener `passive`, `y` limitato all'altezza dell'hero. Nessuna libreria.

---

## TAVOLA 2 — Il cielo rosso e il video
![desktop 02](../capture/11-armageddon/desktop-02.png)

### Cosa si vede
Il nero si apre su una fotografia di cielo in fiamme. In gotico bianco: **"Guarda il video"**. Sotto, una freccia disegnata a mano che punta al player. Il player Vimeo, angoli arrotondati, 13:29 di durata.

### Misure
| Elemento | Valore |
|---|---|
| Sezione `.stage` | altezza `--u × 1.0866` (desktop) / `× 1.28` (≤720px) |
| "Guarda il video" | `--u × 0.098` ≈ **94px** · Curseyt · **bianco, non rosso** |
| Ombra del testo | `0 0 --u×0.028 rgba(0,0,0,0.95)` + `0 --u×0.003 0 rgba(0,0,0,0.6)` |
| Freccia | SVG inline, `--u × 0.21`, `stroke-width: 13`, `drop-shadow(0 0 --u×0.014 rgba(0,0,0,0.9))` |
| Player | left `--col + --u×0.1321` · width `--u × 0.7631` · `aspect-ratio: 16/9` · radius `--u × 0.01582` |
| Player su ≤720px | `left: var(--col)`, `width: var(--u)`, **`border-radius: 0`** — a tutto schermo |
| Sorgente | `player.vimeo.com/...?title=0&byline=0&portrait=0&**dnt=1**`, `loading="eager"` |
| `.watch` | `pointer-events: none` — sta sopra il cielo, mai sopra un controllo |

### Le tre decisioni da capire

**1 — Il titolo qui è bianco, non rosso.** Commento nel CSS: *"the sky behind this band is red, and his red on it is the one thing that would not read."* La regola tipografica cede al contrasto. **Il colore del brand si abbandona quando il fondo lo mangia** — e al suo posto arriva un'ombra doppia, non un contorno.

**2 — `dnt=1` sul player.** Modalità senza tracciamento di Vimeo: niente cookie. Il commento chiude il cerchio: *"which is also why this site has no banner to show."* **La scelta tecnica elimina un elemento di interfaccia.** Nessun cookie banner su tutta la pagina.

**3 — Il player è in pagina, non dietro una copertina.** Un clic solo, quello sul play. Richiesta di Andrei datata nel codice: *"Andrei asked on 5 September ... he wants people to actually press play, so this is the loudest thing in the section after the player itself."*

### La cucitura — il pezzo più tecnico dell'intera pagina
```
.hero::before   0 → 0.992   (da --u×0.78 a --u×0.8785)
.hero::after    0.992 → 0.71 + sky.webp a center calc(--u × -0.0238)
.stage          0.71 → 0 → 0 → #000 + sky.webp a center calc(--u × -0.1453)
```
Tre superfici, due sezioni HTML, **una sola fotografia**. Si agganciano sugli stessi due numeri — `0.992` e `0.71` — così il cielo attraversa il confine fra `<section>` senza mostrare una linea. Il commento: *"the two halves of his one gradient meet without a step."*
→ **Da rubare:** è il modo giusto di far passare un fondo fotografico fra due sezioni. Sostituisce qualunque `border-top`.

---

## TAVOLA 3 — "Sei pronto?" e i biglietti sul fuoco
![desktop 03](../capture/11-armageddon/desktop-03.png)

### Cosa si vede
Nero pieno, poi **"Sei pronto?"** in gotico rosso, enorme. Sotto, il nero si apre di nuovo su una fotografia di fiamme, e da lì emergono due biglietti stampati: quello davanti elenca `outEmail / outFunnel / outHeadline / outViral`, quello dietro ruotato mostra uno scheletro con la spada.

### Misure
| Elemento | Valore |
|---|---|
| "Sei pronto?" | `--u × 0.15832` ≈ **152px** · Curseyt · `#bc0807` · top `--u × 0.86487` (`0.99` su ≤720px) |
| Sezione `.offer` | padding-top `--u × 0.13`, bottom `× 0.075` |
| Fondo fuoco | `flames.webp` a `center calc(--u × 0.0412)` / `max(100%, --u × 1.576)` |
| Maschera sul fuoco | `#000 0 → trasparente --u×0.4304 → trasparente --u×0.6906 → #000 --u×1.1209` |
| Box biglietti | `--u × 0.465962` × `--u × 0.7129`, `margin-left: calc(50% - --u×0.5 + --u×0.275938)` |
| Biglietto davanti | left 0, top `0.043192`, `0.330483` × `0.629732` |
| Biglietto dietro | left `0.155062`, top `0.0706`, `0.3133` × `0.6076`, **`rotate(7.16deg)`** |
| Ombre (entrambi) | `drop-shadow(0 --u×0.012 --u×0.03 rgba(0,0,0,0.55))` + `drop-shadow(0 --u×0.032 --u×0.078 rgba(0,0,0,0.45))` |

### Il micro-teatro dei biglietti — la sequenza esatta
```
t=0        HTML: class="tickets is-spread is-locked"   → arrivano separati
t=vista    IntersectionObserver, threshold 0.3
t=+2500ms  via is-spread  → si accavallano, transition 820ms --ease-heavy
t=+3400ms  via is-locked  → solo ORA rispondono al mouse
```
**A cosa serve `is-locked`:** impedire che l'hover parta a metà volo. È il dettaglio che nessuno nota e che tutti sentono.

All'hover:
```css
.ticket--front    → translate(--u×-0.03, --u×0.008) scale(1.05)
.ticket--back     → translate(--u×0.055, --u×-0.02) rotate(8.9deg)   /* da 7.16° */
.ticket--back img → scale(0.95)
```
Il retro **ruota di più mentre la sua immagine si rimpicciolisce**: due trasformazioni contrarie sullo stesso oggetto. È quello che dà la sensazione della carta che si scosta.

**Il riquadro che riceve l'hover è esattamente l'ingombro dei due biglietti**, non la sezione: commento *"so hovering means hovering them and not half the section."*

### Nota di produzione trovata nel codice
```
/* The mockup places these through Canva's own copies of the artwork, which
   carry more transparent margin than the source PNGs in docs/. These rects
   are re-derived so the *printed* ticket lands exactly where the mockup puts
   it — do not "simplify" them back to the PDF's own numbers. */
```
Il PNG esportato da Canva ha margini trasparenti diversi dal sorgente: i rettangoli sono **ricalcolati sul disegno stampato**, non sui numeri del PDF. È il genere di trappola che fa sembrare "quasi giusto" un layout, e qui è documentata perché nessuno la annulli per pulizia.

---

## TAVOLA 4 — I due bottoni, il contatore, il risparmio
![desktop 04](../capture/11-armageddon/desktop-04.png)

### Cosa si vede
Il biglietto scende e **si sovrappone al bottone bianco COMPRA**. Sotto, COSA INCLUDE? in contorno bianco. Poi quattro celle rosse col conto alla rovescia. Poi, in gotico, **Risparmi €585** con la cifra in rosso. In fondo, i nomi dei prodotti in gotico bianco.

### I due bottoni — misurati
| | COMPRA | COSA INCLUDE? |
|---|---|---|
| Larghezza | `var(--btn)` = **288px** (clamp 206→288) | idem |
| Altezza | `calc(--btn × 0.24759)` = **71px** | idem |
| Raggio | `calc(--btn × 0.0528)` = **15,19px** | idem |
| Testo | `calc(--btn × 0.0868)` = **25px**, peso **800** | idem |
| Fondo | `#fff` | `transparent` |
| Testo | `#000` | `#fff` |
| Bordo | nessuno | `max(1px, --btn × 0.0106)` = **3px** `#fff` |
| Margine sopra | `--u × -0.0116` (**negativo**: il biglietto lo copre, come nel mockup) | `--btn × 0.0714` |
| Destinazione | `buy.stripe.com/...` — **diretto al pagamento** | `<dialog>` nativo |
| Hover | fondo → `#bc0807`, testo → `#fff`, `translateY(-1px)` | fondo → `#fff`, testo → `#000` |

**Due cose da notare.**
1. **Anche il raggio è una frazione del bottone** (`× 0.0528`): il bottone che si rimpicciolisce si arrotonda meno. Coerenza che nessun page builder produce.
2. **Il primario è bianco su nero, il secondario è in contorno.** Il rosso del brand **non è sul bottone**: arriva solo all'hover. Il colore dell'azione è tenuto in riserva.
3. **Il margine negativo è intenzionale**: il biglietto deve coprire il bordo superiore del bottone, *"as drawn"*.

### Il contatore
| Elemento | Valore |
|---|---|
| Cella | `var(--cell)` = clamp(56px → **85px**) quadrata |
| Fondo cella | `#bc0807` |
| Raggio | `calc(--cell × 0.075)` = **6,375px** |
| Cifre | `calc(--cell × 0.33318)` ≈ **28,3px**, peso **800**, `font-variant-numeric: tabular-nums` |
| Etichette | `clamp(9px, --cell×0.145, 12px)`, peso 700, `letter-spacing: 0.1em`, maiuscolo, `rgba(255,255,255,0.5)` |
| Spazio fra celle | `calc(--cell × 0.27359)` |
| Scadenza | `data-until="2026-09-11T00:00:00+02:00"` — **su un attributo solo, in un posto solo** |
| Accessibilità | `role="timer"` + `aria-label` **riscritto ogni secondo**: *"Mancano 4 giorni, 17 ore, 11 minuti e 8 secondi"* |

`tabular-nums` è il dettaglio che tiene ferme le cifre mentre scendono. Senza, il contatore trema.

### Il risparmio — e il fatto che si calcola da solo
| Elemento | Valore |
|---|---|
| "Risparmi" | `clamp(30px, --u×0.085, 86px)` ≈ **81,6px**, Curseyt, `#fff` |
| "€585" | stesso corpo, `#bc0807` |
| Sottoriga | `clamp(11px, --u×0.0155, 16px)`, `letter-spacing: 0.05em`, `rgba(255,255,255,0.55)` |

```js
total = Σ [data-price]        // dalle righe della modale
pay   = [data-pack-price]
write('[data-total]', €784); write('[data-pay]', €199); write('[data-save]', €585);
```
**784, 199 e 585 non sono scritti a mano nella pagina.** Sono un solo dato per riga di prodotto, sommato a runtime. Commento: *"so moving one price cannot leave a stale total behind it."*

→ **Questo è il rimedio al difetto n.6 di tutto lo studio siti** (otto cifre per quattro metriche fra le sue vecchie pagine). Lo ha risolto con il codice, non con la disciplina.

---

## TAVOLA 5 — I quattro nomi e l'apertura delle domande
![desktop 05](../capture/11-armageddon/desktop-05.png)

### Cosa si vede
Quattro nomi in gotico bianco, incolonnati e centrati: **outFunnel · outHeadline · outViral**. Poi **"Domande"** in gotico rosso. Poi undici righe separate da filetti sottilissimi, ognuna con un `+` rosso a destra.

### Misure
| Elemento | Valore |
|---|---|
| Nomi prodotto | `clamp(30px, --u × 0.062, 60px)` ≈ **59,5px**, Curseyt, `#fff`, `line-height: 1.1` |
| Spazio fra nomi | `--u × 0.012` |
| Hover nome | `#bc0807` + `underline`, `text-underline-offset: 0.12em` |
| "Domande" | `clamp(34px, --u × 0.075, 72px)` = **72px**, Curseyt, `#bc0807`, centrato |
| Blocco FAQ | `max-width: min(760px, 100%)`, **allineato a sinistra** dentro un footer centrato |
| Filetti | `1px solid rgba(255,255,255,0.15)`, sopra ogni riga + sotto l'ultima |
| Domanda | `clamp(15px, --u × 0.0198, 20px)` = **19px**, peso **700**, `line-height: 1.35`, `#fff` |
| Padding riga | `clamp(15px, 2.2vw, 22px)` verticale |
| Marcatore | `content: "+"` a `1.35em`, `#bc0807` → diventa `"–"` quando aperta |
| Hover domanda | testo → `#bc0807` |

**Struttura: `<details>` / `<summary>` nativi.** Commento: *"so they open with JavaScript off."* Il marcatore di default è spento due volte — `list-style: none` sul summary **e** `::-webkit-details-marker { display: none }` per Safari, perché Safari disegna il suo triangolo se non gli si dice entrambe le cose.

**Il dettaglio di composizione:** le FAQ sono **allineate a sinistra dentro un footer centrato**. Commento: *"because these are read."* Tutto il resto della pagina è centrato perché va guardato; questo blocco è testo, e il testo si legge da un margine fisso.

### L'aberrazione cromatica sulle domande
Guardando da vicino, alcune lettere delle domande hanno una frangia ciano/rossa. Non è un effetto CSS: è **il subpixel rendering** del testo bianco su nero puro reso a `-webkit-font-smoothing: antialiased`. Su fondo `#000` assoluto il fenomeno si vede più che su un grigio scuro.
→ **Lezione:** il nero puro `#000` come fondo di testo lungo è aggressivo. Un `#0a0a0a` ne toglie metà. (Il nostro `bg-ink-2` è già `#0a0a0a` — su questo il nostro sistema è più corretto del suo.)

---

## TAVOLA 6 — La coda delle domande, il disclaimer, la firma
![desktop 06](../capture/11-armageddon/desktop-06.png)

### Cosa si vede
Le ultime domande, poi un filetto, poi il disclaimer legale in grigio piccolo, poi il link privacy sottolineato, poi ragione sociale, P.IVA e indirizzo.

### Misure
| Elemento | Valore |
|---|---|
| Risposte FAQ | `clamp(14px, --u × 0.0172, 17px)` ≈ **16,5px**, `line-height: **1.66**`, `rgba(255,255,255,0.76)`, `max-width: 64ch` |
| `<strong>` dentro le risposte | `#ffffff` pieno |
| Disclaimer | `clamp(11px, --u×0.0125, 13px)` = **12px**, `line-height: 1.75`, `rgba(255,255,255,0.42)`, `max-width: **88ch**`, centrato |
| Separatore | `border-bottom: 1px solid rgba(255,255,255,0.12)` |
| Link privacy | `rgba(255,255,255,0.62)` → hover `#bc0807` |
| Firma | `Andrei Pascu Sales · P.I. 02001850474 · Viale Giacomo Matteotti 15, 50121 Firenze (FI)` |

### Le due misure di lettura
`64ch` per le risposte, **`88ch` per il disclaimer**. Il legale è più largo di proposito. Commento nel CSS:
```
/* It reads as the fine print it is, but it is set wide enough to actually be
   read — the whole point of putting it here. */
```
E sotto, la nota di un bug risolto:
```
/* Written `.legal .legal__disclaimer` rather than `.legal__disclaimer`: the
   plain class loses to `.legal p` above, which is one specificity point
   heavier, and `margin: 0 auto` was being overruled. */
```
**Un problema di specificità CSS documentato nel file**, con la ragione, perché nessuno lo "pulisca" e rompa il centraggio.

### ⚠️ L'unico difetto visivo della pagina
`help@apsales.eu` è `#0000ee` — il blu di default del browser per i `mailto:`. **È l'unico colore fuori dalla tavolozza in 5.103 pixel.** In una pagina di due colori si vede come una macchia.
→ Una riga di CSS. Non l'ha scritta.

---

## TAVOLE MOBILE — cosa cambia davvero
![mobile 01](../capture/11-armageddon/mobile-01.png)
![mobile 02](../capture/11-armageddon/mobile-02.png)
![mobile 03](../capture/11-armageddon/mobile-03.png)

**Altezza mobile: 2.830px contro 5.103px desktop.** Nessun contenuto tagliato: la composizione è la stessa, scalata.

**C'è un solo media query in tutto il CSS** (`max-width: 720px`), e cambia cinque cose:

| # | Cosa cambia | Perché |
|---|---|---|
| 1 | Video a **tutta larghezza**, `border-radius: 0` | All'inset desktop il player starebbe al 76% dello schermo con margini disuguali. *"the video is the page's whole job here, so it gets the whole width"* |
| 2 | `.stage` da `1.0866` a **`1.28`** | Il player a tutta larghezza è più alto (56% della colonna invece di 43%): senza, la scritta sopra e "Sei pronto?" sotto ci finirebbero addosso |
| 3 | "Guarda il video" da `0.098` a **`0.125`** | Sul telefono la colonna è lo schermo, quindi la stessa frazione viene piccola in assoluto |
| 4 | Freccia da `0.21` a **`0.28`** | idem |
| 5 | "Sei pronto?" da `0.86487` a **`0.99`** | in un blocco `@media` **separato e più in basso nel file** — stessa specificità, decide l'ordine. Il commento lo spiega |

**Ogni numero è dichiarato come misurato a 390px:** *"callout ends 9px above the player, the player ends 25px above the question, and the question ends inside the section."*

**E i due pavimenti in `clamp()`** (`--btn`, `--cell`) esistono solo per il telefono: ai suoi rapporti esatti il bottone verrebbe 117×29px con testo da 10px. Commento: *"Andrei's note on AP-138: the type scale is his rough pass, fix it."*
→ **Il committente ha sbagliato la scala, l'agente l'ha corretta e ha scritto perché.** Questo è il livello di collaborazione uomo-agente che vogliamo.

---

## RIEPILOGO — l'inventario del cantiere

### Colori (tutti)
| Hex | Uso |
|---|---|
| `#000000` | fondo di tutto |
| `#bc0807` | l'unico colore: gotico, celle contatore, marcatori `+`, hover, scrollbar |
| `#ffffff` | testo primario, fondo del bottone che incassa |
| `#ffffff @0.78 / 0.76 / 0.62 / 0.55 / 0.5 / 0.42` | scala di gerarchia — **più vicino al denaro, più opaco** |
| `#e50c0a` | hover della scrollbar (unico rosso secondario) |
| ~~`#0000ee`~~ | ⚠️ difetto: `mailto` non stilizzato |

### Caratteri
| Famiglia | Usi | Ruolo |
|---|---|---|
| Curseyt (blackletter, self-hosted `.woff`, `font-display: block`) | 12 | **grida** — titoli, prezzi, nomi prodotto |
| Plus Jakarta Sans 400/700/800 (Google Fonts, `display=swap`) | 59 | **spiega** — tutto il resto |

### Curve
| Token | Valore | Dove |
|---|---|---|
| `--ease-land` | `cubic-bezier(0.16, 0.86, 0.3, 1)` | ingressi, hover della testata |
| `--ease-heavy` | `cubic-bezier(0.65, 0, 0.25, 1)` | i biglietti (820ms) |

### Animazioni
| Nome | Durata | Delay | Cosa |
|---|---|---|---|
| `ag-zoom` | 1700ms | 0 | ritratto `scale(1.055)` → 1 |
| `ag-fade` | 1400ms | 120ms | splatter opacità |
| `ag-rise` (a) | 1200ms | 180ms | "Armageddon" |
| `ag-rise` (b) | 1200ms | 340ms | "is here" |
| ticket settle | 820ms | 2500ms dalla vista | i biglietti si accavallano |
| ticket unlock | — | +900ms | l'hover si accende |
| parallax | continuo | — | 4 velocità in rAF |

### Comportamenti nativi usati al posto di librerie
`<dialog>` + `showModal()` + `::backdrop{backdrop-filter:blur(4px)}` · `<details>`/`<summary>` · `scrollbar-gutter: stable` · `container-type: inline-size` con `@supports` · `prefers-reduced-motion` che spegne **anche il JavaScript** · `IntersectionObserver` · `fetchpriority="high"` sull'immagine dell'hero, `loading="lazy"` su tutto il resto · `<link rel="preload">` sul font gotico.

---

## Connessioni
- `11-armageddon.md` — il rapporto strategico su questa stessa pagina
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — dove questo inventario diventa un sistema
- `.claude/skills/empire-premium-style/references/design-tokens.css` — i nostri token, da confrontare riga per riga con quelli qui sopra
