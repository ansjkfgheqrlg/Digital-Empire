---
Type: CONCEPT
Status: Active
Tags: #brand #ccm #design-system #guidelines #lancio #grana #competitor
Created: 2026-09-03
Last updated: 2026-09-03
---

# CCM Brand Guidelines — il sistema visivo e verbale del lancio

## Overview

Documento normativo di **Claude Code Mastery** in 18 pagine A4, 15 capitoli. Non è un catalogo di gusti: ogni capitolo chiude con un blocco **"Come si verifica"**, e nessuna regola è entrata nel documento se non era controllabile a occhio o col contagocce.

**Dove vive:** `company/02-info-business/ccm/brand/`
**Il file:** `CCM-Brand-Guidelines.pdf` (18 pagine, 0,88 MB)
**Si rigenera con:** `python build_brand_guidelines.py`

---

## La tesi, ed è la ragione per cui il documento esiste

Il 2 settembre 2026 abbiamo misurato dal DOM (non stimato da screenshot) il sito di `claude-speedrun.com`, concorrente diretto di CCM. Il risultato:

| Elemento | CCM | claude-speedrun |
|---|---|---|
| Colore d'azione | `#fb4604` | `#fb4604` — **identico** |
| Carattere | Onest | Onest — **identico**, 366 usi |
| Raggio bottoni | 12px | 12px — **identico**, 56 usi |
| Raggio pillole | 9999px | 9999px — **identico**, 65 usi |
| Fondo scuro | `#1c1c1c` | `#131313` |
| **Famiglia argento** | **Tre gradienti costruiti** | **Assente** |

Non è somiglianza: è lo stesso sistema visivo. Da qui la decisione che vincola ogni pagina del documento:

> **L'arancione smette di essere la nostra identità e resta il colore dell'azione. L'argento su fondo inchiostro diventa la firma.**

Test operativo: coprire il logo e mostrare un nostro pezzo accanto a uno loro. Se nessuno sa dire quale è nostro, il pezzo non rispetta le guidelines.

---

## Le regole che vincolano ogni pezzo

- **Arancione ≤ 10% dell'area.** Ammesso su: bottone d'azione, occhiello, **una** parola per titolo, il numero di un dato, il punto dentro una pillola argento. Mai come fascia a piena larghezza (è la mossa del concorrente), mai sulla parola "Claude".
- **Otto colori, nessun nono.** Quattro opacità ammesse: 90% · 75% · 60% · 30%.
- **Un heading per pagina/slide/schermata.**
- **Nessuna linea di separazione:** lo stacco si fa con lo spazio.
- **Il gradiente argento solo sui titoli** sopra i 24px, mai nel corpo del testo.
- **Il corsivo è riservato** alla parola in argento-arancione.
- **Da due a tre inversioni di fondo** in una pagina lunga, non una a sezione.
- **Lista nera di parole:** rivoluzionario, definitivo, segreto, hack, guru, trucco, illimitato, garantito.

---

## La grana — capitolo 11, e non è un dettaglio tecnico

Due strati sempre attivi: **`0.55` in overlay + `0.28` in hard-light**. Due e non uno: il primo dà il corpo, il secondo rompe la regolarità del primo (con uno solo si vede il reticolo e sembra un filtro).

**Il confronto è misurato, non asserito.** Gli altri la texture ce l'hanno, ma sussurrata: il concorrente diretto usa un **reticolo appena percettibile** sulle sezioni scure, il sito hub di Andrei Pascu una **mezzatinta a punti quasi invisibile**. Sono scelte difensive.

> **Loro la nascondono, noi la dichiariamo.** È la sola parte del sistema che nessuno può copiarci per sbaglio, perché copiarla richiede di decidere che il rumore è un pregio.

Le quattro regole: non si spegne mai · scende al 13% sotto il testo piccolo · **in stampa è un PNG ripetuto, mai un filtro SVG** (Chromium lo rasterizza e il file supera i 16 MB) · non va sopra i volti né sopra uno screenshot di codice.

---

## Struttura del documento

Copertina · Indice · **01** Perché queste linee esistono · **02** La marca in una frase · **03** Il nome e la firma · **04** La voce · **05** Colore: il sistema · **06** La regola dell'arancione · **07** L'argento è la firma · **08** Tipografia · **09** I componenti · **10** Superfici · **11** La grana · **12** Le applicazioni del lancio · **13** Il confronto misurato · **14** Cosa non facciamo · **15** Checklist di conformità · Colophon

---

## Da dove vengono i valori

**Nessun valore è inventato.**

- Colori, raggi, gradienti, componenti → `Lancio corso skill beast/Leanding Page CCM/ccm-premium/src/app/globals.css`
- Dati del concorrente → `competitor/Andrei Pascu/site-study/capture/07-claude-speedrun/design-tokens.json`

Quando cambia una delle due fonti, il documento va rigenerato.

## Metodo di produzione (riusabile)

HTML + Chromium `page.pdf()` via Playwright. Contenuto in `content.py`, motore in `build_brand_guidelines.py`: si cambia il copy senza toccare la grafica. Verifica automatica del riempimento pagina (fondo dell'ultimo elemento contro il margine utile) — alla consegna **18 su 18 in norma**.

## Connessioni

- [[Concept_Digital_Empire_Design_System]]
- [[Source_Andrei_Pascu_Claude_Speedrun]]
- [[Project_Lancio_CCM]]
- [[Concept_APSOC_Framework]]
- [[Concept_Guardrail_Che_Si_Fanno_Rispettare]]
