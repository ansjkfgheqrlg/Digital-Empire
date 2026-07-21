# Failure Modes — memory-architect
| Fallimento | Sintomo | Prevenzione | Rilevamento | Recupero |
|---|---|---|---|---|
| CP mancanti | task chiusi senza atomo | regola zero nei reparti | audit EOD | CP [RECOVERY] + nota |
| INDEX corrotto | righe duplicate | edit solo via CLI | status | rebuild INDEX dai file |
| Veto ignorato | decisione PROPOSTA scaduta non attivata | WF-MASTER regola 4 | dashboard | attiva default + notifica |
| Metriche vanity | report senza € | P6 regole | review RETRO | riscrivi KPI |
