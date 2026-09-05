---
Type: REGISTRO
Status: Active (append-only)
Tags: #ispettorato #errori #anti-recidiva
Created: 2026-07-20
Last updated: 2026-09-05
---

# REGISTRO-ERRORI — Empire-Wide (Regola Zero Recidiva)

> **Append-only.** Ogni voce chiusa non si riscrive. Un errore già qui che si ripresenta =
> **RECIDIVA = gate ROSSO bloccante** (dossier 15, agente `isp-recidiva-sentinel`).
> Prima di ogni build/run: consultare questo registro (aggancio RECALL, ADR-006).
> Queste 10 voci sono la migrazione iniziale (M1) — errori EMPIRE-WIDE realmente accaduti,
> ricostruiti da Memory/CP verificati. Registri locali (PreventivoForge, EmpireDesk) restano
> dove sono: qui vivono solo gli errori CROSS-CUTTING (dossier 15 §4).

---

| ID | Data | Sintomo | Causa radice | Contromisura | Owner | Stato |
|----|------|---------|---------------|---------------|-------|-------|
| **ERR-20260616-001** | 2026-06-16 | Collisione git: 5 file `06-PLATFORM/Reparti/*.md` in stato "deleted by us", commit bloccato | Naming misto MAIUSCOLO (Max) vs Title-Case (Gael) sullo stesso reparto → Windows `core.ignorecase` li tratta come lo stesso file, git va in conflitto | `git reset --hard` + `git stash drop` manuali (Max) per sbloccare; **regola Title-Case FISSA** imposta in ogni prompt di swarm da allora | Max/Gael | CHIUSO — 0 recidive da allora |
| **ERR-20260616-002** | 2026-06-16 | Swarm di miglioramento qualità girato su Sonnet low-effort senza che nessuno se ne accorgesse fino a fine lavoro | Modello/effort non verificato PRIMA di lanciare uno swarm di valore alto | Verifica esplicita del modello attivo prima di ogni swarm importante; Max stesso ha imposto `/model opus` come standard per build strutturali | Max | CHIUSO |
| **ERR-20260618/22-001** | 2026-06-18, ripetuto 2026-06-22 | Swarm muore a metà lavoro: "You've hit your weekly/session limit" | Due sessioni (Max+Gael) sullo STESSO account condiviso lanciano swarm Opus in parallelo → budget condiviso esaurito più in fretta del previsto | **Regola: un solo swarm Opus per volta**, coordinamento obbligatorio in STATO-EMPIRE prima di ogni swarm grosso | Max/Gael | CHIUSO — regola scritta in ADR e ripetuta in ogni dossier da allora |
| **ERR-20260622-001** | 2026-06-22 | Batch-3 swarm 01-AGENCY: 4 agenti muoiono dopo 14-21 tool_use, prodotto **1 file totale** su 62 attesi | Prompt agenti troppo READ-HEAVY: bruciavano il budget leggendo reference PRIMA di scrivere, morivano prima di produrre valore | **WRITE-EARLY**: struttura fornita inline nel prompt, letture minime (2-3), scrittura immediata file-per-file. Risultato misurato: da 1 file/21 tool_use a 16 file/20 tool_use nel re-run | Max | CHIUSO — pattern riusato con successo (batch-3 completato) |
| **ERR-20260622-002** | 2026-06-22 | Gate 01-AGENCY: 87 occorrenze di namespace AgentDB divergente (`agency/aN` vs `agency/0N-nome`) tra reparti diversi | Due convenzioni nate in prompt diversi senza una mappa autoritativa unica → rischio reale: gli agenti non si trovano le chiavi di stato a vicenda | Normalizzato tutto a `agency/a<N>` (canonico) + creato `company/Ecosistemi/01-AGENCY/NAMESPACE.md` — mappa autoritativa, nessuna chiave nasce fuori da lì | Max | CHIUSO |
| **ERR-20260622-003** | 2026-06-22 | 6 README v1 (A1-A6) elencavano un roster di agenti CHE NON ESISTE PIÙ (`AG-A2-BIBBIA-C1/C2/C3`, path v1 `../../Agenti/`) | La regola di idempotenza ("file esistente → SKIP") ha protetto i file v1 stantii invece di farli superare dal build V2 | **Regola nuova: l'idempotenza va SOSPESA contro i residui v1** — i file legacy sono target di superamento esplicito nel prompt, non di skip automatico | Max | CHIUSO |
| **ERR-20260703-001** | ricorrente, ultima 2026-07-19/20 | `git push origin main` fallisce ripetutamente: `send-pack: unexpected disconnect`, o rifiutato per fast-forward mentre il motore auto-sync di Gael/Max scrive in parallelo | Rete debole su push di pacchi grossi + due motori auto-sync (Max/Gael) che committano/pushano nello stesso minuto sullo stesso branch | Tecnica **light-sync via worktree**: checkout dei soli file cambiati su un worktree scaricato fresco da origin, commit mirato, push immediato — evita di portare tutta la history locale divergente | Max | APERTO — funziona ma è un workaround, non una soluzione (vedi REV-20260720-001) |
| **ERR-20260719-001 (EDE-8 nel registro locale EmpireDesk)** | 2026-07-19 | Max e Gael costruiscono, la stessa sera, DUE switcher-pannelli diversi per lo stesso file `EmpireDesk/ui/index.html`, con contratti API incompatibili (`/api/panels` vs `/api/modules`) — 8 blocchi in conflitto al pull | Nessuno dei due sapeva dell'altro nonostante l'ownership scritta in dossier 17 §5.1: la lettura di STATO-EMPIRE era avvenuta solo a inizio sessione, non prima di editare il file conteso | Merge manuale hunk-per-hunk senza perdita; **regola: su task "focus totale" con 2 sessioni attive sullo stesso file, `git pull` + rilettura STATO PRIMA di ogni editing del file conteso, non solo a inizio sessione** | Max/Gael | CHIUSO |
| **ERR-20260719-002** | 2026-07-19 | Tile "Caroselli" di EmpireDesk sarebbe stato un bottone finto: parte, produce log, exit code — ma fallisce SEMPRE (script chiamato senza l'argomento obbligatorio) | Selftest statico verificava solo che lo script esistesse (path), non COSA si aspettava come input runtime | Trovato PRIMA della release (non da un utente): aggiunto meccanismo generico `input` alle tile + validazione pre-lancio. **Regola: il selftest statico non basta quando lo script richiede argomenti — va letto il codice, non solo verificata l'esistenza** | Max | CHIUSO |
| **ERR-20260720-001** | 2026-07-20 | UI Empire Desk v0.1/v2 (pattern PreventivoForge, launcher a tile) costruita, testata, consegnata — poi BOCCIATA da Max ("graficamente fa schifo, struttura sbagliata"): un giorno di lavoro di Gael in parte da rifare, pivot su piattaforma Aureus esistente | Il pattern "launcher a tile stile PreventivoForge" era corretto per un TOOL cliente monofunzione, ma Empire Desk è l'app GESTIONALE del team — nessuno aveva verificato con Max il target visivo/UX PRIMA di costruire un'intera UI da zero | **Regola nuova: per artefatti ad alto impatto visivo (UI, brand-facing), verificare il riferimento visivo/UX con Max PRIMA del build, non dopo** — vedi anche REGISTRO-REVISIONI REV-20260720-001 per il pattern di correzione studiato | Gael/Max | CHIUSO (pivot eseguito, U0 completato same-day) |
| **ERR-20260905-001** | 2026-09-05 | Il battito/recap di Emperator (`emperator.md` §6.11) è uscito fuori dalla forma fissa almeno quattro volte nello stesso giorno, nonostante la forma fosse scritta carattere per carattere in dottrina e ripetuta nel promemoria di ogni messaggio | La regola viveva solo in prosa (dottrina + reminder), mai in un controllo eseguito prima dell'invio: l'enforcement dipendeva dalla disciplina del turno in corso, non da un gate — quattro incidenti precedenti sulla stessa regola (posizione, gergo, forze, assetto) l'avevano già dimostrato senza che la lezione bastasse | Creato `scripts/verifica_recap.py`: valida meccanicamente il blocco battito (sei righe fisse, ordine, pallino, grassetto, riga singola) prima dell'invio; obbligo scritto in `emperator.md` §6.11 e nel promemoria di `emperator_hook.py` di farlo passare da lì per ogni battito | Emperator | APERTO — chiusura richiede N battiti successivi verificati conformi, nessun `isp-verifier` automatico finché M3 non è costruito |

---

## Come si usa
1. Nuovo errore cross-cutting (tocca più di un ecosistema/reparto, o è un pattern ripetibile
   ovunque) → nuova riga qui. Errore locale a UN prodotto (bug in uno script specifico) →
   resta nel registro locale di quel prodotto (es. `EmpireDesk/REGISTRO-ERRORI.md`).
2. Prima di un fix/build: cercare per parola chiave qui E nel registro locale pertinente.
3. `isp-recidiva-sentinel` (M3) automatizza il confronto — fino ad allora, il RECALL manuale
   di ogni fase (ADR-006) include "ho controllato questo registro?".

## Connessioni
- [[ARCHITETTURA]] · [[15-DOSSIER-ISPETTORATO]] · [[REGISTRO-REVISIONI]] · [[REGISTRO-SUCCESSI]]
- Registri locali: `EmpireDesk/REGISTRO-ERRORI.md` · `Clienti/Prof Autocad/preventivo-forge/REGISTRO-ERRORI.md`
