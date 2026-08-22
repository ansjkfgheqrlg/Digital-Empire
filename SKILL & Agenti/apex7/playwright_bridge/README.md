# Playwright Bridge - Claude Code ↔ Arena.ai - Ultra Grain 4K

Questo bridge permette a **Claude Code**, che non può generare immagini nativamente, di controllare Arena.ai via Playwright e generare caroselli con **grana ultra quality su ogni elemento + 4K nitida**.

## Architettura

```
Claude Code User
   |
   | Digita /inizio-generazione
   v
CLI (playwright_bridge/cli.py)  O  Server FastAPI (playwright_bridge/server.py)
   |
   | Topic: "Content Factory per coach"
   v
APEX-7 CarouselFlow (carousel_flow.py)
   - PlannerAgent + WriterAgent generano 8 slide copy (framework Digital Empire)
   - WriterAgent genera 8 prompt immagine con ultra grain 38% bg + 15-22% su ogni elemento
   - 4K resolution 2160x2700 sharp
   |
   | 8 prompt ultra grain
   v
ArenaPlaywrightClient (arena_client.py)
   - Avvia browser Chromium headless via Playwright
   - Naviga su https://arena.ai
   - Seleziona modello GPT-4o
   - Per ogni prompt: inserisce in textarea, clicca Generate, aspetta immagine, scarica
   - Fallback: se Playwright non disponibile o Arena non raggiungibile, salva prompt per generazione locale
   |
   v
Output: outputs/carousel/<topic>_<timestamp>/
   - slide_01.png ... slide_08.png (2160x2700 4K, ultra grain su ogni elemento)
   - slide_01_prompt.txt (prompt usato)
   - slides_copy.json (copy 8 slide)
   - report.json
   + ZIP pack: <topic>_<timestamp>_CAROSELLO.zip per download
```

## Installazione su Claude Code (workspace completo)

Quando avrai finito, installerai tutto questo workspace su Claude. Ecco come:

### 1. Installa dipendenze Playwright sul tuo sistema Claude

```bash
cd /home/user/apex7
pip install -r requirements_playwright.txt  # creato sotto
pip install playwright pyyaml fastapi uvicorn
playwright install chromium
```

### 2. Configura Claude Code Skill

File `skills/claude-code-bridge/SKILL.md` contiene definizione skill per Claude Code.
Copia workspace in `~/.claude/skills/digital-empire-carousel/` o dove Claude Code legge skills.

Claude Code leggerà automaticamente il comando `/inizio-generazione`.

### 3. Uso - Metodo 1: CLI Interattivo (simula /inizio-generazione)

```bash
# Modalità interattiva - ti chiede argomento
python -m playwright_bridge.cli --interactive --model GPT-4o

# Oppure diretto
python -m playwright_bridge.cli --topic "Content Factory per coach e consulenti" --model GPT-4o
```

Flusso CLI:
```
🎯 /inizio-generazione attivato
👋 Ciao! Sono la Content Factory...
📌 Argomento: Content Factory per coach
✅ Argomento ricevuto...
✍️ Genero copy 8 slide...
🎨 Genero immagini 4K ultra-grain con Playwright...
📦 Carosello pronto! Scarica ZIP: ...
```

### 4. Uso - Metodo 2: Server FastAPI (per integrazione avanzata Claude Code)

```bash
uvicorn playwright_bridge.server:app --host 0.0.0.0 --port 8000 --reload
# Apre http://localhost:8000
```

Poi Claude Code può chiamare:
```bash
curl -X POST http://localhost:8000/inizio-generazione \
  -H "Content-Type: application/json" \
  -d '{"topic": "Content Factory per coach", "model": "GPT-4o"}'

# Risposta: {"job_id": "a1b2c3d4", "status": "queued", ...}

# Controlla stato
curl http://localhost:8000/status/a1b2c3d4

# Download ZIP quando completato
curl -O http://localhost:8000/download/a1b2c3d4
```

### 5. Uso - Metodo 3: Direttamente in Claude Code come Custom Command

Se Claude Code supporta custom commands `/`:

1. Vai in Claude Code settings → Custom Commands
2. Aggiungi comando `/inizio-generazione` con action: `python /path/to/apex7/playwright_bridge/cli.py --interactive`
3. Ora quando digiti `/inizio-generazione` in Claude Code, lui esegue il bridge e ti chiede argomento, genera carosello, e ti dà ZIP da scaricare

## Qualità Ultra Grain 4K - Novità V2

Richiesta: "ci deve essere la grana nello sfondo e in ogni elemento una grana di ultra qualità, aumenta risoluzione rendi tutto più nitido"

Implementato in `carousel_flow.py` → `_enhance_for_ultra_quality()`:

- **Background grain**: 38% (prima 35%) + photographic grain Kodak Portra overlay
- **Element grain**: NUOVO
  - Card dark: 22% grain sulla card stessa
  - Card light: 18% grain su gradient peach
  - Testo bianco: 5% grain su ogni lettera (effetto letterpress)
  - Pill: 12% grain su bordo e background
  - Bottone: 15% grain su gradient
  - Logo E: 10% grain
- **Risoluzione**: 2160x2700 = 2x di 1080x1350, poi downscale Lanczos per nitidezza estrema, DPI 300, subpixel anti-aliasing, ultra sharp focus, crisp edges
- **Grain unificato**: stessa tipologia Kodak 2383 + paper grain 8% su tutti gli elementi per coerenza
- **Extra**: chromatic aberration 0.5px sui bordi glow rosso per realismo analog film

Prompts generati includono ora: "ULTRA grain on ALL elements background cards text buttons 38% bg + 22% card + 5% text + 4K 2160x2700 ultra sharp 8K texture..."

## File del bridge

- `config.yaml` - Config selettori Arena, qualità grain, messaggi Claude Code
- `arena_client.py` - Playwright client con fallback lista selettori, gestione base64/blob/http images, retry
- `carousel_flow.py` - Flow completo topic→copy→images→zip
- `cli.py` - CLI per /inizio-generazione interattivo e diretto
- `server.py` - FastAPI server con endpoint /inizio-generazione, /status, /download
- `requirements_playwright.txt` (da creare)

## Troubleshooting

- Se Arena cambia UI, aggiorna `config.yaml` selectors
- Se Playwright non installato, usa `--no-playwright` per modalità fallback (salva solo prompt, genera immagini via `apex7/outputs/carousel/ref_v2_*.png` con generate_image tool)
- Se vuoi vedere browser: `--no-headless`
- Log in `outputs/carousel/<topic>/report.json`

## Prossimi passi per installazione su Claude

1. Testa localmente: `python -m playwright_bridge.cli --topic "test" --no-playwright` (genera prompt senza browser)
2. Installa playwright: `playwright install chromium`
3. Testa con browser visibile: `python -m playwright_bridge.cli --topic "test" --no-headless --model GPT-4o`
4. Copia intero workspace `/home/user/apex7` in Claude Code skills folder
5. Registra comando `/inizio-generazione`
6. Lancia da Claude Code e verifica flusso topic → copy → Arena generation → ZIP download
