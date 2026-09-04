# Coverage — max18-doc-justin-sung

## ⚠️ DICHIARAZIONE NO-FINTO (leggere per prima)

**Questa non e' una fonte video. E' un documento di testo.**

- **Non ho guardato nessun video.** Il video "Justin Sung 4h55" **non e' disponibile**: il
  checkpoint `EMP-QQ2R` lo dichiarava introvabile perche' nel repo non esiste il link, e il link
  continua a non esistere. Max ha consegnato **il testo**, non il video.
- **Frame estratti: 0. Frame guardati: 0.** Non e' stato scaricato nessun video, non e' stato
  eseguito `frame_extractor.py`, non esiste `frames/` in questo run, non esiste `scenes.json`.
- Di conseguenza **non esiste in questo run alcuna affermazione su cosa si veda a schermo.**
  Dove il testo rimanda a un contenuto visivo ("have a look at this mind map", "here's an example
  of a level three mind map", il grafico dello sforzo/ritardo, i grafici della forgetting curve e
  del carico cognitivo), quel contenuto **non e' stato osservato** e non e' ricostruibile.
- I due diagrammi ASCII presenti in `analisi.md` (curva a U del carico cognitivo, curva
  sforzo/memoria del delayed note-taking) sono **ricostruzioni testuali** fatte da me a partire da
  come l'autore li descrive **a parole**, ed e' scritto anche li'. **Non sono trascrizioni di
  immagini viste.**
- Nessun atomo in `atoms.json` ha un campo `frame` valorizzato: sono **tutti `null`**, per
  costruzione. Lo schema resta quello di `max17-v01-artem` per compatibilita', ma il campo non e'
  applicabile a una fonte testuale.

**Nessuna parte di questo run implica, suggerisce o lascia intendere che il video sia stato visto.**

---

## Numeri della copertura reale

| Grandezza | Valore |
|---|---|
| File sorgente | `C:\Users\Utente\Pictures\materiale\Agency 2026 (1).md` |
| Dimensione del file | 509.995 byte · 366 righe |
| **Blocco Justin Sung** | **riga 366** — 285.119 caratteri · 52.582 parole |
| **Letto davvero** | **285.119 / 285.119 caratteri = 100%** |
| Modalita' di lettura | 12 blocchi da ~24.000 caratteri, tagliati su confine di parola |
| Blocchi letti | **12 / 12** (`js_01.txt` → `js_12.txt`) |
| Atomi estratti | **88** (`atoms.json`) |
| Frame estratti / guardati | **0 / 0** — nessun video |

### Come ho contato

Il file ha **righe lunghissime** (riga 1 = 194.824 caratteri, riga 366 = 285.119). Non e'
leggibile con `Read` a offset/limit di riga, perche' una riga sola sfonda qualsiasi finestra.

Procedura effettiva:

1. Mappata la struttura del file con `Grep` sulle intestazioni e con uno script che stampa la
   **lunghezza di ogni riga** — cosi' ho individuato i due blocchi giganti senza leggerli.
2. Ispezionati i primi 1.500-2.500 caratteri della riga 1 e della riga 366 per capire **cosa
   contiene ciascuna** (riga 1 = Beggiato in italiano; riga 366 = Justin Sung in inglese).
3. Split della sola riga 366 in **12 file da ~24.000 caratteri** su confine di parola
   (`split_doc.py` nello scratchpad di sessione, non nel repo).
4. Letti **tutti e 12** i file, in ordine, nessuno saltato.
5. Verifica di completezza: la somma dei 12 blocchi e' **285.119 caratteri**, esattamente la
   lunghezza della riga 366 (nessun carattere perso nello split, nessuna sovrapposizione).

### Verifica di integrita' della copia

`contenuto-fonte.md` contiene il blocco **byte per byte identico** alla fonte. Verificato con
round-trip SHA-256: il testo riletto dal file scritto ha lo stesso hash del blocco originale.

- **SHA-256 del blocco Justin Sung:** `fe62b46c2ee611fd6a615593b03b5549ead5012d49e3e9bd7f19ee58ff5fbd19`
- **Round-trip identico:** ✅ `True`

Nessun refuso della trascrizione automatica e' stato corretto (restano "note takingaking",
"wrote learning" per *rote*, "space repetition" per *spaced*, "Kim Peak"/"Compique" per *Kim Peek*,
"Dunning Krueger", "icenstudy"/"iconstudy", "105 minuti" dove il senso e' 10-15).

---

## Tracciabilita' degli atomi (P12) — e come mi sono impedito di inventare citazioni

Su una fonte video la traccia e' `video-id#ts + frame-NNN.png`. Qui non esiste ne' l'uno ne'
l'altro. Traccia adottata:

```
Agency 2026 (1).md :: riga 366 :: char <offset> :: <capitolo>
```

**L'offset non e' stimato: e' calcolato.** Ogni atomo porta un campo `ancora` con una frase
letterale del testo; lo script di build (`build_atoms.py`) **cerca quella frase nel testo reale** e
scrive l'offset che trova. Se l'ancora non esiste, **l'atomo viene scartato e segnalato**.

Questo controllo **ha funzionato davvero, e mi ha preso in fallo due volte**: alla prima esecuzione
2 atomi su 88 sono stati scartati perche' le mie ancore erano parafrasi imprecise, non citazioni:

| Atomo | Ancora che avevo scritto | Testo reale |
|---|---|---|
| JS-025 | "your brain will automatically fill in the lower order levels of thinking" | "your brain will automatically **will automatically** fill in the lower order levels of thinking" (ripetizione della trascrizione automatica) |
| JS-055 | "**this** cognitive switch from juggle mode into organizing mode" | "**that** cognitive switch from juggle mode into organizing mode" |

Entrambe corrette sulla base del testo, non del ricordo, e reinserite. Sono errori miei,
intercettati dal meccanismo prima di finire su disco — li scrivo qui perche' e' esattamente il tipo
di scivolamento (citare a memoria invece che dal testo) che il checkpoint `EMP-QQ2R` §3 segnala
come pattern sistemico da controllare.

**Esito finale: 88/88 atomi con offset verificato nel testo. Zero citazioni non verificate.**

### Distribuzione degli atomi

| Capitolo | Atomi |
|---|---|
| cap. 1 — retrieval | 23 |
| cap. 2 — encoding | 21 |
| cap. 3 — mind mapping | 20 |
| cap. 4 — skill acquisition | 24 |
| **Totale** | **88** |

| Tipo | Atomi |
|---|---|
| regola | 37 |
| concetto | 22 |
| framework | 17 |
| numero | 10 |
| cautela | 2 |

Confidenza: **88 `osservato`, 0 `inferito`** — "osservato" qui significa *letto nel testo*, non
*visto a schermo*. Nessun atomo e' un'inferenza mia: dove ho tratto conclusioni di sintesi
(§6 e §7 di `analisi.md`) l'ho fatto **nell'analisi, non negli atomi**, e l'ho dichiarato.

---

## Controllo sulla prima parte del documento (Beggiato) — cosa ho fatto e cosa NON ho fatto

**NON ho ri-studiato Beggiato.** Quel materiale e' gia' chiuso (run `max17-v17-beggiato-agenzia`,
CP-20260904-003, pagina wiki `Source_Giovanni_Beggiato_Guida_Agenzia_AI.md`). Ho fatto **solo un
controllo differenziale** per rispondere a una domanda: *il documento contiene qualcosa di nuovo
rispetto alla pagina wiki gia' esistente?*

**Cosa ho letto della parte Beggiato:**
- le **tre rielaborazioni** ("manuali strategici", righe 3-364, 27.854 caratteri): **lette al 100%**;
- la **trascrizione grezza** (riga 1, 194.824 caratteri): **NON letta integralmente**. Ho eseguito
  su di essa **ricerche mirate** (`verify_beggiato.py`, `verify2.py`) su ~60 termini e numeri, con
  stampa del contesto attorno a ogni occorrenza. **Copertura dichiarata della riga 1: parziale,
  mirata alla verifica, non integrale.** Non ne servivano di piu': quella trascrizione e' gia'
  stata letta al 100% dalla sentinella precedente (dichiarato in CP-20260904-003: 5.550 righe
  deduplicate lette in 12 blocchi).

**Perche' la verifica era necessaria.** I tre manuali sono **rielaborazioni AI**, non trascrizioni.
Prendere per buono il loro contenuto e attribuirlo al relatore sarebbe stato un NO-FINTO mascherato:
avrei messo in wiki, come detto da Beggiato, cose che Beggiato non ha mai detto. Ogni elemento
nuovo e' stato quindi cercato **nella trascrizione grezza** prima di essere integrato.

### Esito della verifica — tre categorie

**(A) Nuovo per la wiki e VERIFICATO nella trascrizione** → integrato nella pagina wiki Beggiato:
dati Eurostat (8% / 6,4% / 12,8%) e di mercato mondiale (84% mai usato l'AI, 16% free chatbot user,
~0,3% paganti, 0,04% coding scaffold); **released capacity** (500 ore/settimana, €5.000/settimana a
€10/ora, "non cash ma potenzialmente cash"); **soglie esatte del close rate**; **niche hopping** con
il tetto dei ~€3.000/mese; metodo di testing delle nicchie; meccanica esatta dello **speed to lead**;
le **7 fasi** e i **3 pilastri**.

**(B) Nuovo ma NON presente nella trascrizione — aggiunte della rielaborazione.** Segnalate come
tali e **mai attribuite al relatore**:

| Elemento | Occorrenze nella trascrizione grezza |
|---|---|
| **"Ikigai"** come framework di scelta nicchia | **0** — il relatore dice "3 P", l'Ikigai e' un innesto |
| **"Ignorance Tax" / "Experience Capital"** | **0** — formule della rielaborazione |
| Tabella a fasce released capacity (€30/ora → €60.000/mese; €50/ora → €100.000/mese) | esiste **solo** l'esempio a €10/ora — le fasce alte sono estrapolazione |
| "Non assumete finche' non raggiungete i €10.000/mese" come soglia di hiring | €10.000/mese compare, ma in **altri contesti** (fatturato dei clienti, timeline dei "primi successi"), **non** come soglia di assunzione |

**(C) Contraddizione trovata — e correzione applicata alla wiki.**

Il **primo** manuale scrive: *"Se chiudete piu' del **30-40%** delle call, siete troppo economici"*.
Il **secondo** e il **terzo** scrivono **60%**. Sono in disaccordo fra loro.

La trascrizione grezza risolve la questione senza ambiguita' (`@58504`):

> "se il vostro close rate e' piu' alto quindi ipotizziamo che il vostro close rate sia del **60%**
> significa che il vostro prezzo e' troppo basso rispetto all'offerta se invece ipotizziamo questo
> sia del **20%** vuol dire che o siete delle scarpe a vendere o che il prezzo e' troppo alto [...]
> golden rule per service business dovreste essere sul **30%**"

Le soglie vere sono dunque **60% / 30% / 20%**. La pagina wiki, scritta nella sessione precedente,
riportava *"Sopra 30% → prezzo troppo basso; sotto 30% → prezzo troppo alto"* — **impreciso**:
schiacciava tre soglie distinte in una. **Corretto in questa sessione**, con la citazione a
supporto. Il valore aggiunto della rielaborazione, qui, e' stato **negativo**: e' cio' che ha fatto
emergere l'imprecisione, ma solo perche' i tre manuali si contraddicono fra loro.

---

## Limiti dichiarati di questo run

1. **Nessun video visto** — vedi la dichiarazione in cima. E' il limite principale e non e'
   superabile senza il video.
2. **Nessuno studio verificato.** Il documento non cita **un solo** riferimento bibliografico
   (titolo/autore/anno) in 52.582 parole. Tutti i numeri sono dichiarazioni dell'autore o rimandi
   generici a "the research". Elencati in `analisi.md` §9.3 e marcati negli atomi di tipo `numero`.
3. **Fonte anche commerciale.** Richiami ricorrenti a newsletter, quiz diagnostico e programma a
   pagamento (icanstudy.com). Alcune stime sui tempi ("mesi con guida, anni da solo") sono
   strutturalmente favorevoli a chi vende il programma.
4. **Montaggio di piu' video**, non un discorso unico: ci sono ripetizioni volute, rimandi ad
   "altri video" e almeno un fuori-onda ("hey it's future me"). Alcune spiegazioni si accavallano
   fra capitoli.
5. **Nessuna patch applicata** a skill o agenti condivisi. Perimetro `EMP-QQ2R` (Fase 1 = studio) e
   presenza dichiarata di altre sentinelle in lavoro parallelo sullo stesso repo. I consigli sono
   nella pagina wiki, **verificati con `Grep`** prima di essere scritti, e restano proposte.

---

## File prodotti da questo run

| File | Contenuto |
|---|---|
| `contenuto-fonte.md` | copia **integrale byte-identica** della parte Justin Sung + mappa dei capitoli con offset misurati |
| `analisi.md` | analisi in 9 sezioni: 3 fondamenta, 4 capitoli, tutti i framework, mappa delle connessioni, tensioni interne, controllo Beggiato, cautele |
| `atoms.json` | 88 atomi, schema `max17-v01-artem` (`frame` sempre `null`), ognuno con `ancora` verificata nel testo |
| `coverage.md` | questo file |
