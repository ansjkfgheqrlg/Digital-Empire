@echo off
chcp 65001 >nul
echo.
echo ================================================
echo   DIGITAL EMPIRE — Outreach Automatico
echo   300 email al giorno - Costo: 0 dollari
echo ================================================
echo.
echo Lancia il sistema e aspetta circa 50-60 minuti.
echo Il sistema trovera' lead, scrivera' le email e le inviera'.
echo.
echo Premi INVIO per partire, Ctrl+C per annullare.
pause >nul
echo.

python run.py

echo.
if %errorlevel% equ 0 (
    echo Sistema completato. Controlla i risultati sopra.
) else (
    echo Qualcosa non ha funzionato. Controlla il messaggio di errore.
)
echo.
pause
