# WF-OFF — IL WORKFLOW DELL'OFFERTA
## Il reparto che esiste per sciogliere un blocco vecchio di sei mesi

> **Riscritto dopo la critica.** Nella prima versione questo reparto *chiedeva* un prezzo e
> bloccava finché non arrivava. Era sbagliato, e la ragione è tutta qui sotto.

---

## 0. L'errore della prima versione, e perché va detto per primo

La prima versione diceva: *il gate del prezzo blocca finché prezzo e data non sono valori veri,
ed è il gate che avrebbe impedito al Manuale Claude Code di restare fermo sei mesi.*

**È falso, e in modo pericoloso.**

Il Manuale non è fermo perché mancasse un controllo. È fermo perché **una persona non ha preso
una decisione**. Un gate che blocca su una decisione mancante non produce la decisione: produce
un blocco documentato. Trasforma *"il prodotto è fermo e non si sa perché"* in *"il prodotto è
fermo e sappiamo che manca il prezzo"* — che è un miglioramento vero, ma non è la soluzione.

E c'è di peggio: **un gate che blocca su una decisione che nessuno prende è un gate che verrà
derogato**, e un gate derogato la prima volta smette di esistere.

### Il principio che ne discende, e vale per tutto l'ecosistema

> **Un gate posto su una decisione umana deve arrivare con la decisione già istruita.**
> «Decidi» delega la fatica. «Confermi questo?» toglie fatica.
> **Fra le due domande ci sono sei mesi.**

---

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-OFF` |
| **Nome** | Workflow Offerta e Prezzo |
| **Missione** | **Istruisce** la decisione su prezzo, data e struttura dell'offerta fino a renderla una conferma di dieci secondi, e la porta a chi la firma |
| **Proprietario** | Reparto `LAN-OFF` — **nuovo**: questa capacità non esiste da nessuna parte nell'Impero |
| **Durata** | 3-5 ore di lavoro della macchina + **il tempo di una firma** |

**Perché è nuovo e non avvolge niente.** Verificato: nell'Impero esistono skill che parlano di
prezzi come materia, ma **nessun organo che decida il prezzo di un prodotto e se ne assuma la
responsabilità**. È il pezzo mancante, e non è un caso che sia proprio quello dove l'azienda è
bloccata.

---

## 2. Trigger

| Tipo | Dettaglio |
|---|---|
| **Comando** | `/lancio-offerta <lancio_id>` |
| **Handoff in ingresso** | il certificato del prodotto (basta l'architettura approvata per cominciare) + la ricerca di mercato |
| **Automatico** | quando un lancio entra in stato `ISTRUITO`, questo workflow **si propone da solo**: è il collo di bottiglia noto, e non aspetta di essere chiamato |

**L'ultima riga è deliberata.** Il reparto che presidia il blocco storico dell'azienda non può
essere un reparto che aspetta di essere invocato.

---

## 3. Input tipizzato

```json
{
  "lancio_id": "string",
  "certificato_path": "string",
  "architettura_path": "string",
  "ricerca_path": "string",
  "catalogo_attuale": [
    { "prodotto": "string", "prezzo": "number", "livello": "0-4", "venduto_copie": "number | null" }
  ],
  "ruolo_prodotto": "vendita | acquisizione-contatti | non-deciso",
  "vincoli": {
    "prezzo_minimo": "number | null",
    "prezzo_massimo": "number | null",
    "data_non_prima_di": "string ISO | null",
    "data_non_dopo": "string ISO | null"
  }
}
```

| Campo | Se manca |
|---|---|
| `certificato_path` | esce 2: non si prezza un prodotto non certificato |
| `ricerca_path` | **si procede lo stesso**, ma la proposta esce marcata *"senza mercato davanti"* — meglio una proposta dichiaratamente cieca che nessuna proposta |
| `catalogo_attuale` | si procede, e la regola dei passaggi **non può essere verificata**: lo si scrive |
| `ruolo_prodotto` | **è il campo che blocca tutto**, vedi §5 |

---

## 4. Le fasi

| # | Fase | Cosa fa | Agente | Output | Durata | Umano |
|---|---|---|---|---|---|---|
| **O0** | Consulta la memoria | Guarda i prezzi già decisi e **quelli scartati con la ragione** | `lan-off-conductor` | `offerta/00-precedenti.json` | 15 min | no |
| **O1** | Sciogli il ruolo | Se il prodotto ha due ruoli contraddittori, **istruisce la scelta** (§5) | `lan-off-conductor` | `offerta/01-ruolo.md` | 30 min | **Sì, se non deciso** |
| **O2** | Colloca nel listino | Determina il livello, e verifica la regola dei passaggi | `lan-off-prezzo` | `offerta/02-livello.json` | 20 min | no |
| **O3** | Guarda il mercato | Estrae i prezzi dei concorrenti dalla ricerca | `lan-off-prezzo` | `offerta/03-mercato.json` | 30 min | no |
| **O4** | **Istruisci la decisione** | Prepara **una proposta e due alternative**, ognuna con la conseguenza (§6) | `lan-off-prezzo` | `offerta/04-proposta.md` | 1 h | no |
| **O5** | La conferma | Presenta la proposta come **domanda binaria** e raccoglie la firma | `lan-off-conductor` | `offerta/05-firma.json` | 10 min | **Sì — è la firma** |
| **O6** | La data | Propone la data dal calendario, verificando che non collida con altri impegni | `lan-off-conductor` | dentro `offerta.json` | 20 min | **Sì — stessa firma** |
| **O7** | La struttura | Costruisce il pacchetto: valore, ancoraggio, bonus, garanzia, motivo per agire adesso | `lan-off-struttura` | `offerta/07-struttura.json` | 1,5 h | no |
| **GATE-OFF-1** | Il controllo | prezzo e data veri, struttura completa, rapporto valore/prezzo ≥3 | `lan-qlt-gate` | verbale | 10 min | — |
| **O8** | Emissione | Scrive `offerta.json` e fa passare il lancio a `DATATO` | `lan-off-conductor` | `offerta.json` | 10 min | no |

**Tre ore e mezza di macchina. Dieci minuti di persona.** È l'unico rapporto che scioglie un
blocco di sei mesi.

---

## 5. Il nodo del doppio ruolo — istruito, non nominato

La prima versione diceva quattro volte *"il Manuale ha due ruoli contraddittori, decide Max"*, e
non gli dava mai gli elementi per decidere. **Nominare un blocco non è istruirlo.**

Quando `ruolo_prodotto` è `non-deciso`, il workflow produce **questo**, e poi si ferma:

### Le due strade, con le conseguenze

| | **A. Il prodotto si vende** | **B. Il prodotto acquisisce contatti** |
|---|---|---|
| Cosa diventa | il prodotto del lancio | il regalo che costruisce la lista per il corso |
| **Il ricavo** | **immediato, da una cosa pronta da marzo** | **spostato su un prodotto che non esiste ancora** |
| Cosa serve in più | un regalo per acquisire contatti — **c'è già**: il framework da 12 pagine | il corso va costruito: mesi |
| Il rischio | il pubblico è piccolo: il ricavo del primo lancio sarà modesto | si costruisce una lista per vendere qualcosa che potrebbe non essere pronto quando la lista è calda |
| Cosa si impara | come converte questo pubblico, con numeri veri | quanto costa acquisire un contatto, e nient'altro |
| Reversibile? | **sì**: un prodotto venduto può diventare un regalo dopo | **no**: un prodotto regalato non si rimette in vendita senza bruciare chi l'ha avuto gratis |

### La riga che rende la decisione facile

> **La strada B sposta il ricavo su un prodotto che non esiste. La strada A incassa da qualcosa
> che è pronto da marzo. E A è reversibile, B no.**

**Il workflow non decide.** Ma presenta la scelta in una forma in cui decidere costa un minuto
invece di sei mesi, e dichiara quale delle due è reversibile — che è l'informazione che quasi
sempre manca quando una decisione si impantana.

---

## 6. Come si istruisce un prezzo — la forma della proposta

Il file `04-proposta.md` ha **sempre** questa forma, e non è negoziabile:

```
PROPOSTA: 47 €

Perché questo numero
  · Listino: livello 1 (7-47 €). 47 è il limite alto del livello — giustificato dalle
    203 pagine, che sono sopra la media della fascia.
  · Mercato: i concorrenti stanno a 39, 49 e 67 € (fonte: ricerca.json, tre schede).
  · Catalogo: oggi non vendiamo niente. Partire dal livello 1 tiene aperta la salita
    al livello 2 per il corso.

ALTERNATIVA PIÙ BASSA: 27 €
  Guadagni: più copie, meno attrito, lista che cresce più in fretta.
  Perdi:    ~40% di ricavo per copia, e il livello 2 diventa un salto più grande.

ALTERNATIVA PIÙ ALTA: 97 €
  Guadagni: margine doppio, posizionamento più alto.
  Perdi:    scatta il beta test obbligatorio (+5-7 giorni), e chiedi 97 € a un
            pubblico che non ci ha mai comprato niente.

NON SO
  · Quanto è disposto a pagare questo pubblico: non è mai stato misurato.
  · Quante persone ci sono nella lista in questo momento.

────────────────────────────────────────────
CONFERMI 47 € ?     [ sì ]   [ no, preferisco ___ ]
```

**Le tre cose che rendono questa forma diversa da una domanda:**

1. **Il numero c'è già.** Non si chiede di produrre un numero: si chiede di validarne uno.
2. **Le alternative hanno la conseguenza accanto**, non solo il valore. Un'alternativa senza
   conseguenza non aiuta a scegliere: allarga la scelta.
3. **`NON SO` è scritto.** Chi firma sa esattamente su cosa sta decidendo al buio, e questa è
   la parte che quasi tutti tolgono per sembrare più sicuri — ed è quella che rende la firma
   possibile, perché toglie il sospetto che ci sia una trappola non detta.

---

## 7. La data — stessa logica

Il prezzo senza la data non sblocca niente: *"€47, presto spero"* è fermo come *"€ non lo so"*.

```
PROPOSTA: apertura martedì 14 ottobre, carrello aperto 5 giorni, chiusura domenica 19 sera

Perché
  · Martedì e mercoledì sono i giorni con più aperture email nella maggior parte dei
    mercati. (assunzione dichiarata: non misurata su questo pubblico)
  · Cinque giorni sono il minimo per fare urgenza vera senza bruciare la lista.
  · Chiudere di domenica sera raccoglie il fine settimana.
  · A ritroso: 30 giorni di preparazione portano l'inizio a lunedì 14 settembre.

CONFLITTI CONTROLLATI
  · Nessun altro lancio previsto in quella finestra.
  · Nessuna festività che svuota le aperture.

CONFERMI 14 OTTOBRE ?     [ sì ]   [ no, preferisco ___ ]
```

**La riga a ritroso è quella che fa firmare.** Mostra che scegliere la data non è scegliere un
giorno: è far partire un conto alla rovescia che comincia adesso.

---

## 8. Il gate — e come è cambiato dopo la critica

| | Prima versione | **Adesso** |
|---|---|---|
| Cosa fa | blocca se prezzo o data sono vuoti o evasivi | **la stessa cosa** — il criterio non cambia |
| Cosa lo accompagna | niente | **una proposta già istruita e una domanda binaria** |
| Cosa succede se nessuno risponde | il lancio resta bloccato in silenzio | dopo **7 giorni** l'inerzia diventa **un problema del lancio**, con la sua riga nello stato e la sua voce nel debrief |

**Il criterio, per intero:**

| Controllo | Superato se |
|---|---|
| `prezzo` | è un numero maggiore di zero |
| `prezzo` non evasivo | non è una stringa, non è `"da definire"`, `"non lo so"`, `"tbd"` |
| `data_apertura` | è una data valida e futura |
| `data_apertura` non evasiva | non è `"presto"`, `"prossimamente"`, `""` |
| `durata_carrello` | è un numero di giorni maggiore di zero |
| `ruolo_prodotto` | è `vendita` o `acquisizione-contatti` — **mai `non-deciso`** |
| struttura | valore dichiarato ≥ 3 volte il prezzo, garanzia presente, **una sola** azione richiesta |
| firma | il campo `firmato_da` contiene un nome di persona |

**L'ultima riga è quella che conta.** Nessuna macchina può riempire `firmato_da`. Non è un
controllo tecnico: è il punto in cui il sistema si ferma e riconosce che ci sono cose che non gli
competono.

### Cosa succede quando l'inerzia dura

| Giorni senza firma | Cosa fa il sistema |
|---:|---|
| 0-2 | niente. Una decisione merita di essere pensata |
| 3 | ricorda, con la proposta allegata, **senza rifarla** |
| 7 | **l'inerzia diventa una voce di stato del lancio**: `bloccato_da: "firma dell'offerta, 7 giorni"` |
| 14 | il lancio passa a `SOSPESO` con data di revisione, e la sentinella dei sospesi lo ripescherà |

**Perché non forza mai.** Perché un prezzo scelto da una macchina per sbloccare un gate è peggio
di un lancio rinviato: il rinvio si vede e si corregge, un prezzo sbagliato si scopre a lancio
finito.

---

## 9. Output tipizzato

```json
{
  "lancio_id": "string",
  "ruolo_prodotto": "vendita | acquisizione-contatti",
  "prezzo": 47.00,
  "valuta": "EUR",
  "livello_listino": 1,
  "data_apertura": "2026-10-14",
  "durata_carrello_gg": 5,
  "data_chiusura": "2026-10-19",
  "struttura": {
    "valore_dichiarato": 189.00,
    "rapporto_valore_prezzo": 4.02,
    "ancoraggio": "string",
    "bonus": [ { "nome": "string", "valore": "number" } ],
    "garanzia": { "giorni": 14, "condizioni": "string" },
    "motivo_per_agire_adesso": "string — una scadenza vera, mai 'affrettati'"
  },
  "alternative_scartate": [
    { "prezzo": 27.00, "perche_no": "string" },
    { "prezzo": 97.00, "perche_no": "string" }
  ],
  "non_misurato": ["disponibilità a pagare del pubblico"],
  "firmato_da": "Max",
  "firmato_il": "2026-09-12T10:30:00"
}
```

**`alternative_scartate` non è burocrazia.** È ciò che, al terzo lancio, permette di guardare
indietro e vedere se si è sempre scelto troppo basso — che è l'errore più comune e il più
invisibile, perché un prezzo basso vende e quindi sembra aver funzionato.

---

## 10. Gli eseguibili

`scripts/offerta.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `colloca_listino` | `colloca_listino(prodotto: dict, catalogo: list[dict]) -> dict` | livello, e se ci sono salti la loro entità |
| `estrai_prezzi_mercato` | `estrai_prezzi_mercato(ricerca: dict) -> list[dict]` | i prezzi dei concorrenti con la fonte |
| `istruisci` | `istruisci(lancio_id: str) -> str` | **il testo della proposta con le due alternative** — è la funzione più importante del reparto |
| `proponi_data` | `proponi_data(oggi: str, giorni_preparazione: int, impegni: list[dict]) -> dict` | data proposta, ragione, conflitti trovati |
| `firma` | `firma(lancio_id: str, chi: str, valore: float \| str) -> dict` | registra la conferma e scrive `offerta.json` |
| `giorni_di_inerzia` | `giorni_di_inerzia(lancio_id: str, oggi: str) -> int` | da quanto la proposta aspetta |

`scripts/gate_offerta.py`

| Funzione | Firma | Ritorna |
|---|---|---|
| `valori_evasivi` | `valori_evasivi(offerta: dict) -> list[str]` | i campi con valori che sembrano decisioni e non lo sono |
| `verifica` | `verifica(lancio_id: str) -> int` | il verbale, e il codice di uscita |

---

## 11. Skill e comando

`/lancio-offerta <id>` istruisce e presenta · `--firma <valore>` registra la conferma ·
`--stato` dice da quanti giorni la proposta aspetta.

**Se manca il certificato del prodotto:** si ferma e dice che il blocco è del reparto Prodotto.
**Se manca la ricerca:** procede lo stesso, e la proposta esce marcata come cieca sul mercato.
**Se il ruolo del prodotto è contraddittorio:** produce il confronto delle due strade (§5) e si
ferma lì. È l'unico caso in cui questo workflow si ferma prima ancora di proporre un numero.

---

## 12. Come si misura che ha funzionato

| Metrica | Bersaglio | Perché questa |
|---|---|---|
| **Giorni fra `ISTRUITO` e la firma** | **≤3** | è la metrica che conta più di ogni altra: misura esattamente il blocco che il reparto esiste per sciogliere. Oggi quel numero è **180** |
| Proposte firmate senza modifica | ≥60% | se quasi tutte vengono modificate, la proposta è tarata male |
| Lanci partiti senza prezzo | **0** | per definizione |
| Alternative scartate registrate | 100% | serve al terzo lancio, non a questo |
| Prezzi rivisti dopo l'apertura | 0 | cambiare prezzo a carrello aperto brucia chi ha già comprato |

**La prima riga da sola giustifica l'esistenza di questo reparto.** Se il tempo fra "prodotto
pronto" e "prezzo firmato" scende da centottanta giorni a tre, l'ecosistema ha già ripagato la
propria costruzione — anche se ogni altro reparto fallisse.

---

## OBIEZIONI

**«Una macchina che propone un prezzo su un mercato che non conosce proporrà sciocchezze.»**
Probabile al primo giro, e per questo la proposta porta sempre `NON SO` in chiaro e due
alternative. Ma il confronto giusto non è *"proposta della macchina contro proposta di un
esperto"*: è *"proposta della macchina contro sei mesi di silenzio"*. Una proposta sbagliata si
corregge in dieci secondi cambiando il numero; un silenzio no.

**«Se la firma non arriva lo stesso, questo reparto non ha risolto niente.»**
Vero, e va detto: **non può risolverlo.** Può ridurre l'attrito da "produci una decisione
difficile" a "conferma un numero", può ricordare, e può rendere l'inerzia visibile invece che
silenziosa. Se dopo tutto questo la firma non arriva, **il problema non è il sistema** — ed è
un'informazione che oggi non abbiamo e che vale.

**«Il rapporto valore/prezzo di almeno tre volte è arbitrario.»**
Sì, è ereditato dal materiale storico e non misurato su questa azienda. Resta come soglia di
partenza, marcato come provvisorio, e il primo lancio ha il compito di produrre il numero vero.
