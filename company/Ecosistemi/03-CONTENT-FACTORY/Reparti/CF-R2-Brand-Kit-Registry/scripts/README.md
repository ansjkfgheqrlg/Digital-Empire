---
Type: SCRIPTS
Status: Active
Tags: #scripts #content-factory #CF-R2 #brand-kit #validator #drift #canva
Created: 2026-06-19
Last updated: 2026-06-19
---

# Script CF-R2 — Brand-Kit & Tenant Registry

> Wrapper carousel-factory + 3 script deterministici per le operazioni CF-R2.
> ADR-003: i file in `carousel-factory/brands/` non vengono mai modificati da questi script.

---

## Wrapper carousel-factory (ADR-003)

I 4 brand seed esistono in `carousel-factory/brands/` come asset del motore v1 (caroselli
HTML/CSS + render Puppeteer). CF-R2 non modifica né quella cartella né i suoi file.

Lo script `brandkit-from-seed.py` è il bridge in sola lettura:

```
carousel-factory/brands/<slug>/config.json
        ↓ (lettura read-only, mai scritto)
brandkit-from-seed.py
        ↓ (trasformazione formato v1 → CF-grade)
brands/<slug>/brand-kit.json (file NUOVO nel registry CF-R2)
```

**Mapping v1 → CF-grade (`brandkit-from-seed.py`):**

| Campo config.json v1 | Campo brand-kit.json CF-grade |
|---|---|
| `brand_name` | `slug` |
| `display_name` | `nome` |
| `instagram` | `handle.ig` |
| `colors.background` | `visual.palette.bg` |
| `colors.accent_1` | `visual.palette.primary` |
| `colors.accent_2` | `visual.palette.accent` |
| `typography.font_hero` | `visual.font.display` |
| `typography.font_regular` | `visual.font.body` |
| `logo.show` (se true) | `visual.logo` → path assets/logo.png se esiste |

Campi assenti nel config v1 (voice, soul_id, icp, canali): impostati a `null` con
nota in `state.json`; richiedono brief committente per completamento.

**Uso:**
```bash
python scripts/brandkit-from-seed.py --slug mentalita-brutale --dry-run
python scripts/brandkit-from-seed.py --slug mentalita-brutale
```

`--dry-run`: produce l'output in stdout senza scrivere nessun file.

---

## Script 1: `brandkit-validator.py` — Validatore schema brand_kit

**Funzione:** esegue la stessa checklist di CF-R2-QA in modalità CLI — utile per
verificare un brand_kit prima di sottometterlo al gate, o per debug di un FAIL.

**Controlla:**
- Schema completo (tutti i campi obbligatori presenti e non null)
- Palette HEX valide (regex `#[0-9A-Fa-f]{6}`)
- Voice: esempi_si e esempi_no ≥2 ciascuno, non pari al segnaposto del template
- Font: display e body dichiarati
- Canali: tipo e publisher presenti, review_umana booleano
- icp.json: dolori/desideri/obiezioni array ≥1, awareness_level e linguaggio presenti

**Output:** exit code 0 (PASS) + riepilogo campi, oppure exit code 1 (FAIL) + lista errori.

**Uso:**
```bash
python scripts/brandkit-validator.py --slug mentalita-brutale
python scripts/brandkit-validator.py --slug manuale-cc --icp brands/manuale-cc/icp.json
```

**Implementazione target:**
```python
# brandkit-validator.py — struttura logica
import json, re, sys
from pathlib import Path

HEX_RE = re.compile(r'^#[0-9A-Fa-f]{6}$')
REQUIRED_FIELDS = ['slug', 'nome', 'handle', 'visual', 'voice', 'soul_id', 'canali']
TEMPLATE_PLACEHOLDERS = ['frasi conformi...', 'frasi bandite...', 'segnaposto non sostituito']

def validate_brand_kit(slug: str) -> dict:
    path = Path(f'brands/{slug}/brand-kit.json')
    errors = []
    # 1. file exists and parsable
    # 2. required fields present
    # 3. palette HEX validation
    # 4. voice examples not equal to template placeholders
    # 5. canali validation
    return {'gate': 'PASS' if not errors else 'FAIL', 'errors': errors}
```

---

## Script 2: `drift-sampler.py` — Campionatore brand-drift

**Funzione:** esegue il campionamento di CF-R2-DRIFT in modalità CLI su un batch di
output file. Confronta palette, voice e font degli output vs il brand_kit del tenant.
Produce un report JSON con le deviazioni rilevate.

**Usa:** per verificare manualmente il drift su un set di output, o per eseguire il
campionamento in modalità schedulata (cron).

**Uso:**
```bash
python scripts/drift-sampler.py --slug mentalita-brutale --output-dir orders/CF-2026-0031/output/
python scripts/drift-sampler.py --slug mentalita-brutale --min-sample 5
```

**Output:** file `drift-report-<slug>-<date>.json` in `brands/<slug>/drift-reports/`
con la stessa struttura dell'output CF-R2-DRIFT.

**Implementazione target:**
```python
# drift-sampler.py — struttura logica
# 1. Carica brand-kit.json per lo slug
# 2. Raccoglie ≥5 file output dalla directory indicata
# 3. Per ogni file HTML: estrae HEX via regex; confronta con palette
# 4. Per ogni file testo: cerca parole_vietate; verifica tono
# 5. Per ogni HTML: controlla font-family nel CSS
# 6. Aggrega deviazioni; emette JSON report; exit 0 se nessuna deviazione, 1 se alert
```

---

## Script 3: `canva-sync.py` — Sincronizzazione brand kit Canva

**Funzione:** esegue la sync brand_kit → Canva in modalità CLI, replicando la logica
di CF-R2-CANVA. Richiede le credenziali MCP Canva configurate nell'ambiente.

**Prerequisito:** gate CF-R2-QA deve essere PASS (verificato dal validator prima di
avviare la sync; blocca se `state.json` non riporta `gate_qa: "PASS"`).

**Uso:**
```bash
python scripts/canva-sync.py --slug mentalita-brutale --operation create
python scripts/canva-sync.py --slug manuale-cc --operation update
python scripts/canva-sync.py --slug vendi-la-skill --dry-run
```

`--dry-run`: simula le chiamate MCP Canva senza eseguirle; stampa le operazioni che
verrebbero eseguite.

**Output:** aggiorna `brands/<slug>/canva/template_ids.json` e `brands/<slug>/state.json`
con `ultima_sync_canva`. In caso di errore API Canva: stampa codice errore e azione
richiesta senza modificare i file.

---

## Note operative

- Tutti gli script operano in `brands/` (cartella CF-R2 registry). Non accedono
  mai a `carousel-factory/` tranne `brandkit-from-seed.py` in sola lettura.
- Log degli script: `brands/<slug>/state.json` (aggiornato) + stdout strutturato.
- In caso di errore critico (file corrotto, permessi mancanti): exit code 2 con
  descrizione specifica — nessuno script fa "silent fail".

---

## Connessioni

- [[cf-r2-creator]] · `agenti/cf-r2-creator.md` — usa logica brandkit-from-seed
- [[cf-r2-drift]] · `agenti/cf-r2-drift.md` — logica drift-sampler
- [[cf-r2-canva]] · `agenti/cf-r2-canva.md` — logica canva-sync
- [[ARCHITETTURA]] · `ARCHITETTURA.md` — schema brand_kit e struttura brands/<slug>/
