# Esempio di lancio (kit di collaudo)

Cos'è: un lancio **finto** con `lancio_id = "esempio"`, sei artefatti validi contro gli schemi di
`PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/schemi/`. Serve a vedere i gate girare, non a decidere niente:
ogni numero è dichiarato di collaudo in `non_misurato`, e nessuno è spacciato per misurato.

- `lancio crea <id> --con-esempio` copia questa cartella dentro `lanci/<id>/` (cambiando `lancio_id`).
- `GATE-PUB-1`, `GATE-STR-1`, `GATE-PRD-1`, `GATE-INT-1`, `GATE-PRV-1` **passano**.
- `GATE-OFF-1` **boccia**: esiste solo `offerta.PROPOSTA.json`, nessuna firma. È il caso normale, non un errore.
- Serve la **rete** per `GATE-INT-1` (riapre davvero example.com, iana.org, python.org) e per `GATE-PRD-1`
  (`link_testati` qui è vuoto, ma su un lancio vero il gate riapre ogni link elencato).
- Il prodotto certificato è `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/00-LEGGIMI.md`, percorso relativo alla radice del repo.
