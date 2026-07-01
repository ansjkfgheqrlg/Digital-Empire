---
name: preventivo-auto
description: "Avvia PreventivoForge: trasforma un annuncio auto straniero (mobile.de, tedesco) in un PREVENTIVO italiano (PDF) per una concessionaria, con foto, scheda tecnica e descrizione tradotte + copy migliorato e prezzo finale calcolato nel titolo (esposto ×1.03 +1500 +1500). Multi-tenant: serve molte concessionarie (la prima è prof-autocad). Usa quando l'utente scrive /preventivo-auto, passa un link mobile.de e vuole il preventivo IT, dice 'crea il preventivo da questo annuncio', 'trasforma questo annuncio tedesco', 'fai il preventivo auto'. Cliente: Prof Autocad."
---

# preventivo-auto — Regia di PreventivoForge

Skill principale che dirige e avvia il workflow **PreventivoForge** del cliente **Prof Autocad**.
Workflow su disco: `Clienti/Prof Autocad/preventivo-forge/`.

## Cosa fa
`URL mobile.de (DE)` → preventivo **italiano** (PDF) per la concessionaria scelta:
foto + scheda tecnica + descrizione tradotte/migliorate + **prezzo finale nel titolo**.

## Quando attivare
- L'utente scrive `/preventivo-auto <url>`.
- L'utente passa un link **mobile.de** e chiede il preventivo / di "rifare l'annuncio in italiano".
- Frasi: "crea il preventivo da questo annuncio", "trasforma questo annuncio tedesco", "fai il preventivo auto".

## Procedura
1. **Identifica input**: URL mobile.de (obbligatorio) + concessionaria (`--dealer`, default `prof-autocad`).
   Se manca l'URL, chiedilo. Se l'utente nomina un'altra concessionaria, verifica che esista
   (`python run.py --list-dealers`); se no, proponi di crearne la config in `concessionarie/<id>/`.
2. **Avvia la pipeline** dalla cartella del workflow:
   ```bash
   cd "Clienti/Prof Autocad/preventivo-forge"
   python run.py "<URL-mobile.de>" --dealer prof-autocad
   ```
   Prima volta su una macchina: `pip install -r requirements.txt && playwright install chromium`,
   e copiare `.env.example` → `.env`.
3. **Se S1 (scraping) viene bloccato** da mobile.de (anti-bot): imposta `PLAYWRIGHT_HEADLESS=false`
   in `.env` e riprova (accetta consenso/captcha a mano una volta), **oppure** usa il fallback:
   salva la pagina come HTML e `python run.py --manual annuncio.html --foto ./foto --dealer prof-autocad`.
4. **Leggi l'esito**: la regia stampa la cartella `runs/<id>/` con `listing.json`, `listing_it.json`,
   e — se Half B è collegata — il `preventivo_*.pdf`. Riporta all'utente prezzo finale e percorso PDF.
5. **Gate**: se un gate è rosso (estrazione/traduzione/prezzo/PDF), NON consegnare: riporta il problema.

## Stato (2026-06-30)
- Half A (Max) collegata: S1 scraping, S2 parsing, S4 pricing, regia. ✅
- Half B (Gael) in arrivo: S3 traduzione+copy, S5 PDF, gate QA. Finché assente, la regia
  produce dati + prezzo e si ferma con nota di handoff (vedi `HANDOFF-GAEL.md`).

## File chiave
- Regia: `preventivo-forge/run.py` · Config dealer: `preventivo-forge/concessionarie/<id>/config.json`
- Contratto dati: `preventivo-forge/schema/listing.schema.json` (CONGELATO)
- Architettura: `preventivo-forge/00-ARCHITETTURA-WORKFLOW.md`
