---
Type: PROJECT
Status: Proposta — versione 4
Tags: #lanci #ecosistema-15 #workflow #fasi #operativo
Created: 2026-09-05
Last updated: 2026-09-05
Versione: 4
---

# 08 — I WORKFLOW

> **Regola di lettura:** questo documento spiega. Il registro decide.
> Se una riga qui contraddice `dati/registro.yaml`, ha torto questa riga.

---

## 1. COSA RENDE UN WORKFLOW ESEGUIBILE

La versione 3 di questo piano aveva sette flussi. I revisori li hanno smontati tutti per lo
stesso motivo: **fasi senza agente, fasi senza criterio di uscita**, e un flusso — quello del
funnel — che non aveva né l'uno né l'altro.

Un elenco di buone intenzioni in ordine cronologico non è un workflow: **è un promemoria**. La
differenza si misura in una domanda sola: se do questo documento a chi costruisce, sa cosa fare
senza chiedere niente a nessuno? Con un promemoria, no. Con un workflow, sì.

Qui ogni fase dichiara cinque campi, e sono obbligatori tutti e cinque. Li verifica INV-18, che
è un controllo eseguito da un programma e non una raccomandazione.

| Campo | Cosa contiene | Perché senza è rotta |
|---|---|---|
| `agente` | l'identificativo dell'agente che esegue la fase | una fase senza esecutore non parte da sola, e nessuno risponde di com'è venuta. L'agente deve esistere davvero: il validatore lo cerca nell'elenco degli agenti |
| `ingresso` | cosa deve esistere sul disco prima che la fase parta | una fase che parte con gli ingressi incompleti produce un artefatto che sembra fatto. Il difetto si scopre a valle, dove costa di più |
| `uscita` | cosa lascia sul disco quando finisce | il lavoro di una fase è un file, o un campo dentro un file. Se non è scritto dove va a finire, due fasi possono scrivere lo stesso campo e l'ultima vince in silenzio |
| `criterio_uscita` | il predicato che dice che è finita | **è il campo che divide un workflow da un promemoria.** Una fase senza criterio non finisce: smette quando qualcuno si stanca |
| `modi_fallimento` | come può andare storta, e cosa si fa in quel caso | senza, il primo intoppo diventa una domanda a una persona. Con, la fase sa già dove va a sbattere e dove si torna |

**Sul criterio di uscita, che è quello che conta.** Non è «quando è pronta» e non è «quando il
responsabile approva». È una condizione che si può verificare guardando i file. Esempio, dal
registro, fase `ME-2`:

> *ogni canale con `raggiungibili_verificati>0` ha una prova fra `esporto-lista`,
> `schermata-conteggio-piattaforma`, `misura-analytics`, con data non anteriore a 30 giorni*

Chi esegue quella fase sa quando fermarsi, e chiunque altro può controllare se ha ragione senza
chiederglielo.

### La differenza fra una FASE e un GATE

| | Fase | Gate |
|---|---|---|
| cosa fa | **produce** | **giudica** |
| dove sta | dentro un workflow | fuori dai workflow, in `gate_finale` |
| chi la esegue | l'agente del reparto proprietario | `lan-gate`, che è di `LAN-QLT` |
| cosa lascia | un artefatto o una sua parte | un verbale, anche quando lascia passare |
| può riscrivere ciò che tocca | sì, è il suo mestiere | **no**: `lan-gate` non ha `Write` né `Edit` (INV-09) |

**La regola che tiene insieme le due colonne: nessun workflow contiene il proprio gate fra le
fasi.** I gate stanno nel campo `gate_finale` del workflow, e li esegue `lancio avanza` — mai il
reparto. Un flusso che si autogiudica non è giudicato.

> *Il difetto che ripara, misurato dai revisori:* nel flusso Prodotto della versione 3, **cinque
> controlli su sette erano eseguiti dallo stesso agente che aveva prodotto la cosa da
> controllare**, mentre dieci righe sopra era scritta la regola «chi produce non approva». Un
> difetto sistematico del produttore era invisibile al controllo per costruzione, perché il
> controllo era quel produttore. Oggi lo impedisce **INV-01** (`giudice != produttore`), che è
> un programma e non un'opinione.

Ne discende una conseguenza pratica per chi costruisce: **una fase non chiude mai un gate.**
Chiude il proprio criterio di uscita, scrive quello che deve scrivere, e finisce. Il verdetto
arriva dopo, da fuori, e può rimandarla indietro.

---

## 2. LA MAPPA DEI DIECI FLUSSI

```
  STATO           FLUSSO            REPARTO    FASI   PRODUCE            CHIUDE CON
  ─────────────────────────────────────────────────────────────────────────────────────
  IDEA
    │
    ├──────────►  WF-MERCATO        LAN-MER      5    pubblico, ricerca  GATE-PUB-1
    │                                                                    GATE-INT-1
    └──────────►  WF-STRATEGIA      LAN-STR      2    decisione          GATE-STR-1
  VALUTATO
    │
    └──────────►  WF-PRODOTTO       LAN-PRD      4    certificato        GATE-PRD-1
  ISTRUITO
    │
    └──────────►  WF-OFFERTA        LAN-OFF      6    previsione         GATE-PRV-1
                  ◄── il cuore                        OFFERTA            GATE-OFF-1
  DATATO                                              (prezzo + data)
    │
    ├──────────►  WF-PAROLA         LAN-CPY      5    testi              GATE-CPY-1
    └──────────►  WF-TESORO         LAN-TSR      4    budget             GATE-TSR-1
  IN_PRODUZIONE                                                          GATE-TSR-2
    │
    ├──────────►  WF-VENDITA        LAN-FNL      4    pagine + cassa     GATE-FNL-1
    └──────────►  WF-EDITORIALE     LAN-EDT      3    piano editoriale   GATE-EDT-1
  PRONTO
    │
    └──────────►  WF-REGIA          LAN-REG      5    apertura           GATE-REG-1
  APERTO ─► CHIUSO                                    consuntivo         GATE-CNS-1
    │
    └──────────►  WF-MEMORIA        LAN-MEM      4    debrief            GATE-MEM-1
  APPRESO   ◄── l'unico finale buono
```

| Workflow | Reparto | Produce | Fasi | Gate finale | Ore | Da → A |
|---|---|---|---:|---|---|---|
| `WF-MERCATO` | `LAN-MER` | `ART-PUB`, `ART-RIC` | 5 | `GATE-PUB-1`, `GATE-INT-1` | 3-6 | `IDEA` → `VALUTATO` |
| `WF-STRATEGIA` | `LAN-STR` | `ART-DEC` | 2 | `GATE-STR-1` | 1-2 | `IDEA` → `VALUTATO` |
| `WF-PRODOTTO` | `LAN-PRD` | `ART-CRT` | 4 | `GATE-PRD-1` | 2-4 · 1-2 retroattiva | `VALUTATO` → `ISTRUITO` |
| **`WF-OFFERTA`** | `LAN-OFF` | `ART-PRV`, `ART-OFF` | 6 | `GATE-PRV-1`, `GATE-OFF-1` | 3-5 + firma | `ISTRUITO` → `DATATO` |
| `WF-PAROLA` | `LAN-CPY` | `ART-CPY` | 5 | `GATE-CPY-1` | 8-14 | `DATATO` → `IN_PRODUZIONE` |
| `WF-VENDITA` | `LAN-FNL` | `ART-FNL` | 4 | `GATE-FNL-1` | 6-12 | `IN_PRODUZIONE` → `IN_PRODUZIONE` |
| `WF-EDITORIALE` | `LAN-EDT` | `ART-EDT` | 3 | `GATE-EDT-1` | 4-8 | `IN_PRODUZIONE` → `IN_PRODUZIONE` |
| `WF-TESORO` | `LAN-TSR` | `ART-BDG` | 4 | `GATE-TSR-1`, `GATE-TSR-2` | 2-4 | `DATATO` → `IN_PRODUZIONE` |
| `WF-REGIA` | `LAN-REG` | `ART-APE`, `ART-CNS` | 5 | `GATE-REG-1`, `GATE-CNS-1` | 3-5 + carrello | `IN_PRODUZIONE` → `CHIUSO` |
| `WF-MEMORIA` | `LAN-MEM` | `ART-DBR` | 4 | `GATE-MEM-1` | 2-4 | `CHIUSO` → `APPRESO` |
| | | **13 artefatti** | **42** | **14 gate** | **34-64 ore** | |

**Le 34-64 ore sono il lavoro di UN lancio**, non la costruzione del sistema. La costruzione sta
in `04-COSTRUZIONE.md` ed è un conto diverso: 118-174 ore.

**Tre osservazioni che si leggono dalla tabella:**

1. **`WF-PAROLA` è il flusso più caro** (8-14 ore) e `WF-VENDITA` il secondo (6-12). Insieme
   fanno più della metà del lavoro di un lancio.
2. **Tre flussi non cambiano stato** (`WF-VENDITA`, `WF-EDITORIALE`, e `WF-PAROLA` che ci entra):
   girano tutti dentro `IN_PRODUZIONE`. Lo stato cambia solo quando la Regia trova tutte le
   condizioni vere insieme.
3. **`WF-OFFERTA` è l'unico che dipende da una firma umana per avanzare**, e per questo la sua
   durata non è stimabile: 3-5 ore di lavoro più il tempo che passa. Nel caso del prodotto pilota
   di questa azienda, quel tempo è finora **sei mesi**.

---

## 3. I DIECI FLUSSI, UNO PER UNO

### 3.1 `WF-MERCATO` — chi c'è là fuori

| | |
|---|---|
| **Reparto** | `LAN-MER` (Mercato) |
| **Produce** | `ART-PUB` (`pubblico.json`), `ART-RIC` (`ricerca.json`) |
| **Innesco** | un lancio entra in `IDEA` |
| **Da → A** | `IDEA` → `VALUTATO` |
| **Chiude con** | `GATE-PUB-1`, `GATE-INT-1` |
| **Ore** | 3-6 |

**Perché è il primo di tutti.** Perché il piano precedente progettava il lancio di un prodotto il
cui canale di traffico era spento da cinque settimane, e non lo sapeva. Prima di ogni altra cosa
si conta chi c'è davvero.

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `ME-1` | censimento dei canali | `lan-pub-censore` | l'elenco dei canali dell'azienda | `pubblico.json`, sezione `canali[]` | ogni canale noto compare, **anche quelli a zero** |
| `ME-2` | prova di ogni numero | `lan-pub-censore` | i canali elencati | ogni canale con `prova.tipo` e `prova.data` | ogni canale con `raggiungibili_verificati>0` ha una prova fra `esporto-lista`, `schermata-conteggio-piattaforma`, `misura-analytics`, con data non anteriore a 30 giorni |
| `ME-3` | verifica dei canali morti | `lan-pub-censore` | i canali dichiarati attivi | campo `stato_canale` | ogni canale attivo ha un'attività registrata negli ultimi 90 giorni, oppure è marcato dormiente |
| `ME-4` | raccolta delle parole vere | `lan-int-analista` | il prodotto e il pubblico censito | `ricerca.json`, sezione `frasi[]` | almeno 15 frasi, ognuna con `fonte.url` |
| `ME-5` | buchi dei concorrenti | `lan-int-analista` | l'elenco dei concorrenti noti | `ricerca.json`, sezione `concorrenti[]` | ogni concorrente ha almeno un buco dichiarato con la fonte che lo mostra |

**Modi di fallimento**

- Un canale non è accessibile → si scrive `raggiungibili_verificati=0`, `prova.tipo=null` e il
  motivo.
- Il numero è noto ma la prova non è recuperabile → **il canale vale zero**. È legittimo scrivere
  che non si sa; non è legittimo contare ciò che non si sa.
- Il canale è stato dirottato su un altro progetto → vale zero e la cosa entra nel verbale. *È
  esattamente ciò che è successo al canale del Manuale il 29/07/2026.*
- Non si arriva a 15 frasi con fonte → si consegna quello che c'è e **il gate blocca**: meglio un
  blocco visibile di quindici frasi inventate.
- Nessun concorrente identificabile → si dichiara e si prosegue. L'assenza di concorrenti è un
  dato, spesso cattivo.

---

### 3.2 `WF-STRATEGIA` — si fa adesso?

| | |
|---|---|
| **Reparto** | `LAN-STR` (Strategia) |
| **Produce** | `ART-DEC` (`decisione.json`) |
| **Innesco** | `GATE-PUB-1` è passato |
| **Da → A** | `IDEA` → `VALUTATO` |
| **Chiude con** | `GATE-STR-1` |
| **Ore** | 1-2 |

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `ST-1` | le cinque domande | `lan-str-filtro` | `ART-PUB` valido, il prodotto proposto | `decisione.json`, sezione `domande[]` | tutte e cinque hanno risposta `si` o `no`, e ognuna cita l'artefatto che la sostiene |
| `ST-2` | confronto con i lanci in coda | `lan-str-filtro` | l'elenco dei lanci non chiusi | campo `perche_questo_e_non_un_altro` | il campo nomina almeno un lancio alternativo e dice perché viene dopo |

**Modi di fallimento**

- Una domanda non ha un artefatto che la sostenga → **la risposta è `no`**. Una risposta senza
  prova vale come negativa, non come dubbio.
- Non ci sono alternative in coda → si dichiara: è il caso normale del primo lancio.

---

### 3.3 `WF-PRODOTTO` — è consegnabile?

| | |
|---|---|
| **Reparto** | `LAN-PRD` (Prodotto) |
| **Produce** | `ART-CRT` (`certificato.json`) |
| **Innesco** | il lancio è `VALUTATO` |
| **Da → A** | `VALUTATO` → `ISTRUITO` |
| **Chiude con** | `GATE-PRD-1` |
| **Ore** | 2-4 integrale · 1-2 retroattiva |

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `PR-1` | scelta della modalità | `lan-prd-collaudatore` | il prodotto e la sua storia | campo `modalita` | vale `integrale` oppure `retroattiva`, e la scelta è motivata |
| `PR-2` | le sei bandiere rosse | `lan-prd-collaudatore` | il file del prodotto | sezione `bandiere_rosse[]` | tutte e sei hanno esito booleano, e chi risulta presente ha la prova allegata |
| `PR-3` | prova dei collegamenti | `lan-prd-collaudatore` | l'elenco dei collegamenti | sezione `link[]` con esito | ogni collegamento è stato aperto e ha un esito registrato |
| `PR-4` | dichiarazione del debito di collaudo | `lan-prd-collaudatore` | la modalità scelta | campo `debito_collaudo` | in retroattiva il campo elenca cosa non è stato verificato e perché |

**Modi di fallimento**

- Il prodotto è nato fuori dal sistema e non ha brief → **modalità retroattiva**. È il percorso
  costruito per il Manuale, pronto dal 07/03/2026: senza, il flusso usciva con errore alla prima
  riga proprio sul prodotto per cui il reparto esiste.
- Una bandiera rossa è presente → il gate blocca, il lancio torna a `VALUTATO` con l'elenco di
  cosa manca.
- Un collegamento è morto → il gate blocca. **La verifica la rifà il gate, non il produttore.**
- Si è tentati di lasciare vuoto il debito di collaudo per far passare il gate → il gate blocca:
  in retroattiva il debito è obbligatorio, anche quando è «nessuno».

---

### 3.4 `WF-OFFERTA` — il cuore

| | |
|---|---|
| **Reparto** | `LAN-OFF` (Offerta) |
| **Produce** | `ART-PRV` (`previsione.json`), `ART-OFF` (`offerta.json`) |
| **Innesco** | `ART-CRT` e `ART-RIC` sono validi |
| **Da → A** | `ISTRUITO` → `DATATO` |
| **Chiude con** | `GATE-PRV-1`, `GATE-OFF-1` |
| **Ore** | 3-5 più il tempo della firma |

> **Questo flusso è spiegato per intero in [[03-FLUSSO-OFFERTA]]**, che contiene la diagnosi di
> dove il prodotto pilota si è fermato davvero, la struttura della firma e le dieci riparazioni.
> Qui c'è solo la tabella operativa, per non dire due volte le stesse cose in modo leggermente
> diverso — che è il difetto da cui è nato tutto questo lavoro.

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `O1` | il ruolo del prodotto | `lan-off-conductor` | `ART-CRT` valido | campo `ruolo_prodotto` | vale `vendita` oppure `acquisizione-contatti` · **punto umano `PU-RUOLO`** |
| `O2` | riconciliazione dei prezzi già dati | `lan-off-conductor` | catalogo, wiki, listino, piani precedenti | sezione `prezzi_precedenti_trovati[]` | ogni fonte trovata è nell'elenco con valore e data |
| `O3` | struttura dell'offerta | `lan-off-conductor` | `ART-CRT`, `ART-RIC` | sezione `struttura` | `valore_dichiarato` è la somma dei soli bonus **con fonte**, la garanzia ha almeno 14 giorni, l'azione richiesta è una sola |
| `O4` | alternative di prezzo con il ricavo | `lan-prv-modello` | `ART-PUB` valido, la struttura | `previsione.json` completo e `confronto_alternative_prezzo[]` | almeno tre prezzi con ricavo atteso, i tre scenari esistono, ogni assunzione dichiara `misurato` o `assunto` |
| `O5` | la proposta e la firma | `lan-off-conductor` | `previsione.json` valido | il testo della proposta e la sua impronta | esiste una proposta di cinque righe con prezzo, data, ricavo atteso, pareggio e caso pessimista · **punto umano `PU-PREZZO`** |
| `O6` | congelamento | `lan-off-conductor` | `offerta.json` con firma valida | `data_chiusura`, lancio in `DATATO` | `GATE-OFF-1` esce 0 e la data di chiusura è coerente |

**I due modi di fallimento che contano**

- La persona non risponde entro 14 giorni a `O5` → il lancio va in `SOSPESO` con la data di
  revisione e **il comando per uscirne**. Qui **non c'è un valore predefinito**, ed è deliberato:
  un prezzo scelto da una macchina produce un danno che si scopre a lancio finito.
- Un agente prova a scrivere il campo `firma` → **il campo è rifiutato**: nessun agente ha
  permesso di scrittura, e il canale deve essere in lista chiusa.

---

### 3.5 `WF-PAROLA` — tutti i testi

| | |
|---|---|
| **Reparto** | `LAN-CPY` (Parola) |
| **Produce** | `ART-CPY` (`copy/manifest.json`) |
| **Innesco** | il lancio è `DATATO`: esistono un prezzo e una data firmati |
| **Da → A** | `DATATO` → `IN_PRODUZIONE` |
| **Chiude con** | `GATE-CPY-1` |
| **Ore** | 8-14 — **il flusso più caro** |

**Perché viene dopo l'offerta e non prima.** Perché ogni testo dice un prezzo e una data. Nella
versione 3 i testi si scrivevano prima, e un cambio di prezzo non invalidava niente: restavano
online pagine che promettevano un numero diverso da quello vero.

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `PA-1` | inventario dei pezzi | `lan-cpy-conductor` | `ART-OFF` firmato, `ART-FNL` se esiste | sezione `pezzi[]` con destinazione | ogni pezzo ha una destinazione risolvibile e un tipo |
| `PA-2` | raccolta delle prove | `lan-cpy-conductor` | `ART-CRT`, `ART-RIC` | l'elenco delle affermazioni dimostrabili | ogni affermazione di categoria `prova` ha un riferimento risolvibile **fuori dal testo stesso** |
| `PA-3` | scrittura dei pezzi | `lan-cpy-conductor` | inventario e prove | i file dentro `copy/` | ogni pezzo dell'inventario esiste come file non vuoto |
| `PA-4` | punteggio | `lan-cpy-conductor` | i pezzi scritti | punteggio per blocco e totale | ogni pezzo ha un punteggio per blocco calcolato con la griglia dichiarata |
| `PA-5` | coerenza con il prezzo firmato | `lan-cpy-conductor` | `ART-OFF` | campo `impronta_offerta` | l'impronta dell'offerta usata coincide con quella dell'offerta corrente |

**Modi di fallimento**

- Un pezzo non ha destinazione → **non si scrive**. Un testo senza posto dove andare è lavoro
  buttato.
- Una prova non esiste → l'affermazione si toglie o si declassa a opinione. Non si scrive un
  numero che non si può mostrare: il gate lo risolve contro `ART-CRT` e `ART-RIC`, **non contro
  il testo**.
- Un pezzo richiede una copertina → si apre **`PU-COPERTINA`**: la copertina la fa Max, la
  macchina fornisce solo cartella aperta, titolo e due righe di brief. Il pezzo resta in attesa e
  compare fra ciò che blocca il lancio.
- Il totale supera 80 ma un blocco sta sotto metà dei suoi punti → **il gate blocca lo stesso**.
  Una media buona nasconde un pezzo rotto.
- Il prezzo cambia dopo la scrittura → tutti i pezzi che lo citano diventano `da_rivedere` e il
  loro controllo si riapre.

---

### 3.6 `WF-VENDITA` — le pagine, e la prova che incassano

| | |
|---|---|
| **Reparto** | `LAN-FNL` (Vendita) |
| **Produce** | `ART-FNL` (`funnel.json`) |
| **Innesco** | esistono i testi approvati |
| **Da → A** | `IN_PRODUZIONE` → `IN_PRODUZIONE` |
| **Chiude con** | `GATE-FNL-1` |
| **Ore** | 6-12 |

**Perché la prova di cassa sta qui e non in fondo.** Perché la versione precedente metteva la
pubblicazione irreversibile **prima** della prova che il pagamento funzionasse. Si vende solo
dopo che un euro vero è entrato ed è tornato indietro.

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `VE-1` | messa online delle pagine | `lan-fnl-costruttore` | `ART-CPY` approvato | sezione `pagine[]` con indirizzo | ogni pagina risponde 200 **da una rete esterna** |
| `VE-2` | installazione della misura | `lan-fnl-costruttore` | le pagine online | `evento_conversione` per ogni pagina | l'evento è stato **visto arrivare** nello strumento di misura, con origine `piattaforma` |
| `VE-3` | prova di cassa | `lan-fnl-costruttore` | la pagina di pagamento collegata | sezione `prova_cassa` | `prova_cassa.stato` vale `incassato_e_rimborsato` e il riferimento della transazione è leggibile nel pannello del fornitore |
| `VE-4` | quota di consenso alla misura | `lan-fnl-costruttore` | lo strumento installato | campo `quota_consenso` | è un numero letto dallo strumento, oppure è dichiarata sconosciuta |

**Modi di fallimento**

- Una pagina non risponde → resta nell'elenco con l'esito, il gate blocca, **le pagine buone
  restano**.
- L'evento non arriva → il gate blocca. **Non si accetta una schermata**: la prova si legge dalla
  piattaforma, altrimenti il gate si fida di chi giudica.
- Il pagamento non va a buon fine → **il lancio non avanza**. È la condizione che nella versione
  precedente non esisteva, e riguarda il difetto più grave trovato dai revisori: l'azienda non
  può incassare un euro.
- La quota di consenso non è misurabile → si dichiara sconosciuta. Senza, ogni previsione tarata
  su quei numeri è sbagliata **di una quantità nota e taciuta**.

---

### 3.7 `WF-EDITORIALE` — i giorni del lancio

| | |
|---|---|
| **Reparto** | `LAN-EDT` (Editoriale) |
| **Produce** | `ART-EDT` (`editoriale.json`) |
| **Innesco** | esistono i testi e le pagine |
| **Da → A** | `IN_PRODUZIONE` → `IN_PRODUZIONE` |
| **Chiude con** | `GATE-EDT-1` |
| **Ore** | 4-8 |

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `ED-1` | calendario a ritroso | `lan-edt-pianificatore` | `ART-OFF`: `data_apertura` e `durata_carrello_gg` | sezione `giorni[]` | ogni giorno fra oggi e la chiusura del carrello esiste come riga |
| `ED-2` | assegnazione dei contenuti | `lan-edt-pianificatore` | `ART-CPY`, i giorni | ogni contenuto con giorno, canale e destinazione | ogni giorno del carrello ha almeno un contenuto, e ogni contenuto punta a una pagina esistente in `ART-FNL` |
| `ED-3` | marcatura degli invii reali | `lan-edt-pianificatore` | il piano assegnato | campo `richiede_autorizzazione` | ogni riga che comporta un invio alla lista è marcata come punto umano · **`PU-INVIO`** |

**Modi di fallimento**

- La data di apertura è troppo vicina per il piano → si dichiara il numero di giorni mancanti e
  **la Regia decide se spostare**.
- Un contenuto punta a una pagina inesistente → il gate blocca.
- L'autorizzazione all'invio non arriva → **l'invio non parte**. Un'email spedita non si
  richiama, e non avrà mai un valore predefinito.

---

### 3.8 `WF-TESORO` — quanto costa e quando si rientra

| | |
|---|---|
| **Reparto** | `LAN-TSR` (Tesoro) |
| **Produce** | `ART-BDG` (`budget.json`) |
| **Innesco** | il lancio è `DATATO` |
| **Da → A** | `DATATO` → `IN_PRODUZIONE` |
| **Chiude con** | `GATE-TSR-1`, `GATE-TSR-2` |
| **Ore** | 2-4 |

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `TE-1` | voci di costo | `lan-tsr-contabile` | il piano del lancio | sezione `voci[]` | ogni voce ha importo, tipo e stato; le voci impegnate hanno chi le ha autorizzate |
| `TE-2` | costo della macchina | `lan-tsr-contabile` | le invocazioni previste per agente | campo `costo_macchina_previsto` | il campo è presente e maggiore di zero |
| `TE-3` | pareggio | `lan-tsr-contabile` | `ART-PRV` | sezione `pareggio` | `copie_per_pareggio` è calcolato da `previsione.json`, e lo scenario usato è dichiarato |
| `TE-4` | sorveglianza dello scarto | `lan-tsr-contabile` | i movimenti registrati | sezione `scarto_corrente` | lo scarto è **ricalcolato dai movimenti**, mai dalla dichiarazione · **fase continua** |

**Modi di fallimento**

- Una voce passa a `impegnato` senza autorizzazione → **lo schema la rifiuta**: impegnare denaro
  è una decisione umana.
- Manca `costo_macchina_previsto` → `GATE-TSR-1` blocca. Ripara il difetto per cui la versione
  precedente prevedeva 41 agenti senza una riga sul costo.
- Manca la previsione → il pareggio non si calcola e il gate blocca. Nella versione precedente il
  gate chiedeva un pareggio che **nessun artefatto produceva**: era insoddisfacibile per
  costruzione.
- Lo scarto supera il dieci per cento → la spesa nuova si blocca e il lancio torna a `DATATO`:
  **non muore**. Si sblocca solo con firma umana tracciata (`PU-SPESA`).

---

### 3.9 `WF-REGIA` — l'apertura e la misura

| | |
|---|---|
| **Reparto** | `LAN-REG` (Regia) |
| **Produce** | `ART-APE` (`apertura.json`), `ART-CNS` (`consuntivo.json`) |
| **Innesco** | testi, pagine, piano editoriale e budget sono tutti validi |
| **Da → A** | `IN_PRODUZIONE` → `CHIUSO` |
| **Chiude con** | `GATE-REG-1`, `GATE-CNS-1` |
| **Ore** | 3-5 più i giorni del carrello |

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `RE-1` | lista di sincronizzazione | `lan-reg-calendarista` | tutti gli artefatti da `ART-PUB` a `ART-BDG` | sezione `lista_sincronizzazione[]` | ogni voce ha esito booleano, e la validità di ogni artefatto è **ricalcolata dai file**, mai letta dallo stato salvato |
| `RE-2` | richiesta del via libera | `lan-reg-calendarista` | la lista tutta vera | campo `via_libera` in attesa | esiste una richiesta esplicita con tutto ciò che serve per decidere in una schermata · **`PU-APERTURA`** |
| `RE-3` | apertura | `lan-reg-calendarista` | `via_libera` firmato per canale ammesso | lancio in `APERTO` | `GATE-REG-1` esce 0 e lo stato è `APERTO` |
| `RE-4` | misura quotidiana | `lan-reg-tracciatore` | il lancio aperto | una riga al giorno con ordini e ricavo | ogni giorno del carrello ha una riga con origine dichiarata · **fase continua** |
| `RE-5` | consuntivo | `lan-reg-tracciatore` | le righe quotidiane, la chiusura | `consuntivo.json` | `ricavo_lordo` ha origine `fornitore-pagamento` o `esporto-piattaforma`, il periodo copre tutte le date del carrello, e gli ordini sono coerenti con ricavo diviso prezzo |

**Modi di fallimento**

- Nove voci vere e una falsa → **il gate blocca** e il lancio torna a `IN_PRODUZIONE` con
  l'elenco delle voci false. Una lista quasi completa non è una lista completa.
- Il via libera non arriva → il lancio resta in `PRONTO`, **senza scadenza**. Aprire una vendita
  è irreversibile verso l'esterno: non ha e non avrà mai un valore predefinito.
- Un gate rifiuta dopo la sincronizzazione → si torna a `IN_PRODUZIONE`. È l'unica transizione
  autorizzata dal gate stesso.
- Il fornitore di pagamento non risponde → codice 3, la riga resta mancante **e dichiarata tale**:
  non si stima.
- Il ricavo è dichiarato a mano → il gate blocca e il lancio resta `APERTO` finché il consuntivo
  non ha un'origine verificabile.

---

### 3.10 `WF-MEMORIA` — cosa impariamo

| | |
|---|---|
| **Reparto** | `LAN-MEM` (Memoria) |
| **Produce** | `ART-DBR` (`debrief.json`) |
| **Innesco** | il lancio è `CHIUSO` e il consuntivo è valido |
| **Da → A** | `CHIUSO` → `APPRESO` |
| **Chiude con** | `GATE-MEM-1` |
| **Ore** | 2-4 |

**Perché esiste.** Perché senza, un lancio finito lascia solo un numero. Un numero senza confronto
non insegna niente: si archivia e si ricomincia da zero al lancio dopo.

| # | Fase | Agente | Ingresso | Uscita | Criterio di uscita |
|---|---|---|---|---|---|
| `MM-1` | calcolo degli scarti | `lan-mem-distillatore` | `ART-PRV` e `ART-CNS` | sezione `scarti[]` | ogni voce prevista ha accanto la voce reale e la differenza in percentuale |
| `MM-2` | cause degli scarti | `lan-mem-distillatore` | gli scarti calcolati | una causa per ogni scarto oltre il 10% | nessuno scarto oltre soglia è privo di causa |
| `MM-3` | distillazione degli schemi | `lan-mem-distillatore` | cause e verbali del lancio | sezione `schemi[]` | almeno tre schemi, ognuno con `si_applica_quando` non vuoto e un riferimento a un artefatto esistente |
| `MM-4` | controfirma della Regia | `lan-reg-calendarista` **(`reparto_ospite: LAN-REG`)** | il debrief completo | campo `controfirma` | la Regia ha controfirmato, oppure ha lasciato scritta l'obiezione accanto |

**Modi di fallimento**

- Manca la previsione perché il lancio è vecchio → si dichiara e il debrief resta parziale,
  **marcato come tale**.
- La causa non si conosce → si scrive «non nota» **e si dice quale misura sarebbe servita**. È un
  risultato utile: dice cosa installare prima del prossimo lancio.
- Gli schemi sono generici → il gate blocca: **uno schema che si applica sempre non si applica
  mai**.
- Regia e Memoria non sono d'accordo → l'obiezione resta scritta accanto invece di essere
  negoziata via. Nessuno dei due scrive da solo la storia di com'è andata.

> **`MM-4` è l'unica fase di tutto il sistema eseguita da un agente di un altro reparto**, e per
> questo dichiara `reparto_ospite: LAN-REG`. Senza quella dichiarazione, `INV-19` boccerebbe il
> workflow — ed è la prova che l'invariante funziona: la deroga esiste, ma va scritta.

---

## 4. I PUNTI UMANI DENTRO I FLUSSI

Sei punti umani, distribuiti dentro i flussi. Ognuno dichiara scadenza, valore predefinito e
comportamento allo scadere: lo verifica `INV-06`.

| Punto | Dove si apre | Domanda | Scadenza | Predefinito | Allo scadere |
|---|---|---|---|---|---|
| `PU-RUOLO` | `WF-OFFERTA` / `O1` | il prodotto si vende o è un regalo? | **7 giorni** | **`vendita`** | si procede col predefinito, si scrive `ruolo_scelto_per_silenzio` e la data di revisione, **e si avvisa** |
| `PU-PREZZO` | `WF-OFFERTA` / `O5` | confermi il prezzo e la data proposti? | **14 giorni** | **nessuno** | `SOSPESO` con `revisione_il` e `come_si_esce` come comando eseguibile |
| `PU-COPERTINA` | `WF-PAROLA` / `PA-3` | la copertina la fa Max: è pronta? | **3 giorni** | nessuno | il pezzo resta in attesa e compare fra ciò che blocca il lancio |
| `PU-INVIO` | `WF-EDITORIALE` / `ED-3` | autorizzo l'invio reale alla lista? | nessuna | nessuno | l'invio non parte |
| `PU-APERTURA` | `WF-REGIA` / `RE-2` | do il via libera all'apertura della vendita? | nessuna | nessuno | resta in `PRONTO`, senza scadenza |
| `PU-SPESA` | `GATE-TSR-2` | autorizzo questa spesa oltre il tetto? | nessuna | nessuno | la spesa non parte, il lancio prosegue con quanto già speso |

### 4.1 La regola, e il fallimento che l'ha resa necessaria

**Il cronometro sta su OGNI punto umano aperto, non sulla firma finale.**

Nella versione 3 il cronometro stava solo sulla firma del prezzo, e contava «da quanti giorni la
proposta aspetta». Sembra ragionevole. Non lo è, e il caso reale lo dimostra:

Il prodotto pilota di questa azienda si è fermato **una domanda prima**, su `PU-RUOLO` — si vende
o si regala? — che nella versione 3 non aveva né scadenza né valore predefinito. E finché quella
domanda resta aperta, **una proposta di prezzo non nasce**. Se la proposta non nasce, il
contatore «da quanti giorni la proposta aspetta» **non parte mai**.

> **Il fallimento era invisibile alla sua stessa misura.** Sei mesi di fermo, e nessun cruscotto
> avrebbe mostrato un solo giorno di ritardo.

### 4.2 I tre casi, e perché sono trattati in modo diverso

| Caso | Come si tratta | Perché |
|---|---|---|
| **La scelta è reversibile** (`PU-RUOLO`) | scadenza + valore predefinito + dichiarazione | fra due strade, quando il tempo scade, si prende quella da cui si torna indietro. Un prodotto venduto può diventare un regalo; un prodotto regalato non si rimette in vendita senza bruciare chi l'ha avuto gratis |
| **La scelta non è reversibile ma è interna** (`PU-PREZZO`) | scadenza, **nessun predefinito**, si va in `SOSPESO` | un prezzo scelto da una macchina per sbloccare un controllo produce un danno che si scopre a lancio finito. Il rinvio invece si vede e si corregge: fra un errore invisibile e un ritardo visibile, si sceglie il ritardo |
| **La scelta è irreversibile verso l'esterno** (`PU-APERTURA`, `PU-INVIO`, `PU-SPESA`) | **nessuna scadenza e nessun predefinito** | un'email spedita non si richiama, una vendita aperta non si chiude in silenzio, un euro impegnato è impegnato |

`PU-COPERTINA` sta a parte: non è una decisione, è un lavoro che solo Max fa. La macchina fornisce
cartella aperta, titolo e due righe di brief, e aspetta. **Era il punto umano più frequente
dell'intero piano e nella versione 3 non compariva in nessuna tabella.**

---

## 5. COSA SUCCEDE QUANDO UNA FASE FALLISCE

I quarantadue modi di fallimento dichiarati nei dieci flussi ricadono in cinque famiglie. Per
ognuna il sistema ha una risposta fissa, e nessuna delle cinque perde il lavoro già fatto.

| Famiglia | Esempi | Cosa fa il sistema |
|---|---|---|
| **Un dato manca** | non si arriva a 15 frasi con fonte · manca `costo_macchina_previsto` · una riga del piano editoriale è incompleta | si consegna quello che c'è, **il gate blocca**, e il verbale elenca cosa manca. Il parziale resta sul disco |
| **Una prova non è ottenibile** | il numero del canale è noto ma la prova no · l'evento di misura non arriva · la quota di consenso non è misurabile | **il dato vale zero oppure si dichiara sconosciuto.** È legittimo scrivere che non si sa; non è legittimo contare ciò che non si sa |
| **Un'autorizzazione non arriva** | il ruolo del prodotto · la firma sul prezzo · il via libera · l'invio · la spesa | dipende dalla reversibilità: valore predefinito dichiarato, oppure `SOSPESO`, oppure attesa senza scadenza (§4.2) |
| **Un cambio a monte invalida il lavoro a valle** | il prezzo cambia dopo che i testi sono scritti · la proposta è rigenerata dopo la firma · la previsione cambia dopo l'offerta | gli artefatti che dipendono diventano **`da_rivedere`** e i loro controlli si riaprono. L'impronta è ciò che se ne accorge |
| **Un fornitore esterno non risponde** | il fornitore di pagamento è irraggiungibile · una pagina non risponde | **codice 3**: il lancio non avanza, lo stato non cambia, il lavoro fatto è salvato. Si riprende, non si ricomincia |

### 5.1 Le tre regole che valgono per tutte e cinque

1. **Nessun fallimento cancella il lavoro fatto.** Ogni ramo di fallimento dice cosa si conserva:
   le frasi con fonte valida, le pagine conformi, i testi sopra soglia, il certificato parziale.
2. **Ogni blocco dice dove si torna.** È `INV-03`: un controllo che blocca senza dire dove si
   torna produce un lancio fermo e nessuno sa a chi tocca. Nella versione 3 **nessuno dei
   controlli lo diceva**.
3. **Uno sforamento di budget non uccide il lancio.** `GATE-TSR-2` blocca la spesa nuova e riporta
   il lancio indietro di uno stato. Uno sforamento che uccide il lancio è un difetto di progetto,
   non un controllo.

---

## 6. LE FASI CONTINUE

Due fasi su quarantadue hanno `tipo_fase: continua`. Non finiscono con un criterio: **girano
finché il lancio si trova in un certo stato.**

| Fase | Workflow | Gira mentre | Cosa fa |
|---|---|---|---|
| `TE-4` sorveglianza dello scarto | `WF-TESORO` | il lancio è in `IN_PRODUZIONE` | ricalcola `scarto_corrente` dai movimenti registrati, non dalle dichiarazioni |
| `RE-4` misura quotidiana | `WF-REGIA` | il lancio è `APERTO` | scrive una riga al giorno con ordini e ricavo letti dai pannelli |

**Perché sono diverse dalle altre.** Una fase normale ha un criterio di uscita perché deve
finire. Queste due non devono finire: devono **accorgersi di qualcosa mentre succede**. Una
sorveglianza che finisce non sorveglia.

### 6.1 Lo sforamento di budget non uccide il lancio

`GATE-TSR-2` è l'unico controllo del sistema di tipo `continuo`, ed è legato a `TE-4`.

```
IN_PRODUZIONE  ──scarto oltre il 10%──►  DATATO
                                          │
                                          │  la spesa nuova è bloccata
                                          │  il lavoro fatto resta
                                          │
                                          └──firma umana tracciata (PU-SPESA)──► IN_PRODUZIONE
```

Il lancio **torna indietro di uno stato**, non muore. E si sblocca solo con una firma umana
registrata, mai da solo.

> Il test rosso dichiarato per questo controllo è esattamente questo: *uno scarto dell'undici per
> cento deve bloccare la spesa nuova e **non** uccidere il lancio.* Un controllo che uccide ciò
> che dovrebbe proteggere è peggio dell'assenza del controllo.

---

## 7. COME SI VERIFICA CHE UN WORKFLOW SIA BEN FORMATO

Tre invarianti governano i flussi, e li esegue un programma.

```bash
cd PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati
PYTHONIOENCODING=utf-8 python valida_registro.py
# 832 controlli eseguiti → PIANO COERENTE  (uscita 0)
```

| Invariante | Verifica che… | Perché serve |
|---|---|---|
| **INV-17** | ogni workflow produce artefatti esistenti, e ogni artefatto è prodotto da **esattamente un** workflow | due workflow che producono la stessa cosa sono due verità in conflitto; un artefatto senza workflow è un file che nessuno sa come si fa |
| **INV-18** | ogni fase ha agente esistente, ingresso, uscita, criterio di uscita e modi di fallimento | è la differenza fra un workflow e un promemoria (§1) |
| **INV-19** | l'agente di ogni fase appartiene al reparto del workflow, oppure la fase dichiara `reparto_ospite` | senza, un reparto fa lavorare gli agenti di un altro in silenzio, e nessuno risponde del risultato |

### 7.1 Le prove rosse su questi tre — eseguite il 2026-09-05

Un controllo che non ha mai bloccato niente è decorativo. Questi sono stati provati rompendo il
registro apposta. **Tutti bloccano.**

| Il caso costruito apposta | Chi lo ferma | Cosa dice |
|---|---|---|
| una fase senza criterio di uscita | INV-18 | `WF-MERCATO/ME-1: manca il campo criterio_uscita` |
| una fase con l'agente di un altro reparto, non dichiarato | INV-19 | `WF-STRATEGIA/ST-1: l'agente lan-cpy-conductor non è del reparto LAN-STR e la fase non dichiara reparto_ospite valido` |
| due workflow che producono lo stesso artefatto | INV-17 | `ART-CPY: prodotto da più workflow (WF-STRATEGIA, WF-PAROLA)` |
| un artefatto che nessun workflow produce | INV-17 | `artefatti che nessun workflow produce: ['ART-DBR']` |
| un workflow su un reparto inesistente | INV-17 | `WF-MERCATO: appartiene al reparto LAN-FANTASMA, che non esiste` |

**La deroga di `INV-19` funziona come deve:** `MM-4` è eseguita da un agente della Regia dentro un
workflow della Memoria, dichiara `reparto_ospite: LAN-REG`, e passa. Tolta la dichiarazione, la
stessa fase viene bocciata. La deroga esiste, ma va scritta — che è tutta la differenza.

### 7.2 Cosa fare prima di aggiungere un flusso o una fase

1. Si scrive nel registro, **mai in un documento**: i documenti spiegano, il registro decide.
2. Si esegue il validatore. Se esce diverso da zero, non si costruisce.
3. Se la fase apre un punto umano, si dichiara `punto_umano` con una sigla che esiste in
   `punti_umani`, e `INV-06` verifica che quel punto abbia scadenza o una ragione per non averla.
4. Se la fase è eseguita da un agente di un altro reparto, si dichiara `reparto_ospite`.
5. Si aggiorna **questo documento** perché torni a corrispondere al registro. Se i due divergono,
   **ha torto questo documento**.

---

## Connessioni

- `dati/registro.yaml` — **la fonte di verità**: sezione `workflow`, dieci voci e quarantadue fasi
- `dati/valida_registro.py` — il programma che verifica `INV-17`, `INV-18`, `INV-19`
- [[07-REPARTI-E-GERARCHIA]] — **chi esegue questi flussi**: i reparti, la catena di comando, i passaggi di consegne
- [[03-FLUSSO-OFFERTA]] — `WF-OFFERTA` per intero: la diagnosi, la firma, le dieci riparazioni
- [[01-ARCHITETTURA]] — `lancio avanza`, gli stati, gli errori, la concorrenza
- [[02-PREVISIONE-E-DENARO]] — il costo delle invocazioni che questi flussi consumano
- [[04-COSTRUZIONE]] — in quale ordine questi flussi vengono costruiti, e con quali criteri di sblocco
- [[06-CRITICA-E-GIRI]] — i difetti dei sette flussi della versione 3, uno per uno

