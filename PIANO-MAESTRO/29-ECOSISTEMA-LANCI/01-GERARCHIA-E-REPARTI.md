---
Type: PROJECT
Status: Proposta
Tags: #lanci #ecosistema-15 #gerarchia #reparti
Created: 2026-09-05
---

# 01 — GERARCHIA, REPARTI E MACCHINA A STATI

> Terza versione. In fondo, il paragrafo 8 dice cosa è cambiato dalle precedenti e **contro quale
> obiezione** ogni cambiamento è stato fatto.

---

## 1. LA GERARCHIA

### 1.1 I sei livelli

| Liv. | Chi | Natura | N. |
|---|---|---|---|
| **L0** | **Max** (proprietario) · Gael (socio operativo) | Persone. Decidono ciò che è irreversibile e ciò che impegna denaro o reputazione | 2 |
| **L1** | **Board dell'Impero** — direzione generale, ricavi, marketing, finanza, tecnologia, operazioni, forgia | Governo trasversale. Non eseguono: **vietano per materia** | 7 (esistenti) |
| **L2** | **Direzione dell'ecosistema** | Orchestra il lancio; unico interlocutore umano mentre il lancio corre | 1 |
| **L3** | **Capi reparto** | Orchestrano il proprio flusso | 11 |
| **L4** | **Agenti operativi** | Producono artefatti. Un mestiere ciascuno | 30 |
| **L5** | **Gate e Sentinelle** | Validano e bloccano. **Non rispondono al reparto che controllano** | 13 gate + 4 sentinelle |

### 1.2 Le due regole che rendono la gerarchia vera

> **Prima: il livello L5 non risponde a L3.** Un gate che dipende dal capo reparto che deve
> bloccare non è un gate: è un timbro.

> **Seconda: i gate non sono un reparto da chiamare. Sono dentro `lancio avanza`.**
> Non esiste un percorso che fa progredire un lancio saltando un gate. Per saltarne uno bisogna
> smettere di usare il sistema.

**Perché la seconda regola è nata.** Nella prima versione la Qualità era un reparto da attivare, e
un reparto di soli controlli in un'azienda di tre persone è la prima cosa che si taglia quando c'è
fretta: non produce niente di visibile. Adesso il controllo non si può tagliare senza tagliare
anche l'avanzamento.

### 1.3 Poteri, per livello

| Livello | Decide da solo | Fa approvare | Può BLOCCARE | Risponde a |
|---|---|---|---|---|
| **L0 Max** | tutto | niente | tutto | — |
| **L0 Gael** | esecuzione tecnica, scelte di implementazione | prezzo, data, pubblicazione, spesa nuova | qualunque costruzione | Max |
| **L1 ricavi** | struttura dell'offerta e listino | il prezzo finale | un lancio con margine negativo | Max |
| **L1 marketing** | standard dei testi e voce del marchio | cambi di standard | testi sotto soglia · voce violata | Max |
| **L1 finanza** | classificazione delle spese | budget nuovo | **spesa oltre il tetto +10%** · lancio senza pareggio calcolato | Max |
| **L1 tecnologia** | architettura e sicurezza | modifiche a sistemi in produzione | credenziali esposte · pagina che non traccia · riscrittura di ciò che andava avvolto | Max |
| **L1 operazioni** | cadenze e carichi | spostamenti che toccano altri ecosistemi | lancio che sfora la capacità dichiarata | Max |
| **L1 forgia** | forma di agenti e skill | — | **artefatto non ufficializzato** | Max |
| **L1 direzione generale** | priorità fra lanci concorrenti | — | lancio che non muove un obiettivo del trimestre | Max |
| **L2 Direzione** | avanzamento, riassegnazioni, ordini di rifacimento | apertura della vendita · sforamenti · deroghe | l'avanzamento di qualunque fase | L1 e L0 |
| **L3 Capo reparto** | come si esegue il proprio flusso | l'uscita del reparto | l'ingresso, se l'input non è conforme | L2 |
| **L4 Operativo** | niente fuori dal proprio contratto | ogni suo output | niente | L3 |
| **L5 Gate** | superato o bloccato | niente | **la fase che presidia** | L2, mai L3 |
| **L5 Sentinella** | l'allarme | niente | ciò che la sua soglia dichiara bloccante | L2 e il Board di materia |

### 1.4 Le nove decisioni che restano a una persona

| # | Decisione | Perché non è delegabile |
|---|---|---|
| 1 | Il prezzo finale | impegna il posizionamento per anni, non il ricavo di un lancio |
| 2 | La data di apertura | impegna la capacità di tutte le altre linee nello stesso periodo |
| 3 | Aprire e chiudere la vendita | irreversibile verso l'esterno |
| 4 | L'invio reale alla lista | un'email spedita non si richiama |
| 5 | Pubblicare una pagina live | irreversibile e indicizzabile |
| 6 | Pagare o attivare un abbonamento | impegna denaro vero |
| 7 | Derogare a un gate | se un agente potesse derogare, il gate non esisterebbe |
| 8 | Annullare o rinviare | tocca promesse già fatte al pubblico |
| 9 | Il ruolo di un prodotto (in vendita o regalo) | è una scelta di modello di business |

Le 3, 4, 5 e 6 sono la stessa famiglia. **Il sistema le prepara fino all'ultimo centimetro e si
ferma con tutto pronto e una riga che dice cosa manca.**

> ⚠️ **Sei di queste nove passano da Max, che ha altre linee di business.** Il piano ne tiene
> conto in due modi: il reparto Offerta **istruisce** la decisione fino a renderla una conferma
> (dossier 05), e lo stato `SOSPESO` ha **uscite dichiarate** invece di essere un vicolo cieco
> (§4.3). Sono le due correzioni nate dalla critica.

### 1.5 L'escalation — procedura, non principio

1. **T+0** — chi rileva scrive `conflitti/CONF-<data>-<n>.md`: le due posizioni testuali, cosa
   costa cedere per ciascuna, **e la data entro cui serve la decisione**, dedotta dal calendario.
2. **T+0** — il file esiste, quindi la Direzione lo vede. Niente notifiche da costruire.
3. **T+2 ore** — se una delle due posizioni viola un gate esistente, **non è un conflitto**: vince
   il gate. *(Metà dei conflitti muore qui.)*
4. **T+1 giorno** — sale al Board di materia, che decide entro un giorno.
5. **T+2 giorni** — se il Board non decide, o il conflitto è fra due materie, sale a Max.
6. **La regola del silenzio:** senza decisione al momento in cui la fase dipendente deve partire,
   **la fase non parte** e il lancio va in `SOSPESO` — **con la data di revisione compilata**,
   mai vuota. Non esiste *"in mancanza di risposta si procede"*.
7. Ogni conflitto chiuso lascia una riga in memoria. **Al terzo della stessa specie si scrive una
   regola** e non si decide più caso per caso.

### 1.6 Chi produce ≠ chi approva

| Output | Lo produce | Lo valida | Dipende da |
|---|---|---|---|
| `decisione.json` | LAN-STR | `GATE-STR-1` | L2 |
| `ricerca.json` | LAN-INT | `GATE-INT-1` | L2 |
| `certificato-prodotto.json` | LAN-PRD | `GATE-PRD-1/2/3` | L2 |
| `offerta.json` | LAN-OFF | `GATE-OFF-1` **+ firma umana** | L0 |
| `copy/` | LAN-CPY | `GATE-CPY-1` | L2 + marketing |
| `funnel.json` | LAN-FNL | `GATE-FNL-1` | L2 + tecnologia |
| `piano-editoriale.json` | LAN-EDT | `GATE-EDT-1` | L2 |
| `budget.json`, spesa | LAN-TSR | `GATE-TSR-1/2` | L2 + finanza |
| apertura della vendita | LAN-REG | `GATE-REG-1` **+ firma umana** | L0 |
| `debrief.md` | LAN-MEM | LAN-REG controfirma | L2 |

L'ultima riga è deliberata: **la Regia fa il lancio e la Memoria lo giudica; poi la Memoria scrive
il debrief e la Regia lo controfirma.** Nessuno dei due scrive da solo la storia di com'è andata.

---

## 2. I DODICI REPARTI

| # | Sigla | Nome | Missione | Produce | Etichetta | Agenti |
|---|---|---|---|---|---|---|
| 1 | `LAN-STR` | Strategia | decide se il lancio si fa adesso | `decisione.json` | 🔵 avvolge `IB-L2-STRA` | 3 |
| 2 | `LAN-INT` | Intelligence | porta le parole vere e i buchi veri | `ricerca.json` | 🔵 avvolge `08-INTELLIGENCE` | 4 |
| 3 | `LAN-PRD` | Prodotto | certifica che è vendibile | `certificato-prodotto.json` | 🔵 avvolge `IB-L2-PROD` | 5 |
| 4 | `LAN-OFF` | **Offerta** | **istruisce** prezzo e data fino alla firma | `offerta.json` | 🟢 **nuovo** | 3 |
| 5 | `LAN-CPY` | Copy | tutti i testi, nell'ordine giusto | `copy/` | 🔵 avvolge `04-MARKETING/L2-1` | 6 |
| 6 | `LAN-FNL` | Funnel | pagine online **che misurano** | `funnel.json` | 🔵 avvolge + estende | 4 |
| 7 | `LAN-TRF` | Traffico | **traffico a pagamento**: volume, costo, resa | `traffico.json` | 🔵 avvolge `L2-2-Advertising` | 3 |
| 8 | `LAN-EDT` | Editoriale | **contenuti organici** che portano al funnel e **che escono** | `piano-editoriale.json` | 🟡 nuovo che avvolge | 4 |
| 9 | `LAN-TSR` | Tesoro | quanto costa **questo lancio** oggi, e quando rientra | `budget.json` | 🟡 nuovo che avvolge | 3 |
| 10 | `LAN-REG` | Regia | calendario, sincronizzazione, apertura, misura | `calendario.md` | 🔵 avvolge `IB-L2-LANC` (si sposta) | 4 |
| 11 | `LAN-QLT` | Qualità | possiede i **criteri** dei gate | i verbali | 🟢 **nuovo** | 4 + 4 sentinelle |
| 12 | `LAN-MEM` | Memoria | il lancio finito diventa vantaggio | `debrief.md` | 🟢 **nuovo** | 2 |

### 2.1 Le tre sovrapposizioni, risolte

La critica ne ha trovate tre che la versione precedente lasciava aperte. **Ognuna è risolta con un
confine scritto, non con una raccomandazione.**

| Coppia | Il confine |
|---|---|
| **`LAN-TRF` vs `LAN-EDT`** | **La linea è il denaro.** Se per far arrivare quella persona si è pagato, è Traffico. Se non si è pagato, è Editoriale. Un video YouTube organico è Editoriale; lo stesso video messo in campagna diventa **anche** Traffico, con il suo costo, e i due numeri restano separati. *(Perché serve: portare traffico comprato e costruire attenzione organica sono due mestieri, e con un solo proprietario il secondo perde sempre — è più lento e meno misurabile.)* |
| **`LAN-TSR` vs Tesoreria dell'Impero** | **La Tesoreria è la fonte di verità sui soldi dell'azienda. `LAN-TSR` è la fonte di verità sui soldi di *questo lancio*.** Ogni euro nasce nel lancio e **sale** in Tesoreria; non scende mai. Se un euro compare in tutti e due i posti con valori diversi, **ha ragione la Tesoreria**, e la divergenza è un difetto da registrare. `LAN-TSR` **non tiene una contabilità**: tiene il budget di un progetto |
| **`LAN-QLT` vs i reparti** | **La Qualità possiede i criteri, non l'esecuzione.** I gate girano dentro `lancio avanza`; il reparto scrive i file di criterio e le griglie di punteggio, e li mantiene. È un reparto **di normazione**, non di controllo manuale: per questo può esistere in un'azienda di tre persone |

### 2.2 Perché `LAN-MEM` esiste con due agenti soli

La critica ha osservato che ha poco lavoro. **È vero, e la risposta non è gonfiarlo.**

`LAN-MEM` lavora **due volte per lancio**: alla chiusura (debrief e distillazione) e all'apertura
del successivo (consegna degli schemi). Fra i due momenti non fa niente, ed è giusto così.

**Ma non si fonde con la Regia**, e la ragione è nella riga di §1.6: la Regia produce il lancio, la
Memoria lo giudica. Fonderli significa far scrivere a chi ha eseguito il verdetto su come è andata
— che è esattamente la regola *chi produce non approva*, violata nel punto in cui fa più danno,
perché il debrief è ciò che orienta tutti i lanci successivi.

**Due agenti, non tre:** il distillatore e il bibliotecario. Il direttore di reparto è superfluo
per due agenti che girano in sequenza.

---

## 3. LA MEMORIA — è una condizione, non un dovere

### 3.1 Il presidio duro

> **Una fase non si chiude se non ha scritto il suo record di memoria.**
> Il gate della fase, oltre al proprio criterio, verifica che il record esista.
> Nessun record → fase aperta → il calendario non avanza.

Il precedente storico è netto: un modello di memoria progettato bene, quattro spazi definiti, i
proprietari dichiarati, **zero righe scritte**. Non è mancata la progettazione: è mancata una
conseguenza. I presidi morbidi — *"la scrivono gli script"*, *"si legge in fase zero"*, *"l'indice
misura"* — sono tutti saltabili senza che succeda niente.

**Adesso saltarla ferma il lavoro.** È l'unica forma di obbligo che in questa azienda ha funzionato.

### 3.2 Gli spazi

Uno per reparto, più quello comune degli schemi. **Un solo proprietario di scrittura per spazio**:
quando due processi scrivono nello stesso posto, prima o poi uno mente.

| Spazio | Scrive | Contiene | Legge | Ritenzione |
|---|---|---|---|---|
| `memoria/strategia/` | LAN-STR | verdetti, **incluse le idee respinte con la ragione** | tutti | permanente |
| `memoria/intelligence/` | LAN-INT | frasi con fonte, dolori, concorrenti, spazi vuoti | tutti | 12 mesi, poi riverifica |
| `memoria/prodotto/` | LAN-PRD | certificati, bandiere rosse trovate, esiti dei test | PRD, CPY, QLT | permanente |
| `memoria/offerta/` | LAN-OFF | prezzi decisi **e scartati, col perché** | OFF, STR, TSR | permanente |
| `memoria/copy/` | LAN-CPY | testi finali, punteggi, versioni scartate | CPY, FNL, EDT | permanente |
| `memoria/funnel/` | LAN-FNL | strutture, numeri per pagina, esiti dei test | FNL, TRF, REG | permanente |
| `memoria/traffico/` | LAN-TRF | costo per canale, creatività | TRF, TSR, REG | permanente |
| `memoria/editoriale/` | LAN-EDT | piani, resa per formato, contenuti riusabili | EDT, TRF | permanente |
| `memoria/tesoro/` | LAN-TSR | budget, spese, scarti, consuntivi | TSR, REG, Board | permanente |
| `memoria/regia/` | LAN-REG | calendari, verbali, tracciamenti | tutti | permanente |
| `memoria/qualita/` | LAN-QLT | ogni verdetto, **inclusi tutti i blocchi** | tutti | permanente |
| `memoria/pattern/` | LAN-MEM | gli schemi riutilizzabili | **tutti, sempre** | permanente |

**Dodici spazi per dodici reparti**, con l'ultimo condiviso. *(La versione precedente ne contava
undici per dodici reparti: un reparto restava senza spazio. Corretto.)*

### 3.3 Lo schema di un record

```json
{
  "id": "MEM-<REPARTO>-<AAAAMMGG>-<n>",
  "reparto": "LAN-OFF",
  "lancio_id": "string",
  "tipo": "decisione | misura | scarto | esito | conflitto",
  "titolo": "una riga in italiano",
  "corpo": "il contenuto vero",
  "fonti": ["percorso o indirizzo verificabile"],
  "numeri": { "chiave": "valore" },
  "misurato": true,
  "contraddice": ["MEM-..."],
  "scritto_da": "string",
  "scritto_il": "ISO",
  "scaduto_il": null,
  "letto_volte": 0
}
```

Quattro regole ereditate: **un identificativo non si riassegna mai** · un record aggiornato
mantiene il suo identificativo · la deduplicazione è un passo esplicito · `contraddice` è
obbligatorio quando applicabile.

Due nostre: **`misurato: false` significa che nessun gate può usarlo come prova** ·
**`letto_volte` si incrementa**, ed è ciò che permette di sapere se la memoria è viva.

### 3.4 Gli schemi riutilizzabili, e il declassamento

| Forza | Quando ci arriva | Cosa comporta |
|---|---|---|
| **osservazione** | un lancio | si annota, non vincola |
| **indizio** | confermato da un secondo | il capo reparto lo **deve leggere** prima di decidere |
| **regola** | confermato da tre | diventa un gate o una regola di reparto |

**E il verso opposto: smentito due volte, scende di grado.** Una memoria che sale soltanto è una
superstizione con la data.

### 3.5 Contro il marciume

| Come muore una memoria | Presidio |
|---|---|
| si riempie di roba mai riletta | `scaduto_il` + potatura a fine lancio: i record scaduti e mai letti vanno in archivio, **non si cancellano**, ma escono dalla ricerca |
| contiene cose false che nessuno corregge | `contraddice` + il declassamento |
| nessuno la legge | **la scrittura è condizione di chiusura di fase**, e `letto_volte` misura |
| diventa illeggibile | l'indice è **generato**, e riporta record totali e mai-letti. **Sopra il 40% di mai-letti la sentinella lo segnala** |

---

## 4. LA MACCHINA A STATI

> Questa sezione è stata **riscritta per intero** dopo la critica: la versione precedente aveva
> sei difetti, fra cui uno stato senza uscita.

### 4.1 Il diagramma

```
   IDEA ──GATE-STR-1──► VALUTATO ──(respinto)──► ARCHIVIATO
                            │
              GATE-INT-1 + GATE-PRD-1/2/3
                            ▼
                        ISTRUITO
                            │  GATE-OFF-1 ✱ firma umana
                            ▼
                         DATATO ◄──────────────┐
                            │                   │ budget saltato
                sprint: testi + funnel + contenuti
                            ▼                   │
                    IN_PRODUZIONE ──────────────┘
                            │  GATE-REG-1
                            ▼
                         PRONTO ──(un gate rifiuta)──► IN_PRODUZIONE
                            │  ✱ via libera umano
                            ▼
                         APERTO
                            │  ✱ chiusura umana
                            ▼
                         CHIUSO
                            │  GATE-MEM-1
                            ▼
                        APPRESO   ← l'unico finale buono

   Da qualunque stato ──► SOSPESO ──► torna allo stato di partenza (§4.3)
                                 └──► ABORTITO (solo Max)
```

### 4.2 Le transizioni — tutte, nessuna esclusa

| Da → A | Cosa deve essere vero | Chi autorizza | Cosa blocca |
|---|---|---|---|
| IDEA → VALUTATO | le cinque domande hanno risposta scritta | `GATE-STR-1` | una sola risposta negativa |
| **VALUTATO → ARCHIVIATO** | il filtro ha respinto | `GATE-STR-1` | — *(era assente dalla tabella: corretto)* |
| **ARCHIVIATO → IDEA** | l'idea viene riproposta con un elemento nuovo | L2 | se non c'è niente di nuovo, resta archiviata |
| VALUTATO → ISTRUITO | ricerca e certificato accettati | `GATE-INT-1` + `GATE-PRD-*` | frase senza fonte · una bandiera rossa |
| ISTRUITO → DATATO | prezzo e data veri | `GATE-OFF-1` **+ persona** | valori vuoti o evasivi |
| DATATO → IN_PRODUZIONE | calendario generato, budget approvato | LAN-REG + `GATE-TSR-1` | budget assente o pareggio non calcolato |
| **IN_PRODUZIONE → DATATO** | **il budget è saltato durante la produzione** | `GATE-TSR-2` | — *(mancava: uno sforamento uccideva il lancio senza rientro)* |
| IN_PRODUZIONE → PRONTO | le dieci voci vere insieme | `GATE-REG-1` | una sola voce falsa |
| **PRONTO → IN_PRODUZIONE** | un gate rifiuta dopo la sincronizzazione | il gate che rifiuta | — |
| PRONTO → APERTO | via libera | **solo persona** | pagina che non traccia · pagamento non provato |
| APERTO → CHIUSO | data di chiusura raggiunta | **solo persona** | — |
| CHIUSO → APPRESO | debrief con ≥3 schemi e cause scritte | `GATE-MEM-1` | debrief incompleto |
| \* → SOSPESO | decisione mancante alla scadenza, o conflitto non risolto | automatico | — |
| **SOSPESO → stato di partenza** | **la causa del blocco è rimossa** | L2, con verbale | la causa è ancora lì |
| **SOSPESO → ABORTITO** | 90 giorni di sospensione, o decisione | **solo Max** | — |
| \* → ABORTITO | — | **solo Max** | — |

### 4.3 `SOSPESO` — adesso ha un'uscita, e prima non ce l'aveva

**Il difetto, dichiarato:** la versione precedente aveva la riga *"da qualunque stato → SOSPESO"* e
**nessuna riga di ritorno**. Un lancio che entrava in sospensione — e ci entrava
**automaticamente**, per la regola del silenzio, ogni volta che una decisione umana mancava — non
aveva un percorso definito per uscirne. **Il piano creava lo stato di abbandono silenzioso che
dichiarava di voler evitare, e lo raggiungeva da solo.**

**Come funziona adesso:**

```json
{
  "stato": "SOSPESO",
  "stato_di_partenza": "ISTRUITO",
  "bloccato_da": "firma dell'offerta",
  "sospeso_il": "2026-09-20",
  "revisione_il": "2026-09-27",
  "come_si_esce": "python <percorso assoluto>/scripts/lancio.py offerta 2026-10-manuale --firma 47"
}
```

| Campo | Perché è obbligatorio |
|---|---|
| `stato_di_partenza` | **si torna esattamente da dove si è usciti**: senza, uscire significa ricominciare |
| `revisione_il` | mai vuoto. Un sospeso senza data di revisione **è** un abbandono |
| `come_si_esce` | **un comando eseguibile**, non una descrizione |

**A 90 giorni di sospensione il sistema non decide da solo:** propone l'abbandono a Max, con cosa
si salva. Chiudere un lancio è una decisione umana anche quando è ovvia.

### 4.4 Il file di stato, con i percorsi corretti

```json
{
  "lancio_id": "2026-10-manuale-claude-code",
  "stato": "IN_PRODUZIONE",
  "dal": "2026-10-08T11:00:00",
  "fasi": {
    "WF-PRD": { "stato": "chiusa",   "artefatto": "certificato-prodotto.json" },
    "WF-CPY": { "stato": "in_corso", "completate": 6, "totali": 11 },
    "WF-FNL": { "stato": "in_corso", "completate": 4, "totali": 9 },
    "WF-EDT": { "stato": "non_aperta" }
  },
  "gate": { "GATE-STR-1": "PASS", "GATE-OFF-1": "PASS", "GATE-CPY-1": "in_attesa" },
  "handoff_pendenti": [
    { "id": "HO-20261011-3", "da": "LAN-CPY", "a": "LAN-FNL",
      "emesso_il": "2026-10-11", "scade_il": "2026-10-13" }
  ],
  "bloccato_da": null,
  "prossimo_passo": "python \"C:/Users/Utente/Desktop/qui tutto/Digital Empire/company/Ecosistemi/15-LANCI/scripts/lancio.py\" avanza 2026-10-manuale-claude-code",
  "aggiornato_il": "2026-10-11T18:20:00"
}
```

**Due correzioni nate dalla critica, e una è imbarazzante:**

1. **`prossimo_passo` porta un percorso assoluto.** La versione precedente scriveva
   `python -m scripts.lancio ...`, che funziona **solo** se ci si trova dentro `15-LANCI/` — da
   qualunque altra cartella è un errore di modulo non trovato. Il piano stava commettendo
   l'errore che citava due righe sotto come lezione già pagata.
2. **`handoff_pendenti` è un campo di stato.** La versione precedente imponeva che il silenzio non
   valesse come accettazione, ma **non dava a un passaggio non accettato nessun posto dove
   manifestarsi**: restava invisibile finché il calendario non saltava. Adesso ha una scadenza, e
   scaduto diventa un blocco.

### 4.5 Gli stati terminali

| Stato | Cosa resta sul disco | Perché |
|---|---|---|
| **APPRESO** | tutto, più gli schemi promossi nel banco comune | è il caso buono |
| **ABORTITO** | tutto, più `perche-abortito.md` con la ragione **e cosa si salva** | metà del valore di un lancio abortito è nel materiale riusabile: testi e ricerca non scadono con la decisione |
| **ARCHIVIATO** | la cartella con `decisione.json` e la ragione | le idee respinte sono un patrimonio: la sesta volta che rispunta la stessa, si vede che è già stata respinta cinque volte |

---

## 5. LO SCAGLIONE MINIMO — corretto dopo la critica

> ⚠️ **La versione precedente proponeva nove agenti su quattro reparti, e non poteva funzionare.**
> Dimostrazione: nessuno dei nove sapeva produrre `ricerca.json` (è di `LAN-INT`, assente) né
> `certificato-prodotto.json` (è di `LAN-PRD`, assente); e `lan-off-prezzo` — nella scheda scritta
> dal piano stesso — **dichiara di non scrivere `offerta.json`**, che spetta al direttore del suo
> reparto, anch'esso assente. Un lancio avviato così si sarebbe fermato in `VALUTATO` per sempre,
> senza mai produrre prezzo e data: **cioè l'unica cosa per cui l'ecosistema esiste.**

### 5.1 Gli undici agenti veri, su sei reparti

| # | Agente | Reparto | Perché è indispensabile |
|---|---|---|---|
| 1 | `lan-direttore` | Direzione | qualcuno deve orchestrare |
| 2 | `lan-str-filtro` | Strategia | le cinque domande |
| 3 | `lan-int-analista` | Intelligence | senza, `ricerca.json` non esiste e il lancio non lascia `VALUTATO` |
| 4 | `lan-prd-collaudatore` | Prodotto | senza, `certificato-prodotto.json` non esiste |
| 5 | **`lan-off-conductor`** | Offerta | **è l'unico che scrive `offerta.json`** |
| 6 | `lan-off-prezzo` | Offerta | istruisce il prezzo |
| 7 | `lan-off-struttura` | Offerta | il prezzo da solo non è un'offerta |
| 8 | `lan-fnl-verificatore` | Funnel | provare che le pagine misurano |
| 9 | `lan-reg-calendarista` | Regia | il calendario |
| 10 | `lan-reg-tracciatore` | Regia | i numeri durante la vendita |
| 11 | `lan-qlt-gate` | Qualità | il motore che fa funzionare tutti i gate |

*(`lan-segretario` è uscito: lo stato lo tiene `stato_lancio.py`, non serve un agente.)*

### 5.2 La modalità pilota — per il primo lancio, e solo per quello

Il Manuale Claude Code è finito da marzo: la ricerca completa e la certificazione integrale
sarebbero lavoro vero su un prodotto che esiste già. **Ma i gate non si aggirano in silenzio.**

Per il **primo** lancio, `GATE-INT-1` e `GATE-PRD-1/2/3` ammettono una **attestazione firmata**:

```json
{
  "gate": "GATE-PRD-2",
  "esito": "SUPERATO PER ATTESTAZIONE",
  "attestato_da": "Max",
  "attestazione": "Il prodotto è finito dal 07/03/2026, 203 pagine. I sei controlli non sono stati eseguiti.",
  "debito": "collaudo integrale entro il primo lancio successivo",
  "vale_per": "solo-lancio-pilota"
}
```

| Regola | Perché |
|---|---|
| L'attestazione **vale una volta sola**, e il campo `vale_per` lo impone | un'eccezione senza scadenza diventa la regola |
| Genera un **debito scritto** che compare nello stato dei lanci successivi | il gate saltato non sparisce: torna |
| **Non si applica a `GATE-OFF-1`** | il prezzo non si attesta: si firma. È il gate per cui l'ecosistema esiste |

**Questa è la differenza fra un'eccezione progettata e una scorciatoia improvvisata.** La seconda
sarebbe successa comunque, il primo giorno, senza traccia.

---

## 6. IL COLLEGAMENTO CON IL RESTO DELL'IMPERO

| Direzione | Con chi | Cosa passa |
|---|---|---|
| ⬅ ingresso | `02-INFO-BUSINESS` | prodotto finito e confezionamento — **lo crea lui, non noi** |
| ⬅ ingresso | `04-MARKETING` | standard dei testi e voce del marchio — **lo standard è suo** |
| ⬅ ingresso | `08-INTELLIGENCE` | dossier sui concorrenti, con le fonti |
| ⬅ ingresso | `09-OPERATIONS` | capacità disponibile nel periodo |
| ➡ uscita | `03-CONTENT-FACTORY` | brief degli asset — **lei produce, noi ordiniamo** |
| ➡ uscita | `14-TESORERIA` | ricavi e costi reali — **lei è la fonte di verità sui soldi** |
| ➡ uscita | `02-INFO-BUSINESS` | acquirenti e accoglienza, alla chiusura della vendita |
| ➡ uscita | `10-MEMORY` | checkpoint, decisioni, debrief |
| ➡ uscita | `01-AGENCY` | contatti di alto valore emersi dal lancio |
| ↔ | `07-FORGE` | agenti e skill da forgiare e registrare |

---

## 7. LA STRUTTURA DEI FILE

```
company/Ecosistemi/15-LANCI/
├── ECOSISTEMA.md · BACKBONE.md · GOVERNO.md · REGISTRO.md · README.md
├── Reparti/<SIGLA>-<Nome>/
│   ├── REPARTO.md · REGOLE.md
│   ├── agenti/<nome>.md        ← la SPECIFICA (l'agente vero sta in .claude/agents/)
│   ├── workflow/WF-*.md
│   └── memoria/SCHEMA.md
├── workflow/                   i 7 flussi
├── scripts/                    17 file .py — tutto ciò che si esegue
├── schemi/                     gli schemi JSON, uno per artefatto
├── template/                   brief, calendario, debrief, conflitto
├── lanci/<AAAA-MM>-<prodotto>/ ⬅ i lanci veri, uno per cartella
├── memoria/                    ⬅ i dodici spazi
└── tests/                      ogni gate ha un caso che FALLISCE
```

**Cosa NON sta qui, e perché:** gli agenti invocabili vivono in `.claude/agents/`, le skill in
`.claude/skills/`, i comandi in `.claude/commands/`. Claude Code li legge solo da lì. **Un agente
scritto solo in `Reparti/*/agenti/` è una specifica, non un agente** — è il difetto numero uno del
reparto attuale: nove schede, zero agenti invocabili.

**La coppia obbligatoria:** ogni agente esiste **due volte**, la specifica e l'agente vero.
`scripts/registro.py` verifica che nessuna delle due esista senza l'altra.

---

## 8. COSA È CAMBIATO NEI TRE GIRI

| Cambiamento | Contro quale obiezione |
|---|---|
| I gate sono **dentro il comando di avanzamento** | *"un reparto di soli controlli in tre persone è la prima cosa che si taglia"* |
| I reparti si **abilitano a condizione tecnica** | *"niente impedisce di costruirli tutti e dodici"* |
| La memoria è **condizione di chiusura di fase** | *"i tre presidi sono tutti saltabili, e uno identico ha già fallito qui"* |
| **Una sola numerazione** dei gate, col reparto nel nome | *"tre serie diverse rendono illeggibile il sistema a due mesi"* |
| Il reparto Offerta **istruisce** invece di chiedere | *"un gate su una decisione mancante documenta il blocco, non lo scioglie"* |
| `SOSPESO` ha **stato di partenza, data di revisione e comando di uscita** | *"è uno stato senza uscita, e ci si arriva automaticamente"* |
| Aggiunte le transizioni **ARCHIVIATO** e **IN_PRODUZIONE → DATATO** | *"uno sforamento di budget in produzione uccide il lancio per costruzione della tabella"* |
| `handoff_pendenti` è **un campo di stato con scadenza** | *"la regola più rigorosa del capitolo non ha un luogo dove manifestarsi"* |
| `prossimo_passo` porta un **percorso assoluto** | *"il piano commette l'errore che sta citando"* |
| Lo scaglione minimo passa da **9 agenti/4 reparti a 11/6**, con la modalità pilota | *"i nove non possono produrre prezzo e data: il lancio si ferma in VALUTATO per sempre"* |
| Le tre **sovrapposizioni fra reparti** hanno un confine scritto | *"il piano si vieta la duplicazione e poi la commette"* |
| `LAN-MEM` scende a **due agenti**, e si dichiara perché non si fonde con la Regia | *"non ha abbastanza lavoro per esistere"* |
| Gli spazi di memoria passano da **undici a dodici** | *"il conto non torna: un reparto resta senza spazio"* |
