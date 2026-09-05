---
Type: CONCEPT
Status: Active
Tags: #emperator #agenti #orchestrazione #gerarchia
Created: 2026-09-03
Last updated: 2026-09-05
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

## La forma del battito — dove Forze e Assetto si dichiarano *(2026-09-05)*

Forze e assetto non vivono in un blocco a parte: si **ricontano dentro ogni recap**. Dal
2026-09-05, per ordine di Max, la forma del recap e' fissa carattere per carattere — prima
cambiava a ogni messaggio e costringeva a rileggerlo invece che scorrerlo:

```
**⏱️ RECAP — <n>%**

🟠 **Fatto:** <una riga>
🟠 **Sto facendo:** <una riga>
🟠 **Farò:** <una riga>
🟠 **Forze:** <n> attive — <GRADO> <nome> <cosa fa> | ...
🟠 **Assetto:** **GOD EMPEROR DOOM** | normale
🟠 **Potere:** <n>%
```

Sei regole: titolo in grassetto con la percentuale · riga vuota · pallino arancione 🟠 davanti a
ogni voce (mai un trattino, mai un `•`) · sei etichette in grassetto coi due punti, sempre tutte
e in quest'ordine · `GOD EMPEROR DOOM` in grassetto · testo dopo l'etichetta normale, una riga
sola. L'arancione e' il colore dell'Impero (`#fb4604`): il pallino non e' decorazione, e' il
segnale che quella riga e' un battito e non testo qualunque.

**Il caso "nessuna" si scrive lo stesso**, per Forze come per Assetto: una riga assente non si
distingue da una dimenticata. Dottrina: `.claude/agents/emperator.md` §6.11. Innestata anche in
`scripts/emperator_hook.py`, perche' una regola che vive solo nella dottrina lunga non viene
eseguita quando il contesto si compatta. Checkpoint: `CP-20260905-002` (**EMP-RCAP**).

## Connessioni
- [[Digital_Empire_6_Phase_Process]]
- [[Tool_Claude_Code_Agenti]]
- [[Digital_Empire_Memory_System]]
