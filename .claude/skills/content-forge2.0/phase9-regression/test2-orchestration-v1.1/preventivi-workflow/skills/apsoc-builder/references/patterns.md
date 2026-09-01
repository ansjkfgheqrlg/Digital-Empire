# Patterns — apsoc-builder

> Pattern operativi specifici per apsoc-builder.

## Pattern principali

### Pattern 1 — Estrazione brief

Pre-processing del brief del cliente per ottenere dati strutturati.

### Pattern 2 — Application APSOC

Applicazione del framework APSOC al dominio specifico.

### Pattern 3 — Validation output

Pre-handoff validation: schema check + tone check.

## Anti-pattern

- ❌ Bypassare la fase di brief
- ❌ Skipping della validation
- ❌ Output senza handoff structured

## Schema visuale

```
Input → Brief extraction → APSOC application → Validation → Handoff
```
