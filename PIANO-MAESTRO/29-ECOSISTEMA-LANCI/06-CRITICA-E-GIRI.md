---
Type: PROJECT
Status: Proposta — versione 4, in attesa di ok Max
Tags: #lanci #ecosistema-15 #critica #TASK-LANCI-ECO-W2 #piano-di-costruzione
Created: 2026-09-05
Last updated: 2026-09-05
Versione: 4 (la 3 è archiviata in `_v3-superata/`, non cancellata)
Autore: Max (via Emperator) · Esecutore della costruzione: Gael
---

# 06 — LA CRITICA ALLA VERSIONE 3, E COSA È CAMBIATO

> **Quando si apre questo documento:** quando una scelta della versione 4 sembra strana, o
> costosa, o eccessiva. Ogni scelta strana è la cicatrice di un difetto misurato, e qui c'è il
> difetto con il suo numero di riga.
>
> Il §8 di `00-LEGGIMI.md` dice **le dodici cose che contano, in breve**. Questo documento è il
> dettaglio di quella tabella e non la contraddice: la §7 qui sotto lega ogni difetto alla riga
> del §8 che lo chiude. Dove un documento diverge da `dati/registro.yaml`, ha torto il documento.

---

# 1. COME È STATA FATTA LA CRITICA

## 1.1 Chi ha letto cosa

La versione 3 era un pacchetto di **undici documenti, 3.718 righe** (misura citata in
`_critica-v3/CRITICA-EMPERATOR.md`, §B). È stata smontata da **quattro revisori indipendenti**,
ognuno su un blocco di documenti disgiunto, senza vedere il rapporto degli altri. A questi si
aggiungono la lettura diretta di chi ha scritto il piano e quattro indagini sul campo, che non
leggevano documenti ma misuravano la macchina e il disco.

| Rapporto | Cosa ha letto | Rilievi negativi con sigla | Cose giudicate solide |
|---|---|---:|---:|
| `CRITICA-A.md` | dossier 01, 02, 03 | **106** (30 difetti · 30 buchi · 24 contraddizioni · 22 punti di prosa) | 16 |
| `CRITICA-B.md` | dossier 04, 05, 06 | **56** (22 difetti · 12 buchi · 12 contraddizioni · 10 punti di prosa) | 14 |
| `CRITICA-C.md` | dossier 07, 08, 09, 10 | **14** difetti strutturali, più due verdetti motivati (agenti, stima) | — |
| `CRITICA-D.md` | secondo passaggio su 07, 08, 10 | **12** (6 difetti · 6 buchi) | 7 |
| `CRITICA-EMPERATOR.md` | dossier 00, 01, 04, 09, con gli ADR alla mano | **13** | 9 |
| **Totale** | | **201 rilievi numerati** | **46** |

Le quattro indagini sul campo, che non sono critiche ma misure:

| Indagine | Domanda a cui risponde | Risposta in una riga |
|---|---|---|
| `ORIGINE.md` | cosa era stato chiesto davvero | tredici vincoli espliciti di Max, V-01…V-13, ricavati dalla task madre riga per riga |
| `INCASSO.md` | l'azienda può incassare un euro? | no: solo un ordine per email, chiuso a mano |
| `PONTE-AGENTI.md` | uno script può far lavorare un agente? | il meccanismo esiste ed è installato, nessuno script dell'azienda lo usa |
| `MOTORE.md` | il motore di orchestrazione dell'Impero regge un lancio? | non così com'è: tetto di sei attività per piano, ruoli chiusi a cinque nomi, non chiama nessun modello |

## 1.2 La regola del metodo

**Ogni rilievo cita il numero di riga. Un rilievo senza riferimento non vale.**
La convenzione usata da tutti i rapporti è `dossier:riga` — per esempio `03:166` è la riga 166 di
`03-WF-PRODOTTO.md`. È la ragione per cui questo documento può ancora, oggi, dire *dove* stava
ogni difetto invece di ricordarsene.

Regola aggiunta durante il lavoro, dopo aver trovato due tabelle dei cambiamenti che dichiaravano
correzioni non presenti nel corpo: **una riga che dichiara una correzione vale solo se la
correzione è nel testo** (`CRITICA-A.md` S-A-15). Un elenco di correzioni che asserisce il falso
disarma il revisore successivo più di quanto lo aiuti.

## 1.3 Di questi, quanti sono fatali

**Dodici**, ed è il numero che compare in `00-LEGGIMI.md` (riquadro d'apertura). Fatale qui ha un
significato stretto e verificabile:

> Un difetto è **fatale** se, costruendo il sistema esattamente come scritto, il primo lancio
> reale non arriva alla fine — o ci arriva certificando qualcosa di falso.

Non è una scala di fastidio. Sono i dodici casi in cui un revisore ha potuto mostrare il punto
esatto in cui la macchina si ferma, o passa quando non dovrebbe. Stanno tutti nella §2.

## 1.4 I limiti di questa critica — dichiarati, non attenuati

1. **È stata fatta su documenti, non su codice funzionante, perché la versione 3 non aveva
   contenuto eseguibile.** Nessun revisore ha potuto far girare niente: si è potuto solo
   dimostrare che una specifica è contraddittoria, non che un programma sbaglia. Il limite è
   simmetrico al difetto che denuncia — il reparto Lanci esistente ha 19 file, 2.377 righe e zero
   eseguibili (`RICOGNIZIONE-LANCI.md`) — ed è la ragione per cui la versione 4 consegna un
   validatore che gira.
2. **Quattro revisori su blocchi disgiunti non vedono i difetti di raccordo.** Il difetto D-C-08
   — il documento che si esegue fermo a una versione precedente di quello che governa — è emerso
   solo perché un revisore ha aperto un dossier fuori dal proprio blocco per una verifica
   incrociata. Quel tipo di difetto è invisibile leggendo un documento alla volta: è il rilievo di
   metodo scritto in fondo a `CRITICA-C.md` D-C-08.
3. **`CRITICA-C.md` è incompleta.** Il rapporto dichiara di sé: «sezioni 1-3 complete, 4-8 in
   lavorazione». Le sue sezioni su buchi, contraddizioni e prosa non esistono. Quello che c'è è
   stato usato; quello che manca non è stato inventato.
4. **Le affermazioni di fatto su un repository invecchiano in poche ore.** `CRITICA-D.md` §5 ha
   trovato due affermazioni della versione 3 già false il giorno stesso: il numero 15 risultava
   già riservato in `REGISTRO-NUMERI.md`, e `python -m empire conform` usciva con **un** blocco,
   non due. Non è una colpa del piano: è la ragione per cui le misure di questo pacchetto portano
   la data e il comando accanto.
5. **Nessun rapporto ha eseguito una chiamata reale a un modello o a un fornitore di pagamento.**
   `PONTE-AGENTI.md` §6 dichiara di non aver eseguito un vero `claude -p --agent` per non
   consumare crediti senza autorizzazione; `INCASSO.md` §8 dichiara di non aver interrogato Brevo
   né Stripe per non esporre credenziali. Le due cose più costose del sistema sono state
   verificate come **capacità presenti**, non come **capacità provate**.

---

# 2. I DIFETTI FATALI — quelli che avrebbero fermato la costruzione

Dodici, ordinati dal più grave. L'ordine è **quanto lontano si sarebbe arrivati prima di
scoprirli**: i primi si scoprono il giorno dell'apertura della vendita, dopo aver speso tutto; gli
ultimi durante la costruzione, che costa meno.

---

## F-01 · L'azienda non può incassare un euro, e nessuno degli undici documenti lo nomina

**Il difetto.** Il piano progettava dodici reparti e cinquanta agenti sopra un'azienda che non ha
una cassa: nessun bottone d'acquisto collegato a un fornitore di pagamento, nessuna consegna
automatica, nessuna misura installata.

**Dove.** Non è una riga sbagliata: è un'assenza. La misura sta in `_critica-v3/INCASSO.md` §1 e
§7 — `Crea siti\Siti CCM\checkout.config.json` righe 7-33 ha tutti i canali di pagamento
(`stripe_base`, `stripe_bump`, `paypal_me`, `bonifico`) a `"attivo": false`; l'unico attivo è
`ordine_email`, un indirizzo di posta personale. `pagamento.html` righe 190, 197, 375: il
passaggio d'acquisto è un collegamento `mailto:`. `company\Memory\tesoreria\entrate.jsonl` e
`spese.jsonl`: **zero righe** entrambi. Nessun tracciamento su nessun sito verificato
(`INCASSO.md` §4). Nel piano v3 l'unica riga che tocca l'argomento è `06:115` (controllo 8,
transazione reale), e sta **dopo** un passo dichiarato irreversibile a `06:76` — rilevato come
D-B-18 in `CRITICA-B.md`.

**Il caso concreto che lo fa cadere.** Si costruiscono S0 e S1 come scritti — 54-72 ore-uomo
(`CRITICA-EMPERATOR.md` E-04). Si arriva al giorno dell'apertura. Il visitatore preme il bottone
d'acquisto e gli si apre il programma di posta.

**Perché è fatale.** È il momento in cui l'intero investimento diventa inutile e non c'è nessuna
riparazione rapida: costruire una cassa non è compito di un reparto Lanci, e nessuno dei dodici
reparti proposti la costruiva. Il piano ordinava il traffico aereo prima della pista.

**Cosa fa la versione 4.** Il primo giorno non è più «crea la cartella»: è **la catena
dell'incasso** (`00-LEGGIMI.md` §3.1), sei gesti che o funzionano o non funzionano, con criterio
di chiusura unico — *un euro è entrato, il prodotto è arrivato, l'euro è tornato indietro, e tutti
e tre i fatti sono leggibili in un pannello*. Nel registro la prova di cassa è dentro
`GATE-FNL-1`, **prima** della pubblicazione irreversibile: criterio
`prova_cassa.stato=='incassato_e_rimborsato' AND prova_cassa.riferimento_transazione != null`,
dato letto dal fornitore di pagamento e non dichiarato dall'agente, con test rosso *«un funnel con
tutte le pagine a 200 ma senza transazione di prova deve BLOCCARE»* (`registro.yaml`, gate
`GATE-FNL-1`; nota `ART-FNL.nota_cassa`). Ed è la **condizione di uscita numero 1**: se il giorno
zero non si chiude in 16 ore-uomo, si ferma tutto (`00-LEGGIMI.md` §7).

---

## F-02 · Il canale che doveva portare pubblico al prodotto pilota era spento da cinque settimane

**Il difetto.** Il piano dimensionava tutto — reparti, scaglioni, ore — sull'affermazione che al
Manuale Claude Code manchino «solo prezzo e data». Al Manuale mancava anche il pubblico.

**Dove.** `CRITICA-EMPERATOR.md` E-10, che risale alla fonte primaria:
`second-brain-vault/wiki/log.md` righe 1054-1063, del 2026-07-29/31, testuale — *«il primo
contenuto YouTube reale generato era ancora sul funnel morto "Manuale Claude Code" — pivot deciso
da Gael a @dosementale»*, e *«`apex7_orchestrator.py` (F1-F5) riscritto per intero su
@dosementale»*. Non è una decisione a parole: è nel codice. Nessuno degli undici dossier della v3,
né `RICOGNIZIONE-LANCI.md`, né `ASSORBIMENTO-LANCI.md`, né il checkpoint CP-20260905-015 lo
nomina (verifica in `ORIGINE.md` §5, righe 244-247).

**Il caso concreto che lo fa cadere.** Il dossier 09 sceglie i quattro reparti dello scaglione
minimo *«perché sono esattamente ciò che manca al Manuale: tutto il resto quel prodotto ce l'ha
già»*. Il prodotto non ha più il motore di traffico. Con l'ordine della v3, l'azienda se ne
accorge il giorno dell'apertura del carrello, dopo 54-72 ore-uomo di costruzione.

**Perché è fatale.** Un'offerta senza nessuno davanti non è un lancio: è un documento. E il costo
della scoperta è tutto il piano, perché arriva alla fine.

**Cosa fa la versione 4.** Nasce `ART-PUB` / `pubblico.json`, ed è il **primo** artefatto della
catena: `dipende_da: []`, nessuno lo precede. Afferma *«quante persone possiamo mettere davanti
all'offerta il giorno dell'apertura, per canale, con la prova di ognuna»*. `GATE-PUB-1` chiede
`somma(canali[].raggiungibili_verificati) > 0` e per ogni canale una prova fra esporto di lista,
schermata di conteggio o misura, non più vecchia di 30 giorni; il conteggio si legge dalla
piattaforma, non lo dichiara l'agente. Test rosso: *«un pubblico.json con 3 canali tutti a
raggiungibili_verificati=0 deve BLOCCARE»*. Lo schema `pubblico.schema.json` porta un campo di
stato del canale con il valore `dirottato`, descritto nel file come *«il campo che sarebbe servito
a luglio»*, e distingue il pubblico posseduto da quello in affitto. È anche la **condizione di
uscita numero 2** (`00-LEGGIMI.md` §7): totale verificato a zero, il lancio si ferma e si va a
costruire pubblico.

---

## F-03 · Il reparto costruito per sbloccare il Manuale era, il primo giorno, inaccessibile al Manuale

**Il difetto.** Il flusso Offerta ammetteva solo prodotti usciti dal flusso Prodotto. Il prodotto
per cui l'ecosistema esiste non ci è mai passato.

**Dove.** `CRITICA-B.md` §1 (la simulazione riga per riga) e D-B-05. Le righe: `04:85` — *«esce 2:
non si prezza un prodotto non certificato»*, ribadito a `04:312`, con l'ingresso definito a
`04:54`.

**Il caso concreto che lo fa cadere.** Giorno 0. Si esegue il comando dell'offerta sul Manuale.
Primo campo dell'ingresso: `certificato_path`. Il Manuale è finito dal 07/03/2026 e non è mai
passato da un flusso di produzione: non ha un certificato. **Codice di uscita 2 alla prima riga di
ingresso.** Lo stesso vale per tutto l'inventario reale dell'azienda: una pagina d'ingresso già online
(`06:212`), 25 contenuti già prodotti (`06:248-249`).

**Perché è fatale.** Il flusso motivante non supera il proprio controllo d'ingresso. Per prezzare
il Manuale bisognerebbe prima farlo certificare come se fosse nuovo, e il costo di quel giro non è
stimato in nessuno dei dossier — mentre sta sul percorso critico del lancio che il piano esiste
per sbloccare.

**Cosa fa la versione 4.** `ART-CRT` dichiara `modalita_ammesse: ["integrale", "retroattiva"]`, e
la nota nel registro dice perché: *«il revisore ha dimostrato che il flusso usciva con codice 2
alla prima riga di input»*. `GATE-PRD-1` accetta la modalità retroattiva solo se il debito di
collaudo è dichiarato: `(modalita=='integrale' OR (modalita=='retroattiva' AND debito_collaudo
dichiarato))`. Lo schema lo rende obbligatorio per costruzione: `certificato.schema.json` righe 53
e 63 impongono `debito_collaudo` con lunghezza minima quando la modalità è retroattiva. Il debito
non è una promessa in prosa: è un campo che il controllo legge.

---

## F-04 · Il punto su cui l'azienda è ferma da sei mesi era l'unico senza scadenza, e la metrica non lo vedeva

**Il difetto.** Il cronometro dell'inerzia stava sulla firma del prezzo. Il Manuale non si ferma
lì: si ferma una fase prima, sulla domanda «questo prodotto si vende o è un regalo?» — e quel
punto non aveva né scadenza, né valore predefinito, né sospensione.

**Dove.** `CRITICA-B.md` D-B-01 e §1. Le righe: `04:97` (la fase O1), `04:117` (*«produce questo,
e poi si ferma»*), `04:315` (*«è l'unico caso in cui questo workflow si ferma prima ancora di
proporre un numero»*), `04:296` (la funzione dell'inerzia, documentata come *«da quanto **la
proposta** aspetta»*). Contro `05:286-294`, la tabella dei sei punti umani con scadenza, che **non
contiene O1**, e contro `05:296-297`, dove la regola giusta è già scritta: *«un'attesa senza
scadenza non è un punto di controllo: è un punto di morte»*.

**Il caso concreto che lo fa cadere.** Giorno 3: niente. La funzione dell'inerzia conta da quando
la proposta aspetta, e in quel ramo la proposta non nasce mai: **l'orologio non parte**. Giorno 7:
nessuna voce di blocco. Giorno 14: nessuna sospensione. Giorno 180: il lancio è fermo esattamente
come oggi, con in più un file `offerta/01-ruolo.md`.

**Perché è fatale.** Il fallimento è invisibile alla sua stessa misura. La metrica regina del
dossier — *«giorni fra ISTRUITO e la firma ≤3, oggi 180»* (`04:323`) — se la firma non arriva mai
non produce un numero alto: **non produce nessun numero**. Il reparto documenta il blocco invece
di scioglierlo.

**Cosa fa la versione 4.** Il cronometro passa dalla firma a **ogni punto umano aperto**. Nel
registro, `punti_umani` è una sezione con sei voci, e la prima è `PU-RUOLO`: scadenza 7 giorni,
valore predefinito `vendita`, con la giustificazione scritta accanto — *«fra due strade, quando
scade il tempo, si prende quella da cui si torna indietro»*, perché un prodotto venduto può
diventare un regalo e un prodotto regalato non si rimette in vendita senza bruciare chi l'ha avuto
gratis. Allo scadere si procede e **si dichiara**: `offerta.schema.json` ha il campo
`ruolo_scelto_per_silenzio`, e il valore `non-deciso` non è ammesso in un file valido. `INV-06`
verifica che ogni punto umano abbia una scadenza oppure una motivazione esplicita per non averla.
E `lancio blocchi` (`01-ARCHITETTURA.md` §8) elenca tutti i punti umani aperti ordinati per giorni
di attesa: nella v3 quel comando non esisteva.

---

## F-05 · La correzione principale era scritta in un dossier e non nell'altro, e il piano di costruzione si mordeva la coda

**Il difetto.** Undici documenti di prosa che contengono le stesse informazioni copiate a mano non
restano coerenti. Il documento che si **esegue** era fermo a una versione precedente di quello che
**governa**, e le sigle divergevano fra documenti.

**Dove.** Quattro rilievi indipendenti sullo stesso guasto:

| Rilievo | Cosa dimostra |
|---|---|
| `CRITICA-EMPERATOR.md` E-05 + `CRITICA-C.md` D-C-08 | il dossier 09 è «seconda versione», 07 e 08 sono «terza»: **9 agenti contro 11**, **4 reparti contro 8**, `lan-segretario` incluso e dichiarato eliminato a `01:409`, il «motore dei gate» come agente contro `scripts/gate.py` |
| `CRITICA-A.md` D-A-02 | il dossier 03 usa sei sigle di reparto (`LAN-PRODOTTO`, `LAN-STRATEGIA`, `LAN-PRICING`, `LAN-COPY`, `LAN-SITI`, `LAN-ESECUZIONE`) che non esistono fra i dodici di `01:120-133`: zero corrispondenze letterali |
| `CRITICA-A.md` D-A-03 | `03:16-17` dichiara che le sigle `GP-*` sono state sostituite; poi `03:170-178` usa sette controlli `GP-0…GP-6` e lo schema del certificato li usa come chiavi. **Sette non entrano in tre, e la mappa non esiste** |
| `CRITICA-C.md` D-C-01 | blocco circolare: per arrivare ad `APPRESO` serve passare `GATE-CPY-1`; per avere quel controllo serve lo scaglione S2; per sbloccare S2 serve un lancio in `APPRESO` |

**Il caso concreto che lo fa cadere.** Gael apre il dossier 09 — che il documento d'apertura gli
indica come *«prima di cominciare»* — e costruisce nove agenti, fra cui uno che il dossier 01 ha
dichiarato eliminato, e **senza** `lan-off-conductor`, l'unico che scrive `offerta.json`. Il
lancio si ferma in `ISTRUITO` per sempre: che è precisamente il difetto che il dossier 01
dichiarava di aver corretto.

**Perché è fatale.** Non è un errore di ragionamento: è un errore di copia, e gli errori di copia
sono inevitabili quando la stessa informazione vive scritta a mano in undici posti. Un piano che
si corregge a giri e propaga le correzioni a mano produce, a ogni giro, un documento aggiornato e
uno no — e chi costruisce apre quello sbagliato.

**Cosa fa la versione 4.** La fonte di verità non è più prosa: è **`dati/registro.yaml`**, un file
dati da cui i documenti citano e gli script leggono. La coerenza non è più affidata all'attenzione
umana ma a un programma:

```bash
cd PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati
PYTHONIOENCODING=utf-8 python valida_registro.py
# 253 controlli eseguiti → PIANO COERENTE
```

`INV-05` rifiuta qualunque sigla che non appartenga all'elenco degli identificativi definiti nel
registro. I documenti scendono da undici a sei, e la regola è scritta in `00-LEGGIMI.md` §5: **se
un documento dice una cosa diversa dal registro, ha torto il documento.** Il blocco circolare
sparisce insieme alla sua causa: non ci sono più scaglioni che abilitano reparti, perché la
costruzione comincia da un lancio vero e non da un'infrastruttura (`00-LEGGIMI.md` §3.4).

---

## F-06 · La firma umana era una stringa: un agente in ciclo di riparazione poteva scriverla

**Il difetto.** Il controllo del prezzo verificava che il campo `firmato_da` contenesse un nome di
persona. Nessun canale, nessuna provenienza, nessun legame col testo firmato, nessun divieto di
scrittura per gli agenti.

**Dove.** `CRITICA-B.md` D-B-02 e D-B-03: `04:228` (*«`firmato_da` contiene un nome di persona»*),
`04:230-232`, `04:295` (`firma(lancio_id, chi, valore) -> dict`, senza riferimento alla proposta).
Lo stesso guasto altrove: `CRITICA-A.md` P-A-18 e B-A-10 — `03:201` (`"firma_umana": "Max | Gael |
null"`), `01:422` (`"attestato_da": "Max"`).

**Il caso concreto che lo fa cadere.** Due casi, entrambi dimostrati:
1. Un agente conduttore in ciclo di auto-riparazione, incalzato da un controllo che blocca, scrive
   `firmato_da: "Max"` per sbloccarsi. Il controllo certifica una decisione umana mai presa, e il
   lancio parte a un prezzo che nessuno ha approvato.
2. Max firma 47 € su una proposta; la proposta viene rigenerata con motivazioni diverse; la firma
   resta formalmente valida su un contenuto che non esiste più.

**Perché è fatale.** È il fallimento peggiore possibile di tutto il sistema — peggiore del blocco
che il reparto vuole curare — perché produce un danno **verso l'esterno** con l'apparenza della
regolarità. Le nove decisioni che il piano dichiarava non delegabili erano protette da una stringa
dentro un file.

**Cosa fa la versione 4.** La firma diventa un oggetto con canale in lista chiusa e impronta del
testo firmato:

- `registro.yaml` → `canali_firma_ammessi: [comando-utente, chat-firmata, file-fuori-agenti]`, con
  la riga esplicita: *«Nessun agente ha permesso di scrittura sul sotto-oggetto "firma" di ART-OFF
  e sul "via_libera" di ART-APE.»*
- `lan-off-conductor` porta `vincolo_scrittura: "NON può scrivere il sotto-oggetto firma"`.
- `GATE-OFF-1` chiede `firma.canale in canali_firma_ammessi AND firma.proposta_hash == sha256(file
  proposta corrente)`, con **due** test rossi: una firma scritta da un agente su canale non
  ammesso deve bloccare, e una firma valida su una proposta poi rigenerata deve bloccare per
  impronta non corrispondente.
- `offerta.schema.json` righe 120-132: la firma richiede `["chi", "canale", "riferimento",
  "proposta_impronta", "il"]`, e l'impronta è descritta come ciò che fa decadere la firma alla
  rigenerazione.
- `INV-10` verifica che ogni artefatto con firma umana dichiari il nome del campo obbligatorio.

---

## F-07 · Cinque controlli su sette erano eseguiti da chi produceva la cosa controllata

**Il difetto.** La regola *«chi produce non approva»* era scritta, ed era violata dieci righe più
sotto, nell'unico flusso specificato per intero.

**Dove.** `CRITICA-A.md` D-A-01 e C-A-03. La regola sta a `03:166`. Le violazioni:
`03:134`+`03:173` (N1 e GP-1, entrambi `lan-prod-intake`), `03:135`+`03:174` (N2 e GP-2),
`03:138`+`03:176` (N5 e GP-4), `03:141`+`03:178` (N8 e GP-6). Contraddice anche `01:30` (*«il
livello L5 non risponde a L3»*) e l'intera tabella di `01:100-111`.

**Il caso concreto che lo fa cadere.** `lan-prod-collaudatore` esegue il collaudo e scrive
`05-collaudo.json`; il controllo GP-4 legge quel file ed è eseguito **dallo stesso agente**. Se il
collaudatore non riconosce come collegamento un riferimento dentro un PDF, la bandiera rossa esce
a zero e il controllo conferma lo zero. Il prodotto passa con 40 collegamenti morti e nessun
verbale lo dice.

**Perché è fatale.** Un difetto sistematico del produttore è invisibile al controllo **per
costruzione**, perché il controllo è quel produttore. Non è un rischio: è una garanzia di cecità.

**Cosa fa la versione 4.** Il registro rende `produttore` e `giudice` due campi obbligatori e
distinti di ogni artefatto, e `INV-01` verifica `giudice != produttore` prima di ogni costruzione.
Il giudice è uno solo, `lan-gate`, e **non ha `Write` né `Edit` fra i propri strumenti**
(`INV-09`): i verbali li scrive lo script, non l'agente. La ragione, scritta nel registro accanto
all'invariante: *«una regola che un programma non controlla è un'opinione»*.

La prova che l'invariante serve è nel registro stesso, lasciata lì apposta: al primo giro il
validatore ha bocciato la riga `nota_controfirma`, scritta un'ora prima, perché dava all'agente
che controfirma il debrief il ruolo di giudice pur avendo permesso di scrittura.

---

## F-08 · In 3.718 righe non compare mai la domanda «quanto ci aspettiamo di incassare»

**Il difetto.** C'erano il prezzo, il tetto di spesa, il pareggio nominato e il consuntivo a
posteriori. Non c'era il modello: quante persone vedono l'offerta, quante comprano, a che prezzo.

**Dove.** `CRITICA-EMPERATOR.md` §B, con le tre conseguenze misurate su righe altrui:
`04:143-170` (la proposta di prezzo, che offre 27/47/97 senza dire cosa cambia in ricavo),
`02:251` e `CRITICA-A.md` P-A-06 (`GATE-TSR-1` pretende *«il pareggio calcolato»*), `01:303` e
`CRITICA-A.md` P-A-09 (il controllo finale conta tre schemi prodotti da chi controlla).

**Il caso concreto che lo fa cadere.** Tre, in fila:
1. Chi firma il prezzo sta scegliendo **un numero, non un risultato**.
2. Il controllo del tetto di spesa chiede un pareggio, e il pareggio è ricavo previsto contro
   costo. Il ricavo previsto non esiste in nessun artefatto del piano: **un controllo che chiede
   un dato che nessun reparto produce non può passare.**
3. A lancio chiuso, il consuntivo è un numero solo. Senza previsione non c'è scarto, e senza
   scarto non c'è niente da imparare: il reparto Memoria eredita un compito impossibile.

**Perché è fatale.** Blocca la firma — che è il punto per cui l'ecosistema esiste — rende
insoddisfacibile un controllo obbligatorio, e svuota l'ultimo stato della macchina.

**Cosa fa la versione 4.** Nasce `ART-PRV` / `previsione.json`, prodotto **prima** della firma e
confrontato col consuntivo alla chiusura. `dipende_da: ["ART-PUB", "ART-RIC"]`, e `ART-OFF` dipende
da lui. `GATE-PRV-1` chiede esattamente tre scenari — pessimista, atteso, ottimista — con il ricavo
calcolato dalla formula dichiarata e **ogni assunzione marcata `misurato` o `assunto`**, con la
fonte obbligatoria per le prime; test rosso: *«una previsione con un tasso di conversione
dichiarato "misurato" e senza fonte deve BLOCCARE»*. `GATE-TSR-1` ora ha un pareggio che qualcuno
produce: *«pareggio.copie calcolato da ART-PRV»*, e il dato arriva da terzi, non dal contabile.
`ART-CNS` smette di essere un testo e diventa un artefatto tipizzato — *«un testo non si confronta
con una previsione»* — e `GATE-MEM-1` pretende una causa scritta per ogni scarto oltre il 10%.
Insieme chiudono **B-043**, *«Digital Empire non misura un solo euro»*.

E la firma cambia forma: da «47, 27 o 97?» a *«47 € su un pubblico verificato di N, con una
conversione del 2%, fa X. 27 fa Y. 97 fa Z. Confermi 47?»* (`00-LEGGIMI.md` §3.3).

---

## F-09 · Tutto il piano poggiava su agenti invocati da programmi, e non diceva mai come si invoca un agente da un programma

**Il difetto.** I controlli «vivono dentro `lancio avanza`», cioè dentro codice che fa lavorare
agenti. Come un file `.claude/agents/*.md` venga invocato da uno script non è scritto in nessuna
delle 3.718 righe.

**Dove.** `CRITICA-EMPERATOR.md` E-02. La misura sul campo è in `PONTE-AGENTI.md` §1-2:
- il comando ufficiale esiste ed è installato (`claude` v2.1.39, opzioni `--agent`, `-p`,
  `--output-format json`), verificato eseguendolo;
- **nessuno script del repository lo usa**: la ricerca mirata su `*.py, *.mjs, *.js, *.ps1, *.sh`
  dà zero risultati applicativi;
- l'unico meccanismo che davvero fa lavorare un file agente è `conductor_auto.py` righe 38-83 di
  YOUTUBE-AUTOMATION-FACTORY, che chiama l'interfaccia grezza e legge una **libreria di prompt
  propria**, non `.claude/agents/`;
- `empire/core/runner.py` è un esecutore vero ma orfano: non punta a `.claude/agents`, non è nelle
  dipendenze dichiarate, nessun comando lo invoca, nessun test lo copre, e si romperebbe sul campo
  `model: sonnet` perché quell'alias vale solo per la riga di comando.

E la risposta esisteva già, pagata: **ADR-014** (2026-08-30) documenta tre guasti e tre lezioni.
La v3 non lo cita mai.

**Il caso concreto che lo fa cadere.** Si scrive `lancio avanza`, si arriva alla prima fase che
richiede un agente, e non c'è una riga che dica come. Chi lo scrive a intuito ripete i tre guasti
già pagati: il prompt multiriga troncato alla prima riga **in silenzio**, l'alias di modello che
restituisce un modello diverso da quello che si crede di pagare, e il tetto di spesa sfondato
senza che nessuno se ne accorga.

**Perché è fatale.** Senza quel ponte l'ecosistema nasce di carta — esattamente il difetto che
dichiarava di curare: 19 file, 2.377 righe, zero eseguibili, zero agenti invocabili.

**Cosa fa la versione 4.** Il registro ha una sezione `ponte` con il meccanismo dichiarato
(`claude -p --agent <id> --output-format json`) e le **quattro regole ereditate da ADR-014**,
ognuna con il guasto che l'ha pagata: prompt da standard input mai come argomento; identificativo
esplicito del modello mai l'alias; lettura di `total_cost_usd` e verifica del budget **prima** di
ogni chiamata; lavoro a blocchi, perché ogni invocazione costa ~0,08-0,11 $ di sola tassa. Più un
tetto: **15 $ per lancio**, e al tetto il lancio si ferma dov'è ed è salvato — si riprende, non si
ricomincia.

---

## F-10 · Nessun controllo diceva cosa succede quando boccia, e nessuno aveva un caso che lo facesse fallire

**Il difetto.** I controlli dicevano tutti *cosa* verificano e nessuno diceva **dove torna il
lancio quando bocciano**, quante volte si riprova, chi decide che si smette. E l'unica riga che
chiedeva un test di fallimento non aveva formato, né esecutore, né obbligo.

**Dove.** `CRITICA-B.md` D-B-08: `04:104` (l'offerta), `05:74` (i testi), `06:78` (il funnel),
`06:279` (l'editoriale) — quattro controlli, zero rami di fallimento. `CRITICA-A.md` B-A-25:
`01:473` dice *«ogni gate ha un caso che FALLISCE»*, ed è l'unica riga di ingegneria del software
in tre dossier, senza formato né esecutore né la regola che imponga il test **prima**
dell'attivazione del controllo.

**Il caso concreto che lo fa cadere.** Pagina di vendita a 74 punti su una soglia di 80. Si
riscrive. La valutazione costa 3 ore e la scrittura 8-12: due giri fanno **+25 ore invisibili** su
una stima di 40-55 che dichiara 15-20 ore di sola valutazione, cioè un giro solo. E se il modello
riscrivendo perde punti altrove, il ciclo non termina — senza che nessuna regola dica quando
fermarsi.

**Perché è fatale.** Un controllo senza ramo di fallimento non è un controllo: è un'asserzione che
fa esplodere il processo. E un controllo senza un caso costruito apposta perché fallisca è
decorativo per costruzione: non si sa se blocca, si sa solo che non ha ancora bloccato.

**Cosa fa la versione 4.** Nel registro, la sezione dei controlli ha cinque campi obbligatori per
ogni voce, e due sono questi: `ramo_fallimento` (dove torna il lancio, cosa si conserva) e
`test_rosso` (il caso costruito apposta perché fallisca). Sono verificati da `INV-03` e `INV-04`,
con le motivazioni scritte accanto: *«nessuno dei gate della versione precedente diceva cosa
succede quando boccia»* e *«un gate senza un caso che lo faccia fallire è decorativo per
costruzione»*. Ogni artefatto porta inoltre `se_fallisce`, mai vuoto, con lo stato di
destinazione. Il ramo non butta il lavoro fatto: `GATE-CPY-1` conserva i testi sopra soglia e fa
rifare **solo i blocchi bocciati**; `GATE-TSR-2` blocca la spesa nuova e non uccide il lancio.

---

## F-11 · Quarantuno agenti, e nessuna riga sul costo di farli girare

**Il difetto.** Il tetto di spesa del lancio copriva solo la spesa esterna. Il costo di far girare
il sistema — le chiamate ai modelli — non aveva una voce, non passava per nessun controllo, non
entrava nel consuntivo, non saliva in Tesoreria e non compariva nel margine.

**Dove.** Quattro revisori lo trovano separatamente: `CRITICA-EMPERATOR.md` E-07, `CRITICA-A.md`
B-A-13, `CRITICA-B.md` B-B-04, `CRITICA-C.md` D-C-13 (che cita `07:48-52` per il tetto che copre
solo pubblicità, commissioni e rimborsi). La stima d'ordine di grandezza, dichiarata come tale,
sta in `CRITICA-D.md` §2: **150-250 invocazioni per il primo lancio**, cioè 12-27 $ di sola tassa
fissa e un conto realistico di **50-150 $ per lancio** una volta contati i testi su modello
pesante.

**Il caso concreto che lo fa cadere.** L'ecosistema che nasce per sapere quanto costa un lancio
non conta quanto costa sé stesso, e il margine che dichiara è sbagliato per eccesso di una
quantità che nessuno ha mai calcolato. In un'azienda che valuta ogni spesa a preventivo e ha un
direttore finanziario e una sentinella dei costi, è un numero che andava scritto **prima** di
costruire.

**Perché è fatale.** Senza costo unitario non esiste pareggio; senza pareggio il controllo del
tetto di spesa non può passare — è lo stesso guasto di F-08, dall'altro lato del conto; e senza
tetto la tassa fissa per invocazione rende quarantuno agenti un moltiplicatore di costo, non una
ricchezza.

**Cosa fa la versione 4.**
- `budget.schema.json` rende `costo_macchina_previsto` un campo **obbligatorio**.
- `GATE-TSR-1` chiede `costo_macchina_previsto presente e > 0`, con test rosso *«un budget senza
  costo_macchina_previsto deve BLOCCARE»*.
- `previsione.schema.json` porta `include_costo_macchina`: il ricavo atteso dichiara se il costo
  della macchina è dentro o fuori.
- Il ponte fissa **15 $ di tetto per lancio** e il comportamento al tetto.
- L'osservabilità lo rende leggibile: ogni invocazione lascia una riga in
  `registro-chiamate.jsonl` con agente, modello, durata, costo ed esito, e `lancio costi <id>` lo
  legge da lì, **mai stimato** (`01-ARCHITETTURA.md` §8).
- Gli agenti scendono da quarantuno a **quindici**, e tre sono al grado più basso perché fanno
  calcoli deterministici: *«un modello linguistico che "ragiona" su un calcolo deterministico è un
  modo caro di sbagliare»* (`registro.yaml`, nota di `lan-prv-modello`).

---

## F-12 · Il controllo sul valore dell'offerta si soddisfaceva inventando un bonus

**Il difetto.** Il controllo del prezzo pretendeva un valore percepito almeno triplo del prezzo, e
il numero del valore lo dichiarava lo stesso agente che costruiva il pacchetto, senza nessuna
regola di derivazione.

**Dove.** `CRITICA-B.md` D-B-04: `04:104` e `04:227` (il rapporto ≥3), `04:103` (chi produce la
struttura), lo schema a `04:262-263` (`valore_dichiarato`, `rapporto_valore_prezzo`). La soglia è
dichiarata arbitraria dal piano stesso a `04:349-351`, e vive in due controlli diversi con due
proprietari (`05:133`, griglia dei testi).

**Il caso concreto che lo fa cadere.** Prezzo 47 €, servono 141 € di valore. Si aggiunge «Bonus:
checklist — valore 99 €». Rapporto 4,0. Controllo verde. Il numero non significa niente e
**finisce sulla pagina di vendita**, dove la griglia dei testi lo riprende come dato.

**Perché è fatale.** Il vincolo non seleziona: istruisce a gonfiare. E il prodotto del controllo
non è un blocco mancato ma un'affermazione falsa verso il cliente, generata dal sistema stesso e
certificata da un controllo verde. È un controllo che produce il danno che dovrebbe prevenire.

**Cosa fa la versione 4.** `GATE-OFF-1` calcola il rapporto solo su
`somma(bonus[].valore dove fonte_valore != null)`. `offerta.schema.json` righe 63-68 rendono
`fonte_valore` obbligatorio per ogni bonus, e descrivono il valore dichiarato come *«somma dei
soli bonus con fonte_valore diversa da null, più il valore del prodotto. Un numero che il gate
ricalcola, mai legge.»* Un bonus senza fonte vale **zero**.

---

# 3. I DIFETTI GRAVI — quelli che avrebbero prodotto un sistema che gira male

Quarantacinque, raggruppati per tema. Nessuno di questi da solo fermava il primo lancio: presi
insieme producevano un sistema che gira, non blocca mai niente, e a fine anno non ha imparato
nulla. Stesso schema della §2, in forma stretta.

## 3.1 Coerenza fra documenti

**G-01 · I conti degli agenti e dei livelli non tornano, nella riga che dichiara di averli rifatti.**
*Dove:* `CRITICA-C.md` §1.1 — `08:116` promette «il conto è stato rifatto e verificato riga per
riga», e la somma della colonna della stessa tabella fa 45, non 41, con due sentinelle interne, non
quattro · `CRITICA-D.md` §1 (11 capi contro 10, 30 operativi contro 29) · `CRITICA-A.md` C-A-15 e
C-A-16 (17 script dichiarati a `01:469`, 11 nominati) · `CRITICA-C.md` §1.2 (gli agenti veri sono
≥55: il reparto Prodotto ha tre conteggi diversi in due dossier — 5, «8», 9).
*Caso:* chi costruisce non sa quanti agenti deve scrivere, e nessuna delle tre cifre è autorevole.
*Perché conta:* un censimento che si autocertifica e sbaglia l'aritmetica non è un censimento, e
tutte le stime di ore che ne discendono sono false.
*v4:* gli agenti non si elencano, si **derivano** dai produttori degli artefatti, e `INV-07`
verifica che li coprano tutti. Sono quindici, contati dal registro.

**G-02 · Tredici controlli dichiarati, quattordici esistenti, e due che rivendicano la stessa transizione.**
*Dove:* `CRITICA-C.md` D-C-11 e `CRITICA-D.md` §1 — `07:103` introduce `GATE-TSR-3` con criterio ed
esecutore; `00:270-289` intitola «i tredici gate — numerazione unica» e non lo contiene; `10:51` e
`10:141` costruiscono sul numero tredici. `GATE-TSR-3` e `GATE-MEM-1` rivendicano entrambi la
transizione da CHIUSO ad APPRESO, con criteri diversi e nessun ordine fra loro.
*Caso:* chi scrive il motore dei controlli legge l'elenco ufficiale e non implementa il
quattordicesimo: la riconciliazione con la Tesoreria resta senza controllo.
*Perché conta:* la «numerazione unica» era presentata come la correzione di un difetto del primo
giro, ed era già scaduta.
*v4:* i controlli sono **quattordici**, elencati una volta sola nel registro, e `INV-05` rifiuta
qualunque sigla fuori elenco. `GATE-TSR-3` non esiste: il perché è in §4, R-05.

**G-03 · Due dossier con lo stesso numero in testa, un agente con due nomi, due prefissi per lo stesso reparto.**
*Dove:* `CRITICA-B.md` D-B-22 (`05:8` porta «# 06 — WF-CPY» dentro un file chiamato `05-`; anche
`06:8` porta «06»; `lan-cpy-giudice` a `05:74` contro `lan-copy-giudice` a `05:244`; il dossier 04
è l'unico senza intestazione YAML, quindi invisibile a qualunque indicizzazione) · `CRITICA-D.md` §1 (il
file `08-…` ha per intestazione «# 11 — AGENTI, SKILL E COMANDI») · `CRITICA-C.md` §1.3
(`lan-prd-` contro `lan-prod-`, usato 33 volte).
*Caso:* nascono due file diversi in `.claude/agents/` per lo stesso mestiere — e `08:159` avverte
da sé: «un disallineamento e l'agente non si trova».
*Perché conta:* è il difetto che `06:30-32` dichiara letale, commesso dai documenti che lo dichiarano.
*v4:* gli identificativi vivono solo nel registro, con lo stesso prefisso di reparto, e il
validatore rifiuta quelli fuori elenco (`INV-05`).

**G-04 · Tabelle dei cambiamenti che dichiarano correzioni non presenti nel corpo.**
*Dove:* `CRITICA-A.md` D-A-14 e C-A-05 (`03:20` dichiara la soglia delle fonti allineata a ≥90%, e
il corpo la lascia al 100% due volte) · C-A-06 (`01:493` rivendica la numerazione unica dei
controlli, il corpo usa `GP-*` ovunque, chiavi del certificato comprese) · `CRITICA-B.md` D-B-20
(`05:339` dichiara cambiata una regola anti-plagio che **nel corpo non esiste**: non è nella
griglia, non è nelle classi, non è una fase) · `CRITICA-D.md` §5 (il conto sbagliato dentro la
tabella stessa: «undici agenti su sei reparti», i reparti distinti sono otto).
*Caso:* il revisore successivo legge la riga, la crede, e non verifica.
*Perché conta:* un elenco di correzioni che asserisce il falso è peggio di nessun elenco.
*v4:* la regola di metodo della §1.2, e il fatto che le correzioni non vivono in una tabella di
prosa ma nel registro, dove il validatore le controlla.

**G-05 · Tre soglie diverse per lo stesso criterio, e tre proprietari per lo stesso criterio.**
*Dove:* `CRITICA-A.md` D-A-14 (≥90% a `03:20`, 100% e solo codici 200/301 a `03:135` e `03:174`,
nessun controllo di raggiungibilità a `02:245`) · C-A-24 (`01:144` dice che la Qualità possiede i
criteri; `03:170-178` li definisce dentro il dossier di un altro reparto; `02:198-203` li fa
scrivere dal mittente del passaggio di consegne) · `CRITICA-B.md` §4.2 (il rapporto valore/prezzo
vive in due controlli con due proprietari).
*Caso:* 17 fonti, una dietro un filtro che risponde 403 a chi non è un navigatore. Una riga boccia,
l'altra passa: il verbale dirà una cosa o l'altra secondo quale riga ha letto chi ha scritto il codice.
*Perché conta:* due criteri sullo stesso oggetto senza regola di precedenza producono un blocco che
nessuno sa a chi appartiene.
*v4:* ogni artefatto ha **un solo** controllo e **un solo** giudice (`INV-01`), e il criterio è
scritto una volta, nel campo `criterio_eseguibile` di quel controllo.

## 3.2 Controlli che non possono fallire

**G-06 · Otto controlli su tredici avevano una frase o niente.**
*Dove:* `CRITICA-A.md` B-A-07 e P-A-01…P-A-09 — «prezzo e data presenti e non evasivi» (`01:296`),
«le dieci voci vere insieme» (`01:299`, l'elenco non esiste), «le cinque domande hanno risposta
scritta» (`01:292`, le domande non sono scritte in nessuno dei tre dossier), «nessuna riga
incompleta» (`02:250`), «pareggio calcolato» (`02:251`), «il budget è saltato» (`01:298`, senza
soglia), «ogni pezzo ha superato il gate della sua classe» (`02:248`, le classi non sono enumerate).
*Caso:* cinque campi con «sì» passano il primo controllo del sistema; `"97-197 da decidere"` passa
il controllo del prezzo.
*Perché conta:* un criterio in italiano non è verificabile da un programma: o diventa un predicato,
o il controllo è un timbro.
*v4:* `criterio_eseguibile` è campo obbligatorio di ogni controllo, scritto come predicato e non
come frase (registro, sezione `gate`).

**G-07 · Il criterio di accettazione era una lista di frasi, e una funzione dichiarava di verificarle.**
*Dove:* `CRITICA-A.md` D-A-18 e P-A-10 — `02:198-203` (le frasi) e `02:315`
(`accetta(handoff_id, chi) -> dict`, «verifica il criterio prima di accettare»).
*Caso:* il destinatario chiama la funzione, che non può fare altro che ritornare accettato.
*Perché conta:* il secondo dei due «sistemi nervosi» del dossier 02 non aveva un solo controllo eseguibile.
*v4:* i passaggi di consegne con criterio in prosa sono usciti dal piano. Gli artefatti dipendono
l'uno dall'altro per `dipende_da`, e la validità si ricalcola dai file contro lo schema, mai da una
dichiarazione (`GATE-REG-1`, campo `dato_da_terzi`).

**G-08 · Le formule del tetto di spesa dividono per zero e non hanno tetto superiore.**
*Dove:* `CRITICA-C.md` D-C-07 (col profilo di spesa «posticipato» il previsto a oggi vale
esattamente 0 per il primo 60% della voce, e quel profilo è il normale per la pubblicità di un
lancio: nella finestra iniziale il divisore è 0 e il criterio è indefinito) · `CRITICA-D.md` D-D-01
(«lineare» e «posticipato» non hanno `min(1, …)`: a voce scaduta il previsto supera l'importo e
gonfia il divisore, facendo sembrare piccolo uno sforamento reale).
*Caso:* 300 € di prova annunci spesi tre giorni prima della finestra prevista. Il controllo divide
per zero: se lo script è difensivo salta il controllo, altrimenti esplode e il comando «sembra
rotto». Lo sforamento del 100% nella fase in cui i soldi si bruciano per errore non è rilevabile.
*Perché conta:* è il controllo che la v3 dichiarava di aver reso «capace di fallire», e restava
incapace di bloccare proprio dove serve.
*v4:* `GATE-TSR-2` ha un criterio unico e sempre calcolabile — `scarto_percentuale(speso, previsto)
<= 10` — un ramo di fallimento che **blocca la spesa nuova senza uccidere il lancio**, e un test
rosso che lo prova: «uno scarto dell'11% deve bloccare la spesa nuova e NON uccidere il lancio».

**G-09 · Il controllo più costoso si spegneva abbassando un numero deciso da chi ha fretta.**
*Dove:* `CRITICA-A.md` D-A-11 — `03:139` (prova sul campo obbligatoria sopra 97 €), `03:156` («se
si fissa un prezzo < 97 €, il controllo si rilegge e il beta decade»), `03:177` (passaggio automatico
sotto soglia).
*Caso:* prezzo a 89 € per chiudere il pilota, controllo saltato, certificato emesso. Due settimane
dopo il prezzo sale a 197 €. Nessuna regola riapre il controllo: esce un prodotto da 197 € senza un
solo collaudatore esterno e con un certificato formalmente valido.
*Perché conta:* il piano prevedeva **esplicitamente** il decadimento del controllo al ribasso, e
niente al rialzo.
*v4:* la firma è legata al testo firmato (F-06) e ogni artefatto a monte che cambia rende
`da_rivedere` quelli a valle, riaprendo i loro controlli (`01-ARCHITETTURA.md` §7).

**G-10 · La prova del tracciamento era un booleano a 60 secondi, e il consenso ai cookie non entrava nel controllo.**
*Dove:* `CRITICA-B.md` D-B-09 (`06:111`, `06:117-120`, `06:126-127` —
`prova_evento(url, evento, timeout_s=60) -> bool`: non è detto **dove** si guarda, e la sola fonte
che conta ha latenza di ore) e D-B-10 (`06:192` nomina il consenso ai cookie come causa numero uno
di fallimento della misura, e `06:118` non dice cosa fa chi esegue la prova davanti all'avviso di consenso).
*Caso:* il controllo restituisce falso su un tracciamento funzionante, blocca il lancio, e viene
derogato la prima volta. Al secondo lancio nessuno lo esegue più. Oppure: chi esegue la prova accetta il
consenso, il visitatore medio lo rifiuta, il controllo è verde e i numeri non arrivano lo stesso.
*Perché conta:* un controllo che boccia a caso viene derogato, e un controllo derogato una volta
smette di esistere.
*v4:* `GATE-FNL-1` chiede per ogni pagina un evento di conversione con `prova.origine=='piattaforma'`;
`funnel.schema.json` richiede `origine`, `identificativo_evento` e `letto_il` per ogni evento, più un
blocco `consenso` obbligatorio con `banner_presente`, `misura_prima_del_consenso` e la quota stimata.
La descrizione nello schema dice perché: senza, ogni previsione è sbagliata di una quantità nota e taciuta.

**G-11 · La pubblicazione irreversibile veniva prima della prova che la cassa funziona.**
*Dove:* `CRITICA-B.md` D-B-18 — `06:76` (la pubblicazione, dichiarata irreversibile), `06:115` (la
transazione reale, dentro il controllo che sta **dopo**), `06:62` (la stessa transazione chiesta
come precondizione d'ingresso: o è duplicata, o sono due cose diverse e non è dichiarato quali).
*Caso:* si pubblica, e solo dopo si scopre che la cassa non incassa. Non esiste procedura per
togliere una pagina pubblicata (`CRITICA-B.md` B-B-10: nessun ritorno indietro, nessuno stato per
«online ma da non promuovere»).
*Perché conta:* l'ordine dei passi è l'unica cosa che un piano di lancio deve azzeccare.
*v4:* la prova di cassa è **dentro** `GATE-FNL-1` e quindi precede l'apertura della vendita
(`ART-FNL.nota_cassa`); il ramo di fallimento riporta a `IN_PRODUZIONE` con l'elenco delle pagine
non conformi, e le pagine conformi restano.

**G-12 · Il reparto che spende denaro non aveva nessun controllo.**
*Dove:* `CRITICA-A.md` D-A-19 — la tabella «chi produce ≠ chi approva» di `01:100-111` ha dieci
righe e non contiene il reparto Traffico; `01:128` gli fa produrre `traffico.json`; nessuno dei
tredici controlli è suo. Aggravante in `CRITICA-D.md` D-D-03: il dato che alimenta il costo di
acquisizione non ha né produttore né schema né passaggio dichiarato.
*Caso:* `traffico.json` dichiara un costo per acquisizione di 3,20 €, il consuntivo dice 11 €.
Nessun controllo confronta i due numeri e il debrief scopre la divergenza a lancio chiuso.
*Perché conta:* l'unico reparto che tocca denaro vero era l'unico senza giudice.
*v4:* i canali a pagamento entrano in `pubblico.json` con la loro prova, la spesa entra in
`budget.json` sotto `GATE-TSR-1` e `GATE-TSR-2`, e `consuntivo.schema.json` separa `per_canale`
tenendo i canali a pagamento distinti dagli organici — con la ragione scritta nello schema:
mescolarli rende impossibile sapere cosa ha funzionato.

**G-13 · Il controllo dell'ultimo stato contava un risultato prodotto da chi il controllo controlla.**
*Dove:* `CRITICA-A.md` P-A-09 — `01:303` e `02:253`: «debrief con ≥3 schemi e cause scritte»,
contato sul risultato del reparto Memoria e giudicato dal reparto Memoria.
*Caso:* tre schemi generici si scrivono in dieci minuti. L'unico controllo dello stato finale è un
contatore che si alimenta da solo.
*Perché conta:* è il punto in cui l'autoassoluzione fa più danno, perché il debrief orienta tutti i
lanci successivi.
*v4:* `ART-DBR` è prodotto dalla Memoria e giudicato da `lan-gate` (`INV-01`), con la controfirma
della Regia come **campo**, non come ruolo di giudice. `GATE-MEM-1` pretende una causa scritta per
ogni scarto oltre il 10%, `si_applica_quando` non vuoto per ogni schema, e che ogni record citi un
artefatto esistente su disco. Test rosso: «un debrief con tre schemi generici e uno scarto del 40%
senza causa deve BLOCCARE».

**G-14 · Lo stesso artefatto era validato due volte, da due reparti, con criteri diversi e senza precedenza.**
*Dove:* `CRITICA-A.md` D-A-15 — `01:103` (la ricerca è validata da `GATE-INT-1`) contro
`03:135`+`03:174` (un secondo controllo la rivalida dentro il flusso Prodotto e può respingerla),
con la macchina a stati (`01:295`) che li mette nella stessa transizione mentre `03:70` dice che il
secondo flusso parte solo dopo, per ordine umano.
*Caso:* la ricerca passa il primo controllo e viene respinta dal secondo. Di chi è la fase bloccata?
*Perché conta:* due giudici sullo stesso oggetto senza precedenza producono uno stallo che nessun
documento sa risolvere.
*v4:* un artefatto, un controllo, un giudice, dichiarati nel registro. Chi riceve un artefatto
valido si fida del verbale.

## 3.3 Dati senza schema e senza versione

**G-15 · Nove schemi su tredici non esistevano, e un nome di file non è un contratto.**
*Dove:* `CRITICA-A.md` B-A-03 (`01:470` promette una cartella con «gli schemi JSON, uno per
artefatto»; ne viene consegnato **uno**) · `CRITICA-B.md` B-B-01 (i tre dossier nominano diciassette
file di uscita e consegnano **tre** schemi) · `CRITICA-A.md` B-A-04 (lo schema del verbale, l'oggetto
più citato dei tre dossier e precondizione di ogni passaggio di consegne, non ha campi né convenzione
di nome, e non è detto se ne esista uno per controllo o uno per tentativo — il che decide se un
secondo tentativo cancella la prova del primo).
*Caso:* due agenti leggono lo stesso nome di file e lo interpretano diversamente; il controllo non
ha niente contro cui confrontare.
*Perché conta:* senza schema, «produce `decisione.json`» ripetuto in tre dossier non nomina un solo
campo, nemmeno l'esito.
*v4:* **tredici schemi su tredici**, versionati, in `dati/schemi/`, e `INV-02` verifica che ogni
artefatto abbia il proprio schema esistente sul disco.

**G-16 · Il manifesto dei testi non aveva schema, e la griglia poggiava su due liste che vivevano dentro un testo libero.**
*Dove:* `CRITICA-B.md` D-B-13 (`05:81`, `06:43`, `02:248`: il funnel deve verificare un criterio che
il manifesto non gli permette di verificare) e D-B-06 (la voce eliminatoria dichiarata automatica a
`05:156` poggia su output pratici che stanno in un percorso senza schema e su prove che stanno in un
markdown: da un testo libero non si estrae una lista tipizzata) · `CRITICA-B.md` §5.3 (le «ancore di
punteggio» promesse a `05:173-174` e mai scritte: 58 punti su 100 non riproducibili fra due
esecuzioni dello stesso giudice).
*Caso:* chi costruisce il giudice apre il file delle fondamenta, non trova campi, e chiede al modello
di «dedurre le prove». La voce eliminatoria torna a essere un'opinione.
*Perché conta:* la correzione di cui il dossier andava più fiero era appesa a due strutture dati che
il piano non definiva.
*v4:* `copy.schema.json` tipizza ogni pezzo con `punteggio.totale` e `punteggio.blocchi`, e prevede
il campo `ancora` per ogni voce — descritto nello schema come «l'esempio concreto che definisce quel
punteggio: senza ancore, due giudici danno voti diversi allo stesso testo». `GATE-CPY-1` risolve le
affermazioni di categoria `prova` contro il certificato e la ricerca, **non contro il testo stesso**.

**G-17 · Nessun artefatto era versionato: un cambio a monte non invalidava niente a valle.**
*Dove:* `CRITICA-B.md` D-B-11 — `05:40-43` (le fondamenta nascono prima del prezzo, per progetto),
`06:212` (la pagina d'ingresso esistente si riusa), `04:327` (la metrica «prezzi rivisti dopo l'apertura: 0»).
*Caso:* Max risponde «preferisco 27» — risposta che `04:169` prevede. La pagina di vendita è già
scritta con l'ancoraggio su 47, la cassa è configurata, le email di recupero citano il prezzo.
Nessun processo se ne accorge.
*Perché conta:* il piano gestiva l'ordine giusto e assumeva che nulla cambiasse, mentre il suo stesso
disegno rendeva il fuori-ordine la normalità.
*v4:* ogni artefatto porta `schema_version` e un'impronta dei propri ingressi; quando un artefatto a
monte cambia, **tutti quelli che dipendono da lui diventano `da_rivedere` e i loro controlli si
riaprono** (`01-ARCHITETTURA.md` §7).

**G-18 · Tre rappresentazioni dello stesso istante nel piano editoriale, senza fonte di verità.**
*Dove:* `CRITICA-B.md` D-B-16 — `06:300`: `"giorno": 12, "data": "2026-10-14", "fase": "T-16"`.
*Caso:* al primo spostamento di data le tre divergono e nessuna riga dice quale comanda.
*Perché conta:* la data di un lancio si sposta quasi sempre, e con la denormalizzazione ogni
spostamento produce un piano editoriale che si contraddice da solo.
*v4:* `editoriale.schema.json` richiede `data_uscita` e una `destinazione` risolvibile, e
`GATE-EDT-1` verifica le destinazioni contro il funnel reale, non contro una copia.

**G-19 · Gli identificativi collidono: un contatore giornaliero senza chi lo assegna.**
*Dove:* `CRITICA-A.md` D-A-16 — il formato `<prefisso>-<AAAAMMGG>-<n>` a `01:205`, `02:79`,
`02:191`, `02:118`, contro la regola di `02:100` («un identificativo non si riassegna mai»).
Nessun lock, nessun contatore atomico, e l'identificativo del passaggio non contiene nemmeno il
lancio.
*Caso:* due lanci in corso — previsti esplicitamente da `01:54` — e sei agenti che chiudono lo stesso
pomeriggio: due leggono la cartella, contano 2 record, scrivono lo stesso identificativo. Il secondo
sovrascrive il primo.
*Perché conta:* la regola più solenne della memoria è violata dal formato dell'identificativo che la enuncia.
*v4:* un lancio è una cartella, e ogni artefatto ha un nome di file fisso dentro quella cartella
(`registro.yaml`, campo `file` di ogni artefatto). Non ci sono progressivi da assegnare.

**G-20 · La proprietà di scrittura era dichiarata dal chiamante: la verifica confrontava un valore con sé stesso.**
*Dove:* `CRITICA-A.md` D-A-17 — `02:295` (`scrivi(reparto: str, …)` «rifiuta se il proprietario non
corrisponde al reparto») contro `02:57` («un solo proprietario di scrittura per spazio»). Il reparto
è un parametro passato dall'agente, e la funzione verifica che la stringa dichiarata corrisponda alla
cartella dedotta dalla stringa dichiarata. Stesso guasto in `CRITICA-B.md` B-B-05: nessun permesso di
scrittura per campo.
*Caso:* un agente dei testi dichiara di essere la Qualità e scrive un verdetto nello spazio dei
verbali. La verifica passa.
*Perché conta:* lo spazio che deve contenere «ogni verdetto, inclusi tutti i blocchi» era scrivibile
da chiunque.
*v4:* il registro dichiara un `produttore` unico per artefatto (`INV-01`), il giudice non ha la penna
(`INV-09`), e i sotto-oggetti di firma non sono scrivibili da nessun agente (F-06).

**G-21 · Concorrenza e idempotenza assenti, e più scrittori sullo stesso indice.**
*Dove:* `CRITICA-B.md` D-B-12 (non è scritto cosa succede se un comando gira due volte, chi scrive il
manifesto mentre cinque agenti producono file, cosa succede con due lanci aperti insieme) ·
`CRITICA-A.md` D-A-23 (`03:137`: N scrittori concorrenti su un solo file indice, senza lock né
strategia di fusione: l'ultimo che scrive vince e perde gli altri) · `CRITICA-A.md` D-A-04 (il
comando su cui poggia l'intera tesi del piano non ha firma, codici di uscita, lock, idempotenza, né
chi lo invoca).
*Caso:* cinque agenti chiudono a due secondi l'uno dall'altro e l'indice finale elenca due moduli su
cinque. Oppure Max e Gael eseguono lo stesso comando a un minuto di distanza da due macchine, e lo
stato viene riscritto da due processi.
*Perché conta:* il difetto si presenta come un guasto misterioso, non come un errore di progetto, e
consuma il miglior meccanismo del piano per diagnosticare un baco che il piano ha introdotto.
*v4:* `01-ARCHITETTURA.md` §2 dà a `lancio avanza` firma, quattro codici di uscita e **tre garanzie
scritte**: lock esclusivo sul file di stato (il secondo esce 1 dicendo chi lo detiene), idempotenza
per chiave `(controllo, tentativo)`, e ricalcolo dai file mai dallo stato.

## 3.4 Agenti

**G-22 · Quindici agenti erano funzioni travestite.**
*Dove:* `CRITICA-C.md` §1.4, con la riga per ognuno: il calendarista fa aritmetica sulle date — e
`07:273` lo dice da sé («il calendario si genera, non si scrive») — il tracciatore raccoglie numeri
che `09:175` mette in colonna «si automatizza», il registratore dei costi fa una scrittura in coda,
la sentinella applica quattro formule, il controllo dei costi valuta `≤ 0,10` (e `07:102` lo spezza
in **due** agenti: uno propone e uno verbalizza), il verificatore delle pagine fa una richiesta HTTP,
due inventarianti fanno lo stesso elenco di file, il misuratore del traffico ricalcola le stesse
formule di un altro agente — cioè due fonti di verità sullo stesso numero — e le quattro sentinelle
trasversali valutano quattro soglie. Confermato da `CRITICA-D.md` §1, che cita l'ammissione del piano
stesso a `08:296`: «Contano, confrontano, aprono indirizzi: non ragionano».
*Caso:* un modello linguistico a cui è vietato scrivere e il cui unico risultato è un booleano: il
modo più costoso mai inventato di scrivere una condizione. Quattro volte.
*Perché conta:* con una tassa fissa per invocazione (F-11), ogni agente inutile è un costo fisso per
lancio, per sempre.
*v4:* il registro ha quindici agenti, e il principio è scritto nella nota di `lan-prv-modello`: dove
c'è una formula da applicare si usa il grado più basso, perché «un modello linguistico che ragiona su
un calcolo deterministico è un modo caro di sbagliare». `INV-08` verifica che nessun agente di grado
basso produca un artefatto che richiede giudizio.

**G-23 · Il giudice in sola lettura doveva produrre il proprio verbale.**
*Dove:* `CRITICA-C.md` D-C-02 — `08:103` e `08:151` danno al giudice `Read, Grep, Glob` e nient'altro;
`07:90`, `07:93`, `07:102`, `07:171` gli assegnano come risultato **il verbale**; `00:297` dice che
senza verbale il controllo non è stato eseguito. Stesso guasto sulla sentinella (`CRITICA-C.md`
D-C-03): sola lettura a `08:106`, e a `07:92` un file JSON da produrre.
*Caso:* si copia l'intestazione alla lettera, il verbale non viene scritto, il passaggio successivo
lo rifiuta «per verbale mancante», e il lancio si blocca senza che nulla dica perché.
*Perché conta:* la correzione che il dossier 08 chiama «la più importante di tutto questo dossier»
rendeva fisicamente impossibile al giudice il compito che tredici righe gli assegnavano.
*v4:* il giudice non scrive il verbale: **lo scrive lo script**. `lan-gate` ha `Read, Bash, Glob,
Grep` e la nota nel registro dice perché non ha `Write` né `Edit` (`INV-09`).

**G-24 · Il campo degli strumenti non sa fare tre delle sei cose che il piano gli chiedeva.**
*Dove:* `CRITICA-C.md` D-C-04 e `CRITICA-D.md` §1 — «scrittura limitata alla propria cartella» non è
esprimibile: il campo concede classi di strumento, **non percorsi** (verificato: 18 agenti reali lo
usano, nessuno dimostra un vincolo di percorso). Il direttore ha tutti gli strumenti, quindi può
compiere da solo l'azione irreversibile che il principio 4 dichiara vietata. E gli operatori con la
sola lettura e scrittura non possono invocare le skill esistenti: **la strategia portante
dell'ADR — avvolgere invece di riscrivere — è ineseguibile con i profili dichiarati.**
*Caso:* l'archivista, che dovrebbe poter scrivere solo nella propria cartella, può riscrivere
l'offerta.
*Perché conta:* «una regola imposta dagli strumenti non viene disobbedita» era vera per due profili
su sei, e presentata come vera per tutti.
*v4:* il registro dichiara gli strumenti agente per agente, e l'unico vincolo che il campo sa davvero
imporre — togliere la penna al giudice — è quello su cui poggia un invariante (`INV-09`). Nessun altro
divieto è affidato a quel campo.

**G-25 · Il contratto d'uscita di ogni agente esisteva solo in prosa, e i campi che lo renderebbero leggibile erano vietati.**
*Dove:* `CRITICA-C.md` D-C-05 — `08:184-185` chiede una sezione «contratto d'uscita, con quale
schema» nel corpo markdown, mentre `08:166` elenca i campi che lo esprimerebbero fra quelli che fanno
scartare il file **in silenzio**. E `CRITICA-D.md` §1: i quattro controlli del verificatore non
aprono mai il corpo, quindi un agente con intestazione perfetta e sezione vuota passa lo stesso.
*Caso:* l'agente dell'offerta restituisce `"prezzo": "97€"` invece di `97.00`. Nessun controllo
scatta: gli schemi validano i file su disco, non ciò che un agente restituisce al chiamante. Il
difetto emerge tre fasi dopo, dentro il calcolo del ricavo netto, come un errore aritmetico.
*Perché conta:* è ciò che rende concatenabile una catena, ed era testo libero.
*v4:* gli agenti non si passano risultati: **scrivono artefatti**, e ogni artefatto è validato contro
il proprio schema prima che il successivo parta (`INV-02`, campo `dipende_da`).

**G-26 · Lo scaglione minimo non poteva eseguire l'unico flusso specificato.**
*Dove:* `CRITICA-A.md` D-A-20 (mancano gli agenti di quattro fasi, fra cui quella obbligatoria nel
percorso del pilota; e la giustificazione di `01:400` è falsa: il certificato lo emette un altro
agente) e D-A-05 (il record di chiusura fase lo scrive il capo del reparto; cinque reparti dello
scaglione minimo non ne hanno uno, quindi il record non si scrive e la fase non si chiude).
*Caso:* il pilota entra nel flusso Prodotto e non ha nessuno che validi l'ingresso, nessuno che
censisca i 203 fogli, nessuno che emetta il certificato. Il primo lancio si blocca alla prima fase,
per una regola introdotta come la correzione principale del piano.
*Perché conta:* il dossier applica alla versione precedente un metodo di verifica che non riapplica a
sé stesso.
*v4:* il nucleo minimo si calcola, non si decide: è l'insieme dei produttori degli artefatti da
`ART-PUB` ad `ART-DBR`, più il giudice, e `INV-07` lo verifica con la motivazione scritta accanto.

**G-27 · Il flusso della Regia non aveva fasi, agenti, risultati né ore.**
*Dove:* `CRITICA-C.md` D-C-06 — la Parte C di `07:231-359` ha sei sezioni e nessuno che le esegua; i
quattro agenti di quel reparto **non compaiono una sola volta** in tutto il dossier 07. Ed è lo stesso
difetto che `10:187` elenca fra i dieci corretti, definendolo «il pre-mortem numero uno, commesso dal
piano stesso».
*Caso:* il reparto che possiede l'apertura della vendita — l'atto per cui l'ecosistema esiste — si
costruisce a intuito, e ciò che nasce non ha un contratto con nessuno.
*Perché conta:* un difetto dichiarato corretto e ripetuto nello stesso pacchetto significa che la
correzione era un'affermazione, non un metodo.
*v4:* la Regia non è un capitolo di prosa: produce `ART-APE` e `ART-CNS`, con schema, produttore,
giudice, controllo, ramo di fallimento e test rosso, come ogni altro artefatto del registro.

**G-28 · «Reparto abilitato» era il vincolo portante del piano di costruzione e non era definito da nessuna parte.**
*Dove:* `CRITICA-C.md` D-C-09 — quattro punti del piano, fra cui il punto 6 della decisione dell'ADR,
poggiano su «il registro rifiuta gli agenti dei reparti non abilitati». Cercando la parola si trovano
quattro occorrenze, **tutte d'uso e nessuna di definizione**: non è scritto in quale file viva
l'elenco, chi lo modifica, con quale prova, né cosa succede alla specifica di un agente rifiutato. E
`08:232` rimanda a una sezione che non contiene alcun concetto di abilitazione: puntatore rotto su
una regola bloccante. Aggravante: il verificatore su cui tutto poggia non ha ore in nessuno scaglione
e non ha una specifica.
*Caso:* si configura l'elenco con i quattro reparti del documento che si esegue, e il verificatore
rifiuta cinque degli undici agenti minimi. Il vincolo che protegge il piano lo sabota.
*Perché conta:* è il meccanismo che avrebbe dovuto rendere «tecnico e non morale» il criterio di
avanzamento, e non esisteva.
*v4:* non ci sono reparti da abilitare. Il vincolo tecnico è uno solo ed è eseguibile: se
`valida_registro.py` non esce zero, il piano è incoerente e non si costruisce.

## 3.5 Costi, tempo, capacità umana

**G-29 · Le 139-187 ore erano solo costruzione: l'esercizio non era contato da nessuna parte.**
*Dove:* `CRITICA-C.md` §2.1 — le durate dei flussi esistono sparse (40-55 ore per i testi, 30-45 per
funnel ed editoriale, 16-30 per la ricerca, 3-5 per l'offerta, ~9,5 più una voce «continuo» senza
numero per il tesoro, nessuna ora dichiarata per la Regia) e **nessun documento le somma**. Nella
lettura più generosa un lancio costa **80-115 ore-uomo**, il 60-80% dell'intero budget di costruzione,
per ogni singolo lancio. §2.3: il criterio di chiusura dello scaglione minimo richiede che un lancio
vero apra e chiuda, quindi lo scaglione include quelle ore e la sua stima non le conta: **110-155
ore, non 30-40**. §2.5: il verificatore, i file di criterio dei tredici controlli, la migrazione del
reparto esistente e la scrittura dei cinquanta agenti (dieci passi ciascuno per procedura del piano
stesso, 17-25 ore) hanno **zero** ore allocate; e 235 file in 139-187 ore fanno 45 minuti a file.
*Caso:* si decide di costruire su un numero che è meno della metà del vero.
*Perché conta:* è il numero che decide se il sistema si ripaga, ed era assente.
*v4:* il primo giorno costa 6-10 ore, il primo più il secondo più il terzo stanno in tre giorni
(`00-LEGGIMI.md` §3), e la costruzione dell'ecosistema comincia **dopo** che un lancio vero è passato
di lì. Il costo di esercizio della macchina ha una voce obbligatoria e un tetto (F-11).

**G-30 · Una stima si contraddice nella stessa pagina, un'altra azzera il proprio margine.**
*Dove:* `CRITICA-C.md` §2.2 (il flusso Intelligence dichiara 16-30 ore e la somma delle sue fasi fa
26-33: chi pianifica sul 16 sbaglia del 60%) · `CRITICA-D.md` D-D-05 (30 ore-uomo consumano l'intera
finestra di quattro giorni assegnata a quel flusso, lasciando zero margine per il rifacimento che il
piano stesso dichiara normale) · `CRITICA-A.md` C-A-07 (quattro numeri diversi per la durata dello
stesso percorso: 20-30 ore, 3-5 giorni, ≤5 giorni, e la somma delle fasi ≥7 giorni) · `CRITICA-B.md`
§4.3 (tre unità di misura del tempo nei tre dossier dello stesso ecosistema, non confrontabili).
*Caso:* il numero di copertina è falso proprio per il caso di copertina, e diventa il bersaglio su cui
il flusso verrà giudicato fallito al primo giro.
*Perché conta:* una stima che il documento stesso smentisce non è una stima.
*v4:* le ore stanno in un posto solo (`04-COSTRUZIONE.md`), e le tre fasi del primo giorno hanno
ognuna il proprio intervallo con il criterio di chiusura accanto.

**G-31 · La condizione di abbandono scattava sul percorso nominale.**
*Dove:* `CRITICA-C.md` §2.4 — «il pilota non esce entro 60 giorni dall'inizio dello scaglione minimo
→ si ferma la costruzione», contro 17 giorni di calendario per lo scaglione più 38 giorni di
calendario di lancio: **55 giorni minimi con zero slittamenti**, mentre il calendario stesso mette da
parte 12 giorni di margine per rifacimenti che definisce normali.
*Caso:* restano 5 giorni di gioco contro 12 giorni di margine previsto: la condizione scatta al primo
rifacimento previsto dal piano.
*Perché conta:* un piano che si autoabbandona sul percorso nominale non ha una condizione di uscita:
ha un guasto.
*v4:* la condizione è **45 giorni** (`00-LEGGIMI.md` §7, riga 3) e non conta più la costruzione di
un'infrastruttura, perché non c'è infrastruttura prima del lancio. La causa è tolta, non il sintomo:
il perché di questa scelta, e non di quella proposta dal revisore, è in §4, R-01.

**G-32 · Le copertine erano il punto umano più frequente del piano e non comparivano in nessuna tabella dei punti umani.**
*Dove:* `CRITICA-B.md` D-B-19 — `06:339-340` («le copertine le fa una persona […] il piano editoriale
prepara titolo e indicazioni, apre la cartella, e si ferma») contro `05:286-294`, i sei punti umani
con scadenza, che non la contengono. Ogni riga del piano editoriale con un formato video è un punto
umano senza scadenza, sulla **stessa persona** che deve firmare il prezzo, approvare la promessa e
dare il via libera. La capacità umana totale non è mai sommata in nessuno dei tre dossier.
*Caso:* la metrica che il dossier chiama la propria ragione d'esistere — «contenuti prodotti che
vengono pubblicati: 100%» — è irraggiungibile per un collo di bottiglia che il dossier stesso dichiara
e non governa.
*Perché conta:* è la regola dell'Impero più frequente in assoluto, e il piano la citava senza contarla.
*v4:* `PU-COPERTINA` è una voce dei punti umani nel registro, con scadenza 3 giorni, nessun valore
predefinito possibile, e il comportamento allo scadere dichiarato: il pezzo resta in attesa e compare
nell'elenco di cosa blocca il lancio. La motivazione nel registro dice che era «il punto umano più
frequente dell'intero piano e non compariva in nessuna tabella».

**G-33 · Nessuno eseguiva le fasi «continue»: non esisteva un processo pianificato.**
*Dove:* `CRITICA-B.md` D-B-21 — `04:55` («il workflow si propone da solo»), `04:236-241` (la scala
dell'inerzia a 3/7/14 giorni), `06:79` («continuo»), `06:281` («ogni giorno controlla, ore:
automatico»). In nessuno dei tre dossier è nominato un processo che li esegua, né chi lo accende. Ed è
lo stesso difetto che `02:42-44` dichiara di aver corretto per la memoria.
*Caso:* nessuno digita il comando per tre giorni e il lancio è fermo senza che niente lo segnali —
che è esattamente il modo in cui il Manuale è rimasto fermo sei mesi, con più file attorno
(`CRITICA-A.md` B-A-08).
*Perché conta:* un sistema che si accorge dei problemi solo quando qualcuno lo interroga non si
accorge di niente.
*v4:* `01-ARCHITETTURA.md` §2.4 dichiara i tre momenti di invocazione, e il terzo è un promemoria
pianificato una volta al giorno sui lanci non chiusi, con la ragione scritta accanto.

## 3.6 Memoria

**G-34 · Il controllo della memoria verificava l'esistenza del record, non il suo contenuto.**
*Dove:* `CRITICA-A.md` D-A-06 — `02:299`: `verifica_fase(lancio_id, fase) -> bool`, «il record della
fase esiste?».
*Caso:* un record con corpo «ok», fonti vuote e nessun numero passa, e la fase chiude. Fra sei mesi
la memoria contiene undici righe «ok» e il piano dichiarerà di aver risolto il problema del reparto
precedente.
*Perché conta:* un booleano di esistenza si soddisfa con qualunque cosa: il presidio duro che era la
tesi centrale di due dossier era più debole del presidio morbido che sostituiva.
*v4:* `GATE-MEM-1` pretende che **ogni record di memoria della fase citi un artefatto esistente su
disco**, e ha come test rosso proprio quel caso: «un record di memoria con corpo "ok" e fonti vuote
deve BLOCCARE».

**G-35 · La fase zero si autoconvalidava, e la prova che citava non esisteva nello schema.**
*Dove:* `CRITICA-A.md` D-A-07 — `02:148-153` indica come prova un campo che lo schema dei record
(`02:116-127`) **non possiede**; e se lo possedesse, l'atto stesso di verificare incrementerebbe il
contatore, quindi il controllo produrrebbe la propria prova. In più il contatore così gonfiato
alimenta l'indice di salute della memoria: la macchina di verifica falsifica la propria metrica.
*Caso:* un agente esegue la ricerca nella memoria, ignora i risultati, e il controllo della prima
fase passa.
*Perché conta:* un controllo che si fabbrica da sé la propria prova non è un controllo.
*v4:* nessun controllo del registro accetta un dato prodotto da chi è giudicato: il campo
`dato_da_terzi` è obbligatorio per ognuno dei quattordici, e dice da dove arriva il numero.

**G-36 · La scadenza dei record era nulla per difetto, quindi la potatura non toccava niente.**
*Dove:* `CRITICA-A.md` D-A-25 e P-A-22 — `02:93` (scadenza nulla per difetto), `01:244` e `02:175`
(la potatura archivia i record scaduti **e** mai letti: una congiunzione quasi sempre falsa), più
`02:63` contro `01:186`: due valori diversi di ritenzione, e i «tipi» non enumerati da nessuna parte.
*Caso:* dopo tre lanci una cartella contiene 140 record scaduti mai, di cui 130 mai letti. La potatura
ne archivia zero e la memoria continua a crescere.
*Perché conta:* l'intero impianto contro il marciume della memoria era inerte per costruzione.
*v4:* la memoria dell'ecosistema è il debrief, che è un artefatto con schema, controllo e ramo di
fallimento — non una cartella di record generici che invecchiano. E la condizione di uscita numero 4
(`00-LEGGIMI.md` §7) la dichiara fallita se dopo due lanci nessuno schema ha cambiato una decisione.

**G-37 · La soglia del 40% era vera dal primo giorno e non aveva conseguenza.**
*Dove:* `CRITICA-A.md` D-A-26 e P-A-17 — `01:247` e `02:178-182`: sopra il 40% di record mai letti «la
sentinella lo segnala», contro `01:174-176`, dove il piano stesso condanna i presidi morbidi perché
«sono tutti saltabili senza che succeda niente».
*Caso:* al primo lancio la memoria è al 100% di mai letti per costruzione. L'allarme suona dal primo
giorno e non smette; viene ignorato entro due settimane e diventa rumore permanente.
*Perché conta:* una soglia senza conseguenza è una frase con un numero dentro, e il piano lo sapeva.
*v4:* nel registro non esistono soglie che «segnalano»: ogni controllo ha un `ramo_fallimento` e un
`exit_code`, e `INV-03` verifica che il ramo non sia vuoto.

**G-38 · Il passaggio scaduto diventava un blocco permanente, e la sospensione non fermava gli orologi.**
*Dove:* `CRITICA-A.md` D-A-08 (un passaggio scaduto valorizza un **campo**, non innesca nessuna
transizione: nessun cronometro, nessuna risalita di livello, nessun processo che lo osservi) · D-A-09 (la
sospensione può durare fino a 90 giorni, la validità dei passaggi è 48 ore: al rientro sono tutti
scaduti e il blocco si rivalorizza subito) · D-A-10 (48 ore solari in un'azienda che lavora a giorni,
senza nessun calendario dichiarato).
*Caso:* il lancio si sospende il 20/09 per la firma mancante e si riattiva il 15/10: rientra
nello stato di partenza e ogni passaggio pendente è scaduto da 23 giorni. L'uscita dalla sospensione
esiste sulla carta e restituisce a un blocco.
*Perché conta:* la correzione fiore all'occhiello del dossier 01 non funzionava per la sua causa
d'ingresso più frequente.
*v4:* il registro ha una sezione di tre righe che chiude il caso: `orologi: congelati_in:
["SOSPESO"], ripartono_da: "il valore che avevano all'ingresso in SOSPESO"`.

## 3.7 Stati, errori, osservabilità, obblighi di legge

**G-39 · Sospendere un lancio aperto non spegneva il carrello.**
*Dove:* `CRITICA-A.md` D-A-27 — `01:284` («da qualunque stato → SOSPESO»), `01:301-302` (aperto e
chiuso sono stati come gli altri), e nessuna transizione di ritorno da aperto a produzione.
*Caso:* giorno 2 di vendita, la consegna automatica smette di funzionare. Il piano non ha uno stato per
«vendita fermata»: si può solo sospendere, che non spegne il carrello, e tornare ad aperto, che non
prova che il guasto sia risolto.
*Perché conta:* è l'unico stato in cui il sistema tocca soldi veri di persone vere, e non aveva un
freno.
*v4:* la sospensione porta con sé `stato_di_partenza`, `revisione_il` e `come_si_esce` come comando
eseguibile, e gli orologi si fermano (G-38). Il presidio sul pagamento non agisce più solo prima
dell'apertura: la prova di cassa è dentro `GATE-FNL-1` e la sincronizzazione di `GATE-REG-1`
ricalcola la validità di tutti gli artefatti dai file, mai dallo stato.

**G-40 · Il rientro per sforamento poteva ciclare all'infinito e ignorava che la data era già pubblica.**
*Dove:* `CRITICA-A.md` D-A-28 — `01:297-298`: nessun contatore di rientri, nessuna uscita verso la
sospensione allo sforamento ripetuto, e nessuna regola su cosa succede quando la data è già stata
comunicata al pubblico. Stesso guasto in `CRITICA-D.md` D-D-02: «tre deroghe obbligano a rifare il
budget da capo» è scritto in prosa, senza contatore, senza controllo, e senza uno schema per il file
che dovrebbe contarle.
*Caso:* sforamento tre volte in due settimane: il lancio oscilla fra due stati mentre il calendario è
pubblico, e la decisione umana su annullare o rinviare non viene mai innescata, perché la macchina
considera il rientro una transizione automatica.
*Perché conta:* rientrare non annulla una promessa fatta fuori.
*v4:* `GATE-TSR-2` ha un ramo di fallimento preciso — la spesa nuova si blocca, il lancio non muore —
e **lo sblocco richiede una firma umana tracciata**. `PU-SPESA` è un punto umano del registro, senza
valore predefinito, con la motivazione «impegna denaro vero».

**G-41 · Due transizioni non avevano nessuno che potesse innescarle.**
*Dove:* `CRITICA-A.md` D-A-29 (il ritorno dallo stato «pronto» ha una condizione, un autorizzatore
generico e nessun controllo che giri in quello stato: `GATE-REG-1` presidia l'ingresso, non la
permanenza) · D-A-30 (il codice di uscita 3 — errore d'ambiente, «riprovabile» — non ha posto nella
macchina a stati, non dice quante volte, con quale attesa, chi riprova, e a che punto un errore
d'ambiente ripetuto diventa un difetto da registrare).
*Caso:* il lancio entra in «pronto» il lunedì e apre il venerdì. Giovedì la pagina di pagamento si
rompe: nessun controllo è previsto per accorgersene, quindi la transizione progettata per questo caso
non si attiva mai. Oppure: la verifica gira mentre la rete è giù, esce 3, e il giorno dopo nessuno sa
che il tentativo c'è stato.
*Perché conta:* una transizione senza soggetto che la inneschi è documentazione, non meccanica.
*v4:* la tabella delle transizioni del registro dichiara per ognuna **chi autorizza**, e il ritorno da
«pronto» a «in produzione» è autorizzato dal controllo che rifiuta. Il codice 3 ha un posto scritto:
`01-ARCHITETTURA.md` §2.2 e §7 dicono cosa lascia sul disco e cosa succede al tetto di spesa esaurito,
al fornitore che non risponde e all'agente che muore a metà.

**G-42 · Nessuna osservabilità: non c'era modo di sapere cosa stesse facendo il sistema mentre gira.**
*Dove:* `CRITICA-C.md` D-C-12 — nei dossier 07, 08, 09, 10 non compaiono mai le parole registro degli
eventi, tracciamento d'esecuzione, telemetria; «cruscotto» compare tre volte e sempre riferito ai
numeri di vendita, mai allo stato del sistema. Manca un registro degli eventi, un identificativo di
correlazione, una misura di durata e consumo per invocazione (che `08:302` promette senza dire dove si
scrive), e una diagnosi di perché il lancio è fermo, da quanto, in attesa di chi. Aggravante in
`CRITICA-A.md` P-A-20: la scala dei tempi di risalita esiste, e `01:87` dichiara «il file esiste,
quindi la Direzione lo vede: niente notifiche da costruire» — scambiando la persistenza per la consegna.
*Caso:* a nove giorni dall'apertura il lancio è ancora in produzione e nessuno sa se un controllo ha
bloccato, se un agente è morto a metà, o se nessuno ha eseguito il comando.
*Perché conta:* un sistema che si guarda solo alla fine si scopre rotto alla fine.
*v4:* `01-ARCHITETTURA.md` §8: una riga in `registro-chiamate.jsonl` per ogni invocazione, un verbale
per ogni verdetto anche quando passa, `lancio elenco`, `lancio costi <id>` e **`lancio blocchi`**, che
elenca tutti i punti umani aperti ordinati per giorni di attesa. È il comando che rende visibile il
problema vero di questa azienda: non i lanci che vanno male, ma quelli che non partono.

**G-43 · Nessun obbligo di legge: recesso, consenso, dati delle persone reali.**
*Dove:* `CRITICA-D.md` §6.5 (si archiviano citazioni testuali di persone reali con l'indirizzo, per
dodici mesi, senza base giuridica, anonimizzazione né diritto alla cancellazione) · `CRITICA-A.md`
B-A-28 (i dati dei collaudatori esterni: dove vivono, per quanto, e se finiscono in uno spazio a
ritenzione permanente — non una riga) · `CRITICA-B.md` B-B-12 (garanzia a 14 giorni e carrello a 5:
il numero vero si conosce 19 giorni dopo la chiusura, e nessuna riga lo dice).
*Caso:* il debrief certifica un risultato che non è ancora accaduto, e l'azienda conserva dati di
persone senza sapere con quale titolo.
*Perché conta:* non sono raccomandazioni: sono obblighi, e l'unico modo di scoprirli tardi è caro.
*v4:* `01-ARCHITETTURA.md` §9 ha una tabella dedicata — credenziali, dati dei clienti fuori dal
repository, diritto di recesso con il consenso esplicito alla rinuncia raccolto al momento del
pagamento, documento fiscale per ogni vendita, quota di consenso alla misura da dichiarare, contenuti
generati da dichiarare. Il primo è già nello schema: `offerta.schema.json` porta
`rinuncia_recesso_raccolta`, con la nota «se false, il rimborso resta dovuto per 14 giorni: va saputo
prima di fare i conti, non dopo il primo rimborso».

**G-44 · Una credenziale in chiaro nel repository, pubblica da mesi e mai sostituita.**
*Dove:* `INCASSO.md` §2 — la chiave del servizio di posta è scritta nel codice lato cliente ed è
duplicata in almeno altri tre file; il repository è pubblico da quando esiste; la voce di arretrato
B-020 è ancora aperta. Nessuno degli undici dossier della v3 la nomina.
*Caso:* chiunque abbia il collegamento può scrivere sulla lista contatti dell'azienda — che è
l'unico pubblico posseduto che l'azienda abbia.
*Perché conta:* è il pubblico su cui poggia ogni previsione di ricavo (F-08).
*v4:* è il **gesto numero 0 del giorno zero**, prima di qualunque altra cosa (`00-LEGGIMI.md` §3.1),
con il criterio di riuscita scritto: la vecchia chiave non funziona più sul servizio. E
`01-ARCHITETTURA.md` §9 spiega perché va cambiata **sul servizio** e non nel file: la storia del
repository resta leggibile.

**G-45 · L'ADR descriveva invece di decidere, e disponeva di un bene altrui.**
*Dove:* `CRITICA-C.md` D-C-14 e `CRITICA-D.md` §4 — degli otto punti della decisione, quattro
descrivono ciò che i dossier hanno già specificato, e uno di quelli riporta un numero sbagliato (i
tredici controlli, che sono quattordici). Il punto sullo spostamento del reparto esistente ammette da
sé che «serve il consenso del suo proprietario», consenso che l'ADR non ha, non chiede, e il cui
titolare non è nemmeno nominato. E manca del tutto la clausola di superamento: se scattano le
condizioni di abbandono, l'ADR resterebbe in vigore a governare un ecosistema abbandonato.
*Caso:* fra sei mesi chi vuole cambiare il numero dei reparti non contraddice una decisione: aggiorna
una descrizione.
*Perché conta:* un ADR che riassume i dossier non vincola nulla, ed è esattamente il tipo di atto che
la Memoria dell'Impero esiste per evitare.
*v4:* l'ADR-023 è un documento a sé (`05-ADR-023.md`), la parte descrittiva vive nel registro che si
valida da solo, e le decisioni che aspettano una persona sono elencate e dichiarate aperte in
`00-LEGGIMI.md` §4 invece di essere prese per silenzio dentro un atto.

---

# 4. I RILIEVI CHE HO RESPINTO — e perché

Duecentouno rilievi non sono duecentouno correzioni. Alcuni erano fondati e curavano il sintomo
invece della causa; altri riguardavano meccanismi che la versione 4 ha eliminato del tutto; altri
ancora chiedevano all'ecosistema di occuparsi di cose che non sono sue. Un documento che accetta
ogni critica non ha giudizio, e chi legge non può più distinguere una scelta da una resa.

Otto rifiuti, con la ragione accanto.

---

**R-01 · «Alzare il tetto della condizione di abbandono a circa 100 giorni.»**
*Chi lo chiede:* `CRITICA-C.md` §2.4.
*La diagnosi era giusta:* con lo scaglione minimo a 17 giorni di calendario più 38 giorni di
lancio, il tetto di 60 giorni scattava al primo rifacimento previsto dal piano stesso (è G-31).
*Perché l'ho respinto:* la riparazione proposta cura il sintomo. Il problema non era che il tetto
fosse basso: era che il piano spendeva quasi tutta la propria condizione d'uscita in
infrastruttura, **prima** di aver provato la sola ipotesi che conta — che il collo di bottiglia sia
davvero organizzativo (`CRITICA-EMPERATOR.md` E-04). Alzando il tetto si compra tempo per
continuare a costruire senza sapere.
*Cosa ho fatto invece:* il tetto **scende** a 45 giorni (`00-LEGGIMI.md` §7, riga 3), e non conta
più la costruzione di un'infrastruttura, perché non c'è infrastruttura prima del lancio. Fermarsi
è diventato più facile, non più difficile.

---

**R-02 · «Il giudice dei testi non riceve la soglia, non sa chi ha scritto il pezzo, e il 10% dei
pezzi viene rigiudicato alla cieca con la concordanza scritta in memoria.»**
*Chi lo chiede:* `CRITICA-B.md` D-B-07.
*La diagnosi era giusta:* 58 punti su 100 sono giudizio, il giudice conosce la soglia, e senza
ancore due esecuzioni dello stesso giudice non sono riproducibili.
*Perché l'ho respinto, per ora:* il 10% di quattordici pezzi fa **1,4 pezzi**. Un campione che non
misura niente, e che raddoppia il costo di ogni giudizio in un sistema che ha una tassa fissa per
invocazione e un tetto di 15 $ per lancio (F-11). La concordanza fra giudici è una misura che ha
senso quando c'è una popolazione: si fa al secondo o terzo lancio, non al primo.
*Cosa ho tenuto:* la parte che costa zero e serve subito — le **ancore** sono un campo dello
schema (`copy.schema.json`, campo `ancora`), e `GATE-CPY-1` non guarda solo il totale: boccia se un
blocco sta sotto il 50% dei propri punti, così un punteggio alto non può nascondere un pezzo
vuoto. Il resto entra quando ci saranno due lanci da confrontare.

---

**R-03 · «Sopprimere l'agente giudice: tutti i controlli sono script.»**
*Chi lo chiede:* `CRITICA-C.md` §1.4 e §1.6 (che propone di scendere a ~21 agenti e cinque moduli),
`CRITICA-D.md` §1 e §8.3.
*La diagnosi era giusta, e l'ho accolta quasi tutta:* quindici agenti erano funzioni travestite
(G-22), e nella versione 4 gli agenti sono **quindici in tutto**, meno dei ventuno proposti.
*Perché ho respinto la parte finale:* due controlli non sono calcolabili. `GATE-INT-1` richiede di
**riaprire una fonte e cercarci dentro una frase** — e il rapporto stesso ammette che quel controllo
resta statistico, non una prova. `GATE-CPY-1` ha una parte di giudizio che nessuna condizione
esprime. Un sistema di controlli interamente scriptato su questi due sarebbe un sistema che
controlla ciò che è facile controllare, e questo è il modo in cui i controlli diventano decorativi.
*Cosa ho fatto:* `lan-gate` resta un agente, di grado intermedio, **e non ha la penna** (`INV-09`).
I verbali li scrive lo script. Il giudizio è di un agente, la scrittura di un programma.

---

**R-04 · «Le scadenze dei passaggi di consegne vanno calcolate in giorni lavorativi, da un
calendario dichiarato.»**
*Chi lo chiede:* `CRITICA-A.md` D-A-10.
*La diagnosi era giusta:* 48 ore solari in un'azienda che lavora a giorni significa che un
passaggio emesso il venerdì sera scade la domenica, e il lunedì il lancio è bloccato senza che sia
successo niente.
*Perché l'ho respinto:* è un rilievo su un meccanismo che **non esiste più**. Nella versione 4 non
ci sono passaggi di consegne con scadenza e criterio di accettazione in prosa: gli artefatti
dipendono l'uno dall'altro per `dipende_da`, e la validità si ricalcola dai file. Riparare un
meccanismo che è uscito dal piano avrebbe aggiunto un calendario di festività a un sistema che non
ne ha bisogno.
*Cosa resta del rilievo:* la lezione, applicata dove il tempo conta ancora — i punti umani. Le
scadenze lì sono in giorni (7, 14, 3), non in ore, e gli orologi si fermano in sospensione
(`registro.yaml`, sezione `orologi`).

---

**R-05 · «Portare l'elenco a quattordici controlli e marcare GATE-TSR-3 come non bloccante al
primo lancio, con la data in cui diventa bloccante.»**
*Chi lo chiede:* `CRITICA-C.md` D-C-11.
*La diagnosi era giusta, ed è accolta per metà:* i controlli sono quattordici, non tredici (G-02).
*Perché ho respinto la seconda metà:* il rapporto dimostra da sé che quel controllo, sul primo
lancio, **non può fallire**, perché i registri della Tesoreria dell'Impero sono a zero righe
(verificato in `INCASSO.md` §1) e il criterio ha un ramo che dichiara il primo popolamento. Un
controllo che per costruzione non può bloccare è, per la definizione del registro stesso,
decorativo — e `INV-04` esiste apposta per non farlo entrare.
*Cosa ho fatto:* il quattordicesimo controllo esiste, ma è `GATE-PUB-1` (F-02) — che blocca
davvero, e ha un test rosso. La riconciliazione con la Tesoreria non è un controllo di questo
ecosistema: è il confine con l'anello successivo, dichiarato in `registro.yaml`
(`mandato.anello_successivo`, ADR-020).

---

**R-06 · «La finestra dei rimborsi deve entrare nel debrief: con garanzia a 14 giorni e carrello a
5, il numero vero si conosce 19 giorni dopo la chiusura.»**
*Chi lo chiede:* `CRITICA-B.md` B-B-12.
*Il fatto è vero e va saputo.*
*Perché l'ho respinto come compito di questo ecosistema:* il confine è scritto e vale anche quando
è scomodo — *«se un'attività continua dopo la chiusura del carrello, non è di questo ecosistema»*
(`01-ARCHITETTURA.md` §10). Un rimborso è un movimento di cassa che avviene fino a due settimane
dopo, e la fonte di verità sui soldi è la Tesoreria: se un numero compare in tutti e due i posti
ed è diverso, ha ragione la Tesoreria.
*Cosa ho fatto perché il fatto non si perda:* è un dato **dichiarato in ingresso**, non un compito
in uscita. `offerta.schema.json` porta `rinuncia_recesso_raccolta`, con la nota che spiega
l'effetto: se il consenso alla rinuncia non è raccolto, il rimborso resta dovuto per 14 giorni e
va saputo **prima** di fare i conti, non dopo il primo rimborso.

---

**R-07 · «Spezzare l'ottimizzatore in due: presidio durante il lancio e apprendimento fra un
lancio e l'altro.»**
*Chi lo chiede:* `CRITICA-B.md` D-B-17.
*La diagnosi era giusta:* con un carrello di cinque giorni e un pubblico piccolo non si raggiungono
i volumi per una sola decisione, quindi il risultato di quell'agente è per costruzione «non si sa
ancora» — e il dossier lo prescriveva pure.
*Perché ho respinto la riparazione:* è più timida della conseguenza. Se un ruolo non può produrre
una decisione, non si spezza in due: si toglie.
*Cosa ho fatto:* nella versione 4 non esiste nessun artefatto di prova comparativa e nessun agente
di ottimizzazione. Il presidio tecnico durante la vendita è quello che serve davvero — le pagine
rispondono, l'evento arriva, la cassa incassa — ed è già dentro `GATE-FNL-1`. L'apprendimento è il
debrief, con gli scarti spiegati (`GATE-MEM-1`).

---

**R-08 · «Sganciare le fondamenta dei testi dal prezzo.»**
*Chi lo chiede:* `CRITICA-B.md` S-06, che la elogia come «la correzione più intelligente dei tre
dossier».
*Perché l'ho respinta:* era la cura giusta per una malattia che la versione 4 non ha più. Nella v3
i testi partivano prima del prezzo perché il prezzo arrivava dopo mesi, e sganciarli evitava che il
blocco si propagasse. Nella versione 4 **il prezzo arriva al terzo giorno** (`00-LEGGIMI.md` §3.3),
prima di qualunque testo. Tenerli sganciati oggi significherebbe conservare il difetto che lo
stesso rapporto segnalava altrove: testi scritti su un'offerta che poi cambia, senza che niente li
invalidi (D-B-11, cioè G-17).
*Cosa ho fatto:* `ART-CPY` dipende da `ART-OFF` e da `ART-RIC` (`registro.yaml`, campo
`dipende_da`). Se l'offerta cambia, i testi diventano `da_rivedere` e il loro controllo si riapre.

---

# 5. LE COSE CHE LA VERSIONE 3 AVEVA GIUSTE — e che la 4 ha tenuto

La versione 3 è il lavoro di una giornata su un problema che l'azienda si porta da mesi, e i
quattro revisori hanno segnalato **46 punti solidi** oltre ai difetti. Non sono cortesie: diverse
di quelle idee sono il motivo per cui la versione 4 ha potuto essere scritta in un giorno invece
che in dieci, perché il pensiero difficile era già fatto.

Qui ci sono quelle che la versione 4 ha preso e portato dentro, con dove sono finite.

| # | Cosa aveva visto la v3 | Chi la difende | Dove vive nella v4 |
|---|---|---|---|
| 1 | **«Un gate posto su una decisione umana deve arrivare con la decisione già istruita: "decidi" delega la fatica, "confermi questo?" la toglie»** (`04:26-28`) | `CRITICA-B.md` S-01 e `CRITICA-EMPERATOR.md` D.1, che la chiamano la pagina migliore del pacchetto | è la forma della firma del terzo giorno, arricchita col ricavo atteso (`00-LEGGIMI.md` §3.3) |
| 2 | **La forma della proposta**: numero già dato, due alternative **con la conseguenza accanto**, blocco «NON SO» esplicito, domanda binaria con la via d'uscita (`04:145-179`) | `CRITICA-B.md` S-02 («tenerla parola per parola») | tenuta parola per parola, con il ricavo previsto accanto a ogni alternativa |
| 3 | **La reversibilità come criterio di scelta** (`04:128`) | `CRITICA-B.md` S-03 | è la giustificazione scritta del valore predefinito di `PU-RUOLO` nel registro: fra due strade si prende quella da cui si torna indietro |
| 4 | **La lista dei valori evasivi** — «da definire», «non lo so», «tbd», «presto», «prossimamente», vuoto (`04:220-228`) | `CRITICA-B.md` S-05, «implementabile in un'ora, cattura un fallimento reale» | `GATE-OFF-1`: `prezzo non in lista_valori_evasivi` |
| 5 | **Il ricalcolo dai file, mai dai JSON di stato** (`03:178`, `03:235`) | `CRITICA-A.md` S-A-01, «l'idea migliore dei tre dossier» | è una delle tre garanzie di `lancio avanza` (`01-ARCHITETTURA.md` §2.3) ed è il `dato_da_terzi` di `GATE-REG-1` |
| 6 | **La sospensione che porta con sé il proprio antidoto**: stato di partenza, data di revisione mai vuota, e l'uscita come **comando eseguibile** (`01:319-334`) | `CRITICA-A.md` S-A-02, `CRITICA-D.md` §7 | stato `SOSPESO` nel registro, completato con gli orologi che si fermano (G-38) |
| 7 | **La convenzione dei codici di uscita**: 0 passa · 1 blocca con verbale · 2 ingresso non valido con **zero file scritti** · 3 ambiente (`03:247-249`) | `CRITICA-A.md` S-A-06, «corretta, discrimina i casi giusti» | campo `exit_code` di ogni controllo e §2.2 di `01-ARCHITETTURA.md`, con la distinzione fra 2 e 3 spiegata |
| 8 | **«Ogni dato assente dichiarato, mai stimato»** (`03:203`) | `CRITICA-A.md` S-A-05 e `CRITICA-B.md` S-04 | `GATE-PRV-1`: ogni assunzione è `misurato` o `assunto`, e una assunzione non può essere prova |
| 9 | **La Regia produce, la Memoria giudica, e nessuno dei due scrive da solo la storia** (`01:111-114`) | `CRITICA-A.md` S-A-09, «l'unico punto in cui la regola viene davvero rispettata» | `ART-DBR` con `controfirma`, e la nota nel registro che spiega perché la controfirma è un **campo** e non un ruolo di giudice |
| 10 | **«Pronto dichiarato» non è «pronto certificato»**, e il percorso per i prodotti già finiti salta la produzione ma **mai** la certificazione (`03:143-148`) | `CRITICA-A.md` S-A-08, «la frase più utile dei tre dossier» | `ART-CRT` in modalità retroattiva, che salta il collaudo integrale solo dichiarando il debito (F-03) |
| 11 | **L'eccezione progettata invece che improvvisata**: attestazione firmata, a scadenza, con un debito scritto (`01:416-436`) | `CRITICA-EMPERATOR.md` D.6 | `debito_collaudo`, obbligatorio nello schema quando la modalità è retroattiva |
| 12 | **L'ingresso tipizzato con la colonna «se manca» e la regola del caso peggiore** (`03:100-113`) | `CRITICA-A.md` S-A-14, «l'unico blocco che un costruttore può implementare senza inventare una riga» | generalizzato a tutti: `se_fallisce` mai vuoto su ogni artefatto (`INV-03`) |
| 13 | **Tre criteri di collaudo veri e implementabili**: il file esiste ed è maggiore di zero byte, ogni modello ha il proprio esempio, ogni collegamento testato con esito registrato **per collegamento** (`03:176`, `03:277-279`) | `CRITICA-A.md` S-A-07, «la prova che il piano sa scrivere un criterio quando vuole» | `GATE-PRD-1`, con i collegamenti testati **dal controllo** e non dichiarati dal produttore |
| 14 | **La tabella «output · chi lo produce · chi lo valida · da chi dipende»** (`01:100-111`) | `CRITICA-A.md` S-A-10, «la forma giusta, da usare come indice generale del sistema» | è diventata la **struttura** del registro: la sezione degli artefatti è quella tabella, resa dato e verificata da `INV-01` |
| 15 | **Il declassamento degli schemi e il campo «si applica quando»** (`01:238`, `02:139-141`) | `CRITICA-A.md` S-A-04, «una memoria che può solo salire è una superstizione con la data» | `GATE-MEM-1`: ogni schema deve avere `si_applica_quando` non vuoto |
| 16 | **La prova di pubblicazione è l'indirizzo, non il codice di uscita** (`06:255-259`) | `CRITICA-B.md` S-10, nata da un fatto reale: uno strumento che stampa «SIMULATA» ed esce zero | `GATE-FNL-1`: ogni pagina risponde 200, e l'evento si legge dalla piattaforma |
| 17 | **Traffico organico e a pagamento non si mescolano** (`06:52-56`) | `CRITICA-B.md` S-11, «mescolarli rende ogni numero successivo una divisione fra grandezze scollegate» | `consuntivo.schema.json`, campo `per_canale`, con la ragione scritta nello schema |
| 18 | **Legare le varianti al traffico disponibile** (`05:229-240`), «aver ucciso 196 varianti inutili» | `CRITICA-B.md` S-08 | portato all'estremo: nessun artefatto di prova comparativa esiste più (§4, R-07) |
| 19 | **Il reparto editoriale ordina e verifica, non produce** (`06:335-336`) | `CRITICA-B.md` S-14, «confine giusto, coerente col resto dell'Impero» | `ART-EDT` ha destinazioni risolvibili contro il funnel: ordina e verifica |
| 20 | **La risalita che muore contro un controllo**: se una delle due posizioni viola un controllo esistente, non è un conflitto, vince il controllo (`01:88-89`) | `CRITICA-A.md` S-A-03, «uccide metà dei conflitti senza riunioni» | conservata: nella v4 le transizioni dichiarano chi autorizza, e il controllo che rifiuta autorizza il ritorno indietro |
| 21 | **Le condizioni di abbandono con soglie numeriche** (`09:206-219`) | `CRITICA-D.md` §7 e `CRITICA-EMPERATOR.md` D.5, «la maggior parte dei piani non ne ha nessuna» | erano tre, ora sono **quattro** (`00-LEGGIMI.md` §7), e la prima è nuova ed è la più importante |
| 22 | **«Un sistema di controlli che non ha mai bloccato non è provato»** (`10:139-144`) | `CRITICA-D.md` §7, «controintuitivo e corretto, raro trovarlo scritto in un piano» | è diventato un invariante: `INV-04`, ogni controllo ha un test rosso dichiarato |
| 23 | **«Un agente scritto solo in una cartella di reparto è una specifica, non un agente»** (`01:476-482`) | `CRITICA-A.md` S-A-13, «diagnosi esatta di un guasto reale e verificato» | il registro elenca gli agenti con grado, modello e strumenti: la specifica e l'agente sono lo stesso dato |
| 24 | **Aver verificato il riuso invece di dichiararlo**: aver misurato che cinque componenti non accettano parametri e aver dichiarato che il piano stesso aveva scritto un contratto inesistente (`05:301-320`, `06:214-227`) | `CRITICA-B.md` S-09, «il comportamento più sano dei tre documenti» | tenuto come metodo: ogni misura di questo pacchetto porta la data e il comando accanto |
| 25 | **Il divieto della parola «pianificato» senza data e nome** (`09:1`) | `CRITICA-EMPERATOR.md` D.8 | tenuto |
| 26 | **La nota d'apertura a Gael** | `CRITICA-EMPERATOR.md` D.9, «risolve un problema umano vero» | riscritta per la v4 in apertura di `00-LEGGIMI.md`; l'originale in `_v3-superata/00-LEGGIMI-GAEL.md` |

**Una cosa va detta senza attenuarla:** la diagnosi centrale della versione 3 — *«non c'è un buco
di capacità, c'è un buco di decisione ed esecuzione»* — è **giusta**, ed è la ragione per cui la
versione 4 non riscrive nessuna delle undici skill già funzionanti. Era incompleta, non falsa:
sotto quei due buchi ce n'era un terzo, l'infrastruttura per incassare (F-01). La correzione della
diagnosi è in `00-LEGGIMI.md` §1, e riconosce entrambe le cose.

---

# 6. I FATTI NUOVI EMERSI DALLA CRITICA — che nessuno sapeva

Quattro fatti che non stavano in nessun documento del piano, in nessun checkpoint e in nessuna
pagina della wiki come problema riconosciuto. Sono venuti fuori indagando, non leggendo. Ognuno
cambia una decisione.

---

## 6.1 Il canale di traffico del prodotto pilota è stato spento il 29/07/2026 e dirottato altrove

**Dove è stato trovato.** `second-brain-vault/wiki/log.md`, righe 1054-1063, voci del 2026-07-29 e
2026-07-31. Portato alla luce da `CRITICA-EMPERATOR.md` E-10 e confermato da `ORIGINE.md` §5.
Testuale: *«il primo contenuto YouTube reale generato era ancora sul funnel morto "Manuale Claude
Code" — pivot deciso da Gael a @dosementale come canale sorgente»*, e *«`apex7_orchestrator.py`
(F1-F5) riscritto per intero su @dosementale — prima era solo il contenuto ad essere cambiato, il
motore restava cablato sul Manuale Claude Code»*.

**Perché nessuno lo sapeva.** Perché è registrato come **correzione tecnica di un motore**, non
come decisione commerciale. Chi ha scritto il piano ha letto il catalogo prodotti, la wiki del
prodotto e i documenti di ricognizione: in tutti e tre il Manuale è «pronto, manca prezzo e data».
Nessuno di quei documenti è stato aggiornato quando il canale è stato dirottato.

**Cosa cambia.** Tutto l'ordine del piano. Il primo controllo del sistema non è più «questa idea
merita?» ma **«quante persone possiamo mettere davanti all'offerta, e con quale prova?»**
(`ART-PUB`, `GATE-PUB-1`, F-02). E diventa una condizione d'uscita: totale verificato a zero, si
smette e si va a costruire pubblico — informazione che, come dice `00-LEGGIMI.md` §7, «vale più di
dodici reparti costruiti bene e mai usati».

**Cosa resta aperto, e va detto:** `ORIGINE.md` §7 dichiara di **non aver potuto determinare** se
esista oggi un canale o un motore di traffico dedicato al Manuale diverso da quello dirottato. Non
c'è una risposta nelle fonti lette. È esattamente ciò che il giorno uno della versione 4 va a
misurare.

---

## 6.2 Lo stesso prodotto ha quattro prezzi diversi in quattro fonti, mai messe sullo stesso tavolo

**Dove è stato trovato.** `CRITICA-EMPERATOR.md` E-11, che le mette in tabella per la prima volta:

| Fonte | Valore | Data |
|---|---|---|
| catalogo prodotti (`CATALOGO PRODOTTI ATTUALE`) | «€ NON LO SO» | 07/03/2026 |
| wiki archiviata, scheda del prodotto | «TBD (**€297-€497** recommended)» | 29/04/2026 |
| `PRODUCT_LADDER.md`, cinque fasce recuperate dalla ricognizione L2 | fasce €97-297 / €497-997 | — |
| dossier 04 del piano v3 | **47 €**, «livello 1 (7-47 €)» | 05/09/2026 |

**Perché nessuno lo sapeva.** Le quattro fonti vivono in quattro posti che nessuno legge insieme:
un catalogo, una pagina di archivio della wiki, un file di formazione assorbito e il piano nuovo.
Il dossier che propone 47 € **non cita né la seconda né la terza**, e costruisce la propria
giustificazione su un solo listino.

**Cosa cambia.** La proposta di prezzo non può nascere da un listino solo. E c'è una cosa più
imbarazzante del non sapere quanto vale il prodotto: **saperlo in quattro modi diversi e non
essersene mai accorti.** Il blocco «NON SO» della proposta v3 — che è un'ottima invenzione —
dichiarava «quanto è disposto a pagare questo pubblico non è mai stato misurato», e taceva questo.

**Un quinto valore, trovato dall'altra indagine.** `INCASSO.md` §6 riporta che il prezzo **è stato
deciso**: `DEC-EST-001-b-003`, riga 15, decisione del 2026-07-21 passata per silenzio-assenso, **67
€ di lancio e 97 € di listino**, coincidente con `checkout.config.json`. La finestra di lancio
dichiarata lì — 31/07/2026 — è scaduta da oltre un mese senza che il pagamento sia mai stato
attivato. Il conto di `00-LEGGIMI.md` §1 dice «quattro valori», ed è il conto del revisore in E-11;
con questo sono cinque, e il quinto è l'unico che sia mai stato una decisione formale. **Nessuno
degli undici dossier della v3 lo cita.**

**Cosa fa la versione 4.** La riconciliazione delle fonti di prezzo esistenti è un passo obbligato
prima della proposta, e la proposta deve dire perché si discosta da ciascuna. Un prezzo proposto
senza guardare i prezzi che l'azienda si è già data non è istruito: è inventato con più pagine.

---

## 6.3 Esisteva già un piano di lancio per questo prodotto, con obiettivo 30/05/2026, ed è morto in silenzio

**Dove è stato trovato.** `second-brain-vault/wiki/09 - Archives/legacy/projects/
Claude_Code_Mastery_Launch.md`, creato il 2026-04-29, letto da `ORIGINE.md` §5 e portato come
rilievo in `CRITICA-EMPERATOR.md` E-12. Contiene una tabella di marcia esplicita — *«START
2026-04-29 → TARGET SHIP 2026-05-30»* — con titolare dichiarato (Max), perimetro, e tre traguardi
datati: 07/05 script e analisi dei concorrenti, 15/05 pagina d'ingresso online e due o tre video pubblicati,
30/05 funnel completo e primi 50 iscritti alla prova.

**Perché nessuno lo sapeva.** Perché **nessun documento registra il mancato rispetto**. La data
obiettivo è passata da oltre tre mesi, e nessuna fonte letta conferma che uno solo dei tre
traguardi sia stato raggiunto. Non c'è un debrief, non c'è un archivio con la ragione, non c'è una
riga in Memoria. La conclusione è una deduzione dalle date, non una dichiarazione di qualcuno — e
questo è precisamente il punto.

**Cosa cambia.** Un ecosistema che nasce per curare l'incapacità di lanciare aveva, a disposizione,
**il caso di studio più vicino che l'azienda possieda**, e non lo ha aperto. Il rischio, senza,
è ricostruire lo stesso piano con più reparti attorno.

**Cosa fa la versione 4.** Rende impossibile che si ripeta, in due modi. Primo: uno stato di
sospensione non esiste senza data di revisione e senza il comando per uscirne, e dopo 90 giorni la
proposta di chiusura sale a Max (`registro.yaml`, transizioni). Secondo: `APPRESO` è **l'unico
finale buono** dei dodici stati, e ci si arriva solo con un consuntivo verificato e un debrief con
gli scarti spiegati. Un lancio che muore senza debrief non è chiuso: è fermo, e si vede.

---

## 6.4 Non esiste nessun modo automatico di incassare, e i registri economici dell'azienda sono a zero righe

**Dove è stato trovato.** `INCASSO.md`, per intero. È l'indagine che ha cambiato di più il piano.
Le prove, con il percorso:

| Fatto | Prova |
|---|---|
| Nessun canale di pagamento attivo per il prodotto pilota | `checkout.config.json` righe 7-33: tutti a `"attivo": false`; l'unico attivo è l'ordine per email |
| Il passaggio d'acquisto è un collegamento di posta | `pagamento.html` righe 190, 197, 375 |
| La pagina di vendita non è online | nessun file di pubblicazione nella cartella, verificato due volte (Memory e disco) |
| Una chiave di pagamento reale esiste, ma per un altro prodotto e senza nessun bottone collegato | `KDP - prodottti digitali\Leanding Page\email-agent\.env` e le sei pagine d'ingresso di quel prodotto, dove la ricerca dà zero risultati |
| Nessun tracciamento installato su nessun sito verificato | ricerca mirata su tutte le pagine d'ingresso: zero occorrenze reali |
| I registri economici sono vuoti | `entrate.jsonl` e `spese.jsonl`: **zero righe** entrambi |
| L'azienda lo dichiara di sé | `STATO-EMPIRE.md` righe 9007-9010, voce B-043, 2026-09-03: *«Digital Empire non misura un solo euro»* |

**Perché nessuno lo sapeva.** Lo sapevano tutti, a pezzi, e nessuno insieme. La voce B-043 è del
2026-09-03, due giorni prima del piano. Il fatto nuovo non è nessuno dei sette: è che **messi in
fila dicono una cosa sola**, e quella cosa contraddice l'ipotesi su cui il piano era costruito.

**Cosa cambia.** L'ordine di tutto. Non si costruisce un ecosistema sopra un'azienda che non può
ricevere un pagamento: si costruisce la cassa, in sei gesti, e la si prova con un euro vero che
entra, consegna e torna indietro (`00-LEGGIMI.md` §3.1). Poi si conta il pubblico. Poi si fa la
previsione e si firma il prezzo. **Solo dopo** comincia l'ecosistema, e comincia sui difetti
misurati di quel lancio invece che su una previsione (`00-LEGGIMI.md` §3.4).

**La sintesi, dall'indagine stessa:** *«Digital Empire può oggi, al massimo, ricevere un ordine per
email e consegnarlo a mano — non esiste un solo percorso automatico, collaudato e misurato che
porti da "qualcuno vede una pagina" a "un euro è arrivato e il prodotto è stato consegnato".»*

---

# 7. LA TABELLA DI CORRISPONDENZA — dove è finito ogni difetto

Copre tutti i 57 difetti citati nelle §2 e §3. La colonna che conta è l'ultima: **come si verifica
che sia davvero risolto**. Non «è stato riscritto» — un comando, un invariante o un test costruito
apposta perché fallisca.

Il comando che vale per tutta la colonna degli invarianti è uno solo:

```bash
cd PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati
PYTHONIOENCODING=utf-8 python valida_registro.py
# 253 controlli eseguiti → PIANO COERENTE   (uscita 0; qualunque altro valore = non si costruisce)
```

Dove la verifica è «test rosso», si intende il caso dichiarato nel campo `test_rosso` di quel
controllo dentro `dati/registro.yaml`: **se quel caso non fa bloccare il controllo, il controllo è
decorativo** e la riparazione non è avvenuta.

## 7.1 I dodici fatali

| Difetto | Grado | Dove è risolto nella v4 | Come si verifica |
|---|---|---|---|
| **F-01** L'azienda non può incassare | fatale | giorno zero (`00-LEGGIMI.md` §3.1) · prova di cassa dentro `GATE-FNL-1` · `ART-FNL.nota_cassa` | test rosso di `GATE-FNL-1`: *un funnel con tutte le pagine a 200 e senza transazione di prova deve bloccare*. Prova esterna: il rimborso compare nel pannello del fornitore |
| **F-02** Il canale di traffico spento | fatale | `ART-PUB` (primo artefatto, `dipende_da: []`) · `GATE-PUB-1` · `pubblico.schema.json` | test rosso di `GATE-PUB-1`: *tre canali tutti a `raggiungibili_verificati=0` devono bloccare*. Condizione d'uscita 2 di `00-LEGGIMI.md` §7 |
| **F-03** Il pilota non entra nel proprio flusso | fatale | `ART-CRT.modalita_ammesse: [integrale, retroattiva]` · `GATE-PRD-1` | validare un certificato con `modalita: "retroattiva"` **senza** `debito_collaudo` contro `certificato.schema.json` (regola condizionale, righe 53 e 63): deve essere rifiutato |
| **F-04** Il blocco vero senza scadenza | fatale | `PU-RUOLO` (7 giorni, predefinito `vendita`) · `ruolo_scelto_per_silenzio` · `lancio blocchi` | `INV-06` nel validatore: togliere `scadenza_giorni` a un punto umano senza motivazione fa uscire il validatore diverso da zero. E `offerta.schema.json` rifiuta `ruolo_prodotto: "non-deciso"` |
| **F-05** Correzione non propagata, sigle divergenti, blocco circolare | fatale | `dati/registro.yaml` come fonte unica · `valida_registro.py` · `INV-05` · sei documenti invece di undici | il comando qui sopra. Prova attiva: scrivere una sigla di reparto inesistente in un campo qualunque e rieseguirlo — deve uscire diverso da zero |
| **F-06** La firma era una stringa | fatale | `canali_firma_ammessi` · `GATE-OFF-1` · `offerta.schema.json` righe 120-132 · `INV-10` | i **due** test rossi di `GATE-OFF-1`: firma di un agente su canale non ammesso, e firma valida su una proposta rigenerata (impronta non corrispondente). Entrambi devono bloccare |
| **F-07** Chi produce approva | fatale | `produttore` e `giudice` obbligatori e distinti · `lan-gate` senza `Write` né `Edit` | `INV-01` e `INV-09` nel validatore. Prova già avvenuta: al primo giro il validatore ha bocciato la riga `nota_controfirma`, scritta un'ora prima |
| **F-08** Nessuna previsione di ricavo | fatale | `ART-PRV` · `GATE-PRV-1` · `GATE-TSR-1` («pareggio calcolato da ART-PRV») · `ART-CNS` tipizzato · `GATE-MEM-1` | test rosso di `GATE-PRV-1`: *un tasso di conversione dichiarato «misurato» e senza fonte deve bloccare*. E `GATE-TSR-1` non passa senza il pareggio prodotto da `ART-PRV` |
| **F-09** Il ponte verso gli agenti non specificato | fatale | `registro.yaml` sezione `ponte` · le quattro regole di ADR-014 · tetto 15 $ per lancio | eseguire `claude -p --agent <id> --output-format json` e leggere `total_cost_usd` nella risposta: se non c'è, il ponte non è quello dichiarato. Il tetto si verifica facendo superare la soglia: il lancio si ferma salvato, non riparte da capo |
| **F-10** Nessun ramo di fallimento, nessun test rosso | fatale | `ramo_fallimento` e `test_rosso` campi obbligatori · `se_fallisce` su ogni artefatto | `INV-03` e `INV-04`: svuotare `ramo_fallimento` di un controllo e rieseguire il validatore — deve uscire diverso da zero |
| **F-11** Nessun costo di esercizio | fatale | `costo_macchina_previsto` obbligatorio · `GATE-TSR-1` · `registro-chiamate.jsonl` · `lancio costi <id>` | test rosso di `GATE-TSR-1`: *un budget senza `costo_macchina_previsto` deve bloccare*. E `lancio costi <id>` legge dal registro delle chiamate, mai da una stima |
| **F-12** Il valore dell'offerta si gonfiava | fatale | `GATE-OFF-1` somma solo i bonus con `fonte_valore` · `offerta.schema.json` righe 63-68 | validare un `offerta.json` con un bonus privo di `fonte_valore`: lo schema lo rifiuta. E rimuovendo la fonte, il rapporto ricalcolato dal controllo scende sotto la soglia e blocca |

**Corrispondenza con il §8 di `00-LEGGIMI.md`** — la tabella breve e questa dicono la stessa cosa:

| §8 riga | Difetto qui | | §8 riga | Difetto qui |
|---:|---|---|---:|---|
| 1 fonte di verità validata | F-05 | | 7 percorso retroattivo | F-03 |
| 2 nasce `pubblico.json` | F-02 | | 8 ramo di fallimento e test | F-10 |
| 3 nasce `previsione.json` | F-08 | | 9 il giudice non ha la penna | F-07 |
| 4 il primo giorno è l'incasso | F-01 | | 10 i bonus richiedono la fonte | F-12 |
| 5 la firma è un oggetto | F-06 | | 11 il costo della macchina | F-11 |
| 6 il cronometro su ogni punto umano | F-04 | | 12 il ponte verso gli agenti | F-09 |

## 7.2 I quarantacinque gravi

| Difetto | Grado | Dove è risolto nella v4 | Come si verifica |
|---|---|---|---|
| **G-01** Conti di agenti e livelli discordi | grave | il nucleo si deriva dai produttori degli artefatti | `INV-07`: togliere dal registro il produttore di un artefatto fa uscire il validatore diverso da zero |
| **G-02** Tredici controlli dichiarati, quattordici esistenti | grave | quattordici controlli, elencati una volta sola | contare la sezione `gate` del registro; `INV-05` rifiuta ogni sigla fuori elenco |
| **G-03** Numeri e nomi doppi | grave | identificativi solo nel registro, prefisso unico per reparto | `INV-05`; aggiungere un agente con prefisso inesistente e rieseguire il validatore |
| **G-04** Correzioni dichiarate e non applicate | grave | le correzioni vivono nel registro, non in una tabella di prosa | il validatore legge il registro, non i documenti: una correzione non applicata al dato non passa |
| **G-05** Tre soglie e tre proprietari per un criterio | grave | un artefatto, un controllo, un giudice, un `criterio_eseguibile` | `INV-01`; e per ogni artefatto esiste esattamente una riga `gate` che lo presidia |
| **G-06** Otto controlli su tredici in prosa | grave | `criterio_eseguibile` obbligatorio, scritto come predicato | il validatore rifiuta un controllo senza criterio; ogni criterio si può eseguire su un file di prova |
| **G-07** Criterio di accettazione in italiano | grave | i passaggi con criterio in prosa sono usciti; resta `dipende_da` | validare un artefatto contro il proprio schema è l'unica accettazione: `INV-02` |
| **G-08** Le formule del tetto dividevano per zero | grave | `GATE-TSR-2`, criterio unico sempre calcolabile | test rosso: *uno scarto dell'11% deve bloccare la spesa nuova e NON uccidere il lancio* |
| **G-09** Il controllo si spegneva abbassando il prezzo | grave | firma legata al testo firmato · artefatti a valle `da_rivedere` al cambio a monte | test rosso (b) di `GATE-OFF-1`: proposta rigenerata → firma decaduta → il controllo blocca |
| **G-10** Prova del tracciamento e consenso ai cookie | grave | `GATE-FNL-1` con `prova.origine=='piattaforma'` · blocco `consenso` obbligatorio nello schema | validare un `funnel.json` senza il blocco `consenso`: `funnel.schema.json` lo richiede e lo rifiuta |
| **G-11** Pubblicazione prima della prova di cassa | grave | prova di cassa **dentro** `GATE-FNL-1` | lo stesso test rosso di F-01; e l'ordine è leggibile in `dipende_da` di `ART-APE`, che richiede `ART-FNL` valido |
| **G-12** Il reparto che spende senza controllo | grave | i canali a pagamento in `pubblico.json` · la spesa sotto `GATE-TSR-1/2` · `per_canale` nel consuntivo | test rosso di `GATE-CNS-1`: *un consuntivo con ricavo dichiarato a mano e origine assente deve bloccare* |
| **G-13** Il controllo finale contava sé stesso | grave | `ART-DBR` giudicato da `lan-gate`, controfirma come campo · `GATE-MEM-1` | `INV-01`; e il test rosso di `GATE-MEM-1`: *tre schemi generici e uno scarto del 40% senza causa devono bloccare* |
| **G-14** Lo stesso artefatto validato due volte | grave | un solo controllo per artefatto | contare: per ogni `id` di artefatto esiste una sola riga `gate` con quel `presidia` |
| **G-15** Nove schemi su tredici mancanti | grave | **tredici schemi su tredici**, versionati, in `dati/schemi/` | `INV-02`: cancellare uno schema e rieseguire il validatore — deve uscire diverso da zero |
| **G-16** Il manifesto dei testi senza schema | grave | `copy.schema.json` con `punteggio.blocchi` e il campo `ancora` | validare un manifesto senza `punteggio`: lo schema lo rifiuta. E il test rosso di `GATE-CPY-1`: *punteggio 85 con un blocco al 30% dei suoi punti deve bloccare* |
| **G-17** Nessun artefatto versionato | grave | `schema_version` in ogni schema · impronta degli ingressi · `da_rivedere` a valle | ogni schema richiede `schema_version` con valore fisso: un file senza quel campo non valida |
| **G-18** Tre rappresentazioni dello stesso istante | grave | `editoriale.schema.json` con `data_uscita` e `destinazione` risolvibile | test rosso di `GATE-EDT-1`: *un contenuto che punta a una pagina inesistente deve bloccare* |
| **G-19** Identificativi che collidono | grave | un lancio è una cartella, ogni artefatto ha un nome di file fisso | il campo `file` di ogni artefatto nel registro è unico: nessun progressivo da assegnare |
| **G-20** Proprietà di scrittura dichiarata dal chiamante | grave | `produttore` unico per artefatto · giudice senza penna · firma non scrivibile | `INV-01` e `INV-09`; e il test rosso (a) di `GATE-OFF-1` sulla firma scritta da un agente |
| **G-21** Concorrenza e idempotenza assenti | grave | le tre garanzie di `lancio avanza` (`01-ARCHITETTURA.md` §2.3) | lanciare due volte il comando sullo stesso lancio in parallelo: il secondo deve uscire 1 dicendo chi detiene il lock. Rieseguirlo senza cambiamenti non deve produrre scritture nuove |
| **G-22** Quindici agenti erano funzioni | grave | quindici agenti in tutto, tre al grado più basso per i calcoli | `INV-08`: nessun agente di grado basso produce un artefatto che richiede giudizio |
| **G-23** Il giudice in sola lettura doveva scrivere | grave | il verbale lo scrive lo script | `INV-09` più il fatto che `lan-gate` produce `verbali` senza avere `Write`: la contraddizione della v3 farebbe fallire il validatore |
| **G-24** Il campo degli strumenti non sa fare tre cose su sei | grave | l'unico divieto affidato a quel campo è quello che sa imporre | `INV-09` è l'unico invariante che poggia sugli strumenti; nessun altro vincolo è scritto lì |
| **G-25** Contratto d'uscita solo in prosa | grave | gli agenti scrivono artefatti, non restituiscono risultati | `INV-02` più `dipende_da`: un artefatto non valido contro lo schema blocca il successivo |
| **G-26** Il nucleo minimo non eseguiva il proprio flusso | grave | il nucleo si calcola dai produttori | `INV-07`, con la motivazione scritta accanto nel registro |
| **G-27** Il flusso della Regia senza fasi né agenti | grave | la Regia produce `ART-APE` e `ART-CNS`, con tutti i campi obbligatori | test rossi di `GATE-REG-1` (*nove voci vere e una falsa devono bloccare*) e di `GATE-CNS-1` |
| **G-28** «Reparto abilitato» mai definito | grave | non ci sono reparti da abilitare | il vincolo tecnico è uno: `valida_registro.py` diverso da zero significa che non si costruisce |
| **G-29** L'esercizio non contato: 80-115 ore per lancio | grave | tre giorni misurati prima dell'ecosistema · costo macchina con tetto | i tre criteri di chiusura di `00-LEGGIMI.md` §3.1-3.3, ognuno con la propria prova esterna; più il test rosso di `GATE-TSR-1` |
| **G-30** Stime che si contraddicono | grave | le ore in un posto solo, con il criterio di chiusura accanto | le tre fasi del primo giorno hanno un intervallo dichiarato e una condizione di chiusura verificabile; il superamento fa scattare la condizione d'uscita 1 |
| **G-31** La condizione di abbandono scattava sul percorso nominale | grave | 45 giorni, e non contano più la costruzione dell'infrastruttura | `00-LEGGIMI.md` §7 riga 3: il conto parte dal giorno zero, che dura ore, non settimane |
| **G-32** Le copertine, punto umano di massa non contato | grave | `PU-COPERTINA` nel registro, scadenza 3 giorni, nessun predefinito | `INV-06`; e il pezzo in attesa compare in `lancio blocchi` |
| **G-33** Nessun processo eseguiva le fasi «continue» | grave | i tre momenti di invocazione dichiarati (`01-ARCHITETTURA.md` §2.4) | il terzo è un promemoria pianificato quotidiano: se non gira, `lancio elenco` mostra il lancio fermo e da quanti giorni |
| **G-34** Il controllo della memoria verificava l'esistenza | grave | `GATE-MEM-1` pretende che ogni record citi un artefatto esistente | test rosso: *un record di memoria con corpo «ok» e fonti vuote deve bloccare* |
| **G-35** La fase zero si autoconvalidava | grave | `dato_da_terzi` obbligatorio su ognuno dei quattordici controlli | il validatore rifiuta un controllo senza `dato_da_terzi`; e nessun criterio usa un dato prodotto da chi è giudicato |
| **G-36** Scadenza nulla per difetto, potatura inerte | grave | la memoria dell'ecosistema è il debrief, con schema e controllo | `GATE-MEM-1`; e la condizione d'uscita 4 (`00-LEGGIMI.md` §7): dopo due lanci senza uno schema che cambi una decisione, la memoria si dichiara fallita |
| **G-37** La soglia del 40% senza conseguenza | grave | nessuna soglia «segnala»: ogni controllo ha un ramo e un codice | `INV-03` |
| **G-38** Passaggio scaduto = blocco permanente | grave | `orologi: congelati_in: ["SOSPESO"]`, ripartono dal residuo | sospendere un lancio, aspettare, riattivarlo: le scadenze devono ripartire dal valore che avevano all'ingresso |
| **G-39** Sospendere un lancio aperto non spegneva il carrello | grave | sospensione con `come_si_esce` eseguibile · prova di cassa in `GATE-FNL-1` · ricalcolo in `GATE-REG-1` | test rosso di `GATE-REG-1`; e il `dato_da_terzi` di quel controllo: la validità si ricalcola dai file, mai dallo stato |
| **G-40** Rientro infinito e deroghe senza contatore | grave | `GATE-TSR-2` blocca la spesa e lo sblocco richiede firma umana tracciata · `PU-SPESA` | test rosso di `GATE-TSR-2`; e `INV-06` sul punto umano della spesa |
| **G-41** Transizioni senza soggetto che le inneschi | grave | ogni transizione dichiara chi autorizza · il codice 3 ha un posto scritto | leggere la colonna `autorizza` della tabella `transizioni` nel registro: nessuna riga è vuota. Per il codice 3, `01-ARCHITETTURA.md` §2.2 e §7 |
| **G-42** Nessuna osservabilità | grave | `registro-chiamate.jsonl` · verbale sempre · `lancio elenco` · `lancio costi` · `lancio blocchi` | eseguire `lancio blocchi`: deve elencare i punti umani aperti ordinati per giorni di attesa. Se non stampa niente e un lancio è fermo, l'osservabilità non funziona |
| **G-43** Nessun obbligo di legge | grave | `01-ARCHITETTURA.md` §9 · `rinuncia_recesso_raccolta` nello schema dell'offerta | validare un'offerta senza il campo del recesso quando il prodotto si scarica subito: lo schema lo prevede e la nota ne dichiara l'effetto sui conti |
| **G-44** Credenziale pubblica mai sostituita | grave | gesto **0** del giorno zero (`00-LEGGIMI.md` §3.1) | criterio già scritto: la vecchia chiave **non funziona più sul servizio**. Finché funziona, il giorno zero non è chiuso |
| **G-45** L'ADR descriveva invece di decidere | grave | `05-ADR-023.md` separato · il descrittivo nel registro · le decisioni aperte dichiarate | `00-LEGGIMI.md` §4 elenca le decisioni che aspettano una persona: nessuna di esse è presa dentro l'ADR per silenzio |

---

## Connessioni

**I documenti del pacchetto (versione 4)**

- `00-LEGGIMI.md` — **da qui si comincia**. Il §8 è la versione breve di questo documento; il §1 i
  numeri misurati; il §7 le quattro condizioni per smettere
- `01-ARCHITETTURA.md` — la macchina: `lancio avanza`, gli stati, il ponte verso gli agenti, il
  motore, gli errori, l'osservabilità, gli obblighi di legge
- `dati/registro.yaml` — **la fonte di verità**. Se questo documento dice una cosa diversa dal
  registro, ha torto questo documento
- `dati/valida_registro.py` — il comando che verifica i dieci invarianti
- `dati/schemi/*.json` — tredici schemi, uno per artefatto
- `_v3-superata/00-LEGGIMI-GAEL.md` — la nota d'apertura della versione 3, archiviata

> **Nota sui puntatori, aggiornata a fine giornata.** Quando questo documento è stato scritto,
> il 02, il 03, il 04 e il 05 erano ancora soltanto voci della mappa. Ora esistono tutti sul disco
> e sono committati: `00-LEGGIMI.md`, `01-ARCHITETTURA.md`, `02-PREVISIONE-E-DENARO.md`,
> `03-FLUSSO-OFFERTA.md`, `04-COSTRUZIONE.md`, `05-ADR-023.md`, questo documento e la cartella
> `dati/`. Gli undici dossier della versione 3 sono in `_v3-superata/`, integrali, con una nota
> che spiega perché sono stati superati.

**I rapporti della critica** — in `_critica-v3/`, tutti conservati, nessuno riassunto

- `CRITICA-A.md` — dossier 01, 02, 03: 106 rilievi, 16 punti solidi
- `CRITICA-B.md` — dossier 04, 05, 06: 56 rilievi, 14 punti solidi
- `CRITICA-C.md` — dossier 07, 08, 09, 10: 14 difetti strutturali (sezioni 4-8 dichiarate incomplete)
- `CRITICA-D.md` — secondo passaggio su 07, 08, 10: 12 rilievi, 7 punti solidi
- `CRITICA-EMPERATOR.md` — 13 rilievi con gli ADR alla mano
- `ORIGINE.md` — cosa era stato chiesto davvero: i tredici vincoli V-01…V-13
- `INCASSO.md` — l'infrastruttura commerciale reale (fatto nuovo §6.4)
- `PONTE-AGENTI.md` — se uno script può far lavorare un agente (F-09)
- `MOTORE.md` — se il motore canonico regge un flusso di lancio (`01-ARCHITETTURA.md` §6)

**Il lavoro che resta la base**

- `PIANO-MAESTRO/RICOGNIZIONE-LANCI.md` (L1) e `PIANO-MAESTRO/ASSORBIMENTO-LANCI.md` (L2) — le
  misure di Gael, citate per nome da tutto il resto
- `PIANO-MAESTRO/26-ECOSISTEMA-LANCI.md` — il documento L3, dichiarato superato, non cancellato
- `_v3-superata/` — la versione 3 integrale

**Gli ADR che governano**

- `company/Memory/decisions/ADR-016-ultimo-metro.md` — il mandato: «resta aperto il buco fra
  pubblicato e venduto. È il prossimo da chiudere»
- `company/Memory/decisions/ADR-014-il-codice-torna-a-chiamare-un-modello.md` — le quattro regole
  del ponte, già pagate (F-09)
- `company/Memory/decisions/ADR-019-motore-orchestrazione-canonico.md` — il motore, e la domanda a
  cui `01-ARCHITETTURA.md` §6 risponde con una misura
- `company/Ecosistemi/REGISTRO-NUMERI.md` — dove il 15 è riservato
- `company/Memory/BACKLOG.md` — B-020 (la chiave pubblica, G-44), B-043 (l'azienda non misura un
  euro, F-08), B-002 e B-003 (prezzo e ruolo del Manuale, F-04 e §6.2)
