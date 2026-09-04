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
