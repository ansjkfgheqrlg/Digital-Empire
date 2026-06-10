# Empire Studio - STRATEGY REGISTRY

> Non esiste "la" strategia. Esistono molte strategie specializzate, attivate dal
> reparto Strategy in base a reparto, tipo di contenuto e stile di implementazione
> wiki. Questo registro le elenca; lo script `generate_strategy_manifest.py` le
> combina nel Manifest della run.

## 1. Strategie per reparto/ambiente
| Reparto | File | Regole chiave |
|---|---|---|
| YouTube | `youtube/youtube-design-system-strategy.md` | frame per capitolo, visione densa long-form |
| TikTok | `tiktok/tiktok-quick-strategy.md` | frame ogni 3-8s, hook+output |
| Web | `web/web-reference-strategy.md` | Playwright render, screenshot sezioni |
| Projects/Repos | `projects-repos-workloads/deep-study-strategy.md` | sola lettura, architettura+perche'+trace |

## 2. Strategie per tipo di contenuto
| Tipo | Regole | Stile wiki |
|---|---|---|
| Design System | frame su componenti/export/token, descrizioni >60 parole | Visual-Heavy Reference |
| Marketing | framework + esempi + metriche | Playbook |
| Automazioni/Tool | comandi esatti + gotchas mostrati | How-to Quick-Reference |
| Teorico/Framework | concetti + applicazioni + mappa | Concept Map |

## 3. Stili di implementazione wiki
- **Atomic Notes + MOC** (default): 1 nota per concetto + mappa di contenuti.
- **Visual-Heavy Reference**: molte reference a frame + descrizioni visive (design/tool).
- **Playbook**: When to use / Framework / Esempi / Metriche (marketing/operativo).
- **How-to Quick-Reference**: passaggi + comandi + gotchas (automazioni).
- **Update-Proposal Integrated**: ogni ingest rilevante genera proposte di update.

## 4. Strategie esterne / indipendenti
- **Cross-Workflow Update**: usa la nuova conoscenza per migliorare altri workflow.
- **Self-Improvement**: l'ecosistema migliora se stesso (strategy-improver + silent-observer).
- **Knowledge Propagation**: come la nuova conoscenza si diffonde in memory e tra i reparti.

## 5. Come si seleziona (decision tree)
Gestito da `strategy-coordinator` + `generate_strategy_manifest.py`:
1. Identifica reparto (YouTube/TikTok/Web/Projects).
2. Identifica tipo contenuto (design/marketing/automazioni/teorico) dal `--focus`.
3. Combina con lo stile wiki appropriato.
4. Genera il Manifest (regole concrete) -> `memory/strategy-applications/`.
5. `strategy-applicator` lo inietta negli handoff; `strategy-controller` ne verifica l'aderenza.

## 6. Versioning
Le strategie sono versionate (v1.0, v1.1...). Le versioni e le proposte di
miglioramento vivono in `memory/strategy-versions/`, gestite da
`meta-strategy-manager` + `strategy-improver` (data-driven, dalle run reali).

## 7. Mappa agenti Strategy
- coordinator (seleziona) · applicator (applica) · controller (verifica) ·
  improver (migliora) · department-strategist (per reparto) ·
  content-type-strategist (per tipo) · meta-strategy-manager (gestisce il registry).
