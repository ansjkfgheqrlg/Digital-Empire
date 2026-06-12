> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 5.1 + 5.3

# WF-PUB-PUBLISH — Upload KDP e pubblicazione

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** PUB-Pubblicazione · **Fase:** 6 — Pubblicazione
**Owner gate:** `mb-pub-coord` + review umana obbligatoria · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Pubblicare il libro su Amazon KDP con tutti i gate verdi (Layout + Cover + Listing + Compliance)
e la review umana firmata. Questo è il punto di non ritorno nella pipeline: una volta pubblicato,
eventuali correzioni richiedono una nuova revisione KDP (lead time 24-72h).

## Input

| Campo | Fonte |
|---|---|
| PDF 6x9 (Gate Layout verde) | WF-PUB-LAYOUT → `mb/pub/<libro-slug>/pdf/book_final.pdf` |
| Cover print-ready + ebook (Gate Cover verde) | WF-PUB-COVER → `mb/pub/<libro-slug>/cover/` |
| listing.yaml (Gate Listing verde) | WF-PUB-LISTING |
| Credenziali KDP | PLATFORM code custody (NON in git) |

## Processo

1. `mb-pub-publisher`: verifica Gate Compliance pre-upload (checklist completa sotto)
2. Review umana obbligatoria: Max o Gael firmano il checklist fisicamente (o via nota in `mb/pub/<libro-slug>/review.md`)
3. `mb-pub-publisher`: upload su KDP Bookshelf — PDF + cover + listing
4. `mb-pub-publisher`: imposta pricing (ebook + print), distribuzioni (KDP Select se applicabile), categorie
5. Libro entra in review KDP (24-72h); `mb-pub-publisher` monitora lo stato
6. Alla pubblicazione: entry wiki log.md + salvataggio metadati in `mb/pub/<libro-slug>/published.yaml`
7. Avvio WF-PUB-MONITOR per questo libro

## Gate Compliance (bloccante — obbligatorio pre-upload)

| Criterio | Note |
|---|---|
| qa_report.md verde | Da WF-PUB-LAYOUT |
| Gate Cover verde | Da WF-PUB-COVER |
| Gate Listing verde | Da WF-PUB-LISTING (copy Marketing ≥80/100) |
| No contenuto ingannevole/duplicato | Verifica vs LIBRO 1-5 esistenti (anti-duplicazione) |
| Disclosure AI | Dichiarazione presente dove richiesta da KDP |
| No claim medici/legali non supportati | Check testo e descrizione |
| Review umana firmata | Vincolo non revocabile senza ADR esplicito |

Gate rosso → blocco assoluto upload + report mb-pub-coord + mb-conductor.

## Acceptance criteria workflow

- Tutti i 4 gate a monte verdi (Layout + Cover + Listing + Compliance)
- Review umana firmata
- Libro pubblicato su KDP (stato: live) con ASIN registrato
- ASIN e URL libro salvati in `mb/pub/<libro-slug>/published.yaml` + log wiki
- WF-PUB-MONITOR attivato per questo ASIN
