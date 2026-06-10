# Empire Studio - Convenzioni (non negoziabili)

Documento di riferimento per chiunque (umano o agente) costruisca dentro Empire
Studio. Nato dall'audit del primo tentativo fallito: serve a impedire che si
ripetano gli errori (stub spacciati per "fatto", file finti, nomi non
estraibili su Windows).

## 1. Regola NO-STUB (anti AP01 "Scaffold-as-Deliverable")
Un artefatto "esiste" solo se e' SOSTANZIALE e REALE.
- **Agente** = cartella `agents/<reparto>/<nome>/` con **7 file canonici**, ognuno
  >= 12 righe non vuote e >= 400 caratteri, senza marker proibiti.
- **Skill** = cartella con `SKILL.md` sostanziale; se e' `tier2-functional`,
  ALMENO uno script `.py` reale (>= 25 righe) che **compila**.
- Marker proibiti (bloccati dal validator): `in costruzione`, `TODO`, `stub`,
  `placeholder`, `da completare`, `coming soon`.
- Cancello: `python scripts/validator.py` deve dare **0 violazioni** prima di
  dichiarare "fatto" qualsiasi fase.

## 2. Regola NO-FINTO
- Niente contenuti inventati spacciati per reali. Se Claude non ha guardato un
  frame, non scrive cosa contiene. Se non e' stata fatta una run, non si scrive
  "coverage 98%".
- Tutto cio' che e' inferenza (non osservato) si etichetta con `➕` (come
  content-forge).

## 3. Nomi file Windows-safe (fix errore 0x80070057)
- Vietati nei nomi: `< > : " / \ | ? * + ( ) [ ]`. Solo `a-z 0-9 - _ .`.
- Lunghezza nome < 120 caratteri.
- I checkpoint usano `CP-NNN-slug-YYYY-MM-DDThhmmss.md` (niente `:` nell'orario).
- Generati **solo** via `scripts/memory_manager.py` (che sanifica) - mai a mano.

## 4. I 7 file canonici di ogni agente (formato fisso)
1. `<nome>.md`        - spec: ruolo, reparto, livello, input/output, handoff, trace
2. `system-prompt.md` - il prompt operativo dell'agente (in italiano)
3. `tools.md`         - tool/CLI/script che usa + schemi I/O (JSON)
4. `playbook.md`      - passi operativi + 3-5 esempi reali
5. `evals.md`         - 5+ casi di test discriminanti con criteri di voto
6. `failure-modes.md` - tabella Failure | Sintomo | Prevenzione | Detection | Recovery
7. `memory.md`        - cosa registra in `memory/` e quando (protocollo P10)

Template completo in `assets/templates/agent-7file/`.

## 5. Tracciabilita' (P12)
Ogni atomo di conoscenza nell'output porta una trace:
- Video: `trace: <video-id>#<timestamp> + frame-<NNN>.png`
- Web:   `trace: <url> + screenshot-<NNN>.png`
- Repo:  `trace: <file-path>:<riga> (sezione <X>)`
- Inferenza Empire (non da fonte): prefisso `➕`.

## 6. Livelli & calibro
- **L1 Conductor** orchestra. **L2 Reparti** (lead + skill di reparto).
  **L3 Agenti** specialisti (7 file). **L4 Skill** a tier:
  - Tier-0 orchestrazione (governano altre skill)
  - Tier-1 di reparto
  - Tier-2 funzionali (con script reale)

## 7. CLI-only, no API, no paid
- Strumenti ammessi: `yt-dlp`, `ffmpeg`/`ffprobe`, `playwright`, `python` (stdlib).
- La "visione" dei video la fa **Claude** leggendo i PNG. Niente vision API.
- content-forge si invoca come skill locale (`/forge ... --target=wiki`).

## 8. Memory-first (P10)
- `memory_manager.py` aggiornato dopo OGNI azione significativa.
- Categorie reali: checkpoints, decisions, sessions, plans, architectures, bugs,
  errors, updates, workflow-state, knowledge-state, agent-state,
  verification-logs, strategy-applications, strategy-versions, projects-state,
  repo-analysis.

## 9. Output verso la wiki di Digital Empire
- Le note forgiate atterrano in `second-brain-vault/wiki/` (sottocartella per
  tipo: `sources/` per materiale ingerito, `concepts/`, `tools/`, `synthesis/`).
- Si aggiorna `wiki/log.md` (riga `## data` + `- INGEST: ...`) e si linka in
  `wiki/index.md` quando rilevante.
