---
name: empire-context
description: "Contesto completo di Digital Empire / EMPIRE OS per chiunque lavori nel monorepo (Max o Gael). ATTIVALA quando: l'utente è Gael o chiede di essere guidato ('guidami', 'cosa devo fare', 'da dove riprendo', 'spiegami il progetto', 'come funziona qui'), all'inizio di una sessione su questo progetto, quando serve sapere cos'è EMPIRE OS, il Piano Maestro, i 10 ecosistemi, la regola memory-first, il sistema di sync GitHub, l'offerta commerciale, o lo stato corrente del lavoro. È la knowledge base aziendale: carica identità, architettura, regole non negoziabili e punta ai file di verità."
---

# Empire Context — La Knowledge Base di Digital Empire

> Skill di progetto (viaggia col repo → identica per Max e Gael).
> Equivalente DE di `exponium-context`. Prima skill del Backbone (dossier 07, §3.2.1).

## 0. PRIMA DI TUTTO (memory-first, ADR-002 — NON negoziabile)

Prima di qualsiasi task leggi SEMPRE, in quest'ordine:
1. `company/Memory/INDEX.md` — indice maestro (decisioni attive, checkpoint)
2. `company/Memory/STATO-EMPIRE.md` — stato corrente, lavori in corso, **"RIPRESA DA"**
3. Se il task tocca un'area con ADR attivi → rispettali (mai contraddirli in silenzio)

Dopo OGNI task chiuso: checkpoint in `company/Memory/checkpoints/CP-YYYYMMDD-NNN.md`
(template in `company/Memory/templates/`) + aggiorna STATO-EMPIRE.md.
**Nessun task è "fatto" finché non è salvato in Memory.**

## 1. Chi siamo

- **Digital Empire** = multi-business company AI-native di **Max** (founder) e **Gael** (socio).
- Lavorano in 2 da PC diversi sullo **stesso monorepo GitHub** (privato:
  `ansjkfgheqrlg/Digital-Empire`) con **un solo account GitHub e un solo account Claude** (di Max).
- Identità git distinte: commit `sync(Max)` vs `sync(Gael)` (`git config user.name`).
- Posizionamento: **"L'agenzia progettata per essere licenziata"** — autonomia del cliente,
  non dipendenza. Brand voice: diretta, provocatoria, trasparente, **"prove non promesse"**.

## 2. Cosa vendiamo (offerta attuale)

| Prodotto | Prezzo | Cosa è |
|---|---|---|
| Outreach Factory | €4.000 | outreach automatizzato (email 300+/gg, LinkedIn, Instagram) sul server del cliente |
| Content Factory | €3.500 | produzione contenuti AI (caroselli, script, caption) |
| Second Brain | €2.500 | knowledge base a grafo + memoria per LLM |
| **Engine Room** (bundle) | €8.000 | tutti e 3 |

Comuni: codice di proprietà del cliente, **€0 canoni mensili**, setup 7 giorni, 90gg supporto.
Vetrine: `presentazione-empire.vercel.app` + `agency-empire-kohl.vercel.app`.
Copy: framework **APSOC** (Attenzione→Problema→Soluzione→Obiezioni→CTA), gate qualità ≥80/100.

## 3. EMPIRE OS — l'architettura (ADR-001)

Digital Empire è organizzata come **holding di 10 ecosistemi di agenti AI** (modello AION
GROUP/Exponium esteso). Piano completo: **`PIANO-MAESTRO/`** (10 dossier — LEGGILI per il
dettaglio, questo è solo l'indice):

| # | Ecosistema | Missione | Dossier |
|---|---|---|---|
| 01 | AGENCY | acquisire + servire clienti (outreach GIÀ ATTIVO — NON toccare senza leggere ADR-003) | 01 |
| 02 | INFO-BUSINESS | lanci, corsi, ebook | 02 |
| 03 | CONTENT-FACTORY | contenuti multi-formato multi-brand (brand_kit+icp come input) | 03 |
| 04 | MARKETING | copywriting (priorità assoluta), ads, email, analytics | 04 |
| 05 | MULTI-BUSINESS | YouTube Automation, Publishing/KDP, E-comm | 05 |
| 06 | PLATFORM | engineering, siti (Crea Siti), security, deploy | 06 |
| 07 | FORGE | crea skill/agenti/team (skill-creator, content-forge) | 06 |
| 08 | INTELLIGENCE | wiki, Empire Studio (ingestione video), Memory Empire | 06 |
| 09 | OPERATIONS | runtime, swarm, costi, scheduling | 06 |
| 10 | MEMORY | memoria operativa (CP/ADR/piani/stato) — interroga PRIMA, scrivi DOPO | 09 |

Gerarchia: Mandato Empire (LX) → Board/C-Suite (L0) → Ecosistemi (L1) → Reparti (L2) →
Workflow (L3) → Funzioni (L4) → Agenti (L5). Backbone+Ruflo+121 skill mappate: dossier 07.
Roadmap 12 fasi con gate: dossier 08. **Fase corrente: vedi STATO-EMPIRE.md.**

## 4. Le regole non negoziabili (i 13 pattern — dettaglio in 00-PIANO-MAESTRO §6)

**METODO (ADR-006):** ogni fase di costruzione segue il **Ciclo di Fase Empire a 9 passi**
(`PIANO-MAESTRO/10-METODO-CICLO-FASE.md`): RECALL → SPEC → PRE-MORTEM → BUILD → GATE →
REVIEW indipendente → TEST → COMMIT → RETRO. **Swarm obbligatorio** su ≥2 aree disgiunte —
vale identico per Max e per Gael (stesso account, stesse capacità: lo swarm lo lancia
Claude Code via Agent tool, chiunque sia l'utente). Prompt sempre idempotenti.
Coordinamento via blocco ⚠️ in STATO-EMPIRE pushato PRIMA del build.

Le 5 che servono SEMPRE:
1. **Memory-first (#13)**: vedi §0.
2. **Wiki-first (#12)**: leggi `second-brain-vault/wiki/index.md` + `log.md`; ogni operazione
   logga in `wiki/log.md`. La wiki è la fonte di verità umana.
3. **Wrap, mai riscrittura (ADR-003)**: i sistemi attivi (outreach in primis) NON si riscrivono
   né si toccano; si wrappano. Verificare sempre su disco prima di assumere.
4. **Dry-run prima di spendere (#3)**: niente spese API/crediti senza ok esplicito di Max.
5. **Gate qualità (#4)**: niente esce senza check (copy APSOC ≥80, brand voce, zero claim
   senza prova).

## 5. Il sistema di sync GitHub (ADR-004)

- Repo: `https://github.com/ansjkfgheqrlg/Digital-Empire` (privato).
- Motore: `scripts/empire-sync.ps1` — `-Mode pull` (allinea), `-Mode push` (commit+rebase+push,
  rate-limit 90s), `-Mode full`. MAI distruttivo, mai force-push.
- Hook in `.claude/settings.json`: SessionStart→pull, Stop→push (automatico per entrambi).
- Conflitto → file `SYNC-CONFLICT.txt` nella root: il lavoro è SALVO in commit locale;
  guida l'utente: `git pull --rebase` → risolvi → `git add -A; git rebase --continue; git push`.
- NON viaggiano su GitHub (per design, `.gitignore`): segreti/.env, sessioni browser
  (instagram/linkedin_session.json, session_data/, maps_session/), DB lead, video mp4, zip,
  PNG copertine KDP, node_modules/.next. File nuovi >100MB → Drive, mai nel repo.
- `Clienti/EXPONIUM` = repo cliente SEPARATO (exponium-client), escluso dal monorepo.
- 7 ex-repo annidati inclusi col loro `.git` rinominato `.git.bak` (NON ripristinare senza ADR).

## 6. Se l'utente è GAEL — come guidarlo

1. Setup iniziale: segui `SETUP-GAEL.md` passo-passo (login gh come ansjkfgheqrlg col codice
   device autorizzato da Max, clone, `git config user.name "Gael"`).
2. Guida con pazienza, zero gergo git: lui non deve MAI usare comandi git a mano.
3. Ogni suo lavoro: stessa disciplina di Max — memory-first (§0), wiki-first, checkpoint.
4. Prima di fargli toccare un'area: leggi il dossier PIANO-MAESTRO relativo + STATO-EMPIRE
   (così non collide col lavoro in corso di Max).
5. Coordinamento: se STATO-EMPIRE dice che Max sta lavorando su X, indirizza Gael su task
   non sovrapposti (cartelle/dossier diversi) — il sync gestisce i merge ma non le decisioni.
6. Domande sul "perché" di una scelta → `company/Memory/decisions/ADR-00*.md`.

## 7. Mappa file di verità (dove guardare per cosa)

| Domanda | File |
|---|---|
| Stato corrente / da dove riprendo? | `company/Memory/STATO-EMPIRE.md` |
| Perché è stato deciso X? | `company/Memory/decisions/` (ADR-001..004) |
| Cosa è stato fatto e quando? | `company/Memory/checkpoints/` + `wiki/log.md` |
| Architettura completa? | `PIANO-MAESTRO/00-PIANO-MAESTRO.md` |
| Dettaglio di un ecosistema? | `PIANO-MAESTRO/0X-ECOSISTEMA-*.md` |
| Prossimi passi / fasi? | `PIANO-MAESTRO/08-ROADMAP-FASI.md` |
| Tutta la conoscenza DE? | `second-brain-vault/wiki/index.md` |
| Setup PC di Gael? | `SETUP-GAEL.md` |
| Sistema outreach attivo? | `Outreach/Outreach Workflow/` (ATTIVO — non toccare, ADR-003) |
| Modello architettonico di riferimento? | wiki `projects/Exponium/Exponium_Content_Factory_Studio.md` |

## 8. Storia essenziale (come siamo arrivati qui — 2026-06-10)

1. Studiato AION GROUP (Content Factory Exponium): holding 6 ecosistemi, LX→L5, Backbone,
   Sentinels — il modello di riferimento.
2. Prodotto il PIANO-MAESTRO (10 dossier, ~3.100 righe) con swarm di 7 agenti paralleli.
3. Aggiunto su richiesta di Max il 10° ecosistema MEMORY (urgenza massima) e COSTRUITO
   `company/Memory/` (INDEX, STATO, CP, ADR, template) + regola memory-first nel CLAUDE.md.
4. Creato il monorepo GitHub + sync automatico bidirezionale Max↔Gael (ADR-004):
   push iniziale 966 MiB, motore sync testato end-to-end.
5. Prossimo: fase F1 della roadmap (scaffolding `company/` completo), poi F2 Backbone.
