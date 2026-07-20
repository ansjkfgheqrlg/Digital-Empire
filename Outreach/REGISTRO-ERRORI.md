# 🧾 REGISTRO-ERRORI — Outreach Runtime (W1) (MIR-6 — standard regola Max 07-05)

> **Obbligatorio (MIR-6):** ogni errore reale di questo runtime va qui con causa+fix+regola, PRIMA di riprovare.
> Owner: 01-AGENCY/A2 · Controllore: ag-a2-qa · Standardizzato da FORGE-AGENT-SKILL (2026-07-20). ADR-003: fix = patch dichiarate, mai riscritture.

| # | Errore | Causa | Fix applicato | Regola per non ripeterlo |
|---|---|---|---|---|
| OE-1 | Su macchine diverse i .bat LinkedIn/Email/IG non partono | Path hardcoded `c:\Users\Utente\...` in `run_daily.bat`, `AVVIA-EMAIL-LIVE.bat`, `Instagram Automation/_avvia_ig.bat` (segnalato CP-20260719-004/EDE-2, alla data NON ancora fixato nel runtime) | — (aperto) | Ogni script nuovo: solo path **relativi alla cartella dello script** (`%~dp0`) o variabili da config; mai user-specific. Test su PC pulito prima del commit. |
| OE-2 | Launcher/scheduler resta bloccato "in corso" all'infinito | `pause` finale nei .bat + stdin non chiuso dal chiamante (scoperto da EmpireDesk, EDE-3) | Lato launcher fixato (stdin=DEVNULL); lato runtime: rimuovere `pause` quando il bat viene chiamato da automazioni (aperto) | I .bat destinati ad automazioni non devono contenere `pause`; interazione solo nei .bat "da doppio click". |
| OE-3 | `WinError 193` lanciando .bat da subprocess Python | .bat non eseguibile direttamente: serve shell | EmpireDesk lancia sempre via `cmd.exe /c` (fixato nel launcher) | Chiunque chiami .bat da codice: sempre `cmd.exe /c`. |
| OE-4 | Follow-up parziali ripetuti da capo dopo interruzione | Nessun checkpoint di avanzamento run | `rerun_partial.py` esiste per riprendere; usare quello, mai rilanciare la run intera | Prima di un rilancio: verificare cosa è già uscito (log/contatori) e riprendere dal punto di interruzione. |
| OE-5 | Token Facebook/IG scaduto → run IG fallisce (backlog aperto B-001) | Token a scadenza | (aperto) runbook rinnovo in `WFs/WF-OUTREACH-INSTAGRAM`/backlog | Quando fissato: segnare data scadenza e promemoria rinnovo qui e in memory/INDEX. |

**Anti-recidiva (Ispettorato, dossier 15):** un errore che si ripete 2 volte → proposta di nuova regola nel workflow del runtime o in `FORGE-AGENT-SKILL/rules/`.
