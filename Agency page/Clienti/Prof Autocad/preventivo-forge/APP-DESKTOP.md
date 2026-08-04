# App Desktop — PreventivoForge (Gael)

Interfaccia grafica (finestra) attorno al motore PreventivoForge. Stile argento, minimal, professionale.
Incolli il link mobile.de → premi un bottone → esce il PDF (si apre da solo).

## Due modi di usarla

### A) Subito, sul tuo PC (serve Python già installato)
Doppio click su **`avvia-app.bat`** → si apre la finestra. Incolla il link, scegli la concessionaria,
premi **«Genera preventivo»**. Vedi i passaggi in diretta; a fine lavoro il PDF si apre da solo.

(Equivalente da terminale: `python app.py`)

### B) App autonoma .exe (da dare al concessionario, senza installare niente)
1. Sul PC di sviluppo, doppio click su **`build_exe.bat`** (una volta sola).
2. Viene creata la cartella **`dist/PreventivoForge/`** con dentro **`PreventivoForge.exe`**.
3. Copi l'INTERA cartella `dist/PreventivoForge/` sul PC di destinazione.
4. Lì: doppio click su `PreventivoForge.exe`. Nessun Python, nessuna chiave AI.

**Requisito unico del PC di destinazione:** Google Chrome installato (il motore usa il Chrome vero
per superare l'anti-bot di mobile.de e per stampare il PDF, senza dipendenze pesanti).

## Come funziona dentro
- `app.py` NON ririscrive la pipeline: lancia `run.py` (Half A/Max) in un thread, cattura i log e
  mostra l'avanzamento, poi apre il PDF prodotto in `runs/<id>/`.
- Il PDF è generato **senza Playwright** (motore `cdp` = Chrome del PC via DevTools) → l'.exe resta leggero.
- Le cartelle scrivibili (`runs/`, `logs/`) finiscono accanto all'eseguibile.

## File coinvolti (tutti Half B / Gael)
- `app.py` — l'applicazione (GUI + orchestrazione).
- `avvia-app.bat` — avvio rapido della GUI (modo A).
- `build_exe.bat` + `preventivo-forge.spec` — packaging in `.exe` (modo B).
- `implementation/render_pdf.py` — motore PDF con percorso `cdp` (Chrome), .exe-ready.

## Note / da rifinire con Max (Half A)
- Lo **scraping live** usa ancora il pacchetto `playwright` come *client* CDP (non scarica il browser):
  l'.exe includerà quel pacchetto (leggero). Migrazione completa a `cdp.py` = eventuale rifinitura di Max.
- `cdp.launch()` (Half A) non passa `--remote-allow-origins=*`: Chrome ≥111 rifiuta la connessione
  WebSocket CDP grezza (io l'ho gestito nel render lanciando Chrome col flag corretto). Utile aggiungerlo
  anche in `cdp.launch` per robustezza dello scraping su Chrome recente.
- La modalità `--manual` col nuovo parser richiede `window.__INITIAL_STATE__` nell'HTML salvato per
  estrarre le dotazioni (il vecchio fallback `<ul><li>` non è più popolato dallo scraper).

## Stato
✅ App funzionante e testata end-to-end (selftest: 4 gate verdi, PDF via cdp-chrome). Packaging pronto
(`build_exe.bat`). Build/test finale dell'.exe da fare sull'ambiente reale. — Gael, 2026-07-02
