@echo off
rem Costruisce l'App Windows autonoma (.exe) di Empire Desk.
rem IMPORTANTE (REGISTRO-ERRORI E8/E9 di PreventivoForge): chiudere EmpireDesk.exe
rem e i Chrome che ha aperto PRIMA di rilanciare la build, altrimenti fallisce in silenzio.
cd /d "%~dp0"
echo ============================================
echo   BUILD APP .EXE - Empire Desk
echo ============================================
echo.
echo [1/3] Installo le dipendenze (se mancano)...
python -m pip install -r requirements.txt >nul 2>&1
python -m pip install pyinstaller >nul 2>&1
echo [2/3] Costruzione in corso...
python -m PyInstaller --noconfirm --clean empiredesk.spec
echo [3/3] Fatto.
echo.
echo App pronta in:  dist\EmpireDesk\EmpireDesk.exe
echo Deve restare DENTRO la cartella "Digital Empire" (lancia le automazioni con path relativi).
echo.
pause
