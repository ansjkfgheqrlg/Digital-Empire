---
name: avvia-ig
description: Avvia il workflow Instagram DM di Digital Empire. Apre una finestra CMD visibile con la run Instagram (hashtag scout → qualifier → DM → follow-up). Usa quando l'utente scrive /avvia-ig o vuole avviare Instagram, mandare DM Instagram, far partire il flusso Instagram.
metadata:
  version: 1.0.0
---

# Avvia Instagram Outreach

Apri SUBITO una finestra CMD visibile con il flusso Instagram. NESSUNA domanda — esegui direttamente.

## Azione immediata

Esegui questo comando PowerShell che apre una nuova finestra CMD visibile sul desktop:

```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Instagram Automation" && echo. && echo  ===================================================== && echo   INSTAGRAM DM - Digital Empire (max 30 DM/giorno) && echo  ===================================================== && echo. && python run_today.py'
```

Dopo aver lanciato il comando, di' all'utente:
- "CMD aperto — flusso Instagram avviato (max 30 DM oggi)"
