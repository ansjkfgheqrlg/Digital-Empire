# bug-error-tracker - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Bug non registrato | problema perso | registrazione obbligatoria | errore non tracciato | registra retroattivamente |
| Report povero | manca contesto | template bug | report scarno | arricchisci |
| Non collegato agli stati | impatto sconosciuto | link agli stati | nessun collegamento | collega |
| Stato non aggiornato | bug 'aperto' gia' risolto | aggiorna lo stato | incoerenza | chiudi/riapri |
| Categoria errata | bug in errors o viceversa | criterio bug vs error | fuori posto | ricolloca |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
