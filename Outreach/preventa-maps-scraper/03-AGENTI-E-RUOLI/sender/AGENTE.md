# AGENTE: Sender-1 — Message Sender Agent (Rate-Limited Outreach)
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Comunicazione & Outreach
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Sender-1` spedisce i messaggi generati da `Writer-1`, applicando **rate limit giornalieri
separati per canale** (default: 15 WhatsApp, 25 Email) per evitare pattern di spam rilevabili e
blocchi degli account di invio.

**Bias comportamentale:** Prudente, non aggressivo. Preferisce sospendere l'invio piuttosto che
sforare un limite.
**Principio cardine:** *"Un lead contattato domani vale più di un account bannato oggi."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `messages: List[Dict]` (da Writer-1, con `canale_primario`), `city: str` |
| **Output** | Sottoinsieme dei messaggi effettivamente inviati (`stato: "contattato"`), gli esclusi restano fuori dal report |
| **Evento pubblicato** | `messages.sent` → `{city, messages[], count}` |
| **Parametri** | `daily_whatsapp_limit` (default 15), `daily_email_limit` (default 25) |

---

## 3. Comportamento

1. Per ogni messaggio determina il canale (`canale_primario`: `whatsapp` o `email`).
2. Se il contatore giornaliero del canale ha raggiunto il limite, **salta il lead** (non lo mette
   in coda, lo esclude da questo run — il lead resta disponibile per il run successivo).
3. Applica un ritardo casuale 1.0–2.5s tra un invio e l'altro (disattivato se `city` contiene
   "test", per non rallentare la suite di test unitari).
4. Marca ogni messaggio inviato con `stato: "contattato"` e pubblica `messages.sent`.

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| Limite giornaliero raggiunto per un canale | Lead saltato con log `WARNING`, spedizione continua sugli altri canali/lead |
| `canale_primario` mancante nel messaggio | Trattato come `"email"` (fallback esplicito) |
| Zero messaggi in input | Evento `messages.sent` con `count: 0` |

---

## 5. CLI Standalone

```
python agente.py --input data/messaggi.json --city Como [--output data/report_contatti.json]
```

---

## 6. Riferimenti
- [`../writer/AGENTE.md`](../writer/AGENTE.md) — agente a monte (genera i messaggi da inviare)
- [`../responder/AGENTE.md`](../responder/AGENTE.md) — agente a valle (classifica le risposte in arrivo)

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_sender.py`, Phase 3, 2026-07-25).*
