> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.1 + 4.2 + 4.3

# Reparto L2 — YT-Ottimizzazione (`MB-YT`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-YT-OPT · **Priorità:** ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Massimizzare il CTR e la retention di ogni video prima della pubblicazione. Questo reparto
possiede i gate #1 (Script) e #4 (SEO), e coordina la scelta finale di titolo, descrizione,
tag, end screen e thumbnail. È il checkpoint di qualità prima che il video passi a YT-Pubblicazione.

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-YT-OPT` | 3 — Ottimizzazione | Titolo finale, descrizione SEO, tag, end screen, thumbnail scelta; gate #1 Script e #4 SEO entrambi verdi |

**Passi 10-12 della pipeline (eseguiti qui):**
- Step 10: titolo + descrizione SEO
- Step 11: tag + end screen + cards
- Step 12: SEO gate (#4) + brand gate

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-title-lab | Genera e testa varianti titolo CTR-first, policy-safe; ≤100 caratteri con keyword primaria |
| T-description-seo | Descrizione SEO ≥200 parole con keyword, timestamp e CTA; ≥200 parole |
| T-tags | Ricerca e selezione 10-15 tag pertinenti; niente keyword stuffing |
| T-endscreen-cards | Impostazione end screen + cards (link, playlist, iscrizione) |
| T-thumb-ab | Spec thumbnail A/B + test leggibilità 120px; volto/soggetto + ≤4 parole |

## Agenti L5 assegnati

- `mb-yt-opt-coord` (coordinator, Sonnet) — coordina WF-YT-OPT e i 4 QA gate video
- `mb-yt-title-smith` (worker, Sonnet) — varianti titolo
- `mb-yt-seo-writer` (worker, Haiku) — descrizione SEO, tag, capitoli/timestamp
- `mb-yt-thumb-strategist` (worker, Sonnet) — spec thumbnail + A/B test

## Gate di competenza (bloccanti)

| Gate | Quando | Criteri chiave |
|---|---|---|
| **#1 Script** | Dopo consegna script da CF | Hook nei primi 15s; struttura retention; brand_kit; lunghezza ±10% target; zero claim non verificabili; similarity < soglia vs ultimi 20 script (anti-ripetitività) |
| **#4 SEO** | Dopo WF-YT-OPT | Titolo ≤100 char con keyword; descrizione ≥200 parole; 10-15 tag; end screen + cards; metadata policy-safe |

Gate #1 rosso → script torna a CF. Gate #4 rosso → rifacimento ottimizzazione.
Mai override senza decisione mb-conductor. Ogni gate rosso → ReasoningBank.

## Anti-ripetitività (criterio script gate)

Similarity check obbligatorio vs gli ultimi 20 script del canale. Se similarità > soglia
(da calibrare con F-MB1): script rifiutato, brief rivisto con nuovi angoli. La cadenza non
supera mai la capacità dei gate: qualità > volume (dossier §4.4).

## KPI di reparto

- % script che passano gate #1 al primo colpo: obiettivo ≥ 80% (baseline post F-MB4)
- % video che passano gate #4 SEO al primo colpo: obiettivo ≥ 90%
- CTR medio canale (letto da WF-YT-ANALYTICS, retro-alimenta i brief): trend crescente
- Similarity media vs ultimi 20 script: < soglia fissata in F-MB1
