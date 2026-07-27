# AGENTE: Scraper-1 — Playwright Browser Driver Agent
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Acquisizione Lead
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Scraper-1` è l'agente driver del browser Playwright: apre Google Maps, esegue la ricerca per
città+categoria e restituisce i lead grezzi (nome attività, telefono, sito web, recensioni) senza
alcuna qualifica — quella è responsabilità di `QualifierAgent` a valle.

**Bias comportamentale:** Esecutore meccanico. Non giudica un lead, lo estrae e basta.
**Principio cardine:** *"Un lead non estratto non esiste per il resto della pipeline."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `city: str`, `categoria: str`, `limit: int` + una `Page` Playwright già inizializzata |
| **Output** | Lista di dict lead grezzi (`nome_attivita`, `telefono`, `sito_web`, `numero_recensioni`, `media_recensioni`, ...) |
| **Evento successo** | `leads.extracted` → `{city, leads[], count}` |
| **Evento fallimento** | `run.failed` → `{city, error}` |

---

## 3. Comportamento

1. Pubblica `search.started` con città e categoria.
2. Richiede una `Page` Playwright valida — se assente, solleva `ValueError` esplicito (nessun
   fallback silenzioso: uno scraper senza browser è un bug di orchestrazione, non un caso limite).
3. Delega l'estrazione vera e propria a `browser.scrape_city()` (motore Playwright condiviso in
   `02-AUTOMAZIONI-E-SCRIPTS/browser.py`) — questo agente non contiene selettori CSS/XPath propri.
4. Pubblica `leads.extracted` con i lead grezzi, oppure `run.failed` in caso di eccezione, e la
   rilancia (l'orchestratore decide se ritentare, il singolo agente non nasconde l'errore).

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| `page` non inizializzata | `ValueError` immediato, nessuno scraping tentato |
| Eccezione durante `browser.scrape_city` | Pubblica `run.failed` con l'errore, poi rilancia l'eccezione |
| Zero lead trovati | Non è un errore: pubblica `leads.extracted` con `count: 0`, il Gate L2→L3 a valle decide se bloccare |

---

## 5. CLI Standalone

```
python agente.py --city Como --categoria "concessionario auto" --limit 10 [--headless]
```
Lancia una sessione Playwright autonoma (utile per test manuali fuori pipeline) e salva i lead
grezzi in `data/raw_leads_output.json`.

---

## 6. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/browser.py`](../../02-AUTOMAZIONI-E-SCRIPTS/browser.py) — motore Playwright condiviso
- [`../../02-AUTOMAZIONI-E-SCRIPTS/agents.py`](../../02-AUTOMAZIONI-E-SCRIPTS/agents.py) — facade di orchestrazione (Conductor)
- [`../qualificatore/AGENTE.md`](../qualificatore/AGENTE.md) — agente a valle (qualifica dei lead estratti)

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_scraper.py`, Phase 3, 2026-07-25).*
