@echo off
rem Apre Aureus Agency OS direttamente nel browser (senza bisogno di server o installazioni).
cd /d "%~dp0"
echo Apertura di Aureus Agency OS...
start "" "platform\dist\index.html"
exit
