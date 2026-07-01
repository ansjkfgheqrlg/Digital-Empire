# Evals — op-translator-copy

## Test funzionali
| Eval | Input | Atteso |
|---|---|---|
| E1 allineamento | `equipment_de` di 10 voci | `equipment_it` di 10 voci |
| E2 glossario | `["Standheizung","Rückfahrkamera"]` | `["Riscaldamento autonomo","Telecamera posteriore"]` |
| E3 umlaut ASCII | `["Rueckfahrkamera","Anhaengerkupplung"]` | tradotti (no residuo) |
| E4 titolo | make/model/variant | `title_it` senza cifre/€ |
| E5 no-invenzione | `equipment_de` vuoto | `description_it` non cita optional |
| E6 colore | `color="Schwarz"` | specs `Colore="Nero"` |
| E7 merge | `listing_it.json` con `price` preesistente | `price` invariato |

## Metriche di qualità
- **German-residue rate** = 0 (Gate B binario).
- **Copertura glossario** ≥ 95% dei termini equipment sul campione reale del cliente.
- **Fedeltà** = 0 fatti inventati (audit manuale su 3 preventivi a campione).

## Comando di verifica
Eseguire un run `--manual` su un annuncio noto e lanciare `qa_gate.gate_b(ctx, dealer)` → `(True, [])`.
Riferimento verificato: run BMW 320d → Gate B PASS.
