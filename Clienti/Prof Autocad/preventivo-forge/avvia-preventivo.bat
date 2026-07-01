@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ============================================
echo    PREVENTIVOFORGE - Prof Autocad
echo ============================================
echo.
set /p URL="Incolla il link di mobile.de e premi INVIO: "
echo.
echo Sto generando il preventivo...
echo (si aprira' una finestra di Chrome: lasciala lavorare da sola, non chiuderla)
echo.
python run.py "%URL%" --dealer prof-autocad
echo.
echo ============================================
echo    FATTO. Il PDF si e' aperto da solo.
echo    (lo trovi anche nella cartella "runs")
echo ============================================
echo.
pause
