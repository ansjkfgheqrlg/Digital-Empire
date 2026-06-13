# SECURITY-QUALITY — 06-PLATFORM

> Reparto trasversale: presidia i gate G-SEC e G-QA su OGNI deliverable PLATFORM, indipendentemente dal reparto di origine.

## Missione
Garantire che nessun codice esca dal PLATFORM senza aver superato i gate di sicurezza e qualità. È un reparto trasversale: serve WEB-ENGINEERING, PRODUCT-ENGINEERING e TOOLING-AUTOMATION. I suoi due agenti (plt-sec-sentinel e plt-qa-runner) sono attivati in sequenza obbligatoria su ogni pipeline prima del deploy.

**Principio di indipendenza:** il SECURITY-QUALITY non è coordinato dai builder — risponde direttamente a plt-director. Se G-SEC o G-QA falliscono, il reparto ha autorità di bloccare la pipeline senza attesa di approvazione.

## Team Agenti
| ID | Agente | Tier | Ruolo |
|---|---|---|---|
| `plt-sec-sentinel` | Security Sentinel | Sonnet | G-SEC: aidefence + security-review + PII check |
| `plt-qa-runner` | QA Runner | Haiku | G-QA: playwright-dev + verify + Lighthouse |

## Workflow L3
| ID | Workflow | Descrizione |
|---|---|---|
| WF-SEC-SCAN | Security Scan | aidefence scan + security-review su ogni deliverable |
| WF-VERIFY | Verify | verify.sh Empire + playwright-dev (test browser reali) |

## Funzioni L4
- **T-aidefence-scan** — scansione aidefence: XSS, injection, misconfiguration OWASP Top 10
- **T-secret-detect** — rilevamento secret/PII hardcoded (regex su tutto il codebase)
- **T-dep-audit** — audit dipendenze `npm audit` + CVE check
- **T-browser-test** — test playwright-dev: navigazione, form, mobile responsiveness
- **T-lighthouse-run** — Lighthouse su tutte le pagine: performance, SEO, accessibility
- **T-verify-run** — lint + build + test suite (verify.sh DE — skill `empire-verify` quando disponibile)
- **T-g-sec-report** — report G-SEC con severity tagging (CRITICAL/HIGH/MEDIUM/LOW)
- **T-g-qa-report** — report G-QA con screenshot, console errors, broken links

## Asset Esistenti Usati
| Path | Utilizzo |
|---|---|
| `playwright-dev` | Test browser reali automatizzati — strumento principale G-QA |
| `verify` | Gate qualità codice — lint, build, test |
| `security-review` | Analisi sicurezza codice — strumento principale G-SEC |
| `review-and-heal` | Review + fix automatico per issues rilevate |
| `site-qa` | Checklist QA specifica per siti |
| `site-report` | Report deliverable qualità finale |

## Gate di Qualità (il reparto LI ESEGUE, non li subisce)
```
G-SEC:
  ✓ 0 vulnerabilità CRITICAL o HIGH
  ✓ 0 secret/PII hardcoded
  ✓ 0 dipendenze con CVE noto non patchato
  → Se verde: sblocca G-QA

G-QA:
  ✓ 0 broken links
  ✓ 0 console errors in produzione
  ✓ Form e navigazione funzionanti
  ✓ Layout mobile (375px e 768px) corretto
  ✓ Lighthouse performance ≥ 90
  ✓ Lighthouse SEO ≥ 95
  → Se verde: sblocca G-BRAND → G-DEPLOY
```

**Regola:** MEDIUM e LOW in G-SEC vengono loggati ma non bloccano (gestiti nel backlog). CRITICAL e HIGH bloccano sempre.

## KPI
| KPI | Target |
|---|---|
| Incidenti security post-deploy | 0 |
| Deliverable con Lighthouse performance ≥ 90 | 100% |
| False negative G-QA (bug trovati in produzione dopo QA verde) | 0 |
| Tempo medio scan G-SEC + G-QA completo | ≤ 45 min |
| First-pass QA (passa al primo giro) | ≥ 80% |

## Connessioni
- [[06-ECOSISTEMI-CORE]] — dossier padre
- [[WEB-ENGINEERING]] — reparto servito (siti)
- [[PRODUCT-ENGINEERING]] — reparto servito (SaaS/App — G-SEC più stringente)
- [[DEPLOY-CICD]] — G-SEC e G-QA verdi sono prerequisito per G-DEPLOY
- [[plt-director]] — authority finale in caso di conflitto sui gate
