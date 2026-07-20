@echo off
rem Costruisce l'App Windows autonoma (.exe) di Empire Desk (PIVOT AREUS, dossier 17 §0-bis).
rem IMPORTANTE (REGISTRO-ERRORI E8/E9 di PreventivoForge): chiudere EmpireDesk.exe
rem e i Chrome che ha aperto PRIMA di rilanciare la build, altrimenti fallisce in silenzio.
cd /d "%~dp0"
echo ============================================
echo   BUILD APP .EXE - Empire Desk (Aureus Agency OS)
echo ============================================
echo.
echo [1/4] Builda la piattaforma Aureus (platform/dist)...
echo       NON tocca la grafica (contenuto platform/ = Max) - solo npm install/build.
pushd platform
call npm install
call npm run build
popd
if not exist "platform\dist\index.html" (
  echo.
  echo ERRORE: platform\dist\index.html non trovato dopo la build.
  echo Controlla l'output di npm run build sopra prima di continuare.
  pause
  exit /b 1
)
echo [2/4] Installo le dipendenze Python (se mancano)...
python -m pip install -r requirements.txt >nul 2>&1
python -m pip install pyinstaller >nul 2>&1
echo [3/4] Costruzione .exe in corso...
python -m PyInstaller --noconfirm --clean empiredesk.spec
echo [4/4] Fatto.
echo.
echo App pronta in:  dist\EmpireDesk\EmpireDesk.exe
echo Deve restare DENTRO la cartella "Digital Empire" (lancia le automazioni con path relativi).
echo.
pause
