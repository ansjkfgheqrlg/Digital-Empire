@echo off
rem Doppio click su questo file per fare il login una tantum su Amazon e LM Arena
rem (PIANO-KDP-67, CP1). Si apre una finestra nera (console) e poi due finestre
rem del browser, una dopo l'altra: fai login in ognuna, poi torna QUI in questa
rem finestra nera e premi Invio quando richiesto.
cd /d "%~dp0"
python -m engine.session_manager
echo.
echo ============================================
echo FATTO. Puoi chiudere questa finestra.
echo ============================================
pause
