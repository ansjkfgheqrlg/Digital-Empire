# REGISTRO-ERRORI — PreventivoForge (memoria di debug)

**Scopo:** ogni errore riscontrato va scritto QUI con causa radice + fix + **regola per non ripeterlo**.
Prima di modificare o consegnare: leggere questo file. **Nessun errore va commesso due volte.**
Vale per Max, Gael e Claude. (Allineato all'ISPETTORATO GENERALE — REGISTRO-ERRORI + gate anti-recidiva.)

---

## Regole permanenti (derivate dagli errori sotto)

1. **Un fetch è "riuscito" solo con i DATI, non solo perché "non è bloccato".** (E1)
2. **Non aprire una sessione browser nuova a ogni scrape**: riusa il profilo/cookie (anti-blocco IP). (E2)
3. **I gate bloccano SOLO su difetti NOSTRI** (prezzo/foto assenti o tagliate, tedesco nel titolo).
   Mai bloccare su qualità della SORGENTE (foto piccole del venditore, 1 parola rara). (E3, E4)
4. **Confronta numeri come numeri**, non come stringhe (0.0 ≠ "0" è un bug). (E5)
5. **La riserva AI copre TUTTI i campi**, e gira PRIMA di costruire i campi derivati + una passata finale. (E6)
6. **Glossario per sigle/enti** (TÜV, HU, AU…) + prompt AI "nessuna parola in tedesco". (E7)
7. **MAI rebuild/zip con l'app aperta** (blocca i file → build/zip falliscono in silenzio).
   Sempre: chiudere l'app → verificare `BUILD_EXIT=0` + timestamp exe fresco. (E8, E9)
8. **Ogni build va provata live su 2-3 auto diverse** prima di consegnarla (0 residui, PDF ok).

---

## Errori registrati (2026-07-05)

| ID | Sintomo | Causa radice | Fix (commit) | Regola |
|----|---------|--------------|--------------|--------|
| **E1** | Scraping "riuscito" ma PDF vuoto / falso "anti-bot" | bail a 20s afferrava la pagina PRIMA che il JS caricasse `window.__INITIAL_STATE__`; il check accettava la pagina senza dati | scraper aspetta `__INITIAL_STATE__` e lo PRETENDE per il successo; bail solo su vera challenge (`07d4886`) | R1 |
| **E2** | IP bloccato da mobile.de dopo molti scrape | profilo Chrome NUOVO a ogni scrape = tante "sessioni bot" dallo stesso IP | profilo persistente `browser-profile/` (riusa il cookie Akamai); tentativo1 fisso, retry freschi (`5045ecd`) | R2 |
| **E3** | Gate IMG blocca l'intero preventivo | 2 foto del VENDITORE sotto 300px → bloccava tutto (non è un difetto nostro; con `contain` si vede intera) | foto piccole/non scaricate = avviso; blocca solo su 0 foto/PDF senza foto/senza fit (`dff8a7d`) | R3 |
| **E4** | Gate B blocca "tedesco residuo" | bloccava su 1 sola parola rara in un optional | blocca solo se tedesco nel titolo o abbondante (>3); residuo minore = avviso (`d771d93`) | R3 |
| **E5** | Gate B "Chilometraggio 0 km vs 0" (auto nuova) | confronto stringhe: `str(0.0)`→`"00"` ≠ `"0"` | confronto numerico normalizzato (int) (`d771d93`) | R4 |
| **E6** | Tedesco residuo in descrizione/highlights (batch 10, #7) | riserva AI correggeva solo equipment/specs, MA descrizione/highlights costruiti PRIMA dalle fonti tedesche; rate-limit AI | AI sulle fonti PRIMA dei derivati + passata FINALE su TUTTI i campi + 4 tentativi con gestione 429 (`da9dfe6`) | R5 |
| **E7** | "TÜV" non tradotto | l'AI lo teneva come nome proprio (ente revisione DE) | glossario tüv/HU/AU→revisione ecc. + prompt AI localizza le sigle (`db286b1`) | R6 |
| **E8** | Rebuild fallito in silenzio (exe vecchio consegnato) | app aperta bloccava un file di log → PyInstaller `--clean` non completava, ma sembrava ok | chiudere l'app prima del rebuild; verificare `BUILD_EXIT=0` + timestamp exe | R7 |
| **E9** | Zip di consegna a 0 MB | app in esecuzione blocca `ClrLoader.dll` → `Compress-Archive` fallisce | zip solo con app chiusa | R7 |

---

## Come si usa
- Nuovo errore → nuova riga in tabella (ID progressivo) + eventuale nuova regola sopra.
- Prima di un fix, controllare se la causa è già nota qui (evita di re-inventare la ruota).
- Prima di consegnare, ripassare la **checklist** in `CHECKLIST-CONSEGNA.md`.
