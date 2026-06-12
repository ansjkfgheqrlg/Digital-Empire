> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 5.1 + 5.2

# WF-PUB-NICHE — Niche research KDP

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** PUB-Ricerca · **Fase:** 1 — Niche Research
**Owner gate:** `mb-pub-coord` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Identificare una niche KDP profittevole, validarla con scorecard misurabile (BSR, keyword,
gap catalogo, producibilità AI) e consegnare la spec libro che guida WF-PUB-BOOK-ORDER.
Nessun libro si ordina senza niche validata e approvata da mb-pub-coord.

## Input

| Campo | Fonte |
|---|---|
| Catalogo esistente LIBRO 1-5 (anti-duplicazione) | `KDP - prodottti digitali/` + WF-PUB-MONITOR |
| Ordine a Intelligence per ricerca trend | Bus HC verso 08-INTELLIGENCE (`WF-COMPETITOR`, `WF-TREND`) |
| Pattern niche vincenti passati | `mb/pub/patterns` |

## Processo

1. `mb-pub-niche-scout`: scansiona categorie KDP → lista 10 niche candidate
2. `mb-pub-niche-scout`: raccoglie dati BSR dei top-10 libri per ogni niche candidata
3. `mb-pub-niche-scout`: verifica gap nel catalogo DE (LIBRO 1-5 esistenti → no duplicazione)
4. Ordine a Intelligence per keyword research KDP approfondita (contratto Bus)
5. `mb-pub-coord`: compila scorecard per le top-3 niche
6. `mb-pub-coord`: seleziona la niche vincente + compila spec libro → approvazione mb-conductor

## Scorecard di validazione niche KDP

| Criterio | Soglia | Fonte dato |
|---|---|---|
| BSR medio top-10 competitor | < 100.000 (domanda reale) | Amazon BSR manuale |
| Numero recensioni top competitor | < 500 (spazio per entrare) | Amazon listing |
| Keyword primaria con volume KDP | Misurabile (tool KDP) | Keyword research |
| Gap catalogo DE | Angolo non duplicato da LIBRO 1-5 | Censimento WF-PUB-MONITOR |
| Producibilità AI (book-factory) | Sì: solo testo + immagini AI generabili | Analisi spec libro |
| Conformità policy KDP | Nessun rischio (medico non supportato, copyright) | Checklist |

## Output — spec libro

```yaml
niche: ""
lingua: "it | en"
keyword_primaria: ""
keyword_secondarie: []
categorie_kdp: []   # 3 categorie target
titolo_ipotetico: ""
sottotitolo_ipotetico: ""
num_capitoli: 0
parole_target: 0
stile: "how-to | narrative | reference"
immagini_per_capitolo: 1
scorecard:
  bsr_medio_competitor: 0
  recensioni_top_competitor: 0
  gap_catalogo: true
  producibilita_ai: true
  conformita_policy: true
stato: "APPROVATA | RIFIUTATA"
```

## Acceptance criteria

- Scorecard compilata con dati verificabili (BSR da Amazon reale, non stimati)
- Zero duplicazioni con LIBRO 1-5 (gap confermato)
- Spec libro completa approvata da mb-pub-coord
- Spec salvata in `mb/pub/niches/<slug>.yaml` + log wiki
