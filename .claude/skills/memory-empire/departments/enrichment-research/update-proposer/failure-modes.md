# Failure Modes — update-proposer

## FM-01: Contenuto duplicato
**Causa:** La skill ha già la sezione proposta
**Fix:** Read del file target prima di generare — se la sezione esiste con contenuto simile → skip

## FM-02: Section heading non trovato
**Causa:** La skill ha una struttura diversa
**Fix:** Usa insert_mode: "append_end" come fallback sicuro

## FM-03: Proposal troppo generica
**Causa:** content_to_add non è specifico
**Fix:** Ogni proposal deve citare i dati concreti (prompt, tecnica, numero) non principi astratti
