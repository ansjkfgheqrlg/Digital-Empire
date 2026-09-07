---
Type: PROJECT
Status: Active
Tags: #competitor #andrei-pascu #fabbrica-siti #piano #studio-totale
Created: 2026-09-07
Last updated: 2026-09-07
Dossier: 33
---

# DOSSIER 33 — STUDIO TOTALE DELL'ECOSISTEMA ANDREI PASCU

## Il piano per prendere tutto, da tutti i suoi siti — e farlo entrare nella Fabbrica

> **Ordine di Max, 2026-09-07:** *"quello che c'è adesso è solamente uno studio su un solo sito, non
> tutti gli altri. Devi fare la stessa identica cosa su tutti gli altri siti di Andrei. Uno studio
> sullo stile, sul tipo di colori, sul tipo di effetti, sul tipo di logica usato, vari report, poi
> tutta anche lo studio e analisi del copy, lo studio totale di tutto il sito, dello schema, di ogni
> sezione, su come è stato costruito, formato, schematizzato. Nello specifico, in dettaglio: effetto,
> colore, tutto. Report, punti, studio, analisi — tutto questo per tutti i siti suoi di Andrei."*
>
> **E il principio sotto l'ordine:** *"dobbiamo copiare da tutti [...] non copiando alla lettera:
> copiando il loro schema, la loro mentalità, le loro mosse. Dobbiamo mangiare letteralmente tutto
> quello che possiamo."* → scritto in dottrina, `emperator.md §6.22`.
>
> **E l'ordine sul metodo:** *"pianificazione e pianificazione fino a che la pianificazione non è
> talmente perfetta da non avere nessun errore, così che l'operatività in sé sarà molto più
> performante e più facile."* → `emperator.md §6.20`, alzata oggi: **il criterio di arresto non è un
> numero, è un giro a vuoto.**

**Giri di critica fatti su questo piano: sette.** P0 → P1 → P2 → P3 → P4 → P5 → P6 → **P7 chiude a
vuoto**. Sono tutti scritti qui sotto, perché il valore del metodo sta nel poter leggere cosa è stato
scartato e perché.

---

## PARTE I — I FATTI, prima del piano

Contati sul disco il 2026-09-07. Nessuno ricordato.

| Fatto | Misura |
|---|---|
| Pagine catturate finora | **10** (`capture/01…09` + `11-armageddon`) |
| Report scritti | 10, per **2.362 righe** più i due di armageddon |
| Screenshot su disco | **381**, fuori dal repo (`.gitignore`, ~76 MB) |
| Pagine con **CSS e JS letti** | **1 su 10** — solo armageddon |
| Pagine con **screenshot per sezione** | **0** — tutte a fette verticali cieche, non per sezione |
| Pagine con **inventario effetti** (keyframes, transizioni, filtri) | **1 su 10** |
| Pagine con **schema strutturale** in dati, non in prosa | **0** |
| Pagine figlie note e mai toccate | almeno **6**: `/outemail`, `/outfunnel`, `/outheadline`, `/outviral`, `Timer`, `Funnel Operator` |
| Difetto noto della macchina di cattura | **B-057**: buca i `<p>` che contengono `<strong>` — e quel file è la base di ogni teardown di copy |

### La diagnosi in una riga

**Non abbiamo studiato un ecosistema: abbiamo fotografato dieci pagine e studiato bene una.**
I nove report vecchi sono buoni su copy e struttura e **ciechi** su come le pagine sono costruite —
cioè sullo strato che, su armageddon, ha prodotto la scoperta più preziosa di tutto lo studio.

---

## PARTE II — I SETTE GIRI

### P0 — il piano ingenuo

Catturare tutti i siti. Per ognuno scrivere un rapporto e un atlante visivo alla profondità di
armageddon. Ventiquattro documenti.

---

### P1 — la critica di P0

**A1 — P0 non ha un modello di costo, e i crediti sono già finiti una volta.**
Armageddon è costato: 1 cattura + 10 schermate viste + CSS e JS letti + 2 documenti da ~25 KB.
Moltiplicato per dodici pagine fa ~600 KB di scrittura e ~130 immagini da guardare. **Un piano che
non può essere finito non è un piano, è una lista di desideri.** E il 6 settembre la sessione è morta
esattamente così.

**A2 — P0 butta via 2.362 righe già scritte.**
I nove report vecchi non sono vuoti: sono **ciechi su una cosa sola**. Vanno **integrati** dove sono
sottili, non riscritti da capo. Riscrivere ciò che è già giusto è il modo più elegante di non
avanzare.

**A3 — P0 corre la macchina rotta dodici volte.**
`site_capture.py` ha B-057 aperto, non scarica CSS né JS, non fa screenshot per sezione, non ha
inventario degli effetti. **Correrla così produce dodici studi a cui manca esattamente ciò che ha
reso prezioso armageddon.** Prima si aggiusta lo strumento.

**A4 — "stessa profondità per tutti" è falso sui fatti.**
Sette pagine sono Squarespace/Framer: il loro CSS sono ventimila righe di framework, e leggerlo non
insegna niente. Tre sono costruite a mano (`claude-speedrun`, `apsales`, `armageddon`): lì il CSS
**è** lo studio. La profondità deve seguire il modo di costruzione.

> **P1 corretto:** prima si aggiusta e si potenzia la macchina; la profondità si differenzia per tipo
> di costruzione; i report esistenti si integrano invece di rifarli; il lavoro si organizza in
> passate con un costo dichiarato.

---

### P2 — la critica di P1

**A1 — "differenziare per tipo di costruzione" deciso da me è una scusa per fare meno.**
Il tipo va **misurato dalla macchina** (firma di Squarespace, Framer, Next, Webflow, o
"artigianale"), scritto nei dati e verificabile. Un criterio di profondità che dipende dal mio
giudizio è un criterio che si piega quando sono stanco.

**A2 — P1 produce dodici studi e non li collega.**
Max non ha chiesto dodici fotografie: ha chiesto di **prendere tutto**. Il valore sta nello **schema
ricorrente** — cosa fa sempre, cosa non fa mai, come cambia al cambiare del prezzo e della
temperatura del traffico. Quel documento non è un'appendice: **è il punto**. E va costruito da
**dati strutturati**, non rileggendo dodici prose (che è come si perdono le cose).

**A3 — P1 non tocca la Fabbrica.**
Uno studio che non diventa pattern, canone o gate è esattamente il guasto già diagnosticato: 2.362
righe che nessun agente legge. **Ogni sito deve chiudersi con un delta alla Fabbrica**, anche se il
delta è "niente di nuovo" — dichiarato.

**A4 — la fusione di `empire-premium-style` non ha un posto.**
Max l'ha chiesta esplicitamente. Ma **non può venire prima della sintesi**: quali nostri pezzi
sopravvivono si decide sapendo cosa abbiamo imparato, non prima.

> **P2 corretto:** la macchina emette **JSON strutturato per sito** oltre alle immagini; la sintesi
> nasce dai dati; ogni sito chiude con un delta alla Fabbrica; la fusione è una fase a sé, **dopo**
> la sintesi.

---

### P3 — la critica di P2

**A1 — l'ambizione, di nuovo.**
Dodici siti × (cattura + schermate per sezione + atlante + rapporto + delta) resta enorme. Va
ordinato per valore: **i tre siti artigianali sono dove vive lo strato 4** (il metodo). I sette
vecchi danno schema e copy, quasi niente metodo. Si lavora a **onde**, e ogni onda **si chiude e si
committa** da sola.

**A2 — "JSON strutturato" senza schema è peggio di niente.**
Se ogni sito emette una forma diversa, la sintesi è impossibile e ci si accorge alla fine. **Lo
schema si definisce prima della prima cattura.**

**A3 — le schermate per sezione, contate, uccidono il budget.**
Max chiede lo screenshot di ogni sezione con la spiegazione. Su `/copy` (26.952 px) le sezioni sono
40+. Dodici siti fanno **500+ immagini da guardare con la visione**. Da sole finiscono i crediti.
Serve una regola: **la visione passa solo sulle sezioni distinte**, deduplicate per firma
strutturale. Una sezione ripetuta si guarda una volta.

**A4 — manca la definizione di "finito".**
Il §6.22 dice *"si potrebbe ricostruire senza riguardare"*. Va reso operativo in una **lista di
spunte per sito**, o "finito" diventa "mi sono stancato".

> **P3 corretto:** onde ordinate per valore; schema dei dati definito prima; deduplicazione delle
> sezioni per firma strutturale; lista di spunte di chiusura per ogni sito.

---

### P4 — la critica di P3

**A1 — la deduplicazione non può essere un mio giudizio.**
La macchina deve calcolare una **firma strutturale** per sezione (tag + classi + numero di figli +
tipo di media + rapporto d'altezza) e raggruppare da sé. Io guardo un rappresentante per gruppo.

**A2 — il copy è finito in fondo, e Max l'ha chiesto esplicitamente.**
*"tutta anche lo studio e analisi del copy"*. E c'è una ragione più forte della richiesta: **il copy
è il suo prodotto vero** — vende corsi di copywriting. Lo strato del copy vale più di quello visivo.
Serve un artefatto **di prim'ordine** per sito: teardown sezione per sezione + le formule ricorrenti.
E la sintesi del copy vale, da sola, quanto quella visiva.

**A3 — dove vivono le cose.**
Dodici siti × cinque artefatti senza una pianta fissa diventano una palude in due giorni.

**A4 — la fusione non ha un perimetro.**
ADR-023 diceva che le quattro skill vecchie *"perdono l'autorità, non i file"*. Fondere
`empire-premium-style` cambia quel patto: va detto **cosa entra, cosa muore, e cosa resta dov'è**.

> **P4 corretto:** il copy diventa artefatto di prim'ordine, con la sua sintesi; pianta delle cartelle
> fissata prima; perimetro della fusione dichiarato.

---

### P5 — la critica di P4

**A1 — il piano assume che faccia tutto io nel filo principale. È così che sono morti i crediti.**
E l'alternativa ovvia — lanciare scagnozzi in parallelo — **è già stata provata e ha fallito due
volte** sul run dei video: *"limite di spesa colpito 2 volte in <24h, sempre dentro agenti paralleli,
mai nel filo sequenziale"* (`MASTER-RUN-TRACKER.md`, 2026-08-24). **Quindi il piano deve vietarlo
esplicitamente**, e dire perché, o qualcuno (io, fra tre settimane) lo riproverà.

**A2 — il piano non sopravvive alla propria morte.**
Se i crediti finiscono a metà di un'onda, la sessione dopo deve **ripartire dal disco**, non da una
riga "RIPRESA DA" — lezione già pagata: *"la riga RIPRESA DA non è una fonte. Prima di ripartire,
misurare su disco"*. Ogni passo deve essere **idempotente e riprendibile**: se l'artefatto esiste e
la sua spunta è verde, si salta.

> **P5 corretto:** esecuzione **solo sequenziale nel filo principale**, divieto scritto di batch
> paralleli con la ragione; ogni passo idempotente, ripresa misurata dal disco.

---

### P6 — la critica di P5

**A1 — non sappiamo quante pagine ha davvero l'ecosistema.**
Tutto il piano dice "dodici" e **dodici è una stima**. Le prove: il bio-link rivelò `outViral` e
`Timer` (mai catturati); `armageddon` ha rivelato quattro pagine figlie (`/outemail`, `/outfunnel`,
`/outheadline`, `/outviral`) e un prodotto in uscita (`Funnel Operator`); il corso `cs2online` vive
su un altro dominio ancora. **Un piano che parte da un numero stimato consegna uno studio incompleto
e non lo sa.** Il passo zero non è catturare: è **enumerare per davvero**, dalle pagine vive.

**A2 — manca cosa fa fallire questo piano.**
Un piano senza i propri modi di rompersi è un piano che si romperà in silenzio.

> **P6 corretto:** **passo 0 = enumerazione reale dell'ecosistema**, dalla navigazione, dai bio-link,
> dalle sitemap e dai link interni delle pagine già in mano; e una sezione dichiarata di modi di
> fallimento.

---

### P7 — chiude a vuoto

Riletto P6 cercando: un attacco al costo, uno all'ordine, uno alla verificabilità, uno alla
completezza. **Nessuno cade su qualcosa di sostanziale.** Le uniche osservazioni rimaste sono di
formulazione, non di sostanza. Il piano si chiude qui, come impone §6.20: si continua **finché un
giro non trova più niente**, e questo non ha trovato niente.

---

## PARTE III — IL PIANO DEFINITIVO

### Passo 0 — ENUMERARE (mezz'ora, prima di qualunque cattura)

Non si stima. Si legge dalle pagine vive:
- i link della barra di navigazione di `andrei-copy.com` (presenti su ogni pagina)
- i link del bio-link e il suo storico
- i link interni già dentro i `copy-integrale.md` delle 10 pagine in mano
- `sitemap.xml` e `robots.txt` di ogni dominio
- i domini noti: `andrei-copy.com`, `claude-speedrun.com`, `apsales.eu`, `bsns.it`, `armageddon.bsns.it`

**Esce:** `competitor/Andrei Pascu/site-study/ECOSISTEMA.md` — l'elenco **vero**, con dominio, ruolo,
prezzo se c'è, e stato (da catturare / catturato / studiato).

**Criterio:** l'elenco è chiuso quando due giri di scoperta non aggiungono più un URL.

---

### Passo 1 — LA MACCHINA (si aggiusta prima di correrla)

`site_capture.py` → **v2**. Cosa aggiunge, e perché ognuna:

| # | Cosa | Perché |
|---|---|---|
| 1 | **Fix B-057** — il testo del `<p>` ricomposto dai figli | il teardown del copy si fonda su quel file |
| 2 | **Scarica CSS e JS** serviti, in `capture/<slug>/src/` | è lo strato 4: su armageddon ha dato tutto |
| 3 | **Riconosce il modo di costruzione** (Squarespace / Framer / Webflow / Next / artigianale) | decide la profondità **per misura**, non per giudizio (P2-A1) |
| 4 | **Segmenta in sezioni** e ne fa lo **screenshot singolo** | è ciò che Max ha chiesto: ogni sezione con la sua spiegazione |
| 5 | **Firma strutturale per sezione** + raggruppamento dei doppioni | la visione passa una volta per gruppo, non per sezione (P3-A3) |
| 6 | **Inventario effetti**: `@keyframes`, transizioni, filtri, blend, `clip-path`, trasformazioni, `will-change` | "il tipo di effetti" richiesto, misurato |
| 7 | **Schema strutturale in JSON**: albero delle sezioni con altezza, ruolo, media, CTA, densità di testo | rende possibile la sintesi dai dati (P2-A2) |
| 8 | **`scheda.json` per sito**, schema fisso | senza schema fisso la sintesi non si fa (P3-A2) |

**Lo schema di `scheda.json`, fissato adesso:**
```
{ url, slug, dominio, ruolo, prezzo, costruzione, altezza, larghezza,
  palette: {testo[], sfondi[]}, caratteri[], scala_tipografica[], raggi[], curve[],
  effetti: {keyframes[], transizioni[], filtri[], blend[]},
  sezioni: [ {i, y, h, ruolo, firma, gruppo, tag, classi, media[], cta[],
              blocchi_testo, densita, screenshot} ],
  cta: [...], media: [...], meta: {...},
  difetti: [...], note_metodo: [...] }
```

---

### Passo 2 — LE ONDE (ordinate per valore, non per comodità)

**Solo sequenziale, nel filo principale. Niente batch di agenti paralleli.**
Ragione scritta: sul run dei video il limite di spesa è stato colpito **due volte in meno di 24 ore**,
sempre dentro agenti paralleli, mai nell'esecuzione sequenziale (`MASTER-RUN-TRACKER.md`, 2026-08-24).
Chi vorrà riprovarci fra tre settimane legga questa riga prima.

| Onda | Pagine | Profondità | Perché prima |
|---|---|---|---|
| **A** | `claude-speedrun.com`, `apsales.eu` | **piena** — CSS+JS letti, come armageddon | sono gli altri due artigianali: lì vive **lo strato 4** |
| **B** | `/outemail`, `/outviral`, `Timer`, `Funnel Operator` + ogni pagina nuova dal Passo 0 | piena o media secondo la costruzione misurata | **mai viste**: sono buchi veri, non integrazioni |
| **C** | le 7 pagine già catturate (`01`…`09`) | **integrazione**: sezioni + effetti + schema + copy, riusando il rapporto esistente | 2.362 righe già scritte da non buttare |
| **D** | sintesi trasversale | — | è il punto (P2-A2) |

Ogni onda **si chiude, si committa e aggiorna `ECOSISTEMA.md`** prima che parta la successiva.

---

### Passo 3 — GLI ARTEFATTI PER SITO (pianta fissa, decisa qui)

```
competitor/Andrei Pascu/site-study/
├── ECOSISTEMA.md                    l'elenco vero, con lo stato
├── capture/<slug>/
│   ├── desktop-NN.png  mobile-NN.png
│   ├── sezioni/NN-<ruolo>.png       ← NUOVO: una immagine per sezione
│   ├── src/                         ← NUOVO: CSS e JS serviti
│   ├── scheda.json                  ← NUOVO: i dati, schema fisso
│   ├── design-tokens.json  copy-integrale.md  dom-blocks.json
└── reports/
    ├── NN-<slug>.md                 rapporto: stile, colori, effetti, logica, difetti
    ├── NN-<slug>-ATLANTE.md         ogni sezione: immagine + misure + effetti + perché
    └── NN-<slug>-COPY.md            ← NUOVO: teardown del copy, sezione per sezione
```

**Il copy è di prim'ordine** (P4-A2): il copy è il prodotto che lui vende davvero.
`NN-<slug>-COPY.md` contiene: la promessa e dove sta · la gestione delle obiezioni · le prove e la
loro verificabilità · la scala di impegno chiesta al lettore · il rapporto grassetto/corpo · le
formule ricorrenti · cosa **non** dice mai.

**Lista di spunte di chiusura di un sito** (P3-A4) — un sito è studiato quando **tutte** sono vere:

- [ ] ogni sezione ha un'immagine, un ruolo e una spiegazione
- [ ] i colori sono presi dal DOM, con il conteggio d'uso
- [ ] la scala tipografica è misurata, non stimata
- [ ] gli effetti sono elencati con i tempi e le curve
- [ ] il copy ha il suo teardown sezione per sezione
- [ ] almeno un difetto reale è documentato (se non ce n'è, è scritto che non ce n'è)
- [ ] `scheda.json` è completo e valido
- [ ] esiste il **delta alla Fabbrica**: cosa entra nel canone, nei pattern, nei gate — o "niente", dichiarato

---

### Passo 4 — LA SINTESI (onda D)

Tre documenti, costruiti **dai `scheda.json`**, non rileggendo le prose:

1. **`SINTESI-SISTEMA-VISIVO.md`** — cosa fa sempre, cosa non fa mai, come cambiano palette,
   tipografia, densità ed effetti al variare di prezzo, temperatura del traffico e anno.
2. **`SINTESI-SISTEMA-COPY.md`** — le formule ricorrenti, la struttura tipica di una sua pagina di
   vendita, come tratta obiezioni, prove, garanzie e prezzo.
3. **`SINTESI-METODO.md`** — **lo strato 4**: come costruisce, con che strumenti, con che disciplina.
   Qui va tutto ciò che si ricava dai CSS commentati, dai `CLAUDE.md` citati, dai ticket, dai mockup
   misurati, dalle date nelle richieste.

---

### Passo 5 — LA FUSIONE DI `empire-premium-style` NELLA FABBRICA

Perimetro dichiarato (P4-A4):

| Cosa | Destino |
|---|---|
| `design-tokens.css` (483 righe): grana, silver-mixing, bubble, card, chip, hl-block, marquee, step-num | **entra nel canone**, tradotto in vanilla-first come impone §5 |
| `reference-page-full.tsx` (837 righe): 17 sezioni già scritte | diventa la **base dei pattern di Corsia B**, uno per uno, man mano che i cantieri li chiedono |
| `section-patterns.md` (117 righe, 10 puntatori su 17 già stale) | **muore**: sostituito dalla galleria generata |
| `build-playbook.md`, `layout-template.md`, `package.json.md`, `components.md` | **entrano nella Corsia B** come riferimento di scaffolding |
| `SKILL.md` di `empire-premium-style` | resta come **ingresso legacy** che rimanda alla Fabbrica, e smette di dettare legge |
| `digital-empire-lms/` | non è una skill: è un progetto. Resta dov'è |

**Poi** il canone sale a **v2** con ciò che le sintesi hanno insegnato, e i pattern crescono dagli 8
attuali con quelli che le onde hanno dimostrato ricorrenti (§10: due usi = pattern).

---

## PARTE IV — COME QUESTO PIANO PUÒ ROMPERSI (P6-A2)

| Modo di rottura | Segno precoce | Cosa si fa |
|---|---|---|
| **I crediti finiscono a metà onda** | — | ogni passo è idempotente: la sessione dopo **misura il disco** (esiste `scheda.json`? esiste la cartella `sezioni/`? esiste il report?) e riparte da lì. Mai da una riga "RIPRESA DA" |
| **La segmentazione in sezioni sbaglia** su un sito costruito male | sezioni con altezza assurda o una sola sezione per tutta la pagina | ripiego dichiarato: fette verticali come oggi, e il sito viene marcato `segmentazione: fallita` in `scheda.json` |
| **Un sito è protetto o cambia sotto le mani** | cattura vuota o diversa dalla precedente | si registra la data di cattura in `scheda.json` e si dichiara nel rapporto. Un sito vivo cambia: lo studio è datato, non eterno |
| **La sintesi trova troppo poco** perché i dati sono disomogenei | campi vuoti in molti `scheda.json` | è il rischio che lo schema fisso esiste per evitare. Se accade, si torna al Passo 1, non si "aggiusta a mano" |
| **Torno a trattare il tutto come dodici documenti** | crescono i report, non cresce la Fabbrica | la spunta *"delta alla Fabbrica"* è nella lista di chiusura di ogni sito, ed è quella che lo impedisce |

---

## PARTE V — L'ORDINE DI ESECUZIONE

```
0.  ECOSISTEMA.md          enumerare per davvero          ← si parte da qui
1.  site_capture.py v2     aggiustare e potenziare
2.  ONDA A                 claude-speedrun + apsales      profondità piena
3.  ONDA B                 le pagine mai viste
4.  ONDA C                 integrazione delle 7 vecchie
5.  ONDA D                 le tre sintesi
6.  FUSIONE                empire-premium-style → Fabbrica
7.  CANONE v2 + pattern    ciò che le onde hanno dimostrato
```

**Ogni riga si chiude, si committa e aggiorna `ECOSISTEMA.md` e `STATO-EMPIRE.md` prima della
successiva.** Nessuna riga si apre se la precedente non è verde.

---

## Connessioni
- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — dove va a finire tutto questo
- `.claude/skills/fabbrica-siti/CLAUDE-SITI.md` — la legge che riceve i delta
- `competitor/Andrei Pascu/site-study/README.md` — lo stato dello studio siti
- `emperator.md §6.20` (il piano si critica finché un giro non trova più niente) · `§6.22` (si prende
  tutto da tutti) · `§6.23` (ti modifichi da solo)
