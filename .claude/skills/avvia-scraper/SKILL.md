---
name: avvia-scraper
description: Avvia lo scraper di nuovi lead per Digital Empire Outreach. Apre una finestra CMD visibile con scrape_only.py. Usa quando l'utente scrive /avvia-scraper o vuole raccogliere nuovi lead, fare scraping, trovare email nuove.
metadata:
  version: 1.0.0
---

# Avvia Scraper Lead

Apri SUBITO una finestra CMD visibile con lo scraper. NESSUNA domanda — esegui direttamente.

## Azione immediata

Esegui questo comando PowerShell che apre una nuova finestra CMD visibile sul desktop:

```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow" && echo. && echo  ===================================================== && echo   SCRAPER LEAD - Digital Empire (target: 300 email) && echo  ===================================================== && echo. && python scrape_only.py --target 300'
```

Dopo aver lanciato il comando, di' all'utente:
- "CMD aperto — scraper avviato, cerca 300 nuove email"
- Ricordagli che usa il checkpoint se esiste, oppure suggerisci `--fresh` per ripartire da zero
