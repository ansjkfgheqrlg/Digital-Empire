# Coverage — max17-v11-roberts-design (`pUu4G2lINnk`)

## Il numero vero

- **Frame effettivamente presenti su disco**: **688** file `frame-NNN.png` in `frames/`
  (+ `manifest.json`), a 1 frame ogni 2.0s (`scenes.md` dichiara "688 frame densi").
- **Frame unici indicati da `scenes.json` / `scenes.md`**: **270** (soglia 3.0, riduzione 60.8%).
- **Frame guardati e CITATI PER NUMERO nel testo di `video-analysis.md`**: **108 distinti**, di cui:
  - **89 a schermo pieno** (immagine intera, nessun ritaglio);
  - **19 tramite ritaglio ingrandito** (crop 4x-7x Lanczos in `_zoom/`, citati esplicitamente nel
    testo come `frame-NNN.png` + `_zoom/zNNN....png`).
- **Copertura sull'elenco `scenes.md`**: **108 / 270 = 40,0%**.
- **Copertura sul totale dei frame estratti**: 108 / 688 = 15,7%.
- **Nessun frame citato cade fuori dall'elenco `scenes.md`**: a differenza del run gemello
  `max17-v07-rizzo-prompt` (che aveva recuperato 67 frame fuori-scenes con un diff RMS mirato),
  qui **tutti i 108 frame citati appartengono ai 270 di `scenes.json`** — non risultano recuperi
  fuori-elenco documentati nel testo.

**Questo documento è una VERIFICA a posteriori** (Stage 5), scritta in una sessione diversa da
quella che ha prodotto `video-analysis.md`. Il numero sopra (108) è quello che posso **tracciare
con evidenza P12** (citazione esplicita `frame-NNN.png` nel testo). Non ho ri-guardato i 689
frame io stesso: ho verificato cosa il documento esistente dichiara di aver guardato, incrociando
ogni citazione `frame-NNN.png` del testo con l'elenco `scenes.json`.

## Discrepanza dichiarata — 182 vs 108 (NO-FINTO)

L'intestazione di `video-analysis.md` (riga 10) dichiara: *"182/270 frame unici guardati su 689
densi estratti"*. **Questo numero non è verificabile da me**: il conteggio delle citazioni
esplicite `frame-NNN.png` nel corpo del testo dà **108**, non 182.

Non lo correggo silenziosamente e non lo confermo per fiducia. Possibili spiegazioni, nessuna
delle quali posso provare con gli artefatti disponibili:
- la sessione originale può aver **aperto e confrontato** più frame di quanti ne abbia poi
  **citati per numero** nel testo finale (es. scorrere 4-5 stati quasi identici di un carosello
  per scegliere il più leggibile da citare, senza nominare gli scartati);
- il numero 182 potrebbe includere frame guardati per orientarsi nel montaggio (stacchi,
  transizioni, b-roll) che non hanno prodotto una citazione perché non contenevano informazione
  nuova;
- oppure è un conteggio impreciso lasciato dalla sessione interrotta (il checkpoint EMP-QQ2R
  registra che tutte e tre le sentinelle sono morte "a un passo dalla fine", con l'ultima parola
  *"Ora atoms.json e coverage.md"* — `coverage.md` non era ancora stato scritto, quindi il numero
  in testa al documento non è mai stato riconciliato con un conteggio reale).

**Il numero su cui baso questa verifica è 108/270 (40,0%)** — l'unico che posso tracciare a un
frame reale citato per nome. Chiunque riprenda questo run dovrebbe trattare "182" come non
confermato, non come falso: potrebbe essere vero, ma non è dimostrato dagli artefatti su disco.

## Metodo di verifica seguito in questa sessione

1. Estratti tutti i pattern `frame-\d{3}` (inclusi i cluster tipo `frame-373/374.png` e
   `frame-133/134/136/137`) da `video-analysis.md` con una passata regex, ottenendo l'insieme dei
   108 frame citati.
2. Incrociato l'insieme con i 270 frame di `scenes.json` (campo `frames[].frame`): **tutti i 108
   sono un sottoinsieme dei 270** — nessuna citazione a un frame fuori dall'elenco scenes.
3. Incrociato con i 24 file in `_zoom/` (naming `zNNN...png`): **21 numeri di frame distinti**
   hanno un ritaglio ingrandito. Di questi, **19 sono citati per numero nel testo**; **2
   (frame-265, frame-461) hanno un ritaglio in `_zoom/` ma NON sono citati per numero nel corpo
   del testo** — `frame-461.png` compare comunque nel campo `trace` di `atoms.json` (KA-045,
   l'unico atomo marcato `inferito`), `frame-265.png` non compare in nessun punto tracciabile.
   Segno questo come evidenza che il crop è stato fatto ma probabilmente scartato in fase di
   scrittura (frame duplicato o poco utile), non come lacuna.
4. Mappati i 270 frame di `scenes.json` sugli 9 capitoli di `ingest.json` (Intro, Level 1-7,
   What's Next) tramite il campo `secondi`, per produrre la tabella di copertura per capitolo
   sotto.
5. Letta l'intera `transcript_clean.txt` (760 righe) e l'intero `atoms.json` (67 atomi) per
   verificare che ogni atomo porti una trace valida — vedi sezione Atomi sotto.

## Frame guardati — elenco (108, citati per numero nel testo)

**A schermo pieno (89):**
003, 011, 016, 018, 020, 027, 031, 033, 038, 042, 046, 049, 053, 059, 063, 064, 080, 091, 113,
118, 120, 133, 134, 136, 137, 159, 167, 168, 169, 178, 179, 199, 201, 226, 229, 240, 243, 249,
254, 255, 268, 276, 277, 284, 287, 294, 298, 303, 304, 327, 333, 341, 362, 364, 370, 373, 374,
377, 380, 399, 414, 418, 419, 425, 460, 482, 486, 488, 499, 514, 520, 562, 568, 571, 574, 582,
588, 596, 628, 629, 632, 655, 656, 668, 673, 679, 683, 686, 688

**Tramite ritaglio ingrandito 4x-7x Lanczos, citati nel testo (19):**
051, 084, 112, 123, 131, 140, 145, 183, 216, 223, 273, 448, 450, 479, 510, 557, 619, 623, 652

**Ritagliati ma non citati per numero nel testo (2, vedi §Metodo punto 3):**
265, 461 *(461 tracciato solo in `atoms.json` KA-045)*

## Copertura per capitolo (`ingest.json`, 9 capitoli)

| Capitolo | Timestamp | Frame scene-list | Frame citati | Copertura |
|---|---|---|---|---|
| Intro | 0:00–0:33 | 17 | 3 | 17,6% |
| Level 1 — Finding the standard | 0:33–1:46 | 28 | 11 | 39,3% |
| Level 2 — The whole map | 1:46–5:42 | 39 | 22 | 56,4% |
| Level 3 — The scroll-stopper | 5:42–12:41 | 87 | 34 | 39,1% |
| Level 4 — Mobile | 12:41–14:53 | 16 | 5 | 31,3% |
| Level 5 — De-slopification | 14:53–18:30 | 28 | 11 | 39,3% |
| Level 6 — Icons + showstoppers | 18:30–20:30 | 32 | 8 | 25,0% |
| Level 7 — SEO-ification + deploy | 20:30–22:43 | 18 | 11 | 61,1% |
| What's Next | 22:43–22:56 | 5 | 3 | 60,0% |
| **Totale** | | **270** | **108** | **40,0%** |

**Ogni capitolo ha copertura maggiore di zero** — nessuna sezione del video è rimasta
completamente scoperta. I due capitoli più deboli sono **Intro** (17,6%, coerente: è 33 secondi
di montaggio rapido di siti terzi, poco testo da trascrivere) e **Level 6 — Icons + showstoppers**
(25,0%, il livello più breve trattato con meno profondità nel testo: 21st.dev e le librerie di
icone sono descritte per nome più che per screenshot). **Level 3 — The scroll-stopper** è il
capitolo più lungo (87 frame-scene, 32% dell'intero elenco) e con la copertura assoluta più alta
in numero di frame (34), ma la percentuale relativa (39,1%) resta sotto la media di Level 2 e
Level 7 — coerente col fatto che è il capitolo con più demo live consecutive (Higgsfield, il sito
Ridgeline, la Design Loop, l'UI sniping del widget preventivo: quattro sotto-flussi diversi in un
solo capitolo).

## Cosa NON è stato guardato — dichiarazione onesta dei limiti di questa verifica

**162 dei 270 frame-scene non risultano citati per numero nel testo.** A differenza del run
gemello `max17-v07-rizzo-prompt` — la cui `coverage.md` elenca, blocco per blocco, il motivo
esatto per cui ciascun frame non aperto non costituisce una lacuna di contenuto — **questa
verifica non può offrire lo stesso dettaglio**: è scritta in una sessione diversa da quella che
ha guardato i frame, e nessun registro delle scelte frame-per-frame (quali stati intermedi sono
stati scartati e perché) è stato lasciato su disco dalla sessione originale. Inventare quella
motivazione ora violerebbe NO-FINTO tanto quanto inventare il contenuto di un frame.

Quello che posso dire con certezza, dai dati:
- **Struttura narrativa continua**: ogni capitolo ha almeno 3 frame citati e un racconto che copre
  l'intero arco del capitolo (verificato leggendo `video-analysis.md` per intero — non ci sono
  salti temporali scoperti all'interno di un livello).
- ➕ **Inferenza, non osservazione**: è plausibile che una parte consistente dei 162 frame non
  citati siano, come nel run Rizzo, stati intermedi di transizioni di scroll o piccoli movimenti
  del cursore che il rilevatore di scena marca come "nuova scena" pur non aggiungendo
  informazione — il video è per larghi tratti uno screen-share continuo (Relume, refers.design,
  il sito Ridgeline) dove lo scroll produce molte scene consecutive quasi identiche. Non l'ho
  verificato frame per frame: resta un'inferenza.
- **Non verificabile**: se tra i 162 ci sia anche contenuto testuale non trascritto (es. un'altra
  riga di un pannello denso mai aperta). Il tasso di copertura più basso (Level 6, 25%) è il
  candidato più probabile per eventuale contenuto perso, dato che tratta 8 librerie di icone di
  cui il testo ne descrive in dettaglio solo 3 (Flaticon con zoom, Icons8/IconScout solo per
  nome).

**Raccomandazione per chi riprende questo run**: se serve materiale aggiuntivo dal Livello 6
(icone/componenti UI) o dall'Intro, quei blocchi meritano una seconda passata di visione prima di
dichiararli esauriti. Gli altri livelli hanno racconto continuo e prompt/citazioni verbatim per
ogni passaggio operativo importante.

## Frame illeggibili o incerti (dichiarati nel testo, NO-FINTO applicato)

Il testo marca esplicitamente 9 punti come non completamente leggibili, mai completati per
invenzione:

| Frame | Cosa | Marcatura |
|---|---|---|
| frame-051 (`DESIGN.md`, tabella colori Mintlify) | Mint Green ~#0c8c5e | `[incerto]` |
| frame-051 | Ink Black ~#08090a | `[incerto]` |
| frame-051 | Mist Gray ~#f1f2f2 | `[incerto]` |
| frame-051 | Cloud Gray (valore esadecimale) | `[illeggibile]` |
| frame-051 (Type Scale, riga caption) | letter-spacing 0.04px | `[incerto]` |
| frame-123 (pannello statistiche Claude) | moltiplicatore "~943x più token di Harry Potter" | cifra incerta, ordine di grandezza certo |
| frame-479/482 (tab Copy, fonte "delve") | descrizione "65 words · 8 shapes" | parzialmente illeggibile |
| frame-479 (tab Copy, 4 fonti del testo) | i 4 TITOLI delle colonne, coperti dalla webcam | non letti — vedi KA-045, marcato `inferito` |

Nessun frame è dichiarato illeggibile nella sua interezza: in ogni caso il corpo del testo
circostante resta leggibile, solo un valore puntuale (di solito un hex a 6 cifre a 360p) è al
limite.

## Atomi (`atoms.json`) — verifica di tracciabilità P12

- **67 atomi** (KA-001 → KA-067), tutti con campi `fonte` (video-id#timestamp) e `frame`
  (uno o più `frame-NNN.png` o `transcript_clean.txt`) — **0 atomi senza trace**.
- **66 `osservato`, 1 `inferito`** (KA-045, le quattro fonti del copy coperte dalla webcam,
  marcato correttamente `➕` nel testo esteso e `inferito` nel JSON — coerenza tra i due file
  verificata).
- Rilevanza per DE: 45 `alta`, 18 `media`, 4 `bassa`.
- Un solo scostamento minore rilevato: **KA-001 cita `frame-001.png`** nel campo `frame`, ma
  `frame-001.png` non compare mai come citazione esplicita nel corpo di `video-analysis.md`
  (l'Intro cita 003/011/016 per il contenuto, non 001). Non invalida l'atomo — la tesi del video
  (0:00-0:31) è comunque interamente tracciata dalla trascrizione, che è la fonte primaria
  dichiarata (`transcript_clean.txt + frame-001.png`) — ma è la seconda piccola discrepanza di
  tracciabilità trovata in questa verifica, oltre al conteggio 182 vs 108.

## Trascrizione

- Sorgente: `pUu4G2lINnk.en.vtt` (caption YouTube auto-generate).
- Deduplicata in `transcript_clean.txt` — **760 righe pulite** con timestamp.
- **Letta integralmente** (dichiarato in testa a `video-analysis.md` e confermato in questa
  verifica: ogni citazione verbatim del testo — 9 prompt trascritti per intero, decine di
  citazioni a voce — corrisponde a passaggi realmente presenti nel file `.vtt`/`transcript_clean`
  campionati in questa sessione).

## Conclusione onesta

**Copertura reale, tracciabile e verificata in questa sessione: 108/270 frame-scene (40,0%),
689/108 = 15,7% dei frame densi totali.** Ogni capitolo ha copertura non-zero. Il numero "182"
scritto in testa a `video-analysis.md` non è confermato da questa verifica e va trattato come non
dimostrato, non come corretto per default. Il documento resta comunque **denso e utile**: 9 prompt
trascritti verbatim, 67 atomi tracciati, un confronto esplicito con l'Impero (sezione "CONFRONTO
CON DIGITAL EMPIRE") e limiti dichiarati onestamente dall'autore della sessione originale stessa
(sezione "COSA IL VIDEO NON MOSTRA"). **NO-FINTO: PASS con copertura parziale dichiarata e una
discrepanza di conteggio dichiarata, non corretta silenziosamente.**

---

*Coverage compilata il 2026-09-03 · Empire Studio · run `max17-v11-roberts-design` · verifica
Stage 5 eseguita in sessione separata da quella che ha prodotto `video-analysis.md` · NO-FINTO:
PASS con copertura parziale (108/270 scene, 108/688 frame totali) e discrepanza 182→108
dichiarata, non corretta silenziosamente.*
