# Wrapper L3 -- Workflow Libri (MULTI-BUSINESS / Publishing)

> **Codice sorgente: `Workflow-libri/`**

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | workflow-libri |
| Ecosistema | 05-MULTI-BUSINESS |
| Reparto L2 | Publishing |
| Stato | ACTIVE |
| Codice sorgente | `Workflow-libri/` |

## Cosa fa

Pipeline completa per produzione libro KDP:
- `agents/` — agenti AI per scrittura/editing
- `scripts/` — automazione pipeline
- `templates/` — template capitoli e copertine
- `input/` → `output/` — flusso produzione

## Handoff Contract (ingresso)

```json
{
  "from": "CEO-001 / CRO-001",
  "to": "workflow-libri",
  "payload": {
    "titolo": "",
    "niche": "",
    "numero_capitoli": 0,
    "target_parole": 30000,
    "lingua": "it | en",
    "kdp_categoria": ""
  },
  "acceptance_criteria": [
    "Manoscritto completo in output/",
    "Copertina KDP-compliant generata",
    "Metadata SEO ottimizzati"
  ]
}
```

## KDP Prodotti esistenti

Libri gia' in produzione: `KDP - prodottti digitali/LIBRO 1,2,4,5`.
GPT-KDP Carousel Factory: `KDP - prodottti digitali/GPT - KDP Carousel Factory/`.
