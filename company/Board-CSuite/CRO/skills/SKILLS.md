---
Type: CONCEPT
Status: Active
Tags: #skills #cro #deal-desk #forecast #pricing
Created: 2026-06-17
Last updated: 2026-06-17
---

# SKILLS — CRO (Chief Revenue Officer)

> Le skill proprie del team CRO. Distinte dalle skill dell'ecosistema Agency (che il CRO usa
> ma non possiede). Forgiate per il presidio del revenue a livello di Board C-Suite.
> Blueprint: `company/Board-CSuite/_BLUEPRINT/BP-CRO.md` §Skill proprie.

---

## SKILL-CRO-001 — deal-desk

**Owner:** `cro-deal-desk`
**Tipo:** skill procedurale bloccante
**Dipende da:** skill `proposal-gate` (Agency A3), skill `discovery-call-brief` (Agency A3)

### Descrizione
Struttura ogni offerta commerciale dell'Agency applicando i criteri del catalogo fisso e
il gate bloccante di qualità. La skill integra il brief discovery con la selezione prodotto
e produce la struttura dell'offerta (non il testo: quello è A3-PROP).

### Algoritmo

1. **Input:** brief discovery JSON (da A3-BRIEF) + prodotto proposto.
2. **Selezione prodotto:**
   - Problema = acquisizione lead → Outreach Factory €4.000.
   - Problema = produzione contenuti → Content Factory €3.500.
   - Problema = knowledge management → Second Brain €2.500.
   - Tutti e 3 i problemi + budget confermato → Engine Room €8.000.
   - Incerto: chiedi chiarimento, non procedere.
3. **Verifica prerequisiti ambiente** — server del cliente compatibile? Se non verificato: STOP.
4. **Esegui proposal-gate** — 8 check sequenziali. FAIL su qualsiasi check = output FAIL con lista.
5. **Output:** struttura offerta approvata + gate result PASS/FAIL.

### Trigger di attivazione
- Ogni volta che un lead avanza a stadio "preventivo" nel WF-DEAL.
- Mai bypassabile: anche un deal "urgente" passa dal gate.

### Skill di supporto richiamate
- `proposal-gate` — checklist bloccante 8 punti (skill Agency)
- `discovery-call-brief` — struttura del brief in input (skill Agency)

---

## SKILL-CRO-002 — revenue-forecast

**Owner:** `cro-forecast-analyst`
**Tipo:** skill analitica (output: documento trimestrale)
**Dipende da:** dati da `cro-pipeline-health`, `cro-infobusiness-launches`, `cro-retention-revenue`

### Descrizione
Produce il forecast revenue trimestrale disaggregato per fonte, con 3 scenari e zero numeri
inventati. Ogni voce è classificata (certa/probabile/possibile) o marcata [DM].

### Algoritmo

1. **Raccolta dati:** input JSON da tutte e 3 le fonti. Se una fonte manca: nota [DM] + prosegui.
2. **Classificazione voci:**
   - Certa: contratto firmato O lancio con data e prezzo definitivi E lista acquirenti confirmata.
   - Probabile: deal >50% atteso O lancio pianificato con prezzo definito.
   - Possibile: deal <50% O lancio senza prezzo O segnale debole.
3. **Calcolo scenari:**
   - Pessimistico: sole voci certe.
   - Base: certe + probabili (weighted 80%).
   - Ottimistico: tutto il pipeline a chiusura piena.
4. **Identificazione rischi:** ogni voce non-certa con nota rischio esplicita.
5. **Produzione priorità:** 3-5 azioni ad alto impatto revenue per il trimestre, ordinate per impatto.
6. **Confronto trimestre precedente:** scostamento % + causa se >20%.
7. **Output:** documento forecast JSON + sintesi narrativa 5 righe per il CEO.

### Vincolo non negoziabile
Nessun numero nel documento finale senza fonte documentata O tag [DM] con motivazione.
Qualsiasi voce ambigua va in pessimistico o esclusa, mai arrotondata verso l'alto.

---

## SKILL-CRO-003 — pricing-arbiter

**Owner:** `cro-pricing-arbiter`
**Tipo:** skill di gate bloccante
**Dipende da:** catalogo corrente in `board/cro/pricing/catalogo-corrente.json`

### Descrizione
Verifica in tempo reale che il prezzo di qualsiasi offerta o lancio sia conforme al catalogo
fisso. Blocca qualsiasi variazione non autorizzata e avvia l'iter B-003 se necessario.

### Algoritmo

1. **Input:** prodotto + prezzo proposto.
2. **Lookup catalogo:** legge `catalogo-corrente.json` (versione attiva).
3. **Confronto:**
   - Prezzo proposto = prezzo catalogo → PASS_CATALOGO (nessuna ulteriore elaborazione).
   - Prezzo proposto ≠ prezzo catalogo → BLOCCA_SCONTO.
4. **Se BLOCCA_SCONTO:**
   a. Propone 2+ alternative al ribasso di prezzo (supporto esteso, bundle upgrade, dilazione).
   b. Se alternativa accettata: deal prosegue a prezzo catalogo.
   c. Se alternativa rifiutata e deal strategico: avvia istruttoria B-003.
5. **Istruttoria B-003:**
   a. Raccoglie: prodotto, delta prezzo, motivo prospect, tipo cliente, storia acquisti.
   b. Stima impatto margine ([DM] se non quantificabile).
   c. Produce dossier per il lotto.
6. **Attende ok lotto:** MAXIMILIAN o CEO. Nessuna variazione esce senza firma.
7. **Se approvato:** aggiorna catalogo (nuova versione), archivia in `cro-memoria`, notifica nodi.
8. **Output:** PASS_CATALOGO | ALTERNATIVA_ACCETTATA | APPROVATO_LOTTO | RIGETTATO.

### Vincolo non negoziabile
Il catalogo attivo è immutabile senza approvazione lotto documentata. Ogni versione è archiviata
prima di essere sostituita. Mai due versioni "attive" contemporaneamente.

---

## Skill di Supporto Richiamate (da Agency)

Il team CRO richiama — ma non possiede — le seguenti skill forgiate in 01-AGENCY:

| Skill | Owner Agency | Uso nel CRO |
|---|---|---|
| `proposal-gate` | A3-QA | Eseguita da `cro-deal-desk` come gate WF-DEAL |
| `discovery-call-brief` | A3-BRIEF | Input obbligatorio per `cro-deal-desk` |
| `outreach-reply-triage` | A2-TRIAGE | Usata da `cro-agency-pipeline` per classificare risposte |
| `case-study-forge` | A6-CASE | Usata da `cro-retention-revenue` per win-back con prove |

---

## Connessioni

- [[cro-deal-desk]] · `agenti/cro-deal-desk.md`
- [[cro-forecast-analyst]] · `agenti/cro-forecast-analyst.md`
- [[cro-pricing-arbiter]] · `agenti/cro-pricing-arbiter.md`
- [[BP-CRO]] · `company/Board-CSuite/_BLUEPRINT/BP-CRO.md` §Skill proprie
- [[WF-DEAL]] · `workflow/WF-DEAL.md`
- [[WF-FORECAST]] · `workflow/WF-FORECAST.md`
- [[WF-PRICING]] · `workflow/WF-PRICING.md`
