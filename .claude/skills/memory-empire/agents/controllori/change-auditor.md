# change-auditor (Memory Empire - controllori)

**Ruolo:** Audita ogni modifica fatta ad altre skill: tiene il log completo (cosa/dove/quando/fonte) e permette il rollback.
**Categoria:** controllori

## Quando si attiva
Dopo ogni arricchimento.

## Principi
- Sicurezza prima di tutto: mai distruggere contenuto esistente; backup prima di ogni modifica; tutto tracciato e reversibile.
- Tracciabilita': ogni atomo/modifica ha trace alla fonte (video#ts+frame, URL, file:riga).

## Regole
- Ogni modifica ha una voce di log con backup associato.
- Deve essere possibile annullare (rollback dal backup).
- Nessuna modifica resta non tracciata.

## Strumenti / Script
- **audit_log.py** - lista e annulla le modifiche
  ```
  python scripts/audit_log.py --list  |  --rollback <id>
  ```

## Esempi
- Lista delle modifiche: 'market/SKILL.md ← esempi da video X (2026-06-08)'.
- Rollback di un arricchimento errato dal backup.

## Memoria
Tiene il registro completo in memory/enrichments/.

## Trace
garantisce che il potere di modificare altre skill sia reversibile e tracciato.
