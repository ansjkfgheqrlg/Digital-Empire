---
Type: SOURCE
Status: Active
Tags: #claude-code #agentic-os #context-engineering #skills #memory #routines #progressive-disclosure #jay-e #robonuggets #max17
Created: 2026-09-02
Last updated: 2026-09-02
---

# Source: Jay E | RoboNuggets — The NEW Agentic OS standard for Claude 5 Models is here (Full Breakdown)

## ⚠️ Avvertenza — fonte in parte promozionale (leggere per prima)

Questo video costruisce tutta la sua narrazione attorno a **un solo elemento con fonte ufficiale esterna verificabile**: un post su X di **Thariq (@trq212), presentato come "Anthropic Lead Engineer"**, riassunto nel video in 6 regole "Then→Now" di context engineering — il post originale non è mai mostrato per intero, solo il titolo e una sintesi generata dall'autore stesso. **Tutto il resto** — il framework **ARMS** (Apps/Routines/Memory/Skills), la piramide di priorità, lo schema "Level 1/2/3", la dashboard **"Rubric Agentic OS"**, il **"Rubric Second Brain"**, l'agente cloud **"Hermes"**, gli esempi cliente, i claim numerici — è **costruzione proprietaria di Jay E (RoboNuggets)**, venduta nel suo corso a pagamento **"The Claude Living Masterclass"** dentro la community Skool "RoboNuggets", e il video stesso funge in parte da teaser di quel corso e della sua agenzia "RoboLabs". Chi riusa questo materiale fra sei mesi deve saperlo prima di citarlo come "standard".

## Overview

Walkthrough di 21m38 (EN, batch `max17` 5/8) in cui l'autore presenta il proprio "Agentic OS" personale — una dashboard custom costruita con Claude Code ("Rubric Agentic OS") — organizzato secondo un framework proprietario a 4 pilastri (**ARMS**: Applications, Routines, Memory, Skills), ciascuno con uno schema didattico "Level 1/2/3" di maturità crescente. Il contributo con fonte ufficiale reale sono le **6 regole "Then→Now"** di context engineering (Thariq/Anthropic) e diverse **funzioni native di Claude Code confermate a schermo** (Skills Directory, `/skill-creator`, modalità headless `claude -p`, Routines native, Settings→Customize, selettore modello).

## Dati Tecnici

- **Video ID:** 8NSyI-npJCU
- **Durata:** 21m38s (1298s)
- **Canale:** Jay E | RoboNuggets — agenzia "RoboLabs", community "RoboNuggets" su Skool · **Lingua:** EN
- **Formato:** Talking head + dashboard custom screen-share + Claude Code UI nativa + Excalidraw + artefatti PDF/HTML
- **Frame:** 649 densi @2s → 181 unici sopra soglia | **Frame letti: 181/181 — coverage 100%** | NO-FINTO: PASS
- **KA:** 70, classificati per `natura`: **10 ufficiale / 56 proprietario / 4 riferimento-esterno**
- **Processing:** pipeline Empire Studio (sessioni precedenti) · Memory Empire Stage C-H 2026-09-02
- **Run:** `empire-studio/runs/max17-v05-jaye-agenticos`

## (a) Contenuto con fonte ufficiale

Le 6 regole "Then→Now" di context engineering, attribuite a Thariq/Anthropic (fonte: `frame-002 @0:02`, trascrizione integrale `frame-472/473/478 @15:36-15:44`):

```
1. Then: rules.              Now: judgment.
2. Then: examples.            Now: interfaces.
3. Then: everything upfront.  Now: progressive disclosure.
4. Then: repeating yourself.  Now: simple tool descriptions.
5. Then: memory in CLAUDE.md. Now: auto memory.
6. Then: simple specs.        Now: rich references.
```

Più 7 funzioni native di Claude Code confermate a schermo con evidenza diretta di UI/output (non l'interpretazione di Jay): Skills Directory/marketplace, skill ufficiale `/skill-creator` in uso reale, modalità headless `claude -p --model --effort --permission-mode`, sintassi permessi `settings.json` (`Write()` vs `Edit()`), funzione nativa "Routines" (schedule/API/webhook), pannello Settings→Customize (Skills/Connectors/Plugins/Memory), selettore modello Auto/Fable/Extra.

## (b) Costruzione proprietaria di Jay E — framework ARMS

```
A — Applications  — le front page, tool e viste a colpo d'occhio
R — Routines      — lo schedule, lavoro ripetuto senza chiedere
M — Memory        — dove vive il contesto che si accumula lavorando
S — Skills        — SOP: fai un task due volte, trasformalo in skill

Piramide di priorità: base SKILLS -> MEMORY -> ROUTINES -> punta APPS
Ogni pilastro ha 3 livelli di maturità (Level 1/2/3), euristica di Jay,
non terminologia Anthropic.
```

Il gap più utile trovato dentro questa costruzione proprietaria: il prompt "Skills · Level 3" usa la soglia esplicita **"roughly 150+ lines"** per definire una skill "grassa" da spezzare in router + file dedicati — soglia riusata in questo ciclo di ingestione per misurare un problema reale in DE (vedi sotto).

## Confronto con Digital Empire — il gap misurato

Verificato leggendo realmente `.claude/agents/` e `.claude/skills/` (170 cartelle) sulla root di DE: **115 delle 170 `SKILL.md` (68%) superano le 150 righe**, la stessa soglia usata nel video per definire una skill da spezzare in router + file dedicati. Le 5 peggiori: `cro-youtube-lead-magnet` (5.160 righe), `cro-call` (5.146), `cro-strategy-social-(ig-tiktok)` (3.942), `printing-press` (3.639), `cro-funnel-architect.md` (2.771). Una skill si carica **intera** quando si attiva — migliaia di righe caricate per rispondere a una domanda che ne richiede decine sono budget bruciato a ogni invocazione. **Non risolto in questo ciclo** (refactoring di 115 file, va approvato da Max): registrato come **B-039** in `company/Memory/BACKLOG.md`.

Il pattern "master router" per la memoria (Level 2 Memory nel video: `CLAUDE.md` che punta a indici per dominio) è invece **già presente in DE** e concettualmente allineato — solo mancava la regola esplicita sull'aggiornamento dei puntatori, ora aggiunta.

## Key Quotes

> "Claude has evolved with today's generation of Claude 5 models... but the way most people set up their agents and operating systems have not caught up." [hook di apertura, marketing]

> "Here is the then and now, all six" [introduzione alle 6 regole, frame-472 @15:40]

> "A stale pointer is worse than no pointer." [prompt "Memory Level 2 — router files", frame-406 @13:30 — regola applicata in questo ciclo]

> "Look through my skills folder... find my 'thick' skills — any skill where one SKILL.md file is doing all the work (roughly 150+ lines or several different jobs mixed into one file)." [prompt "Skills Level 3", frame-267 @8:52 — soglia usata per misurare il gap DE]

## Azione Concreta (Enrichment)

Perimetro imposto dal task, esplicitamente **piccolo**: nessuna skill o agente toccato in questo ciclo.

- **`CLAUDE.md` radice** (**+4 righe, 0 cancellazioni**) — nuova regola "quando un file si sposta/rinomina, il puntatore va aggiornato nello stesso turno", presa dal prompt "Memory Level 2" del video, con fonte in linea `(fonte: 8NSyI-npJCU, 13:30)`.
- **`company/Memory/ROUTINES.md`** (**creato ex-novo**) — indice reale delle automazioni schedulate di DE, verificato di persona (script letti, Windows Task Scheduler interrogato dal vivo): 4 automazioni attive (hook sync `empire-sync.ps1`, hook Emperator, hook guard graphify, task Windows "LinkedIn Daily Outreach"), 5 task registrati ma disabilitati/scaduti, 3 infrastrutture pronte senza run attive. Nessuna automazione inventata.

**NON costruito, dichiarato:** refactoring delle 115 `SKILL.md` sopra le 150 righe — proposta registrata come **B-039**, da approvare da Max prima di partire (tocca 115 file).

## Backlog aperto (registrato, non applicato)

- **B-039** — 115 delle 170 `SKILL.md` di DE superano le 150 righe; rimedio proposto: refactoring a router + file dedicati affidabile a `skill-creator`/`chief-forge` (già esistenti). Da approvare da Max.

## Connessioni

- [[Source_Nate_Herk_Claude_Second_Brain_Levels|Nate Herk — Every Level of a Claude Second Brain Explained (batch max17, 8/8)]] — stesso tema di fondo (architettura di memoria/second brain su Claude Code), stesso batch: là la tassonomia è 5 livelli di *retrieval* per la wiki, qui è "Level 1/2/3" per Skills/Memory/Routines/Apps — entrambi euristiche didattiche di un creator, non standard Anthropic, ed entrambi confrontati onestamente con lo stato reale di DE.
- [[Source_CS2_Bonus_04_Claude_Skills|Claude Speedrun 2 — Bonus 4: Claude Skills]] — stesso oggetto tecnico (struttura `SKILL.md`, front matter, `references/`) verificato da due fonti indipendenti: qui il video mostra la soglia pratica "150+ righe = skill da spezzare", là la struttura tecnica ufficiale del formato — insieme confermano che il formato skill già in uso da DE è corretto, e che il problema è la disciplina di progressive disclosure, non il formato.
- [[Source_Riccardo_Belli_Claude_Codex_Setup|Riccardo Belli Contarini (Martes AI) — Claude Code + Codex: Il Setup di cui NESSUNO Parla (batch max17, 6/8)]] — stesso genere di fonte (creator che vende un setup Claude Code avanzato come "standard"), stesso trattamento metodologico: verificare cosa è realmente nuovo/ufficiale prima di adottarlo, dichiarare esplicitamente cosa NON serve a DE invece di costruire per inerzia.
- [[Tool_Conoscenza_Empire_Agente|conoscenza-empire — Biblioteca Vivente]] — il principio "progressive disclosure" al centro delle 6 regole ufficiali di questo video è lo stesso principio architetturale che governa come `conoscenza-empire` distribuisce formazione a comando invece di caricare tutto sempre.
