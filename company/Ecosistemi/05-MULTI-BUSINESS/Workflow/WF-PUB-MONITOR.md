> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 5.1 + 10

# WF-PUB-MONITOR — BSR, royalty, recensioni e feedback loop

**Ecosistema:** 05-MULTI-BUSINESS · **Reparto L2:** PUB-Pubblicazione · **Fase:** 7 (loop continuo)
**Owner gate:** `mb-pub-royalty-tracker` · **Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Scopo

Monitorare le performance di ogni libro pubblicato (BSR, vendite, royalty, recensioni) e
chiudere il loop verso PUB-Ricerca. Tiene anche il registro del catalogo LIBRO 1-5 esistente.
La cadenza è mensile; alert immediato per recensioni negative o anomalie KDP.

## Input

| Campo | Fonte |
|---|---|
| Pannello KDP Bookshelf (BSR, vendite, royalty) | Credenziali KDP (PLATFORM code custody) |
| Recensioni Amazon (stelle, testo) | Amazon listing libro |
| Soglie di allarme | `mb/pub/patterns` |

## Processo

1. `mb-pub-royalty-tracker`: pull dati mensili (BSR, vendite, royalty) per ogni ASIN attivo
2. `mb-pub-royalty-tracker`: logga metriche in `mb/pub/<libro-slug>/monitor/YYYY-MM.yaml`
3. `mb-pub-royalty-tracker`: classifica libro: ATTIVO / IN DECLINO / CANDIDATO KILL
4. `mb-review-watcher`: pull recensioni nuove → alert per recensioni < 3 stelle
5. `mb-pub-coord`: per libri CANDIDATO KILL (BSR > 200.000 per 90gg) → decisione kill/relaunch
6. Pattern distillati → `mb/pub/patterns` (cross-libro) + wiki log.md

## Classificazione libro

| Classificazione | Criteri | Azione |
|---|---|---|
| ATTIVO | BSR < 100.000; royalty positive | Nessuna azione — monitoraggio mensile |
| IN DECLINO | BSR 100.000-200.000 per 2 mesi consecutivi | Alert mb-pub-coord; valutare aggiornamento listing o promozione |
| CANDIDATO KILL | BSR > 200.000 per 90gg | Decisione mb-pub-coord + mb-conductor: kill (unpublish) o relaunch (nuovo angolo) |

## Censimento catalogo LIBRO 1-5 (F-MB6 — obbligatorio)

Al primo avvio di WF-PUB-MONITOR:
- LIBRO 1: `KDP - prodottti digitali/LIBRO 1` → entry `mb/pub/libro-1/published.yaml`
- LIBRO 2: `KDP - prodottti digitali/LIBRO 2` → entry `mb/pub/libro-2/published.yaml`
- LIBRO 4: `KDP - prodottti digitali/LIBRO 4` → entry `mb/pub/libro-4/published.yaml`
- LIBRO 5: `KDP - prodottti digitali/LIBRO 5` → entry `mb/pub/libro-5/published.yaml`
Per ogni libro: ASIN, URL, BSR corrente, royalty ultimi 30gg, n. recensioni, media stelle.

## Output mensile

```yaml
report_data: "YYYY-MM"
libri_monitorati: 0
sommario:
  attivi: 0
  in_declino: 0
  candidati_kill: 0
royalty_totali_mese: 0.0
pattern_distillati: []
decisioni_richieste: []
```

## Acceptance criteria

- Report mensile generato entro il 5 del mese successivo
- Ogni libro con ASIN monitorato
- Pattern cross-libro salvati in `mb/pub/patterns` + ReasoningBank (INTELLIGENCE)
- Decisioni kill/relaunch escalate a mb-pub-coord + mb-conductor per approvazione
