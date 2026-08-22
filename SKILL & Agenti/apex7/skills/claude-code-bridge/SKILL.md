---
name: claude-code-bridge-inizio-generazione
description: Bridge Playwright che collega Claude Code (che non può generare immagini) ad Arena.ai per generare caroselli Instagram 1080x1350 con standard reference Digital Empire nero grain rosso - comando /inizio-generazione che attende argomento, genera copy 8 slide, controlla Arena via Playwright, e fornisce ZIP scaricabile con grana ultra quality su ogni elemento + 4K nitida.
---

# OBIETTIVO
Permettere a Claude Code di generare caroselli premium Digital Empire tramite comando /inizio-generazione nonostante non possa generare immagini nativamente: intercetta comando, chiede argomento, genera copy 8 slide con framework IL PROBLEMA/LA VERITÀ/LA SOLUZIONE/COME FUNZIONA/IL RISULTATO/DOMANDA VERA/CTA, genera 8 prompt immagine con ultra grain 38% background + 15-22% su ogni elemento + 4K 2160x2700 sharp, controlla Arena.ai via Playwright (Chromium headless) per generare immagini, pacchettizza ZIP con PNG + prompt + copy, fornisce download, con qualità reference esatta nero #000000 grain + glow #FF3B1F + typo sans white grain + serif italic red + pill mono + footer.

# TRIGGER
Questa skill si attiva quando:
- Utente digita /inizio-generazione o /inzio-generazione (typo) o /inizio-carosello o /genera-carosello in Claude Code
- Utente dice "genera carosello", "crea carosello", "Content Factory carosello", "Digital Empire carosello"
- Sistema rileva che Claude Code tenta di generare immagine ma non può (limitazione modello testuale)
- Planner detect intent = carousel-machine + need_playwright_bridge = true
- Utente ha installato workspace apex7 in Claude Code e chiede workflow Playwright

# REGOLE FERREE
1. Comando trigger DEVE essere /inizio-generazione (supporta anche /inzio-generazione con typo) - quando rilevato, NON generare direttamente immagine ma avviare flusso conversazionale: Step 1 chiedi argomento "Dimmi l'argomento del carosello (es. 'Content Factory per coach')", aspetta risposta utente, poi procedi
2. MAI tentare generazione immagine diretta da Claude Code - SEMPRE usa Playwright bridge via arena_client.py che controlla Arena.ai browser automation, altrimenti se Playwright non disponibile usa fallback locale che salva prompt in outputs/carousel per generazione successiva con generate_image tool
3. Qualità ULTRA grain obbligatoria su ogni elemento (richiesta utente esplicita): background grain 38% + element grain - card dark 22%, card light 18%, testo bianco 5%, pill 12%, bottone 15%, logo 10% - MAI solo background con grain, ogni pixel deve avere grain texture, ultra high resolution 4K 2160x2700 source downscaled Lanczos sharp per nitidezza estrema DPI 300
4. Nitidezza massima: risoluzione 2160x2700 (2x di 1080x1350) ultra sharp focus crisp edges high-frequency detail no blur no soft focus 8K texture maps subpixel anti-aliasing - testo deve essere tagliente nitido nonostante grain
5. Flusso 5 step obbligatorio: 1) Chiedi argomento e attendi, 2) Genera copy 8 slide con Analyst+Writer, 3) Genera 8 prompt ultra grain + lancia Playwright Arena generation con progress {current}/{total}, 4) Crea ZIP con 8 PNG + prompt + copy.json + report.json, 5) Fornisci path download ZIP e istruzioni import su Claude
6. Playwright implementation dettagliata: usa config.yaml selectors con fallback list, prova ogni selettore per prompt_input (textarea, contenteditable), generate_button (Send, Generate, submit), generated_images (img src blob/base64), gestisci base64 data URI + blob URL + screenshot fallback, timeout 60s per immagine, delay 2s tra slide per evitare rate limit, headless true default ma supporta --no-headless per debug visivo
7. Quando completamente finito, workspace è installabile su Claude Code: tutto in /home/user/apex7, copiare in ~/.claude/skills/digital-empire-carousel/, installare pip requirements playwright pyyaml fastapi uvicorn + playwright install chromium, registrare comando /inizio-generazione che punta a python -m playwright_bridge.cli --interactive

# WORKFLOW OPERATIVO

## STEP 1: INTERCETTA /inizio-generazione E CHIEDI ARGOMENTO
1.1 Input: utente digita /inizio-generazione in Claude Code (o /inzio-generazione con typo)
1.2 Azione: mostra banner Digital Empire + spiega bridge Playwright + mostra messaggio "🎯 Perfetto, sto aspettando il tuo argomento... Scrivimi di cosa deve parlare il carosello. (es. 'Content Factory per coach', 'Sistema AI per concessionari', 'Recupero carrelli e-commerce')"
1.3 Attendi input utente - topic string - se vuoto usa default "Content Factory per imprenditori"
1.4 Salva topic in working memory L1 + decision log L2 con why = "User ha richiesto carosello su {topic} via /inizio-generazione"
1.5 Output: topic validato

## STEP 2: GENERA COPY 8 SLIDE CON FRAMEWORK DIGITAL EMPIRE
2.1 Input: topic
2.2 Azione: chiama CarouselFlow.generate_copy_from_topic(topic)
   - Planner decompone in 8 slide con ruoli: 1 CONTENT FACTORY hook, 2 IL PROBLEMA (3 ore), 3 LA VERITÀ (problema idee vs esecuzione), 4 LA SOLUZIONE (fabbrica che lavora), 5 COME FUNZIONA (3 step 01 02 03), 6 IL RISULTATO (97% 120+ 5min), 7 DOMANDA VERA (sembreranno AI?), 8 CTA (Smetti di scrivere €6.400->€3.200)
   - Writer genera testi adattati a topic con parole rosse accent identificate (problema, esecuzione, fabbrica, Zero, 3 ore, 4 minuti, dall'AI?, scrivere, lanciare)
   - Analyst verifica coerenza con reference style guide
2.3 Output: slides array 8 oggetti {slide_num, pill_label, icon, text, red_words, role} + salva in slides_copy.json

## STEP 3: GENERA PROMPT ULTRA GRAIN + ESEGUI PLAYWRIGHT SU ARENA.AI
3.1 Input: slides array 8
3.2 Azione per ogni slide:
   - Writer.execute con payload {slide_text, pill_label, icon, slide_number, total_slides=8, red_words, ultra_quality=True, resolution=4K}
   - Genera base prompt nero #000000 grain 38% glow #FF3B1F pill mono footer 3/8
   - Applica _enhance_for_ultra_quality(): aggiungi suffix con ultra grain su ogni elemento (card 22%, text 5%, pill 12%, button 15%, logo 10%) + 4K 2160x2700 ultra sharp DPI 300 Lanczos
   - Salva prompt in slide_0X_prompt.txt
3.3 Lancia ArenaPlaywrightClient.generate_carousel(prompts, output_dir, model=GPT-4o):
   - Se use_playwright=true: start browser headless Chromium, goto https://arena.ai, seleziona modello GPT-4o, loop 8 slide:
     * Trova input via _find_element con fallback selectors, fill prompt, click Generate o Enter, aspetta immagine con polling 2s fino a timeout 60s, estrai src (base64 decode se data URI, screenshot se blob/http), salva slide_0X.png 2160x2700, delay 2s
   - Se use_playwright=false o fallisce: fallback salva prompt + json meta con requires_arena_generation=True per generazione successiva con generate_image tool locale o arena_generator.py
3.4 Progress feedback: "🎨 Genero immagini 4K ultra-grain con Playwright su Arena.ai - Modello GPT-4o - 3/8 slide..."
3.5 Output: image_results array con status success/prompt_saved per ogni slide

## STEP 4: PACKAGE ZIP + REPORT 4K ULTRA GRAIN
4.1 Input: output_dir con 8 PNG + 8 prompt txt + slides_copy.json
4.2 Azione:
   - Crea ZIP archive con shutil.make_archive: <topic>_<timestamp>_CAROSELLO.zip contenente tutto output_dir
   - Calcola size MB
   - Genera report.json con topic, model, slides, image_results, output_dir, zip_path, quality="ULTRA grain 38% bg + 15-22% su ogni elemento + 4K sharp 2160x2700", timestamp
   - Salva report + persist memory L5
4.3 Output: zip_path

## STEP 5: FORNISCI DOWNLOAD E ISTRUZIONI CLAUDE INSTALL
5.1 Output finale a utente:
   - Banner ✅ Carosello pronto! 8 slide 1080x1350 con grana ultra su ogni elemento, risoluzione 4K nitida
   - "📦 Scarica ZIP: {zip_path} - {size} MB - Contiene 8 PNG 2160x2700 + prompt + copy + report"
   - "Output dir: {output_dir}"
   - "Slides: 8 | Images: {success count} | Quality: ULTRA grain 38% + 4K sharp"
   - Istruzioni: "Installa questo workspace su Claude: copia /home/user/apex7 in ~/.claude/skills/digital-empire-carousel/, pip install playwright pyyaml fastapi uvicorn && playwright install chromium, registra comando /inizio-generazione -> python -m playwright_bridge.cli --interactive, lancia da Claude Code"
5.2 Se use_playwright=false (fallback): spiega "Prompts salvati, genera immagini con python -m playwright_bridge.cli --topic ... o usa outputs/carousel/ref_v2_* come esempio già generato con generate_image tool ultra quality"
5.3 Log decisione in L2 + snapshot architettura L4 con version v8.0-ultra-grain-playwright-bridge
