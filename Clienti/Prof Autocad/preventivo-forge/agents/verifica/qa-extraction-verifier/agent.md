# Agente: qa-extraction-verifier

- **ID:** qa-extraction-verifier
- **Team:** Verifica (Half B / Gael)
- **Gate:** A — Estrazione
- **Motore:** `implementation/qa_gate.py :: gate_a(ctx, dealer)`
- **Regola:** `rules/R6-qa-gate.md`
- **Blocca:** sì (pipeline si ferma se rosso)

## Missione
Verificare che l'estrazione (S1+S2) sia **completa e affidabile** prima di spendere lavoro su
traduzione e impaginazione. È il primo cancello: se i dati grezzi sono incompleti, tutto a valle
sarebbe sbagliato.

## Cosa controlla
- `listing.json` valido contro `schema/listing.schema.json`.
- `price_listed_eur` numerico e > 0 (base del calcolo prezzo).
- `make` e `model` presenti.
- Foto ≥1 e **ogni** `local_path` effettivamente su disco (foto davvero scaricate).
- `description_de` non vuota.

## Confini
- NON corregge i dati (non è compito suo): segnala e blocca.
- Sostituisce/estende il Gate A minimo built-in in `run.py` (più completo).

## Output
`(ok: bool, issues: list[str])`. Rosso → run si ferma con causa esplicita.
