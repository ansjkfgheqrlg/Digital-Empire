# Contenuto Integrale — 8NSyI-npJCU
## "The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown)" — Jay E | RoboNuggets

**Fonte audio:** sottotitoli inglesi auto-generati YouTube (`8NSyI-npJCU.en.vtt`), letti per intero nella porzione iniziale 0:00–2:37 per calibrare tono/contesto; il resto del parlato è stato ricostruito dal testo *on-screen* mostrato a schermo parola per parola (più affidabile dei sottotitoli auto-generati per nomi propri e comandi).
**Fonte visiva:** 181/181 frame unici letti nativamente su 649 frame densi estratti (soglia scene-detector 3.0, intervallo 2.0s). Coverage 100% dei frame unici, 0 frame non processati. Dettaglio completo in `runs/max17-v05-jaye-agenticos/coverage.md`.
**Durata:** 21:38 (1298s) · **Canale:** Jay E | RoboNuggets · **Lingua:** inglese
**Run:** `empire-studio/runs/max17-v05-jaye-agenticos`
**Archiviato:** 2026-09-02 (Memory Empire Stage C)

> **Regola applicata:** trascrizione integrale, mai riassunta. Ogni elemento testuale comparso a schermo con contenuto informativo è riportato per esteso. Le incertezze di lettura sono dichiarate esplicitamente (marcate `inferito`), mai nascoste.

---

## ⚠️ AVVERTENZA SULLA NATURA DELLA FONTE (leggere prima di usare questo materiale)

Questo video costruisce l'intera narrazione attorno a **un solo elemento con fonte ufficiale esterna verificabile**: un post su X di **Thariq (@trq212), presentato nel video come "Anthropic Lead Engineer"**, riassunto in 6 regole "Then→Now" di context engineering. Il video **non mostra mai il post originale per intero** — solo il titolo (`frame-002 @0:02`) e una sintesi in 6 punti generata dalla routine "newsletter" dello stesso Jay (`frame-472/473/478 @15:40-15:44`). Il testo esatto pubblicato da Thariq **non è verificabile da questo video**.

**Tutto il resto** — il framework **ARMS** (Apps/Routines/Memory/Skills), la piramide di priorità, lo schema "Level 1/2/3" per ogni pilastro, la dashboard "Rubric Agentic OS", il "Rubric Second Brain" a grafo, l'agente cloud "Hermes", gli esempi cliente Stropro/Beetogreen, i claim numerici non verificati — è **costruzione proprietaria di Jay E (RoboNuggets)**, venduta nel suo corso a pagamento **"The Claude Living Masterclass"** dentro la community Skool "RoboNuggets" (frame-091, frame-497). Il video stesso è in parte un teaser promozionale di quel corso e della sua agenzia di consulenza "RoboLabs".

Questa distinzione è mantenuta rigorosamente in ogni sezione sottostante e nel campo `natura` di `atoms.json`.

---

## PARTE (a) — CONTENUTO CON FONTE UFFICIALE VERIFICABILE

Include: (a.1) le 6 regole "Then→Now" attribuite a Thariq/Anthropic, e (a.2) le funzioni native di Claude Code confermate a schermo tramite UI/output di prodotto reale (non l'interpretazione di Jay, ma l'evidenza visiva diretta del prodotto).

### a.1 — Le 6 regole "Then→Now" di context engineering (Thariq, @trq212)

**Fonte dichiarata a schermo:** post X di Thariq, titolo *"The New Rules of Context Engineering"*, sottotitolo *"For the Claude 5 generation"* (`frame-002 @0:02`, timestamp **0:02**).

**Trascrizione integrale**, così come compare nell'artefatto newsletter auto-generato da Jay (`frame-469`–`frame-478`, timestamp **15:36–15:54**), che è l'unico punto del video in cui le 6 regole sono riportate per esteso:

> Claude Code Just Changed Forever (6 New Rules by Anthropic Engineers)
>
> All the rules, and the free skill that audits your own setup against them.
>
> Claude's models have changed a lot this year, and the rules for setting them up changed with them. One of Anthropic's lead engineers just published the new set, and some are the exact opposite of the advice we have all been following for months.
>
> I break down all six in this video.
>
> The engineer is Tariq, and the article is at 4.3 million views. They stripped what Anthropic did to themselves. They stripped over 80% of Claude Code's system prompt, and the coding advice did not drop a point.
>
> The useful part is how Tariq wrote it. Every old rule sits next to the revised one, so you can see exactly what to undo. 4.3 million people have read it in a few days.
>
> **Here is the then and now, all six:**
>
> 1. **Then: rules. Now: judgment.**
>    Their own prompt went from a wall of do's-and-don'ts to one line about writing code that reads like the surrounding code.
>
> 2. **Then: examples. Now: interfaces.**
>    Examples for a few new models teach one way of doing a thing, and a well-named field teaches it better.
>
> 3. **Then: everything upfront. Now: progressive disclosure.**
>    A thick CLAUDE.md loads on every session and spends your tokens before you type a word.
>
> 4. **Then: repeating yourself. Now: simple tool descriptions.**
>    Saying it twice was a workaround for weaker models, and now it just clutters the session.
>
> 5. **Then: memory in CLAUDE.md. Now: auto memory.**
>    Facts about you belong in the memory system, not stuffed into a guidance file.
>
> 6. **Then: simple specs. Now: rich references.**
>    The highest-fidelity reference is my brand book in an HTML page that Claude reads as code while I see the colors.

**Nota sui claim numerici** (4.3 milioni di visualizzazioni, "80% del system prompt tagliato"): sono affermazioni **riportate** nell'artefatto generato da Jay, attribuite a Thariq/Anthropic ma **non verificabili indipendentemente in questo run** — non è mai mostrato il post originale né una fonte primaria ispezionabile. Trattarle come "dichiarate nel video", non come fatti confermati.

### a.2 — Funzioni native di Claude Code confermate a schermo (evidenza diretta di prodotto)

Questi elementi sono verificabili perché il video mostra **UI di prodotto reale o output di terminale reale**, non un'interpretazione di Jay:

1. **Skills Directory/marketplace nativa** (`frame-177 @5:52`, timestamp **5:52**) — tab Skills/Connectors/Plugins con filtro "Anthropic":
   ```
   /skill-creator          Anthropic   ⭐143.9K   "Create new skills, modify and improve existing skills..."
   /morning                Anthropic   ⭐9.9K     "Render the user's morning brief as a rich HTML artifact..."
   /canvas-design                      ⭐1.9M     "Create beautiful visual art in .png and .pdf documents..."
   /web-artifacts-builder              ⭐1.2M     "Suite of tools for creating..."
   ```

2. **Skill ufficiale `/skill-creator` in uso reale** (`frame-191 @6:20`, timestamp **6:20**) — Jay la invoca dal vivo per generare una nuova skill:
   ```
   /skill-creator Create a skill for something like this and name it "clean-up":
   codex tip: set an automation that keeps your computer running smoothly.
   - kill all headless instances after test runs
   - clear cache
   - audit computer for further opportunities
   ```
   Nota: il meccanismo (`/skill-creator`) è nativo e verificato; il **target creato** (la skill "clean-up" con la sua logica) è proprietario di Jay — vedi Parte (b).

3. **Modalità headless `claude -p`** (`frame-297/308 @9:52-10:14`, timestamp **9:52** e **10:14**) — comando CLI reale, completo di flag:
   ```
   claude -p /clean-up --model fable --effort xhigh --permission-mode bypassPermissions
   ```
   Output di terminale reale mostrato (estratto verificabile — `frame-295 @9:52`):
   ```
   $ claude -p /clean-up --model fable --effort xhigh --permission-mode bypassPermissions
   MODEL: FABLE   EFFORT: XHIGH   DURATION: 32s   EXIT: 0
   FINISHED: 20 Aug 2026, 11:39 am
   ```

4. **Sintassi regole permessi in `settings.json`/`settings.local.json`** (`frame-295/296 @9:52`, timestamp **9:52**) — testo di terminale reale, non un'invenzione di Jay:
   ```
   Permission allow rule (C:\Users\jedoe\.claude\settings.json): Write(.claude/**)
   is not matched by file permission checks — only Edit(path) rules are. Use
   Edit(.claude/**) instead (Edit rules cover all file-editing tools).

   Permission allow rule (C:\Users\jedoe\.claude\settings.local.json):
   Write(.vscode/**) is not matched by file permission checks — only
   Edit(path) rules are. Use Edit(.vscode/**) instead.

   Permission allow rule (.claude/settings.local.json): MultiEdit(.claude/**)
   is not matched by file permission checks — only Edit(path) rules are. Use
   Edit(.claude/**) instead (Edit rules cover all file-editing tools).
   ```

5. **Funzione nativa "Routines"** (`frame-480 @15:58`, timestamp **15:58**) — UI reale di Claude Code:
   ```
   Routines
   Create templated routines that can be kicked off on schedule, by API, or webhook.
   [What do you want automated?]
   suggerimenti: "Summarize my open PRs every weekday morning" |
   "Triage new issues and flag duplicates each morning" |
   "Draft release notes whenever a PR merges"
   [New routine ▾]  [Draft routine]
   Tabs: All | Calendar     Include completed     Search routines
   Nota UI: "Local routines only run while your computer is awake and online."
   ```
   Confermata di nuovo in `frame-564 @18:46` (timestamp **18:46**), home screen nativa "Welcome back, Jay" con sessione in coda visibile.

6. **Pannello Settings → Customize** (`frame-567 @18:52`, timestamp **18:52**) — categorie native reali:
   ```
   Customize: Skills | Connectors (selezionato) | Plugins | Memory
   Desktop app: General | Extensions | Developer
   ```

7. **Selettore modello nativo in chat** (`frame-564 @18:46`, timestamp **18:46**):
   ```
   Auto | Fable 5 | Extra
   ```

**Nota metodologica su a.2**: questi 7 elementi sono classificati `ufficiale` in `atoms.json` (campo `natura`) perché rappresentano **evidenza diretta di UI/output di prodotto**, indipendente dall'interpretazione di Jay — a differenza del framework ARMS e della dashboard, che sono software/concetti costruiti da lui e presentati come propri (vedi Parte b). Non sono comunque "documentazione ufficiale Anthropic" in senso stretto: sono osservazioni dirette di un prodotto reale fatte da un utente terzo in un video promozionale.

---

## PARTE (b) — COSTRUZIONE PROPRIETARIA DELL'AUTORE (Jay E / RoboNuggets)

Tutto quanto segue è il **prodotto didattico e commerciale di Jay E**, venduto nella community RoboNuggets (Skool) tramite il corso **"The Claude Living Masterclass"**. Non va mai archiviato o citato come standard Anthropic.

### b.1 — Intro e credenziali (0:00–0:44)

- `frame-001 @0:00`, `frame-005 @0:08` — hook di apertura: *"Claude has evolved with today's generation of Claude 5 models... but the way most people set up their agents and operating systems have not caught up."* Promessa: framework in 4 parti per *"usare gli agenti meglio del 99% delle persone"* — claim di marketing non verificabile.
- `frame-016 @0:30` — card presentazione "Jay Enriquez".
- `frame-017 @0:32` — slide credenziali: loghi **Unilever, Fresh, Microsoft, Virgin, Ogilvy, Knorr, Lipton** ("worked with brands you may know").
- `frame-018 @0:34` — slide formazione: **University of Technology Sydney — Master of Data Science and Innovation**.
- `frame-019 @0:36` — sito **RoboLabs** ("The Era of AI is Here / RoboLabs helps you lead it") — agenzia di consulenza AI di Jay.
- `frame-020–022 @0:38-0:42` — community **RoboNuggets** (mappa mondiale membri, logo animato).
- `frame-011/012 @0:20-0:22` — illustrazioni pixel-art "FASTER"/"CHEAPER" e fabbrica di robot-lavoratori — metafora visiva di marketing, prodotta dalla stessa micro-app "Generations" di Jay (confermato più avanti in `frame-617-620`, meta-conferma che le grafiche del video sono auto-prodotte).

### b.2 — Il framework ARMS (3:54–5:09, con anticipazione a 0:24)

- `frame-013 @0:24`, `frame-119 @3:56` — diagramma **"The ARMS Framework — Give Claude arms = Give it its own workspace"**: 4 icone su un tavolo — **Memory** (cassetto viola), **Routines** (orologio arancione), **Apps** (dispositivo blu), **Skills** (libro arancione).
- `frame-157 @5:12` — fonte scaricabile: PDF *"A RoboNuggets Guide — Set up your Agentic OS"*, path completo: `C:\Users\jedoe\Documents\App R\.CC\Lessons\Agentic OS\Resources\arms-agentic-os-guide.pdf` (confermato anche in `frame-641 @21:20`).
- **Definizione data nel PDF** (`frame-643 @21:24`): *"An agent is an AI that can do real work: read and write files, use tools, and finish tasks, not just answer questions. Out of the box, every conversation starts from zero. An operating system is the standing structure around the agent: what it shows you, what it runs on a schedule, what it remembers, and what it can reliably do. This guide works with any AI assistant that can read and write files."*
- **README del PDF** (`frame-255/260 @8:28-8:32`):
  ```
  START HERE
  READAME
  What this is. A setup guide for your agentic operating system: the four
  standing parts that make an AI assistant genuinely useful week after week,
  not just chat by chat.
  How to use it. Read the overview below, then set up one part at a time with
  pages 3 to 6. Each part has a copy-paste prompt, and the text in this PDF is
  selectable, so you can paste any prompt straight into your AI. Finish with
  the 7-day plan on page 7.
  The shortcut. Inside the RoboNuggets community at skool.com/robonuggets,
  members set up systems like this together...

  The ARMS framework
  An agent is an AI that can do real work... An operating system is the
  standing structure around the agent...

  A  Applications — The front pages. Small tools and at-a-glance views...
  R  Routines — The schedule. Repeated work that happens on time without you asking.
  ```
- **Prompt Claude Code usato per generare il PDF** (`frame-256 @8:30`): `Make a PDF guide with /robo on how to set up an Agentic OS` seguito da `/align 10`.
- `frame-163 @5:24` — la gerarchia disegnata come **piramide** in Excalidraw: base larga **SKILLS**, poi **MEMORY**, poi **ROUTINES**, punta stretta **APPS**. Ordine di priorità dichiarato dall'autore.

### b.3 — Schema "Level 1/2/3" per ciascun pilastro (euristica didattica di Jay, non terminologia Anthropic)

#### SKILLS (5:09–10:35)
- `frame-201 @6:40` — massima personale: *"SOPs. Do a task twice, make it into a skill."* Level 1: Pre-built Skills OR Build your own.
- `frame-215 @7:08` — **file integrale `SKILL.md` di `clean-up`** (proprietario di Jay):
  ```
  SKILL.md
  name: clean-up
  description: Run or manage the System Care routine (ID #0493) - the daily
  Windows maintenance job that kills headless/leftover and orphaned bun
  processes, clears old temp files, and logs a health report. Also has an
  audit mode that hunts for further opportunities. Triggers on "clean-up,"
  "clean up my computer," "run system care," "computer running hot/laggy,"
  "read the system care log," "is the cleanup schedule working," "/clean-up/audit,"
  "audit my computer."

  Clean-Up (System Care, ID #0493)
  Zero-token maintenance: a plain PowerShell script Windows Task Scheduler
  runs the agent.

  The pieces
  - Script: C:\ROBO\projects\jctc\ID 0493-system-care\system-care.ps1
  - Schedule: Task Scheduler task "Robo System Care" daily 7:00am, current user
  - Log: system-care-log.txt (append entry per run)
  - Project context: shared/projects/jctc/0493/context.md

  What one run does
  1. Kills, in this order:
     - browsers running with --headless
     - webdriver executables (chromedriver, msedgedriver, geckodriver)
     - node processes (parent game + Claude Code sessions and a stale one
       burned 36 CPU-hours)
     - orphaned bun processes
  2. Deletes temp files older than 7 days: %TEMP%, C:\tmp, C:\temp folders
  3. Appends a health report to the log: killed list, RAM freed, disk free,
     chromedriver counts, top 5 RAM and top 5 CPU processes
  ```
  *(font piccolo, alcune parole a bassa confidenza — marcate `inferito` in atoms.json).*
- `frame-226/229/233 @7:30-7:44` — struttura cartelle reale `.claude/skills/roles/`:
  ```
  .claude/skills/roles/
  ├── components/
  ├── drafts/
  ├── icons/
  ├── reference/
  ├── apps.md
  ├── backgrounds.md
  ├── brand-book.html
  ├── courses.md
  ├── infographics.md
  ├── life.md
  ├── SKILL.md
  └── slides.md
  ```
- `frame-241/242/243 @7:56-8:04` — artefatto HTML "BRAND BOOK — The ROBO style": nero `#131311`, arancione `#F17404` (accento principale), giallo `#F6C427` (accento secondario — valori a bassa confidenza); tipografia "Three voices, CLEAR jobs", corpo testo sempre peso 400.
- `frame-267 @8:52` — **prompt integrale "SKILLS · LEVEL 3: Turn thick skills into a skill tree"**:
  ```
  One giant SKILL.md is doing all the work. This splits it into a short
  router plus its own file set, so the agent reads only what it needs.

  Look through my skills folder (.claude/skills) and find my "thick" skills
  — any skill where one SKILL.md file is doing all the work (roughly 150+
  lines or several different jobs mixed into one file).

  Before restructuring anything, ask me these in one batch:
  1. Which skills do I actually use most weeks?
  2. Are any skills off-limits and not to be touched?
  3. How aggressive should the split be: light cleanup, or a full file tree
     per skill?

  Then restructure each thick skill into a skill tree:
  - SKILL.md becomes a short router: it lists, when it triggers, and a table
    pointing to the right file for each job.
  - Each distinct job, reference list, or template moves into its own
    clearly named file inside the skill folder (references/, templates/, or
    plain .md files).
  - The router tells the agent to read ONLY the file that matches the task,
    never everything at once.

  Rules:
  - Do not change what any skill does, only how it is organized.
  - Keep every trigger and every rule. Nothing gets lost.
  - A good split makes SKILL.md shorter, not longer.
  - Show me the before and after line counts for each skill.

  List the thick skills you found and your proposed split for each. Wait for
  my go before touching files.
  ```
  Soglia esplicita: **"roughly 150+ lines or several different jobs mixed into one file"** = regola pratica di Jay, non uno standard pubblicato da Anthropic. (Questa soglia è comunque riutilizzata più avanti in questo ciclo di ingestione — vedi BACKLOG B-039 — perché è misurabile e utile, pur restando di origine non ufficiale.)
- `frame-273 @9:04` — diagramma "Level 2: Thin Skills, Rich References".
- `frame-297/302-305 @9:52-10:08` — esecuzione reale della skill `clean-up` in modalità headless (report completo, vedi anche Parte a.2 per la porzione di output nativo):
  ```
  Clean-up ran. Nothing needed killing - no headless browsers, webdrivers,
  test leftovers, or orphaned bun processes.
  Today's log entry (2026-08-20 11:39): Killed: nothing; Freed: 1.1 MB of old
  temp files (temp folder now 172 MB); Disk C: 397.3 GB free; Processes:
  chrome x24, node x08; Top RAM: Memory Compression 1803 MB, claude 833 MB,
  claude 781 MB, Code 625 MB, MsMpEng 532 MB; Top CPU (lifetime seconds):
  chrome 2942, chrome 1347, chrome 475, ArmouryCrate 247, Code 243.
  Next step: nothing needed - the 7am daily schedule keeps this running on
  its own.
  ```
- `frame-308 @10:14` — **prompt integrale "SKILLS · LEVEL 3: Run skills from your OS with claude -p"**:
  ```
  Headless mode means Claude runs a prompt without a chat window. This
  wires the buttons in your favorite skills to buttons in your own software.

  I want to run my Claude Code skills from buttons in my own software,
  without opening a chat window. This works through headless mode: the
  command 'claude -p "prompt"' runs one prompt and exits.

  Before you build anything, ask me these in one batch:
  1. Which app should hold the buttons: my dashboard HTML, a local web app,
     or something else?
  2. Which 3-5 skills do I run often enough to deserve a button?
  3. Should each button offer options (model, effort level, an extra input
     field), or fire with defaults?

  Then build it:
  - Add one button per skill in my app. Each button runs the matching skill
    headlessly, for example: claude -p /clean-up --model claude-sonnet-5
  - Buttons that need options get a small picker (model, effort) that feeds
    into the command
  - Show run status next to each button (running, done, failed) and where
    the output landed
  - If my app is plain HTML with no server, add the smallest possible local
    helper: an endpoint that shells out claude -p and wire the buttons to it

  Log every run to a simple runs.log file so I can see what fired and when.
  Walk me through one real button press, end to end, before calling it done.
  ```

#### MEMORY (10:35–14:34)
- `frame-325/326 @10:48-10:50` — "MEMORY — Context builds up as you work. Where it lives." Level 1: Filedump - a workspace is just a folder.
- `frame-333-395 @11:04-13:18` — struttura cartelle root reale `C:\ROBO` (leggibilità parziale): `agents`, `.claude`, `codex`, `content`, `dashboard`, `design`, `excalidraw`, `generations`, `hermes`, `shared`, `temp`, `tools`, `.gitignore`; file root `AGENTS.md`, `CLAUDE.md`, `COMMUNITY.md`, `CONTENT.md` e altri `.md` per dominio.
- `frame-369 @12:16` — diagramma "Level 2: Routers + a tree of files".
- `frame-372-381 @12:22-12:40` — Second Brain: anelli concentrici **APPLICATIONS** (esterno) → **ROUTINES** → **MEMORY** → centro **CLAUDE.md**, con 5 cluster dipartimentali: **CONTENT** (viola), **BUSINESS** (viola), **PERSONAL** (giallo), **PRODUCT** (ciano), **COMMUNITY** (ciano). Conteggi indicativi a bassa confidenza: Content ~999/10999, Business 1543/2783, Personal 23579, Community 3242. Campo di ricerca: "Search 60,601 files..." (`frame-340 @11:18`).
- `frame-387/394/400 @12:52-13:18` — **file integrale `CONTENT.md`** (ricostruito su più frame, media confidenza sulle parole esatte):
  ```
  CONTENT.md

  CHOICE
  1 - a3x new ideas
    vidiq, x, google // arXiv, reviews, own ideas
    - Skills: master-content-selection (Ø/dbl) — trend research for content
      opportunities
    - Skills: real-tweet / youtube-numerize (shared) — Gemini-assisted
      research from incoming videos
    - Files: shared/research/history/topic-shortlist.csv (shared) — 5 star
      shortlist, swipe file for flagged topics
    - Files: dashboard/data/content-shortlist.json — "Shortlist" tab

  2 - select idea
    just go do something
    - Skills: master-content-selection (Ø/dbl) — pull preferred topic
    - Files: shared/projects/ (shared) — folders prefixed "active-",
      pre-active video projects
    - References: project_video_production_queue (shared) — Q2 content
      target

  PRODUCTION
  3 - research and write flow
    notepad, cc to research
    - Skills: master-writing (shared) — script lessons, hook research,
      structure
    - Skills: notewise / graphity / real-tweet / youtube-numerize (shared) —
      research inputs
    - Files: shared/projects/<script-title>/outline.docx — in-progress
      script
    - Thinking: project_content_pipeline_review (v2) — 3-phase framework
      (Ideas / Scripting / Distribution)

  4 - ...
    - Reference: creator-benchmark.md — Jay or other creators to X10 pace
      (avg 3 posts per week)
    - Files: strategy.md — first draft, channel, timeline
    - Feedback: project_content_review_us_english.md — AI spelling rules
  ```
- `frame-406 @13:30` — **prompt integrale "MEMORY · LEVEL 2: Build router files for your workspace"**:
  ```
  My workspace has grown and it's getting hard for you to find things.
  Build me router files instead of reorganizing my folders.

  A router file is a short markdown index that points an agent to where
  things live, so it can jump straight to the right folder instead of
  searching everything.

  Ask me first, in one batch:
  1. What are the 3-4 main areas of my work (e.g. content, clients, money,
     health)?
  2. Which files or folders do I touch most often?
  3. Is anything private that should stay out of the indexes?

  Then:
  1. Explore the workspace and map what actually lives where
  2. Write one master router at the root (CLAUDE.md if this is Claude Code)
     — who I am in one line, my main areas, and a table pointing each area
     to its folder and its own index file
  3. Write one short index per area (like CONTENT.md or CLIENTS.md) listing
     its key files, one line each
  4. Keep every index a page — pointers, not documentation
  5. End the master router with the rule you will follow from now on: when
     a file moves or a new project starts, update the router in the same
     turn — a stale pointer is worse than no pointer
  ```
  **Questa singola regola** ("a stale pointer is worse than no pointer") è quella applicata come patch al `CLAUDE.md` radice di Digital Empire in questo ciclo (Stage D-F, vedi ingestion log).

#### ROUTINES (14:34–18:33)
- `frame-439 @14:36` — "ROUTINES — For when you've mastered Skills and Memory, you can now schedule them into automated 'ROUTINES'." Level 1: Local routines - run while the PC is on.
- `frame-456 @15:10` — **configurazione integrale di una Routine reale** ("YouTube to Substack daily", proprietaria di Jay, costruita sulla funzione nativa Routines):
  ```
  Routines / YouTube to Substack daily                          [Run now]

  Description: Daily: turn any new RoboNuggets YouTube video into a 3x
  write draft via the newsletter skill, log it, and ping Jay on Telegram
  every run.
  Status: Active — Next run tomorrow at 8:00 AM
  Folder: C:\ROBO
  Repeats: Every day at 8:00 AM

  Instructions:
  You are running an unattended daily automation for Jay (RoboNuggets). It
  works entirely from C:\ROBO. Do NOT post, publish, or email anything
  anywhere — this produces a draft for review only.

  GOAL: If a new video was published on Jay's YouTube channel, produce a
  Substack newsletter draft (3 full variants) using the newsletter skill,
  log it, and ping Jay on Telegram. Every run ends with a Telegram ping and
  a run-log entry, whatever the outcome.

  KEY PATHS:
  - Project: C:\ROBO\shared\projects\A-0313-substack-newsletter
  - Workshops save to: drafts\[YYYY-MM-DD]-[video-id]-workshop\
  - Canonical workshop template: drafts\2026-07-06-VoK9Kggk78-workshop\
  - Skill: C:\ROBO\.claude\skills\newsletter\SKILL.md (master newsletter skill)
  - Logs: newsletter-log.json (what's been sent)
  ```
- `frame-497-512 @16:32-17:02` — community classroom (moduli corso) e diagramma **"Level 2: Always-on - Hermes in the cloud"**: laptop ⇄ nuvola etichettata "Hermes", agente cloud open-source promosso nel corso "Hermes Agent Masterclass — most powerful open-source 24/7 Agent on the planet" (claim non verificato).
- `frame-511 @17:00` — lista Routines con motore di esecuzione: `morning sync conflict check`, `07:00 client health scan — Hermes`, `08:00 YouTube to substack daily — Desktop`, `09:00 daily inbox digest team — Desktop`, `11:00 deliverables status sweep — Hermes`, `13:00 community pulse digest — Hermes`, `16:30 content pipeline check — Hermes`, `18:00 client report drafts — Hermes`. Footer: **"Claude Desktop 3 · Hermes 14"**.
- `frame-520-530 @17:18-17:38` — sito **Syncthing** (syncthing.net — riferimento esterno reale, non prodotto Anthropic/RoboNuggets) e **prompt integrale "ROUTINES · LEVEL 3: Two-machine sync with Syncthing"**:
  ```
  One prompt, sent to Claude Code on BOTH machines: your computer and your
  always-on machine. Each side gets half of it.

  You are setting up one half of a two-machine sync. This same prompt is
  being run on my other machine, so first detect which machine you are on
  and do your half.

  Goal: keep one shared folder in sync between my main computer and my
  always-on machine using Syncthing, so agents on both sides see the same
  files.

  Before touching anything, ask me these in one batch:
  1. Which folder should sync: my whole workspace, or just a shared
     subfolder?
  2. What is the other machine (name and OS), and how do the two machines
     reach each other: same network, Tailscale, or over the internet?
  3. What must NEVER sync (secrets, node_modules, temp folders)?

  Then:
  1. Install Syncthing for this OS if it's missing, and set it to start on
     boot
  2. Add the folder I chose, with an ignore file covering my exclusions
  3. Show me this machine's Device ID, then ask me for the other machine's
     ID and add it as a trusted device
  4. Share the folder and wait for the other side to accept
  5. Verify: create a test file, confirm it appears on the other machine,
     then delete it
  6. Report exactly what you set up and how I check sync status later

  Security rule: never expose the Syncthing web UI to the internet. Local
  access only.
  ```

#### APPS (18:33–21:06)
- `frame-571 @19:08` — "APPS · Level 2: Search what exists - CLI, MCP, API" (nessun "Level 1" esplicito mostrato per questo pilastro — gap dichiarato dal video stesso).
- `frame-577 @19:12` — **file integrale `SKILL.md` di `search-connectors`** (proprietario di Jay):
  ```
  SKILL.md
  API for X. Any MCP server for X.

  Search Connectors
  Given an app or service, find the best ways to hook into it. Quick pass,
  not an audit.

  Workflow
  1. Identify the app. From /search-connectors (say) or the natural ask
     (for example "MCP for Notion?"). If the vendor's official site/GitHub
     already has a documented API or MCP server, that outranks everything
     else.
  2. Community pass, in order: CLI, then API, then MCP (SDKs/wrappers), then
     GitHub search.
     - github search "<name> cli" — filter stars, sort: best match
     - MCP: check github.com/modelcontextprotocol/servers and a web search
       for "MCP server <name>"
  3. Keep the format 1-2 per category. Health check each pick: last commit
     date, stars, archived or not. Skip anything with no commits in a year
     unless it's the only option, then flag it.
  4. Report using the format below.
  5. End with one recommendation + the install offer, stated flat, not a
     question. If Jay says yes, install and verify it runs (version check
     or a harmless read command).

  Report format:
  Connectors for <app>
  - CLI (vendor): <name> — <link> — one line on what it covers
  - API: <REST/GraphQL> — <link>
  - MCP: <name> — <link> — <stars>
  ```
- `frame-587-595 @19:32-19:48` — esecuzione reale `/search-connectors for Adobe Premiere Pro` (output completo):
  ```
  Connectors for Adobe Premiere Pro (Adobe)
  Official (Adobe)
  - CLI: none exists.
  - API: UXP scripting API — runs inside Premiere (25.6+, enable in
    Preferences > Plugins > Developer mode). Legacy ExtendScript supported
    until Sept 2026.
  - MCP: none official.

  Community
  - CLI: nothing healthy — only a 1-star macOS repo, skip.
  - API/SDK: nothing beyond the official UXP samples has starter code.
  - MCP: hetpatel-11/Premiere-Pro-MCP — npm install -g
    adobe-premiere-pro-mcp — 462 stars, updated yesterday. Windows +
    Premiere 2026+.

  Rec: the hetpatel MCP — most stars, active daily, Windows-tested, 282
  editing tools. Could pair it with your existing sector-video-editing
  skill.

  Sources: Adobe UXP for Premiere, Premiere Scripting Guide, hetpatel MCP
  repo.
  ```
  Confermato da repository GitHub reale aperto a schermo (`frame-595 @19:48`): **`hetpatel-11/Adobe_Premiere_Pro_MCP`** — 462 star, 98 fork, 143 commit. Un secondo repo, **`mvanhorn/cli-printing-press`** (297 branch, 1.851 commit, 4.5k star), è mostrato in `frame-602 @20:02`.
- `frame-605-610 @20:08-20:18` — clip incorporata da un altro video di Jay che promuove il repo `printing-press-library` — autopromozione incrociata.
- `frame-613 @20:24` — "Level 3: Build your own - connectors and apps".
- `frame-617-620 @20:32-20:38` — micro-app **"Generations"** (galleria immagini/video generati da Jay, incluse le grafiche pixel-art di questo stesso video — meta-conferma che le illustrazioni sono auto-prodotte).
- `frame-629 @20:56` — micro-app **"Excalidraw Landing Pad"** (`C:/ROBO/output/excalidraw-landing-pad/index.html`): libreria diagrammi pronti — "Pixel Agents - Blue", "ARMS Pyramid + Levels", "Section 04 How - Pixels vs Words". Conferma che il diagramma piramidale ARMS è un asset auto-prodotto per il video, non un artefatto Anthropic.

### b.4 — Dashboard "Rubric Agentic OS" e "Rubric Second Brain" (software custom di Jay)

- `frame-001 @0:00`, `frame-028-039 @0:54-1:16` — layout completo della dashboard personale: colonna sinistra **Micro Apps** (Generations, Teleprompter, Second Brain, Excalidraw) + **Calendar** (Wk34, Aug 20 2026, meeting list); colonna destra **Email** (47 emails past 24h, box "Flagged - Needs Jay"), **Skills Deck** (`/sprint-planning`, `/newsletter`, `/games` = Opus X-High; `/clean-up` = Fable X-High) e **Routines** (tabella oraria 08:00-21:30 con stati done/Desktop/NEXT/QUEUED); footer "Claude Desktop 5 · Hermes 14"; widget YouTube Studio (170,000 subscribers, 8.5M lifetime views, 5 longforms this month).
- `frame-008 @0:14` — popup di configurazione skill nella dashboard: griglia Model×Effort (Haiku/Sonnet/Opus/Fable × Low/Medium/High/Max).
- `frame-041/046 @1:20-1:30` — autolimitazione dichiarata da Jay: *"questa interfaccia visiva cattura solo il 20-30% di quello che faccio con Claude Code"* — il resto lo fa da CLI/chat, non dalla dashboard.
- `frame-063/064 @2:04-2:06`, `frame-115-117 @3:48-3:52` — "Rubric Second Brain": grafo a nodi con anelli concentrici e cluster colorati (vedi b.3/Memory per il dettaglio).
- `frame-078-081 @2:34-2:42` — **esempi cliente** (case study commerciali dell'agenzia RoboLabs, non riferimenti Anthropic): **"Stropro Agentic OS"** (servizi finanziari Australia — Market Clock, Capital Deployed $1.6Bn+, confermato dal sito reale stropro.com) e **"Beetogreen Agentic OS"** (flotta e-bike — Kilometres Ridden 482,000, Fleet Health).
- `frame-087 @2:52` — community RoboNuggets: 1.2k Members, 51 Online, 4 Admins, badge "Official member of the Claude Partner Network".
- `frame-091 @3:00` — struttura del corso a pagamento **"The Claude Living Masterclass"** (Volume A/B/C con moduli su ARMS, Skills, Memory) — conferma che l'intero video è un teaser/derivato del corso.
- `frame-094 @3:06` — modulo corso **"Agents-as-a-Service"** ("The DOTS Framework", pricing & closing, contratti/fatturazione) — puro contenuto commerciale.

---

## 3. CONFRONTO CON DIGITAL EMPIRE (riportato da `video-analysis.md`, non ripetuto per esteso)

Il confronto completo punto-per-punto tra questo standard proprietario e lo stato reale di Digital Empire (verificato leggendo `.claude/agents/` e `.claude/skills/` sulla root del progetto) è in `runs/max17-v05-jaye-agenticos/video-analysis.md`, sezione "CONFRONTO CON DIGITAL EMPIRE". Il gap più concreto e misurato: **115 dei 170 `SKILL.md` di DE (68%) superano le 150 righe** — la stessa soglia esplicita usata nel video (`frame-267`, prompt "Level 3 — skill tree") per definire una skill "grassa" da spezzare. Vedi `BACKLOG.md` voce B-039 per il rimedio proposto (non eseguito in questo ciclo, da approvare).

---

*(Trascrizione integrale completa, basata su 181/181 frame unici + sottotitoli inglesi. Nessun contenuto riassunto. Fonte dettagliata frame-per-frame: `runs/max17-v05-jaye-agenticos/video-analysis.md`.)*
