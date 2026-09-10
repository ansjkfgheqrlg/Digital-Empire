# Reference — Controllo leggibilita' di una copertina (thumbnail_analyzer.py)

> Conoscenza on-demand per `thumbnail-designer`, e per Max stesso. Fonte: verifica diretta di
> `scripts/thumbnail_analyzer.py` (2026-09-10).

## Cosa NON e'
Non e' un gate automatico e non e' agganciato a nessuna catena di produzione. **La copertina la
fa Max a mano, sempre** (regola permanente, 2026-08-29/2026-09-04) — `produci_video_completo.py`
non genera copertine e non le giudica. `thumbnail_analyzer.py` non parte da solo in nessun punto
della fabbrica: prima di questa nota era citato nel playbook di `thumbnail-designer.md` ma
**zero occorrenze reali** lo invocavano (verificato con grep su tutta la fabbrica).

## Cosa E'
Un controllo **su richiesta**, da lanciare a mano su un file che Max ha gia' fatto, per sapere
se si legge anche in miniatura piccola — prima di metterlo in `VIDEO-PRONTI/video-NN/` o prima
dell'upload. Un consiglio che Max puo' chiedere, non un giudice che si mette in mezzo.

## Uso
```
python thumbnail_analyzer.py --image "VIDEO-PRONTI/video-07/copertina.png"
```
Con Pillow non installato (o su qualunque errore di lettura del file) degrada da solo
all'analisi Mock (`--mock` forza questo ramo anche con Pillow presente) — non fallisce mai in
modo rumoroso, restituisce sempre un JSON.

## Output e come leggerlo
```json
{
  "status": "success",
  "brightness": 65.2,          // 0-100, luminosita' media (100 = tutto bianco)
  "contrast": 74.8,            // 0-100, deviazione standard normalizzata
  "dominant_colors": ["#..."],
  "text_readability_score": 85.0,
  "is_readable": true,
  "notes": ["..."]
}
```
- `is_readable` = `True` solo se **luminosita' fra 40 e 220 (su scala 0-255 interna, ~15.7-86.3
  su scala 0-100)** *e* **contrasto >= 30 (su scala 0-255 interna, ~23.4 su scala 0-100)**.
- `notes` spiega in italiano cosa correggere (troppo scura/chiara, poco contrasto).
- `dominant_colors` sul ramo reale e' un solo colore, preso dal pixel medio dell'immagine
  ridotta a 1x1 — un'euristica dichiarata "mocked per semplicita'" nel codice, non un vero
  color-extraction: utile come indicazione di massima, non come dato preciso.

## Limite dichiarato
Misura **luminosita' e contrasto globali** dell'immagine, non "se il testo si legge" in senso
stretto (non fa OCR, non isola la zona del testo dal resto della scena). E' un indicatore
rapido, non una certificazione — in caso di dubbio la lettura ad occhio in una miniatura di
prova (Max, o `youtube_hunter_playwright.py`/Video IQ in scala reale) resta il giudice finale.

## Connessioni
- `03-AGENTI-E-RUOLI/operatori/thumbnail-designer.md` — playbook che lo cita come strumento
  facoltativo di verifica finale.
- `04-SKILLS-E-REFERENCE/references/scelta-strumenti.md` — perche' Arena (generazione
  automatica) e' spenta e la copertina resta manuale.
