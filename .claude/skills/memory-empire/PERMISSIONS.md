# Memory Empire - PERMESSI & SICUREZZA

Memory Empire e' una skill **potente con permessi ampi**: puo' **modificare altre
skill/workflow** per arricchirli con la conoscenza nuova (es. aggiungere principi,
regole ed esempi di marketing da un video alla skill marketing). Questi permessi
sono reali MA controllati, perche' il potere senza sicurezza rompe le cose.

## Cosa PUO' fare
- **Arricchire** file `.md` di altre skill/workflow (SKILL.md, references/,
  templates/, esempi) aggiungendo conoscenza nuova e pertinente.
- **Creare** nuovi file di conoscenza dentro una skill quando serve.
- **Attivare/richiamare** altri workflow (es. Empire Studio).
- **Scrivere** nella wiki di Digital Empire e nel proprio `knowledge/`.

## Come lo fa (in SICUREZZA — non negoziabile)
1. **APPEND, mai overwrite/delete.** Aggiunge una sezione marcata
   `➕ aggiunto da Memory Empire (data, fonte)`. Non sostituisce e non cancella
   contenuto esistente.
2. **BACKUP prima di ogni modifica** (`memory/enrichments/backups/`).
3. **LOG di ogni modifica** (`memory/enrichments/`), con **rollback** disponibile
   (`audit_log.py --rollback <id>`).
4. **Gate del permission-guard** prima della modifica + **integrity-verifier**
   dopo (se rompe la skill → rollback automatico).
5. **Solo dove e' rilevante** (deciso da relevance-analyzer + gap-analyzer): niente
   modifiche a caso, niente duplicati.

## Limiti
- Non modifica file non-skill critici (config di sistema, `.git`, segreti).
- Per modifiche a skill reali dell'utente: l'enricher **propone e conferma**
  prima di scrivere (e comunque con backup+log reversibili).
- Nessuna modifica resta non tracciata.

## Catena di controllo
`relevance-analyzer → gap-analyzer → permission-guard (gate) → skill-enricher
(backup+append+log) → integrity-verifier → change-auditor (log/rollback)`

Cosi' i permessi sono **massimi ma sicuri**: tutto reversibile, tutto tracciato.
