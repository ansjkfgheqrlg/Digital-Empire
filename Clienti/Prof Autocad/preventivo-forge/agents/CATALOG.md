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
| `op-translator-copy` | S3 | `translate_copy.py` | Gael | ✅ |
| `op-pdf-renderer` | S5 | `render_pdf.py` | Gael | ✅ |

## Team VERIFICA (controlla, blocca)
| Agente | Gate | Controlla | Owner | Stato |
|---|---|---|---|---|
| `qa-extraction-verifier` | A | completezza estrazione (foto+campi+prezzo) | Gael | ✅ |
| `qa-translation-verifier` | B | fedeltà traduzione, no DE residuo, no fatti inventati | Gael | ✅ |
| `qa-price-verifier` | C | ricalcolo prezzo indipendente + formato titolo | Gael | ✅ |
| `qa-output-reviewer` | D | PDF finale completo e corretto | Gael | ✅ |
| `qa-immagini` | IMG | R-09: tutte le foto, complete, mai tagliate | Gael | ✅ |
| `qa-regole-checker` | R | REGOLE-SACRE R-01…R-14 + `regole-check.json` | Gael | ✅ |

Registro macchina: `../orchestration/registry.json`. Routing/escalation: `../orchestration/routing.md`.

## Pipeline
```
S1 scraper → S2 parser → [Gate A] → S3 translate_copy → [Gate B] →
S4 pricer → [Gate C] → S5 render_pdf → [Gate D] → PDF consegnabile
```

## Stato
Half A (Max) ✅ + Half B (Gael) ✅ costruita e verificata end-to-end (run BMW 320d: 4 gate verdi,
PDF 63 KB ispezionato). — 2026-07-01
