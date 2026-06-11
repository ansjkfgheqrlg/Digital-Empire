# 📐 GERARCHIA — Schema LX → L5

> Schema completo della gerarchia di EMPIRE OS.
> Fonte: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §2

## Albero gerarchico

```
👑  LX — DIPARTIMENTO EMPIRE
        Mandato Empire (posizionamento, brand voice, pricing, qualità)
        Sentinels (Cost · Quality · Drift · Security · Brand-Voice)
        → path: company/Mandato/ + company/Sentinels/
         │
L0      BOARD / C-SUITE (7 agenti)
        CEO=Empire-Conductor · COO · CTO · CMO · CRO · CFO · Chief-Forge
        Decisioni cross-ecosistema via hive-mind consensus (raft)
        → path: company/Board-CSuite/
         │
L1      10 ECOSISTEMI (Business Unit indipendenti ma connesse)
        01-AGENCY · 02-INFO-BUSINESS · 03-CONTENT-FACTORY · 04-MARKETING
        05-MULTI-BUSINESS · 06-PLATFORM · 07-FORGE · 08-INTELLIGENCE
        09-OPERATIONS · 10-MEMORY
        → path: company/Ecosistemi/
         │
L2      REPARTI (dentro ogni ecosistema)
        Esempi: AGENCY → Ricerca, Acquisizione, Preventivi, Delivery, Copy, Marketing
        → path: company/Ecosistemi/<NN-NOME>/Reparti/
         │
L3      WORKFLOW (un team per flusso end-to-end)
        Esempi: WF-OUTREACH-EMAIL, WF-LANCIO, WF-KDP-LIBRO, WF-YT-VIDEO
        → path: company/Ecosistemi/<NN-NOME>/Workflow/
         │
L4      FUNZIONI (un team per singola funzionalità)
        Esempi: T-Scraper, T-Qualifier, T-Writer, T-Sender, T-Thumbnail
        → path: company/Ecosistemi/<NN-NOME>/Funzioni/
         │
L5      AGENTI REALI (coordinator + workers)
        Running via Ruflo agent_spawn / Agent tool di Claude Code
        Schema fisso: identità · responsabilità · I/O · acceptance criteria
                      failure handling · shared_state · KPI · escalation
        → path: company/Ecosistemi/<NN-NOME>/Agenti/

⊕       GUILDS (trasversali tra ecosistemi)
        Prompt · Copy/APSOC · Quality · Cost · Design
        → path: company/Guilds/

⊕       SENTINELS (always-on su tutti i livelli)
        Cost · Quality · Drift · Security · Brand-Voice
        → path: company/Sentinels/
```

## Schema canonico team (invariante per ogni L3/L4/L5)

Ogni team ha OBBLIGATORIAMENTE:

```yaml
nome: WF-NOME / T-NOME / agente-nome
livello: L3 | L4 | L5
ecosistema: NN-NOME
coordinator: <agente-coordinator>
workers: [<agente-1>, <agente-2>]
input:
  schema: {}
output:
  schema: {}
acceptance_criteria: []
failure_handling:
  on_fail: retry | escalate | fallback
  escalation_to: <livello-superiore>
shared_state: <namespace AgentDB>
kpi_primario: "..."
```

## Regola: UN TEAM PER OGNI SINGOLA FUNZIONALITÀ

Ereditata da CF (AION GROUP). Non esistono agenti "jolly" che fanno tutto.
Ogni team è specializzato, misurabile, sostituibile.

*Creato: 2026-06-11 · Fonte: `PIANO-MAESTRO/00-PIANO-MAESTRO.md` §2, §6*
