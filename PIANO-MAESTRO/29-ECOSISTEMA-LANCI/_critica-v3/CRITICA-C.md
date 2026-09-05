# CRITICA-C — dossier 07, 08, 09, 10

> Revisione ostile e indipendente. Ogni rilievo porta il riferimento `dossier:riga`.
> Riferimenti incrociati ai dossier 00-06 usati solo come prova, non come bersaglio.
> STATO: sezioni 1-3 complete. 4-8 in lavorazione.

---

## 1. I 50 AGENTI REGGONO? — verdetto

**No. E il numero 50 è a sua volta sbagliato: è per difetto.**

### 1.1 Il conto non torna, nella riga stessa che dichiara di averlo rifatto

`08:116` promette: *"Qui il conto è stato rifatto e verificato riga per riga."* La riga di totale,
`08:134`, dice: **50** *(41 di reparto + 4 sentinelle di reparto già contate + 4 trasversali + 1 direzione)*.

Sommando la colonna "Agenti" della stessa tabella (`08:122-133`), escludendo Direzione e trasversali:
3+4+5+3+6+4+3+4+3+4+4+2 = **45**, non 41. E le sentinelle *dentro* i reparti sono **due**
(`edt-sentinella` a `08:128`, `tsr-sentinella` a `08:128`), non quattro. Il totale 50 è corretto per
caso (45+4+1), la spiegazione che lo giustifica è sbagliata due volte. Un censimento che si
autocertifica e sbaglia l'aritmetica non è un censimento.

### 1.2 Il censimento è incompleto: gli agenti veri sono ≥55

| Agente esistente in un altro dossier | Presente in `08:118-134`? |
|---|---|
| `lan-cpy-giudice` (`05:74`, `05:80`, `05:251`) | **No** — Copy elencato con 6 agenti, senza il giudice |
| `lan-prod-intake`, `-verificatore-ricerca`, `-architetto`, `-produttore`, `-collaudatore`, `-beta-coordinatore`, `-packager`, `-certificatore`, `-inventariante` (`03:298-300`) | **No** — Prodotto elencato con 5 |

Peggio: `03:298` scrive *"la skill e gli **8** agenti"* e poi ne elenca **nove**. Quindi il reparto
Prodotto ha **tre conteggi diversi in due dossier**: 5 (`08:124`), "8" (`03:298`), 9 (l'enumerazione
alla riga successiva). Il numero onesto non è 50: è **almeno 55**, e nessuno lo sa.

### 1.3 Collisione di nomi già scritta nel piano

La sigla del reparto è `LAN-PRD` (`00:259`, `01:124`). L'agente dello scaglione minimo è
`lan-prd-collaudatore` (`01:400`). Il dossier 03 usa `lan-prod-*` **33 volte**. Sono due prefissi per
lo stesso reparto. `08:159` avverte: *"name identico al nome del file. Un disallineamento e l'agente
non si trova."* Il piano contiene già il disallineamento che vieta.

**Riparazione:** una tabella normativa dei nomi in dossier 08 (`lan-<sigla-reparto-3-lettere>-<ruolo>`),
sigla presa da `00:257-268`, e `registro.py` che rifiuta qualunque file `.claude/agents/lan-*.md` il
cui prefisso non corrisponda a un reparto esistente.

### 1.4 Quindici agenti sono funzioni Python travestite — da sopprimere

Il piano non si pone **mai** la domanda "questo richiede un modello linguistico?". Il principio 7
(`08:93`) ragiona su *quale* modello, mai su *se serva un modello*. Elenco con la riga:

| # | Agente | Riga | Cosa fa davvero | Sostituto |
|---|---|---|---|---|
| 1 | `lan-reg-calendarista` | `08:130` | aritmetica sulle date. `07:273` lo dice da sé: *"il calendario si genera, non si scrive… deve essere un file prodotto da un comando"* | `calendario.py` |
| 2 | `lan-reg-tracciatore` | `08:130` | raccoglie i numeri del giorno — che `09:175` mette esplicitamente in colonna "si automatizza" | `tracking.py` |
| 3 | `lan-reg-prova-a-secco` | `08:130` | un flag. `07:89` assegna già la prova a secco al conductor: due agenti per un `--dry-run` | `lancio.py --dry-run` |
| 4 | `lan-tsr-registratore` | `07:91`, `07:95` | append di una riga + chiamata allo script dell'Impero. CRUD | `costi.py` |
| 5 | `lan-tsr-sentinella` | `07:92` | applica le quattro formule di `07:121-130`. Aritmetica su denaro, per giunta | `costi.py` |
| 6 | `lan-qlt-gate-costi` | `08:131` | valuta `≤ 0,10`. Un `if`. E `07:102` lo spezza in due agenti ("la sentinella propone, il gate verbalizza"): **due modelli linguistici per un confronto e una scrittura di file** | `gate.py` |
| 7 | `lan-fnl-verificatore` | `08:126` | HTTP 200 + presenza dell'evento (`00:284`). `requests` + una query | `verifica_pagine.py` |
| 8 | `lan-prd-inventariante` | `08:124` | inventaria i materiali esistenti. Un `glob` | `inventario.py` |
| 9 | `lan-edt-magazziniere` | `08:128` | lo stesso `glob` sui contenuti | `inventario.py` |
| 10 | `lan-trf-misuratore` | `08:127` | le **stesse** formule di `07:124-128` già assegnate a `lan-tsr-sentinella`: due agenti che calcolano lo stesso costo di acquisizione = **due fonti di verità sullo stesso numero** | `costi.py` |
| 11 | `lan-str-obiettivi` | `08:123` | obiettivi derivati da prezzo e `vendite_per_pareggio` (`07:122`) | `pareggio.py` |
| 12-15 | le 4 sentinelle trasversali | `08:133` | quattro soglie: `scaduto_il < oggi`, `mai-letti > 40%` (`01:247`), `SOSPESO senza data di revisione` (`00:317`), azione irreversibile senza firma | `sentinelle.py` |

**L'aggravante sulle sentinelle:** `08:106` concede loro *sola lettura* e *"non agisce: segnala"*.
Un modello linguistico a cui è vietato scrivere e il cui unico output è un booleano è il modo più
costoso mai inventato di scrivere un `if`. Quattro volte.

**Bilancio: 15 agenti → 5 moduli Python** (`calendario.py`, `costi.py`, `verifica_pagine.py`,
`inventario.py`, `sentinelle.py`), tutti già dentro i "17 file .py" che `01:468` dichiara e che
nessuno scaglione specifica (§2.5).

### 1.5 Otto agenti da fondere

| Coppia/gruppo | Righe | Perché è uno solo |
|---|---|---|
| `lan-int-ascoltatore` + `lan-int-osservatore` | `07:165`,`07:170` / `07:167` | stesso mestiere (raccogliere frasi esterne con la fonte), cambia solo il bersaglio: pubblico vs concorrenti. Un `ricercatore` con un parametro. **−1** |
| `lan-cpy-fondamenta` · `vendita` · `derivati` · `email` | `08:125` | quattro scrittori che differiscono per il pezzo; e `08:270` dice che la skill di copy **esiste già e viene invocata**. Ne bastano due (madre + derivati). **−2** |
| `lan-mem-distillatore` + `lan-mem-bibliotecario` | `08:132` | `01:150` ammette che LAN-MEM lavora due volte per lancio. Due agenti per due momenti in sequenza. **−1** |
| `lan-cpy-bibliotecario` | `08:125` | duplica `conoscenza-empire`, che `08:278` dichiara fornitore unico della formazione | **−1** |
| `lan-qlt-gate-fonti` + `gate-copy` | `08:131` | la descrizione ufficiale del gate generico (`08:150`) è *"esegue un criterio di controllo **scritto in un file**"*. Se il criterio è in un file, il gate è **uno**, parametrizzato dal file | **−2** |
| I 12 `conductor` | `08:122-133` | `01:158` ammette già il principio: *"il direttore di reparto è superfluo per due agenti che girano in sequenza"*. Vale identico per TSR (3 agenti, 2 soppressi), TRF (3), REG (4→1), EDT (4→2) | **−4** |

### 1.6 Il verdetto numerico

| | Dichiarato | Reale | Proposto |
|---|---:|---:|---:|
| Agenti | 50 (`08:134`) | ≥55 | **~21** |
| Moduli Python | non contati | — | +5 |

**E lo scaglione minimo si accorcia con loro.** Degli undici di `01:393-407`, quattro sono nella
lista di soppressione (`lan-fnl-verificatore`, `lan-reg-calendarista`, `lan-reg-tracciatore`, e
`lan-qlt-gate` limitatamente ai gate calcolabili). Il minimo vero è **7 agenti + 4 script**, e questo
è l'unico modo di far rientrare S1 nelle ore che dichiara (§2.3).

**Principio mancante, da aggiungere ai sette di `08:83-93`:**
> **8. Se l'output è determinato dall'input, è una funzione, non un agente.** Un agente si giustifica
> solo quando due esecuzioni corrette possono legittimamente differire.

---

## 2. LA STIMA DI COSTRUZIONE REGGE?

**No. Manca la voce più grossa, e non è un dettaglio: è più della metà del totale.**

### 2.1 Le 139-187 ore sono solo COSTRUZIONE. L'ESERCIZIO non è contato da nessuna parte

Le durate dei flussi esistono, sparse, e nessun documento le somma:

| Flusso | Ore-uomo per lancio | Riga |
|---|---|---|
| WF-CPY | 40-55 | `05:24` |
| WF-FNL + WF-EDT | 30-45 (10-15 se le pagine esistono) | `06:28` |
| WF-INT | 16-30 | `07:158` |
| WF-OFF | 3-5 | `04:40` |
| WF-TSR | ~9,5 + **T4 "continuo"**, senza numero | tabella `07:87-95` |
| WF-PRD | non quantificato per il percorso E | `03:17` |
| **WF-REG** | **nessuna ora dichiarata: il flusso non ha tabella** | `07:231-359` |

Nella lettura **più generosa** (pagine già esistenti, percorso prodotto E), **un lancio costa 80-115
ore-uomo**. È il **60-80% dell'intero budget di costruzione**, per ogni singolo lancio, e non compare
in nessuna tabella dei dossier 09 o 10. `10:79` elenca fra le conseguenze negative *"~235 file,
139-187 ore-uomo"* e tace sull'esercizio.

**Riparazione:** una tabella *"COSTO DI ESERCIZIO DI UN LANCIO"* in dossier 09, con la somma
esplicita, e il confronto onesto: *questo sistema costa X ore per lancio; oggi il Manuale ne costa 0
perché non esce.* È il numero che decide se vale la pena costruirlo.

### 2.2 Una stima contraddice sé stessa nella stessa pagina

`07:158`: WF-INT dura **16-30 ore-uomo**. La sua tabella delle fasi (`07:164-172`) somma:
1 + (6-10) + 3 + (5-8) + 3 + 3 + 2 + 2 + 1 = **26-33 ore**. L'estremo inferiore dichiarato è
**dieci ore sotto** il minimo che il flusso stesso richiede. Chi pianifica sul 16 sbaglia del 60%.

### 2.3 S1 è sottostimato di circa 3x

`09:90`: *"S1 — IL MINIMO · 30-40 ore-uomo + il tempo di una firma"*.
`09:113-118`: i criteri di chiusura di S1 richiedono che **un lancio vero** apra, chiuda, produca
`consuntivo.md` con un ricavo e `debrief.md` con tre schemi.

Cioè: S1 non chiude finché non sono state spese anche le 80-115 ore di **esercizio** del §2.1. La
stima di S1 conta la costruzione degli strumenti e non conta l'uso degli strumenti, che è il suo
stesso criterio di chiusura. **S1 è 110-155 ore, non 30-40.**

Questo è esattamente l'errore che il caller prevede — una stima che ignora l'integrazione sbaglia di
2-3x — con l'aggravante che qui non è l'integrazione a mancare: è l'esecuzione.

### 2.4 La condizione di abbandono #2 è aritmeticamente autolesionista

`09:214`: *"Il lancio pilota non esce entro **60 giorni** dall'inizio di S1 → si ferma la costruzione."*

Contiamo:
- S1 a 3 ore al giorno = **2,5 settimane** (`09:92`) ≈ **17 giorni di calendario**;
- il calendario di lancio va da T-30 a T+7 = **38 giorni** (`07:242`);
- totale minimo, con **zero** slittamenti e la firma che arriva istantaneamente: **55 giorni**;
- e il calendario stesso mette da parte **12 giorni di margine** (`07:269`) per rifacimenti che
  definisce *normali*.

Restano 5 giorni di gioco contro 12 giorni di margine previsto. **La condizione scatta al primo
rifacimento previsto dal piano stesso.** Un piano che si autoabbandona sul percorso nominale.

**Riparazione:** o il tetto sale a ~100 giorni, o il pilota gira su un calendario accorciato
(§3, D-C-01) — non entrambe le cose lasciate come sono.

### 2.5 Cosa manca dal conto, voce per voce

| Cosa | Prova | Ore allocate |
|---|---|---|
| **`registro.py`** — il verificatore su cui poggia tutta l'ufficializzazione (`08:218`, `08:225-232`) e il "vincolo tecnico" degli scaglioni (`09:11`, `09:51`, `10:56`) | non compare in S0 (`09:60-69`) né in S1-S4 | **0** |
| `costi.py` (`07:36`) | citato, mai pianificato | 0 |
| I 12 script mancanti: `01:468` dichiara **17 file .py**, S0 ne specifica **5** (`09:62-68`) | — | 0 |
| La scrittura dei 50 (55) agenti: la procedura di `08:200-212` ha **10 passi per agente** (specifica + file agente + 3 registri + wiki con 2 link + verifica + checkpoint). A 20-30 min l'uno | — | **17-25 ore, non contate** |
| I file di criterio dei 13 gate (`00:277-289`), che `08:150` dichiara essere il cuore del gate generico | — | 0 |
| La migrazione di `IB-L2-LANC` (`10:50`) | dichiarata nella decisione | 0 |
| Debug e integrazione fra reparti | mai nominati | 0 |

`10:79` dichiara **~235 file** contro 139-187 ore = **45 minuti a file**, comprese specifiche,
agenti, schemi JSON, pagine wiki e righe di registro. Per i soli agenti la procedura che il piano
stesso scrive ne richiede il doppio.

### 2.6 Le condizioni di sblocco: **una su cinque è un comando**

| Scaglione | Condizione | Eseguibile? |
|---|---|---|
| S0 | `09:73-81` — due comandi, exit code atteso ≠ 0, verbale scritto, stato invariato | ✅ **Sì. È il modello.** |
| S1 | `09:113-118` — *"il carrello si è aperto e chiuso alle date del calendario"* | ❌ prosa |
| S2 | `09:134` — *"si prova facendo fallire uno dei tre di proposito"*, nessun comando | ❌ prosa |
| S3 | `09:143-149` — *"una ricerca finta… viene fermata dal gate"* | ❌ prosa |
| S4 | `09:155-163` — *"uno schema del primo lancio cambia una decisione del secondo, e si vede dove"* | ❌ prosa, e non falsificabile |

Il vincolo *"un lancio in APPRESO"* (`09:126`, `09:140`, `09:153`) **sarebbe** verificabile con un
comando — `lancio stato` esiste (`09:68`) — e non è scritto da nessuna parte.

**Riparazione:** ogni scaglione chiude con `tests/chiusura_S<n>.py`, invocazione ed exit code atteso
scritti nella sua sezione, esattamente come S0. Il criterio di S4 va reso falsificabile: *"esiste un
record in `memoria/pattern/` con `letto_volte ≥ 1` citato per identificativo dentro `decisione.json`
del secondo lancio"* — verificabile con un grep, a differenza di "prende una decisione diversa da
quella che avrebbe preso", che nessuno può provare né smentire.

### 2.7 Un bias ammesso e non prezzato

`09:201`: *"L'analogia può sbagliare, e sbaglierà sempre nello stesso modo — **S1 durerà più del
previsto**."* Detto questo, l'intervallo di S1 resta 30-40. Un errore sistematico dichiarato e non
incorporato non è una stima: è una speranza con una nota a piè di pagina.

---

## 3. DIFETTI STRUTTURALI GRAVI

### D-C-01 · Il lancio pilota non può attraversare la propria macchina a stati — deadlock di costruzione

**Dove:** `09:40-49` (ordine degli scaglioni) · `09:51` (vincolo S1→S2) · `01:266-273` (macchina a
stati) · `00:283`, `00:285` (GATE-CPY-1, GATE-EDT-1) · `01:416` (modalità pilota).

**Perché si rompe.** La macchina a stati impone `DATATO → sprint: testi + funnel + contenuti →
IN_PRODUZIONE → GATE-REG-1 → PRONTO` (`01:266-273`). Lo sprint è governato da `GATE-CPY-1` (punteggio
≥80) e `GATE-EDT-1` (piano editoriale senza righe incomplete). Ma i reparti `LAN-CPY` e `LAN-EDT`
**sono in S2** (`09:130-132`), e S2 *"si sblocca solo con un lancio in `APPRESO`"* (`09:126`), vincolo
dichiarato **tecnico**: *"finché `lanci/` non contiene un lancio in stato `APPRESO`, il registro
rifiuta di registrare gli agenti di S2"* (`09:51`).

Per arrivare ad `APPRESO` serve passare GATE-CPY-1. Per avere GATE-CPY-1 serve S2. Per avere S2 serve
`APPRESO`. **Cerchio chiuso.**

E la valvola di sfogo non copre il caso: la modalità pilota di `01:416` ammette l'attestazione firmata
**solo** per `GATE-INT-1` e `GATE-PRD-1/2/3`. Su CPY ed EDT non è prevista, e su OFF è esplicitamente
esclusa (`01:433`). Aggiungasi `GATE-TSR-1` (`00:286`), il cui reparto è in **S4** (`09:157`).

**Il caso concreto.** Gael costruisce S0 e S1 come scritti, crea il lancio del Manuale, ottiene prezzo
e data, arriva a `DATATO` — e lì il comando `lancio avanza` chiama un gate il cui file di criterio non
esiste, prodotto da un reparto che il registro rifiuta di abilitare. Il pilota si ferma in `DATATO`
per sempre: **lo stesso identico difetto** che `01:386-391` dichiara di aver corretto ("un lancio
avviato così si sarebbe fermato in `VALUTATO` per sempre"), spostato di uno stato in avanti.

**La riparazione.** Introdurre nella macchina a stati un **profilo di lancio** (`profilo:
"minimo" | "completo"`) dichiarato in `offerta.json` e verificato da `stato_lancio.py`:
- `minimo` attraversa 5 gate (STR-1, OFF-1, FNL-1, REG-1, MEM-1) e **salta CPY/EDT/TRF/TSR con debito
  scritto**, con lo stesso meccanismo di attestazione di `01:416-427` (campi `vale_per`, `debito`);
- `completo` attraversa tutti e 14 (v. D-C-13).

Il registro abilita i reparti per **profilo**, non per scaglione. E dossier 09 va riscritto di
conseguenza: oggi S1 costruisce 4 reparti (`09:40`) mentre il minimo vero ne richiede 8 (D-C-10).

---

### D-C-02 · Il gate ha strumenti che gli impediscono di produrre il suo unico artefatto

**Dove:** `08:103` e `08:151` (Gate = sola lettura, `tools: Read, Grep, Glob`) contro `07:90`,
`07:93`, `07:102`, `07:171` (colonna Output di `lan-qlt-gate` = **verbale**) e `00:297` (*"Verbale: il
file che un gate scrive **sempre**, anche quando lascia passare. Senza verbale, il gate non è stato
eseguito"*).

**Perché si rompe.** Un agente con `tools: Read, Grep, Glob` non ha `Write`. Non può scrivere il
verbale. Non ha `Bash`, quindi non può nemmeno invocare `gate.py` perché lo scriva. La correzione che
`08:50` definisce *"la più importante di tutto questo dossier"* rende **fisicamente impossibile** al
gate di eseguire il compito che tredici righe di tabella gli assegnano.

**Il caso concreto.** Gael scrive `.claude/agents/lan-qlt-gate.md` copiando alla lettera il
frontmatter di `08:147-155`. Al primo `lancio avanza`, l'agente valuta correttamente e poi termina: il
verbale non esiste, `handoff.py` (`09:66`) rifiuta il passaggio *"senza verbale di gate"*, e il lancio
si blocca senza che nulla dica perché. Il difetto si presenta come un bug misterioso, non come un
errore di progetto.

**La riparazione.** Il verbale non lo scrive l'agente: **lo scrive `gate.py`**, che invoca l'agente
per la sola parte di giudizio non calcolabile e ne serializza l'esito. Va scritto esplicitamente in
`08:103` e nella tabella di `07:97-103`: *"Chi lo esegue: `gate.py`, che consulta `lan-qlt-gate` solo
per i criteri non calcolabili"*. Conseguenza sana: la maggior parte dei gate non ha bisogno di alcun
agente (§1.4, #6).

---

### D-C-03 · La sentinella read-only deve produrre un JSON (stesso difetto, seconda occorrenza)

**Dove:** `08:106` (Sentinella = sola lettura, *"non agisce: segnala"*) contro `07:92`, dove `T5` dà a
`lan-tsr-sentinella` l'output **`tracking/costi-<data>.json`**.

**Perché si rompe.** Identico a D-C-02, e conferma che non è una svista isolata ma un errore di
modello: il piano ha progettato i profili di strumenti guardando ai *divieti* e mai agli *artefatti
che ciascun ruolo deve produrre*. Le due tabelle non sono mai state confrontate.

**Il caso aggravante.** `07:142` dice che l'assenza di spese per tre giorni è *"un'anomalia"* che la
sentinella deve segnalare. Con sola lettura, la segnalazione muore alla fine del contesto del
sottoagente: nessun file, nessun log (D-C-14), nessuno se ne accorge. Il presidio contro
l'abbandono della registrazione manuale — che `07:91` dichiara *"continuo"* e *"molti importi si
inseriscono a mano"*, cioè la cosa più probabile che venga abbandonata — è muto per costruzione.

**La riparazione.** Le sentinelle diventano `sentinelle.py` (§1.4) che scrive su
`lanci/<id>/log/allarmi.jsonl` e ritorna exit code. Nessun modello linguistico coinvolto.

---

### D-C-04 · Il campo `tools` non sa fare tre delle sei cose che il piano gli chiede

**Dove:** `08:52-59` (la tabella dei profili) e `08:61-63` (*"una regola imposta dagli strumenti
disponibili non viene disobbedita"*).

**Perché si rompe.** L'intuizione è giusta, l'implementazione dichiarata non esiste:

| Profilo | Riga | Il campo `tools` sa farlo? |
|---|---|---|
| **Archivista**: *"scrittura **limitata alla propria cartella di memoria**"* | `08:57` | **No.** `tools: Read, Write` concede `Write` **ovunque**. Il campo non ha alcuna nozione di percorso. L'archivista può riscrivere `offerta.json` |
| **Direttore**: *"tutti"* gli strumenti | `08:59`, `08:101` | **No**, ed è il caso peggiore: il principio 4 (`08:90`) dice *"nessun agente compie da solo un'azione irreversibile — **imposto dagli strumenti**"*. Il direttore ha `Bash`: può spedire, pubblicare, pagare. Il vincolo salta esattamente sul ruolo che può fare più danno |
| **Operatore**: *"lettura, scrittura"* | `08:102` | **Insufficiente.** Tutta la strategia di `08:265-279` ("avvolgere invece di riscrivere") richiede di **invocare skill e agenti esistenti**. Un agente con solo `Read, Write` non ha `Skill`, non ha `Agent`, non ha `Bash`: non può invocare la skill di copy (`08:270`), non può orchestrare le tre skill di sito (`08:273`), non può ordinare alle fabbriche (`08:277`). **La scelta architetturale portante dell'ADR (`10:69`) è ineseguibile con i profili dichiarati** |

**La riparazione, su tre livelli distinti — perché sono tre meccanismi diversi:**
1. `tools` per ciò che sa fare: negare `Write`/`Bash` dove non servono, **e aggiungere `Skill` e
   `Agent` ai profili Operatore e Direttore**, altrimenti l'avvolgimento non funziona;
2. `.claude/settings.json` con regole `permissions.deny` per lo scoping di percorso
   (`Write(company/Ecosistemi/15-LANCI/lanci/**)` negato agli archivisti) — è l'unico posto dove il
   confine di cartella è imponibile;
3. `registro.py` controllo #3 (`08:231`) esteso: verifica non solo che il gate non abbia `Write`, ma
   che **ogni** agente abbia esattamente il set del suo ruolo, e che il direttore **non** abbia `Bash`.

E va cancellata da `08:61-63` la pretesa che gli strumenti impongano da soli le sei regole: ne
impongono due.

---

### D-C-05 · Il contratto d'uscita esiste solo in prosa, e i campi che lo renderebbero leggibile sono vietati

**Dove:** `08:184-185` (lo scheletro chiede *"## 2. Contratto d'ingresso"* e *"## 3. Contratto
d'uscita — cosa restituisci, con quale schema"*) contro `08:166` (i campi `inputs` e `outputs` sono
fra quelli che **fanno scartare il file in silenzio**).

**Perché si rompe.** Il contratto d'uscita di ognuno dei 50 agenti è **testo libero dentro il corpo
markdown**. Nessuno strumento lo legge, nessuno lo verifica, nulla impedisce a un agente di
restituire qualcosa di diverso. È esattamente ciò che `08:61` condanna: *"una regola scritta in prosa
viene disobbedita"*. Il piano applica la propria lezione al campo `tools` e la ignora sul contratto
d'uscita, che è la cosa che rende concatenabile una catena.

**Il caso concreto.** `lan-off-conductor` è *"l'unico che scrive `offerta.json`"* (`01:401`).
`lan-fnl-verificatore` a valle si aspetta un prezzo numerico. Il primo restituisce `"prezzo": "97€"`
invece di `97.00`. Nessun controllo scatta: gli schemi JSON di `09:67` validano gli **artefatti su
disco**, non ciò che un agente **restituisce al chiamante**. Il difetto emerge tre fasi dopo, dentro
`ricavo_netto_unitario = prezzo × (1 − commissione/100)` (`07:121`), come un errore aritmetico.

**La riparazione.** Il contratto esce dal frontmatter e dalla prosa e diventa un file:
`15-LANCI/schemi/<nome-agente>.io.json` con `{"input": "<schema>", "output": "<schema>"}`, riferito
agli schemi di `09:67`. `registro.py` acquisisce un **quinto controllo**: per ogni agente esiste il
suo `.io.json`, gli schemi citati esistono, e **lo schema di uscita di A coincide con lo schema
d'ingresso di B per ogni arco dichiarato in `08:189` (Connessioni)**. Questo, e non la sezione 3 del
corpo, è ciò che rende un orchestratore capace di concatenare 21 agenti.

---

### D-C-06 · WF-REG non ha fasi, agenti, output né ore — lo stesso difetto che il piano dichiara corretto

**Dove:** `07:231-359` (tutta la Parte C).

**Perché si rompe.** `10:187` elenca fra i dieci difetti gravi corretti: *"Il flusso del funnel non
aveva fasi né agenti: dodici sezioni e nessuno che le eseguisse. **Il pre-mortem numero uno,
commesso dal piano stesso**"*. WF-REG lo ripete identico:

| | Parte A (WF-TSR) | Parte B (WF-INT) | Parte C (WF-REG) |
|---|---|---|---|
| Tabella delle fasi | ✅ `07:85` | ✅ `07:162` | ❌ **assente** |
| Colonna Agente | ✅ | ✅ | ❌ |
| Colonna Output | ✅ `07:85` | ❌ **assente** | ❌ |
| Colonna Ore | ✅ | ✅ | ❌ |
| Agenti del reparto nominati | ✅ | ✅ | ❌ **zero**: `lan-reg-conductor`, `-calendarista`, `-tracciatore`, `-prova-a-secco` (`08:130`) **non compaiono una sola volta** in tutto il dossier 07 |

La Parte C ha un calendario (C.1), un grafo (C.2), una lista (C.3), tre esiti (C.4), una tabella di
diagnosi (C.5) e un debrief (C.6): **sei sezioni e nessuno che le esegua.** E LAN-REG è il reparto che
possiede l'apertura della vendita, cioè l'atto per cui l'intero ecosistema esiste.

**Il caso concreto.** `09:102` mette `LAN-REG` nello scaglione minimo. Gael apre il dossier 07 per
sapere cosa deve costruire e trova prosa: non sa quali fasi, quali output tipizzati, quale agente
esegue cosa, quante ore. Costruisce a intuito, e ciò che nasce non ha un contratto con nessuno.

**La riparazione.** Riscrivere `07 Parte C` con la stessa tabella della Parte A: `# | Fase | Cosa fa |
Agente | Output | Ore | Umano`, con almeno R1 generazione del calendario (`calendario.py` →
`calendario.md` + `calendario.json`), R2 sequenza pre-lancio, R3 prova a secco (`lancio.py --dry-run`
→ `dry-run.md`), R4 sincronizzazione (`GATE-REG-1` → verbale), R5 apertura (**umano**), R6
tracciamento giornaliero (`tracking.py` → `tracking/<data>.json`), R7 chiusura (**umano**).
**E la colonna Output va aggiunta anche alla Parte B (`07:162`)**, che oggi ne è priva: otto fasi di
Intelligence senza un solo artefatto tipizzato dichiarato.

---

### D-C-07 · GATE-TSR-2 è indefinito per la maggior parte del lancio — il gate "riparato" continua a non poter bloccare

**Dove:** `07:130` (`scarto_pct = (speso − previsto_a_oggi) / previsto_a_oggi × 100`), `07:102`
(criterio del gate), `07:74-79` (i profili di spesa), `07:66-69` (la dichiarazione di aver risolto).

**Perché si rompe.** `07:69` afferma: *"Il gate o divideva per zero o dava sempre un numero negativo:
**non poteva bloccare mai**"*, e presenta i profili di spesa come la correzione. **La correzione non
elimina lo zero.** Con i profili di `07:74-79`:
- `unico` → `previsto_a_oggi = 0` finché la data d'inizio non è passata;
- `posticipato` → `max(0, (g − tot×0,6)/(tot×0,4))` = **esattamente 0 per il primo 60% della voce**.

Il profilo `posticipato` è il **normale** per la pubblicità di un lancio (si spinge vicino
all'apertura). Sull'esempio di `07:54-59` — voce pubblicità dal 10 al 19 ottobre — `previsto_a_oggi`
vale 0 per sei giorni su dieci. Nella finestra T-30/T-20 quasi tutte le voci danno 0: la somma è 0, e
la formula è **indefinita**, non "piccola".

**Il caso concreto.** Si spendono 300 € di test annunci il 12 ottobre, tre giorni prima della finestra
prevista. `previsto_a_oggi = 0`. Il gate divide per zero: se lo script è difensivo, salta il controllo
e passa; se non lo è, esplode e il comando *"sembra rotto"*. Lo sforamento del 100% del budget nella
fase iniziale — la più tipica — **non è rilevabile**. Il gate che il dossier presenta come riparato
resta incapace di bloccare esattamente nel periodo in cui i soldi si bruciano per errore.

**La riparazione.** Criterio doppio, assoluto e relativo, con lo zero gestito esplicitamente:
```
soglia_assoluta = max(50, 0,10 × budget_massimo)
BLOCCA se  speso > previsto_a_oggi + soglia_assoluta
       oppure (previsto_a_oggi == 0 e speso > 0)   → "spesa fuori finestra", si blocca e si dichiara
scarto_pct si scrive solo quando previsto_a_oggi > 0; altrimenti il campo vale "non calcolabile"
```
— cioè la stessa disciplina che `07:125-126` applica già, bene, al costo di acquisizione.

---

### D-C-08 · Dossier 09 è fermo a una versione precedente e contraddice 01, 08 e 10

**Dove:** `09:1` (*"seconda versione"*) contro `07:10`, `08:10` (*"Terza versione"*).

| Punto | Dossier 09 | Il resto del piano |
|---|---|---|
| Agenti dello scaglione minimo | **9** (`09:40`, `09:104`) | **11** (`01:393-407`, `08:139`, `10:186`) |
| Reparti dello scaglione minimo | **4**: STR, OFF, FNL, REG (`09:98-102`) | **8** distinti nella tabella di `01:396-407`: Direzione, Strategia, Intelligence, Prodotto, Offerta, Funnel, Regia, Qualità |
| `lan-segretario` | incluso (`09:104`) | **soppresso** (`01:409`: *"è uscito: lo stato lo tiene `stato_lancio.py`"*) |
| *"motore dei gate"* fra i nove agenti (`09:106`) | è un agente | è `scripts/gate.py`, uno script (`09:64`) |

**Perché si rompe.** `09:11` e `09:51` fanno del contenuto di S1 un **vincolo tecnico**: *"il registro
rifiuta gli agenti dei reparti non abilitati"*. Se il registro viene configurato con i 4 reparti di
`09:98-102`, **rifiuterà 5 degli 11 agenti minimi** (int-analista, prd-collaudatore, direttore,
qlt-gate e il conductor dell'Offerta appartengono a reparti non elencati). Il vincolo che protegge il
piano lo sabota.

**Il caso concreto.** Gael segue il dossier 09 — che `00:165` gli indica come *"prima di cominciare"* —
costruisce nove agenti fra cui `lan-segretario`, che non esiste più, e non costruisce
`lan-off-conductor`, **l'unico che scrive `offerta.json`** (`01:401`). Il lancio si ferma in
`ISTRUITO` per sempre: il difetto numero 1 di `10:186`, riesumato dal dossier che avrebbe dovuto
recepirne la correzione.

**La riparazione.** Riscrivere `09 §4` sui **numeri di `01:393-407`** (11 agenti, 8 reparti, senza
segretario, con `gate.py` come script e non come agente) e, in cima, portare il dossier 09 a "terza
versione" con l'elenco di cosa ha recepito. Nel frattempo: nessuno costruisca da 09.

**Rilievo di metodo:** questo difetto era invisibile leggendo un dossier alla volta. Prima della
riscrittura serve una **matrice di coerenza** — conteggi di agenti, reparti, gate, skill, comandi,
ore — con una sola cella autorevole per grandezza.

---

### D-C-09 · `registro.py` e "reparto abilitato": il vincolo portante non è definito da nessuna parte

**Dove:** `08:218`, `08:225-232`, `09:11`, `09:51`, `09:232`, `10:56`.

**Perché si rompe.** Quattro punti del piano — fra cui il punto 6 della **decisione dell'ADR**
(`10:56`) — poggiano su *"il registro rifiuta gli agenti dei reparti non abilitati"*. Cercando
"abilitat" in tutto il dossier si trovano **quattro occorrenze, tutte d'uso e nessuna di definizione**.
Non è scritto:
- in quale **file** vive l'elenco dei reparti abilitati, con quale formato;
- **chi** lo modifica e con quale autorità;
- come la modifica si lega alla chiusura di uno scaglione (chi abilita S2, contro quale prova);
- **cosa succede alla specifica** di un agente rifiutato (resta orfana? viola il controllo #1 di
  `08:227`, che rifiuta le specifiche senza agente?).

E `08:232` rimanda a **`dossier 01 §2`** per la nozione di reparto abilitato: quella sezione
(`01:118-134`) elenca i dodici reparti e **non contiene alcun concetto di abilitazione**. Puntatore
rotto su una regola bloccante.

Aggravante: `registro.py` non ha ore in nessuno scaglione (§2.5) e non ha una specifica. Il piano
descrive in dettaglio i suoi quattro controlli (`08:227-232`) e non pianifica mai di scriverlo.

**La riparazione.** `15-LANCI/REGISTRO.md` acquisisce un blocco YAML normativo:
```yaml
reparti_abilitati:
  - sigla: LAN-STR
    abilitato_il: 2026-09-20
    abilitato_da: Gael
    prova: "tests/chiusura_S0.py exit 0"
```
`registro.py` legge quel blocco; lo scaglione lo scrive solo dopo l'exit 0 del proprio test di
chiusura (§2.6). E `registro.py` entra in **S0.9, 4 ore**, prima di qualunque agente.

---

### D-C-10 · Un solo `lan-qlt-gate`, su haiku e in sola lettura, per tredici gate diversi

**Dove:** `08:131` (Qualità: 4 agenti) · `00:277-289` (13 gate) · `08:147-155` (frontmatter: `model:
haiku`) · `08:87` (principio 1: *"un agente = un mestiere"*).

**Perché si rompe.** Tre difetti in uno:
1. **Contro il principio 1**: un agente che esegue tredici criteri diversi fa tredici mestieri. Quando
   sbaglia non si sa quale.
2. **Aritmetica su denaro affidata a un modello leggero**: GATE-TSR-1 richiede
   `totale_previsto ≤ budget_massimo` (`07:101`) e GATE-TSR-2 lo scarto percentuale (`07:102`). Far
   calcolare a `haiku` la somma di venti importi in virgola mobile per decidere se bloccare un
   budget è la scelta sbagliata a **qualunque** costo: non è una questione di prezzo, è che un modello
   linguistico non è un sommatore.
3. **Contro il principio 6** (`08:92`, *"ogni fatto si ricalcola dai file"*): con `Read, Grep, Glob` e
   senza `Bash`, il ricalcolo è a occhio sul testo letto.

**La riparazione.** Separare nettamente:
- **gate calcolabili** (11 dei 13): li esegue `gate.py`, leggendo `qualita/criteri/<GATE>.yaml`,
  con exit code e verbale. Zero agenti, zero costo, riproducibili;
- **gate di giudizio**: solo la parte non calcolabile di `GATE-CPY-1` (che `09:176` già distingue:
  *"la parte calcolabile del punteggio dei testi"* vs *"il giudizio sulla parte non calcolabile"*) e
  la verifica a campione di `GATE-INT-1` (`07:183`), che richiede di leggere una pagina e cercarci una
  frase. Due agenti, su `sonnet`, non su `haiku`.

Corollario: `lan-qlt-gate-costi` sparisce (§1.4) e `LAN-QLT` passa da 4 agenti a 2.

---

### D-C-11 · Tredici gate dichiarati, quattordici esistenti

**Dove:** `07:103` introduce **`GATE-TSR-3`** (riconciliazione col consuntivo) con tanto di criterio,
esecutore e sblocco. `00:270-289` intitola *"I tredici gate — numerazione unica"* e ne elenca
tredici, **senza TSR-3**. `10:51` decide *"tredici gate bloccanti, con numerazione unica"*.
`10:141` costruisce sul numero: *"se il pilota attraversa tredici gate…"*.

**Perché si rompe.** La *"numerazione unica"* è presentata (`00:272`) come la correzione di un difetto
del primo giro (*"c'erano tre serie di sigle diverse nei tre documenti"*). La correzione è già
scaduta: esiste un gate fuori elenco, con un criterio operativo, in un documento di terza versione.
Chi implementa `gate.py` leggendo `00:270-289` non lo implementerà, e la riconciliazione con la
Tesoreria — punto 7 del flusso Tesoro (`07:95`) — non avrà controllo.

**Aggravante sul contenuto di TSR-3.** Il criterio è *"i totali coincidono con la Tesoreria entro
l'1% — **oppure la Tesoreria è vuota, e allora lo si dichiara**"* (`07:103`). Poiché `07:37` accerta
che i registri dell'Impero sono **oggi a zero righe**, sul lancio pilota TSR-3 **non può fallire**:
esce sempre dal ramo "dichiara il primo popolamento". È un gate onesto e inerte, e va detto — perché
`10:139` stabilisce che un sistema di gate che non ha mai bloccato non è provato.

**La riparazione.** Portare l'elenco a **14**, aggiornare `10:51` e `10:141`, e marcare TSR-3 come
`non-bloccante-al-primo-lancio` con la data in cui diventa bloccante (il secondo lancio), così che
non resti inerte per abitudine.

---

### D-C-12 · Nessuna osservabilità: non c'è modo di sapere cosa sta facendo il sistema mentre gira

**Dove:** l'assenza è totale. In `07`, `08`, `09`, `10` la parola *log* non compare mai; *trace*,
*tracciamento di esecuzione*, *osservabilità*, *telemetria* mai; *cruscotto* compare tre volte
(`02:227`, `07:344`, `07:345`) e **sempre riferito ai numeri di vendita**, mai allo stato del sistema.

**Perché si rompe.** Il sistema è composto da 50 agenti, 13 gate, 12 spazi di memoria, 17 script e una
macchina a 12 stati, distribuiti su 38 giorni. Le uniche superfici di osservazione previste sono
`lancio stato` (`09:68`, di cui non è specificato cosa stampi) e i verbali dei gate. Non esiste:
- un **registro degli eventi** (transizione, gate eseguito, handoff accettato/respinto, agente
  invocato) con orario ed esito;
- un **identificativo di correlazione** che leghi le esecuzioni di un lancio;
- una misura di **durata e consumo per invocazione**, che è anche l'unico modo di trasformare le
  stime di `08:283-303` in dati (`08:302` lo promette — *"al primo lancio si registra il numero di
  chiamate per agente e classe"* — senza dire **dove** si registra, né chi scrive quella riga);
- una diagnosi dello stato: perché il lancio è fermo, da quanto, in attesa di chi.

**Il caso concreto.** Al giorno T-9 il lancio è ancora `IN_PRODUZIONE`. Nessuno sa se un gate ha
bloccato, se un agente è morto a metà, o se semplicemente nessuno ha eseguito il comando. `09:231`
diagnostica la morte della memoria con *"l'indice non cambia da giorni"*, che è un sintomo osservato a
mano, non uno strumento.

**La riparazione.** In S0, accanto agli otto punti esistenti:
- `S0.9` — **`lanci/<id>/log/eventi.jsonl`**, una riga per evento
  `{ts, lancio_id, evento, attore, artefatto, esito, exit_code, durata_s, modello, chiamate}`, scritta
  da `lancio.py`, `gate.py`, `handoff.py`, `sentinelle.py`. **3 ore.**
- `S0.10` — `lancio stato --dettaglio` (ultimi eventi, gate superati/bloccati, chi è atteso e da
  quanto) e `lancio doctor` (**ricalcola lo stato dai file** e lo confronta con `stato.json`,
  segnalando la divergenza — cioè il principio 6 di `08:92` reso eseguibile, contro il modello di
  fallimento che `00:347-349` dichiara **il più probabile**). **3 ore.**

Il campo `chiamate`/`modello` nella riga di evento è anche ciò che rende misurabile D-C-13.

---

### D-C-13 · Il costo di esercizio del sistema non è né stimato né limitato — e il gate del budget non lo copre

**Dove:** `08:283-303` (il costo, dichiarato non misurabile) · `07:47-63` (lo schema del budget) ·
`07:101` (GATE-TSR-1).

**Perché si rompe.** `08:285-286` è onesto — *"nessun lancio è mai stato eseguito, quindi non esiste
un dato"* — ma l'onestà non è sufficiente per decidere di costruire. Manca il minimo che **si può**
calcolare senza aver mai eseguito nulla: **il numero di invocazioni per lancio**. È aritmetica sui
documenti stessi: 11 pezzi di copy × 1-2 giri (`08:290`), 8 fasi di Intelligence (`07:164-172`), 13-14
gate, 7 fasi di Tesoro, N giorni di tracciamento × 38. Si arriva a un ordine di grandezza per classe
di modello, e da lì a un tetto.

**Il difetto strutturale, però, è un altro:** `budget_massimo` in `07:48-52` copre **solo la spesa
esterna** (pubblicità, commissioni, rimborsi). Il costo di far girare cinquanta agenti non ha una
voce, non passa per GATE-TSR-1, non entra nel `consuntivo.md` (`07:94`), non sale in Tesoreria
(`07:95`) e non compare nel `margine` (`07:129`). **L'ecosistema che nasce per sapere quanto costa un
lancio non conta quanto costa sé stesso**, e il margine che dichiara è per costruzione sbagliato per
eccesso.

**La riparazione.**
1. Voce obbligatoria in `budget.json`: `{"voce": "costo-sistema", "profilo_spesa": "lineare", ...}`,
   dentro il tetto e dentro GATE-TSR-1;
2. `costi.py` la alimenta dagli eventi di D-C-12 (`chiamate` × tariffa per classe di modello,
   tariffario in un file, non nel codice);
3. `margine` (`07:129`) diventa `ricavo_totale_netto − costo_totale_reale − costo_sistema`;
4. In dossier 08 §10, sostituire i tre aggettivi (*dominante / medio / trascurabile*) con **il conteggio
   delle invocazioni per fase**, che è calcolabile oggi, e con un tetto per lancio.

---

### D-C-14 · L'ADR descrive invece di decidere, e decide una cosa che non può decidere

**Dove:** `10:42-59` (la Decisione) · `10:84` (le conseguenze).

**Perché si rompe.** Degli otto punti della decisione, **due sono vere decisioni** e sei sono riassunti
del piano:

| Punto | Riga | Decide o descrive? |
|---|---|---|
| 1 — nasce `15-LANCI`, numero 15 riservato nello stesso commit | `10:44-45` | ✅ **decide**, ed è irreversibile |
| 4 — `IB-L2-LANC` si sposta | `10:50` | ✅ decide — **ma senza averne l'autorità** (sotto) |
| 2 — dodici reparti | `10:46` | descrive `01:118-134` |
| 3 — sette flussi | `10:48` | descrive |
| 5 — tredici gate | `10:51` | descrive `00:270-289`, **e con il numero sbagliato** (D-C-11) |
| 6 — costruzione a scaglioni | `10:54` | descrive `09` |
| 7 — ogni agente nasce ufficiale | `10:57` | descrive `08:197-212` |
| 8 — tre condizioni di abbandono | `10:59` | descrive, **e rimanda a "dossier 00 §6"** mentre le condizioni operative stanno in `09:206-219` |

Un ADR che riassume i dossier non vincola nulla: fra sei mesi, chi vuole cambiare il numero dei
reparti non sta contraddicendo una decisione, sta aggiornando una descrizione.

**Il punto 4 è peggio che descrittivo: è ultra vires.** `10:84` ammette *"sposta un reparto di un
altro ecosistema: **serve il consenso del suo proprietario**"* — consenso che l'ADR non ha, non
richiede e il cui titolare non è nemmeno nominato. Una decisione registrata che dispone di un asset
altrui è la ricetta del conflitto fra reparti che il piano dichiara di voler prevenire.

**Cosa l'ADR dovrebbe decidere e non decide** (sono le scelte irreversibili vere, quelle che un
lettore fra un anno vorrà ritrovare):
- la **convenzione di denominazione** degli agenti — cioè il punto su cui il piano si contraddice già
  (§1.3);
- il **profilo di strumenti per ruolo** come norma vincolante, con il punto di applicazione
  (`registro.py` + `settings.json`): è la scelta architetturale portante di `08:36-63`, e nell'ADR
  compare come inciso in coda al punto 7;
- **dove si accerta l'ufficialità** — che l'ecosistema si porta il proprio verificatore invece di usare
  gli strumenti dell'Impero (`08:33`) è una deviazione da uno standard di casa: è esattamente ciò che
  un ADR serve a registrare, e non c'è;
- il **contratto d'uscita macchina-leggibile** (D-C-05);
- cosa **decade** se scattano le condizioni di abbandono: l'ADR non ha clausola di superamento, e
  resterebbe "in vigore" a governare un ecosistema abbandonato.

**La riparazione.** Riscrivere la sezione Decisione con 5-6 punti che **vincolano** (numero, nomi,
strumenti, contratti, verificatore, clausola di superamento), spostare i sei descrittivi in un
"Contesto" o in un semplice rimando ai dossier, e subordinare il punto 4 a un consenso scritto e
nominato.

---

_(sezioni 4-8 in lavorazione)_
