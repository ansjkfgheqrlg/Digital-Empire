---
Type: PROJECT
Status: Active
Tags: #fabbrica-siti #design-system #andrei-pascu #emperator #workflow #piano
Created: 2026-09-06
Last updated: 2026-09-06
Dossier: 32
---

# DOSSIER 32 — LA FABBRICA SITI

## Il sistema unico di Digital Empire per produrre qualunque sito o landing page, vivo dentro Emperator e fuori come workflow

> **Ordine di Max, 6 settembre 2026:** *"Tu devi avere un sistema per la produzione di tutti i siti futuri. Consistente. Va a prendere tutti i nostri standard, la nostra qualità, le nostre performance, le nostre capacità di fare siti e quelle di Andrei, sia in grafica che in copy. Questo sistema deve essere vivo e attivo dentro di te, Emperator, e anche al di fuori di te come workflow dentro Digital Empire."*

---

## 0. LA VERITÀ PRIMA DEL PIANO

Max ha chiesto: *"se tutto questo non è stato fatto, sviluppa un piano perché sia così."*

**Non è stato fatto.** Ecco la misura esatta, contata sul disco oggi.

### 0.1 Oggi esistono QUATTRO sistemi per fare siti, e si contraddicono

| Sistema | Dove | Righe | Stack imposto |
|---|---|---|---|
| `empire-premium-style` | `.claude/skills/empire-premium-style/` | 135 + references | **Next.js 16 + Tailwind v4 + Lenis + Framer + GSAP** — "Mai HTML/CSS statico" |
| `website-creator` | `.claude/skills/website-creator/` | SKILL + agenti + knowledge | **"Sempre e solo vanilla HTML+CSS+JS in un singolo file. Zero framework."** |
| Suite `site-*` | `.claude/skills/site-brief` … `site-deploy` | **15 skill, 4.052 righe** | `site-stack` e `site-premium-stack` dicono cose diverse dalle due sopra |
| Agente `site-premium-builder` | `.claude/agents/` | — | **Next.js 15** + shadcn + Radix + Headless UI + Chakra + Three.js + Theatre.js + anime.js |

Le prime due si contraddicono **frontalmente**: una vieta l'HTML statico, l'altra vieta i framework. Entrambe si dichiarano obbligatorie. La quarta impone una versione di Next diversa dalla prima e cinque librerie UI in contemporanea.

**Conseguenza operativa reale:** quale sistema parte dipende da quale frase Max pronuncia. Non da quale lavoro va fatto. Questo non è un sistema: sono quattro opinioni con lo stesso grado.

### 0.2 Niente di quello che abbiamo imparato da Andrei è dentro il codice

Lo studio siti ha prodotto **10 rapporti, 2.362 righe, 371 screenshot, 1.832 blocchi di copy analizzati**. Ha trovato 10 scoperte trasversali e, con `armageddon`, 12 mosse concrete.

**Zero di queste sono dentro una skill.** Vivono in `competitor/Andrei Pascu/site-study/reports/`, che nessun agente legge quando costruisce. Il lavoro di tre mesi è archiviato, non operativo.

### 0.3 Manca il pezzo che rende un sistema un sistema

Non esiste, in nessuno dei quattro:
- una **legge scritta** che decida chi vince quando due regole si scontrano;
- un **canone di misura** unico (i token esistono in `empire-premium-style/references/design-tokens.css`, ma nessun altro sistema li legge);
- un **gate a macchina** che blocchi una consegna fuori canone;
- un **anello di ritorno**: nessun sito costruito ha mai migliorato il sistema che l'ha costruito.

### 0.4 E c'è la scoperta che cambia il piano

`armageddon.bsns.it` è servito con il CSS in chiaro e commentato. I commenti citano:

- `docs/homepage-design/full-page-mockup.pdf` — 826,46 × 2.851,92 unità
- `CLAUDE.md §4` — *"CLAUDE.md says his design wins here"*
- `assets/brand.css` — un brand file di casa, derogato per scelta dichiarata
- `AP-138` — un ticket
- *"Andrei asked on 5 September"* — richieste datate dentro il codice

**Andrei Pascu costruisce le sue landing con Claude Code, con un CLAUDE.md numerato, un brand.css, un mockup PDF misurato e un ticket system.** Con il nostro stesso strumento.

Non siamo indietro sul gusto. Siamo indietro sull'**impianto**: lui ha una legge scritta che l'agente cita per giustificare una deroga, noi abbiamo quattro skill che si smentiscono.

Rapporto completo: [`competitor/Andrei Pascu/site-study/reports/11-armageddon.md`](../competitor/Andrei%20Pascu/site-study/reports/11-armageddon.md)
Inventario visivo: [`…/11-armageddon-ATLANTE-VISIVO.md`](../competitor/Andrei%20Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md)

---

## 1. COSA DEVE ESSERE LA FABBRICA

Un organo solo, con **due bocche**:

| | Dentro Emperator | Fuori, in Digital Empire |
|---|---|---|
| **Cos'è** | §6.20 di `emperator.md` — la legge che Emperator conosce a memoria | `.claude/skills/fabbrica-siti/` — il flusso che chiunque può lanciare |
| **A cosa serve** | Emperator sa **sempre** come si fa un sito Empire, anche in mezzo a un'altra conversazione | Max, Gael o Neri scrivono `/fabbrica-siti <brief>` e la macchina esegue |
| **Chi lo aggiorna** | Ogni sito costruito, via anello di ritorno | idem, stesso file |

**Una sola fonte di verità.** La skill è il corpo, `emperator.md §6.20` è il riassunto operativo che punta al corpo. Come già fatto per il PDF (§6.19 → `pdf_engine_empire.py`).

---

## 2. ARCHITETTURA — sei livelli

```
LIVELLO 0 — LA LEGGE          CLAUDE-SITI.md          chi vince quando due regole si scontrano
LIVELLO 1 — IL CANONE         canone.css + canone.json  ogni misura, ogni colore, una volta sola
LIVELLO 2 — I PATTERN         pattern/*.md            le sezioni, con le misure e il perché
LIVELLO 3 — IL FLUSSO         FLUSSO.md               9 passi dal brief al deploy
LIVELLO 4 — I GATE            gate_siti.py            la macchina che blocca la consegna
LIVELLO 5 — LA MEMORIA        cantieri/               ogni sito costruito torna dentro il canone
```

---

### LIVELLO 0 — LA LEGGE (`CLAUDE-SITI.md`)

Copia diretta della mossa di Andrei, migliorata: **articoli numerati e citabili**, così un agente può scrivere *"deroga concessa da §4"* e la deroga è tracciabile invece che arbitraria.

Bozza degli articoli:

| § | Articolo | |
|---|---|---|
| **§1** | **Il canone vince sul gusto.** Colori, misure, curve e caratteri vengono da `canone.css`. Nessun agente inventa un valore. | non derogabile |
| **§2** | **La colonna vince sul breakpoint.** Ogni misura è una frazione di `--u`. I media query esistono solo dove una frazione produrrebbe un elemento non leggibile o non toccabile, e vanno **motivati in un commento con la misura reale**. | non derogabile |
| **§3** | **Il copy prima del layout.** Nessuna sezione si disegna prima che il suo testo esista. | non derogabile |
| **§4** | **Il design del committente vince sul brand di casa**, se il committente ha un design. La deroga si dichiara nel CSS, con la ragione. *(l'articolo di Andrei, preso di peso)* | derogabile solo verso l'alto |
| **§5** | **La corsia si sceglie dal lavoro, non dal gusto.** Vedi §3 di questo dossier. | non derogabile |
| **§6** | **Ogni numero non ovvio va commentato con la sua origine.** *"letto dal mockup a pagina 2"*, *"misurato a 390px"*. Un numero senza origine è un errore in attesa. | non derogabile |
| **§7** | **Niente animazione senza `prefers-reduced-motion`**, e deve spegnere anche il JavaScript. | non derogabile |
| **§8** | **Nessun dato duplicato in pagina.** Prezzi, totali, conteggi: un dato solo, il resto calcolato. | non derogabile |
| **§9** | **Il gate decide, non l'agente.** Una consegna che non passa `gate_siti.py` non è consegnata. | non derogabile |
| **§10** | **Ogni cantiere lascia una lezione.** Nessun sito è finito finché la sua riga non è in `cantieri/`. | non derogabile |

---

### LIVELLO 1 — IL CANONE (`canone.css` + `canone.json`)

Un file CSS per il browser, un JSON gemello per gli agenti e per il gate. **Generati dallo stesso sorgente**, così non possono divergere.

Contenuto, fuso dalle due scuole:

| Blocco | Da noi | Da Andrei |
|---|---|---|
| **Colori** | palette ink/paper/grey/silver, `#fb4604` come colore dell'azione | **la scala di opacità come gerarchia** — 0.42 → 0.5 → 0.55 → 0.62 → 0.76 → 1, *"più vicino al denaro, più opaco"* |
| **Misura** | — | **`--u`, la colonna di progetto.** Tutto è `calc(var(--u) * frazione)`. `--col` per il bordo sinistro. Container query con fallback `vw` |
| **Pavimenti** | — | **`clamp()` solo su ciò che si tocca o si legge** (`--btn`, `--cell`), motivato con la misura reale a 390px |
| **Tipografia** | Onest variabile 300-800, `ss01 cv11`, tracking -0.025em | **due famiglie e basta: una che grida, una che spiega.** `font-display: block` quando il carattere *è* il design |
| **Raggi** | scala fissa | **il raggio è una frazione dell'elemento** (`calc(var(--btn) * 0.0528)`), non un valore assoluto |
| **Curve** | — | `--ease-land` `cubic-bezier(0.16,0.86,0.3,1)` per gli ingressi · `--ease-heavy` `cubic-bezier(0.65,0,0.25,1)` per gli oggetti pesanti |
| **Grana** | `.grain-fine` doppio layer SVG, blend overlay + hard-light | — (lui non ce l'ha: **è nostra e resta**) |
| **Fondo del testo lungo** | `#0a0a0a` | ⚠️ lui usa `#000` puro e il testo bianco ci sfrangia — **su questo il nostro canone è più corretto del suo, e resta il nostro** |

---

### LIVELLO 2 — I PATTERN (`pattern/*.md`)

Non "ispirazioni": **schede con le misure**, come l'atlante visivo di armageddon. Ogni scheda: a cosa serve, la struttura HTML, le misure in frazioni di `--u`, gli effetti con i tempi esatti, quando **non** usarla.

Il catalogo di partenza — 11 nostri + 9 suoi:

| Pattern | Origine |
|---|---|
| `hero-dark-chips`, `stats-3-cards`, `features-paper`, `timeline`, `value-stack`, `chi-sono-split`, `testimonials-3`, `faq-accordion`, `is-for-dual`, `cta-final-bracketed`, `footer-ink-2` | nostri, già in `empire-premium-style/references/section-patterns.md` |
| **`hero-titolo-due-strati`** — pieno dietro il soggetto + contorno davanti | armageddon §6.1 |
| **`cucitura-fotografica`** — due sezioni, una fotografia, agganciate sullo stesso valore di opacità | armageddon §6.5 |
| **`oggetto-che-si-posa`** — arriva sparso, si compone dopo 2,5s dalla vista, e solo dopo risponde al mouse (`is-locked`) | armageddon §6.4 |
| **`contatore-scadenza`** — scadenza su un attributo solo, `tabular-nums`, `aria-label` riscritto ogni secondo | armageddon §6.7 |
| **`prezzo-che-si-somma`** — `data-price` sulle righe, totale e risparmio calcolati a runtime | armageddon §6.6 |
| **`faq-native`** — `<details>` che funziona senza JS, marcatore `+` → `–` | armageddon §6.8 |
| **`modale-nativa`** — `<dialog>` + `::backdrop` sfocato + chiusura al click fuori | armageddon §6.8 |
| **`tabella-comparativa`** | apsales §6.7 |
| **`colonne-speculari-problema-soluzione`** 1:1 | apsales §6.4 |

---

### LIVELLO 3 — IL FLUSSO (`FLUSSO.md`) — 9 passi

Nessun passo è opzionale. Ogni passo ha un artefatto su disco.

| # | Passo | Artefatto | Chi |
|---|---|---|---|
| **1** | **BRIEF** — cosa vende, a chi, **quanto è caldo il traffico**, cosa deve succedere | `cantieri/<nome>/BRIEF.md` | Emperator con Max |
| **2** | **CORSIA** — A o B, decisa dalla regola §3, scritta e motivata | riga in `BRIEF.md` | automatico |
| **3** | **COPY** — il testo di ogni sezione, prima di qualunque pixel (§3 della legge) | `COPY.md` | `cro-copy-architect` + standard FAQ di Andrei |
| **4** | **MOCKUP MISURATO** — la composizione con le sue proporzioni. Se c'è un PDF/Figma del committente, si misura; se non c'è, si disegna in unità | `MOCKUP.md` con la tabella delle frazioni | Emperator |
| **5** | **CANONE APPLICATO** — token risolti, pattern assegnati sezione per sezione | `MAPPA-PATTERN.md` | automatico |
| **6** | **BUILD** — il codice, con ogni numero non ovvio commentato con la sua origine (§6) | il sito | corsia A o B |
| **7** | **GATE** — `python scripts/gate_siti.py <cantiere>` | `GATE.md` PASS/FAIL | macchina |
| **8** | **QA REALE** — Playwright: cattura a 1440 e 390, confronto col mockup, Lighthouse, tastiera, `prefers-reduced-motion` | `QA.md` + screenshot | macchina |
| **9** | **LEZIONE** — cosa ha funzionato, cosa no, cosa entra nel canone | `cantieri/<nome>/LEZIONE.md` + patch al canone | Emperator |

---

### LIVELLO 4 — I GATE (`scripts/gate_siti.py`)

**Deterministico, non a giudizio.** Il modello dell'hook che già sorveglia il battito.

| # | Controllo | Fallisce se |
|---|---|---|
| 1 | **Colori fuori canone** | un hex nel CSS non è in `canone.json` (e non è dichiarato come deroga §4) |
| 2 | **Misure assolute** | un `px` fuori da `clamp()`, `border`, `outline` o da un commento con origine |
| 3 | **Breakpoint non motivati** | un `@media` senza commento che dichiari la misura reale |
| 4 | **Dato duplicato** | lo stesso prezzo/numero scritto più di una volta nel sorgente |
| 5 | **Motion** | esiste un'animazione e manca `prefers-reduced-motion`, o il blocco non spegne anche il JS |
| 6 | **Accessibilità** | contrasto sotto 4.5:1 su testo <24px · `alt` mancante · nessun `:focus-visible` · timer senza `aria-label` |
| 7 | **Colori di default** | un `mailto:`/link non stilizzato — *il difetto n.1 di armageddon, che noi non ripetiamo* |
| 8 | **Meta e dati strutturati** | manca `canonical`, `og:image` 1200×630, o `FAQPage` JSON-LD quando esistono FAQ — *il difetto n.4 di armageddon* |
| 9 | **Peso** | corsia A oltre 250 KB al primo carico, font esclusi |
| 10 | **Scadenze** | un contatore senza comportamento dichiarato a scadenza scaduta — *il difetto n.2 di armageddon* |

I controlli 7, 8 e 10 nascono direttamente dai difetti misurati sulla sua pagina: **il sistema impara anche dai suoi errori, non solo dalle sue mosse.**

---

### LIVELLO 5 — LA MEMORIA (`cantieri/`)

Una cartella per sito. Dentro: brief, copy, mockup, gate, QA, lezione. E un `INDICE.md` con una riga per cantiere.

**L'anello di ritorno, che oggi non esiste da nessuna parte:** al passo 9, se una soluzione ha funzionato due volte in due cantieri diversi, **diventa un pattern**; se ha fallito due volte, **diventa un controllo del gate**. Il sistema si stringe da solo.

---

## 3. LA DECISIONE DIFFICILE — quale stack

È il nodo vero, ed è il punto dove i quattro sistemi attuali si sono schiantati. La affronto in chiaro invece di scegliere un vincitore per gusto.

**I fatti:**
- `armageddon.bsns.it`: zero framework, 1 CSS scritto a mano, 5,6 KB di JS, nessun build. **Funziona senza JavaScript.** Visivamente non gli manca niente.
- `ccm-premium` / `empire-premium-style`: Next.js 16 + Tailwind + Lenis + Framer + GSAP. Ci dà componenti, rotte, dati, form, aree riservate.

Non esiste un vincitore assoluto: **fanno due mestieri diversi**.

### La regola, e si applica sola

> **Corsia A — PAGINA.** ≤ 3 pagine **e** nessuno stato lato server (niente login, niente form che scrive, niente dati che cambiano da soli).
> → **HTML + CSS + JS vanilla, colonna `--u`, zero build, zero dipendenze.**
> Lanci, landing singole, one-pager, pagine di vendita, pagine evento.

> **Corsia B — SITO.** Tutto il resto.
> → **Next.js 16 + Tailwind v4 + Lenis + Framer + GSAP**, gli stessi token.
> Siti multi-pagina, LMS, aree riservate, dashboard, e-commerce.

**Entrambe leggono lo stesso `canone.css` e gli stessi pattern.** Il canone è uno, la resa è due. Una pagina di Corsia A e una di Corsia B messe fianco a fianco devono sembrare la stessa mano — perché lo sono.

**Perché così e non altrimenti:** oggi mandiamo in produzione una landing di lancio con `npm install`, un build step e sette dipendenze che invecchiano. È peso che paghiamo per sempre su un artefatto che vive tre settimane. Andrei ha dimostrato — misurato, non opinato — che quella stessa pagina si fa meglio senza. Ma un LMS in HTML statico è masochismo, e `website-creator` che lo impone va corretto.

**Costo ombra della scelta:** due corsie significano due implementazioni per ogni pattern nuovo. Mitigazione: il pattern si scrive **prima in vanilla** (corsia A) e la corsia B lo avvolge in un componente. Mai il contrario — dal vanilla al framework si sale, dal framework al vanilla si riscrive.

---

## 4. COSA SI FONDE E COSA SI RITIRA

| Sistema attuale | Destino |
|---|---|
| `empire-premium-style` | **Diventa la Corsia B.** Perde il divieto "mai HTML statico" (§5 della legge decide). Token e pattern migrano nel canone |
| `website-creator` | **Diventa la Corsia A.** Perde il divieto "zero framework". La sua Legge Cosmica #0 (silver mixing) e la grana entrano nel canone |
| Suite `site-*` (15 skill) | **Assorbita nei 9 passi.** `site-brief`→1 · `site-copy`→3 · `site-design`→4 · `site-architecture`+`site-plan`→5 · `site-build`+`site-components`+`site-animate`+`site-3d`→6 · `site-qa`+`site-seo`→7-8 · `site-report`→9 · `site-deploy`→9. Le skill restano come riferimento, **smettono di essere punti d'ingresso** |
| `site-premium-builder` (agente) | **Allineato alla Corsia B.** Via le librerie UI in concorrenza (shadcn + Radix + Headless + Chakra insieme non è uno stack, è un ripostiglio) |
| `.claude/skills/empire-studio/` (copia doppia) | ⚠️ **problema separato ma bloccante**: l'albero Empire Studio esiste in due copie reali. Va risolto prima, o il canone finirà anch'esso in due copie |

---

## 5. IL PIANO DI COSTRUZIONE — 5 fasi

Ogni fase è chiudibile da sola e lascia qualcosa di usabile. Ciclo a 9 passi (ADR-006) su ognuna.

### FASE 1 — LA LEGGE E IL CANONE *(la fondazione, niente parte prima)*
1. `CLAUDE-SITI.md` — i 10 articoli
2. `canone.css` + `canone.json` — fusione dei token nostri + le 7 regole di misura di Andrei
3. ADR-0XX in `company/Memory/decisions/` — **la decisione delle due corsie**, così nessuna sessione futura la rimette in discussione a braccio
**Esito:** esiste una legge citabile. **Senza questa fase, tutto il resto ricrea il problema.**

### FASE 2 — I PATTERN
4. `pattern/` — 11 nostri portati dentro + **9 di Andrei scritti da zero** dall'atlante visivo
5. Ogni scheda: struttura, misure in frazioni, effetti con tempi, quando non usarla
**Esito:** un catalogo che un agente può applicare senza inventare.

### FASE 3 — IL FLUSSO E LA SKILL
6. `.claude/skills/fabbrica-siti/SKILL.md` — i 9 passi, i due binari di corsia
7. `emperator.md §6.20` — il riassunto operativo che punta alla skill (**una fonte sola**, come §6.19 per il PDF)
8. `cantieri/INDICE.md` + i template degli artefatti
**Esito:** `/fabbrica-siti <brief>` esiste e gira. Emperator lo sa a memoria.

### FASE 4 — I GATE E IL QA
9. `scripts/gate_siti.py` — i 10 controlli
10. `scripts/qa_sito.py` — Playwright: cattura 1440+390, confronto col mockup, Lighthouse, tastiera, reduced-motion
**Esito:** una consegna fuori canone **non parte**. Come il battito.

### FASE 5 — IL COLLAUDO SU LAVORO VERO
11. Primo cantiere di prova in Corsia A: **rifare `armageddon` con il nostro canone**, stessa struttura, nostro linguaggio visivo. È il confronto più onesto possibile — stesso lavoro, due mani.
12. Primo cantiere in Corsia B su un sito Empire reale
13. `LEZIONE.md` di entrambi → prima patch al canone
**Esito:** il sistema ha prodotto, si è corretto, ed è vivo.

---

## 6. COSA PRENDIAMO DA CHI — il bilancio onesto

### Da Andrei, 12 cose

| # | Cosa | Dove va |
|---|---|---|
| 1 | La colonna `--u` — tutto è una frazione, la pagina scala come un'immagine | Canone |
| 2 | Il prezzo che si somma dal DOM | Pattern + Gate §8 |
| 3 | Il titolo in due strati | Pattern |
| 4 | La cucitura fotografica sullo stesso valore di opacità | Pattern |
| 5 | `is-locked` — l'hover non risponde finché l'ingresso non è finito | Canone, regola di interazione |
| 6 | Il contatore accessibile con la scadenza su un attributo solo | Pattern |
| 7 | `<details>` e `<dialog>` nativi | Corsia A, standard |
| 8 | `font-display: block` quando il carattere è il design | Canone |
| 9 | FAQ che rispondono contro il proprio interesse (6 su 11) | Standard di copy |
| 10 | Il testo che spiega il timer | Standard di lancio |
| 11 | Le negazioni che chiudono le contestazioni prima del pagamento | Standard legale |
| 12 | **Il CLAUDE.md numerato e citabile** | Livello 0 — **la cosa più importante di tutte** |

### Da noi, 8 cose che lui non ha

| # | Cosa | Perché la teniamo |
|---|---|---|
| 1 | **La grana** doppio layer SVG | Firma visiva Empire, lui non ce l'ha |
| 2 | **Silver mixing** — nessun colore puro | Il suo `#bc0807` è puro e su nero puro sfrangia |
| 3 | **`#0a0a0a` invece di `#000`** per il testo lungo | Misurato: il nero assoluto aggredisce l'antialiasing |
| 4 | **Onest variabile** con `ss01 cv11` | Più flessibile delle sue due famiglie fisse |
| 5 | **Sezioni a fondo alternato** ink → paper → grey | Lui è monocromatico: regge su una pagina, non su un sito |
| 6 | **APSOC** come struttura di copy | Lui ce l'ha come framework insegnato, noi come skill che esegue |
| 7 | **Corsia B** — Next.js per ciò che ha stato | Lui non ha mai fatto un LMS |
| 8 | **Il gate a macchina** | Lui si affida alla disciplina. Noi no: la disciplina si stanca |

---

## 7. RISCHI E OBIEZIONI — prima che le faccia qualcun altro

| Obiezione | Risposta |
|---|---|
| *"Due corsie sono di nuovo due sistemi, hai ricreato il problema"* | No: i quattro sistemi attuali si contraddicono **sulla stessa domanda**. Le due corsie rispondono a **domande diverse**, con **un canone solo** e una regola di scelta che si applica da sé. Se un giorno una corsia non serve più, muore senza toccare il canone |
| *"Copiare `--u` da Andrei ci rende suoi imitatori"* | `--u` non è uno stile, è **un sistema di misura**. Come usare il metro. Lo stile resta nostro: grana, silver mixing, Onest, fondi alternati |
| *"Cinque fasi sono troppe, serve un sito adesso"* | Le fasi 1 e 2 sono ~1 giornata di lavoro e da sole rendono coerente qualunque sito costruito da lì in poi. Il gate può arrivare dopo |
| *"Il gate rallenterà tutto"* | Il gate del battito ha smesso di farmi sbagliare la forma dal giorno uno. Un gate deterministico non rallenta: **toglie il ripasso** |
| **L'obiezione più forte:** *"Il vero problema non è che manca il sistema — è che DE ha prodotto 25 pezzi finiti mai pubblicati (ADR-016, ULTIMO METRO). Un sistema di siti perfetto produrrà siti perfetti mai messi online"* | **È fondata.** Mitigazione dentro il piano: il passo 9 non è "consegna", è **deploy + lezione**. Un cantiere senza URL vivo resta aperto nell'indice e appare nel battito finché non chiude. Il sistema misura le pubblicazioni, non le build |

---

## 8. LA PRIMA MOSSA

**Fase 1, punto 1: `CLAUDE-SITI.md`.**

Non il canone, non i pattern, non la skill: **la legge**. È l'unica cosa che, se manca, fa ricadere tutto il resto nel problema di partenza — regole che si contraddicono senza un arbitro.

È anche il pezzo che Andrei ha e noi no, ed è il motivo per cui la sua pagina è meglio costruita della nostra skill di punta.

---

## Connessioni
- [`competitor/Andrei Pascu/site-study/reports/11-armageddon.md`](../competitor/Andrei%20Pascu/site-study/reports/11-armageddon.md) — il rapporto che ha originato questo dossier
- [`…/11-armageddon-ATLANTE-VISIVO.md`](../competitor/Andrei%20Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md) — le misure da cui nasce il canone
- [`competitor/Andrei Pascu/site-study/README.md`](../competitor/Andrei%20Pascu/site-study/README.md) — le 10 scoperte trasversali dei 9 siti precedenti
- `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` — il ciclo a 9 passi (ADR-006) con cui si costruisce ogni fase
- `company/Memory/decisions/` — dove andrà l'ADR delle due corsie
- ADR-016 / ULTIMO METRO — il rischio che questo dossier deve evitare di alimentare
