# Frame scelti — A6/L06 «Automazione della pubblicazione Video su YouTube»

27 frame unici disponibili (dedup 88,1%), tutorial a schermo condiviso su YouTube Studio.
Guardati **7 su 27** — apertura, caricamento multiplo, e i frame che mostrano lo stato
"Programmato" nell'elenco contenuti (la prova che la funzione dimostrata è quella nativa).

| # | frame | ts | perché guardato |
|---|---|---|---|
| 1 | `frame-005.png` | 0:08 | apertura, contesto del canale usato per la demo |
| 2 | `frame-052.png` | 1:42 | ⭐ finestra "Caricamento di 2 su 4" — upload multiplo, video in coda |
| 3 | `frame-111.png` | 3:40 | elenco contenuti prima della programmazione, per confronto |
| 4 | `frame-125.png` | 4:08 | ⭐⭐ elenco Contenuti con righe in stato "Programmato", data visibile |
| 5 | `frame-140.png` | 4:38 | ⭐ conferma: due video programmati, date diverse, stesso schema |
| 6 | `frame-170.png` | 5:38 | controllo presidio, schermo stabile durante la spiegazione orale |
| 7 | `frame-224.png` | 7:26 | chiusura/transizione |

## Perché contano frame-125 e frame-140

Sono la prova diretta che la funzione dimostrata è lo scheduling **nativo** di YouTube Studio
(colonna "Visibilità" → stato "Programmato" con data), non uno strumento di terze parti. Questo è
rilevante per la regola estratta: la fabbrica può ottenere questa funzionalità senza integrare
nulla di nuovo, semplicemente cambiando cosa fa `youtube_uploader_playwright.py` nello step
Visibilità (oggi imposta sempre "Privato").
