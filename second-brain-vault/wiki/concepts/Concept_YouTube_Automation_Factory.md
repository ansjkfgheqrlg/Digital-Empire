---
Type: CONCEPT
Status: Active
Tags: #youtube-automation #cash-cow #fliki #seo #video-iq #skill #agenti
Created: 2026-07-21
Last updated: 2026-08-24
---

# YouTube Automation Factory (skill operativa)

## Overview
Fabbrica multi-agente che trasforma il metodo Digital Empire di **YouTube Automation / Cash Cow
Channels** (workshop Max_lider / Captain Hook + canale `#🎬crea-video`) in un workflow eseguibile
con agenti che operano, agenti che controllano (gate bloccanti) e sub-agenti di supporto. Serve
direttamente la linea revenue **S5 YouTube-Fliki auto** del Piano Estate (dossier 16).
Skill installata: `.claude/skills/youtube-automation-factory/` — comando `/yt-factory`.

## Il metodo in 3 materie
1. **ANALISI (Video IQ)** — leggere i dati da un **account neutro** (regola Captain Hook): views/ora,
   CTR, retention, punteggio SEO (tag+keyword), riconoscere un **Cash Cow Channel** (costanza, non
   il singolo virale, pochi errori, format ripetibile).
2. **SEO / CERTIFICAZIONE** — la SEO è una "catena di nicchie": certifica a chi mostrare il video.
   Coerenza di nicchia = legge. "Copi il successo, non gli errori": diagnosi (picco-poi-calo=errore
   SEO; crescita lenta=errore thumb/titolo). Decisione **A upside** vs **B sicurezza** su quale video
   replicare (il "momento chiave", caso *Legami d'amore*).
3. **PRODUZIONE (Fliki)** — testo→video: voce, musica sotto la voce, scene, transizioni, sottotitoli
   ON, export ≥1080p MP4, anteprima obbligatoria. Poi upload + metadati SEO + programmazione.

## Architettura (MBA + Content-Forge)
- **Kernel:** SKILL.md + MKD.md (metodo completo espanso) + ARCHITECTURE.md.
- **6 operatori:** niche-scout · video-hunter · seo-analyst · script-writer · video-producer ·
  metadata-optimizer.
- **3 controllori (gate/audit):** niche-gate (coerenza nicchia) · seo-gate (metadati a norma) ·
  performance-auditor (feedback loop).
- **1 supporto:** memory-keeper (memoria dal passo zero).
- **2 tool deterministici testati:** `seo_score.py` (0-100) · `cashcow_check.py` (indice cash cow).
- **Pipeline 6 fasi:** Scouting → Selezione video → Script → Produzione → Pubblicazione → Audit → (loop).

## Come si costruita
Applicando due skill esterne clonate da GitHub:
`ansjkfgheqrlg/master-build-architecture` (struttura/architettura: 3 livelli, memoria dal passo zero,
7 sezioni canoniche per agente) e `ansjkfgheqrlg/content-forge2.0` (trasformazione contenuto grezzo
in artefatti operativi, espansione mai riassunto, MKD come base canonica).

## Evoluzione reale (2026-07-27 → 08-19): da scaffolding a fabbrica vera
Audit del 2026-07-27 trovò lo scaffolding APEX-7 reale e testato (11/11), ma **tutte e 6 le
fasi hardcoded**: canale mock fisso "Legami d'amore", 2 candidati-video finti, stesso script
statico per qualunque video, un "Critic" che restituiva sempre lo stesso punteggio — un gate
strutturalmente incapace di fallire non è un gate, è una formalità.

**Le 6 fasi rese reali una per una** (TASK-YT-001..005, 2026-07-27/29), sul motore condiviso
[[Tool_APEX7_Core_Motore_Condiviso]] (ADR-010):
- **F1 Scouting** — canale scelto da dati reali di 20 canali italiani (mappa Gemini), gate
  Cash Cow Index reso davvero bloccante (retry sui candidati finché uno non supera la soglia).
- **F2 Selezione** — fetch live pubblico dei video del canale (no API key), cache 7gg, scarto
  esplicito dei dati ambigui invece di inventarli.
- **F3 Script** — selezione deterministica tra 20 idee reali pre-scritte, tie-break
  documentato; poi evoluto a: Claude legge il transcript reale del video sorgente e scrive
  lo script (non generativo in codice).
- **F4 Produzione** — spec Fliki multi-scena parsata dallo script reale (non più 1 scena fissa).
- **F5 Pubblicazione** — titolo/descrizione/tag reali (non più placeholder fissi).
- **F6 Audit** — niente più `views_per_hour` finto: senza un video davvero pubblicato non
  scrive nulla (onestà del gate), altrimenti calcola sul fetch pubblico reale.
- **Dashboard** — riflette l'esito vero (PASS/FAIL) invece di essere sempre 🟢, e il vecchio
  runner-fantasma `run_youtube_apex7.py` è stato ritirato (non cancellato, ADR-003).

## Pivot di canale: da "Manuale Claude Code" a @dosementale (2026-07-29 → 07-31)
Il primo contenuto reale prodotto era ancora sul funnel morto "Manuale Claude Code". Gael ha
corretto: il target reale è **@dosementale** ([[Entity_Dose_Mentale_Channel]]), un canale
YouTube destinato a essere venduto già monetizzato — l'unico scopo è generare
visualizzazioni replicando/adattando contenuti reali del canale, nessun funnel a valle. Il
motore F1-F5 (prima ancora cablato sul Manuale) è stato riscritto: canale target fisso,
gate reale sul singolo video da copiare (≥20 viste/ora), script adattato dal transcript
reale del video sorgente. Prima automazione reale di **arena.ai via Playwright** (profilo
persistente, modalità Direct) per generare copertine adattate dalla miniatura reale del
video sorgente, e client API Fliki (`fliki_client.py`) per il rendering video reale.

## Secondo canale: @Legamidiamore, primo video reale pubblicato (2026-08-15 → 08-19)
Parallelamente, la fabbrica è stata cablata anche per [[Entity_Legami_dAmore_Channel]] (voce
femminile, tag SEO a 4 livelli, `credential-keeper` come agente permanente). **Primo video
mai pubblicato da questa fabbrica**: https://youtu.be/2t4BZR3KAiU (18/08), caricato a mano da
Max dopo che l'automazione Playwright dell'upload si è scontrata con "Verify it's you" di
Google (blocco non aggirabile da script, per design). Un pulsante unico "Produci video +
copertina" è stato aggiunto in Aureus/EmpireDesk (`produci_video_completo.py`, 08-08) che
incatena F1-F5 + copertina Arena + video Fliki in un solo comando.

## Connessioni
- [[Tool_APEX7_Core_Motore_Condiviso]] — motore condiviso su cui girano le 6 fasi (ADR-010)
- [[Entity_Legami_dAmore_Channel]] — primo canale con un video reale pubblicato
- [[Entity_Dose_Mentale_Channel]] — canale target dopo il pivot dal funnel Claude Code
- [[Concept_Meta_Ads_Library_Competitor_Research]] — analisi competitor (stesso spirito data-driven)
- [[Concept_Feature_vs_Benefit_Copy]] — copy applicabile a titoli/descrizioni SEO
- [[Concept_AI_vs_Copywriter_Limiti_e_Usi]] — limiti AI nella scrittura di script/hook

## Status
- First added: 2026-07-21 · Aggiornato: 2026-08-24 (backfill storico 06-08/2026, permesso
  esplicito Max) — evoluzione da scaffolding a fabbrica reale, pivot @dosementale, primo
  video pubblicato su @Legamidiamore
- Confidence: Alta — verificato con esecuzione reale, checkpoint CP-20260727-007/009/010/012/014,
  CP-20260728-007..013, CP-20260729-001..010, CP-20260815-001, CP-20260816-001, CP-20260818-001
