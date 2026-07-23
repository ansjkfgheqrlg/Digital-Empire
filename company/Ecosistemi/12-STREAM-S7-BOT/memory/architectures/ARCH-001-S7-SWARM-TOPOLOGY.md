# ARCH-001: Architettura Swarm S7 e Dynamic Workflow

## 1. Topologia (Principio Ruflo: Swarm Hierarchy & Pipeline)
L'ecosistema utilizza un approccio ibrido:
- **Hierarchical (Command & Control)**: Il `chief-forge-agent` orchestra le operazioni ad alto livello, assegna i task macro ai reparti e interroga lo stato di esecuzione. Ha la visione d'insieme.
- **Pipeline (Content-Forge)**: All'interno del *Reparto Forgiatura*, l'`ingestion-agent` processa l'input, lo cede all'`analyst-agent` (parallelizzabile) e confluisce nel `mkd-builder-agent` per la sintesi nel Master Knowledge Document.
- **Pipeline Condizionale**: Nel flusso di trading reale: `quant-analyst-agent` -> Segnale -> `risk-manager-agent` -> Approvazione/Rifiuto -> `execution-agent`.

## 2. Dynamic Workflow & Handoff Protocol
L'Handoff (passaggio di consegne) non avviene passando messaggi lunghi tra gli agenti (Anti-Pattern: *Context Stuffing*). Invece, si basa sul **Case State** condiviso nell'Ecosistema di Memoria.

**Esempio di Handoff (Reparto Forgiatura):**
1. Il Chief Forge istruisce l'Ingestion Agent: "Inizia fase 1 su `trascrizioni_strategia_X.md`".
2. L'Ingestion Agent completa il parsing, scrive i chunk in `memory/checkpoints/` e aggiorna il `MEMORY-INDEX.md` marcando il `case_state: {"fase_forgiatura": "ingestion_completa"}`.
3. Il Chief Forge legge lo stato e attiva il Workflow Builder Agent indicando l'indirizzo di memoria.

## 3. Principio di Federazione (Share)
- **Zero-Trust & Validation**: Ogni output di un reparto subisce una validazione (QA) prima di passare al livello successivo.
- **Memoria Condivisa**: Tutti gli agenti condividono le folder `decisions/` e `checkpoints/` per non perdere mai il contesto senza intasare il system prompt.
