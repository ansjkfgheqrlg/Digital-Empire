# esempio-s3s4 — kit di esempio per la seconda meta' del lancio (S3/S4)
Un lancio finto, `lancio_id` "esempio", con tutti gli artefatti da `copy/manifest.json` a `debrief.json` VALIDI contro gli schemi.
Nessun numero e' misurato: ogni file lo dichiara in `non_misurato`. Serve a vedere com'e' fatto un lancio, non a farne uno.
Con `ReteFinta` (nei test): GATE-CPY-1, FNL-1, EDT-1, TSR-1, TSR-2, CNS-1, MEM-1 passano; GATE-REG-1 BLOCCA perche' `via_libera.chi` e' vuoto (nessuna persona ha dato il via) e mancano pubblico/decisione/certificato/ricerca.
Con `ReteVera` GATE-FNL-1 fallirebbe: le url `https://esempio.invalid/...` non esistono, e `prova_cassa.riferimento_transazione` = "ESEMPIO-nessuna-transazione-vera" — lo stato `incassato_e_rimborsato` e' ammesso SOLO qui.
La firma in `offerta.json` e' finta (`chi` = "ESEMPIO-nessuna-persona"): GATE-OFF-1 non la accetterebbe, e non deve.
Rigenerare: `PYTHONIOENCODING=utf-8 python tests/fixture/s3s4/_genera.py` da `02-AUTOMAZIONI-E-SCRIPTS` (riscrive gli stessi file).
Provare un gate: `python -c "from scripts.gates import esegui_gate, ReteFinta; print(esegui_gate('GATE-REG-1', r'<questa cartella>', ReteFinta()))"`.
Non copiare questi file in `lanci/<id>/`: un lancio vero nasce con `lancio crea` e i suoi artefatti li producono i reparti.
Schemi: `PIANO-MAESTRO/29-ECOSISTEMA-LANCI/dati/schemi/`. Contratto dei gate: `02-AUTOMAZIONI-E-SCRIPTS/scripts/gates/_comune.py`.
