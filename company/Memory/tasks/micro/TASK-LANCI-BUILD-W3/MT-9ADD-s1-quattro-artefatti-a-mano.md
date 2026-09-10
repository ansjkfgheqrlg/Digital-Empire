# MT-9ADD — S1 - i quattro artefatti del Manuale compilati a mano fino alla firma

- **Padre:** TASK-LANCI-BUILD-W3
- **Data:** 2026-09-09
- **Ordine:** 5

## Cosa fa

S1, il primo lancio a mano fino alla firma. Quattro artefatti del Manuale compilati a
mano e validati contro gli schemi che gia' esistono:

| # | Artefatto | Come | Ore |
|---|---|---|---|
| 1 | `pubblico.json` | canale per canale, con la prova di ogni numero | 2-4 |
| 2 | `certificato.json` retroattivo | sei bandiere rosse, link testati, `debito_collaudo` dichiarato | 1-2 |
| 3 | `previsione.json` | la formula del documento 02, rifatta su un foglio | 1-2 |
| 4 | `offerta.json` | fasi O1-O5 del documento 03, fino alla firma | 1-2 |

**Questo scaglione e' il collaudo vero del piano**: se compilare quattro file a mano
seguendo gli schemi risulta impossibile o assurdo, il difetto e' negli schemi, e si scopre
qui dove costa ore invece che dentro il codice dove costa giorni.

La firma su prezzo e data e' di Max. Per ADR-026 si chiede il giorno stesso in cui serve,
non si aspetta in silenzio.

## Gate di chiusura

I quattro file passano la validazione contro i propri schemi, **e** c'e' la firma vera di Max su un prezzo e una data.

## Output

## Stato

**Compilata il 2026-09-10.** Tre artefatti su quattro validi contro i propri schemi (`pubblico.json`, `certificato.json`, `previsione.json`). Il quarto e' `offerta.PROPOSTA.json` e fallisce su un solo campo: `firma`, che nessun agente puo' scrivere (INV-10). **Resta aperta in attesa della firma di Max sul prezzo.**

Esito del collaudo: **il lancio non passa S1.** Pubblico raggiungibile verificato **0**, ricavo atteso **0 EUR** in tutti e tre gli scenari, certificato **non-consegnabile** con 4 bandiere rosse su 6. Dettaglio in `company/Ecosistemi/15-LANCI/lanci/manuale-claude-code/LEGGIMI.md`.
