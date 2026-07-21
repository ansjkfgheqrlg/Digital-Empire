# 04-AGENTS — Registry Digital Empire / ESTATE-2026
> L3 del modello architetturale. Formato canonico: **7 file per agente** (spec · system-prompt · playbook · tools · memory · evals · failure-modes).
> Pack completi in workspace: `chief-forge/`, `memory-architect/`. Gli altri: manifest sintetico qui + espansione all'attivazione.

## CHIEF-FORGE (reparto costruzione) 🔨
| Agente | Ruolo | Stato |
|---|---|---|
| **chief-forge** | Lead/orchestratore build: costruisce tutto, rispetta DoD, revenue-first | ✅ pack 7-file attivo |
| forge-builder | esecutore build concreto (landing, pipeline, wrapper) | manifest |
| funnel-engineer | landing+checkout+email (motore site-*, Stripe/Gumroad ladder) | manifest |
| carousel-ops | wrap carousel-factory, batch run, QA regole | manifest |
| case-study-forge | case study da prove reali (Novacar) | manifest (skill esistente) |

## REVENUE 💰
| Agente | Ruolo | Stato |
|---|---|---|
| pricing-cell | prezzi/offerte (beast-preventivi) — ha prodotto DEC-EST-001 | manifest (skill esistente) |
| closer-a8 | script call/WA (WF-CLOSING-PREP) — WF-S1 §2 | manifest (skill esistente) |

## CONTENT ✍️
| Agente | Ruolo | Stato |
|---|---|---|
| content-forge-invoker | invoca `/forge` su materiale grezzo → artefatti | manifest |
| cro-copy-architect | copy landing/email APSOC | manifest (skill esistente) |

## YOUTUBE 🎬 (lead: department-lead) — vedi YT-AGENT-PACK.md
| Agente | Ruolo | Stato |
|---|---|---|
| department-lead | coordination, classifica input | ✅ esistente |
| yt-channel-ingester · video-single-ingester · yt-screening | ingestion + filtro | ✅ esistenti |
| **yt-fliki-renderer · yt-seo-publisher · yt-performance-analyzer · yt-niche-scout** | render/publish/analyze/scout | 🆕 spec in YT-AGENT-PACK (attivazione 24/07) |

## MEMORY MGMT 🧠
| Agente | Ruolo | Stato |
|---|---|---|
| **memory-architect** | custode memoria, EOD, RETRO, ReasoningBank | ✅ pack 7-file attivo |
| checkpoint-manager | close run (stage 9 YT) | manifest |

## VERIFICATION & CONTROL 🛡️
| Agente | Ruolo | Stato |
|---|---|---|
| silent-observer | audit continuo, gate 🟢🟡🔴 | manifest (esistente) |
| visual-verifier · compliance-auditor | verifica output YT/contenuti, anti-copia | manifest (esistenti) |

## STRATEGY 🧭
| Agente | Ruolo | Stato |
|---|---|---|
| strategy-director | planning P1→P7 (fatto 21/07), RETRO | manifest |

## Regole del registry
1. Nuovo agente: prima `memory_manager.py search` — se esiste già, si wrappa (ADR-EST-002).
2. Ogni agente ha memoria-mandato: chiusura task → checkpoint; fallimento → error; KPI → metric.
3. Espansione in 7-file solo all'attivazione effettiva (evita stub — regola zero stub).
