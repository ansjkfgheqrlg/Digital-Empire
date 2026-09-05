---
Type: PROJECT
Status: Proposta — versione 4
Tags: #lanci #ecosistema-15 #architettura
Created: 2026-09-05
---

# 01 — L'ARCHITETTURA

> **Regola di lettura:** questo documento spiega. Il registro decide.
> Se una riga qui contraddice `dati/registro.yaml`, ha torto questa riga.

---

## 1. LA CATENA — il sistema è questa, non un organigramma

Tredici artefatti, in ordine di dipendenza. Le dipendenze non sono un consiglio: il validatore
verifica che non ci siano cicli, e `avanza` rifiuta di produrre un artefatto se quelli da cui
dipende non sono validi **ricalcolati adesso**, non secondo lo stato salvato.

```
  ART-PUB  pubblico          ── quante persone, con la prova
     │
     ├──► ART-DEC  decisione ── si fa adesso
     │       │
     │       ├──► ART-CRT  certificato ── il prodotto è consegnabile
     │       └──► ART-RIC  ricerca     ── le parole vere, con la fonte
     │               │
     └───────────────┴──► ART-PRV  previsione ── quanto ci aspettiamo di incassare
                              │
                              ▼
                          ART-OFF  offerta ── prezzo + data + FIRMA UMANA
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
          ART-CPY         ART-BDG         (ART-CPY)
           copy            budget              │
              │                                ▼
              └──────────────────────────► ART-FNL  funnel ── online, misura, INCASSA
                                                │
                                          ART-EDT  editoriale
                                                │
                                                ▼
                                        ART-APE  apertura ── VIA LIBERA UMANO
                                                │
                                                ▼
                                        ART-CNS  consuntivo ── quanto è entrato
                                                │
                                                ▼
                                        ART-DBR  debrief ── previsto vs reale
```

**Perché la previsione sta prima dell'offerta e non dopo.** Perché la domanda che si porta a chi
firma non è *«confermi 47 €?»* ma *«confermi 47 €, che su questo pubblico fanno questo ricavo?»*.
Fra le due domande c'è la differenza fra scegliere un numero e prendere una decisione.

**Perché il funnel viene prima dell'apertura e contiene la prova di cassa.** Perché la versione
precedente metteva la pubblicazione irreversibile prima della prova che il pagamento funzionasse.
Si vende solo dopo che un euro vero è entrato ed è tornato indietro.

---

## 2. `lancio avanza` — la spina dorsale, che nella v3 non aveva una riga di specifica

> Il difetto, dichiarato: la v3 fondava la propria tesi su questa frase — *«i controlli non sono
> un reparto da chiamare: sono dentro `lancio avanza`, e per saltarne uno bisogna smettere di
> usare il sistema»* — e poi **non specificava quel comando da nessuna parte**, mentre tre script
> minori avevano firme complete. L'oggetto su cui poggiava tutto era l'unico senza contratto.

### 2.1 La firma

```python
def avanza(
    lancio_id: str,
    *,
    solo_gate: str | None = None,   # esegue un solo controllo, per riprovare dopo una correzione
    a_vuoto: bool = False,          # calcola e stampa, non scrive nulla
) -> int:
    """Fa avanzare un lancio finché un controllo non lo ferma.

    Ritorna il codice di uscita. Non solleva eccezioni verso il chiamante:
    un errore imprevisto diventa codice 3 con il verbale scritto.
    """
```

### 2.2 I codici di uscita

| Codice | Significa | Ha scritto file? |
|---:|---|---|
| **0** | il lancio è avanzato fin dove poteva, nessun controllo lo ferma | sì: stato + verbali |
| **1** | un controllo ha **bloccato** | sì: il verbale del blocco, e lo stato resta dov'era |
| **2** | ingresso non valido (lancio inesistente, artefatto malformato) | **no, nessuno** |
| **3** | ambiente (manca una dipendenza, il fornitore non risponde, il tetto di spesa è esaurito) | sì: il verbale d'ambiente |

La distinzione fra 2 e 3 non è formale: **il 2 non lascia niente sul disco**, quindi si può
riprovare a mente sgombra; il 3 lascia il lavoro fatto e si riprende.

### 2.3 Le tre garanzie

**Esclusività.** `avanza` prende un lock esclusivo sul file di stato del lancio prima di leggere
qualsiasi cosa, e lo rilascia alla fine. Se il lock è già preso, esce **1** dicendo chi lo
detiene e da quando.

> *Il caso concreto che la impone:* Max e Gael lavorano dallo stesso repository su due macchine.
> Due `avanza` sullo stesso lancio a un minuto di distanza, nella v3, avrebbero eseguito due
> volte gli stessi controlli, scritto due verbali con lo stesso nome e riscritto lo stato da due
> processi. Nessuna riga della v3 lo impediva.

**Idempotenza.** Rieseguire `avanza` senza che sia cambiato nulla non produce nessuna scrittura
nuova e riesce. I verbali hanno chiave `(controllo, tentativo)`: un secondo giro identico non
crea un secondo verbale, aggiorna quello.

**Ricalcolo, mai fiducia.** Ogni controllo ricalcola il proprio giudizio **dai file**, mai dal
campo `gate` dello stato. Lo stato è una comodità di lettura, non una fonte.

> *Perché è una garanzia e non una precauzione:* questo repository ha tre casi documentati di
> codice che stampa "successo" senza aver eseguito niente — uno stampa perfino
> `completata con successo (SIMULATA)` ed esce zero. È il modello di fallimento più probabile
> dell'intero sistema, e va trattato come tale.

### 2.4 Chi lo invoca, e quando

| Momento | Chi |
|---|---|
| a mano, quando si vuole sapere a che punto è | la persona |
| alla chiusura di ogni fase | l'agente che ha chiuso la fase |
| una volta al giorno sui lanci non chiusi | un promemoria pianificato |

**La terza riga esiste per un difetto reale:** senza, un lancio può restare fermo per giorni
perché nessuno digita il comando, e il sistema non se ne accorge — che è esattamente il modo in
cui il Manuale è rimasto fermo sei mesi, con più file attorno.

---

## 3. GLI STATI, E LE VIE DI RITORNO

Dodici stati, diciassette transizioni, tutte nel registro. Le tre regole che contano:

**Ogni blocco ha una via d'uscita scritta.** `SOSPESO` porta con sé `stato_di_partenza`,
`revisione_il` (mai vuoto) e `come_si_esce` — che è **un comando eseguibile**, non una
descrizione. L'idea viene dalla v3 ed è la cosa migliore che aveva; qui è estesa a ogni blocco,
non solo a quello.

**Gli orologi si fermano.** Quando un lancio entra in `SOSPESO`, tutte le scadenze si congelano e
ripartono dal valore che avevano.

> *Il difetto che ripara:* nella v3 un lancio sospeso per una firma mancante continuava ad
> accumulare scadenze di consegna, che scattavano tutte insieme al risveglio. Il sistema puniva
> chi tornava.

**Uno sforamento di budget non uccide il lancio.** `IN_PRODUZIONE → DATATO`: la spesa nuova si
blocca, il lancio torna indietro di uno stato e si sblocca solo con una firma tracciata.

---

## 4. IL PONTE — come un programma fa lavorare un agente

> **Il buco più profondo della v3:** tutto il piano poggiava su agenti che «eseguono fasi» dentro
> un comando Python, e **non diceva mai** come un file `.claude/agents/*.md` viene invocato da un
> programma. Se quel ponte non esiste, l'ecosistema nasce di carta — cioè esattamente il difetto
> che dichiarava di curare.

**Verificato sulla macchina il 2026-09-05:** il meccanismo esiste e funziona
(`claude -p --agent <id> --output-format json`); **nessuno script dell'azienda lo usa ancora.**

E le regole d'uso non sono da inventare: **sono già state pagate da ADR-014** (2026-08-30), che
la v3 non citava mai.

| Regola | Perché, e quanto è costata |
|---|---|
| il prompt si passa da **standard input**, mai come argomento | il wrapper troncava i prompt multiriga alla prima riga, **in silenzio** |
| si passa l'**identificativo esplicito** del modello, mai l'alias | `--model sonnet` restituiva `claude-sonnet-4-6`: si pagava un modello per un altro |
| si legge `total_cost_usd` e si verifica il budget **prima** di ogni chiamata | il tetto di spesa è stato sfondato una volta, in silenzio |
| si lavora **a blocchi**, non a unità minima | ogni invocazione costa ~0,08-0,11 $ di **sola tassa**, qualunque sia il contenuto |

**Tetto per lancio: 15 $.** Al tetto il lancio si ferma dov'è, salvato: si riprende, non si
ricomincia. È la stessa disciplina del flusso dei libri, che ha un tetto di 5 $ a libro.

**La conseguenza sul numero degli agenti.** Con una tassa fissa per invocazione, quarantuno
agenti non sono una ricchezza: sono un moltiplicatore di costo fisso. Nel registro gli agenti
sono **quindici**, e tre di essi sono al grado più basso perché fanno calcoli deterministici —
un modello linguistico che «ragiona» su una somma è un modo caro di sbagliare.

---

## 5. IL GIUDICE NON HA LA PENNA

Un solo agente esegue tutti i controlli: `lan-gate`. **Non ha `Write` né `Edit` fra i propri
strumenti**, e l'invariante INV-09 lo verifica.

> *Il difetto che ripara, misurato dai revisori:* nel flusso Prodotto della v3, **cinque
> controlli su sette erano eseguiti dallo stesso agente che aveva prodotto la cosa da
> controllare** — mentre dieci righe sopra era scritta la regola «chi produce non approva».
> Un difetto sistematico del produttore era invisibile al controllo per costruzione, perché il
> controllo era quel produttore.

I verbali li scrive lo script, non l'agente: così anche volendo, il giudice non può riscrivere
ciò che giudica.

**L'unica eccezione, ed è un campo non un ruolo:** il debrief è giudicato da `lan-gate` come tutti
gli altri, ma porta una **controfirma** della Regia. La Memoria giudica il lancio, la Regia
controfirma, e se non è d'accordo l'obiezione resta scritta accanto invece di essere negoziata
via. Nessuno dei due scrive da solo la storia di com'è andata.

---

## 6. IL MOTORE — la risposta a una domanda che aspettava da tre mesi

ADR-019 (2026-09-03, attivo) ha dichiarato canonico `orchestration-layer` e ha scritto:

> *«133 file che nessuno chiama non sono un motore: sono un progetto. Entro il primo lavoro
> reale di Digital Empire che ha bisogno di orchestrazione, il motore canonico deve servirlo
> davvero. […] Se quel lavoro arriva e viene fatto con un altro strumento, questo ADR va
> riaperto — e la domanda diventa un'altra: l'Impero ha davvero bisogno di un motore di
> orchestrazione, o ne ha costruiti sette perché era più divertente che pubblicare?»*

**Questo è quel lavoro**, e la v3 non nominava il motore canonico nemmeno una volta: proponeva
diciassette script nuovi, cioè l'ottavo motore dell'Impero, dopo sette con zero consumatori.

**Misurato il 2026-09-05**, aprendo il codice ed eseguendo i test: il motore canonico ha un tetto
rigido di sei attività per piano, un vocabolario di ruoli chiuso a cinque nomi, e **non sa
chiamare nessun modello**. Non rappresenta un flusso di lancio a tredici artefatti senza essere
prima riscritto.

**La conclusione non è «allora me ne scrivo un altro».** È più semplice, ed è la risposta che
ADR-019 chiedeva:

> **Questo lavoro non ha bisogno di un motore di orchestrazione.**
> Ha bisogno di una macchina a stati con dei controlli: leggere un file, validarlo contro uno
> schema, decidere se si passa, scrivere un verbale. Sono ~400 righe, non 133 file. Non c'è
> parallelismo da coordinare, non c'è un grafo di attività da pianificare: c'è una catena con
> delle attese umane lunghe giorni.

**Cosa comporta, e va deciso da Max (decisione 3 del documento 00):** questa misura è un dato per
ADR-019, non un aggiramento. O si registra che il primo lavoro reale non aveva bisogno di quel
motore — e allora la domanda del §4 di quell'ADR ha una risposta scritta — oppure si decide di
adattarlo comunque, sapendo che significa costruire il collante mancante **prima** di avere un
solo lancio servito, cioè ripetere l'errore che ADR-019 ha già misurato una volta.

**Quello che non si fa, in nessuno dei due casi: costruire un ottavo motore in silenzio.**

---

## 7. GLI ERRORI, LA CONCORRENZA, E COSA SUCCEDE QUANDO QUALCOSA MUORE

| Situazione | Comportamento |
|---|---|
| un agente muore a metà | l'artefatto parziale resta sul disco, marcato `incompleto`; `avanza` lo rigenera dalla fase, non dal principio |
| un file di artefatto è corrotto | codice 2, nessuna scrittura, il file corrotto viene rinominato `.rotto` e non cancellato |
| due `avanza` insieme | il secondo esce 1 dicendo chi ha il lock |
| il fornitore di pagamento non risponde | codice 3, il lancio non avanza, lo stato non cambia |
| il tetto di spesa è raggiunto | codice 3, lavoro salvato, si riprende dopo |
| un artefatto a monte cambia dopo che quelli a valle sono fatti | **tutti gli artefatti che dipendono da lui diventano `da_rivedere`** e i loro controlli si riaprono |

**L'ultima riga è la riparazione di un difetto sottile e grave:** nella v3 nessun artefatto era
versionato, quindi un cambio di prezzo non invalidava niente a valle — e il piano *prevedeva* che
le fondamenta nascessero prima del prezzo, quindi il fuori-ordine era la normalità, non
l'eccezione. Qui ogni artefatto porta `schema_version` e un'impronta dei propri ingressi.

---

## 8. OSSERVABILITÀ — come si sa che sta funzionando mentre gira

La v3 non aveva niente di tutto questo, e un sistema che si guarda solo alla fine si scopre rotto
alla fine.

| Cosa | Dove |
|---|---|
| ogni invocazione di agente | riga in `registro-chiamate.jsonl`: agente, modello, durata, costo, esito |
| ogni verdetto di controllo | verbale in `verbali/`, anche quando passa |
| lo stato di tutti i lanci | `lancio elenco` — una riga per lancio, con da quanti giorni è fermo e su cosa |
| il costo speso finora | `lancio costi <id>` — letto dal registro delle chiamate, mai stimato |
| **cosa blocca l'azienda adesso** | `lancio blocchi` — tutti i punti umani aperti, ordinati per giorni di attesa |

**`lancio blocchi` è il comando più importante del sistema**, e nella v3 non esisteva. È quello
che rende visibile il problema vero di questa azienda: non i lanci che vanno male, ma quelli che
non partono perché una decisione aspetta.

---

## 9. SICUREZZA E OBBLIGHI DI LEGGE — assenti dalla v3, e non sono opzionali

| Materia | Vincolo |
|---|---|
| **credenziali** | nessuna chiave nel repository. Al 2026-09-05 la chiave del servizio di posta è pubblica da mesi e mai sostituita: va cambiata **sul servizio**, perché la storia del repository resta leggibile |
| **dati dei clienti** | nomi e indirizzi degli acquirenti non entrano mai nel repository, in nessun artefatto |
| **diritto di recesso** | 14 giorni per i prodotti digitali venduti a consumatori in UE. Per il download immediato serve il consenso esplicito alla rinuncia, raccolto al checkout: è un campo obbligatorio dello schema dell'offerta |
| **fatturazione** | ogni vendita produce un documento fiscale. Se la cassa non lo emette, lo emette una persona, e il tempo per farlo è un costo del lancio |
| **consenso alla misura** | se il tracciamento parte solo dopo il consenso, i numeri sono sistematicamente più bassi del vero: la quota va dichiarata nel funnel, o ogni previsione tarata su quei numeri è sbagliata di una quantità nota e taciuta |
| **contenuti generati** | dove la legge lo impone, il contenuto prodotto da un modello va dichiarato come tale |

---

## 10. COSA STA FUORI — i confini, e chi possiede cosa

| Direzione | Con chi | Cosa passa |
|---|---|---|
| ⬅ | `02-INFO-BUSINESS` | il prodotto finito — **lo crea lui, non noi** |
| ⬅ | `04-MARKETING` | lo standard dei testi e la voce del marchio — **lo standard è suo** |
| ⬅ | `08-INTELLIGENCE` | i dossier sui concorrenti, con le fonti |
| ⬅ | **ULTIMO METRO** | l'elenco di ciò che è pronto e non è uscito: **è la coda in ingresso di questo ecosistema** |
| ➡ | `14-TESORERIA` | ricavi e costi reali — **lei è la fonte di verità sui soldi dell'azienda** |
| ➡ | `02-INFO-BUSINESS` | gli acquirenti, alla chiusura della vendita |
| ➡ | `10-MEMORY` | checkpoint, decisioni, debrief |
| ↔ | `07-FORGE` | agenti e skill da forgiare e registrare |

**La linea, in una riga:** se un'attività continua dopo la chiusura del carrello, non è di questo
ecosistema.

**E il rapporto col denaro, che va detto esplicitamente:** ogni euro nasce qui e **sale** in
Tesoreria; non scende mai. Se un numero compare in tutti e due i posti ed è diverso, **ha ragione
la Tesoreria**, e la divergenza è un difetto da registrare.
