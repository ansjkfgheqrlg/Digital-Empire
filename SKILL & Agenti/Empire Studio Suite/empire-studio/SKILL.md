---
name: empire-studio
description: "Empire Studio - workflow gerarchico (non una singola skill) per ingerire conoscenza da YouTube, TikTok, siti web e progetti/repo, GUARDARE davvero i video (frame estratti con yt-dlp+ffmpeg + visione nativa di Claude, no API), forgiarla via content-forge e versarla nella wiki di Digital Empire che alimenta Claude Code. Organizzazione aziendale a 4 livelli (L1 Conductor, L2 Reparti, L3 30+ agenti a 7 file, L4 skill a tier di calibro), 9 reparti (4 di ricerca simmetrici: YouTube/TikTok/Web/Progetti-Repo + Processing&Vision, Forge&Wiki, Strategy, Verification&Control, Memory). Multi-strategia, ecosistema di memoria reale, controllori, ruflo/swarm. CLI-only, no API, no paid. ATTIVAZIONE NATURALE (nessun comando): si attiva da sola quando l'utente passa un link (YouTube/TikTok/sito/repo) o chiede di guardare/studiare/ingerire un contenuto per Digital Empire. Nessuno slash command da digitare."
version: 2.0.0
type: workflow
activation: naturale (nessun comando - basta passare un link o chiedere di ingerire/studiare un contenuto)
---

# Empire Studio - Kernel

> **Da un link grezzo (YT/TikTok/web/repo) a conoscenza operativa nella wiki di
> Claude Code** - tramite un'organizzazione gerarchica di reparti, agenti e
> skill, con visione reale dei video, memory-first, CLI-only.

**Attivazione: NATURALE, nessun comando.** L'utente non digita niente di tecnico.
Si attiva da sola (direttamente o richiamata dal router di **Memory Empire**) quando:
- l'utente **passa un link** (YouTube, TikTok, sito, repo/cartella);
- l'utente dice "guarda questo video", "studia questa repo", "prendi tutta la
  formazione da qui", "mettilo nella wiki", o simili;
- si parla di ingerire/studiare contenuti per Digital Empire.

Quando si attiva, Claude (Conductor) esegue **tutto da solo**: guarda il video
(frame reali + visione), estrae il transcript e TUTTA la conoscenza (mai
riassunti), forgia via content-forge **gestito dagli agenti**, e carica il
risultato sia nella **wiki di Digital Empire** sia nella skill **Memory Empire**.

---

## Invarianti (non negoziabili)
1. **NO-STUB**: niente agenti/skill finti. `validator.py` e' il cancello.
2. **NO-FINTO**: se Claude non ha guardato il frame, non scrive cosa contiene. `➕` per inferenze.
3. **Il video va visto**: frame reali (ffmpeg) + visione di Claude, non transcript da solo.
4. **CLI-only, no API, no paid**: yt-dlp, ffmpeg, playwright, python. Visione = Claude.
5. **Memory-first (P10)**: `memory_manager.py` dopo ogni azione, 16 categorie reali.
6. **Tracciabilita' (P12)**: ogni atomo -> `video-id#ts + frame-NNN.png` o `file:riga`.
7. **content-forge -> wiki**: l'output finale e' nella wiki di Digital Empire.

## Come funziona (sintesi)
Tu dai un link/percorso. Il **Conductor** (L1) sceglie il reparto e la strategia,
poi guida la **pipeline a 9 stage** (ingest -> frame -> visione Claude -> atomi ->
verifica -> forge -> wiki -> update proposals -> memory). I reparti di
**Verification** e **Memory** lavorano in parallelo come controllori e archivisti.

Dettaglio completo: `references/ARCHITECTURE.md`.
Regole di costruzione: `references/CONVENTIONS.md`.
Stato reale del roster: `agents/CATALOG.md`.

## Pipeline (vedi ARCHITECTURE.md §5)
`Stage 0 memory+strategy -> 1 ingest -> 2 frame -> 3 VISIONE(Claude) -> 4 atomi ->
5 verifica -> 6 forge -> 7 wiki -> 8 update proposals -> 9 memory close`

## Struttura (progressive disclosure)
```
empire-studio/
├── SKILL.md                 (questo kernel)
├── README.md                (mappa + come si usa + stato onesto)
├── references/
│   ├── ARCHITECTURE.md      (MKD: org, pipeline, ruflo, visione)
│   └── CONVENTIONS.md       (no-stub, no-finto, nomi Windows-safe, 7-file, P12)
├── agents/                  (9 reparti, L3 agenti a 7 file) + CATALOG.md
├── skills/                  (tier0-orchestration / tier1-department / tier2-functional)
├── strategies/              (multi-strategia per reparto/tipo/wiki)
├── scripts/                 (motore reale: yt_ingest, frame_extractor, wiki_writer,
│                             memory_manager, validator, setup_check, ...)
├── memory/                  (ecosistema 16 categorie + MEMORY-INDEX.md)
├── runs/                    (workspace per run: <run-id>/frames, analysis, ...)
└── assets/templates/        (template 7-file agente, skill, video-analysis, ...)
```

## Prerequisiti
`python scripts/setup_check.py` (python + yt-dlp + ffmpeg; playwright opzionale).
La visione dei frame e' eseguita da Claude Code (nessuna vision API).

## Stato
In costruzione **depth-first, reparto per reparto, tutto reale**. Niente e'
"fatto" finche' `python scripts/validator.py` non da 0 violazioni. Vedi
`agents/CATALOG.md` e `README.md` per lo stato puntuale.
