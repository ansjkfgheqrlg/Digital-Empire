# Agente — conductor (regia)

- **Tipo:** regia / supervisore · **Owner:** Max (Half A) · **Stato:** attivo
- **Implementazione:** `run.py` (+ `implementation/common.py` per stato/trace/config).

## Ruolo
È il cervello del run. Prende un URL mobile.de (o input `--manual`) e una concessionaria,
sequenzia gli stage S1→S5, applica i 4 gate, gestisce retry/fallback e budget, e produce
lo stato osservabile. NON fa il lavoro degli stage: li orchestra.

## Input
- `url` (o `--manual <html> [--foto <dir>]`), `--dealer <id>` (default `prof-autocad`), `--run-id?`.
- `dealer` risolto da `dealers.load_dealer()`.

## Output
- Cartella `runs/<id>/` con `raw.json`, `foto/`, `listing.json`, `listing_it.json`,
  (con Half B) `preventivo_*.pdf`, + `state.json`, `trace.jsonl`, `logs/<id>.log`.
- Codice di uscita: 0 ok · 2 S1 fail · 3 Gate A · 4 S4 fail.

## Confini
- Invoca Half B (S3/S5, gate B/C/D) SOLO se i moduli esistono; altrimenti salta con nota handoff.
- Non modifica il data contract. Non scrive fuori da `runs/`, `logs/`.
- Una consegna solo se TUTTI i gate attivi sono verdi.

## Collaborazione
Parla con gli agenti solo via file (`raw.json`→`listing.json`→`listing_it.json`→pdf). Vedi
`../../orchestration/supervisor.md` e `routing.md`.
