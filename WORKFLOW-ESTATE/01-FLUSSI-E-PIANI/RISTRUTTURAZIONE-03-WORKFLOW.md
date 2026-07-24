---
Owner: Max
Controllore: Claude
Origine: WORKFLOW-ESTATE/01-FLUSSI-E-PIANI/RISTRUTTURAZIONE-02-CICLI.md
Governo: company/Mandato/MANDATO-EMPIRE.md
---

# ⚙️ PIANO 3 — OGNI FASE È UN WORKFLOW COMPLETO
> Livello 3 di 7 · 2026-07-24 · **Dimensione migliorata: il LAVORO diventa eseguibile.**
> Domanda a cui risponde: *cosa deve avere una fase per essere un workflow vero, e non un foglio di intenzioni.*

---

## §0 · AUTOCRITICA DEL PIANO 2

| # | Limite del Piano 2 | Perché è un problema vero |
|---|---|---|
| **L2.1** | **Le tracce non hanno un autore** | Si registra *che* è stata presa una decisione, non *chi* l'ha presa. Con Max, Gael e Gemini in parallelo, una decisione senza autore è ingovernabile |
| **L2.2** | **Nessuno legge le tracce** | Il Piano 2 lo ha ammesso. Un archivio che cresce e nessuno interroga è peso morto |
| **L2.3** | **Registra il lavoro ma non lo organizza** | Sa dire cosa è successo. Non sa dire *chi doveva farlo* né *con quale capacità* |
| **L2.4** | **Il rito di sessione è per una persona sola** | Non regge tre esecutori in parallelo |

### Il difetto che li riassume
Il Piano 2 ha costruito **la memoria di un corpo che non ha ancora organi**. Registra fedelmente un
lavoro che resta disorganizzato. È il momento di dare al lavoro una forma.

---

## §1 · DIMENSIONE MIGLIORATA DA QUESTO PIANO

**Una sola: una fase non è più un testo, è una cosa che si esegue.**

Oggi i 6 stream dell'estate sono file di 36-78 righe che dichiarano un `Owner:` e descrivono
delle intenzioni. **Nessuno di loro nomina un agente. Nessuno dichiara una skill.**
Nel frattempo l'azienda possiede **439 agenti, 53 skill, 22 workflow**.

> **439 agenti e 6 stream, e zero collegamenti fra i due.**

Il Piano 3 costruisce quel collegamento. È il piano più importante dei sette, perché è quello in
cui l'ordine di Max — *"ogni fase è un workflow, che deve avere skill, agenti"* — smette di essere
una frase.

---

## §2 · CONTENUTO DEL LIVELLO 3

### 2.1 — 🔑 Il modello esiste già: `YOUTUBE-AUTOMATION-FACTORY/`
**Scoperta del 24/07, e cambia l'impostazione di questo piano.** Un'altra sessione ha costruito la
fabbrica YouTube seguendo la direttiva APEX-7 di Max. Ha prodotto:

```
YOUTUBE-AUTOMATION-FACTORY/
  01-FLUSSI-E-PIANI/       WF1-niche-discovery … WF5-performance-audit
  02-AUTOMAZIONI-E-SCRIPTS/ apex7_orchestrator · quality_gate · gate_agent
                            event_bus · memory · meta_agent · self_improve · ruflo_connector
  memory/                   runs/ · performance_logs · learned_rules · strategy_store
```

Due fatti che contano più di qualunque teoria:
1. **Usa gli stessi 6 pilastri di `WORKFLOW-ESTATE/`.** Non è una coincidenza: è la forma che
   l'azienda produce naturalmente quando costruisce qualcosa di serio.
2. **Ha già i pezzi dell'APEX-7**: gate, gate agent, event bus, memoria, meta-agente, auto-miglioramento.

**Conseguenza per questo piano:** il modello di "workflow completo" **non va inventato — va
riconosciuto e generalizzato**. Vincolo sovrano rispettato in pieno: si aggiunge, non si ricostruisce.

**Ma va anche criticato, perché è nuovo e acerbo.** Le sue tracce di run contengono:
```json
{ "run_id": "yt-run-20260724-142612", "current_phase": 1, "created_at": "..." }
```
Tre campi. Dice *che una run è partita*, non cosa ha deciso, cosa è fallito, quanto è costata.
**È un segnaposto di avvio, non una traccia.** Il Piano 2 ne chiede cinque tipi, con contenuto.
Il Piano 3 adotta la *forma* della fabbrica YouTube e ci innesta le *tracce* del Piano 2.

### 2.2 — Lo standard: cosa rende una fase un WORKFLOW
Sei elementi. Meno di sei, e non è un workflow: è un appunto.

| # | Elemento | Perché è obbligatorio | Come si verifica |
|---|---|---|---|
| 1 | **Agenti assegnati** | senza esecutore il lavoro non parte | `agenti:` non vuoto, ogni id esiste in `empire agents` |
| 2 | **Skill dichiarate** | dice *con quale capacità* si fa | `skill:` non vuoto, ogni voce esiste in `empire skills` |
| 3 | **Ingresso e uscita** | senza uscita definita non si sa quando è finito | `input:` e `output:` dichiarati |
| 4 | **Gate di uscita** | criterio oggettivo di "fatto" | almeno 1 gate con condizione verificabile |
| 5 | **Tracce prodotte** | quali delle 5 tracce del Piano 2 lascia | `tracce:` elenca almeno decisione+prestazione |
| 6 | **Proprietario e controllore** | ADR-008: nessun artefatto orfano | intestazione conforme |

**Elemento 4 — nota che vale per tutto il sistema:** un gate non è un permesso, è **una domanda con
una risposta misurabile**. La differenza si è vista il 23/07: Gate-FUNNEL era 🟢 sulla dashboard e
🔴 nel file, perché il file poneva la domanda vera (*contiene ancora `YOUR_STRIPE`?*) e la dashboard
si limitava a riportare un'opinione.

### 2.3 — I 6 stream estate rimessi in forma
Max ha chiesto esplicitamente che la regola valga **anche per i 6 stream esistenti**.
Stato attuale misurato e destinazione:

| Stream | Oggi | Agenti da collegare | Skill già esistenti da dichiarare |
|---|---|---|---|
| **S1 Concessionari** | 71 righe, solo `Owner: Max` | A2-Acquisizione, A8-Closing | `beast-preventivi`, `cold-email`, `outreach-reply-triage` |
| **S2 Manuale** | 44 righe, `Owner: chief-forge` | IB-L2-VEND, IB-L2-LANC | `cro-copy-architect`, `emails`, `paywalls` |
| **S3/S4 Pagine** | 44 righe, `Owner: Gael` | CF-R4-Produzione-Testuale | `carousel-empire`, `social` |
| **S5 YouTube** | 47 righe, `Owner: YouTube-dept` | **già fatto**: la fabbrica APEX-7 esiste | `youtube-automation-factory`, `youtube-compliance-shield` |
| **S6 Preventa** | 36 righe, `Owner: chief-forge` | A1-Ricerca, A3-Preventivi | `case-study-forge`, `preventivo-auto` |
| **PERF-LOOP** | 78 righe | performance-cell | — |

**S5 è il modello**: è l'unico già in forma di workflow completo. Gli altri cinque si portano lì.
Questa tabella è il lavoro concreto del Piano 3 — non nuove entità, **collegamenti fra entità che
già esistono tutte**.

### 2.4 — L'autore su ogni traccia (risolve L2.1)
Ogni traccia del Piano 2 guadagna un campo obbligatorio: **chi**.
Non "il sistema": l'agente preciso, o la persona precisa. Il meccanismo esiste già e funziona —
`flow done --actor` e `--evidence` rifiutano il vuoto. Si estende a tutte e cinque le tracce.

Serve a una cosa concreta e già successa: il 19/07 Max e Gael hanno lavorato **sullo stesso file in
parallelo** e si è dovuto ricostruire a mano chi aveva fatto cosa (CP-20260719-008).

### 2.5 — Cosa NON fa questo piano
- **Non crea agenti nuovi.** Ce ne sono 439 e non sono collegati: creare il 440° peggiorerebbe il problema.
- **Non definisce chi comanda chi.** È il Piano 4.
- **Non fa leggere le tracce a nessuno** (L2.2 resta aperto). È il Piano 5.

---

## §3 · GATE DI PASSAGGIO L3 → L4

Soglia **5 su 6**.

| # | Criterio | Come si verifica | Se fallisce |
|---|---|---|---|
| **C1** | Lo standard dei 6 elementi è scritto e verificabile | un controllo dice se un file di workflow è conforme | rifare §2.2 |
| **C2** | **Almeno 3 dei 6 stream hanno agenti e skill dichiarati** | `agenti:` e `skill:` non vuoti e con id esistenti | il collegamento non è reale |
| **C3** | Ogni agente citato **esiste davvero** | ogni id compare in `empire agents` | agente inventato: errore grave, si corregge subito |
| **C4** | Ogni traccia ha un autore | nessuna traccia senza `chi` | rifare §2.4 |
| **C5** | Il modello YouTube è riusato, non duplicato | i 5 stream puntano allo stesso standard, non a copie | si è ricostruito invece di generalizzare: viola il vincolo sovrano |
| **C6** | Nessuno stream perde ciò che aveva | il contenuto vecchio resta, si aggiunge soltanto | ripristinare |

**C3 e C6 sono obbligatori anche a 5/6.** C3 perché un agente inventato è la bugia peggiore
possibile in un sistema di esecuzione. C6 perché è il vincolo sovrano di Max.

**Se il gate fallisce 3 volte:** si scende da 6 stream a 1 — S1, quello che porta i soldi — lo si
porta a workflow completo da solo, e si usa come modello per gli altri.

---

## §4 · AUTOCRITICA DEL PIANO 3

### ✅ Cosa ha migliorato davvero
- **Ha trovato il modello invece di inventarlo.** `YOUTUBE-AUTOMATION-FACTORY` esisteva già e
  contiene i pezzi dell'APEX-7: riconoscerlo vale più che progettarne uno nuovo, e rispetta il
  vincolo additivo alla lettera.
- **Ha reso il collegamento agenti↔lavoro un numero**, non un'aspirazione: oggi 0, e la tabella
  §2.3 dice esattamente quali collegamenti creare.
- **Ha criticato anche ciò che adotta**: le tracce della fabbrica YouTube sono tre campi e l'ho
  detto, invece di prenderla per buona perché è nuova.
- **Ha messo un tetto agli agenti nuovi: zero.** Il problema non è la quantità, è il collegamento.

### ⚠️ Cosa manca ancora (compito del Piano 4)
- **Nessuna gerarchia.** Se due agenti dello stesso stream danno risposte opposte, non c'è chi decide.
- **Nessun carico di lavoro.** Un agente può risultare assegnato a sei stream contemporaneamente e
  nessuno se ne accorge.
- **I reparti esistono ma non comandano.** `empire departments` li elenca; nessuno di loro ha
  autorità su un workflow.
- **Non è detto chi controlla chi**: ADR-008 dà un controllore a ogni artefatto, ma non a ogni *lavoro*.

### 🔴 Il rischio di questo piano, dichiarato
**Collegamenti di facciata.** È facilissimo scrivere `agenti: [A2-Acquisizione]` in un file e
dichiarare fatto il Piano 3, senza che quell'agente esegua mai nulla. Sarebbe la stessa malattia del
Piano 1 — descrivere invece di eseguire — a un livello più alto.

La difesa è C3 (l'agente deve esistere davvero) ma **C3 non basta**: verifica che l'agente esista,
non che lavori. La prova vera arriverà solo quando una traccia riporterà quell'agente come autore.
**È il Piano 5 a dover chiudere questo buco, e lo dichiaro qui perché non venga dimenticato.**

### SCORE PIANO 3 — **9.0 / 10**
Il più alto finora: è il piano che esegue l'ordine centrale di Max, e poggia su un modello reale
già costruito e verificato su disco anziché su una proposta. Perde 1 punto per il rischio dei
collegamenti di facciata, che questo livello **non può** chiudere da solo.

---
⛓️ P12: `RISTR-03-WORKFLOW#empire` · migliora: [PIANO 2](RISTRUTTURAZIONE-02-CICLI.md) · migliorato da: [PIANO 4](RISTRUTTURAZIONE-04-GERARCHIA.md)
