@echo off
chcp 65001 >nul
cd /d "c:\Users\Utente\Desktop\qui tutto\Digital Empire\Outreach\Outreach Workflow"
echo =====================================================
echo   EMAIL OUTREACH LIVE - Digital Empire
echo   Scraping LIVE + invio a goccia (max 100/ora, 500/giorno)
echo =====================================================
echo.
python run.py --target 500 --mode completo
echo.
pause
