# 🧠 MEMORY — Outreach Runtime (W1) — memory locale (MIR-1, 2026-07-20)

> Memory di runtime AGGIUNTIVA (wrap ADR-003): questi file NON toccano la logica del runtime.
> Owner: 01-AGENCY / A2-Acquisizione · Controllore: ag-a2-qa (Gate Bibbia) + METHOD-GUARD.

## Stato runtime
- Runtime ATTIVO pre-Impero (email/LinkedIn/IG, ~300+/giorno). Monitorato anche dalla tile EmpireDesk (B0 in corso di chiusura da Gael, ordine pivot Aureus).
- Log operativi: `Outreach/Instagram Automation/run_today_log.txt` e log per-canale nelle sottocartelle.

## Regole di lavoro su QUESTO runtime
1. **ADR-003: wrap, mai riscrittura.** Fix nei .bat/script SOLO via patch dichiarata + riga in `Outreach/REGISTRO-ERRORI.md`.
2. **PII (Mandato Art.7.2):** liste lead/CSV = dati personali. Niente commit di dati lead nei file memory; qui solo stato/contatori.
3. Ogni errore reale → REGISTRO-ERRORI (causa+fix+regola) PRIMA di riprovare la run.

## Stato tecnico noto (da CP-20260719-004, EDE-2)
- ⚠️ `run_daily.bat` (LinkedIn), `AVVIA-EMAIL-LIVE.bat`, `Instagram Automation/_avvia_ig.bat` hanno **path hardcoded di un'altra macchina** (`c:\Users\Utente\...`) → su PC diversi falliscono. Vedi REGISTRO-ERRORI OE-1. Fix pianificato: path relativi.
- ⚠️ `pause` finale nei .bat → se lanciati da scheduler/launcher senza stdin aperto restano appesi (OE-2).
- B-001 backlog: token Facebook/IG da rinnovare (runbook in WF-OUTREACH-INSTAGRAM).

## Contatori rapidi (fonte: probe live EmpireDesk A1 metrics, 2026-07-19)
- LinkedIn run di oggi: 6 righe log · Email in coda: 458 · (rilevati da `EmpireDesk/modules/metrics.py`, mai inventati).

## Storico eventi (ultima in cima)
- 2026-07-20 — Memory locale + REGISTRO-ERRORI creati (MIR-1/6, FORGE-AGENT-SKILL).
