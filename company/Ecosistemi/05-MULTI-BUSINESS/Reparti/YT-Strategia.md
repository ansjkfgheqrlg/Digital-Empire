> Fonte: PIANO-MAESTRO/05-ECOSISTEMA-MULTIBUSINESS.md sez. 2.1 + 4

# Reparto L2 — YT-Strategia (`MB-YT`)

**Ecosistema:** 05-MULTI-BUSINESS · **Codice:** MB-YT-STRAT · **Priorità:** ALTA
**Link:** [[ECOSISTEMA]] · [[BACKBONE]]

## Missione

Governare la strategia di ogni canale YouTube automatizzato: scegliere la niche, validarla,
costruire il brand_kit, pianificare il calendario editoriale. Questo reparto non produce
contenuti — ordina a Content-Factory (03) e possiede i gate prima e dopo.

## Workflow L3 di competenza

| Workflow | Fase pipeline | Output |
|---|---|---|
| `WF-YT-NICHE` | 1 — Ricerca/Strategia | Scheda niche validata + scorecard (domanda, competizione, monetizzabilità, fit AI, RPM stimato) |
| `WF-YT-CHANNEL-LAUNCH` | 1 — Ricerca/Strategia | brand_kit canale completo (nome, persona, voce TTS, palette, template thumbnail, lingua) + canale creato (ok umano obbligatorio) |
| `WF-YT-CALENDAR` | 1 — Ricerca/Strategia | Calendario 30 giorni con titoli provvisori e keyword target per canale |

## Funzioni L4

| Team | Responsabilità |
|---|---|
| T-niche-scout | Scansiona niche YouTube: volume ricerca, competizione, RPM stimato, producibilità AI, rischio policy |
| T-competitor-map | Mappa canali competitor per niche (dopo ingestione F-MB1: frame reali + visione Claude) |
| T-keyword-yt | Keyword research YouTube (search/suggest/tag) — input per calendario e SEO |
| T-brandkit-builder | Compila il brand_kit completo: voce, palette, stile visual, persona, TTS voice |
| T-calendar-planner | Pianifica calendario editoriale 30gg: cadenza, stagionalità, titoli provvisori |

## Agenti L5 assegnati

- `mb-yt-strategy-coord` (coordinator, Sonnet) — coordina i 3 workflow
- `mb-yt-niche-scout` (worker, Sonnet) — scorecard niche
- `mb-yt-competitor-mapper` (worker, Sonnet) — mappa canali competitor
- `mb-yt-keyword-miner` (worker, Haiku) — keyword research
- `mb-yt-brandkit-builder` (worker, Sonnet) — brand_kit canale
- `mb-yt-calendar-planner` (worker, Haiku) — calendario editoriale

## Vincolo F-MB1 (non negoziabile)

`WF-YT-NICHE` e `WF-YT-CHANNEL-LAUNCH` dipendono dall'ingestione Empire Studio dei canali
`@Legamidiamore` e `@dosementale` (F-MB1). Tutti i parametri marcati `[da ingestione F-MB1]`
(RPM target, cadenza regime, struttura script, formato visual) si fissano SOLO dopo i 2 dossier
wiki `sources/` prodotti da Intelligence. Non si inventano benchmark prima.

## Regola di confine

YT-Strategia non scrive script, non genera voiceover, non monta video. Ordina via
`WF-YT-VIDEO-ORDER` (reparto YT-Produzione). La strategia finisce quando il brief è validato e
pronto per Content-Factory.

## KPI di reparto

- % niche validate che passano a WF-YT-CHANNEL-LAUNCH: trend (baseline post F-MB3)
- Tempo da apertura slot a calendario pronto: ≤ 3 giorni lavorativi
- Calendari rispettati (slot riempite in tempo): ≥ 90%
