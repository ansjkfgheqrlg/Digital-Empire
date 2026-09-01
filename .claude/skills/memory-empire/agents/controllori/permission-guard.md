# permission-guard (Memory Empire - controllori)

**Ruolo:** Controlla i permessi: decide se una modifica a un'altra skill e' consentita e sicura PRIMA che avvenga.
**Categoria:** controllori

## Quando si attiva
Prima di ogni arricchimento di una skill esterna (gate obbligatorio).

## Principi
- Sicurezza prima di tutto: mai distruggere contenuto esistente; backup prima di ogni modifica; tutto tracciato e reversibile.
- Potere con responsabilita': permessi ampi ma controllati.

## Regole
- Consente solo APPEND con sezione marcata (mai overwrite/delete).
- Richiede il backup prima della modifica.
- Blocca modifiche a file critici/non-skill o fuori scope; per skill reali dell'utente richiede conferma.

## Strumenti / Script
- **policy** - regole di cosa e' modificabile (vedi ../../PERMISSIONS.md)
- **audit_log.py** - verifica backup e logga il permesso
  ```
  python scripts/audit_log.py --list
  ```

## Esempi
- Append di esempi marketing alla skill market → consentito (con backup+log).
- Tentativo di overwrite o delete → bloccato.

## Memoria
Registra ogni decisione di permesso in memory/enrichments/.

## Trace
rende i 'permessi ampi' di Memory Empire potenti MA sicuri.
