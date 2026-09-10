# BASELINE — la fabbrica YouTube PRIMA dello studio

> Passo 0.1 del [PIANO-STUDIO-AITUBEPRO](../../plans/PIANO-STUDIO-AITUBEPRO.md).
> **Misurata il 2026-09-04**, eseguendo i comandi — nessun numero ripreso da un checkpoint.
> Serve a una cosa sola: fra qualche settimana poter dire **se lo studio ha cambiato qualcosa**,
> con i numeri davanti, invece di raccontarlo.

---

## 1. Salute del motore

| Metrica | Valore | Come l'ho misurata |
|---|---|---|
| Test della fabbrica | **11/11 verdi** (10,18s) | `python test_youtube_apex7.py`, eseguito ora |
| Script Python nella fabbrica | 136 | `find . -name "*.py"` esclusi i profili browser |
| Agenti documentati | **34** | `find 03-AGENTI-E-RUOLI -name "*.md"` |
| Agenti con almeno una soglia numerica | **12 su 34 (35%)** | ricerca di numeri con unità nei file agente |

> I 22 agenti senza un solo numero sono **prosa**: dicono cosa sorvegliare, non con quale
> soglia. È il primo bersaglio naturale del binario A — ogni lezione che porta un numero
> vero (durata, CTR, densità di parole) trasforma un guardiano finto in uno vero.

### 1-bis. Tempo per video — **la misura che ci manca** (A4-L05-04, aperta il 2026-09-05)

| Metrica | Il metro del corso | Il nostro |
|---|---|---|
| **Tempo per video, dall'idea al file pronto** | **5 minuti** (A4/L05, cronometrato in diretta: «sono le 13 e 18» → «ci ho impiegato veramente 5 minuti») | **NON MISURATO** |

Questa baseline conta test, script, agenti e soglie: **non contiene un solo minuto di
produzione reale**. È un buco, e pesa il doppio alla luce di `ADR-016` (Ultimo Metro): **25 pezzi
finiti e mai pubblicati**, il più vecchio fermo da 135 giorni.

Finché il numero non c'è, la frase «noi puntiamo sulla qualità, loro sulla quantità» non è una
scelta dichiarata: è una copertura della lentezza. Nessuno può dire se i nostri gate costano
dieci minuti o tre giorni.

**Come si chiude:** cronometrare **una** produzione vera end-to-end (F1→F5) e scrivere qui il
numero, con la data e cosa era incluso. **Assegnata al gate di categoria A4**, insieme alla
verifica sulla musica (`A4-L04-04`).

**Attenzione a non barare nel confronto:** i 5 minuti del corso comprendono solo scelta della
fonte, riscrittura, montaggio ed export. Non comprendono ricerca di nicchia, controllo dei fatti,
SEO, miniatura e pubblicazione — che nella nostra catena ci sono. Quando misureremo, il confronto
onesto è **passo per passo**, non totale contro totale.

## 2. Le soglie in vigore — copiate esatte

### `02-AUTOMAZIONI-E-SCRIPTS/regolatori.py`
| Costante | Valore | Cosa governa |
|---|---|---|
| `N_GRAM` | 8 | quante parole identiche di fila alla fonte fanno scattare il blocco per copiatura |
| `MIN_ELEMENTI_NUOVI` | 3 | quanti concetti nominati originali deve avere uno script |
| `DURATA_MINIMA_S` | **480** (8:00) | durata minima del video finito |
| `DURATA_MASSIMA_S` | **600** (10:00) | durata massima del video finito |
| `HASH_SIZE` / `DISTANZA_MINIMA_BIT` | 8 / 10 su 64 bit | quanto la copertina deve differire dall'originale |

### `02-AUTOMAZIONI-E-SCRIPTS/apex7_orchestrator.py`
| Costante | Valore | Cosa governa |
|---|---|---|
| `PAROLE_AL_MINUTO` | 185 | conversione parole → durata parlata |
| `PAROLE_MINIME_SCRIPT` | **2220** (= 12:00) | lunghezza minima dello script |
| `CHANNEL_CACHE_TTL_HOURS` | 168 (7 gg) | freschezza dei dati di canale |
| `VIDEO_MATURITY_FLOOR_HOURS` | 24 | sotto quest'età la velocità di visualizzazione è rumore |
| `VIDEO_MULTIPLO_MEDIANA` | 3.0 | quanto un video deve battere la mediana del suo canale per essere "virale" |
| `VIDEO_VPH_MINIMO` | 2.0 | pavimento assoluto: esclude il miglior video di un canale morto |

---

## 3. ⚠️ DUE DIFETTI TROVATI MISURANDO — non erano noti

### D-1 — Le soglie di durata si contraddicono, e nessun video può rispettarle entrambe

| | Valore | Fonte |
|---|---|---|
| durata **massima** ammessa | 600 s (10:00) | `regolatori.DURATA_MASSIMA_S` |
| durata **minima** imposta allo script | 2220 parole ÷ 185 = **720 s (12:00)** | `apex7_orchestrator.PAROLE_MINIME_SCRIPT` |

**La fabbrica chiede l'impossibile: uno script di almeno 12 minuti, e un video di al massimo
10.** Nessun video può passare entrambi.

**Verificato sui video prodotti oggi**, misurati con `ffprobe`:

| video | durata reale | oltre il massimo di |
|---|---|---|
| video-06 | 826,8 s (13:46) | +226,8 s |
| video-07 | 826,4 s (13:46) | +226,4 s |

**Entrambi sforano del 38%.** Sono già caricati su YouTube.

**Decisione rimandata di proposito:** quale sia la durata giusta è esattamente ciò che
insegna la categoria A6 del corso («Quanti video pubblicare, quanto devono durare e
proporzione trend/evergreen»). La chiudo con un numero **motivato dal corso**, non con una
toppa scelta a caso oggi. → prima regola attesa: `A6-Lxx-01`.

### D-2 — Il gate di qualità esiste ma non viene MAI eseguito in produzione

`regolatori.verifica_qualita()` — quello che controlla la durata del video finito — è
chiamato **solo** da `regolatori.py` quando lo si lancia a mano da riga di comando (riga 468).
**La catena di produzione (`produci_video_completo.py` → `apex7_orchestrator.py` →
`fliki_client.py`) non lo invoca mai.**

Conseguenza: il controllo di durata **non ha mai bocciato nulla**, e per questo D-1 è potuto
restare invisibile. Un gate scollegato è peggio di un gate assente: dà l'impressione che
qualcuno stia controllando.

**Sta in binario B** (tocca il motore) → si chiude al gate della categoria A6, insieme a D-1:
prima si decide il numero giusto, poi si collega il controllo che lo fa rispettare.
Collegarlo oggi, con le soglie contraddittorie, bloccherebbe ogni produzione.

---

## 4. Produzione — dove siamo davvero

| Metrica | Valore | Fonte |
|---|---|---|
| Video prodotti registrati | **8** | `memory/video_prodotti.json` |
| Cartelle di consegna | **8** (`video-01` … `video-08`) | `VIDEO-PRONTI/` |
| Video con destinazione YouTube nota | **2** | i due caricati oggi |
| Caricati oggi (privati, pubblicità attive) | 2 — `RUg6TgSd79s`, `QwtZ2e2MY1c` | YouTube Studio |
| In attesa della copertina di Max | 1 (`video-08`) | `VIDEO-PRONTI/video-08/` |

**Il dato che pesa più di tutti:** solo **2 video su 8** hanno una destinazione tracciata.
Gli altri 6 sono stati prodotti e il sistema non sa dove siano finiti. È la stessa ferita di
ADR-016 (*Ultimo Metro*): l'azienda produce e non pubblica, e soprattutto **non sa** cosa ha
pubblicato.

---

## 5. Cosa dovrà muoversi (i numeri su cui giudicare lo studio)

Questi valori vanno rimisurati **a ogni categoria chiusa**. Il piano si giudica qui.

| # | Metrica | Oggi | Direzione attesa |
|---|---|---|---|
| M1 | agenti con soglie numeriche | 12 / 34 | ↑ |
| M2 | soglie contraddittorie | **1** (D-1) | → 0 |
| M3 | gate scollegati dalla produzione | **1** (D-2) | → 0 |
| M4 | video con destinazione tracciata | 2 / 8 | ↑ |
| M5 | CTR medio dei video pubblicati | **non ancora misurato** | da rilevare su YouTube Studio |
| M6 | regole del corso applicate | 0 | ↑ |
| M7 | test della fabbrica | 11/11 | **resta verde, sempre** |

> **M5 è dichiarato mancante, non stimato.** Va letto da YouTube Studio sui video già
> pubblicati prima di chiudere la prima categoria: senza, l'effetto delle lezioni su
> copertine e CTR non sarebbe dimostrabile.

---

# RILETTURA AL GATE DELLA CATEGORIA A4 (2026-09-06)

> Condizione 5 del gate (piano §9): *«baseline riletta, i numeri aggiornati, con il delta
> scritto in chiaro»*. Misurata rieseguendo i comandi, non ricordata.

| Metrica | 2026-09-04 (prima) | 2026-09-06 (dopo A4) | Delta |
|---|---|---|---|
| Test della fabbrica | **11/11 verdi** | **16/16 verdi** | **+5 prove**, tutte sulle regole di binario B applicate al gate |
| Script Python | 136 | 136 | invariato — nessun file nuovo, solo file cambiati |
| Agenti documentati | 34 | 34 | invariato |
| Agenti con almeno una soglia numerica | **12 su 34 (35%)** | **19 su 34 (56%)** | **+7 agenti** |
| Schede di riferimento (`references/`) | 8 | **9** | +1 (`scelta-strumenti.md`, nata dallo studio) |
| Regole a registro | **0** | **59** | +59, tutte con prova (frame o minuto), **59 applicate** |
| Arbitrati (`CONFLITTI.md`) | 0 | **7** | C-001 → C-007 |

**Avvertenza onesta sul 35% → 56%:** il criterio del 2026-09-04 («numeri con unità nei file
agente») non fu registrato come espressione esatta, quindi la mia misura di oggi può non essere
identica alla sua. **La direzione però non è in dubbio e si vede file per file:** `script-writer`
ha guadagnato il budget di parole dei primi 30 secondi, `qa-audio-video` il metro dei −35 dB e la
chiusura sulla musica, `niche-scout` le due domande di liceità e riproducibilità, `video-producer`
intro/outro e sincronia. **Lezione di metodo: una baseline deve registrare il COMANDO, non solo il
numero** — altrimenti il delta si discute invece di leggerlo. Vale per la prossima categoria.

## Cosa è cambiato davvero nel motore (binario B, applicato oggi)

| prima | dopo |
|---|---|
| la **voce** del canale veniva ri-risolta a ogni generazione: bastava che Fliki cambiasse l'ordine del suo elenco e il canale cambiava voce da solo | **`voice_id` fisso** in `CANALI` per entrambi i canali, con l'`_id` reale letto dall'API |
| `aspectRatio` era la costante `"16:9"` scritta nel payload: **Shorts impossibili**, e nessun documento diceva perché | il formato è **dichiarato dal canale** o da `--formato`, tre valori ammessi, default invariato: **la fabbrica può produrre Shorts** |
| il piano editoriale non aveva un posto per le fonti di supporto | colonna **`fonti_extra`** |

## Cosa NON è cambiato, e resta aperto

- **D-1 e D-2 sono ancora aperti di proposito** (durata impossibile e `verifica_qualita()` mai
  invocata): si chiudono al gate della categoria **A6**, col numero motivato dalla lezione sulla
  durata ottimale. Non si tappano con una toppa scelta a caso.
- **Il tempo per video resta NON MISURATO** (§1-bis). È la sola condizione del gate A4 che si
  chiude con un'azione di produzione, non di studio.

## ⭐ D-1 — letta la lezione attesa (A6/L05, 2026-09-10) — NON si chiude con un numero

`A6/L05` («Quanti video pubblicare, quanto devono durare e proporzione trend evergreen»,
`company/Memory/studi/aitubepro/A6-viral-mastery/L05-durata-e-frequenza/`) è la lezione che
questo documento indicava come quella attesa per chiudere D-1. Letta integralmente, parlato +
schermo: **non dà un numero unico di durata ottimale**. Lo dice a voce (*"non c'è una durata
prestabilita che noi dobbiamo fare"*, 03:37-03:57) e lo conferma a schermo in modo decisivo — il
docente scrive lui stesso in diretta le risposte alle quattro domande della lezione, e la voce
«Quanto devono durare i video?» resta **senza risposta scritta per tutti i 14:22**, mentre le
altre tre domande ricevono tutte un numero (`frame-350.png @ 11:38`, `frame-410.png @ 13:38`).

**D-1 resta aperto, ma non per mancanza di studio: perché il numero che si aspettava non esiste
nel corso.** Dichiararlo (invece di forzare uno dei due numeri disponibili — floor 4 minuti,
soglia opzionale 8 minuti — a fare da sostituto) è la scelta che questo stesso documento impone
al §3. La correzione proposta (`A6-L05-02`/`A6-L05-03`, in coda al gate categoria) non è "cambia
la costante": è sostituire `DURATA_MASSIMA_S`/`DURATA_MINIMA_S` fissi con un range **per
tipo di nicchia**, usando i due numeri reali della lezione (4 min floor, 8 min soglia
monetizzazione) come parametri di quella funzione — chiudendo comunque la contraddizione tecnica
con `PAROLE_MINIME_SCRIPT` (nessun video sarà più matematicamente impossibile da produrre), senza
inventare un "numero ottimale" che la lezione non dà. Dettaglio completo: `report.md` §7 nella
stessa cartella.

**D-2 resta aperto**, riverificato lo stesso giorno con lo stesso grep: `verifica_qualita()`
continua a essere invocata solo da CLI (`regolatori.py:468`), mai dalla catena di produzione.

**Trovato nello stesso giro, un terzo difetto non ancora numerato**: `A6/L06` («Automazione della
pubblicazione») ha verificato che `youtube_uploader_playwright.py` imposta **sempre** "Privato" —
non solo prima dell'approvazione di Max (corretto, è il gate voluto, vedi `CONFLITTI.md` C-008),
ma **anche dopo**: non esiste nessun percorso automatico che porti un video già approvato a
diventare pubblico/programmato. È la stessa ferita di `ADR-016` (Ultimo Metro) vista da un angolo
tecnico preciso — registrato come regola `A6-L06-01`, candidato al gate A6.
