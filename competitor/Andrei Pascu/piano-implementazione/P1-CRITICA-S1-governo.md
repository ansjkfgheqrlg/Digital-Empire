# P1 — CRITICA S1 (GOVERNO / COERENZA / COLLISIONE)

**Bersaglio:** `DRAFT-V1-A-lanci.md` (Doom Bot A, 27+23 azioni, corsie C1/C2) e `DRAFT-V1-B-capacita.md` (Doom Bot B, quattro verdetti go/no-go).
**Angolo:** governo, coerenza interna, rischio di collisione con Gael (`TASK-LANCI-BUILD-W3`).
**Metodo:** ogni riga sotto è stata verificata sul disco il 2026-09-10. Dove non è stato possibile, è scritto "non verificabile da qui".
**Non modificato:** nessun file di produzione. Questo è l'unico file nuovo.

---

## 1. Verifica fatti

| # | Fatto dichiarato nei draft | Dove l'ho verificato | Esito |
|---|---|---|---|
| 1 | `catena.py` non esiste | `ls .claude/skills/fabbrica-siti/scripts/` → solo `canone_sync.py`, `galleria.py` | **VERO** |
| 2 | ADR-024 §4 elenca "gli otto controlli" e §6 dice "il gate non esiste ancora... i quattro controlli sono debito dichiarato" | `company/Memory/decisions/ADR-024-canone-v2-onde-a-b.md` §4/§6 | **VERO ma la fonte citata è internamente incoerente**: il titolo del §4 dice testualmente *"Cosa entra nel gate (**quattro** controlli...)"* e poi elenca **otto** voci numerate 1-8; il §6 riprende "i quattro controlli". Draft A cita entrambe le frasi verbatim (corrette) ma non segnala mai che la propria fonte-cardine si contraddice sul numero — nonostante l'intero §1 del piano si fondi su "gli otto controlli" |
| 3 | ADR-025 decisioni 2, 3, 4 (13 artefatti, registro come unica fonte, 15 agenti) | `company/Memory/decisions/ADR-025-ecosistema-lanci.md`, Decisione 2/3/4 | **VERO**, citazione fedele |
| 4 | Campi reali degli schemi (`offerta`, `previsione`, `funnel`, `copy`, `editoriale`, `ricerca`) | `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/schemi/*.json`, letti per intero | **In gran parte VERO** — con un'eccezione grave: **AP-041** (Draft A) propone di riusare `struttura.soglia_rapporto_minima` di `offerta.schema.json` per un significato diverso da quello che il campo ha oggi. Vedi Colpo #3 |
| 5 | "Sei rossi su sei" di `MT-4GNU` | `company/Memory/tasks/micro/TASK-LANCI-BUILD-W3/MT-4GNU-s2c-sei-test-rossi.md` | **VERO ma mal interpretato**: i sei rossi sono nominati esplicitamente per `GATE-PUB-1, GATE-STR-1, GATE-PRD-1, GATE-INT-1, GATE-PRV-1, GATE-OFF-1`. **`GATE-FNL-1` non è fra questi.** Vedi Colpo #4 |
| 6 | Engagement scoring dichiarato in `revops/SKILL.md` | `.claude/skills/revops/SKILL.md`, righe 85-118 (Lead Scoring) e righe 202-206 (callout) | **VERO**, citazione Draft B fedele con numero di riga esatto |
| 7 | Diff reale `content-forge` vs `content-forge2.0` | `diff .claude/skills/content-forge/SKILL.md .claude/skills/content-forge2.0/SKILL.md` | **VERO** per `SKILL.md` (unica riga diversa: `name:`). Il diff dell'intera cartella (inclusi `.git/`) non è stato concluso per rumore binario — **non verificato oltre `SKILL.md`**, quindi il claim "byte-identiche" di Draft B è verificato solo sul file citato, non sulla cartella intera |
| 8 | `tesoreria/entrate.jsonl` e `spese.jsonl` vuoti | `wc -l company/Memory/tesoreria/entrate.jsonl company/Memory/tesoreria/spese.jsonl` → 0 righe, 0 byte entrambi | **VERO** |
| 9 | Conteggio "17 verdi" (13+4) in `MIGLIORAMENTI-DIGITAL-EMPIRE.md` | file letto per intero, righe 23-39 (tabella 🟢, 13 righe: AP-001,002,003,006,007,009,010,011,012,013,014,015,016) + righe 79-87 (AP-029/030/031/032 = 🟢, AP-033 = 🟡) | **VERO**, conteggio esatto confermato |
| 10 | `company/Ecosistemi/15-LANCI/` esiste | `ls company/Ecosistemi/ \| grep -i lanci` → nessun risultato | **FATTO AGGIUNTIVO NON DICHIARATO CON QUESTA FORZA**: la cartella **non esiste ancora sul disco**. Draft A lo ammette come "debolezza #1" (§10) ma in forma attenuata ("i path sono ipotizzati"); in realtà l'intera corsia C2 del piano è, al 2026-09-10, riservata a **zero file reali** |
| 11 | AP-034→AP-060 "23 nuovi" (Draft A §0.1) | conteggio manuale di tutti gli ID usati nel documento | **FALSO/GONFIATO**: gli ID interi usati sono 22 (034-044 e 050-060), più tre suffissi "b" (046b, 047b, 048b) che condividono slot mai emessi come numeri pieni. **045 e 049 non compaiono mai, in nessuna forma.** 22+3 ≠ 23 in nessuna lettura coerente. Vedi Colpo #6 |

---

## 2. Colpi ordinati per gravità

### Colpo #1 (GRAVISSIMO) — AP-034 è "rango 1" ma non è collegato a nessun gate reale

Draft A dichiara `catena.py` (AP-034) l'azione a **priorità massima** dell'intero piano (§1: *"l'azione con la priorità più alta del piano intero"*; §8 rango 1: *"nessuna dipendenza, si può fare oggi"*). La motivazione è che diventerebbe *"il primo gate obbligatorio dell'ecosistema LANCI"*, citando ADR-024 §4.

**Prova che questo non è vero nel registro che governa davvero i lanci.** `GATE-FNL-1.criterio_eseguibile`, letto per intero in `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml` (riga 359 e seguenti):

```
ogni pagina risponde 200 AND ogni pagina ha evento_conversione con
prova.origine=='piattaforma' AND prova_cassa.stato=='incassato_e_rimborsato'
AND prova_cassa.riferimento_transazione != null
```

Zero menzione di `catena.py`, zero menzione degli otto controlli di ADR-024. **Nessuna delle 27+23 azioni del piano propone di estendere `GATE-FNL-1.criterio_eseguibile` con "AND catena.py exit 0".** La verifica finale del piano stesso (§11) controlla solo `ls catena.py` e `python catena.py --help` — mai che un gate lo *chiami*.

**Conseguenza:** se il piano viene eseguito alla lettera, `catena.py` nasce come script isolato che nessun gate consuma — esattamente il difetto che ADR-019 castiga per i motori di orchestrazione (*"133 file che nessuno chiama non sono un motore: sono un progetto"*) e che ADR-016/Ultimo Metro castiga per i contenuti (*"lavoro finito che non esce"*). Qui è lavoro finito che nessun gate invoca.

**Riparazione:** aggiungere un'azione esplicita (assente oggi) che estende `GATE-FNL-1.criterio_eseguibile` con la chiamata a `catena.py` e ne fa un `AND` bloccante, con relativo test rosso in `registro.yaml`. Finché questo non esiste, declassare AP-034 dal rango 1: costruire lo script non chiude nessun gap dichiarato, lo predispone soltanto.

---

### Colpo #2 (GRAVE) — AP-038 viola la corsia C2 che il piano stesso ha definito

Draft A §0.3 definisce la corsia C2 come *"riservata a Gael"* per `company/Ecosistemi/15-LANCI/**`, con collisione dichiarata **"alta"**.

AP-038 (le 22 formule retoriche) dichiara: **DOVE** = `company/Ecosistemi/15-LANCI/copy/libreria/formule/01..22.md` — un path che sta **letteralmente dentro** il perimetro che il piano stesso ha appena marcato C2. Eppure **CORSIA: C1**, e nella tabella maestra §5.1 questa azione è schierata *"Parallelo a S0... su una sessione diversa da quella di Gael"*.

Il confronto con AP-037 (stessa identica sotto-cartella, `copy/libreria/`) rende la contraddizione evidente: AP-037 dichiara correttamente **"CORSIA: C2 (cartella) + C1 (contenuto)"** — la distinzione fine che ci si aspetterebbe. AP-038, sulla stessa identica cartella, salta quella distinzione e dichiara **C1 secco**.

**Aggravante verificata sul disco:** `company/Ecosistemi/15-LANCI/` non esiste ancora (vedi tabella fatti, riga 10). Quindi AP-038, se eseguita "subito, in parallelo a S0" da una sessione diversa da Gael come prescritto, sarebbe la prima a **creare** quella cartella — dentro il perimetro che il piano ha dichiarato esclusivo di Gael, prima ancora che Gael l'abbia toccata. È l'esatta situazione che la nota del piano in §0.3 dice di voler evitare (*"nessuna azione di corsia C1... nessuna azione di corsia C2 viene eseguita da una sessione diversa"*).

**Riparazione:** AP-038 va riclassificata C2(cartella)/C1(contenuto) come AP-037, o subordinata all'apertura della cartella da parte di Gael in `MT-9ADD`/`MT-GEKH`.

---

### Colpo #3 (GRAVE) — AP-041 riusa un campo esistente con un significato diverso

`offerta.schema.json`, `struttura.soglia_rapporto_minima`, esiste già oggi con questa descrizione testuale nello schema:

> *"Parametro del listino, non costante sparsa in due documenti. Dichiarata provvisoria: ereditata dal materiale storico e mai misurata su questa azienda."*

Il campo è la soglia minima del **rapporto valore/prezzo** (default 3), usata in `GATE-OFF-1` per la struttura `rapporto_valore_prezzo`.

AP-041 (Draft A §4.2, Blocco 2) propone: *"Soglia dichiarata in `GATE-CPY-1`, parametrizzata come `soglia_rapporto_minima` di `offerta.schema.json` (stessa disciplina: parametro, non costante sparsa)"* — ma la soglia che AP-041 vuole parametrizzare è tutt'altra cosa: **il numero minimo di fonti esterne** richieste in base alla fascia di prezzo, per `GATE-CPY-1`, non `GATE-OFF-1`.

Sono due gate diversi, due semantiche diverse, **lo stesso nome di campo**. Se implementato alla lettera, o si rompe silenziosamente `GATE-OFF-1` (che leggerebbe un numero con un significato diverso da quello con cui è stato progettato), o serve comunque un campo nuovo — cosa che il piano non dichiara, mentre rivendica esplicitamente di seguire "la stessa disciplina" anti-costante-sparsa. È il difetto opposto di quello che dice di evitare.

**Riparazione:** nuovo campo dedicato (es. `soglia_fonti_esterne_minima`), non riuso del nome esistente.

---

### Colpo #4 (MEDIO-GRAVE) — la "nota sul conteggio dei sei rossi" (§3.11) è un falso allarme, e lo dimostra che il file non è stato aperto

Draft A, §3.11, si preoccupa che il settimo test rosso di AP-008 (per `transizioni[]`, che estende `GATE-FNL-1`) faccia "uscire sette su sei" da `MT-4GNU`, e propone come riparazione di spostarlo in `tests/rossi/s3/`.

Aprendo `MT-4GNU-s2c-sei-test-rossi.md` (riga 9-10): i sei rossi di quella micro-task sono nominati **per nome esatto**: `GATE-PUB-1, GATE-STR-1, GATE-PRD-1, GATE-INT-1, GATE-PRV-1, GATE-OFF-1`. **`GATE-FNL-1` non è fra questi** — è coperto altrove, dentro `MT-GEKH` (S3, "dal prezzo all'apertura", che include esplicitamente `ART-FNL + GATE-FNL-1 + lan-fnl-costruttore`).

Quindi il rosso di AP-008 non sarebbe mai potuto finire in `MT-4GNU` in primo luogo, indipendentemente da come lo si scrive: l'avvertimento risolve un problema che, verificato, non esiste nella forma descritta. Non è un errore grave in sé (la cautela non fa danno), ma è la prova che Draft A ha scritto l'avvertimento **senza aprire il file che cita** — un controllo di trenta secondi che il piano stesso, altrove, pretende da chi lo esegue (§11, "comandi, non dichiarazioni").

---

### Colpo #5 (MEDIO) — canale parallelo non riconciliato fra il piano e la task che Gael sta già eseguendo

`TASK-GAEL-20260908-SETTIMANA-03.md`, task 4️⃣ (`TASK-LANCI-FUNNEL-W3`), istruisce Gael **direttamente e già oggi**:

> *"ogni pagina del funnel... va misurata contro lo studio già sul disco di Andrei Pascu — `competitor/Andrei Pascu/`: la scala prezzi 98→434→999..., le pre-casse..., le 86 parole..."*

Questo è **esattamente** il contenuto che Draft A instrada attraverso un secondo canale formale — AP-041 (scala prezzo/fonti), AP-035 (generatore pre-cassa), AP-058 (86 parole) — ciascuno con un proprio nuovo campo di schema, un proprio criterio di gate, una propria micro-task di destinazione.

Non è un doppione di testo, è un **doppio binario di governo** sullo stesso materiale: Gael è già autorizzato e istruito a leggere e applicare lo studio direttamente nel costruire il funnel (task madre, 08/09), mentre Draft A (09/09) costruisce un percorso parallelo — schema, gate, amendment — per "consegnargli" lo stesso materiale un giorno dopo. Rischio concreto: Gael applica la scala prezzo/fonti a modo suo in `MT-GEKH` prima che AP-041 esista come criterio codificato, rendendo il criterio proposto da Draft A retroattivamente incoerente con quanto già costruito, o ridondante.

**Riparazione:** il piano dovrebbe dichiarare esplicitamente il rapporto fra le proprie azioni C2 e l'istruzione diretta già data a Gael in 4️⃣ — non lo fa in nessun punto.

---

### Colpo #6 (MEDIO) — la numerazione AP-034→AP-060 non torna, buchi non dichiarati

Draft A, §0.1: *"AP-034 → AP-060 (23 nuovi)"*.

Contando tutti gli ID realmente usati nel corpo del documento: `034, 035, 036, 037, 038, 039, 040, 041, 042, 043, 044` (11) + `050, 051, 052, 053, 054, 055, 056, 057, 058, 059, 060` (11) = **22 numeri interi**. Più tre suffissi che condividono slot mai emessi come numeri pieni: `046b, 047b, 048b`.

**`045` e `049` non compaiono in nessuna forma, in nessun punto del documento.** Non sono nemmeno riservati con un placeholder ("saltato apposta"): sono assenti e silenziosi — esattamente il tipo di buco che la stessa Draft A rimprovera al briefing originale in apertura (§0.2, "correzione di fatto"). 22 interi + 3 "b" non fanno "23 nuovi" in nessuna lettura: sono 25 voci se si contano i "b" come azioni a sé, o 22 se non li si contano. In nessun caso il totale dichiarato è esatto.

---

### Colpo #7 (LIEVE-MEDIO) — la scappatoia `non_misurato` di AP-057 non è supportata dallo schema come scritto

AP-057 propone che, quando `evento_conversione.prova.origine` è impossibile da leggere su una pagina di consegna dietro login, *"si dichiara `non_misurato` (campo che lo schema ha già) invece di rendere il gate insoddisfacibile"*.

Verificato `funnel.schema.json`: `pagine[]` ha `evento_conversione` come campo **obbligatorio** (`"required": ["ruolo", "url", "codice_http", "evento_conversione"]`), e dentro `evento_conversione`, `prova` è a sua volta obbligatoria con `origine` come **enum chiuso** (`piattaforma-misura`, `registro-server`, `fornitore-pagamento`) — nessun valore tipo "non misurato" è ammesso lì. `non_misurato` esiste sì nello schema, ma come **array di stringhe libere a livello radice del documento**, non come valore alternativo dentro `pagine[].evento_conversione.prova.origine`.

La scappatoia descritta da AP-057 non è quindi "già gestita dal campo esistente" come il piano afferma: servirebbe comunque una modifica di schema (rendere `evento_conversione` opzionale per `ruolo: "consegna"`, o aggiungere un valore ammesso), che AP-057 non dichiara come necessaria.

---

## 3. Azioni da UCCIDERE

| Azione | Perché uccidere (non solo declassare) |
|---|---|
| **AP-034 come "rango 1" nella forma attuale** | Non uccidere lo script — uccidere la sua priorità dichiarata e la frase "primo gate obbligatorio di LANCI" finché nessuna azione lo cabla dentro `GATE-FNL-1.criterio_eseguibile` (Colpo #1). Nella forma scritta oggi produce un falso senso di urgenza risolta |
| **La riparazione di AP-057 così com'è** | La frase "si dichiara `non_misurato`, campo che lo schema ha già" va tolta: non è vera contro lo schema reale (Colpo #7). Va sostituita con una modifica di schema dichiarata |
| **La nota §3.11 sul "settimo rosso in `MT-4GNU`"** | Va tolta, non archiviata: risolve un problema inesistente (Colpo #4) e occupa spazio in un piano che si vanta di "comandi, non dichiarazioni" |

## 4. Azioni da FONDERE

| Fondere | Con | Perché |
|---|---|---|
| **AP-035 (generatore pre-cassa), AP-041 (scala fonti/prezzo), AP-053 (qualificazione negativa), AP-058 (86 parole)** | in un unico "digest operativo per `MT-GEKH`" allegato a `TASK-LANCI-FUNNEL-W3` | Sono la stessa famiglia di misure che la task madre già chiede a Gael di leggere direttamente da `competitor/Andrei Pascu/` (Colpo #5). Quattro azioni separate, quattro criteri di gate separati, moltiplicano il rischio di canale parallelo invece di ridurlo |
| **AP-038** | il trattamento di corsia di **AP-037** | Stessa cartella (`company/Ecosistemi/15-LANCI/copy/libreria/`), deve ereditare la stessa regola C2(cartella)/C1(contenuto) — non restare C1 secca (Colpo #2) |
| **AP-012 di Draft B (Artefatto 1, vocabolario tag comportamentali email)** | **AP-059 di Draft A (vocabolario leve d'offerta, `09-VOCABOLARIO-LEVE.md`)** | Non sono lo stesso contenuto, ma sono due "vocabolari" nascenti nello stesso ecosistema LANCI, proposti separatamente da due Doom Bot che non si sono letti (dichiarato in apertura di Draft B: "coperto in parallelo"). Vanno almeno cross-linkati nello stesso documento o dichiarati esplicitamente come glossari distinti, altrimenti l'ecosistema nasce con due indici lessicali paralleli |

## 5. Contraddizioni con gli ADR

- **Nessuna violazione diretta trovata** di ADR-003 (Draft A rispetta il wrap su AP-056/AP-004), ADR-023 (AP-042/043 dichiarano correttamente "estende, non sostituisce"), ADR-005 (entrambi i draft instradano gli item minori a BACKLOG correttamente).
- **ADR-028 punto 4** ("mai 'non negoziabile' senza dire esattamente cosa blocca"): Draft A lo rispetta esplicitamente in ogni riga "BLOCCA" e nel §7. **Ma c'è una violazione sostanziale non dichiarata a livello di invariante**: ADR-025 INV-04 impone che *"ogni gate ha un `test_rosso` dichiarato"* — un controllo (AP-034) costruito e non collegato a nessun gate non è tecnicamente in violazione di INV-04 (perché non è lui stesso un gate), ma vanifica lo spirito della regola: un controllo che dovrebbe *diventare* un gate e non lo diventa mai è, nella pratica, peggio di un gate con un test rosso debole — non verrà mai derogato perché non verrà mai invocato (Colpo #1). Il piano cita 04-COSTRUZIONE.md §9 su questo esatto rischio ("un controllo che sbaglia spesso viene derogato") senza notare che la propria costruzione rischia la variante peggiore: non derogato, semplicemente ignorato.
- **ADR-026** (piena autorità di Gael): Draft B la invoca per decidere la tensione breakdown-prezzi al posto di Max (AP-006, patch B) — uso difendibile (è una regola di processo, non un valore di `PU-PREZZO`, che resta riservato) ma al limite, e Draft B lo dichiara onestamente come propria debolezza #4. Non lo classifico come violazione.

## 6. LA MIA OBIEZIONE PIÙ FORTE

**AP-034 (`catena.py`) è dichiarata l'azione a rendimento più alto e priorità massima dell'intero piano, ma nessuna delle 50 azioni combinate dei due draft aggiunge la riga che collegherebbe lo script a un gate reale.** `GATE-FNL-1.criterio_eseguibile`, verificato parola per parola in `dati/registro.yaal` — anzi `registro.yaml` — oggi non nomina né `catena.py` né gli otto controlli di ADR-024. Il piano costruisce l'intera sua argomentazione di apertura (§1, "il ritrovamento che viene prima di tutti gli altri") sul presupposto implicito che scrivere lo script equivalga a colmare il gap che ADR-024 §4 dichiara — e poi non propone mai, in nessuna delle 60 azioni numerate, l'unica riga di `criterio_eseguibile` che renderebbe vera quella equivalenza. È lo stesso difetto — quasi lo stesso identico meccanismo — che il piano condanna nel concorrente (la cassa vera non linkata da nessuna parte: la pagina funziona benissimo, il gate esiste, ma il collegamento fra i due manca) e negli ecosistemi interni già puniti da ADR-016 e ADR-019 (lavoro finito che nessuno consuma). Finché questa riga non esiste, "rango 1" è un'etichetta, non un fatto verificabile — ed è precisamente la distinzione che questo stesso piano, altrove, chiede a tutti gli altri di rispettare.

---

## Connessioni
- `competitor/Andrei Pascu/piano-implementazione/DRAFT-V1-A-lanci.md`
- `competitor/Andrei Pascu/piano-implementazione/DRAFT-V1-B-capacita.md`
- `company/Memory/decisions/ADR-024-canone-v2-onde-a-b.md`, `ADR-025-ecosistema-lanci.md`, `ADR-026-...md`, `ADR-028-niente-blocca-tutto.md`
- `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/registro.yaml`, `dati/schemi/*.json`
- `company/Memory/tasks/TASK-GAEL-20260908-SETTIMANA-03.md`, `tasks/micro/TASK-LANCI-BUILD-W3/MT-4GNU-*.md`, `MT-GEKH-*.md`
