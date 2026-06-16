# SCHEMA CANONICO — Workflow

> Forma MEDIA. Processo eseguibile a passi con trigger, gate e owner. Motore reale: SPARC,
> `agent-planner`, `WF-ADR-REGISTER`. Esempio calibrante:
> `company/Ecosistemi/10-MEMORY/Workflow/WF-ADR-REGISTER.md`.

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando esiste una sequenza ripetibile di passi con input definito, gate di passaggio,
  output e owner per ogni passo (es. registrare un ADR, validare una struttura, fare un design).
- **NO se** è una capability invocabile non procedurale → **Skill**. NO se è un "chi" stabile
  → **Agente/Team**. NO se è una regola di giudizio → **Principio**. Spesso un Team *incarna* un
  Workflow: il Workflow è il "come", il Team è il "chi".

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Nome + Handoff code** (se inter-team/eco, es. `HC-ME-ADR`).
2. **Trigger**: condizioni e segnali tipici di attivazione; natura (obbligatorio/opzionale).
3. **Input**: schema JSON dei dati in ingresso, con campi obbligatori marcati.
4. **Pipeline a passi**: passi numerati, ognuno con OWNER esplicito + azione + branch decisionali.
5. **Gate**: condizioni di passaggio bloccanti (cosa ferma il flusso e perché).
6. **Output**: schema JSON del risultato.
7. **Dry-run / esempio**: una passata reale o criteri "questo caso richiede il workflow?".
8. **Connessioni**.

## Template vuoto (copiabile)
```markdown
# <WF-NOME>
## Handoff: <HC-...>   (se applicabile)
## Trigger
- <segnale> · Natura: OBBLIGATORIO|OPZIONALE
## Input
```json
{ "campo_obbligatorio": "...", "opzionale": null }
```
## Passi
1. <PASSO> (owner: <agente>) → azione → branch {OK|WARNING|FAIL}
2. ...
## Gate
- **G-x:** <condizione bloccante>
## Output
```json
{ "risultato": "...", "stato": "PASS|BLOCCATO" }
```
## Dry-run
<una passata reale>
## Connessioni
```

## Checklist di completezza (per struct-gate)
- [ ] **Trigger** elencati + natura (obbligatorio/opzionale) dichiarata.
- [ ] **Input** con schema JSON e campi obbligatori marcati.
- [ ] **Pipeline** con passi numerati, OGNI passo ha un OWNER esplicito.
- [ ] Almeno un **branch decisionale** (OK/WARNING/FAIL o equivalente).
- [ ] **Gate** bloccanti definiti (cosa ferma il flusso).
- [ ] **Output** con schema JSON.
- [ ] **Dry-run** o criteri di applicabilità presenti.
- [ ] **Connessioni** ≥3.

## Esempio minimo compilato
**WF-STRUCT-VALIDATE.** Trigger: pre/post FORGE (obbligatorio). Input `{artefatto, tipo}`.
Passi: 1. arch-schema-keeper carica schema del tipo (owner schema-keeper); 2. arch-validator
confronta voce per voce la checklist (owner validator) → branch {COMPLETO | INCOMPLETO}.
Gate G-struct: INCOMPLETO → blocca passaggio a FORGE. Output `{stato:"INCOMPLETO", buchi:[...]}`.
Dry-run: agente senza escalation → buchi:["manca escalation"] → BLOCCATO. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- Passi senza owner → nessuno sa chi esegue cosa.
- Nessun gate → un workflow "che non blocca mai" non protegge nulla.
- Input/Output a parole senza schema → non automatizzabile.
- Nessun branch → in realtà è un elenco, non un processo decisionale.
- Confondere Workflow (il come) con Team (il chi): definirli separatamente, poi collegarli.

## Connessioni
- [[Schema-Team]] — il "chi" che incarna il workflow
- [[Schema-Agente]] — gli owner dei singoli passi
- [[README]] — principio della FORMA GIUSTA
- 14-DOSSIER-ARCHITETTURA §4 (WF-ARCH-DESIGN, WF-STRUCT-VALIDATE, WF-ECOSYSTEM-DESIGN)
