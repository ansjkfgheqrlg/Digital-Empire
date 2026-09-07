# 🜂 V2 — PIANO AMPLIATO PER RENDERE VIVA DIGITAL EMPIRE

> **Versione:** 2 di 4 · **Data:** 2026-09-07 · **Autore:** EMPERATOR · **Committente:** Max
> **Stato:** DA CRITICARE (critica 2) — non esecutivo, ma già assegnabile
> **Leggi vincolanti:** le sette leggi di [`00-LEGGIMI.md`](00-LEGGIMI.md) §2 **più tre nuove** (§2 di questo documento)
> **Ripresa:** EMP-MCC4
>
> **V2 non è V1 corretta.** È un altro piano, scritto a partire dai **dieci rilievi FATALI** della
> critica 1 e dalle **3.078 righe di censimento** che V1 non aveva mai letto. Dove V1 regge, V2 lo
> dice e lo tiene identico (§0.1). Dove V1 cade, V2 non la ritocca: cambia impianto.

---

# PARTE 0 — COSA CAMBIA, E SU COSA POGGIA

## 0.1 Le cinque inversioni di V2

| # | V1 diceva | V2 dice | Rilievo che l'ha imposto |
|---|---|---|---|
| 1 | **NEXUS**, sedicesimo ecosistema, 5 organi da costruire (25-40 h) | **Cinque funzioni innestate** su organi già vivi. Nessun ecosistema nuovo, nessun numero 16 | C1 R-5, R-6, R-7, R-10, R-11 + sintesi |
| 2 | Un organo vive perché **ha un proprietario** | Un organo vive perché **ha un consumatore quotidiano già esistente**. È la legge centrale di V2 | C1 R-13 [FATALE] |
| 3 | La fetta verticale si costruisce **riaprendo `empire flow`** sui concessionari | La fetta verticale **strumenta Preventa**, che i concessionari li contatta davvero da agosto | C3 R-16 [FATALE] |
| 4 | Il denaro = **2 Payment Link** in E0 | Il denaro = **mettere fuori la merce**: 30 pezzi fermi, 26 caricabili oggi, 6 libri finiti. Gate del piano espresso in pezzi pubblicati ed euro | C2 R-1, C3 R-5, R-9 [FATALI] |
| 5 | Il ponte agenti va in **una direzione** (scheda → esecutore) | **Due direzioni**, con anagrafe unica dei nomi e adozione dei 162 esecutori orfani | C1 R-9, C3 R-14 [FATALI] |

**E una sesta, di metodo:** V1 metteva i controlli (hook) dentro E4, cioè **dopo** gli scaglioni di
massa che dovevano proteggere. V2 li mette **prima di tutto il lavoro di massa** (E0.7), perché
sono configurazione, non costruzione: mezza-una giornata, e da lì in poi ogni scaglione lavora
sorvegliato. *(C2 R-12 e R-17, trovato da due revisori separatamente.)*

## 0.2 Cosa di V1 resta identico, e non si tocca

1. **Il principio di §11** — *ogni collegamento è sottoprodotto di un'operazione, o un hook che
   blocca*. È l'unica cura che in questo Impero abbia mai funzionato: `ERR-20260905-001` →
   `gate_battito_hook.py`, dieci righe agganciate a un evento, test 6/6, in vigore.
2. **Un contratto solo e una traccia sola** (V1 §9-10). V2 estende: non 3 formati → 1, ma **10
   schemi → 1** (`02d` §C.1).
3. **«Si avvolge, non si riscrive»** (L4 / ADR-003). V2 la applica anche agli organi del piano,
   che è esattamente ciò che V1 non faceva.
4. **Il divieto di §12.2**: chi collega non produce lavoro di reparto. Resta, come divieto.
5. **§18 — produzione sequenziale, ricognizione parallela con scrittura incrementale.** Pagata con
   9/9 contro 1/4 e con le 8.120 righe salvate.
6. **§23 — la Tesoreria è una riga, non uno scaglione.** Corretta è la lettura; sbagliato era
   farla dipendere da un ledger nuovo (§9 di questo piano).
7. **§26 — i gate di fallimento scritti prima di costruire.** V2 li tiene e aggiunge **la data** e
   il **divieto di backfill**.

## 0.3 Le fonti — riaperte, e questa volta complete

`dati/` contiene **8.120 righe**, non 5.042. V1 ne aveva lette 5.042: i cinque censimenti chiusi
**dopo** le 19:23 del 6 settembre non sono mai entrati nel suo testo, e sono proprio quelli che ne
ribaltano l'ordine.

| Censimento | Righe | Cosa impone a V2 |
|---|---|---|
| `censimento-01a-ecosistemi.md` | 1.256 | i 15 ecosistemi scheda per scheda; APEX-7 isolato; la collisione 08/12 |
| `censimento-01b-organi.md` | 1.096 | i 14 organi di governo |
| **`censimento-01c-sintesi-organi.md`** | **468** | **7 organi che nessuno chiama · 0/5 sentinelle autonome · l'Ispettorato mantenuto a backfill · i gate che confermano il falso** |
| `censimento-02-collegamenti.md` | 363 | il Bus a 3 file · `done_step()` con un chiamante solo |
| `censimento-02b-mappa-collegamenti.md` | 619 | la mappa completa dei passaggi |
| **`censimento-02d-sintesi-collegamenti.md`** | **622** | **328 passaggi · 21 con contratto · 0 INTER mai avvenuti · 10 schemi · i 10 collegamenti da accendere per primi** |
| `censimento-03a-popolazione.md` | 1.426 | 439 schede · 164 esecutori · intersezione 2 · le 5 ondate · il guasto di `census.py` |
| `censimento-03b-regolamento-forze.md` | 113 | la gerarchia ADR-015 |
| `censimento-03b2-cadute.md` | 384 | 33 cadute → 29 regole, 12 da rendere meccaniche |
| **`censimento-03c-addestramento.md`** | **1.064** | **il minimo comune (10 righe) e il modulo d'ingaggio in 3 varianti: già progettati. V1 li dava per non fatti** |
| `censimento-04-motori.md` | 81 | la famiglia Outreach |
| **`censimento-04b-motori.md`** | **613** | **25 motori: 9 vivi, 3 rotti dallo stesso guasto, 8 orfani · due involucri già vivi · il ritorno più alto per il minor lavoro** |
| `censimento-01-vivo.md` · `03-forze.md` | 3+3 | indici |

> **Regola che V1 ha violato senza saperlo:** un piano non si scrive mentre i censimenti stanno
> ancora arrivando. V2 nasce a censimenti chiusi e fermi da 12 ore.

## 0.4 La baseline, rimisurata stamattina (2026-09-07, comandi in sola lettura)

| Misura | Comando | Valore oggi |
|---|---|---|
| Agenti operativi | `python -m empire forge scan` | **439 analizzati · OPERATIVO 61 (13,9%) · PARZIALE 324 · DOCUMENTALE 54** |
| Criterio più assente | idem | **C4-uscita assente in 314 (71,5%)** · C5 135 · C6 69 · C1 60 · C3 42 · C2 16 |
| Workflow pronti | `python -m empire controllo` | **2/6** — e le mani di Max: Payment Link, login IG (sessione di 94 gg), login LinkedIn (111 gg), l'`.mp4` che manca |
| Tracce | `python -m empire trace stato` | **25** (6 decisioni · 6 errori · 7 prestazioni · 4 lezioni · 2 sessioni) |
| Denaro registrato | `ls -la company/Memory/tesoreria/` | **`entrate.jsonl` 0 byte · `spese.jsonl` 0 byte**, dal 3 settembre |
| Magazzino fermo | `python scripts/ultimo_metro.py` | **30 pezzi finiti mai usciti · 3.067 MB · 26 caricabili subito · il più vecchio da 139 giorni** |
| Libri finiti | `ls .../libri-performanti-multiagente/LIBRI/libri_pronti/` | **6** (V1 diceva 4) |
| Radice del repo | `ls SYNC-CONFLICT.txt` | **pulita** (il conflitto del 6/9 è stato risolto) |
| Scanner segreti | `ls .githooks/` | `check_blob.py`, `check_memory.py`, `installa.py`, `pre-commit` — **nessuno scanner di segreti** |

**Il numero che conta più di tutti:** il magazzino è **cresciuto** mentre scrivevamo il piano —
da 25 pezzi a 30, dal 5 al 7 settembre. L'Impero continua a produrre roba che non esce.

---

# PARTE I — LE LEGGI

## 1. LA LEGGE CENTRALE DI V2 — IL CONSUMATORE QUOTIDIANO (LC)

> **Nessun organo, funzione, hook o registro si costruisce se non ha scritto accanto QUALE
> CONSUMO QUOTIDIANO GIÀ ESISTENTE lo tiene in vista — con il nome del consumatore, la cadenza, e
> il gate che fallisce se la sua uscita ha più di 24 ore.**

**Perché è la legge centrale, e non una raccomandazione.** L'esperimento «basta un proprietario» è
già stato fatto in casa, e ha fallito. L'**Ispettorato** è l'organo più simile a ciò che il piano
vuole costruire: proprietario vero (è l'organo personale di Max), comando reale
(`python -m empire inspect`), 30 test verdi, 204 file. Risultato misurato: **87 rapporti e 87
telemetrie generati tutti da un solo `backfill`, ultimo giorno coperto il 2026-07-24, 44 giorni
scoperti** — contro una regola che ne pretende uno dopo ogni run.

Un organo senza consumo quotidiano non viene abbandonato: viene **backfillato** quando serve
esibirlo. Che è peggio, perché i suoi numeri sembrano vivi.

Il campione completo dice la stessa cosa da sette direzioni: **7 organi di governo che nessuno
chiama in alcun modo** · **0 sentinelle su 5 si attivano da sole** · l'organo più controllato
(01-agency, ~30 check tutti PASS) ha il suo comando di scrittura *che nessuno chiama*.

E l'unica eccezione vivente conferma la legge al contrario: `gate_battito_hook.py` non sta in
piedi perché ha un proprietario. Sta in piedi perché **il suo prodotto ha un consumatore ogni
pochi minuti** — il battito che Max legge. Se si spegne, qualcuno se ne accorge entro un'ora.

**Corollari operativi, vincolanti:**

- **LC-1** — La scheda di nascita di ogni pezzo di V2 ha una riga obbligatoria: `Consumatore
  quotidiano: <chi> · <ogni quando> · <cosa succede se manca>`. Senza quella riga, il pezzo non
  si costruisce. Non «si costruisce e poi vediamo»: **non si costruisce**.
- **LC-2** — I quattro consumi quotidiani già esistenti su cui si innesta tutto:
  1. **il battito di EMPERATOR** (Max lo legge decine di volte al giorno — hook `Stop` già attivo);
  2. **l'apertura di sessione** (`emperator_boot.py` + `empire/avvia.py`, girano ogni volta);
  3. **il commit** (`.githooks/pre-commit` + il daemon di sync che committa ogni 2-12 minuti);
  4. **il checkpoint di chiusura task** (`scripts/checkpoint.py`, girato 303 volte).
  Un quinto consumo non si inventa: se un pezzo non si aggancia a uno di questi quattro, va
  dichiarato «senza consumatore» e messo in fondo, non davanti.
- **LC-3 — DIVIETO DI BACKFILL sulle telemetrie che alimentano un gate.** Ogni riga di telemetria
  generata a posteriori porta `backfilled: true`, e ogni gate che la legge la **scarta**. È una
  riga di codice; senza, i gate di §26 leggono numeri rimessi a nuovo la mattina del controllo.

## 2. LE TRE LEGGI NUOVE (L8, L9, L10)

Le sette leggi di `00-LEGGIMI.md` §2 restano tutte. Se ne aggiungono tre, ognuna pagata da un
rilievo.

**L8 — ARCHIVIO è uno stato, non una scusa.**
La tassonomia ha **tre** stati, non due: `VIVO` · `DESCRITTO` · `ARCHIVIO`. Un pezzo in ARCHIVIO
ha: (a) una ragione scritta, (b) un puntatore dall'anagrafe, (c) **l'esclusione dichiarata dal
denominatore del 100%**. Serve perché il piano stesso fabbrica archivio (le 36 copie perdenti,
`08-STREAM-S7-BOT`, i due sistemi che i loro documenti vietano di mettere in produzione), e senza
questo stato «senza eliminare niente» e «100% vivo» si contraddicono a vicenda.
*(C1 R-2.)*

**L9 — Un gate è un comando, una condizione di fallimento e un exit code.**
Non un evento da osservare. «Una traccia nasce da sola», «l'uscita finisce dove il contratto
dice», «EMPEROR ordina → un direttore esegue» **non sono gate**: sono descrizioni. Se il comando
non esiste ancora, il gate si scrive come **specifica del comando che dovrà esistere** (nome,
argomenti, condizione di fallimento) e **quella specifica è lavoro dello scaglione stesso**.
Nessuno scaglione di V2 esce senza riga Gate in questa forma.
*(C2 R-7, R-18, R-20 — e L5 che V1 violava nei suoi due scaglioni più costosi.)*

**L10 — Ogni numero cardinale porta i nomi o il puntatore esatto.**
«I 5 ecosistemi che puntano a reparti inesistenti», «i ~10 agenti che tocca», «i 4 libri»: numeri
senza elenco. Uno di questi (`grep "reparti inesistenti"` su tutti i 14 censimenti → **0
risultati**) non è ricostruibile da nessuno che non sia l'autore. In V2 ogni cardinale ha accanto
l'elenco o `file:sezione`. Il segno `~` davanti a un numero che decide un perimetro è vietato.
*(C2 R-16.)*

## 3. LA FORMULA DEL 100% — scritta come comando

V1 non aveva un denominatore: nessun comando poteva stampare «100% raggiunto». V2 lo definisce
prima di partire, perché è il gate finale del piano intero.

```
DENOMINATORE = nodi_censiti − nodi_in_ARCHIVIO
NUMERATORE   = nodi che passano (V-a..V-d) ∧ (C-a..C-d)   [+ R-a per la classe dei reattivi]
100% VIVO E COLLEGATO = NUMERATORE / DENOMINATORE = 1
```

- **`nodi_censiti`** = i 15 ecosistemi + i 25 motori censiti in `04b` + i 14 organi di governo di
  `01b`. Elenco nominale: `dati/censimento-01a`, `04b` §tabella, `01b` §tabella. **Nessun agente
  singolo entra nel denominatore**: gli agenti si misurano con `forge scan` (percentuale propria).
- **`nodi_in_ARCHIVIO`** = decisi uno per uno con ragione scritta (L8), oggi candidati: le 36
  copie perdenti dei duplicati, `08-STREAM-S7-BOT` come archivio d'origine, i due sistemi
  auto-vietati (decisione di Max, §26).
- **Il comando che lo calcola** — `python -m empire vivo --json` — **non esiste**: è il primo
  deliverable di E0.5, e legge lo stato dei nodi dal registro, non dalla memoria di chi lo lancia.

**Baseline onesta, dichiarata:** per la legge L3, oggi i nodi chiusi sono **0 su 15**, non 2 su 15.
`11-APEX-7` e `12-STREAM-S7` passano V-a..V-d ma falliscono C-a..C-c. E APEX-7 non è
semplicemente scollegato: **è progettato per non collegarsi** — il suo Event Bus dichiara
*«Publisher NON SA chi riceve. Subscriber NON SA chi ha inviato → zero coupling»*, ed è l'unico
schema dell'Impero **senza campo `from` e senza campo `to`**. In un piano sull'indirizzamento,
V1 lo esibiva come modello: era l'anti-modello.
*(C1 R-1 [FATALE].)*

## 4. LE DEFINIZIONI CORRETTE

### 4.1 VIVO — invariata (V-a..V-d)

| | Condizione | Come si prova |
|---|---|---|
| V-a | si invoca con un comando dichiarato | il comando esiste ed esce 0 |
| V-b | produce un'uscita conforme a un contratto scritto | l'uscita valida contro lo schema |
| V-c | l'uscita finisce in un posto stabilito | il percorso è dichiarato e il file c'è |
| V-d | un test lo prova, ed è rilanciabile | il test esiste ed è verde |

### 4.2 COLLEGATO — riscritta, con una condizione in più

| | Condizione | Come si prova | Perché è cambiata |
|---|---|---|---|
| C-a | un ingresso dichiarato | il contratto in ingresso esiste | invariata |
| C-b | un'uscita dichiarata verso un destinatario **che esiste come casella** | il contratto nomina il destinatario **e la sua cartella/coda esiste su disco** | `company/metrics/`, `company/runtime/`, `marketing/handoffs/log` sono destinazioni **mai create**: un contratto verso il vuoto passava C-b in V1 |
| C-c | la traccia nasce da sola **nel formato unico e nel registro dell'Impero** | `trace stato --origine hook` la vede | senza «formato unico e registro», qualunque motore con un log privato passava: i due `decision_log.db` di APEX-7 sono tracce automatiche, e rendevano C-c un'opinione |
| **C-d** | **ha servito un consumatore reale almeno una volta** | esiste il fatto: il file consegnato, il lead passato di stato, l'euro incassato | **nuova.** Era già scritta nel regolamento di V1 §17 (*«un agente è consegnato quando ha servito un consumatore reale, non quando esiste»*) e non era mai entrata nelle definizioni che governano i gate |

### 4.3 R-a — la condizione di classe per i reattivi

Sentinelle, guardiani, gate, hook: **la proprietà essenziale della loro classe è scattare da soli
sull'evento sorvegliato.** Nessuna delle sette condizioni la misura — e infatti 5 sentinelle su 5
sono invocabili, non-stub, da 319 a 376 righe l'una, e **0 su 5 si attivano da sole**.

> **R-a — Un artefatto reattivo è vivo solo se si attiva senza invocazione umana, e se esiste il
> test che lo dimostra** (un evento finto → l'artefatto scatta → l'esito è verificabile).

Vale per tutto ciò che V2 costruisce in E0.7 e in E4-N5. Un guardiano che va invocato a mano è un
guardiano morto, anche se il suo codice è perfetto.
*(C1 R-4.)*

---

# PARTE II — LA DIAGNOSI CORRETTA

## 5. Non una malattia: quattro, e V1 ne curava una

V1 diceva: *«ogni atto di collegamento è un atto separato e volontario, e gli atti separati non si
fanno»*. È vero per le tracce (25 in tutta la vita). **Non spiega le altre tre cause misurate**, e
un hook montato sopra di esse non le cura — le fa esplodere.

| # | Causa | Prova misurata | Cura in V2 | Dove |
|---|---|---|---|---|
| 1 | **Volontarietà** — l'atto c'è ma nessuno lo fa | `done_step()` ha **1 solo chiamante** (`empire/flow/cli.py:115`), 0 fuori · 25 tracce in tutta la vita | sottoprodotto o hook che blocca (principio V1 §11, invariato) | E0.7, E3, E4-N3 |
| 2 | **La casella del destinatario non esiste** | `company/runtime/` → `No such file or directory`, ed è deliverable dichiarato di **5 Guild e 5 Sentinelle** · `company/metrics/`, `marketing/handoffs/log`, `platform/handoffs/log`, `Memory/pubblicati.json`: mai creati | **creazione esplicita delle caselle, elencate per nome, PRIMA di ogni hook che le pretende** | E0.5 |
| 3 | **Dieci schemi incompatibili** | `02d` §C.1: *«dieci schemi di comunicazione diversi, nessun validatore e nessun registro dei contratti»* · V1 ne unificava 3 (i formati di traccia) | **10 → 1**, con l'elenco dei dieci e la mappa di conversione (§13) | E4-N3/N2 |
| 4 | **Regole opposte e contratti auto-invalidanti** | INTELLIGENCE-V2 vieta di scrivere la wiki a mano · `CLAUDE.md` WIKI-FIRST ordina di farlo *«senza chiedere il permesso»*: due regole non negoziabili, opposte, entrambe attive · la regola CP-id *«applicata alla lettera invalida per contratto tutti i 328 passaggi»* · `brand_kit` obbligatorio per il Bus, `brand_kit_path: null` nell'unico ordine reale | **ADR che abroga o corregge PRIMA di accendere qualunque hook bloccante.** Un guardiano montato su contratti impossibili produce blocco totale o deroga di massa | E0.6 (nuovo, §21) |
| 5 | **Veti economici e decadimento di configurazione** | S7: *«non manca codice, manca una decisione»* (expectancy negativa) · la finestra di `empire flow` scaduta il 26/7 | decisioni di §26, in testa e non in coda | E0 |

## 6. La frase-cardine della diagnosi era falsa fuori dal perimetro strumentato

V1: *«L'Impero sa attraversare la sua catena. L'ha fatto una volta, a vuoto, per un esame»* —
riferito al dry-run dell'11 giugno, 58 secondi, cliente `DryRun-Client-01 (TEST - non reale)`.

**È falso.** Esiste una catena completa e **non a vuoto**, sugli **stessi identici destinatari**
della fetta verticale che V1 voleva costruire (i concessionari): il flusso **Preventa** —
scraping Maps → qualifica → `EmpireDesk/state/preventa_leads.json` → **invio WhatsApp reale**, max
50/giorno, skill `avvia-outreach-preventa`.

Sul disco: **10 log di run giornalieri** (dal 6 al 22 agosto), **1.045 lead** nel file di stato
(1,3 MB), di cui **22 in stage `CONTACTED` — messaggi realmente inviati** — e **1.023 `NEW` in
coda**. Nessuna di queste tracce passa da `empire flow`: il contatore che V1 leggeva **non le
vede**.

Doppia conseguenza, e la seconda è quella che cambia il piano:

1. La tesi di V1 (*mancano i fili, non i motori*) **esce rafforzata**: l'azienda ha un flusso vivo
   end-to-end con carichi veri, ed è **cieco ai suoi stessi contatori**.
2. Ma E3, così com'era scritta, progettava una fetta verticale sui concessionari **accanto al
   motore concessionari che già gira** — la quinta «costruzione ripetuta» dell'Impero, con 1.023
   lead veri lasciati fuori dal piano.

**In V2 la fetta verticale non si costruisce: si strumenta ciò che già corre.** (§22-E3.)
*(C3 R-16 [FATALE].)*

## 7. Il magazzino pieno — l'omissione più cara di V1

`grep -in "ultimo metro|25 pezzi|B-043|ADR-016"` su V1 → **0 risultati**. V1 proclamava *«prima
ciò che porta denaro»* e poi non conteneva **un solo gate espresso in euro o in pezzi
pubblicati**.

Misurato stamattina: **30 pezzi finiti e mai usciti, 3.067 MB, 26 caricabili subito senza toccare
niente, il più vecchio fermo da 139 giorni.** Più **6 libri** completi in `libri_pronti/` (V1 ne
contava 4, e quattro dei sei esistevano già quando V1 è stata scritta).

E il motore che li produce — `libri-performanti-multiagente`, **9.737 righe**, `python -m
engine.kdp auto`, gate che riscrive i blocchi bocciati, **l'unico motore dell'Impero che dichiara
il costo unitario misurato** — è **orfano di ogni registro**: `grep "libri" company/REGISTRO-IMPRESA.md`
→ 0 righe, mentre `skills-map.yaml` censisce al suo posto **due gusci morti** (`Workflow-libri/`
fermo da 169 giorni, `KDP - prodottti digitali/` da 151) che gli rubano il nome. Viola L6 oggi,
non domani.

Un Payment Link incassa solo se qualcosa è in vendita. V1 costruiva **la capacità** di incassare
(E0) e **il registro** dell'incasso (N4), e saltava **l'atto che sta in mezzo**.
*(C3 R-5, R-9 [FATALI] · C2 R-1 [FATALE].)*

## 8. Il ritorno più alto per il minor lavoro, che V1 non nominava

`censimento-04b` lo scrive testualmente: **il Workflow di pubblicazione automatica è «il ritorno
più alto per il minor lavoro di tutto il censimento»**. `main_orchestrator` muore all'import con
`OpenAIError: Missing credentials` (`OPENROUTER_API_KEY` / `GROQ_API_KEY` assenti dal suo `.env`),
mentre `pubblica.py` e `ig_carousel_publish.py` sono **già verificati funzionanti**, con dry-run di
default e la regola *«nessun PASS finto»*.

Costo: **una chiave nel `.env`** più lo spostamento di un'istanziazione dentro una funzione.
V1 lo lasciava, per implicazione, in E8 — dietro **125-194 ore di lavoro pianificato**. E il
paradosso: E0 ruotava **proprio la chiave OpenRouter**, cioè Max sarebbe passato dalla console
OpenRouter senza che il piano gli facesse incollare la chiave nuova nell'unico `.env` che
l'aspetta.

---

# PARTE III — L'ARCHITETTURA: CINQUE FUNZIONI INNESTATE, NESSUN ECOSISTEMA NUOVO

## 9. Il verdetto su NEXUS, e cosa lo sostituisce

> **NEXUS come cinque funzioni regge. NEXUS come sedicesimo ecosistema no.**

Quattro organi su cinque **esistono già**, in tutto o in parte. Costruirli daccapo dentro un
ecosistema nuovo significa fabbricare il **terzo involucro** e l'**undicesimo schema** — contro
L4, e contro la storia di questo Impero (cinque APEX-7, due workshop estate, tre cartelle
caroselli).

| Funzione | Cosa esiste già | Cosa manca davvero | Dove si innesta |
|---|---|---|---|
| **F1 — Tabella di instradamento** (ex N1) | `29-LANCI/dati/registro.yaml`: **17 passaggi** con carico, criterio di accettazione e comportamento su rifiuto + `valida_registro.py` **INV-20** che li sorveglia a macchina | la **generalizzazione** a scala d'Impero, e la **riparazione del suo buco noto**: `valida_registro.py:483` fa `if p.get("esterno"): continue` — **i passaggi inter-ecosistema non sono sorvegliati**, cioè proprio la classe che F1 deve governare | `empire/registry/` + `registro.yaml` esteso |
| **F2 — Bus con code vere** (ex N2) | `company/Backbone/Bus/` (oggi 3 file: README, template, `.gitkeep`) | **le caselle su disco + HC-v2 + LA POMPA**: quale evento già quotidiano svuota la coda. Senza la pompa, N2 diventa il secondo `handoffs/.gitkeep` | `company/Backbone/Bus/` + hook di avvio sessione (modello `empire/avvia.py`, che dimostra che funziona) |
| **F3 — Emettitore unico di eventi** (ex N3) | `empire/trace.py`: **219 righe, funziona, è testato, rifiuta le tracce senza prova** | il campo **`origine: hook\|agente\|mano`** e **N chiamate dentro i motori vivi**. Il censimento: *«Il pezzo mancante non è la funzione: è il punto di aggancio»* | `empire/trace.py` + una riga dentro `outreach_giornaliero.py`, `pubblica.py`, `engine.kdp` |
| **F4 — Il libro dei fatti-denaro** (ex N4) | `scripts/tesoreria.py` **completo** (entrata, spesa, report, incassa, previsione) + 4 agenti invocabili + i due `.jsonl` **creati e a 0 byte** | **accenderla**: la prima riga scritta, e il campo `costi` reso obbligatorio in `checkpoint.py` (303 checkpoint, campo mai compilato — **un'ora di lavoro**) | `scripts/tesoreria.py`, **nessun secondo libro** |
| **F5 — Il guardiano** (ex N5) | `.claude/settings.json` con **5 hook attivi**, fra cui `gate_battito_hook.py` che **blocca la consegna** · `empire/registry/orphans.py:111-119` (regola `UNREGISTERED`) e `render.py:42-46`: *«Il codice per tenere onesta l'anagrafe esiste ed è scritto. Nessun hook lo esegue»* · INV-20 che valuta criteri a macchina | **il cablaggio**: righe in `settings.json` e un pre-commit — il censimento lo quantifica in *«un file di dieci righe»* | `.claude/settings.json` + `.githooks/pre-commit` |

**La regola di precedenza sui soldi era già scritta** e V1 stava per violarla: *«ogni euro nasce
qui e sale in Tesoreria, non scende mai. Se un numero diverge, ha ragione la Tesoreria»*
(`registro.yaml:1830`). Un ledger dentro NEXUS avrebbe creato **due libri per lo stesso fatto** —
esattamente la malattia dei tre formati di traccia che il piano voleva guarire.

## 10. La scheda di nascita — obbligatoria per ognuna delle cinque

Ogni funzione, prima di una riga di codice, ha questa scheda compilata. **Senza, non si
costruisce** (LC-1).

```
FUNZIONE:            F<n> — <nome>
INNESTO:             <file/cartella esistente che si estende>   (mai "cartella nuova")
PROPRIETARIO:        <nome proprio>            CONTROLLORE: <nome proprio, diverso>
CONSUMATORE QUOTIDIANO: <chi legge la sua uscita, ogni quanto>
COSA SUCCEDE SE SI FERMA: <come e in quanto tempo qualcuno se ne accorge>
GATE:                <comando> → <output atteso> → <exit code>
GATE DI FRESCHEZZA:  fallisce se l'ultima uscita ha più di 24 ore
DIVIETO:             <cosa questa funzione non farà mai>
```

| Funzione | Proprietario | Controllore | **Consumatore quotidiano** | Se si ferma, chi se ne accorge |
|---|---|---|---|---|
| F1 Instradamento | EMPERATOR | Ispettorato | il **battito**: riga «archi sorvegliati / archi rotti» | Max, entro un battito |
| F2 Bus + pompa | COO-EMPIRE | Sentinella Drift | l'**apertura di sessione**: stampa le code e l'età del più vecchio pendente | chiunque apra una chat, subito |
| F3 Emettitore | CTO-EMPIRE | Ispettorato | il **battito**: numero di tracce `origine=hook` di oggi | Max, entro un battito |
| F4 Tesoreria | CFO-EMPIRE | Max | il **checkpoint**: ogni task chiuso scrive il suo costo | al primo task chiuso senza numero |
| F5 Guardiano | EMPERATOR | Max | il **commit** e la **consegna del messaggio** | immediato: il lavoro non passa |

> **Nota di verità.** Questa tabella è la risposta a un'obiezione che ho già ricevuto e che è
> giusta: *«anche l'Ispettorato aveva un proprietario»*. La differenza non è il nome nella
> casella «proprietario» — è la colonna **consumatore quotidiano**, e il fatto che le prime tre
> righe finiscano dentro un battito che **esiste già ed è sorvegliato da una macchina**.

## 11. Se Max dice no — il piano B, scritto prima

V1 faceva dipendere il 60% delle ore da un ADR mai chiesto («NEXUS richiede un ADR. Senza,
l'ecosistema non può essere creato»), e lì il testo finiva.

**In V2 il problema è sciolto per costruzione:** nessuna delle cinque funzioni richiede un
ecosistema nuovo, quindi **non serve l'ADR di nascita di ADR-009**. Serve un solo ADR, più
piccolo e diverso: **ADR-024 — «le cinque funzioni di collegamento si innestano su organi
esistenti; è vietato creare un ecosistema di infrastruttura»**, che è una decisione *restrittiva*,
non espansiva.

**Default dichiarato (ordine permanente di Max del 2026-09-06: procedere senza chiedere):** se
l'ADR-024 non viene contestato entro la chiusura di E1, si intende approvato e si procede
all'innesto. Il numero 16 di `REGISTRO-NUMERI.md` **resta libero**.

## 12. HC-v2 — undici campi, non dieci

Ai dieci campi di V1 §9 se ne aggiunge uno, e non è un dettaglio: **`cp_id`**.

`PIANO-MAESTRO/09-ECOSISTEMA-MEMORY.md:180-182` dichiara: *«un handoff senza CP-id è invalido per
contratto»*. È una regola **attiva**, che oggi invalida **tutti i 328 passaggi**, compresi i 4
attraversati l'11 giugno (il campo non esiste in `trace.jsonl`). Uno schema HC-v2 senza `cp_id`
**nascerebbe già invalido** per una legge scritta dell'Impero.

| Campo | Perché |
|---|---|
| `_instance_id` | oggi `_id` è l'id del *contratto*, non del *messaggio*: due handoff dello stesso tipo si sovrascrivono |
| `created_at` reale | ordinare la coda, misurare l'età del pendente |
| `status` mutabile `pending→accepted→done→rejected` | oggi è la costante `"template"` in tutti e quattro |
| `queue` come **percorso** | `"queue": "leads_ready"` non è una cartella: il destinatario non ha casella |
| `scope` `intra`/`inter` | il Bus è a due livelli, HC-v1 non dice a quale appartiene |
| `brand_kit` / `icp` | il README del Bus li dichiara obbligatori nell'inter: 4 contratti su 4 sarebbero invalidi per la regola del Bus stesso |
| `note_correttive` su reject | il rifiuto deve dire perché |
| `retry` / `escalation_count` | due rifiuti → escalation automatica |
| firma di chi ha accettato | audit |
| **criterio di accettazione valutabile a macchina** | oggi sono frasi italiane: *«qualifier_score >= soglia ICP attiva»*. **Un criterio che nessuna macchina può valutare non è un gate, è un'opinione** |
| **`cp_id`** | **legge della MEMORY, già in vigore** |

**Decisione collegata (§26):** o `cp_id` entra in HC-v2, o si scrive un ADR che modifica la regola
della MEMORY. **Mai in silenzio.**

## 13. I dieci schemi → uno

V1 unificava tre formati di traccia (13/8/10 campi). I censimenti ne contano **dieci** di
comunicazione. Finché sono dieci, *«ogni aggancio è un caso a sé»*.

Lavoro di V2 (dentro E4-F3): l'**elenco nominale dei dieci** (`02d` §C.1) · per ognuno, o la
**mappa di conversione** verso lo schema unico, o la **dichiarazione motivata di esclusione**.

**Il caso duro, dichiarato adesso:** APEX-7 non ha `from` né `to`. Non esiste una conversione
onesta senza un **adattatore pub/sub → HC-v2**, che V1 non aveva stimato. In V2 è una voce con le
sue ore (E6), oppure — alternativa legittima — la **decisione dichiarata**: APEX-7 resta motore
interno fuori perimetro di collegamento, e allora esce dal denominatore del 100% come nodo
ARCHIVIO-funzionale, con la ragione scritta. **Le due strade sono ammesse; il silenzio no.**

## 14. Il ponte agenti — due direzioni, non una

**Il problema misurato:** 439 schede in `company/`, **164 esecutori** invocabili (129 in
`.claude/agents/` + 35 globali), **intersezione: 2 nomi**. Dunque **162 esecutori — la popolazione
che gira davvero: `tesoreria-*`, `outreach-*`, `apex-*`, `formazione-*`, le sentinelle — non hanno
scheda sorgente.**

V1 aveva una freccia sola (`scheda → esecutore`), e con essa **scartava per omissione l'azienda
che lavora**: a regime, la tabella di instradamento avrebbe instradato verso ciò che è *descritto*
ignorando ciò che *funziona*. È la stessa dinamica della copia FORGE *«10 su 10, perfetta —
invisibile allo strumento»* che V1 aveva appena denunciato.

**In V2 il ponte ha quattro pilastri, e nessuno è saltabile:**

1. **Anagrafe unica dei nomi, con unicità eseguibile.** Oggi: 439 file → **416 nomi distinti** (23
   collisioni interne), 32 duplicati divergenti, due schede con lo stesso identificativo
   (`ME-A00-conductor` e `ME-A00-memory-conductor`: *«chi instradasse per codice non saprebbe
   quale prendere»*), e **quattro conteggi che danno quattro numeri** (19 · 123 · 129 · 443).
   Finché è così, il gate «tutti generati» **non è eseguibile** (L9).
2. **C7 — il frontmatter nella scheda.** Un esecutore vive di `model`, `tools`, descrizione-trigger:
   la specifica C1..C6 non porta nessuno dei tre. E il grado **si è già perso una volta**: le 5
   sentinelle **prescritte a Sonnet e Opus girano tutte a `model: haiku`**. Un generatore senza
   sorgente del grado lo perde 439 volte.
3. **La freccia inversa — ADOZIONE.** Per ognuno dei 162 esecutori orfani si genera la scheda da
   `company/` **dall'esecutore** (fonte di verità: chi gira). Poi la coppia entra in F1 come le
   altre. È uno scaglione con le sue ore (E5-bis), non una nota a piè di pagina.
4. **Guardia anti-divergenza.** Marcatura `generato da <scheda> — non modificare` + hash + hook che
   blocca l'edit diretto. Senza, il giorno dopo la generazione qualcuno modifica l'esecutore a mano
   (i 129 di oggi sono nati così) e si riapre la fabbrica dei 36 duplicati **su scala 439**.

*(C1 R-9 [FATALE] · C3 R-14 [FATALE] · C2 R-11.)*

## 15. I punti d'ingresso — tre classi, non una regola sola

V1: *«ogni ecosistema deve avere un comando che parte»*. Ma l'involucro **esiste già in doppia
copia, vivo**:

- **`empire/`** — 14.628 righe, VIVO — *«è già costruito per ricevere i motori altrui: un motore
  che espone `register(sub)` diventa un sottocomando `python -m empire <x>` senza toccare una riga
  di `cli.py`. Il guasto non è che manchi un posto dove agganciare i motori: è che nessuno dei
  motori si è mai agganciato qui»*.
- **`EmpireDesk/`** — VIVO — *«non si avvolge: è lui l'involucro»*, con **4 motori su 25 già
  agganciati** come subprocess, e **uno dei quattro che punta alla cartella sbagliata**
  (`metrics.py` conta i caroselli dove non sono).

E il canale che l'Impero usa **davvero ogni giorno** non è il comando: è la **skill**
(`/avvia-outreach-preventa`, `/empire-studio`, `/tesoreria`, `/ultimo-metro`), con dentro *«gate
deterministici, non contorno»*. V1 non nominava le skill una sola volta: un «comando per
ecosistema» sarebbe nato come **quarta classe di puntatori** da tenere allineati.

| Classe | Come si aggancia | Costo |
|---|---|---|
| **A — motore con CLI proprio** (9 vivi su 25) | modulo `register(sub)` → `python -m empire <x>` | basso, 1-3 h a motore |
| **B — motore dietro skill viva** | **la skill È il punto d'ingresso**: si registra in F1 così com'è | quasi zero |
| **C — motore ad attivazione naturale** (Empire Studio: *«nessun comando. Non si digita niente di tecnico»*) | **decisione esplicita di Max + stima dedicata**: dargli un comando significa costruire `run_studio.py` che incateni ingest → frame → scene → forge → wiki — **un build nuovo, non un wrapper** | alto, fuori scaglione standard |

*(C1 R-6, R-12 · C3 R-4 [FATALE].)*

---

# PARTE IV — LE FORZE

## 16. L'addestramento — già progettato, non si rifà

V1 rimandava a V2 la progettazione del modulo d'ingaggio *«perché il doom bot non è mai partito»*.
**Era partito e aveva consegnato**: `censimento-03c-addestramento.md`, **1.064 righe**, chiuso 17
minuti dopo V1 — 19 fonti, **minimo comune di 10 righe**, **modulo d'ingaggio in 3 varianti**
(scagnozzo / sentinella / doom bot), costo misurato **180-550 token per forza**.

V2 lo **assorbe citandolo**, e non riscrive una riga. *(Rifare un lavoro consegnato è l'errore
della «cartella vuota» che vuota non era: è la ragione per cui esiste L1.)*
*(C3 R-3.)*

## 17. Le 29 regole e i 12 hook — con il costruttore, lo scaglione e il gate

Il difetto di V1 non era l'elenco: era che **i 12 hook [MECCANICA] non stavano in nessuno
scaglione** — nessuna ora, nessun gate, nessun posto — mentre erano *«l'unico pezzo che renderebbe
automatica la disciplina che i gate di E1..E8 presuppongono»*.

In V2 sono **E0.7**, prima di ogni lavoro di massa. Ognuno nasce col suo test **contro il proprio
scheletro vuoto** (regola 21, applicata a se stessa: è già successo che un `--check` approvasse il
template e che un gate lanciato senza opzioni rispondesse `totale: 0` dando **una conferma
falsa**).

| # | Hook | Errore che ha già colpito | Evento |
|---|---|---|---|
| H1 | lavoro chiuso senza traccia | 25 tracce in tutta la vita | `Stop` / fine task |
| H2 | rapporto di agente accettato senza verifica su disco | **6 episodi** di lavoro dichiarato e mai fatto | consegna sub-agente |
| H3 | dato senza sorgente riscontrabile | i «61 lead reali» che non esistevano come file | consegna |
| H4 | controllo che passa sul proprio scheletro vuoto | `--check` che approvava il template · `registry gate` → `totale: 0`, exit 0 | costruzione di ogni gate |
| H5 | indicatore verde nel ramo d'errore | KPI verde su valore illeggibile | costruzione |
| H6 | frontmatter di agente rotto che degrada in silenzio | **4 agenti morti per due caratteri** | pre-commit |
| H7 | numero di checkpoint scelto a mano | ceduto **4 volte in 13 giorni** | pre-commit |
| H8 | due forze che scrivono lo stesso oggetto | 6 episodi, git bloccato incluso | avvio delega |
| H9 | file d'uscita non creato vuoto al primo minuto | le cadute che hanno perso 12 e 3 righe | ingaggio |
| H10 | chiave di stato nata dentro un prompt | famiglia CASO 4 | ingaggio |
| H11 | **segreto committato** | **recidiva tre volte**: B-020 Brevo (in `HEAD` dal commit iniziale), B-021 Arena+OpenRouter, B-023 Instagram — repo **pubblico**, e in `.githooks/` **non esiste uno scanner di segreti** | pre-commit |
| H12 | consegna fuori forma del battito | già in vigore (`gate_battito_hook.py`) — **è il modello**, resta com'è | `Stop` |

**H11 è nuovo rispetto a V1** e chiude una violazione della legge del piano stesso: *«una regola
ceduta due volte diventa un hook»*. Qui è ceduta **tre** volte, e V1 la lasciava regola —
limitandosi a ruotare le chiavi, cioè curando la ferita e lasciando il coltello.
*(C3 R-15.)*

## 18. Parallelo e sequenziale — invariata

**Produzione** (scrive, consuma budget, tocca gli stessi file) → **sequenziale, sempre** (9/9
contro 1/4). **Ricognizione** (sola lettura, aree disgiunte) → **parallelo ammesso, con scrittura
incrementale obbligatoria** (8 doom bot, 7 caduti, **8.120 righe salve**). Il criterio non è la
fortuna: nella ricognizione la scrittura incrementale rende la caduta quasi gratuita.

## 19. Chi esegue — i nomi, che V1 non aveva

`grep -cin "gael"` su V1 → **0**. `grep -cin "neri"` → **0**. Un piano da 130-190 ore con un solo
esecutore nominato (Max, in E0) è un piano che esegue «qualcuno» — e «qualcuno» in questa azienda
ha già prodotto l'Osservabilità.

| Chi | Cosa prende in V2 | Cosa NON si ferma |
|---|---|---|
| **Max** | E0 (le mani: credenziali, `.env`, Payment Link, **caricamento dei pezzi**), le decisioni di §26, le copertine | — |
| **EMPERATOR + forze** | E0.5, E0.6, E0.7, E1, E2, E4, E5a/b/c, E7 | il battito e la manutenzione corrente |
| **Neri** | **E3 — Preventa strumentata**: è il suo terreno dal 23 agosto, i 1.045 lead sono i suoi | l'outreach corrente continua a girare durante E3 |
| **Gael** | **EMPIRE DESK B0-B4 resta il suo «lavoro #1»** e **non si ferma**: E5b (punti d'ingresso) è dove i due piani si toccano, perché EmpireDesk è già uno dei due involucri | — |

**La riconciliazione che V1 non faceva:** il giorno in cui V2 parte, se nessuno lo dice, esistono
**due «lavori #1»** (EMPIRE DESK per Gael, il piano per tutti gli altri) e nessun documento dice
quale vince. **In V2 vince EMPIRE DESK per Gael** — perché E5b ne dipende, non viceversa — e il
piano gli chiede una cosa sola: che i motori agganciati a EmpireDesk espongano `register(sub)`
(§15 classe A).

---

# PARTE V — IL LAVORO

## 20. Il criterio d'ordine, corretto

V1 aveva i tre principi giusti e **li violava alla prima applicazione**. V2 li tiene e li applica:

1. **Prima l'euro che si può incassare oggi** — la merce già prodotta e pagata esce dal magazzino.
2. **Poi i controlli**, perché tutto ciò che viene dopo è lavoro di massa e senza controlli la
   recidiva rientra dentro il piano nato per chiuderla.
3. **Poi il perimetro pulito**, perché le ondate su un elenco sporco vanno rifatte.
4. **Poi la fetta verticale su ciò che già corre**, mai accanto a ciò che già corre.
5. **Solo alla fine la scala orizzontale** (le centinaia di schede).

## 21. Gli scaglioni — con ore, chi, percorsi, gate eseguibile, tetto

> **Regola di tetto (L9 + C3 R-12):** ogni scaglione ha un tetto = **stima alta × 1,5**. Sforato
> il tetto ci si ferma, si scrive perché, e si riporta. Nessuno scaglione si sfonda in silenzio.

---

### **E0 — LE MANI DI MAX** · 2-3 h di Max · *chi: Max*

Non 45 minuti: V1 aveva dimenticato la merce.

1. **Rotazione delle 3 credenziali esposte** (B-020 Brevo · B-021 Arena+OpenRouter, **viva
   adesso** · B-023 Instagram) — **con l'elenco dei file che le portano** (L10):
   `Outreach/Outreach Workflow/.env` · `SKILL & Agenti/Workflow pubblicazione automatica/.env` ·
   `.claude/skills/workflow-pubblicazione-auto/.env` — **e il passo «incolla la nuova in tutti e
   tre»**, che in V1 non c'era.
2. **Login Instagram** (dopo il cambio password) e **LinkedIn** — le sessioni hanno 94 e 111
   giorni.
3. **2 Payment Link Stripe.**
4. **Caricamento dei primi 5 pezzi** dei 26 caricabili (accessi ai negozi = mani di Max), segnati
   con `python scripts/ultimo_metro.py --segna "<ID>"`.

> ⚠️ **Il pericolo che V1 creava.** La chiave OpenRouter **non è un segreto orfano**: è consumata
> da **20+ file Python**, fra cui `Outreach/Outreach Workflow/run.py`, `run_followup.py`,
> `run_reply_manager.py`, `Instagram Automation/personalize.py`, `LinkedIn Automation/personalize.py`.
> L'outreach email è **uno dei 2 workflow su 6 che oggi partono**. Ruotare senza riscrivere i tre
> `.env` **spegne l'unico motore che produce contatti reali** — e i gate di V1 lo avrebbero
> **confermato**, non impedito: *«la vecchia chiave risponde 401»* diventa vero **esattamente
> quando i tre `.env` sono morti**, e `empire controllo` per l'email verifica solo *«credenziali
> Gmail presenti»*, mai OpenRouter.

**Gate (L9):**
```
python -m empire controllo                     → 5/6 workflow pronti   (exit 0)
python scripts/gate_rotazione.py               → vecchia chiave 401 su tutti e 3 i servizi (exit 0)
<dry-run outreach> dopo la rotazione           → exit 0                 ← IL GATE CHE MANCAVA
python scripts/ultimo_metro.py --json | jq .caricabili  → ≤ 21          (5 pezzi usciti)
```
*(`gate_rotazione.py` non esiste: è deliverable di E0.5. Fino ad allora il 401 si verifica a mano
e lo si dichiara.)*

> **Nota sul gate INCASSO, che oggi è finto.** La riga INCASSO di `empire controllo` legge
> `Crea siti/Siti CCM/checkout.config.json` → `rails.stripe_base.attivo`: **un booleano in un file
> del repo**. Chiunque scriva `"attivo": true` con zero link rende il gate verde; e Max che crea
> davvero i link lo lascia rosso finché qualcuno non edita il JSON. In E0.5 diventa una richiesta
> HTTP in sola lettura ai due Payment Link.

---

### **E0.5 — GLI AGGANCI A COSTO ZERO** · 4-6 h · *chi: EMPERATOR*

Tutto ciò che i censimenti quotano in minuti e che V1 aveva messo dietro 50-70 ore di costruzione.

| # | Aggancio | Costo misurato | Perché adesso |
|---|---|---|---|
| 1 | **Chiave nel `.env` del publisher** + istanziazione spostata dentro una funzione | ~1 h | sblocca *«il ritorno più alto per il minor lavoro di tutto il censimento»* |
| 2 | **Prima riga in `entrate.jsonl`** (o `spese.jsonl`) | 1 riga | la Tesoreria è costruita e mai accesa: 0 byte dal 3 settembre |
| 3 | **Campo `costi` obbligatorio in `scripts/checkpoint.py`** | ~1 h | 303 checkpoint, campo **mai compilato**: da quel giorno ogni task chiuso lascia un numero |
| 4 | **Le caselle mancanti create** (elenco, L10): `company/runtime/`, `company/metrics/`, `marketing/handoffs/log`, `platform/handoffs/log`, `company/Memory/pubblicati.json` | ~1 h | 5 Guild e 5 Sentinelle dichiarano deliverable in cartelle che **non esistono**: nessun hook può obbligare un atto che non ha dove finire |
| 5 | **Riga di registro per `libri-performanti-multiagente`** in `REGISTRO-IMPRESA.md` + i due gusci morti marcati ARCHIVIO | ~30 min | il motore più produttivo dell'Impero è orfano; due gusci fermi da 169 e 151 giorni gli rubano il nome |
| 6 | **`metrics.py` di EmpireDesk** che punta alla cartella caroselli giusta | ~30 min | uno dei 4 motori agganciati conta dove non c'è niente |
| 7 | **`python -m empire vivo --json`** — il comando che calcola la formula del 100% (§3) | 2-3 h | senza, il gate finale del piano non è eseguibile (L5/L9) |
| 8 | **`scripts/gate_rotazione.py`** e il gate INCASSO via HTTP | 1-2 h | i due gate di E0 che oggi sono dichiarazioni |

**Gate:**
```
test -s company/Memory/tesoreria/entrate.jsonl                  → exit 0 (file NON vuoto)
python scripts/checkpoint.py cp --titolo "prova" --dry-run      → rifiuta se manca `costi`
test -d company/runtime && test -d company/metrics              → exit 0
grep -c "libri-performanti-multiagente" company/REGISTRO-IMPRESA.md → ≥ 1
python -m empire vivo --json                                    → stampa numeratore/denominatore
python -m empire pubblica --dry-run                             → exit 0 (import non fallisce più)
```

---

### **E0.6 — LE REGOLE CHE SI CONTRADDICONO** · 2-3 h · *chi: EMPERATOR, decide Max*

**Prima di accendere qualunque hook bloccante**, si sciolgono le collisioni note, altrimenti F5
al primo giorno o ferma il lavoro vero o viene spento — e un hook spento è la fine del principio.

1. **INTELLIGENCE-V2 vieta di scrivere la wiki a mano · `CLAUDE.md` WIKI-FIRST la ordina.** Due
   regole non negoziabili, opposte, entrambe attive → **ADR che ne abroga una**.
2. **`cp_id` obbligatorio negli handoff** (§12) → entra in HC-v2, oppure ADR che modifica la regola
   della MEMORY.
3. **`brand_kit` obbligatorio nell'inter-ecosistema** con `brand_kit_path: null` nell'unico ordine
   reale → si compila o si declassa a facoltativo, per ADR.

**Gate:** `ls company/Memory/decisions/ADR-02*.md` → i tre ADR esistono e nominano la regola che
abrogano. *(Gate documentale, dichiarato tale: qui il deliverable è una decisione.)*

---

### **E0.7 — I DODICI HOOK** · 6-10 h · *chi: EMPERATOR*

I 12 di §17. **Configurazione, non costruzione**: righe in `.claude/settings.json` e in
`.githooks/pre-commit`, ognuna che chiama un valutatore **già scritto** (`empire registry
gate/orphans`, INV-20, il modello `gate_battito_hook.py`).

Ognuno nasce con: **evento esatto** · **test contro lo scheletro vuoto** · **consumatore
quotidiano dichiarato** — le tre condizioni che hanno tenuto vivo l'unico guardiano sopravvissuto,
mentre `verify-empire.ps1` (113 check) *«verifica la propria esistenza e nessuno lo lancia»* e le
5 sentinelle aspettano *«il dito che preme»*.

**Gate:**
```
python scripts/test_hooks.py            → 12/12 verdi, ognuno provato con un caso finto (exit 0)
git commit con chiave finta "sk-or-xxx" → RESPINTO                          (H11)
git commit con frontmatter agente rotto → RESPINTO                          (H6)
consegna senza traccia in un task finto → RESPINTA                          (H1)
```

---

### **E1 — IL PERIMETRO PULITO** · **13-20 h** *(V1 diceva 4-6)* · *chi: EMPERATOR*

**La regola di fusione si scrive PRIMA di aprire la prima coppia**, altrimenti sono 36
micro-decisioni editoriali su copie che **divergono tutte** — e nel primo caso è migliore la copia
radice, nel secondo la copia reparto: *«un orchestratore ne leggerebbe uno a caso»*.

> **Regola di fusione (proposta, vale salvo ADR contrario):** vince la copia con **più criteri
> C1-C6** al `forge`; a parità, la **più recente**; la perdente va in `archivio-origine/` con una
> riga di motivo e un puntatore dalla vincente. **Mai cancellare** (L1).

Conto per voci: 36 fusioni (15-25 min l'una) = **9-15 h** · `census.py` riparato + provato contro
il proprio scheletro = 1-2 h · `verify-agents` (**7 FAIL**) e `verify-skills` (**3 FAIL**) = 1 h ·
`empire doctor` (block 2, warn 2, info 43) = 1-2 h · i puntatori di ecosistema = 1 h.

> **Blocco che V1 non aveva visto:** `registry dupes` stampa nel proprio output che la scelta
> dell'albero canonico (`DIGITAL-EMPIRE/` vs `WORKFLOW-ESTATE/`) è *«riservata a un ADR di Max»*.
> **Quell'ADR va chiesto in E0**, o E1 parte e si ferma ad aspettare. Default dichiarato se non
> arriva: vince `DIGITAL-EMPIRE/`.

> ⚠️ **Convivenza (il rischio che V1 non nominava).** Su questo repo gira un **daemon di commit
> automatico**: 30 commit su 50 sono `sync(Max): aggiornamento automatico`, a 2-12 minuti l'uno
> dall'altro. Una fusione è un'operazione a due tempi: se la sessione cade in mezzo, **il daemon ha
> già committato e pushato lo stato misto** — la metà distruttiva che la regola 28 vieta di
> committare, solo che qui a committarla non è la forza, è l'infrastruttura.
> **Vincolo E1:** ogni fusione = **un commit manuale atomico** (vincente + archivio + puntatori
> insieme), **daemon di sync sospeso** per la durata dello scaglione, **radice pulita** prima di
> iniziare (nessun `SYNC-CONFLICT.txt`, nessun rebase pendente — verificato: oggi è pulita).

**Gate:**
```
python -m empire doctor                          → block 0                        (exit 0)
python scripts/verify-agents.py                  → 0 FAIL                          (exit 0)
python scripts/verify-skills.py                  → 0 FAIL                          (exit 0)
python -m empire registry census --json          → gli id coincidono ESATTAMENTE con `forge scan`,
                                                   differenze = 0 e la lista stampata
```
> **Perché il gate è cambiato.** V1 diceva *«`forge scan` e `registry census` danno lo stesso
> numero»*. Ma i due strumenti **classificano diversamente**: `census.py:163-164` marca "agent" per
> path ed **esclude `.claude/`**; `forge scan` conta le 439 schede di `company/`. Oggi: **439 contro
> 70**. Riparata l'indentazione, non c'è **nessuna garanzia** che i due totali coincidano — e
> l'esecutore si troverebbe a scegliere fra «E1 mai chiuso» e «allineo i criteri finché i numeri
> tornano», che è spostare il gate (vietato da L5). Il gate giusto confronta **gli id**, non i
> totali, e **la definizione unica di "agente" si scrive in E1 prima di riparare il contatore**.

---

### **E2 — LA RINOMINA CHE VALE QUARANTA PUNTI** · **8-14 h**, più una misura che decide · *chi: EMPERATOR*

Le 174 schede a un criterio dal pieno: `## Input / Output` → `## Ingresso` + `## Output`. Con un
programma che verifica una per una, mai a mano. Il metodo è giusto: nelle schede i blocchi
`**Input atteso:**` e `**Output prodotto:**` sono **già separati**, la spaccatura è
meccanizzabile. *(Nota: i file con quell'intestazione in `company/` sono **391**, non 174: il
programma ne tocca più del doppio di quelli che cambiano fascia.)*

> **Il conto che nessuno ha fatto, e che decide il costo.** La specifica C4 esige **due** cose: il
> titolo `## Output` **e** *«per ogni artefatto: che cos'è e dove finisce»*. La rinomina dà la
> prima. **Quante delle 174 hanno già la destinazione? Nessun censimento l'ha contato.** Se manca
> nella metà dei casi sono ~87 destinazioni da scrivere (10-15 min l'una) = **+15-22 h**.
> **Primo lavoro di E2: contarle (mezz'ora di script).** La stima si chiude dopo.

**Gate (doppio, perché il punteggio non è il contratto):**
```
python -m empire forge scan --json > /tmp/dopo.json     → OPERATIVO ≥ 53,5%
diff prima.json dopo.json                               → nessun agente peggiorato
                                                          (snapshot `prima.json` PRESO PRIMA della
                                                           prima rinomina: nessun lavoro di V1 lo prevedeva)
grep -A5 "^## Output" <le 174>                          → ognuna contiene un percorso o un comando
```
> Senza il terzo gate, **174 rinomine senza una sola destinazione aggiunta passano al 53,5%
> pieno**: `forge.py:62-64` cerca il titolo, non la destinazione. Sarebbe il punteggio che sale e
> il contratto che resta carta — e ce ne accorgeremmo in E3/E5, quando un orchestratore legge il
> contratto e non trova **dove** consegnare.

---

### **E3 — LA FETTA VERTICALE: PREVENTA STRUMENTATA** · 12-18 h · *chi: Neri + EMPERATOR*

**Non si costruisce un flusso nuovo: si mette il filo addosso al flusso che già corre.** I 5 step
di `WF-S1-CONCESSIONARI` si **mappano** sul flusso Preventa (1.045 lead, 22 già contattati, 1.023
in coda), e i punti di aggancio sono righe di codice dentro il motore che gira:

1. `flow done_step()` chiamato **da dentro** `outreach_giornaliero.py`, al punto in cui il lead
   cambia stato — non dalla riga di comando.
2. `trace.scrivi(origine="hook")` accanto, come **sottoprodotto**.
3. **Ordine cablato: si scrive lo stato PRIMA di inviare**, e il ciclo si riprende da `state.json`,
   mai da capo.

> ⚠️ **Il danno che nessun `git reset` annulla.** Se la sessione cade fra l'invio del messaggio e
> la scrittura dello stato, alla ripresa nessun file dice che il lead è già stato contattato: il
> rilancio **ricontatta un cliente vero**. È l'unico danno del piano che esce dall'azienda.

> **Due cose che V1 diceva e sono false, verificate nel codice:**
> (a) *«la finestra scaduta è QUELLA la ragione per cui il contatore è a zero»* — la `window` letta
> da `workflows.yaml` è usata in **un solo punto**, `empire/flow/cli.py:91`, **dentro una
> `print()`**. È cosmetica: nessuna riga del motore la confronta con la data. La ragione vera è
> quella che V1 aveva già misurato: `done_step()` ha **un solo chiamante**.
> (b) l'elenco dei lavori di E3 **non conteneva il lavoro che chiude gli step**. Senza, i «5/5»
> arrivano in un modo solo: chiusi a mano — cioè l'atto separato e volontario che il piano intero
> giura di abolire.

**Gate:**
```
python -m empire flow status                      → WF-S1: 5/5 step chiusi
python -m empire trace stato --origine hook       → ≥ 5 tracce con origine=hook nella finestra
                                                     (delta, non totale assoluto)
jq .dry_run <state.json del ciclo>                → false
jq '[.[]|select(.stage=="CONTACTED")]|length' preventa_leads.json → > 22   (almeno un lead nuovo
                                                     passato NEW→CONTACTED durante la corsa tracciata)
```
> **Perché il gate di V1 non poteva funzionare.** Diceva *«`trace stato` > 25 senza intervento
> manuale»*. Le tracce sono **esattamente 25 oggi**: il gate passa alla ventiseiesima, e la
> ventiseiesima si scrive in dieci secondi con `empire trace scrivi`, che è pubblico. E la clausola
> «senza intervento manuale» — l'unica che dà senso al gate — **non è verificabile da nessun
> comando**, perché la Traccia non ha un campo di provenienza. Il campo `origine` (E4-F3) **è il
> prerequisito di questo gate**, ed è per questo che F3 sta prima di E3 nella catena dei lavori,
> pur essendo dentro E4 come funzione.

---

### **E4 — LE CINQUE FUNZIONI INNESTATE** · **12-20 h** *(V1 diceva 25-40 per costruirle)* · *chi: EMPERATOR*

Ordine imposto dalla catena: **F3 → F4 → F5 → F2 → F1**.

- **F3 — Emettitore unico** (3-5 h): campo `origine: hook|agente|mano` in `empire/trace.py` +
  le chiamate dentro i motori vivi (Preventa, `pubblica.py`, `engine.kdp`) + la mappa dei 10
  schemi (§13).
- **F4 — Tesoreria accesa** (1-2 h): è già fatta in E0.5 punti 2-3; qui si aggiunge il **report
  quotidiano dentro il battito**.
- **F5 — Guardiano** (2-4 h): è E0.7 già in vigore; qui si aggiunge **il valutatore a macchina dei
  criteri di accettazione** (INV-20 generalizzato).
- **F2 — Bus con la pompa** (4-6 h): code su disco in `company/Backbone/Bus/` + HC-v2 (11 campi) +
  **la pompa**: quale evento già quotidiano le svuota (hook di apertura sessione, modello
  `empire/avvia.py`) + gate sull'età del pendente.
- **F1 — Instradamento** (2-3 h **per gli archi della fetta**, il resto a domanda): generalizzazione
  di `registro.yaml` + INV-20, **con il ramo `if p.get("esterno"): continue` sostituito da una
  verifica vera** — altrimenti F1 nasce cieca proprio sulla classe di passaggi per cui esiste
  (262 INTER su 328).

> **Il difetto che uccide F2 se lo dimentichiamo.** V1 specificava la **struttura dati** e taceva
> il **processo consumatore**. Il Bus attuale **è già** il caso-Osservabilità: 3 file, e il suo
> README dichiara come motori `bus.sh` e `gbus.sh` **che non esistono**, insieme a `fulfilled/`,
> `rejected/`, `runtime/bus/`, gli `inbox/outbox` per ecosistema: **tutti disegnati, nessuno
> creato**. Una coda il cui consumo è un atto CLI volontario finisce come `handoffs/.gitkeep`.
> **Senza la pompa scritta, F2 non si costruisce.**

**Gate:**
```
python -m empire trace stato --origine hook --json   → ≥ 1 traccia nata da hook nelle ultime 24 h
test -s company/Memory/tesoreria/entrate.jsonl       → exit 0
ls company/Backbone/Bus/handoffs/*.json              → ≥ 1 file con status ≠ "template"
python -m empire bus eta --max-ore 24                → exit 0 (nessun pendente più vecchio di 24 h)
python scripts/valida_registro.py --inter            → i passaggi INTER sono sorvegliati (exit 0)
python -m empire inspect --freschezza 24h            → exit 0, e SCARTA le righe backfilled  (LC-3)
```

---

### **E5a — IL GENERATORE** · 8-15 h · *chi: EMPERATOR*
Il generatore scheda→esecutore **non esiste**: in V1 era una freccia in un diagramma. Va scritto,
collaudato contro il proprio scheletro (H4) e provato sui 16 (15 direttori + MAXIMILIAN), con
**C7** (frontmatter: `model`, `tools`, trigger) e la **marcatura anti-divergenza**.
**Gate:** `for a in <i 16>; do <invocazione di prova>; done` → 16/16 rispondono; `git diff` su un
esecutore generato e modificato a mano → **respinto dall'hook**.

### **E5-bis — L'ADOZIONE DEI 162** · 20-40 h · *chi: EMPERATOR, a ondate sequenziali*
Per ogni esecutore orfano si genera la scheda **dall'esecutore**. È il pilastro 3 di §14: senza,
F1 instrada verso ciò che è descritto e ignora ciò che funziona.
**Gate:** `python -m empire anagrafe --orfani` → 0; nomi unici verificati a macchina.

### **E5b — I PUNTI D'INGRESSO** · 15-45 h, **uno per volta** · *chi: EMPERATOR + Gael*
Per classe (§15): A → `register(sub)`; B → la skill si registra così com'è; C → decisione di Max.
Si parte dai **3 ecosistemi della fetta E3**, non da tutti e 15.
**Gate, per ciascuno:** `python -m empire <x> --help` → exit 0 **e** la voce compare in F1.

### **E5c — F1 POPOLATA** · 10-20 h, **solo gli archi della fetta** · *chi: EMPERATOR*
Popolare `skills-map.yaml` (**650 voci, zero campi `consuma`/`produce`**) e `registro-agenti.yaml`
(**142 voci, `input_schema` compilato una volta**) non è un refactoring: è **una campagna di
censimento dati**, mai quotata da nessuno. In V2 si popola **solo per gli archi che la fetta
attraversa**; il resto **a domanda**, dichiarato.

---

### **E6 — I TRE ECOSISTEMI SENZA MOTORE + IL CASO APEX-7** · da stimare dopo E4, con tetto · *chi: EMPERATOR*
`09-OPERATIONS` (si aggancia a F4) · `04-MARKETING` (**i gate APSOC ≥80/≥85 non hanno una sola
funzione che li calcoli in tutto il repo**) · il ramo e-commerce di `05-MULTI-BUSINESS`. Più
**APEX-7**: adattatore pub/sub → HC-v2 **oppure** esclusione dichiarata dal denominatore (§13).

### **E7 — LE ONDATE SUGLI AGENTI** · **69-109 h** *(V1 diceva 30-45)* · *chi: EMPERATOR, sequenziale per famiglia*
| Ondata | Agenti | Lavoro | Ore |
|---|---|---|---|
| 2 | 66 | titolo + sezione gate copiata dal capostipite, 15-20 min l'uno | **16-22 h** |
| 3 | 74 | **la scheda va rimessa in forma sullo scheletro**: riscrittura vera, 30-45 min | **37-55 h** |
| 4 | 64 | id/gate/passi in combinazioni diverse (17 solo C5, 11 solo C6, 25 miste): niente prompt unico | **16-32 h** |

**Regola di ricalcolo (nuova):** dopo i **primi 20 agenti di ogni ondata** si misura il tempo reale
e si riscrive la stima. È un numero che il piano può produrre da solo.
**Gate:** `forge scan --json` per ondata, con la percentuale per criterio, **e** il controllo della
destinazione (come E2).

### **E8 — LA CONSEGNA E GLI ORFANI** · 10-20 h + calendario esterno · *chi: Max (accessi) + EMPERATOR*
I restanti **21 pezzi** del magazzino · i **6 libri** su KDP (copertine = Max, review KDP 24-72 h a
libro: **tempo di calendario, non di lavoro**) · gli orfani **per cartella, non per file**:
`registry orphans` dà **block 11.061, warn 13.962, totale 25.023**; tolti i 4.675 `vendored`
restano ~20.000 voci — a 30 secondi l'una sono ~170 h, e **nessuna regola di triage all'ingrosso
esisteva in V1**.
**Gate:** `ultimo_metro.py --json` → `caricabili = 0`; `entrate.jsonl` con almeno una riga di
vendita reale; `registry orphans` → block < 1.000.

### **E9 — L'AUTO-MIGLIORAMENTO** · dopo E3+E4+E5 · *chi: EMPERATOR*
**Gate dichiarato assente in V2** (onestà, L9): E9 non ha ancora un comando. Se ne scrive uno in
V3 o si dichiara fuori piano.

## 22. La tabella di comando

| Scaglione | Ore | Tetto (×1,5) | Chi | Percorsi in scrittura (blocco COORDINAMENTO) |
|---|---|---|---|---|
| E0 | 2-3 (Max) | 4,5 | Max | i 3 `.env`, negozi esterni |
| E0.5 | 4-6 | 9 | EMPERATOR | `scripts/`, `company/Memory/tesoreria/`, `company/runtime/`, `REGISTRO-IMPRESA.md` |
| E0.6 | 2-3 | 4,5 | EMPERATOR+Max | `company/Memory/decisions/` |
| E0.7 | 6-10 | 15 | EMPERATOR | `.claude/settings.json`, `.githooks/` |
| E1 | 13-20 | 30 | EMPERATOR | `company/**` (36 coppie, elencate), `empire/registry/` |
| E2 | 8-14 (+15-22 da misurare) | 21 | EMPERATOR | `company/**` (391 file toccati, 174 che cambiano fascia) |
| E3 | 12-18 | 27 | Neri+EMPERATOR | `Outreach/preventa-*`, `empire/flow/`, `empire/trace.py` |
| E4 | 12-20 | 30 | EMPERATOR | `empire/`, `company/Backbone/Bus/`, `29-LANCI/dati/` |
| E5a | 8-15 | 22 | EMPERATOR | `scripts/`, `.claude/agents/` |
| E5-bis | 20-40 | 60 | EMPERATOR | `company/**`, `.claude/agents/` |
| E5b | 15-45 | 67 | EMPERATOR+Gael | `empire/`, `EmpireDesk/` |
| E5c | 10-20 | 30 | EMPERATOR | `skills-map.yaml`, `registro-agenti.yaml` |
| E6 | da stimare | — | EMPERATOR | 3 ecosistemi + `11-APEX-7` |
| E7 | 69-109 | 163 | EMPERATOR | `company/**` |
| E8 | 10-20 | 30 | Max+EMPERATOR | negozi esterni, `LIBRI/`, anagrafe |
| **Totale** | **~190-320 h** | | | **10-20 settimane** a 15-20 h effettive |

> **Il calendario, che V1 non conteneva in nessuna riga.** V1 non aveva una sola data né una
> durata. Con le stime corrette e la regola del sequenziale (niente sconto dal parallelismo in
> produzione), da E0 a E8 sono **10-20 settimane**. **Il primo euro, però, non aspetta:** sta in
> **E0**, giorno uno.

## 23. Il cruscotto quotidiano — la misura fra un gate e l'altro

V1 aveva **solo gate di fine scaglione**: uno scaglione da 25-40 ore si scopriva deragliato a
lavoro speso. Gli strumenti per misurarlo ogni giorno **esistono già e sono gratis**.

**Sei numeri, in coda a `STATO-EMPIRE.md` a ogni giornata di lavoro sul piano:**

```
controllo x/6 · OPERATIVO % · tracce (di cui origine=hook) · byte entrate.jsonl
· pezzi ancora fermi (ultimo_metro) · vivo% (empire vivo --json)
```

**Regola:** due giornate di lavoro senza che il numero dello scaglione aperto si muova → **ci si
ferma e lo si dichiara**. È la scrittura incrementale applicata al piano stesso, invece che solo
ai file dei doom bot.

---

# PARTE VI — RISCHI, DECISIONI, AUTOCRITICA

## 24. I rischi, con il piano B (che V1 non aveva)

| # | Rischio | Mitigazione | **Piano B se accade** |
|---|---|---|---|
| R1 | **Limite di sessione** (9 episodi in 3 mesi, condizione permanente) | produzione sequenziale · scrittura incrementale · file d'uscita creato vuoto al primo minuto | lo scaglione riparte dal file parziale; **mai** dal principio |
| R2 | La specifica C4 sbagliata applicata 314 volte | letta nel codice, non dedotta · collaudo per singolo agente · E3 la prova su ~10 prima delle centinaia | si ferma l'ondata e si rifà la specifica: costo massimo 20 schede |
| R3 | **Le cinque funzioni diventano carta** | LC (consumatore quotidiano) + gate di freschezza 24 h + **divieto di backfill** | la funzione senza consumatore **non si costruisce**: il piano B è non partire |
| R4 | **Le sessioni collidono** (daemon di sync ogni 2-12 min; 4 collisioni di numerazione in 13 giorni *nonostante* la regola) | percorsi dichiarati per scaglione · commit atomici · daemon sospeso in E1-E2 · numeri coniati dallo script | `git reflog` + la fusione ripetuta: per questo ogni fusione è un commit solo |
| R5 | **Si costruisce e l'azienda continua a non incassare** | E0 è il denaro, giorno uno, e il gate del piano è in **pezzi pubblicati** | se dopo E3 `entrate.jsonl` è ancora 0 byte, **il piano si ferma** e si riapre la domanda: cosa vendiamo, a chi |
| R6 | **La rotazione delle chiavi spegne l'outreach** | i 3 `.env` elencati in E0 + il gate positivo (dry-run outreach dopo la rotazione) | rollback: la chiave vecchia resta valida finché il dry-run non passa |
| R7 | **E3 ricontatta un lead vero** | stato scritto **prima** dell'invio · ripresa da `state.json` | il lead ricontattato si dichiara a Neri e si annota: danno esterno, va detto |

## 25. Criteri di abbandono — quando si smette

Un piano che sa solo vincere trasforma ogni intoppo in stallo. E lo stallo qui non è teorico: è la
voce più anziana del backlog (**due motori di orchestrazione in conflitto da 8 giorni**, B-047,
perché nessun documento aveva un criterio del tipo *«se entro X non è deciso, si fa Y»*).

1. **Tetto ore** = stima alta × 1,5 (tabella §22). Sforato → ci si ferma e si riporta.
2. **Le decisioni hanno una scadenza e un default** (§26). Nessuna decisione lasciata aperta.
3. **I gate delle cinque funzioni hanno una data**: se entro **4 settimane** dalla chiusura di E4
   non esiste una traccia `origine=hook` nata da un lavoro reale, **F3 è fallita e va detto**, non
   rinviata.
4. **Regola dei due giorni fermi** (§23).

## 26. Le decisioni di Max — con default dichiarato

> Ordine permanente di Max (2026-09-06): *«non chiedermi più niente, per qualsiasi cosa hai già un
> permesso, procedi senza fermarti»*. Quindi qui non ci sono domande: ci sono **default**, che
> valgono se Max non dice il contrario.

| # | Decisione | Default se Max tace | Quando serve |
|---|---|---|---|
| 1 | **ADR-024** — le funzioni si innestano, vietato creare un ecosistema di infrastruttura | **si procede con l'innesto**, il numero 16 resta libero | prima di E4 |
| 2 | **Albero canonico** `DIGITAL-EMPIRE/` vs `WORKFLOW-ESTATE/` (lo chiede `registry dupes`) | vince **`DIGITAL-EMPIRE/`** | prima di E1 |
| 3 | **Repo pubblico o privato** — 3 credenziali già nella storia git pubblica, indicizzabile | **resta pubblico + scanner H11 obbligatorio**; se Max vuole privato, è un comando solo | E0.7 |
| 4 | **`cp_id` negli handoff** — la regola MEMORY invalida oggi tutti i 328 passaggi | **`cp_id` entra in HC-v2** (si adegua lo schema, non si abroga la legge) | E0.6 |
| 5 | **`08` e `12`** (paper trading, expectancy negativa, NFT bocciato 89/89) | **ARCHIVIO con onore** (L8): ragione scritta, fuori dal denominatore, niente cancellazione | E1 |
| 6 | **APEX-7** — adattatore o fuori perimetro | **fuori perimetro dichiarato** finché non serve a un flusso vero | E6 |
| 7 | **Empire Studio** (motore senza comando per scelta) | **resta senza comando**: la skill è l'ingresso | E5b |

## 27. L'obiezione più forte a V2

> *«Hai tolto l'ecosistema e hai chiamato le stesse cinque cose "funzioni". La legge del
> consumatore quotidiano è una frase: l'Ispettorato aveva un proprietario e una regola che
> pretendeva un rapporto dopo ogni run — e ha fatto 87 rapporti con un backfill. Cosa impedisce
> alle tue cinque funzioni di finire nello stesso posto, con un nome diverso?»*

**Tre cose, e sono verificabili, non promesse:**

1. **Non c'è niente da fondare.** Quattro funzioni su cinque sono estensioni di file che girano
   oggi: `trace.py` (219 righe testate), `tesoreria.py` (completo), `registro.yaml`+INV-20 (17
   passaggi sorvegliati), `settings.json` (5 hook attivi, uno dei quali **blocca** la consegna).
   Un'estensione che smette di funzionare **rompe il file che la ospita**, e quel file lo usa
   qualcuno oggi. L'Ispettorato invece era una cartella a parte: poteva smettere senza rompere
   niente.
2. **Il consumatore è nominato e sta dentro qualcosa che gira sempre** — battito, apertura di
   sessione, commit, checkpoint (LC-2). Non un consumo inventato per l'occasione.
3. **Il backfill è vietato a macchina** (LC-3): le righe generate a posteriori portano
   `backfilled: true` e i gate le scartano. La via con cui l'Ispettorato è sembrato vivo **è
   chiusa nel codice**, non nel regolamento.

**E il gate di fallimento ha una data:** 4 settimane dopo E4 senza una traccia nata da sola da un
lavoro reale = fallimento dichiarato. Non «lo sapremo fra tre mesi».

## 28. Cosa V2 NON copre — materia per la critica 2

Dichiarato, non nascosto:

1. **Il numero delle destinazioni mancanti nelle 174 schede** non è misurato: è il primo lavoro di
   E2, e finché non c'è, la stima di E2 ha una coda aperta di 15-22 ore.
2. **E6 non ha ore.** Tre ecosistemi senza motore più l'adattatore APEX-7: stimabili solo dopo E4.
3. **La mappa di conversione dei 10 schemi** è nominata (§13) e non scritta: serve l'elenco
   nominale dei dieci con la loro forma.
4. **E9 non ha gate**, ed è scritto.
5. **Il costo di calendario di E8** dipende da terzi (review KDP 24-72 h a libro, tempi dei
   negozi): non è comprimibile e non è stimato oltre l'ordine di grandezza.
6. **Non ho provato le sette condizioni contro i 15 ecosistemi uno per uno.** So che 0 su 15
   passano C-a..C-d; non ho la lista di cosa manca a ciascuno. È il lavoro che rende `empire vivo
   --json` capace di rispondere davvero, e va fatto in V3.
7. **La riconciliazione con EMPIRE DESK è dichiarata in §19 ma non negoziata con Gael.** Finché non
   la legge, resta una decisione unilaterale scritta.

---

# APPENDICE A — I 41 RILIEVI, E DOVE SONO FINITI

| Critica | Rilievo | Grado | Recepito in |
|---|---|---|---|
| C1 | R-1 APEX-7 anti-modello, 0/15 non 2/15 | FATALE | §3, §13, E6, §26.6 |
| C1 | R-2 nessun denominatore del 100% | GRAVE | **L8** (stato ARCHIVIO), §3, E0.5 punto 7 |
| C1 | R-3 quattro malattie, non una | GRAVE | §5 (tabella causa→cura), **E0.6** |
| C1 | R-4 le condizioni misurano la tubatura | GRAVE | §4.2 (**C-d**), §4.3 (**R-a**), C-b e C-c riscritte |
| C1 | R-5 N4 contraddice §23 | GRAVE | §9-F4: **nessun secondo libro**, la Tesoreria si accende |
| C1 | R-6 l'involucro esiste in doppia copia | GRAVE | §15 (tre classi), E5b |
| C1 | R-7 N1 esiste in miniatura (INV-20) | MEDIO | §9-F1 + **riparazione del ramo `esterno`** |
| C1 | R-8 NEXUS senza proprietario nominato | GRAVE | §10 (tabella con nomi + consumatore) |
| C1 | R-9 il ponte fabbrica doppioni | FATALE | §14 (4 pilastri), E5a, **E5-bis** |
| C1 | R-10 il guardiano esiste smontato in tre pezzi | GRAVE | **E0.7**, §9-F5 |
| C1 | R-11 il Bus senza pompa | GRAVE | §9-F2, E4 (**senza pompa non si costruisce**) |
| C1 | R-12 §14 fonda una quarta classe di ingressi | MEDIO | §15 |
| C1 | R-13 il proprietario non basta: l'Ispettorato | FATALE | **§1 — la legge centrale (LC-1/2/3)** |
| C2 | R-1 Ultimo Metro assente | FATALE | §7-8, **E0 punto 4**, E0.5 punto 1, E8 |
| C2 | R-2 i tre collegamenti prioritari ignorati | GRAVE | **E0.5** |
| C2 | R-3 V1 fondata su censimenti monchi | GRAVE | **§0.3** (fonti riaperte) |
| C2 | R-4 E0 spegne l'outreach | FATALE | **E0** (i 3 `.env` + gate positivo), R6 |
| C2 | R-5 il gate confronta due definizioni | GRAVE | **E1** (gate sugli id, non sui totali) |
| C2 | R-6 il gate di E3 non è valutabile | GRAVE | **campo `origine`** (F3) + gate E3 riscritto |
| C2 | R-7 i gate di E4/E5/E8/E9 non hanno comando | GRAVE | **L9**, tutti i gate riscritti |
| C2 | R-8 la finestra del flow è cosmetica | GRAVE | **E3** (nota (a)) |
| C2 | R-9 E1 costa il doppio | GRAVE | **E1: 13-20 h** + regola di fusione |
| C2 | R-10 E7 costa 69-109 h | GRAVE | **E7 per ondata** + regola di ricalcolo |
| C2 | R-11 la decisione sulle due popolazioni | GRAVE | §14, §26 |
| C2 | R-12 / R-17 i 12 hook senza costruttore | GRAVE | **E0.7** |
| C2 | R-13 E2 premia il punteggio, non il contratto | GRAVE | **E2** (misura + terzo gate + snapshot) |
| C2 | R-14 E5 nasconde tre progetti | GRAVE | **E5a / E5b / E5c** separati |
| C2 | R-15 caduta a metà + daemon di sync | GRAVE | **E1** (commit atomici, daemon sospeso), **E3** (stato prima dell'invio) |
| C2 | R-16 sette punti che stanno solo in una testa | MEDIO | **L10** |
| C2 | R-18 il gate INCASSO legge un flag | FATALE | **E0.5 punto 8** (HTTP ai Payment Link) |
| C2 | R-19 «>25» dista una traccia dal verde | GRAVE | gate E3 come **delta con origine=hook** |
| C2 | R-20 metà scaglioni senza gate | GRAVE | **L9** |
| C2 | R-21 le ore non reggono il conto dei file | GRAVE | **§22** (tabella con tetti) |
| C2 | R-22 E4 si dichiara prerequisito e arriva quarto | MEDIO | E1-E3 si misurano con i comandi esistenti; F3/F4 anticipati (E0.5, E3) |
| C3 | R-1 rimandi a un §30 inesistente | MEDIO | corretto per costruzione |
| C3 | R-2 tabella fonti stantia | GRAVE | **§0.3** |
| C3 | R-3 l'addestramento era già consegnato | GRAVE | **§16** (assorbe 03c) |
| C3 | R-4 l'involucro esiste già | FATALE | §15, E5b |
| C3 | R-5 la fabbrica libri orfana, 6 non 4 | FATALE | §7, **E0.5 punto 5**, E8 |
| C3 | R-6 i numeri dei collegamenti | GRAVE | §0.3, §9-F1, E5c |
| C3 | R-7 manca `cp_id` | GRAVE | **§12** (11 campi) + §26.4 |
| C3 | R-8 il campo `costi` dei 303 checkpoint | MEDIO | **E0.5 punto 3** |
| C3 | R-9 il magazzino pieno | FATALE | **§7, E0 punto 4, E8** |
| C3 | R-10 Gael e Neri non esistono in V1 | GRAVE | **§19** |
| C3 | R-11 nessuna misura fra un gate e l'altro | GRAVE | **§23** (cruscotto quotidiano) |
| C3 | R-12 il piano non sa perdere | GRAVE | **§11, §24, §25, §26** (default) |
| C3 | R-13 le sessioni parallele | GRAVE | **§22** (percorsi) + E1 |
| C3 | R-14 il ponte scarta 162 esecutori | FATALE | **E5-bis** |
| C3 | R-15 nessuno scanner di segreti | GRAVE | **H11** |
| C3 | R-16 Preventa attraversa la catena | FATALE | **§6, E3 riscritta** |

**Dieci FATALI su dieci recepiti.** Nessuno respinto; due (APEX-7, Empire Studio) recepiti come
**decisione dichiarata con default**, che è la forma onesta quando la risposta costa più del
problema.

---

> **Fine di V2.** Ora tocca alla **critica 2**, che per ordine di Max deve essere **più dura della
> prima e sulle scelte architetturali, non sulle sviste**. Le domande che le lascio in eredità,
> perché sono quelle su cui V2 può cadere:
> 1. La **legge del consumatore quotidiano** è davvero una legge, o è la stessa promessa
>    dell'Ispettorato scritta meglio? Cosa impedisce a un consumatore quotidiano di diventare, dopo
>    tre settimane, una riga che nessuno legge?
> 2. **Innestare invece di fondare** protegge dall'organo-di-carta, ma carica cinque funzioni su
>    file che oggi funzionano: qual è il primo file che si rompe, e chi se ne accorge?
> 3. **E0 vale davvero il primo euro?** 26 pezzi caricabili non sono 26 pezzi che qualcuno compra.
>    Il piano misura la pubblicazione: nessun gate misura la **vendita**, e la differenza fra le
>    due è tutto il mestiere.
