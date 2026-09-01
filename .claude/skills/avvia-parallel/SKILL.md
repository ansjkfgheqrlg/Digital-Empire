---
name: avvia-parallel
description: Avvia tutti i flussi outreach di Digital Empire in parallelo — Email + Instagram simultaneamente. Apre DUE finestre CMD visibili. Usa quando l'utente scrive /avvia-parallel o vuole avviare tutto insieme, lanciare email e instagram in parallelo.
metadata:
  version: 1.0.0
---

# Avvia Tutto in Parallelo

Apri SUBITO DUE finestre CMD visibili — una per Email, una per Instagram. NESSUNA domanda — esegui direttamente.

## Azione immediata

Esegui questi DUE comandi PowerShell in sequenza (aprono 2 finestre CMD separate visibili sul desktop):

**Finestra 1 — Email:**
```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow" && echo. && echo  ===================================================== && echo   [1/2] EMAIL OUTREACH - Digital Empire && echo  ===================================================== && echo. && python run.py --target 500 --mode completo'
```

**Finestra 2 — Instagram:**
```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Instagram Automation" && echo. && echo  ===================================================== && echo   [2/2] INSTAGRAM DM - Digital Empire && echo  ===================================================== && echo. && python run_today.py'
```

Esegui entrambi i comandi PowerShell nell'ordine indicato — si apriranno 2 finestre CMD separate.

Dopo aver lanciato, di' all'utente:
- "2 CMD aperti — Email + Instagram in parallelo"
- Email riprende dal checkpoint se esiste (scraping live, no CSV vecchio)
- Instagram: max 30 DM oggi
