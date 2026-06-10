@echo off
chcp 65001 >nul
echo.
echo ================================================
echo   DIGITAL EMPIRE — Outreach Setup
echo   Da fare UNA SOLA VOLTA
echo ================================================
echo.

echo [1/3] Installo le dipendenze Python...
echo.
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo ERRORE: qualcosa e' andato storto con pip.
    echo Assicurati di aver installato Python da python.org
    pause
    exit /b 1
)

echo.
echo [2/3] Dipendenze installate con successo.
echo.
echo ================================================
echo   ORA DEVI CONFIGURARE 2 COSE nel file .env
echo ================================================
echo.
echo   COSA 1 - Token Facebook Ad Library (5 minuti, GRATIS):
echo     1. Vai su: developers.facebook.com/tools/explorer
echo     2. Crea un'app "Consumer" con permesso "ads_read"
echo     3. Genera il token e estendilo a 60 giorni
echo     4. Incollalo nel file .env alla riga FB_ACCESS_TOKEN=
echo.
echo   COSA 2 - App Password Gmail (3 minuti, GRATIS):
echo     1. Vai su: myaccount.google.com/apppasswords
echo     2. Seleziona "Mail" e "Computer Windows"
echo     3. Copia il codice di 16 caratteri
echo     4. Incollalo nel file .env alla riga GMAIL_APP_PASSWORD=
echo.
echo   Per aprire il file .env: leggi SETUP.md per i dettagli completi
echo.
echo ================================================
echo.
set /p RISPOSTA=Hai configurato entrambe le cose? Premi INVIO per il test...
echo.

echo [3/3] Test sistema (10 email, SENZA inviarle)...
echo.
python run.py --target 10 --anteprima

echo.
echo ================================================
if %errorlevel% equ 0 (
    echo   SETUP COMPLETATO!
    echo   Ora puoi usare 2_AVVIA.bat ogni giorno.
) else (
    echo   Qualcosa non va. Controlla il messaggio sopra.
    echo   Per aiuto: rileggi SETUP.md
)
echo ================================================
echo.
pause
