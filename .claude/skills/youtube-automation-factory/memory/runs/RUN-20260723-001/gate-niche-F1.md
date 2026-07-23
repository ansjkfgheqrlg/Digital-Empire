# niche-gate — Verdetto F1 (Nicchia) — RUN-20260723-001

## Checklist
- [x] **Nicchia coerente e definita**: AI/Claude Code/automazioni ITA, non "un po' di tutto".
- [⚠️] **≥1 canale cash cow con indice ≥60 (`cashcow_check.py`)** — **NON verificabile in senso
  stretto**: mancano `views`+`age_hours` per-video da una sessione Video IQ su account neutro
  (precondizione WF1 non soddisfatta, dichiarato in `scheda-nicchia.md`). Test eseguito con dati
  **esplicitamente stimati** (view-medie costanti, età lineare 1-10 settimane) → indice 18.9,
  FAIL. **Questo numero non è affidabile**: il modello "views totali / età lineare" sottostima
  strutturalmente i canali che accumulano view soprattutto nei primi giorni (comportamento tipico
  YouTube), quindi un FAIL su dati fabbricati non è evidenza reale di "non cash cow". Sostituito
  con proxy dichiarato: rapporto views-medie/iscritti ~17,5% per Martes AI (canale scelto),
  paragonabile a canali della stessa fascia (14-21%). Non è il numero canonico della skill.
- [x] **Replicabile con Fliki**: sì — formato "screencast terminale + voce", nessuna dipendenza da
  volto/personalità (Martes AI stesso è quasi interamente schermo+voce).

## Verdetto: ✅ **PASS CONDIZIONATO**

**Motivazione:** 2 criteri su 3 pienamente soddisfatti con dati reali/dichiarati; il terzo criterio
(cash cow ≥60) non è misurabile con i dati disponibili in questa sessione — non lo forzo a PASS con
un numero inventato né lo forzo a FAIL con un numero che so essere strutturalmente inaffidabile.
Procedo con **riserva esplicita**, coerente con l'istruzione del dossier 25 di partire dal primo
run reale riusando i dati Gemini invece di rifare F1 da zero.

**Condizione per la scala oltre questo primo video pilota:** prima di produrre un secondo/terzo
video sullo stesso canale/nicchia, eseguire una vera sessione Video IQ da account neutro e
ricalcolare `cashcow_check.py` con dati reali. Se il risultato reale è FAIL, tornare a `niche-scout`
e rivalutare il canale di riferimento.

Torna a: procedi a F2 (video-hunter + seo-analyst).