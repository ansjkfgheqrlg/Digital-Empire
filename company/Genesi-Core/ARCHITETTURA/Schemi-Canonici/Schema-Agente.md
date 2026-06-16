# SCHEMA CANONICO — Agente

> Forma MEDIA. Singola entità autonoma con identità, missione, I/O JSON, logica, escalation, KPI.
> Motore reale: `architect-agent`, `agent-factory/agent-architect`, shape 7-file (P06). Esempio
> calibrante: `company/Ecosistemi/10-MEMORY/Agenti/ME-A10-memory-sentinel.md`.

## Quando si usa questa forma (e quando NO → quale altra forma)
- **USA** quando serve un esecutore con ruolo singolo, attivato da trigger, che produce output
  strutturato e può escalare (es. validatore, registrar, scout, sentinel).
- **NO se** servono ≥2 ruoli che si coordinano con handoff → **Team**. NO se è una capability
  invocabile senza stato/identità persistente → **Skill**. NO se è solo un processo a passi
  senza un "chi" definito → **Workflow**.

## Struttura obbligatoria (sezioni/campi al millimetro)
1. **Titolo + codice** (id `<eco>-<ruolo>` o `arch-<ruolo>`, convenzione fissa).
2. **Identità**: ecosistema/organo, reparto, tipo (es. sentinel/builder/gate), tier (haiku/sonnet/opus).
3. **Missione**: cosa garantisce in 2–4 frasi + perché quel tier.
4. **Input / Output** con **schema JSON concreto** dei trigger e dell'output (no prosa vaga).
5. **Come ragiona / Logica**: il decision tree o il ciclo a passi numerati.
6. **Trigger**: elenco esatto delle condizioni di attivazione.
7. **KPI**: tabella metrica → target (binari/misurabili).
8. **Escalation / Failure**: cosa fa quando blocca, a chi notifica, casi critici.
9. **Memoria/State**: namespace AgentDB e record ricostruibile (test amnesia), se always-on.
10. **Connessioni**: ≥3 cross-link (reparto, destinatario escalation, collaboratori, dossier).

## Template vuoto (copiabile)
```markdown
# <ID> — <Nome Ruolo>
## Identità
- Ecosistema/Organo: · Reparto: · Tipo: · Tier:  · Codice: <ID>
## Missione
<2–4 frasi + perché il tier>
## Input / Output
**Input — trigger:** <elenco>
```json
{ "tipo": "...", "scopo": "...", "vincoli": [] }
```
**Output:**
```json
{ "risultato": "...", "stato": "PASS|FAIL", "note": [] }
```
## Come ragiona
1. ... 2. ... (decision tree / ciclo)
## Trigger
- <quando si attiva>
## KPI
| KPI | Target |
|---|---|
## Escalation / Failure
- <caso> → <azione> → <a chi>
## Memoria / State
- Namespace: <eco>/... — record ricostruibile
## Connessioni
- [[Reparto]] · [[Destinatario-escalation]] · [[Dossier]]
```

## Checklist di completezza (per struct-gate)
- [ ] Titolo con ID secondo convenzione + sezione **Identità** (reparto + tier).
- [ ] **Missione** presente (2–4 frasi) con motivazione del tier.
- [ ] **Input** E **Output** entrambi con almeno uno schema JSON concreto.
- [ ] **Come ragiona** con passi numerati o decision tree (non prosa generica).
- [ ] **Trigger** elencati esplicitamente.
- [ ] **KPI** in tabella con target misurabili.
- [ ] **Escalation/Failure** definita (≥1 caso con azione e destinatario).
- [ ] **Connessioni** ≥3 cross-link.
- [ ] Se always-on: namespace memoria + record ricostruibile presente.

## Esempio minimo compilato
`arch-validator` (Identità: ARCHITETTURA, L2.4, gate, sonnet). Missione: gate `struct-gate`.
Input `{artefatto, schema_atteso}` → Output `{stato:"INCOMPLETO", buchi:["manca escalation","KPI senza target"]}`.
Ragiona: 1. carica schema canonico, 2. confronta voce per voce checklist, 3. lista buchi.
KPI: falsi-PASS = 0. Escalation: 2 round INCOMPLETO → notifica arch-director. → COMPLETO.

## Anti-pattern (cosa rende lo schema NON valido)
- I/O descritto a parole senza JSON → non wireable a un motore reale (R1 del dossier).
- Manca l'escalation → l'agente blocca in silenzio (buco strutturale ricorrente, ReasoningBank).
- KPI vaghi ("funziona bene") invece di target binari.
- Logica = un paragrafo generico invece di passi/decision tree.
- Missione che sconfina nel contenuto/giudizio (è compito di FORGE/MAXIMILIAN, non dell'agente).

## Connessioni
- [[Schema-Team]] — quando i ruoli sono ≥2 e si coordinano
- [[Schema-Skill]] — quando è una capability senza stato/identità
- [[README]] — principio della FORMA GIUSTA
- 14-DOSSIER-ARCHITETTURA §3 (roster `arch-*`) · §7 (state/memoria)
