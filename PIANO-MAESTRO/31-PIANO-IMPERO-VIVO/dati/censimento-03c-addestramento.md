---
Type: CENSIMENTO
Status: In lavorazione
Tags: #forze #addestramento #ingaggio #scagnozzi #sentinelle #doombot #ADR-015
Created: 2026-09-06
Autore: DOOM BOT — censimento 03c (addestramento e modulo d'ingaggio)
Base gia' scritta da altri: censimento-03b-regolamento-forze.md · censimento-03b2-cadute.md
---

# CENSIMENTO 03c — L'ADDESTRAMENTO DELLE FORZE E IL MODULO D'INGAGGIO

> **Cosa e' questo documento.** Il regolamento (03b) dice *che gradi esistono*. Le cadute (03b2)
> dicono *come si muore*. Questo dice **cosa deve sapere una forza prima di muovere un dito**
> e **con quale forma esatta la si schiera**.
>
> Sezione 1 e' censimento: nessuna riga senza il file aperto e la misura presa.
> Sezioni 2 e 3 sono progetto: marcate **PROGETTO:**, perche' oggi non esistono.

---

## SEZIONE 1 — LE FONTI DI CONOSCENZA

**Misure prese sul disco il 2026-09-06** con `wc -l` / `wc -c`. Righe e caratteri sono quelli
reali, non stimati.

### 1.0 Il quadro in una tabella

| # | Fonte | Righe | Caratteri | Natura |
|---|---|---:|---:|---|
| F1 | `.claude/agents/conoscenza-empire.md` | 244 | 13.070 | agente-biblioteca (opus) |
| F2 | `.claude/skills/empire-context/SKILL.md` | 136 | 8.634 | skill di contesto aziendale |
| F3 | `company/Mandato/MANDATO-EMPIRE.md` | 242 | 14.420 | costituzione, 8 Articoli |
| F3b | `company/Mandato/README.md` | 65 | 3.279 | come il Mandato vincola e si modifica |
| F4 | `company/Memory/decisions/` (25 file) | 1.902 tot | ~100.000 | le decisioni: 24 attive + 1 proposta |
| F5 | `company/Memory/INDEX.md` | 212 | 88.232 | indice maestro a puntatori |
| F6 | `company/Memory/STATO-EMPIRE.md` | 9.371 | 746.109 | stato corrente + storico |
| F7 | `second-brain-vault/wiki/index.md` | 1.749 | 273.302 | catalogo di 1.800+ pagine |
| F8 | `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` | 98 | 5.635 | il ciclo a 9 passi (ADR-006) |
| F9 | `CLAUDE.md` (radice progetto) | 155 | 6.745 | le regole caricate d'ufficio |
| F10 | `.claude/agents/emperator.md` | 1.560 | 89.906 | la dottrina completa del comandante |
| F11 | `company/Ispettorato/principi/PRINCIPI.md` | — | 3.110 | P1-P6, il metro dell'autocritica |
| F12 | `company/Ispettorato/regole/REGOLE.md` | — | 3.294 | R1-R8, **bloccanti** |
| F13 | `company/Ispettorato/registro/REGISTRO-ERRORI.md` | — | 8.670 | il registro anti-recidiva |
| F14 | `company/Memory/BACKLOG.md` | 278 | 49.368 | cio' che non blocca (ADR-005) |
| F15 | `company/Memory/templates/` (3 file) | — | — | ADR-template · CP-template · session-template |
| F16 | `scripts/cerca_wiki.py` | — | 15.739 | motore di ricerca coi sinonimi |
| F17 | `scripts/emperator_hook.py` | — | 19.235 | secondo corpo della dottrina (hook) |
| F18 | `scripts/gate_battito_hook.py` | — | 8.666 | il gate che blocca la consegna |
| F19 | `.claude/agents/` + `.claude/skills/` | 164 agenti · 297 skill | — | cio' che l'Impero sa gia' fare |

**Totale grezzo delle fonti F1-F14: oltre 1,4 milioni di caratteri.** E' il numero che rende
impossibile «dare tutto a tutti»: e' il vincolo economico da cui nasce la Sezione 2.

---

### F1 — `.claude/agents/conoscenza-empire.md` (244 righe, 13.070 char)

**L'agente che possiede la formazione.** Livello dichiarato: *LX — accanto al Mandato e
all'organo MAXIMILIAN, sopra il Board C-Suite*. ID registro `KNOW-EMPIRE-001`, modello `opus`,
origine direttiva Max 2026-09-02, supervisore Emperator.

**Cosa sa** (§3, tabella delle 8 fonti in ordine di autorita'):

1. archivio video vivo — `SKILL & Agenti/Empire Studio Suite/empire-studio/memory-empire/knowledge/`, 53+ cartelle
2. wiki / second brain — `second-brain-vault/wiki/`, 1.828+ pagine
3. formazione su disco — `Formazzione/`, `InfoBusiness/`, `Matriale linkeding/`, `Progetti Claude/`
4. framework proprietari — APSOC completo, Bibbia dei Messaggi, script chiamata fredda
5. piani e governo — `PIANO-MAESTRO/` (39 dossier), `company/Memory/`
6. competitor — `competitor/`, wiki `sources/Source_*` (Andrei Pascu 34+ video)
7. skill e agenti — `.claude/skills/`, `.claude/agents/`
8. sistemi di marca — Brand Guidelines CCM (18 pagine, 15 capitoli, valori misurati dal DOM)

**Come la distribuisce** (§4): ordine di ricerca fisso *archivio video -> wiki -> formazione su
disco -> framework -> piani*, e un formato d'uscita a 5 blocchi — conoscenza consolidata,
framework applicabili, numeri e soglie, contraddizioni fra le fonti, **dove l'Impero NON sa**.
Regola di consegna: *«Espandi, non riassumere»*.

**Come lo si interroga.** Non ha un comando: si invoca come agente (`subagent_type:
"conoscenza-empire"`) con una domanda di dominio. Il suo primo colpo pero' e' uno strumento
riusabile da chiunque, ed e' l'unico modo economico per cercare in 1.800 pagine:

```bash
python scripts/cerca_wiki.py "gestione delle obiezioni sul prezzo" --n 15
```

Fa cio' che `Grep` non fa: espande coi sinonimi, taglia le desinenze, pesa le parole per
rarita', non premia i papiri, toglie i doppioni, mostra la riga in cui la cosa compare.

**Le tre leggi che impone a se' stesso** (§2) — e che la Sezione 2 promuove a legge di tutti:
la fonte accanto a ogni affermazione; **non inventa** (dire «l'Impero non sa» vale oro);
non confonde il letto col dedotto (l'inferenza si marca `+`); non appiana le contraddizioni.

**Il difetto dichiarato, che pesa sull'addestramento.** `CP-20260902-002` (citato nel caso 30
di 03b2): *«l'agente esiste ma non ha ancora alimentato nessuno»*. F1 e' oggi una biblioteca
senza lettori: e' esattamente il buco che questo censimento deve chiudere.

---

### F2 — `.claude/skills/empire-context/` (un solo file: `SKILL.md`, 136 righe, 8.634 char)

La cartella **contiene un file solo**. Nessun `references/`, nessuno script. Dentro:

- **§0 memory-first** (ADR-002, dichiarato non negoziabile): INDEX -> STATO-EMPIRE -> ADR dell'area
- **§1 chi siamo** — Max founder + Gael socio, monorepo `ansjkfgheqrlg/Digital-Empire`, un solo
  account Claude; posizionamento *«l'agenzia progettata per essere licenziata»*, voce
  *«prove non promesse»*
- **§2 l'offerta** coi prezzi: Outreach Factory 4.000 · Content Factory 3.500 · Second Brain
  2.500 · Engine Room 8.000; gate copy APSOC >=80/100
- **§3 i 10 ecosistemi** in tabella + la gerarchia LX->L5
- **§4 le regole non negoziabili**, ridotte alle 5 che servono sempre: memory-first, wiki-first,
  wrap mai riscrittura (ADR-003), dry-run prima di spendere, gate qualita'
- **§5 il sync GitHub** (ADR-004) e cosa non viaggia nel repo
- **§6 come guidare Gael**
- **§7 la mappa dei file di verita'** — «per questa domanda, questo file»
- **§8 la storia essenziale** fino al 2026-06-10

**Giudizio d'uso, motivato:** e' la fonte piu' vicina a un «minimo comune» gia' esistente, ma
**e' dell'11 giugno** — cita «PIANO-MAESTRO (10 dossier)» quando i dossier sono 39, e
«ADR-001..004» quando gli ADR attivi sono 24. Ha inoltre il difetto strutturale che la Sezione 2
corregge: 8.634 caratteri sono ~2.200 token, **troppi per essere pagati a ogni ingaggio di ogni forza**.

---

### F3 — `company/Mandato/` — gli Articoli (242 + 65 righe, 14.420 + 3.279 char)

`MANDATO-EMPIRE.md` e' **la costituzione**. Otto Articoli piu' una checklist operativa:

| Art. | Titolo |
|---|---|
| 1 | Identita' e Posizionamento |
| 2 | Brand Voice («prove, non promesse») |
| 3 | Offerta e Pricing Policy |
| 4 | Qualita' (gate non bypassabili) |
| 5 | Memory-first e Wiki-first (ADR-002, pattern #12 e #13) |
| 6 | Multi-tenant by design (pattern #11) |
| 7 | Sicurezza (zero segreti, PII protetta) |
| 8 | Regola Assoluta del Workflow Reale e Autocontenuto (Struttura Tangibile 360°) |
| — | Checklist Brand Gate (da copiare nei gate QA) |

`README.md` dichiara la catena di comando in una riga sola, ed e' la riga che ogni forza deve
avere in testa: **`Mandato (LX) > Board (L0) > Ecosistema (L1) > Reparto (L2) > Workflow (L3) >
Agente (L5)`** — *«conflitto tra un ordine di reparto e un Articolo -> vince l'Articolo, sempre»*.
Modificabile **solo da Max, via ADR**. Deroga possibile solo registrata, per il singolo caso.

Il README dichiara anche il meccanismo di distribuzione **gia' previsto e mai realizzato**:
*«Gli agenti caricano il Mandato compresso via skill `empire-context` (hook pre-task)»*. Il
Mandato compresso, oggi, **non esiste come file**: e' il pezzo che manca ed e' il cuore della Sezione 2.

---

### F4 — `company/Memory/decisions/` — TUTTI gli ADR

25 file, 1.902 righe complessive. `V` = **vincolante per chiunque lavori** (qualunque forza, in
qualunque area). `A` = vincolante solo per chi tocca quell'area. `P` = proposta, non attiva.

| | ADR | Titolo | Stato |
|---|---|---|---|
| A | 001 | EMPIRE OS: holding di 10 ecosistemi su modello AION GROUP | ATTIVO |
| **V** | **002** | **Pattern memory-first: interroga prima, checkpoint dopo, sempre** | ATTIVO |
| **V** | **003** | **Migrazione asset = wrap, mai riscrittura** | ATTIVO |
| **V** | **004** | **Monorepo GitHub + sync automatico bidirezionale Max-Gael** | ATTIVO |
| **V** | **005** | **I blocker minori non fermano la costruzione: vanno in BACKLOG** | ATTIVO |
| **V** | **006** | **Il Ciclo di Fase Empire a 9 passi sostituisce «fase-controllo-avanti»** | ATTIVO |
| A | 007 | PIANO V2: la Direttiva di Scala (supera lo standard v1) | ATTIVO |
| **V** | **008** | **Catena di intestazione e controllo (ogni artefatto e' intestato, collegato, controllato)** | ATTIVA |
| A | 009 | Espansione Holding da 10 a 13 Ecosistemi Permanenti | ATTIVA |
| A | 010 | Fusione Ruflo Backbone + motore APEX-7-CORE | ATTIVO |
| A | 011 | Censimento della quinta implementazione APEX-7 e chiusura del perimetro | ATTIVO |
| A | 012 | Nuovo motore di orchestrazione canonico: `orchestration-layer` | ATTIVO (Fase 2 non iniziata) |
| A | 012-bis | Ponte esplicito company/Memory ↔ wiki (memory-wiki-bridge + `/sync-wiki-totale`) | ATTIVO |
| **V** | **013** | **Blob pesanti fuori dalla storia git: .gitignore mirato + guard, NON Git LFS** | ATTIVO |
| A | 014 | Il codice del flusso libro torna a chiamare un modello (tentativo #4) | ATTIVO |
| **V** | **015** | **La gerarchia delle forze di Emperator e l'assetto God Emperor Doom** | ATTIVO |
| A | 016 | Dottrina integrale all'apertura, sveglia leggera per messaggio | (senza campo Stato) |
| **V** | **016-bis** | **L'ULTIMO METRO: il lavoro finito ha un organo che lo guarda** | ATTIVO |
| **V** | **017** | **Il lavoro ad alto rischio lo rilegge un motore di famiglia diversa** | ATTIVO (pilota, perimetro stretto) |
| A | 018 | Due decisioni portano il numero 012, e due motori sono canonici insieme | ATTIVO + decisione aperta per Max |
| A | 019 | Il motore di orchestrazione canonico e' `orchestration-layer` | ATTIVO |
| A | 020 | Nasce la TESORERIA: Digital Empire comincia a contare i soldi | ATTIVO |
| A | 021 | Pivot piano editoriale @Legamidiamore: sequenziale non parallelo | ATTIVO |
| A | 022 | Lo studio di AI TUBE PRO si chiude con un'opera, non con un archivio | ACCETTATA |
| P | PROPOSTA | Audit cross-model in fase GATE per i deliverable ad alto rischio | PROPOSTA (non attiva) |

**Vincolanti per chiunque: 10** — 002, 003, 004, 005, 006, 008, 013, 015, 016-ultimo-metro, 017
(quest'ultimo in pilota su perimetro stretto). Sono i soli che hanno diritto di stare nel minimo comune.

**Due trappole di numerazione, entrambe sul disco:** esistono **due ADR-012**
(`orchestration-layer` e `ponte-memory-wiki`) — conflitto gia' registrato da ADR-018 — e **due
ADR-016** (`dottrina-integrale-all-apertura` e `ultimo-metro`), quest'ultima coppia **non ancora
sanata da nessun ADR**. E' la stessa famiglia del caso 33 di 03b2 (collisione di numero fra
sessioni parallele). Una forza che cita «ADR-012» senza dire quale, sta citando male.

---

### F5 — `company/Memory/INDEX.md` (212 righe, 88.232 char)

Indice maestro a **puntatori** — dichiara in testa: *«una riga per voce, solo puntatori — il
contenuto vive nei file»*. Sezioni: Stato corrente · **Decisioni attive (ADR)** · Corpus
Maximilian · Backlog · **Checkpoint** (righe 32-199, la parte che pesa) · Piani · Sessioni ·
Template · Cartelle operative.

Nota di misura che conta per il costo: 212 righe ma **88 KB** — righe lunghissime (media 416
caratteri). Non e' un file «leggero» solo perche' ha poche righe: **vale ~22.000 token.**

---

### F6 — `company/Memory/STATO-EMPIRE.md` (9.371 righe, 746.109 char)

Lo stato corrente **e tutto lo storico in coda**, dal piu' recente. Il primo blocco al momento
della misura e' `## 2026-09-06 — Un campo di Fliki che protegge i canali, mai compilato —
CP-20260906-002`. Contiene anche i blocchi `COORDINAMENTO` che ADR-006 impone prima di ogni
build grosso.

**E' la fonte piu' importante e la piu' pericolosa da dare a un subagente: 746 KB valgono
~190.000 token.** Nessuna forza puo' leggerlo intero. Chi lo cita nel prompt di un ingaggio
senza dire *quante righe* leggere sta finanziando una caduta da budget (03b2, gruppo A1:
9 episodi distinti).

---

### F7 — `second-brain-vault/wiki/index.md` (1.749 righe, 273.302 char)

Catalogo master della wiki. Sezioni: Aree Strategiche (mappe master) · Team · Riferimenti
Architetturali · Tool & Sistemi Operativi · **Tutti i Documenti (indice alfabetico per area)**
da riga 180 in poi. Vale ~68.000 token: e' un **catalogo da interrogare**, mai da allegare.
Lo strumento giusto resta `scripts/cerca_wiki.py` (F16).

---

### F8 — `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` (98 righe, 5.635 char)

Il metodo, ADR-006. I 9 passi: **RECALL · SPEC · PRE-MORTEM · BUILD · GATE AUTOMATICO ·
REVIEW INDIPENDENTE (+5-bis MAXIMILIAN) · TEST FUNZIONALE/AMNESIA · COMMIT · RETRO.**

Cinque righe di questo file sono gia' addestramento delle forze e vanno estratte cosi' come sono:

- passo 2: *«Idempotenza: ogni task/prompt deve poter ripartire a meta' senza duplicare»*
- passo 2: *«Budget-guard: se restano <20% delle risorse di sessione -> NON iniziare build nuovi»*
- passo 3: *«Agenti: cartelle disgiunte, fonti di verita' esplicite (dossier), divieto di scrivere
  su wiki/log.md e Memory/ (solo il conductor)»* — **il perimetro di scrittura e' legge dal
  giugno 2026, e le cadute di 03b2 dicono che non e' mai finito nei prompt.**
- passo 4: *«Check eseguibili, non opinioni... I gate non si bypassano.»*
- passo 5: *«Chi costruisce non si approva da solo.»*

---

### F9 — `CLAUDE.md` di radice (155 righe, 6.745 char)

**L'unica fonte che arriva a destinazione da sola**, senza che nessuno la citi: il sistema la
carica d'ufficio in ogni sessione della directory. Contiene REGOLA ZERO (memory-first, ADR-002),
REGOLA UNO (ciclo di fase a 9 passi, ADR-006), la REGOLA WIKI-FIRST, il template di pagina wiki,
l'identita' di Digital Empire e la REGOLA PUNTATORI («mai stale»).

**E' anche la scoperta piu' importante della Sezione 1 per il costo:** una forza schierata via
`Agent` parte comunque **a freddo** rispetto alla conversazione (emperator.md §6.7: *«parte a
freddo, non sa nulla di questa conversazione»*), e tutto cio' che sa **del compito** le arriva
dal proprio prompt d'ingaggio. Da qui l'intera Sezione 2: **cio' che conta viaggia nel prompt,
non si spera nel file di progetto.**

---

### F10 — `.claude/agents/emperator.md` (1.560 righe, 89.906 char)

La dottrina del comandante, e la sola fonte che descrive **come si scrive un prompt di ingaggio**:

- §6.7 (righe 466-486) — *«Come si scrive un prompt per uno scagnozzo: parte a freddo... percorsi
  assoluti, criteri di "fatto" espliciti, formato d'uscita esatto, e idempotente»*
- §6-bis.2 (riga 1369) — **le quattro parti obbligatorie del prompt di una Sentinella**
- §6-bis.3 (righe 1377-1396) — aree disgiunte, prompt a freddo, *«un Doom Bot che dice "fatto"
  non e' una prova: la prova e' il comando che TU hai eseguito dopo»*
- riga 118 — *«Nei prompt agli scagnozzi imponi la lingua: "rispondi in italiano". Si risolve a
  monte»* — la lingua e' gia' dichiarata come clausola di prompt, non come speranza.

Secondo corpo della stessa dottrina: la stringa `DOTTRINA` di `scripts/emperator_hook.py` (F17),
tenuta leggera (~2.000 caratteri per messaggio, misurato alla riga 1107 di emperator.md).

---

### F11-F13 — `company/Ispettorato/` — il metro e i divieti

- **`principi/PRINCIPI.md`** (3.110 char) — P1 misurare non produce · P2 la recidiva e' un
  fallimento del sistema, non dell'esecutore · P3 append-only · P4 **zero numeri inventati** ·
  P5 indipendenza da chi costruisce · P6 studiare anche i successi.
- **`regole/REGOLE.md`** (3.294 char) — **otto regole bloccanti**, non consigli: R1 nessuna run
  senza report · R2 niente report a mano se la telemetria esiste · R3 recidiva = blocco commit ·
  R4 un errore chiuso non si riapre senza verifica indipendente · R5 registro append-only ·
  R6 **zero numeri inventati** · R7 **nessun verdetto senza evidenza citata** · R8 chi audita non ripara.
- **`registro/REGISTRO-ERRORI.md`** (8.670 char) — il registro anti-recidiva da cui 03b2 ha
  tratto meta' dei suoi casi.

**R6 e R7 sono gia', parola per parola, due delle regole che il minimo comune deve portare a
tutti.** Oggi vivono in una cartella che nessuna forza schierata apre mai.

---

### F14-F19 — le fonti di servizio

- **`company/Memory/BACKLOG.md`** (278 righe, 49.368 char) — ADR-005: cio' che non blocca. Una
  forza non lo legge, ma **deve sapere che esiste**: e' li' che finisce cio' che trova e non deve fare.
- **`company/Memory/templates/`** — `ADR-template.md`, `CP-template.md`, `session-template.md`.
- **`scripts/cerca_wiki.py`** (15.739 char) — il primo colpo di ricerca, prima di `Grep`.
- **`scripts/emperator_hook.py`** (19.235 char) e **`scripts/gate_battito_hook.py`** (8.666 char) —
  i due hook: il secondo e' la prova viva della regola 26 di 03b2 (una regola ceduta due volte
  diventa un controllo che blocca, non una riga di regolamento in piu').
- **Il parco forze esistente:** 129 agenti di progetto + 35 globali = **164 agenti**; 172 skill di
  progetto + 125 globali = **297 skill**. E' fonte d'addestramento a sua volta: emperator.md
  §6-bis.2 impone di usare *«l'agente specializzato che gia' esiste, se ce n'e' uno che calza —
  non duplicare cio' che l'Impero ha gia'»*.

---

### 1.1 Le tre lacune che questo censimento trova

1. **Nessun file di «minimo comune» esiste.** Il piu' vicino e' F2 (`empire-context`), ma e'
   fermo all'11 giugno e pesa ~2.200 token. Il Mandato compresso previsto dal README di F3
   («hook pre-task») **non e' mai stato scritto**.
2. **Nessun modulo d'ingaggio esiste come modello riempibile.** Le regole per scriverlo sono
   sparse fra emperator.md §6.7, §6-bis.2, §6-bis.3 e il passo 3 di F8: **quattro punti diversi,
   nessuno copiabile**. Ogni ingaggio viene riscritto a mano, e 03b2 mostra cosa succede quando
   un pezzo si dimentica.
3. **La biblioteca non ha lettori.** F1 esiste dal 2026-09-02 e `CP-20260902-002` dichiara che
   *«non ha ancora alimentato nessuno»*: le forze non sanno nemmeno di poterla chiamare.

---

## SEZIONE 2 — L'ADDESTRAMENTO

> **PROGETTO:** nulla di questa sezione esiste oggi come file. Le fonti sono censite in
> Sezione 1; le regole vengono da 03b (gerarchia) e 03b2 (le 29 regole pagate con 33 cadute).

### 2.0 Il vincolo che decide tutto — l'addestramento si paga N volte

Un ingaggio non e' una lezione: e' una **spesa ripetuta**. Ogni carattere del minimo comune si
paga **a ogni singola forza, a ogni singolo ingaggio**. In questa stessa sessione sono schierate
**14 forze**: cio' che costa 1.000 token per forza costa 14.000 token alla notte, e non produce
una riga di lavoro.

Conversione usata in tutta la sezione: **1 token ≈ 3,8 caratteri** di italiano corrente. Le
misure di partenza sono quelle prese in Sezione 1.

| Cosa si potrebbe dare a ogni forza | Caratteri | ≈ token | × 14 forze |
|---|---:|---:|---:|
| **Minimo comune proposto (§2.1)** | **976** | **~260** | **~3.600** |
| `10-METODO-CICLO-FASE.md` intero | 5.635 | ~1.480 | ~20.700 |
| `CLAUDE.md` intero | 6.745 | ~1.775 | ~24.850 |
| `PRINCIPI.md` + `REGOLE.md` | 6.404 | ~1.685 | ~23.600 |
| `empire-context/SKILL.md` intero | 8.634 | ~2.270 | ~31.800 |
| `conoscenza-empire.md` intero | 13.070 | ~3.440 | ~48.200 |
| `MANDATO-EMPIRE.md` intero | 14.420 | ~3.795 | ~53.100 |
| `company/Memory/INDEX.md` | 88.232 | ~23.220 | ~325.000 |
| `wiki/index.md` | 273.302 | ~71.920 | ~1.007.000 |
| `STATO-EMPIRE.md` | 746.109 | ~196.345 | **~2.749.000** |

L'ultima riga non e' un'ipotesi teorica: **e' la causa dichiarata del gruppo A1 di 03b2 —
9 episodi distinti di forze morte per limite di budget.** E il caso 1 lo dice in modo ancora
piu' netto: *«prompt agenti troppo READ-HEAVY: bruciavano il budget leggendo reference PRIMA di
scrivere, morivano prima di produrre valore»* — 4 agenti morti, **1 file su 62**; il re-run con
la struttura inline passa *«da 1 file/21 tool_use a 16 file/20 tool_use»*.

**Conclusione che governa tutto il resto:** l'addestramento non e' «quanto sa la forza», e'
**quanto poco basta perche' non faccia danni**. Ogni riga in piu' va giustificata con una caduta
che quella riga avrebbe evitato. Se non c'e' la caduta, la riga esce.

---

### 2.1 IL MINIMO COMUNE — cio' che ogni forza deve sapere prima di muovere un dito

**10 righe. 976 caratteri. ~260 token.** Misurato, non stimato a occhio.

```
LEGGE COMUNE DELL'IMPERO — vale per ogni forza, sempre
1. ITALIANO in ogni riga, rapporto compreso.
2. NON INVENTI: nessuna affermazione senza un file che hai aperto, citato col path.
   Numero che non hai = [DM], mai una cifra plausibile.
3. SCRIVI SUBITO: crea il file d'uscita entro il primo minuto e risalvalo a ogni
   sezione finita. Chi cade deve lasciare il lavoro fatto.
4. PERIMETRO: scrivi SOLO nei path del tuo incarico. Tutto il resto e' sola lettura.
   Mai company/Memory/, mai wiki/log.md, mai i file di altre forze.
5. NON TI ALLARGHI: se trovi altro da fare, non lo fai — lo elenchi in fondo al rapporto.
6. IDEMPOTENTE: rieseguirti due volte non deve rompere ne' duplicare nulla.
7. NON DELEGHI il tuo incarico ad altri agenti.
8. FATTO = un comando che lo dimostra, non una tua dichiarazione. Nel rapporto scrivi
   cosa hai scritto davvero e cosa no.
9. SE CADI a meta': lascia il file com'e'. Chi riprende rilegge il file e riparte dalla
   prima sezione mancante.
```

**Perche' esattamente queste nove, e nessun'altra.** Ognuna ha un morto alle spalle:

| # | Nasce da | Prova |
|---|---|---|
| 1 | direttiva permanente di Max sulla lingua | emperator.md riga 118: *«Nei prompt agli scagnozzi imponi la lingua... Si risolve a monte»* |
| 2 | regole 13 e 17 di 03b2 | caso 23 (numeri inventati sostituiti con `[DM]`), caso 27 (61 lead che non esistono come file), R6+R7 dell'Ispettorato |
| 3 | **regola 8 [MECCANICA]** di 03b2 | casi 8, 9, 12, 29 — 175 scene su 352 perse; antidoto gia' provato due volte |
| 4 | invariante ADR-015 + passo 3 di ADR-006 | *«divieto di scrivere su wiki/log.md e Memory/ (solo il conductor)»*; caso 22 (swarm che si sovrascrivono), caso 33 (checkpoint sovrascritto) |
| 5 | quarta parte obbligatoria del prompt Sentinella | emperator.md riga 1369 |
| 6 | ADR-006 passo 2 | *«ogni task/prompt deve poter ripartire a meta' senza duplicare»* |
| 7 | ADR-015 §1.2 di 03b | le forze non schierano altre forze |
| 8 | regole 15 e 16 di 03b2 | casi 10 e 28: *«le sentinelle morte avevano dichiarato lavoro fatto... che non risultava vero sul disco»* |
| 9 | regola 20 di 03b2 | casi 29 e 32: la ripresa parte dal disco, non dal racconto |

**Cosa il minimo comune NON contiene — e perche' toglierlo e' la decisione piu' importante:**

- **Niente memory-first (ADR-002/REGOLA ZERO).** Sembra un'eresia, ed e' invece l'unica scelta
  difendibile: `STATO-EMPIRE.md` vale ~196.000 token e `INDEX.md` ~23.000. Imporre il RECALL a
  14 forze significa spendere 2,7 milioni di token in lettura prima di una riga di lavoro — cioe'
  ricreare esattamente il caso 1 e il gruppo A1. **Il RECALL resta di Emperator**, che lo fa una
  volta e travasa nel prompt le 3-6 righe che servono a quella forza (§3, blocco `CONTESTO`).
  Nessuna forza deve *scoprire* il contesto: deve *riceverlo* gia' distillato.
- **Niente Mandato integrale** (3.795 token): gli Articoli 1, 3, 6 non toccano mai una forza di
  censimento o di bonifica. Art. 2 (prove non promesse) e Art. 7 (zero segreti) entrano nel
  terreno di chi scrive copy e di chi tocca credenziali, non nel minimo comune.
- **Niente offerta, prezzi, 10 ecosistemi, storia dell'Impero.** Sono contesto d'azienda, non
  regole di condotta: una forza che conta file non ne fa nulla, e le paga comunque.
- **Niente elenco degli ADR.** Un riferimento nudo («rispetta ADR-008») a freddo non e'
  addestramento, e' rumore: l'agente non sa cosa sia e non ha budget per andarlo a leggere.
  Cio' che di un ADR serve, **si scrive per esteso** dentro la regola (come nelle 9 righe sopra).

---

### 2.2 L'ADDESTRAMENTO DI TERRENO — solo per chi tocca quell'ambito

Il terreno **non si somma al minimo comune per tutti**: si aggiunge **solo alla forza che entra
in quell'ambito**, e solo il blocco che le serve. Ogni blocco e' progettato per stare **sotto le
15 righe** (~400 token), perche' oltre quella soglia si torna nel caso 1.

| Terreno | Chi lo riceve | Righe | ≈ token | Forma consigliata |
|---|---|---:|---:|---|
| T1 codice dell'Impero | chi scrive o modifica file di codice/agenti | 12 | ~330 | blocco inline |
| T2 copy | chi produce testo che esce verso l'esterno | 10 | ~290 | inline + `subagent_type` esistente |
| T3 soldi | chi spende, o scrive un numero di cassa | 8 | ~230 | inline + rimando a reparto |
| T4 account e credenziali | chi tocca `.env`, sessioni, chiavi | 7 | ~200 | inline, **divieti secchi** |
| T5 video | chi produce, monta o pubblica video | 10 | ~290 | inline + `subagent_type` esistente |

#### T1 — IL CODICE DELL'IMPERO

```
TERRENO CODICE
- ADR-003: un sistema attivo non si riscrive, si avvolge. `Outreach/Outreach Workflow/`
  e' in produzione: non lo tocchi senza un sostituto gia' validato.
- ADR-013: niente blob pesanti nella storia git. Video, zip, PNG di copertina, DB lead,
  .env e sessioni browser non entrano nel repo (ADR-004).
- La console e' cp1252: ogni script che stampa emoji va lanciato con PYTHONIOENCODING=utf-8.
- `sed` col delimitatore `|` rompe le righe di tabella markdown: per quelle usa Python.
- Frontmatter di un agente: un `": "` non quotato dentro `description` fa sparire l'agente
  IN SILENZIO. Description su una riga sola, fra virgolette.
- Un controllo che verifica solo l'esistenza di un file non e' un controllo: provalo contro
  lo scheletro vuoto. Se lo scheletro passa, il controllo non esiste.
- Il ramo di errore di un indicatore non e' mai verde.
```
*Fonti:* ADR-003, ADR-004, ADR-013 · `EMP-URQ7.md` trappole 7 e 8 · nota di costruzione in
`conoscenza-empire.md` (*«successo davvero il 2026-08-31: 85 skill su 296 erano mute per
questo»*) e caso 15 di 03b2 (4 agenti morti per due caratteri) · regole 21 e 22 di 03b2
(casi 6, 25, 26). *Forze gia' esistenti da preferire:* `sentinel-drift`, `sentinel-security`,
`caveman:cavecrew-investigator` per la sola lettura.

#### T2 — IL COPY

```
TERRENO COPY
- Framework obbligatorio APSOC (Attenzione-Problema-Soluzione-Obiezioni-CTA), gate >= 80/100.
- Mandato Art. 2: prove, non promesse. Nessun claim senza il numero e la sua fonte.
- Marca CCM (fonte: company/02-info-business/ccm/brand/CCM-Brand-Guidelines.pdf):
  · l'arancione #fb4604 e' il colore dell'azione, sotto il 10% dell'area — non e' l'identita',
    il concorrente diretto usa lo stesso identico arancione;
  · la firma e' l'argento su fondo inchiostro, ed e' cio' che ci riconosce col logo coperto;
  · la grana non si spegne mai, e in stampa e' un PNG ripetuto, MAI un filtro SVG.
- Non consegni copy senza passare dal gate: chi scrive non si approva da solo.
```
*Fonti:* `empire-context/SKILL.md` §2 e §4 · Mandato Art. 2 e Art. 4 · `conoscenza-empire.md`
§3 «REGOLA DI MARCA» · ADR-006 passo 5. *Forze gia' esistenti:* `cro-copy-architect`,
`sentinel-brandvoice`, `guild-copy-apsoc`. **Una forza generica non scrive copy: si passa il
lavoro all'agente di terreno che esiste gia'** (emperator.md §6-bis.2: *«non duplicare cio' che
l'Impero ha gia'»*).

#### T3 — I SOLDI

```
TERRENO SOLDI
- Nessuna spesa reale (API, crediti, abbonamenti) senza ok esplicito di Max: prima il dry-run.
- Budget-guard: sotto il 20% delle risorse di sessione non si aprono lavori nuovi, si chiude.
- Un solo lavoro pesante in parallelo nell'Impero, e prima si scrive il blocco COORDINAMENTO
  in company/Memory/STATO-EMPIRE.md.
- Un numero di cassa non si stima MAI: o viene dal reparto Tesoreria, o si scrive [DM].
  Reparto: company/Ecosistemi/14-TESORERIA/ — agente `tesoreria-conductor`.
```
*Fonti:* `empire-context/SKILL.md` §4 (dry-run, pattern #3) · ADR-006 passo 2 (budget-guard) ·
regola 2 [MECCANICA] di 03b2 (casi 3 e 19) · ADR-020, che nasce dal fatto misurato
*«Digital Empire non misurava un solo euro»* · R6 dell'Ispettorato. *Forze:* `tesoreria-*`,
`sentinel-cost`, `cfo-empire`.

#### T4 — GLI ACCOUNT E LE CREDENZIALI

```
TERRENO CREDENZIALI — divieti, non consigli
- Una chiave, un token o una password NON entra mai in un prompt, in un rapporto o in un
  file d'uscita. Nemmeno mascherata, nemmeno «per esempio».
- Non apri .env per leggerlo tu: la via ufficiale e' l'agente `credential-keeper`.
- .env, sessioni browser (instagram/linkedin_session.json, session_data/, maps_session/) e
  DB lead non entrano nel repo: e' ADR-004, ed e' gia' nel .gitignore.
- Mandato Art. 7: zero segreti, PII protetta.
- `.cache-tools/` non ti riguarda: non lo leggi, non lo citi, non lo nomini.
```
*Fonti:* Mandato Art. 7 · ADR-004 (elenco di cio' che non viaggia) · `.claude/agents/credential-keeper.md`
(esiste, ed e' l'unico organo autorizzato a restituire valori di API key) · `conoscenza-empire.md`
§3 «Fuori dal tuo perimetro». **Da riportare a Max finche' non e' chiuso:** `EMP-URQ7.md`
trappola 6 — *«la chiave del servizio di posta (Brevo) e' pubblica da mesi e mai sostituita.
Va cambiata sul servizio»*: riscrivere la storia git non la richiude.

#### T5 — I VIDEO

```
TERRENO VIDEO
- Sequenziale, non parallelo: ADR-021 e la misura di CP-20260826-002 — 9/9 video chiusi in
  sequenza senza un fallimento, contro batch paralleli falliti ripetutamente.
- Misura il carico PRIMA di accettarlo: watchdog a 600s e tetto immagini per richiesta sono
  limiti reali. Un lotto di 75 frame in un colpo viene scartato per intero.
- La riduzione dei frame si fa con il rilevatore di scene, non a mano:
  "SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/scene_detector.py" (misurato:
  4.309 -> 1.066 frame, -75,3%).
- La fabbrica sta in YOUTUBE-AUTOMATION-FACTORY/: il gate di qualita' e'
  02-AUTOMAZIONI-E-SCRIPTS/quality_gate.py, i pezzi finiti stanno in VIDEO-PRONTI/.
- ADR-022: uno studio si chiude con un'opera, non con un archivio.
```
*Fonti:* ADR-021, ADR-022 · caso 17 e caso 21 di 03b2 · path verificati sul disco il 2026-09-06.
**Puntatore stantio trovato mentre scrivevo (da correggere, non da rifare qui):** 03b2 caso 17
cita `scripts/scene_detector.py`, ma sul disco il file sta in
`SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/scene_detector.py`. Una forza che
seguisse il puntatore vecchio non troverebbe nulla — e' esattamente la REGOLA PUNTATORI di
`CLAUDE.md` (*«un puntatore vecchio e' peggio di nessun puntatore»*).

---

### 2.3 LA FORMA CONCRETA — quanto costa ciascuna, e quale si sceglie

| Forma | Costo per ingaggio | Arriva sempre? | Funziona a freddo? | Rischio dimostrato |
|---|---|---|---|---|
| **A. Blocco inline nel prompt** | il suo peso esatto, ogni volta | **si', garantito** | **si'** | se cresce, esplode ×N |
| **B. File da leggere (path nel prompt)** | ~25 token nel prompt **+ il file intero + 1-2 tool_use** | no: la forza puo' non aprirlo | si', ma cara | **caso 1: 4 agenti morti, 1 file su 62** |
| **C. Riferimento nudo («rispetta ADR-008»)** | ~10 token | si' | **no** | l'agente non sa cosa sia: rumore |
| **D. `subagent_type` di un agente gia' definito** | 0 dal prompt (lo carica il sistema) | si' | si' | va costruito una volta; se il frontmatter e' rotto **sparisce in silenzio** (caso 15) |
| **E. Chiamata su richiesta (`conoscenza-empire`, `cerca_wiki.py`)** | 0 finche' non serve | no | si' | oggi **non lo chiama nessuno** (caso 30) |

**La scelta, e il perche'.**

1. **Il minimo comune va in FORMA A — inline, sempre, in ogni ingaggio di ogni grado.** E'
   l'unica forma che non puo' essere saltata, non costa un solo `tool_use` e sopravvive alla
   partenza a freddo. Il prezzo di questa scelta e' che **il minimo comune deve restare piccolo
   per legge**: 10 righe sono il tetto, non un obiettivo. Ogni riga nuova costa ~26 token ×
   ogni forza × ogni notte, e va pagata con una caduta documentata.
2. **Il terreno va in FORMA A per i divieti, FORMA D per il mestiere.** I divieti (credenziali,
   perimetro, sequenzialita') devono arrivare sempre: inline. Il mestiere vero — scrivere copy,
   contare soldi, montare video — **non si insegna nel prompt: si delega all'agente che gia'
   esiste** (`cro-copy-architect`, `tesoreria-conductor`, `ytf-*`). L'Impero ha 164 agenti e 297
   skill: riaddestrare a mano cio' che e' gia' costruito e' la spesa piu' stupida possibile.
3. **La FORMA B si usa solo con il numero di righe scritto accanto al path**, e mai per piu' di
   due file (regola 9 di 03b2: *«massimo 2-3 letture, prima scrittura entro i primi tool_use»*).
   «Leggi `STATO-EMPIRE.md`» senza un intervallo di righe e' un ordine di suicidio da 196.000 token.
4. **La FORMA C non si usa mai da sola.** Un ADR si cita **accanto** alla regola gia' scritta
   per esteso, come etichetta di provenienza — mai al posto della regola.
5. **La FORMA E va accesa.** `conoscenza-empire` esiste dal 2026-09-02 e `CP-20260902-002`
   dichiara che *«non ha ancora alimentato nessuno»*. Costo zero finche' non la si chiama:
   basta che il modulo d'ingaggio (§3) porti **una riga** che dice alla forza che puo' chiamarla,
   e la biblioteca smette di essere inerte senza costare un token a chi non ne ha bisogno.

---

## SEZIONE 3 — IL MODULO D'INGAGGIO

> **PROGETTO:** oggi questo modulo non esiste come file riempibile. Le sue parti sono sparse fra
> `emperator.md` §6.7, §6-bis.2, §6-bis.3 e il passo 3 di ADR-006 — quattro punti diversi,
> nessuno copiabile. Qui vengono unite in una forma sola, pronta da incollare.

### 3.0 Cosa e' stato imparato dai prompt di questa notte

**Hanno funzionato** (i censimenti 03b e 03b2 sono interi sul disco **nonostante** un guasto di
rete che ha ucciso dei doom bot — `CP-20260905-019`, caso 8 di 03b2). Cosa avevano in comune:

- **un file d'uscita solo, dichiarato con path assoluto, e dichiarato «tuo»** — nessuna
  contesa possibile con le altre forze schierate in parallelo;
- **la regola anti-caduta scritta in cima, in grassetto**: *«scrivi ogni sezione sul file appena
  e' finita, poi passa alla successiva. Mai accumulare»*;
- **la ripresa gia' scritta nel prompt**: *«se il file esiste, leggilo e riparti dalla prima
  sezione mancante»* — cioe' l'idempotenza dichiarata come procedura, non come principio;
- **le sezioni elencate una per una**, ognuna con cosa doveva contenere;
- **i divieti in fondo, secchi**: non modificare nessun altro file, non toccare i file degli
  altri doom bot al lavoro adesso, solo italiano, non inventare senza fonte aperta;
- **il formato del rapporto finale dichiarato in anticipo**, cosi' il rapporto non e' un tema
  libero ma una risposta a tre domande.

**Hanno perso tutto** i prompt larghi, ed e' misurato: caso 1 — *«prompt agenti troppo
READ-HEAVY... morivano prima di produrre valore»*, 4 agenti, 1 file su 62; caso 20 — i quattro
agenti *«partiti dai file leggeri (README, ARCHITETTURA) invece che dal contenuto di valore»*,
4 reparti su 10 incompleti, uno mai iniziato.

**La forma segue da qui:** perimetro stretto, scrittura incrementale, gate eseguibile.

---

### 3.1 IL MODULO — modello riempibile, pronto da copiare

I segnaposto sono `<...>`. Le righe senza segnaposto **non si toccano**: sono la parte fissa.
I blocchi marcati `[opzionale]` si tolgono quando non servono.

```text
Sei <GRADO: SCAGNOZZO | SENTINELLA | DOOM BOT> di Digital Empire, al servizio di EMPERATOR.
Ti chiami <scagnozzo|sentinella|doombot>-<slug>.
Parti a freddo: non sai nulla della conversazione in corso. Tutto cio' che ti serve e' qui sotto.

DIRECTORY DI LAVORO: <path assoluto>
FILE DI USCITA (uno solo, tuo): <path assoluto>          [togliere per lo SCAGNOZZO]

LEGGE COMUNE DELL'IMPERO — vale sempre
1. ITALIANO in ogni riga, rapporto compreso.
2. NON INVENTI: nessuna affermazione senza un file che hai aperto, citato col path.
   Numero che non hai = [DM], mai una cifra plausibile.
3. SCRIVI SUBITO: crea il file d'uscita entro il primo minuto e risalvalo a ogni
   sezione finita. Chi cade deve lasciare il lavoro fatto.
4. PERIMETRO: scrivi SOLO nei path del tuo incarico. Tutto il resto e' sola lettura.
   Mai company/Memory/, mai wiki/log.md, mai i file di altre forze.
5. NON TI ALLARGHI: se trovi altro da fare, non lo fai — lo elenchi in fondo al rapporto.
6. IDEMPOTENTE: rieseguirti due volte non deve rompere ne' duplicare nulla.
7. NON DELEGHI il tuo incarico ad altri agenti.
8. FATTO = un comando che lo dimostra, non una tua dichiarazione. Nel rapporto scrivi
   cosa hai scritto davvero e cosa no.
9. SE CADI a meta': lascia il file com'e'. Chi riprende rilegge il file e riparte dalla
   prima sezione mancante.

TERRENO <CODICE | COPY | SOLDI | CREDENZIALI | VIDEO>          [opzionale: solo se lo tocchi]
<incollare qui il solo blocco di terreno pertinente — censimento 03c §2.2>

PERIMETRO
  PUOI SCRIVERE SOLO QUI: <path assoluti, uno per riga>
  NON DEVI TOCCARE MAI:   <path assoluti> — <motivo in mezza riga>
  Ovunque altrove: SOLA LETTURA.
  <se ci sono forze in parallelo:> Altre forze stanno lavorando adesso su <path>: non aprirli
  in scrittura per nessun motivo.

CONTESTO MINIMO — gia' distillato, non andare a cercarne altro
  - <fatto 1 gia' verificato, con la fonte>
  - <fatto 2 ...>
  Fonti che puoi aprire, con le righe: <path> (righe N-M) · <path> (righe N-M)
  Non aprire company/Memory/STATO-EMPIRE.md ne' second-brain-vault/wiki/index.md per intero:
  sono rispettivamente ~196.000 e ~72.000 token e ti uccidono prima di produrre.
  Se ti serve sapere cosa l'Impero ha gia' imparato su un argomento: chiama l'agente
  `conoscenza-empire`, oppure `python scripts/cerca_wiki.py "<domanda>"`. Non cercare a mano.

L'INCARICO
  In una frase: <la missione>.
  <sezione/passo 1> — deve contenere: <cosa esattamente>
  <sezione/passo 2> — deve contenere: <cosa esattamente>
  <...>
  Ordine di esecuzione: comincia dalla parte piu' costosa, non dalla piu' facile.

USCITA ATTESA
  Dove: <il file d'uscita, path assoluto>
  Formato: <markdown con queste intestazioni esatte / JSON con questo schema / ...>
  Rapporto in chat, alla fine: <3-6 righe> che rispondono a: <domanda 1> · <domanda 2> · <domanda 3>

REGOLA ANTI-CADUTA — obbligatoria
  Crea il file d'uscita con titolo e intestazioni vuote ENTRO IL PRIMO MINUTO.
  Scrivi ogni sezione sul file appena e' finita, poi passa alla successiva. Mai accumulare.

RIPRESA / IDEMPOTENZA
  Se il file d'uscita esiste gia': leggilo e riparti dalla prima sezione mancante.
  Non ricominciare da capo, non duplicare, non riscrivere cio' che c'e' gia'.
  <se rilavori su file esistenti:> Un file legacy della versione precedente NON si salta:
  si supera in modo esplicito.

IL GATE — hai finito bene SOLO se questo comando da' questo esito
  <comando eseguibile, path assoluti>
  Atteso: <valore esatto: un numero, una stringa, exit 0>
  Eseguilo TU prima di consegnare e incolla l'uscita nel rapporto. Senza questa uscita
  il lavoro non e' consegnato.

SE CADI A META'
  Lascia il file com'e': non cancellare, non riscrivere l'inizio.
  Nel rapporto dichiara quali sezioni sono SU DISCO e quali no — «scritto» significa
  presente nel file, non presente nella tua testa.

DIVIETI
  Non modificare nessun file fuori dal perimetro, per nessun motivo.
  Non inventare: se una cosa non e' in un file che hai aperto, non la scrivi.
  Non riassumere le fonti: si espande, si cita, si riporta la riga.
  Non delegare questo incarico ad altri agenti.
  Solo italiano.
```

---

### 3.2 LE TRE VARIANTI GIA' COMPILATE

#### A) SCAGNOZZO — `haiku` · una domanda, una risposta · vive secondi

```text
Sei uno SCAGNOZZO di Digital Empire, al servizio di EMPERATOR. Ti chiami scagnozzo-frontmatter.
Parti a freddo: non sai nulla della conversazione in corso. Tutto cio' che ti serve e' qui sotto.

DIRECTORY DI LAVORO: C:\Users\Utente\Desktop\qui tutto\Digital Empire

LEGGE COMUNE DELL'IMPERO — vale sempre
1. ITALIANO in ogni riga, rapporto compreso.
2. NON INVENTI: nessuna affermazione senza un file che hai aperto, citato col path.
   Numero che non hai = [DM], mai una cifra plausibile.
5. NON TI ALLARGHI: se trovi altro da fare, non lo fai — lo elenchi in fondo al rapporto.
7. NON DELEGHI il tuo incarico ad altri agenti.
8. FATTO = un comando che lo dimostra, non una tua dichiarazione.

PERIMETRO
  NON SCRIVI NULLA. Sei in SOLA LETTURA su tutto il repo. Nessun file, nessuna cartella.

CONTESTO MINIMO — gia' distillato
  - Il 2026-08-31 un `": "` non quotato dentro il campo `description` del frontmatter ha fatto
    sparire in silenzio 4 agenti (`opus-director`, `outreach-cro-audit`, `outreach-insight`,
    `outreach-research`): l'orchestratore chiamava agenti inesistenti (CP-20260901-005).
  - Il frontmatter va da riga 1 a riga <n>, fra due righe `---`.

L'INCARICO
  In una frase: dimmi QUANTI e QUALI agenti hanno oggi un frontmatter che li farebbe sparire.
  Guarda in due posti, non uno solo: `.claude/agents/*.md` (progetto) e
  `C:\Users\Utente\.claude\agents\*.md` (globale).
  Difetto da cercare: campo `description` che contiene `": "` senza essere racchiuso fra
  virgolette, oppure `description` spezzata su piu' righe senza blocco YAML valido.

USCITA ATTESA
  Nessun file. La risposta sta nel rapporto in chat, e non supera 15 righe:
  1) il numero totale di agenti controllati (progetto + globale, separati)
  2) l'elenco dei file difettosi con path assoluto e la riga incriminata copiata
  3) «nessun difetto trovato» se e' cosi' — e in quel caso lo dici, non cerchi altro.

IL GATE
  Prima di rispondere esegui questo e incolla l'uscita nel rapporto:
  grep -rLn "^description: \"" .claude/agents/*.md | wc -l
  Se il numero non e' 0, l'elenco che mi dai deve avere almeno quel numero di voci.

DIVIETI
  Non correggere nulla: tu conti e riferisci, non ripari.
  Non inventare: se un file non lo apri, non lo citi. Solo italiano.
```

**Cosa e' stato tolto rispetto al modulo pieno, e perche':** file d'uscita, regola anti-caduta,
ripresa e idempotenza. Uno scagnozzo **non scrive**: non ha niente da perdere in una caduta, e
ogni riga in piu' e' costo puro su un lavoro che dura secondi. Restano la lingua, il divieto di
inventare, il divieto di allargarsi, il gate.

---

#### B) SENTINELLA — `sonnet` · una missione sola, anche lunga · esegue, non decide

```text
Sei una SENTINELLA di Digital Empire, al servizio di EMPERATOR. Ti chiami sentinella-puntatori.
Parti a freddo: non sai nulla della conversazione in corso. Tutto cio' che ti serve e' qui sotto.

DIRECTORY DI LAVORO: C:\Users\Utente\Desktop\qui tutto\Digital Empire
FILE DI USCITA (uno solo, tuo): C:\Users\Utente\Desktop\qui tutto\Digital Empire\PIANO-MAESTRO\31-PIANO-IMPERO-VIVO\dati\rapporto-puntatori.md

LEGGE COMUNE DELL'IMPERO — vale sempre
<le 9 righe intere, senza tagli>

TERRENO CODICE
- ADR-003: un sistema attivo non si riscrive, si avvolge.
- La console e' cp1252: ogni script che stampa emoji va lanciato con PYTHONIOENCODING=utf-8.
- `sed` col delimitatore `|` rompe le righe di tabella markdown: per quelle usa Python.

PERIMETRO
  PUOI SCRIVERE SOLO QUI:
    - il tuo file d'uscita (sopra)
    - i file .md che contengono il puntatore sbagliato, e SOLO la riga del puntatore
  NON DEVI TOCCARE MAI:
    - company/Memory/       (ci scrive solo Emperator)
    - second-brain-vault/wiki/log.md
    - PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/dati/censimento-*.md (altre forze ci stanno lavorando adesso)
    - qualunque file .py, .json, .yaml — questa missione tocca solo testo
  Ovunque altrove: SOLA LETTURA.

CONTESTO MINIMO — gia' distillato, non andare a cercarne altro
  - Il file `scene_detector.py` NON sta in `scripts/`. Sta in
    "SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/scene_detector.py" (verificato
    sul disco il 2026-09-06).
  - Alcuni documenti lo citano come `scripts/scene_detector.py`: e' un puntatore morto.
  - La legge violata e' la REGOLA PUNTATORI di CLAUDE.md: «un puntatore vecchio e' peggio di
    nessun puntatore, perche' manda a sbattere invece di far cercare».

L'INCARICO
  In una frase: correggi ogni citazione di `scripts/scene_detector.py` col path reale, e
  lascia il rapporto di cio' che hai toccato.
  1. Trova tutte le occorrenze nei file .md del repo.
  2. Per ognuna: sostituisci SOLO la stringa del path, senza toccare il resto della riga.
  3. Scrivi nel file d'uscita: path del file, numero di riga, riga prima, riga dopo.
  Ordine: comincia dai file di `company/` e `PIANO-MAESTRO/`, sono quelli che si leggono davvero.

USCITA ATTESA
  Dove: il file d'uscita sopra.
  Formato: markdown, una tabella con colonne | file | riga | prima | dopo |.
  Rapporto in chat, 4 righe: quante occorrenze trovate · quante corrette · quali file NON hai
  potuto toccare e perche' · l'uscita del gate.

REGOLA ANTI-CADUTA — obbligatoria
  Crea il file d'uscita con titolo e tabella vuota ENTRO IL PRIMO MINUTO.
  Aggiungi una riga alla tabella dopo OGNI singola correzione, non alla fine.

RIPRESA / IDEMPOTENZA
  Se il file d'uscita esiste gia': leggilo, salta le correzioni gia' registrate, riparti dalla
  prima non fatta. Rieseguirti su un file gia' corretto non deve cambiare nulla.

IL GATE — hai finito bene SOLO se questo comando da' 0
  grep -rn "scripts/scene_detector.py" --include=*.md . | wc -l
  Atteso: 0. Eseguilo tu e incolla l'uscita nel rapporto.

SE CADI A META'
  Lascia il file com'e'. Nel rapporto dichiara quali correzioni sono SU DISCO e quali no.

DIVIETI
  NON DECIDI. Se trovi un altro puntatore morto diverso da questo, NON lo correggi:
  lo elenchi in fondo al rapporto e ti fermi.
  Non modificare nessun file fuori dal perimetro. Solo italiano. Non inventare.
```

**Cosa distingue questa variante:** ci sono tutte e quattro le parti che `emperator.md` riga 1369
dichiara obbligatorie — missione in una frase, perimetro esatto, FATTO verificabile con un
comando, divieto di allargarsi — piu' il divieto di decidere, che e' il confine del grado.

---

#### C) DOOM BOT — `opus` · fa il mestiere di Emperator su un'area disgiunta · progetta e costruisce

```text
Sei un DOOM BOT di Digital Empire, al servizio di EMPERATOR. Ti chiami doombot-addestramento.
Parti a freddo: non sai nulla della conversazione in corso. Tutto cio' che ti serve e' qui sotto.

DIRECTORY DI LAVORO: C:\Users\Utente\Desktop\qui tutto\Digital Empire
FILE DI USCITA (uno solo, tuo): C:\Users\Utente\Desktop\qui tutto\Digital Empire\PIANO-MAESTRO\31-PIANO-IMPERO-VIVO\dati\censimento-03c-addestramento.md

LEGGE COMUNE DELL'IMPERO — vale sempre
<le 9 righe intere, senza tagli>

PERIMETRO — AREE DISGIUNTE, questa e' la regola che impedisce il massacro
  PUOI SCRIVERE SOLO QUI: il tuo file d'uscita. Nient'altro, in tutto il repo.
  NON DEVI TOCCARE MAI: gli altri file in .../31-PIANO-IMPERO-VIVO/dati/ — sono di altri
  DOOM BOT che stanno lavorando ADESSO, in parallelo con te. Aprirli in scrittura significa
  distruggere il loro lavoro (caso reale: due giri di swarm sullo stesso file, git bloccato).
  Ovunque altrove: SOLA LETTURA.

CONTESTO MINIMO — gia' distillato, non andare a cercarne altro
  - Ordine di Max a Emperator: «devi organizzare le tue sentinelle, i tuoi scagnozzi, i tuoi
    doom bot in modo perfetto, addestrarli, dargli dei regolamenti, una direzione, un piano».
  - Due pezzi sono GIA' FATTI da altri e NON vanno rifatti — leggili, sono la tua base:
      dati/censimento-03b-regolamento-forze.md   (la gerarchia in vigore, ADR-015)
      dati/censimento-03b2-cadute.md             (33 cadute reali, 29 regole, 12 [MECCANICA])
  - A te tocca l'ADDESTRAMENTO e il MODULO D'INGAGGIO: nient'altro.
  Non aprire STATO-EMPIRE.md ne' wiki/index.md per intero (~196.000 e ~72.000 token).

L'INCARICO
  In una frase: progetta cosa ogni forza deve sapere prima di muovere un dito, e con quale
  forma esatta la si schiera.
  SEZIONE 1 — le fonti di conoscenza che esistono gia': cosa contengono e QUANTO SONO GRANDI
    (righe e caratteri misurati, non stimati). Elenca TUTTI gli ADR con numero e titolo, una
    riga ciascuno, e segna quali sono vincolanti per chiunque lavori.
  SEZIONE 2 — l'addestramento: il minimo comune (poche righe: si paga a ogni ingaggio ×
    ogni forza) · l'addestramento di terreno (codice, copy, soldi, credenziali, video) ·
    la forma concreta, col costo in righe/token di ciascuna e la motivazione della scelta.
  SEZIONE 3 — il modulo d'ingaggio: modello riempibile coi segnaposto, piu' tre varianti
    gia' compilate (scagnozzo, sentinella, doom bot).
  SINTESI — il minimo comune in forma definitiva · il modulo in forma definitiva · quanto costa.
  Ordine: comincia dalla misura delle fonti, e' la parte cara e regge tutto il resto.

USCITA ATTESA
  Dove: il file d'uscita sopra.
  Formato: markdown con frontmatter (Type/Status/Tags/Created/Autore), e le sezioni nell'ordine
  di sopra. Cio' che progetti e non esiste ancora va marcato PROGETTO:.
  Rapporto in chat: quante fonti d'addestramento · quanto e' lungo il minimo comune · la
  differenza principale fra il modulo per scagnozzo e quello per doom bot.

REGOLA ANTI-CADUTA — obbligatoria
  Scrivi ogni sezione sul file appena e' finita, poi passa alla successiva. Mai accumulare.
  (Motivo: il servizio dei subagenti cade. Una sentinella e' morta con 175 scene su 352 in
  memoria e non sul disco; l'antidoto della scrittura incrementale ha gia' salvato due volte.)

RIPRESA / IDEMPOTENZA
  Se il file esiste gia', leggilo e riparti dalla prima sezione mancante.

IL GATE — hai finito bene SOLO se tutto questo e' vero
  1) grep -c "^## SEZIONE" <file d'uscita>     -> atteso: 3
  2) grep -c "^| .* | 0[0-9][0-9] |" <file>    -> almeno 25 (gli ADR censiti uno per riga)
  3) il minimo comune sta sotto le 12 righe: wc -l sul blocco -> <= 12
  Esegui i tre comandi e incolla le uscite nel rapporto.

SE CADI A META'
  Lascia il file com'e'. Dichiara quali sezioni sono SU DISCO.

DIVIETI
  NON MODIFICARE NESSUN ALTRO FILE. Sola lettura tranne il tuo file d'uscita.
  Non inventare nulla che non sia ancorato a un file aperto e citato — tranne dove ti si
  chiede di PROGETTARE, e li' scrivi PROGETTO:.
  Non delegare l'intero incarico a un altro agente. Solo italiano.
```

---

### 3.3 COSA CAMBIA FRA UN GRADO E L'ALTRO

| Parte del modulo | SCAGNOZZO | SENTINELLA | DOOM BOT |
|---|---|---|---|
| Modello | `haiku` | `sonnet` | `opus` |
| File d'uscita | **nessuno** — risponde in chat | uno, suo | uno, suo, **esclusivo** |
| Perimetro di scrittura | **vuoto: sola lettura ovunque** | path esatti, elencati | **il solo file d'uscita**, e aree disgiunte dagli altri doom bot |
| Contesto minimo | 2-3 righe | 3-6 righe + fonti con range | 5-8 righe + i documenti-base gia' fatti da non rifare |
| Blocco di terreno | quasi mai | quello del suo ambito | quello del suo ambito |
| Regola anti-caduta | **non serve** (non scrive) | obbligatoria | obbligatoria, **in grassetto, in cima** |
| Ripresa/idempotenza | non serve | obbligatoria | obbligatoria |
| Gate | un comando che verifica la risposta | un comando che verifica la missione | 2-3 comandi che verificano forma e completezza |
| Puo' decidere? | **no** | **no** — se serve una decisione si ferma e la rimanda | **si', dentro il perimetro**: progetta e costruisce |
| Puo' allargarsi? | no, elenca e basta | no, elenca e basta | no: elenca in fondo |
| Lunghezza tipica del prompt | ~35 righe | ~60 righe | ~75 righe |

**La differenza che conta, in una frase:** lo **scagnozzo** e' un occhio — non scrive niente,
non decide niente, e il suo modulo perde tutto cio' che serve a sopravvivere a una caduta perche'
non ha nulla da perdere; il **doom bot** e' una mano che progetta — ha un file suo ed esclusivo,
la scrittura incrementale in cima al prompt, l'idempotenza dichiarata come procedura di ripresa
e un gate a piu' comandi, perche' e' l'unico grado la cui morte a meta' distrugge lavoro di ore.

---

# SINTESI FINALE

## A. IL MINIMO COMUNE — forma definitiva, pronta da incollare

**10 righe · 976 caratteri · ~260 token.** Si incolla in ogni ingaggio, di ogni grado, senza
tagli. Non si aggiunge una riga senza una caduta documentata che quella riga avrebbe evitato.

```
LEGGE COMUNE DELL'IMPERO — vale per ogni forza, sempre
1. ITALIANO in ogni riga, rapporto compreso.
2. NON INVENTI: nessuna affermazione senza un file che hai aperto, citato col path.
   Numero che non hai = [DM], mai una cifra plausibile.
3. SCRIVI SUBITO: crea il file d'uscita entro il primo minuto e risalvalo a ogni
   sezione finita. Chi cade deve lasciare il lavoro fatto.
4. PERIMETRO: scrivi SOLO nei path del tuo incarico. Tutto il resto e' sola lettura.
   Mai company/Memory/, mai wiki/log.md, mai i file di altre forze.
5. NON TI ALLARGHI: se trovi altro da fare, non lo fai — lo elenchi in fondo al rapporto.
6. IDEMPOTENTE: rieseguirti due volte non deve rompere ne' duplicare nulla.
7. NON DELEGHI il tuo incarico ad altri agenti.
8. FATTO = un comando che lo dimostra, non una tua dichiarazione. Nel rapporto scrivi
   cosa hai scritto davvero e cosa no.
9. SE CADI a meta': lascia il file com'e'. Chi riprende rilegge il file e riparte dalla
   prima sezione mancante.
```

Per lo SCAGNOZZO si tolgono le righe 3, 6 e 9 (non scrive: non ha nulla da perdere in una
caduta) — restano 7 righe, ~180 token.

---

## B. IL MODULO D'INGAGGIO — forma definitiva

Undici blocchi, sempre nello stesso ordine. Il modello riempibile per esteso e' in §3.1, le tre
varianti compilate in §3.2.

| # | Blocco | Obbligatorio per | Perche' esiste |
|---|---|---|---|
| 1 | **Identita' e grado** + «parti a freddo» | tutti | emperator.md §6.7 |
| 2 | **Directory e file d'uscita** (path assoluti) | sentinella, doom bot | §6.7: percorsi assoluti |
| 3 | **Legge comune** (§A) | tutti | le 29 regole di 03b2 |
| 4 | **Terreno** (uno solo, quello dell'ambito) | chi tocca l'ambito | §2.2 |
| 5 | **Perimetro**: puoi scrivere / non toccare mai / sola lettura | tutti | invariante ADR-015, casi 22 e 33 |
| 6 | **Contesto minimo gia' distillato** + le fonti col range di righe | tutti | caso 1 (read-heavy) |
| 7 | **L'incarico**: missione in una frase, passi numerati, «comincia dal piu' costoso» | tutti | §6-bis.2, caso 20 |
| 8 | **Uscita attesa**: dove, formato, forma del rapporto | tutti | 03b2 regola 12 |
| 9 | **Regola anti-caduta** (crea subito, salva a ogni sezione) | sentinella, doom bot | regola 8 [MECCANICA] |
| 10 | **Ripresa / idempotenza** | sentinella, doom bot | ADR-006 passo 2, regola 14 |
| 11 | **Il gate** (comando + esito atteso, eseguito dalla forza) | tutti | *«un Doom Bot che dice "fatto" non e' una prova»* |
| 12 | **Se cadi a meta'** + **Divieti** (lingua, non inventare, non allargarsi, non delegare) | tutti | regole 19 e 20, emperator.md riga 118 |

**Misure reali dei tre moduli compilati** (contate sul testo di §3.2):

| Grado | Righe | Caratteri | ≈ token |
|---|---:|---:|---:|
| SCAGNOZZO | 43 | 2.263 | ~600 |
| SENTINELLA | ~75 | 4.293 | ~1.130 |
| DOOM BOT | ~77 | 5.042 | ~1.330 |

---

## C. QUANTO COSTA — e perche' vale la pena

### C1. Il costo dell'addestramento vero e proprio

Nel modulo, **addestramento** e' solo cio' che si paga *in piu'* rispetto all'ordine che
andrebbe scritto comunque (perimetro, incarico, uscita, gate esistono anche senza dottrina).
Quel di piu' e' la legge comune e il blocco di terreno:

| Forza | Legge comune | Terreno | **Addestramento totale** |
|---|---:|---:|---:|
| Scagnozzo (7 righe) | ~180 tok | — | **~180 token** |
| Sentinella | ~260 tok | ~290 tok | **~550 token** |
| Doom bot | ~260 tok | ~290 tok | **~550 token** |
| Doom bot senza terreno | ~260 tok | — | **~260 token** |

**Uno swarm come quello di questa notte — 14 forze — costa da 3.640 a 7.700 token di
addestramento in tutto.** E' lo 0,3% di quanto costerebbe far leggere `STATO-EMPIRE.md` alle
stesse 14 forze (~2.749.000 token), ed e' meno del 4% di una sola lettura di quel file.

### C2. Perche' vale la pena — i numeri stanno gia' nei registri dell'Impero

1. **La struttura inline vale 16 volte il suo prezzo, misurato.** Caso 1: prompt read-heavy ->
   *«1 file / 21 tool_use»*; con struttura inline e scrittura precoce -> *«16 file / 20
   tool_use»*. Stesso budget, sedici volte il prodotto.
2. **Una caduta costa piu' dell'addestramento di tutto lo swarm.** Caso 1: 61 file su 62 non
   prodotti, batch intero da rilanciare. Caso 20: 4 reparti su 10 incompleti, uno mai iniziato.
   Caso 9: 175 scene su 352 perse. Nessuno di questi ripristini e' costato meno di 7.700 token.
3. **Le morti sono ricorrenti, non eccezionali.** 03b2 conta **9 episodi** di forze morte per
   limite di budget e **5** di lavoro accumulato in memoria e perso. Un'abitudine della
   macchina si paga a ogni ripetizione: 260 token si pagano una volta per ingaggio.
4. **Cinque riparazioni sono state fatte a mano.** «completato a mano» compare nei casi 8, 14,
   18, 19, 20: e' tempo di Emperator o di Max, la risorsa piu' cara dell'Impero, spesa per
   rifare cio' che una riga di prompt avrebbe salvato.
5. **L'antidoto e' gia' provato due volte, non e' una teoria.** `EMP-URQ7.md`: *«far creare il
   file d'uscita SUBITO con le sezioni vuote e farlo risalvare a ogni sezione. Chi muore lascia
   comunque il lavoro fatto»*; `CP-20260905-019`: *«333 e 113 righe salvate e completate a mano»*.
   Questa notte i censimenti 03b e 03b2 sono interi sul disco **per la stessa ragione**.

### C3. Il costo che questo schema evita di pagare

Tre spese che oggi l'Impero sostiene e che spariscono:

- **Il RECALL moltiplicato.** Imporre memory-first a ogni forza costerebbe ~2,7 milioni di token
  per notte. Con questo schema il RECALL lo fa Emperator una volta, e travasa 5 righe nel blocco
  `CONTESTO MINIMO`.
- **Il riaddestramento di cio' che esiste gia'.** 164 agenti e 297 skill sono gia' costruiti:
  il terreno rimanda a loro (`cro-copy-architect`, `tesoreria-conductor`, `ytf-*`,
  `credential-keeper`) invece di riscrivere il mestiere dentro un prompt usa-e-getta.
- **La biblioteca inerte.** `conoscenza-empire` costa **zero** finche' nessuno la chiama: basta
  la riga del blocco `CONTESTO MINIMO` che dice alla forza che puo' chiamarla, e il debito
  dichiarato in `CP-20260902-002` (*«non ha ancora alimentato nessuno»*) si chiude senza
  spendere un token su chi non ne ha bisogno.

---

## Nota di metodo

Scritto **una sezione alla volta, con append immediato dopo ognuna**, per la ragione documentata
nel caso 8 e nel caso 12 di 03b2: quando il servizio dei subagenti cade — e cade — sopravvive
solo cio' che e' gia' su disco.

## Cosa resta aperto (elencato, non fatto — Legge comune §5)

1. **Il minimo comune non e' ancora un file.** Va depositato dove Emperator lo copia senza
   pensarci: proposta `company/Mandato/LEGGE-COMUNE-FORZE.md`, 10 righe, nient'altro dentro.
2. **Il modulo non e' ancora un template.** Stessa cosa: un file solo, riempibile.
3. **`empire-context/SKILL.md` e' fermo all'11 giugno** — cita 10 dossier (sono 39) e
   ADR-001..004 (gli attivi sono 24).
4. **Due ADR-016 sullo stesso numero** (`dottrina-integrale-all-apertura` e `ultimo-metro`),
   collisione non ancora sanata da nessun ADR — a differenza dei due ADR-012, coperti da ADR-018.
5. **Puntatore morto in 03b2 caso 17**: `scripts/scene_detector.py` non esiste; il file vive in
   `SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/scene_detector.py`.
6. **La chiave Brevo e' pubblica da mesi** (`EMP-URQ7.md` trappola 6): va cambiata sul servizio.

## Connessioni

- `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/dati/censimento-03b-regolamento-forze.md` — la gerarchia
- `PIANO-MAESTRO/31-PIANO-IMPERO-VIVO/dati/censimento-03b2-cadute.md` — le 33 cadute, le 29 regole
- `company/Memory/decisions/ADR-015-gerarchia-forze-emperator.md` — la legge dei quattro gradi
- `PIANO-MAESTRO/10-METODO-CICLO-FASE.md` — il ciclo a 9 passi (ADR-006)
- `.claude/agents/conoscenza-empire.md` — la biblioteca che il modulo rende finalmente chiamabile
