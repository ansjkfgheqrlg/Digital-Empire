# WORKFLOW S1 — Concessionari Anticipati (Versione Operativa)

**Owner:** Chief Forge Department + Max (relazioni)  
**Goal:** Chiudere ≥2 anticipi di PreventivoForge entro 7 giorni  
**Revenue Priority:** Massima (unico stream con certezza ≥95%)

---

## 1. Obiettivo

Anticipare le vendite di settembre a luglio usando il prodotto già consegnato (Novacar live).

---

## 2. Fasi del Workflow

| Fase | Nome | Agente / Responsabile | Output | Memory |
|------|------|-----------------------|--------|--------|
| 1 | Scout Lead | Max | Lista 7 concessionari caldi | decisions/ |
| 2 | Forge Offerta | offer-forge (content-forge2.0) | Offerta "Partenza Anticipata Luglio" | architecture/ |
| 3 | Script Call | A5/A8 | Script + sequenza email | planning/ |
| 4 | Esecuzione | Max | Contatti + negoziazione | performance/ |
| 5 | Verifica | compliance-auditor | Kill-switch + licenze | checkpoints/ |
| 6 | Chiusura | Chief Forge | Deal salvato + CP | checkpoints/ |

---

## 3. Agenti Coinvolti

- `concessionari-closer` (da forgiare)
- `offer-forge` (content-forge2.0)
- `compliance-auditor` (esistente)

---

## 4. Memory Path

```
company/Memory/ESTATE-WORKSHOP/stream-S1/
├── decisions/
├── performance/
└── checkpoints/
```

---

## 5. Regole

- Revenue prima di tutto
- Max gestisce le relazioni
- Chief Forge gestisce la forgiatura e i checkpoint

---

**Creato da Chief Forge Department** — 20 Luglio 2026