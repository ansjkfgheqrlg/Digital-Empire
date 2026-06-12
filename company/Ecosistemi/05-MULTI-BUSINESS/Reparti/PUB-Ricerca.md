> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.2 + 5.1

# Reparto L2 — PUB-Ricerca (`MB-PUB`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-PUB-RIC · **Priorità:** MEDIA-ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Identificare niche KDP profittevoli, validare la domanda tramite BSR e analisi competizione,
e consegnare una scheda niche che guida tutta la pipeline libro. Senza una niche validata
non si ordina nessun manoscritto a Content-Factory.

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-PUB-NICHE` | 1 — Niche Research | Scheda niche validata + spec libro (formato, lunghezza target, angolo, lingua, n. capitoli); scorecard con BSR competitor, keyword primaria + secondarie, gap catalogo |

**Input:** risultati dell'ordine a Intelligence (`WF-COMPETITOR`, `WF-TREND`) + dati BSR Amazon
**Output:** scheda niche approvata da mb-pub-coord prima di attivare WF-PUB-BOOK-ORDER

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-kdp-niche-scout | Scansiona categorie KDP: BSR dei top10, volume keyword, stagionalità, gap nel catalogo DE |
| T-keyword-kdp | Keyword research KDP: keyword primaria per titolo/sottotitolo + 7 keyword per listing + 3 categorie KDP |
| T-competition-grader | Scorecard competizione: cover quality, n. recensioni, prezzo medio, analisi listing dei competitor |

## Agenti L5 assegnati

- `mb-pub-niche-scout` (worker, Sonnet) — niche research KDP completo
- `mb-pub-coord` (coordinator, Sonnet) — approva la scheda niche prima di passare a step 2

## Criteri di validazione niche (dossier §5 + §3 QA gate)

Una niche è validata quando:
1. Keyword primaria ha volume ricerca misurabile su KDP (strumento: keyword research KDP)
2. Top-10 competitor: BSR medio < 100.000 (domanda reale); nessun gigante con >1.000 recensioni domina
3. Gap nel catalogo DE: l'angolo scelto non duplica libri già in `KDP - prodottti digitali/LIBRO 1..5`
4. Producibilità AI: il contenuto è generabile con book-factory (no illustrazioni complesse, no ricerca specialistica non supportata)
5. Conformità KDP: niente niche con alto rischio policy (contenuto medico non supportato, copyright)

## Sinergia con il catalogo esistente

Il catalogo `KDP - prodottti digitali/LIBRO 1-5` viene censito da WF-PUB-MONITOR (reparto
PUB-Pubblicazione). I dati BSR/royalty reali di quei libri sono input privilegiato per
T-kdp-niche-scout: niche già vinte → replicare l'angolo su sottonicchie adiacenti.

## KPI di reparto

- % niche validate che diventano ordini a CF (conversione ricerca → produzione): ≥ 70%
- Tempo apertura ricerca → scheda niche approvata: ≤ 2 giorni lavorativi
- Libri prodotti su niche validate che raggiungono BSR < 50.000 entro 90gg: trend (baseline post F-MB6)
