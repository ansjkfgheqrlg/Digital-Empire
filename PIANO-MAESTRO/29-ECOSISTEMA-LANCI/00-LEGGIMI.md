---
Type: PROJECT
Status: Proposta — versione 4, in attesa di ok Max
Tags: #lanci #ecosistema-15 #architettura #TASK-LANCI-ECO-W2 #piano-di-costruzione
Created: 2026-09-05
Last updated: 2026-09-05
Versione: 4 (la 3 è archiviata in `_v3-superata/`, non cancellata)
Autore: Max (via Emperator) · Esecutore della costruzione: Gael
---

# 🚀 ECOSISTEMA LANCI — PIANO DI COSTRUZIONE, VERSIONE 4

> **Questo è il documento da cui si comincia.** Gli altri si consultano, non si studiano.
> La versione 3 è stata smontata da quattro revisori indipendenti: **oltre cinquanta difetti
> sostanziali, dodici fatali**. Il §8 dice quali, e cosa è cambiato di conseguenza.

---

# 1. IL PROBLEMA, IN NUMERI MISURATI OGGI

Non è teoria e non è la diagnosi della versione precedente: sono misure fatte il 2026-09-05,
con il comando o il file accanto.

| Fatto | Misura | Dove l'ho verificato |
|---|---|---|
| Il prodotto pilota esiste davvero | **203 pagine**, verificate dentro il file | il PDF sul disco |
| È fermo da | **dal 07/03/2026** — sei mesi | catalogo prodotti, campo Status: "Pronto" |
| Il suo prezzo | **quattro valori diversi**, in quattro fonti, mai messi sullo stesso tavolo | catalogo · wiki · listino · piano v3 |
| **Il canale che doveva portargli pubblico** | **spento il 29/07/2026** e dirottato su un altro progetto | `second-brain-vault/wiki/log.md:1054-1063` |
| **Modo automatico di incassare un euro** | **non esiste** | nessun bottone d'acquisto collegato a nessuna cassa |
| **Misura di quanto entra** | **non esiste** | nessun tracciamento installato |
| **Pagine di vendita del prodotto** | **non sono online** | verificato |
| Un piano di lancio per questo prodotto | **esisteva già**, con obiettivo 30/05/2026 | wiki, progetto del 29/04/2026 |
| Quel piano | **è morto in silenzio**, tre mesi fa, senza che nessun documento lo registri | — |
| Il reparto Lanci che esiste | 19 file, 2.377 righe, **0 eseguibili, 0 agenti invocabili** | ricognizione L1 di Gael |
| Le skill utili già installate | **11 su 11 funzionanti** | verificate una per una |

## La diagnosi, corretta rispetto alla versione precedente

La versione 3 diceva: *«non c'è un buco di capacità, c'è un buco di decisione ed esecuzione»*.
**È giusto ma incompleto, e l'incompletezza è costata l'intero dimensionamento del piano.**

C'è un terzo buco, ed è sotto gli altri due: **manca l'infrastruttura per incassare.**
Oggi Digital Empire può, al massimo, ricevere un ordine per email e consegnarlo a mano.
Non c'è cassa, non c'è misura, non ci sono pagine online, e non si sa quante persone ci
sono nella lista.

Il piano precedente progettava **dodici reparti e cinquanta agenti sopra un'azienda che non
può ricevere un pagamento.** Non è un dettaglio di priorità: è come costruire il traffico
aereo prima della pista.

> **Il problema, in una riga:** il Manuale non è fermo perché manchi un'organizzazione.
> È fermo perché manca **un prezzo, un pubblico e una cassa** — e di questi tre, due non
> erano nemmeno nominati nel piano che avrebbe dovuto sbloccarlo.

---

# 2. LA TESI DELLA VERSIONE 4

## 2.1 Il mandato non lo inventiamo: è già scritto

ADR-016 (*L'Ultimo Metro*, 2026-09-03) ha misurato che l'azienda ha **25 pezzi finiti mai
usciti, 2.137 MB fermi, il più vecchio da 135 giorni, zero vendite documentate**. E si chiude
dichiarando il buco che resta aperto:

> *«Non esiste una misura di cosa succede DOPO la pubblicazione. L'Ultimo Metro chiude il buco
> fra "prodotto" e "pubblicato"; **resta aperto quello fra "pubblicato" e "venduto".
> È il prossimo da chiudere.»***

**Quello è questo ecosistema**, ed era già registrato due giorni prima che il piano v3 nascesse.
Il v3 non lo cita mai: si presentava come un organigramma invece che come l'anello mancante di
una catena che esiste già.

```
  Memory (ADR-002)        interno: nessun lavoro è fatto finché non è salvato
  Ultimo Metro (ADR-016)  prodotto ────────────► pubblicato
  LANCI  ←── noi          pubblicato ──────────► venduto ──► misurato
  Tesoreria (ADR-020)     l'euro nei conti dell'azienda
```

Un ecosistema che sa qual è l'anello prima e quale dopo è architettura. Un elenco di dodici
reparti è una lista.

## 2.2 Il centro non è l'organigramma: è la catena degli artefatti

**Questo è il cambiamento che rende la versione 4 diversa da tutte le precedenti.**

Nel v3 il sistema era definito da *chi fa cosa* — dodici reparti, quarantuno agenti, sei livelli
di comando. Il risultato, misurato dai revisori: sei sigle di reparto usate in un documento e
inesistenti nell'altro, sette nomi di controllo contro tre ufficiali senza mappa, una correzione
applicata nel documento di governo e mai arrivata in quello che si esegue.

**Nessuno di quei difetti è un errore di ragionamento. Sono tutti errori di copia** — e sono
inevitabili quando la stessa informazione vive scritta a mano in undici posti.

Nella versione 4 il sistema è definito da **cosa deve esistere e chi lo certifica**:

| | v3 | **v4** |
|---|---|---|
| Unità di base | il reparto | **l'artefatto** |
| Definito in | undici documenti di prosa | **un file dati, `dati/registro.yaml`** |
| Coerenza garantita da | attenzione umana | **un programma: `dati/valida_registro.py`** |
| «Chi produce non approva» è | una frase scritta e violata cinque volte su sette | **l'invariante INV-01, verificato a ogni build** |
| Schemi dei file prodotti | 4 su 13 | **13 su 13, versionati** |
| Contenuto eseguibile | **zero** | il validatore, che gira e ha già bocciato un errore mio |

Il registro contiene tredici artefatti, quattordici controlli, quindici agenti, dodici stati,
diciassette transizioni, sei punti umani e **dieci invarianti**. Il comando che lo verifica:

```bash
cd PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati
PYTHONIOENCODING=utf-8 python valida_registro.py
# 253 controlli eseguiti → PIANO COERENTE
```

**Se esce diverso da zero, il piano è incoerente e non si costruisce.** Non è una
raccomandazione: è la stessa disciplina che il piano pretende dai lanci, applicata al piano.

> **La prova che lo strumento serve:** al primo giro il validatore ha bocciato **me**. Avevo
> dato all'agente che giudica il debrief il permesso di scrivere — violando l'invariante che
> avevo scritto un'ora prima. È in `registro.yaml`, campo `nota_controfirma`, lasciato lì
> apposta.

## 2.3 I tre artefatti che prima non esistevano

| Artefatto | Perché è nuovo |
|---|---|
| **`pubblico.json`** | Il v3 progettava il lancio di un prodotto **il cui canale di traffico era spento da cinque settimane**, e nessuno dei suoi 11 dossier lo sapeva. Adesso il primo controllo di tutti chiede: quante persone possiamo mettere davanti all'offerta, e con quale prova? |
| **`previsione.json`** | In 3.718 righe il v3 non conteneva **mai** la domanda «quanto ci aspettiamo di incassare». Senza, la firma del prezzo è cieca, il controllo del budget è insoddisfacibile (chiedeva un pareggio che nessuno produceva), e il debrief non ha niente da confrontare. |
| **`consuntivo.json`** | Era un testo (`consuntivo.md`). Un testo non si confronta con una previsione: senza confronto non c'è scarto, e senza scarto non si impara niente. |

Insieme chiudono **B-043** — *«Digital Empire non misura un solo euro»*.

---

# 3. IL PRIMO GIORNO — è cambiato, ed è il cambiamento più importante

> Il v3 cominciava con *«crea la cartella dell'ecosistema»*. La versione 4 comincia con
> **«incassa un euro vero e restituiscilo»**.

**La ragione, in una riga:** finché non esiste una cassa, dodici reparti sopra un'azienda che
non può ricevere un pagamento sono dodici reparti inutili — e ci si accorge della cassa mancante
il giorno dell'apertura, dopo aver speso tutto il resto.

## 3.1 Il giorno zero: la catena dell'incasso — 6-10 ore

Nessun agente, nessun reparto, nessuna cartella di ecosistema. Solo quattro cose che o
funzionano o non funzionano.

| # | Gesto | Come si sa che è andato |
|---|---|---|
| 0 | **Sostituire la chiave del servizio di posta**, esposta pubblicamente da mesi | la vecchia chiave non funziona più sul servizio (B-020) |
| 1 | Collegare una cassa a una pagina qualunque | esiste un indirizzo dove si può pagare |
| 2 | **Pagare davvero, con una carta vera** | la transazione compare nel pannello del fornitore |
| 3 | **Farsi arrivare il prodotto** | il file arriva a chi ha pagato, senza intervento umano |
| 4 | **Rimborsare quel pagamento** | il rimborso compare nel pannello |
| 5 | Installare la misura e vedere l'evento di acquisto | l'evento compare nello strumento di misura |

**Criterio di chiusura del giorno zero, uno solo:**

> Un euro è entrato, il prodotto è arrivato, l'euro è tornato indietro, e tutti e tre i fatti
> sono leggibili in un pannello — non dichiarati da nessuno.

**Se questo non succede, non si costruisce nient'altro.** Non è una raccomandazione morale: è
la condizione di uscita numero uno del §7.

## 3.2 Il giorno uno: contare il pubblico — 2-4 ore

Prima di qualsiasi cartella e di qualsiasi agente, si compila **`pubblico.json`** a mano,
seguendo `dati/schemi/pubblico.schema.json`.

Un canale senza prova vale **zero**. È legittimo scrivere che non si sa; non è legittimo
contare ciò che non si sa.

**Criterio:** il totale verificato è un numero, e quel numero è entrato in un file.
Se il totale è zero, **il lancio non parte e il problema dell'azienda non è organizzativo** —
ed è l'informazione più preziosa che si possa comprare con quattro ore di lavoro.

## 3.3 Il giorno due: la previsione, e la firma — 3-5 ore + il tempo di una firma

Con il pubblico contato e il prodotto pronto, si compila **`previsione.json`** (la formula sta
nello schema, si rifà a mano su un foglio) e si porta a Max **una proposta di prezzo che dice il
ricavo atteso**, non solo il numero.

> *«47 € su un pubblico verificato di N, con una conversione del 2%, fa X euro.
> 27 € fa Y. 97 € fa Z. Confermi 47?»*

**Questo è il punto per cui l'intero ecosistema esiste**, e nel v3 arrivava dopo 54-72 ore-uomo
di infrastruttura. Qui arriva al terzo giorno, e i tre giorni sono tutti spesi su cose che
servono al lancio, non al sistema.

## 3.4 Solo dopo: l'ecosistema

La cartella `company/Ecosistemi/15-LANCI/`, gli script, gli agenti — tutto ciò che il v3
metteva al primo giorno — comincia **dopo** che un lancio vero è passato per le tre fasi qui
sopra, e ha lasciato dietro di sé i difetti misurati che dicono **quale** pezzo di sistema
serve davvero.

Il §6 dice come.

---

# 4. LE DECISIONI CHE ASPETTANO MAX

Sono **quattro**, e la prima blocca tutto il resto.

| # | Decisione | Dove sono gli elementi | Costo dell'attesa |
|---|---|---|---|
| **1** | **Il Manuale si vende o è un regalo?** | `03-FLUSSO-OFFERTA.md` §3 — le due strade con le conseguenze, e quale è reversibile | **sei mesi finora.** Adesso ha una scadenza di 7 giorni e un default reversibile: se non arriva risposta si procede con "vendita" e si può tornare indietro |
| 2 | Approvare l'**ADR-023** | `05-ADR-023.md`, pronto da copiare | senza, la cartella dell'ecosistema non può nascere: lo impone ADR-009 |
| 3 | Riaprire o no **ADR-019** | `01-ARCHITETTURA.md` §6 | nessuno: la risposta è già misurata, serve solo che sia registrata |
| 4 | Sostituire la chiave di posta esposta | §3.1 gesto 0 | **cresce ogni giorno**: è pubblica dal repository, e la storia resta leggibile anche dopo |

**La 1 e la 4 si possono chiudere oggi in dieci minuti.** Le altre due sono formalità che
seguono.

---

# 5. LA MAPPA DEL PACCHETTO

| # | Documento | Cosa contiene | Quando lo apri |
|---|---|---|---|
| **00** | *questo* | problema, tesi, primo giorno, decisioni, quando si smette | adesso |
| 01 | `01-ARCHITETTURA.md` | la macchina: artefatti, stati, controlli, errori, concorrenza, il ponte verso gli agenti, il motore | prima di costruire |
| 02 | `02-PREVISIONE-E-DENARO.md` | il modello del ricavo, il costo di far girare il sistema, il pareggio, gli obblighi di legge | scaglione 1 |
| 03 | `03-FLUSSO-OFFERTA.md` | il cuore: prezzo e data istruiti fino alla firma, riscritto dopo la demolizione | scaglione 1 |
| 04 | `04-COSTRUZIONE.md` | ordine, ore, criteri di sblocco eseguibili, pre-mortem, condizioni di abbandono | prima di cominciare |
| 05 | `05-ADR-023.md` | la decisione da registrare, pronta | **passo zero** |
| 06 | `06-CRITICA-E-GIRI.md` | i difetti trovati nella v3, uno per uno, e cosa è cambiato | quando una scelta sembra strana |
| **dati/** | `registro.yaml` · `valida_registro.py` · `schemi/*.json` | **la fonte di verità** | sempre |

**Regola che nasce dal difetto peggiore della v3:** se un documento dice una cosa diversa dal
registro, **ha torto il documento**. I documenti spiegano; il registro decide.

---

# 6. IL GLOSSARIO

| Parola | Cosa vuol dire qui |
|---|---|
| **Artefatto** | un file che afferma qualcosa di verificabile. È l'unità del sistema |
| **Controllo (gate)** | qualcosa che può bloccare davvero. Se non può bloccare, non è un controllo |
| **Verbale** | il file che un controllo scrive **sempre**, anche quando lascia passare |
| **Invariante** | una cosa che deve essere sempre vera, e che un programma verifica |
| **Punto umano** | una decisione che nessuna macchina può prendere. Ha sempre una scadenza e un comportamento allo scadere |
| **Default per silenzio** | quando un punto umano scade e la scelta è reversibile, si procede e **si dichiara** |
| **Misurato / assunto** | i due stati di ogni numero. Un numero assunto **non può essere prova** per un controllo |
| **Irreversibile verso l'esterno** | un'email spedita, un pagamento, una pagina pubblicata. **Lo fa sempre una persona** |
| **Avvolgere** | usare una capacità che esiste già tramite un contratto, invece di riscriverla |

Le sigle di reparto e di agente **non stanno qui**: stanno nel registro, e chi ne inventa una
fuori da quell'elenco fa fallire il validatore. È il rimedio al difetto per cui il documento
operativo della v3 non era installabile sopra quello di governo.

---

# 7. QUANDO SI SMETTE

> Un piano senza condizione di uscita è una scommessa senza limite di perdita. Le tre della v3
> erano buone; queste sono quattro, e la prima è nuova ed è la più importante.

| # | Se accade | Allora |
|---|---|---|
| **1** | **Il giorno zero non si chiude in 16 ore-uomo** — cioè non si riesce a incassare, consegnare e rimborsare un euro | **si ferma tutto.** Il problema dell'azienda non è organizzativo: è che non ha una cassa. Nessun reparto la costruisce |
| **2** | `pubblico.json` esce con **totale verificato pari a zero** | **si ferma il lancio** e si va a costruire pubblico. Un'offerta senza nessuno davanti non è un lancio: è un documento |
| **3** | Il lancio pilota non esce **entro 45 giorni** dal giorno zero | si ferma la costruzione e si guarda la causa. Se il blocco è una firma che non arriva, nessun reparto in più la farà arrivare |
| **4** | Dopo **due lanci** nessuno schema ha cambiato una decisione | la memoria si dichiara fallita e si smette di mantenerla, invece di riempirla per abitudine |

**Fermarsi alla 1 o alla 2 non sarebbe un fallimento.** Sarebbe la scoperta, pagata in due
giorni invece che in tre mesi, che il collo di bottiglia era altrove — ed è un'informazione che
oggi non abbiamo e che vale più di dodici reparti costruiti bene e mai usati.

---

# 8. COSA È CAMBIATO DALLA VERSIONE 3 — in breve

Il dettaglio, difetto per difetto, sta in `06-CRITICA-E-GIRI.md`. Qui le dodici cose che
contano.

| # | Cambiamento | Contro quale difetto misurato |
|---|---|---|
| 1 | **La fonte di verità è un file dati validato da un programma** | sigle divergenti fra documenti, correzioni non propagate, sette nomi di controllo contro tre |
| 2 | **Nasce `pubblico.json` e viene prima di tutto** | il piano lanciava un prodotto col canale di traffico spento da cinque settimane, e non lo sapeva |
| 3 | **Nasce `previsione.json`** | mai, in 3.718 righe, la domanda «quanto ci aspettiamo di incassare» |
| 4 | **Il primo giorno è la catena dell'incasso, non la cartella** | l'azienda non può incassare un euro, e il piano non lo nominava |
| 5 | **La firma è un oggetto con canale chiuso e impronta del testo** | `firmato_da` era una stringa: un agente in ciclo di riparazione poteva scrivere "Max" e far partire un lancio a un prezzo mai approvato |
| 6 | **Il cronometro sta su ogni punto umano aperto, non sulla firma del prezzo** | il Manuale si ferma su una domanda precedente, e lì non c'era né scadenza né default: la proposta non nasceva mai e l'orologio non partiva |
| 7 | **Percorso retroattivo per i prodotti già finiti** | il flusso usciva con errore alla prima riga proprio sul prodotto per cui era stato costruito |
| 8 | **Ogni controllo ha un ramo di fallimento e un test che lo fa fallire** | nessuno dei controlli diceva cosa succede quando boccia |
| 9 | **Il giudice non ha il permesso di scrivere** | cinque controlli su sette erano eseguiti dallo stesso agente che produceva la cosa giudicata |
| 10 | **Il valore dei bonus richiede una fonte** | il rapporto valore/prezzo si raggiungeva inventando un bonus: il controllo istruiva a gonfiare |
| 11 | **Il costo di far girare il sistema è una voce obbligatoria, con un tetto** | 41 agenti e nessuna riga sul costo, in un'azienda con un direttore finanziario |
| 12 | **Il ponte verso gli agenti è specificato, ereditando ADR-014** | tutto il piano poggiava su agenti orchestrati da programmi, e non diceva mai come si invoca un agente da un programma |

---

## Connessioni

- `dati/registro.yaml` — **la fonte di verità**
- `_v3-superata/` — la versione 3 integrale, archiviata e non cancellata
- [[RICOGNIZIONE-LANCI]] · [[ASSORBIMENTO-LANCI]] — L1 e L2, il lavoro di Gael: restano la base
- `company/Memory/decisions/ADR-016-ultimo-metro.md` — il mandato
- `company/Memory/decisions/ADR-014-il-codice-torna-a-chiamare-un-modello.md` — il ponte
- `company/Memory/decisions/ADR-019-motore-orchestrazione-canonico.md` — il motore
- `company/Ecosistemi/REGISTRO-NUMERI.md` — dove il 15 è riservato
