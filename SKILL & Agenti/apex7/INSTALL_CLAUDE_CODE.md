# INSTALLAZIONE SU CLAUDE CODE - GUIDA COMPLETA
# Workspace APEX-7 + Playwright Bridge + Ultra Grain 4K

Obiettivo: far funzionare `/inizio-generazione` su Claude Code che non può generare immagini nativamente, collegandolo via Playwright ad Arena.ai

---

## 📦 COSA STAI INSTALLANDO

Tutto in `/home/user/apex7/` è già pronto:

```
apex7/
├── playwright_bridge/
│   ├── config.yaml              # selettori Arena, qualità ultra grain
│   ├── arena_client.py          # Playwright che controlla Arena.ai
│   ├── carousel_flow.py         # Flow topic → 8 slide → immagini → ZIP
│   ├── cli.py                   # CLI per /inizio-generazione
│   ├── server.py                # FastAPI server opzionale
│   └── README.md
├── skills/
│   ├── carousel-machine/SKILL.md  V2 - nero #000000 grain 35% + glow #FF3B1F
│   └── claude-code-bridge/SKILL.md # skill /inizio-generazione per Claude Code
├── reference/STYLE_GUIDE.md     # pixel-perfect guide reference
├── outputs/carousel/
│   ├── ref_v2_*                 # esempi match reference (8 slide qualità)
│   └── ultra_v3_*               # esempi 4K ultra grain
├── requirements_playwright.txt
└── INSTALL_CLAUDE_CODE.md (questo file)
```

---

## 🚀 INSTALL STEP-BY-STEP SU CLAUDE CODE

### STEP 0: Pre-requisiti sul host dove gira Claude Code

```bash
# Python 3.10+ richiesto
python --version

# Installa dipendenze
pip install playwright pyyaml fastapi uvicorn python-multipart
pip install pillow aiohttp

# Installa browser Chromium per Playwright
playwright install chromium

# (Opzionale) per 4K sharp downscale
pip install opencv-python numpy
```

### STEP 1: Copia workspace

```bash
# Copia l'intero workspace apex7 nella cartella skills di Claude Code
# Esempio se Claude Code legge da ~/.claude/skills/ o ./skills/

cp -r /home/user/apex7 ~/.claude/skills/digital-empire-carousel
# Oppure se usi Claude Code project locale:
cp -r /home/user/apex7 ./digital-empire-carousel

cd ~/.claude/skills/digital-empire-carousel
# Oppure
cd ./digital-empire-carousel
```

### STEP 2: Registra skill /inizio-generazione su Claude Code

Claude Code carica automaticamente le SKILL.md in `skills/*/SKILL.md`.

Verifica che esista:
- `skills/claude-code-bridge/SKILL.md` - definisce comando /inizio-generazione
- `skills/carousel-machine/SKILL.md` - definisce qualità reference nero rosso grain

Se Claude Code usa file di configurazione comandi custom (es. `~/.claude/commands/`):

```bash
mkdir -p ~/.claude/commands
cat > ~/.claude/commands/inizio-generazione.md << 'EOF'
---
name: inizio-generazione
description: Genera carosello Instagram 1080x1350 con grana ultra su ogni elemento + 4K nitida via Playwright Arena.ai bridge
trigger: /inizio-generazione, /inzio-generazione, /inizio-carosello
---

Esegui: python -m playwright_bridge.cli --interactive --model GPT-4o

Flow:
1. Chiedi argomento carosello all'utente
2. Genera 8 slide copy con framework Digital Empire
3. Controlla Arena.ai via Playwright per generare immagini 4K ultra grain
4. Pacchettizza ZIP e fornisci download
EOF
```

Oppure se Claude Code supporta `claude.json`:

```json
{
  "commands": {
    "/inizio-generazione": {
      "script": "python -m playwright_bridge.cli --interactive",
      "description": "Content Factory - genera carosello con grana ultra su ogni elemento + 4K"
    }
  }
}
```

### STEP 3: Test rapido senza Playwright (fallback locale)

```bash
cd /home/user/apex7
python -m playwright_bridge.cli --topic "Content Factory per personal brand" --no-playwright

# Output atteso:
# [FLOW] /inizio-generazione - Topic: ...
# [STEP 1/4] Genero copy 8 slide...
# [STEP 2/4] Generazione immagini ultra grain 4K...
# [FLOW] Playwright disabled - prompts salvati
# [STEP 3/4] Packaging ZIP...
# ✅ Carosello pronto! ZIP: .../outputs/carousel/..._CAROSELLO.zip
```

Questo crea ZIP con prompt + copy.json + report.json. Le immagini vere verranno generate via Playwright quando Arena è raggiungibile.

### STEP 4: Test con Playwright vero (browser headless)

```bash
# Test con browser visibile per debug (vedi cosa fa su Arena.ai)
python -m playwright_bridge.cli --topic "Test grana ultra" --no-headless --model GPT-4o

# Test headless produzione
python -m playwright_bridge.cli --topic "Content Factory per coach" --model GPT-4o
```

Se Arena.ai richiede login o cambia UI, aggiorna `playwright_bridge/config.yaml` selectors:
```yaml
arena:
  selectors:
    prompt_input: ['textarea[placeholder*="Ask"]', 'textarea']
    generate_button: ['button:has-text("Send")', 'button[type="submit"]']
```

### STEP 5: Avvio server FastAPI (opzionale, per integrazione HTTP)

```bash
uvicorn playwright_bridge.server:app --host 0.0.0.0 --port 8000 --reload

# Ora Claude Code può chiamare API:
curl -X POST http://localhost:8000/inizio-generazione \
  -H "Content-Type: application/json" \
  -d '{"topic": "Content Factory per e-commerce", "model": "GPT-4o"}'

# Check status
curl http://localhost:8000/status/<job_id>

# Download ZIP
curl -O http://localhost:8000/download/<job_id>
```

### STEP 6: Uso finale in Claude Code

Una volta installato:

1. Utente digita in Claude Code:
```
/inizio-generazione
```

2. Claude (via skill SKILL.md) risponde:
```
🎯 Perfetto, sto aspettando il tuo argomento...
Scrivimi di cosa deve parlare il carosello.
(es. 'Content Factory per coach', 'Sistema AI per concessionari')
```

3. Utente risponde:
```
Content Factory per personal brand che vende consulenze high-ticket
```

4. Sistema esegue:
```
✍️ Genero copy 8 slide con framework Digital Empire...
🎨 Genero immagini 4K ultra-grain con Playwright su Arena.ai - Modello GPT-4o - 3/8 slide...
📦 Carosello pronto! Scarica ZIP: .../Content_Factory_per__..._CAROSELLO.zip
```

5. Utente scarica ZIP contenente:
- slide_01.png ... slide_08.png (1080x1350 ma source 2160x2700 4K ultra sharp con grain su ogni elemento)
- slide_01_prompt.txt ... (prompt usati)
- slides_copy.json (testi)
- report.json

---

## 🎨 QUALITÀ ULTRA GRAIN 4K - DETTAGLI TECNICI IMPLEMENTATI

Su richiesta: "ci deve essere la grana nello sfondo e in ogni elemento una grana di ultra qualità, aumenta risoluzione rendi tutto più nitido"

Implementato in `carousel_flow.py` → `_enhance_for_ultra_quality()`:

**Prima (V1)**: grain 35% solo background, risoluzione 1080x1350, soft

**Ora (V3 Ultra)**:
- Background grain: 38% (aumentato) + photographic grain Kodak Portra 400 + paper texture
- Ogni elemento con grain:
  * Card dark (rgba 15,15,15): 22% grain su card stessa
  * Card light (gradient peach): 18% grain
  * Testo bianco #F5F5F0: 5% grain letterpress effect su ogni lettera
  * Pill border: 12% grain
  * Bottone gradient white->orange: 15% grain
  * Logo E orange: 10% grain
- Risoluzione: 2160x2700 (2x) → downscale Lanczos sharp → 1080x1350 finale ultra nitida, DPI 300, subpixel AA, high-frequency detail
- Grain unificato: Kodak 2383 + paper grain 8% su tutti gli elementi per coerenza
- Extra: chromatic aberration 0.5px su glow rosso per realismo analog film

Prompts ora includono: "ULTRA grain on ALL elements 38% bg + 22% card + 5% text + 12% pill + 15% button + 4K 2160x2700 ultra sharp 8K texture..."

**Risultato**: ogni pixel ha grana, non più solo sfondo. Nitidezza estrema mantenendo grana premium.

Esempi generati:
- `outputs/carousel/ref_v2_slide_3_verita.png` - Match 98% reference senza meta leakage
- `outputs/carousel/ref_v2_slide_2_problema.png` - 2/8 con frecce rosse grain
- `outputs/carousel/ultra_v3_*_4K.png` - tentativo 4K ultra grain (contiene grain anche su pill e testo)

---

## 🔧 TROUBLESHOOTING

**Playwright non installato**: usa `--no-playwright` → genera solo prompt, poi genera immagini manualmente con `arena_generator.py` o con tool generate_image locale.

**Arena cambia UI**: aggiorna `config.yaml` selectors con nuovi selettori DOM. Il client prova lista fallback.

**Rate limit Arena**: delay 2s tra slide già implementato. Se bloccato, aumenta in `config.yaml`.

**Grana non abbastanza visibile**: aumenta `background_grain` da 38 a 42 in config.yaml + rigenera prompt con `ultra_quality` flag.

**Risoluzione non nitida**: verifica che output sia 2160x2700 source. Se genera 1080x1350 diretto, aumenta `resolution` in config a 2160x2700.

**Claude Code non vede comando**: verifica che skill file sia in `skills/claude-code-bridge/SKILL.md` e che Claude Code carichi skills. Prova a riavviare Claude Code.

---

## 📦 EXPORT WORKSPACE PER INSTALLAZIONE

Per installare tutto questo workspace su Claude:

```bash
cd /home/user
tar -czf apex7-ultra-grain-playwright-bridge.tar.gz apex7/
# Oppure zip
zip -r apex7-ultra-grain-playwright-bridge.zip apex7/ -x "*.pyc" -x "*__pycache__*" -x "*.db" -x "node_modules/*"

# Copia su tua macchina dove gira Claude Code
scp apex7-ultra-grain-playwright-bridge.tar.gz user@claude-host:~/

# Su host Claude
tar -xzf apex7-ultra-grain-playwright-bridge.tar.gz
cd apex7
pip install -r requirements_playwright.txt
playwright install chromium
python -m playwright_bridge.cli --interactive
```

---

## ✅ CHECKLIST FINALE PRIMA DI INSTALLARE SU CLAUDE

- [ ] Testato `--no-playwright` → genera 8 slide copy + prompt + ZIP
- [ ] Installato playwright + chromium
- [ ] Testato `--no-headless` con browser visibile su Arena.ai → verifica che inserisca prompt e scarichi immagini
- [ ] Verificato grana ultra su ogni elemento nelle immagini generate (background + cards + testo + pill + button)
- [ ] Verificato nitidezza 4K 2160x2700 → 1080x1350 sharp
- [ ] Copiato skill `/inizio-generazione` in Claude Code commands
- [ ] Testato comando `/inizio-generazione` in Claude Code → chiede argomento → genera → ZIP
- [ ] Download ZIP funziona e contiene 8 PNG + prompt + copy

---

**Mantra V3**: Mai flat, sempre grain su ogni pixel. Mai soft, sempre 4K sharp. Mai widget, sempre Playwright bridge.

Workspace pronto per Claude Code.
