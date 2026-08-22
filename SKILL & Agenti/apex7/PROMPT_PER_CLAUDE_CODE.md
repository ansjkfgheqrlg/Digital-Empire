# PROMPT DA INCOLLARE SU CLAUDE CODE - INSTALLAZIONE COMPLETA
# Copia TUTTO questo blocco e incollalo su Claude Code dopo avergli dato lo zip

---

## PROMPT PER CLAUDE CODE (ITALIANO - CHIRURGICO)

Sei il Setup Agent di Digital Empire - APEX-7 Ultra Grain 4K + Playwright Bridge.

**IL TUO COMPITO:** Estrarre completamente la cartella zippata che ti fornirò, installare tutte le dipendenze, configurare Playwright per Arena.ai, e rendere operativo il comando `/inizio-generazione`.

**CONTESTO:** Ti fornirò una directory zippata `apex7-ultra-grain-playwright-bridge.zip` (o simile) che contiene l'intero workspace APEX-7. Questa cartella DEVE essere estratta tutta, non solo alcuni file. Contiene:
- `playwright_bridge/` con arena_client.py, carousel_flow.py, cli.py, server.py, config.yaml
- `skills/carousel-machine/SKILL.md` V2 nero #000000 grain 35% + glow #FF3B1F
- `skills/claude-code-bridge/SKILL.md` che definisce /inizio-generazione
- `reference/STYLE_GUIDE.md` e reference images 8 slide
- `outputs/carousel/ref_v2_*.png` e `ultra_v3_*.png`
- `requirements_playwright.txt`
- `INSTALL_CLAUDE_CODE.md`

**ISTRUZIONI ESATTE - ESEGUI IN ORDINE:**

### FASE 1: ESTRAZIONE CARTELLA

1. Quando ti fornisco lo zip, chiedimi dove si trova o trova tu lo zip più recente in download / workspace.
2. Estrai TUTTA la cartella con:
```bash
unzip apex7-ultra-grain-playwright-bridge.zip -d ./
# oppure
tar -xzf apex7-ultra-grain-playwright-bridge.tar.gz
# Assicurati che la struttura sia:
# ./apex7/playwright_bridge/
# ./apex7/skills/
# ./apex7/reference/
# NON estrarre solo un sottofile, TUTTA la cartella
```
3. Verifica estrazione:
```bash
ls -R ./apex7/ | head -n 100
ls -lh ./apex7/playwright_bridge/
ls -lh ./apex7/skills/carousel-machine/
```
Devi vedere config.yaml, arena_client.py, carousel_flow.py, cli.py, server.py, SKILL.md

### FASE 2: INSTALL DIPENDENZE

4. Entra nella cartella apex7:
```bash
cd apex7
```

5. Installa dipendenze Playwright Bridge:
```bash
pip install -r requirements_playwright.txt
# Equivale a:
pip install playwright pyyaml fastapi uvicorn python-multipart pillow aiohttp numpy opencv-python
```

6. Installa browser Chromium per Playwright (FONDAMENTALE):
```bash
playwright install chromium
# Se fallisce prova:
playwright install --with-deps chromium
```

7. Verifica installazione:
```bash
python -c "import playwright; print('playwright ok')"
python -c "import yaml, fastapi; print('deps ok')"
playwright --version
```

### FASE 3: TESTA IL BRIDGE SENZA BROWSER (FALLBACK LOCALE)

8. Test rapido che il flusso /inizio-generazione generi copy + prompt + ZIP (senza aprire browser):
```bash
python -m playwright_bridge.cli --topic "Test installazione Content Factory" --no-playwright
```
Devi vedere:
- [FLOW] /inizio-generazione
- [STEP 1/4] Genero copy 8 slide
- [STEP 2/4] 8 ultra-quality prompts generated
- [STEP 3/4] ZIP Created ..._CAROSELLO.zip
- ✅ Carosello pronto!

Se vedi ERROR, leggi log e fixa dipendenze.

9. Verifica output:
```bash
ls -lh outputs/carousel/*_CAROSELLO.zip
unzip -l outputs/carousel/*_CAROSELLO.zip | head -n 20
```
Deve contenere: slide_01.png (prompt salvato), slide_01_prompt.txt, slides_copy.json, report.json

### FASE 4: TESTA CON PLAYWRIGHT VERO (BROWSER HEADLESS)

10. Solo se STEP 3 è ok, testa con browser vero su Arena.ai (headless):
```bash
python -m playwright_bridge.cli --topic "Test Playwright Arena" --model GPT-4o --headless
```
Se Arena richiede login o cambia UI, aggiorna `playwright_bridge/config.yaml` selectors. Il client prova fallback selectors automatico.

11. Per debug visivo (vedi browser aprirsi):
```bash
python -m playwright_bridge.cli --topic "Debug visivo" --model GPT-4o --no-headless
```

### FASE 5: REGISTRA COMANDO /inizio-generazione SU CLAUDE CODE

12. Ora registra il comando custom /inizio-generazione in Claude Code in modo che quando utente digita `/inizio-generazione` parta il flusso.

Se Claude Code supporta file in `~/.claude/commands/`:
```bash
mkdir -p ~/.claude/commands
cp skills/claude-code-bridge/SKILL.md ~/.claude/commands/inizio-generazione.md
# Oppure crea wrapper:
cat > ~/.claude/commands/inizio-generazione.md << 'ENDCMD'
---
name: inizio-generazione
description: Genera carosello Instagram 1080x1350 ultra grain 4K via Playwright Arena.ai bridge
trigger: /inizio-generazione, /inzio-generazione
run: python -m playwright_bridge.cli --interactive --model GPT-4o
---
ENDCMD
```

Se Claude Code usa `claude.json` o `settings.json`, aggiungi:
```json
{
  "custom_commands": {
    "/inizio-generazione": "cd /path/to/apex7 && python -m playwright_bridge.cli --interactive --model GPT-4o",
    "/inzio-generazione": "cd /path/to/apex7 && python -m playwright_bridge.cli --interactive --model GPT-4o"
  }
}
```

13. Verifica registrazione:
```bash
cat ~/.claude/commands/inizio-generazione.md
# oppure
grep -r "inizio-generazione" ~/.claude/
```

### FASE 6: TEST FINALE END-TO-END COME UTENTE

14. Simula utente che digita /inizio-generazione:
```bash
python -m playwright_bridge.cli --interactive --model GPT-4o
```
- Deve chiederti: "📌 Argomento (es. 'Content Factory per coach')"
- Inserisci: "Content Factory per coach e consulenti"
- Deve generare 8 slide copy + 8 prompt ultra grain + ZIP
- Alla fine: "📦 Scarica ZIP: .../outputs/carousel/..._CAROSELLO.zip"

15. Se hai server FastAPI attivo (opzionale):
```bash
uvicorn playwright_bridge.server:app --host 0.0.0.0 --port 8000 --reload &
curl -X POST http://localhost:8000/inizio-generazione -H "Content-Type: application/json" -d '{"topic": "Test API", "model": "GPT-4o"}'
curl http://localhost:8000/list
```

### FASE 7: QUALITÀ ULTRA GRAIN 4K - VERIFICA

16. Controlla che le immagini generate abbiano:
- Background #000000 con grain 38% su tutto
- Grain su ogni elemento: card dark 22%, card light 18%, testo bianco 5%, pill 12%, bottone 15%, logo 10%
- Risoluzione 2160x2700 source → 1080x1350 sharp ultra nitida
- Glow rosso #FF3B1F angolare blur 120px
- Pill mono border rgba(255,255,255,0.25) + icona rossa + footer 3/8 + logo E gradient

Confronta con reference in `reference/` e `outputs/carousel/ref_v2_*.png` - devono avere stessa grana e stessa nitidezza.

17. Se grana non abbastanza visibile: aumenta in `playwright_bridge/config.yaml`:
```yaml
carousel:
  grain_config:
    background_grain: 42
    element_grain: 20
```

### REPORT FINALE

18. Alla fine, dammi report:
- Estrazione: OK (lista file)
- Dipendenze: OK (playwright, yaml, fastapi)
- Browser Chromium: OK
- Test --no-playwright: OK con ZIP path
- Test Playwright headless: OK / FAIL con log
- Comando /inizio-generazione registrato: OK percorso
- Qualità ultra grain 4K verificata: OK

Se tutto OK, rispondi con "✅ INSTALLAZIONE COMPLETATA - /inizio-generazione operativo su Claude Code con ultra grain 4K + Playwright bridge Arena.ai"

**IMPORTANTE:** Estrai TUTTA la cartella, non solo alcuni file. Il workspace è interdipendente (orchestrator + memory + agents + playwright_bridge). Se estrai solo parte, il flusso fallirà.

---

## PROMPT CORTO (VERSIONE RAPIDA PER COPIA-INCOLLA VELOCE)

Se vuoi versione corta da incollare subito su Claude Code:

```
Ti fornirò uno zip apex7-ultra-grain-playwright-bridge.zip. ESTRAI TUTTA LA CARTELLA con unzip, entra in apex7/, installa pip install -r requirements_playwright.txt && playwright install chromium, testa python -m playwright_bridge.cli --topic "Test" --no-playwright deve creare ZIP in outputs/carousel/, poi registra comando /inizio-generazione e /inzio-generazione che lancia python -m playwright_bridge.cli --interactive --model GPT-4o. Verifica che generi 8 slide con grana ultra su ogni elemento (38% bg + 22% card + 5% testo + 12% pill + 15% bottone + 4K 2160x2700 sharp). Report finale con OK/FAIL per ogni fase. Estrai TUTTA la cartella, non solo file singoli.
```

---

## NOTE PER TE (UTENTE CHE FORNISCE ZIP)

1. Comprimi workspace: `cd /home/user && tar -czf apex7-ultra-grain-playwright-bridge.tar.gz apex7/` oppure `zip -r apex7-ultra-grain-playwright-bridge.zip apex7/`
2. Carica zip su Claude Code (drag & drop o path)
3. Incolla PROMPT LUNGO sopra a Claude Code
4. Claude estrarrà, installerà, testerà
5. Poi potrai digitare `/inizio-generazione` e ti chiederà argomento → genera carosello → ZIP download
```

