# Empire Desk

Un solo `.exe` Windows = la plancia di comando di Digital Empire. Ogni tile lancia con un
click un'automazione REALE già esistente nel monorepo (ADR-003: wrapper, mai riscrittura).

Spec vincolante: `PIANO-MAESTRO/17-EMPIRE-DESK-APP.md`. Errori/lezioni: `REGISTRO-ERRORI.md`.

## Architettura in breve

- `app.py` — un solo file: registro tile core (`_CORE_TILES`), loader moduli (`_load_modules`),
  gestore subprocess (`TileManager`), bridge HTTP locale (`_Handler`), 3 motori GUI in ordine
  di fallback:
  1. **Chrome-app**: server HTTP locale su `127.0.0.1:<porta libera>` + finestra
     `chrome.exe --app=http://127.0.0.1:<porta>/`. Non dipende da WebView2.
  2. **pywebview**: se Chrome non è installato. Espone `_WebApi` come `js_api`.
  3. **Tkinter**: fallback finale, GUI minimale a bottoni (nessun PC resta senza app; NON mostra
     i pannelli dei moduli — solo le tile lanciabili — limite accettato per un fallback di riserva).
- `ui/index.html` — un solo file HTML/CSS/JS, con un piccolo bridge dual-mode: se gira dentro
  pywebview usa `window.pywebview.api.*`, altrimenti (finestra Chrome-app) usa `fetch('/api/...')`.
  Stessa UI, motore indifferente. `edApi(route, payload)` è il bridge generico usato dai pannelli
  dei moduli (globale, perché il loro HTML è iniettato via `innerHTML`).
- Ogni tile = `{id, icon, name, desc, kind, script, cwd, input}` (core o da modulo). `kind:
  "readonly"` (solo STATO Empire) non lancia processi, legge un file.

## B1 — Seam moduli (dopo B0, CORE ORA IN FREEZE)

Dopo B0/B1, `app.py`/`ui/index.html` **non si toccano più**: ogni funzionalità nuova (B2/B3/B4
di Gael, A1-A4 di Max, dossier 17 §5) entra SOLO come file in `EmpireDesk/modules/<nome>.py`,
contratto (dossier 17 §5.3):

```python
MODULE = {
    "id": "metrics",                    # univoco, mai uguale a un'altra tile/modulo
    "tile": {...} | None,               # opzionale: tile aggiuntiva nel grid (schema come sopra)
    "routes": {"metrics/summary": fn},  # fn(payload: dict) -> dict, montate su POST /api/<route>
    "panel_html": "<div class='panel'>…</div>",  # opzionale: pannello nello switcher UI
}

def selftest() -> tuple[bool, str]: ...  # entra nel selftest globale — MAI lanci reali qui
```

- Il loader (`_load_modules()` in `app.py`) scandisce `modules/*.py` a ogni avvio, importa ognuno
  in isolamento: **un modulo rotto (import fallito, `MODULE` malformato, tile con schema
  sbagliato, route duplicata) si segnala nel selftest e si salta — non fa mai cadere il resto
  dell'app**, incluse le tile core.
- Classi CSS disponibili per `panel_html` (già definite in `ui/index.html`, palette coerente):
  `.panel`, `.panel h2`, `.panel .hint`, `.panel .btn`, `.panel .inp`, `.panel .log-pane`.
- Bottone header "Pannelli" apre lo switcher (tab per modulo con `panel_html`); "Selftest"
  ora include anche il selftest di ogni modulo caricato + i moduli scartati per errore.
- **Regola anti-collisione (dossier 17 §5.4):** Gael possiede `app.py`/`ui/index.html` +
  `modules/scheduler.py` (B2) `modules/notify.py` (B3) `modules/taskboard.py` (B4). Max possiede
  `modules/metrics.py` `modules/revenue.py` `modules/licenze.py` `modules/fliki.py` (A1-A4).
  Nessuno tocca i moduli dell'altro.

## Path e portabilità

`REPO_ROOT` si risolve risalendo da `app.py`/`EmpireDesk.exe` cercando le cartelle marcatore
`PIANO-MAESTRO/` e `company/` (radice del monorepo Digital Empire). L'app **deve restare
dentro il repo** (non è portabile su un altro PC senza il monorepo): lancia automazioni che
vivono in `Outreach/`, `Clienti/`, `Workfolw crea caroselli à/`, ecc.

## Sviluppo

```
pip install -r requirements.txt
python app.py                 # avvia con fallback automatico dei 3 motori
python app.py --selftest      # verifica tile (core+moduli) + selftest dei moduli (NON lancia nulla)
```

## Build .exe

```
build_exe.bat
```
Output: `dist/EmpireDesk/EmpireDesk.exe` — copiare l'intera cartella `dist/EmpireDesk/`
DENTRO il repo (es. `EmpireDesk/dist/EmpireDesk/`) prima di usarla, non altrove.

## Tile v0.1 (8)

| Tile | Lancia |
|---|---|
| Outreach Email | `Outreach/AVVIA-EMAIL-LIVE.bat` |
| Outreach Instagram | `Outreach/Instagram Automation/_avvia_ig.bat` |
| LinkedIn | `Outreach/LinkedIn Automation/run_daily.bat` |
| Scraper Lead | `Outreach/Outreach Workflow/scrape_only.py` |
| PreventivoForge | `Clienti/Prof Autocad/preventivo-forge/avvia-app.bat` |
| Caroselli | `Workfolw crea caroselli à/carousel-factory` → `node scripts/generate.js` |
| Empire Studio | `SKILL & Agenti/Empire Studio Suite/empire-studio/scripts/yt_ingest.py <url>` |
| STATO Empire | `company/Memory/STATO-EMPIRE.md` (sola lettura) |

## Roadmap (dossier 17 §3)
- P5: scheduler run programmate, metriche settimana, notifiche fine-run.
- P6: licenze concessionari, pannello revenue, tile Fliki/WF-YT.
