> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.2 + 5.1 + 5.3

# Reparto L2 — PUB-Packaging (`MB-PUB`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-PUB-PKG · **Priorità:** MEDIA-ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Confezionare il libro per la pubblicazione KDP: cover print-ready, listing completo con copy
APSOC, 7 keyword e 3 categorie ottimizzate. Questo reparto ordina il copy a Marketing (04) e
la cover a Content-Factory (03) — non li produce internamente.

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-PUB-COVER` | 4 — Cover | Spec cover (trim + spine da n. pagine reale) → ordine a CF → cover print-ready + versione ebook; Gate Cover superato |
| `WF-PUB-LISTING` | 5 — Listing | Listing completo: titolo/sottotitolo, descrizione A+ (copy ordinato a Marketing/APSOC), 7 keyword, 3 categorie, pricing consigliato; Gate Listing superato |

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-cover-spec | Calcola dimensioni cover (trim + bleed + spine da n. pagine KDP) e compila il brief per CF |
| T-listing-builder | Assembla il listing completo integrando il copy APSOC ricevuto da Marketing |
| T-category-picker | Seleziona 3 categorie KDP ottimali per massimizzare visibilità e BSR |

## Agenti L5 assegnati

- `mb-pub-listing-builder` (worker, Haiku) — assembla listing + categorie + 7 keyword
- `mb-pub-coord` (coordinator, Sonnet) — supervisione e gate approval

## Gate di competenza (bloccanti)

### Gate Cover

Criteri di pass:
- Dimensioni trim + bleed corrette per il numero di pagine reale del libro (dato da WF-PUB-LAYOUT)
- Testo dorso (spine) leggibile se libro ≥ 100 pagine
- Conformità al template KDP (colori, dimensioni, formato file .PDF o .PNG 300dpi)
- Versione ebook (cover senza dorso, formato JPG 2560x1600 min)

### Gate Listing

Criteri di pass:
- Titolo/sottotitolo senza keyword stuffing (policy KDP); keyword primaria presente nel titolo
- Descrizione APSOC ≥ 300 parole, approvata dal Copy Gate di Marketing (gate 80/100)
- Esattamente 7 keyword popolate; 3 categorie coerenti con la niche (testate per BSR potenziale)
- Pricing nella fascia di mercato (analisi WF-PUB-NICHE)
- Nessuna promessa non verificabile nella descrizione (Mandato Empire: "prove non promesse")

## Sinergia Marketing → Listing

Il copy per la descrizione A+ viene ordinato a Marketing (04) tramite contratto Bus:
`{brand_kit, icp, formato_copy: descrizione_kdp, framework: APSOC, vincoli_piattaforma: KDP}`.
Marketing restituisce la descrizione già validata con il Copy/APSOC Guild gate ≥ 80/100.
PUB-Packaging non riscrive il copy: lo integra nel listing.

## KPI di reparto

- % cover che passano Gate Cover al primo colpo: ≥ 85%
- % listing che passano Gate Listing al primo colpo (include gate Marketing): ≥ 90%
- Lead time PDF consegnato → listing ready: ≤ 3 giorni lavorativi
