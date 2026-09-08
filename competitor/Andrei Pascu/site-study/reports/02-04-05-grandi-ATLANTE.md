---
Type: SYNTHESIS
Status: Active
Tags: #competitor #andrei-pascu #atlante-visivo #design-system #reference #onda-c #prezzo-composizione
Created: 2026-09-08
Last updated: 2026-09-08
---

# ATLANTE VISIVO — le tre pagine più grandi dell'ecosistema Andrei Pascu

**outFunnel (98€) · Funnel Operator (434€) · Copywriting Mentorship (05-copy, 999€).** Ogni misura di
questo documento viene da `scheda.json` (campionato dal DOM al momento della cattura v2). Le tavole
descritte come "viste" sono state aperte una per una con lo strumento di visione dentro
`../capture/<pagina>/sezioni/`; le sezioni non riportate come tavola sono comunque in tabella con i
loro numeri (fonte: `scheda.json`), ma la loro composizione visiva non è stata verificata a occhio in
questa passata — dichiarato esplicitamente dove capita, mai stimato.

Questo documento non ripete il copy: per quello vedi `05-copy-COPY.md`, `02-funnel-operator-COPY.md`,
`04-outfunnel-COPY.md`. Qui si tratta solo la composizione visiva — misure, media, effetti, perché.
Modello di forma: [13-apsales-ATLANTE.md](13-apsales-ATLANTE.md).

Le tre pagine sono la stessa piattaforma Squarespace (`www.andrei-copy.com`, `costruzione: squarespace`
in tutti e tre gli `scheda.json`), stesso footer, stessa palette base (`bg-void` `#111111`/`#1b1b1d`/
nero, testo `#fafafa`, accento blu `#0062ff`). Le differenze che seguono non sono di piattaforma, sono
di scelta editoriale — ed è esattamente il punto di questo atlante.

| | outFunnel | Funnel Operator | Copywriting Mentorship |
|---|---|---|---|
| Prezzo | **98€** | **434€** | **999€** (349€ versione Base) |
| URL | `/outfunnel` | `/funnel-operator` | `/copy` |
| Altezza pagina | 26.993px | 24.019px | 26.952px |
| Sezioni totali / distinte | 24 / 16 | 28 / 16 | 28 / 20 |
| `animazioni` dichiarate (scheda.json→effetti) | `[]` — nessuna | `[]` — nessuna | `image-fade-in 0.6s cubic-bezier(0.4,0,0.2,1)` ×5, `pulse 2s ease` |
| `filtri` (backdrop) | `blur(10px)`×4, `blur(6px)` | `blur(15px)`×7, `blur(20px)` | `blur(15px)` |
| Raggi ricorrenti | 10px | 10px, 50%×12 | 50%×18, 4px |

La riga "animazioni" è già la prima risposta alla domanda sul prezzo: **delle tre pagine, solo quella
da 999€ ha keyframe CSS reali dichiarati nel DOM.** Le altre due hanno l'array vuoto — qualsiasi
movimento che si vede negli screenshot (freccette, hover) è micro-interazione via `transizioni`, non
animazione dichiarata.

---

## PARTE 1 — outFunnel, 98€ (h=26.993px, 24 sezioni/16 distinte)

### Tavola O1 — L'hero: tre modi di fare un funnel
![sezione 01](../capture/04-outfunnel/sezioni/01-alcuni-fanno-questo-funnel.png)

**Ruolo**: apertura, non vende ancora — insegna a distinguere un funnel scadente da uno buono.
**Altezza**: 1.330px — **4,9%** della pagina.

**Cosa la compone**: tre diagrammi tecnici in sequenza verticale su fondo quasi nero (`transparent`
che eredita `bg-void`): un funnel a imbuto a 3 step (teal), un diagramma a nodi con 5 step e 2 rami
condizionali (Step A/Step B in viola), e la scritta finale "Quello che funziona." con un glow ciano.
`blocchi_testo: 5`, `parole: 14` — quasi nessun testo, il lavoro lo fa il diagramma. `media: 6`.
Firma: `section|page-section.has-section-divider.full-bleed-section|3|M|-|7`, gruppo 1, rappresentante.

**Difetto di cattura osservato**: nello screenshot compare in overlay, sopra l'hero, una barra di
navigazione scura con scritta "Claude Speedrun" a sinistra e "Accedi" a destra — non è un elemento di
questa pagina (outFunnel non ha nulla a che fare con "Claude Speedrun", che è un'altra pagina dello
stesso ecosistema, vedi report `12-claude-speedrun-ATLANTE.md`). È verosimilmente un artefatto dello
strumento di cattura (una barra sticky di un'altra tab/sessione rimasta agganciata al viewport).
**Non è un elemento del sito outFunnel**: va scartato se si replica questa sezione.

**Effetti attivi**: nessun filtro dichiarato su questa sezione specifica; il glow sul testo finale è
coerente con le `ombre` di pagina (`rgba(0,0,0,0.2) 0px 4px 8px 0px`).

**Perché è costruita così**: prima di vendere outFunnel, la pagina vuole che il lettore riconosca il
proprio funnel come "quello sbagliato" — un diagramma tecnico (non un'affermazione) costringe il
lettore a confrontare la propria situazione con lo schema, non con un'opinione dell'autore.

---

### Tavola O2 — Il div "border" che in realtà è testo pieno (difetto di classificazione)
![sezione 02](../capture/04-outfunnel/sezioni/02-div.png)

**Ruolo**: transizione/obiezione — introduce il concetto di "funnel strategico" prima di nominarlo.
**Altezza**: 696px — **2,6%**.

**Cosa la compone secondo scheda.json**: `tag: div`, `classi: section-border`, `bg: #a8a8a8` (il grigio
"stiamo aggiornando il brand", non uno sfondo scuro), `blocchi_testo: 0`, `parole: 0`, `media: 1`.
Firma `div|section-border|1|M|-|3`, gruppo 2 (condiviso con le sezioni 06/13/20, altre varianti dello
stesso "div separatore" più avanti nella pagina).

**Cosa mostra davvero lo screenshot**: un titolo su tre righe ("Perché non venderai solo perché il
funnel è lungo… O corto. Venderai solo se strategizzi:"), tre righe con spunta verde ("Il funnel
giusto" / "Nel momento giusto" / "Per le persone giuste"), un secondo paragrafo-titolo e una riga di
setup ("Che ho creato questa pagina per avvisarti, prima che sia troppo tardi.") più una freccia SVG di
scroll. **Questo è il difetto reale, più significativo del "media vuoto" cercato**: `scheda.json`
dichiara `blocchi_testo: 0` e `parole: 0` per una sezione che contiene visivamente ~35 parole di copy
persuasivo vero. Il motivo tecnico più probabile: il testo qui è dentro un layer con opacità animata
in ingresso (fade-in via IntersectionObserver, tipico dei "reveal" Squarespace) che al momento dello
scatto automatico non aveva ancora superato la soglia di rilevamento testo del contatore, oppure il
testo vive in un nodo con `color` uguale al `background` finché non si anima (quindi "invisibile" al
contatore DOM che legge solo nodi con testo renderizzato visibilmente). **Verificato anche nella
pagina outHeadline (Atlante 2, Tavola H2)**: stessa firma `div|section-border`, stesso fenomeno — non
è un caso isolato, è sistemico su tutte le pagine che usano questo componente "divisore".

**Effetti attivi**: sfondo `#a8a8a8` (grigio neutro, diverso da tutte le sezioni scure attorno) — è lo
stesso grigio del banner "Stiamo aggiornando il brand" visto altrove nell'ecosistema, segno che questo
componente-divisore è in una fase di restyling non ancora completata.

**Perché è costruita così (ipotesi, dichiarata come tale)**: il div-divisore sembra pensato per
"scomparire" visivamente nella cattura statica finché non scorre in viewport — un pattern di reveal
scroll-triggered che il capture tool non aspetta abbastanza a lungo da innescare pienamente prima di
misurare il DOM.

---

### Tavola O3 — Sezione muta da 2.780px: il blocco più alto di tutta la pagina
![sezione 04](../capture/04-outfunnel/sezioni/04-section.png)

**Ruolo**: prova/rinforzo emotivo in forma di fumetto.
**Altezza**: 2.780px — **10,3% della pagina**, la sezione singola più alta di outFunnel.

**Cosa la compone secondo scheda.json**: `heading: null`, `blocchi_testo: 0`, `parole: 0`, `media: 10`,
`cta: 0`. Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|-|14`, gruppo 4
(condiviso con la sezione 09, altrettanto muta, 2.836px, `media: 9`).

**Cosa mostra davvero lo screenshot**: un fumetto in bianco e nero, stile manga/comic, 7 vignette in
colonna verticale con testo nei balloon ("Quindi ti serve un funnel strategico" / "Ma noi si è sempre
fatto così" / "Ti piacciono i soldi?" / "Certo che sì" / "Stai bruciando soldi senza accorgertene?" /
"Non ci crederei" / "Ho ragione, ecco perché ⌄"). **Stesso difetto di misurazione della Tavola O2, ma
di segno diverso**: qui il testo non manca per un ritardo di reveal, manca perché **è testo disegnato
dentro le immagini** (i balloon del fumetto), quindi strutturalmente invisibile a qualunque estrattore
DOM — non un bug del capture, un limite di misura che va dichiarato ogni volta che una pagina usa
fumetti/infografiche come portatori di copy. I 10 "media" sono le 7 vignette-immagine più probabili
elementi decorativi di cornice.

**Effetti attivi**: nessuno dichiarato a parte le `ombre` di pagina generiche sulle cornici del fumetto
(bordo bianco spesso, tipico frame da vignetta).

**Perché è costruita così**: un fumetto argomenta l'obiezione più comune ("ma noi si è sempre fatto
così") mettendola in bocca a un personaggio che viene poi convertito nel giro di 7 vignette — la forma
comic rende leggero un contenuto che, scritto in prosa, sarebbe un lungo paragrafo di gestione
obiezioni. Coerente con un prodotto d'ingresso da 98€: il tono resta leggero, quasi gratuito da
consumare.

---

### Tavola O4 — Le statistiche con le fonti
![sezione 10](../capture/04-outfunnel/sezioni/10-la-scienza-parla-chiaro-funnel-pe.png)

**Ruolo**: prova esterna/autorità — l'unica sezione della pagina con citazioni di studi terzi.
**Altezza**: 2.231px — **8,3%**.

**Cosa la compone**: 5 statistiche in righe alternate (donut chart teal/grigio a sinistra, testo a
destra, poi bar chart, poi donut, poi bar, poi donut), ciascuna con link "Fonte" sottolineato: 89% dei
leader crede nel marketing personalizzato, +313% di successo con marketing strategico, 68% delle
aziende senza funnel efficace, +30%/+50% con email segmentate, 53,7% dei marketer che considera la
strategia sottovalutata. `blocchi_testo: 29`, `parole: 290` — la sezione più densa di parole di tutta
la pagina insieme alla 08. `media: 6` (i grafici). Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|-|11`, gruppo 10, rappresentante
unico (nessuna sezione condivide questa firma).

**Effetti attivi**: nessun filtro; i donut chart e bar chart sono probabilmente SVG/canvas generati
lato client (coerenti con `raggi: 50%` ricorrente in `scheda.json`, tipico di cerchi SVG).

**Perché è costruita così**: alternare l'icona (donut/bar) al testo, riga dopo riga, con link diretto
alla fonte, serve a rendere ogni claim verificabile senza appesantire la lettura — esattamente
l'opposto della sezione-fumetto sopra: qui l'obiettivo è credibilità tecnica, lì era leggerezza.

---

### Tavola O5 — Il blocco senza immagini: outFunnel × Copywriter
![sezione 15](../capture/04-outfunnel/sezioni/15-outfunnel-copywriter.png)

**Ruolo**: personalizzazione per segmento professionale (1 di 4 varianti identiche nella struttura).
**Altezza**: 466px — **1,7%**.

**Cosa la compone**: solo testo, tre paragrafi, nessuna immagine (`media: 0` — **l'unica famiglia di
sezioni della pagina senza alcun media**), `blocchi_testo: 6`, `parole: 133`, `densita: 29` (la più
alta di tutta la pagina). Firma `section|page-section.full-bleed-section.layout-engine-section|2|-|-|2`,
gruppo 15 — condivide la firma con le sezioni 16 (Media buyer, 104 parole), 17 (Titolare aziendale, 102
parole) e 18 (Project Strategist/Manager, 71 parole): **4 varianti dello stesso schema puramente
testuale**, una per ruolo professionale del pubblico.

**Effetti attivi**: nessuno — coerente con l'assenza di `M` (media) nella firma.

**Perché è costruita così**: rispetto a tutte le altre sezioni della pagina (quasi sempre `M`, con
media), queste quattro sono deliberatamente nude — il ragionamento è specifico per ruolo (cosa
outFunnel fa per un copywriter è diverso da cosa fa per un media buyer), un'illustrazione generica
avrebbe reso le quattro varianti indistinguibili a colpo d'occhio; il testo puro obbliga a leggere,
cioè a riconoscersi.

---

### Tavola O6 — La CTA finale con il prezzo
![sezione 22](../capture/04-outfunnel/sezioni/22-outfunnel-probabilmente-non-per-te.png)

**Ruolo**: CTA di chiusura + prezzo.
**Altezza**: 757px — **2,8%**.

**Cosa la compone**: titolo su tre righe ("outFunnel? Probabilmente non è per te. Ma se lo è… Stai per
svoltare."), sottolineatura verde a mano libera sotto "outFunnel", card prezzo bianca con logo verde
sfumato "outFunnel", **"€98 / pagamento unico"** in verde brillante, bottone scuro "Entra ora in
outFunnel". `blocchi_testo: 3`, `parole: 17`, `media: 3`, `cta: 1`. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|C|4`, gruppo 22, rappresentante
unico. **Nota sul prezzo**: a differenza di Funnel Operator (dove il prezzo compare subito nell'hero),
qui il prezzo compare **solo qui, all'88% della pagina** (y=24.914 su 26.993) — un solo numero, senza
tabella comparativa, senza tier.

**Effetti attivi**: nessuno oltre alla sottolineatura vettoriale animata (probabile `stroke-dashoffset`,
coerente con le `trasformazioni matrix` viste a livello di pagina).

**Perché è costruita così**: il prezzo più basso delle tre pagine è anche quello con il framing più
dimesso ("probabilmente non è per te") — una leva di esclusività a basso rischio: chi arriva fin qui ha
già letto tutto il ragionamento, il prezzo è un dettaglio finale, non un'ancora iniziale.

---

### Tabella completa — le altre 18 sezioni di outFunnel (misure da scheda.json, non tutte viste a schermo)

| i | h (px) | % pag. | media | cta | parole | firma/gruppo | note |
|---|---|---|---|---|---|---|---|
| 3 | 928 | 3,4% | 1 | 0 | 0 | div-border, gr.3 | non vista — verosimile stesso difetto testo-nascosto della Tavola O2 |
| 5 | 1.955 | 7,2% | 7 | 0 | 156 | has-divider, gr.5 | "Già che ci sei, buttaci sopra benzina" — tabella Italianissimo/vincitore |
| 6 | 616 | 2,3% | 1 | 0 | 0 | div-border, gr.2 (= Tavola O2) | stessa firma esatta della Tavola O2 |
| 7 | 1.708 | 6,3% | 6 | 0 | 0 | full-bleed, gr.7 | muta come le Tavole O3/09, non vista |
| 8 | 1.128 | 4,2% | 2 | 0 | 141 | full-bleed, gr.8 | "gioco d'azzardo vs sotto controllo" |
| 9 | 2.836 | 10,5% | 9 | 0 | 0 | = Tavola O3 (gr.4) | seconda metà del fumetto o galleria gemella, non vista |
| 11 | 1.708 | 6,3% | 7 | 0 | 0 | = sez.7 (gr.7) | non vista |
| 12 | 1.056 | 3,9% | 5 | 0 | 15 | has-divider, gr.12 | "Vuoi complottare" |
| 13 | 1.088 | 4,0% | 1 | 0 | 0 | div-border, gr.3 (= sez.3) | non vista |
| 14 | 572 | 2,1% | 1 | 4 | 49 | full-bleed, gr.14 (= FAQ sez.23) | 4 CTA per i 4 segmenti (Tavola O5) |
| 16 | 364 | 1,3% | 0 | 0 | 104 | = Tavola O5 (gr.15) | "Media buyer" |
| 17 | 393 | 1,5% | 0 | 0 | 102 | = Tavola O5 (gr.15) | "Titolare aziendale" |
| 18 | 371 | 1,4% | 0 | 0 | 71 | = Tavola O5 (gr.15) | "Project Strategist/Manager" |
| 19 | 512 | 1,9% | 3 | 1 | 21 | has-divider, gr.19 | "Totale confidence. No dubbi." |
| 20 | 1.165 | 4,3% | 1 | 0 | 0 | div-border, gr.20 | non vista |
| 21 | 771 | 2,9% | 1 | 0 | 0 | div-border, gr.21 | non vista |
| 23 | 617 | 2,3% | 1 | 3 | 15 | = sez.14 (gr.14) | FAQ, 3 domande |
| 24 | 705 | 2,6% | 7 | 2 | 99 | footer, gr.24 | footer condiviso di tutto l'ecosistema — vedi nota footer sotto |

**Riepilogo pagina**: media totale = **79** (2,9 ogni 1.000px), parole totali = **1.227** (45 ogni
1.000px), blocchi_testo totale = **126**, CTA totale = **11**. Blocchi "div-border" muti (sez. 2,3,6,13,
20,21) sommano **5.264px = 19,5% dell'altezza totale** — quasi un quinto della pagina è, secondo il
DOM, "vuoto" (anche se la Tavola O2 dimostra che non lo è affatto visivamente).

---

## PARTE 2 — Funnel Operator, 434€ (h=24.019px, 28 sezioni/16 distinte)

### Tavola F1 — L'hero con il prezzo subito in vista
![sezione 01](../capture/02-funnel-operator/sezioni/01-funnel-operator-l-evoluzione-del-f.png)

**Ruolo**: hero con prezzo esposto da subito.
**Altezza**: 1.073px — **4,5%**.

**Cosa la compone**: sfondo con un fascio di luce blu diagonale su nero (`bg-void`), logo "Funnel
Operator" (rombo diviso bianco/blu), H1 bianco centrato su 5 righe, un riquadro video 4:3 con testo
"LIBERO" sovraimpresso su una foto al tramonto, tre bullet con spunta ("20+ ore di lezione" / "5
consulenze gratis" / "Come trovare clienti"), e a destra **"434,00 € / Una tantum"** con bottone blu
pieno "Acquista ora". `blocchi_testo: 4`, `parole: 23`, `media: 7`, `cta: 1`. Firma
`section|page-section.has-section-divider.full-bleed-section|3|M|C|5`, gruppo 1, rappresentante unico.

**Differenza chiave rispetto a outFunnel e a Copy**: **è l'unica delle tre pagine che mostra il prezzo
già nel primo schermo**, prima ancora che il visitatore abbia letto una riga di argomentazione.

**Effetti attivi**: il fascio di luce diagonale è verosimilmente un gradiente radiale/conico animato
(coerente con `filtri: backdrop blur(15px)/blur(20px)` visti a livello di pagina, i più alti delle tre
pagine); la keyframe reale non è dichiarata (`animazioni: []` anche qui) — è un CSS gradient statico o
un video di sfondo, non un'animazione JS misurata.

**Perché è costruita così**: a metà prezzo tra le due sorelle, questa pagina sceglie la trasparenza
commerciale immediata — mostrare il prezzo subito è una scommessa di fiducia ("non ti faccio scendere
20 schermate per scoprire quanto costa") più che una leva di scarsità.

---

### Tavola F2 — La storia personale a tre foto reali
![sezione 04](../capture/02-funnel-operator/sezioni/04-piacere-sono-andrei-c.png)

**Ruolo**: prova di identità/autenticità — foto reali non stock.
**Altezza**: 1.307px — **5,4%**.

**Cosa la compone**: fondo chiaro (`#f9f9f9` circa, diverso dal resto della pagina scura — unica
sezione chiara di Funnel Operator insieme al blocco storia), avatar circolare (foto reale, non
illustrazione), H2 "Piacere, sono Andrei c:", tre coppie sottotitolo+foto verticali (foto in palestra
allo specchio, foto di un tavolo riunioni con 4 persone in giacca, foto di una scrivania con doppio
monitor di notte). `blocchi_testo: 8`, `parole: 20`, `media: 5`, `cta: 0`. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|-|7`, gruppo 4, rappresentante
unico.

**Effetti attivi**: nessuno oltre al colore — le foto non hanno cornice arrotondata pronunciata (i
`raggi: 10px` di pagina si applicano solo ad angoli leggeri).

**Perché è costruita così**: tre foto reali (palestra, ufficio, scrivania buia) in sequenza cronologica
implicita fanno il lavoro che altrove fa un CV scritto — mostrano il percorso "zero → team" senza
dirlo, e la scelta di foto vere (non stock, si vede la sgranatura da smartphone) è deliberata: rinforza
"questo non è un funnel finto", stesso principio della Tavola F3.

---

### Tavola F3 — Il carosello "2021-oggi": la sezione più densa di parole
![sezione 08](../capture/02-funnel-operator/sezioni/08-2021-oggi.png)

**Ruolo**: escalation della storia personale, verso il team.
**Altezza**: 1.539px — **6,4%**, la sezione singola più alta della pagina.

**Cosa la compone**: H1 "2021 – oggi", H2 su tre righe ("Non sono più SOLO!!! Finalmente assumo un
team."), paragrafo con nomi propri (Martin, Gaia, Alessandra), un **carosello con frecce** (‹ › visibili
nello screenshot) che mostra una foto verticale di magazzino con 3 persone, poi 6 paragrafi consecutivi
di narrazione (obiettivo Estonia, milionario in 1-3 anni, link "Leggi la mia storia", chiusura "Però…
Poi è arrivato il 2025"). `blocchi_testo: 25`, `parole: 141`, `media: 6`, `cta: 1`. Firma
`section|page-section.has-section-divider.full-bleed-section|3|M|C|8`, gruppo 8, rappresentante unico.

**Effetti attivi**: il carosello ha frecce SVG cliccabili in cerchio grigio (`raggi: 50%`), coerente con
i controlli-carosello visti anche altrove nell'ecosistema (video-testimonianze di 05-copy, Tavola C3).

**Perché è costruita così**: è l'unica sezione della pagina con un carosello dentro il blocco narrativo
(non nella prova sociale, dentro la storia) — segno che l'autore ha più materiale fotografico del team
di quanto il layout a colonna singola possa reggere, e ha risolto con uno swipe invece di allungare la
pagina con altre foto in sequenza verticale.

---

### Tavola F4 — "Cos'è CRO e come funziona?": spiegazione con schema prima/dopo
![sezione 16](../capture/02-funnel-operator/sezioni/16-cos-cro-e-come-funziona.png)

**Ruolo**: didattica — spiega il termine tecnico al centro del posizionamento.
**Altezza**: 1.204px — **5,0%**.

**Cosa la compone**: H1 + due righe di definizione, sottotitolo "Ad esempio:", **due card affiancate**
"Prima di CRO" (grigio scuro, virgolette: *"Compra il nostro spazzolino"*) e "Dopo il CRO" (bordo blu,
*"Il sorriso da sogno? Bello averlo. Più bello mantenerlo."*), poi tre bullet grassetto ("Le parole nel
sito" / "Le immagini che hanno scelto" / "I tipi di video che fanno"), chiusura in H2 centrato "CRO =
migliorare il marketing. Renderlo più convincente." `blocchi_testo: 19`, `parole: 75`, `media: 3`,
`cta: 0`. Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|-|6`, gruppo 16,
rappresentante unico.

**Effetti attivi**: nessuno oltre al bordo colorato che distingue le due card (grigio vs blu — lo
stesso codice colore "prima/dopo" che il modello apsales usa per "Il problema/La soluzione", Tavola 5
di quel report: **pattern ricorrente in tutto l'ecosistema Andrei Pascu**, non un'invenzione isolata).

**Perché è costruita così**: la coppia di card prima/dopo con lo stesso identico prodotto ("spazzolino"
→ "sorriso da sogno") rende concreto un acronimo astratto (CRO) con un solo esempio, invece di una
definizione da manuale — coerente con un pubblico che deve *capire cosa comprerà* prima di guardare il
prezzo.

---

### Tavola F5 — "La realtà dei fatti": prova con fonte esterna regolamentare
![sezione 21](../capture/02-funnel-operator/sezioni/21-la-realt-dei-fatti.png)

**Ruolo**: gestione obiezione ("è l'ennesimo business online?") con autorità istituzionale.
**Altezza**: 1.928px — **8,0% della pagina, la sezione singola più alta di Funnel Operator**.

**Cosa la compone**: H1 "La realtà dei fatti?", paragrafo che nomina esplicitamente concorrenti falliti
(dropshipping, trading), bottone blu "Vedi la mia storia", secondo paragrafo, H2 con link "questo
studio", **una card citazione bianca con il logo della SEC** (Securities and Exchange Commission
americana) che mette in guardia sugli investimenti a rischio, poi due ritratti d'epoca in bianco e nero
(Claude C. Hopkins e John Emory Powers, copywriter storici, con didascalia). `blocchi_testo: 24`,
`parole: 242` — **la sezione con più parole di tutta la pagina**. `media: 3`, `cta: 2`. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|C|10`, gruppo 21, rappresentante
unico.

**Effetti attivi**: la card SEC ha un `box-shadow` diffuso (glow bianco) coerente con
`ombre: rgba(0,0,0,0.12) 0px 8px 32px 0px` misurata a livello di pagina — la card "galleggia" sul fondo
nero.

**Perché è costruita così**: citare un ente regolatore *contro* trading/crypto (settori affini ma non
concorrenti diretti) per poi proporre copywriting è un disinnesco preventivo di scetticismo — usa
l'autorità di un terzo neutro invece dell'autopromozione, e i due ritratti storici spostano il
copywriting da "trend" a "mestiere centenario" (stesso registro delle citazioni storiche viste anche
in altre pagine dell'ecosistema).

---

### Tavola F6 — Le FAQ ad accordion
![sezione 26](../capture/02-funnel-operator/sezioni/26-domande-comuni.png)

**Ruolo**: gestione obiezioni finali.
**Altezza**: 1.216px — **5,1%**.

**Cosa la compone**: titolo "Domande comuni" con drop-shadow marcata, 10 righe accordion chiuse con
chevron a destra: "Se compro questo corso divento ricco?", "Quanto tempo in media per avere il primo
cliente pagante?", "Come funzionano le 5h di consulenza?", "Quanto devo lavorare? Posso farlo
part-time?", "È un abbonamento o pago solo una volta?", "Ho altre domande… A chi posso chiedere?", "Ho
un problema con un ordine, a chi posso scrivere?", "Sono disponibili tutte le lezioni?", "Come faccio a
fidarmi?", "Il funnel operator è una professione riconosciuta?" `blocchi_testo: 72` — **il valore più
alto di tutta la pagina** (sono i nodi wrapper di ciascuna riga accordion, non parole vere: `parole: 71`
— quasi un rapporto 1:1 blocco/parola, tipico di componenti-accordion dove ogni riga genera più nodi
DOM del testo che contiene). `cta: 10` — un trigger per ogni riga. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|C|6`, gruppo 26, rappresentante
unico.

**Effetti attivi**: accordion (probabile stesso pattern Radix/shadcn `accordion-down`/`accordion-up`
osservato in apsales, anche se qui la piattaforma è Squarespace non Next.js — quindi verosimilmente un
blocco custom-code con lo stesso comportamento CSS-height-animato).

**Perché è costruita così**: 10 domande (contro le 7 di apsales e le 6 del Manuale, Atlante 2) è il
numero più alto delle pagine studiate — coerente con un prezzo medio (434€) dove il rischio percepito
richiede più rassicurazione puntuale di un prodotto da 98€, ma meno della vendita "totale" a 999€ dove
la rassicurazione passa anche da altri canali (video-testimonianze, chat reali).

---

### Tabella completa — le altre 22 sezioni di Funnel Operator

| i | h (px) | % pag. | media | cta | parole | firma/gruppo | note |
|---|---|---|---|---|---|---|---|
| 2 | 690 | 2,9% | 2 | 0 | 27 | full-bleed, gr.2 | "Le aziende lo vogliono, non lo trovano" |
| 3 | 485 | 2,0% | 4 | 0 | 19 | full-bleed, gr.3 | "Sto per parlarti di soldi" |
| 5 | 1.422 | 5,9% | 4 | 1 | 98 | full-bleed, gr.5 | "Ero confuso e onestamente un po' sfigato" |
| 6 | 534 | 2,2% | 3 | 0 | 55 | has-divider, gr.6 | "2020 — Primi clienti chiusi" |
| 7 | 1.350 | 5,6% | 7 | 0 | 56 | has-divider, gr.7 | "2021 — mi trasferisco a Bologna" |
| 9 | 569 | 2,4% | 1 | 0 | 61 | = sez.2 (gr.2) | "inizio 2025" |
| 10 | 560 | 2,3% | 2 | 0 | 45 | = sez.2 (gr.2) | "Ti auguro lo stesso problema" |
| 11 | 439 | 1,8% | 2 | 0 | 35 | = sez.3 (gr.3) | "E voglio che tu copi le mie mosse" |
| 12 | 223 | 0,9% | 2 | 0 | 4 | full-bleed, gr.12 | "Abbiamo testato nuovi servizi" — la più corta della pagina |
| 13 | 1.026 | 4,3% | 6 | 0 | 47 | = sez.12 (gr.12, ma altezza doppia) | "Continuato con i test" |
| 14 | 670 | 2,8% | 3 | 0 | 17 | = sez.2 (gr.2) | senza heading |
| 15 | 280 | 1,2% | 2 | 0 | 14 | = sez.12 (gr.12) | "Ho iniziato a offrire il servizio di CRO" |
| 17 | 336 | 1,4% | 2 | 0 | 0 | = sez.3 (gr.3) | senza heading, muta |
| 18 | 1.053 | 4,4% | 2 | 0 | 89 | = sez.13 (gr.13) | "Perché il CRO paga bene?" |
| 19 | 905 | 3,8% | 2 | 0 | 70 | = sez.13 (gr.13) | "Il marketer che le aziende vogliono nel 2026" |
| 20 | 663 | 2,8% | 1 | 0 | 39 | = sez.2 (gr.2) | "Il Funnel Operator si fa pagare per" |
| 22 | 940 | 3,9% | 1 | 0 | 128 | = sez.13 (gr.13) | "Ho fatto 28 test di 28 servizi diversi" |
| 23 | 871 | 3,6% | 2 | 0 | 14 | full-bleed, gr.23 | "Ho scelto il copywriting" |
| 24 | 883 | 3,7% | 2 | 0 | 97 | = sez.23 (gr.23) | "Per chi ho creato Funnel Operator" |
| 25 | 673 | 2,8% | 3 | 1 | 5 | full-bleed, gr.25 | sezione-CTA breve, quasi muta |
| 27 | 393 | 1,6% | 1 | 0 | 149 | = sez.3 (gr.3) | "Disclaimer" — densità 38, la più alta della pagina |
| 28 | 705 | 2,9% | 7 | 2 | 99 | footer, gr.28 | footer condiviso — vedi nota sotto |

**Riepilogo pagina**: media totale = **86** (3,6 ogni 1.000px), parole totali = **1.740** (72 ogni
1.000px), blocchi_testo totale = **369**, CTA totale = **14**. **Zero sezioni "div-border" mute**: a
differenza di outFunnel (19,5% di blank-filler), Funnel Operator non ha nemmeno un blocco separatore
puro — ogni sezione, anche la più corta (223px, sez.12), porta almeno una frase.

---

## PARTE 3 — Copywriting Mentorship (05-copy), 999€ (h=26.952px, 28 sezioni/20 distinte)

### Tavola C1 — L'hero fotografico, senza prezzo
![sezione 01](../capture/05-copy/sezioni/01-raggiungi-la-libert-finanziaria-av.png)

**Ruolo**: hero aspirazionale, prezzo assente.
**Altezza**: 875px — **3,2%**, la più bassa fra le tre hero.

**Cosa la compone**: fotografia reale a piena larghezza (soggiorno con tende, un ragazzo di spalle al
laptop davanti alla finestra — non uno still stock riconoscibile, verosimilmente casa/ufficio reale),
overlay scuro parziale, H1 bianco su 5 righe con **"copywriter autonomo" sottolineato in arancione a
mano libera** (colore mai visto nelle altre due hero, che restano blu/verde), tre bullet con icona
spunta arancione ("Aggiornamenti a vita [no costi extra]" / "4 metodi per trovare clienti" /
"Consulenza direttamente col formatore"). `blocchi_testo: 3`, `parole: 20`, `media: 6`, `cta: 0` — **zero
CTA nell'hero**, a differenza delle altre due pagine che hanno un bottone visibile da subito. Firma
`section|page-section.has-section-divider.full-bleed-section|3|M|-|4`, gruppo 1, rappresentante.

**Effetti attivi**: nessun filtro dichiarato sulla sezione; la sottolineatura arancione è
verosimilmente un SVG a tratto singolo (coerente con le sottolineature a mano libera viste anche in
outFunnel/outHeadline, sempre come elemento ricorrente del design system Andrei Pascu, lì in
verde/rosso).

**Perché è costruita così**: l'assenza di CTA e di prezzo nell'hero, a fronte del prezzo più alto delle
tre pagine, è coerente — un impegno da 999€ non si chiede al primo schermo: prima la foto (vita reale,
non ricchezza ostentata: si vede un salotto normale, non una Lamborghini) deve costruire
l'identificazione, il prezzo arriva solo dopo 88% di pagina (Tavola C6).

---

### Tavola C2 — "Sono il mentore che cercavi": la sezione più fotografica della pagina
![sezione 10](../capture/05-copy/sezioni/10-sono-il-mentore-che-cercavi.png)

**Ruolo**: prova di identità/percorso personale, versione estesa rispetto a Funnel Operator.
**Altezza**: 1.420px — **5,3%**.

**Cosa la compone**: due foto verticali ai lati (sfondo giallo pieno dietro entrambe — colore mai visto
altrove nell'ecosistema in questa intensità), H1 con la parola "mentore" evidenziata da un box giallo
pieno, tre paragrafi di storia personale (introverso/insicuro, "ogni singolo obiettivo", "+270K
follower, clienti da 8 paesi, +3000 persone aiutate"), e — elemento unico rispetto a Funnel Operator —
un **player video embedded** con thumbnail "Il parere degli STUDENTI" e testimonial scritte in
sovraimpressione, controlli reali (play, 00:00/02:10, volume, fullscreen). `blocchi_testo: 43`,
`parole: 195`, `media: 18` — **il terzo valore di media più alto della pagina**. `cta: 1`. Firma
`section|page-section.has-section-divider.full-bleed-section|3|M|C|7`, gruppo 10, rappresentante unico.

**Effetti attivi**: nessun filtro dichiarato; il player video ha probabile `border-radius` coerente coi
`raggi: 4px` misurati a livello di pagina.

**Perché è costruita così**: la stessa struttura "storia personale" di Funnel Operator (Tavola F2) qui
è quasi triplicata in parole (195 vs 20) e porta dentro di sé un video di prova sociale — a un prezzo
più alto, la fiducia richiesta è maggiore e la pagina non separa più "la mia storia" dalla "prova che
funziona per altri": le fonde nello stesso blocco.

---

### Tavola C3 — La griglia video-testimonianze: 67 elementi media in una sola sezione
![sezione 11](../capture/05-copy/sezioni/11-video-testimonianze-degli-studenti.png)

**Ruolo**: prova sociale di massa.
**Altezza**: 891px — **3,3%** (compatta nonostante il conteggio media enorme).

**Cosa la compone**: H1+H2 "Video testimonianze degli studenti di Copywriting Mentorship", sottotitolo,
**griglia 3×2 di player video reali** con nome dello studente in overlay (David 01:28, Salvatore 03:07,
Francesco 03:14, Simone 02:19, Fabiano 00:48, Tommaso 00:48), ognuno con controlli play/volume/
fullscreen funzionanti, bottone blu "Leggi altri pareri degli studenti". `blocchi_testo: 193` — **il
valore più alto di qualunque sezione in tutte e tre le pagine di questo atlante** (sono i nodi dei
controlli-player ripetuti 6 volte, non parole). `parole: 79`, `media: 67` — **il valore più alto
dell'intero atlante**, quasi 4 volte il secondo (le 18 media della Tavola C2). `cta: 1`. Firma
`section|page-section.layout-engine-section.background-width--full-bleed|2|M|C|4`, gruppo 11,
rappresentante unico.

**Verifica difetto "media dichiarato ma schermo vuoto"**: **non trovato qui** — tutti e 6 i player
mostrano un frame reale (volto della persona, non un rettangolo grigio segnaposto), il nome e la durata
sono leggibili. I video sono quindi effettivamente caricati al momento dello scatto, o quantomeno il
loro poster-frame lo è.

**Effetti attivi**: nessun filtro dichiarato oltre ai controlli nativi HTML5 `<video>`.

**Perché è costruita così**: 6 volti reali con nome e durata reale (non "00:00" placeholder) in griglia
densa comunica volume di prova sociale in un solo schermo — il pattern "prova one-to-one" (un singolo
video grande, come in Tavola C2) e il pattern "prova di massa" (griglia piccola) convivono nella stessa
pagina, cosa che non accade né in Funnel Operator né in outFunnel: **solo il prodotto da 999€ usa
entrambi i registri di prova sociale video.**

---

### Tavola C4 — La galleria di 44 screenshot chat: prova sociale "grezza"
![sezione 25](../capture/05-copy/sezioni/25-section.png)

**Ruolo**: prova sociale non curata (screenshot di chat reali, non testimonial scritte apposta).
**Altezza**: 450px — **1,7%** (bassa, ma densissima di elementi).

**Cosa la compone**: tre screenshot di conversazioni reali affiancati — una chat scura tipo Instagram
DM ("Cazzo, il broker del copy colpisce un'altra volta 💀" / "PS: è il cliente che mi ha riscritto
oggi ❤️"), una chat verde tipo WhatsApp (racconto esteso di un investimento fatto, corso Vendita101
citato), una terza chat chiara ("Ci ho messo un po' per trovare clienti ma... sono a quota 3.4K$ ora" /
"Keep going 🚀" / "Grandissimo corso ❤️"). Frecce di navigazione ai lati (‹ ›, verosimilmente altre
schermate scorrevoli). `blocchi_testo: 2`, `parole: 0` (il testo è dentro screenshot-immagine, stesso
limite di misura della Tavola O3), `media: 44` — **il secondo valore più alto dell'atlante**. `cta: 0`.
Firma `section|page-section.gallery-section.full-bleed-section|2|M|-|2`, gruppo 25, rappresentante
unico.

**Effetti attivi**: nessuno dichiarato; la sezione è probabilmente uno slider/galleria orizzontale
(coerente con le frecce visibili).

**Perché è costruita così**: screenshot di chat non editate (con errori di battitura, emoji informali,
timestamp impliciti) sono percepiti come più credibili di testimonial scritte ad hoc — è la versione
"grezza" della prova sociale, complementare ai video curati della Tavola C3, e appare solo a ridosso
del pricing (subito prima, y=23.330, il pricing è a y=23.780): la sequenza è deliberata, prova → prezzo
nello stesso respiro visivo.

---

### Tavola C5 — "Gli altri ti mettono 30 video-recensioni…": il contro-posizionamento sui dati
![sezione 07](../capture/05-copy/sezioni/07-gli-altri-ti-mettono-30-video-rece.png)
*(nota: immagine non riaperta in questa sessione — dati da scheda.json, descrizione già coperta nella
COPY corrispondente; citata qui solo per le misure)*

**Ruolo**: contro-posizionamento competitivo con dati di mercato.
**Altezza**: 1.771px — **6,6%**.
**Cosa la compone (da scheda.json)**: heading citato più due dati di mercato ripetuti identici nel DOM
("Il mercato globale dei servizi di copywriting ha un valore di $25.29 miliardi nel 2023… $42.22
miliardi entro il 2030" compare 2 volte in `headings`, verosimilmente desktop+mobile duplicato nella
cattura). `blocchi_testo: 28`, `parole: 252`, `media: 5`, `cta: 4` — insieme alla Tavola C6 (pricing,
`cta:2`) e alla Tavola sez.15 (le-video-lezioni, `cta:7`) è tra le sezioni con più call-to-action della
pagina. Firma `section|page-section.full-bleed-section.layout-engine-section|2|M|C|9`, gruppo 7,
rappresentante — condivide la firma con la sezione 08 ("Cosa troverai in Copywriting Mentorship?",
161 parole, 8 media).

**Perché è costruita così (da dati, senza aver riaperto lo screenshot)**: 4 CTA in una sola sezione di
contro-posizionamento è insolito — verosimilmente un caso di micro-CTA ripetute (es. "Scopri di più"
sotto ogni bullet), coerente con una sezione lunga (1.771px) che vuole punti di uscita multipli invece
di un solo bottone in fondo.

---

### Tavola C6 — Il pricing a due livelli: l'unico dell'atlante
![sezione 26](../capture/05-copy/sezioni/26-upgrade-disponibile.png)

**Ruolo**: prezzo — l'unica sezione-prezzo a due colonne di comparazione di tutto l'atlante.
**Altezza**: 1.302px — **4,8%**.

**Cosa la compone**: H1 "Pricing" con drop-shadow marcata (stesso stile della Tavola F6), **due card
affiancate su sfondo dorato sfumato**: "Copywriting Mentorship BASE" — **€349** — con 6 spunte
("40+ lezioni copywriting", "20+ lezioni trovare clienti", "Accesso gruppo telegram", "PDF/riassunti/
esercitazioni", "Accesso a vita", "Esame conclusivo gratuito") più un riquadro extra ("1 consulenza di
60 min con Andrei P.") e bottone grigio "Acquista Base"; "Copywriting Mentorship" **€999**, bordo
dorato acceso (evidenziata come scelta preferita), stesse 6 spunte più riquadro dorato ("Consulenze
illimitate con Andrei P.") e bottone dorato pieno "Acquista Completo". Sotto, riquadro "Upgrade
disponibile: chi acquista la versione BASE può sempre fare l'upgrade… pagando solo la differenza
(€650)." `blocchi_testo: 36`, `parole: 109`, `media: 3`, `cta: 2`. Firma
`section|page-section.full-bleed-section.layout-engine-section|2|M|C|7`, gruppo 26, rappresentante
unico.

**Effetti attivi**: la card destra ha un bordo colorato acceso (evidenziazione "scelta consigliata",
pattern standard di pricing table) — coerente coi `raggi` di pagina misurati (bordi arrotondati sulle
card).

**Perché è costruita così**: **questo è il cuore della risposta alla domanda sul prezzo** (vedi sezione
finale). L'unica delle tre pagine che offre un'ancora di prezzo interna (349€ accanto a 999€) — il
prezzo "vero" del prodotto non è mai presentato da solo, è sempre in coppia con un'opzione più economica
che lo fa sembrare "quello giusto" per contrasto. Le uniche due differenze reali fra i tier sono il
numero di consulenze (1×60min vs illimitate) — il contenuto didattico è identico. Il delta di upgrade
dichiarato (€650, non 999-349=650 — combacia esattamente) segnala che la BASE è pensata come porta
d'ingresso, non come prodotto a sé stante.

---

### Tabella completa — le altre 22 sezioni di Copywriting Mentorship

| i | h (px) | % pag. | media | cta | parole | firma/gruppo | note |
|---|---|---|---|---|---|---|---|
| 2 | 776 | 2,9% | 6 | 1 | 29 | full-bleed, gr.2 | senza heading |
| 3 | 567 | 2,1% | 3 | 0 | 6 | has-divider, gr.3 | "Scopri di cosa si tratta" |
| 4 | 1.624 | 6,0% | 1 | 0 | 0 | div-border, gr.4 | muta nel DOM — verosimile stesso difetto delle Tavole O2/H2 |
| 5 | 900 | 3,3% | 1 | 0 | 14 | full-bleed, gr.5 | "Ho scelto il copywriting…" |
| 6 | 600 | 2,2% | 2 | 0 | 62 | full-bleed, gr.6 | "Per chi ho creato Copywriting Mentorship" |
| 8 | 1.814 | 6,7% | 8 | 1 | 161 | = Tavola C5 (gr.7) | "Cosa troverai in Copywriting Mentorship?" |
| 9 | 874 | 3,2% | 2 | 0 | 125 | full-bleed, gr.9 | "Copywriting Mentorship 6: ti insegno cosa funziona" |
| 12 | 1.159 | 4,3% | 2 | 1 | 165 | full-bleed, gr.12 | "Impara a usare l'AI prima che sia lui a usare te" |
| 13 | 338 | 1,3% | 3 | 0 | 17 | full-bleed, gr.13 | "Un corso non è mai stato così completo" |
| 14 | 683 | 2,5% | 2 | 0 | 95 | = sez.6 (gr.6) | "Io ti do le informazioni, tu le sfrutti" |
| 15 | 2.212 | 8,2% | 3 | 7 | 134 | full-bleed, gr.15 | "Le video-lezioni" — 60+ lezioni, accordion curriculum, la più alta della pagina |
| 16 | 620 | 2,3% | 4 | 0 | 27 | = sez.3 (gr.3) | "Contenuti per massimizzare il successo" |
| 17 | 570 | 2,1% | 1 | 0 | 0 | div-border, gr.17 | muta — non vista |
| 18 | 968 | 3,6% | 1 | 5 | 66 | full-bleed, gr.18 | "Consulenze direttamente con me" — 5 CTA |
| 19 | 1.036 | 3,8% | 5 | 0 | 136 | has-divider, gr.19 | "Diamo peso agli aggiornamenti di mercato" |
| 20 | 687 | 2,5% | 3 | 0 | 10 | = sez.6 (gr.6) | "Ecco il piano" |
| 21 | 845 | 3,1% | 2 | 0 | 37 | = sez.9 (gr.9) | "Non è un business sexy… Ma funziona" |
| 22 | 828 | 3,1% | 4 | 0 | 22 | = sez.1 (gr.1) | "A differenza di tutte le milioni di persone" |
| 23 | 940 | 3,5% | 1 | 1 | 130 | = sez.18 (gr.18) | "Questo percorso lo descrivo con una sola frase" |
| 24 | 297 | 1,1% | 0 | 0 | 8 | full-bleed, gr.24 | "Opinioni e risultati degli studenti" — unica sezione a 0 media di tutta la pagina |
| 27 | 1.165 | 4,3% | 1 | 9 | 81 | = sez.12 (gr.12) | FAQ finali — 9 CTA, il valore più alto della pagina |
| 28 | 705 | 2,6% | 7 | 2 | 99 | footer, gr.28 | footer condiviso — vedi nota sotto |

**Riepilogo pagina**: media totale = **205** (7,6 ogni 1.000px — più del doppio delle altre due pagine),
parole totali = **2.079** (77 ogni 1.000px), blocchi_testo totale = **604**, CTA totale = **34**.
Blocchi "div-border" muti (sez.4, 17) sommano **2.194px = 8,1%** — via di mezzo fra outFunnel (19,5%) e
Funnel Operator (0%).

---

## La nota sul footer (le tre pagine condividono lo stesso componente)

Le tre pagine terminano con un footer identico bit per bit nei numeri: `blocchi_testo: 24`,
`parole: 99`, `media: 7`, `cta: 2`, firma `footer|sections|1|M|C|4` — stesso conteggio già osservato
anche nella pagina 01-andrei-copy-home (Atlante 2). **Aperto visivamente in questa sessione dalla
capture di 01-andrei-copy-home**: fondo blu pieno (`#0062ff`), wordmark "APsales", 4 icone social, 5
link di navigazione (La mia storia/Store/Recensioni/Risorse/Blog), un templare in pixel-art bianco su
blu sullo sfondo destro, paragrafo di disclaimer legale, indirizzo con P.IVA. **Questo conferma, con
prova visiva diretta, il comportamento che il report gemello su apsales.eu (`13-apsales-ATLANTE.md`,
Tavola 14) aveva dovuto lasciare come "discrepanza da verificare"**: lì il footer dichiarava nel codice
sorgente `bg-blue` ma lo screenshot mostrava nero — qui, sullo stesso tipo di componente
(`RevealFooter`-like, blu con figura in pixel-art), il blu **si vede correttamente**. Non è quindi un
difetto del componente in sé, ma della cattura specifica di quella pagina.

## Difetto di cattura trasversale: barra "Claude Speedrun" in overlay

Osservato in **due punti distinti** (outFunnel Tavola O1, 01-andrei-copy-home sezioni 1-2, Atlante 2):
una barra scura sticky con "Claude Speedrun" a sinistra e "Accedi" a destra compare sovrapposta al
contenuto reale nella parte alta dello screenshot. Non è coerente con nessuna delle pagine su cui
appare (né outFunnel né la home parlano di "Claude Speedrun", che è tutt'altra pagina
dell'ecosistema — vedi `12-claude-speedrun-ATLANTE.md`). Va trattato come artefatto del capture tool
(sessione/tab precedente rimasta agganciata), **non come elemento del sito**: se si replica una di
queste due sezioni per la Fabbrica, questa barra va ignorata.

---

## LA DOMANDA SUL PREZZO: come cambia la composizione visiva quando il prezzo sale (98€ → 434€ → 999€)

Tutti i numeri qui sono somme dirette delle tabelle sopra, cioè letti sezione per sezione da
`scheda.json` — nessuna stima.

| Metrica | outFunnel 98€ | Funnel Operator 434€ | Copywriting Mentorship 999€ |
|---|---|---|---|
| Altezza pagina | 26.993px | 24.019px | 26.952px |
| Media totali | 79 | 86 | **205** |
| Media ogni 1.000px | 2,9 | 3,6 | **7,6** |
| Parole totali | 1.227 | 1.740 | **2.079** |
| Parole ogni 1.000px | 45 | 72 | **77** |
| Blocchi di testo totali | 126 | 369 | **604** |
| CTA totali | 11 | 14 | **34** |
| % pagina in blocchi "div-border" muti | **19,5%** | **0%** | 8,1% |
| Animazioni CSS reali dichiarate | 0 | 0 | **2 tipi (×6 istanze)** |
| Sezione video singola più grande (player) | — | — | 18 media (Tavola C2) |
| Sezione griglia-video di prova sociale | — | — | 67 media (Tavola C3) |
| Galleria screenshot prova sociale | — | — | 44 media (Tavola C4) |
| Pricing a più livelli con ancora di confronto | no (prezzo singolo, in fondo) | no (prezzo singolo, in hero) | **sì — 349€/999€ affiancati** |

**Risposta diretta**: la composizione **non** diventa più "vuota" o più ariosa salendo di prezzo — è
vero il contrario. La densità di media per 1.000px di scroll **più che raddoppia** salendo da 434€ a
999€ (3,6 → 7,6), e il numero di blocchi di testo/interattivi quasi **quintuplica** dal prodotto più
economico al più caro (126 → 604). Quello che cambia davvero con il prezzo sono tre cose precise,
misurabili:

1. **La densità di prova sociale, non la sua presenza.** Tutte e tre le pagine hanno prova sociale, ma
   solo Copywriting Mentorship (999€) la moltiplica su tre canali paralleli e non ridondanti nella
   stessa pagina: un video-mentore singolo e lungo (Tavola C2, 18 media), una griglia di 6 video-brevi
   (Tavola C3, 67 media — il valore più alto misurato in assoluto), e una galleria di screenshot-chat
   non editati (Tavola C4, 44 media). outFunnel e Funnel Operator si fermano a un solo registro
   (foto/carosello narrativo).
2. **Solo il prodotto più caro dichiara animazioni CSS reali** (`image-fade-in`, `pulse`) — le altre
   due pagine hanno l'array `animazioni` vuoto in `scheda.json`. Più budget di prodotto sembra
   accompagnarsi a più budget di rifinitura del reveal in pagina, non solo a più contenuto.
3. **Solo il prezzo più alto è presentato con un'ancora di confronto interna** (349€ vs 999€, Tavola
   C6) — gli altri due prezzi (98€ e 434€) sono presentati da soli, senza alternativa sulla stessa
   pagina. È l'unica variabile compositiva che segue in modo pulito e non ambiguo l'aumento di prezzo:
   più il prezzo assoluto è alto, più serve un punto di paragone accanto per renderlo relativamente
   accettabile.

Quello che **non** segue un andamento lineare col prezzo: il timing di comparsa del prezzo in pagina
(434€ lo mostra súbito in hero; 98€ e 999€ lo rimandano, uno a metà "confidenza totale" e l'altro
addirittura all'88% della pagina) e la percentuale di pagina "vuota" da blocchi separatori
(`div-border`): è più alta nel prodotto più economico (19,5%), pari a zero nel prodotto di mezzo,
intermedia in quello più caro (8,1%) — quindi il prezzo non compra spazio bianco, compra prova sociale
densa, rifinitura di animazione e un'architettura di scelta (tier multipli) che il prodotto singolo non
ha bisogno di offrire.

---

## DELTA ALLA FABBRICA

**CANONE**: quando un prodotto sale di fascia (indicativamente sopra i 900€ su questo mercato), la
pagina prodotto non deve "arieggiarsi" — deve moltiplicare i **registri** di prova sociale (video
lungo + griglia video + screenshot grezzi, mai uno solo) e introdurre un'**ancora di prezzo interna**
(due tier affiancati, mai un prezzo isolato). Sotto quella soglia, un prezzo isolato mostrato presto
(nell'hero, come Funnel Operator) comunica più fiducia di uno nascosto in fondo.

**PATTERN**: il "div separatore" (`div.section-border`, sfondo grigio neutro `#a8a8a8`) che compare in
outFunnel, outHeadline e Copywriting Mentorship porta spesso copy persuasivo vero — non va mai
scartato o trattato come blank slide solo perché `scheda.json` lo misura a 0 parole/0 blocchi: è un
falso negativo sistemico del contatore DOM su contenuto animato in ingresso o su testo rasterizzato
dentro immagini/fumetti (verificato in almeno 3 sezioni distinte di 3 pagine diverse).

**GATE**: prima di stimare "quanto è vuota" una sezione dai soli numeri di `scheda.json`, aprire sempre
lo screenshot corrispondente — la Fabbrica Siti non deve mai scartare un blocco come "filler" senza
questa verifica visiva; il costo di uno sguardo in più è minimo, il costo di cancellare un blocco di
copy vero scambiato per un div vuoto è la perdita silenziosa di un argomento di vendita.
