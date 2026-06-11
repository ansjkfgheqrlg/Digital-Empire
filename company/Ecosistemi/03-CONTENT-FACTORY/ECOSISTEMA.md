# 🎬 03 — CONTENT-FACTORY

> **Livello:** L1 · **Priorità:** ALTA · **Stato:** parziale (workflow esistono, non coordinati)
> Dossier completo: `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md`

## Missione

Produrre contenuti multi-formato (caroselli, video, testi, visual) per TUTTI
gli ecosistemi della holding e per i clienti agency. **Multi-tenant by design:**
lo stesso motore serve DE stessa, i clienti agency, i canali YouTube, i libri KDP.
Input obbligatori: `brand_kit` + `icp`.

## Formati prodotti

| Formato | Tool/Pipeline | Ecosistema servito |
|---|---|---|
| Caroselli LinkedIn/Instagram | Canva automation + Playwright | AGENCY, INFO-BIZ, DE brand |
| Video Reels/Shorts | script AI + HeyGen/Runway + ffmpeg | MULTI-BUSINESS (YT), AGENCY |
| Post social (caption, thread) | copy-workflow A1-A8 | tutti |
| Email marketing | copy-workflow A5-A6 | INFO-BIZ, AGENCY |
| Visual/Template | empire-style, Canva | tutti |

## Reparti L2

| # | Reparto | Missione | Path |
|---|---|---|---|
| L2.1 | Strategia | brief, calendario, ICP alignment | `Reparti/Strategia/` |
| L2.2 | Video | script → produzione → montaggio → QA | `Reparti/Video/` |
| L2.3 | Testuale | post, email, thread, caption | `Reparti/Testuale/` |
| L2.4 | Visual&Design | template, caroselli, cover | `Reparti/Visual-Design/` |
| L2.5 | Pubblicazione | scheduling, distribuzione multicanale | `Reparti/Pubblicazione/` |

## Workflow principali

- `WF-CAROUSEL` — brief → slide design Canva → caption APSOC → publish
- `WF-VIDEO-SHORT` — script → HeyGen/Runway → montaggio ffmpeg → QA → upload
- `WF-POST-SOCIAL` — brief ICP → copy-workflow → brand gate → schedule
- `WF-EMAIL-SEQUENCE` — brief → A5/A6 → APSOC gate → invio

## Come si collega al Backbone

- **BUS:** riceve brief da AGENCY, INFO-BIZ, MULTI-BUSINESS; invia asset finiti al richiedente
- **BRAIN:** namespace `content/*` — stato produzione, performance contenuti
- **GOVERNANCE:** brand gate G2 su OGNI output (brand_kit dichiarato)

## Asset esistenti (da migrare in F3)

- `caroselli/` — workflow caroselli esistente
- `Workfolw_Crea_Caroselli/` — automazione Canva
- `SKILL & Agenti/Ecosistema - Content Factory/` — pipeline video AION adattata
- `Outreach/outreach-dashboard-premium/` — dashboard (condivisa con AGENCY)

*Fonte: `PIANO-MAESTRO/03-ECOSISTEMA-CONTENT-FACTORY.md` · Aggiornato: 2026-06-11*
