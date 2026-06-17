# WF-ECOSYSTEM-MANDATE — Mandato Ecosistema Nuovo → Build → Operativo

> Workflow CF-grade | Owner: `cf-conductor` + `cf-ecosystem-builder` | Figura: Chief-Forge
> Blueprint: [[BP-Chief-Forge]] | Versione: 1.0 · 2026-06-17

---

## Scopo

Governare il ciclo completo di creazione di un nuovo ecosistema L1 della holding: dalla richiesta
strategica del Board fino all'ecosistema operativo e navigabile. Questo è il workflow a maggiore
impatto e rischio della figura Chief-Forge: ogni ecosistema richiede mesi di build e budget
significativo. La qualità dell'analisi e del mandato è decisiva.

**Regola fondamentale:** nessun ecosistema viene avviato senza approvazione esplicita del CEO
e blueprint ARCHITETTURA approvato. Nessuna eccezione.

---

## Trigger

- CEO/Board chiede esplicitamente un nuovo ecosistema
- `cf-intake-router` riceve richiesta con `tipo_richiesta: "ecosistema"` da qualsiasi ecosistema
- `cf-ecosystem-builder` identifica un gap strategico non coperto dai 10 ecosistemi esistenti

---

## Input

```json
{
  "tipo": "richiesta_ecosistema",
  "nome_proposto": "NN-NOME-ECOSISTEMA",
  "motivazione_strategica": "...",
  "problema_da_risolvere": "...",
  "richiedente": "CEO | CFO | XX-ECO",
  "budget_indicativo": "USD | non specificato",
  "urgenza": "STRATEGIC | HIGH | NORMAL"
}
```

---

## Flusso passo-passo

```
FASE 1 — ANALISI FATTIBILITÀ
  cf-ecosystem-builder (con cf-conductor)
    ├─ Verifica: i 10 ecosistemi esistenti coprono davvero questo gap? (evita ecosistemi fantoccio)
    ├─ Analisi dipendenze: quali skill/agenti già esistono? Quali mancano e vanno pre-forgiati?
    ├─ Analisi costo: stima agenti (n, tier, frequenza), costo build FORGE, costo operativo mensile
    ├─ Analisi rischi: dipendenze non risolte, ecosistemi concorrenti, timeline realistiche
    └─ Draft org chart L1→L5 ad alto livello (non millimetrico — quello è compito ARCHITETTURA)

  [Gate G1: analisi fattibilità completa]

FASE 2 — PROPOSTA AL CEO
  cf-conductor → CEO
    ├─ Documento proposta CF-PROP-YYYYMMDD-NNN con:
    │     missione · org chart preview · n agenti stimati · costo build · costo mensile
    │     timeline build · rischi · dipendenze pre-requisito · raccomandazione
    ├─ CEO può: APPROVA | DEFER | RIGETTA con motivazione
    └─ Se DEFER o RIGETTA → cf-memoria registra la decisione con motivazione → FINE

  [Gate G2: approvazione esplicita CEO — BLOCCANTE]
    APPROVA → Fase 3
    DEFER/RIGETTA → FINE (registrato)

FASE 3 — PRE-REQUISITI
  cf-conductor
    ├─ Identifica skill/agenti mancanti richiesti dall'ecosistema
    ├─ Per ogni pre-requisito: avvia WF-CAPABILITY-INTAKE separato (o verifica esistenza)
    └─ Aspetta che tutti i pre-requisiti siano nel registro prima di procedere

  [Gate G3: tutti i pre-requisiti disponibili nel registro]

FASE 4 — BLUEPRINT ECOSISTEMA
  cf-architettura-liaison → ARCHITETTURA L2.5 (Progettazione Ecosistemi)
    ├─ Invia mandato CF-MANDATO-YYYYMMDD-NNN con approvazione CEO allegata
    ├─ ARCHITETTURA disegna: org L1→L5 completa, BACKBONE, namespace memoria, handoff inter-eco
    │   dossier principale, reparti L2, agenti L5 (schede) — struttura millimetrica
    └─ Riceve blueprint validato con struct_gate

  [Gate G4: struct_gate PASS da ARCHITETTURA L2.5]
    PASS → Fase 5
    FAIL → revisione ARCHITETTURA con gap specifici (max 1 revisione)

FASE 5 — BUILD ECOSISTEMA
  cf-forge-liaison → FORGE (WF-ECOSYSTEM-NEW)
    ├─ Invia forge_order con blueprint ecosistema
    ├─ FORGE costruisce: cartella ecosistema, BACKBONE, agenti, workflow, principi, scripts, kpi, state
    ├─ Ogni sotto-componente (agente, workflow) segue il proprio gate di build nella FORGE
    └─ Monitora avanzamento; tempo build stimato (da misurare per ecosistemi reali)

  [Gate G5: ecosistema consegnato da FORGE — tutte le cartelle presenti]

FASE 6 — GATE OPERATIVO
  cf-ecosystem-builder + cf-eval-warden
    ├─ Verifica struct-gate ecosistema:
    │     ├─ BACKBONE.md presente?
    │     ├─ Namespace memoria attivo?
    │     ├─ Almeno 6 agenti con schede millimetriche?
    │     ├─ Almeno 1 workflow CF-grade?
    │     ├─ Handoff inter-eco definiti?
    │     └─ Navigabile nell'Explorer?
    └─ Decisione: OPERATIVO | INCOMPLETO (lista gap)

  [Gate G6: ecosistema OPERATIVO]

FASE 7 — REGISTRAZIONE E HANDOFF
  cf-conductor
    ├─ cf-agent-registry: registra tutti gli agenti del nuovo ecosistema
    ├─ cf-skill-portfolio: aggiunge skill del nuovo ecosistema al catalogo
    ├─ cf-memoria: registra evento fondativo ecosistema con pattern
    ├─ Aggiorna PIANO-MAESTRO (se applicabile) con riferimento al nuovo ecosistema
    └─ Handoff formale: il nuovo ecosistema viene presentato a CEO e al team che lo guiderà

  [FINE: ecosistema nella holding, registri aggiornati]
```

---

## State machine

| Stato | Descrizione | Transizione |
|---|---|---|
| `ANALISI_IN_CORSO` | Studio fattibilità e costo | → `PROPOSTA_PRONTA` |
| `PROPOSTA_PRONTA` | In attesa approvazione CEO | → `APPROVATA` o `RIGETTATA` o `DEFERRED` |
| `PRE_REQUISITI` | Build pre-requisiti mancanti | → `BLUEPRINT_PENDING` |
| `BLUEPRINT_PENDING` | In lavorazione da ARCHITETTURA L2.5 | → `BLUEPRINT_READY` |
| `BUILD_IN_PROGRESS` | FORGE sta costruendo l'ecosistema | → `BUILD_CONSEGNATO` |
| `GATE_OPERATIVO` | Verifica completezza ecosistema | → `OPERATIVO` o `INCOMPLETO` |
| `OPERATIVO` | Ecosistema nella holding | terminale |
| `RIGETTATO` | CEO ha rifiutato con motivazione | terminale |

---

## KPI di flusso

| Metrica | Target |
|---|---|
| Proposte con analisi costo/impatto complete | 100% |
| Ecosistemi avviati senza approvazione CEO | 0 |
| Ecosistemi consegnati con gate operativo PASS | da misurare |
| Pre-requisiti identificati e risolti prima di Fase 4 | 100% |

---

## Connessioni

- [[agenti/cf-conductor.md]] · [[agenti/cf-ecosystem-builder.md]]
- [[agenti/cf-architettura-liaison.md]] · [[agenti/cf-forge-liaison.md]]
- [[agenti/cf-eval-warden.md]] · [[agenti/cf-memoria.md]]
- [[14-DOSSIER-ARCHITETTURA]] §2 (L2.5 Progettazione Ecosistemi)
- [[07-FORGE/Workflow/WF-ECOSYSTEM-NEW.md]] — workflow operativo di build in FORGE
- [[workflow/WF-CAPABILITY-INTAKE.md]] — per i pre-requisiti di Fase 3
