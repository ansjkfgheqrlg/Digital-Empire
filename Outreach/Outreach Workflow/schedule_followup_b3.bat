@echo off
chcp 65001 >nul
echo.
echo ================================================
echo   DIGITAL EMPIRE — Schedula Follow-up Batch 3
echo   Data invio: 2026-05-10 09:00
echo ================================================
echo.

:: Trova il percorso completo di python.exe
for /f "delims=" %%i in ('where python 2^>nul') do (
    set PYTHON_PATH=%%i
    goto :found
)

echo ERRORE: Python non trovato nel PATH.
echo Installa Python da python.org e riprova.
pause
exit /b 1

:found
echo Python trovato: %PYTHON_PATH%
echo.

set TASK_NAME=DigitalEmpire_FollowupB3
set SCRIPT_DIR=c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow
set SCRIPT=send_followup_b3.py

echo Creazione Windows Task Scheduler...
schtasks /create /tn "%TASK_NAME%" /tr "\"%PYTHON_PATH%\" \"%SCRIPT_DIR%\%SCRIPT%\" --auto" /sc ONCE /sd 10/05/2026 /st 09:00 /f /rl HIGHEST

if %errorlevel% equ 0 (
    echo.
    echo ================================================
    echo   TASK CREATO CON SUCCESSO!
    echo   Nome    : %TASK_NAME%
    echo   Script  : %SCRIPT%
    echo   Quando  : 2026-05-10 alle 09:00
    echo ================================================
    echo.
    echo Verifica con: schtasks /query /tn "%TASK_NAME%"
) else (
    echo.
    echo ERRORE nella creazione del task.
    echo Prova a eseguire come Amministratore.
)
echo.
pause
