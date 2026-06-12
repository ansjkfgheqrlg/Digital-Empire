> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 5.1 + 5.3

# WF-PUB-COVER — Spec cover e ordine a Content-Factory

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** PUB-Packaging · **Fase:** 4 — Cover
**Owner gate:** `mb-pub-coord` (Gate Cover) · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Calcolare le dimensioni esatte della cover KDP (dipendono dal numero di pagine reale del PDF
consegnato da WF-PUB-LAYOUT), compilare il brief per Content-Factory, ricevere la cover e
superare il Gate Cover prima di procedere al listing.

## Input

| Campo | Fonte |
|---|---|
| PDF 6x9 con qa_report.md verde (output WF-PUB-LAYOUT) | `mb/pub/<libro-slug>/pdf/` |
| Numero pagine reale del PDF | qa_report.md (campo `num_pagine`) |
| brand_kit libro (palette, font, stile) | `mb/pub/<libro-slug>/brand_kit.yaml` o spec niche |
| Template KDP cover (dimensioni per n. pagine) | KDP Print Cover Calculator |

## Processo

1. `mb-pub-coord` (T-cover-spec): legge `num_pagine` dal qa_report.md
2. Calcola dimensioni cover: trim (6" x 9") + bleed (0.125") + spine (num_pagine × 0.002252" per carta bianca)
3. Compila brief cover per CF: dimensioni, stile visual, testo (titolo + sottotitolo + autore), palette
4. Ordine a CF via contratto Bus (dry-run costo → Cost-Sentinel verde)
5. CF consegna: cover print-ready (PDF 300dpi) + versione ebook (JPG 2560x1600 min)
6. `mb-pub-coord`: verifica Gate Cover (criteri sotto)

## Contratto Bus verso Content-Factory (cover)

```json
{
  "from": "05-MULTI-BUSINESS/WF-PUB-COVER",
  "to": "03-CONTENT-FACTORY",
  "payload": {
    "tipo": "cover_kdp",
    "dimensioni": {
      "larghezza_totale_pollici": 0.0,
      "altezza_pollici": 9.0,
      "spine_pollici": 0.0,
      "bleed_pollici": 0.125
    },
    "testo": {
      "titolo": "",
      "sottotitolo": "",
      "autore": ""
    },
    "stile": "minimalista | colorato | fotografico | illustrato",
    "palette": {},
    "formati_output": ["cover_print_ready.pdf", "cover_ebook.jpg"]
  },
  "acceptance_criteria": [
    "Dimensioni esatte (trim + spine + bleed)",
    "Testo dorso leggibile (≥80px alla scala reale)",
    "Formato PDF 300dpi print-ready conforme KDP",
    "Versione ebook JPG ≥2560x1600",
    "Zero elementi fuori margini di sicurezza"
  ]
}
```

## Gate Cover (bloccante)

| Criterio | Note |
|---|---|
| Dimensioni trim + bleed corrette | Per il numero di pagine reale da qa_report.md |
| Testo dorso leggibile | Solo se libro ≥ 100 pagine |
| Conformità template KDP | Colori, dimensioni, formato file |
| Versione ebook presente | JPG ≥2560x1600 senza dorso |
| Zero elementi fuori margini di sicurezza KDP | Cover Previewer KDP |

Gate rosso → CF rilavora la cover; log failure.

## Acceptance criteria workflow

- Dimensioni cover calcolate correttamente da num_pagine reale
- Gate Cover: PASS
- Cover salvata in `mb/pub/<libro-slug>/cover/` + log wiki
