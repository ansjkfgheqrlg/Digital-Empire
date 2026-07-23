# Empire Desk — System Tray Command Center

Command Center ultra-minimalista per Windows: un'app **System Tray** (barra
in basso a destra) che funge da launcher per i tuoi script di automazione.
L'interfaccia non è ingombrante: tutto avviene dall'icona nella tray.

## Caratteristiche
- **Menu dinamico** generato da `workflows.json` (oggetti con `name` + `script_path`).
- **Esecuzione non bloccante** via `QProcess` (processo OS separato): la UI non si freeza mai.
- **Toast nativi** della System Tray ad avvio/errore/completamento.
- **Auto-reload** del menu quando `workflows.json` cambia (`QFileSystemWatcher`).
- **Limiti & coda**: `max_concurrent` configurabile; i lanci in eccesso vengono accodati.
- **Stop live**: clicca un workflow attivo per fermarlo (`proc.kill()`).
- **Icona animata** (spinner) quando ci sono workflow in esecuzione.
- **Logging su file** (`empire_desk.log`) di ogni esecuzione.
- **🧠 Genera Prompt (APEX-7)**: voce di menu che pilota l'Orchestrator `apex7`
  (in background, non blocca la tray) e mostra il risultato, persistendolo in
  `apex7_memory.db`. Richiede la cartella `apex7/` accanto a `empire_desk.py`.

## Requisiti
- Python >= 3.9
- PySide6 >= 6.5 (unica dipendenza)

## Installazione / Avvio (sviluppo)
```bash
pip install PySide6
python empire_desk.py
```
Clic destro sull'icona "E" nella tray per aprire il menu.

## Configurazione (`workflows.json`)
```json
{
  "settings": {
    "log_file": "empire_desk.log",   // "" o omesso -> nessun log su file
    "python": "auto",               // "auto" = interprete corrente, o un path
    "auto_reload": true,            // ricarica il menu su modifica file
    "max_concurrent": 2             // max workflow paralleli
  },
  "workflows": [
    {
      "name": "Pulizia Log",
      "script_path": "scripts/clean_logs.py",
      "args": ["--verbose"],        // opzionale
      "cwd": "scripts",             // opzionale (relativo allo script)
      "enabled": true               // opzionale (default true)
    }
  ]
}
```
*Il formato legacy (lista diretta di oggetti) resta supportato.*

## Packaging (distribuzione Windows)
```bash
pip install pyinstaller
pyinstaller build.spec
```
Genera `dist/EmpireDesk/` — un eseguibile standalone `EmpireDesk.exe` in
modalità windowed (niente console), già con `workflows.json` e `scripts/` inclusi.

## Struttura
```
EmpireDesk/
├── empire_desk.py      # App completa (PySide6)
├── workflows.json      # Configurazione workflow
├── scripts/            # I tuoi script di automazione
├── pyproject.toml      # Metadati / entry point
├── build.spec          # PyInstaller
└── README.md
```
