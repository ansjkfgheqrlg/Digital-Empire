# Stage 8 — Packaging & Delivery

> Ultimo stadio. Assembla l'output finale in una forma consegnabile all'utente: cartella, zip, o `.skill` file.

## Obiettivo

Da `stage-06/output/<artifact-slug>/` produrre l'artefatto finale impacchettato, con README di handoff aggiornato e — se target è `skill` e l'ambiente lo richiede — un file `.skill` installabile.

## Agente

Nessun agente dedicato. Eseguito direttamente dal Conductor via script.

## Script principale

**`scripts/package_target.py`**:

```bash
python scripts/package_target.py <artifact_dir> [--zip] [--skill] [--out <path>]
```

Per `target=skill`, può anche invocare il packager ufficiale Anthropic:

```bash
python scripts/package_target.py <skill-dir> --skill --out packaged/
```

## Input attesi

```
<workspace>/forge-run-<ts>/stage-06/output/<artifact-slug>/
<workspace>/forge-run-<ts>/stage-07/qa-report.md   # solo se PASS o WARN
```

## Output canonici

```
<workspace>/forge-run-<ts>/stage-08/packaged/
├── <artifact-slug>/             # copia "clean" dell'output finale
│   └── ...
├── README.md                    # handoff: come usare, dove installare, qa summary
├── qa-summary.md                # estratto di qa-report.md per l'utente
└── (opzionale) <artifact-slug>.zip
└── (opzionale, solo skill) <artifact-slug>.skill
```

## Quando si attiva

Quando Stage 7 conclude con PASS o WARN (mai con FAIL).

## 🎁 Il MKD è SEMPRE incluso nel deliverable finale

Anche se l'utente ha chiesto target=agent/workflow/skill/altro, il deliverable finale include:
- L'artefatto richiesto (es. cartella `<agent-slug>/`)
- 🎁 **Il MKD bonus** (`master.md` + companion files): l'utente ottiene gratis il documento perfetto archiviabile

Questo perché il MKD è prodotto in Stage 4 indipendentemente — il costo cognitivo è già pagato.

`package_target.py` copia automaticamente `stage-04/master.md` & co in `packaged/<artifact>/master-knowledge-document/`.

## Quando si conclude

L'artefatto è presente in `stage-08/packaged/` ed è leggibile/installabile.

## Failure modes specifici

| Failure | Mitigazione |
|---|---|
| `package_target.py` errore I/O | Retry; se fail di nuovo, segnala all'utente |
| Skill packaging fallisce (per target=skill) | Mantieni l'output non-pacchettato; l'utente può comunque consumarlo manualmente |

## Output finale al Conductor

Il Conductor presenta all'utente:
1. Path dell'artefatto finale
2. `README.md` (sintesi: cosa è stato fatto, qa stats, come usarlo)
3. `qa-summary.md` (esito Stage 6)
4. Eventuali `next_suggestions` raccolti dai builder lungo il pipeline

## Note operative

- L'artefatto rimane disponibile anche fuori da `stage-07/`: l'utente può sempre tornare in `stage-06/output/` per la versione "lavorata".
- Il `.skill` packaging è SEMPRE opzionale: se Anthropic CLI non è disponibile, lo step viene saltato con WARN.
