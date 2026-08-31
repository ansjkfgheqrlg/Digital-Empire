---
Owner: Max (committente) · Esecutore: GAEL · Controllore: Claude (audit + review)
Origine: audit W1 richiesto da Max 2026-08-31 (verificato eseguendo il codice, non leggendo i checkpoint)
Governo: ADR-006 (ciclo 9 passi) + REGOLA ZERO memory-first + ADR-003 (wrap, mai riscrittura)
Emesso: 2026-08-31 · Settimana: W2 (lun 1 set -> dom 7 set 2026)
Riferimenti: TASK-GAEL-20260824-SETTIMANA-01.md (chiusa) · CP-20260825-002 · CP-20260827-001/002/003/004
---

# 📋 Task settimanali GAEL — Settimana 2 (1-7 settembre 2026)

## 0. Prima di tutto: la W1 è chiusa e verificata

Non te lo scrivo per farti un complimento, te lo scrivo perché conta per come parte questa
settimana. Max ha chiesto un controllo vero della W1 e l'ho fatto **rieseguendo il codice sulla
sua macchina**, non leggendo i tuoi checkpoint:

- `pytest tests/` nel workflow KDP → **135 passed in 22.31s** (esattamente il numero dichiarato
  nel commit `741c7b90`)
- `python -m engine.kdp stato` → **4 libri, 24/24 capitoli ciascuno, 36.871 / 37.168 / 38.128 /
  39.668 parole**
- `python -m engine.kdp pacchetto the-winter-term` → **exit 0, COMPLETO**
- `python -m engine.kdp pacchetto the-quiet-hours` → **exit 1**, e il motivo è giusto (manca
  `COPERTINA-PROMPT.md`, perché è un libro prodotto *prima* del fix)
- capitoli letti a campione: è prosa vera, non riempitivo

Il gate distingue davvero COMPLETO da CARICABILE, gli exit code sono corretti, il codice non
chiama nessun modello come dichiarato. **Il flusso funziona.** Le altre 5 task W1 hanno tutte
checkpoint con comando e output incollati (`CP-20260827-001..004`). Il lavoro c'è ed è onesto:
da qui in poi si scala, non si ricostruisce.

**Quindi la W2 non è una settimana di impianto: è riparare e poi correre.** Quattro task, in
quest'ordine esatto:

| | Task | Cosa produce |
|---|---|---|
| ⚫ | **TASK-KDP-FIX-W2** | ripara 6 difetti misurati — **si fa per prima, ordine di Max** |
| 🟣 | **TASK-KDP-PIANO-W2** | piano editoriale settimanale + 3 agenti + comando ufficiale |
| 🟢 | **TASK-KDP-5LIBRI-W2** | 5 libri completi in cartella |
| 🔴 | **TASK-LANCI-ECO-W2** | il piano dell'ecosistema Lanci (spezzato in L1→L6) |

---

# ⚫ TASK-KDP-FIX-W2 — **PRIMA DI TUTTO: sistemare quello che non va nei libri**

⚠️ **Questa task viene PRIMA delle altre tre. Ordine di Max.** Non aprire il piano editoriale, non
scrivere agenti, non iniziare libri nuovi finché questi 6 punti non sono chiusi. Sono tutti
difetti **misurati oggi 2026-08-31 rieseguendo il codice**, non impressioni.

Il senso è uno solo: **oggi la fabbrica produce libri che non arrivano da nessuna parte.**
Aumentare il ritmo prima di aver riparato questo significa moltiplicare per 5 un problema, non
una resa.

---

## FIX-1 — 4 libri scritti, **0 pubblicati**, 0 euro. Questo è il difetto numero uno.

**Misurato:**
```
LIBRI/libri_pubblicati/   ->  contiene solo .gitkeep
```
e però:

| Libro | `pubblicabile` | pagine reali | bloccanti | verifiche non eseguite |
|---|---|---|---|---|
| The_Quiet_Hours | **True** | 118 | 0 | 0 |
| The_Ninth_Winter | **True** | 119 | 0 | 0 |
| The_Second-Hand_Spellbook | **True** | 118 | 0 | 0 |
| The_Winter_Term | False | 116 | 1 (manca il .png) | 0 |

**Tre libri sono dichiarati pubblicabili dal tuo stesso codice, con zero bloccanti e zero
controlli saltati, e sono fermi su disco.** Il workflow è stato costruito per portare i libri su
KDP: fin qui ha prodotto manoscritti, non pubblicazioni. Un catalogo con 0 titoli online non
vende niente e non produce nemmeno un dato: senza vendite reali non sai se la nicchia funziona,
se il prezzo regge, se la copertina converte. **Stai costruendo al buio.**

**Cosa fai:**
1. Carichi su KDP i 3 libri già pubblicabili. L'upload è manuale e lo fa una persona (regola
   generale: le azioni irreversibili verso l'esterno le fa un umano) — **quella persona sei tu**,
   è scritto nella SOP: *"Gael genera la copertina e carica su KDP"*.
2. Generi il `.png` mancante di The_Winter_Term dal suo `COPERTINA-PROMPT.md`, poi
   `kdp consegna the-winter-term --cover <file.png>` e carichi anche quello.
3. Per ognuno registri l'ASIN:
   `python -m engine.kdp pubblicato <slug> --asin B0XXXXXXXX --prezzo <prezzo>`
   così `libri_pubblicati/` smette di essere vuoto e il catalogo esiste davvero.

**Se qualcosa ti blocca sull'upload** (account, verifica fiscale, KDP che rifiuta un file):
**scrivilo subito a Max, non aspettare la fine della settimana.** Se è un blocco esterno reale,
lo dici e passi al FIX-2 — ma dev'essere dichiarato, non silenzioso.

**Gate FIX-1**: 4 ASIN registrati (o, per ciascuno non caricato, il motivo esterno esplicito
scritto nel checkpoint). `ls LIBRI/libri_pubblicati/` non è più vuoto.

---

## FIX-2 — B-018 si è aggravato: 4 libri, 4 nicchie, 3 nomi d'autore

**Misurato** (`python -m engine.kdp nicchia-stato`):
```
Nicchia: small town romance suspense
Punteggio corrente: 77.4/100 (sana)
Libri nel catalogo: 0
```
La nicchia attiva ha **zero** libri. I 4 scritti stanno tutti fuori: psychological thriller,
amish romance suspense, cozy fantasy bookshop, dark academia mystery. Tre nomi d'autore diversi.
Conseguenza già dentro il prodotto consegnato: **la pagina "Also by" esce vuota su tutti e
quattro.** Un lettore che finisce un libro e vorrebbe il prossimo non trova niente.

Non è colpa tua: era una decisione che spettava a una persona e nessuno l'ha presa. **Adesso la
prendi tu**, e Max la ratifica o la ribalta.

**Cosa fai:** scegli **UNA nicchia** e **UN nome d'autore** per il catalogo, motivandoli con i
numeri di `kdp nicchie` (non con "mi piace"), e applichi con:
```
python -m engine.kdp nicchia-scegli --keywords "<la nicchia scelta>"
```
Poi decidi cosa fare dei 4 libri già scritti fuori nicchia: restano come sono (sono già scritti,
non si buttano) ma **non contano come catalogo** — e da lunedì tutto quello che esce sta dentro.

**Gate FIX-2**: `kdp nicchia-stato` mostra la nicchia decisa, la motivazione coi numeri è nel
checkpoint, B-018 è chiuso in `BACKLOG.md`.

---

## FIX-3 — 3 pacchetti su 4 escono **exit 1**

**Misurato oggi:**
```
kdp pacchetto the-winter-term            -> exit 0   COMPLETO
kdp pacchetto the-quiet-hours            -> exit 1   [MANCA] prompt copertina
kdp pacchetto the-ninth-winter           -> exit 1   [MANCA] prompt copertina
kdp pacchetto the-second-hand-spellbook  -> exit 1   [MANCA] prompt copertina
```
Non è un difetto di codice — è che quei 3 sono nati **prima** del fix del 25/08 che ha fatto
entrare `COPERTINA-PROMPT.md` nel pacchetto. Ma il risultato pratico è che oggi il tuo gate dice
"non conforme" su tre quarti del catalogo, e un gate che è rosso di default smette di essere
letto.

**Cosa fai:** recuperi il prompt copertina di ognuno (`copertina-prompt.md` c'è già in
`in_lavorazione/the-ninth-winter/` e `the-second-hand-spellbook/`; **the-quiet-hours non ce l'ha
proprio** — va riscritto dalla copertina esistente) e rigeneri i 3 pacchetti finché
`kdp pacchetto` non esce **0** su tutti e quattro.

**Gate FIX-3**: 4 pacchetti su 4 a exit 0. Incolla i 4 output.

---

## FIX-4 — 66 avvisi "trattini", **falsi positivi al 100%**

**Misurato** — ho contato gli avvisi di tutti e 4 i `validazione.json`:

| Libro | avvisi trattino | veri difetti |
|---|---|---|
| The_Quiet_Hours | 29 | **0** |
| The_Ninth_Winter | 14 | **0** |
| The_Second-Hand_Spellbook | 15 | **0** |
| The_Winter_Term | 8 | **0** |

**66 avvisi, 66 falsi positivi.** Su The_Quiet_Hours ho verificato uno per uno: `spiral-bound`,
`chain-link`, `hand-painted`, `night-time`, `straight-backed`, `pay-as-you-go`… sono **parole
composte inglesi corrette**, 29 su 29. Su The_Winter_Term sono 8 occorrenze dello stesso cognome:
`Ashworth-Kane`.

Il controllo serve a bloccare le **lineette lunghe** (`—` `–` `--`) nella narrazione — regola
giusta e non negoziabile. Ma sta segnalando anche il trattino corto **dentro una parola**, che in
inglese è ortografia normale. Il danno è concreto: chi apre `validazione.json` e trova 29 avvisi
tutti sbagliati smette di leggerli, ed è esattamente così che una lineetta vera passa. **Un canale
di avvisi rumoroso al 100% è peggio di nessun avviso.**

**Cosa fai:** in `engine/validators.py`, `valida_lineette` deve continuare a bloccare `—` `–` `--`
e **smettere** di segnalare `-` fra due caratteri alfabetici (`\w-\w`). Aggiungi il test di
regressione: una frase con `spiral-bound` non genera avvisi, una frase con `—` sì. Poi rivalida i
4 libri e mostra che gli avvisi trattino sono scesi a 0 senza aver disattivato il controllo.

**Gate FIX-4**: test nuovo verde, suite ancora tutta verde, 4 libri rivalidati con 0 avvisi
trattino.

---

## FIX-5 — La stima pagine sbaglia sistematicamente, e ha già fatto perdere un giro

**Misurato** — dal tuo stesso commit `741c7b90`: *"La stima a 320 parole/pagina ha sbagliato di
nuovo: 120,9 stimate contro 113 reali alla prima consegna."* Non è la prima volta ("**di
nuovo**"). Il minimo non negoziabile è 115 pagine reali: una stima che sovrastima di ~7 pagine
fa credere di essere a posto quando si è sotto, e il difetto si scopre solo al PDF, cioè dopo
aver scritto tutto.

Con 5-7 libri a settimana, un giro perso per libro è mezza settimana buttata.

**Cosa fai:** ricalcola il rapporto parole/pagina **dai dati veri che ora hai** — 4 libri con
parole esatte e pagine reali contate sul PDF:
```
36.871 -> 119 pagine    37.168 -> 118    38.128 -> 118    39.668 -> 116
```
(nota che non è nemmeno monotòno: il libro con più parole ha meno pagine — quindi il divisore
fisso è la modellazione sbagliata, e va capito perché prima di ritararlo). Correggi la costante o
il modello, e fai in modo che la stima dichiari sempre di essere una stima, con il margine di
errore misurato.

**Gate FIX-5**: la stima sui 4 libri esistenti cade entro ±3 pagine dal reale. Incolla il
confronto stimato/reale per tutti e 4.

---

## FIX-6 — Il magazzino non regge una settimana

**Misurato** (`python -m engine.kdp magazzino`): **3 totali, 1 libero, 2 in uso, 0 fatti.**
Con 1 libro al giorno il magazzino è finito mercoledì. E non esiste oggi nessun processo che lo
riempia prima che si svuoti — ogni volta è ripartito da zero, a mano.

**Cosa fai adesso, subito**: `kdp nicchie` sulla nicchia scelta in FIX-2, e riempi il magazzino
con **almeno 7 argomenti** validati, così il piano editoriale della task successiva ha da cui
pescare. (Il *processo* che lo riempie ogni settimana è KDP-SCOUT, ed è la task dopo. Qui serve
solo lo stock per partire.)

**Gate FIX-6**: `kdp magazzino` mostra ≥7 argomenti liberi, tutti con `dati_amazon` reali.

---

## Definition of Done — TASK-KDP-FIX-W2

- [ ] FIX-1: 4 ASIN registrati (o blocco esterno dichiarato per iscritto), `libri_pubblicati/` non vuoto
- [ ] FIX-2: 1 nicchia + 1 autore decisi e applicati, B-018 chiuso
- [ ] FIX-3: 4 pacchetti su 4 a exit 0
- [ ] FIX-4: falsi positivi trattino a 0, lineette lunghe ancora bloccate, test di regressione verde
- [ ] FIX-5: stima pagine entro ±3 dal reale sui 4 libri
- [ ] FIX-6: magazzino ≥7 argomenti liberi con dati reali

**Solo quando queste 6 caselle sono spuntate si passa alla task successiva.**

---

# 🟣 TASK-KDP-PIANO-W2 — Piano editoriale settimanale + team di 3 agenti + comando ufficiale

**Questa è la task centrale della settimana.** Non è "un piano generico". È l'esatto equivalente
per i libri di quello che Max ha già fatto per YouTube, e il modello da copiare esiste già ed è
consultabile.

## Il modello da copiare (guardalo PRIMA di progettare)

`YOUTUBE-AUTOMATION-FACTORY/memory/piano_editoriale_70.json` — 70 video, 30 giorni, 3 strategie.
Struttura: `{generato_il, canale, periodo, totale_video, strategie{}, righe[]}`.

Guarda **una riga vera** (`righe[0]`) e nota il livello di dettaglio: giorno, data, strategia,
**url sorgente REALE** (mai inventato), vph della sorgente, titolo adattato, schemi di titolo
applicati, hook a 3 secondi, caption, hashtag, note di esecuzione, e **il comando CLI già pronto
da incollare**. Chi apre quel file al giorno 14 non deve decidere niente: deve solo eseguire.

**Il tuo piano libri deve avere lo stesso livello.** Se una riga del tuo piano lascia una
decisione aperta a chi la esegue, quella riga non è finita.

## Cosa deve contenere ogni riga del piano (7 righe, una per giorno)

| Campo | Cosa ci va | Da dove viene |
|---|---|---|
| `giorno` | 1-7 | — |
| `data_produzione` | data assoluta | — |
| `nicchia` | la nicchia di quel libro | decisione di catalogo (vedi sotto) |
| `punteggio_nicchia` | numero reale | `kdp nicchie`, **mai a sensazione** |
| `dati_amazon` | recensioni mediane, concorrenti deboli, prezzo medio | `kdp nicchie` |
| `titolo_lavoro` | il titolo del libro | tuo |
| `autore` | il nome d'autore | decisione di catalogo |
| `premessa` | 3-5 righe: chi è il protagonista, cosa gli succede, qual è la posta in gioco | tuo |
| `struttura_prevista` | 24 capitoli, ~1600 parole/cap, target pagine | standard del workflow |
| `angolo_differenziante` | perché questo libro non è uguale ai concorrenti | dai concorrenti letti |
| `comando_cli` | `python -m engine.kdp nuovo "<Titolo>" --nicchia "<nicchia>"` già compilato | — |

**Vincolo duro**: ogni `dati_amazon` deve venire da un run vero di `kdp nicchie`. Un numero
inventato in un piano editoriale è peggio di un piano assente, perché ci si costruisce sopra.
Vale l'Art.2 (zero dati finti): se la rete non risponde, il piano esce con meno righe e lo dici.

## Prerequisito: la decisione di catalogo è già stata presa in FIX-2

Il piano si appoggia alla nicchia e al nome d'autore decisi in **FIX-2**: le 7 righe stanno
tutte dentro quella nicchia, sotto quello stesso nome. Se FIX-2 non è chiuso, questa task non
parte — è il motivo per cui il blocco fix viene prima.

Se pensi che serva più di una nicchia, la risposta è no per questa settimana: 7 libri in 1
nicchia con 1 autore sono un catalogo che si somma e ha "Also by" pieno; 7 libri in 7 nicchie
sono 7 esordi che non si aiutano tra loro. Se hai un motivo forte per dissentire, scrivilo nel
checkpoint e chiedi a Max prima di eseguire — **non decidere in silenzio**.

## Il team: 3 agenti, non 1 e non 8

Max ha chiesto un **piccolo team ufficiale di 3 agenti, perfettamente architettato**. Non
inventare una struttura nuova: **copia lo standard già in uso nell'Impero** — guarda come sono
fatti gli agenti in
`company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/agenti/*.md`
(~125-136 righe l'uno: missione, input, output, regole, gate, connessioni). Stesso formato.

I 3 ruoli, con confini netti — **ogni agente ha un solo mestiere**:

| Agente | Mestiere | Input | Output | Non deve MAI |
|---|---|---|---|---|
| **KDP-SCOUT** (ricerca) | trova e misura nicchie/argomenti candidati | keyword candidate + catalogo attuale | JSON argomenti con `dati_amazon` reali, scartati inclusi con motivo | produrre un numero non misurato; proporre non-storie (diari/planner) |
| **KDP-EDITOR** (piano) | trasforma gli argomenti misurati in 7 righe eseguibili | output di SCOUT + decisione di catalogo | `piano_editoriale_settimana.json` + `.md` leggibile | inventare `dati_amazon`; lasciare una riga senza `comando_cli` |
| **KDP-GATE** (controllo) | verifica il piano PRIMA che qualcuno lo esegua | il piano | verdetto PASS/BLOCK con motivi puntuali | dire PASS con un campo mancante o un dato senza fonte |

**Perché GATE esiste separato**: nel workflow KDP il gate che blocca (`kdp blocco`) ha già
bocciato 2 volte su 7 su "The Winter Term" e **aveva ragione entrambe le volte**. È il pezzo che
funziona meglio di tutto il flusso. Il piano editoriale merita lo stesso trattamento: chi scrive
il piano non è chi lo approva.

I 3 agenti vivono in
`company/Ecosistemi/02-INFO-BUSINESS/Workflow/libri-performanti-multiagente/agenti/` — cioè
**dentro il workflow che già funziona**, non in una cartella nuova scollegata.

## Il comando ufficiale

Ne servono **due**, distinti, e la distinzione è il punto:

**1. `/piano-libri`** — genera il piano della settimana.
Fa girare i 3 agenti in sequenza (SCOUT → EDITOR → GATE) e produce:
```
LIBRI/_piani/piano_<YYYY-MM-DD>.json
LIBRI/_piani/piano_<YYYY-MM-DD>.md
```
Se GATE dice BLOCK, il piano **non** viene scritto e il comando esce diverso da 0 dicendo cosa
manca. Stessa logica di `kdp copy`: valida prima di salvare, e se sbaglia non scrive niente.

**2. `/libro-del-giorno`** — il comando che avvia il flusso di produzione.
Questo è quello che Max ha chiesto esplicitamente: **un solo comando, e parte tutto.**
Sequenza obbligatoria:
```
1. legge LIBRI/_piani/piano_<settimana corrente>.json
2. calcola che giorno è OGGI dentro quella settimana
3. prende la riga di oggi (nicchia + titolo + premessa + angolo: tutto già deciso)
4. controlla che non ci sia un libro incompleto aperto
   -> se c'è, si finisce QUELLO (regola 6 non negoziabile, già nella skill)
5. esegue `kdp nuovo` con i parametri della riga
6. entra nel ciclo di scrittura della skill /libro (blocchi da 8 capitoli + `kdp blocco`)
7. copy -> consegna -> pacchetto
```
Se il piano della settimana non esiste o è scaduto, il comando **si ferma e dice di lanciare
`/piano-libri`** — non improvvisa un libro a caso. Un comando che inventa quando manca l'input è
il modo esatto in cui è nato B-018.

Entrambi i comandi vanno registrati come skill vere in
`.../libri-performanti-multiagente/.claude/skills/`, accanto a `libro/SKILL.md` che esiste già.
E **la procedura si scrive nella skill**, non in un terzo documento: la lezione del 2026-08-23
(tre documenti che si contraddicevano, con il gate più importante assente in due su tre) è già
stata pagata una volta.

## Gate TASK-KDP-PIANO-W2

`/piano-libri` gira e produce un piano da 7 righe con `dati_amazon` reali (incolla il run di
`kdp nicchie` che li ha prodotti). Poi `/libro-del-giorno` gira su quel piano e apre davvero il
libro del giorno giusto senza che tu gli dica nient'altro. Incolla nel checkpoint: i due
comandi, l'output, e il path del piano.

---

# 🟢 TASK-KDP-5LIBRI-W2 — 5 libri completi, in cartella, pronti

Max vuole **5 libri pronti entro la settimana**, in cartella, tutto strutturato. Il piano della
task precedente ne prevede 7 (uno al giorno): **5 è il gate, 7 è il bersaglio.** Meglio 5 finiti
bene che 7 abbozzati — questa regola non cambia.

"Pronto" significa **`kdp pacchetto <slug>` esce 0 E il libro è caricabile su KDP**, cioè:

| Artefatto | Verifica |
|---|---|
| manoscritto `.docx` impaginato | `kdp pacchetto` |
| `.pdf` con **pagine reali contate**, mai stimate | ≥115 pagine, verdetto in `validazione.json` |
| `.epub` | `kdp pacchetto` |
| `COPERTINA-PROMPT.md` | `kdp pacchetto` |
| **immagine di copertina `.png`** | `kdp consegna <slug> --cover <file.png>` |
| `KDP_METADATA.txt` (titolo, sottotitolo, descrizione, 7 keyword) | `kdp copy` valida PRIMA di salvare |
| `validazione.json` con **`bloccanti: []` e `verifiche_non_eseguite: []`** | il verdetto |

**Le copertine le generi tu** (SOP: "Gael genera la copertina e carica su KDP"). Tesseract è
installato dal 2026-08-23 e legge il titolo in copertina: quel controllo ora gira davvero, non
farlo tornare a "VERIFICA A MANO".

**I 4 libri vecchi non contano qui**: sono già stati rimessi a posto in FIX-3 (pacchetto a exit 0)
e caricati in FIX-1. I 5 del gate sono **libri nuovi di questa settimana**, dentro la nicchia
decisa in FIX-2.

**Struttura finale** — non inventarne una nuova, quella giusta esiste già:
```
LIBRI/libri_pronti/<Titolo_Libro>/     <- il pacchetto (5 cartelle nuove)
LIBRI/in_lavorazione/<slug>/           <- il progetto (capitoli, outline, riassunti)
LIBRI/_piani/piano_<data>.json         <- il piano della settimana (nuovo)
```

## Gate TASK-KDP-5LIBRI-W2

5 cartelle in `libri_pronti/` con `kdp pacchetto` a **exit 0** e `validazione.json` con zero
bloccanti e zero verifiche non eseguite. Incolla nel checkpoint i 5 output di `kdp pacchetto`
per intero. **Un pacchetto che esce 1 non conta, anche se il libro è bello.**

## Nota sul ritmo (leggila, ti serve per organizzare i giorni)

"The Winter Term": creato alle 20:06:13, consegnato alle 20:49. **43 minuti** per 24 capitoli e
39.668 parole, con 2 bocciature del gate incluse. Il ritmo di 1 libro/giorno **è dimostrato
possibile** — non è una speranza, è scritto nel tuo `metriche.json`. Il collo di bottiglia non è
la scrittura: è la ricerca nicchia e la decisione, ed è esattamente ciò che il piano editoriale
toglie di mezzo pagandolo una volta sola per tutta la settimana.

---

# 🔴 TASK-LANCI-ECO-W2 — Ecosistema LANCI: **prima il piano, poi (e solo poi) la costruzione**

⚠️ **Questa task ha una regola diversa dalle altre due. Leggila tutta prima di toccare un file.**

Max è stato esplicito: **prima devi consegnare un piano perfetto, estremamente progettato,
chirurgico. Poi si costruisce.** Non aprire cartelle, non scrivere agenti, non creare
l'ecosistema finché il piano non è approvato da Max. Il piano è il deliverable della settimana;
la costruzione è la W3.

**È una task enorme, quindi è spezzata in 6 sotto-task con gate propri (L1→L6).** Si fanno in
quest'ordine: ognuna è l'input della successiva. Chiudi e segna ogni L prima di aprire la
seguente — se la settimana finisce a L4, hai comunque consegnato qualcosa di completo e
riprendibile, non un cantiere aperto.

| # | Sotto-task | Output | Tempo indicativo |
|---|---|---|---|
| **L1** | Ricognizione di cosa esiste davvero | `RICOGNIZIONE-LANCI.md` | mezza giornata |
| **L2** | Estrazione del contenuto dai progetti vecchi | `ASSORBIMENTO-LANCI.md` | mezza giornata |
| **L3** | Architettura: ecosistema + reparti | bozza `26-ECOSISTEMA-LANCI.md` §1-2 | 1 giorno |
| **L4** | Il flusso end-to-end di UN lancio + comando ufficiale | §3 dello stesso doc | mezza giornata |
| **L5** | Agenti e gate per reparto | §4 dello stesso doc | 1 giorno |
| **L6** | ADR proposto + consegna a Max | ADR in `decisions/` | 1 ora |

---

## L1 — RICOGNIZIONE (cosa c'è davvero, misurato)

Max vuole sapere **cosa esiste già** sui lanci prima di decidere. Ti do quello che ho trovato io
in questo audit, così non ricominci da zero — **verificalo e completalo, non fidarti**:

**Esiste ed è vero:**
- `company/Ecosistemi/02-INFO-BUSINESS/Reparti/IB-L2-LANC-Lanci-Campagne/` — **1.805 righe** di
  documentazione: 9 agenti (`IB-COORD-LANCI`, `IB-LANC-PLANNER`, `ASSET`, `COPY-LIAISON`, `DRY`,
  `QA`, `TRACKER`, `WEBINAR`, `DEBRIEF`), `ARCHITETTURA.md`, `KPI.md`, `PRINCIPI.md`,
  `REGOLE.md`, `SKILLS.md`, e 2 workflow (`WF-LANCIO` T-30→T+7, `WF-WEBINAR`).
- Il workflow WF-LANCIO ha input JSON, gate, sequenza. **È scritto bene.**

**È il problema:**
- `scripts/README.md` dice *"Script pianificati (build in V2)"* — `launch_calendar.py`,
  `dry_run_costs.py`, `launch_debrief_diff.py`: **nessuno dei tre esiste.**
- `state/README.md`: schema, nessuno stato.
- `SKILLS.md`: skill *"da forgiare"*, nessuna forgiata.
- **Zero file eseguibili nell'intero reparto.** È un ecosistema di carta: descrive perfettamente
  un lancio che nessun comando sa avviare. È esattamente la differenza fra il reparto Lanci di
  oggi e il workflow KDP di ieri sera.

**Output L1**: `PIANO-MAESTRO/RICOGNIZIONE-LANCI.md` — per ogni pezzo esistente una riga:
cosa fa / **esiste davvero o è carta** / si tiene, si assorbe o si butta / perché. Niente "PASS
finti", vale la regola di sempre.

**Gate L1**: il documento distingue esplicitamente ciò che è eseguibile da ciò che è solo
descritto, con il comando che lo dimostra (`ls`, `python -c "import ..."` — qualcosa che prova
l'esistenza, non la fiducia).

---

## L2 — ASSORBIMENTO: estrarre il contenuto dai progetti vecchi

**Materiale storico da assorbire** (Max li ha indicati — sono progetti vecchi, valgono come
contenuto, **non** come architettura da copiare):
```
Progetti Claude/Info-Business-HQ_Knowledge/          (Priorità 1/2/3)
InfoBusiness/                                        (catalogo prodotti, Funnel Unico Perfetto.pdf, Webinar/)
System OMEGA/.../CONTESTO - SOLO ESEMPI/Product Creation Lab/
System OMEGA/.../CONTESTO - SOLO ESEMPI/Product Pricing Strategist.skill
System OMEGA/.../CONTESTO - SOLO ESEMPI/Project-Marketing University.md
System OMEGA/.../CONTESTO - SOLO ESEMPI/Project-Strategy Command Center/
System OMEGA/.../CONTESTO - SOLO ESEMPI/VSL Script Builder.skill
System OMEGA/.../CONTESTO - SOLO ESEMPI/Webinar Script Master.skill
Lancio corso skill beast/ · Lanco ebook/ · Formazzione/
```
Max lo dice chiaro: *"prima facevamo tutto con dei progetti, i classici progetti. Adesso al posto
dei progetti del cavolo facciamo workflow, reparti, team di agenti, piccoli ecosistemi."*
Quindi: **il contenuto di quei progetti si assorbe, la loro forma si butta.** La pipeline a 3
fasi di Product Creation Lab (Architettura → Produzione → Qualità/Packaging) e la sua catena
FASE 0→3 (Strategy Command Center → Infobusiness HQ → Marketing University → Product Creation
Lab) sono **la sostanza buona**: vanno tradotte in reparti e workflow, non lasciate lì.

**Output L2**: `PIANO-MAESTRO/ASSORBIMENTO-LANCI.md` — per ogni progetto vecchio: quali
framework/checklist/criteri concreti contiene, e in quale reparto del nuovo ecosistema finiscono.
Il livello giusto è quello della pipeline di Product Creation Lab che Max ti ha mandato: gate
espliciti ("score ≥60/100", "beta test obbligatorio ≥€97", "6 red flag assoluti"), non concetti.

**Gate L2**: ogni riga del documento punta a un file sorgente reale e a un reparto di
destinazione. Zero righe "da approfondire".

---

## L3 — ARCHITETTURA: l'ecosistema e i suoi reparti

Un ecosistema nuovo, **`company/Ecosistemi/14-LANCI/`** (14 è il primo numero libero: l'ultimo è
`13-ARENA-APEX`). Deve seguire lo standard di ecosistema già in uso — guarda
`company/Ecosistemi/02-INFO-BUSINESS/ECOSISTEMA.md` e `BACKBONE.md` per la forma esatta
(missione, reparti L2, workflow, collegamento a Backbone/BUS/BRAIN/GOVERNANCE, asset esistenti).

I reparti che Max ha nominato esplicitamente, più quelli che il flusso richiede. **Nel piano
motiva ogni reparto: perché esiste, cosa produce, cosa lo blocca.** Se un reparto non ha un
output verificabile, non è un reparto — è un capitolo.

| Reparto L2 | Di cosa risponde | Materiale storico che assorbe |
|---|---|---|
| **Strategia** | va lanciato o no; filtro anti-ADD; allineamento OKR; go/no-go strategico | Strategy Command Center (FASE 0) |
| **Intelligence & Competitor** | analisi competitor, ricerca target, pain point, obiezioni, TOV | Marketing University / Client Research Engine (FASE 2) |
| **Prodotto** | validazione idea (scoring), architettura, produzione, QC, handoff | Product Creation Lab + Infobusiness HQ (FASI 1 e 3) |
| **Pricing & Offerta** | strategia prezzo, offer stack, bonus, garanzia | Product Pricing Strategist.skill |
| **Copy** | sales page, VSL, webinar, email, ads — tutto il copy del lancio | VSL Script Builder, Webinar Script Master, skill `cro-copy-architect` (già installata) |
| **Siti & Funnel** | **il sotto-ecosistema che Max ha chiesto**: sales page, landing, checkout, thank you, upsell — costruiti e messi online | skill `empire-premium-style` + `site-*` (già installate) |
| **Marketing & Traffico** | ads, organico, partner, affiliati, lista | skill `ads`, `ad-creative`, `launch` (già installate) |
| **Esecuzione Lancio** | calendario T-30→T+7, dry-run, go/no-go, tracking, debrief | **IB-L2-LANC esistente — si SPOSTA qui, non si riscrive** (ADR-003) |

**Sul sotto-ecosistema Siti**, che Max ha chiesto per nome: deve occuparsi di *organizzare e
strutturare perfettamente tutti i siti dove il lancio avviene*. Nel piano specifica quali pagine
servono per un lancio (sales page, landing opt-in, pagina webinar, checkout, thank you,
upsell/downsell), chi le costruisce, con quale skill, e **come si verifica che siano online e
funzionanti** — non "fatte", *online e funzionanti*.

**Gate L3**: §1-2 di `26-ECOSISTEMA-LANCI.md` scritte, con per ogni reparto missione in 1 frase,
cosa produce, cosa lo blocca. Se un reparto non ha un output verificabile, non è un reparto: o lo
motivi o lo togli.

---

## L4 — IL FLUSSO end-to-end di UN lancio + il comando ufficiale

Questo è il cuore, ed è la parte che oggi manca completamente: **dal "abbiamo un'idea" al
"carrello chiuso e debrief scritto"**, in una sequenza sola, con chi fa cosa e quale gate ferma
cosa.

Deve avere lo stesso taglio del flusso KDP che hai già costruito e che funziona: un comando
ufficiale che parte, legge lo stato, sa a che punto è, e non improvvisa quando manca un input.
Stessa filosofia di `/libro-del-giorno`: **un comando, e parte.**

Nel piano scrivi: nome del comando, cosa legge, cosa produce, dove si ferma e perché, e quali
passaggi restano necessariamente umani (l'incasso, la pubblicazione, l'invio alla lista: azioni
irreversibili verso l'esterno — quelle le fa una persona, sempre).

**Gate L4**: §3 scritta — la sequenza completa con i gate bloccanti, il comando ufficiale
definito, e i punti di intervento umano dichiarati esplicitamente.

---

## L5 — AGENTI E GATE per ogni reparto

**Per ogni reparto il piano deve dire, obbligatoriamente:**
1. missione in 1 frase
2. gli agenti (nome, mestiere in 1 riga, input, output) — **stesso formato dei 9 agenti di
   IB-L2-LANC**, che è già lo standard giusto
3. il/i workflow con i gate BLOCCANTI (chi ferma cosa, e con quale criterio misurabile)
4. **cosa è eseguibile** — quali script/comandi, con nome e firma. Questo è il campo che nel
   reparto attuale è vuoto ed è il motivo per cui non serve a niente.
5. le connessioni: cosa riceve da chi, cosa passa a chi

Regola che vale per tutti: **chi produce non approva.** È la lezione di `kdp blocco`, che ha
bocciato 2 volte su 7 e aveva ragione entrambe. Un reparto che si autocertifica non è un gate.

**Gate L5**: §4 scritta — ogni reparto ha i suoi agenti nel formato standard e almeno un gate
bloccante con criterio misurabile (non "qualità alta": un numero, o una condizione verificabile).

---

## L6 — ADR proposto e consegna

Un ADR **proposto, non applicato**, in `company/Memory/decisions/`: creazione di `14-LANCI`,
spostamento di IB-L2-LANC dentro (ADR-003: si sposta, non si riscrive), cosa si assorbe dai
progetti vecchi e cosa si archivia. Con le alternative scartate e il perché — un ADR senza
alternative scartate è un annuncio, non una decisione.

**Gate L6**: `26-ECOSISTEMA-LANCI.md` completo + ADR proposto. **Nessuna cartella `14-LANCI/`
creata prima dell'ok di Max.**

---

## Costruzione: **NON questa settimana**

Il piano lo approva Max. Poi si costruisce (W3). Se avanza tempo dopo aver chiuso le prime task,
puoi costruire **un solo pezzo pilota** — il più piccolo che dimostra che il piano regge (es.
`launch_calendar.py`, già specificato riga per riga in `scripts/README.md`, che produce un
calendario deterministico senza chiamare niente). Nient'altro.

## Gate TASK-LANCI-ECO-W2

L1→L6 chiuse, ognuna col suo output. Se la settimana finisce prima, dichiara nel checkpoint
l'ultima L chiusa: sono pensate per essere consegnabili una per una.

---

## Regole valide per tutte e 3

1. **Prova, non dichiarazione** — comando + output reale incollato nel checkpoint. La W1 è stata
   riverificata rieseguendo il codice: continua a scrivere checkpoint che reggono a quel
   trattamento, perché quel trattamento continuerà.
2. **Task chiusa → checkpoint** in `company/Memory/checkpoints/` **scritto con
   `python -m empire mem write --kind checkpoint --view`** (non a mano: è il bug che B-009 ha
   fatto 5 volte) + `stato` aggiornato in `EmpireDesk/state/taskboard.json`.
3. **ADR-003 vale ovunque**: il workflow KDP funziona — si estende, non si riscrive. IB-L2-LANC è
   scritto bene — si sposta, non si rifà.
4. **Ordine di priorità, non negoziabile**: **FIX → PIANO → 5 LIBRI → LANCI**. Il blocco fix
   viene prima di tutto per ordine esplicito di Max: si ripara la fabbrica, poi si aumenta il
   ritmo. Le prime tre producono libri e pubblicazioni (revenue); la quarta produce un piano
   (impianto). Se la settimana si stringe, si stringe sull'ultima — che è spezzata in L1→L6
   apposta per potersi fermare a metà senza lasciare un cantiere aperto.
5. Item minori → `company/Memory/BACKLOG.md`. Non fermano la settimana.
6. Se ti blocchi più di una sessione sullo stesso punto → blocco ⚠️ COORDINAMENTO in
   `STATO-EMPIRE.md`, e Claude interviene. Non perdere giorni da solo.

---

## Definition of Done — Settimana 2

**⚫ TASK-KDP-FIX-W2 — prima di tutto**
- [ ] FIX-1: 4 ASIN registrati (o blocco esterno dichiarato), `libri_pubblicati/` non vuoto
- [ ] FIX-2: 1 nicchia + 1 autore decisi e applicati, B-018 chiuso
- [ ] FIX-3: 4 pacchetti su 4 a exit 0
- [ ] FIX-4: falsi positivi trattino a 0, lineette lunghe ancora bloccate, test di regressione
- [ ] FIX-5: stima pagine entro ±3 dal reale sui 4 libri
- [ ] FIX-6: magazzino ≥7 argomenti liberi con dati reali

**🟣 TASK-KDP-PIANO-W2**
- [ ] 3 agenti (SCOUT/EDITOR/GATE) scritti nello standard del reparto
- [ ] `/piano-libri` produce 7 righe con `dati_amazon` reali
- [ ] `/libro-del-giorno` legge il piano e apre il libro del giorno giusto da solo

**🟢 TASK-KDP-5LIBRI-W2**
- [ ] 5 pacchetti nuovi a exit 0, zero bloccanti, zero verifiche non eseguite

**🔴 TASK-LANCI-ECO-W2** (fermarsi a metà è previsto: dichiara l'ultima L chiusa)
- [ ] L1 ricognizione · [ ] L2 assorbimento · [ ] L3 architettura
- [ ] L4 flusso + comando · [ ] L5 agenti e gate · [ ] L6 ADR proposto
- [ ] **Zero cartelle `14-LANCI/` create prima dell'ok di Max**

**Fine settimana**
- [ ] Checkpoint con lo stato reale di tutte e 4 (fatto / parziale + dove sei / bloccato + perché)
