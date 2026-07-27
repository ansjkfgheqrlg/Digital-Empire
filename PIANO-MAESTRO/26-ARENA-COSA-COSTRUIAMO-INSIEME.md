# 26 — ARENA: COSA COSTRUIAMO INSIEME (contratto operativo + arsenale prompt Max & Gael)

> Creato **2026-07-27 (lunedì)** da Arena, su richiesta diretta di Max: *"dimmi le task che dovremo fare
> io e Gael con te, cosa possiamo costruire con te… non sarai tu a costruire le cose: ci darai solamente
> i prompt ampi + indicazioni."*
> **Presa d'atto: accettato.** Questo dossier definisce il mio ruolo, poi consegna **8 prompt ampi**
> pronti da incollare, con indicazioni, gate e destinazione dell'output.
> Ogni numero e ogni path qui dentro è stato **letto sul disco oggi**, non ricordato.
> Riferimenti vivi: dossier [19](19-ARENA-BUILD-LIST.md), [21](21-ARENA-PROMPTS-MASTER-PACK.md),
> [23](23-ANALISI-PRODOTTI-DE-POTENZIALE.md), [24](24-CALENDARIO-ESECUTIVO-ESTATE-V2-E-S7.md),
> [25](25-GAEL-TASK-BOARD-OPERATIVO.md).

---

## §0 — IL CONTRATTO: chi sono io e cosa NON faccio

Max ha ragione a fissarlo subito, quindi lo scrivo nero su bianco e ci vincolo il resto del documento.

| | **ARENA (io)** | **MAX + GAEL (+ Claude Code locale)** |
|---|---|---|
| Ruolo | **Cervello di progettazione.** Analisi, architettura, prompt, gate, review, dossier | **Mani.** Esecuzione, credenziali, mondo reale, decisioni di business |
| Produce | Prompt ampi, indicazioni, spec, checklist, criteri di accettazione, autocritica | Codice che gira, email inviate, chiamate fatte, video pubblicati, soldi incassati |
| Non fa | Non manda email, non scrapa live, non pubblica, non tocca i vostri segreti, non chiude vendite | Non deve riprogettare da zero ciò che gli passo già progettato |

**Perché questa divisione non è una limitazione ma la scelta giusta:** io lavoro su un **clone del repo**,
senza le vostre credenziali (`.env`, OAuth YouTube, sessioni browser) — che è esattamente come deve essere.
Tutto ciò che tocca il mondo esterno resta vostro. In cambio io brucio contesto e tempo di analisi
**al posto vostro**, senza consumare la sessione locale di Claude Code mentre lui costruisce.

### Il loop di lavoro con me (3 tempi)
```
1. VOI  → mi date un obiettivo ("fai partire l'outbound su Verona") o un problema
2. IO   → prompt ampio + indicazioni + gate + dove salvare + autocritica dei rischi
3. VOI  → eseguite in locale con Claude Code → mi riportate l'output/errore
4. IO   → review indipendente (passo 6 del ciclo a 9 passi, ADR-006) → correzione o via libera
```
Il passo 4 è quello che vale di più e che oggi vi manca: **una revisione fatta da chi non ha costruito.**
Il vostro `AGENTS.md` la impone (REGOLA UNO), ma finora review e build cadono spesso sulla stessa sessione.

---

## §1 — LA VERITÀ DI PARTENZA (misurata oggi, non stimata)

Prima di dire cosa costruire, dico cosa **c'è già**, perché il rischio numero uno di questo repo è
ricostruire roba che esiste (ADR-003: *wrappa, non riscrivere*).

| Fatto misurato | Numero reale | Fonte sul disco |
|---|---|---|
| Agenti censiti | **435** | `WORKFLOW-ESTATE/03-AGENTI-E-RUOLI/STATO-AGENTI.md` |
| Di cui **operativi** | **57 (13,1%)** | idem — 324 parziali, 54 documentali |
| Prodotto consegnato a cliente reale | **1** (Novacar, via `Clienti/Prof Autocad`) | sezione sito `agency-empire/src/sections/09b-prove-novacar.tsx` |
| Ticket workflow a listino | **€5.000–15.000** | dossier 23 §1 |
| Ticket Preventa | **€490 setup + €149/mese** | `agency-empire/src/sections/03b-preventa.tsx` |
| Macchina outreach | **esiste e gira** | `Outreach/Outreach Workflow/empire_auto_v3.py` |
| Script APSOC concessionari | **già scritti (5 documenti)** | `Outreach/preventa-outreach-pack` |
| Skill YouTube completa | **esiste, mai eseguita in produzione** | `.claude/skills/youtube-automation-factory` |
| Sistema nervoso APEX-7 | **Level 2 operativo, test verdi** | `company/Ecosistemi/12-STREAM-S7-BOT/STATO-RIPRESA.md` |

### 🩸 La diagnosi onesta (ve la devo, è il vostro stesso standard)

**Non vi manca niente da costruire. Vi manca di FAR GIRARE.**

Il task board (dossier 25) segna `G-A4` — il **run reale** dell'outreach su Verona/Padova/Vicenza — come
**"🟢 SBLOCCATO"**, con gli input di Max già dati. Sbloccato il 23/07. Oggi è il 27/07: **quattro giorni**,
e lo stato è ancora "sbloccato", non "completo". Nel frattempo sono stati chiusi refactoring, APEX-7 Level 2,
ricostruzioni di agenti — tutto lavoro buono, **tutto a valle di zero euro incassati**.

Il dossier 24 lo aveva già scritto nella sua autocritica: *"Ancora nessun euro incassato… l'incasso arriva
con l'outbound."* Quella riga è ancora vera 4 giorni dopo. **Questo è il collo di bottiglia, ed è l'unica
cosa che i prompt qui sotto sono ordinati per risolvere.**

Traduzione operativa: dei prossimi 7 giorni, **il 70% del tempo va sui prompt del Blocco A** (cassa).
Blocco B e C esistono, ma non prima che A abbia prodotto **numeri veri** (email partite, risposte, demo).

---

## §2 — COSA POSSIAMO COSTRUIRE INSIEME (le 4 categorie)

| # | Categoria | Cosa faccio io | Cosa fate voi | Valore |
|---|---|---|---|---|
| 1 | **Macchine di cassa** | progetto sequenze, script, criteri di qualifica, gate anti-figuraccia | eseguite, mandate, chiamate | 🟢🟢 diretto |
| 2 | **Fabbriche di contenuto** | architettura pipeline, prompt di produzione, rubriche di qualità | fate girare, pubblicate | 🟢 compounding |
| 3 | **Infrastruttura agenti** | spec APEX-7, criteri operativi C1-C6, review indipendente | scrivete il codice, testate | 🟡 abilitante |
| 4 | **Asset di vendita** | copy, struttura, obiezioni, prove | approvate, impaginate, usate | 🟢 sblocca ticket alti |

**Cosa NON ha senso chiedermi** (ve lo dico ora per non farvi perdere giri):
- di eseguire scraping live, mandare email, pubblicare video → **non ho le vostre credenziali, ed è giusto così**;
- di decidere prezzi o ICP al posto vostro → sono decisioni di business, restano di Max (ADR);
- di riscrivere da zero pezzi già funzionanti → violerebbe ADR-003, e vi ha già morso in passato.

---

## §3 — TASK BOARD: chi fa cosa questa settimana (27/07 → 02/08)

### 🔵 MAX — il collo di bottiglia sei tu su 3 cose, ~90 min/giorno
| Quando | Task | Perché tocca a te e non a Gael |
|---|---|---|
| **Lun 27** | **M-A1** — dai l'ok al lancio outbound reale (lista A + lista B) e fissa il **tetto giornaliero** di email (consiglio: 20/giorno per dominio, in salita) | è rischio reputazione del dominio: decisione tua |
| **Lun 27** | **M-A2** — consegna il **materiale di prova Novacar**: 2-3 numeri veri + 1 screenshot PDF + 1 frase del cliente | senza prove un ticket da €10k non si chiude a freddo (dossier 23 §5) |
| **Mar 28** | **M-A3** — blocca **2 slot/giorno** in agenda per le chiamate a freddo. Le chiamate restano umane (dossier 25) | è l'unico anello che nessuna macchina copre |
| **Mer 29+** | **M-A4** — fai le demo che arrivano. Script demo: prompt **P4** | vendi tu |
| Continuo | **M-A5** — ogni sera: 3 righe in `company/Memory/STATO-EMPIRE.md` (contatti, risposte, demo) | senza misura non sapete se funziona |

### 🟣 GAEL — build, ma solo quello che serve alla cassa (in quest'ordine, rigido)
| Quando | Task | Prompt da usare | Gate |
|---|---|---|---|
| **Lun 27** | **G-1** run reale outbound lista B (concessionari Verona/Padova/Vicenza) | **P1** | prime 20 email partite, 0 bounce hard |
| **Lun-Mar** | **G-2** lista A (ICP workflow €5-15k) + dogfooding | **P2** | 40 lead qualificati, score ≥7 |
| **Mar 28** | **G-3** war-room: cruscotto giornaliero contatti→risposte→demo | **P3** | 1 numero visibile ogni mattina |
| **Mer-Gio** | **G-4** refactoring scraper in ecosistema APEX-7 (era G-A5) | **P5** | 6 pilastri Art.8, `python -m empire conform` senza block |
| **Gio-Ven** | **G-5** YouTube APEX-7 end-to-end (era G-B5) | **P6** | 1 video prodotto dalla pipeline senza mani |
| **Ven-Sab** | **G-6** batch agenti documentali → operativi | **P7** | +15 agenti operativi misurati |

### ⚫ ARENA (io) — quello che vi consegno mentre voi eseguite
| Task | Output | Quando |
|---|---|---|
| **AR-1** questo dossier + 8 prompt | ✅ fatto ora | oggi |
| **AR-2** review indipendente di ogni output che mi riportate | verdetto + difetti trovati | on demand |
| **AR-3** kit di vendita workflow €5-15k (pagina proposta + obiezioni) | **P4** in versione compilata | quando Max dà M-A2 |
| **AR-4** autopsia settimanale: cosa ha prodotto numeri, cosa no | dossier 27 | domenica 02/08 |

---

## §4 — L'ARSENALE: 8 PROMPT AMPI

> **Come si usano.** Ogni prompt è auto-contenuto: si apre Claude Code **nella cartella del repo** e si
> incolla il blocco tra `=== INIZIO PROMPT ===` e `=== FINE PROMPT ===`. I prompt sono scritti
> **idempotenti** (rilanciarli non rompe nulla) come impone il vostro ciclo a 9 passi.
> Ogni prompt finisce con la stessa coda obbligatoria: checkpoint + STATO-EMPIRE + push.

### 🔻 CODA OBBLIGATORIA (vale per tutti gli 8 — è già inclusa in ognuno)
```
Chiudi il lavoro così, senza saltare passaggi:
1. Scrivi il checkpoint SOLO con il runtime, mai a mano:
   python -m empire mem write --kind checkpoint --view
   (la scrittura manuale è il bug B-009 del BACKLOG: ha già causato 4 collisioni di ID)
2. Aggiorna company/Memory/STATO-EMPIRE.md con: cosa hai fatto, cosa resta, RIPRESA DA
3. Verifica: python -m empire conform   (zero block prima di committare)
4. git add -A && git commit && git push
```

---

## 🥇 BLOCCO A — CASSA (fare questa settimana, prima di tutto il resto)

### P1 — RUN REALE OUTBOUND CONCESSIONARI (Preventa) — owner Gael, ok di Max
**Obiettivo business:** trasformare `G-A4` da "sbloccato" a **"prime 20 email partite"**. È il task che
è fermo da 4 giorni ed è il più vicino a un euro incassato.
**Prerequisito:** ok di Max sul tetto giornaliero (M-A1).

`=== INIZIO PROMPT P1 ===`
```
CONTESTO. Sei dentro il monorepo Digital Empire. Prima di toccare qualsiasi cosa leggi
company/Memory/INDEX.md e company/Memory/STATO-EMPIRE.md (REGOLA ZERO del file AGENTS.md).

OBIETTIVO UNICO DI QUESTA SESSIONE: mandare in produzione la campagna outbound verso i
concessionari auto di Verona, Padova e Vicenza per vendere Preventa (490 euro setup +
149 euro al mese). Non costruire niente di nuovo: tutto l'occorrente esiste già.

ASSET DA WRAPPARE, MAI DA RISCRIVERE (regola ADR-003, verifica che esistano prima di partire):
- motore outreach live: Outreach/Outreach Workflow/empire_auto_v3.py
- script APSOC gia' scritti: Outreach/preventa-outreach-pack
- scraper lead: Outreach/preventa-maps-scraper
Se qualcosa non parte, RIPARA il pezzo esistente: non creare un secondo motore parallelo.

FAI, IN QUEST'ORDINE, FERMANDOTI AL PRIMO ERRORE VERO:

1) STATO REALE. Dimmi in una tabella secca: quanti lead ci sono gia' caricati, di quali
   province, quanti hanno email valida, quanti sono duplicati. Numeri contati sul file,
   non stimati. Se i lead di Verona/Padova/Vicenza non ci sono, estraili adesso.

2) GATE ANTI-FIGURACCIA (obbligatorio, prima di ogni invio). Scrivi ed esegui un controllo
   che blocca la partenza se anche solo una di queste e' falsa:
   - ogni email ha un destinatario con dominio che risolve (niente MX morti)
   - nessun placeholder rimasto nel testo (cerca parentesi quadre, XXX, TODO, nome_azienda)
   - il nome del salone nel messaggio combacia col lead giusto (test incrociato su 5 a caso)
   - esiste un link di disiscrizione e un riferimento fisico mittente
   - nessun lead e' gia' stato contattato nei 90 giorni precedenti
   Il gate deve stampare VERDE/ROSSO per criterio, e uscire con codice 1 se rosso.

3) DRY-RUN VISIBILE. Genera i primi 20 messaggi REALI su lead REALI ma senza inviare, e
   salvali in un file che io possa leggere. Mostrami 3 messaggi interi in chat: li approvo
   a occhio prima dell'invio.

4) INVIO GRADUALE. Solo dopo il mio ok esplicito in chat: invia 20 messaggi, non uno di piu'.
   Warm-up del dominio: 20 oggi, 30 domani, 50 dopodomani, mai a gradini piu' ripidi.
   Registra ogni invio con timestamp in un log persistente.

5) FOLLOW-UP ARMATO. Verifica che la sequenza G+2 / G+5 sia schedulata davvero sui lead
   inviati oggi (non solo che lo script esista). Dimostramelo mostrando le date calcolate.

6) NUMERO DEL GIORNO. Stampa una riga sola, che Max leggera' domani mattina:
   "inviate N | consegnate N | aperte N | risposte N | demo N".

REGOLE DURE:
- Non inventare lead, non inventare email, non inventare risultati. Se un dato non c'e', dillo.
- Nessuna credenziale nel repo: solo .env locale.
- Se il volume di invio supera il tetto, fermati e chiedi.

AUTOCRITICA FINALE OBBLIGATORIA: elenca le 3 cose che nel run di oggi possono farci finire
in spam o farci fare brutta figura col cliente, e cosa hai messo in piedi per evitarle.

[CODA OBBLIGATORIA: checkpoint via runtime + STATO-EMPIRE + conform + push]
```
`=== FINE PROMPT P1 ===`

**Gate di accettazione:** 20 email realmente partite, log su disco, 0 placeholder, follow-up schedulato.
**Se fallisce:** non passare a P2. Il problema è qui.

---

### P2 — LISTA A: DOGFOODING PER IL TICKET GROSSO (€5-15k) — owner Gael
**Obiettivo business:** il dossier 23 dice che **una vendita workflow vale più di tutti i 7 concessionari
di settembre messi insieme**. E la leva migliore è il *dogfooding*: usare la nostra macchina di outreach
per venderci la macchina di outreach.

`=== INIZIO PROMPT P2 ===`
```
CONTESTO. Monorepo Digital Empire. Leggi prima company/Memory/STATO-EMPIRE.md e
PIANO-MAESTRO/23-ANALISI-PRODOTTI-DE-POTENZIALE.md (spiega perche' questo task e' il jackpot).

OBIETTIVO: costruire la LISTA A e la sequenza di contatto per vendere i workflow done-for-you
da 5.000 a 15.000 euro (Outreach Workflow e Content Workflow). Il canale e' outbound freddo,
perche' l'inbound non esiste (le pagine IG sono a zero, dossier 23 §0).

L'ARGOMENTO DI VENDITA PIU' FORTE CHE ABBIAMO, USALO COME SPINA DORSALE:
"Il sistema che ti sto vendendo e' esattamente quello con cui ti ho trovato e contattato."
Questa frase deve essere dimostrabile in ogni messaggio, non solo dichiarata.

ICP GIA' DECISO DA MAX (non ridiscuterlo): aziende del Nord Italia con fatturato 1-5 milioni
che vendono a business e hanno un commerciale o un piccolo team vendite, ma nessun sistema di
acquisizione ripetibile. Il segnale di dolore che cerchiamo: assumono venditori ma non hanno
flusso di lead.

FAI:

1) SEGNALI DI QUALIFICA. Progetta un punteggio 1-10 basato su segnali OSSERVABILI dall'esterno
   (non su supposizioni). Esempi di segnale forte: annunci di lavoro aperti per commerciali o
   business developer (= vogliono crescere ma non hanno sistema), sito senza alcuna form di
   contatto qualificata, nessun caso studio pubblicato, presenza LinkedIn del titolare attiva.
   Per ogni segnale dichiara: dove si legge, quanto pesa, perche'.

2) ESTRAZIONE. Costruisci la lista di almeno 40 aziende che rispettano l'ICP, con: azienda,
   sito, settore, nome e ruolo del decisore, fonte del contatto, segnali trovati, punteggio.
   Usa fonti pubbliche. Se un dato non lo trovi, lascia il campo vuoto: MAI riempirlo a intuito.

3) SEQUENZA IN 4 TEMPI, in italiano nativo, ognuno sotto i 700 caratteri:
   - T1 gancio: cita UN segnale specifico e verificabile di quella azienda (niente "ho visto il
     vostro sito e mi piace molto"). Chiudi con una domanda facile, non con una richiesta di call.
   - T2 (+2 giorni) prova: il caso Novacar con numeri veri, presi da
     agency-empire/src/sections/09b-prove-novacar.tsx. Non gonfiare nulla.
   - T3 (+5 giorni) rovesciamento: mostra che li abbiamo trovati col sistema che vendiamo.
   - T4 (+9 giorni) chiusura educata: lasciali andare in modo che restino aperti in futuro.

4) OBIEZIONI DEL TICKET ALTO. Tabella a 4 colonne (obiezione, cosa nasconde davvero, risposta
   parola per parola, prova da mostrare) su almeno queste: "costa troppo", "ci pensiamo a
   settembre", "abbiamo gia' un'agenzia", "lo facciamo internamente", "non abbiamo tempo di
   seguirvi", "mandami una mail".

5) CABLAGGIO. Aggancia la lista A al motore esistente Outreach/Outreach Workflow come SECONDA
   campagna separata, senza toccare la campagna concessionari gia' viva. Due liste, un motore.

VINCOLI: nessuna promessa di risultato garantito, nessun numero inventato, nessuna finta
urgenza. Il lettore e' un imprenditore che riceve 20 email uguali al giorno: la nostra deve
essere l'unica che dimostra di aver guardato la sua azienda per davvero.

AUTOCRITICA FINALE: quali sono le 3 ragioni piu' probabili per cui questa sequenza verra'
ignorata, e cosa hai cambiato nel testo per ridurle.

[CODA OBBLIGATORIA: checkpoint via runtime + STATO-EMPIRE + conform + push]
```
`=== FINE PROMPT P2 ===`

**Gate:** 40 lead con score, 4 messaggi scritti, campagna separata cablata, dry-run pulito.

---

### P3 — WAR-ROOM: IL NUMERO CHE VEDETE OGNI MATTINA — owner Gael
**Obiettivo:** oggi non sapete se l'outbound funziona, perché **nessuno misura**. Un cruscotto brutto ma
vero batte una dashboard bella che nessuno apre.

`=== INIZIO PROMPT P3 ===`
```
CONTESTO. Monorepo Digital Empire. Esiste gia' un runtime con un comando dash
(python -m empire dash) e una cartella 06-DASHBOARD-E-METRICHE nei workflow: usali, non
costruire una dashboard nuova da zero (ADR-003).

OBIETTIVO: ogni mattina Max deve vedere UN SOLO schermo con lo stato della cassa. Non
analytics: il minimo che fa prendere una decisione.

LE UNICHE 6 METRICHE AMMESSE (se ne aggiungi altre, stai sbagliando):
1. contatti inviati ieri / totale settimana
2. risposte ricevute (positive, negative, neutre) con il testo delle positive in chiaro
3. demo prenotate e per quando
4. proposte inviate e loro valore in euro
5. euro effettivamente incassati (non "pipeline", non "potenziale": incassati)
6. il prossimo passo assegnato a una persona con una data

REQUISITI:
- deve girare con un comando solo e stampare a terminale, senza server e senza browser
- se un dato manca deve scrivere "non misurato", mai zero: zero e' un'informazione, mancante e' un'altra
- deve leggere i log reali prodotti dalla campagna, non un file compilato a mano
- se il valore di oggi e' peggiore di ieri, deve dirlo esplicitamente con una riga di allarme

Aggiungi un file breve che spieghi a Max come lanciarlo (un comando, nient'altro).

AUTOCRITICA FINALE: quale di queste 6 metriche rischia di essere raccolta male e portare a una
decisione sbagliata, e come l'hai resa affidabile.

[CODA OBBLIGATORIA: checkpoint via runtime + STATO-EMPIRE + conform + push]
```
`=== FINE PROMPT P3 ===`

---

### P4 — KIT DI VENDITA DEL TICKET GROSSO — owner Max (con me)
**Obiettivo:** il gap CRO numero 1 individuato nel dossier 23 è **la mancanza di prove**. Questo prompt lo chiude.
**Prerequisito:** M-A2 (Max consegna il materiale Novacar).

`=== INIZIO PROMPT P4 ===`
```
CONTESTO. Digital Empire vende workflow done-for-you da 5.000 a 15.000 euro. Abbiamo un solo
caso reale documentato: Novacar (concessionario, software di preventivazione consegnato e in
uso). I numeri veri sono nella sezione sito agency-empire/src/sections/09b-prove-novacar.tsx:
leggili da li' e non alterarli di una virgola.

OBIETTIVO: produrre il kit che permette a Max di chiudere una vendita da 5-15k senza
improvvisare. Tre pezzi.

PEZZO 1 - CASO STUDIO IN UNA PAGINA. Struttura: situazione di partenza (cosa faceva il
concessionario prima, con il dettaglio noioso e concreto del lavoro manuale) / cosa abbiamo
costruito / cosa e' cambiato in numeri misurati / cosa direbbe il cliente. Scrivilo in modo che
un imprenditore che non capisce niente di software capisca perche' vale soldi. Vietato l'uso di
"innovativo", "all'avanguardia", "soluzione a 360 gradi", "rivoluzionario".

PEZZO 2 - SCRIPT DELLA DEMO CALL DA 30 MINUTI. Minutaggio esplicito:
  0-3   inquadrare: perche' siamo qui, cosa succede nei prossimi 27 minuti, permesso di procedere
  3-12  diagnosi: le domande che fanno dire al cliente da solo quanto gli costa il problema
        (in ore perse e in clienti persi, quantificati da lui, non da noi)
  12-22 dimostrazione ancorata a quello che ha appena detto, non un tour del prodotto
  22-27 prezzo detto ad alta voce senza scuse, e silenzio
  27-30 prossimo passo con data
  Per ogni blocco: le frasi esatte, e cosa fare se il cliente svicola.

PEZZO 3 - LA PAGINA DI PROPOSTA. Un documento che Max manda dopo la demo: ambito preciso di cosa
e' incluso e cosa no, tempi, prezzo, condizioni di pagamento, cosa serve dal cliente, cosa
succede se le cose vanno male. Deve essere cosi' chiaro da non richiedere una seconda chiamata
per spiegarlo.

REGOLE: italiano nativo, tono da pari a pari. Niente garanzie di risultato. Il prezzo si dice,
non si nasconde in fondo. Se un numero non lo abbiamo, si scrive "da misurare insieme": mai
inventarlo, perche' la prima bugia scoperta uccide un ticket da 10k.

AUTOCRITICA FINALE: qual e' il punto piu' debole di questo kit davanti a un imprenditore
scettico che ha gia' avuto una brutta esperienza con un'agenzia, e come lo hai coperto.
```
`=== FINE PROMPT P4 ===`

---

## 🥈 BLOCCO B — MACCHINE (dopo che il Blocco A ha prodotto numeri)

### P5 — SCRAPER → ECOSISTEMA APEX-7 (era G-A5) — owner Gael

`=== INIZIO PROMPT P5 ===`
```
CONTESTO. Leggi company/Memory/STATO-EMPIRE.md e
company/Ecosistemi/12-STREAM-S7-BOT/STATO-RIPRESA.md: APEX-7 e' gia' operativo a Level 2
(Event Bus, Memory a 5 query, 6 quality gate, Gate Agent, Meta-Agent) e i test sono verdi.
Questo lavoro non inventa un'architettura: APPLICA quella.

OBIETTIVO: portare Outreach/preventa-maps-scraper da script a ecosistema completo secondo
l'articolo 8 del Mandato (i 6 pilastri) e il metodo APEX-7.

CONDIZIONE DI PARTENZA NON NEGOZIABILE: lo scraper oggi alimenta una campagna VIVA. Se lo rompi,
fermi la cassa. Quindi:
- prima di toccare qualsiasi cosa, fai girare quello che c'e' e registra l'output come baseline
- ogni modifica deve lasciare l'output identico o migliore rispetto alla baseline, e lo dimostri
- il vecchio punto di ingresso deve continuare a funzionare anche dopo il refactoring

FAI:
1) fotografia: cosa fa oggi, quali file, dove si rompe, quali dati produce (contati, non stimati)
2) i 6 pilastri riempiti davvero, non cartelle vuote: flussi, automazioni, agenti, skill,
   template, metriche
3) gli agenti dello scraper devono essere OPERATIVI secondo i 6 criteri gia' implementati in
   empire/forge.py (identita', ruolo, ingresso, uscita, successo, comportamento). Il buco piu'
   comune nel nostro parco agenti e' l'USCITA: il 73% non dichiara cosa produce. Non ripeterlo.
4) i quality gate di APEX-7 applicati ai punti dove lo scraper puo' sbagliare in silenzio:
   lead duplicati, telefoni malformati, aziende chiuse, categoria sbagliata
5) misura finale con: python -m empire forge scan  (dimmi il prima e il dopo)

GATE DI USCITA: python -m empire conform senza block, baseline rispettata, forge scan che
mostra il miglioramento in numeri.

AUTOCRITICA FINALE: cosa in questo refactoring rischia di rompere la campagna in produzione, e
come lo hai reso reversibile.

[CODA OBBLIGATORIA: checkpoint via runtime + STATO-EMPIRE + conform + push]
```
`=== FINE PROMPT P5 ===`

---

### P6 — YOUTUBE END-TO-END, MODELLO AUTORITÀ (era G-B5) — owner Gael
**Framing vincolante** (dossier 20): Andrei Pascu fa **100-500 view a video** e guadagna **€3.750-6.710/mese**
— *non* dall'AdSense, ma vendendo prodotti. Dose Mentale ha **198.000 iscritti** e l'ultimo video **649 view**.
Quindi: **si costruisce il canale-funnel, non il canale-views.**

`=== INIZIO PROMPT P6 ===`
```
CONTESTO. Leggi PIANO-MAESTRO/20-ANALISI-YOUTUBE-PIANO-CHIRURGICO.md prima di scrivere una riga:
contiene dati reali estratti dai canali, e la conclusione che vincola questo lavoro.

VINCOLO STRATEGICO: il canale NON punta alle visualizzazioni ne' all'AdSense. Punta ad autorita'
e vendita di prodotti. Un video da 200 visualizzazioni giuste vale piu' di uno da 20.000
sbagliate. Ogni scelta della pipeline deve rispondere a: questo porta un cliente, o solo view?

ASSET ESISTENTE DA WRAPPARE: .claude/skills/youtube-automation-factory contiene gia' 11 agenti e
i workflow. Non ricostruirla: rendila eseguibile davvero. Oggi non e' mai girata in produzione.

OBIETTIVO: una pipeline che da un'idea arriva a un video pronto alla pubblicazione senza che
nessuno debba invocare gli step a mano.

CATENA DA RENDERE AUTOMATICA:
  scelta argomento (dal dolore reale dei lead che rispondono all'outbound, non dalle keyword)
  -> struttura del video con i primi 15 secondi scritti parola per parola
  -> copione completo
  -> voce e montaggio
  -> copertina e titolo
  -> descrizione con il link tracciato al prodotto
  -> pubblicazione
  -> lettura delle metriche a 7 giorni che rientra nella scelta del prossimo argomento

REQUISITI DURI:
- deve essere rilanciabile: se cade al passo 5, riparte da 5 e non da 1
- ogni passaggio lascia una traccia leggibile: si deve poter capire perche' ha deciso cosi'
- un gate di qualita' che blocca la pubblicazione se: il video non ha una CTA a un prodotto
  nostro, oppure i primi 15 secondi non contengono una promessa concreta, oppure il titolo
  promette qualcosa che il contenuto non mantiene
- la pubblicazione vera resta dietro un interruttore che di default e' spento: prima si guarda
  il video, poi si accende

PROVA CHE VOGLIO: un video reale prodotto dalla catena dall'inizio alla fine, e il file finito
che posso guardare. Non uno schema di come funzionerebbe.

AUTOCRITICA FINALE: dove questa pipeline produrra' contenuto mediocre indistinguibile dagli
altri mille canali di AI in italiano, e cosa hai messo per impedirlo.

[CODA OBBLIGATORIA: checkpoint via runtime + STATO-EMPIRE + conform + push]
```
`=== FINE PROMPT P6 ===`

---

### P7 — AGENTI DA CARTA A OPERATIVI (batch misurato) — owner Gael

`=== INIZIO PROMPT P7 ===`
```
CONTESTO. python -m empire forge scan oggi dice: 435 agenti, 57 operativi (13,1%), 324 parziali,
54 documentali. Il buco piu' grande non e' il comportamento: e' l'USCITA, il 73% degli agenti non
dichiara cosa produce, quindi il loro lavoro non e' verificabile.

OBIETTIVO: promuovere un BATCH di 15 agenti, dando la precedenza a quelli che toccano i soldi
(acquisizione, preventivi, chiusura), non a quelli piu' facili.

METODO, uno per volta, senza scorciatoie:
1) python -m empire forge prossimo  per sapere chi e' il prossimo e cosa gli manca
2) leggi cosa c'e' gia' scritto: il contenuto originale si CONSERVA, si aggiunge, non si sostituisce
3) colma i criteri mancanti dando priorita' assoluta all'USCITA: cosa produce esattamente questo
   agente, in che formato, dove lo scrive, e come si capisce se e' venuto bene o male
4) rimisura quel singolo agente e mostrami il punteggio prima e dopo
5) checkpoint + commit: un agente promosso = una fase chiusa (metodo deciso il 25/07)

DIVIETI:
- vietato il riempimento di facciata per far salire il punteggio: se un agente e' inutile,
  proponi di archiviarlo invece di gonfiarlo. Preferisco 400 agenti veri a 435 finti.
- vietato toccare i file di corredo (evals, failure-modes): non sono agenti, sono gia' esclusi
- attenzione ai comandi con la barra dentro i backtick nei file markdown: hanno gia' rotto il
  controllo conform 4 volte (e' scritto nel BACKLOG). Scrivili senza backtick.

ALLA FINE: fammi vedere la tabella riassuntiva prima/dopo dei 15, e i 3 agenti che secondo te
andrebbero archiviati invece che promossi, con la motivazione.

[CODA OBBLIGATORIA: checkpoint via runtime + STATO-EMPIRE + conform + push]
```
`=== FINE PROMPT P7 ===`

---

## 🥉 BLOCCO C — LEVA (quando A e B girano)

### P8 — L'AUTOPSIA SETTIMANALE (il prompt che tiene onesto il sistema) — owner Max, ogni domenica

`=== INIZIO PROMPT P8 ===`
```
CONTESTO. Monorepo Digital Empire. Leggi company/Memory/STATO-EMPIRE.md, i checkpoint della
settimana in company/Memory/checkpoints e i log della campagna outbound.

OBIETTIVO: dirmi la verita' su questa settimana, non farmi sentire bene.

RISPONDI A QUESTE 6 DOMANDE, IN QUEST'ORDINE, CON I NUMERI SUL TAVOLO:
1. Quanti euro sono entrati questa settimana? Se zero, scrivi zero grande.
2. Quante persone nuove hanno saputo che esistiamo? (contatti realmente partiti)
3. Quante hanno risposto? Cosa hanno detto, testuale, le positive e le negative.
4. Cosa abbiamo costruito che NON ha ancora prodotto un solo contatto o un solo euro?
   Elencalo senza pieta', anche se e' bello e ci siamo divertiti a farlo.
5. Qual e' l'unica cosa che, se la settimana prossima facessimo solo quella, ci porterebbe
   piu' vicino a un incasso?
6. Cosa stiamo evitando di fare perche' e' scomodo? (di solito: telefonare, chiedere soldi,
   chiedere a un cliente soddisfatto di dirlo pubblicamente)

REGOLA: non ammorbidire. Se la settimana e' stata di costruzione pura senza cassa, dillo con
quelle parole. Il repo e' pieno di dossier che dicono "l'incasso arriva la settimana prossima":
se lo dice anche questo, e' un segnale che si e' rotto qualcosa nel metodo, non nel mercato.

Chiudi con: le 3 task della settimana entrante, una per Max, una per Gael, una per Arena.
```
`=== FINE PROMPT P8 ===`

---

## §5 — REGOLE DI INGAGGIO CON ARENA (come farmi rendere al massimo)

1. **Datemi l'obiettivo, non il compito.** "Voglio 5 demo prenotate" mi fa progettare meglio di
   "scrivimi un'email".
2. **Riportatemi gli errori interi**, non riassunti: traceback completo, output del comando.
   Un errore troncato mi fa indovinare, e indovinare è il modo in cui si perde tempo.
3. **Chiedetemi la review**, non solo la costruzione. Il vostro ciclo a 9 passi
   (`PIANO-MAESTRO/10-METODO-CICLO-FASE.md`) impone che chi rivede non sia chi ha costruito:
   io sono l'unico qui che può farlo strutturalmente.
4. **Un obiettivo per sessione.** I prompt sopra sono volutamente monomaniacali.
5. **Non chiedetemi il permesso per le decisioni di business.** Prezzi, ICP, chi chiamare: vostri.
   Io do lo scenario e i rischi, la firma è di Max.

---

## §6 — AUTOCRITICA DI QUESTO DOSSIER (obbligo del vostro stesso metodo)

1. **Rischio numero uno: questo diventa il ventiseiesimo dossier che nessuno esegue.** Il repo ha già
   25 dossier di piano, 435 agenti, 7 piani di ristrutturazione — e zero euro incassati questa settimana.
   *Difesa:* il Blocco A è composto da task che finiscono con un fatto verificabile dall'esterno
   (email partite, non "sistema pronto"). Se venerdì non ci sono 20 email partite, questo dossier ha fallito
   e va detto in P8, non riscritto in un dossier 27.
2. **Sto assumendo che il motore outreach parta al primo colpo.** Non l'ho eseguito: non ho le credenziali
   e non devo averle. *Difesa:* il passo 1 di P1 è una fotografia dello stato reale prima di ogni invio.
3. **Il tetto di 20 email/giorno può sembrare timido** con 61 lead già caricati. *Difesa:* un dominio bruciato
   costa mesi; una settimana di rampa costa 4 giorni. Il rischio è asimmetrico.
4. **Il Blocco B è più divertente del Blocco A, e questo è precisamente il pericolo.** Refactoring APEX-7 e
   pipeline YouTube sono lavoro affascinante; telefonare a un concessionario di Vicenza no. Il vostro storico
   dice che quando c'è scelta vince il lavoro affascinante. *Difesa:* l'ordine in §3 è vincolante, e P8
   chiede esplicitamente "cosa abbiamo costruito che non ha prodotto un euro".
5. **Non ho verificato di persona i 61 lead né la deliverability del dominio.** Sono dati che ho letto nei
   vostri documenti, non misurati da me. Vanno confermati nel passo 1 di P1 prima di fidarsene.

---

## §7 — LA RISPOSTA SECCA ALLA DOMANDA DI MAX

> *"Cosa possiamo costruire con te?"*

**Tre cose, in ordine di valore:**

1. **La disciplina di far girare quello che avete già.** Non vi serve un altro sistema: ne avete 435 pezzi.
   Vi serve qualcuno fuori dalla costruzione che chieda ogni settimana "quanti euro sono entrati" e non
   accetti "abbiamo rifattorizzato" come risposta. Questo lo posso fare io, e nessuno dentro il repo lo sta facendo.
2. **Prompt e architetture di qualità alta senza consumare la vostra sessione locale.** Io brucio il contesto
   sull'analisi, Claude Code lo brucia sul codice. È una divisione del lavoro, non una ridondanza.
3. **La review indipendente che il vostro metodo richiede e che oggi non avete.** Il passo 6 del ciclo a 9 passi
   esiste sulla carta; strutturalmente non può farlo chi ha appena costruito.

> *"Non sarai tu a costruire le cose?"*

**No. E lo trovo giusto** — non per modestia, ma perché la parte che vi manca non è la costruzione:
quella la sapete fare fin troppo bene. Vi manca il pezzo tra "costruito" e "incassato".
Quello si attraversa con le mani e con il telefono, e sono le vostre.

**Il primo passo è oggi: P1, venti email.** Il resto di questo documento conta zero finché quelle non partono.
