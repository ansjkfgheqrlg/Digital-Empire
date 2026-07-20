# 🧾 REGISTRO-ERRORI — YouTube Lead Machine (W7) (MIR-6 — standard regola Max 07-05)

> Scope: runtime produzione/operazioni del canale + manutenzione del kit. Owner: FORGE-AGENT-SKILL → 04-MARKETING W7.
> **Complementare, NON duplicato**: i failure-modes della SKILL (deriva di metodo) stanno in
> `.claude/skills/youtube-lead-machine/failure-modes.md`. Qui solo errori di esecuzione/processo.

| # | Errore | Causa | Fix applicato | Regola per non ripeterlo |
|---|---|---|---|---|
| YE-1 | yt-dlp non scarica trascrizioni nel sandbox (TLS EOF su youtube.com) | Rete sandbox bloccante verso YouTube | Ingest via fetch esterno + trascrizione completa letta (metodo CP-20260719-009) | Mai affidarsi a yt-dlp nel sandbox: usare fetch_page; salvare NOTE strutturate, mai solo il dump VTT. |
| YE-2 | Collisioni di numerazione checkpoint (007→009, 001→004) in un giorno | Sessioni parallele su main scrivono CP stesso numero | Rinumerazione + nota nel CP (pattern consolidato) | Prima di scrivere un CP: `git pull` e controllare l'ultimo numero usato sul main; se conflitto, rinumerare e tracciare. |
| YE-3 | Versione toolkit `master-build-architecture` rischiava sovrascrittura con clone GitHub meno completo | Clone fresco diverso dalla copia main | ADR-009 punto 3: reference = versione main; NOTA BENE in STATO-EMPIRE | Per ogni vendor: confrontare SEMPRE clone vs copia main prima di sostituire; decisione scritta in ADR. |

**Anti-recidiva:** 2 ripetizioni → regola promossa nel kit o in `FORGE-AGENT-SKILL/rules/`.
