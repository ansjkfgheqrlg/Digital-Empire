# Memory — conductor

## Per-run (in `runs/<id>/`)
- `state.json` — stato di ogni step (`running`/`done`/`warning`/`skipped`/`failed`/`blocked`) + timestamp.
- `trace.jsonl` — log append-only di ogni evento/handoff (audit).
- `logs/<id>.log` — log testuale leggibile.

## Cross-run
- Nessuno stato mutabile condiviso tra run (isolamento by design).
- `browser-profile/` (gitignored) persiste sessione/consenso mobile.de tra run → riduce blocchi.

## Cosa NON ricordare
- Niente segreti in stato/trace. Niente dati cliente fuori da `runs/`.

## Apprendimento
I pattern di fallo ricorrenti (es. selettori mobile.de cambiati) vanno annotati qui e in
`failure_modes.md`, e riportati a Max per indurire scraper/parser.
