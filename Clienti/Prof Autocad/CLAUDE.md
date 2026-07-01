# CLAUDE.md — Cliente Prof Autocad

## Identità
Cartella del **primo cliente ufficiale** di Digital Empire: **Prof Autocad** (concessionario auto,
import dalla Germania). Qui vive **PreventivoForge**: workflow che trasforma un annuncio
**mobile.de (tedesco)** in un **preventivo italiano (PDF)** per il cliente finale, **multi-concessionaria**.

## Prima di lavorare qui (memory-first)
1. Leggi `../../company/Memory/STATO-EMPIRE.md` (blocco 🛑 in cima + blocco cliente).
2. Leggi `../../STATO-SITUAZIONE.md` (cruscotto: chi fa cosa ora).
3. Deliverable: `preventivo-forge/` → brain tecnico `preventivo-forge/CLAUDE.md`, architettura
   `preventivo-forge/00-ARCHITETTURA-WORKFLOW.md`, handoff `preventivo-forge/HANDOFF-GAEL.md`.

## Regole non negoziabili
- **Data contract CONGELATO:** `preventivo-forge/schema/listing.schema.json` (+ `listing_it.schema.json`).
  Non cambiarlo senza aggiornare architettura + avvisare l'altro socio (è la cucitura Max↔Gael).
- **Split 50/50:** Max = Half A (acquisizione/dati/prezzo/regia). Gael = Half B (traduzione+copy/PDF/QA).
  Lavora SOLO sulla tua metà.
- **Multi-tenant:** ogni concessionaria = `preventivo-forge/concessionarie/<id>/config.json`
  (prezzo/logo/contatti). Mai hardcodare valori di un dealer nel codice.
- **Prezzo:** `finale = round(esposto ×1.03 +1500 +1500)` (parametrico per dealer).
- **Segreti:** solo in `.env` (vedi `.env.example`), mai committati.

## Stato (2026-06-30)
- Half A (Max): scraper/parser/pricer/regia/schema/multi-tenant/skill ✅ testato. Fondamenta agenti+orchestration in corso.
- Half B (Gael): S3 traduci+copy, S5 PDF, 4 QA → in costruzione (handoff).

## Riferimento formato preventivo
`Preventivo BMW Z4 2003 FR 3.0i.pdf` (in questa cartella) = modello del PDF finale.
