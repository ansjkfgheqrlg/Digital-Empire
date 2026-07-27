# AGENTE: Qualifier-1 — Lead Qualifier Agent (Site Analyst)
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Acquisizione Lead
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Qualifier-1` trasforma lead grezzi (usciti da `Scraper-1`) in lead **qualificati e prioritizzati**
(ALTA/MEDIA/BASSA), analizzando presenza/qualità del sito web e segnali di reputazione, in
parallelo per performance (`checker.qualify_leads_parallel`, ThreadPoolExecutor).

Da questa versione (v2.0) integra anche il **Data-Validator-Gate**: se collegato a un `GateAgent`,
ogni lead qualificato passa da `gate_agent.validate_lead()` prima di proseguire — scarta i lead
senza alcun canale di contatto (telefono E sito assenti) o con reputazione negativa consolidata.

**Bias comportamentale:** Analista scettico. Qualifica solo ciò che è verificabile dai dati, non
inferisce intenzioni.
**Principio cardine:** *"Una priorità ALTA non richiesta è peggio di zero lead."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `leads: List[Dict]` (lead grezzi da Scraper-1), `city: str` |
| **Output** | Lista di lead qualificati con `priorita_lead` (ALTA/MEDIA/BASSA) + eventuali campi di note |
| **Evento pubblicato** | `leads.qualified` → `{city, leads[], count}` |
| **Dipendenza opzionale** | `gate_agent: GateAgent` — se assente, nessun filtro Data-Validator applicato (comportamento legacy) |

---

## 3. Comportamento

1. Delega la qualifica parallela a `checker.qualify_leads_parallel()` (motore condiviso in
   `02-AUTOMAZIONI-E-SCRIPTS/checker.py`) — questo agente non contiene logica di scoring propria.
2. Se `gate_agent` è configurato, applica `validate_lead()` a ogni lead qualificato: i lead che
   falliscono (nessun canale di contatto, o reputazione <4.0/5 su ≥5 recensioni) vengono scartati
   e il conteggio degli scarti viene loggato.
3. Pubblica `leads.qualified` con la lista finale (post-gate se applicabile).

**Nota di progettazione:** il filtro Data-Validator-Gate è opzionale via constructor param, non
obbligatorio — questo permette a chiamanti legacy (test, script standalone) di istanziare
`QualifierAgent()` senza gate e mantenere il comportamento pre-v2.0 invariato.

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| `gate_agent` passato non implementa `validate_lead` | `AttributeError` catturato per-lead, il lead viene mantenuto (fail-open, non fail-closed: un gate rotto non deve bloccare l'intera pipeline) |
| Zero lead in input | `checker.qualify_leads_parallel([])` ritorna lista vuota, evento pubblicato con `count: 0` |
| Tutti i lead scartati dal gate | Evento `leads.qualified` con lista vuota — il Gate L3→L4 a valle decide se bloccare il workflow |

---

## 5. CLI Standalone

```
python agente.py --input data/raw_leads.json --city Como [--output data/qualified.json]
```

---

## 6. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/checker.py`](../../02-AUTOMAZIONI-E-SCRIPTS/checker.py) — motore di qualifica parallela
- [`../gate/AGENTE.md`](../gate/AGENTE.md) — Data-Validator-Gate (`validate_lead`)
- [`../scraper/AGENTE.md`](../scraper/AGENTE.md) — agente a monte (fornisce i lead grezzi)

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_qualificatore.py`, Phase 3, 2026-07-25), che già
includeva il wiring del Data-Validator-Gate.*
