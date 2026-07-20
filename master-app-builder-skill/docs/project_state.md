# Stato progetto — Master App Builder Skill

- Ultimo aggiornamento: 2026-07-19
- Fase corrente: 7 — Documentazione
- Checkpoint verificato: 7
- Branch/versione: workspace / v2.1 draft

## Completato
- Definito lo scopo della skill: framework operativo per costruire applicazioni.
- Creato `SKILL.md`, pronto da copiare in una configurazione agente.
- Creati SRS, README e script di bootstrap Python.
- Integrati agenti operativi, agente di reference (REF) e supervisore (SUP) nella skill.
- Aggiunti agenti specialistici ACC, INT, PERF, DATA, REV e FIN con matrice di attivazione.
- Creato sistema di memoria persistente a livelli con indice, ADR, rischi, fonti e handover.
- Aggiunte librerie `docs/rules/`, `docs/workflows/`, `docs/references/`, `docs/agents/` e gap analysis.
- Reso WF-0 (workflow core) un gate obbligatorio prima di SRS, design, architettura e codice.
- Aggiunti PM, WFL, CNT, MOB, LEG e SRE al registro degli agenti.
- Esteso il registro a 55 agenti operativi, inclusi PO, UXR, MKT, IXD, VIS, L10N, DSN, SEO, DESK, CLI, AI, MLOPS, ANA, PAY, IOT, TST, PRIV, FRAUD, GRC, DBRE, CLOUD, SUPP, TRAIN, MEM e CHG.
- Estesa la reference library con 60+ fonti primarie su standard web, sicurezza, privacy, delivery, cloud, AI, UX, pagamenti e mobile.
- Verificato il bootstrap con Python 3.13.13.

## Decisioni approvate
- Lingua italiana e approccio Python-first.
- Skill indipendente dalla piattaforma dell'agente.
- Checkpoint obbligatori con risultati di verifica non inventati.

## Assunzioni e rischi
- Il formato di importazione della skill dipende dalla piattaforma di destinazione; `SKILL.md` è Markdown portabile.
- Non sono presenti dipendenze runtime per questo progetto documentale.

## Verifiche eseguite
| Comando/controllo | Esito | Note |
|---|---|---|
| `python --version` | Pass | Python 3.13.13 |
| `python scripts/session_bootstrap.py` | Pass | Dipendenze non richieste |
| `python -m py_compile scripts/session_bootstrap.py` | Pass | Sintassi Python verificata |

## Prossimo passo
- Importare o incollare `SKILL.md` nella piattaforma agente scelta e, se necessario, adattarne il manifest.
