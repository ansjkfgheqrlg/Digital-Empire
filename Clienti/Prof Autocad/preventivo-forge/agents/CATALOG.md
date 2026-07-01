# CATALOG — Agenti PreventivoForge

Agenti CF-grade (7 file: `agent.md`, `system_prompt.md`, `tools.md`, `playbook.md`,
`failure_modes.md`, `evals.md`, `memory.md`). Comunicano SOLO via file in `runs/<id>/`.

## Regia
| Agente | Ruolo | Owner | Stato |
|---|---|---|---|
| `conductor` | supervisore run: sequenza, gate, retry/fallback, stato/trace | Max | ✅ |

## Team OPERATIVO (fa il lavoro)
| Agente | Stage | Script | Owner | Stato |
|---|---|---|---|---|
| `op-scraper` | S1 | `scraper.py` | Max | ✅ |
| `op-parser` | S2 | `parser.py` | Max | ✅ |
| `op-pricer` | S4 | `pricer.py` | Max | ✅ |
| `op-translator-copy` | S3 | `translate_copy.py` | Gael | ⬜ |
| `op-pdf-renderer` | S5 | `render_pdf.py` | Gael | ⬜ |

## Team VERIFICA (controlla, blocca)
| Agente | Gate | Controlla | Owner | Stato |
|---|---|---|---|---|
| `qa-extraction-verifier` | A | completezza estrazione (foto+campi+prezzo) | Gael | ⬜ |
| `qa-translation-verifier` | B | fedeltà traduzione, no DE residuo, no fatti inventati | Gael | ⬜ |
| `qa-price-verifier` | C | ricalcolo prezzo indipendente + formato titolo | Gael | ⬜ |
| `qa-output-reviewer` | D | PDF finale completo e corretto | Gael | ⬜ |

Registro macchina: `../orchestration/registry.json`. Routing/escalation: `../orchestration/routing.md`.
