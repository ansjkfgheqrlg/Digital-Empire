---
name: avvia-email
description: Avvia il workflow email di Digital Empire Outreach. Apre una finestra CMD visibile con la run email completa (scraping → qualifier → writer → bibbia → invio). Usa quando l'utente scrive /avvia-email o vuole avviare la run email, mandare le email, far partire il flusso email.
metadata:
  version: 1.0.0
---

# Avvia Email Outreach

Apri SUBITO una finestra CMD visibile con il flusso email. NESSUNA domanda — esegui direttamente.

## Azione immediata

Esegui questo comando PowerShell che apre una nuova finestra CMD visibile sul desktop:

```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow" && echo. && echo  ===================================================== && echo   EMAIL OUTREACH - Digital Empire && echo   Riprendo dal checkpoint se esiste... && echo  ===================================================== && echo. && python run.py --target 500 --mode completo'
```

Dopo aver lanciato il comando, di' all'utente:
- "CMD aperto — il flusso email è in esecuzione"
- Ricordagli che può stoppare con CTRL+C e il checkpoint salva tutto
