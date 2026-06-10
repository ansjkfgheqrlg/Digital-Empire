# transcript-processor - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Auto-sub rumorosi | ripetizioni, parole spezzate | dedup + merge righe | righe quasi identiche | fondi i segmenti sovrapposti |
| Lingua inattesa | testo non in en/it | rileva lingua | mismatch lingua | segnala; usa quello disponibile |
| Timestamp persi | testo senza ancore | conserva i cue times | nessun timestamp | stima per posizione |
| Transcript assente | nessun vtt | fallback a sola visione | file mancante | dichiara limite, procedi coi frame |
| Caratteri rotti | mojibake/accenti | decode utf-8 robusto | caratteri non validi | normalizza encoding |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
