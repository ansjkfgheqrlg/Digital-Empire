# AGENTE: Sheets-1 — Google Sheets Integration Agent
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Salvataggio & Sincronizzazione
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Sheets-1` sincronizza i lead finali (post-outreach) su un Google Sheet condiviso, così il team
commerciale ha visibilità in tempo reale senza dover aprire i CSV locali. Deduplica e batching
sono delegati al modulo condiviso `sheets.py` — questo agente si limita a orchestrare la chiamata
e a gestire il caso "non configurato" senza bloccare la pipeline.

**Bias comportamentale:** Best-effort, mai bloccante. Se Sheets non è configurato, la pipeline
prosegue lo stesso (il CSV locale resta la fonte di verità).
**Principio cardine:** *"Google Sheets è una comodità, non una dipendenza critica del workflow."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `leads: List[Dict]` (lead finali), `city: str` |
| **Config** | `sheet_id`, `creds_path` (default `credentials.json`), `push_only_alta`, `worksheet_name` (default `Foglio1`) |
| **Evento successo** | `sheets.synced` → `{city, success: true}` (anche se skippato per assenza config) |
| **Evento fallimento** | `run.failed` → `{city, error}` |

---

## 3. Comportamento

1. Se `sheet_id` è vuoto/non impostato: pubblica comunque `sheets.synced` con `success: true` e
   ritorna — **non è un errore**, è la modalità "solo CSV locale".
2. Se configurato: delega a `sheets.upload_to_google_sheets()` (deduplica, batching, filtro
   `only_alta` se richiesto).
3. In caso di eccezione (credenziali invalide, quota API, Sheet ID errato): pubblica `run.failed`
   con l'errore e lo rilancia — qui il fallimento È bloccante, perché la chiamata era stata
   esplicitamente richiesta e non deve fallire in silenzio.

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| `sheet_id` assente | Skip silenzioso (log `WARNING`), pipeline prosegue |
| Credenziali JSON invalide/assenti | Eccezione propagata dopo `run.failed` |
| Sheet ID errato o permessi insufficienti | Eccezione propagata dopo `run.failed` |

---

## 5. CLI Standalone

```
python agente.py --input data/leads_finali.csv --sheet-id <ID> [--creds credentials.json] [--only-alta]
```

---

## 6. Riferimenti
- [`../../02-AUTOMAZIONI-E-SCRIPTS/sheets.py`](../../02-AUTOMAZIONI-E-SCRIPTS/sheets.py) — motore di upload condiviso (deduplica/batching)
- [`../gate/AGENTE.md`](../gate/AGENTE.md) — valuta il Gate L5→L6 prima di questo step

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_integratore_sheets.py`, Phase 3, 2026-07-25).*
