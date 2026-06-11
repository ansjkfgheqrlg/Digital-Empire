# Wrapper L3 -- Crea Siti (PLATFORM / Siti)

> **Codice sorgente: `Crea siti/`**

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | crea-siti |
| Ecosistema | 06-PLATFORM |
| Reparto L2 | Siti |
| Stato | ACTIVE |
| Codice sorgente | `Crea siti/` |

## Cosa fa

Produzione siti web per clienti e prodotti DE:
- Template per siti CCM
- Design system empire-style (`SKILL & Agenti/empire-style/`)
- Skills: Web Builder, Website Creator

## Handoff Contract (ingresso)

```json
{
  "from": "01-AGENCY (cliente) | 02-INFO-BUSINESS (prodotto)",
  "to": "crea-siti",
  "payload": {
    "tipo": "landing | sito_completo | sales_page",
    "brand_kit": {},
    "copy_fornito": true,
    "deadline_giorni": 7
  },
  "acceptance_criteria": [
    "Mobile-first responsive",
    "Core Web Vitals >= 90",
    "Copy APSOC >= 80 integrato"
  ]
}
```
