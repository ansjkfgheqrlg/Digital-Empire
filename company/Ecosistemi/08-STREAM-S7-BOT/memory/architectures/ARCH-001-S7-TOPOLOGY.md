# ARCH-001-S7-TOPOLOGY

## 1. Vision & Topologia dello Sciame (Principi Ruflo)
La macchina S7 deve operare con capitale reale, pertanto la gerarchia deve essere chirurgica.
La topologia scelta è **Hierarchical-Pipeline Ibrida**:
- **Hierarchical**: Il `chief-forge` (Conductor) ha il comando centrale. Interroga la memoria e assegna i macro-task.
- **Pipeline**: I reparti (Forgiatura, Quant, Risk, Execution) operano a stadi. Es: Ingestion -> Analyst -> MKD -> Quant -> Risk.

## 2. Dynamic Workflow & Handoff
Il passaggio di consegne avviene modificando il `case_state` in `MEMORY-INDEX.md` (Federation Zero-Trust).
Nessun "Context Stuffing" nei prompt. L'agente che subentra legge il Checkpoint precedente.

## 3. Reparti Digital Empire
- **Chief Forge**: Gestisce l'intera macchina S7.
- **Reparto Forgiatura**: Costruito sulla pipeline a 9 stadi di `/content-forge`. Dedicato alla creazione di Master Knowledge Documents dalle raw notes.
- **Reparto Quant & Risk**: Agenti specializzati (mempool-analyzer, expectancy-calculator, risk-manager) che eseguono le regole estratte dal MKD.
- **Reparto Meta & QA**: Agenti che validano gli schemi e osservano i fallimenti silenziosamente (Silent Observer).
