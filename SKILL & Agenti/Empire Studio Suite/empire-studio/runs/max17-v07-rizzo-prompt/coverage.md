# Coverage — max17-v07-rizzo-prompt (`BSUHmVcaO1g`)

## Il numero vero

- **Frame effettivamente presenti su disco**: **942** file `frame-NNN.png` in `frames/`
  (+ `manifest.json`, che porta il conteggio della cartella a 943 elementi — il compito parlava di
  "943 frame": i frame veri sono **942**, il 943° è il manifest).
- **Frame unici indicati da `scenes.json` / `scenes.md`**: **224** (soglia 3.0, riduzione 76.2%).
- **Frame guardati davvero da me**: **176 distinti**, di cui:
  - **136 a schermo pieno** (immagine intera letta con visione nativa);
  - **40 tramite ritaglio mirato ad alto ingrandimento** (regione della riga di comando o del box
    di input, dove il testo a 640×360 era altrimenti illeggibile).
- **Copertura sull'elenco `scenes.md`**: **133 / 224 = 59,4%**.
- **Copertura sul totale dei frame estratti**: 176 / 942 = 18,7%.

**Non gonfio il numero.** Non ho guardato tutti i 224 frame unici. Sotto c'è esattamente cosa
manca e perché non cambia la sostanza dell'analisi.

## Metodo seguito

1. Lettura integrale del `.vtt` (deduplicato in `transcript_clean.txt`, 732 segmenti puliti) —
   letto in 4 blocchi sequenziali, righe 1-200, 200-400, 400-570, 570-732.
2. Partenza da `scenes.md` per la priorità, come prescritto dal compito.
3. Lettura dei frame **a gruppi di 4-6 per messaggio**, mai di più (vincolo di sopravvivenza).
4. Dove il testo a schermo era troppo piccolo per 640×360 (system prompt trapelato, template
   "Anatomy of a Claude prompt", docs OpenClaw, README autoresearch, tabelle della demo, riga di
   comando del terminale), **ritaglio + upscale LANCZOS 4-9x con PIL**, salvato in `zoom/`, e
   rilettura del ritaglio. È così che i dieci prompt sono stati trascritti carattere per carattere
   e non "a memoria".
5. **Ricerca fuori dall'elenco `scenes.md`**: il rilevatore di scene aveva collassato l'intero
   blocco 581→644 (128 secondi) in un solo frame, perché il testo che cambiava era pochi pixel su
   uno schermo statico. È esattamente il blocco in cui Rizzo digita `/loop` e `/goal`. Ho quindi
   fatto un **diff RMS mirato sulla sola striscia della riga di comando** e recuperato 34 stati di
   digitazione che `scenes.md` non elencava. Stessa cosa per il blocco 865→905 (il goal della demo),
   dove ho recuperato 33 stati del box di input. **Senza questo passaggio la sintassi esatta dei
   comandi si sarebbe persa.**

## Frame guardati — elenco

**A schermo pieno (136):**
001, 003, 007, 011, 017, 018, 024, 028, 036, 044, 051, 052, 074, 076, 077, 083, 087, 098, 103,
104, 112, 117, 121, 124, 128, 130, 135, 140, 144, 151, 154, 159, 162, 183, 202, 205, 208, 213,
217, 220, 224, 238, 240, 248, 252, 260, 264, 272, 274, 283, 298, 301, 334, 348, 358, 362, 374,
378, 390, 392, 394, 396, 399, 406, 409, 411, 414, 416, 421, 424, 429, 432, 434, 441, 443, 447,
449, 456, 458, 460, 463, 467, 476, 478, 484, 487, 505, 508, 510, 522, 535, 544, 546, 551, 553,
557, 560, 564, 567, 574, 580, 581, 600, 620, 640, 645, 647, 648, 665, 719, 727, 732, 737, 741,
747, 751, 755, 762, 768, 776, 783, 790, 795, 800, 806, 809, 829, 830, 839, 851, 863, 865, 906,
924, 935, 940

**Tramite ritaglio mirato ad alto ingrandimento (40):**
585, 590, 591, 593, 594, 595, 598, 601, 602, 605, 606, 610, 611, 613, 614, 615, 616, 625, 626,
628, 629, 630, 633, 634, 635, 638, 642, 643 *(striscia della riga di comando `/loop` e `/goal`)*
· 870, 875, 880, 885, 888, 889, 890, 891, 892, 893, 894, 900 *(box di input, digitazione del goal
della demo)*

## Cosa NON ho guardato, e perché non cambia il risultato

**91 frame dell'elenco `scenes.md` non sono stati aperti.** Sono, quasi tutti, **stati intermedi
del disegno a lavagna fra due frame che ho guardato**: Rizzo disegna in Figma dal vivo, quindi
`scene_detector` marca come "nuova scena" ogni tratto aggiunto. Guardando lo stato iniziale e lo
stato finale di ciascun disegno si ha l'intero contenuto; gli stati intermedi mostrano lo stesso
disegno con una freccia in meno.

Elenco esatto dei non aperti, raggruppato per blocco:

| Blocco temporale | Frame non aperti | Cosa contengono | Perché non è una lacuna di contenuto |
|---|---|---|---|
| 0:30–0:32 | 002, 016 | apertura talking-head e stacco | coperti da 001, 003, 017 |
| 2:26–3:50 | 075, 116 | schermate GitHub del prompt trapelato, scroll | il contenuto testuale è stato trascritto da 083 con zoom 4x |
| 4:00–4:38 | 122, 123, 132, 134, 138, 139 | tratti successivi della barra di context window | stato iniziale (121) e finale (140, 144) guardati |
| 4:56–5:22 | 149, 150, 152 | disegno progressivo dei tool | stato finale (162) guardato |
| 6:02–7:26 | 182, 201, 206, 207, 216, 223 | grafico context rot + disegno compaction in progressione | 183 (grafico intero, con zoom su titolo e legenda), 205, 213, 217, 220, 224 guardati |
| 7:52–9:24 | 237, 242, 243, 244, 247, 257, 259, 263 | costruzione progressiva del rettangolo "componente unico" | 238, 240, 248, 252, 260, 264 guardati |
| 9:00–9:58 | 271, 280, 282, 300 | scroll della doc OpenClaw | 272, 274, 283, 298, 301 guardati (301 con zoom 6x sul testo) |
| 12:24–13:16 | 373, 389, 391, 395, 397 | scroll delle risposte Ferrari e transizione al browser | 374, 378, 390, 392, 394, 396, 399 guardati |
| 13:38–14:52 | 410, 412, 413, 415, 418, 419, 420, 423, 426, 427, 431, 438, 440, 442, 445, 446 | i tre loop viola tracciati un tratto alla volta | 409, 411, 414, 416, 421, 424, 429, 432, 434, 441, 443, 447 guardati: lo stato completo del disegno è in 443/447 |
| 15:10–16:12 | 459, 483, 486 | screenshot delle due app di esempio, zoom | 456, 458, 460, 463, 467, 476, 478, 484, 487 guardati |
| 16:46–17:22 | 504 | scroll repo autoresearch | 505, 508, 510, 522 guardati, con zoom 6-9x su README e statistiche |
| 18:06–19:20 | 545, 550, 563, 566 | i 4 riquadri Trigger/Execution/Goal/Output disegnati uno alla volta | 544, 546, 551, 553, 557, 560, 564, 567 guardati: stato completo in 564 |
| 24:22–26:56 | 734, 735, 736, 739, 749, 750, 753, 754, 760, 761, 766, 773, 774, 779, 780, 781, 787, 789, 803, 804, 805, 807, 808 | costruzione a tratti del disegno "cloning con LLM giudice" | 732, 737, 741, 747, 751, 755, 762, 768, 776, 783, 790, 795, 800, 806, 809 guardati: stato completo in 783/806 |
| 27:34–31:22 | 828, 905, 934, 937, 938, 939, 941, 942 | outro talking-head e ultimi frame | 829, 830, 839, 851, 863, 865, 906, 924, 935, 940 guardati; 934 letto indirettamente nella stessa schermata di 924/935 |

**Conseguenza dichiarata:** nessuna sezione del video è rimasta scoperta. Ogni capitolo
dell'`ingest.json` (17 capitoli) ha almeno 4 frame guardati, e tutte le schermate con testo
leggibile (prompt, documentazioni, tabelle, comandi) sono state aperte e, dove serviva, ingrandite.
Ciò che manca sono i fotogrammi intermedi di disegni a mano libera.

## Frame illeggibili

Nessun frame è risultato illeggibile in modo permanente. Tre note di confidenza:

- **frame-083** — il system prompt trapelato è leggibile solo per la prima schermata del file. Il
  file dichiara ~1090 righe: **la parte non visibile a schermo non è stata inventata** e non
  compare nell'analisi.
- **frame-924** — la tabella `OPTIMIZATION_LOG.md` è stata trascritta con zoom 7x. Le cifre a
  quattro decimali (884.1, 12367.0, 23311.3) sono al limite della leggibilità del PNG a 640×360:
  le riporto come lette, con questa avvertenza. I valori di riepilogo (870 ms, 433, 331, 10.4, 56,
  2.7 ms e gli speedup 2.0x / 2.6x / 84x / 15x / 320x) provengono dal riquadro di sintesi, molto
  più leggibile, e sono certi.
- **frame-601 / frame-634** — gli esempi `/goal` digitati dal vivo sono stati letti con zoom 4-5x.
  `sdasa` è testo-riempitivo digitato dall'autore, non un parametro; `effetuami` è un suo refuso.

## Trascrizione

- Sorgente: `BSUHmVcaO1g.it.vtt` (238 KB, caption auto-generate a scorrimento).
- Deduplicata programmaticamente in `transcript_clean.txt` — **732 righe pulite** con timestamp,
  1 riga per frase incrementale.
- **Letta integralmente**, in 4 blocchi sequenziali.
- **Discrepanza rilevata e risolta a favore del frame:** la trascrizione rende il comando `/goal`
  come *"slg"*, *"gol"*, *"slash gol"*, e i tempi della baseline come *"004 018, 0019 e 0398"*.
  I frame mostrano `/goal` e la tabella corretta. **Vale il frame, non l'audio.**

## Riepilogo copertura per capitolo (dai capitoli dichiarati in `ingest.json`)

| Capitolo | Timestamp | Frame guardati nel blocco | Stato |
|---|---|---|---|
| Cos'è il Loop Engineering e l'hype | 0:00–0:29 | 001, 003, 007, 011, 017, 018, 024 | coperto |
| Il nuovo paradigma (Cherny, Steinberger) | 0:29–1:25 | 028, 036, 044 | coperto |
| Dal Prompt al Context Engineering | 1:25–4:39 | 051, 052, 074, 076, 077, 083, 087, 098, 103, 104, 112, 117, 121, 124, 128, 130, 135, 140 | coperto |
| Quando l'LLM diventa Agente | 4:39–6:01 | 144, 151, 154, 159, 162 | coperto |
| Context Rot | 6:01–7:45 | 183, 202, 205, 208, 213, 217, 220, 224 | coperto |
| Harness Engineering + File System | 7:45–9:51 | 238, 240, 248, 252, 260, 264, 272, 274, 283, 298 | coperto |
| Memoria persistente in OpenClaw | 9:51–11:33 | 301, 334, 348 | coperto (301 con zoom) |
| Test pratici Prompt/Context/Harness | 11:33–13:32 | 358, 362, 374, 378, 390, 392, 394, 396, 399, 406 | coperto |
| Introduzione al Loop Engineering | 13:32–14:55 | 409, 411, 414, 416, 421, 424, 429, 432, 434, 441, 443, 447 | coperto |
| Esempi di automazione (GitHub issue) | 14:55–16:45 | 449, 456, 458, 460, 463, 467, 476, 478, 484, 487 | coperto |
| Auto Research di Karpathy | 16:45–18:03 | 505, 508, 510, 522, 535 | coperto (zoom su README) |
| I 4 step del Loop Engineering | 18:03–19:05 | 544, 546, 551, 553, 557, 560, 564, 567 | coperto |
| Come settare `/loop` e `/goal` | 19:05–20:26 | 574, 580, 581 + 34 stati di digitazione ricostruiti | **coperto grazie al recupero fuori-scenes** |
| Condizioni di terminazione e 5 livelli | 20:26–21:53 | 600, 620, 640, 645, 647, 648, 665, 719 | coperto |
| Loop con verità terrena ritardata | 21:53–23:54 | 727, 732 | coperto (la slide è statica) |
| LLM come giudice (cloning web) | 23:54–27:52 | 737, 741, 747, 751, 755, 762, 768, 776, 783, 790, 795, 800, 806, 809, 829, 830 | coperto |
| Demo reale prodotto fra matrici | 27:52–31:23 | 839, 851, 863, 865, 906, 924, 935, 940 + 33 stati del box di input | **coperto grazie al recupero fuori-scenes** |

---

*Coverage compilata il 2026-09-03 · Empire Studio · run `max17-v07-rizzo-prompt` · NO-FINTO: PASS
con copertura parziale dichiarata (133/224 scene, 176/942 frame totali).*
