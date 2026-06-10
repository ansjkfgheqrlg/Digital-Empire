# update-proposer - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Proposte generiche | 'migliora il workflow' vago | ancora al workflow specifico | nessun target preciso | specifica file/agente da toccare |
| Proposte non tracciabili | manca il perche' | trace al video/frame | trace assente | aggiungi la fonte ispiratrice |
| Falsa rilevanza | proposta non pertinente | soglia di match | match debole | scarta sotto soglia |
| Workflow-state assente | non sa cosa esiste | popola workflow-state | stato vuoto | chiedi contesto al Conductor |
| Modifica accidentale | tocca file esistenti | solo proposta, mai write | diff su file esterni | annulla, resta in sola lettura |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
