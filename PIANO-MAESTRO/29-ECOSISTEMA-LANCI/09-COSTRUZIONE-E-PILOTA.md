# IL PIANO DI COSTRUZIONE — seconda versione
*(riscritto: le durate erano in un'unità di misura che non esiste, e lo scaglione minimo era una raccomandazione)*

---

## 0. Le tre correzioni

| Crepa della prima versione | Correzione |
|---|---|
| Le durate erano in **giorni pieni di lavoro**, che non esistono: chi costruisce ha una frazione di settimana e altre task aperte | ora sono in **ore-uomo**, con la conversione in calendario dichiarata accanto |
| Lo scaglione minimo era una **raccomandazione**, e niente impediva di costruire tutto | è un **vincolo tecnico**: il registro rifiuta gli agenti dei reparti non abilitati |
| **Non esisteva una condizione di abbandono**: implicitamente si continuava per sempre | tre condizioni scritte prima di cominciare |

---

## 1. La regola che governa tutto

> **Nessuno scaglione si chiude con della carta. Ognuno finisce con qualcosa che si esegue e
> che si può vedere fallire.**

Il precedente è misurato: il reparto Lanci esistente ha **2.377 righe di documentazione e zero
file eseguibili**, ed è sembrato vivo per due mesi e mezzo. La forma che gliel'ha permesso è una
frase — *"script pianificati, build in V2"* — scritta senza data e senza un nome.

**Divieto per tutta la costruzione:** nessun file può contenere la parola "pianificato" senza
accanto una data e un nome. Senza la data non è pianificato: è desiderato.

---

## 2. L'ordine, e perché è controintuitivo

L'ordine naturale sarebbe seguire il flusso: strategia, intelligence, prodotto, e così via.
**È l'ordine sbagliato**, e la ragione è dimostrabile: costruire i reparti prima
dell'infrastruttura li fa nascere come documenti. È esattamente così che è nato il reparto che
oggi non esegue niente.

```
S0  FONDAMENTA        stato, memoria, motore dei gate — nessun reparto
     │                ▼ prova: un lancio finto attraversa gli stati e SI BLOCCA dove deve
S1  MINIMO            4 reparti, 9 agenti: dall'idea alla vendita chiusa
     │                ▼ prova: il Manuale Claude Code esce davvero
S2  MATERIALI         testi, funnel, contenuti — lo sprint parallelo
     │                ▼ prova: un funnel completo online e misurato
S3  INTELLIGENZA      mercato, prodotto, traffico
     │                ▼ prova: una ricerca con 15 fonti verificate, e una falsa respinta
S4  CHIUSURA          tesoro, qualità completa, memoria
     │                ▼ prova: uno schema del primo lancio cambia una decisione del secondo
S5  AUTOMAZIONE       solo ciò che ha già girato a mano
```

**Il vincolo fra S1 e S2 è tecnico, non morale:** finché `lanci/` non contiene un lancio in stato
`APPRESO`, il registro **rifiuta** di registrare gli agenti di S2. Non è sconsigliato: non si può.

---

## 3. S0 — FONDAMENTA · 24-32 ore-uomo

*(a 3 ore al giorno: due settimane di calendario. A tempo pieno: tre giorni.)*

| # | Cosa | File | Prova che è fatto | Ore |
|---|---|---|---|---:|
| S0.1 | Cartella dell'ecosistema e file di testa | `15-LANCI/` + 5 file | esistono; il registro dei numeri dice **15 occupato** | 3 |
| S0.2 | **Macchina a stati** | `scripts/stato_lancio.py` | un lancio finto attraversa gli stati; **ogni transizione illecita viene rifiutata** | 6 |
| S0.3 | **Motore dei gate** | `scripts/gate.py` | un gate finto **blocca davvero** e scrive il verbale | 5 |
| S0.4 | **Memoria** | `scripts/memoria.py` | scrive un record, **rifiuta** un record senza proprietario, genera l'indice | 5 |
| S0.5 | Validatore dei passaggi | `scripts/handoff.py` | **rifiuta** un passaggio senza verbale di gate | 3 |
| S0.6 | Schemi JSON | `schemi/*.json` | ogni artefatto ha il suo schema, e uno di prova lo supera | 3 |
| S0.7 | Comando unico | `scripts/lancio.py` | `crea`, `stato`, `avanza`, `riprendi` funzionano | 4 |
| S0.8 | Test | `tests/` | **ogni gate ha un caso che FALLISCE** | 3 |

### Il criterio di chiusura — un comando

```bash
python -m scripts.lancio crea prova-vuota --prodotto "Prova"
python -m scripts.lancio avanza prova-vuota
```

**Deve bloccarsi al gate dell'offerta**, uscire con codice diverso da zero, scrivere il verbale,
e lasciare lo stato dov'era.

**Se esce zero, S0 non è chiuso**, per quanto codice sia stato scritto.

**Perché la memoria sta qui e non in fondo:** l'obiezione più forte contro tutto il modello di
memoria è che nessuno la riempirà. L'unica risposta è renderla un **effetto dell'esecuzione**
invece che un compito. Se `memoria.py` non esiste quando nascono i reparti, i reparti nasceranno
senza scriverci dentro, e non ci scriveranno mai.

---

## 4. S1 — IL MINIMO · 30-40 ore-uomo + il tempo di una firma

*(a 3 ore al giorno: due settimane e mezzo, più l'attesa della firma — che non è lavoro.)*

**Quattro reparti**, scelti perché sono esattamente ciò che manca al Manuale: tutto il resto quel
prodotto ce l'ha già.

| Reparto | Perché serve per questo lancio |
|---|---|
| `LAN-STR` | decide che si fa **adesso**, non ancora "presto" |
| `LAN-OFF` | **il pezzo mancante da sei mesi** |
| `LAN-FNL` | la pagina esiste ma nessuno ha provato che misuri |
| `LAN-REG` | calendario, apertura, tracciamento, chiusura |

**Nove agenti**: direttore dell'ecosistema, segretario, filtro della strategia, prezzo, struttura
dell'offerta, verificatore delle pagine, calendarista, tracciatore, motore dei gate.

**Cosa NON si costruisce, deliberatamente:** testi, ricerca, certificazione, traffico, contenuti,
tesoro, memoria completa. Per il Manuale **esistono già**. Rifarli sarebbe la malattia opposta e
altrettanto grave.

### Il criterio di chiusura

1. `offerta.json` contiene un prezzo che è un numero e una data che è una data.
2. `funnel.json` dichiara ogni pagina col suo esito e l'evento di conversione **scattato almeno
   una volta in prova**.
3. Il carrello si è aperto e chiuso alle date del calendario.
4. `consuntivo.md` riporta un ricavo reale — **anche se è zero**.
5. `debrief.md` esiste con almeno tre schemi.

**Il punto 4 va letto bene:** S1 è chiuso anche se il lancio incassa poco. **Non è chiuso se
nessuno sa quanto ha incassato.** La differenza fra le due cose è tutto ciò che questo ecosistema
esiste per costruire.

---

## 5. S2 · 35-45 ore-uomo — *si sblocca solo con un lancio in `APPRESO`*

| Reparto | Cosa | Prova |
|---|---|---|
| `LAN-CPY` | 6 agenti, la griglia di punteggio, il gate a 80 | un testo reale ottiene un punteggio **calcolato**, e uno scadente viene **bocciato** |
| `LAN-FNL` completo | le nove pagine, il ciclo di ottimizzazione | un funnel intero con i numeri per pagina |
| `LAN-EDT` | il piano dei 37 giorni, gli agganci alle fabbriche | un piano dove **nessuna riga lascia una decisione aperta** |

**Il criterio:** i tre girano insieme e il punto di sincronizzazione blocca davvero. Si prova
**facendo fallire uno dei tre di proposito**: se la vendita si apre lo stesso, il punto di
sincronizzazione non esiste.

---

## 6. S3 · 25-35 ore-uomo — *si sblocca con due lanci in `APPRESO`*

| Reparto | Prova |
|---|---|
| `LAN-INT` | una ricerca finta, con frasi plausibili e senza fonte, **viene fermata dal gate** |
| `LAN-PRD` | un prodotto con un collegamento rotto viene bloccato **dal test**, non da una persona |
| `LAN-TRF` | due canali con costo di acquisizione separato e non mischiato |

**Il criterio di S3 è il caso costruito apposta per fallire.** Se il gate anti-invenzione non
ferma una ricerca inventata, tutto il reparto è decorativo.

---

## 7. S4 · 25-35 ore-uomo — *due lanci **e** almeno un gate che ha bloccato davvero*

| Reparto | Prova |
|---|---|
| `LAN-TSR` | uno scarto oltre il 10% blocca, e si sblocca **solo con una firma tracciata** |
| `LAN-QLT` completo | ogni gate ha un caso di fallimento nei test |
| `LAN-MEM` | **uno schema del primo lancio cambia una decisione del secondo, e si vede dove** |

**Il criterio di S4 è il più bello di tutti:** al secondo lancio, il capo della Strategia legge
uno schema del primo e **prende una decisione diversa da quella che avrebbe preso**. Se non
succede, quella non è memoria: è archivio.

---

## 8. S5 — l'automazione e i suoi confini

| Si automatizza | Non si automatizza mai |
|---|---|
| generare il calendario | aprire la vendita |
| controllare che le pagine rispondano e traccino | l'invio reale alla lista |
| calcolare scarti, costo di acquisizione, pareggio | pagare o attivare abbonamenti |
| raccogliere i numeri del giorno | pubblicare una pagina live |
| la parte calcolabile del punteggio dei testi | il giudizio sulla parte non calcolabile |
| proporre uno schema riutilizzabile | promuoverlo a regola |

**La regola che separa le colonne:** si automatizza ciò che, sbagliando, produce un file
sbagliato. Non si automatizza ciò che, sbagliando, produce un danno fuori dall'azienda.

---

## 9. Il totale, dichiarato onestamente

| Scaglione | Ore-uomo | A 3 ore al giorno | A tempo pieno |
|---|---:|---|---|
| S0 | 24-32 | 2 settimane | 3-4 giorni |
| S1 | 30-40 | 2,5 settimane | 4-5 giorni |
| S2 | 35-45 | 3 settimane | 5-6 giorni |
| S3 | 25-35 | 2 settimane | 3-4 giorni |
| S4 | 25-35 | 2 settimane | 3-4 giorni |
| **Totale** | **139-187** | **~3 mesi** | **~3,5 settimane** |

**La conversione va detta, perché la prima versione non la diceva e questo genera la delusione
della seconda settimana:** centoquaranta ore a tre ore al giorno sono **tre mesi di calendario**.
Chi legge "S0 in 3-5 giorni" e poi ci mette due settimane pensa che il piano fosse sbagliato,
mentre era solo scritto in un'unità di misura che nella vita reale non esiste.

**E le stime su cosa si basano:** per analogia con l'unico flusso di questo repo che è stato
costruito e funziona davvero. L'analogia può sbagliare, e sbaglierà sempre nello stesso modo —
**S1 durerà più del previsto**, perché contiene l'unica parte che non dipende da chi costruisce:
una persona che firma un prezzo.

---

## 10. QUANDO SI SMETTE — le tre condizioni

> La prima versione non le aveva. Un piano senza condizione di uscita è una scommessa senza
> limite di perdita.

| # | Se accade | Allora |
|---|---|---|
| **1** | S0 supera **64 ore-uomo** (il doppio del massimo stimato) senza che i comandi base girino | **si ferma tutto.** Se l'infrastruttura è fuori portata, dodici reparti lo sono a maggior ragione: si torna al piano e si taglia |
| **2** | Il lancio pilota non esce **entro 60 giorni** dall'inizio di S1 | **si ferma la costruzione** e si guarda la causa. Se il blocco è una firma che non arriva, nessun reparto in più la farà arrivare |
| **3** | Dopo **due lanci** non esiste un solo schema che abbia cambiato una decisione | **la memoria si dichiara fallita** e si smette di mantenerla, invece di riempirla per abitudine |

**Fermarsi alla condizione 1 o 2 non sarebbe un fallimento del lavoro.** Sarebbe la scoperta,
pagata poco e presto, che il problema di questa azienda sui lanci non è organizzativo — ed è
un'informazione che oggi non abbiamo e che vale più di dodici reparti costruiti bene e mai usati.

---

## 11. Il pre-mortem, con l'antidoto accanto

| Fallimento | Sintomo precoce | Antidoto nel piano |
|---|---|---|
| **Diventa carta** | a fine settimana ci sono file nuovi e nessun comando nuovo | S0 non contiene un solo documento di dottrina: solo eseguibili |
| **Non viene usato** | il Manuale esce a mano, fuori dal sistema | S1 ha come criterio **quel** lancio dentro **quel** sistema |
| **Duplica l'Impero** | nasce un secondo posto dove si contano i soldi o si scrivono i testi | ogni reparto etichettato col percorso di ciò che avvolge |
| **Si costruisce senza ufficializzare** | gli agenti funzionano nella sessione e non compaiono negli elenchi | la procedura con i comandi di verifica, in ogni scaglione |
| **Muore la memoria** | l'indice non cambia da giorni | scrittura come **condizione di chiusura di fase** |
| **Si costruisce tutto invece del minimo** | compaiono cartelle di reparti non abilitati | **il registro le rifiuta** |
| **Gael non lo fa suo** | il piano resta aperto e la costruzione non parte | la nota d'apertura, e tutta la costruzione lasciata a lui |
