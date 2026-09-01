---
name: avvia-linkedin
description: Avvia il workflow LinkedIn di Digital Empire (commenti + connessioni + messaggi). Apre una finestra CMD visibile. Usa quando l'utente scrive /avvia-linkedin o vuole avviare LinkedIn, fare commenti su LinkedIn, mandare connessioni LinkedIn.
metadata:
  version: 1.0.0
---

# Avvia LinkedIn Outreach

Apri SUBITO una finestra CMD visibile con il flusso LinkedIn. NESSUNA domanda — esegui direttamente.

## Azione immediata

Esegui questo comando PowerShell che apre una nuova finestra CMD visibile sul desktop:

```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\LinkedIn Automation" && echo. && echo  ===================================================== && echo   LINKEDIN OUTREACH - Digital Empire && echo   20 connessioni + 20 messaggi + 30 commenti/giorno && echo  ===================================================== && echo. && python run_today.py'
```

Dopo aver lanciato il comando, di' all'utente:
- "CMD aperto — flusso LinkedIn avviato"
