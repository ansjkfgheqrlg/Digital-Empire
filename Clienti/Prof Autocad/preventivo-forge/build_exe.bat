@echo off
rem Costruisce l'App Windows autonoma (.exe) di PreventivoForge.
rem Serve una volta sola sul PC di sviluppo. L'output e' portabile.
cd /d "%~dp0"
echo ============================================
echo   BUILD APP .EXE - PreventivoForge
echo ============================================
echo.
echo [1/3] Installo le dipendenze (se mancano)...
python -m pip install -r requirements.txt >nul 2>&1
python -m pip install pyinstaller websocket-client >nul 2>&1
echo [2/3] Costruzione in corso (puo' richiedere qualche minuto)...
python -m PyInstaller --noconfirm preventivo-forge.spec
echo [3/3] Fatto.
echo.
echo App pronta in:  dist\PreventivoForge\PreventivoForge.exe
echo Copia l'intera cartella "dist\PreventivoForge" sul PC che deve usarla.
echo (Il PC deve avere Google Chrome installato.)
echo.
pause
