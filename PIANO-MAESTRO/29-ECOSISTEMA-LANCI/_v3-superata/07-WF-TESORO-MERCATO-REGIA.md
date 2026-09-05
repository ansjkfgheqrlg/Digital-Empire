---
Type: PROJECT
Status: Proposta
Tags: #lanci #ecosistema-15 #budget #mercato #regia
Created: 2026-09-05
---

# 07 — WF-TSR (TESORO), WF-INT (MERCATO), WF-REG (REGIA)

> Terza versione. La precedente aveva **due gate sul budget che non potevano fallire** e un
> **calendario incompatibile con i flussi che orchestrava**. Il paragrafo finale elenca le
> correzioni.

---
---

# PARTE A — WF-TSR · IL TESORO DEL LANCIO

## A.1 Identità e confine

| Campo | Valore |
|---|---|
| **Sigla** | `WF-TSR` |
| **Missione** | Sa **quanto costa questo lancio ogni giorno** e **quante vendite servono per rientrare**, e blocca la spesa quando esce dal seminato |
| **Proprietario** | `LAN-TSR` |
| **Durata** | vive per tutto il lancio: nasce a T-30 e chiude sette giorni dopo |

**Il confine con la Tesoreria dell'Impero, ed è la cosa più importante:**

> **La Tesoreria è la fonte di verità sui soldi dell'azienda. `LAN-TSR` è la fonte di verità sui
> soldi di *questo lancio*.** Ogni euro nasce nel lancio e **sale** in Tesoreria; non scende mai.
> Se un euro compare in tutti e due i posti con valori diversi, **ha ragione la Tesoreria**.

> ⚠️ **Due fatti verificati che cambiano l'attuazione di questo confine:**
> 1. **Esiste già uno script di tesoreria dell'Impero.** Il nostro `costi.py` **non lo
>    riscrive**: gli passa i movimenti. Il piano precedente stava creando un secondo motore.
> 2. **I registri dell'Impero sono oggi a zero righe.** Quindi la riconciliazione di fine lancio,
>    al primo giro, **riconcilia contro il vuoto**: non è un controllo, è un primo popolamento.
>    Va detto, perché un confronto con zero che "torna" non prova niente.

> ⚠️ **E la sentinella dei costi esiste già.** `LAN-TSR` **non ne crea una seconda**: le passa le
> soglie del lancio e riceve i suoi allarmi.

## A.2 L'input — con le date, che prima mancavano

```json
{
  "lancio_id": "string",
  "offerta_path": "string",
  "budget_massimo": 800.00,
  "budget_approvato_da": "Max",
  "valuta": "EUR",
  "voci": [
    { "voce": "pubblicita", "descrizione": "campagne pre-lancio",
      "importo_previsto": 400.00,
      "data_prevista_inizio": "2026-10-10",
      "data_prevista_fine": "2026-10-19",
      "profilo_spesa": "lineare | anticipato | posticipato | unico",
      "canale": "ads-meta", "gia_pagato": false }
  ],
  "commissione_pagamento_pct": 3.5,
  "rimborso_atteso_pct": 5
}
```

> ⚠️ **Le tre righe di data e profilo sono nuove, e senza di esse il gate sullo scarto non poteva
> funzionare.** La versione precedente confrontava la spesa reale con *"il previsto a oggi"* —
> una grandezza che **nessun campo permetteva di calcolare**, perché le voci non avevano date.
> Il gate o divideva per zero o dava sempre un numero negativo: **non poteva bloccare mai.**

**Come si calcola adesso il previsto a una data:**

```
previsto_a_oggi = somma, su tutte le voci:
    unico      → l'intero importo se la data di inizio è passata, altrimenti 0
    lineare    → importo × (giorni trascorsi / giorni totali della voce)
    anticipato → importo × min(1, giorni trascorsi / (giorni totali × 0,4))
    posticipato→ importo × max(0, (giorni trascorsi − giorni totali × 0,6) / (giorni totali × 0,4))
```

**Il default è `lineare`**, e — come ogni default — **finisce scritto nel campo `assunzioni`**.

## A.3 Le fasi

| # | Fase | Cosa fa | Agente | Output | Ore | Umano |
|---|---|---|---|---|---:|---|
| **T1** | Budget | somma le voci, applica i default dichiarandoli, confronta col tetto | `lan-tsr-conductor` | `budget.json` | 2 | **Sì**: il tetto lo fissa una persona |
| **T2** | Pareggio | quante vendite servono, in tre scenari | `lan-tsr-conductor` | dentro `budget.json` | 1 | no |
| **T3** | Prova a secco | simula la spesa **senza spendere** e dice se il tetto regge | `lan-tsr-conductor` | `dry-run-costi.md` | 2 | no |
| **GATE-TSR-1** | Approvazione | §A.4 | `lan-qlt-gate` | verbale | 0,5 | **Sì**: la firma |
| **T4** | Registrazione | ogni spesa reale con data, voce, canale, importo, **prova** | `lan-tsr-registratore` | `spesa.json` | continuo | **Sì**: molti importi si inseriscono a mano |
| **T5** | Vigilanza | ricalcola scarto e costo di acquisizione | `lan-tsr-sentinella` + la sentinella dell'Impero | `tracking/costi-<data>.json` | automatico | no |
| **GATE-TSR-2** | Lo scarto | §A.4 | `lan-qlt-gate` | verbale | — | sblocco **solo umano** |
| **T6** | Consuntivo | costi, ricavi, margine, **dove la previsione ha sbagliato** | `lan-tsr-conductor` | `consuntivo.md` | 3 | no |
| **T7** | Salita in Tesoreria | passa i definitivi allo script dell'Impero | `lan-tsr-registratore` | handoff | 1 | no |

## A.4 I gate — rifatti perché potessero fallire

| Gate | Criterio | Chi lo esegue | Se blocca | Come si sblocca |
|---|---|---|---|---|
| **GATE-TSR-1** | `totale_previsto ≤ budget_massimo` ∧ pareggio calcolato ∧ **100% delle voci con date e profilo** ∧ 100% delle assunzioni dichiarate ∧ **`budget_approvato_da` diverso da chi ha scritto le voci** | `lan-qlt-gate` | il lancio non passa in produzione | si taglia una voce, o **una persona diversa** alza il tetto lasciandolo scritto |
| **GATE-TSR-2** | `(speso − previsto_a_oggi) / previsto_a_oggi ≤ 0,10`, **calcolabile grazie ai profili di spesa** | `lan-tsr-sentinella` propone, `lan-qlt-gate` verbalizza | **si ferma ogni spesa nuova**, il lancio continua col già pagato | **solo firma umana** in `deroghe.json`, con importo, motivo e nuovo tetto |
| **GATE-TSR-3** | il consuntivo esiste e i totali coincidono con la Tesoreria entro l'1% — **oppure la Tesoreria è vuota, e allora lo si dichiara invece di dire che torna** | `lan-tsr-conductor` | il lancio non passa ad *appreso* | si sana la divergenza, o si dichiara il primo popolamento |

> ⚠️ **L'aggiunta al primo gate — *"approvato da una persona diversa da chi ha scritto le voci"* —
> nasce da un rilievo semplice e imbarazzante:** nella versione precedente il gate confrontava un
> tetto e delle voci **scritti dalla stessa persona nello stesso file**, con sblocco *"alza il
> tetto"*. Non poteva fallire.

**Perché il secondo gate blocca solo la spesa e non il lancio:** fermare un lancio a metà per uno
sforamento costa più dello sforamento. Ma continuare a spendere alla cieca è come si perdono i
soldi due volte. Il compromesso: **il lancio va avanti con ciò che è già pagato**, e ogni euro
nuovo richiede una firma.

**E il presidio contro la deroga che diventa abitudine:** **tre deroghe sullo stesso lancio
obbligano a rifare il budget da capo.** Un tetto derogato tre volte non è un tetto.

## A.5 Le formule

```
ricavo_netto_unitario = prezzo × (1 − commissione/100) × (1 − rimborsi/100)
vendite_per_pareggio  = arrotonda_per_eccesso( totale_previsto / ricavo_netto_unitario )

costo_acquisizione(canale) = spesa(canale) / clienti_paganti_attribuiti(canale)
   ⚠️ con zero clienti attribuiti NON è infinito: è "non calcolabile", e si scrive così
   ⚠️ sotto i 10 clienti si scrive "non significativo", non un numero

ritorno_sulla_spesa(canale) = ricavo_attribuito(canale) / spesa(canale)
margine = ricavo_totale_netto − costo_totale_reale
scarto_pct = (speso − previsto_a_oggi) / previsto_a_oggi × 100
```

**La nota sull'attribuzione, che è il punto debole di ogni calcolo di questo tipo:**
l'attribuzione per canale **è un'assunzione**, non una misura, a meno che ogni canale non abbia la
sua pagina d'ingresso separata. Per questo la regola *mai mischiare traffico gratuito e comprato*
non è pignoleria: **è la sola cosa che rende il costo di acquisizione un numero vero.**

## A.6 Fallimenti

| Sintomo | Cosa fa il sistema |
|---|---|
| Nessuna spesa registrata per tre giorni | la sentinella tratta l'assenza come **anomalia**, non come "zero spese" |
| Costo di acquisizione enorme | si scrive "non significativo sotto i 10 clienti" |
| Il consuntivo non torna con la Tesoreria | il terzo gate blocca; se la Tesoreria è vuota, **lo dichiara** invece di far finta che torni |
| Una spesa senza prova | si registra con `prova: null` **e resta segnalata**: non si rifiuta il fatto, si rifiuta di fingere che sia documentato |

---
---

# PARTE B — WF-INT · MERCATO E CONCORRENTI

## B.1 Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-INT` · Proprietario `LAN-INT` |
| **Missione** | Porta al lancio **le parole vere del pubblico** e **i buchi veri dei concorrenti**, con la fonte accanto a ogni affermazione |
| **Durata** | **16-30 ore-uomo** la prima volta su un mercato; **4** per un aggiornamento |

## B.2 Le fasi

| # | Fase | Cosa fa | Agente | Ore |
|---|---|---|---|---:|
| **I1** | Consultazione della memoria | cosa l'Impero sa già di questo mercato — **fase zero obbligatoria** | `lan-int-conductor` | 1 |
| **I2** | Raccolta delle voci | le frasi vere del pubblico, **ognuna con l'indirizzo** | `lan-int-ascoltatore` | 6-10 |
| **I3** | Dolori | raggruppa le voci per frequenza | `lan-int-analista` | 3 |
| **I4** | Concorrenti | offerta, prezzo, promessa, funnel, canali, **e le recensioni a una e due stelle** | `lan-int-osservatore` | 5-8 |
| **I5** | Buchi | ciò che nessuno copre, dalle lamentele ricorrenti | `lan-int-analista` | 3 |
| **I6** | Obiezioni | la mappa ordinata per frequenza × intensità | `lan-int-analista` | 3 |
| **I7** | Tono di voce | 20-30 frasi vere | `lan-int-ascoltatore` | 2 |
| **GATE-INT-1** | **Anti-invenzione** | §B.3 | `lan-qlt-gate-fonti` | 2 |
| **I8** | Archiviazione | ogni pezzo diventa un record, deduplicato | `lan-int-conductor` | 1 |

## B.3 Il gate anti-invenzione — il cuore

| Controllo | Soglia |
|---|---|
| Numero di frasi | **≥15** |
| Frasi con fonte | **100%** — nessun campo vuoto passa |
| **Fonti raggiungibili** | **≥90%** *(vedi la nota sotto)* |
| **Verifica a campione** | **5 frasi su 15 estratte a caso devono comparire nella pagina che le cita** |
| Dolori distinti | ≥5, con controllo che non siano lo stesso riscritto |
| Concorrenti | ≥3, ognuno con prezzo e promessa compilati |
| Buchi | ≥3, ognuno collegato a una lamentela vera |
| Frasi di tono | ≥20 |

> ⚠️ **Contraddizione risolta.** Due documenti del piano precedente chiedevano cose diverse sullo
> **stesso file**: uno *"100% delle fonti raggiungibili"*, l'altro *"≥90%"*. Un solo collegamento
> morto su quindici avrebbe messo il primo lancio in stallo fra due reparti.
> **Vale ≥90%**, e la ragione è che un indirizzo può morire per conto suo fra la raccolta e la
> verifica, senza che la frase sia inventata. **Le fonti irraggiungibili si elencano nel verbale**,
> e le loro frasi non contano nel conteggio delle quindici.

**La verifica a campione è ciò che separa questo gate dalla buona intenzione.** Contare quindici
frasi è facile e si può fare inventandole. Aprire cinque pagine estratte a caso e cercarci dentro
la frase citata non si può falsificare senza costruire pagine finte.

> **Il campione è salito da 3 a 5 su 15** dopo la critica: tre su quindici è il 20%, e chi ne
> inventa dodici mettendone tre vere ha una probabilità concreta di passare. Resta comunque un
> controllo statistico, non una prova: **va detto**.

## B.4 Cosa scade

| Cosa | Scadenza |
|---|---|
| Prezzi dei concorrenti | **3 mesi** |
| Offerta e promessa dei concorrenti | 6 mesi |
| Frasi del pubblico e dolori | 12 mesi |
| Buchi | 6 mesi — uno che resta vuoto per anni di solito è vuoto per una ragione |
| Tono di voce | 12 mesi |

**L'aggiornamento è incrementale**, non una ricerca nuova: quattro ore invece di trenta. Ed è il
motivo per cui il registro ha identificativi stabili.

## B.5 Il confine con la biblioteca dell'Impero

| Chi | Possiede |
|---|---|
| L'agente della conoscenza | **tutta la formazione dell'Impero**. È il fornitore unico |
| L'ecosistema Intelligence | l'intelligence generale su mercati e concorrenti |
| **`LAN-INT`** | **solo la ricerca legata a un lancio** |

**La regola che evita la seconda biblioteca:** `LAN-INT` **non archivia metodi** — archivia
*osservazioni di mercato datate*. Quando da un'osservazione nasce un metodo, quel metodo **sale**
all'agente della conoscenza. Se `LAN-INT` comincia a contenere framework, sta diventando una
biblioteca parallela e va potato.

---
---

# PARTE C — WF-REG · LA REGIA

## C.1 Il calendario — rifatto, perché il precedente era incompatibile

> ⚠️ **Il difetto:** il calendario precedente dava **un giorno alla ricerca**, che nel suo stesso
> flusso ne dichiara due-quattro, e **un giorno al prodotto**, che ne dichiara tre-cinque anche
> nel caso più veloce. Zero margine ovunque. E due bocciature della pagina di vendita — che il
> piano stesso ammette come normali — spostavano il lancio senza che nessun documento lo dicesse.
> *(In più i "37 giorni" da T-30 a T+7 sono 38.)*

**Il calendario nuovo: 38 giorni, con il margine dichiarato.**

| Giorno | Cosa deve essere pronto | Chi | Margine |
|---|---|---|---|
| **T-30** | lancio creato, data fissata, calendario generato | REG | — |
| **T-30 → T-28** | budget approvato e pareggio calcolato | TSR | 1 g |
| **T-30 → T-26** | **ricerca chiusa e verificata** | INT | 2 g |
| **T-27 → T-24** | **certificato del prodotto** (percorso "già esistente") | PRD | 1 g |
| **T-25 → T-23** | grande promessa, approvata da una persona | CPY | 1 g |
| **T-23 → T-20** | **pagina di vendita** — il documento madre | CPY | 1 g |
| **T-20 → T-18** | punteggio della pagina di vendita ≥80 | QLT | **2 g — il margine per una bocciatura** |
| **T-18 → T-8** | **SPRINT IN PARALLELO** | CPY · FNL · EDT | 2 g |
| ↳ | tutti gli altri testi | CPY | |
| ↳ | le pagine costruite e online | FNL | |
| ↳ | il piano editoriale completo | EDT | |
| **T-14** | i contenuti pre-lancio cominciano a uscire | EDT | — |
| **T-8** | tutte le pagine rispondono **e tracciano** | FNL | 1 g |
| **T-7** | campagne pronte ma **spente** | TRF | — |
| **T-7** | la lista si scalda: parte la sequenza pre-lancio | REG | — |
| **T-5** | **prova a secco completa**, senza spedire né spendere | REG | 1 g |
| **T-3** | iscrizioni al webinar aperte | FNL + EDT | — |
| **T-1** | **sincronizzazione + via libera** | QLT + **persona** | — |
| **T-0** | **si apre la vendita** | **persona** | — |
| **T-0 → T+5** | ogni giorno: numeri, diagnosi, **azione** | REG | — |
| **T+5** | **si chiude la vendita** | **persona** | — |
| **T+6** | consuntivo | TSR | — |
| **T+7** | debrief con ≥3 schemi | MEM | — |

**Il margine totale dichiarato: 12 giorni su 38.** Non è generosità: è la somma dei rifacimenti
che i gate del piano stesso prevedono come normali. Un calendario senza margine, con nove gate che
possono bloccare, è un calendario che salta al primo blocco.

**E il calendario si genera, non si scrive.** Se la data slitta, si rigenera: è il motivo per cui
deve essere un file prodotto da un comando.

## C.2 Il grafo delle dipendenze

```
offerta (prezzo + data)
   │
   ├──► budget ──► [GATE-TSR-1] ──┐
   │                              │
ricerca ──► certificato ──────────┼──► grande promessa ──► PAGINA DI VENDITA ──► [GATE-CPY-1]
                                  │                                                    │
                                  │        ┌───────────────────────────────────────────┘
                                  │        │
                                  │   ╔════╧═══════ SPRINT PARALLELO ═══════╗
                                  │   ║  testi │ funnel │ editoriale        ║
                                  │   ╚════╤════════════╤═══════════╤═══════╝
                                  └────────┴──► [GATE-REG-1] ◄──────┘
                                                   │
                                             via libera umano
                                                   │
                                             APERTURA VENDITA
```

**Il vincolo che vale più di tutti:** lo sprint **non parte** finché la pagina di vendita non ha
superato il suo gate. Tre reparti che lavorano su una promessa non approvata producono tre
versioni diverse della stessa cosa, e il rifacimento costa più del tempo che si credeva di
guadagnare.

## C.3 La lista di sincronizzazione — dieci voci, tutte vere insieme

| # | Voce | Come si verifica |
|---|---|---|
| 1 | Prodotto certificato, zero bandiere rosse | il certificato con esito positivo |
| 2 | Prezzo e data confermati e non cambiati | confronto con la versione firmata |
| 3 | Tutte le pagine rispondono | controllo automatico |
| 4 | Tutte le pagine registrano l'evento | l'evento è arrivato almeno una volta |
| 5 | **Cassa provata con una transazione reale** | la prova registrata |
| 6 | Le quattro sequenze email caricate e programmate | verifica sullo strumento |
| 7 | Piano editoriale approvato **e primi contenuti già usciti** | conteggio degli indirizzi pubblicati |
| 8 | Budget approvato, scarto entro il 10% | il gate del tesoro |
| 9 | Prova a secco eseguita e superata | il verbale |
| 10 | **Chi risponde ai clienti durante la vendita è designato e disponibile** | **è una persona, e va nominata** |

**La decima è quella che tutti dimenticano e che rovina i lanci:** si apre la vendita e nessuno sa
chi risponde a chi scrive *"il pagamento non funziona"*.

## C.4 Il via libera — tre esiti, tutti scritti

| Esito | Quando | Cosa comporta |
|---|---|---|
| **Si parte** | tutte e dieci vere | si apre alla data |
| **Si parte ridotto** | mancano voci non essenziali (es. gli annunci) | si apre **senza quel pezzo, dichiarandolo**: il lancio parte organico e il pezzo si aggiunge |
| **Si rinvia** | manca una voce essenziale (prodotto, pagamento, pagine) | **nuova data, calendario rigenerato, ragione scritta** |

**Un rinvio non è un fallimento: è la cosa che questo sistema esiste per rendere possibile.** Oggi
l'alternativa al rinvio non è aprire lo stesso — è restare fermi sei mesi senza che nessuno lo
dichiari.

## C.5 Il tracciamento — diagnosi e azione

| Numero | Sotto soglia | Diagnosi | **L'azione, entro lo stesso giorno** |
|---|---|---|---|
| Iscrizioni | <20% | la pagina non convince, o il traffico è sbagliato | si cambia il titolo, non tutta la pagina; se è traffico comprato si guarda quale annuncio porta gente sbagliata |
| Apertura email | <20% | il titolo dell'email | si riscrive quello della prossima, e si rimanda a chi non ha aperto con un titolo diverso |
| Click | <1% | il contenuto | si accorcia e si porta l'invito più in alto |
| Presenza al webinar | <30% | i promemoria | se ne aggiunge uno a un'ora e uno a dieci minuti |
| Conversione | <2% | prezzo, prova o obiezioni | si aggiungono prove e si affronta l'obiezione più frequente fra chi ha scritto |
| Costo di acquisizione | oltre il pareggio | si paga più di quanto si incassa | **si spegne quel canale**, non si aspetta |
| Vendite a metà periodo | <30% dell'atteso | il problema è a monte | si controlla in quest'ordine: la pagina traccia? il pagamento funziona? il prezzo è visibile? |

**Ogni riga ha un'azione, e l'azione si esegue entro lo stesso giorno.** Un cruscotto che segnala e
non fa agire è un cruscotto che si smette di guardare al terzo giorno.

## C.6 Il debrief

| Sezione | Contenuto |
|---|---|
| Previsto contro reale | ogni numero del piano accanto al numero vero |
| **Scarti oltre il 10%** | **ognuno con una causa scritta.** Uno scarto senza causa = debrief non finito |
| Cosa ha funzionato / cosa no | con l'evidenza, non con l'impressione |
| **I gate** | quali hanno bloccato, quanto è costato, **se avevano ragione** |
| **Almeno tre schemi riutilizzabili** | nel formato del banco della memoria |
| Cosa cambia nel prossimo lancio | azioni concrete |

**La sezione sui gate è quella che nessuno pensa di mettere e che vale di più:** dice se il sistema
che abbiamo costruito ha funzionato, non solo se il lancio ha venduto.

---

## D. COSA È CAMBIATO

| Cambiamento | Contro quale obiezione |
|---|---|
| Le voci di budget hanno **date e profilo di spesa** | *"il gate divide per una grandezza che nessun campo permette di calcolare: non può fallire"* |
| Il budget è **approvato da chi non l'ha scritto** | *"confronta un tetto e delle voci scritti dalla stessa persona, con sblocco «alza il tetto»"* |
| La riconciliazione **dichiara quando i registri sono vuoti** | *"riconcilia contro il vuoto e lo chiama controllo"* |
| Si **usa** lo script di tesoreria dell'Impero e la sua sentinella | *"il piano ne stava creando una seconda copia"* |
| Il calendario è di **38 giorni con 12 di margine dichiarato** | *"dà un giorno a lavori che ne dichiarano quattro, e due bocciature previste spostano il lancio senza che nessuno lo dica"* |
| Le fonti raggiungibili: **una sola soglia, ≥90%** | *"due documenti chiedono 100% e 90% sullo stesso file: stallo garantito"* |
| Il campione di verifica sale a **5 su 15** | *"tre su quindici lascia passare chi ne inventa dodici"* |
| Le durate passano a **ore-uomo** | *"i giorni pieni non esistono in un'azienda dove si fa anche altro"* |
