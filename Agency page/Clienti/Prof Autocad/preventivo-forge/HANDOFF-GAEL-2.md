# 🤝 HANDOFF → GAEL — ROUND 2 (template Novacar + controlli + App .exe)

> Priorità di Max (2026-07-01). Il motore gira già LIVE (Chrome+CDP, dati veri, prezzo ok).
> Ora serve la **QUALITÀ VISIVA** + l'**App**. Leggi PRIMA: `regole/REGOLE-SACRE.md` (inviolabili)
> e il modello `../Preventivo BMW Z4 2003 FR 3.0i.pdf`. Concessionaria reale = **Novacar srl**
> (`concessionarie/novacar/` con `logo.png` + dati). "Prof Autocad" è stato rimosso: usa `novacar`.

## TASK 1 (PRIORITÀ MASSIMA) — Rifare il PDF sul modello Novacar
Riscrivi `templates/` + `render_pdf.py` per produrre ESATTAMENTE la struttura del modello (vedi REGOLE-SACRE R-01…R-14):
1. **Pagina 1 = SOLO logo** (grande, centrato) — `dealer.logo_path` in `dealer._dir`.
2. **Ogni pagina: logo in alto a sinistra** (piccolo).
3. **Pagina 2:** header con logo + blocco dati azienda in alto a destra (`config.legal` + `config.contacts`:
   ragione sociale, P.IVA, Sede Legale, cell., e-mail, PEC) → poi **titolo grande** auto → **scheda tecnica**
   (tabella barra scura + righe alternate; campi come nel modello). Font/tabella migliorabili, struttura no.
4. **Pagina 3:** "Equipaggiamento principale" (bullet) + "Condizioni di garanzia" + blocco
   **"Totale in strada (Iva inclusa) € <finale>"** con dettaglio + nota "Offerta valida salvo disponibilità del fornitore".
5. **Pagine foto:** 2 foto grandi per pagina, **TUTTE** le foto dell'annuncio, **MAI tagliate**
   (`object-fit: contain`, mai `cover`), alta qualità, dimensione uniforme. (R-09 = critica.)
6. **Ultima pagina = SOLO logo.**
- Colori dal config: `accent_color` (barre scure), `highlight_color` (arancione logo).
- Multi-pagina A4 reale (CSS `@page` + `page-break-after`).

## TASK 2 — Motore PDF senza Playwright (per l'.exe)
`render_pdf._html_to_pdf` deve usare **`implementation/cdp.py`** (Chrome del PC via CDP), NON il chromium
di Playwright: scrivi l'HTML in un file temp, apri Chrome headless via `cdp.launch(...headless=True)` +
`cdp.Page(port).navigate(file_uri)` → `print_pdf(print_background=True)` → scrivi i byte. Così l'.exe non
impacchetta chromium/GTK. (`cdp.py` è pronto, l'ho fatto io — Max.)

## TASK 3 — Nuovo agente `qa-immagini` (Gate IMG) — REGOLA R-09
`qa_gate.py`: `gate_img(ctx, dealer) -> (bool, issues)`:
- n. foto nel PDF == n. foto in `listing.json.images` (nessuna esclusa)
- ogni foto presente su disco, risoluzione minima decente, **nessun crop** (il template usa `contain`)
- + agente CF-grade 7-file `agents/verifica/qa-immagini/`.

## TASK 4 — Nuovo agente `qa-regole-checker` (Gate R) — REGOLE R-01…R-14
`qa_gate.py`: `gate_regole(ctx, dealer) -> (bool, issues)` che verifica una per una le regole sacre
(logo cover/header/footer presenti, blocco dati azienda, titolo, scheda, sezioni, prezzo, italiano, ecc.)
e scrive `runs/<id>/regole-check.json` (PASS/FAIL per regola). + agente CF-grade `agents/verifica/qa-regole-checker/`.
**Wiring:** avvisa Max → aggiunge le 2 chiamate (Gate IMG + Gate R) in `run.py` dopo S5.

## TASK 5 — App .exe (GUI minimal ARGENTO, elegante, professionale)
Interfaccia desktop bellissima e semplice (Max: **argento**, minimal, moderna, curata al pixel).
- 1 campo "Incolla link mobile.de" + 1 bottone grande + barra di avanzamento elegante + apertura PDF a fine.
- Sotto il cofano chiama il motore (via una funzione `genera_preventivo(url, dealer)` — se non c'è, la definiamo insieme).
- Impacchetta con **PyInstaller** (onedir) usando il motore **senza Playwright** (solo requests/bs4/lxml/jinja2/jsonschema/Pillow/websocket-client + il Chrome del cliente).
- Il concessionario NON installa né Python né Claude: copia la cartella, doppio click sull'.exe.

## Dopo ogni preventivo
Aggiungi una voce in `Memory/storico-preventivi/` (data, auto, id, esito, prezzo, path PDF) + aggiorna `Memory/INDEX.md`.

## Definition of Done
`avvia-preventivo.bat` (o l'.exe) su un annuncio reale → PDF **identico per struttura al modello Novacar**,
Gate R + Gate IMG verdi, tutte le foto complete. Poi CP + STATO + push.
