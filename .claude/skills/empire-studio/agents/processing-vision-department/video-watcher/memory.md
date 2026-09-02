# video-watcher - Memory (P10)

L'agente aggiorna l'ecosistema di memoria dopo OGNI video guardato. Niente run
senza traccia.

## Cosa registra e dove
- **checkpoints/**: dopo aver completato la visione di un video.
  ```
  python scripts/memory_manager.py --checkpoint "video <id> guardato: <N> frame visti, <M> atomi (<X> marcati +)" --phase 3 --trace "video <id> run <run-id>"
  ```
- **knowledge-state/**: gli atomi visivi estratti (cosa ora "sa" l'ecosistema da
  questo video), con trace.
  ```
  python scripts/memory_manager.py --record knowledge-state --title "atomi visivi <id>" --body "<lista atomi + trace>"
  ```
- **agent-state/**: performance della propria run (frame visti/totali, frame
  illeggibili, % atomi tracciati) per il miglioramento.
- **errors/** o **bugs/**: se un frame era illeggibile o un Read e' fallito,
  delega la registrazione al bug-error-tracker (o registra direttamente con
  `--record errors`).

## Quando
- Prima di iniziare: legge eventuali checkpoint/knowledge-state della stessa run
  (per non riguardare frame gia' analizzati).
- Dopo ogni video: checkpoint + knowledge-state.
- A fine handoff: agent-state.

## Two-layer (P10)
- Short-term: lo stato della run corrente (quali frame gia' visti) vive in
  `runs/<run-id>/video-analysis.md` + `atoms.json`.
- Long-term: knowledge-state + checkpoints in `memory/`, indicizzati in
  MEMORY-INDEX.md, riusabili in run future (es. stesso canale).

## Trace (P12)
Ogni entry di memoria porta il riferimento al video e ai frame, cosi' che la
catena fonte->frame->atomo->nota wiki sia ricostruibile.
