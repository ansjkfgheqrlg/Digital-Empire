# ✂ CRITICA 2 — ESECUZIONE

> **Oggetto:** `V1-PIANO-GENERALE.md` · **Angolo:** dove si inceppa quando qualcuno lo esegue davvero
> **Revisore:** indipendente, non autore del piano (ADR-017)
> **Data:** 2026-09-06
> **Metodo:** ogni rilievo ha una prova — un file dei censimenti con la sezione, o un comando lanciato in sola lettura con il suo esito. Rilievi senza prova: eliminati prima della consegna.

---

### R-1 — Il ritorno piu' alto per il minor lavoro non esiste nel piano  [FATALE]
- **Dove:** V1 §22 (tutti gli scaglioni E0..E9) e §21 (criterio d'ordine, principio 1 e 3)
- **Cosa dice il piano:** §21: *«Prima cio' che non costa e sblocca molto»* e *«Prima cio' che porta denaro»*. Poi, negli scaglioni, il Workflow pubblicazione automatica — l'Ultimo Metro in persona — **non compare mai**.
- **Perche' non funziona all'atto pratico:** il censimento 04b lo dichiara testualmente *«il ritorno piu' alto per il minor lavoro di tutto il censimento»*: `main_orchestrator` muore all'import per `OpenAIError: Missing credentials` (`OPENROUTER_API_KEY`/`GROQ_API_KEY` assenti dal `.env`), mentre `pubblica.py` e `ig_carousel_publish.py` sono **gia' verificati funzionanti**, con dry-run di default e regola *«nessun PASS finto»*. In coda ci sono 25 pezzi finiti mai usciti, il piu' vecchio da 135 giorni (ADR-016). Costo dichiarato: **una chiave nel `.env`** piu' lo spostamento di un'istanziazione dentro una funzione. V1 lo lascia — al massimo, per implicazione — dentro E8 «gli orfani per triage», dietro E1..E7: **125-194 ore di lavoro pianificato prima di girare una chiave**. E il paradosso e' doppio: E0 tocca **proprio OpenRouter** (rotazione B-021), cioe' Max passera' dalla console OpenRouter in E0 e il piano non gli fa scrivere la chiave nuova nell'unico `.env` che la aspetta.
- **Prova:** `grep -n -i "ultimo|pubblica|metro|OPENROUTER"` su `V1-PIANO-GENERALE.md` → zero occorrenze di Ultimo Metro / Workflow pubblicazione (solo la rotazione B-021 in §22-E0 e la parola «orfani» in E8). Contro: `dati/censimento-04b-motori.md` §3.6 e tabella «DORMIENTI col guasto» riga 1 («E' il ritorno piu' alto per il minor lavoro di tutto il censimento»), sezione D riga 3 (orfano, `published.json` = `{}`).
- **Dove si romperebbe:** non si rompe: peggio, **non parte**. Il principio d'ordine di §21 viene violato dal suo stesso autore alla prima applicazione, e chi esegue segue l'ordine scritto, non il principio.
- **Con quale conseguenza:** 25 pezzi gia' pagati restano fermi per tutta la durata di E1..E7 (settimane di calendario, vedi R-8); B-043 («DE non misura un solo euro») resta aperto mentre il piano dichiara il denaro «primo scaglione».
- **Cosa proporresti al posto:** dentro E0: Max incolla la chiave nel `.env` del publisher (e' lavoro da credenziali, identico al resto di E0); primo pezzo di E1: l'aggancio Carousel Factory → `pubblica.py --live` (04b: «i due motori sono a un argomento di distanza»).

### R-2 — I tre collegamenti che il censimento mette per primi sono ignorati o rimandati  [GRAVE]
- **Dove:** V1 §22 (E3, E4, E8) e §23; tabella fonti §0.3
- **Cosa dice il piano:** E3 accende la catena AGENCY (coerente col punto 1 di 02d). La Tesoreria e' «fuori scaglione, perche' e' una riga» ma «va agganciata a N4 (il ledger)» — cioe' dietro E4. Dell'Ultimo Metro→LAN-STR e del campo `costi` nei checkpoint: **nulla**.
- **Perche' non funziona all'atto pratico:** `censimento-02d` Sintesi C ordina i dieci collegamenti da accendere per primi con criterio misurato (incasso · sblocco a valle · motore gia' presente su entrambi i lati). I primi tre: la catena AGENCY (V1 la prende), **#312 ULTIMO METRO → LAN-STR** («non richiede di produrre niente: la fila e' gia' piena»), **#313 LAN-REG → TESORERIA** («costo di accensione: una riga scritta a mano»). Il quarto, **#291 campo `costi` in `checkpoint.py`**, e' quotato «un'ora di lavoro, e da quel giorno ogni task chiuso lascia un numero». V1 aggancia la Tesoreria a N4, che sta in E4 (25-40 h), dietro E1+E2+E3 (22-34 h): una cosa da «una riga scritta a mano» aspetta 47-74 ore di lavoro a monte. Il #291 (un'ora) non e' in nessuno scaglione.
- **Prova:** `grep -n "312|313|LAN-STR|LAN-REG|costi.*checkpoint|02d"` su `V1-PIANO-GENERALE.md` → **0 risultati**. Contro: `dati/censimento-02d-sintesi-collegamenti.md`, Sintesi C punti 2, 3 e 4 (righe 276-316 del file).
- **Dove si romperebbe:** al primo giorno di E4: chi esegue costruira' il ledger N4 «perche' senza di lui nessun altro scaglione e' misurabile» mentre i due agganci che gli darebbero i primi numeri veri (tesoreria a una riga, costi nei checkpoint a un'ora) restano spenti — il ledger nasce di nuovo vuoto, come `entrate.jsonl`.
- **Con quale conseguenza:** ~50-70 ore di costruzione prima del primo numero misurato, quando i censimenti quotano il primo numero a 1-2 ore da subito; e il rischio R3 di V1 («NEXUS diventa un altro pezzo di carta») aumenta invece di diminuire, perche' N4 parte senza alimentatori.
- **Cosa proporresti al posto:** uno scaglione E0.5 «gli agganci a costo zero» (½ giornata): riga in tesoreria, campo `costi` obbligatorio in `checkpoint.py`, `pubblicati.json` creato — tre alimentatori vivi prima che N4 esista.

### R-3 — V1 e' fondato sui censimenti nella versione monca, e non lo sa piu'  [GRAVE]
- **Dove:** V1 §0.3 (tabella fonti) e §27 (punti 1, 2, 3)
- **Cosa dice il piano:** §0.3: «`02b` 208 righe», «`04`+`04b` 196 righe»; §27: «il censimento dei motori e' al 20% … `04b` e' a 115 righe», «le tre sintesi degli organi … mancano».
- **Perche' non funziona all'atto pratico:** oggi, sul disco, quei file sono finiti: `02b` **619 righe** (dichiarata «tabella completa»), `04b` **613 righe** («Censimento 04b chiuso il 2026-09-06. 25 motori schedati»), `01c` **468 righe**, `02d` **622 righe**, `03c` **1.064 righe**. V1 non cita mai `01c`, `02d`, `03c` (grep → 0 occorrenze). Non e' solo un problema di completezza — e' che **le parti arrivate dopo ribaltano l'ordine del lavoro**: 02d mette per primi collegamenti che V1 non nomina (R-2), 04b individua il ritorno piu' alto (R-1), 01c consegna il vizio dei gate che confermano il falso (R-5). Chi eseguisse V1 domani lavorerebbe con la mappa vecchia avendo quella nuova nel cassetto.
- **Prova:** `wc -l dati/*.md` → 02b=619, 04b=613, 01c=468, 02d=622, 03c=1.064; `grep -c "01c|02d|03c" V1-PIANO-GENERALE.md` → **0**.
- **Dove si romperebbe:** in V2, se il rifacimento riparte dal testo di V1 invece che dai censimenti chiusi: gli scaglioni verrebbero raffinati nell'ordine sbagliato ereditato.
- **Con quale conseguenza:** ore di V2 spese a dettagliare E-scaglioni la cui priorita' e' gia' smentita dai dati di casa.
- **Cosa proporresti al posto:** V2 riapre i cinque file chiusi dopo V1 PRIMA di toccare gli scaglioni, e lo dichiara in testa alla sua tabella fonti.

