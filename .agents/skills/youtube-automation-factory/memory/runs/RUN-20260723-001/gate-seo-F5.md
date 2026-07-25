# seo-gate — Verdetto F5 (Pubblicazione) — RUN-20260723-001

## Ricalcolo indipendente
`python scripts/seo_score.py --json metadati-F5.json` → **100.0/100** (title 25, description 25,
tags 20, thumbnail 15, subtitles 15, 0 note). Ricalcolato ora dal gate, non ereditato dal
metadata-optimizer (evita di fidarsi di un numero gonfiato).

## Checklist
- [x] **Titolo**: keyword "installare Claude Code" presente, 56 caratteri (dentro 20-70), coerente
  col contenuto reale del video.
- [x] **Descrizione**: prime righe con hook+valore, keyword presente, link+CTA presenti (Manuale +
  iscrizione), >200 caratteri.
- [x] **Tag**: 10 tag rilevanti, keyword principale tra i tag, presi dalla lista SEO già preparata
  da Gemini per "Setup & Terminale" (`04_TEMPLATE_DESCRIZIONE_SEO.md`).
- [x] **Miniatura**: brief presente e chiaro (`brief-miniatura-F5.md`), differenziale dichiarato
  rispetto al cluster.
- [x] **Sottotitoli**: ON (dichiarato in produzione-spec-F4.md e nei metadati).
- [x] **Punteggio ≥70 E ≥ punteggio del target**: 100 ≥ 70. Non esiste un punteggio del "target"
  da battere in questo run (F2 adattata, nessun video singolo replicato — vedi candidati-video-F2.md)
  → criterio soddisfatto per costruzione (non c'è un avversario da superare, solo la soglia).

## Verdetto: ✅ **PASS**

## ⚠️ Cosa NON è coperto da questo PASS (onestà, non è una pubblicazione reale)
Questo gate certifica i **metadati**. Non certifica:
- Il file video (non renderizzato — `qa-audio-video` resta `na`, F4).
- La miniatura vera (non renderizzata — `thumbnail_analyzer.py` non eseguito, F5).
- La pubblicazione reale (G-B3 bloccata da M-EST-8, canale YouTube non ancora designato da Max).

**Il flusso si ferma qui per design** (istruzione esplicita del run): tutto ciò che serve per
pubblicare è pronto e verificato, manca solo (a) il render umano in Fliki, (b) il canale/
credenziali YouTube.

Non si procede a "PUBBLICA". RIPRESA DA: quando Max decide il canale (M-EST-8), eseguire il render
reale, poi `qa-audio-video` + `thumbnail_analyzer.py` su file reali, poi pubblicare, poi F6
(performance-auditor).