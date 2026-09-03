---
Type: CONCEPT
Status: Active
Tags: #emperator #agenti #orchestrazione #gerarchia
Created: 2026-09-03
Last updated: 2026-09-03
---

# Emperator — Gerarchia delle Forze e God Emperor Doom

## Overview
Struttura di comando di [[Emperator]]: tre gradi di agenti subordinati separati dalla **natura**
del lavoro, piu' un assetto personale potenziato per le opere enormi. Decisa da Max il
2026-09-03 e formalizzata in ADR-015.

## Dettagli

| Grado | Natura del lavoro | Modello | Nome | Durata |
|---|---|---|---|---|
| **Scagnozzo** | una domanda → una risposta: controlla, conta, cerca, verifica | haiku | `scagnozzo-<slug>` | secondi |
| **Sentinella** | una missione sola, anche lunga: ripulisce, bonifica, migra, porta a standard. Esegue, non decide | sonnet | `sentinella-<slug>` | minuti/ore |
| **Doom Bot** | fa il mestiere di Emperator su un'area disgiunta di un build grosso | opus | `doombot-<slug>` | quanto il build |
| **God Emperor Doom** | non e' un agente: e' Emperator in assetto massimo, con 11 obblighi di disciplina | — | — | quanto l'opera |

**La regola piu' importante:** ogni schieramento e ogni ingresso/uscita dall'assetto massimo si
dichiara **per iscritto** nel messaggio stesso (blocchi `FORZE SCHIERATE` e
`GOD EMPEROR DOOM — ATTIVO/CHIUSO`). Niente si attiva in silenzio.

**Gli 11 obblighi di God Emperor Doom:** dichiarazione d'ingresso · recall totale · pensiero ad
alta voce sui propri pensieri · piano battuto min. 3 volte · pre-mortem · schieramento delle
forze · battito dei 10 minuti · salvataggio a ogni micro-passo · ogni "fatto" misurato ·
autocritica finale · dichiarazione d'uscita con checkpoint.

**Dove vive:** `.claude/agents/emperator.md` §2-ter, §6-bis, §6-ter — e, in forma compressa,
nella stringa `DOTTRINA` di `scripts/emperator_hook.py` (legge della doppia scrittura, §6.13).

## Connessioni
- [[Digital_Empire_6_Phase_Process]]
- [[Tool_Claude_Code_Agenti]]
- [[Digital_Empire_Memory_System]]
