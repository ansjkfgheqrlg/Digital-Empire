# CENSIMENTO 02d — LE QUATTRO SINTESI DEI COLLEGAMENTI

> **Cosa dicono i 328 passaggi di consegne, messi tutti insieme.**
> Rilevazione: 2026-09-06 · Autore: DOOM BOT 02d · Committente: EMPERATOR
> Materia prima: `dati/censimento-02b-mappa-collegamenti.md` (619 righe, tabella completa, 12 fonti spogliate).
> Riscontro sull'infrastruttura: `dati/censimento-02-collegamenti.md` (363 righe).
> Ogni numero di questo file e' stato ricontato riga per riga sulla tabella di 02b, non stimato.
> Dove ho riaperto il disco e ho trovato altro, l'ho scritto: vedi **RETTIFICHE** in fondo alla Sintesi A.

---

## SINTESI A — I NUMERI

### A.1 Quanti sono

| Misura | Valore | Come e' stata presa |
|---|---:|---|
| **Passaggi di consegne censiti** | **328** | righe numerate della tabella di 02b, da 1 a 328: nessun buco, nessun duplicato (verificato) |
| di cui **INTRA** (dentro un ecosistema) | **57** | colonna di stato marcata `INTRA` e nient'altro |
| di cui **INTER** (fra ecosistemi diversi) | **262** | colonna di stato marcata `INTER` e nient'altro |
| di cui **misti** (una riga che copre entrambi) | **9** | righe #86, #119, #121, #137, #154, #187, #193, #282, #318 |
| **Totale righe con una componente INTER** | **271** (82,6%) | 262 + 9 |
| **Totale righe con una componente INTRA** | **66** (20,1%) | 57 + 9 |
| di cui marcati **VAGO** | **55** (16,8%) | 43 INTER, 10 INTRA, 2 misti (#86, #154) |

**Cosa dice il 16,8%.** Un passaggio su sei e' dichiarato senza carico o senza criterio: "alimenta",
"si intreccia con", "in coordinamento con", "DIPENDE DA". Il dossier dei LANCI ha gia' scritto la
frase che li giudica tutti: *"Un passaggio senza criterio di accettazione e' una speranza: chi riceve
scopre che manca qualcosa quando e' gia' al lavoro"*
(`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/07-REPARTI-E-GERARCHIA.md:407-409`).

### A.2 Quanti hanno un contratto scritto

| Stato del contratto | Righe | % |
|---|---:|---:|
| **SI — contratto su disco** | **21** | 6,4% |
| **NO — nessun contratto** | **299** | 91,2% |
| stato intermedio (motore c'e', contratto no) | 8 | 2,4% |

I 21 con contratto si dividono in due famiglie che non si somigliano per niente:

**Famiglia 1 — i 4 HC dell'AGENCY** (righe #17, #19, #21, #23). Sono file JSON veri:
`company/01-agency/A1-RICERCA/handoffs/HC-A1-A2-leads.json`,
`A2-ACQUISIZIONE/handoffs/HC-A2-A3-call.json`,
`A3-PREVENTIVI/handoffs/HC-A3-A4-contratto.json`,
`A4-DELIVERY/handoffs/HC-A4-A6-testimonianza.json`. Schema `HC-v1`, creati il 2026-06-11,
tutti e quattro con `"status": "template"`. Sono **tutti e quattro INTRA-AGENCY**.

**Famiglia 2 — i 17 passaggi dei LANCI** (righe #299-#315). Non sono file di contratto: sono **dati
dentro un registro leggibile da un programma**, `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml:1741`
in poi, e sono **verificati da una macchina**: `dati/valida_registro.py:479-501` esegue INV-20, che
boccia il registro se un passaggio non cita due reparti esistenti, un artefatto esistente, un criterio
di accettazione **e cosa succede se e' rifiutato**. Verificato aprendo i due file.

**Il quinto contratto del repo** — `company/Backbone/Bus/contracts/HC-template.json`, l'unico
INTER-ecosistema (01-AGENCY → 04-MARKETING) — non compare come riga numerata in 02b perche' e' un
modello, non un passaggio dichiarato da un dossier. Conteggio del gemello confermato:
`find company empire -iname "*handoff*" -o -iname "HC-*"` → **5 file in tutto il repo**.

Gli 8 a stato intermedio: #279 e #280 (il Bus a due livelli), #287 (la skill `empire-handoff`),
#290-#293 (i 4 contratti `HC-ME-*` della MEMORY: il codice si usa, il file di contratto non c'e'),
#321 (`registry.yaml` del Bus).

### A.3 Quanti sono stati percorsi almeno una volta

| Stato | Righe | Quali |
|---|---:|---|
| **Percorsi davvero (a vuoto)** | **4** | #17, #19, #21, #23 |
| Semi-percorsi (il codice gira, il passaggio no) | 1 | #18 — l'outreach gira, senza contratto |
| Parzialmente percorsi (uomo→file, non ecosistema→ecosistema) | 5 | #290, #291, #292, #293, #295 |
| **MAI percorsi** | **318** | tutti gli altri |
| **INTER percorsi** | **0** su 271 | **nessun passaggio fra due ecosistemi e' mai avvenuto** |

**L'unico ciclo noto.** `company/Memory/state/agency/trace.jsonl` (22 righe) registra
`CY-20260611-001`, **2026-06-11 dalle 18:13:12 alle 18:14:10 — 58 secondi**, con 4 `handoff_sent`,
4 `handoff_received` e 3 `gate_passed`: tutti e 4 gli HC attraversati.
Ma `state.json` porta `"dry_run": true`, `"lead_id": "DRYRUN-001"`,
`"lead_nome_azienda": "DryRun-Client-01 (TEST - non reale)"`. Nessun invio, nessun euro, nessun file
di handoff prodotto. Da allora `updated_at` e' fermo: **87 giorni**, `"active": []`, `"failed": []`.

I 5 parziali della MEMORY sono l'unica cosa viva della mappa, ma non sono passaggi nel senso di questo
censimento: sono un uomo che scrive un file. I checkpoint esistono (**303** file in
`company/Memory/checkpoints/`), gli ADR esistono (**25** in `company/Memory/decisions/`) — e il campo
`costi` di `HC-ME-POST` (`PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:45`) **non e' compilato in nessuno dei 303**.

### A.4 I tre numeri che riassumono tutto

- **6,4%** dei passaggi ha un contratto scritto.
- **1,2%** e' stato percorso una volta, in un test, con un cliente finto, 87 giorni fa.
- **0%** degli INTER — cioe' di tutto cio' che tiene insieme l'azienda — e' mai avvenuto.

### A.5 RETTIFICHE al gemello 02b

Ho riaperto il disco su tre affermazioni di 02b. Due vanno corrette.

**1. `orders/` ESISTE.** 02b scrive: *"`find . -type d -name "orders"` → 0 risultati. Il punto
d'ingresso unico non esiste"* (nota alla FONTE 3a, ripetuta nelle righe #92, #93, #113).
Il fatto misurato oggi: `company/Ecosistemi/03-CONTENT-FACTORY/Reparti/CF-R5-Visual-Design-Caroselli/orders/`
contiene **due ordini reali**:
- `CF-2026-PREVENTA-001` (2026-08-06) — `state.json` + `trace.jsonl` di 19 eventi, 8 slide prodotte,
  gate FORMATO e BRAND `PASS` ma dichiaratamente **a mano** (*"CF-R5-QA non ancora costruito come
  script reale"*), `handoff-cf-r6: "non_eseguito"`.
- `CF-2026-PREVENTA-002` (2026-08-27) — primo ordine sul Ramo C, `caroselli.py` + `carousel-factory`,
  gate **automatico e' codice** (*"Exit 1 se fallisce"*), 6 slide consegnate in
  `SKILL & Agenti/Workflow agency creative/Arsenale Caroselli/Preventa/2026-08-27_.../` (verificato: 14 file).

**La correzione non cambia il conteggio dei passaggi percorsi.** In entrambi gli ordini il committente
e' Max/claude a mano, non un ecosistema, e in entrambi `handoff-cf-r6` risulta **non eseguito**.
L'ordine e' partito e ha prodotto: il *passaggio di consegne* no. Ma cambia il giudizio su CF: **il
motore c'e' davvero**, ed e' il piu' vicino all'accensione di tutto l'Impero (vedi Sintesi C, punto 5).

**2. Il brand kit ESISTE, con un altro nome.** 02b: *"`find . -name "brand-kit.json"` → 0 risultati"*
(#93, #146, #320). Vero alla lettera. Ma esistono **5 configurazioni di brand** reali in
`Workfolw crea caroselli à/carousel-factory/brands/{preventa, brand-agency, brand-education,
brand-personal, mentalita-brutale}/config.json`, e l'ordine CF-2026-PREVENTA-002 ne dichiara una nel
campo `brand_kit_path`. Non sono nello schema di CF (`03-ECOSISTEMA-CONTENT-FACTORY.md:66-88`) e il
primo ordine ha `brand_kit_path: null` — ma il pezzo non e' da inventare, e' da normalizzare.

**3. Confermato senza rettifica: il Bus non esiste.** Righe #279 e #280 di 02b dicono
*"script esiste, traffico zero"*. **Gli script non esistono.** Verifica mia:
`find . -name "bus.sh" -o -name "gbus.sh" -o -name "validate-handoff.sh" -o -name "costs.sh"` →
**0 risultati**. `company/Backbone/Bus/` contiene 3 file: `README.md`, `contracts/HC-template.json`,
`handoffs/.gitkeep` (0 byte). Il README lo scrive da solo alla riga 107:
**"## Stato: DA COSTRUIRE (F2, task 2.3)"**. `company/metrics/` **non esiste**.
La nota di chiusura di 02b (FONTI 10-12) diceva gia' la cosa giusta; le due righe di tabella no.

---

## SINTESI B — LA MATRICE

### B.1 Come e' stata costruita

Ogni riga della tabella di 02b ha un mittente e un destinatario scritti in prosa
(`A3-PREVENTIVI`, `mb-yt-asset-receiver`, `06c-INTELLIGENCE`, `committente qualsiasi`).
Li ho normalizzati sui 13 ecosistemi numerati dell'Impero. Il risultato si divide in tre:

| Categoria | Righe |
|---|---:|
| **Archi fra due ecosistemi nominati e diversi** (la matrice) | **186** |
| Archi dentro lo stesso ecosistema | 61 |
| Archi con almeno un capo non-ecosistema (`QUALSIASI`, `TUTTI`, `committente`, Board/LX, Backbone, Max) | 81 |
| | **328** |

Gli 81 fuori matrice non sono rumore: contengono i 3 broadcast dell'Impero
(#217 alert OPERATIONS→tutti, #246 deprecazione FORGE→tutti, #275 alert push), i 4 "9→1"
(#204 FORGE, #210/#257 INTELLIGENCE, #216/#266 OPERATIONS) e le 4 righe della matrice
Core×Business (#220-#223), che da sole valgono 5 celle ciascuna.

### B.2 La matrice — chi consegna a chi e quante volte

Righe = **DA**. Colonne = **A**. Solo archi INTER fra ecosistemi nominati.

| DA \ A | 01 AG | 02 IB | 03 CF | 04 MK | 05 MB | 06 PL | 07 FG | 08 IN | 09 OP | 10 ME | 11 AP | 14 TS | 29 LA | **OUT** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **01 AGENCY** | — | 1 | **5** | 2 | 1 | **5** | 2 | 3 | 2 | 1 | · | · | · | **22** |
| **02 INFO-BUSINESS** | 4 | — | **9** | **7** | 2 | 1 | · | 2 | 3 | 1 | · | · | · | **29** |
| **03 CONTENT-FACTORY** | 2 | 2 | — | **8** | 4 | 2 | · | 3 | 1 | · | · | · | · | **22** |
| **04 MARKETING** | 3 | 3 | **5** | — | · | 4 | 2 | 1 | 1 | 1 | · | · | · | **20** |
| **05 MULTI-BUSINESS** | 1 | 2 | **9** | **6** | — | 4 | 4 | **5** | 3 | · | · | · | · | **34** |
| **06 PLATFORM** | 1 | 2 | 1 | 1 | · | — | 1 | 2 | 3 | · | · | · | · | **11** |
| **07 FORGE** | 1 | 2 | 1 | · | · | 3 | — | 4 | 4 | 1 | · | · | · | **16** |
| **08 INTELLIGENCE** | 4 | 2 | 2 | 3 | · | 2 | 4 | — | 1 | 2 | · | · | · | **20** |
| **09 OPERATIONS** | 2 | 2 | 1 | 1 | · | 1 | · | 3 | — | · | · | · | · | **10** |
| **10 MEMORY** | · | · | · | · | · | · | · | 1 | · | — | · | · | · | **1** |
| **11 APEX-7** | · | · | · | · | · | · | · | · | · | · | — | · | · | **0** |
| **14 TESORERIA** | · | · | · | · | · | · | · | · | · | · | · | — | · | **0** |
| **29 LANCI** | · | · | · | · | · | · | · | · | · | · | · | **1** | — | **1** |
| **IN** | **18** | **16** | **33** | **28** | **7** | **22** | **13** | **24** | **18** | **6** | **0** | **1** | **0** | **186** |

Passaggi **dentro** un ecosistema (non in matrice): 01-AGENCY **21** · 29-LANCI **15** ·
04-MARKETING **8** · 02-INFO-BUSINESS **5** · 05-MULTI-BUSINESS **4** · 03-CONTENT-FACTORY **3** ·
08-INTELLIGENCE **2** · 06-PLATFORM **1** · 07-FORGE **1** · 11-APEX-7 **1** ·
**09-OPERATIONS 0 · 10-MEMORY 0 · 14-TESORERIA 0**.

Coppie ordinate distinte: **70**. Di queste, **28 sono bidirezionali** — cioe' 56 archi su 186 hanno
un ritorno progettato. Le altre 14 coppie sono a senso unico.

Le rotte piu' battute sulla carta:
`02-IB → 03-CF` **9** · `05-MB → 03-CF` **9** · `03-CF → 04-MKT` **8** · `02-IB → 04-MKT` **7** ·
`05-MB → 04-MKT` **6** · `01-AG → 03-CF` **5** · `01-AG → 06-PL` **5** · `04-MKT → 03-CF` **5** ·
`05-MB → 08-IN` **5**.

### B.3 GLI ECOSISTEMI ISOLATI — e conta piu' della matrice

**Isolato del tutto — non riceve da nessuno E non consegna a nessuno:**

- **11-APEX-7** — `IN = 0`, `OUT = 0`. Un solo passaggio in tutto il censimento (#322), ed e' interno.
  Non e' solo scollegato: parla un'altra lingua. Il suo Event Bus dichiara
  *"Nessun agente chiama un altro direttamente. Publisher NON SA chi riceve. Subscriber NON SA chi ha
  inviato → zero coupling"* (`company/Ecosistemi/11-APEX-7-CORE/BACKBONE.md:168-189`): e' il **decimo
  schema di comunicazione dell'Impero, e l'unico senza `from` e senza `to`**. Anche volendo collegarlo,
  non c'e' un campo dove scrivere il destinatario.

**Isolati a meta' — non ricevono da nessun ecosistema:**

- **29-LANCI** — `IN = 0`. E' l'ecosistema con i passaggi meglio scritti dell'Impero (15 INTRA con
  contratto e criterio di rifiuto, verificati da INV-20) e **nessuno gli manda niente**. L'unica cosa
  che entra e' #312, `ULTIMO METRO → LAN-STR`, e ULTIMO METRO non e' un ecosistema: e' una coda
  (`07-REPARTI-E-GERARCHIA.md:436`, `registro.yaml:1822`), l'elenco di 25 pezzi finiti mai pubblicati,
  il piu' vecchio da 135 giorni (ADR-016).
- **14-TESORERIA** — `IN = 1`, `OUT = 0`. Riceve da un solo mittente (#313, `LAN-REG → TESORERIA`) e
  non consegna a nessuno. E' l'organo che dovrebbe contare i soldi di tutti e non e' collegato a nessuno
  dei nove che li spendono. Su disco: `company/Ecosistemi/14-TESORERIA/` ha un `README.md` e due
  cartelle **vuote** (`agenti/`, `workflow/`); il motore vero sta altrove
  (`scripts/tesoreria.py`, funzionante) e i suoi due libri mastri,
  `company/Memory/tesoreria/entrate.jsonl` e `spese.jsonl`, sono **0 byte**.

**Quasi isolato:**

- **10-MEMORY** — `OUT = 1` (verso la wiki), `IN = 6`. E' il solo ecosistema con codice usato ogni
  giorno, e sulla mappa e' quasi solo un deposito: riceve e non rilancia.

**Non isolato ma sbilanciato fino a diventare fragile:**

- **05-MULTI-BUSINESS** — `OUT = 34` (il piu' alto dell'Impero), `IN = 7`, e riceve da **soli 3**
  mittenti. Ordina a 8 ecosistemi e non produce quasi niente in proprio: lo dichiara il suo stesso
  dossier (*"i passi 5-9 sono eseguiti da Content-Factory su ordine"*,
  `05-ECOSISTEMA-MULTIBUSINESS.md:186-188`). **Se CF non risponde, MB non esiste.**

**Ecosistemi senza vita interna:** 09-OPERATIONS, 10-MEMORY e 14-TESORERIA hanno **0 passaggi INTRA**.
Nessuno dei tre ha mai dichiarato come si passa il lavoro al proprio interno.

### B.4 I COLLI DI BOTTIGLIA — se restano fermi, si ferma l'azienda

Carico = archi INTER in entrata + in uscita. Fra parentesi i passaggi interni.

| # | Ecosistema | IN | OUT | Carico | (INTRA) | Perche' e' un collo |
|---:|---|---:|---:|---:|---:|---|
| 1 | **03-CONTENT-FACTORY** | **33** | 22 | **55** | (3) | Riceve piu' di chiunque altro nell'Impero. E' il fornitore di 02-IB (9), 05-MB (9), 01-AG (5), 04-MKT (5). Se CF e' fermo, MB non ha prodotto, IB non ha corsi, AG non ha asset cliente. |
| 2 | **04-MARKETING** | **28** | 20 | **48** | (8) | *"Il suo prodotto e' il copy degli altri 8 ecosistemi"* (`04-ECOSISTEMA-MARKETING.md:20`) e *"nessun ecosistema scrive copy di conversione in autonomia"* (`:68-70`). Ogni riga di copy che porta a un incasso dovrebbe attraversarlo. |
| 3 | **02-INFO-BUSINESS** | 16 | **29** | **45** | (5) | Il secondo committente dell'Impero. Ordina a 8 ecosistemi per fare un lancio. |
| 4 | **08-INTELLIGENCE** | **24** | 20 | **44** | (2) | Riceve dal **numero massimo di partner distinti (9)**. E' il passaggio piu' a monte: *"ogni ecosistema, prima di un task non banale, ottiene un context pack"*, con copertura dichiarata ≥95% (`06c-...-V2.md:56`, `:270`). |
| 5 | **05-MULTI-BUSINESS** | 7 | **34** | **41** | (4) | Il piu' dipendente: vedi B.3. |
| 6 | **01-AGENCY** | 18 | 22 | **40** | **(21)** | Contando i 21 INTRA e' il **piu' caricato in assoluto: 61 passaggi**. Ed e' il pilastro revenue dichiarato: *"tutto il resto di EMPIRE OS lo alimenta o lo amplifica"* (`01-ECOSISTEMA-AGENCY.md:16`). |
| 7 | **06-PLATFORM** | **22** | 11 | **33** | (1) | *"l'implementazione e il deploy vivono in PLATFORM"* (`06a-...-V2.md:91-93`). Nessun sito, nessuna landing, nessun checkout esiste senza di lui. |
| 8 | **07-FORGE** | 13 | 16 | **29** | (1) | *"nessun ecosistema crea agenti, skill o team in autonomia"* (`06b-...-V2.md:98-99`). E' il collo di bottiglia della **crescita**, non della produzione. |
| 9 | **09-OPERATIONS** | 18 | 10 | **28** | (0) | *"ogni run passa da qui e ogni run genera un evento di ritorno"* (`06d-...-V2.md:78-81`). E' il collo di bottiglia del **denaro misurato**. |

**La lettura che conta.** I quattro colli veri non sono i piu' grandi: sono i quattro **trasversali**
(06, 07, 08, 09), perche' il loro dossier dichiara che **nessuno puo' aggirarli**
(`06-ECOSISTEMI-CORE.md:11`: *"Nessun ecosistema business tocca direttamente codice, creazione di
agenti, memoria o runtime: lo chiede ai core via handoff contract"*). Sono 4 divieti assoluti su
5 ecosistemi che incassano — e nessuno dei 4 ha mai ricevuto un handoff.

Il risultato e' un'azienda a due velocita': **AGENCY, CF e MB hanno motori che girano** (outreach,
`caroselli.py`, YouTube factory) e li fanno girare **fuori** dai passaggi progettati; MARKETING,
PLATFORM, FORGE, OPERATIONS, TESORERIA e LANCI hanno i passaggi progettati e **niente che li percorra**.

---

## SINTESI C — I DIECI DA ACCENDERE PER PRIMI

Ordinati per importanza, non per facilita'. Criterio, in quest'ordine:
**(1)** sta su un percorso che porta a un incasso reale · **(2)** ne sblocca molti a valle ·
**(3)** ha gia' un motore vero da entrambe le parti, quindi accenderlo costa poco.
Per ognuno: **cosa esiste gia'** e **cosa manca esattamente**.

---

### 1 · La catena AGENCY — #17 → #19 → #21 → #23 (A1→A2→A3→A4→A6)
**La ragione:** e' l'unica strada dell'Impero gia' asfaltata da capo a fondo, e finisce in un
contratto firmato con pagamento verificato. E' gia' stata percorsa una volta: manca solo il carico vero.

- **Esiste gia':** i 4 contratti su disco (`company/01-agency/A{1,2,3,4}-*/handoffs/HC-*.json`,
  schema `HC-v1`, criteri di accettazione scritti, `failure_handling` con `on_reject` e `on_timeout`);
  `Outreach/Outreach Workflow/leads.db` reale; gli avvii `/avvia-email`, `/avvia-ig`, `/avvia-parallel`,
  `/avvia-outreach-preventa`; `Outreach/agents/outreach-message-team/rule_keeper_lint.py`
  (enforcement deterministico della Bibbia); `scripts/agency-trace.ps1`, che sa scrivere gli eventi;
  la traccia `CY-20260611-001` che dimostra che i 4 passaggi si attraversano.
- **Manca esattamente:** (a) i 4 JSON hanno `"status": "template"` — nessuno ha mai avuto un `_id`
  d'istanza, un `ts` o uno `status` mutabile; (b) `dry_run: true` va tolto e va passato un lead vero;
  (c) `scripts/agency-trace.ps1` va invocato **a mano, un evento alla volta**: nessuno script lo chiama
  (`grep -rn "agency-trace"` → nessun chiamante). Serve una riga di chiamata dentro il codice
  dell'outreach, non un sistema nuovo.

### 2 · #312 · ULTIMO METRO → LAN-STR — la coda gia' piena
**La ragione:** e' il passaggio piu' vicino a un incasso di tutta la mappa, e **non richiede di
produrre niente**: la fila d'ingresso e' gia' piena di 25 pezzi finiti mai usciti, il piu' vecchio
fermo da 135 giorni (ADR-016, misurato il 2026-09-03: 25 pezzi, 3 depositi sorvegliati).

- **Esiste gia':** `company/Memory/decisions/ADR-016-ultimo-metro.md`; `scripts/ultimo_metro.py`
  funzionante; la skill `.claude/skills/ultimo-metro`; il passaggio scritto come dato in
  `registro.yaml:1822` con criterio (*"il prodotto esiste come file ed e' dichiarato pubblicabile"*)
  e comportamento in caso di rifiuto; i 25 pezzi.
- **Manca esattamente:** (a) `company/Memory/pubblicati.json` — il registro di cio' che e' uscito
  davvero, dichiarato dall'ADR-016 come pezzo n.3 — **non esiste**: senza di lui la lista mente;
  (b) nessun lancio e' mai stato aperto, quindi `LAN-STR` non ha mai ricevuto la coda;
  (c) **INV-20 non verifica questo passaggio**: `valida_registro.py:483` fa `if p.get("esterno"): continue`,
  e questa riga ha `esterno: true`. E' scritto come dato ma **non e' sorvegliato**.

### 3 · #313 · LAN-REG → 14-TESORERIA — l'unico euro che passa fra due ecosistemi
**La ragione:** e' letteralmente l'unico passaggio dell'Impero che porti denaro reale da un ecosistema
a un altro, e il ricevente e' gia' codice funzionante. Se si accende, DE misura il primo euro della
sua storia (voce B-043).

- **Esiste gia':** il passaggio come dato in `registro.yaml:1830` con la regola di precedenza scritta
  (*"ogni euro nasce qui e sale in Tesoreria, non scende mai. Se un numero diverge, ha ragione la
  Tesoreria"*); `scripts/tesoreria.py` completo (entrata, spesa, report, incassa, previsione) con i
  suoi 4 agenti in `.claude/agents/tesoreria-*`.
- **Manca esattamente:** (a) `company/Memory/tesoreria/entrate.jsonl` e `spese.jsonl` esistono e sono
  **0 byte**: mai una riga; (b) `company/Ecosistemi/14-TESORERIA/` ha un `README.md` e due cartelle
  **vuote** (`agenti/`, `workflow/`) — l'ecosistema formale e il motore vero non sono lo stesso oggetto;
  (c) come il #312, `esterno: true` → **INV-20 lo salta**. Costo di accensione: una riga scritta a mano.

### 4 · #291 · qualsiasi team → 10-MEMORY, campo `costi` di `HC-ME-POST`
**La ragione:** e' l'aggancio piu' economico fra il lavoro che si fa ogni giorno e i soldi.
Il flusso gia' gira 303 volte; manca **un campo**.

- **Esiste gia':** `scripts/checkpoint.py`; **303 checkpoint** in `company/Memory/checkpoints/`;
  **25 ADR**; l'enforcement cablato (hook SessionStart, `CLAUDE.md`, Memory-Sentinel dichiarata) —
  *"l'unico enforcement dell'Impero che sia cablato e non solo scritto"*
  (`09-ECOSISTEMA-MEMORY.md:170-186`).
- **Manca esattamente:** il contratto dichiara `HC-ME-POST: {task_id, esito, output_paths, lezioni, costi}`
  (`:45`) e **il campo `costi` non e' stato compilato in nessuno dei 303 checkpoint**. Aggiungerlo al
  template e renderlo obbligatorio in `checkpoint.py` e' un'ora di lavoro, e da quel giorno ogni task
  chiuso lascia un numero. E' l'alimentatore naturale del punto 3.

### 5 · #160 / #180 (MB → CF, ordine) + #166 (il ritorno con 4 gate)
**La ragione:** e' il collegamento con **piu' motore vero da entrambe le parti** in tutto l'Impero, ed
e' anche il piu' pesante della mappa (9 archi `05-MB → 03-CF`). Senza di lui MB non ha prodotto.

- **Esiste gia' (RETTIFICA di A.5):** `orders/` esiste con **2 ordini reali** completi di `state.json`
  e `trace.jsonl`; `caroselli.py` (21 KB) + `carousel-factory` rendono davvero; **il gate del secondo
  ordine e' codice** (*"conta i PNG, controlla peso minimo e dimensioni reali 1080x1080, verifica
  copy.json e caption non vuota. Exit 1 se fallisce"*); 5 `config.json` di brand;
  `YOUTUBE-AUTOMATION-FACTORY/` con `fliki_client.py` sul lato MB.
- **Manca esattamente:** (a) l'ordine e' emesso da Max/claude a mano, non da un reparto MB —
  serve che `WF-YT-VIDEO-ORDER` scriva lui il `state.json`; (b) `mb-yt-handoff-validator` e i suoi
  **4 gate bloccanti** (script ≤ soglia similarita', audio -14 LUFS, visual ≥1080p, SEO) non esistono:
  e' il ritorno meglio specificato dell'Impero e non ha una riga di codice; (c) in **entrambi** gli
  ordini `handoff-cf-r6: "non_eseguito"` — il reparto QA di CF non e' costruito.

### 6 · #140 · 04-MARKETING (M2) → 01-AGENCY — il primo handoff che il dossier stesso mette per primo
**La ragione:** e' l'unico passaggio dell'Impero che un dossier indichi esplicitamente come "il primo
da fare" (`04-ECOSISTEMA-MARKETING.md:436`), e sblocca il collo di bottiglia n.2 della Sintesi B.
Porta copy reale dentro l'unica catena che incassa.

- **Esiste gia':** sul lato AGENCY il copy si consuma davvero (Bibbia dei Messaggi + `rule_keeper_lint.py`
  che blocca l'invio); sul lato MARKETING esistono le skill (`cro-copy-architect`, `copy-workflow`,
  `market-copy`) e lo standard APSOC.
- **Manca esattamente:** (a) `company/04-marketing/` **non esiste** come cartella operativa (esiste solo
  `company/Ecosistemi/04-MARKETING/` con `ECOSISTEMA.md` 58 righe e `BACKBONE.md` 46 righe di scheletro);
  (b) il **contratto di risposta** `{copy_finale, score_A8, qa_report, brand_gate, pattern_usati}`
  (`:95`) — l'unico contratto di ritorno formalizzato dell'Impero — non ha un file; (c) il registro
  `marketing/handoffs/log` (#157) non e' mai stato creato: *e' il registro dei passaggi, e non contiene niente*.

### 7 · #307 · LAN-FNL → LAN-REG — l'unico criterio che esige un euro incassato
**La ragione:** e' il solo criterio di accettazione di tutto l'Impero che pretenda una prova di cassa
**incassata e rimborsata**, e un evento arrivato *dalla piattaforma* (*"non si accetta una schermata"*,
`07-REPARTI-E-GERARCHIA.md:423`, `08-WORKFLOW.md:335`). E' il punto in cui la mappa smette di essere carta.

- **Esiste gia':** il passaggio come dato in `registro.yaml`, verificato da INV-20 (questo **non** e'
  `esterno`, quindi e' sorvegliato); l'artefatto `ART-FNL` dichiarato; il reparto `LAN-REG` con i suoi agenti.
- **Manca esattamente:** (a) nessuna piattaforma di cassa e' collegata — nessun `sale_closed`, nessun
  webhook, nessuna prova di incasso+rimborso mai eseguita; (b) le pagine non esistono (dipende da
  06-PLATFORM, che ha `IN=22` e `0` handoff ricevuti); (c) nessun lancio e' mai stato aperto.

### 8 · #200 / #234 / #272 · 06-PLATFORM → 09-OPERATIONS — l'evento `{commessa, costo, durata, esito}`
**La ragione:** e' **dichiarato da entrambe le parti in tre dossier diversi** (`06-ECOSISTEMI-CORE.md:50`,
`06a-...-V2.md:295`/`:377`, `06d-...-V2.md:92`) — il segno piu' forte di consenso architetturale che
esista nella mappa — e se esistesse *sarebbe il primo euro misurato dell'Impero*.

- **Esiste gia':** il contratto di risposta di PLATFORM e' l'unico dell'Impero che porti gia' il campo
  **`costo_evento`** nello schema (`06a-...-V2.md:377`); `empire/trace.py` (219 righe) funziona, e'
  testato e rifiuta le tracce senza prova.
- **Manca esattamente:** (a) `company/metrics/` **non esiste** come cartella; (b) `costs.sh` non esiste;
  (c) nessun emettitore: `Observability/` e' **al 100% documentazione, zero righe di codice**;
  (d) `empire/trace.py` ha **un solo chiamante automatico** (`empire/avvia.py:82`) che scrive
  **un solo tipo di traccia su cinque**. Il pezzo mancante non e' la funzione: e' il punto di aggancio.

### 9 · #283 / #325 · ogni gate/run/handoff → `company/metrics/runs.jsonl`, evento `sale_closed`
**La ragione:** `sale_closed` e' l'evento che collegherebbe l'intera mappa a un incasso. Compare in
**due file** dell'Impero (`07-BACKBONE-RUFLO-SKILLS.md:219-222` e
`company/Ecosistemi/01-AGENCY/BACKBONE.md:110`) e **non e' mai stato emesso**.

- **Esiste gia':** lo schema evento a 13 campi con 9 tipi, gia' scritto e concordato fra due documenti;
  i gate dell'AGENCY (Bibbia, Preventivo, Delivery) esistono come regole applicate.
- **Manca esattamente:** (a) la cartella di destinazione; (b) **tre formati incompatibili per la stessa
  cosa** — `Observability/README.md` (13 campi), `empire/trace.py` (8 campi), `agency/trace.jsonl`
  (10 campi): finche' restano tre, nessuno puo' scrivere una funzione sola che li alimenti tutti.
  **Prima si sceglie uno schema, poi si emette.**

### 10 · #257 · QUALSIASI ecosistema → 08-INTELLIGENCE — il context pack pre-task
**La ragione:** e' il passaggio piu' a monte di tutto l'Impero — *"ogni ecosistema, prima di un task
non banale, ottiene un context pack"*, copertura dichiarata **≥95%** (`06c-...-V2.md:56`, `:270`) — e
08-INTELLIGENCE e' l'ecosistema che riceve dal **numero massimo di partner distinti (9)**.
Sblocca moltissimo a valle. E' decimo, e non primo, per una ragione sola: **da solo non porta un euro**.

- **Esiste gia':** Empire Studio (motore di ingestione reale, con run su disco); Memory Empire v3;
  la wiki `second-brain-vault/wiki/` con `index.md` e `log.md`; la regola WIKI-FIRST cablata in `CLAUDE.md`.
- **Manca esattamente:** (a) le 3 skill proprie dichiarate (`context-pack`, `wiki-sync-guard`,
  `ingest-router`, `06c-...-V2.md:73`) **non sono forgiate**; (b) nessun ticket, nessuno SLA, nessun
  team liaison ING-LEAD/MEM-LEAD costruito; (c) la copertura reale e' **0%**, contro un ≥95% dichiarato.

---

### C.1 Cosa hanno in comune i dieci

Otto su dieci **non chiedono di costruire un motore**: chiedono di **agganciare due motori che gia'
girano**. I pezzi mancanti ricorrenti sono tre, sempre gli stessi:

1. **Un punto di aggancio dentro il codice che gia' gira** (una chiamata a `trace.scrivi()`, a
   `agency-trace.ps1`, a `checkpoint.py --costi`). Il docstring di `empire/trace.py` lo aveva gia'
   diagnosticato: *"scrivere la traccia era un atto separato, e gli atti separati non si fanno"*.
2. **Una cartella di destinazione che non esiste** (`company/metrics/`, `marketing/handoffs/log`,
   `platform/handoffs/log`, `forge/handoffs/log`, `company/Memory/pubblicati.json`).
3. **Uno schema scelto fra i dieci censiti.** L'Impero ha **dieci schemi di comunicazione diversi**,
   nessun validatore e nessun registro dei contratti (`Bus/contracts/registry.yaml` "da creare F2").
   Finche' sono dieci, ogni aggancio e' un caso a se'.

---

## SINTESI D — LE BUGIE DELL'ARCHITETTURA

Nessuna e' stata detta con malizia: sono frasi scritte al presente per cose che si voleva costruire e
non si e' costruito. Ma sono scritte al presente, e chi le legge oggi crede che esistano. Per ognuna:
**la frase del documento, citata con file e riga, contro il fatto misurato.**

---

### D.1 · "sul BUS" — il BUS non c'e'

> *"Ogni passaggio è un **handoff contract** `{from, to, payload, acceptance_criteria}` sul BUS."*
> — `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:34`

> *"Il sistema nervoso di EMPIRE OS: nessuna azione isolata, ogni passaggio di lavoro tra agenti,
> team, reparti ed ecosistemi è un **messaggio tracciato e append-only**."*
> — `PIANO-MAESTRO/07-BACKBONE-RUFLO-SKILLS.md:55-57`

**Il fatto.** `find . -name "bus.sh" -o -name "gbus.sh" -o -name "validate-handoff.sh" -o -name "costs.sh"`
→ **0 risultati**. `company/orchestrator/` non esiste. `company/runtime/bus/` e
`company/runtime/group-bus/` non esistono. `company/Backbone/Bus/` contiene **3 file**: `README.md`,
`contracts/HC-template.json`, `handoffs/.gitkeep` da 0 byte. Il README lo dice da solo:
**`company/Backbone/Bus/README.md:107` — "## Stato: DA COSTRUIRE (F2, task 2.3)"**.
La strada su cui dovrebbero viaggiare tutti i 328 passaggi non e' mai stata asfaltata.

### D.2 · I 16 codici contratto dell'AGENCY — nessuno esiste

> Sedici passaggi INTER nominati con codice proprio: `HC-AG-IB-01`, `HC-IB-AG-01`, `HC-AG-CF-01`,
> `HC-CF-AG-01`, `HC-AG-MK-01`, `HC-MK-AG-01`, `HC-AG-MB-01`, `HC-MB-AG-01`, `HC-PL-AG-01`,
> `HC-AG-PL-01`, `HC-FG-AG-01`, `HC-AG-FG-01`, `HC-IN-AG-01`, `HC-AG-IN-01`, `HC-OP-AG-01`, `HC-AG-OP-01`
> — `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:38-53`

**Il fatto.** Nessuno dei 16 esiste come file. `grep -rn "HC-" --include=*.py --include=*.sh` su
`company/` e `empire/` → **0 risultati**: nessuna riga di codice dell'Impero nomina un contratto.
I 4 contratti che esistono davvero sono tutti INTRA-AGENCY e hanno un altro prefisso.
La V2 ne aggiunge altri 6 (`01-ECOSISTEMA-AGENCY-V2.md:60-69`) e la V2 di INFO-BUSINESS altri 11
(`02-ECOSISTEMA-INFOBUSINESS-V2.md:71-90`): **33 codici contratto nominati, zero file**.

### D.3 · "lo chiede ai core via handoff contract" — nessuna delle 20 celle e' mai stata percorsa

> *"Nessun ecosistema business tocca direttamente codice, creazione di agenti, memoria o runtime:
> lo chiede ai core via handoff contract."* — `PIANO-MAESTRO/06-ECOSISTEMI-CORE.md:11`
> La Matrice di dipendenza Core × Business (`:501-506`) e' l'unica tabella 20-celle dell'Impero in cui
> nessuna cella e' vuota.

**Il fatto.** Nessuna delle 20 celle ha un contratto, un file o un log.
`company/Ecosistemi/06-PLATFORM|07-FORGE|08-INTELLIGENCE|09-OPERATIONS/` contengono solo
`ECOSISTEMA.md` e `BACKBONE.md`, e cinque ecosistemi hanno un `BACKBONE.md` di **46 righe identiche**:
uno scheletro, non un backbone. E le tre regole gemelle hanno lo stesso destino:

- *"nessun ecosistema business scrive o modifica codice di produzione in autonomia... l'implementazione
  e il deploy vivono in PLATFORM"* (`06a-ECOSISTEMA-PLATFORM-V2.md:91-93`) → 06-PLATFORM ha
  `IN = 22` sulla carta e **0 handoff ricevuti**.
- *"nessun ecosistema crea agenti, skill o team in autonomia. Ogni capability nuova passa dalla FORGE"*
  (`06b-ECOSISTEMA-FORGE-V2.md:98-99`) → ~248 agenti progettati, zero passati dalla FORGE come handoff.
- *"nessun ecosistema ingerisce contenuto esterno o scrive pagine wiki 'a mano' fuori standard"*
  (`06c-ECOSISTEMA-INTELLIGENCE-V2.md:119-122`) → **la regola operativa del repo dice il contrario**:
  `CLAUDE.md` (WIKI-FIRST) ordina di creare pagine wiki direttamente e chiude con
  *"Non chiedere il permesso. Fallo autonomamente."* Due regole non negoziabili, opposte, nello stesso
  repo, entrambe attive.

### D.4 · "ogni run genera un evento di ritorno" — nessuna run ha mai reso un costo

> *"È l'unico ecosistema con cui OGNI altro ha un handoff obbligatorio bidirezionale (ogni run passa
> da qui e ogni run genera un evento di ritorno)"* — `PIANO-MAESTRO/06d-ECOSISTEMA-OPERATIONS-V2.md:78-81`
> Risposta obbligatoria: `{esito, costo_reale, durata, tier_usato, evento_ledger_id, alert_generati}` (`:118-119`)

**Il fatto.** `company/metrics/` **non esiste**. `costs.sh` non esiste. `company/Backbone/Observability/`
contiene **un solo file**, `README.md`: e' al 100% documentazione, zero righe di codice, zero file di
dati. **Nessuna run dell'Impero ha mai restituito un `costo_reale`.** E' esattamente la voce B-043
(*"DE non misura un solo euro"*), scritta nero su bianco anche nel docstring di `scripts/tesoreria.py`:
*"Misurato il 2026-09-03: Digital Empire non misurava un solo euro."*

### D.5 · "un handoff senza CP-id è invalido per contratto" — nessuno dei 328 ne porta uno

> *"l'acceptance criteria di OGNI team L3/L4 della holding include 'CP scritto in Memory' — un handoff
> senza CP-id è invalido per contratto."* — `PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:180-182`

**Il fatto.** Nessuno dei 328 passaggi porta un CP-id, nemmeno i 4 percorsi l'11 giugno: le righe di
`company/Memory/state/agency/trace.jsonl` hanno i campi
`ts / cycle_id / step / event / from_reparto / to_reparto / hc / agent / payload_summary / notes`
— **`cp_id` non c'e'** (verificato aprendo il file).
E' la regola che, applicata alla lettera, **invalida per contratto l'intera mappa** — inclusi i 4 soli
passaggi che siano mai stati attraversati.

### D.6 · "nessun lavoro parte senza ordine valido" — l'ordine c'e', il passaggio no

> *"Nessun lavoro parte senza ordine valido. Il CF-Conductor (L1) rifiuta ordini incompleti"*
> — `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md:63`

**Il fatto — con rettifica a favore.** Contro quanto scritto in 02b, `orders/` **esiste** e contiene
2 ordini reali (vedi A.5). Ma nessuno dei due e' stato aperto da un committente-ecosistema:
`CF-2026-PREVENTA-001` dichiara `brand_kit_path: null` e i suoi gate FORMATO/BRAND sono
*"verifica manuale (CF-R5-QA non ancora costruito come script reale)"*; in **entrambi**
`handoff-cf-r6: "non_eseguito"` — *"CF-R6-QA-Gate non ancora costruito come reparto operativo"*.
E il conductor che dovrebbe rifiutare gli ordini incompleti (`CF-A00-conductor`, `CF-D-DISPATCH`)
non esiste: chi ha aperto quei due ordini e' Max con Claude, a mano.
**Il lavoro parte. L'ordine lo si scrive dopo, per onesta'.**

### D.7 · "nessun ecosistema scrive copy di conversione in autonomia" — tutto il copy vero e' nato fuori

> *"Regola: **nessun ecosistema scrive copy di conversione in autonomia**. Può fare bozze, ma il gate
> A8 + brand gate vive qui."* — `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING.md:68-70`
> *"il copy che vende è SEMPRE di Marketing"* — `03-ECOSISTEMA-CONTENT-FACTORY.md:520`

**Il fatto.** `company/04-marketing/` non esiste; esiste solo `company/Ecosistemi/04-MARKETING/` con
`ECOSISTEMA.md` (58 righe) e `BACKBONE.md` (46 righe di scheletro condiviso). Nessun handoff di
MARKETING esiste su disco, **ne' in entrata ne' in uscita**. Nel frattempo il copy di conversione
realmente prodotto e usato — i messaggi outreach sotto `rule_keeper_lint.py`, gli 8+6 slide dei
caroselli Preventa con prezzo e CTA — e' stato scritto **fuori** da MARKETING, senza gate A8, senza
brand gate e senza il contratto di risposta. La regola c'e'; l'ecosistema che dovrebbe applicarla ha
`IN = 28` sulla carta e **0** nella realta'.

### D.8 · "ogni reparto ha almeno un handoff reale entro M5" — nessuno ne ha mai avuto uno

> *"ogni reparto ha almeno un handoff reale entro M5"* — `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md:676`
> *"primo handoff reale previsto: copy reale per outreach/preventivo + baseline KPI"* — `04-ECOSISTEMA-MARKETING.md:436`

**Il fatto.** Nessun reparto di 04-MARKETING ha mai avuto un handoff, reale o simulato. Ed e' l'unica
promessa della mappa che porti **una data**: una scadenza scritta per una cosa che non e' mai iniziata.

### D.9 · "vietato consegnare un ruolo in un markdown" — 307 passaggi su 328 sono markdown

> *"costruisce gli script eseguibili reali (.py/.ps1: orchestrazione, dispatch, QA) richiesti dallo
> standard §0 — **'vietato consegnare un ruolo in un markdown'**"*
> — `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:232`

**Il fatto.** Questo censimento e' la dimostrazione della regola violata: **307 dei 328 passaggi
(91,2%) vivono solo in prosa markdown**, e l'agente che avrebbe dovuto impedirlo
(`frg-orchestration-builder`) non e' mai stato creato. Insieme a lui manca `frg-handoff-designer`,
che *"verifica ogni contratto I/O"* (`:195`, `:206`): **il progettista dei contratti dell'Impero e'
un agente mai forgiato**.

### D.10 · "~248 agenti progettati, 19 censiti" — il registro dei destinatari e' inservibile

> *"Registro Identity-HR disallineato dal reale (rischio già segnalato in `V2-INDEX.md`:
> ~248 agenti progettati, 19 censiti)"* — `PIANO-MAESTRO/06b-ECOSISTEMA-FORGE-V2.md:547`

**Il fatto — la bugia e' doppia.** Oggi `company/Backbone/Identity-HR/registro-agenti.yaml` ha
**653 righe e 142 voci `- id:`** (verificato): quindi anche il "19" del dossier e' vecchio. Ma il
disallineamento resta di oltre il 40%, e soprattutto il registro **non serve a instradare**: dei 142
agenti, `input_schema` e' compilato **1 volta**, `output_schema` **1 volta**, `reports_to` **7**,
`supervises` **7**. E l'unico lettore, `scripts/verify-agents.py`, **non guarda nessuno di quei campi**.
Il gate `G-REGISTRY` (*"artefatto non consegnabile finche' il registro non e' coerente (100% agenti
censiti)"*, `:465`), se acceso oggi, bloccherebbe **ogni consegna dell'Impero**.
E il Bus dichiara che mittenti e destinatari sono *"validati contro Identity-HR"*
(`07-BACKBONE-RUFLO-SKILLS.md:62-64`): con questo registro, la validazione rifiuterebbe quasi tutti.

### D.11 · Il gate B2 — "un handoff che attraversa 2 ecosistemi e torna `done`"

> *"B2.3 wiring nei primi workflow reali (outreach AGENCY, F4)"* — `07-BACKBONE-RUFLO-SKILLS.md:94-96`
> Gate B2: un handoff di test che **attraversa 2 ecosistemi e torna `done`** (`:512`)

**Il fatto.** Mai superato. Il solo ciclo esistente (11 giugno) e' interamente **dentro** 01-AGENCY:
non ha attraversato nessun confine. E lo schema `HC-v1` dei 4 contratti veri non ha nemmeno un campo
`status` mutabile — e' costante `"template"` in tutti e quattro: **non esiste un posto dove scrivere
`done`**.

### D.12 · "brand_kit obbligatorio nell'inter-ecosistema" — i 4 contratti veri sarebbero tutti invalidi

> *"`brand_kit` obbligatorio nel payload inter-ecosistema (pattern #11 multi-tenant)... handoff inter
> senza `brand_kit` = invalido"* — `company/Backbone/Bus/README.md:57`, `:96`

**Il fatto.** Lo schema `HC-v1` **non ha il campo**: i 4 contratti dell'AGENCY sarebbero invalidi 4 su 4
per la regola del loro stesso Bus. E il file che il pattern richiede non esiste con quel nome:
`find . -name "brand-kit.json"` → 0. Esistono **5 `config.json` di brand** in
`carousel-factory/brands/` (vedi A.5), che sono la cosa giusta con il nome sbagliato e uno schema diverso.

### D.13 · "tutto il resto di EMPIRE OS lo alimenta o lo amplifica"

> *"AGENCY è il pilastro revenue della holding: tutto il resto di EMPIRE OS lo alimenta o lo amplifica."*
> — `PIANO-MAESTRO/01-ECOSISTEMA-AGENCY.md:16`

**Il fatto.** Sulla carta AGENCY riceve **18 archi INTER** da 8 ecosistemi diversi.
**Nessuno dei 18 e' mai avvenuto.** L'unica cosa che alimenta davvero AGENCY oggi e' `leads.db` e uno
script che qualcuno lancia a mano.

### D.14 · TESORERIA "ecosistema 14" — due cartelle vuote

> *"ogni euro nasce qui e sale in Tesoreria, non scende mai. Se un numero compare in tutti e due i
> posti ed è diverso, ha ragione la Tesoreria."*
> — `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/07-REPARTI-E-GERARCHIA.md:444-447`, `dati/registro.yaml:1830`

**Il fatto.** `company/Ecosistemi/14-TESORERIA/` contiene `README.md` e due cartelle **vuote**
(`agenti/`, `workflow/`). Non ha `ECOSISTEMA.md`, non ha `BACKBONE.md`. Il motore vero
(`scripts/tesoreria.py`, completo e funzionante) sta fuori dall'ecosistema che porta il suo nome, e i
suoi due libri mastri (`company/Memory/tesoreria/entrate.jsonl`, `spese.jsonl`) sono **0 byte**.
La regola di precedenza fra due numeri e' scritta con cura chirurgica per un confronto che non e' mai
stato possibile fare: **i numeri sono zero da entrambe le parti**.

---

## LA FRASE CHE RIASSUME IL CENSIMENTO

L'Impero non ha un problema di progettazione dei passaggi: **328 passaggi censiti, 55 marcati VAGO,
68 senza criterio di accettazione, 260 con un criterio scritto** (contato riga per riga).
Ha un problema di **percorrenza**: 21 hanno un contratto, 4 sono
stati attraversati una volta in 58 secondi con un cliente finto, **nessuno ha mai attraversato un
confine fra due ecosistemi**.

E la diagnosi era gia' scritta in casa, nel docstring di `empire/trace.py`:

> *"scrivere la traccia era un atto separato, e gli atti separati non si fanno."*

Vale identica per i passaggi di consegne. Finche' consegnare sara' **un atto in piu'** invece di un
sottoprodotto del lavoro, questa mappa restera' una mappa di strade su cui non passa nessuno.

---

*Fine del censimento 02d. Sintesi A, B, C, D complete.*
*Gemelli: `dati/censimento-02-collegamenti.md` (infrastruttura) · `dati/censimento-02b-mappa-collegamenti.md` (la tabella dei 328).*
