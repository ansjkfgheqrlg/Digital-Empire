# AGENTE: Responder-1 — Incoming Reply Handler Agent
> **Versione:** 2.0 · **Owner:** GAEL · **Controllore:** A2-QA · **Origine:** FORGE
> **Ecosistema:** preventa-maps-scraper · **Reparto:** Comunicazione & Outreach
> **File Python:** [`agente.py`](./agente.py)

---

## 1. Identità e Missione

`Responder-1` classifica le risposte ricevute dai lead contattati in 4 categorie di intento e
propone una risposta suggerita coerente, così che chi gestisce la conversazione (umano o agente a
valle) non debba interpretare il testo da zero.

**Bias comportamentale:** Interprete conservativo, basato su keyword — non usa un LLM, quindi ogni
classificazione è deterministica e riproducibile (nessuna allucinazione possibile).
**Principio cardine:** *"Meglio una classificazione generica corretta che una specifica sbagliata."*

---

## 2. Ingresso / Uscita

| | Descrizione |
|---|---|
| **Input** | `lead_id: str`, `reply_text: str` |
| **Output** | `{lead_id, reply_received, esito, suggested_response}` |
| **Evento pubblicato** | `reply.processed` → il dict di output completo |

---

## 3. Logica di Classificazione (ordine di valutazione, primo match vince)

```
1. NO_GRAZIE          — contiene: no / non / togli / spam / rifiut* / cancella / basta
2. DOMANDA_OBIEZIONE   — contiene: prezzo / costo / tariffa / quanto costa / funziona / compatibile
3. INTERESSATO         — contiene: interessa / sì / si / info / chiamaci / ok / va bene / chiamata
4. RISPOSTO (fallback) — nessuno dei pattern sopra
```

**Nota di progettazione:** l'ordine è intenzionale — un messaggio come *"no grazie, quanto costa
comunque?"* viene classificato `no_grazie` (priorità al rifiuto), non `domanda_obiezione`, perché
il pattern NO_GRAZIE è valutato per primo.

---

## 4. Failure Modes

| Scenario | Comportamento Atteso |
|---|---|
| Testo vuoto o solo spazi | Cade nel fallback `risposto` (nessun pattern matcha una stringa vuota) |
| Testo con più intent contrastanti | Vince il primo pattern in ordine di valutazione (vedi §3) |

---

## 5. CLI Standalone

```
python agente.py --lead-id "+39 333 1234567" --text "Sì mi interessa, chiamatemi pure"
```

---

## 6. Riferimenti
- [`../sender/AGENTE.md`](../sender/AGENTE.md) — agente a monte (invia i messaggi che generano le risposte)

---

*Agente ricostruito in formato cartella-per-agente (Phase B, 2026-07-27) — logica invariata rispetto
all'implementazione flat originale (`agente_responder.py`, Phase 3, 2026-07-25).*
