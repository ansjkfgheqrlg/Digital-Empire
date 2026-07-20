# TOOLS — youtube-script-factory (retrofit MIR-5 sprint 1)

3 tool Python, **estratti 2026-07-20 dalle SEZIONI 7-9 di `Skill-youtube.md`** (wrap ADR-003: markdown
intoccato, è lui il master; in caso di modifica alle sezioni 7-9 → ri-estrarre e verificare `py_compile`).
Stato verifica: **compilano 3/3 (`python3 -m py_compile`)**; non eseguiti end-to-end in sandbox (CLI interattive).
Persistenza locale: scrivono JSON nella cartella di lavoro corrente.

| Tool | Scopo | Funzioni chiave | Uso |
|---|---|---|---|
| `tools/genera_script.py` (1.255r) | Genera hook (20 formule/4 categorie), 5 titoli (6 formule), **script completo 7 componenti** + timestamps | `genera_hooks` · `genera_titoli` · `genera_script_completo` | `python3 tools/genera_script.py` → salva script JSON |
| `tools/checklist_qualita.py` (908r) | Scoring automatico **45 punti / 11 sezioni** + report qualità | `valuta_script` · `checklist_interattiva` (richiede input s/n) · `valuta_da_script_json` · `stampa_report` | `python3 tools/checklist_qualita.py` → salva report JSON |
| `tools/backlog_manager.py` (770r) | Backlog contenuti: priorità, **mix target Anchor 70 / Shift 20 / Conversion-Audit 10**, performance per video, piano settimanale | `aggiungi_video` · `aggiorna_stato` · `aggiorna_performance` · `aggiorna_quality_score` (_load/save JSON) | `python3 tools/backlog_manager.py` |

## Regole d'uso
1. **Score prima della registrazione:** nessuno script entra in `batch-XX/` pianificato se non ha
   passato `checklist_qualita.py` con voto dalla fascia "buono" in su (scala 45pt — vedi spec.md §debito 2).
2. **Backlog come unica pila:** i video futuri si domano in `backlog_manager.py` (mix 70/20/10 vincolato);
   il piano di registrazione (sessioni da 4h) resta nel kit `Formazzione/Youtube/batch-01/PIANO-BATCH-01.md`.
3. **Output JSON:** gli script/report generati NON vanno nel vault wiki — sono artefatti operativi
   della factory; la conoscenza distillata va in wiki (WIKI-FIRST) a parte.
4. Esecuzione su macchina Windows di Max: stessi comandi (`python` invece di `python3` se serve).
