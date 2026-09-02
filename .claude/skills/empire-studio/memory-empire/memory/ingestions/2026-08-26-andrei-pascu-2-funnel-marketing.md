# Ingestion Report — Stage H
## VYyIF1r6tkw — The 2 most used funnels in social marketing

**Data:** 2026-08-26
**Run:** andrei-pascu-001/cat2-marketing
**Video #:** 1/cat2 (primo video Livello 2, dopo conferma Max)
**WATCH-001:** N_video cat2=1 = N_MemoryEmpire cat2=1 → MATCH ✅

---

## Pipeline Completata

| Stage | Status | Dettagli |
|-------|--------|---------|
| 1 — yt_ingest | ✅ | ingest.json scritto ok; print finale titolo ha lanciato UnicodeEncodeError non bloccante (console cp1252) |
| 2 — frame_extractor | ✅ | 168 frame @2s, 3-digit naming |
| 3 — VISIONE nativa | ✅ | 10/168 frame letti (campionamento dichiarato, video sotto soglia coverage-100%), VTT integrale letto per intero, NO-FINTO PASS |
| 4 — atoms | ✅ | 9 KA, 8 sezioni |
| 5 — verifica | ✅ | PASS |
| 7 — wiki | ✅ | 1 pagina Source nuova + index.md + log.md aggiornati |
| C — archive | ✅ | 4 file in knowledge/VYyIF1r6tkw/ |
| D — enrichment | ✅ | 3 connessioni KB (2 conferme, 1 gap/proposta) |
| E — gate | ✅ | PASS |
| F — apply | ✅ (nessuna patch necessaria) | Contenuto già coperto da `funnel-designer` esistente, gap unico registrato come proposta |
| G — audit | ✅ | Nessuna incertezza sui dati, cross-ref primo tocco della skill funnel-designer |
| H — questo file | ✅ | Stage H report |

---

## Top KA

1. **KA-04/05** `frame-040` — Calcolo margine marketing + introduzione ROAS con esempio numerico (cubo €15).
2. **KA-06/07** `frame-060/080` — Definizione operativa funnel vendita diretta vs funnel di contatti.
3. **KA-08** `frame-100` — Diagnosi: funnel di contatti come possibile "red flag"/stampella per prodotto o copy debole.
4. **KA-09** `frame-140` — Criteri di scelta funnel per soglia di prezzo + trade-off operativo.

---

## Azione concreta eseguita

**Nessuna patch applicata.** I concetti quantitativi (ROAS, soglie di prezzo funnel corto/lungo) sono già coperti in modo più dettagliato dalla skill esistente `copy-workflow/skills/funnel-designer` (references/funnel-economics.md + SKILL.md righe 74-113) — verificato, nessuna azione necessaria.

**Proposta non ancora eseguita (richiede seconda conferma indipendente, regola anti-overfitting):**
- Aggiungere un segnale diagnostico "funnel di contatti usato per compensare prodotto/copy debole" nella sezione "Segnali di Funnel Rotto" di `funnel-economics.md` — fonte singola (questo video), non ancora patchato.

---

## Wiki Pages Create

- `second-brain-vault/wiki/sources/Source_Andrei_Pascu_2_Funnel_Marketing.md`

---

## Nuovi Concetti Wiki

Nessuno — primo video di cat2, contenuto già coperto dalla skill `funnel-designer` esistente. Nessuna pagina Concept nuova giustificata.

---

## Brands Analizzati

Nessuno — solo esempi didattici generici (cubo, magliette e-commerce, vendita case, corso proprio citato come esempio prezzo).

---

## Note Speciali

- Primo video del run FUORI da cat1-copywriting — primo contenuto di marketing/funnel strategico invece che copywriting tecnico puro.
- Prima connessione diretta con la skill `copy-workflow/skills/funnel-designer`, mai toccata prima nel run.
- Nessuna tensione rilevata con skill esistenti in questo video (a differenza del video 24 cat1 con `beast-preventivi`, ancora aperta con Max).
