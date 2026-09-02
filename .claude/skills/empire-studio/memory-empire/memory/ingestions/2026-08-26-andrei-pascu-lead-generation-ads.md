# Ingestion Report — Stage H
## 8Pf7d57Q0Jk — Come generare contatti con le ads (lead generation)

**Data:** 2026-08-26
**Run:** andrei-pascu-001/cat2-marketing
**Video #:** 3/15 cat2
**WATCH-001:** N_video cat2=3 = N_MemoryEmpire cat2=3 → MATCH ✅

---

## Pipeline Completata

| Stage | Status | Dettagli |
|-------|--------|---------|
| 1 — yt_ingest | ✅ | 838s, 0 capitoli, 1 sub IT, nessun errore |
| 2 — frame_extractor | ✅ | 419 frame @2s, 3-digit naming |
| 3 — VISIONE nativa | ✅ | 10/419 frame letti (campionamento dichiarato), VTT dedup letto per intero, NO-FINTO PASS |
| 4 — atoms | ✅ | 14 KA, 13 sezioni — il video più denso di cat2 finora |
| 5 — verifica | ✅ | PASS |
| 7 — wiki | ✅ | 1 pagina Source nuova + index.md + log.md aggiornati |
| C — archive | ✅ | 4 file in knowledge/8Pf7d57Q0Jk/ |
| D — enrichment | ✅ | 5 connessioni KB (4 gap con patch, 1 conferma) |
| E — gate | ✅ | PASS |
| F — apply | ✅ | 3 patch reali applicate (ads/SKILL.md, ads/audience-targeting.md, lead-magnets/SKILL.md) |
| G — audit | ✅ | Timestamp stimati dichiarati esplicitamente, dati non verificati marcati |
| H — questo file | ✅ | Stage H report |

---

## Top KA

1. **KA-04** — Framework 3 categorie ads: Esperimento / Evolvo / Awareness.
2. **KA-07/08** — Targeting content-based (creativa che targetizza) + scaling con variabili nel hook.
3. **KA-10** — Criterio di spegnimento ad = ritorno, mai spesa nominale fissa.
4. **KA-14** — Lead magnet problema adiacente + feedback loop di fiducia.

---

## Azione concreta eseguita (non solo proposta)

3 patch reali applicate in questa sessione (record del run per numero di patch in un solo video):
1. `C:\Users\Utente\.claude\skills\ads\SKILL.md` — sezione "3-Tier Campaign Lifecycle".
2. `C:\Users\Utente\.claude\skills\ads\references\audience-targeting.md` — sezione "Content-Based Targeting".
3. `C:\Users\Utente\.claude\skills\lead-magnets\SKILL.md` — sotto-principio "problema adiacente" nel Principio 4.

Tutte con fonte dichiarata esplicitamente nel testo (caso studio singolo, video reale) per permettere verifica/correzione futura.

---

## Wiki Pages Create

- `second-brain-vault/wiki/sources/Source_Andrei_Pascu_Lead_Generation_Ads.md`

---

## Nuovi Concetti Wiki

Nessuno — contenuto integrato come patch a skill esistenti (`ads`, `lead-magnets`).

---

## Brands Analizzati

- Vasco (cliente reale, servizi marketing fotovoltaico) — dati reali condivisi.
- Competitor generico di Vasco, menzionato ma non mostrato ("non posso fartelo vedere") — non descritto nei KA per rispetto NO-FINTO.

---

## Note Speciali

- Primo video del run con VTT processato via script python di dedup locale (invece di 4 letture paginate raw) — riduzione costo significativa, timestamp dei KA quindi stimati (dichiarato esplicitamente in ogni file per trasparenza P12).
- Doppio setup di ripresa: consulenza vera (ambiente domestico, cuffie da chiamata) + intro/outro in studio standard del canale (coerente col pattern osservato in altri video del run con setup multipli).
