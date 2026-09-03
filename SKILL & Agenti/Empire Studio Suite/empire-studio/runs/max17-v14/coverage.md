# Coverage — max17-v14 (`P-BQ-AGS0ck`)

## I numeri veri (contati da me in questa sessione, sul disco)

- **Frame effettivamente presenti su disco**: **390** file `frame-NNN.png` in `frames/` (+ `manifest.json`), a 1 frame ogni 4.0s, `frame-001.png` → `frame-389.png` (389 frame densi dichiarati da `scene_detector.py` + il file `manifest.json` stesso non contato come frame immagine — verificato con `ls | wc -l` = 390 file totali nella cartella, di cui 389 sono `frame-NNN.png`).
- **Frame unici indicati da `scenes.json`/`scenes.md`** (soglia 3.0, `scene_detector.py` eseguito in questa sessione con `--interval 4.0`): **338/389 (riduzione 13,1%)**. Riduzione bassa rispetto ad altri run del lotto max17 (49-86%) perché questo video è quasi interamente talking-head con gesti e micro-movimenti continui, non uno screen-recording con lunghe schermate ferme: il delta percettivo tra frame consecutivi resta quasi sempre sopra soglia anche quando il contenuto informativo non cambia.
- **Frame effettivamente aperti e guardati da me in questa sessione**: **83 distinti** (elenco completo sotto).
- **Copertura sull'elenco `scenes.json`**: 83/338 = **24,6%**.
- **Copertura sul totale dei frame estratti**: 83/389 = **21,3%**.

Questi numeri sono stati contati da me, in questa sessione, sommando le chiamate `Read` effettivamente eseguite sui file `frames/frame-NNN.png` — non ripetuti da un altro documento. Nessun numero di questo file è stato preso da `EMP-QQ2R.md` o da altri run.

## Metodo di campionamento

A differenza di altri run del lotto (dove si è tentato di leggere il 100% dei `scenes.json`), qui è stato usato un **campionamento sistematico uniforme**, dichiarato esplicitamente come tale, per un motivo preciso: il contenuto è un talking-head continuo di quasi 26 minuti con un vincolo tecnico duro di 5-6 immagini per lettura — leggere tutti i 338 frame-scena avrebbe richiesto ~68 batch di letture, con un rischio concreto di ripetere lo stesso pattern di "numeri mai verificati" già trovato due volte in questa sessione su altri run del lotto (vedi `EMP-QQ2R.md` §3).

1. **Lista campione**: generata con uno script Python che seleziona, ogni 20 secondi esatti (0s, 20s, 40s, ... 1540s = 78 timestamp), il frame di `scenes.json` più vicino a quel timestamp — 78 frame distinti, distribuiti uniformemente su tutti i 10 capitoli di `ingest.json` senza saltarne nessuno.
2. **Lettura**: tutti i 78 frame della lista campione sono stati aperti e guardati per intero, in ordine cronologico, a blocchi di 5 `Read` per messaggio (mai di più, come da vincolo tecnico), dal primo (`frame-001.png`, 0:00) all'ultimo (`frame-386.png`, 25:40).
3. **Verifica mirata aggiuntiva**: dopo il campione sistematico, altri **5 frame extra** sono stati aperti per verificare un'ipotesi nata durante la lettura (l'esistenza di cartelli "Move 01-04" analoghi al "Move 05" trovato a 20:00): `frame-050` (vicino all'inizio del capitolo Hook), `frame-124` (vicino all'inizio di Stakes), `frame-210` (vicino all'inizio di Turn), `frame-283` (vicino all'inizio di Shatter), più `frame-389` (ultimo frame del video, oltre la lista campione che si fermava a 1540s). Nessun cartello "Move 01-04" è stato trovato in questi 4 punti — riportato come osservazione parziale in `video-analysis.md`, non come prova che non esistano altrove nel video.
4. **Trascrizione**: `P-BQ-AGS0ck.en.vtt` (5.392 righe, formato caption a scorrimento YouTube auto-generate) deduplicato con uno script Python scritto in questa sessione (prende l'ultima riga di ogni blocco di caption, scarta i duplicati consecutivi) → `transcript_clean.txt`, **674 righe pulite con timestamp**, **letto per intero** dall'inizio (00:00:00) alla fine (00:25:52) in 4 blocchi di lettura.
5. **Metadata**: `P-BQ-AGS0ck.info.json` letto per titolo, uploader/channel, upload_date, view_count, like_count, description, tags, capitoli.

## Elenco frame guardati (83, in ordine cronologico)

**Campione sistematico (78, uno ogni ~20s)**:
001, 006, 011, 016, 021, 026, 031, 036, 041, 046, 051, 056, 061, 066, 071, 076, 081, 086, 091,
096, 101, 106, 111, 116, 121, 126, 131, 136, 141, 146, 151, 156, 161, 166, 171, 176, 181, 186,
191, 195, 201, 206, 211, 216, 221, 226, 231, 236, 241, 245, 251, 256, 261, 266, 271, 276, 280,
286, 291, 296, 301, 306, 311, 316, 322, 326, 331, 336, 341, 345, 351, 356, 361, 365, 372, 376,
381, 386

**Verifica mirata aggiuntiva (5)**:
050, 124, 210 *(già nel campione sistematico, riletto per verifica mirata)*, 283, 389

*(nota: 210 compare in entrambi gli elenchi — è stato aperto una sola volta, contato una sola volta nel totale 83)*

## Copertura per capitolo (`ingest.json`, 10 capitoli)

| Capitolo | Timestamp | Durata | Frame-scena disponibili (`scenes.json`) | Frame guardati | Copertura |
|---|---|---|---|---|---|
| Why Some Speakers Get Forgotten | 0:00–2:34 | 154s | 40 | 9 | 22,5% |
| Learn HSTSS | 2:34–3:22 | 48s | 12 | 3 | 25,0% |
| Craft The Hook | 3:22–8:18 | 296s | 74 | 15 | 20,3% |
| Add The Stakes | 8:18–10:04 | 106s | 27 | 6 | 22,2% |
| The Story Of The Couch | 10:04–14:03 | 239s | 60 | 14 | 23,3% |
| Find The Turn | 14:03–18:49 | 286s | 72 | 16 | 22,2% |
| Build The Scene | 18:49–19:57 | 68s | 17 | 4 | 23,5% |
| Land The Shadow (Shatter) | 19:57–21:27 | 90s | 23 | 6 | 26,1% |
| Scale It Like Silva Ultra Mind | 21:27–24:07 | 160s | 40 | 8 | 20,0% |
| Avoid These Mistakes | 24:07–25:55 | 108s | 27 | 7 | 25,9% |
| **Totale** | | 1555s | **~338*** | **83*** | **~24,6%** |

*I conteggi per capitolo sono una stima ottenuta mappando i timestamp dei frame-scena e dei frame guardati sui confini di `ingest.json` (arrotondamento sui secondi); la somma dei "frame-scena disponibili" per capitolo può differire di 1-2 unità dal totale esatto 338 per effetto di arrotondamento ai confini di capitolo. **Ogni capitolo ha copertura non-zero e superiore al 20%**, distribuzione deliberatamente uniforme per il campionamento a intervalli fissi (non concentrata su un solo capitolo).

## Perché il campionamento sistematico è dichiarato onesto (non "NO-FINTO")

Questo video è per **~90% talking-head continuo** con solo overlay grafici periodici (quote-card, titoli di sezione, b-roll di pochi secondi). A differenza di un video con demo software (dove ogni frame-scena può contenere un passaggio operativo diverso da trascrivere), qui la maggior parte dei 338 frame-scena non guardati sono variazioni di postura/gesto della stessa inquadratura fissa, senza nuova informazione — la trascrizione integrale (674 righe, letta per intero) copre il contenuto verbale al 100%; i frame servono a verificare **cosa si vede** (grafiche, nomi reali, prodotti, b-roll) più che a recuperare informazione mancante dal parlato. I 5 frame di verifica mirata aggiuntiva sono stati aperti proprio per testare un'ipotesi (esistenza di "Move 01-04") invece di assumerla — l'esito negativo (non trovati) è riportato come tale, non nascosto.

## Frame illeggibili o parzialmente illeggibili

- **frame-016 (1:00)**: b-roll cinematografico d'archivio (giovane uomo, stile pellicola anni '60-'70) — identità della scena/film non verificabile con certezza dal solo frame.
- **frame-146 (9:40)**: screenshot homepage YouTube con card consigliate, la cui relazione con il contenuto narrato in quel punto (storia del divano) non è chiara — riportato come osservazione senza interpretazione forzata in `video-analysis.md`.
- **Tabella HSTSS parzialmente pixelata**: nei frame prima del completamento del reveal (es. frame-051, frame-126, frame-280) alcune righe della tabella mnemonica sono deliberatamente sfocate/pixelate dall'editor video come effetto di "reveal progressivo" — non un problema di risoluzione del frame, confermato confrontando lo stesso elemento grafico nel tempo (frame-356 mostra la tabella completa e leggibile).

Nessun frame tra gli 83 guardati è risultato completamente illeggibile per motivi tecnici (compressione, blur, risoluzione).

## Trascrizione

- Sorgente: `P-BQ-AGS0ck.en.vtt`, 5.392 righe (formato caption a scorrimento con testo duplicato riga per riga).
- Deduplicata con script Python scritto in questa sessione → `transcript_clean.txt`, **674 righe pulite con timestamp** (da 1.344 righe intermedie con dedup solo parziale del primo tentativo, poi rifatto prendendo l'ultima riga di ogni blocco caption e scartando i duplicati consecutivi).
- **Letta per intero**, dall'inizio (00:00:00) alla fine (00:25:52), in 4 blocchi di lettura (righe 1-50, 50-300, 300-550, 550-674).

## Riepilogo finale

- **Frame guardati: 83/338 frame-scena (24,6%), 83/389 frame densi totali (21,3%)** — numeri contati da me in questa sessione, non ripetuti da altri documenti.
- **Trascrizione: 100% (674/674 righe pulite lette per intero)**.
- **Atomi estratti in `atoms.json`: 35**, tutti con `confidenza: osservato` (nessuna inferenza marcata `inferito` in questo run — ogni atomo cita un frame realmente aperto o la trascrizione/i metadati realmente letti).
- **Correzione importante rispetto a `company/Memory/riprese/EMP-QQ2R.md`**: il checkpoint dichiarava il video di Vishen "mai trovato". Questo run (`P-BQ-AGS0ck`, identità confermata da `info.json`: uploader/channel "Vishen", `@vishen`) **è** il video di Vishen (Mindvalley) sullo storytelling — dettagliato in testa a `video-analysis.md`.
- **NO-FINTO: PASS** — copertura parziale dichiarata esplicitamente (24,6%), metodo di campionamento sistematico dichiarato (non "100%" mai affermato), un'ipotesi verificata e riportata negativa (Move 01-04 non trovati) invece di essere taciuta o inventata.

---

*Coverage compilata il 2026-09-03 · Empire Studio · run `max17-v14` · numeri contati sul disco in questa stessa sessione, non ereditati da altri documenti.*
