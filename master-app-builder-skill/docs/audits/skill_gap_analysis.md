# Gap Analysis — Master App Builder Skill

## Analisi eseguita
La skill aveva già governance, memoria, QA, sicurezza e alcuni agenti specialistici. Mancavano però una base normativa/principi separata e riusabile, un workflow come artefatto obbligatorio iniziale, una libreria di reference operative e ruoli dedicati a prodotto, processi, compliance, affidabilità e localizzazione.

## Lacune chiuse

| Lacuna | Rischio | Intervento |
|---|---|---|
| Workflow non imposto come primo artefatto | Si costruiscono schermate o API senza flusso di valore | `docs/workflows/` e gate WF-0 obbligatorio prima di SRS/architettura |
| Regole UI, link e flussi disperse | Incoerenza e regressioni UX | Cartella `docs/rules/` con principi canonici |
| Fonti non curate come libreria | Decisioni non verificabili | `docs/references/` con catalogo ufficiale e protocollo REF |
| Ruoli operativi incompleti | Lacune su processo, compliance, release e contenuti | Registro esteso e matrice di attivazione |
| Collegamenti interni/esterni non governati | Broken link, navigazione incoerente, rischio sicurezza | Regole specifiche link e ownership |

## Decisione
Il workflow utente/di business è ora il primo artefatto obbligatorio: **nessuna app passa a SRS, UI, API o modello dati senza WF-0 approvato dal supervisore**.
