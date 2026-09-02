# memory-architect - Failure Modes (P09)

| Failure | Sintomo | Prevenzione | Detection | Recovery |
|---|---|---|---|---|
| Categoria mancante | eventi senza posto | copertura completa | eventi orfani | aggiungi categoria |
| Schema permissivo | entry incoerenti | schemi stretti | voci difformi | stringi lo schema |
| Naming non-safe | nomi problematici | regola di naming | validator | correggi la convenzione |
| Two-layer confuso | short/long mescolati | separazione netta | stato in posto errato | ripartisci correttamente |
| Architettura non versionata | modifiche non tracciate | versioning | nessun ARCH | registra la versione |

I failure vengono loggati dal bug-error-tracker in `memory/bugs/` o `memory/errors/`; il silent-observer li usa per il miglioramento.
