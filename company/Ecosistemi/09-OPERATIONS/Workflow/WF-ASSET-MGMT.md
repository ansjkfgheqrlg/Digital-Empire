> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. 09 §3 L3 WF-ASSET-MGMT

# L3 — WF-ASSET-MGMT (Asset Management Multi-Tenant)

**Ecosistema:** 09-OPERATIONS · **Reparto L2:** STORAGE-ASSETS
**Coordinator:** `ops-asset-keeper` · **Direttore:** `ops-director`
**Connessione:** [[ECOSISTEMA.md]] · [[BACKBONE.md]]

## Missione

WF-ASSET-MGMT assegna a ogni asset prodotto dalla holding un nome canonico,
una posizione nota, un hash anti-duplicato e una data di scadenza. Senza questo,
gli asset si moltiplicano come file senza nome e nessuno trova nulla. Pattern
multi-tenant (pattern #11): lo stesso motore gestisce asset DE, clienti agency,
canali YouTube, libri KDP — distinti per `brand_kit`.

**Vincolo ADR-004:** asset binari pesanti (video mp4, zip, PNG copertine, session data)
NON nel monorepo GitHub → Drive o storage locale. WF-ASSET-MGMT custodisce l'indice
di dove ogni asset vive davvero.

## Naming convention canonico

```
<brand_kit>/<ecosistema>/<commessa|progetto>/<tipo>/<YYYYMMDD>-<nome>.<ext>
```

**Esempi:**
- `DE/09-OPERATIONS/backup-wiki/wiki/20260611-wiki-snapshot.zip`
- `exponium/06-PLATFORM/sito-v2/render/20260611-hero-mobile.png`
- `DE/03-CONTENT-FACTORY/caroselli-q2/carousel/20260611-linkedin-01.png`

## Classi di asset e retention

| Classe | Descrizione | Retention | Delete |
|---|---|---|---|
| deliverable-cliente | output consegnato al cliente | permanente | solo ok umano |
| asset-interno | usato da DE internamente | 1 anno | automatico |
| render-intermedio | step di produzione non finale | 30 giorni | automatico |
| backup | snapshot di wiki/knowledge/registry | 90 giorni rolling | automatico |
| session-data | sessioni browser (escluse dal repo) | run lifetime | automatico a run end |

## Processo decisionale (`ops-asset-keeper`)

1. Asset in ingresso: calcola hash SHA-256 → esiste già? Sì → NON duplica, registra alias
   e avvisa il produttore (dedup). No → applica naming canonico, classifica per tipo.
2. Verifica regola repo ADR-004: binario pesante dentro monorepo? → alert immediato +
   indica destinazione corretta (Drive/locale). Non si committa.
3. Assegna retention dalla classe; intermedi senza classe dichiarata → default 30gg + warning.
4. Pulizia periodica (via SCHEDULING/WF-CRON): scaduti → cestino logico 7gg → eliminazione.
   Deliverable clienti: mai hard-delete senza ok umano.
5. Ogni registrazione finisce in `operations/assets` (AgentDB) per lookup veloce.

## Input / Output

**Asset in ingresso (registrazione):**
```json
{
  "path_originale": "...",
  "brand_kit": "DE|<cliente>",
  "ecosistema": "03-CONTENT-FACTORY",
  "commessa": "caroselli-q2",
  "classe": "render-intermedio",
  "retention_override": null
}
```

**Risposta registrazione:**
```json
{
  "asset_id": "ASS-YYYYMMDD-NNN",
  "path_canonico": "DE/03-CONTENT-FACTORY/caroselli-q2/render/20260611-nome.png",
  "hash": "sha256:...",
  "scadenza": "2026-07-11",
  "duplicato": false
}
```

## Gate di qualità

- `G-NAMING` — ogni asset ha path canonico prima di essere registrato
- `G-NO-REPO-BINARY` — alert immediato per binari pesanti nel monorepo
- `G-DEDUP` — hash check obbligatorio; nessun duplicato silenzioso

## KPI

| Metrica | Target |
|---|---|
| Asset senza path canonico | 0 a regime |
| Duplicati rilevati / duplicati totali | 100% (0 silenziosamente duplicati) |
| Asset fuori retention eliminati puntualmente | 100% |
| Lookup asset per commessa (tempo risposta) | ≤ 3s |
