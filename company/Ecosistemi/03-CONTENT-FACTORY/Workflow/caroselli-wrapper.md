# Wrapper L3 -- Caroselli Workflow (CONTENT-FACTORY / Produzione)

> **Codice sorgente: `caroselli/`**

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | caroselli-workflow |
| Ecosistema | 03-CONTENT-FACTORY |
| Reparto L2 | Produzione |
| Stato | ACTIVE |
| Codice sorgente | `caroselli/3-sistemi-ai/` |

## Cosa fa

Genera caroselli AI-powered per Instagram/LinkedIn:
- Input: brand_kit + ICP + topic
- Output: slide strutturate pronte per Canva/pubblicazione

## Handoff Contract (ingresso)

```json
{
  "from": "01-AGENCY | 02-INFO-BUSINESS | 04-MARKETING",
  "to": "caroselli-workflow",
  "payload": {
    "brand": "",
    "topic": "",
    "numero_slide": 10,
    "piattaforma": "instagram | linkedin",
    "obiettivo": "awareness | conversione | educazione"
  },
  "acceptance_criteria": [
    "Hook slide 1 score >= 80",
    "Struttura narrativa coerente",
    "CTA presente nell'ultima slide"
  ]
}
```
