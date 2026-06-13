# WF-CORSO — Produzione Corso End-to-End

## Reparto: L2-PRODOTTO
## Owner: IB-PM-product-manager + IB-MKD-forger + IB-CURRIC-designer + IB-PLATFORM-op

## Trigger
Brief validato da WF-VALIDAZIONE con score ≥60/100 E gate B1 verde (prezzo prodotto deciso nel catalogo).

## Input (payload)
```json
{
  "prodotto": "nome-corso",
  "cartella_raw": "Formazzione/[folder]/",
  "brief_validato": "path al brief da IB-VALIDATION-analyst",
  "icp": "descrizione ICP",
  "outcome_primario": "cosa sa fare lo studente al termine",
  "formato": "video|testo|ibrido",
  "durata_target": "ore totali corso",
  "deadline_piattaforma": "data smoke test richiesta"
}
```

## Pipeline

1. **IB-MKD-forger** — `content-forge` su cartella raw → MKD completo
   - GATE: MKD copre 100% atomi fonte; ogni atomo tracciato alla fonte; zero contenuto inventato
   - Prodotto DE: `Formazzione/Claude code/` → MKD per Manuale Claude Code; `Lancio corso skill beast/` → MKD per Corso Skill Beast

2. **IB-CURRIC-designer** — MKD + brief → curriculum strutturato (moduli → lezioni → outcome + esercizi)
   - GATE: ogni lezione ha 1 outcome verificabile; progressione didattica validata; durata totale dichiarata

3. **Review IB-PM** — verifica curriculum vs brief validato: ICP può seguire il percorso senza salti
   - GATE: approvazione IB-PM scritta con data

4. **HANDOFF → CONTENT-FACTORY** (se corso video): script lezioni → moduli video montati
   - Acceptance: durata, formato MP4, qualità audio; timing da brief CF

5. **IB-PLATFORM-op** — carica su piattaforma orchestrando `formazione-orchestrator`:
   - `formazione-database` (schema Supabase, contenuti)
   - `formazione-admin` (accessi, upload risorse)
   - `formazione-design` (UI brand Empire)
   - `formazione-student` (percorso, progress tracking)
   - GATE: smoke test "studente fantasma" completa modulo 1 end-to-end; zero errori 500

6. **T-DESIGN-PRODOTTO** — copertina, workbook, certificato
   - GATE: brand voice conforme, formati pronti per sales asset

## Gate (soglie)
| Gate | Responsabile | Criterio pass |
|---|---|---|
| Gate MKD | IB-MKD-forger | 100% atomi coperti, zero perdita |
| Gate curriculum | IB-CURRIC-designer + IB-PM | Ogni lezione 1 outcome; progressione logica |
| Gate piattaforma | IB-PLATFORM-op | Smoke test verde; paywall attivo |
| Gate brand voice | IB-PM | Zero contenuto generico o promesse non dimostrabili |

## Output
Corso live su piattaforma + asset vendita preliminari (copertina, curriculum pubblico per sales page) → handoff a L2-VENDITE per offer stack e pricing.

## Dry-run: come si esegue
1. IB-PM esegue smoke test studente su ambiente staging (non produzione)
2. Stima costi sessione (agenti Sonnet, storage Supabase) → Cost-Sentinel valuta
3. Se dry-run verde → autorizzazione deploy su produzione

## Handoff in uscita
```json
{
  "from": "infobusiness/prodotto",
  "to": "infobusiness/vendite-funnel",
  "payload": {
    "corso": "nome-corso",
    "piattaforma_url": "url corso live",
    "curriculum_pubblico": "path markdown",
    "asset_copertina": "path immagini",
    "smoke_test": "verde | timestamp"
  },
  "acceptance_criteria": ["smoke test verde", "catalogo aggiornato con prezzo", "brief per sales page allegato"]
}
```
