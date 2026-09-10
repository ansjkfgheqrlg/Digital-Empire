# 35 — PIANO DI RICOSTRUZIONE: IL LIBRO DELL'AGENCY V2

> **Ordine di Max, 2026-09-10:** *"È veramente schifoso a livello di contenuti. Ti ho detto
> chiaramente che deve esserci tutta la formazione acquisita, tutta la conoscenza. Tutto su ogni
> argomento. Può essere enorme, questo libro deve essere una risorsa enorme. Devi rivedere
> completamente il modo in cui strutturi e inserisci il contenuto nella documentazione. Il PDF
> deve raggiungere minimo 100 pagine, ma questo come minimo."*
>
> Estetica e design: **approvati, non si toccano**. Il difetto è tutto nel contenuto.

- **Data:** 2026-09-10
- **Stato del piano:** V4 esecutivo (dopo tre giri di critica: P1, P2, P3 — tutti scritti sotto)
- **Sostituisce:** `PIANO-MAESTRO/34-LIBRO-AGENCY.md` (V1, 1.627 righe, 11 pagine PDF)

---

## PARTE 0 — LA DIAGNOSI: perché è uscito un libro da 11 pagine

Non è stata sfortuna né fretta. Sono cinque errori concatenati, e vanno nominati tutti perché
ognuno ha una contromisura diversa nel piano.

### Errore 1 — Ho scelto il formato prima del contenuto

Ho preso `pdf_engine_empire.py` — un motore nato per **dossier da 10-11 pagine**, dove ogni
pagina è un `<section>` ad altezza fissa `297mm` con `overflow:hidden` — e ho fatto entrare il
libro dentro quel formato. Il vincolo tecnico ha deciso quanto contenuto poteva esistere: undici
chiamate `doc.page()` scritte a mano, undici pagine. **Il contenitore ha deciso il contenuto.**

Peggio: `overflow:hidden` significa che qualunque contenuto ecceda l'altezza della pagina viene
**tagliato in silenzio**, senza errore. Quel motore non è solo inadatto a un libro: è
attivamente pericoloso per un libro.

### Errore 2 — Doppia compressione: ho riassunto materiale già riassunto

La conoscenza dell'Impero è una piramide a quattro livelli:

| Livello | Cos'è | Quanto pesa (misurato) |
|---|---|---|
| L1 — Sorgente | video/corsi originali | — |
| L2 — Integrale | `knowledge/<id>/contenuto-integrale.md` — tutto ciò che è stato visto e trascritto | **753.606 parole**, 78 cartelle |
| L3 — Atomi | `atoms.json` — conoscenza atomizzata con ancora verbatim + relazioni | **2.128 atomi KA** su 24 run |
| L4 — Pagine wiki | `Source_*.md` — sintesi già lavorata, con verdetto e gap-analysis | **79.737 parole**, 73 pagine |

Per scrivere il libro ho dato agli scagnozzi **solo L4** — il livello più alto e già sintetico
della piramide — e ho chiesto di riorganizzarlo. Riorganizzare una sintesi produce una sintesi
della sintesi. Il materiale vero (L2 e L3) non è mai entrato nel libro.

### Errore 3 — Ho ristretto il perimetro con una scusa metodologica

L'ordine era "tutta la formazione acquisita". Io ho selezionato **7 fonti su 73** con un criterio
che suonava rigoroso ("solo le pagine con tag attinenti ad agenzia") e l'ho persino scritto nel
libro come pregio, sotto la voce "Copertura e fonti". Non era rigore: era la mia comodità
travestita da criterio. Un libro che dichiara con orgoglio di aver escluso il 90% del materiale
disponibile ha già fallito il proprio mandato.

### Errore 4 — Ho dato agli agenti un target di LUNGHEZZA, non di COPERTURA

Nei tre prompt agli scagnozzi ho scritto *"orientativamente 250-450 righe"*. Un target di
lunghezza produce sempre compressione: l'agente ha materiale per 2.000 righe, legge "450", e
taglia. Ho ordinato io la sintesi che poi ho consegnato. **Il target giusto non è quanto è
lungo il capitolo: è quanti atomi della fonte sono entrati.**

### Errore 5 — Nessun gate. Il risultato corto è passato perché nulla lo fermava

È lo stesso identico schema del battito: la forma era scritta in dottrina, e usciva sbagliata
quattro volte al giorno finché non è nato `verifica_recap.py`, un controllo meccanico che
**blocca** invece di ricordare. Per i documenti non esiste nessun equivalente. Nessuno script
ha detto "questo capitolo cita 25 atomi su 323 disponibili: RIFIUTATO". Senza gate, la versione
corta passa sempre — perché è quella che costa meno a chi scrive.

> **La lezione, in una riga:** un documento non esce denso perché me lo ricordo. Esce denso
> perché una macchina conta gli atomi e rifiuta la consegna se mancano.

---

## PARTE 1 — I NUMERI VERI, contati sul disco il 2026-09-10

Nessuna stima. Ogni cifra sotto è stata contata da script su disco in questa sessione.

### 1.1 Il giacimento

| Giacimento | Misura |
|---|---|
| Atomi di conoscenza (`atoms.json`, 24 run) | **2.128 KA** |
| Contenuto integrale (`knowledge/`, 78 cartelle) | **753.606 parole** |
| Pagine wiki fonte (73 pagine) | **79.737 parole** |
| Studio competitor Andrei Pascu (130 file) | **413.292 parole** |
| Skill di dominio CRO/agency (`agency-scalping` 126.144 + `cro-call` 39.478 + altre 6) | **254.732 parole** |
| **Totale materiale disponibile** | **≈ 1.500.000 parole** |

Il libro V1 consegnato: **14.000 parole**. Ha usato **l'1,8% del materiale** — e su quel 1,8%
ha applicato un'ulteriore compressione.

### 1.2 I dieci run più ricchi (dove sta la conoscenza densa)

| Run | Atomi | Argomento |
|---|---|---|
| `max18-v09` NmoOZVTrTXA | 323 | agenti vocali, Vapi/Retell/n8n, offerte aziendali |
| `max18-v08` DI5aWJiFAt8 | 229 | Claude Cowork, delega operativa, subagenti |
| `max18-v06` JTn5pqm9ecM | 228 | costruzione agenti AI, 8 tecniche |
| `max18-v01` RnoC5IlOUhs | 205 | second brain Obsidian + Claude |
| `max18-doc` justin-sung | 88 | scienza dell'apprendimento |
| `max18-v04` 140FuW7b9pk | 78 | mindset, 4 emozioni |
| `max17-v02` beggiato-team | 77 | team marketing AI a 6 agenti |
| `max18-v05` RnNSRF4s9nk | 72 | bot trading con Claude Code |
| `max17-v07` rizzo-prompt | 71 | loop engineering, 5 livelli di verifica |
| `max17-v05` jaye-agenticos | 70 | agentic OS, framework ARMS |

Gli altri 14 run coprono SEO, LinkedIn, vendita, design, storytelling, personal brand, CFO AI,
caroselli, cross-model review, guida agenzia 4h17.

### 1.3 Il motore: misurato, non ipotizzato

Costruito e girato un test reale in questa sessione (`scratchpad/test_flusso.py`):
il CSS standard-oro applicato a un **flusso continuo** invece che a pagine fisse.

| Misura | Risultato del test |
|---|---|
| Pagine prodotte da 7.920 parole | **13** |
| Parole per pagina (testo denso puro) | **609** |
| Parole per pagina (stima con titoli, tabelle, citazioni, spazi) | **≈ 420-450** |
| Peso per pagina | **12,4 KB** |
| Grana incorporata | **1 sola volta**, riusata su tutte le pagine |
| Font veri incorporati | **3** (Onest + IBM Plex Mono) |
| Header/footer ripetuti su ogni pagina | sì, via `display_header_footer` di Playwright |

**Conseguenza:** 700 pagine ≈ 8,7 MB. Sotto il limite duro di 16 MB, sopra la soglia di
attenzione di 8 MB → la grana va generata una volta a risoluzione più bassa, oppure il PDF si
consegna in due tomi. Deciso in V4 (§5.4).

### 1.4 La scala che il materiale impone

| Ipotesi di densità | Parole totali | Pagine |
|---|---|---|
| 100 parole per atomo (citazione + una riga di contesto) | 212.800 | ≈ 500 |
| **150 parole per atomo (citazione verbatim + contesto + perché conta + come si applica)** | **319.200** | **≈ 740** |
| 200 parole per atomo (+ esempio costruito + collegamenti) | 425.600 | ≈ 990 |

**Il minimo di 100 pagine chiesto da Max corrisponde al 13% degli atomi.** Non è il bersaglio:
è il pavimento sotto cui il lavoro è rifiutato in partenza. Il bersaglio vero è la riga in
grassetto: **≈ 740 pagine, 2.128 atomi su 2.128.**

---

## PARTE 2 — PIANO V1 (prima stesura, poi criticata tre volte)

**V1 in una riga:** un volume unico da ~740 pagine, sette parti tematiche, un capitolo per fonte,
ogni capitolo scritto da un agente che deve citare ≥85% degli atomi della propria fonte, motore
PDF in flusso continuo, gate meccanico che conta gli atomi e rifiuta i capitoli magri.

### 2.1 Architettura del libro (V1)

- **Libro I — Il Metodo Digital Empire** (il nostro, non la formazione): ~90 pagine
- **Libro II — Acquisizione clienti**: LinkedIn organico, cold DM, SEO, caroselli, lead gen
- **Libro III — Vendita, prezzo, preventivi**
- **Libro IV — Consegna, delivery, scala, team**
- **Libro V — Costruire con l'AI**: agenti, Claude Code, second brain, token, orchestrazione
- **Libro VI — Contenuto, brand, storytelling, lanci**
- **Libro VII — Apprendimento, metodo di studio, mindset**
- **Appendici**: indice degli atomi, indice delle fonti, glossario

### 2.2 Produzione (V1)

Sette ondate, una per Libro. Ogni ondata: 4-6 agenti in parallelo, un capitolo per agente.
Ogni agente riceve: la fonte L2 (`contenuto-integrale.md`) + L3 (`atoms.json`) + la pagina wiki
L4 come mappa, e l'obbligo di citare tutti gli atomi.

### 2.3 Il gate (V1)

`scripts/gate_densita_libro.py`: conta i KA-id citati nel capitolo, li confronta con `atoms.json`,
rifiuta sotto l'85%.

---

## PARTE 3 — P1, PRIMA CRITICA (attacca V1)

**C1.1 — "Un capitolo per fonte" produce un libro che è un elenco di recensioni, non un libro.**
Ventiquattro capitoli, ognuno "cosa dice il video X", è la stessa struttura della wiki, solo più
lunga. Un lettore che vuole imparare l'acquisizione clienti non vuole leggere sei recensioni di
sei video: vuole *l'acquisizione clienti*, con dentro ciò che le sei fonti dicono, in conflitto
dove sono in conflitto. **L'organizzazione deve essere per ARGOMENTO, con le fonti che entrano
dentro l'argomento** — non per fonte.

**C1.2 — L'85% di copertura è un numero inventato.** Perché 85 e non 100? Se l'ordine è "tutta
la conoscenza", la soglia è **100% degli atomi**, con la sola eccezione degli atomi che il gate
stesso marca come duplicati fra fonti (lo stesso principio detto da due autori entra una volta
sola, con due citazioni). Serve quindi un passaggio di **deduplica fra fonti** prima della
scrittura, non una soglia di comodo.

**C1.3 — Sette ondate sequenziali sono lente e fragili.** Se ogni ondata richiede una sessione,
il libro finisce fra due settimane e ogni sessione rischia di perdere il filo. Serve un
**assemblaggio incrementale**: il PDF si rigenera ad ogni ondata, cresce, e Max lo vede crescere.
Un libro che esiste già a 200 pagine e cresce vale più di un libro perfetto che non esiste.

**C1.4 — Manca del tutto il Libro I.** "Il metodo Digital Empire, ~90 pagine" è scritto in una
riga, come se fosse la parte facile. È la parte che nessuna fonte esterna può scrivere al posto
nostro, e nella V1 del libro era 244 righe. Va costruito da: le 9 skill di produzione + i
**dossier di reparto** (`company/01-agency/*/BACKBONE.md`) + gli ADR + i checkpoint. Materiale
interno mai censito in questo piano.

**C1.5 — Nessuna parola su cosa fare con i 413.292 parole di Andrei Pascu.** Sono il 27% del
giacimento totale e il piano V1 le ignora.

---

## PARTE 4 — PIANO V2 (risponde a P1)

- **Organizzazione per argomento**, non per fonte (C1.1). Ogni capitolo è una *questione*
  ("Come si trova il primo cliente quando non hai case study"), e dentro entrano tutti gli atomi
  pertinenti, da qualunque fonte vengano, con la fonte citata atomo per atomo.
- **Copertura 100%** con deduplica dichiarata (C1.2): nasce un **registro degli atomi**
  (`atomi-index.json`) che mappa ogni KA a uno o più capitoli. Un atomo non mappato = buco che
  il gate segnala.
- **Assemblaggio incrementale** (C1.3): il PDF si rigenera ad ogni ondata.
- **Libro I costruito dal materiale interno** (C1.4), con censimento dedicato.
- **Andrei Pascu entra come Libro dedicato** (C1.5): è un corpus coerente (copywriting, funnel,
  lanci, email) e merita la propria parte.

---

## PARTE 5 — P2, SECONDA CRITICA (attacca V2)

**C2.1 — Il registro degli atomi è il vero collo di bottiglia, e V2 lo tratta come un dettaglio.**
Mappare 2.128 atomi su ~60 capitoli è un lavoro di classificazione che nessun umano farà a mano e
che un agente farebbe male se gli dessi 2.128 atomi insieme. Serve una **fase 0 di indicizzazione**
fatta a blocchi (un agente per run, che classifica i propri atomi in argomenti da una tassonomia
fissa data in anticipo). Senza tassonomia fissa data prima, ogni agente inventa le proprie
etichette e l'indice non si ricompone.

**C2.2 — "100% degli atomi" può produrre un libro illeggibile.** Alcuni atomi sono meccanici
(«il relatore apre il video dicendo il proprio nome»). Trattarli tutti come uguali gonfia senza
arricchire. Serve una **classificazione di peso** per atomo: *portante* (entra espanso),
*di supporto* (entra come citazione dentro un paragrafo), *di contesto* (entra nell'indice degli
atomi in appendice, non nel corpo). Così il 100% è mantenuto — nessun atomo sparisce — ma il
corpo del libro resta leggibile e l'appendice garantisce la tracciabilità totale.

**C2.3 — Il gate conta i KA-id, ma un agente può citare un KA-id senza portarne il contenuto.**
Scrivere «(KA-045)» accanto a una frase generica supera il gate e non insegna niente. Il gate
deve misurare anche **la sostanza**: parole per atomo portante (soglia), presenza dell'ancora
verbatim della fonte (la citazione letterale deve comparire, verificabile con ricerca nel testo
sorgente — è la stessa tecnica anti-invenzione già usata negli atomi).

**C2.4 — Il peso del PDF a 740 pagine (8,7 MB) sfora la soglia di attenzione.** V2 non decide.

**C2.5 — Nessuna previsione di quanto costa.** Ventiquattro-trenta run di agente da ~100-130K
token l'uno = ~3-4 milioni di token. Va detto prima, non scoperto a metà.

---

## PARTE 6 — PIANO V3 (risponde a P2)

- **Fase 0 — Indicizzazione** (C2.1): tassonomia degli argomenti fissata PRIMA, poi un agente per
  run classifica i propri atomi (argomento + peso portante/supporto/contesto) producendo
  `atomi-index.json`. Nessuno scrive un capitolo prima che l'indice esista.
- **Tre pesi per atomo** (C2.2): portante → espanso nel corpo (≥150 parole); supporto → citato
  dentro il flusso; contesto → riga nell'indice degli atomi in appendice. Copertura 100%
  garantita su tutti e tre i livelli.
- **Gate a tre misure** (C2.3): copertura KA, parole per atomo portante, presenza dell'ancora
  verbatim verificata contro il file sorgente.
- **Peso PDF** (C2.4): grana rigenerata a `size=90` e opacità invariata → immagine più leggera;
  se il PDF supera 12 MB, consegna in **due tomi** (Libri I-IV / Libri V-VIII), stesso stile,
  numerazione continua.
- **Costo dichiarato** (C2.5): ~30 run di agente, ~3,5 milioni di token, 6-8 ondate.

---

## PARTE 7 — P3, TERZA CRITICA (attacca V3)

**C3.1 — La tassonomia degli argomenti è la decisione più importante del piano, e V3 la lascia
implicita.** Se la tassonomia è sbagliata, 2.128 atomi finiscono nei posti sbagliati e il libro è
un magazzino ordinato male. Va scritta **in questo piano**, non rimandata alla Fase 0. E va
scritta partendo dagli atomi che esistono davvero, non da un'idea a priori di cosa dovrebbe
esserci in un libro sull'agenzia.

**C3.2 — Il libro rischia di essere una miniera senza porta d'ingresso.** Settecento pagine senza
un apparato di navigazione sono inutilizzabili. Servono, e vanno costruiti apposta: indice
generale a due livelli, **indice analitico** (concetto → pagina), **indice delle fonti**
(autore/video → capitoli in cui compare), **indice degli atomi** (KA-id → pagina), e per ogni
Libro una pagina di apertura che dice cosa ci si trova e in che ordine leggerlo.

**C3.3 — "Il metodo nostro" e "la formazione altrui" mischiati per argomento fanno perdere il
confine che Max ha chiesto esplicitamente.** V2 ha spostato l'organizzazione per argomento (giusto),
ma così il Libro I separato non basta più: dentro ogni capitolo tematico servirà un **blocco
finale dichiarato** — *"Cosa fa Digital Empire su questo punto"* — visivamente distinto, che tiene
il confine senza spezzare l'argomento.

**C3.4 — Il piano non dice cosa succede al libro V1 esistente.** Va dichiarato: `34-LIBRO-AGENCY.md`
e il suo PDF restano come **prima edizione**, archiviati, non cancellati (il lavoro fatto non si
butta, e serve come termine di paragone per misurare il salto). Il V2 nasce con numero nuovo.

**C3.5 — Nessun criterio di "finito".** Quando il libro è finito? Serve una definizione
verificabile da macchina, non a occhio.

---

## PARTE 8 — PIANO V4, ESECUTIVO

### 8.1 Identità del prodotto

| Voce | Valore |
|---|---|
| Titolo | **Il Libro dell'Agency — Edizione Integrale** |
| Sorgente | `PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE.md` |
| Motore | `PIANO-MAESTRO/scripts/pdf_engine_libro.py` (nuovo, modalità flusso) |
| Costruttore | `PIANO-MAESTRO/scripts/build_libro_integrale_pdf.py` |
| PDF | `PIANO-MAESTRO/36-LIBRO-AGENCY-INTEGRALE.pdf` + doppione in `documentazione Empire/Piani/Agency/` |
| Prima edizione (archiviata) | `34-LIBRO-AGENCY.*` — resta, non si cancella |
| Bersaglio | **≥ 700 pagine**, 2.128 atomi coperti al 100% |
| Pavimento di rifiuto | 100 pagine (sotto: lavoro respinto in partenza) |

### 8.2 La tassonomia — otto Libri, scritta ora (C3.1)

Costruita sugli argomenti che gli atomi coprono davvero, non a priori:

| # | Libro | Fonti principali che ci confluiscono | Atomi stimati |
|---|---|---|---|
| **I** | **Il Metodo Digital Empire** — come operiamo noi | 9 skill di produzione + BACKBONE di reparto + ADR + checkpoint | interni |
| **II** | **Trovare clienti** — ICP, outreach, LinkedIn, SEO, lead gen, caroselli | Trivellato, Beggiato LinkedIn, Nico SEO, Artem caroselli, Pascu lead-gen | ~280 |
| **III** | **Vendere e prezzare** — call, diagnosi, preventivi, obiezioni, retainer | Barron, Beggiato Karpathy, Pascu preventivi, cro-call, beast-preventivi | ~260 |
| **IV** | **Consegnare e scalare** — fulfillment, team, hiring, qualità, handover | Beggiato guida 4h17, Team Marketing AI, Belli Codex, delivery-playbook | ~230 |
| **V** | **Costruire con l'AI** — agenti, Claude Code, Cowork, agenti vocali, token, orchestrazione | v06, v08, v09, v01, Rizzo, Jay E, Belli token, Herk | ~1.100 |
| **VI** | **Contenuto, brand, lanci** — copy, funnel, storytelling, personal brand, YouTube | Pascu (413K parole), Vishen, MiK Cosentino, cro-copy-architect | ~200 |
| **VII** | **Imparare e decidere** — scienza dell'apprendimento, mindset, metodo di studio | Justin Sung, Jim Rohn, CFO AI (decisione sui numeri) | ~180 |
| **VIII** | **Apparati** — indice analitico, indice fonti, indice atomi (tutti i 2.128), glossario | tutte | — |

Il **Libro V è il più grande** (~1.100 atomi, oltre metà del giacimento): è il riflesso onesto di
cosa l'Impero ha davvero studiato quest'anno. Verrà diviso in sotto-parti (agenti, Claude Code,
memoria/second brain, orchestrazione, voce).

### 8.3 Le fasi

**FASE 0 — Indicizzazione (blocca tutto il resto)**
1. Scrivere `scripts/indicizza_atomi.py`: legge tutti gli `atoms.json`, produce lo scheletro di
   `atomi-index.json` con `{ka_id, run, tipo, contenuto, ancora, fonte}`.
2. Un agente per run (24 run, a ondate da 6): assegna a ogni proprio atomo **Libro + capitolo +
   peso** (portante / supporto / contesto) scegliendo SOLO dalla tassonomia §8.2.
3. Deduplica: `scripts/dedup_atomi.py` raggruppa atomi che dicono la stessa cosa da fonti diverse
   → un atomo "principale" con più citazioni.
4. **Uscita di Fase 0:** `atomi-index.json` completo, 2.128 atomi mappati, zero orfani.

**FASE 1 — Il motore**
5. `pdf_engine_libro.py`: flusso continuo, CSS standard-oro riusato verbatim, header/footer
   ripetuti, copertine e aperture di Libro come pagine forzate, indice generato da codice,
   numerazione continua. Base tecnica già verificata (§1.3).
6. Test di tenuta: 200 pagine finte → verifica peso, tempo di build, integrità.

**FASE 2 — Scrittura, otto ondate (una per Libro)**
7. Per ogni capitolo un agente riceve: gli atomi del capitolo dall'indice (con ancora verbatim),
   il puntatore ai `contenuto-integrale.md` da cui vengono, la pagina wiki come mappa,
   e **nessun target di lunghezza** — solo la lista di atomi da coprire e la soglia di parole
   per atomo portante.
8. Ogni capitolo chiude con il blocco dichiarato **"Cosa fa Digital Empire su questo punto"** (C3.3).
9. Dopo ogni ondata: rigenerazione del PDF (il libro cresce e si vede crescere).

**FASE 3 — Apparati e chiusura**
10. Indici generati da codice (analitico, fonti, atomi, generale) — non scritti a mano.
11. Vaglio pubblico: nessuna credenziale, nessun cliente reale, nessun numero interno.
12. Doppione + checkpoint + chiusura.

### 8.4 Il gate — `scripts/gate_densita_libro.py` (il pezzo che mancava)

Rifiuta un capitolo se anche solo una di queste condizioni non è soddisfatta:

| Misura | Soglia | Perché |
|---|---|---|
| Copertura atomi assegnati | **100%** — ogni KA del capitolo compare | l'ordine è "tutta la conoscenza" |
| Parole per atomo portante | **≥ 150** | sotto quella soglia è una citazione, non conoscenza trasmessa |
| Ancora verbatim presente | **≥ 90% degli atomi portanti** | impedisce di citare un KA-id senza portarne il contenuto |
| Blocco "Cosa fa DE" | presente | tiene il confine metodo/formazione |
| Marker vietati | zero | NO-STUB |

Il gate stampa l'elenco esatto dei KA mancanti: chi riscrive sa cosa aggiungere, non deve indovinare.

### 8.5 Criterio di "finito" (C3.5), verificabile da macchina

Il libro è finito quando, tutte insieme:
1. `atomi-index.json` non ha atomi orfani (2.128 / 2.128 mappati);
2. `gate_densita_libro.py` passa su **tutti** i capitoli;
3. il PDF generato ha **≥ 700 pagine**;
4. i quattro indici sono generati e i riferimenti di pagina risolvono;
5. il vaglio pubblico passa;
6. il doppione esiste.

### 8.6 Costo e ritmo, dichiarati prima

- **Fase 0:** 24 run di classificazione (~40K token l'uno) ≈ 1M token
- **Fase 2:** ~35-40 capitoli (~120K token l'uno) ≈ 4,5M token
- **Totale stimato:** ≈ 6M token, 8-10 ondate, distribuite su più sessioni con checkpoint.
- Ogni ondata lascia il libro **più grande e già consegnabile**: non esiste uno stato in cui il
  lavoro fatto non serve a niente.

### 8.7 Cosa cambia in permanenza (oltre questo libro)

L'errore 5 della diagnosi non riguarda solo il libro: riguarda **tutti** i documenti che produco.
Perciò, nello stesso turno in cui parte questo piano:
- il gate di densità nasce come **strumento generale**, non come script del libro;
- la regola entra in `emperator.md` come dottrina: *un documento di conoscenza non si misura in
  pagine, si misura in atomi coperti e parole per atomo — e lo dice una macchina, non io*;
- la stessa regola entra nella memoria di Emperator.

---

*Piano scritto il 2026-09-10. V1 → P1 → V2 → P2 → V3 → P3 → V4, i tre giri di critica restano
scritti sopra come da regola di Max. Approvazione richiesta prima della Fase 0.*
