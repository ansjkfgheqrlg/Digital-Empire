@echo off
chcp 65001 >nul
echo Creazione Windows Task Scheduler per l'invio delle email rimanenti...
schtasks /create /tn "DigitalEmpire_SendRemaining" /tr "\"c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow\send_all_remaining.bat\"" /sc ONCE /sd 09/05/2026 /st 09:30 /f /rl HIGHEST

if %errorlevel% equ 0 (
    echo.
    echo TASK CREATO CON SUCCESSO!
    echo Partira' domani (09 Maggio 2026) alle 09:30.
) else (
    echo.
    echo ERRORE: Esegui questo file come Amministratore (Tasto destro -^> Esegui come amministratore)
)
pause
