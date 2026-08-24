---
Type: PROJECT
Status: Shipped — consegna abbonabile pronta (cliente reale Novacar srl)
Tags: #cliente #automotive #workflow #preventivi #mobile-de #multi-tenant #novacar
Created: 2026-06-30
Last updated: 2026-08-24
---

# Project — Novacar srl (ex "Prof Autocad") · PreventivoForge

> **Nome cliente corretto**: il placeholder iniziale "Prof Autocad" è stato sostituito dal
> cliente reale **Novacar srl** (concessionaria import auto, Milano) dal 2026-07-01. La
> cartella su disco resta `Clienti/Prof Autocad/` (non rinominata per non rompere i
> riferimenti a fine sessione — item minore in backlog).

## Overview
Primo **cliente ufficiale** di Digital Empire: **Prof Autocad**, concessionario auto che importa
dalla Germania. Costruiamo **PreventivoForge**: workflow che trasforma un **annuncio mobile.de
(tedesco)** in un **preventivo italiano (PDF)** — foto + scheda + descrizione tradotte e copy
migliorato, **prezzo finale nel titolo** (`esposto ×1.03 +1500 +1500`). **Multi-concessionaria.**

## Dettagli
- Codice/SPEC: `Clienti/Prof Autocad/preventivo-forge/` (architettura `00-ARCHITETTURA-WORKFLOW.md`).
- Pipeline: S1 scraping (Playwright) → S2 parsing → GateA → S3 traduci+copy → GateB → S4 prezzo →
  GateC → S5 PDF preventivo → GateD.
- Team: 5 agenti operativi + 4 verificatori + conductor; skill regia `/preventivo-auto`.
- Build 50/50: **Max = Half A** (acquisizione/dati/prezzo/regia, ✅ fatta e testata) ·
  **Gael = Half B** (traduzione+copy, PDF, QA — handoff in `preventivo-forge/HANDOFF-GAEL.md`).
- Metodo: `architect-agent` (RBI) + `content-forge` (agenti 7-file) + repo `master-build-architecture`.

## Stato al 2026-07-01
Half A runnable e testata (Max). **Half B COMPLETA e verificata (Gael, 2026-07-01, CP-20260701-001):**
S3 traduzione+copy (glossario DE→IT deterministico ~150 termini), S5 render PDF (Playwright + template
Jinja2), QA Gate A/B/C/D bloccanti, 3 RULES, 6 agenti CF-grade (42 file). Test end-to-end reale
`run.py --manual` (BMW 320d) → PDF 63 KB, 4 gate ALL GREEN, prezzo 26.900→30.707 € (ricalcolo indipendente),
PDF ispezionato. Confine ADR-003 rispettato (run.py/schema/Half A non toccati). Traduzione deterministica → €0 API.

## Evoluzione 2026-07-01 → 07-03: da prototipo a consegna abbonabile
- **Scraping LIVE mobile.de risolto** (01/07): mobile.de è dietro Akamai Bot Manager
  (blocca anche Chrome pilotato da Playwright con fingerprint automation) e non espone i
  dati auto in JSON-LD. Fix: lo scraper lancia **Google Chrome reale** e si collega via
  **CDP** (`connect_over_cdp`), leggendo i dati veri da `window.__INITIAL_STATE__`. Prova
  live reale: annuncio Mercedes-Benz GLA 220 (esposto 47.490€ → 51.915€), 26/26 foto, 4
  gate verdi, PDF 810 KB.
- **Modello reale = Novacar srl** (01/07): riferimento PDF "Preventivo BMW Z4" fornito dal
  cliente reale. Scritte 14 **REGOLE-SACRE** inviolabili sul layout PDF (pag.1 solo logo,
  logo su ogni pagina, foto tutte e mai tagliate, ultima pagina solo logo, ecc.), con 2
  agenti QA dedicati (`qa-immagini` Gate IMG, `qa-regole-checker` Gate R-01..R-14).
- **App Desktop GUI** (02-03/07): prima Tkinter minimal, poi **GUI premium via pywebview**
  (WebView2, richiesta esplicita di Max "alza del 2000% la qualità grafica"), con fallback
  automatico a Tkinter se WebView2 assente. Motore PDF migrato da Playwright a **CDP/Chrome**
  (`Page.printToPDF`) per essere eseguibile dall'.exe senza dipendenze pesanti.
- **Kill-switch abbonamento** (03/07): `implementation/licenza.py` — controllo online prima
  di ogni preventivo (sospeso→blocca, rete-giù→grace period, anti-furbata su cache),
  gestito da remoto via Gist. Storico automatico di ogni preventivo consegnato in
  `Memory/storico-preventivi/`.
- **EXE frozen ri-testata**: `PreventivoForge.exe --selftest` → 6/6 gate + 14/14 REGOLE
  verdi, PDF prodotto dall'eseguibile senza Python installato sul PC cliente.

## Stato finale (2026-07-03)
**Consegna abbonabile pronta**: guida `CONSEGNA-NOVACAR.md` (requisiti PC, uso, SmartScreen,
attivazione/sospensione kill-switch). Pipeline sorgente end-to-end verificata: Mercedes GLA
47.490€ → 51.915€, 6/6 gate, 14/14 REGOLE. Residuo non bloccante: test su PC realmente privo
di Chrome, eventuale firma codice per rimuovere l'avviso SmartScreen di Windows.

## Connessioni
- [[Digital_Empire_6_Phase_Process]]
- [[Concept_Decisioni_Architetturali_ADR]] — ADR-003 (wrap non riscrittura) applicato sistematicamente
- Memory: `company/Memory/checkpoints/CP-20260630-002.md`, `company/Memory/STATO-EMPIRE.md`
- Skill motore: [[content-forge]] · copywriting · cro-copy-architect · playwright-dev · architect-agent
