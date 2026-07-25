# PIANO 1 — FONDAMENTA ONESTE
> Livello 1 di 7 · **Stato: Proposta** · Owner: Max · Controllore: Claude · Origine: RISTRUTTURAZIONE-00-BRIEF.md

---

## 0. Autocritica di RISTRUTTURAZIONE-00-BRIEF
Il Brief 00 identifica correttamente la presenza di 398 cartelle vuote ed esegue una diagnosi dividendo il problema in tre macro-categorie (spazzatura locale, sessioni mai partite e sensori spenti). Tuttavia, pecca di:
1. **Mancanza di dettaglio analitico:** Non elenca in modo atomico quali percorsi contengono le cartelle vuote di "Tipo 3" (sensori spenti).
2. **Nessun isolamento di sicurezza:** Non formalizza una barriera tra le cartelle tecniche locali e GitHub, lasciando spazio a push accidentali di sessioni browser intere.
3. **Statistiche grezze:** Mancanza di uno score numerico sullo stato dei 6 gate esistenti del piano estate.

---

## 1. Dimensione Migliorata
**Veridicità e Isolamento dell'Inventario.** 
L'obiettivo di questo livello è mappare la realtà cruda del monorepo, definendo esattamente cosa esiste e isolando la spazzatura locale da ciò che deve essere tracciato su Git.

---

## 2. Il Contenuto

### A. Mappatura Atomica dei "Sensori Spenti" (Tipo 3)
Queste cartelle sono destinate ad accogliere i record macchina delle esecuzioni, ma ad oggi contengono 0 file:
1. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/architectures/` (0 file) - Dovrebbe archiviare la struttura dei grafi dei workflow eseguiti.
2. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/brainstorms/` (0 file) - Dovrebbe contenere le trascrizioni dei passaggi chiave.
3. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/checkpoints/` (0 file) - Dovrebbe registrare gli stati intermedi per la ripresa.
4. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/decisions/` (0 file) - Registro decisionale macchina.
5. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/errors/` (0 file) - Tracciamento ed escalation dei crash.
6. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/feedback/` (0 file) - Valutazioni e audit umani.
7. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/metrics/` (0 file) - KPI quantitativi registrati via script.
8. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/performances/` (0 file) - Tempi di esecuzione e telemetria.
9. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/plans/` (0 file) - Piani dinamici generati sul momento.
10. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/reasoning-bank/` (0 file) - Ragionamenti complessi archiviati.
11. `WORKFLOW-ESTATE/02-AUTOMAZIONI-E-SCRIPTS/sessions/` (0 file) - Log cronologici delle sessioni operative.
12. `company/Memory/tasks/01-agency/` ... `10-memory/` (10 cartelle, 0 file totali) - TODO list macchina mai valorizzate.

### B. Stato Reale dei 6 Gate Estate (2026-07-24)
- **Gate-DEC:** 🔴 **NON CONFORME** - Nessun file macchina `.json` registra l'attivazione della decisione `dec_001_attiva`.
- **Gate-FUNNEL:** 🔴 **NON CONFORME** - Stripe placeholder presenti in `manuale.html`. Nessun link di checkout reale configurato.
- **Gate-CONTATTI:** 🔴 **NON CONFORME** - Mancanza di un'evidenza macchina collegata al file `lead.csv`.
- **Gate-S4 (Mentalità Brutale):** ⏳ **STANDBY** - Esecuzione bloccata, la pipeline non è autonoma al 100%.
- **Gate-S5 (YouTube):** ⏳ **STANDBY** - `FLIKI_API_KEY` vuota. Il processo non è in grado di invocare il rendering del competitor "Dose Mentale".
- **Gate-REV:** ⏳ **STANDBY** - `anticipi_chiusi = 0`.

---

## 3. Gate di Passaggio 1→2

Il passaggio al Livello 2 è consentito solo se si soddisfano i seguenti criteri oggettivi:
1. **Aggiornamento di `.gitignore`:** Presenza di righe esplicite che bloccano il push di `EmpireDesk/chrome-profile/` e di qualsiasi cartella temporanea locale (`dist/`, `.venv/`, `node_modules/`).
2. **Esecuzione di `empire conform WORKFLOW-ESTATE`:** Deve restituire `0` blocchi bloccanti.
3. **Censimento approvato:** Il comando `python -m empire.registry.cli census` non deve produrre file orfani non dichiarati nel registro.

*Cosa fare in caso di fallimento:* Se un file orfano viene rilevato, l'esecuzione di qualunque script di automazione si arresta sollevando un'eccezione di tipo `RegistryComplianceError` e registrando l'evento nel log locale di sicurezza.

---

## 4. Autocritica del Piano 1
- **Cosa ho migliorato:** Ho mappato analiticamente i sensori spenti del Tipo 3 e formalizzato lo stato reale dei gate, introducendo una regola rigida di arresto se la compliance del registro fallisce.
- **Cosa manca ancora:** Questo livello descrive solo l'inventario; non attiva la scrittura dei log né risolve la telemetria spenta (questo è compito del Livello 2).
- **SCORE:** **9.0 / 10** (Struttura chiara, additiva, aderente al vincolo sovrano).

---
⛓️ Trace P12: `RISTR-PIANO-01#fondamenta` · fonte: CP-20260724-002 · migliorato da: [RISTRUTTURAZIONE-02-TRACCIABILITA.md](RISTRUTTURAZIONE-02-TRACCIABILITA.md)
