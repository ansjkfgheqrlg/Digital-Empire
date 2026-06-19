---
Type: SKILLS
Status: Active
Tags: #skills #analytics #ottimizzazione #pattern-library #L2.4
Created: 2026-06-18
Last updated: 2026-06-18
---

# Skill del Reparto — L2.4 Analytics & Ottimizzazione

> **Reparto:** L2.4 · **Ecosistema:** 04-MARKETING · **Versione:** v2

---

## Skill proprie (da forgiare via 07-FORGE)

### `copy-performance-loop` — P1

**Cosa fa:** Codifica il loop §4b del dossier v2 come skill eseguibile:
diagnosi per sezione APSOC da dati di performance, scrittura del risultato
(pattern o antipattern) nella ReasoningBank, richiesta di revisione mirata
a COPY-MASTER. La skill è il "motore" del WF-OPTIMIZATION-LOOP in forma
eseguibile da agente.

**Owner:** AN4 (usa la skill); AN-LEAD (coordina)
**Namespace output:** `marketing/copy/patterns/{icp}` e `marketing/copy/antipatterns/{icp}`
**Priorità build:** P1 — abilita il loop auto-migliorante del sistema
**Via:** 07-FORGE — PRD → architettura → build (standard §8 piano V2)

**Input:** diagnosi AN2/AN5 strutturata + verdetto AN3 (se disponibile)
**Output:** pattern/antipattern scritto nel namespace + notifica ad AN-LEAD

---

### `icp-pattern-library` — P1

**Cosa fa:** Lettura e scrittura strutturata dei pattern vincenti per ICP.
Schema standard: `{icp, formato, sezione_apsoc, pattern, evidenza, data_consolidamento}`.
Funzioni: `read_patterns(icp, formato, sezione)`, `write_pattern(pattern_obj)`,
`list_patterns(icp)`, `check_antipattern(icp, formato, sezione)`.
Il COPY-MASTER usa questa skill per interrogare la ReasoningBank prima di scrivere.

**Owner:** AN4 (scrive); COPY-MASTER in L2.1 (legge)
**Namespace:** `marketing/copy/patterns/{icp}` e `marketing/copy/antipatterns/{icp}`
**Priorità build:** P1 — interconnessa con `copy-performance-loop`
**Via:** 07-FORGE — stesso batch della `copy-performance-loop`

---

## Skill esistenti mappate a questo reparto

| Skill | Reparto/Funzione | Come viene usata |
|---|---|---|
| `ab-testing` | L2.4 / WF-AB-TEST | AN3 usa questa skill come motore del disegno esperimenti; codifica il calcolo campione e il protocollo di verdetto |
| `analytics` | L2.4 / WF-TRACKING-SETUP | AN1 usa questa skill per il tracking plan; motore della specifica tecnica UTM + eventi |
| `market-audit` | L2.4 / AN-OBSERVER | Ausiliaria per il report KPI ecosistema prodotto da AN-OBSERVER per il CMO |
| `market-report` | L2.4 / AN-OBSERVER | Ausiliaria del report periodico; `market-report-pdf` per output stampabile CMO |

**Regola anti-contraddizione (§6 dossier v2):** prima di forgiare `copy-performance-loop`
e `icp-pattern-library`, AN-LEAD esegue `skill-contradiction-analyzer` contro le esistenti
(in particolare contro `cro-copy-architect` e `analytics`). Le nuove skill devono
complementare, non sovrapporre.

---

## Connessioni

- [[WF-OPTIMIZATION-LOOP]] · `workflow/WF-OPTIMIZATION-LOOP.md` — usa `copy-performance-loop`
- [[WF-AB-TEST]] · `workflow/WF-AB-TEST.md` — usa `ab-testing`
- [[WF-TRACKING-SETUP]] · `workflow/WF-TRACKING-SETUP.md` — usa `analytics`
- [[04-ECOSISTEMA-MARKETING-V2]] · `PIANO-MAESTRO/04-ECOSISTEMA-MARKETING-V2.md §5-6`
