---
Type: REGOLE
Status: Active
Tags: #regole #non-negoziabili #ricerca #lead #intelligence #A1
Created: 2026-06-22
Last updated: 2026-06-22
---

# Regole Non Negoziabili — A1 Ricerca & Market Intelligence

> Queste regole non hanno eccezioni. Se una situazione sembra richiedere di violarle,
> la risposta è escalation, non violazione.

---

## R1 — Questo reparto NON riscrive lo scraper runtime (ADR-003)

Lo scraper multi-fonte, `extractor.py`, `qualifier.py`, `competitor.py`, `cro_audit.py`
vivono in `Outreach/Outreach Workflow/` e sono il runtime live. A1 li WRAPPA: li invoca,
ne legge/scrive lo stato, ne documenta input/output, ne parametrizza l'esecuzione.

Nessun agente di A1 riscrive, sostituisce o forka il runtime live. Una modifica al runtime
si propone solo via ADR esplicito approvato, mai in silenzio dentro un task di sourcing.

**Perché esiste questa regola:** il runtime è in produzione e alimenta l'outreach reale.
Una riscrittura non coordinata rompe la pipeline revenue senza che nessuno la presidi.

---

## R2 — Nessuno scraping di nicchia nuova senza ICP esplicito

Prima che AG-A1-SCRAPE parta su una nicchia non ancora coperta, deve esistere un profilo ICP
in `agency/a1/icp` prodotto da AG-A1-ICP (skill `icp-radar`). L'ICP definisce target, fonti,
soglia di qualifica.

AG-A1-COORD blocca l'avvio di una run su nicchia nuova priva di ICP. Nicchia già coperta →
si riusa l'ICP esistente (e si valuta se aggiornarlo).

**Perché esiste questa regola:** scrappare senza ICP produce volume non qualificabile.
AG-A1-QUAL non ha un metro contro cui scorare e il gate diventa arbitrario.

---

## R3 — AG-A1-QA è bloccante su tutti gli output del reparto

Nessun lead entra in leads.db, nessun report intel esce verso 08-INTELLIGENCE, nessun dossier
pre-call va ad A8 senza gate verde di AG-A1-QA. Il gate non ha deroga per urgenza.

Soglie del gate:
- **Sourcing:** completezza dati ≥80%, no duplicati, GDPR-light rispettato.
- **Intel:** fonti citate e verificabili, nessuna metrica inventata.
- **Brief:** nessun campo vuoto, dossier consegnato prima della call.

Se A2/A3/A8 ha urgenza → AG-A1-COORD può consegnare output parziale con nota di rischio
esplicita SOLO con approvazione di AG-DIR. AG-A1-QA documenta il bypass non autorizzato se avviene.

---

## R4 — Nessuna metrica inventata (Mandato Art.2)

Ogni claim su mercato, ICP, competitor, trend cita la fonte (URL, dataset, skill). Un report
con "conversione media nicchia 4%" senza fonte è una violazione automatica. La risposta corretta
in assenza di dato è `[DM]` (Da Misurare) + il motivo, non un numero plausibile.

AG-A1-QA verifica il campo `fonti[]` su ogni report. Vuoto o non verificabile = FAIL.
Committente interno che chiede una previsione di mercato senza dato → risposta: "non abbiamo
la fonte; possiamo dichiarare il segnale qualitativo, non il numero."

---

## R5 — GDPR-light e dedup obbligatori prima dello store

Prima di inserire un lead in leads.db / `agency/leads`:
- **Dedup:** `memory_search` su `agency/leads` per evitare duplicati (stesso dominio/email).
- **GDPR-light:** solo dati business pubblici (email aziendale, telefono pubblico, sito);
  nessun dato personale sensibile; rispetto delle fonti che vietano lo scraping.

AG-A1-QA blocca lo store se il dedup non è stato eseguito o se i dati violano la GDPR-light.

---

## R6 — Il dossier pre-call rispetta la SLA delle 2 ore

Il dossier per la discovery call di A8 si consegna ≥2h prima della call. Un dossier completo
ma in ritardo è un dossier mancato: il closer non ha tempo di studiarlo. AG-A1-BRIEF prioritizza
le richieste pre-call sopra le run di sourcing schedulate quando la SLA è a rischio.

**Eccezione unica:** call fissata con <2h di preavviso → AG-A1-BRIEF consegna il dossier "best
effort" disponibile + dichiara esplicitamente cosa manca. Non è un bypass del gate: è trasparenza.

---

## R7 — Lo scarto lead porta sempre un motivo

Nessun lead viene scartato in silenzio. AG-A1-QUAL registra il motivo (fuori ICP, dati
incompleti, settore escluso, duplicato, freschezza) in `agency/reasoning`. Lo scarto senza
motivo butta il learning insieme al lead e impedisce la calibrazione dell'ICP.

---

## Connessioni

- [[PRINCIPI]] · `principi/PRINCIPI.md` — il "perché" di queste regole
- [[ag-a1-qa]] · `agenti/ag-a1-qa.md` — esecutore dei gate R3/R4/R5
- [[ARCHITETTURA]] · `ARCHITETTURA.md §4` — i gate del reparto in dettaglio
- [[01-ECOSISTEMA-AGENCY-V2]] · Mandato Art.2 + ADR-003 come fonte di R1 e R4
