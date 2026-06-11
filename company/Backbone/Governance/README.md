# ⚖️ GOVERNANCE — Gate qualità e coerenza

> **Backbone component.** Garantisce che ogni output rispetti il Mandato Empire.

## Funzione

Tre livelli di controllo:
1. **Strutturale** — `verify-empire.sh` verifica che `company/` abbia 0 cartelle vuote, tutti i README, coerenza con i dossier
2. **Qualità** — gate APSOC (A8 ≥80/100), brand gate G2, copy gate Bibbia
3. **Architetturale** — contradiction-analyzer verifica che le decisioni non contraddicano ADR attivi

## Tool (da costruire in F2)

| Tool | Funzione | Stato |
|---|---|---|
| `verify-empire.sh` | gate struttura completa holding (ispirato a CF verify.sh) | da costruire F2 |
| `empire-verify` skill | skill wrapper del verify script | da forgiare P0 |
| `empire-brand-gate` skill | checklist brand gate eseguibile | da forgiare P0 |
| `contradiction-analyzer` | verifica coerenza decisioni vs ADR | skill installata |

## Checklist verify-empire (requisiti gate F1)

- [ ] `company/GRUPPO.md` esiste
- [ ] `company/Mandato/MANDATO-EMPIRE.md` esiste
- [ ] `company/Board-CSuite/` ha 7 schede agente
- [ ] `company/Ecosistemi/` ha 10 cartelle, ognuna con ECOSISTEMA.md + BACKBONE.md
- [ ] `company/Backbone/` ha 6 componenti con README
- [ ] `company/Guilds/` ha 5 guild con README
- [ ] `company/Sentinels/` ha 5 sentinel con README
- [ ] `company/Gerarchia/` ha schema LX→L5
- [ ] `company/Memory/` ha INDEX + STATO + almeno 1 CP + almeno 1 ADR
- [ ] 0 cartelle vuote senza README

## Stato: da costruire (F2, task 2.5)
