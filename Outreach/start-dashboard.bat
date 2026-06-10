@echo off
chcp 65001 > nul
echo.
echo  ╔══════════════════════════════════════════════════╗
echo  ║     Digital Empire — Outreach Dashboard          ║
echo  ║     http://localhost:3000  (locale)              ║
echo  ╚══════════════════════════════════════════════════╝
echo.

cd /d "%~dp0outreach-dashboard-premium"

:: Avvia Next.js in background
echo [1/2] Avvio Next.js dev server...
start "Next.js Dashboard" cmd /k "npm run dev"

:: Attendi che Next.js sia pronto
timeout /t 5 /nobreak > nul

:: Controlla se ngrok è installato e prova ad aprire tunnel
echo [2/2] Tentativo apertura tunnel pubblico con ngrok...
where ngrok >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo.
    echo  ngrok trovato! Apro tunnel pubblico...
    echo  L URL pubblico apparira nella finestra ngrok.
    echo.
    start "ngrok Tunnel" cmd /k "ngrok http 3000"
) else (
    echo.
    echo  ngrok NON trovato. Il dashboard e accessibile solo localmente:
    echo  http://localhost:3000
    echo.
    echo  Per URL pubblico, installa ngrok:
    echo  1. Vai su https://ngrok.com/download
    echo  2. Scarica e metti ngrok.exe in C:\Windows\System32\
    echo  3. Registrati su ngrok.com e configura: ngrok config add-authtoken IL_TUO_TOKEN
    echo  4. Rilancia questo script
    echo.
)

echo.
echo  Dashboard avviato. Apri http://localhost:3000 nel browser.
echo  Chiudi questa finestra per fermare tutto.
echo.
pause
