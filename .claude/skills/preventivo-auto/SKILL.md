---
name: preventivo-auto
description: "Avvia PreventivoForge: trasforma un annuncio auto straniero (mobile.de, tedesco) in un PREVENTIVO italiano (PDF) per una concessionaria, con foto, scheda tecnica e descrizione tradotte + copy migliorato e prezzo finale calcolato nel titolo (esposto ×1.03 +1500 +1500). Multi-tenant: serve molte concessionarie (la prima è novacar). Usa quando l'utente scrive /preventivo-auto, passa un link mobile.de e vuole il preventivo IT, dice 'crea il preventivo da questo annuncio', 'trasforma questo annuncio tedesco', 'fai il preventivo auto'. Cliente: Novacar srl."
---

# preventivo-auto — Regia di PreventivoForge

Skill principale che dirige e avvia il workflow **PreventivoForge** del cliente **Novacar srl**.
Workflow su disco: `Clienti/Novacar srl/preventivo-forge/`.

## Cosa fa
`URL mobile.de (DE)` → preventivo **italiano** (PDF) per la concessionaria scelta:
foto + scheda tecnica + descrizione tradotte/migliorate + **prezzo finale nel titolo**.

## Quando attivare
- L'utente scrive `/preventivo-auto <url>`.
- L'utente passa un link **mobile.de** e chiede il preventivo / di "rifare l'annuncio in italiano".
- Frasi: "crea il preventivo da questo annuncio", "trasforma questo annuncio tedesco", "fai il preventivo auto".

## Procedura
1. **Identifica input**: URL mobile.de (obbligatorio) + concessionaria (`--dealer`, default `novacar`).
   Se manca l'URL, chiedilo. Se l'utente nomina un'altra concessionaria, verifica che esista
   (`python run.py --list-dealers`); se no, proponi di crearne la config in `concessionarie/<id>/`.
2. **Avvia la pipeline** dalla cartella del workflow:
   ```bash
   cd "Clienti/Novacar srl/preventivo-forge"
   python run.py "<URL-mobile.de>" --dealer novacar
   ```
   Prima volta su una macchina: `pip install -r requirements.txt && playwright install chromium`,
   e copiare `.env.example` → `.env`.
3. **Se S1 (scraping) viene bloccato** da mobile.de (anti-bot): imposta `PLAYWRIGHT_HEADLESS=false`
   in `.env` e riprova (accetta consenso/captcha a mano una volta), **oppure** usa il fallback:
   salva la pagina come HTML e `python run.py --manual annuncio.html --foto ./foto --dealer novacar`.
4. **Leggi l'esito**: la regia stampa la cartella `runs/<id>/` con `listing.json`, `listing_it.json`,
   e — se Half B è collegata — il `preventivo_*.pdf`. Riporta all'utente prezzo finale e percorso PDF.
5. **Gate**: se un gate è rosso (estrazione/traduzione/prezzo/PDF), NON consegnare: riporta il problema.

## Regola di routing — soglia intervento umano
Riferimento di mercato dallo studio competitor su Andrei Pascu (outFunnel Lezione 3): **sopra 1.000 €**
un funnel non dovrebbe chiudersi da solo, serve un umano nel loop. Il valore di un'auto supera quasi
sempre questa soglia — quindi ogni PDF generato da questa pipeline va trattato come **bozza da
verificare**, non come preventivo pronto per l'invio automatico al cliente finale: la concessionaria
(o Max) resta il controllo umano prima che il documento esca. Se in futuro la pipeline dovesse
generare preventivi sotto soglia (es. accessori, servizi minori), quello è il caso in cui la chiusura
automatica end-to-end diventa accettabile senza revisione.

## Stato (2026-06-30)
- Half A (Max) collegata: S1 scraping, S2 parsing, S4 pricing, regia. ✅
- Half B (Gael) in arrivo: S3 traduzione+copy, S5 PDF, gate QA. Finché assente, la regia
  produce dati + prezzo e si ferma con nota di handoff (vedi `HANDOFF-GAEL.md`).

## File chiave
- Regia: `preventivo-forge/run.py` · Config dealer: `preventivo-forge/concessionarie/<id>/config.json`
- Contratto dati: `preventivo-forge/schema/listing.schema.json` (CONGELATO)
- Architettura: `preventivo-forge/00-ARCHITETTURA-WORKFLOW.md`
