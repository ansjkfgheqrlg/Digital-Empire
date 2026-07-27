# 27 — AUTOPSIA DELLA SETTIMANA (21 → 27 luglio 2026)

> Prompt **P8** del dossier 26, eseguito da Arena il 27/07 su richiesta di Max.
> Consegna richiesta: *"dimmi la verità su questa settimana, non farmi sentire bene."*
> Ogni numero qui sotto è stato contato sui file, non stimato. Metodo dichiarato per ognuno.

---

## 1. Quanti euro sono entrati questa settimana?

# € 0

Zero. Non "in arrivo", non "in pipeline": **zero incassato.**

*Come l'ho verificato:* non esiste nel repository un solo file che registri un pagamento, una
fattura, un incasso o una proposta accettata in questa settimana. Nessuna delle 38 note di
lavoro (checkpoint) di questi 7 giorni menziona un euro entrato. Se l'incasso c'è stato fuori
dal repo, questa autopsia non lo può vedere — ma allora **il problema è che non lo state
tracciando da nessuna parte**, ed è comunque un problema.

---

## 2. Quante persone nuove hanno saputo che esistiamo?

# 2

Due. Due concessionari, entrambi di **Brescia** — non di Verona, Padova o Vicenza, che erano le
province decise.

| Chi | Quando | Canale |
|---|---|---|
| Autobase Brescia (Hyundai, Mazda, EMC, Foton) | 25/07 | WhatsApp |
| Gruppo Carmeli (Renault Dacia) | 25/07 | WhatsApp |

*Fonte:* `Outreach/preventa-maps-scraper/data/report_contatti.json` — 2 record, entrambi
`stato: contattato`, `data_primo_contatto: 2026-07-25`.

### Il dato che fa più male di tutti

Ho contato le email **già scritte, personalizzate e pronte** che stanno ferme nei file:

| File | Email pronte |
|---|---|
| `emails_b5_ready.json` | 208 |
| `emails_b6_ready.json` | 182 |
| `emails_perfect_batch.json` | 50 |
| `emails_ready.json` | 37 |
| `emails_b4_ready.json` | 31 |
| **TOTALE** | **508** |

**Cinquecentotto messaggi pronti da mandare. Ne sono partiti due.**

E l'ultimo invio di massa registrato dal sistema è del **3 giugno 2026**: 592 email inviate in
totale nello storico (448 consegnate, 102 in errore), tutte tra maggio e inizio giugno. **Da
55 giorni la macchina di outreach non manda niente**, mentre nel frattempo la si continua a
migliorare.

---

## 3. Quante hanno risposto? Cosa hanno detto?

# 0 risposte

Nessuna risposta registrata. Né positiva né negativa.

*Con 2 contatti partiti, è statisticamente normale: su 2 messaggi la risposta attesa è tra 0 e 1.*
**Non è un problema di copy. È un problema di volume: 2 non è un test, è un aneddoto.**

Gli unici "dialoghi" presenti nei file della campagna sono **finti**: `report_test.json` contiene
scambi con «Autosalone Test Uno», «Concessionaria Test Due», «Auto Premium Test Tre». Sono dati
di collaudo, correttamente etichettati come test — ma **non c'è nient'altro**.

---

## 4. Cosa abbiamo costruito che NON ha prodotto un contatto né un euro?

Senza pietà, come richiesto. Tutta roba fatta bene. Tutta a valle di zero.

| Cosa | Quando | Contatti prodotti | Euro prodotti |
|---|---|---|---|
| **APEX-7 Level 2** — event bus, memory 5-query, 6 quality gate, meta-agent, test verdi | 27/07 | 0 | 0 |
| **Ricostruzione 7 agenti preventa** (phase A + phase B + verifica runtime) | 25-27/07 | 0 | 0 |
| **Riorganizzazione "Estate = cervello non muscolo"** — 4 script spostati con `git mv` | 27/07 | 0 | 0 |
| **`empire/forge.py`** — misuratore di quanto un agente è operativo, 6 criteri, CLI | 25/07 | 0 | 0 |
| **Promozione agenti PEZZO 1 + 2** (closer-A8, cro-copy-architect) | 25/07 | 0 | 0 |
| **I 7 piani di ristrutturazione** (fondamenta, cicli, workflow, gerarchia, sessioni, autonomia, apex) | 24/07 | 0 | 0 |
| **`empire/flow/`** — motore workflow con gate | 23/07 | 0 | 0 |
| **Dossier 22, 23, 24, 25** — piani, analisi prodotti, calendario, task board | 22-23/07 | 0 | 0 |
| **Sezioni sito** Preventa + Prove Novacar | 23/07 | 0 | 0 |
| **Skill YouTube Automation Factory** (29 file, 11 agenti) — *mai eseguita in produzione* | 21/07 | 0 | 0 |
| **Dossier 26 + kit vendita P4 + pulizia sito** (io, oggi) | 27/07 | 0 | 0 |

**38 checkpoint in 7 giorni. 7 solo oggi. Due messaggi WhatsApp partiti.**

Metto anche il mio lavoro in questa tabella, perché vale la stessa regola: il dossier 26, il kit
di vendita e la pulizia del sito **non hanno prodotto un contatto né un euro**. Sono strumenti.
Uno strumento che nessuno impugna pesa esattamente quanto niente.

### La riga più dura

Il vostro `agency-empire` ha una pagina che elenca **435 agenti**, un runtime con 20 comandi, un
sistema nervoso multi-agente con quality gate a 7 livelli — e un file
`report_contatti.json` **con dentro due record.**

---

## 5. L'unica cosa da fare la settimana prossima

## Mandare le 508 email che sono già scritte.

Non scriverne di nuove. Non migliorare il copy. Non rifattorizzare lo scraper. Non finire
APEX-7 Level 3.

**Aprire i file, prendere i messaggi già pronti, e mandarli** — con la rampa di sicurezza
(20 il primo giorno, 30, 50, fino a 80/giorno per dominio).

Perché è questa e non altro:
- **è già fatto.** Il costo marginale è vicino a zero: il lavoro è stato pagato settimane fa
  e sta lì a scadere;
- **è l'unico anello mancante.** Avete lead, messaggi, motore, follow-up, tracking. Manca
  l'invio;
- **produce l'unica cosa che oggi non avete: dati veri.** Con 500 contatti sapete il tasso di
  risposta reale. Con 2 non sapete niente e continuate a decidere alla cieca;
- **niente altro può produrre cassa in 7 giorni.** Il ticket €5-15k ha un ciclo di settimane:
  se le prime demo non partono adesso, agosto è vuoto per definizione.

Se la settimana prossima parte **solo** questo e nient'altro, la settimana è vinta.
Se parte tutto il resto e non questo, è persa — anche se produce altri 38 checkpoint.

---

## 6. Cosa stiamo evitando perché è scomodo?

Tre cose. Sono tutte e tre della stessa famiglia: **espongono al rifiuto di un essere umano.**

### 1. Premere "invia" su lead veri
Costruire è sicuro: se sbagli, rifattorizzi. Mandare 500 email è irreversibile — puoi ricevere
un "no", un insulto, o peggio: il silenzio. **Il refactoring è una forma elegante di rimandare.**

Il segnale è nei numeri: `G-A4` (il run reale) è marcato **🟢 SBLOCCATO dal 23/07** nel dossier 25.
Da allora sono stati chiusi APEX-7 Level 2, la ricostruzione di 7 agenti, una riorganizzazione di
cartelle. **Tutte cose che nessuno aveva chiesto con urgenza. E il task sbloccato è ancora lì.**

Il 25/07, che è il giorno in cui *finalmente* sono partiti 2 messaggi, è anche il giorno in cui
sono stati chiusi 2 checkpoint di refactoring agenti. **Si è preferito lavorare sugli agenti che
sui concessionari.**

### 2. Telefonare
Il dossier 25 dice, correttamente, che *"le chiamate a freddo restano umane (Max)"*. Nel
repository **non c'è traccia di una sola chiamata fatta**: nessun registro, nessun esito, nessuna
nota. I 2 contatti del 25/07 sono su WhatsApp — il canale dove non ti possono dire di no in faccia.

### 3. Chiedere a Novacar la testimonianza
Novacar è un cliente **servito, con la macchina in uso e 65 documenti prodotti**. Una telefonata
di 10 minuti. È l'asset a più alto rapporto valore/sforzo dell'intera azienda, ed è aperto da
settimane.

Perché non si fa: chiedere una testimonianza è chiedere un favore, e chiedere un favore è
esporsi. È molto più comodo scrivere un dossier sull'importanza delle testimonianze.

> **Nota di contesto, perché sia chiaro quanto è costato non chiederla:** oggi ho rimosso dal sito
> tre testimonianze con nome e cognome — Marco Resta, Sara Conti, Luca Pellegrini — che **non
> corrispondono a nessuna persona presente in nessun file del repository**. Erano lì al posto di
> quella vera, che sarebbe costata una telefonata.

---

# Le 3 task della settimana entrante

## 🔵 MAX — mandare, non preparare
**Lunedì mattina, prima di qualsiasi altra cosa:** dai l'ok al lancio e **guarda partire i primi
20 messaggi**. Poi ogni giorno: rampa (20→30→50→80) fino a esaurire i 508.
**In parallelo, due telefonate:** Novacar per la testimonianza, e i primi 5 concessionari che
rispondono.
**Criterio di riuscita:** venerdì il numero della domanda 2 non è "2". Se è sotto 100, è fallita.

## 🟣 GAEL — congelare la costruzione
**Nessun nuovo build questa settimana.** Non APEX-7 Level 3, non il refactoring dello scraper,
non YouTube. L'unica cosa ammessa: **far funzionare l'invio** (se si inceppa, lo ripari) e il
cruscotto di P3 che stampa ogni mattina *inviate / risposte / demo*.
**Criterio di riuscita:** ogni sera esiste una riga con i numeri del giorno.
*Se venerdì l'invio gira e ci sono 3 nuovi checkpoint di refactoring, quei 3 checkpoint sono
il problema.*

## ⚫ ARENA — fare il conto, non i piani
**Nessun nuovo dossier.** Il mio unico compito: venerdì 31/07 rifaccio questa autopsia con i
numeri nuovi, e rispondo a una domanda sola — **il tasso di risposta reale su ~500 contatti**.
Poi review dei messaggi che arrivano e sistemazione delle obiezioni che escono davvero.
**Criterio di riuscita:** il dossier 28 non esiste. Esiste solo un aggiornamento di questa tabella.

---

## Verdetto

**Questa settimana è stata costruzione pura senza cassa.** Con quelle parole, come richiesto.

Non è stata una settimana pigra: 38 checkpoint, un sistema nervoso multi-agente operativo, agenti
ricostruiti, test verdi. **È stata una settimana di lavoro serio speso interamente sul lato
sbagliato del problema.**

Il prompt P8 chiedeva di segnalare se anche questo dossier dicesse *"l'incasso arriva la settimana
prossima"* — perché sarebbe il segno che si è rotto il metodo. **Lo dico chiaramente: non è il
mercato che non risponde. Il mercato non ha ancora ricevuto 506 dei nostri 508 messaggi.**

Il mercato non vi ha detto di no. **Non gli avete ancora chiesto niente.**
