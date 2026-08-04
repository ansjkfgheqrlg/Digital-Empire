# Gerarchia degli agenti

Quattro livelli, applicati dal codice in `core/approvals.py` tramite `require_level()`. Ogni
agente dichiara il proprio `level` in `agents/base.py` e chiama `self.authorize(azione)` prima
di compiere un'azione riservata: un tentativo fuori livello solleva `AuthorizationError`.

## Livelli

| Livello | Agenti | Puo' | Non puo' |
|---|---|---|---|
| **OPERATIONAL** | `ResearchAgent`, `ScriptAgent`, `ProductionAgent`, `CopywritingAgent`, `ThumbnailAgent`, `CompetitorAnalysisAgent`, `NicheChannelScoutAgent`, `ProfitableNicheAgent` | eseguire, raccogliere dati, preparare bozze | approvare riferimenti o script, cambiare la nicchia, saltare i controlli |
| **REVIEWER** | `ReviewAgent` | verificare completezza e pertinenza, chiedere integrazioni, respingere | approvare uno script, decidere sulla produzione |
| **SENIOR** | `SeniorDecisionAgent` | approvare riferimenti e script, decidere priorita' e proposte di nicchia | bloccare (e' compito dei regolatori) |
| **REGULATORY** | `RegulatoryAgent` | bloccare e sbloccare, verificare transizioni e originalita' | approvare contenuti |

## Perche' un regolatore non approva

Se chi verifica potesse anche approvare, verificherebbe se stesso. `require_level()` nega
esplicitamente al livello `REGULATORY` le azioni `approve_*`, e nega a tutti gli altri
`block_workflow`. La separazione e' verificata dai test in `tests/test_approvals.py`.

## Azioni riservate

Definite in `RESTRICTED_ACTIONS` (`core/approvals.py`):

| Azione | Livello minimo |
|---|---|
| `review_candidate` | REVIEWER |
| `approve_reference` | SENIOR |
| `approve_script` | SENIOR |
| `decide_niche_proposal` | SENIOR |
| `set_production_priority` | SENIOR |
| `block_workflow` | REGULATORY (esclusivo) |
| `clear_regulatory_block` | REGULATORY (esclusivo) |

## Il revisore esterno

`DigitalEmpireCopyReviewer` **non** e' un agente della fabbrica e non ha un livello: rappresenta
il settore copy di Digital Empire, cioe' un'approvazione esterna che la fabbrica puo' solo
attendere. Per questo il suo esito e' registrato sull'asset (`digital_empire_status`) e non
fra le `Approval` interne.
