---
Type: CONCEPT
Status: Active
Tags: #cto #scripts #automazione #verify #report
Created: 2026-06-17
Last updated: 2026-06-17
---

# SCRIPTS — Script Tecnici della Figura CTO

> Connessioni: [[SKILLS]] · [[cto-quality-gate]] · [[cto-security-sentinel]] · [[cto-tech-debt-tracker]]

---

## Nota metodologica

Gli script descritti qui sono tool di supporto per la figura CTO: automatizzano operazioni
ripetitive (verifica struttura, report debito, log sicurezza) senza richiedere l'attivazione
completa degli agenti. Sono script leggeri, non workflow completi. Status: da-sviluppare
(build in una sessione FORGE futura dopo la build delle skill primarie).

---

## SCR-001 — `verify_structure.sh`

**Status:** da-sviluppare
**Eseguito da:** `cto-quality-gate` (come parte di empire-verify) + manuale dal conductor

**Scopo:** Verifica che la struttura di `company/` rispecchi `PIANO-MAESTRO/`. Confronta
l'albero di cartelle atteso (derivato dal Piano Maestro) con quello reale. Produce una lista
di deviazioni: cartelle mancanti, cartelle extra non previste, file in posizioni errate.

**Output atteso:**
```
[OK] company/Board-CSuite/ — conforme
[OK] company/Board-CSuite/CEO-Empire-Conductor/ — conforme
[WARN] company/Board-CSuite/temp-work/ — cartella non prevista da PIANO-MAESTRO
[OK] company/Memory/ — conforme
Totale: 1 deviazione rilevata — vedere report struttura per dettagli
```

**Come funziona (logica):**
1. Legge la struttura attesa da `PIANO-MAESTRO/00-PIANO-MAESTRO.md` (o da un file di mapping).
2. Esegue un tree di `company/` (escludendo `node_modules`, `.git`, `*.bak`).
3. Confronta i due alberi.
4. Produce il report con le deviazioni.

**Frequenza:** prima di ogni deploy significativo; nel ciclo settimanale di WF-SECURITY-AUDIT.

---

## SCR-002 — `tech_debt_report.sh`

**Status:** da-sviluppare
**Eseguito da:** `cto-tech-debt-tracker` (report settimanale) + manuale dal conductor

**Scopo:** Legge `state/tech-debt-register.json` e produce un report human-readable del
debito tecnico corrente: n. item per gravità, trend rispetto alla settimana precedente,
top-5 per priorità con proposta di scheduling.

**Output atteso:**
```
=== TECH DEBT REPORT — 2026-06-17 ===
Totale item aperti: 12 (+3 rispetto a settimana scorsa)
  Critici: 0 | Alti: 3 | Medi: 7 | Bassi: 2
Trend: IN CRESCITA (3 item nuovi, 1 risolto)

TOP 5 PRIORITÀ:
1. [TD-021] landing-page-builder senza dry-run — ALTO — proposta: prossima sessione FORGE
2. [TD-007] bundle size >500KB su sito-crea-siti — MEDIO — proposta: sessione ottimizzazione
...
```

**Frequenza:** ogni lunedì; on-demand dal conductor.

---

## SCR-003 — `security_scan_report.py`

**Status:** da-sviluppare
**Eseguito da:** `cto-security-sentinel` (nel WF-SECURITY-AUDIT) + automatico se integrato

**Scopo:** Esegue una scansione rapida del repo per pattern di segreti comuni (API key,
token, password in variabili) e produce un report con le occorrenze trovate, la posizione
esatta (file:linea), e il tipo di segreto (oscurato nell'output per sicurezza).

**Pattern cercati (esempi non esaustivi):**
- `sk_[a-zA-Z0-9]{32,}` (API key format OpenAI-style)
- `ruf_[a-zA-Z0-9]{20,}` (Ruflo token format)
- `AKIA[A-Z0-9]{16}` (AWS access key)
- `password\s*=\s*["'][^"']{8,}` (password hardcoded)
- `Bearer [a-zA-Z0-9._-]{20,}` (JWT/Bearer token)

**Output:** lista findings con file, linea, tipo segreto oscurato.

**Frequenza:** nel WF-SECURITY-AUDIT periodico; pre-push hook (se configurato).

---

## SCR-004 — `lighthouse_batch.sh`

**Status:** da-sviluppare
**Eseguito da:** `cto-quality-gate` (come parte di empire-verify per sistemi web multipli)

**Scopo:** Esegue Lighthouse su una lista di URL (sistemi web della holding in staging o
produzione) e produce un report aggregato con i score di ognuno. Identifica i sistemi
sotto la soglia ≥90 per dashboard del conductor.

**Input:** lista URL dal `state/platform-status.json`.
**Output:** report tabellare con URL, score per dominio, delta vs. settimana scorsa.

**Frequenza:** settimanale post-audit; post-deploy significativo.

---

## SCR-005 — `adr_index_rebuild.sh`

**Status:** da-sviluppare
**Eseguito da:** `cto-memoria` (dopo ogni nuova scrittura ADR)

**Scopo:** Ricostruisce l'indice degli ADR tecnici in `company/Memory/decisions/`:
lista di tutti gli ADR con ID, titolo, data, stato (attivo/superato), sistemi impattati.
Utile per il RECALL rapido di `cto-memoria` e per il contraddiction check di `tech-adr`.

**Output:** `state/adr-index.json` aggiornato.

---

## Come Commissionare la Build a FORGE

Per ciascuno script, il `cto-forge-liaison` invia a FORGE un brief tecnico con:
- Scopo e output atteso (vedi sopra).
- Dipendenze permesse: bash/python standard (no librerie pesanti).
- Dry-run mode obbligatorio: ogni script deve avere un flag `--dry-run` che simula
  l'output senza scrivere file o lanciare processi pesanti.
- Acceptance criteria: output conforme al formato descritto + dry-run funzionante.

Priorità di build: SCR-001 (struttura) → SCR-002 (debito) → SCR-003 (security scan)
→ SCR-004 (lighthouse batch) → SCR-005 (adr index).

---

## Connessioni

- [[SKILLS]] · `skills/SKILLS.md`
- [[cto-quality-gate]] · `agenti/cto-quality-gate.md`
- [[cto-security-sentinel]] · `agenti/cto-security-sentinel.md`
- [[cto-tech-debt-tracker]] · `agenti/cto-tech-debt-tracker.md`
- [[cto-memoria]] · `agenti/cto-memoria.md`
- [[STATE]] · `state/README.md`
- [[BP-CTO]] · `company/Board-CSuite/_BLUEPRINT/BP-CTO.md`
