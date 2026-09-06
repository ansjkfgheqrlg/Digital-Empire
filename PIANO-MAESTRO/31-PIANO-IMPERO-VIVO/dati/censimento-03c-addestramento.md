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
