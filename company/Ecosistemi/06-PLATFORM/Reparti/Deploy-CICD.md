> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# L2 DEPLOY & CI/CD — Pipeline di Deploy

> Reparto L2 · Ecosistema: 06-PLATFORM
> Riferimento: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md` · `company/Ecosistemi/06-PLATFORM/BACKBONE.md`

---

## Missione

Eseguire il deploy di ogni sito, SaaS e tool di Digital Empire in modo ripetibile, monitorato e reversibile. DEPLOY & CI/CD è l'ultimo anello della catena — riceve solo deliverable che hanno superato G-SEC e G-QA. Custodisce le procedure di rollback e tiene il log di ogni deploy nella memoria `platform/deploy`.

**Infrastruttura primaria:** Vercel (deploy + preview + logs + rollback). GitHub Actions come layer CI quando necessario.

---

## Workflow L3

| Workflow | Descrizione | Trigger |
|---|---|---|
| **WF-DEPLOY** | vercel:deploy → vercel:logs → smoke test → emit evento OPERATIONS | ogni build approvata |

### Fasi di WF-DEPLOY

1. `vercel:setup` (prima volta per repo): configurazione progetto, env vars, dominio
2. `vercel:deploy` → URL preview generato
3. smoke test automatico (playwright su URL preview)
4. Promozione a production (se smoke verde)
5. `vercel:logs` monitoring (15 min post-deploy)
6. Emit evento `{commessa, costo, durata, esito}` → OPERATIONS
7. Entry `platform/deploy` in AgentDB → `memory_store`

---

## Funzioni L4

| ID Funzione | Descrizione | Tool |
|---|---|---|
| T-vercel-setup | Prima configurazione progetto su Vercel (env, dominio, team) | skill `vercel:setup` |
| T-vercel-deploy | Lancio deploy (preview + production) | skill `vercel:deploy` |
| T-smoke-test | Test post-deploy su URL live (critical paths) | skill `playwright-dev` |
| T-vercel-logs | Monitoring log reale post-deploy | skill `vercel:logs` |
| T-rollback | Rollback a versione precedente se smoke rosso | skill `vercel:deploy` rollback flag |
| T-cost-emit | Emissione evento costo per OPERATIONS | schema evento standard |

---

## Agenti L5 del reparto

| ID Agente | Ruolo | Tier |
|---|---|---|
| `plt-deploy-op` | Deploy Vercel + logs + rollback — esegue WF-DEPLOY | Haiku |
| `plt-qa-runner` | Smoke test post-deploy (playwright) | Haiku |
| `plt-custodian` | Verifica handover deploy al cliente (se commessa Agency) | Haiku |

---

## Gate G-DEPLOY

```
Prerequisiti:
  ✓ G-SEC verde (aidefence + security-review)
  ✓ G-QA verde (site-qa + playwright)
  ✓ G-BRAND verde (stile conforme)

WF-DEPLOY:
  → vercel:deploy (preview)
  → smoke test preview URL
  → SE PASS → production push
  → vercel:logs 15 min
  → SE tutto verde → emit costo → log memory
  → SE smoke FAIL → rollback + escalation plt-director
```

---

## Procedure di rollback

1. `plt-deploy-op` esegue rollback immediato a versione precedente su Vercel
2. Incidente loggato in `platform/incidents` via `memory_store`
3. `plt-qa-runner` ri-esegue smoke su versione rollback (verifica stabilità)
4. Escalation a `plt-director` con diff tra versioni

---

## Asset esistenti

| Path / Skill | Stato |
|---|---|
| skill `vercel:deploy` | USA |
| skill `vercel:logs` | USA |
| skill `vercel:setup` | USA |
| skill `playwright-dev` | USA — smoke test |
| `agency-empire-landing/` | EVOLVI (aggiungere CI verify pre-deploy, fase P3) |

---

## Emissione evento costo (schema)

```json
{
  "ecosistema": "06-PLATFORM",
  "workflow": "WF-DEPLOY",
  "commessa": "<id_commessa>",
  "agente": "plt-deploy-op",
  "costo_api": 0.00,
  "durata_min": 12,
  "esito": "success | rollback",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}
```

Questo evento va a OPERATIONS (cost attribution ledger).

---

## KPI

| KPI | Target |
|---|---|
| Deploy senza rollback | ≥ 95% |
| Tempo deploy (vercel:deploy → production live) | ≤ 8 min |
| Smoke test copertura (critical paths testati) | 100% per sito |
| Emit evento costo per ogni deploy | 100% |

## Connessioni

- [[06-PLATFORM/ECOSISTEMA.md]] — panoramica PLATFORM
- [[06-PLATFORM/BACKBONE.md]] — namespace AgentDB `platform/deploy`
- [[06-PLATFORM/Reparti/Security-Quality.md]] — gate G-SEC e G-QA prerequisiti
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo, fasi P3-P4
