---
Type: PROJECT
Status: Proposta
Tags: #lanci #ecosistema-15 #copy #APSOC
Created: 2026-09-05
---

# 06 — WF-CPY · IL FLUSSO DEI TESTI

> Terza versione. La griglia di punteggio è stata **rifatta** dopo la critica: la versione
> precedente dichiarava sessanta punti calcolabili a macchina e ne aveva undici, e la sua soglia
> bocciava per costruzione otto pezzi su quattordici. Il paragrafo 9 dice cosa è cambiato.

---

## 1. Identità

| Campo | Valore |
|---|---|
| **Sigla** | `WF-CPY` |
| **Nome** | Flusso dei materiali di marketing |
| **Missione** | Produce **tutti i testi del lancio nell'ordine giusto** — la pagina di vendita come documento madre, e da lei ogni altro pezzo — con ogni pezzo passato dal suo gate prima di uscire |
| **Proprietario** | `LAN-CPY` — avvolge il reparto Copywriting di 04-MARKETING, il reparto Email-Lifecycle, la skill `cro-copy-architect` e la guild che sorveglia lo standard |
| **Durata** | **40-55 ore-uomo**, di cui 15-20 di sola valutazione |

> ⚠️ **La durata è cambiata dopo la critica.** La versione precedente diceva "5-8 giorni" e non
> contava il tempo di valutazione, che con una griglia in gran parte giudicata **non è
> trascurabile**: sono 2-3 ore a pezzo sui pezzi lunghi. Dichiararlo adesso evita la sorpresa
> della seconda settimana.

---

## 2. Trigger e precondizioni — il gate d'ingresso è spezzato in due

> ⚠️ **Correzione importante.** La versione precedente chiedeva `offerta.json` per far partire
> **tutto** il flusso, comprese le fondamenta. Ma **una grande promessa non contiene un prezzo**:
> bloccare anche quella dietro la decisione ferma da sei mesi significa **riprodurre il blocco che
> l'ecosistema esiste per sciogliere.**

| Fase | Cosa richiede | Perché |
|---|---|---|
| **C1 — Fondamenta** (grande promessa, mappa delle obiezioni) | ricerca **+** architettura del prodotto. **Non il prezzo** | la promessa si scrive e si fa approvare **mentre** Max decide il prezzo |
| **C2 in poi** (pagina di vendita e tutto il resto) | `offerta.json` con prezzo e data | pagina di vendita, cassa, video e webinar contengono il pacchetto di valore, l'ancoraggio e l'invito all'azione: **senza prezzo sono scrivibili solo a metà, e la metà mancante è quella che vende** |

**Il guadagno concreto:** il giorno in cui il prezzo esiste, la pagina di vendita parte in
ventiquattro ore invece che in tre giorni, perché la promessa è già scritta e già approvata.

**Comando:** `/lancio-copy <lancio_id>` · `--fondamenta` per la sola fase C1.

---

## 3. La gerarchia di scrittura, e il suo perché

Prima il **fondamento** (grande promessa + mappa delle obiezioni), poi la **pagina di vendita**,
poi tutto il resto.

**La pagina di vendita viene prima perché è il documento madre:** contiene per intero
l'argomentazione — promessa, meccanismo, prove, obiezioni, offerta. Ogni altro pezzo è una
**derivazione**: la pagina d'ingresso è la sua promessa compressa, i video sono la sua versione
parlata, le email ne distribuiscono le sezioni nel tempo, gli annunci ne sono l'aggancio.

Scrivere i derivati prima della madre produce incoerenza di messaggio e rifacimenti a catena:
ogni modifica alla madre costa N riscritture. Con quest'ordine, costa zero.

---

## 4. Le fasi

| # | Fase | Cosa fa | Agente | Output | Ore | Parallelo | Umano |
|---|---|---|---|---|---:|---|---|
| **C0** | Intake | valida l'input, congela la lista dei pezzi in base al tipo di funnel | `lan-cpy-conductor` | `copy/00-intake.json` | 1 | no | no |
| **C1** | **Fondamenta** | la **grande promessa unica**, il posizionamento contro i buchi dei concorrenti, la **mappa delle obiezioni** ordinata per frequenza × intensità, il tono di voce estratto, il lessico da usare e da vietare | `lan-cpy-fondamenta` | `copy/01-fondamenta.md` + `copy/01-obiezioni.json` | 6-8 | no | **Sì, 30 min** — vedi §7 |
| **C2** | Pagina di vendita | la madre, con la struttura completa e il pacchetto di valore | `lan-cpy-vendita` | `copy/10-vendita.md` | 8-12 | no | no |
| **GATE-CPY-1** | il giudizio sulla madre | la griglia (§5) | `lan-cpy-giudice` → `sentinel-quality` | `copy/gate/10-punteggio.json` | 3 | — | — |
| **C3a** | Pagine del funnel | ingresso, ringraziamento, cassa | `lan-cpy-derivati` | `copy/20-*.md` | 4-6 | **sì** | no |
| **C3b** | Video | breve (3-5 min) ed evento (8-12 min) | `lan-cpy-derivati` | `copy/30-*.md` | 5-7 | **sì** | no |
| **C3c** | Webinar | derivato dalla grande promessa (§6) | `lan-cpy-derivati` | `copy/40-webinar.md` | 6-8 | **sì** | no |
| **C3d** | Le quattro sequenze email | pre-lancio, vendita aperta, recupero, accoglienza | `lan-cpy-email` | `copy/50-*.md` | 8-10 | **sì** | no |
| **C3e** | Annunci | per canale, tre angoli diversi | `lan-cpy-derivati` | `copy/60-*.md` | 3-4 | **sì** | no |
| **C4** | Coerenza | corrispondenza fra i passaggi del funnel, copertura delle obiezioni, voce del marchio | `lan-cpy-giudice` + `sentinel-brandvoice` | `copy/70-coerenza.json` | 3 | no | no |
| **C5** | Consegna | il manifest, e la verifica che ogni file dichiarato esista | `lan-cpy-bibliotecario` | `copy/manifest.json` | 2 | no | **Sì, 30 min** |

---

## 5. LA GRIGLIA DI PUNTEGGIO — rifatta

### 5.1 L'errore della versione precedente, dichiarato

La versione precedente scriveva: *"~60 punti sono calcolabili o verificabili a macchina"*.
**Falso.** Verificato voce per voce: i punti genuinamente deterministici erano **11** (densità di
numeri, corrispondenza fra passaggi, dotazione di varianti), che diventavano 19 con una sola voce
implementata bene.

**Sessanta dichiarati contro undici reali.** Il gate era per l'ottanta per cento *un giudizio con
un numero attaccato* — cioè precisamente la cosa che il piano vieta.

E c'era di peggio: la stessa griglia si applicava a ogni pezzo, con la regola *"nessun blocco sotto
metà dei suoi punti"*. **Facendo il conto, una pagina d'ingresso da 150 parole non poteva
passare il proprio gate**: non ha spazio per dieci frasi del pubblico né per cinque punti di
dolore, quindi il suo blocco B usciva sotto la metà per costruzione. **Otto pezzi su quattordici
bocciati sempre.** Un gate che boccia sempre viene disattivato al secondo lancio.

### 5.2 La correzione, in tre mosse

| # | Mossa | Effetto |
|---|---|---|
| 1 | **I testi nascono strutturati**, non come prosa libera: front-matter e blocchi marcati (`::claim`, `::prova`, `::beneficio`, `::azione`, `::variante`) | quattro voci diventano conteggi veri: si passa da **11 a ~42 punti** davvero automatici |
| 2 | **Tre griglie, non una**, per classe di pezzo | i pezzi corti smettono di essere bocciati per ciò che non possono contenere |
| 3 | **Due voci ambigue diventano meccaniche**, definendole su liste già esistenti | la voce eliminatoria e quella anti-genericità smettono di essere opinioni |

### 5.3 Le tre classi di pezzo

| Classe | Quali pezzi | Griglia | Soglia |
|---|---|---|---|
| **Madre** | pagina di vendita, script del webinar | griglia piena, 100 punti | **≥80** e nessun blocco sotto metà |
| **Pagina breve** | ingresso, ringraziamento, cassa, video breve | le voci che non si applicano **escono dal denominatore** | **≥80% dei punti applicabili** |
| **Micro** | singola email, singolo annuncio | cinque voci soltanto: aggancio, problema o promessa, voce eliminatoria, anti-genericità, una sola azione | binaria: tutte e cinque superate |

**Perché il denominatore variabile e non voci a zero:** una pagina d'ingresso *non deve* contenere
cinque punti di dolore. Darle zero su quella voce è punirla per aver fatto bene il suo mestiere.

### 5.4 La griglia madre — 100 punti, e quali sono automatici

**Blocco A — struttura (30 punti, 5 per voce)**

| Voce | Punti | Criterio | Auto? |
|---|---:|---|---|
| A1 Attenzione | 5 | titolo con un elemento specifico della ricerca; nessun claim indimostrabile in apertura | giudizio |
| A2 Problema | 5 | dolore preso dalla ricerca e citabile; **se la soluzione appare prima del problema → 0** | parziale |
| A3 Promessa e meccanismo | 5 | la trasformazione "da → a" presa dall'architettura del prodotto, **non inventata**, più il meccanismo nominato | giudizio |
| A4 Prova | 5 | ≥3 prove di ≥2 categorie. **Una sola prova non verificabile → 0** | **auto** con i blocchi `::prova` |
| A5 Obiezioni | 5 | le prime cinque della mappa, ognuna completa di affermazione, prova e beneficio | **auto** con i blocchi marcati |
| A6 Offerta e azione | 5 | pacchetto esplicito con valore ≥3 volte il prezzo; **una sola** azione; motivo per agire adesso che sia reale | **auto** se il pacchetto è un dato |

**Blocco B — aderenza alla ricerca (20 punti)**

| Voce | Punti | Criterio | Auto? |
|---|---:|---|---|
| B1 Frasi del pubblico | 8 | ≥10 frasi della ricerca usate — **vedi §5.5 per il metodo** | **auto** |
| B2 Dolori coperti | 6 | 5 su 5 → 6 · 4 su 5 → 3 · ≤3 → 0 | giudizio |
| B3 Buchi dei concorrenti | 6 | ≥3 trasformati in argomenti | giudizio |

**Blocco C — obiezioni (15 punti)**

| Voce | Punti | Criterio | Auto? |
|---|---:|---|---|
| C1 Obiezioni complete | 9 | 5 su 5 con affermazione + prova + beneficio | **auto** con i blocchi |
| C2 Dubbi generati e non gestiti | 6 | zero → 6 · uno → 3 · ≥2 → 0 | giudizio |

**Blocco D — specificità e prova (15 punti)**

| Voce | Punti | Criterio | Auto? |
|---|---:|---|---|
| D1 Affermazioni provate | 6 | 100% provate o riformulate | parziale |
| D2 Densità di numeri | 5 | ≥5 numeri concreti ogni 1.000 parole | **auto** |
| **D3 Promesse indimostrabili** | 4 | **voce eliminatoria** — vedi §5.6 | **auto**, dopo la correzione |

**Blocco E — voce e anti-genericità (10 punti)**

| Voce | Punti | Criterio | Auto? |
|---|---:|---|---|
| E1 Test di sostituzione | 5 | vedi §5.7 | **auto**, dopo la correzione |
| E2 Voce del marchio | 5 | verdetto di `sentinel-brandvoice`, che **esiste già** | delegato |

**Blocco F — meccanica (10 punti)**

| Voce | Punti | Criterio | Auto? |
|---|---:|---|---|
| F1 Una sola azione | 4 | inviti multipli alla **stessa** azione → 4; azioni diverse → 0 | **auto** con i blocchi |
| F2 Corrispondenza col passaggio precedente | 3 | il pezzo dichiara da dove arriva | **auto** |
| F3 Dotazione per i test | 3 | **solo sui pezzi che avranno traffico sufficiente** — vedi §5.8 | **auto** |

**Il conto onesto: ~42 punti automatici su 100**, non sessanta. E la parte giudicata ha **ancore
di punteggio e motivazione scritta obbligatoria** per ogni voce sotto il massimo.

### 5.5 La similarità delle frasi — il metodo, che prima mancava

La versione precedente scriveva *"similarità ≥0,8"* **senza dire con quale metodo**. È una soglia
vuota: con un confronto carattere per carattere una parafrasi vera non arriva mai a 0,8 e la voce
vale sempre zero; con un confronto di significato, 0,8 lo raggiunge quasi ogni frase dello stesso
argomento e la voce vale sempre otto. **La stessa soglia, due comportamenti opposti, e la scelta
lasciata a chi costruisce.**

| | Deciso |
|---|---|
| **Metodo** | coseno su rappresentazione semantica multilingue (modello `paraphrase-multilingual-MiniLM-L12-v2`), normalizzato |
| **Soglia** | **0,72** |
| **Obbligo** | il piano consegna una **tabella di taratura con dieci coppie di frasi e il punteggio atteso**, così l'implementazione si verifica invece di essere creduta |

**Regola generale che ne discende:** *nessuna soglia di similarità entra in un piano senza il
metodo e la tabella di taratura.* Una costante senza metodo non è un criterio.

### 5.6 La voce eliminatoria — definita, e quindi automatizzabile

Prima diceva: *"una sola promessa indimostrabile boccia il pezzo, anche a 96 punti"*, e **non
diceva chi decide che una promessa è indimostrabile**. Era il punto di massimo arbitrio del
sistema, in mano all'organo meno controllabile.

**La definizione operativa, adesso:**

> Una promessa è **indimostrabile** quando afferma un **risultato del lettore** (un guadagno, un
> tempo, un esito) che:
> **(a)** non corrisponde a nessun output pratico verificabile nell'architettura del prodotto, **e**
> **(b)** non è sostenuto da almeno una prova di categoria *dimostrazione* o *testimonianza* già
> presente nelle fondamenta.

**Con questa definizione la voce diventa un controllo su due liste** — gli output pratici
dell'architettura e le prove delle fondamenta — quindi **automatica**, e il veto smette di essere
un'opinione.

E distingue ciò che prima si confondeva: **promessa di risultato** (bocciabile senza prova) da
**promessa di contenuto** (verificabile leggendo il prodotto).

### 5.7 Il test di sostituzione — reso meccanico

L'idea era buona — *sostituisci il nostro nome con quello del concorrente: il testo deve rompersi*
— ma "si rompe in almeno cinque punti" non è misurabile, e "il concorrente principale" non era
nemmeno definito.

**Adesso si conta:** il numero di affermazioni del pezzo che citano **un elemento dichiarato
assente nei concorrenti** (i buchi trovati dalla ricerca) **oppure un dato proprietario** (un
numero nostro, una data, il nome di un metodo, una storia vera).

≥5 → 5 punti · 2-4 → 3 · ≤1 → 0.

È un conteggio su due liste già esistenti. E *"il concorrente principale"* si definisce
nell'input: è il primo dell'elenco.

### 5.8 La dotazione per i test — legata al traffico, non imposta a tutti

Prima si chiedevano tre varianti di titolo e due di invito all'azione **su ogni pezzo**. Su
ventotto email fanno **196 varianti** — da testare con un metodo che il piano stesso dichiara
inapplicabile sotto i trecento visitatori per versione.

**Adesso:** la voce si applica **solo ai pezzi che riceveranno abbastanza traffico per decidere**
— pagina di vendita e pagina d'ingresso. Sugli altri vale `non applicabile`, ed esce dal
denominatore.

E se il volume atteso è sotto i trecento per versione, **si producono due varianti e si sceglie
per mestiere**, come prescrive il flusso del funnel. Coerenza fra documenti, che prima non c'era.

### 5.9 Chi giudica — e chi ha il veto

> ⚠️ **Correzione:** la versione precedente creava `lan-copy-giudice` come organo di giudizio,
> mentre **`sentinel-quality` esiste già** ed è l'agente il cui mandato è *vigilare sul punteggio
> dei testi sotto la soglia e sugli output senza prova, su ogni consegna*. Era una duplicazione
> dell'unico organo che aveva esattamente quel compito.

| Chi | Ruolo |
|---|---|
| `lan-cpy-giudice` | **esegue** la griglia e produce il punteggio |
| `sentinel-quality` *(già esistente)* | **riceve** i punteggi e ha il **potere di veto** |

La griglia diventa il criterio della sentinella dell'Impero, non un secondo tribunale.

---

## 6. Il webinar — quattro derivazioni di una frase sola

Il metodo parte da **una domanda unica**: *qual è l'unica idea che, se il pubblico la percepisce
raggiungibile, rende tutte le altre obiezioni irrilevanti?*

Da quella promessa discendono, in cascata:

| Pezzo | Come deriva |
|---|---|
| **Il titolo** | la promessa in forma di beneficio specifico |
| **L'apertura** | caso reale → domanda scomoda → verità che riformula il problema |
| **I tre segreti** | ciascuno demolisce **una** delle tre obiezioni più forti, e riconduce alla promessa |
| **Il pitch** | il percorso che rende la promessa raggiungibile, col pacchetto e il motivo per agire adesso |

**Non sono quattro pezzi: sono quattro derivazioni della stessa frase**, e il gate lo verifica —
se il titolo non è riconducibile alla promessa, il webinar non passa.

---

## 7. I punti umani — con la scadenza e cosa succede allo scadere

> ⚠️ **Il difetto che la critica ha trovato ed è il più pericoloso di tutti:** il flusso completo
> di un lancio passa **sei volte** per una decisione di Max in trentasette giorni, e la versione
> precedente non dichiarava **mai** cosa succede se la risposta non arriva. In un'azienda dove
> Max ha altre quattro linee di business, è la causa numero uno per cui i piani a fasi muoiono.

**Per ogni punto umano ci sono solo due comportamenti onesti allo scadere**, e vanno scritti prima:

| Punto | Chi | Scadenza | Allo scadere |
|---|---|---|---|
| Approvazione dei moduli del prodotto | Max o Gael | 48 h | **si procede** con l'architettura proposta, marcata `approvata per silenzio` nel verbale |
| **Approvazione della grande promessa** | Max | 48 h | **si ferma e si sposta la data** — non esiste un default per la promessa: è la frase da cui discende tutto |
| Reclutamento dei beta tester | Max | 7 giorni | escalation con tre opzioni scritte: allunga, recluta lui, o deroga firmata |
| Firma del prezzo | Max | 7 giorni | l'inerzia diventa **una voce di stato del lancio**; a 14 giorni il lancio va in sospensione con data di revisione |
| Approvazione finale dei testi | Max | 48 h | **si procede** con i testi che hanno superato il gate, marcati `consegnati per silenzio` |
| Via libera a T-1 | Max | 24 h | **si ferma e si sposta la data** |

**La regola generale:** dove esiste un default ragionevole, si procede e lo si dichiara. Dove non
esiste, si ferma e si sposta la data. **Un'attesa senza scadenza non è un punto di controllo: è un
punto di morte.**

---

## 8. Il riuso dei componenti già esistenti — la verità, corretta

> ⚠️ **Il piano precedente dichiarava una cosa falsa, verificata sul codice.** Diceva che il
> reparto Copy consegna il contenuto delle obiezioni *"tipizzato sui parametri che i componenti si
> aspettano"*. **Quei componenti non hanno parametri:** il contenuto è scritto dentro il codice.

**Cosa è vero, misurato:**

| Fatto | Conseguenza |
|---|---|
| I cinque componenti di gestione obiezioni **non accettano parametri** | vanno **parametrizzati**: è lavoro vero, va assegnato e stimato (mezza giornata), e sta sul percorso critico |
| Appartengono alla pagina di un'**agenzia di servizi web**, non a un info-prodotto | tre obiezioni su quattro sono di un altro pubblico (*"ho già un sito"*) |
| Il file vive in una cartella duplicata | **va deciso quale delle due copie è la fonte**, prima di toccarle |

**Quindi il riuso è del guscio grafico, non del contenuto.** È comunque un guadagno — la parte
difficile di quei componenti è il comportamento visivo — ma va detto per quello che è.

**Questa correzione vale più di quanto sembri:** due documenti dichiaravano verificato un
contratto che non esisteva. È la forma leggera della malattia che tutto questo piano combatte, e
l'ha commessa il piano stesso.

---

## 9. Cosa è cambiato dalla prima versione

| Cambiamento | Contro quale obiezione |
|---|---|
| Le fondamenta **non dipendono più dal prezzo** | *"il piano blocca la promessa dietro la decisione ferma da sei mesi, cioè riproduce il blocco che vuole risolvere"* |
| **Tre griglie per classe di pezzo**, con denominatore variabile | *"la pagina d'ingresso non può passare il proprio gate per costruzione: otto pezzi su quattordici bocciati sempre"* |
| I punti automatici dichiarati sono **42, non 60**, e i testi nascono strutturati per arrivarci | *"sono undici, e il documento si autoconfuta nella sezione degli script"* |
| La similarità ha **metodo, soglia e tabella di taratura** | *"0,8 senza metodo è o impossibile o gratuito, e la scelta resta a chi costruisce"* |
| La voce eliminatoria ha una **definizione a due liste** | *"chi decide che una promessa è indimostrabile non è mai nominato"* |
| Il test di sostituzione diventa **un conteggio** | *"si rompe è la parola meno misurabile del documento"* |
| La dotazione per i test si applica **solo dove c'è traffico** | *"196 varianti da testare con un metodo che il piano stesso vieta"* |
| Il giudizio passa a **`sentinel-quality`**, che esiste già | *"il piano duplica l'unico organo che ha esattamente quel mandato"* |
| **Sei punti umani con scadenza e comportamento allo scadere** | *"il percorso critico passa sei volte per la stessa persona senza un solo timeout"* |
| Il riuso dei componenti è **corretto e stimato** | *"il contratto dichiarato non esiste: verificato sul codice"* |
| La durata include **le ore di valutazione** | *"quattro o cinque giorni-uomo di sola valutazione, non previsti"* |
| L'anti-plagio passa a **dieci parole**, con soglia a due sequenze | *"a otto parole i falsi positivi su frasi idiomatiche sono garantiti"* |
