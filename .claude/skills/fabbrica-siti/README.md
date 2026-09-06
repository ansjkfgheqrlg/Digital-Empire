# FABBRICA SITI — Digital Empire

Il sistema unico per produrre qualunque sito o landing page dell'Impero.
Una legge, un canone, due corsie.

**Non è ancora invocabile come skill.** La Fase 3 (`SKILL.md` + i 9 passi) è aperta — vedi lo stato
sotto. Quello che c'è oggi è già usabile a mano: la legge si legge, il canone si importa.

---

## Cosa c'è, oggi

```
fabbrica-siti/
├── CLAUDE-SITI.md          ← LA LEGGE. 10 articoli numerati e citabili. Si legge per prima.
├── canone/
│   ├── canone.css          ← i valori, per il browser. Lo importano tutte e due le corsie.
│   └── canone.json         ← gemello a macchina, lo leggerà gate_siti.py
├── scripts/
│   └── canone_sync.py      ← verifica che i due canoni non divergano. PASS al 2026-09-06.
└── README.md               ← questo file
```

---

## Come si usa adesso

**Corsia A — pagina vanilla**
```html
<link rel="stylesheet" href="canone.css">
<body class="grain-fine">
  <div class="page"> … </div>
</body>
```

**Corsia B — Next.js 16 + Tailwind v4**
```css
/* src/app/globals.css */
@import "./canone.css";
@import "tailwindcss";
```

**Prima di consegnare**
```bash
python .claude/skills/fabbrica-siti/scripts/canone_sync.py
```

---

## Le due corsie in una riga

> **≤ 3 pagine e nessuno stato lato server → Corsia A** (vanilla, colonna `--u`, zero build).
> **Tutto il resto → Corsia B** (Next.js 16 + Tailwind v4 + Lenis + Framer + GSAP).
> Stesso canone. La resa è due, la mano è una.

Deciso in `company/Memory/decisions/ADR-023-fabbrica-siti-due-corsie.md`. Non si cambia in una
conversazione.

---

## Stato di costruzione

| Fase | Cosa | Stato |
|---|---|---|
| **1** | Legge + canone + ADR-023 | **CHIUSA — 2026-09-06** |
| 2 | I 20 pattern (11 Empire + 9 da Andrei Pascu) | aperta |
| 3 | Il flusso a 9 passi + `SKILL.md` + `emperator.md §6.20` | aperta |
| 4 | `gate_siti.py` (10 controlli) + `qa_sito.py` (Playwright) | aperta |
| 5 | Collaudo: rifare `armageddon` col nostro canone + un sito Empire reale | aperta |

---

## Da dove viene

Metà di questo canone è Empire: la grana, il silver mixing, Onest, i fondi alternati, `#0a0a0a`
al posto del nero puro.

L'altra metà è misurata sul sito `armageddon.bsns.it` di Andrei Pascu il 2026-09-06: la colonna
`--u`, la scala di opacità come gerarchia, il raggio come frazione dell'elemento, le due curve, il
prezzo che si somma dal DOM.

E l'idea stessa di questo impianto viene da una riga trovata nei commenti del suo CSS:
*"CLAUDE.md §4 says his design wins here."*

- `PIANO-MAESTRO/32-DOSSIER-FABBRICA-SITI.md` — l'architettura completa
- `competitor/Andrei Pascu/site-study/reports/11-armageddon-ATLANTE-VISIVO.md` — le misure
- `competitor/Andrei Pascu/site-study/reports/11-armageddon.md` — il rapporto
