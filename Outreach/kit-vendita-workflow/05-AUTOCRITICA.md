# AUTOCRITICA DEL KIT — dove si rompe davanti a uno scettico

> Richiesta esplicita del prompt P4. Scritta da Arena, 2026-07-27.
> Domanda: *qual è il punto più debole di questo kit davanti a un imprenditore scettico che ha
> già avuto una brutta esperienza con un'agenzia?*

---

## LA RISPOSTA SECCA

**Il punto più debole è che Novacar non prova che sappiamo fare quello che stiamo vendendo.**

Non è un problema di come è scritto il caso studio. È un problema di **sostanza**, e nessuna
formulazione lo risolve:

| Cosa vendiamo | Cosa prova Novacar |
|---|---|
| Outreach Workflow / Content Workflow — macchine che **portano clienti** | un software di **preventivi auto** |
| €5.000-15.000 | consegnato a un cliente con ticket €490 + €149/mese |
| «vi troviamo clienti» | «vi produciamo un documento» |

Lo scettico che ha già preso una fregatura da un'agenzia **fa esattamente questa domanda**, ed è
la domanda giusta:

> *"Ok, avete fatto un programma per i preventivi di un concessionario. Io devo trovare clienti.
> Chi avete aiutato a trovare clienti?"*

**Oggi la risposta onesta è: nessuno ancora.** Non c'è un caso Outreach Workflow su disco. C'è un
motore che gira (`Outreach/Outreach Workflow/empire_auto_v3.py`), 61 lead caricati, e un run reale
che al 27/07 non risulta completato.

---

## COME L'HO COPERTO (e perché la copertura è parziale)

### 1. Non ho nascosto il salto: l'ho reso il messaggio
Nel Pezzo 1 e nello script (minuto 12) il caso Novacar è presentato **esplicitamente come fuori
settore**: *"ti faccio vedere una cosa che non c'entra niente col tuo settore, guarda la forma del
problema"*. Non provo a far passare il concessionario per un caso di lead generation.

**Quanto regge:** buono con chi ragiona per analogia. **Dove cede:** chi vuole la prova nel suo
settore non la accetta, e ha ragione lui.

### 2. Ho spostato la prova dal risultato al metodo
Il caso studio non dimostra "portiamo clienti". Dimostra tre cose più piccole ma **verificabili**:
consegniamo davvero, misuriamo quello che facciamo, mettiamo controlli che bloccano gli errori.
Il dettaglio delle **quattordici regole di impaginazione mai scritte da nessuno** è il pezzo più
forte del kit: mostra come lavoriamo, non cosa promettiamo.

**Quanto regge:** molto bene con imprenditori tecnici o operativi. **Dove cede:** con chi compra
solo risultati e non gli interessa il come.

### 3. Ho usato l'ammissione come leva (la mossa più forte del kit)
Nello script, **prima** che lo chieda il cliente:
> *"questo caso non dimostra che Novacar vende di più… la testimonianza firmata non ce l'ho ancora,
> e non te la invento"*

Chi ha appena preso una fregatura da un'agenzia ha sviluppato un radar per il gonfiato. Sentirsi
dire spontaneamente *"questo non lo dimostra"* è **l'unica cosa che quel radar non si aspetta**, e
sposta la fiducia più di qualsiasi numero.

**Quanto regge:** è la parte migliore, funziona proprio col profilo peggiore. **Dove cede:** se poi
sul sito trova "il 90% vuole iniziare la settimana dopo", l'effetto si annulla e diventa
controproducente — sembra che anche l'onestà fosse una tecnica. → **Vedi `04-AVVISO-CONFLITTO-SITO.md`.**

### 4. Ho messo per iscritto cosa succede se va male
La sezione 7 della proposta (*"se le cose vanno male"*) esiste solo per questo profilo di cliente:
cosa succede se sforiamo, se non si può fare, se vuole fermarsi, e la riga *"il workflow è vostro,
se ce ne andiamo non si spegne niente"*.

Chi è stato in ostaggio di un'agenzia (accessi, account, sistemi che muoiono col contratto)
riconosce quelle righe al volo, perché sono **esattamente** quello che gli è mancato l'altra volta.

**Quanto regge:** è la sezione che chiude i diffidenti. **Dove cede:** sono promesse scritte da noi.
Valgono finché non le rispettiamo la prima volta davvero.

---

## LE ALTRE 4 DEBOLEZZE (in ordine di gravità)

### ⚠️ 2 — Lo script presume un Max che sa stare zitto
Tre punti dello script vivono di silenzio: dopo il numero delle ore, dopo il prezzo, dopo *"rispetto
a cosa?"*. **Il silenzio dopo il prezzo è la singola tecnica più difficile della vendita**, e chi non
l'ha allenata lo rompe entro due secondi — vanificando tutto il blocco 22-27.

**Copertura parziale:** l'ho scritto esplicitamente (*"il primo che parla dopo il prezzo, perde"*).
**Cosa serve davvero:** provarlo ad alta voce due volte prima della prima demo. Non basta leggerlo.

### ⚠️ 3 — La proposta è un modello, non un documento
Ha ~15 campi tra parentesi quadre. Compilata male (parentesi rimaste, prezzo a intervallo, sezione
"non incluso" vuota) **fa più danno che bene**: sembra un template riciclato, che è precisamente
l'accusa che lo scettico si aspetta di poter fare.

**Copertura:** checklist finale in fondo al file. **Rischio residuo:** la fretta. Un cliente che
riceve una proposta con `[Nome]` dentro è un cliente perso, e non te lo dirà mai.

### ⚠️ 4 — La garanzia del sito non combacia con questi workflow
Il sito promette: *"se entro 30 giorni non produce almeno 1 risultato misurabile, rimettiamo mano
gratis"*, con esempi (lead generati, post pubblicati, email mandate).
**Il problema:** "1 risultato misurabile" è talmente basso che il cliente sveglio lo nota
(*"quindi mi garantite una email mandata?"*), mentre "lead generati" è talmente alto che dipende
dal suo mercato, non da noi.

L'ho riportata **fedelmente** nel kit (non potevo contraddire una promessa pubblica), ma va
ridefinita: **il risultato garantito dev'essere un output del sistema, non un esito di mercato.**

### ⚠️ 5 — Il kit non dice a chi NON vendere
Non c'è un criterio di squalifica. Con capacità di delivery dichiarata a **3 workflow/mese**
(M-EST-7), vendere al cliente sbagliato costa più che non vendere: blocca uno slot e produce un
cliente scontento senza testimonianza.

**Nello script c'è un accenno** (*"se dice meno di 6, chiudi presto"*), ma è debole. Servirebbero
3 criteri secchi di NO — es. nessun processo ripetibile esistente, nessun referente unico,
aspettativa di risultati di vendita garantiti.

---

## COSA RENDEREBBE QUESTO KIT MOLTO PIÙ FORTE (in ordine di impatto)

| # | Cosa | Sforzo | Impatto |
|---|---|---|---|
| 1 | **La testimonianza firmata di Novacar** — una telefonata di 10 minuti a un cliente soddisfatto. È l'asset a più alto rapporto valore/sforzo di tutto il repo | 10 min di Max | 🟢🟢🟢 |
| 2 | **Il dogfooding come caso studio**: far girare l'outreach su noi stessi e documentarlo (*"il sistema che ti vendo è quello con cui ti ho trovato"*) — copre esattamente il buco n.1 | dipende da P1 | 🟢🟢🟢 |
| 3 | **Sistemare i 4 punti del sito** (file 04) | 30 min di Gael | 🟢🟢 |
| 4 | **Un video di 90 secondi** della macchina Novacar che gira, da mandare prima della demo | 1 ora | 🟢🟢 |
| 5 | **3 criteri di squalifica** scritti | 15 min | 🟢 |

---

## LA COSA CHE NON POSSO RISOLVERE IO

Questo kit rende **massimamente vendibile ciò che avete oggi**. Non può creare la prova che manca.

La prova che manca — *"abbiamo portato clienti a qualcuno"* — si crea in un modo solo: **facendo
girare l'outbound su voi stessi e documentandolo.** È il P1 del dossier 26, quello segnato
"sbloccato dal 23/07" e non ancora completato.

**Finché quel run non parte, ogni demo che fai parte con una mano legata dietro la schiena** — e
nessun copy, nemmeno perfetto, la slega.
