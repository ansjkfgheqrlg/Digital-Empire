---
Type: CONCEPT
Status: Active
Tags: #processo #git #memoria #guardrail #qualita
Created: 2026-08-27
Last updated: 2026-08-27
---

# Guardrail che si fanno rispettare da soli

## Overview
Principio operativo di Digital Empire, ricavato da due regole che erano scritte, corrette
e **ignorate**: una regola che dipende dalla buona volontà non è un controllo, è un
desiderio. Un controllo è qualcosa che **impedisce** il guasto nel momento in cui stai per
farlo. Formalizzato il 2026-08-27 chiudendo B-008 e B-009.

## Il problema che lo ha generato
- **B-009** (collisioni di ID checkpoint): riaccaduto **5 volte**. Il fix esisteva da
  luglio (`python -m empire mem write`, con lock anti-collisione). La regola era scritta
  due volte nel backlog. Continuava a succedere.
- **B-008** (blob pesanti in git): aperto a giugno, ancora aperto ad agosto, mentre il
  repo arrivava a **3,1 GB** e un push da 899 MB moriva.

## Le tre regole ricavate

### 1. Scoprire *perché* la regola non veniva seguita, prima di riscriverla
Il fix di B-009 non veniva usato perché **era rotto**: `python -m empire mem write` moriva
su `ModuleNotFoundError: No module named 'yaml'`. Chiunque ci avesse provato lo trovava non
funzionante e tornava a scrivere il checkpoint a mano. Non era pigrizia: era uno strumento
guasto, e per due volte la risposta era stata "ripetere la regola" invece di provarla.

> Prima di riscrivere una regola ignorata, **eseguila**. Spesso non è disobbedienza, è un
> difetto.

### 2. Un guardrail non deve poter fallire — e se fallisce, mai in silenzio
Il controllo nuovo ha **zero dipendenze oltre stdlib e `git`**, apposta: quello vecchio è
morto su un `import`.

Lezione pagata subito: alla prima esecuzione il nuovo controllo ha **rilevato** la
collisione e poi è **morto stampandola** (`UnicodeEncodeError` sui caratteri box-drawing
nella console cp1252 di Windows), e il fallback difensivo ha lasciato passare il commit.
Un guardrail che fallisce in silenzio è **peggio** di nessun guardrail, perché aggiunge
falsa sicurezza. Era anche la ripetizione di [[Concept_Decisioni_Architetturali_ADR]]/B-013,
già documentata.

> Nei messaggi di un controllo: **solo ASCII**. Non puoi imporre un encoding a chi ti chiama.

### 3. Un controllo che dà falsi allarmi verrà disattivato
La soglia del guard sui blob è **5 MB** perché il deliverable legittimo più grosso (PDF di
un libro, ~3 MB) ci sta **sotto**: così il controllo non spara mai sul lavoro normale. Se
sparasse ogni giorno, la risposta prevedibile sarebbe `--no-verify` per abitudine — e a
quel punto il controllo non esiste più.

Corollario: le deroghe vanno **previste e motivate** dentro il controllo, non lasciate
all'aggiramento.

## Dove vive
- `.githooks/check_memory.py` — collisioni ID checkpoint (B-009) + CRLF nella memoria (B-028)
- `.githooks/check_blob.py` — blob > 5 MB verso la storia normale (B-008)
- `.githooks/installa.py` — attivazione **per macchina**: i hook non sono versionati da git,
  quindi un hook committato non si attiva da solo su nessun altro PC. `core.hooksPath`
  punta a `.githooks/`, che invece è versionato: aggiornare il controllo per tutti diventa
  un commit normale.

⚠️ Va lanciato **una volta per macchina**. Finché Max non lo fa sul suo PC, da lui i
controlli non esistono — ed è proprio la seconda macchina a creare le collisioni.

## Connessioni
- [[Concept_Decisioni_Architetturali_ADR]] — ADR-013 nasce da questo principio
- [[Tool_Workflow_Pubblicazione_Automatica]] — stesso principio applicato agli esiti:
  tre stati (PASS / FAIL / PASS PARZIALE) perché "pronto ma non loggato" non si travesta
  da successo
- [[Tool_Pipeline_Libri_KDP]] — il gate che distingue COMPLETO da CARICABILE
- [[Tool_Memory_Wiki_Bridge]] — l'altro ponte fra memoria e wiki
