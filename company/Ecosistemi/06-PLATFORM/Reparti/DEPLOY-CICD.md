# DEPLOY-CICD — 06-PLATFORM

> Reparto responsabile di tutto il ciclo di deploy: Vercel, monitoring log, rollback e smoke test post-deploy.

## Missione
Gestire il gate G-DEPLOY e l'intero ciclo di vita post-QA: deploy su Vercel (o altro target), monitoring log nelle prime ore critiche, rollback immediato se necessario, smoke test post-deploy. Emette l'evento costo per OPERATIONS a ogni deploy completato. È l'ultimo reparto nella pipeline — il suo verde significa che il lavoro è in produzione e funzionante.

**Prerequsito non negoziabile:** DEPLOY-CICD non viene attivato finché G-SEC e G-QA non sono verdi nel shared_state. plt-deploy-op verifica questo prima di procedere.

## Team Agenti
| ID | Agente | Tier | Ruolo |
|---|---|---|---|
| `plt-deploy-op` | Deploy Operator | Haiku | Deploy Vercel + logs + rollback + evento costo |

## Workflow L3
| ID | Workflow | Descrizione |
|---|---|---|
| WF-DEPLOY | Deploy Completo | vercel:deploy + logs + rollback + smoke post-deploy |

## Funzioni L4
- **T-prereq-check** — verifica G-SEC ✓ e G-QA ✓ nel shared_state prima di procedere
- **T-vercel-deploy** — esecuzione deploy Vercel con monitoring build log
- **T-smoke-test** — GET sulle 5 pagine chiave: HTTP 200, no error boundary React
- **T-log-watch** — monitoring `vercel:logs` per 10 minuti post-deploy (zero 5xx)
- **T-rollback** — rollback a versione precedente se smoke test o log watch falliscono
- **T-cost-event** — emissione evento `{commessa, durata_deploy, esito, url}` per OPERATIONS
- **T-notify** — notifica plt-cc-master con URL produzione + report deploy

## Asset Esistenti Usati
| Path | Utilizzo |
|---|---|
| `vercel:deploy` | Deploy principale su Vercel |
| `vercel:logs` | Monitoring log post-deploy |
| `vercel:setup` | Setup iniziale progetto Vercel (nuovi clienti) |
| `agency-empire-landing/` | Sito pilota per testare la pipeline CI/CD |

## Procedura di Rollback
```
1. smoke test fallisce su ≥1 pagina critica
   → plt-deploy-op → vercel rollback immediato (< 2 min)
   → notifica plt-cc-master con URL fallita + error
   → plt-cc-master → escalation a plt-site-builder per fix

2. log watch mostra >1% 5xx nei primi 10 min
   → plt-deploy-op → valuta: fluttuazione (aspetta 2 min) o rollback
   → se persiste → rollback + notifica plt-director

3. deploy build Vercel fallisce
   → plt-deploy-op → analizza log → identifica errore specifico
   → rimanda a plt-site-builder con path:error per fix
   → retry dopo fix (max 3 tentativi prima di escalation plt-director)
```

## Gate G-DEPLOY (checklist)
```
✓ G-SEC verde nello shared_state
✓ G-QA verde nello shared_state
✓ Build Vercel completata senza errori
✓ Smoke test: HTTP 200 su 5 pagine chiave
✓ Log watch: 0 errori 5xx in 10 min
✓ Evento costo emesso per OPERATIONS
→ G-DEPLOY VERDE: URL produzione consegnato
```

## KPI
| KPI | Target |
|---|---|
| Deploy completati senza rollback | ≥ 90% |
| Rollback eseguiti correttamente quando necessari | 100% |
| Tempo medio deploy + smoke test + log watch | ≤ 15 min |
| Eventi costo emessi per deploy | 100% |
| Build Vercel fallite per errori evitabili (tipo mismatch, env missing) | < 5% |

## Connessioni
- [[06-ECOSISTEMI-CORE]] — dossier padre
- [[SECURITY-QUALITY]] — G-SEC e G-QA prerequisiti
- [[plt-deploy-op]] — agente operativo del reparto
- [[plt-cc-master]] — riceve l'esito finale e chiude il ciclo
- [[BACKBONE]] — registro agenti
