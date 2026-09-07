---
Tipo: VERIFICA
Stato: Chiuso
Autore: scagnozzo-verifica-A4
Data: 2026-09-06
---

# VERIFICA GATE A4 — controllo a campione delle 62 regole

Mandato: condizione 6 del gate di categoria A4 (piano di studio §9). Compito: non essere
d'accordo, provare a smontare. Ho eseguito `registro.py`, `registro.py --verifica`,
`registro.py --da-applicare` (esito dichiarato: 62/62 regole, tutte a norma, tutte applicate,
zero da applicare), poi ho scelto 5 regole a campione e per ognuna ho controllato tre cose
separate leggendo io stesso il `parlato.txt` della lezione e il file toccato nella fabbrica —
**non mi sono fidato del conteggio automatico**, ed è stata la scelta giusta: il conteggio
automatico dice "tutto applicato" anche dove non lo è (vedi §7).

---

## 1. Le 5 regole scelte, e perché

| # | ID | Tipo | Rischio | Perché l'ho scelta |
|---|---|---|---|---|
| 1 | **A4-L04-04** | vincolo | **ALTO** | Tocca un gate bloccante in produzione (qa-audio-video). Se la prova o la misura fossero false, la fabbrica boccerebbe video buoni o farebbe passare video rotti. |
| 2 | **A4-L14-03** | vincolo | **ALTO** | Dichiara una contraddizione interna al corso sorgente (5 secondi in L10, 4 secondi in L14) e cita se stessa come prova che "nessuno l'ha letta". Rischio: che la nostra scheda abbia semplicemente copiato la stessa contraddizione senza risolverla. |
| 3 | **A4-L01-03** | vincolo | **medio** | Tocca `02-AUTOMAZIONI-E-SCRIPTS/assemble_piano_editoriale.py`, cioè il motore di produzione vero — binario B, quindi il caso in cui una regola sbagliata farebbe più danno, e quello per cui il gate di categoria esiste. |
| 4 | **A4-L19-03** | **parametro** | basso | Porta un numero secco (10%) verificabile a schermo, ed è il tipo di regola più facile da falsificare: basta guardare se il numero c'è davvero e se non è già stato smentito da una lezione successiva (lo è: A4-L20-02). |
| 5 | **A4-L00-01** | vincolo | basso | Scelta a caso fra le regole a basso rischio: è la prima regola di tutto lo studio (A4-L00-01) e viene citata da altre cinque regole successive come fondamento — se questa fosse vuota, lo sarebbe anche tutto ciò che ci si appoggia. |

---

## 2. Verifica per regola

### 2.1 — A4-L04-04 (vincolo, ALTO)

> *"Un gate BLOCCANTE controlla solo cio' che esiste. Il criterio sul volume della musica resta
> sospeso [...] finche' non e' accertato [...] se i nostri video contengono musica."*

**a) LA PROVA ESISTE?** SÌ.
File: `SKILL & Agenti/Empire Studio Suite/empire-studio/runs/corso-aitubepro/47e15a85-5075-4f4e-8cba-dcc07a86b835/parlato.txt`, righe 201-206 (22:20-23:04):
> *"[22:20] la musica, scoltate la musica di sotto [...] [22:34] [...] background music, la bassiamo, e in automatico si [22:41] abbassera anche il volume [...] [23:04] [...] se noi volessimo aggiungere la nostra musica o la vogliamo rimuovere ci basterà cliccare su mor[e]"*
Il contenuto citato dalla regola (pannello musica, abbassamento automatico) è davvero lì, al minuto dichiarato (@ 22:41). Citazione approssimativa per via della trascrizione automatica ("bassiamo" = "abbassiamo"), ma il contenuto c'è.

**b) È APPLICATA DAVVERO?** SÌ, e più di quanto la misura chiedesse.
File: `03-AGENTI-E-RUOLI/controllo/qa-audio-video.md`. Il criterio "Bilanciamento Volumi" alla riga 25 è marcato **"❌ CRITERIO INAPPLICABILE — NON SPUNTARLO, NON BOCCIARE"**, con motivazione al §9 (righe 75-113) e chiusura formale al §10 (righe 116-144, regola A4-L20-01, datata 2026-09-06) che spiega perché la domanda aperta da questa regola è stata risolta con due fatti verificati nel codice (`fliki_client.py:252` non ha campi musica). La misura chiedeva solo "segnalato come DA ACCERTARE"; la fabbrica è andata oltre e ha chiuso la verifica.

**c) DICE QUALCOSA DI UTILE?** SÌ. Non è banale: prima di questa regola il gate bocciava (o rischiava di bocciare) video per un criterio riferito a una cosa che non esiste nel payload. È un cambiamento di comportamento reale, non un'annotazione decorativa.

**Verdetto sulla regola: solida.**

---

### 2.2 — A4-L14-03 (vincolo, ALTO)

> *"NESSUNA soglia di durata rende lecito l'uso di una clip protetta [...] Terzo dei quattro miti
> del camuffamento"* [nota: il testo della regola dice "terzo", il file aggiornato la elenca come
> mito **#5**, vedi punto (b)]

**a) LA PROVA ESISTE?** SÌ.
File: `.../runs/corso-aitubepro/0ff3fc46-a1ac-43a7-97df-3e8a34b43a57/parlato.txt`, righe 233-236:
> *"[20:44] [...] [20:51] io dovrei toglierlo per me non vale la pena [...] [20:56] [...] sono 4 secondi di video che [21:03] non possono dire nulla perché siamo dentro il ferius, ok, quindi comunque andate super tranquilli"*
"Ferius" è la trascrizione automatica storpiata di "fair use". Il minuto dichiarato dalla regola (@ 20:51) è l'inizio del blocco di parlato che contiene la frase citata (che si completa a 20:56-21:03): la prova esiste, con un'approssimazione di 5-12 secondi sul timestamp esatto della frase-chiave, fisiologica vista la registrazione a blocchi.

**b) È APPLICATA DAVVERO?** SÌ, e la scheda fa più di quanto la singola regola dichiari.
File: `04-SKILLS-E-REFERENCE/references/monetizzazione-compliance.md`, §5 "I sette miti del camuffamento" (riga 86). Il mito è alla riga 106, elencato come **mito #5** (non #3 come diceva il testo della regola A4-L14-03 — la numerazione è cambiata perché lo stesso file elenca **7** miti, non 4): *"Sono 4 secondi di video [...] | L14 · 20:51 | La stessa soglia inesistente del mito 3, con un numero diverso. L10 diceva 5 secondi, L14 dice 4 [...]"*. La scheda mette esplicitamente le due cifre (5" di L10 alla riga 104, 4" di L14 alla riga 106) una accanto all'altra e usa la contraddizione stessa come prova che nessuno dei due l'ha verificata. Applicazione confermata, e più accurata del previsto.

**c) DICE QUALCOSA DI UTILE?** SÌ, è la regola più tagliente delle 5: non solo respinge il mito, ma trasforma l'incoerenza del corso sorgente in una prova a favore della propria tesi.

**Verdetto sulla regola: solida**, con una imprecisione minore non pericolosa: il testo della regola in `L14_final_cut_avanzato.py` dice ancora "Quinto dei sei miti" mentre il file applicato oggi ne ha sette (vedi §3 sotto — imprecisione di conteggio nella documentazione, non nel contenuto).

---

### 2.3 — A4-L01-03 (vincolo, medio, binario B)

> *"Il piano editoriale deve avere una colonna 'fonti_extra' dove atterrano i link del materiale
> di supporto: una fonte senza un posto dove stare non viene mai riusata."*

**a) LA PROVA ESISTE?** SÌ (fonte: schermo, non verificabile da parlato — controllato comunque il contesto).
File: `.../runs/corso-aitubepro/a256cb78-f4a2-43e6-bc73-d296e75ed2bc/parlato.txt`, righe 36-39 (05:27-05:50):
> *"[05:27] Guardate qui io, vedete che c'è tutta la storia [...] [05:35] Vado a reperire quante più informazioni possibili sull'argomento, quindi mi salvo il link [...] [05:43] E me lo metto magari nelle note, ok, ecco lo qui che ciò il testo."*
Il minuto dichiarato (@ 05:44) e il contenuto (link messo "nelle note") corrispondono. La regola cita anche un frame (`frame-087.png`) che non ho potuto ispezionare visivamente da questo ruolo, ma il contenuto verbale conferma la sostanza.

**b) È APPLICATA DAVVERO? NO — QUI IL CONTROLLO AUTOMATICO SBAGLIA.**
File: `02-AUTOMAZIONI-E-SCRIPTS/assemble_piano_editoriale.py`.
La colonna `fonti_extra` **esiste** in `campi_csv` (riga 661) e viene scritta nel CSV (righe 668-671, con commento che cita esplicitamente A4-L01-03). Fin qui la misura sembra rispettata.
Ma la riga (`riga = {...}`) costruita alle righe 613-634 — cioè il dizionario che alimenta ogni singola voce del piano — **non contiene mai la chiave `"fonti_extra"`**. L'ho verificato con un grep mirato: l'unica volta che quella stringa compare nella costruzione dei dati è nel commento. Il codice che scrive il CSV fa `r.get("fonti_extra") or []` (riga 670): siccome nessuno l'ha mai messa nel dizionario, quel `.get()` restituirà **sempre lista vuota**, per ogni riga, per sempre — finché qualcosa a monte non viene modificato per popolarla davvero.
**La colonna esiste, ma è strutturalmente morta: non ha alcuna sorgente di dati.** La promessa della regola ("una fonte trovata non viene più persa") non è mantenuta: oggi non viene persa una fonte che comunque non atterra mai in quella colonna, perché nessun codice gliela passa.
Ho anche controllato **perché** `--da-applicare` non se ne accorge: la funzione `verifica()` in `L01_scaricare_testi.py` (righe 106-107) fa `contiene(..., ["fonti_extra"])`, cioè **cerca solo se la parola compare nel file** — e compare, nel commento e nell'intestazione colonna. Non controlla se la colonna riceve mai un valore. Questo è esattamente il tipo di errore che il mandato mi ha chiesto di cercare: "--da-applicare cerca parole chiave, tu leggi il senso".

**c) DICE QUALCOSA DI UTILE?** L'intento sì (è collegata al problema serio delle regole A4-L01-01/A4-L05-02 sul rischio di invenzione quando il materiale è insufficiente); l'esecuzione oggi no — è un guscio vuoto.

**Verdetto sulla regola: FALLIMENTO nel punto (b).** Applicata solo a parole.

---

### 2.4 — A4-L19-03 (parametro, basso)

> *"Il volume della musica in Fliki e' una PERCENTUALE, e il riferimento visto a schermo e' 10%.
> Conferma su prova la prescrizione che avevamo gia' in casa ('musica al 10-15%')."*

**a) LA PROVA ESISTE?** SÌ.
File: `.../runs/corso-aitubepro/08d6a09e-b4a8-4322-a654-1bfed76b7207/parlato.txt`, riga 46:
> *"[06:03] Metto volume, 10% ad esempio."*
Il numero (10%) e il contesto (slider del volume musica) corrispondono. Scarto fra il minuto della prova (frame @ 05:52) e la riga di parlato più vicina (06:03): 11 secondi, plausibile perché frame e trascrizione parlato di questo corpus derivano da estrazioni asincrone.

**b) È APPLICATA DAVVERO? PARZIALMENTE — TROVATA UN'INCOERENZA REALE NELLO STESSO FILE.**
File: `04-SKILLS-E-REFERENCE/references/fliki-avanzato.md`. La nota che spiega da dove viene il 10% c'è, righe 58-63, come richiesto dalla misura. Fin qui applicata.
Ma la regola successiva **A4-L20-02** (stessa lezione L20, misura: *"fliki-avanzato §4 riconcilia le tre cifre [...] oggi la scheda prescriveva 10-15% con il pavimento troppo alto"*) dichiara esplicitamente, alla riga 79 dello stesso file:
> *"Quindi la banda è 5-15%, con il tipico in basso, e la nostra vecchia prescrizione «10-15%» aveva il pavimento troppo alto."*
Eppure la **checklist operativa** dello stesso documento, alla **riga 56**, non è mai stata corretta:
> *"- [ ] Il volume della traccia musicale è impostato al **10% - 15%** rispetto alla voce (100%) [...]"*
**Il file dichiara da solo, ventitré righe più sotto, che quella voce di checklist è sbagliata — e non la corregge.** Chi eseguisse oggi quella checklist alla lettera userebbe ancora il pavimento vecchio, quello che il documento stesso chiama troppo alto.
Ho controllato anche qui la funzione `verifica()` (in `L20_aggiornamento_fliki.py`, riga 165): `contiene(FA, ["5-15%", "gradevole"])`. Restituisce Vero perché quelle due stringhe compaiono altrove nel file (§4) — non controlla se la vecchia voce in checklist (§3, riga 56) sia stata tolta. Stesso identico difetto del punto 2.3: keyword-match che non legge il senso.
Nota per completezza: oggi questo criterio non ha impatto pratico, perché §10 di `qa-audio-video.md` dichiara che i nostri video non hanno musica — ma il giorno in cui ne avranno una, chi seguirà la checklist alla riga 56 userà il numero che il documento stesso ha già smentito.

**c) DICE QUALCOSA DI UTILE?** La regola A4-L19-03 in sé è "vera ma (per ora) vuota": conferma un numero che oggi non governa nulla in produzione, perché lo strumento a cui si riferisce (musica) non è mai usato dalla fabbrica. Diventa utile solo se un giorno la musica entrerà nel payload — e in quel giorno la checklist andrebbe comunque corretta prima, altrimenti la regola avrà lavorato per niente.

**Verdetto sulla regola: vera ma vuota, e ha esposto un secondo caso reale di "applicata a parole, non nei fatti".**

---

### 2.5 — A4-L00-01 (vincolo, basso, scelta casuale)

> *"Uno strumento entra in produzione solo se ha uno storico dimostrabile [...]: si scelgono i
> 'verificati' e i 'popolari', mai il piu' nuovo."*

**a) LA PROVA ESISTE?** SÌ.
File: `.../runs/corso-aitubepro/bf8e9863-6a84-45ff-aa36-fd28d09d1707/parlato.txt`, righe 43-46:
> *"[04:42] [...] voglio far semplicemente vedere come funziona, vedere quanti ce ne [04:48] sono, il consiglio che bidò ovviamente è quello di vedere le velocemente, di cercare [04:54] principalmente questi o verificati o popolari semplicemente perché sono quelli che [04:59] vuol dire che stanno funzionando, soprattutto quelli verificati [...]"*
Corrispondenza esatta con il minuto dichiarato (@ 04:48) e con la frase citata dalla regola.

**b) È APPLICATA DAVVERO?** SÌ.
File: `04-SKILLS-E-REFERENCE/references/scelta-strumenti.md`. Esiste per intero, spiega perché si usano Fliki e Arena (righe 30-39), enuncia il criterio "verificati/popolari" (righe 10-15) e lo applica concretamente a un caso vero, i sintetizzatori vocali (§ "Il criterio messo alla prova", righe 65-90, che cita esplicitamente A4-L00-01 alla riga 81). Prima di questa scheda — dice il file stesso alla riga 5-6 — "la fabbrica non aveva nessun criterio scritto".

**c) DICE QUALCOSA DI UTILE?** SÌ, è tutt'altro che banale: è la regola-fondamento su cui si appoggiano esplicitamente almeno altre 4 regole dello studio (A4-L03-04, A4-L13-01, A4-L15-03, A4-L17-03, e implicitamente A4-L16-02). Se fosse vuota, lo sarebbe una parte consistente dell'impalcatura.

**Verdetto sulla regola: solida, e infrastrutturale.**

---

## 3. Il difetto peggiore che ho trovato

Non è una singola frase sbagliata: è un **pattern che si ripete identico due volte** fra le 5 regole
controllate, e che il controllo automatico del registro non può vedere per costruzione.

**Il registro dichiara "applicata" una regola quando la sua funzione `verifica()` trova certe
parole chiave nel file di destinazione — non quando controlla che quelle parole producano
davvero l'effetto promesso.** Ho trovato due istanze concrete:

1. **A4-L01-03** (§2.3): la colonna `fonti_extra` esiste nell'intestazione del CSV di
   `assemble_piano_editoriale.py` (riga 661) ma **nessuna riga del piano la popola mai** — il
   dizionario costruito alle righe 613-634 non contiene quella chiave, quindi il valore scritto
   sarà sempre una lista vuota. `verifica()` (riga 107 di `L01_scaricare_testi.py`) cerca solo
   `"fonti_extra" in testo` e la trova — nel commento, non nel dato. **Marcata FATTA, di fatto morta.**

2. **A4-L19-03 / A4-L20-02** (§2.4): `fliki-avanzato.md` dichiara da sé, alla riga 79, che la
   propria checklist (riga 56: "10% - 15%") ha "il pavimento troppo alto" e che il valore corretto
   è 5-15% — ma **non corregge la riga 56**. `verifica()` (riga 165 di `L20_aggiornamento_fliki.py`)
   cerca `"5-15%"` e `"gradevole"`, li trova nel paragrafo di spiegazione (§4), e dichiara la
   regola applicata senza accorgersi che la checklist operativa (§3) contraddice ancora se stessa
   nello stesso documento.

Il fatto che entrambi i casi passino `registro.py --da-applicare` con l'etichetta "0 da
applicare" (di fatto: 62/62 marcate FATTA) è precisamente il motivo per cui il piano prevede
questo controllo a campione manuale come condizione 6 del gate: uno strumento che certifica sé
stesso con grep sulle proprie parole chiave non può scoprire questi due casi. Nessuno dei due è
tracciato in `CONFLITTI.md` o in `BACKLOG.md` — sono scoperte nuove di questa verifica.

Non ho trovato due regole che si contraddicono nel merito (la coppia più vicina, A4-L10-02 vs
A4-L14-03 sui "5 secondi"/"4 secondi", è in realtà una contraddizione **del corso sorgente**
correttamente registrata e riconciliata dalla nostra scheda, non un errore nostro — vedi §2.2).
Non ho trovato prove senza un minuto (lo schema lo impedisce strutturalmente e l'ho verificato
a campione). Ho invece trovato, cercandolo esplicitamente, un'imprecisione minore di
documentazione: `monetizzazione-compliance.md` riga 92 dice "i miti erano quattro, sono
diventati sei" ma il file oggi (dopo l'aggiunta del mito #7 da A4-L12-01) ne elenca **sette** nel
titolo e nella tabella — la nota di changelog non è stata aggiornata all'ultimo passaggio. Difetto
reale ma cosmetico, minore rispetto ai due sopra.

---

## 4. Verdetto finale

**NON PASSA senza correzione, ma per un motivo circoscritto e riparabile in due modifiche puntuali.**
Su 5 regole controllate, 3 sono solide (A4-L04-04, A4-L14-03, A4-L00-01) e 2 rivelano un
"applicata FATTA" che nei fatti è vuoto o autocontraddittorio (A4-L01-03: colonna morta;
A4-L19-03/L20-02: checklist non corretta). Il gate non dovrebbe chiudersi con lo stato "62/62
applicate" finché queste due righe di codice/documento non vengono davvero allineate a quello che
il registro dichiara già fatto — altrimenti la condizione 6 del gate (questo stesso controllo)
avrebbe verificato a vuoto.
