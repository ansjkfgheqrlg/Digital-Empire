# Coverage — max17-v16

## Numeri (dichiarazione onesta — copertura PARZIALE dei frame, campionamento sistematico)

- Frame densi estratti (1 ogni 4.0s): **858** (`frame-001.png` → `frame-858.png`, 0:00 → 57:08), confermati contro `frames/manifest.json`.
- Frame unici elencati in `scenes.md` (sopra soglia di cambiamento percettivo 10.0): **273** — lista/timestamp generata da una sentinella precedente (morta per errore di connessione, non di merito), verificata in questa sessione contro `frames/manifest.json` (timestamp coerenti, nessuna discrepanza trovata sull'indice).
- **Frame guardati nativamente in questa sessione: 20 su 858 totali (2,3%), 20 su 273 unici (7,3%)**.
- **Trascrizione audio: 100% letta** — file `.vtt` originale (12.048 righe grezze con caption a scorrimento duplicate riga per riga) ripulito con uno script Python locale (deduplica dei cue ripetuti, nessun contenuto alterato o inventato — solo rimozione di righe identiche consecutive) in `clean_transcript.txt` (1.504 righe), letto per intero in 4 blocchi da questa sessione, dall'inizio (00:00:00) alla fine (00:57:10).

**Questa NON è una copertura totale dei frame** ed è dichiarata esplicitamente come campionamento mirato, per il motivo strutturale spiegato sotto — non per limite di tempo/budget saltato a caso.

## Perché il campionamento è appropriato per QUESTO video (motivazione, non scusa)

I video precedenti del lotto `max17` sono tutorial a schermo condiviso, dove ogni frame porta potenzialmente un'informazione nuova (un passaggio UI, un risultato di ricerca, un prompt diverso) — lì la regola è guardare ogni frame unico. **Questo video è la registrazione di un intervento dal vivo a un evento** (platea, palco, relatore che parla e gesticola, lavagna a fogli mobili). Le conseguenze pratiche verificate in questa sessione:

1. **Il contenuto informativo denso è quasi tutto nell'audio**, non nei frame — il relatore parla ininterrottamente per 57 minuti, i frame per la maggior parte del tempo mostrano solo il relatore che si muove sul palco davanti a uno sfondo fisso (proiettore acceso su una slide di sfondo, o schermo bianco).
2. **Le slide proiettate e i disegni a mano restano fissi per lunghi tratti** — `scenes.json` conferma "durate schermata" fino a **128 secondi** (`frame-367`, 24:24→26:32) e **124 secondi** (`frame-159`, 10:32→12:36), molto più lunghe delle poche decine di secondi tipiche di uno screen-share che scorre.
3. **Verificato di persona**: `frame-159.png` (nominale 10:32) e `frame-324.png` (nominale 21:32) mostrano lo **stesso identico disegno a mano** (grafico "SUPPLY/DOMANDA" su flip-chart) — non un errore di estrazione (controllato contro `frames/manifest.json`, timestamp coerenti con l'indice), ma il fatto fisico che l'oggetto sul palco non viene rimosso per minuti.

Dato questo, la strategia adottata è stata: **leggere il 100% dell'audio** (dove sta la stragrande maggioranza del contenuto informativo) e **campionare i frame nei punti dove appare testo nuovo su schermo o sulla lavagna** (slide con numeri/framework, testimonianze, il disegno a mano stesso), usando `scenes.md` come mappa per non perdere transizioni di scena.

## Come è stata condotta la copertura

- **Trascrizione**: file sorgente `gUnQK6bWHkI.it.vtt` (12.048 righe, formato caption a scorrimento con testo duplicato riga per riga). Deduplicato con uno script Python locale (`clean_vtt.py`, salvato nello scratchpad di sessione, non nel repo) che tiene solo l'ultima versione (più completa) di ogni cue e rimuove i duplicati consecutivi — nessun contenuto riscritto o inventato, solo compressione meccanica del formato. Risultato: `clean_transcript.txt`, 1.504 righe con timestamp preservati, letto per intero in 4 blocchi (righe 1-400, 400-800, 800-1200, 1200-1504).
- **Frame guardati nativamente (20, elencati con motivo della scelta)**:

| Frame | Timestamp nominale | Motivo della scelta |
|---|---|---|
| `frame-001.png` | 0:00 | Slide di apertura (titolo "micro personal brand") |
| `frame-047.png` | 3:04 | Stessa slide di apertura, verifica secondo sguardo |
| `frame-107.png` | 7:04 | Slide "la strategia che vi mostrerò..." |
| `frame-155.png` | 10:16 | Disegno a mano flip-chart in corso di tracciamento |
| `frame-159.png` | 10:32 | Disegno completo "SUPPLY/DOMANDA" su flip-chart |
| `frame-160.png` | — (interno, non in scenes.md) | Verifica ravvicinata dello stesso disegno |
| `frame-208.png` | 13:48 | Relatore scrive a mano "F.E." + cifra sulla lavagna |
| `frame-324.png` | 21:32 | Stesso disegno supply/domanda, verifica persistenza nel tempo |
| `frame-418.png` | 27:48 | Slide "Una sera si fece i calcoli..." (1000 True Fans) |
| `frame-470.png` | 31:16 | Testimonianza Marco Scardeoni & Partners |
| `frame-497.png` | 33:04 | Transizione verso sezione Instagram Authority Funnel |
| `frame-540.png` | 35:56 | Disegno a mano "funnel a ragnatela" |
| `frame-599.png` | 39:52 | Slide "La verità dopo + di una decade..." (pricing) |
| `frame-663.png` | 44:08 | Slide "Step 2. Storie in Evidenza (la struttura)" — 14 card leggibili |
| `frame-729.png` | 48:32 | Slide ciclo settimanale ("Dopo la Settimana 4, si riparte...") |
| `frame-773.png` | 51:28 | Slide "8 Segreti Per diventare Un Leader Da Seguire" |
| `frame-798.png` | 53:08 | Slide "Il Potere dello Story Telling" con foto evento passato |
| `frame-824.png` | 54:52 | Relatore in chiusura sezione storytelling |
| `frame-828.png` | 55:08 | Foto di un evento affollato passato (prova sociale storytelling) |
| `frame-858.png` | 57:08 | Ultimo frame — slide di chiusura "E può trasformare anche la VOSTRA..." |

- **Metadata**: `ingest.json` letto per intero (titolo, uploader, durata 3430s, nessun capitolo ufficiale). `frames/manifest.json` interrogato via script per confermare `timestamp_sec` di frame specifici e risolvere il dubbio sulla persistenza del disegno flip-chart.
- **Confronto con la codebase DE**: verificata via `find`/`Grep` l'esistenza di `cro-strategy-social-(ig-tiktok)`, `social`, `market-social`, `icp-radar`, `pricing`, `market-launch` prima di citarli in `video-analysis.md`; eseguiti grep mirati (`lista d'attesa|waitlist|sold.?out`, `storie in evidenza|highlight`, `zona di consapevolezza|awareness|buca di conversione`) per verificare i gap dichiarati nella sezione Consigli, non assunti a fiducia.

## Frame illeggibili o parzialmente illeggibili

- `frame-208.png` (13:48) — la cifra scritta a mano dal relatore accanto a "F.E." è parzialmente coperta dal proprio braccio nell'istante dello scatto; leggibile con certezza solo l'inizio "55.0..." — non trascritta come cifra esatta in `video-analysis.md`/`atoms.json`, riportata come incerta.
- `frame-540.png` (35:56) — disegno a mano con linee curve ed etichette molto piccole; la corrispondenza con il "funnel a ragnatela" descritto a voce è plausibile ma le etichette esatte sul disegno non sono leggibili con certezza.
- Acronimo "**O.T.S.C.B**" leggibile su una card di `frame-663.png` (Storie in Evidenza) ma **mai spiegato** né a voce né su schermo in nessun punto coperto da questa sessione — riportato come sigla non decifrata in `video-analysis.md`, non interpretata a caso.

## Correzioni / cautele di lettura documentate per trasparenza

- **Falsa pista investigata e risolta**: al primo confronto tra `frame-159.png` (nominale 10:32) e `frame-324.png` (nominale 21:32) — entrambi mostranti lo stesso disegno a mano "SUPPLY/DOMANDA" — è sorto il sospetto di un bug di sincronizzazione tra `scenes.json` e i frame reali (drift dei timestamp su un video di 57 minuti). Verificato con `frames/manifest.json` (che assegna `timestamp_sec = (indice-1) × 4.0`, quindi frame-159 → 632s → 10:32 e frame-324 → 1292s → 21:32, entrambi coerenti con l'indice): **non è un bug**, è semplicemente che un oggetto fisico (la lavagna a fogli mobili) resta sul palco, visibile in inquadratura, per undici minuti dopo essere stato disegnato. Documentato qui invece di essere silenziosamente ignorato, perché è un pattern strutturale utile per capire come campionare video di eventi dal vivo in futuro (vedi KA-029 in `atoms.json`).
- I numeri finanziari dichiarati a voce dal relatore (35+ milioni di euro, singoli case study clienti, 60 milioni di visualizzazioni ecc.) **non sono verificati indipendentemente** da questa sessione — nessuna dashboard, CRM o screenshot di incasso è stato visto a schermo che li confermi. Riportati sempre come "dichiarazione dell'autore", mai come fatto auditato, in `video-analysis.md`.
- L'ordine cronologico esatto di alcuni aneddoti biografici (2012→2014→2016) è ricostruito dalla sola trascrizione audio, senza conferma visiva delle date sulle foto d'archivio proiettate (non lette a schermo intero in questa sessione).

## Riepilogo finale

- **Frame guardati nativamente: 20/858 (2,3%) — campionamento mirato dichiarato, non copertura totale.**
- **Trascrizione audio: 1.504/1.504 righe deduplicate lette (100%)**, corrispondenti a tutte le 12.048 righe grezze del `.vtt` originale.
- **Atomi estratti in `atoms.json`: 29** — 24 confermati anche o soprattutto dall'audio, 5 confermati solo/principalmente dal frame guardato (KA-005/006/010/013/019/020/021/024/025/027/028/029 hanno riferimento frame; il resto è "n/a (solo audio)").
- **Numeri finanziari dichiarati raccolti: 20+** (tabella completa in `video-analysis.md`), tutti etichettati come dichiarazioni verbali non verificate indipendentemente.
- **Nessun frame è stato descritto senza essere stato realmente aperto e guardato in questa sessione** (regola NO-FINTO) — dove il contenuto di un frame non guardato viene menzionato in `video-analysis.md` (es. foto d'archivio, screenshot DM), è sempre esplicitamente qualificato come "descritto dalla trascrizione, non guardato a schermo intero in questa sessione".
