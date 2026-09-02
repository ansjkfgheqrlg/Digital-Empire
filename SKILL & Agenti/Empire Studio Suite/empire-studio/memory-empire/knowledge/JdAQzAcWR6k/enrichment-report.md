# Enrichment Report — JdAQzAcWR6k

**Video:** "How to Create VIRAL Carousels in ChatGPT (No Coding)" — Artem Novitckii, 7m40s, EN
**Run:** `empire-studio/runs/max17-v01-artem`
**Stage C-H eseguiti:** 2026-09-02
**Atoms disponibili:** 40 KA — 9 alta rilevanza DE, 13 media, 18 bassa

---

## Stage D — Relevance / Gap / Scout

### Perimetro valutato

Il brief indicava di valutare due bersagli precisi e due concetti precisi: `.claude/skills/carousel-empire/SKILL.md` (per il pattern "slide-per-slide invece di carosello intero" + "visual anchor") e `.claude/skills/image/SKILL.md` (per la tecnica del riferimento visivo di coerenza di stile fra immagini di una stessa serie). Nessun altro artefatto era nel perimetro.

**`carousel-empire`**: esiste, `.claude/skills/carousel-empire/SKILL.md`, letto integralmente (251 righe prima della patch). Workflow a 7 step: Step 2 genera `carousel_content.json` con schema fisso a 7 tipi di slide (`hook/problem/solution/how_it_works/proof/differentiator/cta`), Step 3-4 installano Playwright ed eseguono `scripts/generate_carousel.py`, che **genera tutte le 7 slide in un solo passaggio** da un solo file HTML/JSON — nessuna iterazione slide-per-slide, nessun concetto di immagine di riferimento tra una slide e l'altra (il "brand" è fisso via CSS, non via reference-image).

**`image`**: esiste, `.claude/skills/image/SKILL.md`, letto integralmente (340 righe prima della patch). La tabella "Model Comparison" cita "multi-image reference" come capacità di Gemini Image; la sezione "When to Use Which" ha un ramo "Need product/brand consistency across many images? → Flux (multi-image reference), Gemini Nano Banana Pro, Recraft V3"; "Common Mistakes" #7 dice genericamente "Inconsistent brand visuals — use Flux multi-reference or design templates for consistency". Tutti e tre i punti parlano di consistenza *di brand* generica (loghi, colori, stile aziendale) attraverso immagini scollegate tra loro nel tempo — **nessuno descrive il pattern operativo specifico**: generare la prima immagine di una serie ordinata, poi usare quella stessa immagine (non un moodboard esterno) come reference per ognuna delle successive, in sequenza.

### Verifica del gap (non solo dichiarato, verificato di persona)

- `grep -in "visual anchor|slide.by.slide|slide-per-slide|one at a time"` su `carousel-empire/SKILL.md`: **0 risultati**. Nessun concetto di generazione iterativa esisteva prima della patch.
- Lettura diretta di Step 2-4 di `carousel-empire/SKILL.md`: confermato che lo script genera sempre tutte le slide in un'unica esecuzione da un unico JSON, con HTML/CSS a template fisso (non image-gen).
- `grep -in "anchor|first image.*reference|reference.*first image"` su `image/SKILL.md`: **0 risultati** sul termine "anchor"; "multi-image reference" compare 2 volte ma sempre in senso generico di "riferimento di brand", mai come "usa l'immagine 1 della serie come riferimento per l'immagine 2, 3, N".

**Verdetto**: gap reale su entrambi i fronti, confermato prima di scrivere qualunque riga. Il gap su `image` è più stretto del previsto dal brief: la capacità tecnica di base (multi-image reference) era già nota alla skill — mancava solo la tecnica operativa nominata esplicitamente e applicata a una *serie ordinata* invece che a un moodboard di brand generico.

---

## Stage E — Gate (permission-guard)

Entrambe le patch sono **additive**: `git diff --numstat -- .claude/skills/` → **+126 / -0** (120 righe su `carousel-empire/SKILL.md`, 6 righe su `image/SKILL.md`). Nessuna riga preesistente rimossa, riscritta o contraddetta in silenzio.

- La patch di `carousel-empire` **non sostituisce** il workflow HTML/Playwright esistente (Step 1-7): la nuova sezione è esplicitamente dichiarata "Modalità Alternativa", con la frase "Il template HTML fisso... resta la modalità di default: deterministico, brand-safe... usalo per il 90% dei casi" — il default resta invariato.
- La patch di `image` è inserita come nuova sottosezione dentro "AI Image Generation", senza toccare la tabella "Model Comparison" né "When to Use Which" preesistenti — le arricchisce con un rimando incrociato, non le riscrive.
- **Attribuzione in linea obbligatoria**: ogni aggiunta porta `(fonte: JdAQzAcWR6k — Artem Novitckii, mm:ss)` (in `carousel-empire`) o l'equivalente in inglese con video-id e timestamp (in `image`, coerente con la lingua della skill).
- **Anti-overfitting**: fonte singola (un video, un autore che vende una community). I due prompt master sono riportati come **testo esatto riusabile con placeholder**, non come claim di efficacia — la tecnica "genera slide 1, poi ancorala" è scritta come procedura operativa falsificabile, non come promessa di risultato (il video dichiara "quasi 100.000 views" per il carosello di esempio, ma questo numero **non è citato nella patch** — solo la tecnica, non il risultato aneddotico, per evitare di vendere una promessa non verificabile come regola).
- **Il blocco anti-plagio del video** ("Do not copy: exact text / exact branding / exact compositions") è stato preservato testuale nei due prompt master riportati — è disciplina operativa, non claim.

**Riserva registrata**: il video mostra la tecnica applicata a un solo carosello (Morning Routine, 8 slide) con un solo autore. Non c'è un secondo caso indipendente a supporto nella fonte. La patch resta operativa perché il principio ("un modello di image-gen produce un'immagine alla volta, quindi generare in sequenza con riferimento riduce l'incoerenza") è un fatto tecnico plausibile sul funzionamento dei modelli, non un'invenzione di marketing dell'autore — ma non è stato testato da Digital Empire in questa sessione (nessuna generazione reale eseguita, solo patch di documentazione).

---

## Stage F — Patch applicate (2 file, 2 blocchi, +126 righe, 0 cancellazioni)

### 1. `carousel-empire/SKILL.md` — +120 righe, 0 cancellazioni

Nuova sezione **"## Modalità Alternativa — Stile AI-Generativo con Visual Anchor"**, inserita dopo lo Step 7 "Report Finale" e prima di "## Esempi Contenuto per Prodotto":

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| Solo un modo di generare le slide: HTML/Playwright, tutte e 7 in un'unica esecuzione da un unico JSON | Ramo alternativo esplicito, da usare solo su richiesta, per stile illustrato/collage: generazione **slide-per-slide**, non l'intero carosello in un prompt | KA-001, KA-030 |
| Nessun concetto di immagine-riferimento tra slide | **Visual anchor**: la slide 1 (hook) generata bene diventa reference per tutte le successive — spendere la maggior parte del tempo lì | KA-002, KA-039 |
| Nessun prompt riusabile per questo pattern | I **due prompt master integrali** con placeholder (`[TOPIC]`, `[INSERT TEXT HERE]`, `[SLIDE TYPE]`, `[SLIDE GOAL]`, `[SLIDE TEXT]`, `[DESCRIBE WHAT SHOULD BE ON THE SLIDE]`) — Slide 1 Prompt (5 versioni) e Slide [X] Prompt (3 versioni, "use slide 1 as the visual anchor") | KA-015, KA-016 |
| Nessuna regola su come scegliere tra generazioni multiple | "Pick the best of N" esplicito: generare 3-5 versioni per slide e scegliere manualmente, non affidarsi alla prima generazione | KA-017 |
| Nessuna disciplina anti-plagio quando si usa un riferimento esterno (es. Pinterest) | Blocco "Do not copy: exact text / exact branding / exact compositions" preservato nei prompt master | KA-015, KA-016 |
| Nessun rimando a quale modello usare per questo pattern | Cross-reference a `image/SKILL.md`, tabella "Model Comparison", per il modello con miglior supporto multi-image reference | — (collegamento interno) |

### 2. `image/SKILL.md` — +6 righe, 0 cancellazioni

Nuova sottosezione **"### Visual Anchor — Style Consistency Across a Series"**, inserita dentro "AI Image Generation", dopo "When to Use Which" e prima di "### Prompting Basics":

| Gap nella skill (prima) | Cosa aggiunge il video | KA |
|---|---|---|
| "Multi-image reference" citato solo come capacità tecnica generica di Gemini/Flux, mai come tecnica operativa nominata | Pattern esplicito: genera la prima immagine della serie molto bene, poi passala come reference per ogni generazione successiva della stessa serie, invece di chiedere l'intera serie in un solo prompt | KA-001, KA-002, KA-030, KA-039 |
| Nessun cross-link a `carousel-empire` per un caso d'uso concreto già implementato | Rimando esplicito a `carousel-empire/SKILL.md`, sezione "Modalità Alternativa — Stile AI-Generativo con Visual Anchor", per i prompt completi | — (collegamento interno) |

**Line endings verificati e preservati**: entrambi i file erano **LF puro** (0 CRLF) prima della patch (verificato via conteggio binario `\r\n` vs `\n`-only) e sono rimasti LF puro dopo — nessuna conversione accidentale.

---

## Skill NON toccate, con motivazione

Nessuna terza skill è stata valutata o toccata: il brief limitava esplicitamente il perimetro a `carousel-empire` e `image`. In particolare, **non è stata creata** una nuova skill `carousel-visual-scout` né un nuovo agente `carousel-copy-strategist` — sono proposte esplicite del `video-analysis.md`/`contenuto-integrale.md` (Consigli §2 e §3) che il brief non ha chiesto di costruire: restano proposte non applicate, segnalate qui e nel log di ingestione invece di essere costruite di iniziativa.

Non è stato toccato nemmeno il Publer-style "mockup del feed IG" (Consiglio §5 del video-analysis.md, Step 5 di `carousel-empire`) — reale, ma fuori dal perimetro esplicito del brief (che limitava l'enrichment ai due concetti "slide-per-slide" e "visual anchor", non al self-check del feed).

---

## Stage H — Sintesi

**Skill/artefatti valutati:** 2/2 richiesti dal brief (`carousel-empire`, `image`), entrambi esistenti e patchati. **Patchati:** 2/2.
**Totale:** +126 righe, **0 cancellazioni** (verificato su `git diff --numstat`).
**Line endings preservati:** entrambi i file erano LF puro e sono rimasti LF puro.

**Cosa era già coperto e non è stato duplicato:**
- Il blocco "Model Comparison" e "When to Use Which" di `image/SKILL.md` già menzionavano "multi-image reference" come capacità — non riscritti, solo estesi con la sottosezione nuova che nomina la tecnica operativa specifica.
- Il formato tecnico "4:5 vertical Instagram carousel slide, 1080x1350" richiesto in entrambi i prompt master del video è **già identico** al formato invariante di `carousel-empire` (1080×1350px, 4:5 IG) — nessuna modifica necessaria lì, segnalato come conferma di allineamento, non come gap.

**Tensione aperta:** nessuna. Il gap era netto: la tecnica "visual anchor su serie ordinata" non esisteva testualmente in nessuna delle due skill prima di questa sessione.

**Non applicato in questa sessione, registrato per non perderlo:**
- Skill `carousel-visual-scout` (ricerca automatica di riferimenti stilistici Pinterest/Behance/Dribbble) — proposta reale del `video-analysis.md`, fuori dal perimetro esplicito del brief.
- Agente/sotto-fase `carousel-copy-strategist` (varianti hook A/B/C con raccomandazione motivata, prima del render) — stessa nota.
- Mockup del feed Instagram nello Step 5 "Self-Check Visivo" di `carousel-empire` (equivalente locale di Publer) — stessa nota.

---

## Tracciabilità

- Contenuto integrale: `memory-empire/knowledge/JdAQzAcWR6k/contenuto-integrale.md`
- Atoms: `memory-empire/knowledge/JdAQzAcWR6k/atoms.json` (40 KA, ognuno con `trace` = `JdAQzAcWR6k#mm:ss + frames/frame-NNN.png`)
- Manifest: `memory-empire/knowledge/JdAQzAcWR6k/ingest-manifest.json`
- Analisi visiva: `empire-studio/runs/max17-v01-artem/video-analysis.md` — coverage 117/117 frame unici, NO-FINTO PASS
- Coverage report: `empire-studio/runs/max17-v01-artem/coverage.md`
- Audit Stage G: `memory-empire/memory/audit/2026-09-02-JdAQzAcWR6k-stage-g.md`
- Log ingestione: `memory-empire/memory/ingestions/2026-09-02-artem-novitckii-caroselli-chatgpt.md`
- Wiki: `second-brain-vault/wiki/sources/Source_Artem_Novitckii_Caroselli_ChatGPT.md`
- Patch applicate: `.claude/skills/carousel-empire/SKILL.md` (+120/-0), `.claude/skills/image/SKILL.md` (+6/-0)
