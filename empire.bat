@echo off
REM EMPIRE — launcher senza installazione.
REM Owner: Max · Controllore: Claude · Origine: FORGE (seed CP-20260722-003)
REM Uso da qualunque cartella:  "C:\...\Digital Empire\empire.bat" status
REM Alternativa permanente:     pip install -e "C:\...\Digital Empire"
setlocal
set "PYTHONPATH=%~dp0;%PYTHONPATH%"
python -m empire %*
endlocal
