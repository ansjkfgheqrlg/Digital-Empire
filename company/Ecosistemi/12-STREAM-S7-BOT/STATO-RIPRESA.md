# STATO-RIPRESA — APEX-7 / Stream S7

> Quando Max dice **"via"**, riparti da qui. Non re-derivare: e' gia' tutto scritto.

**Ultimo aggiornamento:** 2026-07-27
**Checkpoint Memory:** `company/Memory/checkpoints/CP-20260727-002.md`

---

## Dove siamo

**APEX-7 Level 2 — operativo, testato, verde.**

```
python test_apex7.py   →   exit 0, tutti i controlli superati
Gate APEX L6→L7        →   PASSED 7/7, score 1.0
```

## Mappa dei file (tutti in questa cartella)

| File | Ruolo | Stato |
|---|---|---|
| `event_bus.py` | Bus P0-P3, retry, DLQ, replay, 19 eventi | ✅ L2 |
| `memory_interface.py` | 5 query, indice, checkpoint/restore | ✅ L2 |
| `quality_gates.py` | 6 gate L1→L7, 33 criteri con rubrica | ✅ |
| `gate_verifiers.py` | Verificatori eseguibili | ✅ |
| `gate_agent.py` | Ispettore, macchina a stati reale | ✅ L2 |
| `meta_agent.py` | Registro, pattern, spawn-limit, override | ✅ L2 |
| `orchestrator.py` | Gate↔task, remediation, metriche | ✅ L2 |
| `worker_agent.py` | Claim per competenza | ✅ L2 |
| `ruflo_adapter.py` + `apex7_workflow.ruflo.yaml` | Config unica, backend intercambiabile | ✅ |
| `prompts/*.txt` | 7 prompt interni agenti | ✅ |
| `APEX-7.md` | Documentazione completa | ✅ |
| `test_apex7.py` | End-to-end con assert | ✅ verde |
| `main.py` + `*_engine.py` + `data_manager.py` + `risk_manager.py` | Bot S7 (Level 1) | ⏳ da collegare al ciclo APEX |

## Prossimo passo (L2 → L3)

**Loop adattivi con dati reali dal bot S7.** Concretamente:
1. Collegare `analysis_engine`/`execution_engine` al ciclo
   Orchestrator → Gate → Memory (oggi girano su un ramo separato del bus).
2. Tarare le soglie dei gate su esecuzioni misurate, non su numeri scelti a mano
   (criterio C5 del gate L2_TO_L3).
3. Far scrivere al bot le sue metriche nel layer `metrics` della memoria, cosi'
   `strategy_fetch` puo' imparare quali segnali hanno reso.

## Task parallelo richiesto da Max (non iniziato)

Usare **/content-forge** per convertire agenti / skill / flussi di lavoro da
markdown descrittivo a **agenti e skill OPERATIVI**, uno per uno, con checklist,
applicando APEX-7 come metodo (recall → spec → build → gate → test → commit).

## Come rieseguire il test

```bash
cd company/Ecosistemi/12-STREAM-S7-BOT
python test_apex7.py
```
Nota: la console Windows e' cp1252 — i print usano marcatori ASCII, niente emoji.
