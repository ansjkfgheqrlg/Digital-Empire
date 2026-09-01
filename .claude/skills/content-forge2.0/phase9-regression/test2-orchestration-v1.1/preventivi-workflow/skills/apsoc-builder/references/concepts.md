# Concetti — apsoc-builder

> Concetti chiave applicati da apsoc-builder dentro il workflow preventivi.

## Cosa è questa skill

apsoc-builder è un componente specializzato del workflow preventivi-workflow. Non opera isolato — riceve input da altri componenti e produce output strutturato.

## Principi

1. **Rigore senza burocrazia**: applica le regole APSOC senza diventare pedante
2. **Output azionabile**: ogni deliverable può essere usato senza modifiche
3. **Tracciabilità**: ogni claim ancorato al manuale APSOC

## Quando si attiva

Spawnato dall'orchestrator quando arriva la fase corrispondente nel workflow.

## Esempio applicato

Cliente videomaker chiede preventivo: skill spawnata → produce sezione → handoff a next component.

## ➕ Esempio aggiuntivo

Cliente B2B SaaS: skill adatta tone e contenuti al target enterprise.

## Connessioni

- Si appoggia su: skill `apsoc-builder` per template base
- Vedi anche: workflow `full-copy-workflow`
