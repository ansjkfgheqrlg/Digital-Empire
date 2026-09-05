# CRITICA-EMPERATOR — i rilievi che ho trovato io, leggendo di persona

Dossier letti integralmente da me: 00, 01, 04, 09. Gli altri sono in mano ai tre revisori.

---

## A. I QUATTRO DIFETTI DI FONDO — quelli che nessuno dei tre giri precedenti ha visto

### E-01 — Il piano ignora ADR-019 e sarebbe l'OTTAVO motore di orchestrazione dell'Impero
**Gravità: massima. È il difetto che da solo giustifica la riscrittura.**

ADR-019 (2026-09-03, ATTIVO) dichiara canonico
`company/Ecosistemi/11-APEX-7-CORE/orchestration-layer/` (133 file, 24 test) e scrive al §4:

> «Entro il primo lavoro reale di Digital Empire che ha bisogno di orchestrazione, il motore
> canonico deve servirlo davvero. Se quel lavoro arriva e viene fatto a mano, o con un altro
> strumento, o non arriva affatto entro tre mesi, questo ADR va riaperto.»

Il piano LANCI **è** quel lavoro: sette flussi orchestrati, gate, stato persistente, riprese.
E propone (dossier 01 §7, dossier 09 §3) **17 script nuovi** — `stato_lancio.py`, `gate.py`,
`memoria.py`, `handoff.py`, `lancio.py` — cioè un motore di orchestrazione nuovo, senza nominare
una sola volta quello canonico.

ADR-019 §2 misura il male: l'Impero ha prodotto **sette linee di orchestrazione per un componente
che nessuno ha mai chiamato**. Questo piano ne creerebbe l'ottava. E violerebbe anche ADR-003
(wrap, mai riscrittura), che il piano cita come propria bandiera per i reparti ma non applica
all'infrastruttura.

**Riparazione:** la V4 deve decidere esplicitamente, con le prove in mano:
o LANCI diventa il primo consumatore del motore canonico (e allora ADR-019 §4 è soddisfatto),
o dichiara con misure perché non può, e allora **riapre ADR-019** invece di aggirarlo in silenzio.
Il silenzio non è un'opzione: è la malattia che ADR-018 e ADR-019 sono nati per curare.

---

### E-02 — Il piano ignora ADR-014, che ha già pagato i guasti del far chiamare un modello dal codice
**Gravità: alta.**

Tutto il piano poggia su agenti che «eseguono fasi» dentro `lancio avanza`. Ma non dice **mai**
come un file `.claude/agents/*.md` viene invocato da uno script Python. È il buco tecnico più
profondo del pacchetto: se quel ponte non esiste, l'ecosistema nasce di carta — esattamente il
difetto che dichiara di curare (19 file, 2.377 righe, 0 eseguibili).

E la cosa peggiore è che **la risposta esiste già, pagata a caro prezzo**. ADR-014 (2026-08-30,
ATTIVO) documenta tre fallimenti e le tre lezioni chiuse con prove:

| Lezione già pagata | Cosa impone |
|---|---|
| il wrapper `claude.CMD` troncava i prompt multiriga alla prima riga | il prompt si passa **da stdin**, mai in argv |
| `--model sonnet` restituiva `claude-sonnet-4-6`: l'alias mente | si passa **l'ID esplicito** e si **verifica** `modelUsage` nella risposta |
| limite di spesa sfondato in silenzio | `--output-format json` dà `total_cost_usd`; il budget si verifica **prima** di ogni chiamata |
| ~0,08-0,11 $ di sola tassa d'invocazione | si lavora **a blocchi**, non a unità minima, o la tassa mangia tutto |

Il piano LANCI non contiene **nessuna** di queste quattro righe. Un ecosistema con 41 agenti che
ignora la tassa d'invocazione ha un costo per lancio che nessuno ha calcolato.

**Riparazione:** la V4 eredita il pattern di ADR-014 come vincolo, con il costo per lancio
calcolato in anticipo e un tetto di spesa per lancio, come esiste per i libri (5 $/libro).

---

### E-03 — Il mandato vero dell'ecosistema è già scritto in ADR-016, e il piano non lo cita
**Gravità: alta. È un difetto di identità, non di dettaglio.**

ADR-016 «L'ULTIMO METRO» (2026-09-03, ATTIVO) misura che l'azienda ha **25 pezzi finiti mai
usciti, 2.137 MB fermi, il più vecchio da 135 giorni, zero vendite documentate**. E chiude
dichiarando il buco che resta aperto:

> «**Non esiste una misura di cosa succede DOPO la pubblicazione** (visualizzazioni, vendite,
> conversioni). L'Ultimo Metro chiude il buco fra "prodotto" e "pubblicato"; **resta aperto
> quello fra "pubblicato" e "venduto". È il prossimo da chiudere.**»

**Quello è il mandato dell'ecosistema LANCI, già registrato due giorni prima del piano.**
Il piano invece si presenta come «l'organo che mette in fila le capacità e istruisce prezzo e
data»: giusto ma parziale, e soprattutto **scollegato dalla catena di organi che esiste già**.

La catena vera, che la V4 deve dichiarare come propria posizione:

```
Memory (ADR-002)        interno: nessun lavoro è fatto finché non è salvato
Ultimo Metro (ADR-016)  prodotto → pubblicato
LANCI                   pubblicato → venduto → misurato     ← IL POSTO VUOTO
Tesoreria (ADR-020)     l'euro nei conti dell'azienda
```

**Riparazione:** la V4 si apre dichiarando questa posizione. Un ecosistema che sa qual è l'anello
prima e quale dopo è architettura; un organigramma di dodici reparti è una lista.

---

### E-04 — Il piano contraddice la propria diagnosi
**Gravità: massima sul dimensionamento.**

Il dossier 00 §1 diagnostica, e la diagnosi è giusta:

> «Digital Empire non ha un buco di *capacità* sui lanci. Ha un buco di **decisione ed
> esecuzione**. Le capacità esistono già.»

E la risposta a un buco di decisione è: **12 reparti, 41-50 agenti, ~235 file, 139-187 ore-uomo,
~3 mesi di calendario.** Quella è la risposta a un buco di capacità, non di decisione.

Il piano lo sente e prova a rimediare con lo scaglione minimo, ma il minimo è comunque
**54-72 ore-uomo prima che esca un euro** (S0 24-32 + S1 30-40), cioè **un mese e mezzo a tre
ore al giorno** — per vendere un prodotto che è pronto da sei mesi e a cui manca un numero.

**La contro-obiezione onesta, che va scritta:** un ecosistema serve anche ai lanci futuri, non
solo a questo. Vero. Ma il piano stesso pone la condizione d'uscita n.2 (dossier 09 §10): se il
pilota non esce entro 60 giorni si ferma tutto. Con S0+S1 a 54-72 ore, il piano **consuma quasi
tutta la propria condizione d'uscita in infrastruttura**, prima di aver provato la sola ipotesi
che conta: che il collo di bottiglia sia davvero organizzativo.

**Riparazione:** invertire l'ordine. Prima il lancio vero con l'osso minimo (giorni, non mesi),
poi l'ecosistema costruito **sui difetti misurati di quel lancio**. Non è meno architettura: è
architettura guidata da dati invece che da previsione.

---

## B. IL BUCO CHE ATTRAVERSA TUTTO IL PIANO: nessun numero previsto

**In 3.718 righe non compare mai la domanda «quanto ci aspettiamo di incassare».**

C'è il prezzo (47 €), c'è il budget, c'è il pareggio nominato, c'è il consuntivo a posteriori.
Non c'è **il modello**: quante persone vedono l'offerta × quante comprano × a che prezzo.

Conseguenze concrete, tutte e tre gravi:

1. **La firma del prezzo resta cieca.** Il dossier 04 §6 presenta «47 €» con le alternative 27 e
   97, ma senza dire cosa cambia in ricavo. Chi firma sta scegliendo un numero, non un risultato.
   Con il modello la domanda diventa: *«47 € su una lista di N con una conversione del 2% fa X.
   27 € fa Y. Confermi?»* — ed è una domanda che si firma in dieci secondi.
2. **Il gate del budget è insoddisfacibile.** `GATE-TSR-1` pretende il «pareggio calcolato»
   (dossier 00 §5.2), ma il pareggio è ricavo previsto contro costo, e il ricavo previsto non
   esiste in nessun artefatto del piano. **Un gate che chiede un dato che nessun reparto produce
   non può passare.**
3. **Non si può sapere se il lancio è andato bene.** Senza previsione, il consuntivo è un numero
   solo: non c'è scarto, e senza scarto non c'è nulla da imparare. Il reparto Memoria eredita un
   compito impossibile.

**Riparazione:** un artefatto nuovo, `previsione.json`, prodotto **prima** della firma e
confrontato col consuntivo alla chiusura. È il pezzo che rende l'ecosistema previsionale invece
che descrittivo — ed è anche l'unico modo di chiudere B-043 («DE non misura un solo euro»).

---

## C. DIFETTI PUNTUALI CHE HO VERIFICATO IO

### E-05 — Contraddizione fra dossier 01 e dossier 09 sullo scaglione minimo
Il dossier 01 §5 **corregge** lo scaglione minimo dopo la critica: da 9 agenti su 4 reparti a
**11 agenti su 6 reparti**, e lo dimostra: i nove non sanno produrre `ricerca.json` né
`certificato-prodotto.json`, e nessuno di loro scrive `offerta.json` — «un lancio avviato così si
sarebbe fermato in VALUTATO per sempre».

Il dossier 09 §4 — che è **il piano di costruzione**, quello che si esegue — dice ancora:
«**Quattro reparti** [...] **Nove agenti**: direttore dell'ecosistema, segretario, filtro della
strategia, prezzo, struttura dell'offerta, verificatore delle pagine, calendarista, tracciatore,
motore dei gate» (righe 94-105), **compreso il `segretario` che il dossier 01 §5.1 dichiara
esplicitamente eliminato**.

**La correzione è stata scritta in un dossier e non propagata nell'altro.** Chi costruisce apre il
09, non il 01: costruirebbe esattamente la configurazione che il piano stesso ha dimostrato
impossibile. È un difetto di consistenza fra documenti, ed è la prova che 11 dossier separati non
sono un formato sicuro per un piano che si corregge a giri.

### E-06 — S5 sparisce dal totale delle ore
Il dossier 09 §8 descrive lo scaglione S5 (automazione), ma la tabella §9 conta solo S0-S4.
Il totale «139-187 ore» **non include S5**. O S5 ha un costo e va contato, o non è uno scaglione.

### E-07 — Il costo in denaro non compare mai
Nessuna riga del piano dice quanto costa **far girare** un lancio (chiamate ai modelli). Con 41
agenti e la tassa di ~0,08-0,11 $ per invocazione misurata in ADR-014, il costo per lancio è una
grandezza reale e non calcolata. Un ecosistema che non conosce il proprio costo unitario non può
calcolare nessun pareggio — e infatti vedi B.2.

### E-08 — Tre numerazioni per la stessa cosa
`26-ECOSISTEMA-LANCI.md` (il documento L3 di Gael), `29-ECOSISTEMA-LANCI/` (questo pacchetto),
`15-LANCI` (il numero dell'ecosistema). Chi cerca «i lanci» trova tre numeri diversi. Va scelta
una convenzione e dichiarata in testa.

### E-09 — La stima si dichiara fatta «per analogia con l'unico flusso di questo repo che è stato
costruito e funziona davvero» (dossier 09 §9) e **non dice quale sia**. Non verificabile: una
stima la cui base non si può controllare non è una stima, è un numero.

---

## C-bis. I TRE FATTI PORTATI DALLA RICOGNIZIONE DELLE ORIGINI (file ORIGINE.md)

### E-10 — Il piano progetta il lancio di un prodotto il cui canale di traffico è SPENTO
**Gravità: massima sul pilota. Nessun documento del piano lo sa.**

`second-brain-vault/wiki/log.md`, righe 1054-1063, 2026-07-29/31, testuale:

> «CORREZIONE: il primo contenuto YouTube reale generato era ancora sul funnel morto "Manuale
> Claude Code" — pivot deciso da Gael a @dosementale come canale sorgente (replica per un canale
> da vendere già monetizzato, **zero funnel**).»
> «`apex7_orchestrator.py` (F1-F5) riscritto per intero su @dosementale — prima era solo il
> contenuto ad essere cambiato, il motore restava cablato sul Manuale Claude Code.»

Cinque settimane prima che questo piano nascesse, **il motore di traffico del prodotto pilota è
stato dichiarato morto e dirottato altrove**, in codice, non a parole. Le fonti L1, L2, L3, il
checkpoint CP-20260905-015 e tutti gli 11 dossier del piano **non lo menzionano mai** e continuano
a trattare il Manuale come «pronto, manca solo prezzo e data».

**Perché è devastante per il piano com'è:** il dossier 09 §4 sceglie quattro reparti per S1
*«perché sono esattamente ciò che manca al Manuale: tutto il resto quel prodotto ce l'ha già»*.
Non ce l'ha già: **non ha più il pubblico**. E l'ecosistema, con l'ordine attuale, se ne
accorgerebbe solo al momento dell'apertura del carrello — cioè dopo 54-72 ore-uomo di costruzione.

**Riparazione:** la V4 mette la **verifica del pubblico** prima di tutto il resto, e la rende
gate. Non si istruisce un prezzo per un'offerta che nessuno vedrà: si misura prima quante persone
si possono raggiungere il giorno dell'apertura, e quel numero entra nella previsione (§B).

### E-11 — Quattro prezzi per lo stesso prodotto, mai riconciliati, e il piano ne ignora due
**Gravità: alta, colpisce proprio il reparto che è il cuore del piano.**

| Fonte | Valore | Data |
|---|---|---|
| `Info-Business-HQ_Knowledge/.../CATALOGO PRODOTTI ATTUALE` | «€ NON LO SO» | 07/03/2026 |
| `second-brain-vault/wiki/09 - Archives/legacy/entities/Manuale_Claude_Code_Product.md` | «TBD (**€297-€497** recommended)» | 29/04/2026 |
| `PRODUCT_LADDER.md` (5 fasce recuperate da L2) | fasce €97-297 / €497-997 | — |
| **dossier 04 §6 di questo piano** | **47 €**, «livello 1 (7-47 €)» | 05/09/2026 |

La proposta di prezzo del piano è **un sesto del valore minimo** suggerito dalla fonte del 29
aprile, e il dossier 04 non cita né quella fonte né il listino: costruisce la giustificazione su
un solo listino, come se le altre non esistessero. Il blocco `NON SO` della proposta (che è
un'ottima invenzione) dichiara *«quanto è disposto a pagare questo pubblico: non è mai stato
misurato»* — ma tace il fatto ben più imbarazzante che **in casa esistono già tre risposte diverse
e nessuno le ha messe una accanto all'altra**.

**Riparazione:** la fase O0 («consulta la memoria») diventa obbligatoriamente una
**riconciliazione delle fonti di prezzo esistenti**, con l'elenco dei valori trovati e la loro
data, e la proposta deve spiegare perché si discosta da ciascuno. Un prezzo proposto senza
guardare i prezzi che l'azienda si è già data non è istruito: è inventato con più pagine.

### E-12 — La scadenza mancata non è dichiarata da nessuna parte
`second-brain-vault/wiki/09 - Archives/legacy/projects/Claude_Code_Mastery_Launch.md` (29/04/2026)
contiene un piano di lancio con **«START 2026-04-29 → TARGET SHIP 2026-05-30»** e tre milestone
datate. La data obiettivo è passata da **oltre tre mesi**. Nessun documento dell'azienda registra
il mancato rispetto, e il nuovo piano non lo cita.

**Perché conta, e non è pignoleria:** significa che **esisteva già un piano di lancio per questo
prodotto**, con date e milestone, ed è morto in silenzio. Un ecosistema che nasce per curare
l'incapacità di lanciare deve partire dall'autopsia del lancio già fallito, non ignorarlo. È
letteralmente il caso di studio più vicino che l'azienda possieda.

**Riparazione:** l'autopsia di quel piano diventa un ingresso obbligato della V4 — cosa c'era,
cosa mancava, in che punto esatto si è fermato. Senza, si rischia di ricostruire lo stesso piano
con più reparti attorno.

### E-13 — Il vincolo di Max, ripetuto due volte, e la seconda volta è oggi
`TASK-GAEL-20260831-SETTIMANA-02.md` registra l'ordine di Max del 2026-09-04: *«Deve essere tutto
ancora più architettato»* — **prima** che questo piano fosse consegnato. Ed è la stessa cosa che
Max ha ripetuto oggi, 2026-09-05, davanti al piano finito.

Questo va letto senza addolcirlo: **il piano V3 non ha soddisfatto una richiesta che era già stata
posta**, e la ragione non è la quantità (3.718 righe sono tante) ma la natura: il piano è
**organizzativo** dove doveva essere **ingegneristico**. Ha reparti, missioni, confini, ruoli — e
non ha schemi dati versionati, contratti verificabili, invarianti, gestione degli errori, modello
di costo, modello previsionale, osservabilità. «Più architettato» non vuol dire più reparti: vuol
dire che ogni pezzo del sistema è **specificato al punto che due persone diverse lo costruirebbero
uguale**. Oggi non lo è.

---

## D. CIÒ CHE È SOLIDO E VA SALVATO — non si butta il buono

1. **Il principio di §0 del dossier 04**: *«un gate posto su una decisione umana deve arrivare con
   la decisione già istruita; "decidi" delega la fatica, "confermi questo?" la toglie»*.
   È il pensiero migliore dell'intero pacchetto e va promosso a legge dell'ecosistema.
2. **La forma della proposta** (dossier 04 §6): numero + due alternative con la conseguenza +
   il blocco `NON SO` esplicito. Va tenuta parola per parola e solo arricchita con il ricavo previsto.
3. **`SOSPESO` con `stato_di_partenza`, `revisione_il`, `come_si_esce` come comando eseguibile**
   (dossier 01 §4.3). È architettura vera.
4. **La memoria come condizione di chiusura di fase** invece che come dovere (dossier 01 §3.1).
5. **Le tre condizioni di abbandono** (dossier 09 §10). Pochissimi piani le hanno.
6. **La modalità pilota con attestazione firmata, a scadenza e con debito** (dossier 01 §5.2):
   è un'eccezione progettata invece di una scorciatoia improvvisata.
7. **La metrica «giorni fra ISTRUITO e la firma, oggi 180, bersaglio ≤3»** (dossier 04 §12).
8. **Il divieto della parola «pianificato» senza data e nome** (dossier 09 §1).
9. **La nota d'apertura a Gael**: è scritta bene e risolve un problema umano vero.
