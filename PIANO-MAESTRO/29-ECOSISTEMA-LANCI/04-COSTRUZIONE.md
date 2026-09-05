---
Type: PROJECT
Status: Proposta — versione 4
Tags: #lanci #ecosistema-15 #costruzione #scaglioni #pre-mortem
Created: 2026-09-05
Last updated: 2026-09-05
Versione: 4
---

# 04 — LA COSTRUZIONE

> **Regola di lettura:** questo documento spiega. Il registro decide.
> Se una riga qui contraddice `dati/registro.yaml`, ha torto questa riga.

---

## 1. IL PRINCIPIO DI ORDINAMENTO

La versione 3 ordinava la costruzione per **completezza**: prima l'infrastruttura, poi i reparti,
poi il lancio. Con quell'ordine, il primo euro arrivava dopo 54-72 ore-uomo di lavoro su cose che
nessuno aveva ancora provato a usare.

Questa versione ordina per **una regola sola**:

> **Si costruisce solo ciò che serve al prossimo passo di un lancio vero che sta già camminando.**

La conseguenza pratica è che **i primi due scaglioni non contengono una riga di codice**. Non è
pigrizia: è il modo di scoprire quale software serve davvero, invece di dedurlo. Un ecosistema
progettato prima di aver visto un lancio soffrire è un ecosistema progettato contro i problemi
immaginati.

**E c'è una ragione più dura,** già misurata in questa azienda: esistono sette motori di
orchestrazione con zero consumatori (ADR-019). Costruire prima di avere un consumatore è l'errore
che questa azienda commette con più costanza. Qui il consumatore — un lancio vero — viene prima.

---

## 2. GLI SCAGLIONI

| # | Nome | Contiene codice? | Ore-uomo | Non parte se |
|---|---|---|---|---|
| **S0** | La catena dell'incasso | **no** | 6-10 | — è il primo |
| **S1** | Il primo lancio a mano, fino alla firma | **no** | 5-9 | S0 non è chiuso |
| **S2** | La macchina minima | sì | 45-65 | S1 non è chiuso |
| **S3** | Dal prezzo all'apertura | sì | 35-50 | S2 non è chiuso |
| **S4** | La chiusura e la memoria | sì | 15-22 | S3 non è chiuso |
| **S5** | Il governo: osservabilità e comandi | sì | 12-18 | S4 non è chiuso |
| | **Totale** | | **118-174** | |

**Le condizioni di sblocco non sono opinioni: sono comandi.** Ognuna è al §3, e o esce zero o lo
scaglione non è chiuso, per quanto lavoro sia stato fatto.

---

## 3. SCAGLIONE PER SCAGLIONE

### S0 — La catena dell'incasso · 6-10 ore · nessun codice

**Cosa si fa:** si rende l'azienda capace di ricevere un euro e restituirlo.

| # | Gesto | Fatto quando |
|---|---|---|
| 0 | **Sostituire la chiave del servizio di posta**, pubblica da mesi | la vecchia chiave non funziona più **sul servizio** (B-020) |
| 1 | Collegare una cassa a una pagina qualunque | esiste un indirizzo dove si può pagare |
| 2 | Pagare davvero, con una carta vera | la transazione compare nel pannello del fornitore |
| 3 | Farsi arrivare il prodotto | il file arriva a chi ha pagato, senza intervento umano |
| 4 | Rimborsare quel pagamento | il rimborso compare nel pannello |
| 5 | Installare la misura e vedere l'evento d'acquisto | l'evento compare nello strumento di misura |
| 6 | **Annotare le commissioni lette sulla transazione** | il numero entra nel documento 02, §8, riga 5 |

**Condizione di sblocco — eseguibile da chiunque, senza fidarsi di nessuno:**

> Aprire il pannello del fornitore di pagamento e vedere, **sulla stessa transazione**: un incasso,
> una consegna, un rimborso. E nello strumento di misura, l'evento corrispondente.

**Se non si chiude in 16 ore-uomo, si ferma tutto** (condizione di abbandono 1, §6).

> **Perché la sicurezza sta al gesto zero e non in fondo.** La chiave esposta cresce di valore ogni
> giorno che resta valida, e sostituirla richiede dieci minuti. È l'unico gesto dell'intero piano
> che costa meno di quanto costa rimandarlo di un giorno.

### S1 — Il primo lancio a mano, fino alla firma · 5-9 ore · nessun codice

**Cosa si fa:** si porta un lancio vero — il Manuale — da `IDEA` a `DATATO` **compilando a mano i
file**, validati contro gli schemi che già esistono.

| # | Artefatto | Come | Ore |
|---|---|---|---|
| 1 | `pubblico.json` | a mano, canale per canale, con la prova di ogni numero | 2-4 |
| 2 | `certificato.json` in modalità **retroattiva** | il prodotto esiste già: sei bandiere rosse, link testati, `debito_collaudo` dichiarato | 1-2 |
| 3 | `previsione.json` | la formula del documento 02, rifatta su un foglio | 1-2 |
| 4 | `offerta.json` | fasi O1-O5 del documento 03, **fino alla firma** | 1-2 + il tempo della firma |

**Condizione di sblocco:**

```bash
# i quattro file esistono e passano la validazione contro i propri schemi
python -c "import json,jsonschema,sys; ..."   # o qualunque validatore di schema
```

più **la firma vera di Max su un prezzo e una data**.

> **Questo scaglione è il vero collaudo del piano.** Se compilare quattro file a mano seguendo gli
> schemi risulta impossibile o assurdo, il difetto è negli schemi, e si scopre qui — dove costa
> ore — invece che dentro il codice, dove costa giorni.
>
> **E se il lancio non supera S1, non serve nessun software:** significa che il problema
> dell'azienda non è l'automazione.

### S2 — La macchina minima · 45-65 ore

**Cosa si costruisce**, e niente altro:

| Pezzo | Ore | Contenuto |
|---|---:|---|
| `stato_lancio.py` + comando `lancio` | 8-12 | crea, legge, elenca; `stato.json` con lock su file |
| Caricamento e validazione degli artefatti | 4-6 | un artefatto è valido solo contro il proprio schema, ricalcolato |
| `avanza` | 10-14 | la firma del documento 01 §2: lock esclusivo, idempotenza, codici 0/1/2/3, verbali |
| Il ponte verso gli agenti | 6-10 | ADR-014: prompt da standard input, identificativo esplicito del modello, `total_cost_usd` letto e budget verificato **prima** della chiamata, `registro-chiamate.jsonl` |
| I sei controlli di questa metà | 12-18 | `GATE-PUB-1`, `GATE-STR-1`, `GATE-PRD-1`, `GATE-INT-1`, `GATE-PRV-1`, `GATE-OFF-1` — **ognuno col suo test rosso scritto prima** |
| I sei agenti di questa metà | 5-8 | `lan-pub-censore`, `lan-str-filtro`, `lan-prd-collaudatore`, `lan-int-analista`, `lan-prv-modello`, `lan-off-conductor`, più `lan-gate` |

**Condizione di sblocco — è la stessa della versione 3, ed era la cosa migliore che aveva:**

```bash
python -m scripts.lancio crea prova-vuota --prodotto "Prova"
python -m scripts.lancio avanza prova-vuota
```

> **Deve bloccarsi al controllo dell'offerta**, uscire con codice **1**, scrivere il verbale, e
> lasciare lo stato dov'era.
>
> **Se esce zero, S2 non è chiuso**, per quanto codice sia stato scritto. Un sistema che lascia
> passare un lancio senza prezzo è il sistema che c'è già oggi, con più file dentro.

**E la seconda condizione, che la versione 3 non aveva:**

```bash
# i test rossi dei sei controlli girano e FALLISCONO come devono
python -m pytest tests/rossi/ -v
```

Un controllo senza un caso che lo faccia fallire è decorativo per costruzione (INV-04).

### S3 — Dal prezzo all'apertura · 35-50 ore

| Pezzo | Ore |
|---|---:|
| `ART-CPY` + `GATE-CPY-1` + `lan-cpy-conductor` | 12-16 |
| `ART-FNL` + `GATE-FNL-1` + `lan-fnl-costruttore` — **inclusa la prova di cassa** | 10-14 |
| `ART-EDT` + `GATE-EDT-1` + `lan-edt-pianificatore` | 6-9 |
| `ART-BDG` + `GATE-TSR-1` + `GATE-TSR-2` + `lan-tsr-contabile` | 4-6 |
| `ART-APE` + `GATE-REG-1` + `lan-reg-calendarista` | 3-5 |

**Condizione di sblocco:** un lancio di prova arriva a `PRONTO` e **si ferma lì**, perché
`PU-APERTURA` non ha default e non ce l'avrà mai.

### S4 — La chiusura e la memoria · 15-22 ore

| Pezzo | Ore |
|---|---:|
| `ART-CNS` + `GATE-CNS-1` + `lan-reg-tracciatore` | 6-9 |
| `ART-DBR` + `GATE-MEM-1` + `lan-mem-distillatore` + controfirma | 6-9 |
| Il ponte verso la Tesoreria | 3-4 |

**Condizione di sblocco:** un lancio chiuso arriva ad `APPRESO`, e il debrief contiene **almeno tre
schemi con `si_applica_quando` non vuoto**.

### S5 — Il governo · 12-18 ore

| Pezzo | Ore |
|---|---:|
| `lancio blocchi` — **il comando più importante del sistema** | 3-4 |
| `lancio costi` — letto dal registro delle chiamate, mai stimato | 2-3 |
| `lancio elenco` con giorni di fermo e causa | 2-3 |
| Il promemoria giornaliero sui lanci non chiusi | 2-4 |
| `lan-direttore` | 3-4 |

**Condizione di sblocco:** `lancio blocchi` mostra, in una schermata, tutti i punti umani aperti
dell'azienda ordinati per giorni di attesa. **Se quel comando fosse esistito, il Manuale non
sarebbe stato fermo sei mesi in silenzio.**

---

## 4. LA STIMA — metodo, e dove sbaglia

### 4.1 Cosa c'è dentro le ore

Le stime del §2 **includono** ciò che le stime software di solito dimenticano, e che i revisori
hanno segnalato come il difetto tipico:

| Voce | Inclusa | Nota |
|---|---|---|
| scrivere il codice | sì | |
| **scrivere i test rossi** | sì | uno per ogni controllo: 14 in tutto |
| **l'integrazione fra i pezzi** | sì | è la voce che fa sbagliare le stime di 2-3 volte quando è omessa |
| **il debug del ponte verso gli agenti** | sì | ADR-014 dice che quel ponte ha già fatto perdere tempo tre volte |
| la scrittura degli agenti | sì | |
| **il lavoro sui dati reali** (compilare gli artefatti del lancio vero) | sì, in S0 e S1 | |
| il tempo delle firme umane | **no** | non è ore-uomo di costruzione: è attesa, e ha le sue scadenze |
| la produzione dei contenuti del lancio | **no** | è lavoro di lancio, non di costruzione |

### 4.2 L'onestà sulla stima

**Questa stima è un'assunzione, non una misura.** Non esiste in azienda una misura di quante ore
costa costruire un ecosistema, perché nessuno l'ha mai registrata.

La banda 118-174 ore ha un rapporto di 1,47 fra estremo alto e basso. **È stretta per un lavoro
mai fatto prima**, e va trattata con la regola del documento 02: finché un numero è assunto, si
pianifica sul valore peggiore. **Si pianifichi su 174 ore.**

A tre ore al giorno sono circa **due mesi di calendario**, e la condizione di abbandono 3 dice cosa
succede se il pilota non esce entro 45 giorni dal giorno zero.

**La prima misura vera arriva alla fine di S2:** se S2 costa più del 40% oltre la stima alta, le
stime di S3-S5 vanno rifatte prima di proseguire, non dopo.

---

## 5. IL PRE-MORTEM

> Il metodo: si assume che fra tre mesi il progetto sia fallito, e si scrive **perché**. Ogni causa
> porta la propria contromisura e — più importante — **il segnale che la vede arrivare**.

| # | È fallito perché… | Probabilità | Contromisura | Segnale precoce |
|---|---|---|---|---|
| **1** | La firma sul prezzo non è mai arrivata, di nuovo | **alta** — è già successo per sei mesi | `PU-RUOLO` con default reversibile a 7 giorni; `PU-PREZZO` con `SOSPESO` a 14 | `lancio blocchi` mostra un punto umano aperto da più di 5 giorni |
| **2** | Si è costruito il sistema e non si è mai lanciato | **alta** — l'azienda ha 25 pezzi finiti mai usciti (ADR-016) e sette motori con zero consumatori (ADR-019) | S0 e S1 non contengono codice; S2 non parte finché un lancio vero non ha una firma | S2 comincia senza che S1 sia chiuso |
| **3** | La catena dell'incasso non si chiude | media | condizione di abbandono 1: 16 ore e si ferma tutto | il gesto 2 (pagare davvero) non riesce al primo tentativo |
| **4** | Il pubblico verificato è troppo piccolo perché un lancio abbia senso | **media-alta** — il canale previsto è spento dal 29/07/2026 | condizione di abbandono 2 | `pubblico.json` con totale sotto le poche centinaia |
| **5** | Il costo delle chiamate sfonda il tetto e il lancio si ferma a metà | media | tetto a 15 $, lavoro a blocchi, calcoli deterministici fuori dai modelli, costo letto prima di ogni chiamata | `lancio costi` supera 8 $ prima dello stato `DATATO` |
| **6** | Gli agenti «riparano» i propri blocchi scrivendo firme | **bassa ma catastrofica** | firma come oggetto, canali in lista chiusa, nessun permesso di scrittura, impronta del testo | un verbale mostra una firma con canale non ammesso |
| **7** | Due macchine si pestano i piedi sullo stesso repository | media | lock esclusivo su `avanza`; blocco di coordinamento in `STATO-EMPIRE.md` prima dei lavori grossi | due verbali con lo stesso nome, o uno stato riscritto due volte |
| **8** | Il piano diventa carta come il precedente | media | il registro è validato da un programma; ogni scaglione chiude con un comando che esce zero | uno scaglione dichiarato chiuso senza il suo comando |
| **9** | Si costruisce l'ottavo motore di orchestrazione | bassa | documento 01 §6: questo lavoro non ne ha bisogno; la decisione va registrata in ADR-019 | compare una cartella `orchestrator/` o simile |
| **10** | Il primo lancio va male e il sistema viene abbandonato per delusione | media | S4 e il debrief esistono apposta: uno scarto spiegato vale più di un lancio riuscito per caso | il debrief non viene scritto entro 7 giorni dalla chiusura |

**Le due cause più probabili sono la 1 e la 2, e sono le stesse che hanno ucciso il lancio del
30/05/2026.** L'intera struttura degli scaglioni è costruita contro quelle due.

---

## 6. LE CONDIZIONI DI ABBANDONO

> Un piano senza condizione di uscita è una scommessa senza limite di perdita. Queste sono
> **misurabili**, e vanno lette prima di cominciare, quando non c'è ancora niente da difendere.

| # | Se accade | Allora | Come si misura |
|---|---|---|---|
| **1** | S0 non si chiude in **16 ore-uomo** | **si ferma tutto.** Il problema dell'azienda non è organizzativo: è che non ha una cassa, e nessun reparto la costruisce | le ore spese su S0 |
| **2** | `pubblico.json` esce con totale verificato **zero** | si ferma il lancio e si va a costruire pubblico. Un'offerta senza nessuno davanti non è un lancio: è un documento | il campo `raggiungibili_verificati` sommato |
| **3** | Il lancio pilota non è `APERTO` entro **45 giorni** dal giorno zero | si ferma la costruzione e si guarda la causa. Se il blocco è una firma che non arriva, nessun reparto in più la farà arrivare | data di `APERTO` meno data di S0 |
| **4** | Dopo **due lanci** nessuno schema ha cambiato una decisione | la memoria si dichiara fallita e si smette di mantenerla, invece di riempirla per abitudine | i campi `si_applica_quando` dei debrief, confrontati con le decisioni prese |
| **5** | S2 costa oltre il **40%** in più della stima alta | **non si prosegue**: si rifanno le stime di S3-S5 prima, non dopo | ore spese su S2 contro 65 |

**Fermarsi alla 1 o alla 2 non è un fallimento.** È la scoperta, pagata in due giorni invece che in
tre mesi, che il collo di bottiglia era altrove.

---

## 7. L'ORDINE DENTRO OGNI SCAGLIONE — il test rosso viene prima

Per ogni controllo, in quest'ordine e non in un altro:

1. **Si scrive il test rosso** — il caso costruito perché fallisca. Deve fallire subito, perché il
   controllo non esiste ancora.
2. Si scrive il controllo.
3. Il test rosso continua a fallire **per la ragione giusta** (blocca), non per un errore.
4. Si scrive il caso verde.

> **Un test che nasce verde non prova niente.** Il primo test di questo ecosistema deve fallire,
> così quando diventerà verde si saprà che è successo qualcosa.

I quattordici test rossi sono già dichiarati nel registro, campo `test_rosso` di ogni gate. **Non
vanno inventati durante la costruzione: vanno copiati da lì.**

---

## 8. IL LAVORO SU DUE MACCHINE

Max e Gael lavorano dallo stesso repository da due macchine diverse. Tre regole, e la prima è
già codice:

| # | Regola | Dove vive |
|---|---|---|
| 1 | `avanza` prende un **lock esclusivo** sul file di stato prima di leggere. Se il lock è preso, esce 1 dicendo chi lo detiene e da quando | documento 01, §2.3 |
| 2 | Prima di un lavoro grosso, **blocco di coordinamento** in `company/Memory/STATO-EMPIRE.md` e push | metodo dell'Impero |
| 3 | Si committa e si pusha **alla fine di ogni sessione**, non alla fine dello scaglione | — |

---

## 9. COME SI SA CHE UNO SCAGLIONE È CHIUSO — il riepilogo

| Scaglione | Comando o verifica | Esito richiesto |
|---|---|---|
| **S0** | pannello del fornitore + strumento di misura | incasso, consegna, rimborso ed evento sulla **stessa** transazione |
| **S1** | validazione dei quattro file contro i propri schemi | tutti validi, **più una firma vera** |
| **S2** | `lancio crea prova-vuota` + `lancio avanza prova-vuota` | **codice 1**, blocco al controllo dell'offerta, verbale scritto, stato invariato |
| **S2** | `pytest tests/rossi/` | i sei test rossi bloccano come devono |
| **S3** | un lancio di prova avanza | si ferma a `PRONTO` |
| **S4** | un lancio chiuso avanza | arriva ad `APPRESO`, con ≥3 schemi |
| **S5** | `lancio blocchi` | elenca i punti umani aperti, ordinati per giorni di attesa |
| **sempre** | `cd dati && PYTHONIOENCODING=utf-8 python valida_registro.py` | esce **0** |

**L'ultima riga vale per ogni giorno di lavoro, non solo per la fine di uno scaglione.** Se il
validatore esce diverso da zero, il piano è incoerente e non si costruisce sopra un piano
incoerente.

---

## Connessioni

- `dati/registro.yaml` — la fonte di verità; i quattordici `test_rosso` stanno lì
- [[00-LEGGIMI]] — il primo giorno e le condizioni di uscita
- [[01-ARCHITETTURA]] — `avanza`, il ponte, gli errori, l'osservabilità
- [[02-PREVISIONE-E-DENARO]] — il costo della macchina, che entra nel tetto di S2
- [[03-FLUSSO-OFFERTA]] — ciò che S1 percorre a mano
- [[05-ADR-022]] — la decisione da registrare **prima** di creare la cartella
- `company/Memory/decisions/ADR-014-il-codice-torna-a-chiamare-un-modello.md`
- `company/Memory/decisions/ADR-019-motore-orchestrazione-canonico.md`
