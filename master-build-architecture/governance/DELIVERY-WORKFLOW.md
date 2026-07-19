# Regole — Workflow di delivery

1. Il ciclo obbligatorio è: Workflow → Requisiti → Architettura → Design → Implementazione → Review → Test → Supervisione → Release.
2. Un incremento è verticale: include codice, test, aggiornamento memoria e documentazione impattata.
3. Nessun merge/release critico senza REV e QA; SEC interviene quando cambia superficie di attacco o dato sensibile.
4. Ogni bug ha severità, riproducibilità, workflow impattato, owner e test di non regressione.
5. Ogni cambio incompatibile è registrato in changelog e ADR con piano di migrazione/rollback.
6. Il deploy deve avere health check, osservabilità minima e rollback documentato.
