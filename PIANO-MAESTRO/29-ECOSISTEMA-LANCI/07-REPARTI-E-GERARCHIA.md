---
Type: PROJECT
Status: Proposta — versione 4
Tags: #lanci #ecosistema-15 #reparti #gerarchia #organigramma #ADR-023
Created: 2026-09-05
Last updated: 2026-09-05
Versione: 4
---

# 07 — I REPARTI E LA GERARCHIA

> **Regola di lettura:** questo documento spiega. Il registro decide.
> Se una riga qui contraddice `dati/registro.yaml`, ha torto questa riga.

---

## 1. PERCHÉ I REPARTI ERANO SPARITI, E PERCHÉ TORNANO

La versione 3 aveva dodici reparti. Non li ha persi per una scelta di stile: **i revisori li
hanno demoliti tutti per lo stesso motivo, e il motivo è misurato.** Erano nomi.

Nessuno di quei dodici reparti possedeva un file. Nessuno aveva uno schema che dicesse cosa
produce. Nessuno aveva un capo che rispondesse quando un controllo bocciava. Esistevano solo
come voci di un organigramma ricopiato a mano in undici documenti — e il risultato è quello che
si ottiene sempre quando la stessa informazione vive scritta a mano in undici posti: **sei sigle
di reparto comparivano in un dossier e non esistevano nell'altro**, e il documento operativo non
era installabile sopra quello di governo.

La versione 4 ha reagito togliendoli del tutto. È stata la reazione giusta al difetto sbagliato:
i reparti erano vuoti, ma toglierli ha portato via anche **il livello di organizzazione** — chi
possiede cosa, a chi tocca rifare il lavoro quando un gate boccia, chi può attivare chi.

Qui i reparti tornano, ma ancorati. La regola è una sola, e non è una raccomandazione:

> **Un reparto esiste se e solo se possiede un artefatto con uno schema.**
> Lo verifica `INV-13`, a ogni esecuzione del validatore.

### La differenza fra un'etichetta e un proprietario

| | Reparto come **etichetta** (v3) | Reparto come **proprietario** (v4) |
|---|---|---|
| Dove è definito | in prosa, in undici documenti | in `dati/registro.yaml`, sezione `reparti` |
| Cosa possiede | niente | uno o più artefatti, ognuno con schema JSON |
| Come si sa che esiste davvero | qualcuno l'ha scritto | `INV-13`: un reparto operativo senza artefatti fa uscire 1 |
| Se due reparti rivendicano la stessa cosa | nessuno se ne accorge | `INV-13` nomina l'artefatto e i due reparti |
| Chi risponde quando un gate boccia | non dichiarato | il campo `capo`, verificato da `INV-14` |
| Come si fa il suo lavoro | non dichiarato | il campo `workflow`, verificato da `INV-17` |
| Cosa **non** fa | non dichiarato | il campo `confine`, con scritto chi lo fa al posto suo |

**Le due eccezioni sono deliberate, e sono i due reparti di governo.** `LAN-DIR` e `LAN-QLT`
possiedono zero artefatti, e `INV-13` pretende la proprietà solo dai reparti di tipo
`operativo`. Non è una scappatoia: la Direzione non può possedere un artefatto perché sarebbe
parte in causa nei conflitti che deve arbitrare, e la Qualità non può possederne uno perché
`INV-01` le vieta di produrre ciò che giudica.

---

## 2. L'ORGANIGRAMMA

```
  L0   MAX  ·  persona
       │      firma il prezzo · dà il via libera · abbandona un lancio
       │
       │ attiva
       ▼
  L1   LAN-DIR  Direzione ──────── attiva ────────▶   LQ   LAN-QLT  Qualità
       │  capo: lan-direttore                              capo: lan-gate
       │  non produce e non giudica                        giudica TUTTI gli artefatti
       │                                                   niente Write né Edit    (INV-09)
       │ attiva                                            non risponde agli operativi (INV-16)
       │                                                   lo invoca solo `lancio avanza`
       │
  L2   ├── LAN-MER  Mercato      ART-PUB · ART-RIC      WF-MERCATO
       ├── LAN-STR  Strategia    ART-DEC                WF-STRATEGIA
       ├── LAN-PRD  Prodotto     ART-CRT                WF-PRODOTTO
       ├── LAN-OFF  Offerta      ART-PRV · ART-OFF      WF-OFFERTA
       ├── LAN-CPY  Parola       ART-CPY                WF-PAROLA
       ├── LAN-FNL  Vendita      ART-FNL                WF-VENDITA
       ├── LAN-EDT  Editoriale   ART-EDT                WF-EDITORIALE
       ├── LAN-TSR  Tesoro       ART-BDG                WF-TESORO
       ├── LAN-REG  Regia        ART-APE · ART-CNS      WF-REGIA
       └── LAN-MEM  Memoria      ART-DBR                WF-MEMORIA
             │
             │ ogni capo attiva gli agenti del PROPRIO reparto, e solo quelli (INV-19)
             ▼
  L3   gli agenti esecutori — eseguono una fase, restituiscono un risultato tipizzato
```

**La Qualità è disegnata di lato, non sotto.** Non è una convenzione grafica: è la posizione
gerarchica dichiarata nel registro. `LAN-QLT` risponde a `LAN-DIR` e a nessun altro, e nessun
reparto operativo può attivarla. Il §5 dice perché una sola delle due protezioni non basta.

### I dodici reparti in una tabella

| Sigla | Nome | Tipo | Possiede | Capo | Agenti | Workflow |
|---|---|---|---|---|---:|---|
| `LAN-DIR` | Direzione | governo | — | `lan-direttore` | 1 | — |
| `LAN-QLT` | Qualità | governo | — | `lan-gate` | 1 | — |
| `LAN-MER` | Mercato | operativo | `ART-PUB` · `ART-RIC` | `lan-pub-censore` | 2 | `WF-MERCATO` |
| `LAN-STR` | Strategia | operativo | `ART-DEC` | `lan-str-filtro` | 1 | `WF-STRATEGIA` |
| `LAN-PRD` | Prodotto | operativo | `ART-CRT` | `lan-prd-collaudatore` | 1 | `WF-PRODOTTO` |
| `LAN-OFF` | Offerta | operativo | `ART-PRV` · `ART-OFF` | `lan-off-conductor` | 2 | `WF-OFFERTA` |
| `LAN-CPY` | Parola | operativo | `ART-CPY` | `lan-cpy-conductor` | 1 | `WF-PAROLA` |
| `LAN-FNL` | Vendita | operativo | `ART-FNL` | `lan-fnl-costruttore` | 1 | `WF-VENDITA` |
| `LAN-EDT` | Editoriale | operativo | `ART-EDT` | `lan-edt-pianificatore` | 1 | `WF-EDITORIALE` |
| `LAN-TSR` | Tesoro | operativo | `ART-BDG` | `lan-tsr-contabile` | 1 | `WF-TESORO` |
| `LAN-REG` | Regia | operativo | `ART-APE` · `ART-CNS` | `lan-reg-calendarista` | 2 | `WF-REGIA` |
| `LAN-MEM` | Memoria | operativo | `ART-DBR` | `lan-mem-distillatore` | 1 | `WF-MEMORIA` |

Dodici reparti, quindici agenti, tredici artefatti, dieci workflow. Ogni artefatto ha un
proprietario e uno solo; ogni agente ha un reparto e uno solo; ogni reparto operativo ha un
workflow. Non è una descrizione: sono quattro affermazioni che `INV-13`, `INV-14` e `INV-17`
ricalcolano ogni volta che il validatore gira.

> **Una divergenza trovata scrivendo questo documento, e lasciata scritta.** La lista `reparti`
> del registro contiene **dieci** reparti operativi. Il campo `chi` del livello `L2`, dentro la
> sezione `gerarchia`, dice «i capi dei **nove** reparti operativi». I due punti dicono la stessa
> cosa e sono divergenti, e nessun invariante li confronta: `INV-14` verifica che ogni reparto
> abbia un capo, non quanti reparti ci siano. È la stessa famiglia di difetto per cui è nato
> `INV-22` — due punti che dicono la stessa cosa e possono divergere in silenzio — e si chiude
> allo stesso modo, con un controllo, non con una correzione a mano. Il conteggio giusto è
> **dieci**: si ottiene contando la lista, che è il dato; il campo `chi` è una didascalia.

---

## 3. I DODICI REPARTI, UNO PER UNO

Prima i due di governo, poi i dieci operativi nell'ordine in cui la catena li attraversa.

### 3.1 `LAN-DIR` — Direzione · governo

**Missione** — porta un lancio da `IDEA` ad `APPRESO` e risponde a Max di cosa è successo.

- **Possiede** — niente, di proposito.
- **Agenti** — `lan-direttore` (doombot, `claude-opus-5`): orchestra il lancio, unico
  interlocutore umano mentre corre.
- **Capo** — `lan-direttore`.
- **Workflow** — nessuno. La Direzione non esegue un flusso: decide quale far partire.
- **Il confine** — non produce nessun artefatto e non giudica nessun artefatto. Se lo facesse
  sarebbe parte in causa nei conflitti che deve arbitrare. Produrre è dei dieci reparti
  operativi, giudicare è di `LAN-QLT`.

### 3.2 `LAN-QLT` — Qualità · governo

**Missione** — esegue tutti i controlli e scrive i verbali, anche quando lasciano passare.

- **Possiede** — niente, e non per omissione: `INV-01` vieta che il giudice di un artefatto ne
  sia il produttore, e `lan-gate` giudica tutti e tredici gli artefatti.
- **Agenti** — `lan-gate` (sentinella, `claude-sonnet-5`): esegue tutti e quattordici i gate.
- **Capo** — `lan-gate`.
- **Workflow** — nessuno. I gate non sono un flusso: sono ciò che ferma i flussi.
- **Il confine** — non produce artefatti (`INV-01`), non ha permesso di scrittura (`INV-09`), non
  risponde a nessun reparto operativo (`INV-16`). I verbali li scrive lo script, non l'agente.

### 3.3 `LAN-MER` — Mercato · operativo

**Missione** — sa quante persone possiamo mettere davanti all'offerta e con quali parole parlano.

- **Possiede** — `ART-PUB` (`pubblico.json`), che afferma *«quante persone possiamo mettere
  davanti all'offerta il giorno dell'apertura, per canale, con la prova di ognuna»*; e `ART-RIC`
  (`ricerca.json`), che afferma *«le parole vere del pubblico e i buchi veri dei concorrenti,
  ognuna con la fonte»*.
- **Agenti** — `lan-pub-censore` (sentinella, `claude-sonnet-5`), `lan-int-analista` (sentinella,
  `claude-sonnet-5`, l'unico con `WebFetch` fra gli strumenti).
- **Capo** — `lan-pub-censore`.
- **Workflow** — `WF-MERCATO`, 5 fasi, 3-6 ore, gate finali `GATE-PUB-1` e `GATE-INT-1`.
- **Il confine** — non costruisce pubblico e non fa campagne: conta ciò che c'è e porta la prova
  di ogni numero. Costruire pubblico è lavoro di `04-MARKETING`.
- **Perché i due artefatti stanno insieme** — pubblico e ricerca rispondono alla stessa domanda,
  chi c'è là fuori e cosa dice, e attingono alle stesse fonti. Separarli avrebbe prodotto due
  reparti da un agente ciascuno, cioè due titoli.

### 3.4 `LAN-STR` — Strategia · operativo

**Missione** — decide se questo lancio si fa adesso, e non un altro.

- **Possiede** — `ART-DEC` (`decisione.json`): *«questo lancio si fa adesso, e non un altro»*.
- **Agenti** — `lan-str-filtro` (scagnozzo, `claude-haiku-4-5-20251001`).
- **Capo** — `lan-str-filtro`.
- **Workflow** — `WF-STRATEGIA`, 2 fasi, 1-2 ore, gate finale `GATE-STR-1`.
- **Il confine** — non sceglie il prezzo e non sceglie la data: sono dell'Offerta. Qui si decide
  solo se vale la pena istruire il lancio.

### 3.5 `LAN-PRD` — Prodotto · operativo

**Missione** — certifica che il prodotto è consegnabile a un cliente pagante senza vergogna e
senza rischio.

- **Possiede** — `ART-CRT` (`certificato.json`): *«il prodotto è consegnabile a un cliente
  pagante senza vergogna e senza rischio»*.
- **Agenti** — `lan-prd-collaudatore` (sentinella, `claude-sonnet-5`).
- **Capo** — `lan-prd-collaudatore`.
- **Workflow** — `WF-PRODOTTO`, 4 fasi, 2-4 ore in modalità integrale e 1-2 in retroattiva, gate
  finale `GATE-PRD-1`.
- **Il confine** — non crea il prodotto: è di `02-INFO-BUSINESS`. Qui si collauda ciò che arriva
  già fatto, anche in modalità retroattiva — il percorso costruito per il Manuale, pronto dal
  07/03/2026 e mai passato da un flusso di produzione.

### 3.6 `LAN-OFF` — Offerta · operativo

**Missione** — istruisce prezzo e data fino a renderli una conferma di dieci secondi.

- **Possiede** — `ART-PRV` (`previsione.json`): *«quanto ci aspettiamo di incassare, con la banda
  e le assunzioni dichiarate»*; e `ART-OFF` (`offerta.json`): *«il prezzo, la data e la struttura
  dell'offerta, firmati da una persona»*.
- **Agenti** — `lan-off-conductor` (doombot, `claude-opus-5`, con il vincolo dichiarato *non può
  scrivere il sotto-oggetto firma*), `lan-prv-modello` (scagnozzo, `claude-haiku-4-5-20251001`).
- **Capo** — `lan-off-conductor`.
- **Workflow** — `WF-OFFERTA`, 6 fasi, 3-5 ore più il tempo della firma, gate finali `GATE-PRV-1`
  e `GATE-OFF-1`. È il flusso per cui l'intero ecosistema esiste.
- **Il confine** — non firma. La firma è di una persona, per canale ammesso, e nessun agente di
  questo reparto ha permesso di scrittura sul campo `firma`.
- **Perché i due artefatti stanno insieme** — la previsione esiste per rendere la firma del
  prezzo una decisione invece che una scelta di gusto: sono due metà dello stesso atto. Tenerle
  in due reparti avrebbe rifatto il difetto della versione precedente, dove il prezzo si
  sceglieva senza sapere quanto produceva.
- **Perché `lan-prv-modello` è al grado più basso** — qui non c'è niente da interpretare, c'è una
  formula da applicare. Un modello linguistico che ragiona su un calcolo deterministico è un modo
  caro di sbagliare.

### 3.7 `LAN-CPY` — Parola · operativo

**Missione** — tutti i testi del lancio, ognuno col punteggio calcolato e la destinazione.

- **Possiede** — `ART-CPY` (`copy/manifest.json`): *«tutti i testi del lancio, ognuno col suo
  punteggio calcolato e la sua destinazione»*.
- **Agenti** — `lan-cpy-conductor` (doombot, `claude-opus-5`).
- **Capo** — `lan-cpy-conductor`.
- **Workflow** — `WF-PAROLA`, 5 fasi, 8-14 ore, gate finale `GATE-CPY-1`.
- **Il confine** — non possiede lo standard dei testi né la voce del marchio: sono di
  `04-MARKETING` e si ricevono come vincolo, non si ridiscutono qui.

### 3.8 `LAN-FNL` — Vendita · operativo

**Missione** — le pagine sono online, misurano, e la cassa ha incassato un pagamento vero.

- **Possiede** — `ART-FNL` (`funnel.json`): *«le pagine sono online, misurano, e la cassa ha
  incassato un pagamento di prova vero»*.
- **Agenti** — `lan-fnl-costruttore` (sentinella, `claude-sonnet-5`).
- **Capo** — `lan-fnl-costruttore`.
- **Workflow** — `WF-VENDITA`, 4 fasi, 6-12 ore, gate finale `GATE-FNL-1`.
- **Il confine** — non decide cosa dicono le pagine (è della Parola) e non porta traffico (è
  dell'Editoriale e di `04-MARKETING`). Qui si costruisce e si prova che incassa.

### 3.9 `LAN-EDT` — Editoriale · operativo

**Missione** — riempie i giorni del lancio di contenuti che escono davvero e portano da qualche
parte.

- **Possiede** — `ART-EDT` (`editoriale.json`): *«i contenuti dei giorni del lancio, ognuno con
  la data di uscita e dove porta»*.
- **Agenti** — `lan-edt-pianificatore` (sentinella, `claude-sonnet-5`).
- **Capo** — `lan-edt-pianificatore`.
- **Workflow** — `WF-EDITORIALE`, 3 fasi, 4-8 ore, gate finale `GATE-EDT-1`.
- **Il confine** — non spedisce niente da solo: ogni invio reale alla lista è un punto umano
  (`PU-INVIO`), perché un'email spedita non si richiama.

### 3.10 `LAN-TSR` — Tesoro · operativo

**Missione** — sa quanto costa il lancio, quanto costa farlo girare, e a quante copie va in pari.

- **Possiede** — `ART-BDG` (`budget.json`): *«quanto costa questo lancio, quanto costa farlo
  girare, e a quante copie va in pari»*.
- **Agenti** — `lan-tsr-contabile` (scagnozzo, `claude-haiku-4-5-20251001`).
- **Capo** — `lan-tsr-contabile`.
- **Workflow** — `WF-TESORO`, 4 fasi, 2-4 ore, gate finali `GATE-TSR-1` e `GATE-TSR-2` — il
  secondo è di tipo continuo e sorveglia lo scarto mentre il lancio corre.
- **Il confine** — non è la Tesoreria dell'azienda (ecosistema 14): qui si governa il costo di
  **un** lancio. Se un numero compare in tutti e due i posti ed è diverso, ha ragione la
  Tesoreria.

### 3.11 `LAN-REG` — Regia · operativo

**Missione** — porta il lancio all'apertura con tutte le condizioni vere insieme, e ne misura il
risultato.

- **Possiede** — `ART-APE` (`apertura.json`): *«tutte le condizioni di apertura sono vere
  insieme, e una persona ha dato il via»*; e `ART-CNS` (`consuntivo.json`): *«quanto è entrato
  davvero, da dove, e quanto è costato davvero»*.
- **Agenti** — `lan-reg-calendarista` (sentinella, `claude-sonnet-5`), `lan-reg-tracciatore`
  (scagnozzo, `claude-haiku-4-5-20251001`).
- **Capo** — `lan-reg-calendarista`.
- **Workflow** — `WF-REGIA`, 5 fasi, 3-5 ore più i giorni del carrello, gate finali `GATE-REG-1`
  e `GATE-CNS-1`.
- **Il confine** — non apre la vendita: il via libera è di una persona e non avrà mai un default,
  perché è irreversibile verso l'esterno.
- **Perché i due artefatti stanno insieme** — chi porta all'apertura e chi misura cosa è successo
  devono essere lo stesso organo, altrimenti il consuntivo lo scrive qualcuno che non sa cosa era
  stato promesso il giorno dell'apertura.

### 3.12 `LAN-MEM` — Memoria · operativo

**Missione** — trasforma un lancio finito in vantaggio per il prossimo.

- **Possiede** — `ART-DBR` (`debrief.json`): *«previsione contro realtà, ogni scarto con la sua
  causa, e cosa il prossimo lancio deve fare di diverso»*.
- **Agenti** — `lan-mem-distillatore` (sentinella, `claude-sonnet-5`).
- **Capo** — `lan-mem-distillatore`.
- **Workflow** — `WF-MEMORIA`, 4 fasi, 2-4 ore, gate finale `GATE-MEM-1`. L'ultima fase, `MM-4`,
  è eseguita da `lan-reg-calendarista` e per questo dichiara `reparto_ospite: LAN-REG`: senza
  quella dichiarazione `INV-19` boccerebbe il workflow.
- **Il confine** — non giudica le persone e non riscrive la storia: confronta previsione e
  realtà, scrive le cause degli scarti, e la Regia controfirma. Se i due non sono d'accordo,
  l'obiezione resta scritta accanto.
- **Perché la controfirma è un campo e non un ruolo** — `lan-reg-calendarista` ha permesso di
  scrittura, e un giudice che può riscrivere ciò che giudica non è un giudice (`INV-09`). Il
  primo giro del validatore ha bocciato proprio questa riga, scritta un'ora prima.

---

## 4. LA CATENA DI COMANDO

Cinque livelli. La regola che li tiene insieme è una sola, ed è scritta nel registro:
**un livello può attivare solo il livello sotto.**

| Livello | Chi | Cosa decide | Può attivare |
|---|---|---|---|
| **L0** | **Max** | tutto ciò che è irreversibile verso l'esterno — apertura della vendita, invii reali, spese oltre il tetto — più il prezzo e l'abbandono di un lancio | `L1` |
| **L1** | `LAN-DIR` | l'ordine del lavoro, quale reparto attivare, quando fermarsi | `L2`, `LQ` |
| **L2** | i capi dei nove reparti operativi | come il proprio reparto produce il proprio artefatto | `L3` |
| **L3** | gli agenti esecutori | niente: eseguono una fase e restituiscono un risultato tipizzato | — |
| **LQ** | `LAN-QLT` | se un artefatto passa o blocca | — |

**`L0` è l'unico livello non delegabile.** Gli altri quattro sono ruoli che una macchina esegue;
il primo è una persona, e le tre cose che decide non hanno e non avranno mai un valore
predefinito.

### 4.1 Le quattro regole, e perché esistono

| Regola | Perché |
|---|---|
| **Un livello attiva solo il livello sotto** | senza, si perdono insieme la spesa e la responsabilità. È una regola economica prima che organizzativa: vedi 4.2 |
| **Nessun reparto attiva il giudice per farsi approvare** | il giudice lo invoca `lancio avanza`, mai un reparto. Se lo invocasse il reparto, **sceglierebbe quando farsi giudicare** — cioè quando è pronto a passare |
| **Un capo reparto non attiva agenti di un altro reparto** | è `INV-19`: le responsabilità evaporano quando il lavoro attraversa i confini in silenzio. Il lavoro risulta fatto, ma nessuno ne risponde |
| **Solo `L0` autorizza ciò che è irreversibile verso l'esterno** | un'email spedita non si richiama, una vendita aperta non si chiude in silenzio |

### 4.2 La ragione economica, che è la meno ovvia e la più stringente

Da ADR-014, misurato: **ogni invocazione di un agente costa 0,08-0,11 dollari di sola tassa**,
qualunque sia il contenuto della richiesta. Il tetto per lancio è **15 dollari**.

Una catena in cui chiunque può attivare chiunque non è soltanto disordinata: **è un moltiplicatore
di costo senza freno.** Con quindici agenti che possono chiamarsi liberamente, il numero di
invocazioni non ha un massimo prevedibile, e il tetto si esaurisce senza che nessuno sappia chi
ha chiamato cosa.

Con la catena a livelli, invece, il conto si fa: il documento `02-PREVISIONE-E-DENARO.md` §4.2
stima **48-79 invocazioni per lancio**, cioè 3,84-8,69 dollari di sola tassa. È una stima
possibile solo perché la catena è chiusa.

> **La conseguenza pratica per chi costruisce:** quando un agente ha bisogno di qualcosa che sta
> in un altro reparto, **non chiama quell'agente**. Dichiara l'ingresso mancante, la fase si
> ferma, e `LAN-DIR` attiva il reparto giusto. Costa un giro in più e rende visibile la
> dipendenza, invece di nasconderla dentro una chiamata.

---

## 5. IL GIUDICE STA FUORI — E GLI SI TOGLIE TUTTO

`LAN-QLT` è disegnato di lato nell'organigramma, e non è una scelta grafica.

**Due protezioni, e servono entrambe:**

| Protezione | Invariante | Cosa gli toglie |
|---|---|---|
| non ha `Write` né `Edit` fra i propri strumenti | **INV-09** | **la penna** |
| non risponde a nessun reparto operativo: risponde solo alla Direzione | **INV-16** | **il padrone** |

**Perché una sola delle due non basta**, ed è il punto che vale la pena capire:

- Togliergli la penna ma lasciarlo sotto un capo reparto significa che **il capo può premere**.
  Il giudice non può riscrivere l'artefatto, ma può essere convinto a lasciarlo passare da chi
  ha interesse a farlo passare.
- Togliergli il padrone ma lasciargli la penna significa che **può riparare ciò che dovrebbe
  bocciare**. Nessuno gli ordina niente, ma il difetto sparisce comunque — e nessuno lo saprà
  mai, perché il verbale lo scrive lui.

Togliergliene una sola lascia intatto il modo di aggirarlo. Per questo il registro le dichiara
insieme, e il validatore le verifica insieme.

**E la terza, che non è un invariante ma una regola di invocazione:** il giudice lo chiama
`lancio avanza`, mai un reparto. Un reparto che potesse invocare il proprio giudice sceglierebbe
il momento — e il momento scelto è sempre quello in cui si passa.

> **I verbali li scrive lo script, non l'agente.** Così anche volendo, il giudice non può
> riscrivere ciò che ha giudicato: la sua unica uscita è un verdetto, e il verdetto lo trascrive
> il programma.

### L'unica eccezione, ed è un campo non un ruolo

Il debrief (`ART-DBR`) è giudicato da `lan-gate` come tutti gli altri artefatti, ma porta una
**controfirma** di `lan-reg-calendarista`, cioè della Regia che ha eseguito il lancio.

La Memoria giudica il lancio, la Regia controfirma, e se non è d'accordo **l'obiezione resta
scritta accanto** invece di essere negoziata via. Nessuno dei due scrive da solo la storia di
com'è andata.

La controfirma è un **campo dell'artefatto**, non il ruolo di giudice: `lan-reg-calendarista` ha
permesso di scrittura, e dargli il ruolo di giudice avrebbe violato `INV-09`. Il primo giro del
validatore ha bocciato esattamente questa riga, scritta un'ora prima — è la prova che
l'invariante serve a chi lo scrive, non solo a chi lo legge.

---

## 6. I PASSAGGI DI CONSEGNE

Un passaggio senza criterio di accettazione è una speranza: chi riceve scopre che manca qualcosa
quando è già al lavoro, e torna indietro. `INV-20` verifica che ognuno citi due reparti
esistenti, un artefatto esistente, un criterio di accettazione e cosa succede se il passaggio è
rifiutato.

### 6.1 I tredici passaggi interni

| Da | A | Passa | Accettato quando | Se rifiutato |
|---|---|---|---|---|
| `LAN-MER` | `LAN-STR` | `ART-PUB` | il totale verificato è un numero, e ogni canale che contribuisce ha una prova non più vecchia di 30 giorni | torna a `LAN-MER`, il lancio resta in `IDEA` |
| `LAN-MER` | `LAN-OFF` | `ART-RIC` | almeno 15 frasi con fonte apribile, e il campione riaperto dal gate risulta raggiungibile | torna a `LAN-MER`, le frasi con fonte valida si conservano |
| `LAN-STR` | `LAN-PRD` | `ART-DEC` | cinque risposte, nessuna negativa, ognuna con l'artefatto che la sostiene | `ARCHIVIATO` con la ragione, riproponibile con un elemento nuovo |
| `LAN-PRD` | `LAN-OFF` | `ART-CRT` | nessuna bandiera rossa presente, link testati dal gate, e in modalità retroattiva il debito di collaudo dichiarato | torna a `LAN-PRD`, il lancio torna a `VALUTATO` con l'elenco di cosa manca |
| `LAN-OFF` | `LAN-CPY` | `ART-OFF` | prezzo e data esistono, la firma ha canale ammesso e l'impronta corrisponde alla proposta corrente | torna a `LAN-OFF`, la proposta si conserva e la fase `O5` si riapre |
| `LAN-OFF` | `LAN-TSR` | `ART-PRV` | i tre scenari esistono e ogni assunzione dichiara stato `misurato` oppure `assunto` | torna a `LAN-OFF`, la previsione si conserva marcata non valida |
| `LAN-CPY` | `LAN-FNL` | `ART-CPY` | punteggio totale almeno 80, nessun blocco sotto metà dei propri punti, ogni prova risolvibile | torna a `LAN-CPY`, si rifanno solo i blocchi bocciati |
| `LAN-CPY` | `LAN-EDT` | `ART-CPY` | ogni pezzo destinato a un contenuto editoriale esiste come file non vuoto | torna a `LAN-CPY` con l'elenco dei pezzi mancanti |
| `LAN-FNL` | `LAN-REG` | `ART-FNL` | ogni pagina risponde, l'evento è arrivato dalla piattaforma, e la prova di cassa è incassata e rimborsata | torna a `LAN-FNL`, le pagine conformi restano |
| `LAN-EDT` | `LAN-REG` | `ART-EDT` | nessuna riga incompleta, ogni contenuto punta a una pagina esistente, ogni giorno del carrello ha un contenuto | torna a `LAN-EDT` con le righe incomplete evidenziate |
| `LAN-TSR` | `LAN-REG` | `ART-BDG` | costo totale sotto il tetto, pareggio calcolato dalla previsione, costo macchina presente | torna a `LAN-TSR`, il budget si conserva marcato oltre tetto |
| `LAN-REG` | `LAN-MEM` | `ART-CNS` | il ricavo ha origine verificabile e il periodo copre tutte le date del carrello | torna a `LAN-REG`, il lancio resta `APERTO` |
| `LAN-MEM` | `LAN-DIR` | `ART-DBR` | ogni scarto oltre il dieci per cento ha una causa, almeno tre schemi con `si_applica_quando`, e la controfirma della Regia | torna a `LAN-MEM`, il lancio resta `CHIUSO` e non diventa `APPRESO` |

**Si legge una cosa, guardando la colonna di destra: nessun rifiuto cancella il lavoro fatto.**
Ogni riga dice dove si torna e cosa si conserva. È la riparazione del difetto per cui, nella
versione 3, nessun controllo diceva cosa succede quando boccia.

### 6.2 I due passaggi verso l'esterno

| Da | A | Passa | Accettato quando |
|---|---|---|---|
| **ULTIMO METRO** | `LAN-STR` | l'elenco di ciò che è pronto e non è uscito | il prodotto esiste come file ed è dichiarato pubblicabile |
| `LAN-REG` | **TESORERIA** | ricavi e costi reali | ogni numero ha un'origine leggibile in un pannello |

Il primo è **la coda in ingresso di questo ecosistema**: ADR-016 ha misurato 25 pezzi finiti mai
usciti, e quella è la fila da cui i lanci nascono.

Il secondo ha una regola sua, e va detta esplicitamente: **ogni euro nasce qui e sale in
Tesoreria, non scende mai.** Se un numero compare in tutti e due i posti ed è diverso, **ha
ragione la Tesoreria**, e la divergenza è un difetto da registrare.

---

## 7. I COMANDI E CHI PUÒ INVOCARLI

`INV-21` verifica che ogni comando dichiari da quale livello può essere invocato, e che quel
livello esista. Un comando che chiunque può invocare è un comando senza responsabile.

| Comando | Cosa fa | Chi |
|---|---|---|
| `lancio crea <id> --prodotto <nome>` | crea la cartella del lancio con `stato.json` in `IDEA` | `L0` `L1` |
| `lancio avanza <id>` | fa avanzare il lancio finché un controllo non lo ferma | `L0` `L1` |
| `lancio avanza <id> --solo-gate <GATE>` | riesegue un solo controllo dopo una correzione | `L0` `L1` `L2` |
| `lancio avanza <id> --a-vuoto` | calcola e stampa senza scrivere niente | `L0` `L1` `L2` |
| `lancio elenco` | una riga per lancio, con da quanti giorni è fermo e su cosa | `L0` `L1` `L2` |
| **`lancio blocchi`** | **tutti i punti umani aperti, ordinati per giorni di attesa** | `L0` `L1` `L2` |
| `lancio costi <id>` | quanto è costato finora, letto dal registro delle chiamate | `L0` `L1` `L2` |
| `lancio sospendi <id> --motivo <testo> --revisione <data>` | porta il lancio in `SOSPESO` e congela gli orologi | `L0` `L1` |
| `lancio riprendi <id>` | riporta il lancio allo stato di partenza con un verbale | `L0` `L1` |
| **`lancio firma <id> --prezzo <n> --data <gg/mm/aaaa>`** | registra la firma umana sul prezzo | **solo `L0`** |
| **`lancio via-libera <id>`** | autorizza l'apertura della vendita | **solo `L0`** |
| **`lancio abbandona <id> --motivo <testo>`** | porta il lancio in `ABORTITO`, conservando ciò che si salva | **solo `L0`** |

### 7.1 I tre comandi che solo Max può invocare

| Comando | Perché nessun altro |
|---|---|
| `lancio firma` | nessun agente ha permesso di scrittura sul campo `firma`, il canale è in lista chiusa e l'impronta lega la firma al testo esatto. Nella versione 3 `firmato_da` era una stringa: **un agente in ciclo di riparazione poteva scrivere «Max» per sbloccarsi**, e un lancio sarebbe partito a un prezzo mai approvato |
| `lancio via-libera` | aprire una vendita è irreversibile verso l'esterno. `PU-APERTURA` non ha scadenza e non avrà mai un valore predefinito |
| `lancio abbandona` | chiudere un lancio è una decisione che costa tutto il lavoro fatto. A 90 giorni di sospensione il sistema **propone** l'abbandono, non lo esegue |

### 7.2 `lancio blocchi`, e perché il registro lo chiama il più importante

Stampa tutti i punti umani aperti dell'azienda, ordinati per giorni di attesa.

Nella versione 3 non esisteva, e la conseguenza è misurabile: **il prodotto pilota di questa
azienda è fermo dal 07/03/2026** su una decisione che nessuno vedeva scritta da nessuna parte.
Non c'era un posto dove guardare per sapere che qualcosa aspettava.

> Rende visibile il problema vero di Digital Empire: **non i lanci che vanno male, ma quelli che
> non partono perché una decisione aspetta.**

---

## 8. COSA IMPEDISCE CHE I REPARTI TORNINO A ESSERE ETICHETTE

Dieci invarianti nuovi, tutti eseguiti da un programma.

```bash
cd PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati
PYTHONIOENCODING=utf-8 python valida_registro.py
# 832 controlli eseguiti → PIANO COERENTE  (uscita 0)
```

| Invariante | Verifica che… |
|---|---|
| **INV-13** | ogni artefatto appartiene a un solo reparto, e ogni reparto operativo ne possiede almeno uno |
| **INV-14** | ogni agente appartiene a un reparto, e ogni reparto ha un capo che è un suo agente |
| **INV-15** | la catena di comando non ha cicli |
| **INV-16** | il reparto che giudica non risponde a nessun reparto operativo |
| **INV-17** | ogni workflow produce artefatti esistenti, e ogni artefatto è prodotto da esattamente un workflow |
| **INV-18** | ogni fase ha agente, ingresso, uscita, criterio di uscita e modi di fallimento |
| **INV-19** | l'agente di ogni fase appartiene al reparto del workflow, o la fase dichiara `reparto_ospite` |
| **INV-20** | ogni passaggio cita due reparti, un artefatto e un criterio di accettazione |
| **INV-21** | ogni comando dichiara da quale livello si invoca, e quel livello esiste |
| **INV-22** | il campo `produce` di ogni agente coincide con gli artefatti di cui è davvero produttore |

### 8.1 Le prove rosse — eseguite il 2026-09-05

Un controllo che non ha mai bloccato niente è decorativo. Questi sono stati messi alla prova
rompendo il registro apposta, un difetto per volta. **Tutti bloccano.**

| Il caso costruito apposta | Chi lo ferma | Cosa dice |
|---|---|---|
| un artefatto posseduto da due reparti | INV-13 | `ART-CRT: posseduto da più reparti (LAN-STR, LAN-PRD)` |
| un capo che non appartiene al proprio reparto | INV-14 | `LAN-CPY: il capo lan-gate non è fra gli agenti del reparto` |
| un ciclo nella catena di comando | INV-15 | `ciclo di comando: LAN-DIR -> LAN-MEM -> LAN-DIR` |
| il giudice che risponde a un reparto operativo | INV-16 | `LAN-QLT giudica gli artefatti ma risponde a LAN-OFF` |
| due workflow che producono lo stesso artefatto | INV-17 | `ART-CPY: prodotto da più workflow (WF-STRATEGIA, WF-PAROLA)` |
| un artefatto che nessun workflow produce | INV-17 | `artefatti che nessun workflow produce: ['ART-DBR']` |
| un workflow su un reparto inesistente | INV-17 | `WF-MERCATO: appartiene al reparto LAN-FANTASMA, che non esiste` |
| una fase senza criterio di uscita | INV-18 | `WF-MERCATO/ME-1: manca il campo criterio_uscita` |
| una fase con l'agente di un altro reparto, non dichiarato | INV-19 | `WF-STRATEGIA/ST-1: l'agente lan-cpy-conductor non è del reparto LAN-STR` |
| un passaggio senza criterio di accettazione | INV-20 | `passaggio LAN-MER -> LAN-STR: nessun criterio di accettazione` |
| il campo `produce` di un agente che diverge dal vero | INV-22 | `lan-str-filtro: dichiara di produrre ['ART-CPY', 'ART-DEC'] ma è produttore di ['ART-DEC']` |

### 8.2 INV-22 è nato da una prova sbagliata

Vale la pena raccontarlo, perché è la ragione per cui le prove rosse si fanno davvero invece di
dichiararle.

Una delle prove doveva alterare il campo `produce` di un **workflow**. Era costruita con una
sostituzione di testo, e la sostituzione ha colpito il campo `produce` di un **agente** — che si
chiama allo stesso modo e compare prima nel file. Risultato: il validatore **non ha bloccato**, e
sembrava un difetto del controllo.

Non lo era. Il controllo sui workflow funzionava; mancava del tutto il controllo sugli agenti.
**Il campo `produce` di un agente poteva dire una cosa e il campo `produttore` dell'artefatto
un'altra, senza che nulla se ne accorgesse** — cioè esattamente la famiglia di difetto per cui
questo registro esiste: due punti che dicono la stessa cosa e possono divergere in silenzio.

Da lì è nato `INV-22`. **L'errore della prova ha trovato un buco vero.**

---

## Connessioni

- `dati/registro.yaml` — **la fonte di verità**: sezioni `reparti`, `gerarchia`, `passaggi`, `comandi`
- `dati/valida_registro.py` — il programma che verifica gli invarianti di questo documento
- [[00-LEGGIMI]] — il problema, la tesi, il primo giorno
- [[01-ARCHITETTURA]] — la macchina: la catena degli artefatti, `avanza`, il ponte verso gli agenti
- [[08-WORKFLOW]] — **come lavorano i reparti descritti qui**, fase per fase
- [[02-PREVISIONE-E-DENARO]] — il costo per invocazione, che è la ragione economica della catena di comando
- [[06-CRITICA-E-GIRI]] — i difetti della versione 3, uno per uno
- `company/Memory/decisions/ADR-014-il-codice-torna-a-chiamare-un-modello.md` — la tassa per invocazione
- `company/Memory/decisions/ADR-016-ultimo-metro.md` — la coda in ingresso di questo ecosistema
