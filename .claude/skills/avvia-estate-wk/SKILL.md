---
name: avvia-estate-wk
description: Accende il sistema nervoso del Workflow Estate di Digital Empire con un solo comando. Apre una finestra CMD visibile che rigenera la dashboard, valuta i gate, misura gli agenti, conta le tracce e stampa il cruscotto di accensione. Usa quando l'utente scrive /avvia-estate-wk o vuole accendere/avviare il workflow estate, il cervello estate, il sistema nervoso estate.
metadata:
  version: 1.0.0
---

# Avvia Workflow Estate (sistema nervoso)

Accende il cervello del Workflow Estate con UN comando. NESSUNA domanda — esegui direttamente.

## Azione immediata

Esegui questo comando PowerShell che apre una finestra CMD visibile sul desktop e accende il sistema nervoso:

```powershell
Start-Process cmd -ArgumentList '/k', 'chcp 65001 >nul && cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire" && echo. && echo  ===================================================== && echo   WORKFLOW ESTATE - ACCENSIONE SISTEMA NERVOSO && echo  ===================================================== && echo. && python -m empire avvia-estate'
```

Il comando `empire avvia-estate`, in ordine:
1. rigenera la **dashboard** dai dati veri
2. valuta i **6 gate** + i controlli di completamento
3. misura gli **agenti operativi**
4. conta i **cicli di memoria** (tracce)
5. scrive una **traccia di sessione** — l'accensione stessa lascia traccia
6. stampa il **cruscotto**: stato, cosa fare adesso, cosa resta a Max

Non fa partire invii/incassi/pubblicazioni (porte d'uscita = decisione di Max). Accende il
cervello, non spara verso l'esterno.

## Dopo aver lanciato, di' all'utente:
- "CMD aperto — sistema nervoso Workflow Estate acceso."
- Riporta l'esito: `✅ ACCESO` (exit 0) oppure `ACCESO CON RISERVA` se ci sono controlli di costruzione rossi.
- Ricorda i 3 comandi vivi: `empire estate` · `empire forge scan` · `empire trace stato`.
- Le 2 voci che restano sono di Max: lead veri (Gate-CONTATTI) + incasso/Payment Link Stripe (Gate-REV).
