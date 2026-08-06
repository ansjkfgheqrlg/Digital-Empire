---
Type: CONCEPT
Status: Active
Tags: #reparto-produzione #caroselli #arena #playwright #contenuti #preventa #agency
Created: 2026-08-03
Last updated: 2026-08-03
---

# Reparto Produzione — Digital Empire

## Overview
Ordine di Max (2026-08-03, [[CP-20260803-004]]/[[CP-20260803-006]]): l'azienda deve
avere un concetto organizzativo di **"progetti"** e **"categorie"** per la produzione
di contenuti — non un motore unico monolitico, ma un umbrella sotto cui ogni
brand/prodotto ha il proprio progetto, riusando lo stesso motore tecnico dove
possibile (ADR-003: wrap, mai riscrittura).

## I 3 motori caroselli trovati su disco (non sono la stessa cosa)
Prima di costruire qualsiasi cosa, sono stati mappati 3 sistemi caroselli reali,
esistenti, indipendenti — confusi facilmente perché tutti "generano caroselli
Instagram":

| Motore | Percorso | Come genera i visual | Brand attivi |
|---|---|---|---|
| **ArenaAI (caroselli - agency)** | `SKILL & Agenti/Workflow agency creative/caroselli - agency/` | Automazione **reale via Playwright** su Arena.ai (browser profile persistente, battle→direct mode, modello "chatgpt medium", captcha solver, catena slide1→slide2→slide3 via allegato immagine precedente) | Digital Empire Agency (@digitalempireagency.e) |
| **carousel-factory** | `Workfolw crea caroselli à/carousel-factory/` | Puppeteer + Handlebars (HTML→PNG), foto generate **a mano su Gemini** (nessuna chiave API image-gen in `.env`) | mentalità-brutale (PLAN-v1 APEX-7 di un'altra sessione in corso, non toccato) |
| **carousel-empire** (skill Claude) | `~/.claude/skills/carousel-empire/` | Python standalone, genera 7 PNG 1080×1350 senza foto/Arena | Digital Empire Agency (usato per @crea.illtuo_impero) |

**Confermato da Max** (2026-08-05): quando dice "quello stile perfetto collegato con
Arena attraverso Playwright" intende ArenaAI, ma **non il motore Playwright grezzo**
(chat Direct+Image, prompt scritti a mano) — intende un **Agent workspace già
costruito DENTRO Arena stessa** (Arena "Agent Mode"), con un file system persistente
(`apex7/agents/memory/orchestrator/playwright_bridge/...`), raggiungibile solo tramite
una chat archiviata specifica + comando `/inizio-generazione`. Vedi [[CP-20260805-010]]
e [[CP-20260805-013]] (primo output reale, flusso esatto verificato). Il motore
Playwright grezzo resta comunque infrastruttura condivisa reale (usata per Agency),
solo non è il percorso per nuovi progetti come Preventa.

## Come è organizzato oggi (dopo Progetto Preventa)
```
SKILL & Agenti/Workflow agency creative/
├── caroselli - agency/          ← Progetto "Agency" (esistente, non toccato)
│   ├── ArenaAI/                 ← motore condiviso (browser_manager, arena_generator)
│   ├── Agents/                  ← copywriter/orchestrator specifici Agency
│   ├── Core/browser_manager.py
│   └── config.py                ← credenziali (⚠️ vedi nota sicurezza sotto)
└── caroselli - preventa/        ← Progetto "Preventa" (NUOVO, 2026-08-03)
    ├── Agents/copywriter_agent_preventa.py   ← copy specifico Preventa
    ├── orchestrator_preventa.py              ← RIUSA ArenaAI via import, non copiato
    ├── config_preventa.py                    ← isola output/allegati da Agency
    └── output_preventa/
```

**Pattern per un futuro "Progetto X"**: nuova cartella sibling `caroselli - X/`,
proprio `Agents/copywriter_agent_X.py` (stesso schema JSON: 3 slide + descrizione),
proprio `config_X.py` (proprio `LOCAL_DOWNLOAD_DIR`/`ALLEGATI_DIR`), un
`orchestrator_X.py` che importa `ArenaAI/arena_generator.py` dalla cartella Agency
e sovrascrive i due attributi di `config` (il modulo condiviso) prima di chiamarlo.
Mai duplicare `ArenaAI/`/`Core/` — è il motore, si riusa.

Dettaglio tecnico del come/perché in [[Progetto_Preventa_Carousel]].

## Arsenale Caroselli — libreria dei caroselli finiti (nuovo, 2026-08-06)
Richiesta esplicita di Max: "un'arsenale dei caroselli, una cartella per ogni
prodotto". Separato dalle cartelle motore (dove vive solo codice): gli output
finiti (PNG + copy.json + zip) vanno in
`SKILL & Agenti/Workflow agency creative/Arsenale Caroselli/<Prodotto>/<data_topic>/`.
Non un motore nuovo — solo dove atterrano i risultati, indipendentemente da quale
motore/progetto li ha generati. Vedi il `README.md` dentro quella cartella per la
struttura esatta.

## ⚠️ Nota sicurezza (non ancora risolta, decisione di Max)
`caroselli - agency/config.py` contiene email+password reali di Arena.ai e le
chiavi API Groq/OpenRouter **in chiaro, committate in git** (tracciate dal primo
commit del monorepo, già pushate). Segnalato a Max 2026-08-03, in attesa di
decisione (spostare in `.env` + rotazione credenziali, o altro). Vedi
[[CP-20260803-006]] per i dettagli.

## Connessioni
- [[Progetto_Preventa_Carousel]] — il primo progetto nuovo sotto questo reparto
- [[Preventa_Logica_Completa_Metodo]] — il prodotto Preventa che questi caroselli promuovono
- [[Framework_Barnum_Rainbow_5Pilastri]] — stessa disciplina di "non inventare, riusare regole scritte" applicata ai messaggi di outreach
