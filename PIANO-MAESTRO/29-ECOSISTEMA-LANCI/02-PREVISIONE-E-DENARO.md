---
Type: PROJECT
Status: Proposta — versione 4
Tags: #lanci #ecosistema-15 #previsione #denaro #pareggio
Created: 2026-09-05
Last updated: 2026-09-05
Versione: 4
---

# 02 — LA PREVISIONE E IL DENARO

> **Regola di lettura:** questo documento spiega. Il registro decide.
> Se una riga qui contraddice `dati/registro.yaml` o uno schema in `dati/schemi/`, ha torto
> questa riga.

---

## 1. LA DOMANDA CHE MANCAVA

In 3.718 righe, la versione 3 del piano non conteneva mai la domanda **«quanto ci aspettiamo di
incassare»**.

Non è una dimenticanza di stile. Ha prodotto tre guasti misurabili, tutti e tre già citati dal
registro:

| # | Guasto | Dove si vedeva |
|---|---|---|
| 1 | **La firma del prezzo era cieca** | si chiedeva a una persona di confermare un numero, non un risultato. Confermare «47 €» è una scelta di gusto; confermare «47 €, che su questo pubblico fanno questo ricavo» è una decisione |
| 2 | **Il controllo del budget era insoddisfacibile per costruzione** | pretendeva «il pareggio calcolato», e il pareggio è ricavo previsto contro costo. Il ricavo previsto non esisteva in nessun artefatto: nessun lancio avrebbe mai potuto passare quel controllo |
| 3 | **Il debrief ereditava un compito impossibile** | senza previsione, il consuntivo è un numero solo. Un numero solo non ha scarto, e senza scarto non si impara niente: si archivia |

Questo documento è il rimedio ai tre. Descrive **come si costruisce `previsione.json`**, **quanto
costa far girare la macchina**, **come si calcola il pareggio**, e **quali numeri l'azienda oggi
non ha**.

L'ultima parte è la più importante, e sta al §8.

---

## 2. IL MODELLO DEL RICAVO

### 2.1 La formula, scritta nel file e non solo nel codice

```
ricavo_lordo = pubblico_raggiungibile × tasso_visita × tasso_acquisto × prezzo
```

È il campo `formula` di `previsione.json`, ed è una costante dello schema: il file la porta
scritta dentro.

**Perché una formula dentro il file dati e non solo dentro il programma.** Una previsione di cui
non si può rifare il conto a mano non è una previsione: è un numero che qualcuno deve credere.
Chi firma il prezzo deve poter prendere un foglio, rifare la moltiplicazione e ottenere lo stesso
risultato. Se non torna, il difetto si scopre prima della firma e non dopo il lancio.

### 2.2 I quattro ingressi, e chi li possiede

| Ingresso | Da dove viene | Chi **non** può sceglierlo |
|---|---|---|
| `pubblico_raggiungibile` | `ART-PUB` (`pubblico.json`), campo `raggiungibili_verificati` sommato sui canali | il modello di previsione. Lo riceve, non lo stima |
| `prezzo` | `ART-OFF` se già firmato, altrimenti `proposta-in-corso` | il modello. In istruttoria si ricalcola per ogni alternativa proposta |
| `tasso_visita` | quota del pubblico che arriva sulla pagina | — è un'assunzione, e va dichiarata tale |
| `tasso_acquisto` | quota dei visitatori che compra | — è un'assunzione, e va dichiarata tale |

Il vincolo sui primi due è scritto nello schema come valore costante (`fonte_pubblico: "ART-PUB"`)
ed è la ragione per cui `GATE-PRV-1` non è auto-soddisfacibile: **il modello non può migliorare la
propria previsione scegliendosi il pubblico**.

### 2.3 I tre scenari sono obbligatori

Lo schema pretende `pessimista`, `atteso`, `ottimista`, tutti e tre, ognuno con i propri tassi e
il proprio `ricavo_lordo`.

**Perché tre e non uno.** Un numero solo nasconde l'incertezza invece di dichiararla, e fa firmare
al buio a chi crede di vedere. Tre numeri costringono a rispondere alla domanda che conta davvero:
*«e se va male, va male quanto?»*

**Come si costruiscono i tre scenari, senza inventarli.** La banda non si sceglie a sentimento: si
dichiara da dove viene.

| Scenario | Cosa rappresenta | Regola |
|---|---|---|
| **pessimista** | il caso che si è disposti ad accettare | i tassi più bassi fra quelli che si è disposti a considerare possibili. **È lo scenario su cui si decide se il lancio si fa**: vedi §6 |
| **atteso** | il caso su cui si pianifica | i tassi che si dichiarano più probabili, con la ragione scritta in `perche_questo_scenario` |
| **ottimista** | il tetto | serve a una cosa sola: verificare che anche il caso migliore stia dentro la capacità di consegna e di assistenza |

### 2.4 Ogni assunzione porta il proprio stato

Lo schema ammette due soli stati per ogni assunzione: **`misurato`** o **`assunto`**.

- `misurato` **richiede** una `fonte`, e lo schema la impone (`if stato == misurato then required: fonte`).
- `assunto` richiede di dichiarare `da_dove_viene_se_assunto`: un riferimento di settore, il lancio
  precedente di un altro prodotto, oppure — ed è legittimo — **«numero di comodo»**.

> **La regola che tiene in piedi tutto il sistema:** dichiarare «numero di comodo» è legittimo.
> Nasconderlo no.
>
> Un'assunzione travestita da misura è la bugia più costosa dell'intero ecosistema, perché **entra
> in un controllo come prova**. Il test rosso di `GATE-PRV-1` è costruito esattamente su questo
> caso: *una previsione con un tasso di conversione dichiarato «misurato» e senza fonte deve
> bloccare*.

---

## 3. DAL LORDO AL NETTO — la cascata che il piano precedente non aveva

Il ricavo lordo non è denaro dell'azienda. Fra il lordo e ciò che resta ci sono cinque scalini, e
**quattro dei cinque oggi non hanno un numero misurato in casa** (§8).

| # | Scalino | Come si calcola | Stato del dato oggi |
|---|---|---|---|
| 1 | **Rimborsi** | `ricavo_lordo × quota_rimborsi` | **assunto.** Nessun lancio precedente misurato: non esiste una quota storica |
| 2 | **Commissioni di incasso** | `ricavo_lordo × percentuale_fornitore + numero_ordini × quota_fissa_per_transazione` | **assunto** finché la cassa non è collegata. Si misura al giorno zero, sulla transazione di prova |
| 3 | **Imposte** | dipende dal regime fiscale dell'azienda e dal paese del cliente | **non noto.** Vedi §7: è una domanda per il commercialista, non per questo documento |
| 4 | **Costo di consegna** | quota-parte mensile degli strumenti usati, divisa per i lanci del periodo | **assunto** |
| 5 | **Costo della macchina** | le chiamate ai modelli — §4 | **stimabile adesso**, ed è l'unico dei cinque che questo documento calcola |

**La regola di prudenza, e la ragione per cui è così:** finché uno scalino è `assunto`, il pareggio
si calcola **con il valore peggiore che si è disposti a considerare**, non con quello atteso. Un
pareggio ottimistico è peggio di nessun pareggio: fa partire lanci che non stanno in piedi, e lo
si scopre a lancio finito.

---

## 4. QUANTO COSTA FAR GIRARE LA MACCHINA

> Questa sezione colma un buco rilevato esplicitamente da un revisore: il piano precedente
> prevedeva 41 agenti e **non conteneva una sola riga sul costo**, in un'azienda che ha un
> direttore finanziario e un tetto di spesa già sfondato una volta in silenzio (ADR-014).

### 4.1 Il costo ha un pavimento fisso, e non dipende da quanto lavoro fa l'agente

Da ADR-014 (2026-08-30), misurato: **ogni invocazione di un agente costa 0,08-0,11 $ di sola
tassa**, qualunque sia il contenuto della richiesta. A questa tassa si somma il costo dei token
effettivi, che dipende dal modello e dal volume.

La conseguenza è aritmetica e va detta chiaramente: **il numero di agenti non è una ricchezza, è
un moltiplicatore di costo fisso.** Quarantuno agenti che si passano il lavoro a pezzetti costano
più di quindici che lavorano a blocchi, a parità di risultato.

È la ragione per cui il registro ne ha quindici, e per cui tre di essi sono al grado più basso:
`lan-prv-modello`, `lan-tsr-contabile` e `lan-reg-tracciatore` fanno calcoli deterministici, e un
modello che «ragiona» su una somma è un modo caro di sbagliare.

### 4.2 Il conto delle invocazioni per un lancio

Stima per un lancio che **non incontra blocchi**. È un pavimento, non una previsione di spesa.

| Artefatto | Agente | Invocazioni stimate | Perché |
|---|---|---:|---|
| ART-PUB | `lan-pub-censore` | 1-2 | conta i canali e allega le prove |
| ART-DEC | `lan-str-filtro` | 1 | cinque domande su artefatti già esistenti |
| ART-CRT | `lan-prd-collaudatore` | 2-3 | collaudo e verifica dei link |
| ART-RIC | `lan-int-analista` | 3-5 | più giri: le fonti vanno aperte davvero |
| ART-PRV | `lan-prv-modello` | 1 | è una formula |
| ART-OFF | `lan-off-conductor` | 2-4 | istruttoria, alternative di prezzo, revisione dopo la firma |
| ART-CPY | `lan-cpy-conductor` | 8-15 | è il pezzo più grosso: tutti i testi del lancio |
| ART-FNL | `lan-fnl-costruttore` | 3-5 | pagine, misura, prova di cassa |
| ART-EDT | `lan-edt-pianificatore` | 3-5 | i contenuti dei giorni del carrello |
| ART-BDG | `lan-tsr-contabile` | 1-2 | somme |
| ART-APE | `lan-reg-calendarista` | 1-2 | lista di sincronizzazione |
| ART-CNS | `lan-reg-tracciatore` | 1-2 | legge i numeri dai pannelli |
| ART-DBR | `lan-mem-distillatore` | 2-3 | confronto, cause, schemi |
| — | `lan-gate` (14 controlli) | 14-20 | almeno uno per controllo, più le riprove |
| — | `lan-direttore` | 5-10 | orchestrazione e interlocuzione umana |
| | **Totale** | **48-79** | |

**Il pavimento di spesa, di sola tassa:**

```
48 × 0,08 $ =  3,84 $      (caso migliore)
79 × 0,11 $ =  8,69 $      (caso peggiore senza blocchi)
```

Più il costo dei token, che va misurato e non stimato.

### 4.3 Il tetto di 15 $, e perché è stretto

Il registro fissa `tetto_spesa_per_lancio_usd: 15.00`.

**Verdetto onesto: il tetto regge il lancio pulito e non regge un lancio con molte riprove.**
Fra 3,84 $ e 8,69 $ di sola tassa, il margine per i token e per i giri di correzione è quello che
resta. Ogni ciclo «il controllo boccia → si corregge → si riprova» aggiunge almeno due invocazioni.

Non lo alzo, e la ragione è deliberata: **un tetto che non stringe mai non è un tetto.** Il
comportamento al tetto è già scritto nel registro ed è quello giusto — *il lancio si ferma dov'è,
salvato; non si ricomincia, si riprende*. Un lancio che sbatte contro il tetto è
un'informazione utile: dice che sta girando in tondo su un controllo.

**Le tre regole che tengono il costo dentro il tetto:**

1. **Si lavora a blocchi, non a unità minima** (ADR-014). Un agente che produce dieci testi in una
   chiamata costa una tassa; dieci chiamate da un testo ne costano dieci.
2. **I calcoli deterministici non passano da un modello.** Somme, percentuali, validazioni di
   schema e conteggi di file sono codice.
3. **Il costo si legge, non si stima.** Ogni invocazione scrive una riga in
   `registro-chiamate.jsonl` con `total_cost_usd` letto dalla risposta, e `lancio costi <id>` lo
   somma. Dal primo lancio in poi, questa sezione smette di essere una stima.

### 4.4 Il costo della macchina è una voce obbligatoria del budget

Nello schema di `budget.json`, `costo_macchina_previsto` è **campo obbligatorio** e
`GATE-TSR-1` **blocca se manca o è zero**. Il suo test rosso è esattamente questo: *un budget senza
`costo_macchina_previsto` deve bloccare*.

---

## 5. IL PAREGGIO

### 5.1 La formula

```
prezzo_netto_per_copia = prezzo − (commissioni per copia) − (imposte per copia) − (rimborsi attesi per copia)

copie_per_pareggio     = costo_totale_previsto ÷ prezzo_netto_per_copia
```

dove `costo_totale_previsto` **include il costo della macchina** — lo schema ha il campo
`include_costo_macchina` proprio per rendere impossibile dimenticarsene senza dichiararlo.

### 5.2 Il pareggio non è un numero: è un confronto

Un pareggio da solo non dice niente. Dice qualcosa solo messo accanto a **quante copie il pubblico
verificato può realisticamente produrre**:

```
copie_possibili_pessimista = pubblico_raggiungibile × tasso_visita_pess × tasso_acquisto_pess
```

| Confronto | Significa |
|---|---|
| `copie_per_pareggio` **>** `copie_possibili_ottimista` | il lancio **non può** andare in pari. Non è un rischio: è un'impossibilità aritmetica. Si cambia prezzo, o pubblico, o non si fa |
| `copie_per_pareggio` **>** `copie_possibili_atteso` | va in pari solo se va meglio del previsto. Decisione umana, presa sapendolo |
| `copie_per_pareggio` **<** `copie_possibili_pessimista` | il lancio regge anche nel caso brutto |

**Questa tabella è il vero prodotto di tutto il documento.** È ciò che trasforma la firma del
prezzo da scelta di gusto in decisione.

### 5.3 Il confronto fra alternative di prezzo

Lo schema prevede `confronto_alternative_prezzo`: un elenco di prezzi con il ricavo atteso di
ciascuno. **È la ragione per cui la previsione viene prima dell'offerta e non dopo.**

La domanda che arriva a chi firma non è *«confermi 47?»*. È:

> *«Su un pubblico verificato di N, con questi tassi: 27 € fanno X, 47 € fanno Y, 97 € fanno Z.
> Il pareggio è a K copie. Confermi 47?»*

Il tempo di lettura è lo stesso. La qualità della decisione no.

---

## 6. LE TRE SOGLIE — quando un lancio non si fa

Queste soglie **non sono controlli automatici** e non stanno nel registro come gate: sono i criteri
con cui una persona decide. Stanno qui perché siano scritti prima, quando non c'è ancora niente da
difendere.

| # | Soglia | Cosa si fa |
|---|---|---|
| **1** | Il ricavo **pessimista** è sotto il `costo_totale_previsto` | il lancio non si fa a queste condizioni. Si cambia prezzo, o pubblico, o si accetta di perderci **per iscritto e con la ragione** (acquisire clienti, provare un canale) |
| **2** | `copie_per_pareggio` supera le copie possibili nello scenario **ottimista** | non si fa. È aritmetica, non prudenza |
| **3** | Il `costo_macchina_previsto` supera **il 10%** del ricavo atteso | il sistema costa troppo per questo lancio. Su lanci piccoli si fa a mano: un ecosistema che mangia un decimo del ricavo è un lusso, non uno strumento |

**La soglia 3 è quella che protegge dall'errore tipico di questa azienda:** costruire una macchina
elegante attorno a un ricavo che non la ripaga.

---

## 7. GLI OBBLIGHI CHE COSTANO — struttura, non aliquote

> **Avvertenza necessaria.** Questa sezione dice **quali voci esistono** e **come entrano nel
> conto**. Non contiene aliquote né percentuali: il regime fiscale di Digital Empire non è
> dichiarato in nessun documento che ho trovato sul disco, e un numero fiscale inventato in un
> piano è peggio di un numero assente, perché sembra vero.
>
> **Le tre domande al commercialista stanno al §8, e vanno fatte prima del primo incasso, non dopo.**

| Materia | Come entra nel conto | Chi deve confermare |
|---|---|---|
| **Diritto di recesso** | prodotti digitali venduti a consumatori in UE: 14 giorni. Per il download immediato serve il consenso esplicito alla rinuncia, **raccolto al momento del pagamento** — è campo obbligatorio dello schema dell'offerta. Senza, il rimborso è dovuto anche a prodotto già scaricato: entra come `quota_rimborsi` più alta | commercialista |
| **Imposta sul valore aggiunto** | per i servizi digitali a consumatori UE l'imposta segue il paese del cliente, con un regime dedicato di dichiarazione unica. Effetto pratico: **il prezzo esposto e l'incasso netto divergono in modo diverso per ogni paese** | commercialista |
| **Documento fiscale** | ogni vendita ne produce uno. Se la cassa non lo emette da sola, lo emette una persona: quel tempo è un costo del lancio e va in `voci` come voce con importo | commercialista |
| **Consenso alla misura** | se il tracciamento parte solo dopo il consenso, i numeri misurati sono **sistematicamente più bassi del vero**. La quota va dichiarata in `funnel.json`, o ogni previsione tarata su quei numeri è sbagliata di una quantità nota e taciuta | nessuno: è una misura, si fa |
| **Contenuti generati** | dove la legge lo impone, il contenuto prodotto da un modello va dichiarato come tale | commercialista o legale |

---

## 8. COSA L'AZIENDA NON SA — la lista, e come si smette di non saperlo

Questa è la sezione che rende il documento onesto. **Il primo lancio gira quasi interamente su
assunzioni, e va dichiarato adesso**, non scoperto a consuntivo.

| # | Numero mancante | Perché manca | Come si misura | Quando |
|---|---|---|---|---|
| 1 | **Il pubblico raggiungibile** | nessuno l'ha mai contato; il canale che doveva portarlo è spento dal 29/07/2026 | si compila `pubblico.json` a mano, canale per canale, con la prova | giorno uno |
| 2 | **Il tasso di visita** | nessun lancio precedente misurato | si misura al primo lancio | primo lancio |
| 3 | **Il tasso di acquisto** | idem | idem | primo lancio |
| 4 | **La quota di rimborsi** | idem | idem, a 14 giorni dalla chiusura | primo lancio + 14 giorni |
| 5 | **Le commissioni di incasso** | la cassa non è ancora collegata | si leggono sulla transazione di prova del giorno zero | giorno zero |
| 6 | **Il costo in token per lancio** | nessuno script dell'azienda usa ancora il ponte verso gli agenti | `registro-chiamate.jsonl` + `lancio costi` | primo lancio |
| 7 | **Il regime fiscale applicabile** | non dichiarato in nessun documento sul disco | tre domande al commercialista (sotto) | prima del primo incasso |
| 8 | **La quota di consenso alla misura** | nessun tracciamento installato | si legge dallo strumento di misura dopo l'installazione | giorno zero |

### Le tre domande al commercialista, da fare prima del primo incasso

1. Con quale regime vendiamo un prodotto digitale a un consumatore italiano, e con quale a un
   consumatore di un altro paese UE?
2. Chi emette il documento fiscale: la cassa o noi? Se noi, con che tempi?
3. Che cosa dobbiamo esporre al cliente prima del pagamento perché la rinuncia al recesso sia
   valida?

**Nessuna delle tre richiede il piano.** Si possono fare oggi.

---

## 9. IL CONFINE CON LA TESORERIA

| | |
|---|---|
| Chi possiede il **previsto** | questo ecosistema (`previsione.json`, `budget.json`) |
| Chi possiede il **reale** | questo ecosistema lo **legge** (`consuntivo.json`), la Tesoreria lo **possiede** |
| Se i due numeri divergono | **ha ragione la Tesoreria**, e la divergenza è un difetto da registrare |
| Direzione del flusso | ogni euro nasce qui e **sale** in Tesoreria. Non scende mai |

`ART-CNS` legge il ricavo da un'origine verificabile — il fornitore di pagamento o l'esporto della
piattaforma — e `GATE-CNS-1` **blocca un consuntivo dichiarato a mano**. Il suo test rosso è
proprio quello: *un consuntivo con ricavo dichiarato a mano e origine assente deve bloccare*.

---

## 10. COME SI VERIFICA CHE QUESTO DOCUMENTO SIA RISPETTATO

| Cosa | Comando o meccanismo |
|---|---|
| Gli schemi dei due artefatti sono validi | `cd dati && PYTHONIOENCODING=utf-8 python valida_registro.py` |
| Una previsione è ben formata | validazione contro `dati/schemi/previsione.schema.json` |
| Un'assunzione non si spaccia per misura | `GATE-PRV-1`, test rosso dichiarato |
| Il costo della macchina è nel budget | `GATE-TSR-1`, test rosso dichiarato |
| Lo sforamento in corsa non uccide il lancio | `GATE-TSR-2`: blocca la spesa nuova, riporta a `DATATO`, sblocco solo con firma tracciata |
| Il consuntivo non è dichiarato a mano | `GATE-CNS-1`, test rosso dichiarato |
| Il costo speso davvero | `lancio costi <id>`, letto da `registro-chiamate.jsonl` |

---

## Connessioni

- `dati/registro.yaml` — la fonte di verità
- `dati/schemi/previsione.schema.json` · `dati/schemi/budget.schema.json` · `dati/schemi/consuntivo.schema.json`
- [[00-LEGGIMI]] — il problema, la tesi, il primo giorno
- [[01-ARCHITETTURA]] — la catena, il ponte, gli obblighi di legge (§9)
- [[03-FLUSSO-OFFERTA]] — dove questa previsione diventa una firma
- `company/Memory/decisions/ADR-014-il-codice-torna-a-chiamare-un-modello.md` — la tassa per invocazione
- `company/Memory/decisions/ADR-020` — Tesoreria, che possiede il reale
