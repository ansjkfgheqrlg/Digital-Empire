# Empire Studio

Workflow gerarchico per trasformare link grezzi (YouTube, TikTok, siti web,
progetti/repo) in conoscenza operativa dentro la wiki di Digital Empire - con
**visione reale dei video**, organizzazione a reparti, memory-first, CLI-only.

Questa e' la **ricostruzione pulita** (v2.0), nata dall'audit del primo tentativo
che era in gran parte impalcatura: stub spacciati per "fatti", video-watcher
finto, pipeline senza codice, due copie divergenti, nomi file non estraibili su
Windows. Qui ogni pezzo e' **reale e validato**.

## Come si usa (ATTIVAZIONE NATURALE - nessun comando)
Non si digita niente di tecnico. **Basta passare un link o chiedere a parole.**
Esempi naturali:
- "Guarda questo video: https://youtu.be/XXXX" → ingestione YouTube
- "Prendi tutta la formazione da questo canale" + link
- "Studia questa repo: ./qualche-repo" → deep study (non modifica nulla)
- "Mettilo nella wiki" / "non tralasciare nessun dettaglio"

Appena ricevo un link o una richiesta del genere (anche richiamato dal router di
**Memory Empire**), Claude (Conductor) fa **tutto da solo**: guarda il video
(frame reali + visione) → estrae transcript e TUTTA la conoscenza (mai riassunti)
→ forgia via content-forge **gestito dagli agenti** → scrive nella **wiki di
Digital Empire** e in **Memory Empire** → propone update ai workflow → registra in memory.

## Prerequisiti
```
python scripts/setup_check.py
```
Servono: `python`, `yt-dlp`, `ffmpeg` (+ `playwright` opzionale per il web).
La **visione** dei frame e' eseguita da Claude Code stesso: nessuna API a pagamento.

## Struttura
- `SKILL.md` - kernel/entrypoint
- `references/ARCHITECTURE.md` - org chart, pipeline, ruflo, protocollo visione
- `references/CONVENTIONS.md` - regole no-stub / no-finto / Windows-safe / 7-file / P12
- `agents/` + `agents/CATALOG.md` - 9 reparti, agenti a 7 file, stato reale
- `skills/` - skill a tier (tier0 orchestrazione, tier1 reparto, tier2 funzionali)
- `scripts/` - il motore reale (yt_ingest, frame_extractor, wiki_writer, memory_manager, validator, ...)
- `memory/` - ecosistema di memoria a 16 categorie + MEMORY-INDEX.md
- `strategies/` - multi-strategia
- `runs/` - workspace delle run (frames, analysis, ...)

## Stato (onesto, verificato dal filesystem)
Vedi `agents/STATUS.md` (auto-generato dal disco, non puo' mentire). Gate:
```
python scripts/validator.py    # 0 violazioni
python scripts/catalog_status.py
```
- **50/50 agenti** completi (7 file reali ciascuno) nei 9 reparti.
- **20/20 skill**: 4 tier-0 (orchestrazione) + 6 tier-1 (reparto) + 10 tier-2
  (funzionali, con script .py reali che compilano).
- **14 script motore** reali e testati (yt_ingest, frame_extractor, wiki_writer,
  memory_manager, validator, scan_repo, update_proposer, prepare_forge_input,
  make_report, clean_transcript, web_research, generate_strategy_manifest,
  ruflo_bridge, package).
- **Motore provato end-to-end** su video YouTube reale (`runs/test-youtube-001/`):
  ingest -> 6 frame veri (ffmpeg) -> visione reale di Claude -> analysis reale.
- **Strategie** multi-strategia (registry + strategie per reparto/tipo/wiki).
- **ruflo/swarm**: topologia hierarchical (queen=conductor) con fallback Task/Agent.
- **Packaging**: `packaged/empire-studio-clean.zip` si estrae con l'estrattore
  nativo di Windows senza errore 0x80070057 (verificato).

Cosa resta come uso (non costruzione): eseguire `/empire <link>` su contenuti
reali per popolare la wiki, e affinare le strategie sui dati delle run.

## Cosa NON e' (per evitare l'errore precedente)
- Non e' un esercito di micro-servizi Python autonomi (impossibili). Gli "agenti"
  sono ruoli che **Claude** assume eseguendo il workflow; gli script sono le mani.
- Non e' una singola skill: e' un workflow che CONTIENE skill e agenti.
- Non ci sono descrizioni di video inventate: la visione e' reale (Claude legge i PNG).
