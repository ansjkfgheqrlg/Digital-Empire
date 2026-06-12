> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.3 + 6

# WF-ECOM-PRODUCT — Ricerca prodotto e-commerce (ATTIVABILE ora)

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** ECOM-Ricerca · **Stato:** ATTIVABILE (zero spesa)
**Owner gate:** `mb-ecom-coord` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Unico workflow e-commerce attivabile nella fase attuale (pre-F-MB7). Esegue la ricerca
prodotto in modalità pura: zero spesa, output = dossier wiki in `sources/` prodotto da
Intelligence. Produce il materiale per la decisione E1 (scelta modello).

## Regola fondamentale

Questo workflow è eseguito da **Intelligence (08)** su ordine di MB. MB non ricerca
internamente — ordina la ricerca tramite contratto Bus e riceve il dossier. Non si attivano
WF-ECOM-STORE, WF-ECOM-ADS, WF-ECOM-FULFILL prima del gate E1 (mb-conductor + ok umano).

## Input

| Campo | Fonte |
|---|---|
| Budget: zero spesa API/pubblicità | Cost-Sentinel (vincolo assoluto) |
| Asset esistenti (cover libri, brand_kit) | `mb/pub/` + `KDP - prodottti digitali/` |
| Modelli e-comm candidati da valutare | mb-conductor |

## Processo

1. `mb-ecom-coord`: compila ordine a Intelligence (contratto Bus sotto)
2. Intelligence esegue `WF-COMPETITOR` + `WF-TREND` per il dominio e-commerce
3. Intelligence produce dossier wiki `sources/` con analisi modelli, trend, margini
4. `mb-ecom-coord`: riceve dossier + compila scorecard prodotto
5. `mb-ecom-coord`: presenta scorecard a mb-conductor per decisione E1

## Contratto Bus verso Intelligence

```json
{
  "from": "05-MULTI-BUSINESS/WF-ECOM-PRODUCT",
  "to": "08-INTELLIGENCE",
  "payload": {
    "dominio": "ecomm-digital-physical",
    "domande_ricerca": [
      "Quale modello (POD/dropshipping/digitale) è più sinergico con MB-PUB?",
      "Margini reali per POD su piattaforme Amazon Merch, Printful, Redbubble?",
      "Trend domanda 2025-2026 per merch derivato da libri KDP?",
      "Requisiti tecnici e costi setup per ogni modello?"
    ],
    "output_atteso": "dossier_wiki",
    "vincoli": "zero spesa API o pubblicità durante la ricerca"
  },
  "acceptance_criteria": [
    "Dossier in wiki sources/ con dati verificabili e fonti",
    "Scorecard margine per ogni modello candidato",
    "Sezione sinergia con MB-PUB (riuso brand_kit e cover)",
    "Requisiti tecnici per ogni modello"
  ]
}
```

## Scorecard prodotto (output per decisione E1)

| Modello | Margine netto stimato | Sinergia MB-PUB | Complessità setup | Decisione |
|---|---|---|---|---|
| POD (Merch Amazon / Printful) | `[da dossier Intelligence]` | Alta (stesso brand_kit) | Bassa | `[da E1]` |
| Digitale (ebook su Gumroad) | `[da dossier Intelligence]` | Alta (asset già esistenti) | Minima | `[da E1]` |
| Dropshipping | `[da dossier Intelligence]` | Bassa | Alta | `[da E1]` |

## Acceptance criteria

- Dossier wiki `sources/` prodotto da Intelligence con dati verificabili
- Scorecard compilata (dati reali, non stime inventate)
- Decisione E1 richiesta a mb-conductor + ok umano prima di qualsiasi azione store
- Zero spesa in qualsiasi step di questo workflow
