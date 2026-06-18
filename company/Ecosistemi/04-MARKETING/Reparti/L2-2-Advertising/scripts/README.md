---
Type: CONCEPT
Status: Active
Tags: #scripts #advertising #automation #L2-2
Created: 2026-06-18
Last updated: 2026-06-18
---

# SCRIPTS — L2.2 Advertising

> Script target V2 deterministici per il reparto. Tutti i script sono **deterministici**:
> stesso input → stesso output. Nessuno script lancia campagne reali: producono output
> testabili in dry-run prima di qualsiasi uso in produzione.

---

## Script 1 — `audience-builder.py`

**Scopo:** costruisce il brief audience strutturato per piattaforma dato un ICP e i dati
da 08-INTELLIGENCE. Automatizza il passo 1-2 di AD1 (Audience Analyst).

**Input:** `{icp_id, piattaforme[], intelligence_data{}, awareness_level}`
**Output:** `audience_brief.json` con segmenti, lookalike brief, budget split consigliato,
note di esclusione — pronto per AD2 e AD5.

**Deterministico:** stessa ICP + stessi dati intelligence → stesso brief audience.
Non accede alle piattaforme. Non richiede credenziali API.

**Stato:** target V2 — da forgiare in V2-6 dal reparto FORGE, sulla base di questo spec.

---

## Script 2 — `creative-matrix.py`

**Scopo:** genera la matrice copy × visual × audience e produce le specifiche per ogni
creative nella matrice. Automatizza la fase di design di AD2.

**Input:** `{copy_varianti[], visual_asset[], segmenti_audience[], budget_test, criterio_priorità}`
**Output:** `creative_matrix.json` con N creative complete (copy_id + visual_id + audience_id),
budget per variante, ordine di priorità per test, flag per fan-out swarm se N > 4.

**Deterministico:** stessa matrice input → stesso ordine output.
Gestisce il caso "budget limitato": riduce automaticamente la matrice al numero di varianti
finanziabili secondo la soglia AN3, con nota esplicita sulle varianti escluse.

**Stato:** target V2 — da forgiare in V2-6.

---

## Script 3 — `compliance-preflight.py`

**Scopo:** esegue il check di compliance automatizzato (AD4) su una lista di creative
per una o più piattaforme. Produce il report G3 in formato JSON.

**Input:** `{creative[], piattaforme[], categoria_prodotto}`
**Output:** `compliance_report.json` con per ogni creative: esito per piattaforma (PASS/FAIL),
elementi verificati, fail bloccanti con estratto + regola + correzione richiesta.

**Deterministico:** stesso input → stesso report (regole di compliance codificate come costanti,
non come ragionamento LLM libero). Quando le policy cambiano: si aggiornano le costanti dello script.

**Stato:** target V2 — da forgiare in V2-6.

---

## Note di build

Tutti e tre gli script target seguono il pattern V2 per i deterministici:
1. Nessuna dipendenza da API di piattaforma in fase di test (dry-run puro)
2. Input e output JSON strutturati (schema validato)
3. Testabili con fixture statiche senza credenziali
4. Log di ogni esecuzione in `marketing/ads/experiments/{campaign_id}/`

Build order: `audience-builder` (dipende solo da dati interni) → `creative-matrix`
(dipende da audience-builder) → `compliance-preflight` (indipendente, parallelizzabile).

---

## Connessioni

- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §L2.2`
- [[ad1-audience-analyst]] · `agenti/ad1-audience-analyst.md`
- [[ad2-creative-iterator]] · `agenti/ad2-creative-iterator.md`
- [[ad4-compliance-checker]] · `agenti/ad4-compliance-checker.md`
