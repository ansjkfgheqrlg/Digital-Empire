---
Type: CENSIMENTO
Status: Active
Tags: #impero-vivo #cadute #agenti-delegati #anti-recidiva
Created: 2026-09-06
Fonte: company/Memory/checkpoints/ · company/Memory/riprese/ · company/Memory/STATO-EMPIRE.md · company/Ispettorato/registro/REGISTRO-ERRORI.md
---

# CENSIMENTO 03b2 — LE CADUTE DEGLI AGENTI DELEGATI

> Ogni caso qui sotto e' un fallimento reale di un agente delegato (swarm, scagnozzo,
> sentinella, doom bot, sub-agente) registrato in un file dell'Impero. Nessuna riga e'
> ricostruita a memoria: ognuna cita il percorso da cui viene.

---

### CASO 1 — Quattro agenti morti, un file
- **Fonte:** `company/Ispettorato/registro/REGISTRO-ERRORI.md` (ERR-20260622-001)
- **Cosa e' successo:** Nel batch-3 dello swarm 01-AGENCY "4 agenti muoiono dopo 14-21 tool_use, prodotto **1 file totale** su 62 attesi". Lo swarm e' stato lanciato, ha consumato il budget e ha restituito quasi niente.
- **Perche':** "Prompt agenti troppo READ-HEAVY: bruciavano il budget leggendo reference PRIMA di scrivere, morivano prima di produrre valore".
- **Cosa e' costato:** 61 file su 62 non prodotti, un intero batch da rilanciare. Il re-run misurato passa "da 1 file/21 tool_use a 16 file/20 tool_use".
- **Regola che l'avrebbe evitato:** Struttura inline nel prompt, massimo 2-3 letture, prima scrittura entro i primi tool_use (WRITE-EARLY).

