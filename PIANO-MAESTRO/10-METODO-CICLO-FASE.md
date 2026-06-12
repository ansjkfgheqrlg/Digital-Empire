# 🔄 10 — IL CICLO DI FASE EMPIRE (metodo di costruzione chirurgico)

> Evoluzione di "fase → controllo → avanti" (troppo povero, direttiva Max 2026-06-11, ADR-006).
> **OGNI fase di costruzione di EMPIRE OS — eseguita da Max, da Gael o da agenti — segue
> questi 9 passi. Nessun passo si salta. Vale identico per entrambi.**
> Sintesi di: SPARC, ciclo BUILD di AION GROUP, memory-first (ADR-002), lezioni reali
> (CP-001: scritture concorrenti; CP-005: swarm morto su session limit).

---

## I 9 passi

### 0. RECALL (memory-first, ADR-002)
Leggi `company/Memory/STATO-EMPIRE.md` + INDEX + CP/ADR rilevanti + `BACKLOG.md`.
Se Ruflo attivo: `memory_search` sui pattern di fasi simili (cosa è già andato storto?).
**Esci dal passo solo se sai:** cosa è stato fatto, cosa è in corso (anche dall'altro!), quali ADR vincolano.

### 1. SPEC (micro-spec della fase, 10 righe max)
- **DONE WHEN** misurabili (numeri, non aggettivi).
- **Out-of-scope** esplicito (cosa NON si fa in questa fase).
- **Dipendenze** (fasi/asset richiesti) e **budget** (tempo/token/crediti disponibili).
- Item minori che spuntano → dritti in BACKLOG (ADR-005), MAI nello scope.

### 2. PRE-MORTEM (3 minuti, scritto)
"Questa fase fallisce perché…" — minimo 3 modi concreti + contromisura per ognuno.
Contromisure OBBLIGATORIE sempre:
- **Idempotenza**: ogni task/prompt deve poter ripartire a metà senza duplicare (verifica l'esistente prima di scrivere).
- **Reversibilità**: git = rollback sempre possibile; mai overwrite distruttivi (pattern Memory Empire: backup→append→log).
- **Budget-guard**: se restano <20% delle risorse di sessione → NON iniziare build nuovi; chiudere col passo 7 (lezione CP-005: 6 agenti morti sul limite).

### 3. BUILD (esecuzione)
- **Swarm obbligatorio** quando il lavoro copre ≥2 aree/cartelle disgiunte (pattern Piano Maestro §7) — mai un agente solo dove più agenti paralleli servono. Vale per Max E per Gael.
- PRIMA di lanciare: scrivere il blocco **⚠️ COORDINAMENTO** in STATO-EMPIRE + push (l'altro socio non deve collidere).
- Agenti: cartelle disgiunte, fonti di verità esplicite (dossier), divieto di scrivere su wiki/log.md e Memory/ (solo il conductor).
- Dry-run prima di qualsiasi spesa reale (pattern #3).

### 4. GATE AUTOMATICO (deterministico)
Check eseguibili, non opinioni: struttura completa, 0 cartelle vuote, 0 file magri (<15 righe),
0 stub/TODO/placeholder, conteggi attesi (es. "37 schede agente"), JSON/YAML validi,
contradiction-check vs ADR/Mandato. Rosso = si torna al passo 3. **I gate non si bypassano.**

### 5. REVIEW INDIPENDENTE (anti auto-promozione)
Un agente/occhio **DIVERSO da chi ha costruito** fa review a campione del CONTENUTO
(il gate 4 misura la forma, questo la sostanza): 3-5 file a caso, coerenza col dossier
di riferimento, qualità reale, niente testo riempitivo. Chi costruisce non si approva da solo.

### 5-bis. REVIEW MAXIMILIAN (ADR-007 — da quando l'organo esiste, fase V2-3)
L'organo MAXIMILIAN risponde a UNA domanda: **"Max approverebbe questo?"** — scala
abbastanza grande? abbastanza chirurgico? è "un file markdown" travestito? cosa avrebbe
chiesto IN PIÙ? Se boccia: si torna al passo 3. Finché l'organo non esiste, il conductor
applica manualmente i tratti del corpus (`company/Memory/maximilian-corpus/`).

### 6. TEST FUNZIONALE / "AMNESIA"
La fase produce qualcosa di **usabile**, non solo presente:
- Documentazione/org → test amnesia: una sessione fredda (o l'altro socio) capisce e naviga solo leggendo?
- Workflow/codice → un'esecuzione end-to-end (dry o reale piccola) passa?
- Skill → trigger test: si attiva quando deve?

### 7. COMMIT (il lavoro non esiste finché non è condiviso)
Nell'ordine: **CP** in Memory (template) → **STATO-EMPIRE** aggiornato (fase, RIPRESA DA,
rimozione blocco coordinamento) → entry in **wiki/log.md** → **push** (empire-sync).
Senza CP-id la fase NON è chiusa (ADR-002). Senza push, per l'altro socio non è mai esistita.

### 8. RETRO (2 minuti) → poi fase successiva
- Lezioni/errori → nel CP (campo dedicato) e, quando attivo, nel ReasoningBank.
- BACKLOG aggiornato (item emersi).
- SOLO ORA si apre la fase successiva. **Mai due fasi aperte insieme dalla stessa persona.**

---

## Regole trasversali (sempre attive)

| Regola | Perché |
|---|---|
| Una fase per ciclo, mai parallelizzare fasi (i task DENTRO la fase sì — swarm) | drift e collisioni |
| Coordinamento Max↔Gael via STATO-EMPIRE, sempre PRIMA di costruire | account e repo condivisi |
| Prompt agenti sempre idempotenti | gli agenti muoiono (rete, limiti) — successo = ripartenza pulita |
| Budget-guard al 20% | chiudere bene > costruire tanto |
| Gate rosso 2 volte di fila sullo stesso punto → STOP + escalation (ADR o decisione Max) | non sbattere la testa |
| I numeri dei DONE WHEN vengono dai dossier PIANO-MAESTRO, non inventati | il dossier è la fonte di verità |

## Mini-checklist da copiare in ogni CP di fase
```
[ ] 0 RECALL fatto (STATO+ADR+BACKLOG letti)
[ ] 1 SPEC scritta (DONE WHEN numerici)
[ ] 2 PRE-MORTEM (≥3 rischi + contromisure)
[ ] 3 BUILD (swarm se ≥2 aree; coordinamento pushato prima)
[ ] 4 GATE automatico verde
[ ] 5 REVIEW indipendente fatta (chi: ___)
[ ] 6 TEST funzionale/amnesia passato
[ ] 7 COMMIT (CP+STATO+wiki+push)
[ ] 8 RETRO (lezioni nel CP, BACKLOG aggiornato)
```

## Connessioni
- [[00-PIANO-MAESTRO]] §7 (Dynamic Workflows + Swarm) — questo metodo lo rende operativo
- [[08-ROADMAP-FASI]] — le fasi F1-F12 si eseguono TUTTE con questo ciclo
- ADR-002 (memory-first) · ADR-005 (backlog) · ADR-006 (questo metodo)
