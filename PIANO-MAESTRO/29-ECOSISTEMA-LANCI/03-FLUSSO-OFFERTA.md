---
Type: PROJECT
Status: Proposta — versione 4
Tags: #lanci #ecosistema-15 #offerta #prezzo #firma
Created: 2026-09-05
Last updated: 2026-09-05
Versione: 4
---

# 03 — IL FLUSSO OFFERTA

> **Regola di lettura:** questo documento spiega. Il registro decide.
> Se una riga qui contraddice `dati/registro.yaml` o `dati/schemi/offerta.schema.json`, ha torto
> questa riga.

---

## 1. PERCHÉ QUESTO È IL CUORE

L'intero ecosistema esiste per produrre **due numeri**: un prezzo e una data.

Tutto il resto — il pubblico, la ricerca, il certificato, i testi, le pagine, il calendario — o
serve a istruire quei due numeri, o serve a eseguirli. Un prodotto pronto da sei mesi senza prezzo
e senza data non è un prodotto in ritardo: **è un prodotto che non esiste per il mercato.**

La versione 3 lo sapeva e lo dichiarava. Poi, alla verifica dei revisori, il suo flusso Offerta
**documentava il blocco invece di scioglierlo**: il prezzo restava una domanda aperta, con più
pagine attorno.

Questa versione ha un compito misurabile: **portare la decisione a essere una conferma di dieci
secondi**, e renderla impossibile da falsificare.

---

## 2. LA DIAGNOSI ESATTA — dove il Manuale si è fermato davvero

Questo paragrafo è il più importante del documento, perché la versione 3 aveva sbagliato bersaglio.

**I fatti, con la fonte:**

| Fatto | Fonte |
|---|---|
| Il prodotto è pronto | catalogo prodotti, `Status: Pronto`, **07/03/2026** |
| Ha 203 pagine, verificate | il file sul disco |
| Il prezzo dichiarato è **«€ NON LO SO»** | catalogo prodotti |
| La wiki dice **«€297-€497»** | wiki, 29/04/2026 |
| Il listino ha due fasce diverse | listino |
| Il piano v3 proponeva **47 €** | dossier 04 della versione 3 |
| Esisteva già un piano di lancio, obiettivo **30/05/2026** | wiki, progetto del 29/04/2026 |
| Quel piano è morto in silenzio | nessun documento lo registra |

**La diagnosi della v3:** manca la firma sul prezzo, quindi mettiamo un cronometro sulla firma.

**La diagnosi corretta, e la differenza costa sei mesi:** il Manuale non si è fermato sulla firma
del prezzo. Si è fermato **una domanda prima**, su una domanda che nessuno ha mai posto
formalmente:

> **Questo prodotto si vende, o è un regalo per acquisire contatti?**

Finché quella domanda è aperta, **una proposta di prezzo non nasce**. E se la proposta non nasce,
un cronometro che conta «da quanti giorni la proposta aspetta una firma» **non parte mai**.

> **Il fallimento era invisibile alla sua stessa misura.**
> È il difetto più grave trovato in tutta la revisione, ed è la ragione per cui in questa versione
> il cronometro sta su **ogni punto umano aperto** e non sulla firma finale.

---

## 3. LE SEI FASI

Ogni fase ha: cosa entra, chi lavora, cosa esce, e **come si sa che è finita**. Nessuna fase è
«completata» perché qualcuno lo dice.

| Fase | Cosa entra | Chi | Cosa esce | È finita quando |
|---|---|---|---|---|
| **O1** | `ART-CRT`, `ART-PUB` | `lan-off-conductor` + **persona** | `ruolo_prodotto` | il campo vale `vendita` o `acquisizione-contatti` |
| **O2** | le fonti di prezzo esistenti in azienda | `lan-off-conductor` | `prezzi_precedenti_trovati[]` | ogni fonte trovata è nell'elenco, con data |
| **O3** | `ART-CRT`, `ART-RIC` | `lan-off-conductor` | `struttura` | il rapporto valore/prezzo è **ricalcolato**, non dichiarato |
| **O4** | `ART-PRV`, `ART-PUB` | `lan-prv-modello` | `confronto_alternative_prezzo[]` | almeno tre prezzi hanno un ricavo atteso |
| **O5** | tutto quanto sopra | **persona** | `firma` | la firma esiste, con canale ammesso e impronta corrispondente |
| **O6** | `offerta.json` firmato | `lan-off-conductor` | `data_chiusura`, stato `DATATO` | `GATE-OFF-1` esce 0 |

### O1 — Il ruolo del prodotto

**È il punto umano `PU-RUOLO`**, e ha tre proprietà che nella versione 3 non aveva nessuna:

| Proprietà | Valore | Perché |
|---|---|---|
| scadenza | **7 giorni** | dopo sei mesi di silenzio, una scadenza è il minimo |
| default | **`vendita`** | vedi sotto |
| allo scadere | si procede col default, si scrive `ruolo_scelto_per_silenzio: true` e `ruolo_revisione_il`, **e si avvisa** | la scelta resta visibile e revocabile invece di sparire dentro un valore qualunque |

**Perché il default è «vendita» e non «regalo».** Non perché vendere sia meglio: perché **è la
strada da cui si torna indietro**.

- Un prodotto messo in vendita può diventare un regalo il mese dopo. Nessuno si offende.
- Un prodotto regalato **non si rimette in vendita** senza bruciare chi l'ha avuto gratis.

> **La regola generale, che vale per ogni punto umano di tutto il sistema:** fra due strade, quando
> il tempo scade, si prende quella da cui si torna indietro — e si dichiara di averlo fatto.

**Cosa cambia a valle, e va detto a chi decide:** se il ruolo è `acquisizione-contatti`, il prezzo
può essere zero, la previsione misura contatti invece di euro, e il pareggio si calcola sul valore
atteso di un contatto — numero che oggi **l'azienda non ha** (documento 02, §8). È una conseguenza
da conoscere prima di scegliere, non dopo.

### O2 — La riconciliazione dei prezzi già dati

**Fase nuova, e nasce da un fatto specifico:** questa azienda si è già data quattro prezzi diversi
per lo stesso prodotto, in quattro posti, in date diverse, e **non li ha mai messi sullo stesso
tavolo**.

Lo schema pretende `prezzi_precedenti_trovati[]` con `fonte`, `valore`, `data` e — quando ci si
discosta — `perche_ci_discostiamo`.

> **La regola:** un prezzo proposto senza guardare i prezzi che l'azienda si è già data non è
> istruito. È inventato, con più pagine attorno.

Discostarsi è legittimo: la wiki diceva 297-497 € e si può proporre 47 €. **Non è legittimo
proporre 47 € senza sapere che qualcuno, cinque mesi prima, aveva scritto 297.**

### O3 — La struttura dell'offerta

Quattro elementi obbligatori: `valore_dichiarato`, `rapporto_valore_prezzo`, `garanzia`,
`azione_richiesta`.

**La riparazione che conta — i bonus.** Nella versione 3 il rapporto valore/prezzo doveva essere
almeno 3, e **lo stesso agente che costruiva il pacchetto decideva quanto valeva**. Il modo più
rapido per arrivare a 3 era aggiungere una riga: *«Bonus: lista di controllo, valore 99 €»*. Il
controllo diventava verde. **Il controllo istruiva a gonfiare.**

Qui ogni bonus porta `fonte_valore`, e la lista è chiusa:

| `fonte_valore` | Significa |
|---|---|
| `prezzo-listino-proprio` | è già in vendita a quel prezzo da noi |
| `prezzo-mercato-con-url` | qualcun altro lo vende a quel prezzo, e l'indirizzo è nel file |
| `costo-produzione` | quanto è costato farlo |
| `null` | **il bonus vale zero nel calcolo** |

Il valore dichiarato è la somma dei soli bonus con fonte, più il valore del prodotto, e **il gate
lo ricalcola invece di leggerlo**.

**La soglia 3 è dichiarata provvisoria.** È ereditata dal materiale storico e non è mai stata
misurata su questa azienda: sta nello schema come parametro (`soglia_rapporto_minima`), non come
costante sparsa in due documenti.

**La garanzia ha un minimo di 14 giorni, e non è una scelta di marketing:** è l'obbligo di legge
sui prodotti digitali venduti a consumatori nell'Unione. Il campo `rinuncia_recesso_raccolta` dice
se al momento del pagamento si raccoglie il consenso esplicito alla rinuncia: se è `false`, **il
rimborso resta dovuto per 14 giorni anche a prodotto già scaricato**, e questo cambia i conti del
documento 02.

**Una sola azione richiesta.** Due azioni in una pagina sono zero azioni.

### O4 — Le alternative di prezzo, con il ricavo di ciascuna

Qui la previsione entra nell'offerta. Almeno tre prezzi, ognuno col proprio ricavo atteso calcolato
sul pubblico verificato.

Il prodotto di questa fase è **la frase che si porta a chi firma**:

> *«Su un pubblico verificato di N persone, con questi tassi dichiarati:
> 27 € fanno X · 47 € fanno Y · 97 € fanno Z.
> Il pareggio è a K copie. Il pessimista dice W.
> Confermi 47?»*

**Questo è l'intero scopo dell'ecosistema, in cinque righe.** La differenza fra questa domanda e
«confermi 47?» è la differenza fra una decisione e una scelta di gusto — e costa dieci secondi in
più a chi legge.

Le alternative scartate si conservano in `alternative_scartate[]` con `perche_no`. **Non servono a
questo lancio: servono al terzo**, per vedere se si sceglie sempre troppo basso — l'errore più
comune e il più invisibile, perché un prezzo basso vende, e quindi sembra aver funzionato.

### O5 — La firma

**È il punto umano `PU-PREZZO`: 14 giorni, e nessun default.**

L'assenza di default è deliberata e va difesa: **un prezzo scelto da una macchina per sbloccare un
controllo produce un danno che si scopre a lancio finito.** Il rinvio, invece, si vede e si
corregge. Fra un errore invisibile e un ritardo visibile, si sceglie il ritardo.

Allo scadere dei 14 giorni il lancio va in `SOSPESO`, con `revisione_il` e `come_si_esce` — e
`come_si_esce` **è un comando eseguibile**, non una descrizione.

### O6 — Il congelamento

Con la firma valida: si calcola `data_chiusura` da `data_apertura` e `durata_carrello_gg`, il
lancio passa a `DATATO`, **e il conto alla rovescia parte**.

Da qui in poi ogni artefatto a valle si costruisce contro questo prezzo e questa data. Se uno dei
due cambia, vale il §6.

---

## 4. LA FIRMA — perché è un oggetto e non una stringa

> **Il difetto peggiore trovato in tutta la revisione, ed è peggiore del blocco che il reparto vuole
> curare.**

Nella versione 3 la firma era il campo `firmato_da`, una stringa. Conseguenza dimostrata:
**qualunque agente in ciclo di auto-riparazione poteva scrivere «Max» per sbloccarsi**, e il
controllo avrebbe certificato una decisione umana mai presa. Un lancio sarebbe partito, con spesa
vera e pubblicazione vera, a un prezzo che nessuno aveva approvato.

Qui la firma è un oggetto con cinque campi obbligatori:

| Campo | Cosa impedisce |
|---|---|
| `chi` | — |
| `canale` | **lista chiusa**: `comando-utente`, `chat-firmata`, `file-fuori-agenti`. Un canale fuori lista fa fallire il controllo |
| `riferimento` | il comando digitato o l'identificativo del messaggio: la firma è rintracciabile |
| `proposta_impronta` | l'impronta del testo firmato. Lega la firma **a quel testo**, non all'idea generica |
| `il` | quando |

**E la riga che vale più di tutte le altre:**

> **Nessun agente ha permesso di scrittura sull'oggetto `firma`**, né su `via_libera` di `ART-APE`.
> Il vincolo è nel registro (`vincolo_scrittura` di `lan-off-conductor`) e nei canali ammessi.

È il punto in cui il sistema riconosce che ci sono cose che non gli competono. **La riga di codice
che lo impedisce vale più della frase che lo dichiara** — e la versione 3 aveva solo la frase.

---

## 5. SE LA FIRMA NON ARRIVA

| Quando | Cosa succede |
|---|---|
| giorno 0-13 | il lancio resta in `ISTRUITO`. `lancio blocchi` lo mostra fra i punti umani aperti, con i giorni di attesa |
| giorno 14 | il lancio va in `SOSPESO`, con `stato_di_partenza: ISTRUITO`, `revisione_il` e `come_si_esce` |
| in `SOSPESO` | **gli orologi si fermano.** Tutte le altre scadenze si congelano al valore che avevano |
| quando la causa è rimossa | si torna a `stato_di_partenza` con un verbale, autorizzato al livello L2 |
| a 90 giorni | si propone `ABORTITO` **a Max, che è l'unico che può deciderlo** |

**Perché gli orologi si fermano.** Nella versione 3 un lancio sospeso continuava ad accumulare
scadenze di consegna che scattavano tutte insieme al risveglio: **il sistema puniva chi tornava**.

**Perché `SOSPESO` non è `ABORTITO`.** Un lancio sospeso conserva tutto il lavoro fatto. Il Manuale,
oggi, sarebbe un lancio sospeso da sei mesi con tutti gli artefatti a monte già validi: al ritorno
si riparte dalla proposta, non dal principio.

---

## 6. SE QUALCOSA CAMBIA DOPO LA FIRMA

**Il caso che la versione 3 non gestiva.** Nessun artefatto era versionato: un cambio di prezzo non
invalidava niente a valle. E siccome il piano *prevedeva* che le fondamenta nascessero prima del
prezzo, **il fuori-ordine era la normalità, non l'eccezione**.

| Cosa cambia | Cosa succede |
|---|---|
| la **proposta** viene rigenerata | `proposta_impronta` non corrisponde più → **la firma decade**, `GATE-OFF-1` blocca, O5 si riapre |
| la **previsione** cambia dopo la firma | `previsione_riferimento.impronta` non corrisponde → l'offerta diventa `da_rivedere` |
| il **prezzo** cambia | tutti gli artefatti che dipendono da `ART-OFF` (`ART-CPY`, `ART-BDG`, `ART-EDT`, `ART-FNL`) diventano `da_rivedere` e i loro controlli si riaprono |
| il **pubblico** cambia | la previsione si ricalcola; se il ricavo atteso si sposta oltre la soglia dichiarata, l'offerta va rivista |

> **La regola:** una firma vale per **quel testo**, non per l'argomento. Rigenerare la proposta e
> tenere la firma vecchia è far partire un lancio a un prezzo che nessuno ha approvato in quella
> forma.

---

## 7. IL PERCORSO PER I PRODOTTI GIÀ FINITI

**Il difetto, dimostrato dal revisore:** nella versione 3 il flusso Prodotto usciva con errore alla
prima riga di ingresso **proprio sul prodotto per cui il reparto era stato costruito**. Il Manuale è
pronto dal 07/03/2026 e non è mai passato da un flusso di produzione: non ha un brief, non ha un
percorso di validazione, non ha nulla di ciò che il flusso pretendeva in ingresso.

`ART-CRT` ammette due modalità: `integrale` e **`retroattiva`**.

| Modalità | Quando | Cosa pretende |
|---|---|---|
| `integrale` | prodotto costruito dentro il sistema | tutto il percorso |
| `retroattiva` | prodotto già finito | le sei bandiere rosse tutte false, il file esistente e non vuoto, ogni link testato **dal controllo**, e un **`debito_collaudo` dichiarato** |

**Il `debito_collaudo` è la parte onesta:** dice cosa non è stato verificato perché il prodotto è
nato fuori dal sistema. Non lo nasconde, non lo condona: lo scrive, così il debrief lo trova.

---

## 8. IL CONTROLLO — `GATE-OFF-1`

**Criterio eseguibile** (dal registro, testuale):

```
prezzo è numero > 0 AND prezzo non in lista_valori_evasivi AND data_apertura è data futura
valida AND durata_carrello_gg > 0 AND ruolo_prodotto in [vendita, acquisizione-contatti] AND
firma.canale in canali_firma_ammessi AND firma.proposta_hash == sha256(file proposta corrente)
AND somma(bonus[].valore dove fonte_valore != null) usata per rapporto_valore_prezzo
```

| | |
|---|---|
| **Dati da terzi** | la firma non è scrivibile da nessun agente; il canale è in lista chiusa; l'impronta lega la firma al testo esatto |
| **Ramo di fallimento** | torna a `ISTRUITO`. **La proposta si conserva**, la firma decade, O5 si riapre |
| **Codice di uscita** | 1 (blocca con verbale) |

**I due test rossi dichiarati** — se non falliscono, il controllo è decorativo:

1. un `offerta.json` con `firma.chi = "Max"` **scritta da un agente** e canale non ammesso **deve
   bloccare**;
2. una firma valida su una proposta **poi rigenerata** **deve bloccare** per impronta non
   corrispondente.

**La `lista_valori_evasivi`** contiene i valori che sembrano una risposta e non lo sono: `"NON LO
SO"`, `"da definire"`, `"TBD"`, `0` quando il ruolo è `vendita`. Esiste perché nel catalogo prodotti
di questa azienda il prezzo del Manuale è, alla lettera, **«€ NON LO SO»**, e un sistema che accetta
quella stringa come prezzo non ha capito qual è il suo lavoro.

---

## 9. I DIFETTI RIPARATI — tabella di corrispondenza

| # | Difetto della versione 3 | Riparazione | Come si verifica |
|---|---|---|---|
| 1 | Il cronometro stava sulla firma, ma il blocco vero era a monte: la proposta non nasceva mai | `PU-RUOLO` con 7 giorni e default reversibile, prima di tutto | registro, `punti_umani`; INV-06 |
| 2 | `firmato_da` era una stringa scrivibile da un agente | firma come oggetto, canale in lista chiusa, nessun permesso di scrittura | `GATE-OFF-1` test rosso (a) |
| 3 | La firma non era legata al testo firmato | `proposta_impronta` | `GATE-OFF-1` test rosso (b) |
| 4 | Il rapporto valore/prezzo era auto-soddisfacibile con bonus inventati | `fonte_valore` obbligatoria, `null` → vale 0, gate ricalcola | schema, `bonus.fonte_valore` |
| 5 | Il prezzo si proponeva ignorando i quattro prezzi già dati dall'azienda | fase O2 e `prezzi_precedenti_trovati[]` | schema |
| 6 | La firma era cieca: nessun ricavo accanto al numero | `previsione_riferimento` obbligatorio + fase O4 | schema, campo obbligatorio |
| 7 | Il flusso non ammetteva prodotti già finiti | modalità `retroattiva` con `debito_collaudo` | `GATE-PRD-1` |
| 8 | Nessuna via d'uscita dal blocco | `SOSPESO` con `come_si_esce` eseguibile; orologi congelati | registro, `orologi` |
| 9 | Un cambio a monte non invalidava niente a valle | impronte e stato `da_rivedere` | documento 01, §7 |
| 10 | La garanzia era una scelta di marketing | minimo 14 giorni per obbligo di legge, e `rinuncia_recesso_raccolta` | schema, `garanzia.giorni` |

---

## 10. LA PROPOSTA CONCRETA PER IL MANUALE

Non è un esempio: è ciò che si porta a Max **appena `pubblico.json` esiste**.

| Passo | Contenuto | Chi |
|---|---|---|
| 1 | **La domanda O1:** il Manuale si vende o è un regalo? Con le due conseguenze, e quale è reversibile | oggi, in dieci minuti |
| 2 | La riconciliazione dei quattro prezzi trovati, con le date | `lan-off-conductor` |
| 3 | Il pubblico verificato, canale per canale — **incluso il fatto che quello previsto è spento dal 29/07/2026** | `lan-pub-censore` |
| 4 | Tre prezzi con il ricavo atteso di ciascuno, e il pareggio | `lan-prv-modello` |
| 5 | **La domanda O5**, in una riga sola | a Max |

**Il costo dell'attesa, dichiarato:** sei mesi finora. Da adesso, sette giorni e poi il default
reversibile — e il default viene scritto nel file come tale, non nascosto.

---

## 11. COME SI VERIFICA CHE QUESTO DOCUMENTO SIA RISPETTATO

| Cosa | Comando o meccanismo |
|---|---|
| Il registro è coerente | `cd dati && PYTHONIOENCODING=utf-8 python valida_registro.py` |
| Un'offerta è ben formata | validazione contro `dati/schemi/offerta.schema.json` |
| Una firma falsa non passa | `GATE-OFF-1`, test rosso (a) |
| Una firma su testo cambiato non passa | `GATE-OFF-1`, test rosso (b) |
| Il giudice non può riscrivere l'offerta | INV-09: `lan-gate` non ha `Write` né `Edit` |
| Il produttore non giudica sé stesso | INV-01, verificato per tutti e tredici gli artefatti |
| Ogni punto umano ha una scadenza o una ragione per non averla | INV-06 |
| Cosa blocca l'azienda adesso | `lancio blocchi` |

---

## Connessioni

- `dati/registro.yaml` — la fonte di verità
- `dati/schemi/offerta.schema.json` — il contratto di questo artefatto
- [[00-LEGGIMI]] — il problema e le decisioni che aspettano Max
- [[01-ARCHITETTURA]] — la catena, gli stati, il giudice senza penna
- [[02-PREVISIONE-E-DENARO]] — da dove viene il ricavo atteso che rende la firma una decisione
- [[06-CRITICA-E-GIRI]] — i difetti trovati, uno per uno
