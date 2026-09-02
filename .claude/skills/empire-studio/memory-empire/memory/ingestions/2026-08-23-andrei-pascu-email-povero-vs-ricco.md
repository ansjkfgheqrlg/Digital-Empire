# Ingestion Report — Stage H
## fGpz-uOgr4k — email marketing povero, email marketing ricco

**Data:** 2026-08-23
**Run:** andrei-pascu-001/cat1-copywriting
**Video #:** 13/29 cat1
**WATCH-001:** N_video=13 = N_MemoryEmpire=13 → MATCH ✅

---

## Pipeline Completata

| Stage | Status | Dettagli |
|-------|--------|---------|
| 1 — yt_ingest | ✅ | 29s, 0 capitoli, 1 sub IT |
| 2 — frame_extractor | ✅ | 15 frame @2s |
| 3 — VISIONE nativa | ✅ | 15/15 frame letti (coverage 100%), NO-FINTO PASS |
| 4 — atoms | ✅ | 4 KA, 1 sezione |
| 5 — verifica | ✅ | PASS (con caveat esplicito su attribuzione riga-personaggio) |
| 7 — wiki | ✅ | 1 pagina Source nuova (nessun Concept: riciclo, non novità) + index.md + log.md |
| C — archive | ✅ | 4 file in knowledge/fGpz-uOgr4k/ |
| D — enrichment | ✅ | Nessuna azione skill nuova (già coperto dai video 11-12), 1 idea formato segnalata |
| E — gate | ✅ | PASS |
| F — apply | ✅ | Nessuna azione richiesta |
| G — audit | ✅ | Lacune documentate (overlay "outEmail" non identificato) |
| H — questo file | ✅ | Stage H report |

---

## Top KA

1. **KA-04** `frame-010` — Personalizzazione: nome a metà frase come domanda diretta + promessa numerata + chiusura storytelling.
2. **KA-01** `frame-001` — Sconto generico vs hook di personalità diretto.
3. **KA-03** `frame-006` — Doppio esempio urgency clichè ("offerta imperdibile", "ultima possibilità").
4. **KA-02** `frame-003` — Welcome email debole/burocratica.

---

## Nota su enrichment

Nessuna skill patchata in questa ingestione: tutti i pattern del video erano già coperti dalle
patch applicate ai video 11 (`cro-copy-architect`) e 12 (`emails`). Patchare di nuovo sarebbe
ridondante — la disciplina "non duplicare enrichment già fatto" vale quanto "fare enrichment
reale quando c'è qualcosa di nuovo".

**Idea segnalata (non implementata)**: il formato stesso (split-screen comparativo con badge
fatturato) è un pattern di contenuto virale riusabile per contenuti DE (carousel-empire, Reels
agenzia) — proposta per valutazione futura, fuori scope di questa ingestione.

---

## Wiki Pages Create

- `second-brain-vault/wiki/sources/Source_Andrei_Pascu_Email_Povero_Vs_Ricco.md`

---

## Brands Analizzati

Nessuno — contenuto interamente esemplificativo/parodico, esempi inventati per illustrare il contrasto.

---

## Note Speciali

- Overlay finale "outEmail" (0:28) non identificato con certezza — possibile brand/tool, segnalato DA VERIFICARE.
- Attribuzione riga-per-personaggio (povero/ricco) esplicitamente non confermata, per assenza di caption on-screen e impossibilità di distinguere il parlante dai soli frame statici a 2s di intervallo.
- Video 13/29 chiude la sessione di ingestione single-thread. Da qui in avanti (video 14+) la
  missione procede in batch paralleli di agenti (approvato da Max), con serializzazione degli
  aggiornamenti condivisi (tracker/wiki-index/checkpoint) a cura del conduttore per evitare le
  collisioni già osservate in questa sessione (CP-20260823-004).
