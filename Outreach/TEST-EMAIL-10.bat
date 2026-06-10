@echo off
chcp 65001 >nul
cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow"
echo =====================================================
echo   TEST EMAIL (10 lead, ANTEPRIMA - non invia nulla)
echo   Scraping LIVE dei nuovi target (no CSV vecchio)
echo =====================================================
echo.
python run.py --target 10 --anteprima
echo.
echo --- FINITO. Controlla le email qui sopra. ---
pause
