# Failure Modes — skill-enricher

## FM-01: enrich_skill.py non esiste
**Fix:** Usa Edit direttamente, ma sempre dopo backup manuale (cp)

## FM-02: File target non trovato
**Fix:** Verifica path con Glob prima di procedere. Se non esiste → segnala a dept-lead

## FM-03: Contenuto corrotto dopo append
**Fix:** Read il file dopo modifica. Se corrotto → rollback immediato dal backup

## FM-04: Backup già esiste (timestamp clash)
**Fix:** Aggiungi ms al timestamp. Non sovrascrivere mai un backup.
