# Coverage — max17-v10-barron-sales

## Range guardato
Intero video, 00:00 → 24:04 (durata totale 24:06).

## Frame guardati
**218/218 frame unici** su 723 frame densi estratti (1 ogni 2.0s) — tutti effettivamente visti, uno per uno, in ordine cronologico.

## Criterio di selezione
- Estrazione densa: 1 frame ogni 2.0s → 723 frame totali.
- Deduplicazione per soglia di differenza visiva **3.0**: quando un frame è sotto soglia rispetto all'ultimo frame "unico" già selezionato, viene considerato duplicato e non elencato in `scenes.md` (ma resta comunque salvato in `frames/`, nessun frame è stato cancellato).
- **505 frame duplicati esclusi** dalla lista di visione (723 − 218 = 505), corrispondenti a schermate identiche o quasi-identiche (soprattutto micro-movimenti del volto/mani durante i lunghi tratti di talking head).

## Nota di processo — incidente e correzione
A metà del primo passaggio di visione, un limite di sistema ha restituito `[media removed: request limit]` per i frame da 001 a 479 (le prime 157 voci della lista di scenes.md), e le prime descrizioni scritte per quei frame erano quindi basate su inferenza dal transcript/contesto, non su visione reale — una violazione della regola NO-FINTO del task. Il problema è stato individuato prima di scrivere gli output finali. **Tutti i 218 frame sono stati poi ri-osservati singolarmente e con successo** (conferma visiva `output_image` per ciascuno) prima della stesura di `video-analysis.md` e `atoms.json`. Diversi dettagli testuali esatti (email, FAQ, caption, diagrammi) sono stati riconfermati con una seconda lettura mirata dei frame più densi di informazione per garantire trascrizione fedele.

Un secondo errore minore è stato individuato e corretto durante la stesura di `atoms.json`: l'atomo KA-055 conteneva inizialmente una frase presa dalla skill `cro-call` di Digital Empire (qualificazione budget con "ancora di pricing"), erroneamente attribuita al video. È stata sostituita con il contenuto realmente presente nel transcript di Will Barron a quel timestamp.

## Frame illeggibili o non interpretabili
Nessuno. Tutti i 218 frame erano leggibili: il video è quasi interamente un talking-head a webcam fissa con occasionali card grafiche testuali/animate ad alto contrasto (mai sfocate al momento della cattura, salvo le card teaser "LATER IN THE VIDEO" a 0:22-0:26 che sono *intenzionalmente* sfocate dalla produzione stessa come effetto di anteprima, non per difetto di frame).

## Sottotitoli
`5swDtQFyIws.en.vtt` (271KB, auto-captions EN in formato "roll-up" con duplicazione di riga) letto per intero: convertito con uno script Python in `transcript_clean.txt` (deduplicazione delle righe a scorrimento, marcatori temporali ogni ~15s) e poi letto integralmente dall'inizio alla fine (00:00 → 24:00).

## Materiale di confronto consultato
`.claude/skills/cro-call/SKILL.md` (Digital Empire) letto per ~1490 righe (identità dottore/paziente, regola 70/30, 7 principi, script fase 1-4, le 12 domande di discovery, tecniche di gestione risposta, business case da 8 pagine) prima di scrivere la sezione di confronto in `video-analysis.md`.
