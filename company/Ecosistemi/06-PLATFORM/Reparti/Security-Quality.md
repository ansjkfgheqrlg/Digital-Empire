> Fonte: PIANO-MAESTRO/06-ECOSISTEMI-CORE.md sez. PLATFORM

# L2 SECURITY & QUALITY — Gate Sicurezza e Qualità

> Reparto L2 · Ecosistema: 06-PLATFORM
> Riferimento: `company/Ecosistemi/06-PLATFORM/ECOSISTEMA.md` · `company/Ecosistemi/06-PLATFORM/BACKBONE.md`

---

## Missione

Garantire che ZERO codice esca da PLATFORM senza aver superato la catena di gate: sicurezza (aidefence + security-review + PII check) e qualità (site-qa, verify, playwright). SECURITY & QUALITY non scrive feature: le blocca finché non sono sicure e conformi.

**Regola assoluta:** nessun deploy salta un gate. G-SEC → G-QA → G-BRAND → G-DEPLOY sono sequenziali e obbligatori.

---

## Workflow L3

| Workflow | Descrizione | Frequenza |
|---|---|---|
| **WF-SEC-SCAN** | aidefence scan + security-review su ogni deliverable; has_pii su ogni output con dati utente | ogni build |
| **WF-VERIFY** | verify.sh Empire + playwright-dev (test browser reali su siti/tool) | ogni build + post-deploy |

---

## Funzioni L4

| ID Funzione | Descrizione | Tool |
|---|---|---|
| T-aidefence-scan | Scansione AI-defence su output di ogni agente | `aidefence_scan` |
| T-security-review | Security review codice: OWASP top 10, segreti in git, env exposure | skill `security-review` |
| T-pii-check | Verifica PII su ogni output che potrebbe contenere dati utente | `aidefence_has_pii` |
| T-verify-run | Esecuzione verify.sh Empire: lint + type-check + build + brand gate | skill `verify`, `empire-verify` |
| T-playwright-run | Test browser automatizzati (user journey, responsive, performance) | skill `playwright-dev` |
| T-qa-report | Report QA consolidato per il commit record | output strutturato |

---

## Agenti L5 del reparto

| ID Agente | Ruolo | Tier |
|---|---|---|
| `plt-sec-sentinel` | Security always-on: aidefence, security-review, has_pii — attivo su ogni build | Sonnet |
| `plt-qa-runner` | QA browser con playwright-dev + verify | Haiku |

---

## La catena di gate obbligatoria

```
G-SEC
  ├─ aidefence_scan → verde
  ├─ security-review → 0 issue critiche
  └─ has_pii → nessun dato sensibile esposto
        │
        ▼
      G-QA
        ├─ site-qa verde
        ├─ playwright test tutti green
        └─ verify.sh exit 0
              │
              ▼
            G-BRAND
              └─ stile conforme empire-premium-style / brand kit cliente
                    │
                    ▼
                  G-DEPLOY
                    └─ smoke test post-deploy verde
```

Qualsiasi gate rosso → blocco; escalation a `plt-director`.

---

## Escalation

- Issue critica security → blocco immediato + escalation `plt-director` + notifica Board
- QA fallita × 2 → `plt-cc-master` rivede il brief del reparto upstream
- PII rilevato in output pubblico → revoca deploy + incidente tracciato in Memory `platform/incidents`

---

## Asset esistenti

| Path / Skill | Stato |
|---|---|
| skill `playwright-dev` | USA |
| skill `verify` | USA |
| skill `security-review` | USA |
| skill `review-and-heal` | USA — fix regressioni QA |
| Ruflo `aidefence_scan`, `aidefence_has_pii` | USA |

---

## Nuove skill da creare (via FORGE)

| Skill | Scopo | Priorità |
|---|---|---|
| `empire-verify` | verify.sh DE: lint+build+playwright+brand gate in un unico comando | ALTA |

---

## KPI

| KPI | Target |
|---|---|
| Incidenti security post-deploy | 0 |
| First-pass QA (deliverable passa al primo giro) | ≥ 80% |
| Lighthouse performance siti consegnati | ≥ 90 |
| Scan aidefence eseguiti / build totali | 100% |

## Connessioni

- [[06-PLATFORM/ECOSISTEMA.md]] — panoramica PLATFORM
- [[06-PLATFORM/BACKBONE.md]] — GOVERNANCE: Security Sentinel su ogni build
- [[06-PLATFORM/Reparti/Deploy-CICD.md]] — G-DEPLOY finale
- [[company/Sentinels/Security-Sentinel/README.md]] — sentinel always-on della holding
- [[PIANO-MAESTRO/06-ECOSISTEMI-CORE.md]] — dossier completo
