# R6 — Gate di Qualità A/B/C/D (Half B / Gael)

> RBI operabile a freddo. Motore: `implementation/qa_gate.py`.
> Agenti: `qa-extraction-verifier` (A), `qa-translation-verifier` (B), `qa-price-verifier` (C),
> `qa-output-reviewer` (D). Ogni gate ritorna `(ok: bool, issues: list[str])`. **Bloccante.**

## OBIETTIVO
Impedire che un preventivo difettoso arrivi al cliente. Ogni gate verifica **in modo
indipendente** l'output dello stage precedente; un gate rosso ferma la pipeline con messaggio chiaro.

## TRIGGER / WIRING
- `qa_gate.gate_a/b/c/d(ctx, dealer)` — chiamati dopo S2/S3/S4/S5.
- `run.py` oggi ha solo il Gate A minimo built-in. **Wiring pendente (Max):** aggiungere in `run.py`
  le 3 chiamate `gate_b/gate_c/gate_d` dopo S3/S4/S5 (passando `dealer` per i controlli forti).
- Comodo: `qa_gate.run_all(ctx, dealer)` → dict `{A,B,C,D: (ok, issues)}`.

## GATE A — Estrazione (`gate_a`)
| Controllo | Blocca se |
|---|---|
| `listing.json` valido vs schema | errori di schema |
| `price_listed_eur` numerico > 0 | mancante/non numerico |
| `make`, `model` presenti | mancanti |
| foto ≥1 e ogni `local_path` esiste su disco | foto dichiarate ma assenti |
| `description_de` non vuota | vuota |

## GATE B — Traduzione (`gate_b`)
| Controllo | Blocca se |
|---|---|
| `title_it`, `description_it` presenti | mancanti |
| `len(equipment_it) == len(equipment_de)` | disallineati |
| 0 residui tedeschi in `content.*` | token tedesco rilevato (`looks_german`, indipendente) |
| prezzo **non** in `title_it` | presente |
| numeri specs invariati vs `listing.json` (Anno, Km, Potenza) | alterati |
| `highlights_it` ≤ 6 | > 6 |

## GATE C — Prezzo (`gate_c`, ricalcolo INDIPENDENTE)
- Ricalcola `round(listed × (1 + pct/100) + fixed_1 + fixed_2)`.
- Parametri: da `dealer.pricing_resolved` se `dealer` è passato (vera indipendenza), altrimenti
  dal `breakdown` di `listing_it.json`.
| Controllo | Blocca se |
|---|---|
| ricalcolo == `price.final_eur` | diverso |
| coerenza `surcharge_eur` | scostamento > 0.5 € |
| `final_title` contiene prezzo formattato + `€` + marca | formato errato |

## GATE D — Output PDF (`gate_d`)
| Controllo | Blocca se |
|---|---|
| esiste `preventivo_*.pdf` e > 20 KB | assente/troppo piccolo |
| `specs_it`, `description_it`, `equipment_it` non vuoti | sezione mancante |
| prezzo in `final_title` | assente |
| tutte le foto di `listing.json` su disco | mancanti (gallery incompleta) |
| (se `dealer`) re-render HTML: 0 placeholder `{{ }}`, immagini incorporate | placeholder non risolti |

## GESTIONE ERRORI
- File di stage mancante (es. `listing_it.json`) → gate rosso con causa esplicita.
- `jsonschema` non installato → il check di schema è saltato con nota (non è un falso PASS).

## CASI LIMITE
- Glossario incompleto → Gate B rosso su residui: **azione = estendere `glossary_de_it.py`**, non allentare il gate.
- Prezzo di listino sospetto (parsing) → Gate C lo prende ricalcolando in modo indipendente.

## LOG
Ogni gate ritorna la lista `issues` (motivo del blocco). Il chiamante (run.py/conductor) logga e
scrive lo stato in `state.json` (`GATE_x -> passed|blocked`).
