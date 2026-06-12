> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.2 + 5.1 + 5.3

# Reparto L2 — PUB-Pubblicazione (`MB-PUB`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-PUB-PUB · **Priorità:** MEDIA-ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Pubblicare il libro su Amazon KDP dopo la review umana obbligatoria, monitorare BSR/royalty/
recensioni, e chiudere il loop retro-alimentando PUB-Ricerca con i dati reali. Tiene anche il
registro del catalogo LIBRO 1-5 esistente.

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-PUB-PUBLISH` | 6 — Pubblicazione | Libro pubblicato su KDP con pricing, categorie, listing approvati; review umana firmata; Gate Compliance superato |
| `WF-PUB-MONITOR` | 7 — Monitor (loop continuo) | Report mensile BSR/vendite/royalty/recensioni → feedback a WF-PUB-NICHE (reparto Ricerca) |

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-kdp-uploader | Upload manuale (o assistito) su KDP: PDF 6x9 + cover + listing; pricing input |
| T-pricing | Raccomandazione pricing nella fascia di mercato (input: analisi competitor WF-PUB-NICHE) |
| T-royalty-tracker | Monitora BSR, vendite, royalty, recensioni dal pannello KDP; logga in `mb/pub/<libro-slug>/` |
| T-review-watcher | Monitora nuove recensioni: alert per recensioni negative, reply pattern, feedback a Ricerca |

## Agenti L5 assegnati

- `mb-pub-publisher` (worker, Haiku) — upload KDP + pricing + checklist pre-pubblicazione
- `mb-pub-royalty-tracker` (worker, WASM/Haiku) — BSR/royalty/recensioni + feedback loop
- `mb-pub-coord` (coordinator, Sonnet) — supervisione gate Compliance e review umana

## Gate Compliance (bloccante — obbligatorio)

Prima di ogni pubblicazione:
- Checklist contenuti KDP: no contenuto ingannevole/duplicato rispetto ai LIBRO 1-5 esistenti
- Disclosure AI: dichiarazione dove richiesta da KDP (obbligatoria per contenuto generato da AI)
- `qa_report.md` verde (consegnato da WF-PUB-LAYOUT)
- Gate Cover verde (consegnato da WF-PUB-COVER)
- Gate Listing verde con copy Marketing approvato
- **Review umana finale: obbligatoria su OGNI libro** (vincolo non revocabile senza ADR esplicito)

Gate rosso → blocco pubblicazione; report a mb-pub-coord + mb-conductor.

## Catalogo esistente (censimento obbligatorio F-MB6)

Libri già in catalogo da censire in WF-PUB-MONITOR:
- `KDP - prodottti digitali/LIBRO 1` — stato, BSR attuale, royalty, recensioni
- `KDP - prodottti digitali/LIBRO 2` — idem
- `KDP - prodottti digitali/LIBRO 4` — idem
- `KDP - prodottti digitali/LIBRO 5` — idem
Censimento = entry in `mb/pub/<libro-slug>/` + pagina wiki `projects/` per ogni libro.

## Loop monitor → strategia

`WF-PUB-MONITOR` legge i dati mensili e alimenta il ciclo:
- BSR stabile < 50.000: libro attivo, no azione
- BSR degradato > 200.000 per 90gg: decisione mb-pub-coord → kill o relaunch (nuova niche)
- Recensioni negative ricorrenti su stesso tema: pattern distillato → brief CF migliorato

## KPI di reparto

- Libri pubblicati senza violazioni KDP: 100% (sospensione account = KPI critico)
- BSR medio catalogo attivo entro 90gg da pubblicazione: < 100.000 (obiettivo F-MB6)
- Royalty mensili per libro censiti e loggati: 100% di copertura
