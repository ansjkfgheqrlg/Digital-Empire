---
Type: SOURCE
Status: Active
Tags: #caroselli #instagram #chatgpt-image #visual-anchor #carousel-empire #image-generation #ai-image #artem-novitckii #max17
Created: 2026-09-02
Last updated: 2026-09-02
---

# Source: Artem Novitckii — How to Create VIRAL Carousels in ChatGPT (No Coding)

## Overview
Tutorial di 7m40 in cui l'autore mostra come generare caroselli Instagram con ChatGPT Image senza codice, risolvendo il problema principale dei caroselli AI "one-shot": un modello di image gen produce **una sola immagine alla volta**, quindi chiedere l'intero carosello in un solo prompt produce slide incoerenti tra loro. La soluzione — il **visual anchor** — genera la slide 1 (hook) con cura, poi la allega come immagine di riferimento a ogni prompt successivo, così ogni nuova slide eredita tipografia, colori, texture e mood. Video 1 del batch `max17`.

Il contributo che vale davvero per Digital Empire non è "un altro modo di fare caroselli" — DE ha già `carousel-empire`, un motore end-to-end HTML+Playwright a template fisso, più maturo per il 90% dei casi — ma **due pattern operativi con prompt riusabili**: la generazione **slide-per-slide invece di carosello intero**, e il **visual anchor** stesso, applicabili come ramo alternativo quando serve uno stile illustrato/collage che l'HTML/CSS non può produrre. Entrambi confermati come gap reali in `carousel-empire` e `image` prima di essere patchati.

## Dati Tecnici

- **Video ID:** JdAQzAcWR6k
- **Durata:** 7m40s (460s)
- **Canale:** Artem Novitckii — Co-founder @ Aha!, "Teaching how to build and scale AI Systems", Auckland · **Lingua:** EN
- **Formato:** Talking head + screen share ChatGPT/Pinterest/Google Docs/Canva/Publer + whiteboard Excalidraw
- **Frame:** 230 densi @2s → 117 unici sopra soglia | **Frame letti: 117/117 — coverage 100%** | NO-FINTO: PASS
- **KA:** 40 (9 alta rilevanza DE, 13 media, 18 bassa) | 39 osservati, 1 inferito
- **Processing:** pipeline Empire Studio (sessione precedente) · Memory Empire C-H 2026-09-02
- **Run:** `empire-studio/runs/max17-v01-artem`

## Il Principio — Perché i Caroselli AI "One-Shot" Falliscono

```
PROMPT UNICO "genera 6 slide"        VS        SLIDE-PER-SLIDE + VISUAL ANCHOR
─────────────────────────                      ──────────────────────────────
ogni slide creata da zero,                      slide 1 curata al massimo,
senza consapevolezza delle altre                poi allegata come reference
        |                                               |
        v                                               v
"un po' disordinato,                            "molto rifinito, coerente
 senza gusto"                                    slide dopo slide, sembra
                                                  fatto da un designer"
```

Confronto mostrato a video sullo stesso topic/brief, side-by-side. Il carosello slide-per-slide+anchor è lo stesso che l'autore dichiara aver ottenuto "quasi 100.000 views" una volta pubblicato (Instagram Insights confermati per Interactions 12.911, Comments 6.003, Shares 1.743 — il numero di Views esatto non è leggibile con certezza nello screenshot, riportata solo la dichiarazione verbale).

## I Due Prompt Master — Riusabili con Placeholder

Recuperati parola per parola da un Google Doc mostrato integralmente a schermo (uno dei 4 prompt integrali di questo ingest, insieme al prompt di copy morning-routine e al prompt meta "GPT Stage 2 Carousel"; il quinto prompt del video, LinkedIn "recreate this infographic", **non è recuperato integralmente** — solo frammenti, dichiarato esplicitamente come tale):

```
Slide 1 Prompt — hook/cover, 5 versioni
Borrow from references: typography hierarchy, spacing, colour treatment,
texture, visual pacing, layout logic.
Do not copy: exact text, exact branding, exact compositions.
Format: 4:5 vertical Instagram carousel slide, 1080x1350.

Slide [X] Prompt — slide successive, 3 versioni
Use slide 1 as the visual anchor.
Match slide 1's: typography feel, spacing, colour treatment, texture,
raw editorial mood, utility details, visual hierarchy, design language.
Do not make this slide feel like a new carousel.
```

(Testo esatto completo nei due prompt in `contenuto-integrale.md`, Parte 6, e nella patch applicata a `carousel-empire/SKILL.md`)

## Il Metodo Completo — "The Stupid Simple Instagram Carousel System"

```
1. Copy definita bene            → 40% del tempo
2. Hook slide = visual anchor    → 50% del tempo (il passo più importante)
3. Slide successive, ancorate    → 10% del tempo
4. Canva Magic Layers (opz.)     → solo per micro-tweak, mai per rigenerare
```

Prima della copy: **ChatGPT Project dedicato** ("Instagram Carousel Copy Writer") con Sources caricate (`slide-count.md`, `SKILL.md`), a sua volta derivato da "The Carousel Bible" — documento di ricerca su psicologia dei caroselli (Autonomy, Commitment Escalation, Dopamine Loops, Reduced Cognitive Load) e statistiche di terzi citate (non verificate indipendentemente da questa sessione). Output strutturato: PLAYBOOK/TIER/SLIDE COUNT motivato/HOOK CATEGORY, poi per ogni slide 3 varianti di hook (A/B/C) + raccomandazione + copy finale.

Prima di generare: ricerca del visual anchor **su Pinterest, non Instagram** — la reference può essere "letteralmente qualsiasi cosa, una copertina di libro, un poster".

## L'Output — carosello "Morning Routine", 8 slide

Ogni slide generata in 3-5 versioni, scelta manuale della migliore ("pick the best of N"). Anteprima pre-pubblicazione con **Publer** (`publer.com/tools/instagram-post-preview`, gratuito, no login). Rifiniture minori con **Canva Magic Layers** (mai per rigenerare interi design — "I only use magic layers if the fix is very small"). Stesso prompt stack riusato per infografiche LinkedIn (Parte 4 del video), cambiando solo il "Carousel topic".

## Key Quotes

> "The reason why most AI carousels fail is because these image generation models... can only generate one image at a time. So the moment you ask it to create a full six slide carousel in one go, every single slide is being created from scratch without any awareness of the other slides."

> "Use slide 1 as the visual anchor." [dal Prompt Master 2, letteralmente]

> "This is the most important step... you should spend the most time here." [sulla generazione della hook slide/visual anchor, 50% del tempo]

> "I only use magic layers if the fix is very small. Otherwise, I'll let ChatGPT do all the heavy lifting."

> "The unlock is not the image. It's the system." [slogan sulla lavagna Excalidraw]

## Azione Concreta (Enrichment)

**2/2 artefatti richiesti dal brief valutati ed entrambi patchati. +126 righe, 0 cancellazioni.**

- `carousel-empire/SKILL.md` (**+120**) — nuova sezione "Modalità Alternativa — Stile AI-Generativo con Visual Anchor" dopo lo Step 7 "Report Finale": principio slide-per-slide, definizione di visual anchor, i due prompt master integrali con placeholder, regole operative (pick-best-of-N, blocco anti-plagio "Do not copy"). Il workflow HTML/Playwright a template fisso **resta il default per il 90% dei casi** — questa è un ramo esplicitamente alternativo, non una sostituzione.
- `image/SKILL.md` (**+6**) — nuova sottosezione "Visual Anchor — Style Consistency Across a Series": la skill citava già "multi-image reference" come capacità tecnica di Gemini/Flux, ma mai come tecnica operativa nominata esplicitamente (prima immagine della serie come reference per tutte le successive) — gap più stretto del previsto, colmato con un rimando incrociato a `carousel-empire`.

**Nessuna terza skill toccata.** Nessuna nuova skill/agente costruito di iniziativa (proposte `carousel-visual-scout`, `carousel-copy-strategist`, mockup feed IG stile Publer — restano non applicate, fuori dal perimetro esplicito del brief). Dettaglio in `memory-empire/knowledge/JdAQzAcWR6k/enrichment-report.md`.

## Conferma Interessante — DE Usa Già Questo Pattern Altrove

`carousel-empire` (la skill Claude patchata qui) non è l'unico motore caroselli di Digital Empire. **ArenaAI** (`SKILL & Agenti/Workflow agency creative/caroselli - agency/`, mappato in [[Reparto_Produzione_Digital_Empire]]) è un'automazione Playwright reale su Arena.ai, attiva su @digitalempireagency.e, che genera le slide con esattamente lo stesso principio: **"catena slide1→slide2→slide3 via allegato immagine precedente"**. Il pattern "visual anchor" non era quindi sconosciuto a DE — era già in produzione in un motore diverso (ArenaAI), semplicemente non documentato dentro `carousel-empire`. Questo conferma indipendentemente che la tecnica funziona nella pratica, non solo nella teoria di un singolo video esterno.

## Nota di trasparenza — limiti della fonte

Il video mostra un solo ciclo di produzione (carosello Morning Routine, 8 slide, un autore). Il quinto prompt (LinkedIn "recreate this infographic") **non è recuperato integralmente** — solo frammenti tra motion blur e testo minuscolo, dichiarato esplicitamente come tale in `contenuto-integrale.md`. Le statistiche di terzi citate in "The Carousel Bible" (70K follower/2 mesi, 11M views/mese, ecc.) non sono verificate indipendentemente, solo riportate come citate dal documento fonte del video. Nessuna generazione reale è stata eseguita da Digital Empire in questa sessione per validare empiricamente la tecnica — la patch resta documentazione operativa in attesa di un primo uso reale.

## Connessioni

- [[Reparto_Produzione_Digital_Empire]] — mappa i 3 motori caroselli reali di DE (ArenaAI, carousel-factory, carousel-empire); ArenaAI usa già la stessa catena "slide N ancorata alla slide N-1" mostrata in questo video, confermando il pattern indipendentemente.
- [[Source_Giovanni_Beggiato_Team_Marketing_AI]] — stesso batch `max17`, stesso pattern di sessione (Memory Empire chiuso a valle di una pipeline Empire Studio già fatta, con applicazione dei consigli): là il gap era la verifica browser reale in `market-audit`, qui è il pattern visual anchor in `carousel-empire`/`image` — entrambi patchano skill esistenti invece di inventarne di nuove.
- [[Tool_Workflow_Pubblicazione_Automatica]] — il braccio di pubblicazione che prende in carico i caroselli già generati (da `carousel-empire` o da ArenaAI) e li pubblica; questo video aggiunge un passo di anteprima pre-pubblicazione (Publer) che quel tool oggi non ha.
- [[Tool_Memory_Wiki_Bridge]] — il ponte per cui questa ingestione esiste come pagina wiki invece di restare solo in `memory-empire/knowledge/`.
