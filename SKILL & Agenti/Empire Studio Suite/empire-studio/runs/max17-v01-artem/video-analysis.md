# Video Analysis — "How to Create VIRAL Carousels in ChatGPT (No Coding)"

- **ID YouTube:** JdAQzAcWR6k
- **Titolo:** How to Create VIRAL Carousels in ChatGPT (No Coding)
- **Canale/Autore:** Artem Novitckii (co-founder @ Aha!, "Teaching how to build and scale AI Systems", Auckland — da LinkedIn mostrato nel video, frame-176)
- **URL:** https://www.youtube.com/watch?v=JdAQzAcWR6k
- **Durata:** 460s = 7m40s
- **Lingua:** inglese
- **Ingested:** 2026-09-02T12:39:44
- **Frame guardati: 117/117 unici (100%)** — vedi `coverage.md`

## Capitoli ufficiali (da `ingest.json`)

| Start | Titolo |
|---|---|
| 0:00 | Preview of the carousels |
| 0:29 | Why most AI carousels fail |
| 1:13 | Part 1: The visual anchor solution |
| 1:58 | Part 2: How to build it (4-step system) |
| 5:25 | Part 3: Polishing with Canva Magic Layers |
| 6:14 | Part 4: Same system for LinkedIn |
| 6:51 | Summary |

---

## LA TESI DEL VIDEO (perché gli AI carousel "one-shot" falliscono)

Detto a voce (00:00:41–01:16): i modelli di image gen (ChatGPT Image, "Nana Banana") sanno generare **una sola immagine alla volta**. Appena chiedi un carosello intero da 6 slide in un colpo solo, ogni slide viene creata "da zero" a partire dal brief, senza consapevolezza delle altre — risultato: carosello generico, incoerente, "senza gusto". La soluzione dichiarata: **fornire un ancoraggio visivo (visual anchor) per ogni slide generata**. L'anchor è semplicemente la prima slide fatta molto bene: una volta che una slide "inchioda" tipografia, colori, mood, la si allega come immagine di riferimento a ogni prompt successivo, e ogni nuova slide è "costretta" a rispettarla.

Confronto mostrato a video (frame-023→034, chat "GPT Stage 2 Carousel"): due caroselli generati con lo stesso topic/brief — uno con **prompt one-shot** (risultato: "un po' disordinato, senza gusto") e uno con **generazione slide-per-slide + visual anchor** (risultato: "molto rifinito, coerente slide dopo slide, sembra fatto da un designer che ci ha pensato" — ed è il carosello che narra di aver ottenuto quasi 100.000 views).

---

## IL METODO — 4 passi (slide di chiusura, frame-207/216/217/219/221/228)

**"The Stupid Simple Instagram Carousel System"**

1. **Make sure the copy is good** (40% of time)
2. **Generate hook slide, this is your visual anchor** (50% of time)
3. **Build one slide at the time, using visual anchor as style reference** (10% of time)
4. **Use Canva Magic Layers to make small tweaks** (like text or spacing)

Ripetuto quasi identico a voce come "riassunto in 4 step semplici" (00:06:53–00:07:22), con le stesse percentuali di tempo: copy 40%, hook/visual anchor 50% ("this is the most important step... you should spend the most time here"), slide-per-slide 10%, poi eventuali micro-tweak in Canva Magic Layers.

⚠️ Nota: le percentuali sommano 100% sulle prime 3 voci (40+50+10); il quarto punto (Canva Magic Layers) è un passo opzionale a parte, non una fetta di tempo del ciclo principale — coerente con quanto detto a voce: *"I only use magic layers if the fix is very small. Otherwise, I'll let ChatGPT do all the heavy lifting."* (00:06:10).

---

## LA "COPY BIBLE" — ChatGPT Project dedicato al testo

Prima di generare qualunque immagine, Artem passa dalla copy. Ha creato un **ChatGPT Project** chiamato **"Instagram Carousel Copy Writer"** (frame-014/065/069/080/091) con **due file caricati come Sources**:

- `slide-count.md`
- `SKILL.md`

(nomi file letti per intero e con certezza nel tab "Sources" del progetto, frame-069)

Questi due file sono a loro volta addestrati/derivati da un documento più ampio, **"THE CAROUSEL BIBLE"** (frame-072/074, Google Doc), che contiene ricerca sulla psicologia dei caroselli:

**"1.2 [...perch]e[...] Work: The Psychology"**
- **The Self-Paced Consumption Advantage** — citazione: *"With short form videos you are being told information at someone else's pace... but with carousels you are able to swipe through these photos and these slides at your own pace."* — Alex Dashchuk
- **Key Psychological Principles:**
  1. Autonomy — Users control the pace, creating a more comfortable experience
  2. Commitment Escalation — Each swipe is a micro-commitment that increases
  3. Dopamine Loops — The anticipation of the next slide creates reward-seeking behavior
  4. Reduced Cognitive Load — Bite-sized information is easier to process and remember
- **The "Deep Engagement" Effect** — citazione: *"Reels are all about shiny object syndrome. Yes, they grab your attention, but more people they're not doing a great job at keeping it. They provide that really surface engagement of a quick view. Carousels generate what I would call deep engagement. People are pausing, they're reading, they're taking in what you're saying."* — attribuito a "Instagram Algorithm LOVES this content" (fonte citata così nel doc)

**"1.3 Performance Benchmarks & Statistics" — Verified Performance Data from Sources:**

| Metric | Result | Source (citata nel doc) |
|---|---|---|
| Followers gained (2 months) | 70,000 | "Everything I know about carousels" |
| Followers in one month | 54,000 | "Everything I know about carousels" |
| Monthly views | 11 million | "Everything I know about carousels" |
| Views in 30 days | 180 million | Steven Bisi |
| Revenue from 6 carousel posts | $20,000+ | "Instagram Algorithm LOVES this" |

⚠️ Onestà sulla trascrizione: `frame-072`/`frame-074` mostrano questa pagina a leggera sfocatura da scroll (motion blur); i numeri e le citazioni sopra sono confermati leggibili con sicurezza medio-alta, ma il titolo esatto della sezione "1.2 [...] Work: The Psychology" ha una parola tagliata dal blur (probabile "Why Carousels Work" o simile — non ricostruibile con certezza al 100%).

---

## IL PROMPT DI COPY (uso reale) — integrale

Digitato nel progetto ChatGPT "Instagram Carousel Copy Writer" (frame-080, @2:38):

```
I want to make a carousel about my morning routine and habits. I wake up
everyday at 7 am, I have cold shower, I do a bit of stretching, I walk
outside for 10 min to get sunlight in my eyes, I journal and pray for 10
min, I dont use my phone in the first hour of the morning because it
disrupts the dopamine
```

Risposta strutturata del progetto (frame-080/091/097/137, ricostruita leggendo più frame in sequenza dello stesso chat scrollato):

```
🗒️ CAROUSEL — Morning Routine

PLAYBOOK: Tip / Value
TIER: TOFU growth
SLIDE COUNT: 8 because it fits the Magic 8 format: hook, why, 6 useful habits, CTA
HOOK CATEGORY: Curiosity Gap / Challenge using a personal "How I" angle

—

S1 COVER
HOOK A: I protect my first hour
HOOK B: My dopamine-proof morning
HOOK C: Your phone ruins your morning
RECOMMENDED: B
It's more curiosity-driven, more modern, and ties directly to the dopamine
angle without sounding preachy.

FINAL S1 COPY:
My dopamine-proof morning
No phone.
No scrolling.
No cheap hits.
Just a clean start.

S2 SECOND-CHANCE HOOK
THE PROBLEM
Most people lose the day before they even get out of bed.
They wake up.
Grab the phone.
Train their brain to chase.
the next → [testo tagliato dal frame successivo, non ricostruibile]

S3 FIRST VALUE DROP
01 — WAKE UP AT 7AM
Same time
Every day
Not because I'm perfect. Because your brain loves rhythm more than motivation.
```

Il formato "PLAYBOOK / TIER / SLIDE COUNT (con motivazione) / HOOK CATEGORY", poi per ogni slide **3 varianti di hook (A/B/C) + una raccomandazione motivata + il copy finale**, è lo schema fisso di output del progetto — visibile identico per ogni slide successiva nel chat (S2, S3...).

⚠️ Il testo esatto della fine di S2 ("the next →" seguito da testo tagliato) non è ricostruibile da nessun frame disponibile.

---

## LA RICERCA DEL VISUAL ANCHOR — Pinterest

Narrato (03:12–03:29): *"we're going to find a visual reference on how we want our Instagram carousel to look like... I actually [don't] look for inspiration on Instagram. I prefer to look at Pinterest. The reference could be literally anything like a book cover or a poster."*

Frame mostrati: ricerca Pinterest "book cover" (frame-099) e "poster" (frame-104) — gallery di risultati generici (copertine libri, poster grafici). Poi la vera reference scelta, salvata in una bacheca Pinterest **"Instagram Carousel Design"** (frame-105/108): il pin **"Fun and Playful Instagram Carousel Canva Design Template"**, un carosello di riferimento blu/nero/giallo-lime dal titolo "My mantra before starting work" con 4 slide di esempio ("01 Start small.", "02 Do your best.", "03 Learn as you go.", "04 That's enough for today."). Questo pin è lo stile (tipografia bold nera, blocchi giallo-lime, sfondo blu/crema) che verrà "preso in prestito" (mai copiato direttamente) per il carosello sulla morning routine.

---

## I DUE PROMPT MASTER (i pezzi più preziosi del video) — integrali, parola per parola

Entrambi mostrati per intero in un Google Doc, letto scorrendo su schermo (frame-114→123 per il primo, frame-134 per il secondo).

### PROMPT MASTER 1 — "Slide 1 Prompt" (hook / slide di copertina)

```
Slide 1 Prompt

Create 5 different versions of slide 1 for an Instagram carousel.

Use the attached references as visual inspiration only.

Borrow from the references:
- typography hierarchy
- spacing
- colour treatment
- texture
- visual pacing
- layout logic

Do not copy:
- exact text
- exact branding
- exact compositions

Carousel topic:
Morning Routine

Slide type:
Cover / hook slide.

Slide goal:
Stop the scroll and make people want to swipe.

Text for slide 1:
[INSERT TEXT HERE]

Visual direction:
[DESCRIBE WHAT SHOULD BE ON THE SLIDE]

Style direction:
Make it feel raw, editorial, clear, useful, and highly readable. It should
feel designed, but not overly polished or corporate.

Format:
4:5 vertical Instagram carousel slide, 1080x1350.

Rules:
- keep the exact text only
- make all text readable
- do not add random words
- do not copy the references directly
- make each version visually distinct
```

Ricostruito leggendo in sequenza: intestazione + "Borrow from"/"Do not copy" (frame-114/115), "Carousel topic" → "Format" (frame-118/119), lista "Rules" completa (frame-121/122/123, dove il pulsante "Show more" del box è stato espresso in chat e la lista compare integrale). Versione **compilata** effettivamente inviata in chat per la morning routine (frame-108/122): stesso testo, con `Text for slide 1:` = *"My dopamine-proof morning"* al posto del placeholder.

### PROMPT MASTER 2 — "Slide [X] Prompt" (tutte le slide successive, tab "Rest of the slides" dello stesso Google Doc)

```
Slide [X] Prompt

Create 3 versions of a slide [x] of my Instagram carousel.

Use slide 1 as the visual anchor.

Match slide 1's:
- typography feel
- spacing
- colour treatment
- texture
- raw editorial mood
- utility details
- visual hierarchy
- overall design language

Do not copy the references directly.
Do not make this slide feel like a new carousel.
It must feel like the same visual family as Slide 1.

Carousel topic:
My morning routine

Slide type:
[SLIDE TYPE]

Slide goal:
[SLIDE GOAL]

Text on slide:
[SLIDE TEXT]

Visual direction:
[DESCRIBE WHAT SHOULD BE ON THE SLIDE]

Format:
4:5 vertical Instagram carousel slide, 1080x1350.

Rules:
- keep the exact text only
- make all text readable
- do not add random words
- keep it visually consistent with slide 1
- one clear idea only
```

(frame-134, unico frame che mostra questo secondo template, testo piccolo ma leggibile per intero; la voce "utility details" nella lista "Match slide 1's" è la meno nitida delle otto — confidenza media, non alta come il resto del prompt).

Versione **compilata** usata per la slide 2 (frame-141/143): stesso testo con "Carousel topic: My morning routine" seguito da "Slide [type/goal]: THE PROBLEM" e il copy di S2 incollato sotto.

---

## GENERAZIONE — cosa è uscito, slide per slide (carosello "Morning Routine")

Ricostruito incrociando le chat ChatGPT (frame-040→159) con il tool di anteprima Publer (frame-157→164, che mostra tutte le 8 slide caricate in ordine):

1. **Hook (visual anchor)** — "My dopamine-proof morning / No phone. No scrolling. No cheap hits. / Just a clean start." — collage tipografico nero/crema/blu con blocco giallo-lime, scarabocchio grafico blu a forma di spirale. 5 versioni generate, questa la scelta ("I like it the most").
2. **Second-chance hook / problema** — "Most people lose the day before they even get out of bed. / They wake up. / Grab the phone. / Train their brain to chase." — su sfondo crema, stesso scarabocchio blu.
3. **01 — WAKE UP AT 7AM** — "Same time. Every day. / Not because I'm perfect. Because your brain loves rhythm more than motivation." — sfondo nero.
4. Slide (probabile su doccia fredda/stretching, testo visibile solo parzialmente in frame-153): "tough. / It's about doing a hard thing before the world starts asking for your attention." — sfondo nero. ⚠️ Il numero/etichetta esatti di questa slide (04? 05?) non sono leggibili nel frame disponibile.
5. **Slide "Journal + Pray"** — "10 minutes. / Write what's in my head. / Pray for what I can't control. / That's how I stop carrying noise into the rest of the day." — sfondo nero, etichetta "05 — JOURNAL + PRAY" visibile in alto (frame-154).
6-7. Non mostrate individualmente a schermo con testo leggibile (coperte solo dal riepilogo Publer).
8. **CTA finale** — "THE BEST HABIT / No phone for the first hour. / Comment MORNING and I'll send my full routine." — sfondo nero con blocco giallo-lime.

Ogni slide è generata con **3 versioni** (tranne slide 1, 5 versioni e l'ultima, 5 versioni — "last slide" prompt visto in frame-153/154), e Artem sceglie manualmente la migliore ogni volta: *"some of these don't quite look right, but one of them actually looks decent, so I'll pick this one and I'll continue doing so."* (04:56–05:02). Tempo dichiarato per l'intero ciclo di prompting: **~10 minuti** (05:02).

---

## STRUMENTO DI ANTEPRIMA — Publer (free tool)

Narrato (05:09–05:15): *"I found this tool online just to show you how this carousel would look like on Instagram."* Tool identificato con certezza dall'URL in barra indirizzo (frame-157/158/159/163/164): **`publer.com/tools/instagram-post-preview`** — Publer, sezione "Free Tools", "Instagram Post Preview". Interfaccia: campo testo caption a sinistra, area "Click or Drag & Drop image" con le 8 thumbnail caricate, anteprima live del post Instagram a destra (con puntini/carosello). Nessun login richiesto per l'anteprima mostrata.

---

## CANVA MAGIC LAYERS — rifinitura (Part 3, cap. 5:25)

Narrato (05:34–06:14): se una slide è "90-95% there" ma un elemento o del testo è leggermente sbagliato, invece di rigenerare l'intera slide con ChatGPT, Artem la carica in **Canva → Magic Layers**, che trasforma qualunque immagine in **layer editabili e spostabili**. Percorso mostrato a schermo: Canva homepage (`canva.com`) → riga icone in alto (Magic Layers è la prima icona, poi Presentation, Social media, Video, Print Shop, Doc, Whiteboard, Website, Email, Photo editor, Custom size, Upload) → click Magic Layers → upload della hook slide dalla cartella locale (file picker mostra `slide-1.png`...`slide-8.png`, frame-173) → il progetto apre con ogni elemento (testo, forme) selezionabile e spostabile singolarmente. Demo dal vivo: sposta lo scarabocchio grafico, poi modifica il testo in "My morning routine" (con un typo scherzoso: *"I can't spell"*, 06:07).

Regola dichiarata: *"I only use magic layers if the fix is very small. Otherwise, I'll let ChatGPT do all the heavy lifting."* (06:10) — Magic Layers è un correttivo per micro-tweak, non il metodo principale.

---

## PARTE 4 — Stesso sistema per LinkedIn (cap. 6:14)

Narrato: il sistema non è specifico per caroselli Instagram, funziona anche per infografiche LinkedIn ("crashing on LinkedIn" — probabile refuso caption per "crushing"). Esempio: post LinkedIn reale di Artem (frame-176/193/195) mostrato come prova sociale — profilo **Artem Novitckii, Co-founder @ Aha!**, post sul tool stack aziendale (Stripe per pagamenti ricorrenti, Mercury/Revolut Business per banking) con infografica del flusso strumenti e CTA verso un video "che mostra l'interno di ogni tool menzionato" (link `lnkd.in/ec...dn` parzialmente leggibile). Metriche visibili: **1.271 reazioni** (incluso "Ariel Cohen and 1,271 others"), **390 commenti**, **28 repost**.

**I due riferimenti presi per il format infografico** (03:12/06:31–06:34, *"I found two infographics that I wanted to copy, this one and this one"*): uno dei due, mostrato integralmente (frame-197), è **"How LLM-SEO Finds Your Brand"** di **Madhav Mistry** — flowchart completo: User → Query → LLM Search Console → Query Parsing → Refined Question / First Answer → Large Language Model (icone Gemini, Claude) → AI Instructions → box "Choose a Path" → Extra Thinking Instructions / Extra Thinking Model LLMs (Claude 4 Sonnet, GPT-4o Reasoning, Gemini 2.5 Pro) → Deeper Reasoning Model → Retrieval Agents (Short-Term / Long-Term) → Retrieval Agent A / B → Public Web Sources / Search Engines (icone Blog, News, Google, Bing...) → footer "Master the Layers → Train the AI. Structure for retrieval. Publish for visibility." / "Structure → Retrieve → Cite | Repost it to your Network | Follow Madhav Mistry".

Prompt dichiarato a voce: *"I gave it a prompt and I just said recreate this infographic"* (06:34–06:38). Il prompt digitato in chat è visibile ma su più righe piccole e in parte sfocate (frame-196/199/200); i frammenti leggibili con sicurezza includono: *"...Google just killed SEO. [...] website will become invisible. They [...] the new Google Search, and it's the first time it's been updated in 25 years. [...] it's not really search anymore, it's [AI] looking for the answer [...] Generative Engine Optimization. Which means people need to structure content on your website in a way that AI engines like Gemini and ChatGPT actually cite your website as an answer. For example, turn your page headers into actual questions. Instead of 'Our Services,' write 'What does [your brand] do?' AI looks for question-answer pairs, so give it exactly that. [...] Comment SEARCH and I'll send you the skill + my full SEO playbook"* — ⚠️ trascrizione **best-effort**, alcune singole parole/frasi di collegamento non sono ricostruibili con certezza dalla risoluzione dello screenshot; il senso generale (script per un'infografica virale su "SEO è morto, arriva GEO") è comunque chiaro e confermato dal risultato generato.

**Risultato generato** (frame-201, perfettamente leggibile): infografica **"Google Search Changed. SEO Alone Is Not Enough."** — sottotitolo "What AI Mode means for your website, and how to optimize for GEO" — 4 sezioni numerate:
1. OLD SEARCH VS NEW AI SEARCH — schema "Old Search" (Search → Click → website → info) vs "New AI Search" (Question → AI answer → chat) — "Biggest shift in search in decades"
2. WHAT GOOGLE SAYS — box con "No magic community required"
3. YOUR GEO PLAYBOOK
4. WHAT TO IGNORE

più un box **"Claude GEO Audit Skill"** con esempio: *"Change 'Our Services' → 'What does [X] do?'"*, e CTA finale: **"Comment SEARCH and I'll send the skill + full GEO playbook"**.

Commento a voce sul risultato (06:38–06:45): *"it created this beautiful-looking LinkedIn post that I can probably get couple of hundred likes and couple of leads."*

---

## PREVIEW INIZIALE (0:00, prima del tutorial vero e proprio)

Lavagna Excalidraw **"ChatGPT Image for Instagram Carousel"** (frame-001/007/011) mostrata come teaser prima ancora di spiegare il metodo, con due caroselli affiancati:

- **"Carousel 1" (con Reference)** — le stesse 6 slide del carosello IG reale già pubblicato: "I AUTOMATED MY CAROUSELS WITH CHATGPT", "MOST PEOPLE WILL USE IT WRONG AND GIVE UP", "THE SECRET IS THE VISUAL BRIEF", "MAKE 3 VERSIONS OF SLIDE 1 FIRST", "THEN USE THIS REPEATABLE SYSTEM", "Comment IMAGE" (asterisco blu come motivo grafico ricorrente).
- **"Carousel 2" (No reference)** — la stessa infografica/tema "Google just killed SEO. GEO is in." mostrata poi per intero nella Parte 4 (stile bianco/nero minimal, non lo stile denso di frame-201 — probabile bozza precedente con lo stesso claim).

## RISULTATI REALI MOSTRATI — Instagram Insights del carosello già pubblicato

Narrato (00:01–00:11): *"the carousels I've made using Chat GPT image... actually posted one of them on my Instagram. It got nearly 100,000 views and a lot of engagement... Each carousel only took me like 15 minutes to make."*

Screenshot Instagram Insights (frame-004/005/006) della slide 1 "I AUTOMATED MY CAROUSELS WITH CHATGPT / The workflow is stupidly simple" con badge blu (etichetta piccola, non perfettamente leggibile) e mini-anteprima delle slide successive più "Swipe to steal the workflow". Pannello destro (parzialmente leggibile per via di sfocatura/compressione):
- **Views**: cifra a 5 cifre, area 8x.xxx — non leggibile con certezza al 100% per via dell'offuscamento in due dei tre frame; coerente con "nearly 100,000" dichiarato a voce.
- **Accounts reached**, **Followers/Non-followers %** (barre viola/bianca) — presenti ma percentuali esatte non trascritte per bassa confidenza.
- **Interactions**: **12,911** (leggibile, frame-004)
- **Comments**: **6,003** (frame-006)
- **Shares**: **1,743** (frame-006)
- Numero "Likes"/"Saves" presente ma cifra non trascritta con sicurezza sufficiente.

⚠️ Onestà sui numeri: solo Interactions (12.911), Comments (6.003) e Shares (1.743) sono trascritti con confidenza alta. Il numero di Views esatto non è leggibile con certezza nei frame disponibili — si riporta quindi la dichiarazione verbale ("nearly 100,000 views") come fonte primaria per quella cifra.

---

## LA COMUNITÀ / CTA FINALE

Narrato (07:24–07:33): *"I also have a school community where we do a weekly call where you can ask me any questions."* Frame-224 mostra una community Skool con card "AI CONTENT", nome community non perfettamente leggibile (assomiglia a "Artemis", coerente col nome dell'autore — non riportato come certo), post visibili: "Welcome to [...] 👋", "My AI Stack Right Now (Continuously Updated)", "System #002: Free Local Way to Transcribe Reels, TikToks and YT", "Discovery #001: How to Use ChatGPT Image 2 to Automate Instagram [...]".

Chiusura video (07:33–07:42): *"Hopefully, this system will help you generate more content and spend less time doing so. Subscribe for more videos like this. I post them every week."*

---

## CIÒ CHE IL VIDEO NON MOSTRA

- **Il prompt esatto e integrale usato per "recreate this infographic"** (LinkedIn) — solo frammenti leggibili tra motion blur e testo minuscolo (vedi sopra, sezione Parte 4).
- **Il contenuto completo delle slide 4, 6 e 7** del carosello Morning Routine — coperte solo dalle thumbnail nel tool Publer, mai aperte singolarmente a schermo intero con testo leggibile.
- **Nessun costo/pricing dichiarato** per ChatGPT Plus/Team, Canva Pro (necessario per Magic Layers) o Publer — il video presume l'accesso a questi strumenti senza discuterne il costo.
- **Nessun timer o durata reale del rendering** delle immagini ChatGPT — si vede solo "Thought for Xm Ys" nell'interfaccia, non il tempo reale trascorso dall'utente in attesa.
- **Il file `slide-count.md` e `SKILL.md`** del progetto Copy Writer non vengono mai aperti a schermo — si vede solo il loro nome nel tab Sources, non il contenuto.
- **Nessuna generazione di immagini con "Nana Banana" (Gemini)** mostrata dal vivo, nonostante sia citata a voce come alternativa a ChatGPT Image nell'introduzione — tutta la demo usa solo ChatGPT.

---

## CONFRONTO CON DIGITAL EMPIRE

**Cosa fa questo video meglio o più velocemente di come lavora DE oggi:**

1. **Visual anchor via multi-image reference, non template HTML fissi.** Il sistema DE per i caroselli (`carousel-empire`, verificato in `.claude/skills/carousel-empire/SKILL.md`) genera 7 slide da uno schema JSON fisso (`hook / problem / solution / how_it_works / proof / differentiator / cta`), renderizzate con **HTML + Playwright a 1080×1350**, palette e font invarianti (`#0A0A0A`, `#FF3D00`, Space Grotesk/Inter). È deterministico e brand-safe, ma ogni carosello DE ha **la stessa identica composizione grafica**, cambia solo il testo. Il metodo di Artem invece genera lo stile stesso via AI image (ChatGPT Image) ancorato a un'unica hook slide di riferimento — permette variazione visiva reale slide-per-slide (collage, texture, illustrazioni) che il sistema a template fisso di DE non può produrre.
2. **Deep-copy research prima del design.** Artem separa nettamente "far scrivere bene il copy" (40% del tempo, ChatGPT Project dedicato con Sources caricate) da "fare il design" — con un intero documento "The Carousel Bible" di psicologia e benchmark citati con fonte. `carousel-empire` ha regole di contenuto (headline max 6 parole, ecc.) ma non un progetto/knowledge-base dedicato alla ricerca di cosa rende un carosello virale con statistiche verificate e citate.
3. **Riuso dello stesso metodo su più piattaforme (IG + LinkedIn) con lo stesso prompt stack**, cambiando solo il "Carousel topic" nei placeholder. `carousel-empire` è scritto esplicitamente solo per Instagram (1080×1350, handle IG); DE non ha un equivalente dichiarato per LinkedIn infographic nello stesso skill.
4. **Anteprima gratuita pre-pubblicazione** (Publer's Instagram Post Preview) come step esplicito del workflow, prima di pubblicare — un self-check visivo "in the wild" del feed reale, in aggiunta a quello locale. `carousel-empire` ha un self-check visivo Step 5 (leggere ogni PNG con visione nativa) ma non un mockup del feed IG stesso.

**Cosa DE fa già meglio (o alla pari):**

1. **DE ha già un motore di generazione caroselli end-to-end**, non solo un metodo manuale copia-incolla di prompt in ChatGPT: `carousel-empire` produce automaticamente 7 PNG + caption + 25 hashtag suddivisi per volume, con uno script Python (`scripts/generate_carousel.py`) invocabile in un comando — l'intero flusso di Artem è invece manuale, slide-per-slide, "pick the best of N versions" a mano ogni volta (~10 minuti dichiarati, ma solo per 8 slide, con supervisione umana costante).
2. **Brand invarianti già codificati** (palette, font, logo, handle) — evita il rischio, presente nel metodo di Artem, che l'AI "derivi" leggermente lo stile tra una slide e l'altra nonostante il visual anchor (rischio implicito ammesso dallo stesso Artem: *"ChatGPT gets you 90 or 95% there... maybe one element or text is slightly off"*).
3. **Caption e hashtag generati con criteri di volume espliciti** (alto/medio/basso volume) nello stesso skill — nel video di Artem la caption/hashtag della morning routine non vengono mai mostrati a schermo.

**Cosa va rubato, concretamente:**

- Il **pattern "visual anchor" (prima slide come reference-image per tutte le successive)** applicato alla skill `image` di DE (che supporta già Gemini/Nano Banana con multi-image reference, Flux, Ideogram — verificato in `.claude/skills/image/SKILL.md`) come modalità alternativa a `carousel-empire` per caroselli con stile illustrato/organico, non solo card di testo su sfondo piatto.
- I **due prompt master riusabili** (Slide 1 / Slide [X]) con placeholder `[INSERT TEXT HERE]`, `[SLIDE TYPE]`, `[SLIDE GOAL]` — struttura pulita, riusabile 1:1 come blueprint per un nuovo modo di generare varianti in `carousel-empire` o in una skill gemella basata su image-gen.
- Il blocco **"Do not copy: exact text / exact branding / exact compositions"** — disciplina esplicita anti-plagio quando si usa un riferimento Pinterest/LinkedIn come ispirazione, utile da inserire come regola fissa in qualunque skill DE che usi immagini di terzi come riferimento visivo.

---

## CONSIGLI

*(nomi verificati in `.claude/skills/` prima di citarli)*

1. **Cosa migliorare in DE con questa conoscenza**: `carousel-empire` (SKILL.md) oggi produce solo caroselli a template HTML fisso — non c'è modo di ottenere uno stile "illustrato/collage" come quello mostrato nel video (asset grafici disegnati, texture, scarabocchi). Aggiungere allo Step 2 dello skill un ramo alternativo "stile AI-generativo": invece di renderizzare HTML con Playwright, generare la hook slide con la skill `image` (che supporta Gemini/Nano Banana con riferimento multi-immagine — vedi `.claude/skills/image/SKILL.md`, tabella "Model Comparison"), poi passare quell'immagine come reference alle slide successive, replicando esattamente il pattern "visual anchor" del video.

2. **Quale skill nuova creare**: non esiste oggi in `.claude/skills/` una skill dedicata alla ricerca di stile carosello ("visual research", tipo la ricerca Pinterest fatta a mano da Artem). Proposta: skill `carousel-visual-scout` che, dato un topic, propone 3-5 riferimenti stilistici (via WebSearch su Pinterest/Behance/Dribbble) con motivazione, da passare poi come `[reference image]` a `carousel-empire` o alla skill `image` — oggi questo passaggio in DE è del tutto assente (il brand è fisso, quindi non serve normalmente, ma serve per contenuti "fuori standard DE" tipo contenuti cliente white-label).

3. **Quale agente nuovo serve**: DE non ha un agente equivalente a un "copy project" con Sources dedicate e output strutturato (Playbook/Tier/Slide count motivato/Hook A-B-C con raccomandazione). La skill `carousel-empire` genera direttamente il JSON finale senza mostrare varianti di hook. Proposta: sotto-fase nello Step 2 di `carousel-empire` (o agente `carousel-copy-strategist` dedicato) che produce **3 varianti di hook con motivazione esplicita del perché una è la migliore**, prima di passare al render — replica diretta dello schema "HOOK A/B/C + RECOMMENDED" osservato nel video, oggi assente nello skill DE.

4. **Quale workflow nuovo costruire**: workflow "un topic → carosello Instagram + infografica LinkedIn dallo stesso contenuto", analogo alla Parte 4 del video (stesso prompt stack, cambia solo `Carousel topic`/piattaforma). Oggi `carousel-empire` è scoped solo a Instagram 1080×1350; non esiste un equivalente LinkedIn (dimensioni diverse, tono più "infografica dati" che "hook emotivo"). Va costruito come variante dello stesso skill con un secondo template dimensionale e tono, non da zero.

5. **Quale workflow/skill esistente potenziare, e con quale pezzo preciso**: `carousel-empire` (SKILL.md), Step 5 "Self-Check Visivo" — oggi la checklist verifica solo elementi di brand (logo, counter, handle, colori). Aggiungere un passaggio equivalente al tool Publer del video: dopo il render, montare le 7 slide in un mockup del feed Instagram (anche solo HTML/CSS locale che simula il carosello con puntini e swipe) per un controllo "come lo vedrà davvero l'utente sullo scroll", non solo PNG isolati — è il gap più concreto e riproducibile 1:1 dal video (Publer Instagram Post Preview, `publer.com/tools/instagram-post-preview`, gratuito, nessun login richiesto per l'anteprima).

**Nessun gap inventato oltre questi**: gli altri elementi del video (caption/hashtag, calendario di pubblicazione, monetizzazione) non vengono nemmeno mostrati a schermo dall'autore stesso — non c'è quindi materiale sufficiente per confrontarli con DE senza inventare.
