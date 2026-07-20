---
Type: REGISTRO
Status: Active (append-only)
Tags: #ispettorato #revisioni #primo-colpo-migliore
Created: 2026-07-20
Last updated: 2026-07-20
---

# REGISTRO-REVISIONI — "Primo Colpo Migliore"

> **Direttiva Max (2026-07-20):** "se ti richiedo 10 modifiche, studia TUTTE le modifiche —
> non solo l'ultima — per fare il lavoro meglio al primo output la prossima volta."
> Append-only. Agente responsabile (M3): `isp-revision-analyst`.
> KPI collegato: `revisioni_medie_per_task` (kpi/KPI-EMPIRE-WIDE.md) — deve calare nel tempo.

## Come si compila una voce
Per ogni task con **N ≥ 1 correzioni** prima dell'accettazione:
1. Elencare OGNI correzione della catena (non solo l'ultima) — cosa è cambiato, perché.
2. Isolare il PATTERN comune: cosa mancava fin dal primo output che, capito subito, avrebbe
   evitato tutte le correzioni.
3. Scrivere la regola generale (non solo il fix del caso specifico).
4. Il pattern entra anche in `MEMORY.md` (feedback) se riguarda il modo di lavorare col Max,
   non solo l'artefatto tecnico.

---

## REV-20260720-001

**Task:** costruzione UI Empire Desk v0.1/v2 (launcher a tile, stile PreventivoForge).
**Correzioni ricevute:** 1 — ma di scala massima: bocciatura totale + pivot dell'intera UI su
un'altra base (Aureus Agency OS), non un aggiustamento.
**Catena studiata:**
1. UI costruita e consegnata come launcher a tile (pattern verificato 2 volte su PreventivoForge
   e Prof Autocad — pattern GIUSTO per quei contesti).
2. Correzione di Max: "graficamente fa schifo, struttura sbagliata" — il pattern era corretto
   per un tool cliente monofunzione, SBAGLIATO per l'app gestionale interna del team (aspettative
   visive/di struttura completamente diverse).
**Pattern estratto:** il riuso di un pattern collaudato NON garantisce che sia il pattern giusto
per un contesto diverso — "già provato altrove" ha guidato la scelta senza verificare col Max
il target visivo/UX PRIMA di investire ore di build.
**Regola generale (write-once, vale per ogni futuro artefatto ad alto impatto visivo/brand):**
per UI/brand-facing NUOVE (non incrementali su qualcosa di già approvato), mostrare un riferimento
visivo o chiedere conferma esplicita del target ("è più simile a X o a Y?") PRIMA del build,
non dopo la consegna. Il costo di una domanda è minuti; il costo di un pivot è ore.
**Collegato a:** ERR-20260720-001 (REGISTRO-ERRORI).

---

## REV-20260720-002

**Task:** push git di questa stessa sessione (più commit, 19-20/07).
**Correzioni ricevute:** N ripetuto — `git push` fallito per disconnessione rete o fast-forward
respinto, richiesto retry manuale più volte nella stessa sessione.
**Catena studiata:**
1. Primi tentativi: `git push origin main` diretto → fallisce (rete o race col motore auto-sync).
2. Tentativo con `git pull --rebase` → conflitto risolto a mano, ancora fallisce al push successivo
   perché origin è avanzato di nuovo nel frattempo.
3. Convergenza sulla tecnica **light-sync via worktree** (checkout mirato su un worktree fresco
   da origin, commit isolato, push immediato) — funziona in modo affidabile.
**Pattern estratto:** su un repo con motore auto-sync CONCORRENTE che scrive ogni pochi minuti,
tentare `push`/`rebase` sul working tree principale (che può avere ore di modifiche non correlate)
è strutturalmente fragile — il worktree isolato al task specifico converge molto più in fretta.
**Regola generale:** per push isolati e urgenti su repo con sync concorrente, preferire da SUBITO
la tecnica light-sync worktree invece di provare prima il push diretto e "scoprire" il fallimento.
**Nota onesta:** questo è ancora un workaround (ERR-20260703-001 resta APERTO) — la soluzione
di fondo (coordinare il motore auto-sync per non collidere mai) non è stata costruita.

## Connessioni
- [[REGISTRO-ERRORI]] · [[REGISTRO-SUCCESSI]] · [[15-DOSSIER-ISPETTORATO]] · [[ARCHITETTURA]]
