> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 5.1 + 5.3

# WF-PUB-LISTING — Listing KDP completo

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** PUB-Packaging · **Fase:** 5 — Listing
**Owner gate:** `mb-pub-coord` (Gate Listing) · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Costruire il listing KDP completo (titolo, sottotitolo, descrizione A+, 7 keyword, 3 categorie,
pricing) che massimizza la visibilità organica e converte il traffico. Il copy della descrizione
viene ordinato a Marketing (04) — MB non lo scrive internamente.

## Input

| Campo | Fonte |
|---|---|
| Spec libro (keyword primaria + secondarie, niche) | WF-PUB-NICHE |
| Cover Gate verde | WF-PUB-COVER |
| Copy descrizione APSOC (ordinato a Marketing) | Bus HC verso 04-MARKETING |
| Pricing competitor (da WF-PUB-NICHE scorecard) | `mb/pub/niches/<slug>.yaml` |

## Processo

1. `mb-pub-listing-builder`: ordina copy descrizione a Marketing (contratto Bus sotto)
2. Marketing produce descrizione APSOC ≥300 parole, gate Copy/APSOC ≥80/100
3. `mb-pub-listing-builder`: riceve copy approvato + assembla listing completo
4. `mb-pub-listing-builder`: seleziona 7 keyword finali (primaria nel titolo/sottotitolo + 6 secondarie)
5. `mb-pub-listing-builder` (T-category-picker): seleziona 3 categorie KDP ottimali
6. `mb-pub-listing-builder`: calcola pricing nella fascia di mercato
7. `mb-pub-coord`: verifica Gate Listing

## Contratto Bus verso Marketing (descrizione)

```json
{
  "from": "05-MULTI-BUSINESS/WF-PUB-LISTING",
  "to": "04-MARKETING",
  "payload": {
    "brand_kit": {},
    "icp": "<profilo reader target>",
    "formato_copy": "descrizione_kdp",
    "framework": "APSOC",
    "vincoli_piattaforma": "KDP: no keyword stuffing, no promesse mediche/legali, disclosure AI obbligatoria",
    "keyword_primaria": "",
    "lunghezza_min_parole": 300
  },
  "acceptance_criteria": [
    "Copy APSOC gate ≥80/100 (Marketing interno)",
    "≥300 parole",
    "Keyword primaria integrata naturalmente",
    "Zero promesse non verificabili (Mandato Empire)"
  ]
}
```

## Gate Listing (bloccante)

| Criterio | Note |
|---|---|
| Titolo + sottotitolo | Keyword primaria presente; niente keyword stuffing |
| Descrizione APSOC | ≥300 parole, gate Marketing ≥80/100, zero claim non verificabili |
| 7 keyword | Compilate (primaria + 6 secondarie); coerenti con la niche |
| 3 categorie KDP | Coerenti con niche; testate per BSR potenziale |
| Pricing nella fascia | Analisi competitor WF-PUB-NICHE |
| Disclosure AI | Presente se richiesta da KDP |

## Output — listing.yaml

```yaml
titolo: ""
sottotitolo: ""
descrizione: ""   # copy APSOC gate-verde
keywords_kdp: []  # esattamente 7
categorie: []     # esattamente 3
prezzo_ebook: 0.00
prezzo_print: 0.00
gate_listing: "PASS"
```

## Acceptance criteria workflow

- Copy descrizione ricevuto con gate Marketing ≥80/100
- Gate Listing: PASS
- listing.yaml salvato in `mb/pub/<libro-slug>/listing.yaml` + log wiki
