# ADR-004 — Monorepo GitHub + sync automatico bidirezionale Max↔Gael

- **Data:** 2026-06-10
- **Stato:** ATTIVO
- **Decisori:** Max (richiesta esplicita + 3 risposte di autorizzazione)

## Contesto
Max e Gael lavorano in due su EMPIRE OS da PC diversi. Serve: tutto il workspace su GitHub,
pull automatico a inizio sessione, push automatico dopo ogni blocco di lavoro, su entrambi i PC.

## Decisione
1. **Monorepo privato `ansjkfgheqrlg/digital-empire`** = l'intero workspace Digital Empire
   (scelta esplicita di Max: SOLO account ansjkfgheqrlg; token rinnovato via device flow).
2. **Sync engine:** `scripts/empire-sync.ps1` (modes pull/push/full) — mai distruttivo,
   lock anti-sovrapposizione, rate-limit push 90s, conflitti → abort + `SYNC-CONFLICT.txt`
   (lavoro sempre al sicuro in commit locale).
3. **Hook Claude Code di progetto** (`.claude/settings.json`, viaggiano col repo):
   SessionStart → `-Mode pull` · Stop → `-Mode push`. Valgono identici per Gael dopo il clone.
4. **Esclusioni blindate** (`.gitignore`): segreti/.env, sessioni e profili browser
   (instagram/linkedin_session.json, session_data/, maps_session/ — TROVATI VIVI e rimossi
   dallo staging), DB lead con PII, node_modules/.next, video mp4, zip, PNG copertine KDP
   (2 GiB), file >100MB. I media pesanti viaggiano via Drive, non via git.
5. **Repo annidati:** 7 inclusi nel monorepo rinominando `.git`→`.git.bak` (reversibile;
   decisione esplicita Max). `Clienti/EXPONIUM` resta repo indipendente (condiviso col
   cliente su exponium-client). Vendor (github-repos/, astrowind) esclusi.
6. Identità git per-PC: Max = "Max" <max.infoproducer@gmail.com>; Gael configura la sua
   (SETUP-GAEL.md). `core.autocrlf false` + `.gitattributes * -text` (zero churn CRLF).

## Alternative scartate
- Repo separati per area — rompe l'interconnessione richiesta ("tutto collegato").
- Submodule per i repo annidati — fragili e ostili per workflow a due non-git-expert.
- Push solo manuale — contraddice la richiesta ("dopo ogni buona parte, automatico").
- Drive/Dropbox sync — niente storia, niente merge, conflitti binari.

## Conseguenze
- Gael: setup una-tantum in SETUP-GAEL.md, poi zero comandi git.
- Il push automatico committa anche stati intermedi: accettato (workspace di conoscenza).
- File >100MB nuovi vanno su Drive (regola d'oro n.3 di SETUP-GAEL).
- I 7 ex-repo perdono la loro storia git individuale nel monorepo (storia preservata
  nei rispettivi `.git.bak` locali).

## Contradiction-check
Nessun conflitto con ADR-001/002/003. Rafforza ADR-002 (la memoria viaggia col repo:
anche Gael eredita company/Memory e la regola memory-first).
