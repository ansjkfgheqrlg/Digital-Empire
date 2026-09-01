# Failure Modes — routing-dispatch / department-lead

## FM-01: Empire Studio non attivato su link YouTube
**Causa:** Claude usa WebFetch/WebSearch per default invece di Empire Studio.
**Sintomo:** Video analizzato da fonti secondarie, nessun run creato in empire-studio/runs/.
**Fix:** Il hook UserPromptSubmit ora inietta la regola obbligatoria. Se ancora non parte: activation-monitor rileva il fallimento e il dept-lead esegue il fallback manuale.

## FM-02: intent-classifier timeout
**Causa:** Classificazione lenta o blocco.
**Sintomo:** Nessun file `intent-<ts>.json` dopo 10s.
**Fix:** Department-lead classifica manualmente: se c'è un URL → INGEST_LINK; se c'è "ingerisci/guarda/studia" → INGEST_KEYWORD.

## FM-03: Log non scritto
**Causa:** Errore durante la scrittura in memory/routing/.
**Fix:** Scrivi su un file temporaneo e riprova. Se ancora fallisce, logga inline nel contesto.

## FM-04: Loop di re-attivazione
**Causa:** activation-monitor continua a segnalare "failed" anche dopo re-attivazione.
**Fix:** Massimo 2 tentativi di re-attivazione, poi segnala al Conductor per intervento manuale.
