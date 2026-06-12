> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 5.1 + 5.2

# WF-PUB-BOOK-ORDER — Ordine manoscritto a Content-Factory

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** PUB-Produzione · **Fase:** 2 — Ordine manoscritto
**Owner gate:** `mb-pub-coord` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Compilare il contratto Bus per richiedere a Content-Factory (03) la produzione del manoscritto
in formato Markdown + image_prompts.yaml. MB non scrive il manoscritto internamente — lo ordina
con spec precise e ne valida la consegna prima di passare a WF-PUB-LAYOUT.

## Input

| Campo | Fonte |
|---|---|
| Spec libro approvata (output WF-PUB-NICHE) | `mb/pub/niches/<slug>.yaml` |
| brand_kit (se libro ha persona/stile riconoscibile) | `mb/pub/<libro-slug>/brand_kit.yaml` (opzionale) |
| Stima costo (dry-run) | Cost-Sentinel (Operations 09) |

## Processo

1. `mb-pub-coord`: dry-run stima costo (generazione testo + immagini) → Cost-Sentinel verde
2. `mb-pub-coord`: compila contratto Bus verso CF con spec_libro completa
3. CF produce: manoscritto MD (capitoli strutturati) + image_prompts.yaml (prompt per ogni immagine)
4. `mb-pub-coord`: valida la consegna vs acceptance criteria
5. Consegna validata → passa a WF-PUB-LAYOUT

## Contratto Bus verso Content-Factory

```json
{
  "from": "05-MULTI-BUSINESS/WF-PUB-BOOK-ORDER",
  "to": "03-CONTENT-FACTORY",
  "payload": {
    "spec_libro": {
      "niche": "",
      "titolo": "",
      "sottotitolo": "",
      "lingua": "it | en",
      "num_capitoli": 0,
      "parole_per_capitolo_target": 0,
      "stile": "how-to | narrative | reference",
      "immagini_per_capitolo": 1
    },
    "brand_kit": null,
    "formato_output": ["manoscritto.md", "image_prompts.yaml"],
    "deadline_giorni": 0,
    "budget_approvato": true
  },
  "acceptance_criteria": [
    "manoscritto.md con tutti i capitoli (struttura H1/H2/H3 pulita)",
    "image_prompts.yaml con 1 prompt per capitolo (stile coerente, no placeholder)",
    "Parole totali nella fascia ±10% del target",
    "Zero claim non verificabili nel testo",
    "Lingua corretta (grammatica, sintassi, registro)"
  ],
  "status": "pending | fulfilled | rejected"
}
```

## Acceptance criteria workflow

- Cost-Sentinel verde prima dell'invio del contratto
- Manoscritto MD consegnato con struttura corretta (capitoli completi, nessun segnaposto)
- image_prompts.yaml con prompt coerenti allo stile definito
- Parole totali ±10% del target
- Zero claim medici/legali/finanziari non supportati
- Consegna validata da mb-pub-coord prima di attivare WF-PUB-LAYOUT
