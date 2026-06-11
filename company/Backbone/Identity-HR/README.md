# 👤 IDENTITY-HR — Registro agenti

> **Backbone component.** Fonte di verità per tutti gli agenti della holding.

## Funzione

Ogni agente che opera in EMPIRE OS è censito qui: ruolo, ecosistema, tier modello,
costo stimato, performance, stato (attivo/in pausa/ritirato).
La **07-FORGE** è l'unica che può aggiornare questo registro (assumere/ritirare).

## File principale (da creare in F2)

`Identity-HR/registro-agenti.yaml`

Schema per ogni agente:
```yaml
- id: empire-conductor
  nome: CEO / Empire-Conductor
  livello: L0
  ecosistema: board
  tier_modello: opus
  stato: attivo
  costo_stimato_per_task: 0.05
  kpi_primario: "decisioni cross-ecosistema risolte / sessione"
  creato: 2026-06-11
  creato_da: fondatori
```

## Agenti censiti (Board — già documentati)

| ID | Nome | Livello | Tier |
|---|---|---|---|
| empire-conductor | CEO | L0 | opus |
| empire-coo | COO | L0 | sonnet |
| empire-cto | CTO | L0 | sonnet |
| empire-cmo | CMO | L0 | sonnet |
| empire-cro | CRO | L0 | sonnet |
| empire-cfo | CFO | L0 | haiku |
| empire-chief-forge | Chief Forge | L0 | opus |

L5 agents (A1-A8, S1-S3 copy-workflow, ecc.): da censire in F3 durante migrazione asset.
Totale stimato: ~180+ agenti su tutti i livelli.

## Stato: parziale — Board censito; L1-L5 da censire (F2-F3, task 2.6)
