# Wrapper L3 -- Lancio Corso/Ebook (INFO-BUSINESS / Lanci)

> **Codice sorgente: `Lancio corso skill beast/` + `InfoBusiness/` + `Formazzione/`**

## Identita'

| Campo | Valore |
|---|---|
| ID workflow | lancio-infobusiness |
| Ecosistema | 02-INFO-BUSINESS |
| Reparto L2 | Lanci |
| Stato | ACTIVE (CCM) / EXPERIMENTAL (ebook) |
| Blocker | Prezzo Manuale Claude Code da definire con Max |

## Cosa fa

Orchestrazione lancio prodotto info:
1. Definizione prodotto + pricing
2. Funnel (da `InfoBusiness/Funnel Unico Perfetto.pdf`)
3. Copy sequenze email (via `04-MARKETING/copy-workflow`)
4. Landing page (via `06-PLATFORM/crea-siti`)
5. Asset grafici (via `03-CONTENT-FACTORY`)
6. Pubblicazione + analytics

## Prodotti attivi

| Prodotto | Stato | Prezzo | Note |
|---|---|---|---|
| Manuale Claude Code (CCM) | In lancio | DA DEFINIRE | Blocker attivo |
| Agency Scalping | Formazione | Verifica | `Formazzione/Agency Scalping/` |

## Handoff Contract (ingresso)

```json
{
  "from": "CEO-001 / CRO-001",
  "to": "lancio-infobusiness",
  "payload": {
    "prodotto": "",
    "prezzo": 0,
    "data_lancio": "",
    "icp": "",
    "obiettivo_revenue": 0
  },
  "acceptance_criteria": [
    "Funnel completo approvato da CMO-001",
    "Copy APSOC >= 85 (pagina vendita)",
    "Landing page live e testata"
  ]
}
```
