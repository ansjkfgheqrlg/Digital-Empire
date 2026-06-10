@echo off
chcp 65001 >nul 2>&1
title Outreach Dashboard - Digital Empire
color 0A
cls
echo.
echo  ============================================
echo   OUTREACH DASHBOARD - Digital Empire v3.0
echo  ============================================
echo.
echo  Avvio server in corso...
echo.
cd /d "%~dp0outreach-dashboard-premium"
if not exist "node_modules" (
    echo  [!] Prima installazione - eseguo npm install...
    npm install
)
start "" http://localhost:3001
npm start -- --port 3001
