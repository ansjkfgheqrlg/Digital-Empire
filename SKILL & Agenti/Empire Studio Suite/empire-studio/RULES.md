# Empire Studio — RULES (checklist non negoziabili)

> Questo file è la **fonte di verità delle regole**.
> Ogni agente del verification-control-department lo legge prima di ogni verifica.
> Il Conductor lo legge a ogni session-init.
> Nessuna regola qui è negoziabile o opzionale.

---

## REGOLA 0 — SESSION INIT (PRIMA di qualsiasi azione)

Prima di avviare qualsiasi pipeline o rispondere all'utente su Empire Studio:

```
GATE SESSION-INIT:
□ Letto: company/Memory/INDEX.md
□ Letto: company/Memory/STATO-EMPIRE.md
□ Verificato: ADR attivi rispettati (nessuna contraddizione silenziosa)
□ Verificato: nessun errore noto in CP recenti da ripetere
```

**Viola REGOLA 0 = BLOCCA tutto. Leggi prima.**

---

## REGOLA 1 — MEMORY EMPIRE OBBLIGATORIO POST-OGNI-VIDEO

Dopo OGNI video ingerito (YouTube, TikTok, qualsiasi fonte):

```
GATE MEMORY EMPIRE (Stages C-H):
□ Stage C: knowledge/<video-id>/contenuto-integrale.md scritto (MAI riassunti)
□ Stage C: knowledge/<video-id>/atoms.json scritto
□ Stage C: knowledge/<video-id>/ingest-manifest.json scritto
□ Stage D: enrichment-research eseguito (relevance → gap → scout → propose)
□ Stage E: permission-guard approvato/negato ogni proposal
□ Stage F: enrichments applicati (o log motivazione skip)
□ Stage G: audit log scritto in memory/audit/
□ Stage H: report all'utente (cosa archiviato + skill arricchite/non arricchite)
```

**Viola REGOLA 1 = video NON è "fatto". Niente avanza senza Memory Empire.**

---

## REGOLA 2 — FRAME REALI (NO-FINTO)

```
□ Video scaricato con yt-dlp (no skip)
□ Frame estratti con ffmpeg --interval 2 (densa, non --max-frames)
□ Claude legge OGNI frame PNG via Read nativo
□ Nessuna descrizione di frame non letto (violazione NO-FINTO)
□ Inferenze marcate con ➕
□ Ogni atom tracciato: video-id#timestamp + frame-NNN.png
```

---

## REGOLA 3 — NO-STUB (validator.py è il cancello)

```
□ python scripts/validator.py → 0 violazioni prima di dichiarare "fatto"
□ Nessun agente/skill con placeholder
□ Nessun file <15 righe che dichiara di essere "completo"
```

---

## REGOLA 4 — CLI-ONLY (no API, no paid)

```
□ Nessuna chiamata a API esterne a pagamento
□ Nessuna API OpenAI/Anthropic diretta nel pipeline
□ Tutti gli strumenti: yt-dlp, ffmpeg, playwright, python — gratuiti
□ La visione la fa Claude nativo (zero costo aggiuntivo)
```

---

## REGOLA 5 — TRACCIABILITÀ P12

```
□ Ogni knowledge atom ha trace: "video-id#timestamp + frame-NNN.png" o "file:riga"
□ Nessun fatto senza fonte verificabile
□ video-analysis.md ha Visual Timeline con frame reali + descrizioni reali
```

---

## REGOLA 6 — COMPANY/MEMORY SINCRONIZZATA

```
□ Checkpoint scritto in company/Memory/checkpoints/ dopo ogni task chiuso
□ STATO-EMPIRE.md aggiornato (cosa fatto, lavori in corso, RIPRESA DA)
□ ADR scritti per ogni decisione architetturale
□ Nessun task è "fatto" senza checkpoint
```

---

## KNOWN ERRORS (da NON ripetere — aggiornato da error-triage-controller)

| ID | Errore | Gravità | Quando | Prevenzione |
|----|--------|---------|--------|-------------|
| ERR-001 | Memory Empire omesso dal pipeline comunicato | CRITICA | 2026-06-13 sessione Andrei Pascu | compliance-auditor verifica RULES §1 prima di ogni pipeline |
| ERR-002 | CATALOG.md dice "⬜ planned" ma file esistono | MEDIA | N/A | validator.py verifica coerenza CATALOG vs filesystem |

---

## CHECKLIST PRE-COMUNICAZIONE ALL'UTENTE

Prima di comunicare "pipeline avviato" o "video fatto":

```
□ Memory Empire incluso nel piano? (RULES §1)
□ company/Memory/ letto? (RULES §0)
□ Frame reali pianificati (--interval 2)? (RULES §2)
□ Nessun errore noto (KNOWN ERRORS) nella sessione?
```

**Se una sola casella è ☐ → NON comunicare. Correggi prima.**
