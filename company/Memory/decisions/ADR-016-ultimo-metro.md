# ADR-016 — L'ULTIMO METRO: il lavoro finito ha un organo che lo guarda

- **Stato:** ATTIVO
- **Data:** 2026-09-03
- **Deciso da:** Max (delega piena a Emperator: *"prendi il controllo, fai tutto"*)
- **Sostituisce:** niente
- **Tocca:** 02-INFO-BUSINESS, 03-CONTENT-FACTORY, YOUTUBE-AUTOMATION-FACTORY, Board C-Suite

---

## Il fatto che ha causato questa decisione

Due indagini indipendenti, partite da domande diverse, sono arrivate alla stessa conclusione:
**Digital Empire produce e non pubblica.**

Misurato il 2026-09-03 con `scripts/ultimo_metro.py`, contando i file sul disco:

| | |
|---|---|
| Pezzi finiti e mai usciti | **25** |
| Lavoro fermo | **2.137 MB** |
| Caricabili subito, senza toccare niente | **23** |
| Il piu' vecchio e' fermo da | **135 giorni** |

I dettagli che rendono il fatto incontestabile:

- **5 libri** in `libri_pronti/`. Tre di essi hanno manoscritto in pdf ed epub, copertina
  finita, dati per Amazon compilati, report e validazione. **Non manca niente.** La cartella
  `libri_pubblicati/` accanto contiene **solo un file segnaposto**: e' vuota da sempre.
- **16 video**, 1,4 GB, in una cartella che si chiama testualmente **`da pubblicare`**.
  Tre di essi hanno per nome *"Il nuovissimo pronto per la pubblicazione"*. Datati
  20-25 aprile 2026.
- **4 video** dalla fabbrica YouTube, di fine agosto, in `VIDEO-PRONTI`.
- **Zero vendite documentate** da tutta questa produzione.

---

## La diagnosi — e la correzione della diagnosi

La prima ipotesi era che mancassero gli strumenti di pubblicazione. **Falsa, verificata:**
`social-publisher` (con `check_ready.py` e `push_social.py`) e `workflow-pubblicazione-auto`
esistono, sono scritti bene e funzionano. La fabbrica YouTube ha il suo flusso.

La causa vera e' un'altra, ed e' piu' semplice e piu' grave:

> **Nessun organo di Digital Empire guardava dentro i depositi.**
> Il lavoro finito era **invisibile**. Chi lo finiva gli dava il nome giusto, lo metteva
> nella cartella giusta, e passava al pezzo successivo. Nessuna procedura, nessun agente,
> nessuna riunione chiedeva mai *"cosa e' pronto e non e' uscito?"*.

Un'azienda che non misura il proprio lavoro fermo non sa di averlo. Le mani c'erano.
Mancava l'occhio.

---

## La decisione

**Si istituisce l'ULTIMO METRO: l'organo che vede il lavoro finito e fermo.**

1. **`scripts/ultimo_metro.py`** — apre i depositi noti, riconosce cosa e' completo,
   incrocia con il registro di cio' che e' gia' uscito, produce la lista di cosa caricare
   oggi, ordinata dal piu' vecchio. Segnala anche cosa manca ai pezzi incompleti.
2. **skill `ultimo-metro`** — il comando che lo esegue e collega ogni pezzo pronto al
   pubblicatore gia' esistente per il suo canale.
3. **`company/Memory/pubblicati.json`** — il registro di cio' che e' uscito davvero.
4. **`company/Memory/ULTIMO-METRO.md`** — il rapporto rigenerato a ogni esecuzione.

### Il principio, che vale oltre questo caso

> **Un pezzo di lavoro non e' "fatto" finche' non e' uscito.**
> Finito e non pubblicato ha lo stesso valore economico di non fatto: zero. Con in piu' il
> costo di averlo prodotto. E' la stessa legge di ADR-002 — *nessun task e' fatto finche'
> non e' salvato in Memory* — applicata all'altro capo della catena: **verso l'esterno**.

### Wrap, non riscrittura (ADR-003)

L'Ultimo Metro **non pubblica**. E' l'occhio, non la mano. I pubblicatori esistenti restano
gli unici a pubblicare, e non vengono ne' toccati ne' sostituiti.

---

## Conseguenze

**Buone:**
- Il lavoro fermo diventa un numero visibile. Un numero visibile e' un numero che si puo'
  far scendere.
- 23 pezzi sono caricabili oggi senza produrre nient'altro: e' il ritorno piu' rapido
  disponibile all'azienda in questo momento.
- Due libri si sbloccano con poco lavoro: `The_Winter_Term` ha solo bisogno della copertina.
- I dirigenti (CEO, CRO, COO) hanno finalmente il problema numero uno del loro perimetro
  scritto nero su bianco, con i numeri.

**Costi e rischi:**
- **Segnare i pezzi pubblicati e' obbligatorio.** Se non si segna, la lista mente e in due
  settimane nessuno la guarda piu'. Una lista che mente e' peggio di nessuna lista.
- **L'eta' e' quella dell'ultimo tocco**, non della fine del lavoro: un `git checkout` puo'
  ringiovanire un pezzo. Il semaforo e' una soglia di allarme, non una data anagrafica.
- **"Finito" e' misurato sui file presenti**, non sulla qualita' del contenuto. Il giudizio
  di qualita' resta alle sentinelle.

---

## Vuoti dichiarati — non risolti da questo ADR

- **⚠️ Non esiste un caricatore automatico per Amazon KDP.** I libri vanno caricati a mano.
  Costruirlo o rinunciarci e' una decisione ancora da prendere.
- **⚠️ I caroselli non sono sorvegliati**: sono sparsi in cartelle senza schema comune.
  Va prima deciso dove vive un carosello finito.
- **⚠️ Non esiste una misura di cosa succede DOPO la pubblicazione** (visualizzazioni,
  vendite, conversioni). L'Ultimo Metro chiude il buco fra "prodotto" e "pubblicato";
  resta aperto quello fra "pubblicato" e "venduto". E' il prossimo da chiudere.

---

## Verifica

Eseguito il 2026-09-03: 25 pezzi rilevati, 3 depositi sorvegliati, 0 depositi non trovati,
rapporto scritto. Nessun file esistente modificato o cancellato.

---

*Legami: ADR-002 (memory-first, la stessa legge sul lato interno) · ADR-003 (wrap, mai
riscrittura) · ADR-008 (nessun artefatto orfano) · Mandato Art. 2 (prove, non promesse) ·
skill `ultimo-metro`, `social-publisher`, `workflow-pubblicazione-auto`*
