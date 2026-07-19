# Empire Desk

Un solo `.exe` Windows = la plancia di comando di Digital Empire. Ogni tile lancia con un
click un'automazione REALE già esistente nel monorepo (ADR-003: wrapper, mai riscrittura).

Spec vincolante: `PIANO-MAESTRO/17-EMPIRE-DESK-APP.md`. Errori/lezioni: `REGISTRO-ERRORI.md`.

## Architettura in breve

- `app.py` — un solo file: registro tile (`TILES`), gestore subprocess (`TileManager`),
  bridge HTTP locale (`_Handler`), 3 motori GUI in ordine di fallback:
  1. **Chrome-app**: server HTTP locale su `127.0.0.1:<porta libera>` + finestra
     `chrome.exe --app=http://127.0.0.1:<porta>/`. Non dipende da WebView2.
  2. **pywebview**: se Chrome non è installato. Espone `_WebApi` come `js_api`.
  3. **Tkinter**: fallback finale, GUI minimale a bottoni (nessun PC resta senza app).
- `ui/index.html` — un solo file HTML/CSS/JS, con un piccolo bridge dual-mode: se gira dentro
  pywebview usa `window.pywebview.api.*`, altrimenti (finestra Chrome-app) usa `fetch('/api/...')`.
  Stessa UI, motore indifferente.
- Ogni tile = `{id, icon, name, desc, kind, cmd, cwd, input}`. `kind: "readonly"` (solo STATO
  Empire) non lancia processi, legge un file.

## Path e portabilità

`REPO_ROOT` si risolve risalendo da `app.py`/`EmpireDesk.exe` cercando le cartelle marcatore
`PIANO-MAESTRO/` e `company/` (radice del monorepo Digital Empire). L'app **deve restare
dentro il repo** (non è portabile su un altro PC senza il monorepo): lancia automazioni che
vivono in `Outreach/`, `Clienti/`, `Workfolw crea caroselli à/`, ecc.

## Sviluppo

```
pip install -r requirements.txt
python app.py                 # avvia con fallback automatico dei 3 motori
python app.py --selftest      # verifica che le 8 tile siano lanciabili (NON lancia nulla)
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
